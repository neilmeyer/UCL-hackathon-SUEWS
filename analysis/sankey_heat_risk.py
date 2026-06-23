"""
SUEWS Hackathon — Sankey/Alluvial Flow Diagram
================================================
Visualises the flow from Neighbourhood Archetype → Heat Risk Band →
Vulnerability Driver → RAGG Risk Category.

Pre-built with placeholder data. On the day, replace the data section
with real archetype names and SUEWS output values.

Outputs: docs/sankey_heat_risk.html (interactive, embeddable on GitHub Pages)

Usage:
    python analysis/sankey_heat_risk.py

Requires: plotly (pip install plotly)
"""

import plotly.graph_objects as go
from pathlib import Path

# =============================================================================
# DATA — Replace with real values on hackathon day
# =============================================================================

# Node labels (each unique item across all columns)
labels = [
    # Column 0: Neighbourhood Archetypes (indices 0-5)
    "Compact High-Rise (LCZ 1)",      # 0
    "Compact Mid-Rise (LCZ 2)",       # 1
    "Open Low-Rise (LCZ 6)",          # 2
    "Informal Settlement (LCZ 7)",    # 3
    "Dense Trees (LCZ A)",            # 4
    "Sparse / Bare (LCZ F)",          # 5

    # Column 1: Dangerous-Heat Hours Band (indices 6-9)
    ">300 hours",                     # 6
    "200–300 hours",                  # 7
    "100–200 hours",                  # 8
    "<100 hours",                     # 9

    # Column 2: Primary Vulnerability Driver (indices 10-14)
    "High Impervious Fraction",       # 10
    "Low Tree Canopy",                # 11
    "Informal Housing Materials",     # 12
    "High Population Density",        # 13
    "Anthropogenic Heat (QF)",        # 14

    # Column 3: RAGG Risk Category (indices 15-18)
    "🔴 Red — Critical",             # 15
    "🟠 Amber — Elevated",           # 16
    "🟢 Green — Manageable",         # 17
    "⬜ Grey — Immaterial",           # 18
]

# Colour palette (BCL-inspired: dark navy background, distinct node colours)
node_colours = [
    # Archetypes — steel blue family
    "#5B9BD5", "#5B9BD5", "#7EC8E3", "#E87040", "#4CAF50", "#B0BEC5",
    # Heat hours — severity gradient
    "#D32F2F", "#FF8F00", "#FDD835", "#66BB6A",
    # Vulnerability drivers — muted tones
    "#78909C", "#78909C", "#78909C", "#78909C", "#78909C",
    # RAGG — canonical
    "#D32F2F", "#FF8F00", "#4CAF50", "#9E9E9E",
]

# Links: source → target with a value (population or flow weight)
# Format: (source_index, target_index, value)
links_data = [
    # Archetype → Heat Hours Band
    (0, 6, 180),   # Compact High-Rise → >300h
    (1, 7, 150),   # Compact Mid-Rise → 200-300h
    (2, 8, 120),   # Open Low-Rise → 100-200h
    (3, 6, 200),   # Informal Settlement → >300h
    (4, 9, 90),    # Dense Trees → <100h
    (5, 7, 60),    # Sparse/Bare → 200-300h

    # Heat Hours Band → Vulnerability Driver
    (6, 10, 180),  # >300h → High Impervious
    (6, 12, 140),  # >300h → Informal Housing
    (6, 13, 60),   # >300h → High Population Density
    (7, 10, 90),   # 200-300h → High Impervious
    (7, 11, 70),   # 200-300h → Low Tree Canopy
    (7, 14, 50),   # 200-300h → Anthropogenic Heat
    (8, 11, 80),   # 100-200h → Low Tree Canopy
    (8, 14, 40),   # 100-200h → Anthropogenic Heat
    (9, 11, 50),   # <100h → Low Tree Canopy (mild)
    (9, 10, 40),   # <100h → High Impervious (mild)

    # Vulnerability Driver → RAGG Category
    (10, 15, 180), # High Impervious → Red
    (10, 16, 130), # High Impervious → Amber
    (11, 16, 100), # Low Tree Canopy → Amber
    (11, 17, 100), # Low Tree Canopy → Green
    (12, 15, 140), # Informal Housing → Red
    (13, 15, 60),  # High Population Density → Red
    (14, 16, 90),  # Anthropogenic Heat → Amber
    (14, 18, 0),   # (placeholder)
]

# Filter out zero-value links
links_data = [(s, t, v) for s, t, v in links_data if v > 0]

sources = [l[0] for l in links_data]
targets = [l[1] for l in links_data]
values = [l[2] for l in links_data]

# Link colours — semi-transparent, tinted by source node
link_colours = [
    node_colours[s].replace(")", ", 0.35)").replace("rgb", "rgba")
    if "rgb" in node_colours[s]
    else f"rgba({int(node_colours[s][1:3], 16)}, {int(node_colours[s][3:5], 16)}, {int(node_colours[s][5:7], 16)}, 0.35)"
    for s in sources
]

# =============================================================================
# BUILD THE FIGURE
# =============================================================================

fig = go.Figure(data=[go.Sankey(
    arrangement="snap",
    node=dict(
        pad=20,
        thickness=25,
        line=dict(color="#1a1a2e", width=1),
        label=labels,
        color=node_colours,
        hovertemplate="%{label}<br>Total flow: %{value}<extra></extra>",
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        color=link_colours,
        hovertemplate=(
            "%{source.label} → %{target.label}<br>"
            "Population affected: %{value}<extra></extra>"
        ),
    ),
)])

fig.update_layout(
    title=dict(
        text="Urban Heat Risk Flow: Archetype → Hazard → Vulnerability → Risk Rating",
        font=dict(size=16, color="#E0E0E0"),
        x=0.5,
    ),
    font=dict(size=11, color="#B0BEC5"),
    paper_bgcolor="#0d1b2a",
    plot_bgcolor="#0d1b2a",
    height=550,
    margin=dict(l=20, r=20, t=60, b=20),
)

# =============================================================================
# SAVE
# =============================================================================

output_path = Path(__file__).resolve().parent.parent / "docs" / "sankey_heat_risk.html"
fig.write_html(
    str(output_path),
    include_plotlyjs="cdn",
    full_html=True,
    config={"displayModeBar": False},
)

print(f"✓ Sankey diagram saved to: {output_path}")
print(f"  Embed in docs/index.md with:")
print(f'  <iframe src="sankey_heat_risk.html" width="100%" height="580" frameborder="0"></iframe>')
