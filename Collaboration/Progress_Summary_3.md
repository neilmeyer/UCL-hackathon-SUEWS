# Progress Summary 3 — Hackathon Day (24 June 2026, ~16:00)

> Third checkpoint. Scenarios spec written, intervention runs prepared.

---

## What's Done Since Checkpoint 2

| Step | Status |
|------|--------|
| Identified the city as Colombo-like (coordinates, names, climate) | ✅ |
| Created Cheat Sheet for verbal discussions | ✅ |
| Created Sue Grimmond Checklist (physics explanations) | ✅ |
| Added "Model Physics" section to HTML page | ✅ |
| Added "What We Would Change" table to HTML page | ✅ |
| Fixed heat matrix labels (no more overlap) | ✅ |
| Added hover tooltips to heat matrix (every cell explained) | ✅ |
| Wrote full page spec (Not-Colombo_Baseline-and-Scenario_UI.md) | ✅ |
| Created intervention scenario script (run_scenarios.py) | ✅ |
| Running intervention scenarios (Trees / Cool Roofs / Combined) | ⏳ Next |

---

## Current State of the Page

**Live at:** https://neilmeyer.github.io/UCL-hackathon-SUEWS/

Sections present:
1. ✅ Hero + stat cards
2. ❌ City context paragraph (to add)
3. ✅ Baseline present (hazard table, risk table, charts)
4. ✅ Baseline future (CrunchTest +2.5°C)
5. ✅ Model physics (roughness, OHM, Macdonald)
6. ❌ What-If Scenarios (awaiting simulation results)
7. ✅ Where Bridge Holds/Breaks (caveats)
8. ❌ Recommendations (to add after scenarios)
9. ✅ Interactive visualisations (3 charts)
10. ✅ What We Would Change table
11. ✅ Citations
12. ✅ Footer

---

## Intervention Scenarios — Ready to Run

Script: `analysis/run_scenarios.py`

| Scenario | Change | Grids Modified |
|----------|--------|---------------|
| A: Trees | evetr 3% → 15%, paved reduced by 12% | Hotspots (4,5,7,9) |
| B: Cool Roofs | albedo paved+bldgs 0.2 → 0.5 | Hotspots (4,5,7,9) |
| C: Combined | Both A + B | Hotspots (4,5,7,9) |

Expected output: `analysis/intervention_scenarios.csv` with dangerous-heat hours for all 10 grids under each scenario.

---

## Next Steps

1. Run `analysis/run_scenarios.py` (~5 min)
2. Add city context paragraph to HTML
3. Add scenarios section to HTML with results table
4. Add recommendations section
5. Rebuild scenario comparison chart with intervention bars
6. Final commit + push
7. Save transcript to `transcripts/`

---

## Key Conversations

- **Sue Grimmond** asked about the physics — we added roughness/OHM/Macdonald explanations
- She wants to see: why refuges are hottest, what we'd change, understanding of model limitations
- Her checklist is in `Collaboration/Sue_Checklist.md`

---

## Files Created This Session

```
Collaboration/
├── Progress_Summary_1.md      (checkpoint 1)
├── Progress_Summary_2.md      (checkpoint 2)
├── Progress_Summary_3.md      (THIS FILE)
├── Sue_Checklist.md           (physics Q&A for expert panel)
├── Cheat_Sheet.md             (plain English explainer)
├── Not-Colombo_Baseline-and-Scenario_UI.md  (page spec)
├── BCL-aligned-Ideas_v1.md    (pre-day strategy)
├── Ideas_v1.md                (pre-day research)
└── UCL-SUEWS-Hackathon-overview.md  (full overview)

analysis/
├── heat_hazard_results.csv           (present scenario)
├── scenario_comparison_results.csv   (present vs future)
├── risk_index_results.csv            (full risk bridge)
├── run_scenarios.py                  (intervention script - ready to run)
├── update_heat_matrix.py             (chart generator)
├── sankey_heat_risk.py               (chart generator)
├── heat_matrix.py                    (original template)
└── scenario_comparison.py            (original template)
```

---

## Time Remaining

~1 hour until 17:00 submission deadline.

Priority order:
1. Run scenarios (5 min)
2. Update HTML with results (10 min)
3. Push (1 min)
4. Save transcript (5 min)
5. Any polish time remaining

---

*Timestamp: 24 June 2026, ~16:00 BST*
