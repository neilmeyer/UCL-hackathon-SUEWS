# UCL SUEWS Community Hackathon — Full Overview

> Prepared 23 June 2026, the evening before the event. This document consolidates everything we know, everything we've prepared, and our strategy for tomorrow.

---

## What the Hackathon Is

A half-day event (14:00–17:00, 24 June 2026) at UCL East where ~20 researchers, students, and practitioners use the SUEWS urban climate model — driven via an AI agent — to model urban heat in a heat-vulnerable city and translate that hazard into a socioeconomic heat-risk indicator.

**Organisers:** Ting Sun (UCL), Sue Grimmond (Reading)
**Table leads:** Vitor Lavor, Megan Stretton, Matthew Paskin, Yiqing Liu (SUEWS); Jiapei Liu (AI tools)

---

## What We Have to Deliver

| Deliverable | Where | Judged By |
|-------------|-------|-----------|
| GitHub Pages site (public) | `https://neilmeyer.github.io/UCL-hackathon-SUEWS/` | External panel (Policy relevance, Presentation quality) |
| Repository files (SUEWS config, code, outputs) | `https://github.com/neilmeyer/UCL-hackathon-SUEWS` | Expert panel (Scientific soundness) |
| AI session transcripts | `transcripts/` folder | Expert panel (Innovation & AI collaboration) |
| Discourse channel posts (before the day) | SUEWS Community Discourse | Expert panel (Professional contribution) |

---

## How We're Scored

Five criteria, each out of 20, totalling 100:

| Criterion | Weight | Panel | Key Evidence |
|-----------|--------|-------|--------------|
| Scientific soundness | 20 | Expert | Correct SUEWS config, reproducible workflow, proper citation |
| Policy relevance & honest bridging | 20 | External | Pages site — where the hazard-to-indicator link holds and breaks |
| Professional contribution | 20 | Expert | Discourse posts before/during the event |
| Presentation quality | 20 | External | Pages site narrative and visualisations |
| Innovation & AI collaboration | 20 | Expert | Transcripts — creative, effective use of suews-agent + AI tool |

---

## What We've Set Up (Pre-Day)

### Infrastructure
- **Repo:** `neilmeyer/UCL-hackathon-SUEWS` — created from template, public ✅
- **GitHub Pages:** Enabled, main branch /docs ✅
- **Pages URL:** https://neilmeyer.github.io/UCL-hackathon-SUEWS/ ✅
- **SuPy 2026.6.5:** Installed, test simulation ran successfully (48 timesteps, 1081 output columns, 0.3s) ✅
- **suews-agent MCP server:** Configured in Kiro settings (needs reload to connect) ✅
- **GitHub CLI (`gh`):** Installed and authenticated ✅
- **Plotly:** Installed for interactive visualisations ✅

### Pre-Built Visualisation Templates
All in `analysis/`, outputting to `docs/`:

| Script | Output | Purpose |
|--------|--------|---------|
| `sankey_heat_risk.py` | `docs/sankey_heat_risk.html` | BCL-style flow: Archetype → Hazard Band → Vulnerability → RAGG |
| `heat_matrix.py` | `docs/heat_matrix.html` | RoL-style grid: archetypes × risk dimensions |
| `scenario_comparison.py` | `docs/scenario_comparison.html` | Grouped bars: current vs +2.5°C with threshold lines |

**On the day:** swap placeholder data for real SUEWS output, re-run scripts, commit.

### Strategy Documents
All in `Collaboration/`:

| File | Content |
|------|---------|
| `Ideas_v1.md` | 12 researched ideas with pre-test actions and sources |
| `BCL-aligned-Ideas_v1.md` | How Beyond Countdown methodology maps onto the hackathon |
| `UCL-SUEWS-Hackathon-overview.md` | This document |

---

## Our Strategy: The BCL Approach to Climate Risk

We're applying Beyond Countdown's outside-in governance diagnostic methodology to urban heat risk. The core framing:

### The Parallel

