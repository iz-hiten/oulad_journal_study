# OULAD Journal Project

Exploratory and statistical analysis of the **Open University Learning Analytics Dataset (OULAD)**, toward a series of journal papers on online education, student retention and assessment design. The analysis uses Python (NumPy, Pandas, Matplotlib, Seaborn).

Every step, result and decision is recorded so the work is fully traceable and reproducible.

## Start here
| If you want to... | Read |
|---|---|
| Understand the project in 5 minutes | [`SUMMARY.md`](SUMMARY.md): current context, findings and next steps |
| Read the research gaps and objectives (PDF, 10 pages) | [`docs/OULAD_Research_Objectives.pdf`](docs/OULAD_Research_Objectives.pdf): dataset overview, Step 01 findings, **7 research gaps explained (section 5)**, the 5 objectives P1-P5, comparison, recommendation, references |
| See every action in order | [`LOG.md`](LOG.md): chronological log of actions, decisions, findings and issues |
| Know why something was done | [`decisions/`](decisions/): one folder per decision, each with a `decision.md` |
| Check prior work on OULAD | [`literature/literature_review.md`](literature/literature_review.md) |
| Understand the research gaps simply | [`literature/research_gaps_explained.md`](literature/research_gaps_explained.md) |
| See the outputs of a step | [`results/`](results/) |

## Folder structure
```
oulad_journal/
├── README.md              ← you are here
├── SUMMARY.md             ← project context and findings so far
├── LOG.md                 ← chronological record of everything
├── requirements.txt       ← pinned library versions
├── code/                  ← one script per step (stepNN_name.py)
├── results/stepNN_name/   ← outputs of each step (reports, tables, plots)
├── decisions/DNNN_topic/  ← decision.md for every decision
├── literature/            ← literature scan of prior OULAD studies
├── docs/                  ← OULAD_Research_Objectives.pdf (gaps + objectives)
└── data/raw/              ← OULAD CSVs (not in Git; downloaded by step00)
```

## Reproduce
From the project root:
```bash
pip install -r requirements.txt
python code/step00_download_data.py     # downloads OULAD (~47 MB zip, ~500 MB extracted)
python code/step01_overview.py          # Step 01: overview and data quality of studentInfo
python code/make_objectives_pdf.py      # rebuilds docs/OULAD_Research_Objectives.pdf (gaps + objectives)
```
Tested with Python 3.13.7 on Windows 11.

## Progress
| Step | Script | Results | Status |
|---|---|---|---|
| 00 Data download | `code/step00_download_data.py` | `data/raw/` | Done |
| 01 Overview of studentInfo | `code/step01_overview.py` | `results/step01_overview/` | Done |
| 01b Literature scan and objectives | `code/make_objectives_pdf.py` | `literature/`, `docs/` | Done (objective choice pending) |
| 02 Cleaning | — | — | Next |

## Decisions
| ID | Decision | Status |
|---|---|---|
| [D001](decisions/D001_project_structure/decision.md) | Project structure and tooling | Accepted |
| [D002](decisions/D002_data_source/decision.md) | Use the UCI mirror as the data source | Accepted |
| [D003](decisions/D003_first_table/decision.md) | Start the analysis with studentInfo.csv | Accepted |
| [D004](decisions/D004_missing_value_marker/decision.md) | Treat "?" as a missing value | Accepted |
| [D005](decisions/D005_research_objectives/decision.md) | Five refined research objectives for Q1 journals | Proposed |
| [D006](decisions/D006_github_data_policy/decision.md) | Keep raw data out of Git; add a download script | Accepted |

## Conventions
- Scripts are run from the project root and write only to `results/stepNN_name/`.
- Raw data in `data/raw/` is never modified.
- Every new decision gets a folder `decisions/DNNN_topic/decision.md` and an entry in `LOG.md`.
- `SUMMARY.md` is updated at the end of each step.

## Dataset and citation
Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data*, 4, 170171. https://doi.org/10.1038/sdata.2017.171. Licence: CC-BY 4.0. Mirror: [UCI ML Repository #349](https://archive.ics.uci.edu/dataset/349).
