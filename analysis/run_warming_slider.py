"""
Run SUEWS at intermediate warming increments (0, +0.5, +1.0, +1.5, +2.0, +2.5°C)
to produce data for an interactive warming slider visualisation.

Approach: Linearly interpolate forcing between present (0°C) and future (+2.5°C)
files to create intermediate warming levels. This captures the non-linear
threshold response as more timesteps cross the 35°C dangerous heat threshold.

Output: warming_slider_data.csv + warming_slider.html (Plotly interactive)
"""
import supy
import yaml
import numpy as np
import pandas as pd
from pathlib import Path
import plotly.graph_objects as go

base = Path(r'c:\Code\SUEWS\UCL-hackathon-SUEWS\data\uda-city-hackathon')
analysis = Path(r'c:\Code\SUEWS\UCL-hackathon-SUEWS\analysis')
docs = Path(r'c:\Code\SUEWS\UCL-hackathon-SUEWS\docs')

THRESHOLD = 35.0
SPINUP_FRAC = 30 / 91  # skip first 30 days
WARMING_LEVELS = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5]

NAMES = ['Jade Gardens', 'Serendib Rise', 'Taman Melati', 'Kampong Lama',
         'Dhobi Lines', 'Lusitano Square', 'Mlima Moto', 'Victoria Exchange',
         'Fuzhou Lanes', 'Zheng He Towers']
TYPES = ['Refuge', 'Refuge', 'Refuge', 'Hotspot', 'Hotspot', 'Core', 'Hotspot', 'Core', 'Hotspot', 'Core']

# Population density (people/ha daytime) from uda-city.yml
POP_DENSITY = [80, 80, 80, 300, 300, 250, 300, 250, 300, 250]
# Outdoor worker fraction from socioeconomic.csv
OUTDOOR_WORKER_FRAC = [0.30, 0.28, 0.32, 0.62, 0.60, 0.22, 0.65, 0.20, 0.63, 0.18]

def create_intermediate_forcing(fraction):
    """
    Create forcing at a given warming fraction (0=present, 1=+2.5°C).
    Interpolates Tair and ldown between present and future forcing files.
    """
    present_path = base / 'forcing' / 'present_hot_humid' / 'UDA_2024_data_60.txt'
    future_path = base / 'forcing' / 'future_hot_humid' / 'UDA_2024_data_60.txt'

    # Read both files
    with open(present_path) as f:
        present_lines = f.readlines()
    with open(future_path) as f:
        future_lines = f.readlines()

    header = present_lines[0]
    output_lines = [header]

    for i in range(1, len(present_lines)):
        if not present_lines[i].strip():
            continue
        p_cols = present_lines[i].split()
        f_cols = future_lines[i].split()

        # Interpolate Tair (col 11, 0-indexed) and ldown (col 17, 0-indexed)
        p_tair = float(p_cols[11])
        f_tair = float(f_cols[11])
        new_tair = p_tair + fraction * (f_tair - p_tair)

        p_ldown = float(p_cols[17])
        f_ldown = float(f_cols[17])
        new_ldown = p_ldown + fraction * (f_ldown - p_ldown)

        # Build new line
        new_cols = list(p_cols)
        new_cols[11] = f"{new_tair:.4f}"
        new_cols[17] = f"{new_ldown:.4f}"
        output_lines.append(' '.join(new_cols) + '\n')

    # Write to intermediate forcing directory
    warming_deg = fraction * 2.5
    out_dir = base / 'forcing' / f'warming_{warming_deg:.1f}'
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / 'UDA_2024_data_60.txt'
    with open(out_path, 'w') as f:
        f.writelines(output_lines)

    return out_dir


def create_config_for_forcing(forcing_dir):
    """Create a SUEWS config pointing to the given forcing directory."""
    with open(base / 'uda-city.yml') as f:
        cfg = yaml.safe_load(f)

    # Update forcing path (relative to base)
    rel_path = forcing_dir.relative_to(base)
    cfg['model']['control']['forcing']['file'] = str(rel_path / 'UDA_2024_data_60.txt').replace('\\', '/')

    out_path = base / f'uda-city-warming-{forcing_dir.name}.yml'
    with open(out_path, 'w') as f:
        yaml.dump(cfg, f, default_flow_style=False, allow_unicode=True)
    return out_path


