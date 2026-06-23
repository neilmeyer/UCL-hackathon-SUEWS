# BCL-Aligned Hackathon Strategy

> How Beyond Countdown's outside-in governance methodology maps onto the SUEWS urban heat hackathon — and how to use it as a differentiator.

---

## The Core Parallel

| Beyond Countdown | SUEWS Hackathon |
|-----------------|-----------------|
| Outside-in governance intelligence | Outside-in physical climate modelling |
| Gap between governance-as-structured and governance-as-lived | Gap between modelled hazard and actual human risk |
| 18 Macro Risks × 20 Local Risks | Hazard × Exposure × Vulnerability (UNDRR) |
| Bearing Report: diagnosis, not certification | SUEWS output: indicative estimate, not measurement |
| "Where it holds and where it breaks" | Exactly what judges ask for ("honest bridging") |

---

## 1. Frame the Submission Like a Mini Bearing Report

**Structure your GitHub Pages site as:**

1. **Executive Summary** — One sentence: what the city faces, what the model shows, what breaks
2. **Risk Assessment** — SUEWS output by neighbourhood archetype (heat hazard layer)
3. **Exposure & Vulnerability Mapping** — Population × archetype characteristics
4. **Gap Analysis** — Where the hazard-to-indicator bridge holds and where it breaks
5. **CrunchTest Scenario** — The +2–3°C amplified heatwave: what happens under stress
6. **Strategic Recommendations** — What would reduce risk (tree cover, albedo, informal settlement upgrading)
7. **Sources & Caveats** — Model limitations, data gaps, what you'd need to verify

This is the BCL report structure applied to climate risk. Judges see a professional, structured output rather than a generic results dump.

---

## 2. RAGG Rating for Neighbourhood Archetypes

Apply BCL's Red/Amber/Green/Grey classification to each neighbourhood:

| Rating | Dangerous-Heat Hours (per hot season) | Meaning |
|--------|---------------------------------------|---------|
| 🔴 Red | >200 hours above threshold | Material heat exposure, inadequate adaptive capacity |
| 🟠 Amber | 100–200 hours | Exposure exists; some resilience factors present |
| 🟢 Green | <100 hours | Manageable with existing urban form |
| ⬜ Grey | N/A | Structurally immaterial (e.g., water bodies, parks) |

**Why this works:** Immediately legible. Mirrors the risk communication language BCL uses for governance. Judges from outside the SUEWS team (the external panel scoring policy relevance and presentation) will understand it instantly.

---

## 3. Trajectory Indicators: Present → Future

Borrow BCL's ↑ → ↓ ⚡ indicators to show how risk *changes* under the future scenario:

| Archetype | Current Rating | Future (+2.5°C) Rating | Trajectory |
|-----------|---------------|----------------------|------------|
| Compact high-rise (LCZ 1) | 🟠 Amber | 🔴 Red | ↓ Deteriorating |
| Open low-rise (LCZ 6) | 🟢 Green | 🟠 Amber | ↓ Deteriorating |
| Informal settlement | 🔴 Red | 🔴 Red (worse) | ↓ Deteriorating |
| Dense trees (LCZ A) | 🟢 Green | 🟢 Green | → Stable |

**The narrative:** "Under current conditions, 3 of 8 archetypes are in the Red zone. Under +2.5°C warming, 5 of 8 shift to Red. The direction of travel is clear."

---

## 4. CrunchTest = Climate Stress Test

BCL's CrunchTest asks: "What happens to this organisation when a latent risk materialises?"

**Your climate equivalent:** "What happens to this neighbourhood during a 5-day heatwave?"

