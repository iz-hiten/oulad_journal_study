# D005 — Refine research objectives for Q1 journals

**Date:** 2026-11-05  **Step:** 01b  **Status:** PROPOSED (waiting for the user's choice)

## Context
The first-draft list of 16 objectives was too broad, and several of them (plain dropout prediction, SHAP on top of a classifier) are saturated in the literature (see `literature/literature_review.md`). Q1 reviewers expect a clear gap, rigorous validation and a real-world contribution.

## Proposed objectives (one paper each)
- **P1. Leakage audit:** How much do common OULAD evaluation practices (row-level split, post-cutoff assessment features) inflate reported performance, and does the model ranking change under student-grouped temporal validation?
- **P2. Assessment design:** Do assessment design properties (TMA vs CMA, weighting, timing, deadline spacing) relate to withdrawal and final results across modules, after controlling for student background?
- **P3. Intersectional fairness:** Are early-warning errors and calibration unequal across *intersections* (IMD × disability × age × education), with uncertainty quantified for small groups? Is IMD missingness informative?
- **P4. Timing of intervention:** Survival analysis of when withdrawal happens, and the earliest week at which a calibrated model is useful under a fixed advisor capacity.
- **P5. Cross-module transfer:** Do at-risk predictors and their SHAP explanations stay stable when a model is applied to an unseen module or a later presentation?

## Recommendation
Start with **P2** or **P3**. They are the least crowded, they use data we already understand, and both work as statistics-led papers that rely heavily on Pandas/NumPy (ML optional). P1 has the strongest novelty but needs heavier ML experiments.

## Consequences
The chosen objective decides which tables we need and what the next steps are. Rejected objectives stay recorded here.
