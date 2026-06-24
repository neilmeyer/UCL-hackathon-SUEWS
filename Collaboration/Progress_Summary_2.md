# Progress Summary 2 — Hackathon Day (24 June 2026, ~15:15)

> Second checkpoint. Site is live and submission-ready.

---

## What's Done Since Checkpoint 1

| Step | Status |
|------|--------|
| Run FUTURE scenario (+2.5°C) on all 10 grids | ✅ |
| Calculate risk bridge (hazard × exposure × vulnerability) | ✅ |
| RAGG-rate all neighbourhoods (present + future) | ✅ |
| Update all 3 interactive visualisations with real data | ✅ |
| Write full `docs/index.html` — dark themed, BCL-style | ✅ |
| Add `.nojekyll` to skip Jekyll | ✅ |
| Fix submodule error (removed .git from nested repo) | ✅ |
| Pages build succeeding, site live | ✅ |

---

## Live Deliverables

- **Pages site**: https://neilmeyer.github.io/UCL-hackathon-SUEWS/
- **Repo**: https://github.com/neilmeyer/UCL-hackathon-SUEWS

---

## Key Results (Final)

### Present Scenario — Risk Ranking

| Rank | Neighbourhood | Type | Hazard | Exposure | Vuln | Risk | RAGG |
|------|---------------|------|--------|----------|------|------|------|
| 1 | Dhobi Lines | Hotspot | 0.59 | 1.00 | 0.92 | 1.00 | 🔴 Red |
| 2 | Fuzhou Lanes | Hotspot | 0.48 | 1.00 | 0.97 | 0.96 | 🔴 Red |
| 3 | Serendib Rise | Refuge | 0.41 | 0.77 | 0.27 | 0.53 | 🟠 Amber |
| 4 | Mlima Moto | Hotspot | 0.07 | 1.00 | 1.00 | 0.49 | 🟠 Amber |
| 5 | Lusitano Square | Core | 0.06 | 0.77 | 0.09 | 0.17 | 🟢 Green |
| 6 | Jade Gardens | Refuge | 1.00 | 0.00 | 0.32 | 0.14 | 🟢 Green |
| 7 | Zheng He Towers | Core | 0.00 | 0.77 | 0.00 | 0.00 | ⬜ Grey |

### Future Scenario — Trajectory Signal
- **Mlima Moto**: 🟠 Amber → 🔴 Red (only neighbourhood changing RAGG band)
- All others hold their present band
- Dangerous hours increase 5–7× across all neighbourhoods

### The Core Finding
**The hottest neighbourhood (Jade Gardens, 38.1°C peak, 75 dangerous hours) ranks 7th on risk. Dhobi Lines (36.9°C, 44 hours) ranks 1st — because 300 people/ha live there with 10% AC and 60% outdoor workers.**

---

## What the Pages Site Contains

1. Hero section with stat cards (2 Red, 507 hours, 10 grids, 7× increase)
2. Key finding callout (red border)
3. Hazard table — all 10 neighbourhoods, present + future
4. Interactive scenario comparison chart (Plotly)
5. Risk bridge table with RAGG ratings
6. Interactive heat matrix (Plotly)
7. CrunchTest narrative (+2.5°C trajectory)
8. Interactive Sankey flow diagram (Plotly)
9. "Where the bridge holds" section
10. "Where the bridge breaks" caveats section
11. Citations (both required SUEWS papers + UNDRR framework)
12. Footer with method summary

---

## Remaining Before 17:00

- [ ] Save final transcript to `transcripts/`
- [ ] Optional: add BCL tagline at top of page
- [ ] Optional: post on SUEWS Discourse (Professional contribution criterion)
- [ ] Final commit and push

---

## Git Log

```
db147e9 Fix Pages build: remove submodule ref, add dataset files directly
59fbfa4 Replace markdown with styled HTML page - dark theme, BCL aesthetic
3e54ba7 Complete submission: Pages site, real visualisations, risk analysis, citations
ace6f19 Progress checkpoint 1: present scenario complete, 10 grids simulated
5033a9e Add overview doc, update data/bridge to point at live UDA-city dataset
2859238 Add hackathon prep: ideas, BCL strategy, and interactive visualizations
9ed9812 Add setup session transcript (23 June 2026)
4c98d2a Initial commit from template
```

---

*Timestamp: 24 June 2026, ~15:15 BST*
