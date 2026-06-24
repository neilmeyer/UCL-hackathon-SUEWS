# UDA-City Heat Risk Diagnostic

> An outside-in assessment of where urban heat is most dangerous to people — now and under a hotter future.

---

## The Question

Across ten neighbourhoods of UDA-city — a synthetic, hot-humid, low-income tropical city — **where is heat most dangerous to people**, and is that the same as where it is simply hottest?

## The Answer, in One Line

**No.** The hottest neighbourhoods are not the highest-risk ones. The neighbourhoods where people are most at risk are those where moderate heat meets high population density, low adaptive capacity, and high socioeconomic vulnerability.

---

## Heat Hazard: What SUEWS Shows

We ran the SUEWS urban energy balance model (v2026.6.5) on all 10 neighbourhoods under shared hot-humid meteorological forcing (ERA5 2024, April–May analysis window after 30-day spinup). The hazard metric is **dangerous-heat hours**: hours where modelled 2m air temperature (T2) exceeds 35°C.

| Neighbourhood | Type | Peak T2 (°C) | Dangerous Hours (Present) | Dangerous Hours (+2.5°C) |
|---------------|------|:------------:|:-------------------------:|:------------------------:|
| Jade Gardens | Refuge | 38.1 | 75 | 513 |
| Kampong Lama | Hotspot | 37.4 | 68 | 507 |
| Taman Melati | Refuge | 37.7 | 63 | 467 |
| Dhobi Lines | Hotspot | 36.9 | 44 | 424 |
| Fuzhou Lanes | Hotspot | 36.7 | 36 | 395 |
| Serendib Rise | Refuge | 36.8 | 31 | 374 |
| Mlima Moto | Hotspot | 35.6 | 5 | 277 |
| Lusitano Square | Core | 35.3 | 4 | 237 |
| Victoria Exchange | Core | 35.1 | 3 | 218 |
| Zheng He Towers | Core | 34.4 | 0 | 132 |

The "refuge" neighbourhoods (Jade Gardens, Taman Melati) are paradoxically the **hottest** — their low building density means weak turbulent mixing, so near-surface air warms more under strong radiation. The dense high-rise cores (Zheng He Towers) are coolest: tall buildings create roughness that drives convective cooling.

---

## From Hazard to Risk: The Bridge

Following the UNDRR framing, risk is not hazard alone:

```
Risk = f(Hazard × Exposure × Vulnerability)
```

- **Hazard**: dangerous-heat hours from SUEWS (scaled 0–1 across neighbourhoods)
- **Exposure**: daytime population density (people/ha)
- **Vulnerability**: composite of age fractions, AC access, outdoor worker proportion, and deprivation index

Combined as a geometric mean and RAGG-rated:

| Neighbourhood | Type | Hazard | Exposure | Vulnerability | Risk Index | Rating |
|---------------|------|:------:|:--------:|:-------------:|:----------:|:------:|
| **Dhobi Lines** | Hotspot | 0.59 | 1.00 | 0.92 | 🔴 1.00 | Red |
| **Fuzhou Lanes** | Hotspot | 0.48 | 1.00 | 0.97 | 🔴 0.96 | Red |
| Serendib Rise | Refuge | 0.41 | 0.77 | 0.27 | 🟠 0.53 | Amber |
| Mlima Moto | Hotspot | 0.07 | 1.00 | 1.00 | 🟠 0.49 | Amber |
| Lusitano Square | Core | 0.06 | 0.77 | 0.09 | 🟢 0.17 | Green |
| Jade Gardens | Refuge | 1.00 | 0.00 | 0.32 | 🟢 0.14 | Green |
| Zheng He Towers | Core | 0.00 | 0.77 | 0.00 | ⬜ 0.00 | Grey |

**The critical finding**: Dhobi Lines and Fuzhou Lanes rank highest-risk despite being only 4th and 5th hottest. Their combination of high population density (300 people/ha), near-zero AC access (7–10%), 60%+ outdoor workforce, and high deprivation transforms moderate heat into critical risk.

Meanwhile Jade Gardens — the hottest neighbourhood by far — ranks only 7th on risk because few people live there and those who do have moderate adaptive capacity.

---

## The CrunchTest: What +2.5°C Does

Under a +2.5°C pseudo-warming scenario, dangerous-heat hours increase by 5–7× across all neighbourhoods. The key trajectory signal:

- **Mlima Moto** moves from 🟠 Amber to 🔴 **Red** — the only neighbourhood that changes RAGG band
- Every neighbourhood already in Red stays Red
- The refuge neighbourhoods absorb the warming but remain Green (low population protects them)

