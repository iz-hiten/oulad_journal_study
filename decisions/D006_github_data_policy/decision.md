# D006 — Keep raw data out of Git; add a download script

**Date:** 2026-11-05  **Step:** 01c (repository setup)  **Status:** Accepted

## Context
The project will be pushed to GitHub. The extracted OULAD files total about 500 MB, and `studentVle.csv` alone is 433 MB. GitHub rejects files over 100 MB, and committing data that anyone can download publicly bloats the repository.

## Decision
- Exclude `data/raw/` and `data/processed/` via `.gitignore`.
- Add `code/step00_download_data.py`, which downloads the UCI zip, checks that it really is a zip, extracts it and verifies all 7 CSVs.
- Pin library versions in `requirements.txt`.
- Add `README.md` as the entry point to the repository.

## Alternatives considered
- Git LFS: works, but needs extra setup and has storage quotas, and the data is already public.

## Consequences
Anyone who clones the repo runs `pip install -r requirements.txt` and then `python code/step00_download_data.py` to reproduce every result.
