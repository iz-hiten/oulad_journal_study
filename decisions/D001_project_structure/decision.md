# D001 — Project structure and tooling

**Date:** 2026-11-05  **Step:** 00 (setup)  **Status:** Accepted

## Context
The project produces several journals on OULAD. Every script, result and decision needs to be traceable.

## Decision
- `code/`: one script per step, named `stepNN_<name>.py`, run from the project root.
- `results/stepNN_<name>/`: every output of that step (report.txt, CSV tables, later plots).
- `decisions/DNNN_<topic>/decision.md`: one folder per decision.
- `data/raw/`: original files, never modified. Cleaned data, if any, goes to `data/processed/`.
- `LOG.md`: chronological log of every action and decision.
- `SUMMARY.md`: current context, key findings and next steps.
- Tooling: Python 3.13.7, numpy 2.4.6, pandas 3.1.1, matplotlib 3.10.1, seaborn 0.13.2 (installed with pip on 2026-11-05).

## Alternatives considered
- One Jupyter notebook: rejected because it is harder to diff and harder to map each result to a step.

## Consequences
Each step can be rerun on its own, and its outputs can be regenerated deterministically.
