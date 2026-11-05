"""
Step 01 - First look and data quality check of OULAD studentInfo.csv

Purpose : understand the shape, types, missing values, duplicates and the
          value distribution of every attribute before any analysis.
Input   : data/raw/studentInfo.csv
Output  : results/step01_overview/  (report.txt + CSV tables)
Run     : python code/step01_overview.py   (from the project root)

Key Pandas / NumPy functions demonstrated:
  pd.read_csv(na_values=...), df.shape, df.dtypes, df.info(), df.head(),
  df.describe(), df.isnull().sum(), df.duplicated(), df.nunique(),
  Series.value_counts(), np.round
"""
from pathlib import Path
import io

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw" / "studentInfo.csv"
OUT = ROOT / "results" / "step01_overview"
OUT.mkdir(parents=True, exist_ok=True)

# OULAD marks missing values with "?" (see decisions/D004)
df = pd.read_csv(RAW, na_values="?")

lines = []
def log(text=""):
    print(text)
    lines.append(str(text))

log("=== STEP 01: OVERVIEW OF studentInfo.csv ===\n")

# 1. Shape and types
log(f"Rows: {df.shape[0]}   Columns: {df.shape[1]}\n")
buf = io.StringIO()
df.info(buf=buf)
log("--- df.info() ---")
log(buf.getvalue())

log("--- First 5 rows ---")
log(df.head().to_string())
log()

# 2. Missing values
missing = pd.DataFrame({
    "missing_count": df.isnull().sum(),
    "missing_pct": np.round(df.isnull().mean() * 100, 2),
})
missing.to_csv(OUT / "missing_values.csv")
log("--- Missing values per column ---")
log(missing.to_string())
log()

# 3. Duplicates
full_dups = df.duplicated().sum()
key_dups = df.duplicated(subset=["code_module", "code_presentation", "id_student"]).sum()
log(f"Fully duplicated rows: {full_dups}")
log(f"Duplicate (module, presentation, student) keys: {key_dups}")
log(f"Unique students: {df['id_student'].nunique()}  "
    f"(rows per student, mean = {len(df) / df['id_student'].nunique():.3f})")
log()

# 4. Numeric summary
num_cols = ["num_of_prev_attempts", "studied_credits"]
num_desc = df[num_cols].describe().T
num_desc["skew"] = df[num_cols].skew()
num_desc.to_csv(OUT / "numeric_summary.csv")
log("--- Numeric attributes: describe() + skew ---")
log(num_desc.round(3).to_string())
log()

# 5. Categorical summary
cat_cols = ["code_module", "code_presentation", "gender", "region",
            "highest_education", "imd_band", "age_band", "disability",
            "final_result"]
cat_desc = df[cat_cols].describe().T
cat_desc.to_csv(OUT / "categorical_summary.csv")
log("--- Categorical attributes: describe() ---")
log(cat_desc.to_string())
log()

# 6. Value counts for each categorical attribute
vc_rows = []
for col in cat_cols:
    vc = df[col].value_counts(dropna=False)
    pct = np.round(vc / len(df) * 100, 2)
    log(f"--- value_counts: {col} ---")
    log(pd.DataFrame({"count": vc, "pct": pct}).to_string())
    log()
    for val, c in vc.items():
        vc_rows.append({"column": col, "value": val, "count": c, "pct": pct[val]})
pd.DataFrame(vc_rows).to_csv(OUT / "value_counts.csv", index=False)

(OUT / "report.txt").write_text("\n".join(lines), encoding="utf-8")
print(f"\nSaved outputs to {OUT}")