def run_and_extract(config_path):
    """Run simulation and return dangerous-heat hours per grid."""
    sim = supy.SUEWSSimulation(str(config_path))
    sim.run()
    df = sim.output['SUEWS']
    results = {}
    for gridiv in range(1, 11):
        t2 = df.loc[gridiv]['T2']
        spinup = int(len(t2) * SPINUP_FRAC)
        t2_a = t2.iloc[spinup:]
        results[gridiv] = (t2_a > THRESHOLD).sum() / 4.0
    return results


# --- RUN ALL WARMING LEVELS ---
all_results = {}

for warming in WARMING_LEVELS:
    fraction = warming / 2.5
    print(f"\n{'='*50}")
    print(f"Running warming level: +{warming:.1f}°C (fraction={fraction:.2f})")
    print(f"{'='*50}")

    if warming == 0.0:
        # Use present forcing directly
        results = run_and_extract(base / 'uda-city.yml')
    elif warming == 2.5:
        # Use future forcing directly - need config pointing to future
        forcing_dir = base / 'forcing' / 'future_hot_humid'
        cfg_path = create_config_for_forcing(forcing_dir)
        results = run_and_extract(cfg_path)
        cfg_path.unlink()
    else:
        # Create intermediate forcing and run
        forcing_dir = create_intermediate_forcing(fraction)
        cfg_path = create_config_for_forcing(forcing_dir)
        results = run_and_extract(cfg_path)
        cfg_path.unlink()
        # Clean up intermediate forcing
        import shutil
        shutil.rmtree(forcing_dir)

    all_results[warming] = results
    print(f"  Dhobi Lines: {results[5]:.1f}h | Kampong Lama: {results[4]:.1f}h | Zheng He: {results[10]:.1f}h")


# --- BUILD DATAFRAME ---
rows = []
for warming in WARMING_LEVELS:
    for g in range(1, 11):
        hours = all_results[warming][g]
        # Calculate unsafe outdoor work hours (ILO-based):
        # If T2 > 35°C, outdoor work should cease. Hours above threshold × outdoor worker fraction
        unsafe_work_hours = hours * OUTDOOR_WORKER_FRAC[g-1]
        # Working hours in analysis period: 61 days × 10h workday = 610h total
        total_work_hours = 61 * 10
        work_hours_lost_pct = (unsafe_work_hours / total_work_hours) * 100

        rows.append({
            'warming': warming,
            'gridiv': g,
            'name': NAMES[g-1],
            'type': TYPES[g-1],
            'dangerous_hours': round(hours, 1),
            'pop_density': POP_DENSITY[g-1],
            'outdoor_worker_frac': OUTDOOR_WORKER_FRAC[g-1],
            'unsafe_work_hours': round(unsafe_work_hours, 1),
            'work_hours_lost_pct': round(work_hours_lost_pct, 1),
        })

df = pd.DataFrame(rows)
df.to_csv(analysis / 'warming_slider_data.csv', index=False)
print(f"\nSaved data: {analysis / 'warming_slider_data.csv'}")


# --- BUILD PLOTLY SLIDER HTML ---
print("\nBuilding interactive slider visualisation...")

# Color scheme by type
type_colors = {'Refuge': '#66BB6A', 'Hotspot': '#EF5350', 'Core': '#5B9BD5'}

# Create figure with slider
fig = go.Figure()

# Add traces for each warming level (only first visible)
for i, warming in enumerate(WARMING_LEVELS):
    subset = df[df['warming'] == warming].sort_values('dangerous_hours', ascending=True)

    fig.add_trace(go.Bar(
        x=subset['dangerous_hours'],
        y=subset['name'],
        orientation='h',
        marker_color=[type_colors[t] for t in subset['type']],
        text=[f"{h:.0f}h ({wl:.0f}% work lost)" for h, wl in zip(subset['dangerous_hours'], subset['work_hours_lost_pct'])],
        textposition='outside',
        textfont=dict(size=11, color='#e0e0e0'),
        hovertemplate='<b>%{y}</b><br>' +
                      f'Warming: +{warming:.1f}°C<br>' +
                      'Dangerous hours: %{x:.0f}h<br>' +
                      '<extra></extra>',
        visible=(i == 0),
        name=f'+{warming:.1f}°C'
    ))

# Add threshold annotation line at various key points
fig.add_vline(x=100, line_dash="dot", line_color="rgba(255,143,0,0.5)",
              annotation_text="ILO: work restrictions needed", annotation_position="top")

# Create slider steps
steps = []
for i, warming in enumerate(WARMING_LEVELS):
    step = dict(
        method="update",
        args=[{"visible": [j == i for j in range(len(WARMING_LEVELS))]},
              {"title": f"Dangerous Heat Hours by Neighbourhood — +{warming:.1f}°C Warming"}],
        label=f"+{warming:.1f}°C"
    )
    steps.append(step)

