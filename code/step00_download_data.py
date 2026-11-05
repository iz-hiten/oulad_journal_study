"""
Step 00 - Download and extract OULAD into data/raw/

The raw data (about 500 MB extracted) is NOT stored in Git, because
studentVle.csv alone is 433 MB and GitHub rejects files over 100 MB.
Run this script once after cloning (see decisions/D002 and D006).

Run: python code/step00_download_data.py   (from the project root)
"""
from pathlib import Path
import urllib.request
import zipfile

URL = ("https://archive.ics.uci.edu/static/public/349/"
       "open+university+learning+analytics+dataset.zip")
ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
ZIP = RAW / "anonymisedData.zip"
EXPECTED = ["assessments.csv", "courses.csv", "studentAssessment.csv",
            "studentInfo.csv", "studentRegistration.csv", "studentVle.csv", "vle.csv"]

RAW.mkdir(parents=True, exist_ok=True)

if not ZIP.exists():
    print(f"Downloading {URL} ...")
    urllib.request.urlretrieve(URL, ZIP)

with open(ZIP, "rb") as f:
    if f.read(2) != b"PK":
        ZIP.unlink()
        raise SystemExit("Download is not a zip file (the server may have returned a web page). Retry.")

with zipfile.ZipFile(ZIP) as z:
    z.extractall(RAW)

missing = [f for f in EXPECTED if not (RAW / f).exists()]
if missing:
    raise SystemExit(f"Missing after extraction: {missing}")
for f in EXPECTED:
    print(f"{f:<26}{(RAW / f).stat().st_size / 1e6:8.1f} MB")
print("OULAD ready in", RAW)
