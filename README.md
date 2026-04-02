# Petri Nets for Trading (Tiny Lab)

A minimal, staged project for learning Petri nets with toy systems first,
then porting the same patterns into trading workflows.

## Milestone 1

- Tiny Petri net core (`Place`, `Transition`, `Marking`, `PetriNet`, `Engine`)
- Text rendering helpers
- Demo notebook: traffic light
- Unit tests including a duplicate-send prevention invariant

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev,notebooks]
pytest
marimo run notebooks/00_traffic_light.py
```

## Why this structure?

The point is to keep each feature small and visible:

1. state in places
2. actions as transitions
3. eligibility from structure
4. firing updates marking

Then grow toward guards, colored tokens, timing, and stochastic behavior.
