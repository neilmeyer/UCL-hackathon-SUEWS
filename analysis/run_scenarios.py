"""
Run three intervention scenarios for the hotspot neighbourhoods (grids 4,5,7,9)
and compare dangerous-heat hours against baseline.

Scenarios:
  A: Trees — increase evetr from 3% to 15% (reduce paved by 12%)
  B: Cool roofs — increase albedo for paved and bldgs from 0.2 to 0.5
  C: Combined — both A and B together
"""
import supy
import yaml
import copy
import numpy as np
import pandas as pd
from pathlib import Path

base = Path(r'c:\Code\SUEWS\UCL-hackathon-SUEWS\data\uda-city-hackathon')
HOTSPOT_GRIDS = [3, 4, 6, 8]  # 0-indexed: Kampong Lama(3), Dhobi Lines(4), Mlima Moto(6), Fuzhou Lanes(8)
THRESHOLD = 35.0
SPINUP_FRAC = 30 / 91  # skip first 30 days

def run_and_extract(config_path):
    """Run simulation and return dangerous-heat hours per grid."""
    sim = supy.SUEWSSimulation(str(config_path))
    sim.run()
    df = sim.output['SUEWS']
    results = {}
    for gridiv in range(1, 11):
        t2 = df.loc[gridiv]['T2']
        spinup = int(len(t2) * SPINUP_FRAC)
        t2_a = t2.iloc[spinup:]
        results[gridiv] = (t2_a > THRESHOLD).sum() / 4.0
    return results

def modify_config(changes_fn, output_name):
    """Load base config, apply changes, save, return path."""
    with open(base / 'uda-city.yml') as f:
        cfg = yaml.safe_load(f)
    changes_fn(cfg)
    out_path = base / output_name
    with open(out_path, 'w') as f:
        yaml.dump(cfg, f, default_flow_style=False, allow_unicode=True)
    return out_path

# --- BASELINE ---
print("Running BASELINE...")
baseline = run_and_extract(base / 'uda-city.yml')
print(f"  Baseline done. Kampong Lama: {baseline[4]:.1f}h, Dhobi Lines: {baseline[5]:.1f}h")

# --- SCENARIO A: TREES ---
def add_trees(cfg):
    """Increase evetr from current to +12%, reduce paved by same amount, in hotspot grids."""
    for idx in HOTSPOT_GRIDS:
        site = cfg['sites'][idx]
        lc = site['properties']['land_cover']
        current_evetr = lc['evetr']['sfr']['value']
        current_paved = lc['paved']['sfr']['value']
        add = 0.12
        lc['evetr']['sfr']['value'] = current_evetr + add
        lc['paved']['sfr']['value'] = current_paved - add

print("\nRunning SCENARIO A (Trees +12% in hotspots)...")
cfg_a = modify_config(add_trees, 'uda-city-scenario-a.yml')
scenario_a = run_and_extract(cfg_a)
cfg_a.unlink()
print(f"  Trees done. Kampong Lama: {scenario_a[4]:.1f}h, Dhobi Lines: {scenario_a[5]:.1f}h")

# --- SCENARIO B: COOL ROOFS ---
def cool_roofs(cfg):
    """Increase albedo for paved and bldgs to 0.5 in hotspot grids."""
    for idx in HOTSPOT_GRIDS:
        site = cfg['sites'][idx]
        lc = site['properties']['land_cover']
        lc['paved']['alb']['value'] = 0.5
        lc['bldgs']['alb']['value'] = 0.5

print("\nRunning SCENARIO B (Cool roofs, albedo 0.5 in hotspots)...")
cfg_b = modify_config(cool_roofs, 'uda-city-scenario-b.yml')
scenario_b = run_and_extract(cfg_b)
cfg_b.unlink()
print(f"  Cool roofs done. Kampong Lama: {scenario_b[4]:.1f}h, Dhobi Lines: {scenario_b[5]:.1f}h")

# --- SCENARIO C: COMBINED ---
def combined(cfg):
    add_trees(cfg)
    cool_roofs(cfg)

print("\nRunning SCENARIO C (Trees + Cool roofs combined)...")
cfg_c = modify_config(combined, 'uda-city-scenario-c.yml')
scenario_c = run_and_extract(cfg_c)
cfg_c.unlink()
print(f"  Combined done. Kampong Lama: {scenario_c[4]:.1f}h, Dhobi Lines: {scenario_c[5]:.1f}h")

# --- RESULTS TABLE ---
names = ['Jade Gardens','Serendib Rise','Taman Melati','Kampong Lama',
         'Dhobi Lines','Lusitano Square','Mlima Moto','Victoria Exchange',
         'Fuzhou Lanes','Zheng He Towers']
types = ['Refuge','Refuge','Refuge','Hotspot','Hotspot','Core','Hotspot','Core','Hotspot','Core']

rows = []
for g in range(1, 11):
    rows.append({
        'gridiv': g,
        'name': names[g-1],
        'type': types[g-1],
        'baseline_hours': round(baseline[g], 1),
        'trees_hours': round(scenario_a[g], 1),
        'cool_roofs_hours': round(scenario_b[g], 1),
        'combined_hours': round(scenario_c[g], 1),
    })

df_out = pd.DataFrame(rows)
df_out['trees_reduction_pct'] = ((df_out['baseline_hours'] - df_out['trees_hours']) / df_out['baseline_hours'].replace(0, np.nan) * 100).fillna(0).round(1)
df_out['cool_roofs_reduction_pct'] = ((df_out['baseline_hours'] - df_out['cool_roofs_hours']) / df_out['baseline_hours'].replace(0, np.nan) * 100).fillna(0).round(1)
df_out['combined_reduction_pct'] = ((df_out['baseline_hours'] - df_out['combined_hours']) / df_out['baseline_hours'].replace(0, np.nan) * 100).fillna(0).round(1)

print("\n=== INTERVENTION SCENARIO RESULTS ===\n")
print(df_out[['name','type','baseline_hours','trees_hours','cool_roofs_hours','combined_hours']].to_string(index=False))

# Save
out_path = Path(r'c:\Code\SUEWS\UCL-hackathon-SUEWS\analysis\intervention_scenarios.csv')
df_out.to_csv(out_path, index=False)
print(f"\nSaved: {out_path}")
