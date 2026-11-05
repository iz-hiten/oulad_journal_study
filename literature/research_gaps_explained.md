# Research gaps explained (plain language)

*Companion to `literature_review.md` and `docs/OULAD_Research_Objectives.pdf`. Written 2026-11-05.*

A **research gap** is a question that matters in the real world and that earlier papers have not answered, have answered badly, or have answered with conflicting results. Each gap below has the same structure: what it means, an example, what has been done, what is missing, and what our data already shows.

---

## Gap 1: Reported accuracy may be inflated by data leakage (objective P1)

**What it means.** *Data leakage* means the model sees information during training that it would not have in real life at prediction time. The model then looks better in the paper than it would be in a real university.

**Two kinds of leakage in OULAD:**
1. **Same student in training and test data.** OULAD has 32,593 rows but only 28,785 students, so 3,808 rows belong to students who appear more than once. A random row split can put Student A's module-1 row in training and module-2 row in test. The model partly *recognises the student* instead of learning general patterns. It is like a teacher grading an exam after seeing the student's previous answer sheet.
2. **Using future information.** A paper claims to predict risk "at week 4", but its features include an assessment score that was only released in week 6. In real life the university would not have that score at week 4. OULAD does not even record when scores were released, which makes this easy to get wrong.

**What has been done.** Recent papers (Information 2025/26; arXiv 2605.25794) show that both problems can raise AUC noticeably and propose safe pipelines.

**What is missing.** Nobody has gone back and measured **how much the well-known published OULAD results are inflated**, or whether the "best model" stays the best once leakage is removed.

**Why it matters.** A university that buys or builds an early-warning system based on an inflated number will trust it too much.

---

## Gap 2: The assessment design itself is not studied (objective P2)

**What it means.** Almost every OULAD paper asks *"Which student will fail or drop out?"* and uses that student's own behaviour (clicks, late submissions, scores). Very few ask *"Does the way a course is assessed push students to drop out?"*

**Example.** Module X has its first tutor-marked assignment (TMA) on day 20, worth 25% of the grade. Module Y starts with a small computer-marked quiz (CMA) worth 0%, and its first TMA comes on day 45. If withdrawals in Module X spike just before day 20, that is evidence about **course design**, not just about weak students.

**Design features OULAD records:** assessment type (TMA / CMA / Exam), weight, due date, and so the number of assessments, the gap between deadlines, and the date of the first assessment.

**What has been done.** A 2026 MDPI *Data* paper uses late-submission ratio and score trends to predict dropout. That is still *student behaviour*.

**What is missing.** Treating **design properties as explanatory factors** across modules, and checking whether coursework (TMA/CMA) predicts exam results equally well in every module.

**Why it matters.** Course designers can change deadlines and weightings far more easily than they can change students' backgrounds. The findings are directly actionable.

---

## Gap 3: Fairness is studied one attribute at a time (objective P3)

**What it means.** A model is "unfair" if it makes more mistakes for one group of students than another. For example, it might miss at-risk disabled students more often than at-risk non-disabled students.

**The single-attribute problem.** Existing OULAD fairness papers check gender, *or* disability, *or* deprivation (IMD) separately. A model can look fair on each attribute alone and still be unfair to a **combination** of them. This is called **intersectionality**.

*Example:* error rates look similar for men vs women and for deprived vs non-deprived students, but the model misses far more at-risk **disabled students from deprived areas over 35**. No single-attribute check would reveal this.

**The conflicting-results problem.** One study (JLA) finds that bias mitigation works; another (Frontiers 2026) finds that adversarial debiasing made the gaps *worse*. They use different metrics, so the results cannot be compared directly.

**The small-group problem.** Our data has only 216 students aged 55+ (0.66%). If their error rate is 30% vs 25% for everyone else, that 5-point gap might be **random noise** from a small sample. Most papers report the number without a **confidence interval**, so readers cannot tell real gaps from noise.

**What is missing.** An intersectional fairness audit that reports uncertainty and only claims the gaps that are statistically reliable.

---

## Gap 4: Missing data may itself be a signal (part of P3)

