# Cheat Sheet — What You Need to Know

> Plain English. No jargon. This is what you'd say if someone asked "tell me about the city."

---

## The City

**UDA-city** is a fictional coastal tropical city — think Colombo, Sri Lanka (that's where the coordinates point). Hot, humid, rapidly growing, lower-income. It rains a lot but has a brutal hot season (April–May) when temperatures hit 33–38°C with 81% humidity. Think of the air as a hot wet blanket that never lifts.

It has **10 named neighbourhoods** in three types:

---

## The Three Types of Neighbourhood

### 🟢 REFUGE (3 neighbourhoods) — the outskirts
**Jade Gardens · Serendib Rise · Taman Melati**

Picture: suburban edge-of-city. Low-rise houses (5–9m), lots of paved roads (57–59%), some trees (11%), patches of grass and water. Not many people — 80/hectare during the day. Think of a quieter residential fringe with gardens and open space.

Paradox: these are the **hottest** by temperature, because the buildings are too short and sparse to create wind flow that moves heat away. Heat just sits.

### 🔴 HOTSPOT (4 neighbourhoods) — the informal settlements
**Kampong Lama · Dhobi Lines · Mlima Moto · Fuzhou Lanes**

Picture: dense, packed, low-rise informal housing. Narrow lanes, metal roofs, almost no trees (3%), mostly paved/bare ground (68–71%). Packed with people — **300–400 per hectare**. These are the slums.

Who lives here:
- 62–65% work outdoors (street vendors, construction, markets)
- Only 6–10% have any air conditioning
- High deprivation (0.80–0.85 on a 0–1 scale)
- Young population: 12–14% are under 5
- Very few elderly (7–8% over 65) — people don't live long enough

These are **highest risk** — not because they're the absolute hottest, but because the people there have no way to escape the heat.

### 🔵 CORE (3 neighbourhoods) — the formal city centre
**Lusitano Square · Victoria Exchange · Zheng He Towers**

Picture: the CBD. Mid-to-high-rise buildings (18–25m), concrete and glass, offices and commerce. Moderate greening (6% trees, some parks). Population 250/ha during the day (workers flood in), drops to 130 at night (they go home).

Who's here:
- 70–78% have AC access
- Only 18–22% work outdoors
- Low deprivation (0.25–0.30)
- Slightly older demographic (13–15% over 65)

These are the **coolest** — tall buildings create wind turbulence that whisks heat away, and provide shade in the streets below. Also **lowest risk** because the people have resources to cope.

---

## What the Numbers Mean (in human terms)

| Metric | What it actually means |
|--------|----------------------|
| Paved fraction (e.g., 71%) | How much of the ground is concrete, asphalt, roads. More = hotter. |
| Building fraction (e.g., 34%) | How much of the ground is covered by buildings. More tall buildings = cooler (counterintuitive). |
| Evergreen tree fraction (e.g., 11%) | Tree cover. More = cooler via shade + evaporation. |
| Building height (e.g., 25.5m) | Taller = more wind turbulence = cooler streets. Also more shade. |
| FAI (frontal area index) | How much "wall" faces the wind. Higher = more drag = more mixing = cooler. |
| Population density (e.g., 400/ha) | How many people per hectare. 400/ha is extremely dense — think narrow lanes, people everywhere. |
| AC access (e.g., 8%) | Fraction of people with air conditioning. 8% = almost nobody can cool down. |
| Outdoor workers (e.g., 62%) | People who HAVE to be outside in the heat. They can't go inside. |
| Deprivation index (e.g., 0.82) | Overall poverty level. 0 = wealthy, 1 = extreme deprivation. |
| Dangerous-heat hours (e.g., 68) | Hours in the hot season where outdoor air exceeds 35°C. At 81% humidity, this is genuinely dangerous to human health. |

---

## The Punchline (what we found)

**The hottest places are NOT the most dangerous places.**

- Jade Gardens hits 38°C — but only 80 people/ha live there, and they have some AC.
- Kampong Lama hits 37.4°C — and 400 people/ha live there with almost zero AC, two-thirds working outside, in metal-roofed housing that amplifies heat further.

**Under +2.5°C warming:**
- Dangerous hours go from ~70 → ~500 in the worst areas
- That's 35% of the hot season continuously above 35°C
- For people with no AC and outdoor jobs, this approaches survivability limits

---

## What to Say If Asked

**"What does SUEWS actually do?"**
> "It calculates how heat moves through a neighbourhood — how much radiation arrives, how much is stored in roads and buildings, how much is carried away by wind, and how much is evaporated by trees. It gives you outdoor air temperature at 2 metres height for each neighbourhood, every 15 minutes."

**"Why did you use a risk bridge?"**
> "Because temperature alone doesn't tell you who's in danger. A hot park with no one in it is hazardous but not risky. A moderately hot slum packed with outdoor workers who can't cool down is extremely risky. The bridge combines the physical heat with who's there and how vulnerable they are."

**"What's the geometric mean?"**
> "It's like a multiplication average. If ANY one of the three pillars (hazard, exposure, vulnerability) is near zero, the risk drops — even if the others are high. So a hot empty park gets low risk (exposure ≈ 0). A packed slum with moderate heat gets high risk (all three pillars are high)."

**"What can't the model do?"**
> "It can't see inside buildings. Metal roofs in informal housing amplify heat far beyond what outdoor air shows. It also uses dry-bulb temperature — in 81% humidity, the real physiological danger is much worse than 35°C sounds. And it treats each neighbourhood as one block — it can't see the individual street corner where someone is actually standing."

**"What would make it better?"**
> "Turn on the AC waste heat feedback, use a humidity-aware heat metric, and couple it with indoor temperature modelling for informal housing. Those three changes would bring the model closer to what people actually experience."

---

## The One Sentence You Need

> "The hottest neighbourhood in UDA-city is a sparsely populated refuge. The highest-risk neighbourhood is a moderately hot informal settlement where 400 people per hectare live with 8% air conditioning and 62% outdoor jobs — and under 2.5°C of warming, they'll spend a third of the hot season above 35°C with no way to escape."

---

*This is what the whole submission is about. Everything else is evidence for this statement.*