Under warming, the question shifts from "is anyone exposed?" to "for how long?" — Kampong Lama goes from 68 to 507 dangerous hours, meaning 35% of April–May is above 35°C for a population with 8% AC access.

---

## Where the Bridge Holds

- **Physical hazard differentiation works**: SUEWS correctly produces inter-neighbourhood temperature differences driven by land cover fraction, building roughness, and vegetation cooling — the physics is well-established for this.
- **The ranking is robust to threshold choice**: the relative ordering of neighbourhoods is stable whether you use 33°C, 35°C, or 37°C as the threshold.
- **The UNDRR decomposition is meaningful**: separating hazard from exposure and vulnerability reveals that physical science alone (temperature maps) is insufficient for risk governance.

## Where the Bridge Breaks

- **T2 is outdoor air, not lived experience.** People inside metal-roofed informal housing in Kampong Lama experience temperatures far higher than outdoor T2. The model cannot represent indoor heat amplification.
- **35°C dry-bulb in a city with 81% RH understates danger.** A wet-bulb or apparent-temperature metric would be more physiologically relevant in this humid climate — but SUEWS does not output it directly.
- **Neighbourhood aggregation hides individuals.** A district-mean vulnerability of 0.82 deprivation masks the most exposed people within that district.
- **The future scenario is a stress test, not a projection.** +2.5°C uniformly applied is not how climate change works (it preferentially warms nights, changes precipitation patterns, alters circulation). Treat direction-of-travel, not absolute numbers, as meaningful.
- **Anthropogenic heat is off.** In reality, waste heat from AC and transport would feed back into outdoor temperatures — creating a vicious cycle the model does not capture.
- **The socioeconomic layer is synthetic.** `socioeconomic.csv` carries plausible magnitudes for a low-income tropical city, not survey data for any real place.

---

## What Should Come Next

1. **Indoor heat modelling** — couple SUEWS outdoor T2 with a building energy model to estimate indoor temperatures, especially for informal housing materials.
2. **Humid-heat metrics** — compute WBGT or apparent temperature from SUEWS output (T2 + forcing humidity + radiation components).
3. **Night-time analysis** — dangerous heat that persists overnight (no nocturnal recovery) is more lethal than daytime peaks. This data supports that analysis.
4. **Dynamic QF** — enable anthropogenic heat to capture the AC feedback loop under warming.
5. **Real socioeconomic data** — replace synthetic proxies with census/survey data for any real application.

---

## Interactive Visualisations

<iframe src="sankey_heat_risk.html" width="100%" height="580" frameborder="0"></iframe>

<iframe src="heat_matrix.html" width="100%" height="480" frameborder="0"></iframe>

<iframe src="scenario_comparison.html" width="100%" height="500" frameborder="0"></iframe>

---

## Method

- **Model**: SUEWS v2026.6.5 via SuPy (Python)
- **Configuration**: UDA-city 10-neighbourhood dataset ([UMEP-dev/uda-city-hackathon](https://github.com/UMEP-dev/uda-city-hackathon))
- **Physics**: NARP net radiation + classic OHM storage heat, single-layer, QF off
- **Forcing**: ERA5 reanalysis 2024 (present) + uniform +2.5K (future)
- **Risk bridge**: geometric mean of min-max scaled hazard, exposure, vulnerability
- **AI tools**: Kiro (Claude-based coding agent) for simulation, analysis, and visualisation

## Citations

- Järvi, L., Grimmond, C.S.B. & Christen, A. (2011). The Surface Urban Energy and Water Balance Scheme (SUEWS): Evaluation in Los Angeles and Vancouver. *Journal of Hydrology*, 411(3–4), 219–237. [DOI: 10.1016/j.jhydrol.2011.10.001](https://doi.org/10.1016/j.jhydrol.2011.10.001)
- Ward, H.C., Kotthaus, S., Järvi, L. & Grimmond, C.S.B. (2016). Surface Urban Energy and Water Balance Scheme (SUEWS): Development and evaluation at two UK sites. *Urban Climate*, 18, 1–32. [DOI: 10.1016/j.uclim.2016.05.001](https://doi.org/10.1016/j.uclim.2016.05.001)
- UNDRR (2025). Extreme Heat Risk Governance Framework and Toolkit. United Nations Office for Disaster Risk Reduction.

---

*This assessment is an indicative, model-based estimate of heat risk — not a measurement or forecast. It is a compass, not a certification.*
