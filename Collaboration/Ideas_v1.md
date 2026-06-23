# Hackathon Ideas & Pre-Testing Notes

> Compiled 23 June 2026, the day before the event. These are ideas to explore in advance or deploy on the day.

---

## 1. Scenario Comparison: "What-If" Land Cover Changes

**Concept:** Run SUEWS for the same neighbourhood archetype but vary a single parameter (e.g., tree fraction, impervious fraction, building height) to isolate its cooling/heating effect.

**Why it's strong:** Directly demonstrates scientific understanding of urban heat drivers. Judges want to see you know *what* SUEWS is sensitive to and *why*.

**Pre-test:** Use SuPy to load sample data, duplicate the state, change `fr_evergreen_tree` from 0.05 → 0.25, re-run, and compare output air temperatures.

**Source:** [SUEWS sensitivity analysis literature (AMS Journals)](https://journals.ametsoc.org/doi/full/10.1175/2007JAMC1598.1); [SUEWS Advanced Tutorial (UMEP)](https://umep-docs.readthedocs.io/projects/tutorial/en/latest/Tutorials/SuewsAdvanced.html)

---

## 2. "Dangerous-Heat Hours" as Your Primary Hazard Metric

**Concept:** Count the number of hours where outdoor air temperature (or WBGT estimate) exceeds a threshold (e.g., 35°C apparent temperature, or 28°C WBGT). Express this per sub-district.

**Why it's strong:** Maps directly to the UNDRR framework's emphasis on exposure duration. A recent EGU abstract describes combining temperature distributions with activity patterns and expressing results as "time above a heat threshold" — exactly what SUEWS can output.

**Pre-test:** After running a 24h simulation, filter output for `T_air > 35` and count rows. This becomes your heat hazard layer.

**Source:** [EGU26 abstract on dynamic heat exposure (Copernicus)](https://meetingorganizer.copernicus.org/EGU26/EGU26-9251.html); [Statista — cities by hours exceeding wet-bulb thresholds](https://www.statista.com/chart/31008/cities-by-annual-hours-exceeding-wet-bulb-temperature-uncomprehensable-heat-thresholds/)

---

## 3. UNDRR Extreme Heat Risk Governance Framework (COP30, Nov 2025)

**Concept:** Anchor your hazard-to-risk bridge in the UNDRR's published framework. It defines extreme heat risk across three dimensions: hazard, exposure, and vulnerability — with governance as the cross-cutting enabler.

**Why it's strong:** This is almost certainly what the organisers will reference on the day. Knowing the framework in advance gives you a head start framing the narrative.

**Key ideas from the framework:**
- Risk = f(Hazard, Exposure, Vulnerability)
- Decision-makers need indicators that support action at different timescales (immediate response vs long-term planning)
- The toolkit emphasises measuring governance *capacity*, not just physical hazard

**Pre-test:** Draft a simple 3-column table: Hazard (from SUEWS), Exposure (population density per archetype), Vulnerability (proxy: informal settlement fraction or income level).

**Source:** [UNDRR Extreme Heat Risk Governance Framework and Toolkit (Nov 2025)](https://www.undrr.org/publication/documents-and-publications/extreme-heat-risk-governance-framework-and-toolkit); [WMO announcement](https://wmo.int/media/news/new-framework-and-toolkit-strengthens-extreme-heat-governance)

---

## 4. Interactive Plotly Charts on GitHub Pages

**Concept:** Generate interactive HTML charts (temperature time-series, scenario comparisons) using Plotly in Python, save as `.html`, and embed in your GitHub Pages site using `<iframe>` or `<embed>` tags.

**Why it's strong:** Judges score "Presentation quality" — interactive charts are far more engaging than static images, and they demonstrate AI-tool fluency.

**How:** `plotly.offline.plot(fig, filename='docs/temp_chart.html')` → then in `docs/index.md`: `<iframe src="temp_chart.html" width="100%" height="400"></iframe>`

**Pre-test:** Create a dummy chart now and confirm it renders on your Pages site.

**Source:** [Plotly community — displaying graphs on GitHub Pages](https://community.plotly.com/t/how-to-display-plotly-graph-on-github-pages/44398)

---

## 5. Local Climate Zones (LCZ) as Neighbourhood Archetypes

**Concept:** The city will have "many neighbourhoods (archetypes)." These are almost certainly Local Climate Zones — the standard typology linking urban form to thermal behaviour. Know the LCZ numbering (LCZ 1 = compact high-rise, LCZ 6 = open low-rise, LCZ G = water, etc.).

**Why it's strong:** If you can immediately map the dataset's archetypes to LCZ categories and discuss their expected thermal behaviour, you'll sound authoritative in your narrative.

**Pre-test:** Review the LCZ classification and sketch expected temperature rankings (compact high-rise > open low-rise > dense trees).

**Source:** [Stewart & Oke (2012) — BAMS](https://journals.ametsoc.org/view/journals/bams/93/12/bams-d-11-00019.1.xml); [Global LCZ map (100m resolution)](https://www.researchgate.net/publication/363055094_A_global_map_of_local_climate_zones_to_support_earth_system_modelling_and_urban-scale_environmental_science)

---

## 6. Urban Trees as a Cooling Intervention — Quantify the Benefit

**Concept:** SUEWS can model increased tree cover and its effect on latent heat flux (evapotranspiration cooling). Run a "current" vs "10% more tree canopy" scenario.

**Why it's strong:** Directly policy-relevant. A 2026 Nature paper found trees halve the UHI effect globally but benefits are unequally distributed — a perfect hook for the "honest bridging" criterion.

**Key numbers:** Trees reduce air temperature by 0.5–5.8°C depending on canopy density and climate. Street trees had the highest air temperature reduction effect in a 2026 study.

**Pre-test:** In sample data, increase deciduous tree fraction by 10%, re-run, compare peak temperatures.

**Source:** [Trees halve UHI globally (Nature, 2026)](https://www.nature.com/articles/s41467-026-71825-x); [Air temperature reduction by urban green strategies (Nature, 2026)](https://www.nature.com/articles/s44284-025-00370-3)

---

## 7. Informal Settlements & Disproportionate Heat Exposure

**Concept:** Frame your risk indicator around the most vulnerable: informal settlement residents experience chronic heat stress that weather stations underestimate. WBGT in informal housing regularly exceeds safe activity thresholds.

**Why it's strong:** The city is described as "rapidly urbanising, heat-vulnerable, lower-income, hot-humid." Informal settlements are almost certainly in the dataset. Explicitly naming this vulnerability is what "honest bridging" means.

**Key fact:** A 2021 study found wet bulb temperatures in informal settlements approached the upper limits of human survivability — and these conditions are underestimated by standard monitoring.

**Pre-test:** Draft a narrative paragraph linking SUEWS output (hazard) → population in informal settlement archetype (exposure) → lack of cooling infrastructure (vulnerability) → risk indicator.

**Source:** [Chronic heat stress in tropical urban informal settlements (ResearchGate)](https://www.researchgate.net/publication/356114578_Chronic_heat_stress_in_tropical_urban_informal_settlements); [Low-cost interventions for heat stress mitigation (Nature, 2025)](https://www.nature.com/articles/s44284-025-00370-3)

---

## 8. Wet Bulb Globe Temperature (WBGT) as the Bridge Metric

**Concept:** SUEWS outputs air temperature, humidity, and radiation components. These can be combined to estimate WBGT — the internationally recognised heat stress index used by ISO 7243, military, and sports bodies.

**Why it's strong:** WBGT is "probably the most widely used [heat metric], especially in international contexts" (CarbonPlan). The UNDRR framework references it. Using it shows scientific rigour.

**Thresholds to know:**
- 28°C WBGT: moderate risk, rest breaks needed
- 32°C WBGT: high risk, heavy work should stop
- 35°C wet-bulb: upper limit of human survivability (>6 hours)

**Pre-test:** Write a Python function that estimates simplified WBGT from SUEWS output (T_air, relative humidity, radiation).

**Source:** [UNU — What is Wet-Bulb Temperature](https://unu.edu/ehs/article/what-wet-bulb-temperature-and-why-does-it-matter); [CarbonPlan — Modeling Extreme Heat](https://carbonplan.org/research/extreme-heat-explainer)

---

## 9. The "+2–3°C / Amplified Heatwave" Future Scenario

**Concept:** The template will include a hotter-future forcing variant. This is your climate change scenario. Compare present-day dangerous-heat hours vs future dangerous-heat hours to quantify the *additional* risk.

**Why it's strong:** Showing how risk *changes* under warming is more compelling than a single snapshot. It makes the policy case: "without intervention, dangerous hours increase from X to Y per year."

**Pre-test:** Run the same configuration with forcing temperatures uniformly increased by +2.5°C. Compare output statistics.

**Source:** [PNAS — Lower moist heat stress tolerance thresholds (2023)](https://www.pnas.org/doi/10.1073/pnas.2305427120)

---

## 10. Storytelling Structure for the Pages Site

**Concept:** Structure your GitHub Pages narrative as: Question → Method → Result → Caveats → Recommendation.

**Tips from research:**
- Lead with the human impact ("X thousand people face Y dangerous-heat hours per year")
- Use a single compelling chart above the fold
- Be explicit about what the model *cannot* do — this is what "honest bridging" rewards
- End with a policy-actionable statement

**Pre-test:** Draft the skeleton of `docs/index.md` now with placeholder sections. On the day, just fill in the numbers.

**Source:** [Data storytelling best practices (GitHub repos)](https://github.com/gabriellearruda/storytelling-with-data); [GitHub Pages showcase tips (Unicorn Platform)](https://unicornplatform.com/blog/showcase-your-projects-with-a-github-personal-page/)

---

## 11. Prompt Engineering for the suews-agent

**Concept:** The "Innovation and AI collaboration" criterion scores creative, effective use of the agent. Plan your prompts in advance:
- Start broad: "What archetypes are in this dataset and what are their characteristics?"
- Then specific: "Run a 7-day simulation for archetype X under the heatwave forcing"
- Cross-check: "Compare the sensible heat flux output for archetypes A and B — which is hotter and why?"
- Meta: "What are the limitations of this SUEWS configuration for representing night-time cooling?"

**Why it's strong:** Showing a deliberate prompt strategy in your transcript demonstrates methodology, not just ad-hoc usage.

**Pre-test:** Write 10 prompt templates now, categorised by phase (explore → simulate → analyse → narrate → critique).

**Source:** [Anthropic prompting best practices](https://docs.anthropic.com/en/resources/prompt-library/career-coach); [AI prompt engineering for urban planning (Scribd)](https://www.scribd.com/document/945070893/Prompts-for-Planning-AI-Integration-LLM-Prompt-Design-for-Supporting)

---

## 12. Sensitivity Table: Know What SUEWS Cares About

**Concept:** Before the day, know which parameters have the biggest effect on SUEWS temperature output. Key sensitivity drivers from the literature:

| Parameter | Effect on Peak Temperature | Notes |
|-----------|---------------------------|-------|
| Impervious fraction | ↑↑ strong warming | More paved = more sensible heat |
| Tree canopy fraction | ↓↓ strong cooling | Evapotranspiration + shading |
| Building height / H:W ratio | ↑ moderate (complex) | Traps heat but also provides shade |
| Anthropogenic heat (QF) | ↑ moderate | Waste heat from AC, traffic |
| Albedo | ↓ moderate cooling | Cool roofs / light surfaces |
| Irrigation | ↓ moderate cooling | Evaporative cooling |

**Why it's strong:** This lets you explain *why* archetype A is hotter than B — not just that it is. That's "Scientific soundness."

**Pre-test:** Run sample data with QF doubled, compare temperature delta.

**Source:** [Sensitivity of urban heat predictions (AMS)](https://journals.ametsoc.org/doi/full/10.1175/2007JAMC1598.1); [SUEWS Beijing sensitivity study (GMD)](https://gmd.copernicus.org/preprints/gmd-2022-305/)

---

## Summary: Priority Actions Before Tomorrow

1. **Draft your Pages skeleton** (idea 10) — have the narrative structure ready
2. **Write prompt templates** (idea 11) — 10 prompts across explore/simulate/analyse/narrate/critique
3. **Pre-write the WBGT function** (idea 8) — have the Python snippet ready to paste
4. **Read the UNDRR framework summary** (idea 3) — know the Risk = Hazard × Exposure × Vulnerability framing
5. **Prepare a scenario comparison script** (idea 1) — change one parameter, compare, visualise
6. **Sketch an interactive chart** (idea 4) — confirm Plotly HTML embeds work on your Pages site

These can all be tested tonight using the sample data we already ran successfully.