Run the amplified-heatwave forcing. Report:
- Peak temperature reached
- Consecutive hours above danger threshold
- Night-time minimum (does it cool below 25°C? If not, there's no recovery)
- Which archetypes breach survivability limits

Frame it as: "The CrunchTest reveals that under a sustained heatwave, informal settlement archetypes exceed safe outdoor activity thresholds for 14+ consecutive hours, with no nocturnal recovery."

---

## 5. "Compass, Not Certification" — Epistemic Honesty

BCL's methodology page states its output is "an indicative, point-in-time analytical judgement — not a certification, audit, or statement of verified internal fact."

Apply the same language to SUEWS:

> "This assessment is an indicative, model-based estimate of heat hazard — not a measurement. SUEWS represents neighbourhood-scale energy balance physics but cannot capture micro-scale effects (individual building shading, indoor temperatures, human behaviour). The gap between modelled outdoor air temperature and lived heat experience is real, and it is wider for informal settlements where building materials, ventilation, and occupancy patterns differ most from model assumptions."

This is exactly what "honest bridging" means. It's also exactly how BCL talks.

---

## 6. Macro Risk × Local Risk = Dual-Axis Diagnostic

**Macro Heat Risks (external pressures arriving at the city):**
- Background climate warming (+2–3°C by mid-century)
- Increased heatwave frequency and intensity
- Urban Heat Island amplification from ongoing urbanisation
- Energy system stress during heat events (AC demand → grid failure → heat exposure)

**Local Heat Vulnerabilities (neighbourhood-specific weaknesses):**
- High impervious fraction (traps heat)
- Low tree canopy (no evapotranspirative cooling)
- High population density in informal housing
- Limited access to cooling infrastructure
- Outdoor workforce with no shade provision

**The diagnostic:** Risk materialises where macro pressure meets local vulnerability. SUEWS quantifies the macro (temperature output). The socioeconomic data quantifies the local. The bridge function multiplies them.

---

## 7. Professional Contribution — BCL's Tone

When posting on the SUEWS Discourse channel (which scores "Professional contribution"), write in BCL's voice:

- Structured, evidence-based observations
- Honest about what you don't know
- Designed to help others, not to show off
- Asks constructive questions rather than making claims

**Example post:**
> "We've been testing scenario comparisons using SuPy — varying tree fraction by ±10% produces a ~1.5°C difference in peak afternoon air temperature in the sample data. Has anyone explored whether the anthropogenic heat (QF) parameter has a similar magnitude of effect? Useful to know which lever matters more for the policy narrative."

That's professional, constructive, community-oriented — and it's how BCL talks to its audience.

---

## 8. Data Presentation — BCL's Visual Language

BCL uses:
- Compact grids (the RoL matrix)
- Single-letter/number codes (B.3, X2)
- Colour-coded risk (RAGG)
- One-line trajectory summaries

**Apply this to your Pages site:**

```
NEIGHBOURHOOD HEAT RISK SUMMARY

Archetype A (Compact High-Rise)    🟠 B.3 ↓  X1
Archetype B (Open Low-Rise)        🟢 A.2 →  X6
Archetype C (Informal Settlement)  🔴 D.5 ↓  X3
Archetype D (Dense Trees)          🟢 A.1 →  —
```

This is dense, professional, and immediately scannable — exactly what a presentation panel wants to see.

---

## 9. "See the Picture Forming Before You Have to Act"

BCL's tagline applies directly to climate risk:

> "See the heat picture forming before vulnerable communities have to act."

Use this as the conceptual frame for your Pages site. The model shows what's coming. The risk indicator shows who's exposed. The gap analysis shows what governance (city planning, tree planting, informal settlement upgrading) could do about it.

---

## 10. Innovation & AI Collaboration — The BCL Angle

**Your differentiator for the "Innovation and AI collaboration" criterion:**

You're not just using an AI agent to run SUEWS. You're applying a structured outside-in risk assessment methodology (developed for governance intelligence) to urban climate risk. The AI agent is your execution layer; the BCL framework is your analytical layer.

In your transcript, make this explicit:
> "We're applying Beyond Countdown's outside-in diagnostic methodology to climate risk. The same principle applies: read the observable evidence (physical model output, land cover data, population distribution), identify the gap between architecture and lived reality, and say plainly where the bridge holds and where it breaks."

That's novel. That's cross-disciplinary. That's exactly what "Innovation" rewards.

---

## Summary: How to Deploy This Tomorrow

| Phase | BCL Concept | Hackathon Application |
|-------|-------------|----------------------|
| Explore | Outside-in reading of public record | Read the dataset without assumptions; let the model speak |
| Diagnose | Dual-axis scoring (Leadership × Lived) | Dual-axis scoring (Hazard × Vulnerability) |
| Classify | RAGG rating per risk | RAGG rating per neighbourhood |
| Stress-test | CrunchTest scenarios | Amplified-heatwave forcing run |
| Narrate | Gap analysis + trajectory | "Where the bridge holds and where it breaks" |
| Caveat | "Compass, not certification" | "Indicative estimate, not measurement" |
| Recommend | Strategic recommendations | Policy-actionable interventions |

---

*This framing makes your submission distinctive. Everyone else will produce heat maps and temperature charts. You'll produce a structured risk diagnostic with a clear analytical methodology — the kind of output that a board, a city planner, or a UNDRR policy team would actually use.*
