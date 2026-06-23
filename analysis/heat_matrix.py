"""
SUEWS Hackathon — Heat Risk Matrix (RoL-style)
===============================================
A heatmap grid showing Hazard Level × Vulnerability Level for each
neighbourhood archetype. Mirrors BCL's Realisation of Legacy matrix.

Outputs: docs/heat_matrix.html (interactive, embeddable on GitHub Pages)

Usage:
    python analysis/heat_matrix.py

Requires: plotly (pip install plotly)
"""

import plotly.graph_objects as go
import numpy as np
from pathlib import Path

# =============================================================================
# DATA — Replace with real values on hackathon day
# =============================================================================

# Archetypes (rows)
archetypes = [
    "Compact High-Rise (LCZ 1)",
    "Compact Mid-Rise (LCZ 2)",
    "Open High-Rise (LCZ 4)",
    "Open Low-Rise (LCZ 6)",
    "Informal Settlement (LCZ 7)",
    "Dense Trees (LCZ A)",
    "Sparse / Bare (LCZ F)",
    "Water (LCZ G)",
]

# Dimensions (columns) — scored 1-5 (5 = worst)
dimensions = [
    "Peak\nTemperature",
    "Dangerous\nHeat Hours",
    "Night-time\nMinimum",
    "Population\nDensity",
    "Adaptive\nCapacity",
    "Overall\nRisk",
]

# Score matrix (archetypes × dimensions) — 1=low risk, 5=critical
# Replace with real data on the day
scores = np.array([
    [5, 5, 4, 4, 3, 5],  # Compact High-Rise
    [4, 4, 4, 4, 3, 4],  # Compact Mid-Rise
    [4, 3, 3, 3, 3, 3],  # Open High-Rise
    [3, 2, 2, 2, 4, 2],  # Open Low-Rise
    [5, 5, 5, 5, 1, 5],  # Informal Settlement
    [1, 1, 1, 2, 5, 1],  # Dense Trees
    [4, 4, 3, 1, 3, 3],  # Sparse/Bare
    [1, 1, 1, 1, 5, 1],  # Water
])

# RAGG colour scale: 1=Green, 2=Green-amber, 3=Amber, 4=Amber-red, 5=Red
colorscale = [
    [0.0, "#2E7D32"],   # 1 — Green
    [0.25, "#66BB6A"],  # 2 — Light green
    [0.5, "#FF8F00"],   # 3 — Amber
    [0.75, "#E65100"],  # 4 — Dark amber
    [1.0, "#C62828"],   # 5 — Red
]

# Text overlay showing the score
text_labels = scores.astype(str)

# =============================================================================
# BUILD THE FIGURE
# =============================================================================

fig = go.Figure(data=go.Heatmap(
    z=scores,
    x=dimensions,
    y=archetypes,
    colorscale=colorscale,
    zmin=1,
    zmax=5,
    text=text_labels,
    texttemplate="%{text}",
    textfont=dict(size=14, color="white"),
    hovertemplate=(
        "<b>%{y}</b><br>"
        "%{x}: %{z}/5<extra></extra>"
    ),
    colorbar=dict(
        title=dict(text="Risk", side="right"),
        tickvals=[1, 2, 3, 4, 5],
        ticktext=["Low", "", "Moderate", "", "Critical"],
        len=0.6,
    ),
))

fig.update_layout(
    title=dict(
        text="Neighbourhood Heat Risk Matrix",
        font=dict(size=16, color="#E0E0E0"),
        x=0.5,
    ),
    font=dict(size=11, color="#B0BEC5"),
    paper_bgcolor="#0d1b2a",
    plot_bgcolor="#0d1b2a",
    xaxis=dict(
        side="top",
        tickfont=dict(size=10, color="#B0BEC5"),
    ),
    yaxis=dict(
        tickfont=dict(size=10, color="#B0BEC5"),
        autorange="reversed",
    ),
    height=450,
    margin=dict(l=200, r=80, t=80, b=20),
)

# =============================================================================
# SAVE
# =============================================================================

output_path = Path(__file__).resolve().parent.parent / "docs" / "heat_matrix.html"
fig.write_html(
    str(output_path),
    include_plotlyjs="cdn",
    full_html=True,
    config={"displayModeBar": False},
)

print(f"✓ Heat matrix saved to: {output_path}")
print(f"  Embed in docs/index.md with:")
print(f'  <iframe src="heat_matrix.html" width="100%" height="480" frameborder="0"></iframe>')
