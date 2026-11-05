# Project Log — OULAD journal

Chronological record of every action and decision. Newest entries at the bottom.
Format: `date | step | type (ACTION / DECISION / FINDING / ISSUE) | description | link`

| Date | Step | Type | Description | Link |
|---|---|---|---|---|
| 2026-11-05 | 00 | ACTION | Installed numpy 2.4.6, pandas 3.1.1, matplotlib 3.10.1, seaborn 0.13.2 on Python 3.13.7 | — |
| 2026-11-05 | 00 | DECISION | Project folder structure: code / results / decisions / data, plus LOG.md and SUMMARY.md | [D001](decisions/D001_project_structure/decision.md) |
| 2026-11-05 | 00 | ISSUE | The official OU download URL returned an HTML page (91 KB) instead of the zip | — |
| 2026-11-05 | 00 | DECISION | Downloaded OULAD from the UCI mirror (46.7 MB zip, 7 CSVs) into data/raw | [D002](decisions/D002_data_source/decision.md) |
| 2026-11-05 | 01 | DECISION | Begin the analysis with studentInfo.csv (holds the target `final_result`) | [D003](decisions/D003_first_table/decision.md) |
| 2026-11-05 | 01 | DECISION | Load the CSVs with `na_values="?"` | [D004](decisions/D004_missing_value_marker/decision.md) |
| 2026-11-05 | 01 | ACTION | Wrote and ran `code/step01_overview.py`; outputs in `results/step01_overview/` | [report](results/step01_overview/report.txt) |
| 2026-11-05 | 01 | FINDING | 32,593 rows × 12 cols; no duplicate rows or keys; 28,785 unique students (some take more than one module) | — |
| 2026-11-05 | 01 | FINDING | Only `imd_band` has missing values: 1,111 (3.41%) | — |
| 2026-11-05 | 01 | FINDING | `imd_band` label inconsistency: `10-20` lacks the `%` that every other band has | — |
| 2026-11-05 | 01 | FINDING | `num_of_prev_attempts` (skew 3.81) and `studied_credits` (skew 1.88, max 655) are right-skewed | — |
| 2026-11-05 | 01 | FINDING | Target `final_result`: Pass 37.9%, Withdrawn 31.2%, Fail 21.6%, Distinction 9.3% | — |
| 2026-11-05 | 01b | ACTION | Brainstormed 16 candidate objectives in 6 themes | — |
| 2026-11-05 | 01b | ACTION | Web literature scan of prior OULAD studies (8 searches) | [review](literature/literature_review.md) |
| 2026-11-05 | 01b | FINDING | Saturated: accuracy benchmarking of dropout models; papers that add SHAP to a classifier | [review](literature/literature_review.md) |
| 2026-11-05 | 01b | FINDING | Gaps: leakage audit, assessment-design effects, intersectional fairness with uncertainty, intervention timing under capacity, cross-module explanation stability | [review](literature/literature_review.md) |
| 2026-11-05 | 01b | DECISION (proposed) | Refined to 5 Q1-oriented objectives; recommend starting with P2 or P3 | [D005](decisions/D005_research_objectives/decision.md) |
| 2026-11-05 | 01b | ACTION | Generated the 8-page objectives PDF with `code/make_objectives_pdf.py` (reportlab 5.1.0) | [PDF](docs/OULAD_Research_Objectives.pdf) |
| 2026-11-05 | 01c | ISSUE | studentVle.csv is 433 MB, over GitHub's 100 MB file limit | — |
| 2026-11-05 | 01c | DECISION | Exclude data/raw from Git; add a download script, requirements.txt and README.md | [D006](decisions/D006_github_data_policy/decision.md) |
| 2026-11-05 | 01c | ACTION | Wrote a plain-language explanation of the 7 research gaps | [gaps](literature/research_gaps_explained.md) |
| 2026-11-05 | 01c | ACTION | Added section 5 "Research gaps explained" to the objectives PDF (v1.1, now 10 pages); README updated | [PDF](docs/OULAD_Research_Objectives.pdf) |
