# D002 — Data source

**Date:** 2026-11-05  **Step:** 00 (setup)  **Status:** Accepted

## Context
OULAD (Open University Learning Analytics Dataset, Kuzilek et al., 2017, *Scientific Data* 4:170171) is published by the Open University and mirrored by the UCI ML Repository (id 349).

## Decision
Use the UCI mirror: https://archive.ics.uci.edu/static/public/349/open+university+learning+analytics+dataset.zip

## Reason
The official link (https://analyse.kmi.open.ac.uk/open_dataset/download) returned a 91 KB HTML page, not the data. The UCI file is a valid 46.7 MB zip containing all 7 CSV tables and `OULAD.names`.

## Consequences
Cite both the original paper and the UCI repository in the journals. The licence is CC-BY 4.0.
