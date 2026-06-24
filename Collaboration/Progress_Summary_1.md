# Progress Summary 1 — Hackathon Day (24 June 2026, ~14:30)

> Checkpoint so we can reseed/resume from another session if needed.

---

## What We've Done

### Pre-day (23 June)
1. Created practice repo `neilmeyer/UCL-hackathon-SUEWS` from template ✅
2. Confirmed SuPy 2026.6.5 works (test simulation) ✅
3. GitHub Pages enabled (main branch, /docs) ✅
4. Built 3 interactive visualisation templates (Sankey, heat matrix, scenario comparison) ✅
5. Researched 12 ideas + BCL-aligned strategy ✅
6. suews-agent MCP server configured (needs reload) ✅
7. Plotly installed and working ✅

### Day-of (24 June, 14:00 onwards)
8. Discovered challenge dataset already published at `UMEP-dev/uda-city-hackathon` ✅
9. Cloned dataset into `data/uda-city-hackathon/` ✅
10. **Ran SUEWS on all 10 neighbourhoods — PRESENT scenario** ✅
11. Calculated dangerous-heat hours per neighbourhood ✅
12. Saved results to `analysis/heat_hazard_results.csv` ✅

---

## Key Findings So Far

### Present Scenario — Dangerous-Heat Hours (T2 > 35°C, April–May analysis window)

| Rank | Neighbourhood | Peak T2 (°C) | Mean T2 (°C) | Dangerous Hours |
|------|---------------|--------------|--------------|-----------------|
| 1 | Jade Gardens (refuge) | 38.15 | 29.43 | 75.0 |
| 2 | Kampong Lama (hotspot) | 37.38 | 29.43 | 68.0 |
| 3 | Taman Melati (refuge) | 37.68 | 29.38 | 62.75 |
| 4 | Dhobi Lines (hotspot) | 36.91 | 29.35 | 44.0 |
| 5 | Fuzhou Lanes (hotspot) | 36.71 | 29.30 | 36.25 |
| 6 | Serendib Rise (refuge) | 36.76 | 29.28 | 31.0 |
| 7 | Mlima Moto (hotspot) | 35.59 | 29.18 | 5.0 |
| 8 | Lusitano Square (core) | 35.34 | 29.14 | 4.25 |
| 9 | Victoria Exchange (core) | 35.11 | 29.11 | 2.75 |
| 10 | Zheng He Towers (core) | 34.37 | 29.03 | 0.0 |

### Critical Insight (confirms risk_bridge.md prediction)
**The hottest neighbourhoods are NOT the highest-risk ones.**

- Jade Gardens is hottest (38.15°C peak, 75 dangerous hours) — but it's a *refuge* with only 80 people/ha and 45% AC access.
- Kampong Lama is second-hottest (68 hours) — AND has 400 people/ha at night, only 8% AC access, 62% outdoor workers, and 0.82 deprivation index.
- The dense high-rise cores (Zheng He Towers, Victoria Exchange) are *coolest* — tall buildings create roughness that enhances turbulent mixing.

**This is the tension the judges want us to surface.**

---

## What's In the Repo Right Now

```
UCL-hackathon-SUEWS/
├── analysis/
│   ├── heat_hazard_results.csv    ← REAL DATA from simulation
│   ├── sankey_heat_risk.py        ← viz template (needs real data update)
│   ├── heat_matrix.py             ← viz template
│   └── scenario_comparison.py     ← viz template
├── bridge/
│   └── heat-to-risk.md            ← points to uda-city-hackathon bridge
├── Collaboration/
│   ├── Ideas_v1.md
│   ├── BCL-aligned-Ideas_v1.md
│   ├── UCL-SUEWS-Hackathon-overview.md
│   └── Progress_Summary_1.md      ← THIS FILE
├── data/
│   ├── README.md
│   └── uda-city-hackathon/        ← FULL CHALLENGE DATASET
│       ├── uda-city.yml           (10-neighbourhood SUEWS config)
│       ├── risk_bridge.py         (runnable bridge function)
│       ├── risk_bridge.md         (bridge documentation)
│       ├── socioeconomic.csv      (vulnerability proxies)
│       ├── scenarios.yml          (present + future +2.5°C)
│       ├── neighbourhoods.yml     (metadata)
│       ├── agent_manifest.yml     (agent entry point)
│       └── forcing/               (present + future met files)
├── docs/
│   ├── index.md                   ← Pages skeleton (needs writing)
│   ├── sankey_heat_risk.html      ← interactive (placeholder data)
│   ├── heat_matrix.html           ← interactive (placeholder data)
│   └── scenario_comparison.html   ← interactive (placeholder data)
└── transcripts/
    └── session-2026-06-23-setup.md
```

---

## Next Steps (in order)

1. **Run the FUTURE scenario** (+2.5°C forcing) and compare
2. **Run risk_bridge.py** to get the full risk index with socioeconomic data
3. **Update visualisation scripts** with real neighbourhood names and data
4. **Write docs/index.md** (the judged Pages site) using BCL Bearing Report structure
5. **Commit and push** regularly
6. **Save this session transcript** to `transcripts/`

---

## Technical Notes for Resume

- **Python**: 3.12, SuPy 2026.6.5, Plotly installed
- **GitHub CLI**: authenticated as `neilmeyer` with write access to `UCL-hackathon-SUEWS`
- **Pages URL**: https://neilmeyer.github.io/UCL-hackathon-SUEWS/
- **Repo URL**: https://github.com/neilmeyer/UCL-hackathon-SUEWS
- **Challenge dataset**: https://github.com/UMEP-dev/uda-city-hackathon
- **Simulation**: SuPy loads `uda-city.yml` directly via `SUEWSSimulation(config_path)`
- **Output access**: `sim.output['SUEWS']` → MultiIndex DataFrame (grid, datetime), column `T2` is 2m air temp
- **Timestep**: 5-min model (300s), 15-min output (900s) → 96 outputs/day/grid
- **Spinup**: first 30 days (March), analysis window = April–May (61 days)
- **Threshold**: 35°C on T2 (dry-bulb) — reference default, can be adjusted
- **Risk formula**: geometric mean of (hazard, exposure, vulnerability), each [0,1] scaled

---

## The City: UDA-city

- Locale: 6.93°N 79.86°E (Colombo-like, synthetic)
- 10 neighbourhoods in 3 types:
  - **Refuge** (1-3): Jade Gardens, Serendib Rise, Taman Melati — greener, lower density
  - **Hotspot** (4,5,7,9): Kampong Lama, Dhobi Lines, Mlima Moto, Fuzhou Lanes — dense informal, high pop, low AC
  - **Core** (6,8,10): Lusitano Square, Victoria Exchange, Zheng He Towers — formal high-rise
- QF is OFF — population = exposure data only
- Forcing: present hot-humid (ERA5 2024) + future +2.5°C pseudo-warming

---

*Timestamp: 24 June 2026, ~14:30 BST*
