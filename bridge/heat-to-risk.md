# Heat-to-risk bridge

The reference bridge is in the challenge dataset: `data/uda-city-hackathon/`

- `risk_bridge.py` — the runnable function
- `risk_bridge.md` — how it works, plus caveats
- `socioeconomic.csv` — per-neighbourhood vulnerability proxies

## Summary

Risk = geometric mean of (Hazard, Exposure, Vulnerability), each scaled [0,1]:

```
risk_index = (hazard · exposure · vulnerability) ^ (1/3)
```

- **Hazard**: hours where T2 > 35°C (from SUEWS output)
- **Exposure**: daytime population density (people/ha)
- **Vulnerability**: age fractions, AC access, outdoor workers, deprivation index

Key insight: the **hottest** neighbourhood is not necessarily the **highest-risk** one.

This is a reference, not the answer you must copy. Threshold, weights, and combination rule are your choices to justify.
