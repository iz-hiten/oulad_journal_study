# D003 — Start with studentInfo.csv

**Date:** 2026-11-05  **Step:** 01  **Status:** Accepted

## Context
OULAD has 7 related tables:

| Table | Rows |
|---|---|
| courses | 22 |
| assessments | 206 |
| vle | 6,364 |
| studentInfo | 32,593 |
| studentRegistration | 32,593 |
| studentAssessment | 173,912 |
| studentVle | 10,655,280 (433 MB) |

## Decision
Analyse `studentInfo.csv` first.

## Reasons
- It holds the target variable `final_result` (Pass / Fail / Withdrawn / Distinction).
- It holds all the demographic attributes (gender, region, education, IMD band, age, disability) plus prior attempts and credits, so it has a mix of categorical and numeric data that is ideal for demonstrating Pandas/NumPy relationship analysis.
- It is small (3.4 MB) and loads instantly.
- The other tables join to it on (`code_module`, `code_presentation`, `id_student`), so it is the hub of the schema.

## Alternatives considered
- `studentVle.csv` (click behaviour): richer, but 10.6M rows and it needs aggregation first. Deferred to a later step.
- Merging all tables up front: more complex. Better done once the base table is understood.
