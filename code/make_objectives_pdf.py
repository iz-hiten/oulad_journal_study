"""
Builds docs/OULAD_Research_Objectives.pdf: the five refined, Q1-oriented
research objectives (decision D005) in moderate detail.

Run: python code/make_objectives_pdf.py   (from the project root)
Requires: reportlab
"""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (KeepTogether, PageBreak, Paragraph,
                                SimpleDocTemplate, Spacer, Table, TableStyle)

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "OULAD_Research_Objectives.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)

ACCENT = colors.HexColor("#1F4E79")
LIGHT = colors.HexColor("#E8EEF5")
GREY = colors.HexColor("#555555")

ss = getSampleStyleSheet()
H_TITLE = ParagraphStyle("t", parent=ss["Title"], textColor=ACCENT, fontSize=22, leading=27)
H_SUB = ParagraphStyle("s", parent=ss["Normal"], alignment=TA_CENTER, textColor=GREY, fontSize=10.5)
H1 = ParagraphStyle("h1", parent=ss["Heading1"], textColor=ACCENT, fontSize=15, spaceBefore=6, spaceAfter=6)
H2 = ParagraphStyle("h2", parent=ss["Heading3"], textColor=ACCENT, fontSize=11, spaceBefore=7, spaceAfter=2)
BODY = ParagraphStyle("b", parent=ss["BodyText"], fontSize=9.6, leading=13.2)
BUL = ParagraphStyle("bl", parent=BODY, leftIndent=12, bulletIndent=2)
CELL = ParagraphStyle("c", parent=BODY, fontSize=8.6, leading=11)
CELLB = ParagraphStyle("cb", parent=CELL, fontName="Helvetica-Bold")
SMALL = ParagraphStyle("sm", parent=BODY, fontSize=8.2, leading=10.5, textColor=GREY)


def p(text, style=BODY):
    return Paragraph(text, style)


def bullets(items):
    return [Paragraph(i, BUL, bulletText="•") for i in items]


