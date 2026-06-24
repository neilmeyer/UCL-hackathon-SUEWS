# City dataset

The focus city is **UDA-city** — a synthetic, lower-income, hot-humid city with 10 named neighbourhoods.

Loaded from [UMEP-dev/uda-city-hackathon](https://github.com/UMEP-dev/uda-city-hackathon) into `data/uda-city-hackathon/`.

## Load it

Tell your AI agent:

> Add the challenge city from https://github.com/UMEP-dev/uda-city-hackathon into my data/ folder, then load it and confirm it runs.

Or: `gh repo clone UMEP-dev/uda-city-hackathon` and point the agent at `agent_manifest.yml`.

## Key facts

- Location: 6.93°N, 79.86°E (coastal tropical, Colombo-like)
- 10 neighbourhoods: 3 refuge, 4 hotspot, 3 core
- Forcing: present hot-humid + future +2.5°C
- QF is OFF — population is exposure data, not model heat
- Risk bridge: `risk_bridge.py` (geometric mean of hazard × exposure × vulnerability)
