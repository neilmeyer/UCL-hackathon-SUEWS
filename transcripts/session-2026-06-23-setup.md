# Hackathon Setup Session — 23 June 2026

## Summary

Practice run of the SUEWS Community Hackathon onboarding workflow using Kiro (AI coding agent).

## Steps Completed

### Step 1: Create repo from template
- Created `neilmeyer/UCL-hackathon-SUEWS` from template `UMEP-dev/suews-hackathon-template`
- Repo is public, cloned locally
- **Status: ✅ Done**

### Step 2: Read TASK_BRIEF.md
- Understood the hackathon task: use SUEWS (via suews-agent) to model urban heat in a heat-vulnerable city, then translate hazard into a socio-economic heat-risk indicator
- Key deliverables: GitHub Pages site, AI transcripts, honest bridging narrative
- Judging: 5 criteria × 20 points = 100 total
- **Status: ✅ Done**

### Step 3: Run SUEWS simulation
- Installed SuPy 2026.6.5 (Python wrapper for SUEWS)
- Loaded built-in sample data (London site)
- Ran 48-timestep simulation successfully
- Output: 48 rows × 1081 columns (energy balance, temperature, water fluxes)
- Note: suews-agent MCP server configured but full install deferred (large git dependency)
- **Status: ✅ Done**

### Step 4: Publish GitHub Pages
- Enabled Pages in repo settings: main branch, /docs folder
- Pages URL: https://neilmeyer.github.io/UCL-hackathon-SUEWS/
- **Status: ✅ Done**

### Step 5: Save transcript and push
- This file is the transcript
- **Status: ✅ Done**

## URLs

- **Repo:** https://github.com/neilmeyer/UCL-hackathon-SUEWS
- **Pages:** https://neilmeyer.github.io/UCL-hackathon-SUEWS/

## Tools Used

- Kiro (AI coding agent in VS Code)
- GitHub CLI (`gh`) v2.93.0
- SuPy 2026.6.5 (SUEWS Python interface)
- Git for Windows

## SUEWS Simulation Output (excerpt)

```
SuPy version: 2026.6.5
Forcing rows: 105408
Simulation period: 2012-01-01 00:05:00 to 2012-01-01 04:00:00
No. of grids: 1
Elapsed: 0.3s
Output shape: (48, 1081)
```
