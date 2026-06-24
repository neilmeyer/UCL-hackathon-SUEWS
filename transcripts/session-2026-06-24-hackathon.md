# Session Transcript — 24 June 2026 (Hackathon Day)

**Event:** SUEWS Community Hackathon, UCL East  
**Team:** Neil Meyer + Kiro (Claude)  
**Reviewer:** Prof. Sue Grimmond (SUEWS co-creator)  
**Time:** ~09:00–17:00 BST  

---

## What We Built

A complete heat-risk diagnostic for UDA-city (a synthetic Colombo-like tropical metropolis) demonstrating that **temperature alone is insufficient for heat-risk governance**.

### Deliverable
- **Live site:** https://neilmeyer.github.io/UCL-hackathon-SUEWS/
- **Repo:** https://github.com/neilmeyer/UCL-hackathon-SUEWS

---

## Timeline

### Morning (setup + baseline)
- Cloned UMEP-dev/uda-city-hackathon challenge dataset (10 neighbourhoods, 3 types)
- Configured SUEWS v2026.6.5 via SuPy for all 10 grids
- Ran present-climate simulation (ERA5 2024, hot-humid forcing, April–May)
- Ran future-climate simulation (+2.5°C uniform warming stress test)
- Calculated risk bridge: Hazard × Exposure × Vulnerability → RAGG rating

### Afternoon (analysis + visualisation)
- Built interactive Plotly charts: scenario comparison, heat matrix, Sankey flow
- Created dark-theme GitHub Pages site with full narrative
- Sue Grimmond reviewed physics — added roughness/OHM/Macdonald explanations
- Ran intervention scenarios (Trees +12%, Cool Roofs albedo 0.5, Combined)
- Updated page with scenarios, recommendations, governance framing

---

## Key Findings

1. **Hottest ≠ highest risk.** Jade Gardens peaks at 38.1°C (rank 1 on temperature) but ranks 7th on risk. Dhobi Lines (36.9°C) ranks 1st because 300 people/ha, 10% AC, 60% outdoor workers.

2. **Refuges are hottest due to low roughness.** Sparse, green neighbourhoods have low z₀ (Macdonald parameterisation from low λp). Weak turbulent mixing traps heat near the surface. Dense high-rise cores are coolest because tall buildings drive convective transport.

3. **+2.5°C warming increases dangerous hours 5–7×.** Kampong Lama goes from 68h → 507h (35% of April–May above 35°C). Mlima Moto moves from Amber to Red.

4. **Cool roofs dominate as intervention.** Albedo 0.5 reduces dangerous hours by 88–100% in hotspots. Trees at +12% canopy actually *increase* dangerous hours slightly — insufficient canopy without roughness benefit.

5. **Physical interventions buy time, not solutions.** Under +2.5°C even with cool roofs, hundreds of dangerous hours remain. The residual gap must be closed by governance.

---

## Intervention Scenario Results

| Neighbourhood | Baseline (h) | Trees (h) | Cool Roofs (h) | Combined (h) |
|---|---|---|---|---|
| Kampong Lama | 68 | 69 | 8 | 16 |
| Dhobi Lines | 44 | 48 | 4 | 5 |
| Mlima Moto | 5 | 16 | 0 | 0 |
| Fuzhou Lanes | 36 | 42 | 4 | 5 |

---

## Model Configuration

- **Model:** SUEWS v2026.6.5 via SuPy
- **Forcing:** ERA5-based synthetic hot-humid (present) + uniform +2.5°C (future)
- **Timestep:** 15-min output, 96 per day
- **Analysis window:** April–May (61 days, skip 30-day spinup)
- **Threshold:** 35°C dry-bulb
- **Physics enabled:** OHM (Objective Hysteresis Model), Macdonald roughness, Penman-Monteith evaporation
- **Physics not enabled:** QF (anthropogenic heat), SPARTACUS radiation, dynamic OHM

---

## Tools Used

- **SuPy** — Python wrapper for SUEWS
- **Plotly** — Interactive visualisations
- **Kiro (Claude)** — AI coding partner (all code, analysis, page design)
- **GitHub Pages** — Hosting
- **gh CLI** — Deployment

---

## What We'd Improve Given More Time

1. Enable QF (anthropogenic heat feedback loop)
2. Implement WBGT (wet-bulb globe temperature) — more physiologically relevant at 81% RH
3. SPARTACUS multi-layer radiation for better canyon differentiation
4. Dynamic OHM for humid conditions with frequent rainfall
5. Larger tree intervention (30%+ closed canopy with tall trees for roughness benefit)
6. Indoor heat model for metal-roofed housing

---

## Sue Grimmond's Review Notes

- Confirmed roughness/OHM explanation is physically sound
- Suggested Macdonald parameterisation naming (λp, z₀)
- Noted FAI values drive the core ventilation effect
- Approved "Where Physics Ends and Governance Begins" framing
- Checklist at `Collaboration/Sue_Checklist.md`

---

*Transcript generated: 24 June 2026, ~16:30 BST*
