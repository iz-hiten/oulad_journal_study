# Literature scan: prior OULAD studies (2026-11-05)

Method: 8 web searches covering dropout prediction, fairness, assessment timing, systematic reviews, XAI/generalisation, clickstream and leakage. These are leads only. **Every paper must be opened and verified (venue, year, numbers) before citing.**

## 1. What is saturated (hard to publish in Q1 without a new angle)
| Theme | Representative work | Note |
|---|---|---|
| Dropout / result prediction, ML vs DL accuracy | Jha et al. 2019 (CSEDU conference, AUC up to 0.91 with GBM, DOI 10.5220/0007767901540164); CNN+LSTM ensemble (ScienceDirect S0045790621002548); comparative LR/SVM/RF/XGBoost studies | Many papers; "model X beats model Y" is no longer novel |
| Systematic reviews | Alhakbani: 19 benchmark studies; 2024 SLR of OULAD predictive modelling (shallow / ensemble / DL) | Gaps they flag: model limitations, feature-selection comparisons, evaluation beyond accuracy |
| SHAP / LIME explanations | Ensemble+SHAP+LIME (PMC13287638); time-window+SHAP (i-JET 62480); CR-NODE (MDPI Algorithms 18(12):781) | SHAP on a classifier is common; explanation *stability* is less studied |

## 2. Active, not saturated
| Theme | Work | Open issue |
|---|---|---|
| Fairness | JLA accuracy-fairness trade-offs (gender, age, disability, IMD); Frontiers in Education 2026 (10.3389/feduc.2026.1841724): adversarial debiasing *widened* gaps; regional audit (Sustainability 18:9440, 10.3390/su18189440); JEDM: demographics alone ≈ baseline; MDPI Electronics 14(9):1856 | Results conflict; metrics are not comparable; intersectional groups rarely studied; small groups (e.g. age 55+) |
| Leakage / validation | Information 17(6):581 (10.3390/info17060581) time-consistent framework; arXiv 2605.25794 leakage-excluded early prediction; arXiv 2604.08870 survival benchmark | Row-level splits put the same student in train and test; assessment info leaks into "early" features; **no formal audit of how much published OULAD results are inflated** |
| Assessment trajectories | MDPI *Data* 11(11):281 (2026): late-submission ratio, score slope, inactivity → withdrawal (OR 1.052 per 0.10 lateness, Brier 0.1068) | Focus is dropout; assessment *design* (TMA vs CMA vs exam, weighting, spacing) as the object of study is thin. OULAD has no grade-release times (arXiv 2605.25794) |
| Cross-course generalisation | BDCC 9(11):297 workload-aware DSS; leave-one-module-out projects (GitHub, not peer-reviewed) | Few peer-reviewed studies test transfer to unseen modules |

## 3. Our own observations that link to gaps (Step 01)
- 32,593 enrolments but 28,785 unique students: 3,808 repeat enrolments, which is a direct leakage risk under row-level splits.
- `imd_band` 3.41% missing, plus a label error (`10-20` without `%`). Most papers drop these rows or ignore them; whether the missingness is informative is untested.
- Imbalance: Distinction 9.3%; age 55+ is only 216 rows (0.66%), so fairness metrics on small groups need confidence intervals.
- Withdrawn is 31.2%, the largest real-world problem in the data.

## 4. Reviewer expectations at Q1 venues
Candidate venues: Computers & Education, British Journal of Educational Technology, Internet and Higher Education, IEEE Transactions on Learning Technologies, Education and Information Technologies. **Check the current quartile on SCImago/JCR before submitting.**

1. The contribution must be a research finding, not a demonstration of tools. NumPy/Pandas go in Methods.
2. Theory framing (e.g. Tinto's student departure model, self-regulated learning, assessment-for-learning).
3. Leakage-safe validation: student-grouped and temporal splits, leave-one-module-out.
4. Evaluation beyond accuracy: calibration (Brier), PR-AUC for imbalance, subgroup metrics, CIs, statistical tests, effect sizes.
5. Actionability: when can an institution intervene, and with what capacity?
6. Reproducibility: public code, fixed seeds, documented preprocessing.

## Sources
- https://www.semanticscholar.org/paper/e12f5b550636107cd10d4dc9089b73b48c793dbb
- https://www.sciencedirect.com/science/article/abs/pii/S0045790621002548
- https://www.mdpi.com/2306-5729/11/11/281
- https://arxiv.org/pdf/2604.08870
- https://arxiv.org/html/2605.25794v1
- https://doi.org/10.3390/info17060581
- https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2026.1841724/full
- https://learning-analytics.info/index.php/JLA/article/download/8543/7911
- https://doi.org/10.3390/su18189440
- https://jedm.educationaldatamining.org/index.php/JEDM/article/download/718/225
- https://www.mdpi.com/2079-9292/14/9/1856
- https://arxiv.org/html/2504.11504
- https://www.researchgate.net/publication/381904274
- https://www.researchgate.net/publication/361234995
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5704676/
- https://doi.org/10.3390/bdcc9110297
- https://www.mdpi.com/1999-4893/18/12/781
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13287638/