| BCL Concept | Hackathon Application |
|-------------|---------------------|
| Outside-in reading of the public record | Outside-in physical model (SUEWS) reading observable inputs |
| Gap between governance-as-structured and governance-as-lived | Gap between modelled hazard and actual human experience |
| Macro Risk × Local Risk | Hazard × Exposure × Vulnerability (UNDRR) |
| RAGG rating (Red/Amber/Green/Grey) | Neighbourhood heat risk classification |
| Trajectory indicators (↑ → ↓ ⚡) | Present vs Future scenario direction of travel |
| CrunchTest stress scenarios | Amplified-heatwave forcing run |
| "Compass, not certification" | "Indicative estimate, not measurement" |
| Bearing Report structure | Pages site narrative structure |

### Pages Site Structure (BCL Bearing Report format)

1. **Executive Summary** — One sentence: what the city faces
2. **Risk Assessment** — SUEWS output by archetype (Sankey + heat matrix)
3. **Exposure & Vulnerability** — Population × characteristics
4. **Gap Analysis** — Where the bridge holds and breaks
5. **CrunchTest** — The +2.5°C scenario: what happens under stress
6. **Recommendations** — Interventions (tree cover, albedo, settlement upgrading)
7. **Caveats & Limitations** — What the model cannot represent
8. **Citations** — Proper SUEWS citation + UNDRR framework reference

---

## What's Revealed on the Day

We don't have these yet — they arrive at kickoff:

- **The focus city** (synthetic, hot-humid, lower-income, rapidly urbanising)
- **Complete city dataset** (land cover, building form, population, anthropogenic heat, hot-season forcing, +2-3°C future variant)
- **The heat-to-risk bridge function** (currently a placeholder in `bridge/heat-to-risk.md`)
- **UNDRR indicator calculation approach and reference material**
- **The hackathon template repo** (under UMEP-dev — different from our practice repo)

---

## Day-Of Workflow

### Phase 1: Explore (14:10–14:30)
- Read the revealed dataset and bridge function
- Ask suews-agent: "What archetypes are in this dataset? What are their characteristics?"
- Map archetypes to LCZ categories
- Identify which look most heat-vulnerable

### Phase 2: Simulate (14:30–15:15)
- Run SUEWS for all archetypes under current forcing
- Run SUEWS for all archetypes under +2.5°C forcing
- Extract dangerous-heat hours (hours where T_air > threshold)
- Calculate WBGT estimates if humidity data is available

### Phase 3: Analyse (15:15–15:45)
- Apply the heat-to-risk bridge function
- Classify archetypes using RAGG rating
- Build the Sankey flow diagram with real data
- Build the heat matrix with real scores
- Build the scenario comparison chart

### Phase 4: Narrate (15:45–16:30)
- Write the Pages site using the Bearing Report structure
- Embed the interactive charts
- Write the gap analysis: where the bridge holds, where it breaks
- Add SUEWS citations
- Add UNDRR framework reference

### Phase 5: Polish & Submit (16:30–17:00)
- Final commit and push
- Verify Pages renders correctly
- Save AI session transcript to `transcripts/`
- Submit repo link to organisers

---

## Key Numbers to Know

| Metric | Threshold | Source |
|--------|-----------|--------|
| WBGT moderate risk | 28°C | ISO 7243 |
| WBGT high risk (heavy work stops) | 32°C | ISO 7243 |
| Wet-bulb survivability limit | 35°C (>6 hours) | UNU |
| Tree cooling effect | 0.5–5.8°C air temp reduction | Springer 2025 |
| Informal settlement WBGT exceedance | Regularly > activity thresholds | ResearchGate 2021 |

---

## SUEWS Citation (Required)

> Järvi, L., Grimmond, C.S.B. and Christen, A. (2011). The Surface Urban Energy and Water Balance Scheme (SUEWS): Evaluation in Los Angeles and Vancouver. *Journal of Hydrology*, 411(3–4), 219–237. DOI: 10.1016/j.jhydrol.2011.10.001