def table(rows, widths, header=True):
    data = [[Paragraph(str(c), CELLB if (header and r == 0) else CELL) for c in row]
            for r, row in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    style = [
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#B0B8C4")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]
    if header:
        style += [("BACKGROUND", (0, 0), (-1, 0), LIGHT)]
    t.setStyle(TableStyle(style))
    return t


def kv_table(pairs):
    rows = [[k, v] for k, v in pairs]
    data = [[Paragraph(k, CELLB), Paragraph(v, CELL)] for k, v in rows]
    t = Table(data, colWidths=[3.6 * cm, 13.4 * cm])
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#B0B8C4")),
        ("BACKGROUND", (0, 0), (0, -1), LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return t


# --------------------------------------------------------------------------
OBJECTIVES = [
    {
        "id": "P1",
        "title": "Leakage-aware re-evaluation of OULAD early-warning models",
        "problem": "Universities deploy early-warning systems trusting published accuracy figures. "
                   "If those figures are inflated by flawed evaluation, institutions over-trust the model "
                   "and misallocate support staff.",
        "gap": "Recent work (Information 17(6):581; arXiv 2605.25794) shows that row-level splits and "
               "post-cutoff assessment features inflate AUC. A regional fairness audit (Sustainability "
               "18:9440) flags the same issue. However, <b>no study systematically quantifies how much "
               "published OULAD results are inflated</b>, or whether model rankings change.",
        "evidence": "32,593 enrolments but only 28,785 unique students, so 3,808 repeat enrolments can "
                    "fall on both sides of a random split.",
        "rqs": [
            "RQ1. How much do AUC / F1 change between a row-level random split and a student-grouped, "
            "time-ordered split?",
            "RQ2. How much of the apparent early-week performance comes from features computed after the "
            "prediction cutoff (e.g. assessment scores released later)?",
            "RQ3. Does the ranking of common models (LR, RF, XGBoost, LSTM) stay the same under leakage-safe "
            "evaluation?",
        ],
        "data": "studentInfo, studentRegistration, studentAssessment, assessments, studentVle, vle",
        "method": "Recreate 3-4 typical published pipelines; evaluate each under (a) a random row split, "
                  "(b) GroupKFold by id_student, (c) a train-on-2013 / test-on-2014 presentation split, and "
                  "(d) strict cutoff-first feature truncation at weeks 2, 4, 8 and 12.",
        "metrics": "ROC-AUC, PR-AUC, macro-F1, Brier score; inflation = metric(leaky) - metric(safe) with "
                   "bootstrap 95% CIs; Kendall's tau for rank stability.",
        "contribution": "A quantified leakage audit and a reusable leakage-safe evaluation protocol for "
                        "OULAD that other researchers can follow.",
        "pandas": "merge, groupby().agg, cutoff filtering with boolean masks, np.random.default_rng for "
                  "reproducible bootstraps.",
        "risk": "Needs the heaviest ML work. Results depend on which published pipelines are chosen, so "
                "the selection must be justified.",
    },
    {
        "id": "P2",
        "title": "Assessment design and student outcomes in online distance education",
        "problem": "Course teams choose assessment types, weights and deadlines with little evidence. "
                   "Poorly spaced or heavily weighted early assessments may push students to withdraw.",
        "gap": "OULAD assessment studies (e.g. MDPI Data 11(11):281, 2026) use student-level submission "
               "behaviour (lateness, score slope) to <b>predict dropout</b>. The <b>design of the assessment "
               "model itself</b> (TMA vs CMA vs exam, weighting, timing, spacing) as an explanatory "
               "factor is largely unstudied.",
        "evidence": "206 assessments across 22 module-presentations, with type (TMA / CMA / Exam), "
                    "weight and due date available for every assessment.",
        "rqs": [
            "RQ1. How do assessment designs differ across modules (number, type mix, weighting, deadline "
            "spacing, date of the first assessment)?",
            "RQ2. Are design features associated with withdrawal and pass rates after controlling for "
            "student demographics and prior attempts?",
            "RQ3. Do coursework scores (TMA, CMA) predict exam performance equally well, and does that "
            "relationship vary by module?",
            "RQ4. Is withdrawal concentrated around specific assessment deadlines?",
        ],
        "data": "assessments, studentAssessment, courses, studentInfo, studentRegistration",
        "method": "Build presentation-level design descriptors; use multilevel (mixed-effects) logistic "
                  "regression with students nested in presentations; deadline-aligned withdrawal "
                  "event plots; correlations between TMA/CMA and exam scores with Fisher z comparisons.",
        "metrics": "Odds ratios with 95% CIs, intraclass correlation (ICC), Spearman rho, effect sizes "
                   "(Cramer's V, Cohen's d).",
        "contribution": "Evidence-based guidance for designing assessment in online courses. Framed by "
                        "assessment-for-learning theory and Tinto's model of student departure.",
        "pandas": "merge, pivot_table, groupby, np.diff for deadline spacing, pd.cut, crosstab, "
                  "corr(method='spearman').",
        "risk": "Only 22 presentations exist at the design level, so the analysis must be framed as "
                "associational and the multilevel structure handled carefully.",
    },
    {
        "id": "P3",
        "title": "Intersectional fairness and informative missingness in at-risk prediction",
        "problem": "Early-warning tools may systematically under-flag or over-flag disadvantaged students. "
                   "Missing socio-economic data may itself mark a vulnerable group that is silently dropped.",
        "gap": "OULAD fairness studies (JLA; Frontiers in Education 2026; JEDM; MDPI Electronics 14:1856) "
               "examine <b>single attributes</b> and reach <b>conflicting conclusions</b> about mitigation. "
               "Intersectional groups, uncertainty for small groups, and whether IMD missingness is "
               "informative remain unstudied.",
        "evidence": "imd_band is 3.41% missing (1,111 rows) and has a label error ('10-20' without '%'); "
                    "age 55+ is only 216 rows (0.66%); disability is 9.7%.",
        "rqs": [
            "RQ1. Is missing imd_band associated with different outcomes (i.e. is it informative, not "
            "missing at random)?",
            "RQ2. Do error rates and calibration of an early-warning model differ across intersections "
            "(IMD x disability x age x education)?",
            "RQ3. Which gaps remain statistically reliable once uncertainty for small groups is accounted for?",
            "RQ4. Does group-aware recalibration reduce the gaps without reducing overall usefulness?",
        ],
        "data": "studentInfo (core), plus early-week VLE and assessment features for the predictive model",
        "method": "Missingness analysis (chi-square, logistic model of missingness); a leakage-safe baseline "
                  "model; subgroup metrics with bootstrap CIs and Bayesian shrinkage for small groups; "
                  "comparison of mitigations (reweighting, group-wise calibration).",
        "metrics": "Equal-opportunity difference, FPR/FNR gaps, calibration error per group, Brier score, "
                   "PR-AUC; 95% CIs throughout.",
        "contribution": "The first intersectional, uncertainty-aware fairness audit of OULAD, and a test of "
                        "whether missing data marks a disadvantaged group.",
        "pandas": "isnull, groupby on multiple keys, crosstab(normalize='index'), value_counts, "
                  "np.percentile for bootstrap CIs.",
        "risk": "Intersections become very small, so the paper must report CIs and avoid over-claiming. "
                "OULAD has no ethnicity attribute.",
    },
    {
        "id": "P4",
        "title": "When to intervene: withdrawal timing and capacity-aware early warning",
        "problem": "Advisors can contact only a limited number of students each week. Institutions need "
                   "to know <b>when</b> withdrawal risk peaks and how early a warning is accurate enough "
                   "to act on.",
        "gap": "Most OULAD models predict a single end-of-course label. Survival benchmarks are emerging "
               "(arXiv 2604.08870), but linking withdrawal timing to <b>intervention capacity</b> "
               "(e.g. the top-k students an advisor can call) is rare.",
        "evidence": "31.2% of enrolments end in withdrawal, the largest outcome problem in the data; "
                    "studentRegistration records the exact unregistration day.",
        "rqs": [
            "RQ1. What does the withdrawal hazard look like over the course weeks, and does it differ by "
            "module and student background?",
            "RQ2. From which week does a calibrated model give useful precision for the top-k flagged "
            "students?",
            "RQ3. How many withdrawals could be reached under realistic advisor capacities?",
        ],
        "data": "studentRegistration, studentInfo, studentVle (weekly aggregates), studentAssessment, courses",
        "method": "Kaplan-Meier curves and Cox / discrete-time hazard models; weekly landmark models with "
                  "cutoff-first features; precision@k and capacity simulation.",
        "metrics": "Concordance index, time-dependent AUC, Brier score, precision@k, recall@k.",
        "contribution": "An operational answer to when and how many: guidance on intervention timing for "
                        "online universities.",
        "pandas": "pd.cut into weeks, groupby + cumsum for weekly engagement, merge_asof-style cutoffs, "
                  "np.where for event indicators.",
        "risk": "Survival analysis needs the lifelines package; withdrawals recorded before the course "
                "starts must be handled consistently.",
    },
    {
        "id": "P5",
        "title": "Cross-module transferability of at-risk predictors and their explanations",
        "problem": "A model trained on one course is often reused for a new course. If its predictors or "
                   "explanations change, advisors receive misleading reasons for flagging a student.",
        "gap": "SHAP is widely applied to OULAD models (i-JET; MDPI Algorithms 18:781), but few "
               "peer-reviewed studies test whether <b>explanations remain stable</b> on unseen modules "
               "or later presentations.",
        "evidence": "7 modules (AAA-GGG) of very different sizes (2.3% to 24.3% of enrolments) and 4 "
                    "presentations, which is a natural setting for transfer tests.",
        "rqs": [
            "RQ1. How much does predictive performance drop with leave-one-module-out and forward-in-time "
            "transfer?",
            "RQ2. Are the top SHAP features and their directions stable across modules?",
            "RQ3. Which features transfer reliably and which are module-specific?",
        ],
        "data": "All tables; VLE activity types from vle",
        "method": "Leave-one-module-out and 2013 to 2014 transfer; SHAP on tree models; rank-stability "
                  "measures across folds.",
        "metrics": "AUC / PR-AUC drop, Kendall's tau and Jaccard top-k overlap of feature rankings, "
                   "sign agreement.",
        "contribution": "Evidence on when an early-warning model, and its explanations, can safely be "
                        "reused across courses.",
        "pandas": "pivot of activity_type clicks, groupby by module, rank(), set operations on top-k lists.",
        "risk": "SHAP explanations are not causal; the smallest module (AAA, 748 rows) gives unstable "
                "estimates.",
    },
]

story = []

# ---- Cover / introduction -------------------------------------------------
story += [
    Spacer(1, 1.2 * cm),
    p("Refined Research Objectives", H_TITLE),
    p("Open University Learning Analytics Dataset (OULAD)", H_SUB),
    p("Five Q1-oriented study proposals, based on a literature scan and first-pass data exploration", H_SUB),
    p("Version 1.0  |  5 November 2026  |  Decision record D005", H_SUB),
    Spacer(1, 0.8 * cm),
    p("1. Purpose", H1),
    p("This document refines an initial list of 16 candidate objectives into five study proposals. "
      "Each one addresses a gap in the existing OULAD literature and can support a stand-alone journal "
      "article. Each objective states the real-world problem, the gap, the evidence already seen in the "
      "data, research questions, data and methods, evaluation metrics, expected contribution and risks."),
    p("2. Dataset at a glance", H1),
    table([
        ["Table", "Rows", "Contents"],
        ["studentInfo", "32,593", "Demographics, prior attempts, credits, final_result (target)"],
        ["studentRegistration", "32,593", "Registration and unregistration day"],
        ["studentAssessment", "173,912", "Submission day, score, banked flag"],
        ["assessments", "206", "Type (TMA / CMA / Exam), due date, weight"],
        ["studentVle", "10,655,280", "Daily clicks per student per VLE resource"],
        ["vle", "6,364", "Resource activity type and planned weeks"],
        ["courses", "22", "Module-presentation length"],
    ], [4 * cm, 2.4 * cm, 10.6 * cm]),
    Spacer(1, 4),
    p("Source: Kuzilek, Hlosta and Zdrahal (2017), <i>Scientific Data</i> 4:170171; CC-BY 4.0; "
      "obtained from the UCI ML Repository (id 349).", SMALL),
    p("3. Key observations from Step 01 (studentInfo)", H1),
]
story += bullets([
    "Outcome distribution: Pass 37.9%, Withdrawn 31.2%, Fail 21.6%, Distinction 9.3%. Withdrawal is "
    "the dominant problem.",
    "28,785 unique students over 32,593 enrolments: 3,808 repeat enrolments (a leakage risk).",
    "Only imd_band has missing values (3.41%); one band label is inconsistent ('10-20').",
    "Small groups: age 55+ (0.66%), no formal qualifications (1.06%), postgraduate (0.96%).",
    "Right-skewed numeric attributes: num_of_prev_attempts (skew 3.81), studied_credits (skew 1.88, max 655).",
])
story += [p("4. What the literature has already covered", H1)]
story += bullets([
    "<b>Saturated:</b> accuracy comparisons of ML / DL dropout models (AUC up to 0.91 reported in 2019); "
    "adding SHAP / LIME explanations to a classifier.",
    "<b>Active but unresolved:</b> fairness (conflicting results), leakage-safe validation, assessment "
    "trajectories, cross-course generalisation.",
    "<b>Implication:</b> a new paper must offer a methodological or substantive insight, not a new "
    "accuracy score.",
])
story.append(PageBreak())

# ---- Objectives -----------------------------------------------------------
for i, o in enumerate(OBJECTIVES):
    block = [p(f"{o['id']}. {o['title']}", H1),
             p("Real-world problem", H2), p(o["problem"]),
             p("Gap in the literature", H2), p(o["gap"]),
             p("Evidence from our data", H2), p(o["evidence"]),
             p("Research questions", H2)]
    block += bullets(o["rqs"])
    block += [Spacer(1, 6), kv_table([
        ("Data tables", o["data"]),
        ("Method", o["method"]),
        ("Metrics", o["metrics"]),
        ("Contribution", o["contribution"]),
        ("Key Pandas / NumPy", o["pandas"]),
        ("Risks / limits", o["risk"]),
    ])]
    story += block
    if i < len(OBJECTIVES) - 1:
        story.append(PageBreak())

story.append(PageBreak())

# ---- Comparison and recommendation ----------------------------------------
story += [
    p("5. Comparison of objectives", H1),
    table([
        ["", "Novelty", "Effort", "ML needed", "Fits Pandas / NumPy focus", "Main tables"],
        ["P1 Leakage audit", "High", "High", "Heavy", "Medium", "All"],
        ["P2 Assessment design", "High", "Medium", "Light", "High", "assessments, studentAssessment"],
        ["P3 Intersectional fairness", "Medium-high", "Medium", "Moderate", "High", "studentInfo (+ early features)"],
        ["P4 Intervention timing", "Medium", "Medium-high", "Moderate", "Medium", "studentRegistration, studentVle"],
        ["P5 Cross-module transfer", "Medium", "High", "Heavy", "Medium", "All"],
    ], [3.8 * cm, 2.1 * cm, 2.1 * cm, 2.0 * cm, 3.2 * cm, 3.8 * cm]),
    p("6. Recommendation", H1),
    p("Start with <b>P2 (assessment design)</b> or <b>P3 (intersectional fairness)</b>. Both are less "
      "crowded, build on data already explored, and suit a statistics-led paper in which Pandas and "
      "NumPy carry most of the analysis. P1 offers the strongest methodological novelty and is a good "
      "second paper once the leakage-safe pipeline exists, because P3, P4 and P5 can reuse it."),
    p("7. Quality requirements for Q1 submission", H1),
]
story += bullets([
    "The contribution is a research finding about education; tool usage belongs in the Methods section.",
    "Theory framing: e.g. Tinto's model of student departure, self-regulated learning, assessment for learning.",
    "Leakage-safe validation: student-grouped and temporal splits; strict prediction cutoffs.",
    "Evaluation beyond accuracy: PR-AUC, calibration (Brier), subgroup metrics, 95% CIs, effect sizes.",
    "Actionable implications for institutions, and an honest limitations section (one UK university, "
    "2013-2014 data, anonymised modules, no ethnicity or motivation data, clicks are proxies for learning).",
    "Reproducibility: public code, fixed random seeds, documented preprocessing.",
])
story += [
    p("Candidate venues (check the current quartile on SCImago / JCR before submitting): Computers &amp; "
      "Education; British Journal of Educational Technology; The Internet and Higher Education; IEEE "
      "Transactions on Learning Technologies; Education and Information Technologies.", BODY),
    p("8. Key references (verify before citing)", H1),
]
refs = [
    "Kuzilek J., Hlosta M., Zdrahal Z. (2017). Open University Learning Analytics dataset. Scientific Data 4:170171.",
    "Jha N.I., Ghergulescu I., Moldovan A.-N. (2019). OULAD MOOC dropout and result prediction using "
    "ensemble, deep learning and regression techniques. CSEDU. doi:10.5220/0007767901540164",
    "Explainable early warnings for dropout through longitudinal assessment trajectories: evidence from "
    "OULAD (2026). Data (MDPI) 11(11):281.",
    "Time-consistent prediction in higher education: a framework for preventing data leakage in "
    "longitudinal models. Information (MDPI) 17(6):581. doi:10.3390/info17060581",
    "When can we trust early warnings? Leakage-excluded early outcome prediction from LMS interaction "
    "logs. arXiv:2605.25794.",
    "A unified survival benchmark for temporal dropout risk prediction in learning analytics. arXiv:2604.08870.",
    "Toward sustainable and equitable AI in education through a regional fairness audit of dropout "
    "prediction using OULAD. Sustainability 18:9440. doi:10.3390/su18189440",
    "Fairness mitigation on OULAD (2026). Frontiers in Education. doi:10.3389/feduc.2026.1841724",
    "Unveiling accuracy-fairness trade-offs: investigating ML models in student performance prediction. "
    "Journal of Learning Analytics.",
    "Investigating demographic features and their connection to performance, predictions and fairness "
    "in EDM models. Journal of Educational Data Mining.",
    "Evaluating fairness strategies in educational data mining. Electronics (MDPI) 14(9):1856.",
    "Early student risk detection using CR-NODE with explainable AI. Algorithms (MDPI) 18(12):781.",
    "Interpretable predictive modeling for educational equity: a workload-aware decision support "
    "system. Big Data and Cognitive Computing 9(11):297. doi:10.3390/bdcc9110297",
    "Predictive modelling with OULAD: a systematic literature review (2024); Alhakbani, Open learning "
    "analytics: a systematic review of benchmark studies using OULAD.",
]
for k, r in enumerate(refs, 1):
    story.append(p(f"[{k}] {r}", SMALL))
story += [Spacer(1, 6), p("Full links are listed in literature/literature_review.md in the project repository.", SMALL)]


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GREY)
    canvas.drawString(2 * cm, 1.2 * cm, "OULAD Research Objectives  |  D005  |  v1.0")
    canvas.drawRightString(A4[0] - 2 * cm, 1.2 * cm, f"Page {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm,
                        topMargin=1.8 * cm, bottomMargin=2 * cm,
                        title="OULAD Refined Research Objectives", author="OULAD journal project")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(f"Saved {OUT}")
