# D004 — Treat "?" as missing

**Date:** 2026-11-05  **Step:** 01  **Status:** Accepted

## Context
The raw CSVs encode missing values as the string `?`, for example in `imd_band`, `date_unregistration` and `vle.week_from`.

## Decision
Load every OULAD table with `pd.read_csv(path, na_values="?")`.

## Reason
Without this, `?` is counted as a real category, so `isnull()` underreports missing data and numeric columns are read as strings.

## Consequences
In studentInfo, `imd_band` shows 1,111 missing values (3.41%). How to handle them is decided in Step 02.