> Ward, H.C., Kotthaus, S., Järvi, L. and Grimmond, C.S.B. (2016). Surface Urban Energy and Water Balance Scheme (SUEWS): Development and evaluation at two UK sites. *Urban Climate*, 18, 1–32. DOI: 10.1016/j.uclim.2016.05.001

Plus the specific software version citation from https://docs.suews.io/stable/#how-to-cite-suews

---

## Prompt Templates (Ready to Paste)

### Explore
1. "What neighbourhood archetypes are in this dataset and what are their land cover characteristics?"
2. "Which archetype has the highest impervious fraction? Which has the most tree cover?"
3. "Show me the meteorological forcing — what's the hottest period?"

### Simulate
4. "Run SUEWS for all archetypes under the current hot-season forcing. Return the hourly air temperature output."
5. "Now run the same configuration under the +2.5°C amplified-heatwave forcing."
6. "For each archetype, count the hours where T_air exceeds 35°C."

### Analyse
7. "Compare peak temperatures across archetypes — rank from hottest to coolest."
8. "Apply the bridge function to convert dangerous-heat hours into the risk indicator."
9. "What would happen if we increased tree cover by 15% in the informal settlement archetype?"

### Critique
10. "What are the main limitations of this SUEWS configuration for representing night-time heat in informal settlements?"
11. "Where does the hazard-to-indicator bridge function break down — what does it assume that may not hold?"
12. "If we had more time, what additional data or model features would improve this assessment?"

---

## Repo Structure (Current)

```
UCL-hackathon-SUEWS/
├── .gitignore
├── README.md
├── TASK_BRIEF.md
├── ONBOARDING_PROMPT.md
├── analysis/
│   ├── README.md
│   ├── sankey_heat_risk.py
│   ├── heat_matrix.py
│   └── scenario_comparison.py
├── bridge/
│   └── heat-to-risk.md          ← placeholder, revealed on day
├── Collaboration/
│   ├── Ideas_v1.md
│   ├── BCL-aligned-Ideas_v1.md
│   └── UCL-SUEWS-Hackathon-overview.md
├── data/
│   └── README.md                ← dataset arrives on day
├── docs/
│   ├── index.md                 ← Pages site (to be written)
│   ├── sankey_heat_risk.html    ← interactive Sankey
│   ├── heat_matrix.html         ← interactive heatmap
│   └── scenario_comparison.html ← interactive bar chart
└── transcripts/
    ├── README.md
    └── session-2026-06-23-setup.md
```

---

## Tonight's Checklist

- [x] Repo created and Pages live
- [x] SUEWS confirmed working (SuPy test simulation)
- [x] Visualisation templates built and tested
- [x] BCL strategy documented
- [x] Prompt templates written
- [ ] Draft `docs/index.md` skeleton with placeholder sections
- [ ] Post on SUEWS Discourse channel (Professional contribution)
- [ ] Skim the UNDRR Extreme Heat Risk Governance Framework
- [ ] Test that Pages renders the iframe embeds correctly

---

## Key Links

| Resource | URL |
|----------|-----|
| Our repo | https://github.com/neilmeyer/UCL-hackathon-SUEWS |
| Our Pages site | https://neilmeyer.github.io/UCL-hackathon-SUEWS/ |
| SUEWS docs | https://docs.suews.io/ |
| suews-agent | https://github.com/UMEP-dev/suews-agent |
| SUEWS Discourse (hackathon channel) | https://community.suews.io/t/welcome-to-the-suews-community-hackathon-24-june/69 |
| UNDRR Heat Framework | https://www.undrr.org/publication/documents-and-publications/extreme-heat-risk-governance-framework-and-toolkit |
| Beyond Countdown | https://beyondcountdown.com |
| SuPy PyPI | https://pypi.org/project/supy |

---

*We're set. Tools work, strategy is clear, templates are ready. Tomorrow we focus on the science and the story.*
