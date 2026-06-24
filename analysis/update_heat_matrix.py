"""Update heat matrix with hover tooltips for each cell."""
import plotly.graph_objects as go
import numpy as np
from pathlib import Path

names = ['Jade Gardens (Refuge)','Serendib Rise (Refuge)','Taman Melati (Refuge)',
         'Kampong Lama (Hotspot)','Dhobi Lines (Hotspot)','Lusitano Square (Core)',
         'Mlima Moto (Hotspot)','Victoria Exchange (Core)','Fuzhou Lanes (Hotspot)','Zheng He Towers (Core)']

dimensions = ['Peak Temp', 'Danger Hours', 'Pop Density',
              'Vulnerability', 'Adapt Capacity', 'Overall Risk']

scores = np.array([
    [5, 5, 1, 2, 3, 2],
    [4, 3, 1, 2, 3, 3],
    [4, 4, 1, 2, 3, 2],
    [4, 4, 5, 5, 1, 4],
    [4, 3, 5, 5, 1, 5],
    [3, 1, 4, 1, 4, 2],
    [3, 1, 5, 5, 1, 4],
    [3, 1, 4, 1, 4, 2],
    [3, 3, 5, 5, 1, 5],
    [2, 1, 4, 1, 5, 1],
])

# Hover descriptions for each cell
descs = [
    # Peak Temp
    ['38.1°C peak — hottest in city','36.8°C — moderate','37.7°C — second hottest',
     '37.4°C — very hot','36.9°C — hot','35.3°C — mild',
     '35.6°C — mild','35.1°C — mild','36.7°C — hot','34.4°C — coolest in city'],
    # Dangerous Heat Hours
    ['75 hours above 35°C','31 hours above 35°C','63 hours above 35°C',
     '68 hours above 35°C','44 hours above 35°C','4 hours above 35°C',
     '5 hours above 35°C','3 hours above 35°C','36 hours above 35°C','0 hours above 35°C'],
    # Population Density
    ['80 people/ha — sparse','80 people/ha — sparse','80 people/ha — sparse',
     '300 day / 400 night — very dense','300 day / 400 night — very dense',
     '250 day / 130 night — daytime influx','300 day / 400 night — very dense',
     '250 day / 130 night — daytime influx','300 day / 400 night — very dense',
     '250 day / 130 night — daytime influx'],
    # Vulnerability
    ['40% deprivation, 45% AC','38% deprivation, 50% AC','42% deprivation, 42% AC',
     '82% deprivation, 8% AC, 62% outdoor workers','80% deprivation, 10% AC, 60% outdoor workers',
     '30% deprivation, 70% AC','85% deprivation, 6% AC, 65% outdoor workers',
     '28% deprivation, 72% AC','83% deprivation, 7% AC, 63% outdoor workers',
     '25% deprivation, 78% AC'],
    # Adaptive Capacity
    ['Moderate: 11% trees, 45% AC','Moderate: 11% trees, 50% AC','Moderate: 11% trees, 42% AC',
     'Very low: 3% trees, 8% AC, metal roofs','Very low: 3% trees, 10% AC',
     'High: 6% trees, 70% AC, formal buildings','Very low: 3% trees, 6% AC',
     'High: 6% trees, 72% AC, formal buildings','Very low: 3% trees, 7% AC',
     'Highest: 6% trees, 78% AC, tall concrete/glass'],
    # Overall Risk
    ['Green — hot but few people exposed','Amber — moderate across all pillars',
     'Green — hot but few people exposed','Red — high hazard + exposure + vulnerability',
     'Red — HIGHEST RISK: dense, vulnerable, hot','Green — cool, wealthy, good AC',
     'Red — extreme vulnerability, rising hazard','Green — cool, wealthy, good AC',
     'Red — all three pillars high','Grey — coolest, wealthiest, best-adapted']
]

# Build hover text matrix (rows = neighbourhoods, cols = dimensions)
hover_text = []
for i, name in enumerate(names):
    row = []
    for j, dim in enumerate(dimensions):
        dim_clean = dim.replace('<br>', ' ')
        row.append(f"<b>{name}</b><br>{dim_clean}: {scores[i,j]}/5<br><br>{descs[j][i]}")
    hover_text.append(row)

colorscale = [[0.0,'#2E7D32'],[0.25,'#66BB6A'],[0.5,'#FF8F00'],[0.75,'#E65100'],[1.0,'#C62828']]

fig = go.Figure(data=go.Heatmap(
    z=scores, x=dimensions, y=names,
    colorscale=colorscale, zmin=1, zmax=5,
    text=scores.astype(str), texttemplate="%{text}", textfont=dict(size=13, color="white"),
    hovertext=hover_text, hovertemplate="%{hovertext}<extra></extra>",
    colorbar=dict(title=dict(text="Risk", side="right"), tickvals=[1,2,3,4,5],
                  ticktext=["Low","","Moderate","","Critical"], len=0.6)))

fig.update_layout(
    title=dict(text="UDA-City Neighbourhood Heat Risk Matrix", font=dict(size=15, color="#E0E0E0"), x=0.5),
    font=dict(size=11, color="#B0BEC5"), paper_bgcolor="#0d1b2a", plot_bgcolor="#0d1b2a",
    xaxis=dict(side="top", tickfont=dict(size=11, color="#B0BEC5"), tickangle=0),
    yaxis=dict(tickfont=dict(size=10, color="#B0BEC5"), autorange="reversed"),
    height=520, margin=dict(l=210, r=80, t=80, b=20))

out = Path(__file__).resolve().parent.parent / "docs" / "heat_matrix.html"
fig.write_html(str(out), include_plotlyjs="cdn", full_html=True, config={"displayModeBar": False})
print(f"Updated: {out}")
