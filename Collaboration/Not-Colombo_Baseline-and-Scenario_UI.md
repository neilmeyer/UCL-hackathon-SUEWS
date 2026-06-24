# Not-Colombo: Baseline & Scenario UI Spec

> A spec for the final GitHub Pages deliverable. The page should tell a complete story from baseline through interventions to honest limits — readable by a non-domain person.

---

## Page Structure (top to bottom)

### 1. Hero
- Title: "UDA-City Heat Risk Diagnostic"
- Subtitle/question: "Where is heat most dangerous to people — and what can we do about it?"
- Four stat cards: key headline numbers

### 2. The City (context)
- One paragraph: what UDA-city is, where it is (Colombo-like), hot-humid, 10 neighbourhoods
- Simple map/diagram OR a compact table showing the three neighbourhood types (Refuge / Hotspot / Core) with a one-liner each
- Why it matters: "This is a lower-income city where 400 people per hectare live without air conditioning"

### 3. Baseline — Present Climate
- Headline: "This is the city today"
- Key finding callout (red box): "The hottest neighbourhood is NOT the highest-risk one"
- Hazard table: all 10 neighbourhoods, peak T2, dangerous hours
- Risk bridge table: hazard × exposure × vulnerability → RAGG rating
- One interactive chart: scenario comparison (present vs future)
- One interactive chart: heat risk matrix with hover tooltips

### 4. Baseline — Future (+2.5°C)
- Headline: "This is the city under 2.5°C of warming"
- Key numbers: hours increase 5–7×, Mlima Moto moves Amber → Red
- Narrative: "Under warming, Kampong Lama spends 35% of April–May above 35°C for a population with 8% AC access"
- Same table with future columns shown alongside present

### 5. The Model Physics (why it works this way)
- Why refuges are hottest (roughness length, OHM, Macdonald)
- Why cores are coolest (FAI, turbulent mixing, self-shading)
- Keep it short — 3 paragraphs max, use parameter names

### 6. What-If Scenarios — "What can we do?"
- Intro: "We tested three interventions the model can simulate. Each changes a physical parameter in the hotspot neighbourhoods and re-runs SUEWS."

#### Scenario A: Plant Trees (+12% canopy in hotspots)
- What we changed: `evetr` fraction 3% → 15% in grids 4, 5, 7, 9
- Result: dangerous hours reduced from X → Y (Z% reduction)
- Confidence: 🟢 High — SUEWS evapotranspiration physics well-validated
- Narrative: "Tripling tree canopy in the informal settlements reduces dangerous hours by ~N, equivalent to removing Z days of extreme heat per season"

#### Scenario B: Cool Roofs (albedo 0.2 → 0.5 in hotspots)
- What we changed: `alb` for paved and bldgs surfaces raised to 0.5
- Result: dangerous hours reduced from X → Y
- Confidence: 🟠 Moderate — bulk albedo doesn't capture street-level reflected radiation trade-offs
- Narrative: "Reflective surfaces reduce peak temperature by ~N°C but the effect is smaller than trees because it doesn't add evaporation"

#### Scenario C: Combined (Trees + Cool Roofs)
- What we changed: both interventions together
- Result: combined reduction
- Confidence: 🟢 High for the physics; 🔴 Low for real-world implementation feasibility
- Narrative: "Even with both interventions, Kampong Lama still faces X dangerous hours. The residual gap is what governance must close."

#### Summary comparison table
| Scenario | Kampong Lama DH | Dhobi Lines DH | Reduction vs Baseline |
|---|---|---|---|
| Baseline (present) | 68 | 44 | — |
| A: Trees | ? | ? | ?% |
| B: Cool roofs | ? | ? | ?% |
| C: Combined | ? | ? | ?% |
| Future (+2.5°C, no intervention) | 507 | 424 | +600% |

### 7. The Gap — What the Model Can't Fix
- Headline: "Where physics ends and governance begins"
- Bullet list of things we CANNOT model but matter:
  - Indoor heat amplification (metal roofs)
  - Human behaviour (do people stay indoors? do they hydrate?)
  - Work-hour restrictions for outdoor workers
  - AC provision and the waste-heat feedback loop
  - Emergency shelter / cooling centres
  - Real demographics (actual census data vs synthetic proxies)
- Framing: "The model shows where and when it's dangerous. It shows what land-cover changes reduce the hazard. But the gap between 'the air is 37°C' and 'this person is in danger' is filled by governance, infrastructure, and individual capacity — none of which the model holds."

### 8. What We'd Recommend (policy-facing)
- 3–5 concrete, prioritised recommendations:
  1. **Priority street-tree planting in Kampong Lama and Dhobi Lines** — highest impact per tree based on model evidence
  2. **Cool-roof programmes targeting metal-roofed informal housing** — model supports albedo effect; real-world co-benefit of reducing indoor heat (not modelled but literature-supported)
  3. **Heat early-warning system keyed to outdoor-worker hours** — model output directly supports timing (which hours exceed threshold)
  4. **Night-time cooling assessment** — model shows whether T2 drops below 25°C overnight (recovery threshold); if not, intervene with shelter access
  5. **Do NOT rely on temperature alone for policy** — the risk bridge demonstrates that hazard ranking ≠ risk ranking; policy must combine physical data with exposure and vulnerability

### 9. Where the Bridge Holds / Breaks
- Already written — keep as-is
- This is the "honest bridging" the judges score directly

### 10. Interactive Visualisations
- Sankey flow: Neighbourhood → Hazard → Vulnerability → Risk
- Heat matrix: 10 rows × 6 columns with hover
- Scenario comparison: grouped bars

### 11. Method + Citations
- Model version, forcing source, physics options
- Both SUEWS papers + UNDRR framework
- AI tool acknowledgment

### 12. Footer
- "This is a compass, not a certification"
- Event details, repo link

---

## Data Requirements

| Item | Source | Status |
|------|--------|--------|
| Present simulation (10 grids) | SuPy run | ✅ Done |
| Future simulation (10 grids) | SuPy run, modified forcing | ✅ Done |
| Scenario A: Trees | SuPy run, modified evetr | ❌ To run |
| Scenario B: Cool roofs | SuPy run, modified alb | ❌ To run |
| Scenario C: Combined | SuPy run, both changes | ❌ To run |
| Risk bridge (all scenarios) | Python calculation | ❌ To calculate |
| Socioeconomic data | socioeconomic.csv | ✅ Available |

---

## Visual Tone
- Dark navy background (#0d1b2a)
- RAGG colour coding (Red/Amber/Green/Grey)
- BCL stat-card style for key numbers
- Plotly interactive charts on dark background
- Professional, data-dense, accessible to non-technical reader
- Every claim tagged with confidence level (🟢 🟠 🔴)

---

*Created: 24 June 2026, ~15:40 BST*
