# Project Summary — OULAD journal

*Last updated: 2026-11-05 (after Step 01b, literature scan)*

## Goal
Write journal papers that demonstrate important NumPy and Pandas functions on the OULAD dataset, and highlight relationships between its attributes.

## Dataset
**OULAD**: Open University Learning Analytics Dataset (Kuzilek et al., 2017). 7 tables covering 22 module presentations (7 modules, 2013–2014) and 28,785 students. Source and licence: [D002](decisions/D002_data_source/decision.md).

## Folder map
| Path | Contents |
|---|---|
| `data/raw/` | Original OULAD CSVs (never modified) |
| `code/` | One script per step |
| `results/stepNN_*/` | Outputs of each step |
| `decisions/DNNN_*/decision.md` | One record per decision |
| `LOG.md` | Chronological log of everything |

## Steps completed
### Step 01: Overview and data quality of `studentInfo.csv`
Script: `code/step01_overview.py`. Results: `results/step01_overview/`.

- 32,593 enrolments × 12 attributes: 2 numeric, 9 categorical, plus the ID `id_student`.
- No duplicate rows. Each (module, presentation, student) key is unique.
- 28,785 unique students. Some students enrolled in more than one module or presentation.
- **Missing:** only `imd_band`, 1,111 rows (3.41%).
- **Data-quality issue:** the `imd_band` value `10-20` is missing its `%` sign.
- **Numeric:** `num_of_prev_attempts` has median 0 and max 6 (skew 3.81). `studied_credits` has median 60 and max 655 (skew 1.88, so likely outliers).
- **Imbalances:** disability Y = 9.7%; age 55+ = 0.66%; education levels "No Formal quals" and "Post Graduate" ≈ 1% each.
- **Target `final_result`:** Pass 37.9%, Withdrawn 31.2%, Fail 21.6%, Distinction 9.3%. The classes are moderately imbalanced.

### Step 01b: Literature scan and objective refinement
See `literature/literature_review.md` and `decisions/D005_research_objectives/decision.md`.
- Saturated: dropout accuracy benchmarks; papers that add SHAP to a classifier.
- 5 proposed Q1 objectives: P1 leakage audit · P2 assessment design · P3 intersectional fairness · P4 intervention timing · P5 cross-module transfer.
- Our data supports these gaps: 3,808 repeat enrolments (leakage risk), `imd_band` missingness not yet tested as a signal, age 55+ only 0.66% (needs CIs).

**Pending:** the user chooses objective(s) from D005.

## Decisions so far
D001 structure · D002 data source · D003 start with studentInfo · D004 `?` = missing · D005 objectives (PROPOSED) · D006 raw data excluded from Git

Objectives document: `docs/OULAD_Research_Objectives.pdf`. Repository entry point: `README.md`.

## Open questions / next step
**Step 02: Cleaning.** Decisions needed:
1. How to handle the missing `imd_band` values (drop, mark as "Unknown", or impute by region).
2. Fix the `10-20` label to `10-20%`.
3. Whether to treat outliers in `studied_credits`.
4. Converting ordinal attributes (`imd_band`, `age_band`, `highest_education`) to ordered categories so they can be correlated.

**Step 03 onward:** relationships, including correlation, groupby, crosstab, and each attribute vs `final_result`.