sliders = [dict(
    active=0,
    currentvalue={"prefix": "Warming: ", "font": {"size": 16, "color": "#e0e0e0"}},
    pad={"t": 60},
    steps=steps,
    bgcolor="#1b2838",
    activebgcolor="#5B9BD5",
    bordercolor="#5B9BD5",
    font={"color": "#e0e0e0"}
)]

fig.update_layout(
    sliders=sliders,
    title=dict(
        text="Dangerous Heat Hours by Neighbourhood — +0.0°C Warming",
        font=dict(size=18, color='#fff')
    ),
    xaxis=dict(
        title="Hours above 35°C (April–May, post-spinup)",
        range=[0, max(df['dangerous_hours']) * 1.15],
        gridcolor='rgba(255,255,255,0.05)',
        color='#B0BEC5'
    ),
    yaxis=dict(
        color='#B0BEC5',
        tickfont=dict(size=12)
    ),
    plot_bgcolor='#0d1b2a',
    paper_bgcolor='#0d1b2a',
    font=dict(color='#e0e0e0'),
    height=550,
    margin=dict(l=140, r=120, t=100, b=60),
    showlegend=False,
)

# Save HTML
slider_path = docs / 'warming_slider.html'
fig.write_html(str(slider_path), include_plotlyjs='cdn')
print(f"Saved visualisation: {slider_path}")

# --- ALSO BUILD THE WORK-HOURS-LOST VIEW ---
fig2 = go.Figure()

for i, warming in enumerate(WARMING_LEVELS):
    subset = df[df['warming'] == warming].sort_values('unsafe_work_hours', ascending=True)

    fig2.add_trace(go.Bar(
        x=subset['unsafe_work_hours'],
        y=subset['name'],
        orientation='h',
        marker_color=[type_colors[t] for t in subset['type']],
        text=[f"{h:.0f}h lost" for h in subset['unsafe_work_hours']],
        textposition='outside',
        textfont=dict(size=11, color='#e0e0e0'),
        hovertemplate='<b>%{y}</b><br>' +
                      f'Warming: +{warming:.1f}°C<br>' +
                      'Unsafe outdoor work hours: %{x:.0f}h<br>' +
                      f'Outdoor workers: ' + '%{{customdata[0]:.0%}}<br>' +
                      '<extra></extra>',
        customdata=subset[['outdoor_worker_frac']].values,
        visible=(i == 0),
        name=f'+{warming:.1f}°C'
    ))

steps2 = []
for i, warming in enumerate(WARMING_LEVELS):
    step = dict(
        method="update",
        args=[{"visible": [j == i for j in range(len(WARMING_LEVELS))]},
              {"title": f"Unsafe Outdoor Work Hours — +{warming:.1f}°C Warming<br><sup>Hours where outdoor labour should cease (ILO guideline: T2 > 35°C)</sup>"}],
        label=f"+{warming:.1f}°C"
    )
    steps2.append(step)

sliders2 = [dict(
    active=0,
    currentvalue={"prefix": "Warming: ", "font": {"size": 16, "color": "#e0e0e0"}},
    pad={"t": 60},
    steps=steps2,
    bgcolor="#1b2838",
    activebgcolor="#EF5350",
    bordercolor="#EF5350",
    font={"color": "#e0e0e0"}
)]

fig2.update_layout(
    sliders=sliders2,
    title=dict(
        text="Unsafe Outdoor Work Hours — +0.0°C Warming<br><sup>Hours where outdoor labour should cease (ILO guideline: T2 > 35°C)</sup>",
        font=dict(size=16, color='#fff')
    ),
    xaxis=dict(
        title="Hours of unsafe outdoor work (April–May)",
        range=[0, max(df['unsafe_work_hours']) * 1.15],
        gridcolor='rgba(255,255,255,0.05)',
        color='#B0BEC5'
    ),
    yaxis=dict(
        color='#B0BEC5',
        tickfont=dict(size=12)
    ),
    plot_bgcolor='#0d1b2a',
    paper_bgcolor='#0d1b2a',
    font=dict(color='#e0e0e0'),
    height=550,
    margin=dict(l=140, r=120, t=120, b=60),
    showlegend=False,
)

work_path = docs / 'work_hours_slider.html'
fig2.write_html(str(work_path), include_plotlyjs='cdn')
print(f"Saved work hours visualisation: {work_path}")

print("\n✅ Done! Slider visualisations ready.")
print(f"   {slider_path}")
print(f"   {work_path}")
