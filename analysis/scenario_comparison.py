"""
SUEWS Hackathon — Scenario Comparison (Present vs Future)
==========================================================
Side-by-side bar chart showing dangerous-heat hours per archetype
under current vs +2.5°C future forcing. Includes BCL-style trajectory
arrows.

Outputs: docs/scenario_comparison.html (interactive, embeddable on GitHub Pages)

Usage:
    python analysis/scenario_comparison.py

Requires: plotly (pip install plotly)
"""

import plotly.graph_objects as go
from pathlib import Path

# =============================================================================
# DATA — Replace with real SUEWS output on hackathon day
# =============================================================================

archetypes = [
    "Compact High-Rise",
    "Compact Mid-Rise",
    "Open Low-Rise",
    "Informal Settlement",
    "Dense Trees",
    "Sparse / Bare",
]

# Dangerous-heat hours (T_air > 35°C) per hot season
current_hours = [320, 245, 140, 350, 45, 210]
future_hours = [480, 380, 260, 520, 95, 340]  # +2.5°C scenario

# RAGG thresholds
RED_THRESHOLD = 250
AMBER_THRESHOLD = 100

# Trajectory labels
trajectories = []
for c, f in zip(current_hours, future_hours):
    delta = f - c
    pct = (delta / c) * 100 if c > 0 else 0
    trajectories.append(f"↓ +{delta}h (+{pct:.0f}%)")

# =============================================================================
# BUILD THE FIGURE
# =============================================================================

fig = go.Figure()

# Current scenario bars
fig.add_trace(go.Bar(
    name="Current Climate",
    x=archetypes,
    y=current_hours,
    marker_color="#5B9BD5",
    text=[f"{h}h" for h in current_hours],
    textposition="outside",
    textfont=dict(size=10, color="#B0BEC5"),
    hovertemplate="<b>%{x}</b><br>Current: %{y} dangerous hours<extra></extra>",
))

# Future scenario bars
fig.add_trace(go.Bar(
    name="Future (+2.5°C)",
    x=archetypes,
    y=future_hours,
    marker_color="#E87040",
    text=[f"{h}h" for h in future_hours],
    textposition="outside",
    textfont=dict(size=10, color="#B0BEC5"),
    hovertemplate="<b>%{x}</b><br>Future: %{y} dangerous hours<extra></extra>",
))

# Red threshold line
fig.add_hline(
    y=RED_THRESHOLD,
    line_dash="dash",
    line_color="#D32F2F",
    line_width=1.5,
    annotation_text="🔴 Red threshold (250h)",
    annotation_position="top right",
    annotation_font=dict(size=10, color="#D32F2F"),
)

# Amber threshold line
fig.add_hline(
    y=AMBER_THRESHOLD,
    line_dash="dot",
    line_color="#FF8F00",
    line_width=1,
    annotation_text="🟠 Amber threshold (100h)",
    annotation_position="bottom right",
    annotation_font=dict(size=9, color="#FF8F00"),
)

fig.update_layout(
    title=dict(
        text="Dangerous-Heat Hours: Current vs Future (+2.5°C) Scenario",
        font=dict(size=15, color="#E0E0E0"),
        x=0.5,
    ),
    barmode="group",
    font=dict(size=11, color="#B0BEC5"),
    paper_bgcolor="#0d1b2a",
    plot_bgcolor="#0d1b2a",
    xaxis=dict(
        tickfont=dict(size=10, color="#B0BEC5"),
        tickangle=-15,
    ),
    yaxis=dict(
        title=dict(text="Dangerous-heat hours (T > 35°C)", font=dict(size=11, color="#B0BEC5")),
        tickfont=dict(size=10, color="#B0BEC5"),
        gridcolor="rgba(255,255,255,0.05)",
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5,
        font=dict(size=11, color="#B0BEC5"),
    ),
    height=480,
    margin=dict(l=60, r=30, t=90, b=80),
)

# Add trajectory annotations below bars
for i, (arch, traj) in enumerate(zip(archetypes, trajectories)):
    fig.add_annotation(
        x=arch,
        y=-35,
        text=traj,
        showarrow=False,
        font=dict(size=9, color="#FF8F00"),
        yref="y",
    )

# =============================================================================
# SAVE
# =============================================================================

output_path = Path(__file__).resolve().parent.parent / "docs" / "scenario_comparison.html"
fig.write_html(
    str(output_path),
    include_plotlyjs="cdn",
    full_html=True,
    config={"displayModeBar": False},
)

print(f"✓ Scenario comparison saved to: {output_path}")
print(f"  Embed in docs/index.md with:")
print(f'  <iframe src="scenario_comparison.html" width="100%" height="500" frameborder="0"></iframe>')