**What it means.** `imd_band` (a deprivation index of the student's home area) is missing for 1,111 rows (3.41%). Most papers simply **delete those rows** or fill them with the most common value.

**Why that can be wrong.** Data is not always missing by chance. It could be missing because the address could not be matched, because the student lives outside the UK index areas, or because registration was incomplete. If those students **withdraw more often**, then:
- deleting them hides a vulnerable group from the analysis;
- the missingness itself could be a useful warning signal.

**Statistical terms.** *MCAR* means missing completely at random, so deleting is safe. *MAR/MNAR* means missingness is related to other variables or to the outcome, so deleting causes bias. We can test which applies, for example with a chi-square test of "imd missing" vs `final_result`.

**Status.** This is a **hypothesis to test**. We have not yet checked whether the missing rows behave differently. This will be one of the first things done in Step 02.

---

## Gap 5: Accuracy alone is not enough (applies to all objectives)

**Imbalance.** Only 9.3% of rows are Distinction. A model that never predicts Distinction is still "90.7% accurate" on that class. That is why reviewers want **PR-AUC** and **macro-F1**, not just accuracy.

**Calibration.** If a model says "70% risk of withdrawal" for 100 students, about 70 of them should actually withdraw. Many models rank students well but their probabilities are wrong. An advisor deciding whom to call needs probabilities that can be trusted. This is measured with the **Brier score** and calibration plots, which most OULAD papers do not report.

---

## Gap 6: When to intervene, given limited staff (objective P4)

**What it means.** Most papers predict one label at the end of the course (pass / fail / withdraw). A university's real question is different: *"Each week my advisors can call 50 students. Which 50, and from which week is the model good enough to rely on?"*

**The trade-off.**
- Predict in **week 2**: lots of time to help, but less data, so the model is less accurate.
- Predict in **week 10**: more accurate, but many students have already withdrawn.

**What is needed.**
- **Survival analysis**, which asks *when* withdrawal happens (the "hazard" over time), not just *whether* it happens.
- **Precision@k**: of the top k students the model flags, how many are truly at risk?

**What has been done.** A 2026 arXiv survival benchmark exists.

**What is missing.** Linking withdrawal timing to **real advisor capacity**.

**Our data.** 31.2% of enrolments end in withdrawal, and `studentRegistration` records the exact day of unregistration, which is what survival analysis needs.

---

## Gap 7: Models and explanations may not transfer between courses (objective P5)

**What it means.** A model is often trained on old courses and used on a new one. Two questions arise:
1. **Does accuracy hold up?** Test by training on 6 modules and testing on the 7th ("leave-one-module-out"), or training on 2013 and testing on 2014.
2. **Do the explanations hold up?** SHAP tells us *why* a student was flagged, e.g. "low forum activity". In a module built around discussion forums that is a meaningful reason. In a module with no forum it is meaningless. If the top reasons change between modules, advisors get misleading explanations.

**What has been done.** Many papers apply SHAP, but on a single train/test split.

**What is missing.** Peer-reviewed tests of **explanation stability** across unseen modules and presentations. SHAP is also not causal: it shows what the model uses, not what causes withdrawal.

**Our data.** 7 modules of very different sizes (AAA is 2.3% of rows, BBB 24.3%) and 4 presentations, a natural setting for transfer tests. The small AAA module will give unstable estimates, which must be reported.

---

## Summary table
| # | Gap in one sentence | Objective |
|---|---|---|
| 1 | Published accuracy may be inflated because the same student, or future data, leaks into training | P1 |
| 2 | Nobody tests whether assessment design (type, weight, deadlines) drives withdrawal | P2 |
| 3 | Fairness is checked one attribute at a time, with no uncertainty for small groups | P3 |
| 4 | Missing deprivation data may mark a vulnerable group that gets deleted | P3 |
| 5 | Accuracy ignores imbalance and whether risk probabilities can be trusted | All |
| 6 | Models do not say *when* to intervene given limited staff | P4 |
| 7 | Explanations may change when a model is reused on a new course | P5 |
