# Sue Grimmond Checklist

> What the SUEWS co-creator would want to see in our submission. These are the things that score "Scientific soundness" from the expert panel.

---

## The Questions She's Asking

### "Why is Jade Gardens (the refuge) the hottest?"

**Answer (physics-based):**
- Low building plan-area fraction (λp = 0.047) and low mean building height (5.2m)
- This gives a small aerodynamic roughness length (z0) via the Macdonald parameterisation
- Weak z0 → weak turbulent mixing → sensible heat stays trapped near the surface
- High paved fraction (59%) dominates OHM storage heat — absorbs shortwave during day, re-radiates at night
- The 11% evergreen tree cover provides some evapotranspiration but cannot overcome the roughness deficit
- Net effect: the "greenest" neighbourhood paradoxically has the weakest convective ventilation

### "Why are the high-rise cores coolest?"

**Answer:**
- High frontal-area index (FAI): Zheng He Towers = 0.39, Mlima Moto = 0.90
- FAI drives z0 via Macdonald → larger roughness → enhanced turbulent transport of QH away from surface
- Tall canyon geometry (H:W ratio) provides self-shading, reducing direct radiation load at street level
- Building fraction (34–44%) displaces paved surfaces that would dominate OHM storage
- More wall area relative to plan area → more longwave emission upward → faster nocturnal cooling

### "What would you change?"

1. **Turn on QF (anthropogenic heat)** — AC waste heat feedback loop; as warming drives AC adoption, QF amplifies outdoor warming. The model supports it (emissions method) but it's off for comparability.

2. **Use SPARTACUS radiation** — multi-layer scheme handles canyon reflections, sky-view factor, wall interactions. Current NARP is simpler. SPARTACUS would better differentiate dense low-rise from dense high-rise.

3. **Add deciduous trees** — current config has 0% deciduous everywhere. Tropical trees are often semi-deciduous in dry season → reduced LAI → reduced evapotranspiration exactly when heat is highest.

4. **Dynamic OHM** — classic OHM uses fixed a1/a2/a3 coefficients. Dynamic OHM adapts to surface moisture state — matters in a humid city with frequent rainfall.

5. **Heterogeneous forcing / coupling** — all grids share one forcing file. In reality, advection between neighbourhoods creates micro-climate differences. WRF-SUEWS coupling would capture that.

6. **Humidity in the hazard metric** — 81% RH at 35°C is far more dangerous than 35°C dry. A WBGT or apparent temperature output would be more physiologically relevant.

---

## What to Hard-Bake Into the Page

- [x] Section explaining **why refuges are hotter than cores** (roughness + OHM physics)
- [x] Name specific parameters: λp, FAI, z0, Macdonald, OHM coefficients
- [x] "What we'd change" section with concrete model improvements
- [x] Reference the physics options available in SUEWS (SPARTACUS, dynamic OHM, QF)
- [x] Show we understand this is NARP + classic OHM, single-layer — and what that implies

---

## Language That Signals Understanding

Use these phrases (Sue will recognise them):

- "Aerodynamic roughness length drives the turbulent transport"
- "OHM storage heat flux dominates the impervious fraction"
- "The Macdonald parameterisation translates λf and building height to z0/zd"
- "NARP calculates net all-wave radiation from observed/forcing components"
- "Single-layer means no vertical stratification within the urban canopy"
- "QF off means population is exposure data, not a model heat source"

---

*Created: 24 June 2026, ~15:20 BST*
