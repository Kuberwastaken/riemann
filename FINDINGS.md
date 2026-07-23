# FINDINGS — an honest ledger of what this project actually produced

*This document is extracted from the repository's own logs, notes, and experiment
writeups ([`logs/LOG.md`](logs/LOG.md), [`experiments/weil_positivity/`](experiments/weil_positivity/),
[`GAPS.md`](GAPS.md), [`LEADS.md`](LEADS.md)). Nothing is added, inflated, or promoted
beyond what those sources claim; every hedge and every self-correction they record is
preserved here. Where the sources disagree with each other, the disagreement is flagged.*

## The one honest headline

**This project did not prove the Riemann Hypothesis, did not come close, and never
claims to.** Its two products are (1) a curated, annotated, synthesized **archive** of
every serious approach to RH (178 primary sources + 6 bibliographies + the
[`BREAKDOWN`](BREAKDOWN.md)/[`ATTACK`](ATTACK.md) analyses), and (2) a small numerical +
computer-assisted **laboratory** around Weil positivity that produced a handful of
genuinely-new-looking but modest results, several proven elementary lemmas, a set of
rigorous *subspace* certificates, some numerical structural observations, and — to its
credit — a few conjectures that its own instruments then killed. The archive's own
verdict on RH's status (from [`BREAKDOWN.md`](BREAKDOWN.md) §1): *"No visible route is
close."*

The tiers below are ordered by strength of claim, strongest first.

---

## Tier 1 — Apparently-new results (with the audit status the logs record)

All novelty claims below are relative to **this repository's own 178-source literature
sweep** (`notes/`, `experiments/weil_positivity/NOTE.md` "Relation to prior work"). None
has been externally refereed. Read "apparently new" as "not found in the collected
literature," not as "confirmed new."

1. **Theorem A — explicit coercivity of the archimedean Weil form on the prime-free
   window.** For real `f` supported in `[-half log2, half log2]` with the two pole
   constraints, `G(f) >= c0 ||f||^2`. Connes-Consani 2020 prove only `>= 0`; Theorem A
   supplies the missing **quantitative floor**. Status: the proof (`PROOF-c0.md`) is
   written in full and is elementary (monotonicity of the digamma kernel + a trace
   identity + a stochastic-dominance rearrangement), independent of the prolate/Sonin
   machinery; its computational ingredients are Arb ball-arithmetic certified.
   - **Discrepancy to flag honestly:** `PROOF-c0.md` states the theorem with `c0 >= 0.37`
     and a float estimate of `0.378`, but the machine-certified value recorded in
     `LOG.md`, `README`, and `GAPS.md` is **`c0 >= 0.349152`** (ball radius 5e-30). The
     rigorous certified figure `0.349152` is the one to trust; the `0.37` in the theorem
     statement was the pre-certification float estimate and is slightly optimistic. Either
     way the bound captures ~63% of the measured sharp value ~ 0.55.

2. **The certified positivity curve (Certified Results 1-4).** Rigorous (Arb verified
   integration + certified Cholesky) coercivity `W(f) >= c||f||^2` of the *full* Weil
   functional on explicit finite-dimensional test-function families:

   | L | primes active | certified c |
   |---|---|---|
   | 0.450 | {2} | 0.072606 |
   | 0.500 | {2} | 0.014842 |
   | 0.545 | {2} | 0.001285 |
   | 0.600 | {2,3} | 0.000076 |

   The L=0.45 point is, per the repo's sweep, the **first rigorous Weil-positivity
   statement with an active prime beyond the Connes-Consani ratio-2 window**, sitting in
   the "cancellative" regime where norm-perturbation arguments provably fail; the L=0.60
   point is the **first rigorous multi-prime** such statement.
   - **Hard limits the logs insist on:** these are statements about explicit
     **14-dimensional families**, *not* about all of `L^2[-L,L]`. They are **not T1**
     (the open target). At L=0.60 the archimedean part alone is still `+0.0112` on that
     family - the certificate proves positivity *surviving* a two-prime deficit that eats
     99.3% of it, not the full-space "primes rescue" inversion.

3. **Certified Result 5 - the rescue phenomenon, machine-verified.** On one rigorously
   assembled 22-dim family at L=0.62 (primes {2,3}): a certified vector with
   `v^T G v = -0.02776113 +/- 5.8e-9 < 0` (archimedean part rigorously indefinite) *and*
   certified `W >= 2.0624e-5 ||f||^2 > 0` (full form rigorously coercive). "Positivity
   created by the prime terms," upgraded from observation to rigorous fact - on that
   family, at the first scale where the mechanism activates.

4. **The mu-invariant reformulation of T1.** Where the archimedean form `G > 0`
   (L < L* ~ 0.59), define `mu(L) = lambda_min(G^{-1/2} Q2 G^{-1/2})`. Then exactly
   **T1 <=> G > 0 and mu(L) > -1** - the one-prime Weil positivity is precisely the
   statement that the prime-2 transfer is a strict contraction in the archimedean metric.
   This is an exact algebraic reformulation (a reframing, not a theorem about RH);
   measured headroom `1+mu` shrinks from 0.69 to 0.008 across the one-prime window.

5. **The certified razor corridor.** At the window `[e^{-0.7}, e^{0.7}]` (primes {2,3,4})
   the full Weil-form infimum is certified `<= 1.187e-7` while RH asserts `>= 0` - a
   certified, per-window quantitative face of "RH is barely true" (the arithmetic-side
   counterpart of de Bruijn-Newman `Lambda = 0`).

---

## Tier 2 — Small concrete contributions (proven, elementary)

- **Lemma 1 (sharp half-factor prime bound).** For `supp f in [-L,L]` and shift `a >= L`,
  `|g(a)| <= half ||f||^2`, hence `||Q2|| <= (log2)/sqrt2 = 0.490129...`. Rigorous
  (disjoint-support Cauchy-Schwarz), **sharp** (dipole extremals), and it reproduces the
  numerically measured deficit saturation to six digits - the two measurements
  cross-certify.
- **Lemma 1'.** General prime-power norm bound `||Q_n|| <= Lambda(n)/sqrt(n)`, giving an
  explicit total-prime-norm constant per window (0.4901 one prime; 1.1244 for {2,3}; ...).
- **Lemma 1''.** The equality case of Lemma 1: extremals are exactly the two-strip
  "dipoles"; only edge mass is exposed to the prime.
- **The prime-threshold anatomy.** Identifying the CC support-ratio-2 threshold as *the
  prime threshold* (ratio 2 = largest prime-free window; ratio 2+delta activates exactly
  one arithmetic term), and the resulting exact core/dipole geometry.
- **Gap 3 resolution (by direct reading of CCM 2025).** There is **no Caratheodory-Fejer
  shortcut** to T1 - CCM's construction is positivity-agnostic by design (their metric is
  shifted by the smallest eigenvalue *whatever its sign*). The dictionary runs the other
  way: the repo's finite-section certificates can rigorously verify the
  sign/simplicity/evenness hypotheses that CCM's Theorem 1.1 *assumes*. A new, unclaimed
  **contribution surface** was identified - but **not executed** (see Tier 4).

---

## Tier 3 — Numerical observations / structural discoveries (NOT certified)

Labeled numerical throughout; resolution ~10^-5 (N=48 basis), validated only against the
explicit-formula identity, not proven.

- **The four-regime map** of Weil positivity as the window `L` grows: prime-free ->
  perturbative -> cancellative -> arithmetic-rescue/criticality, with the boundaries
  located (perturbative ends ~ 0.39; purely-archimedean positivity dies at L* = 0.59 +/-
  0.01). See [`experiments/weil_positivity/RESULTS.md`](experiments/weil_positivity/RESULTS.md).
- **Just-in-time rescue.** Single-prime truncations of the Weil form go indefinite almost
  immediately past their own window; each next prime term arrives "just in time" to
  restore positivity (mu(0.58) = -1.05 for G+Q2 alone, yet G+Q2+Q3 >= 0).
- **Completion-criticality.** Adding the *last* in-window prime power lands `lambda_min`
  at 0 to 5-6 digits at every window tested, while every proper truncation is strictly
  indefinite and term-by-term monotonicity is false (adding n=4 at L=1.2 *lowers*
  `lambda_min`). Consistent either with exact criticality or with positivity below the
  10^-5 resolution floor - the logs do not overclaim which.
- **Minimizers node on the zeros.** Full-form minimizers develop Fourier nodes *at the
  actual zeta zeros* (a node at gamma_1 = 14.13 by L=1.1, interlacing several by L=1.9) -
  the zeta-cycles small-eigenvalue mechanism made visible.

---

## Tier 4 — Unadjudicated items (explicitly labeled as such)

- **Novelty of Theorem A and the certified curve.** Rests entirely on the repository's
  own literature sweep. Not confirmed by external referees or a systematic MathSciNet/
  zbMATH search. Treat as "not found in 178 collected sources," pending adjudication.
- **The contribution surface to CCM 2025 (Lead 2 / Gap 3 inversion).** Identified as
  finishable "in days" but **not done** - no epsilon_N sign/simplicity/evenness
  certificates were produced.
- **Lead 1 - the graded-mode architecture for full-space T1.** A proposed proof
  architecture (dyadic Fourier blocks + certified finite section + explicit high-block
  coercivity + Cotlar-Stein cross-terms) that "survives every refutation of the session"
  and has "no known obstruction." **Unbuilt.** The logs estimate 2-4 weeks of
  constant-chasing for a strong analyst and are explicit that it "is not a route to RH in
  any near horizon."
- **The surviving criticality-envelope problem.** After Gap 4 was refuted (below), what
  remains well-posed is deriving the *shape* of the super-exponential approach to
  criticality from Paley-Wiener extremal theory. Open.
- **Gap 5 - the Deninger function-field consistency test.** Compute the leafwise
  cohomology / transverse index of Deninger's constructed system for a function-field
  base, where Weil's theorem says what the answer must be. **Nobody has run it** - its
  absence from the literature is itself the finding. Open and cheap.

---

## Tier 5 — Rediscoveries, retractions, and self-refutations (with attribution)

The project killed several of its own conjectures with its own instruments; these are
recorded as prominently as the positive results.

- **Gap 4 - the `e^{-4 gamma_1 L}` criticality-rate "law": REFUTED.** The conjecture (the
  first zeta zero gamma_1 = 14.1347 as the rate constant governing how fast the
  completed-window form approaches criticality; 4 gamma_1 = 56.54 matching an early
  measured slope ~ 56) was killed by a high-precision follow-up: certified `lambda_min` at
  L = 0.64/0.68/0.72 give local log-slopes -62.35 and -76 +/- 5, i.e. the decay
  **accelerates** beyond 4 gamma_1 (multi-zero suppression, not single-zero domination).
  The earlier ~56 slope was "a short-baseline coincidence."
- **The second-moment (Tr B^2) test: NEGATIVE.** The two-vector moment ladder refining
  Theorem A saturates at **77% of T1's requirement** (floors 0.378 -> 0.311, all below the
  0.4901 prime bar). Closing T1 by this route needs a genuinely new spectral input
  (certified constrained-prolate data) - "a genuine project beyond this session."
- **The spatial-block criterion (v1): REFUTED numerically**, and then the whole class:
  the elementary edge-coercivity constant is positive only for delta <~ 3e-7, and IMS
  localization costs 1/delta^2 against a log(1/delta) gain. **All spatial-decomposition
  routes to T1 - sharp and smooth - are closed.** T1 must be won globally in the spectral
  variable.
- **Folklore corrections captured in the notes** (attribution preserved): Woit never wrote
  a dedicated Atiyah-2018 blog post (critiques live at Aperiodical/Lipton/Cook/Carroll);
  the 2019 "revived abandoned approach" framing of the Jensen-polynomials work was
  **Emory's press release, not Quanta**; the "revived approach" optimism was rebutted
  decisively by Farmer. (See [`notes/surveys-expository.md`](notes/surveys-expository.md).)
- **Housekeeping self-corrections** in the log: the archimedean-dominance boundary was
  N-convergence-corrected to L* = 0.59 +/- 0.01; three drifted timestamp estimates were
  corrected; the L=0.60 certificate's framing was explicitly walked back from "primes
  rescue" to "positivity surviving a two-prime deficit" once the finite-family caveat was
  noticed.

---

## Attribution — what this all builds on

The proven foundation under every experiment here is other people's: **Weil 1952** (the
positivity criterion), **Connes-Consani 2020** (archimedean positivity on the ratio-2
window, the theorem Theorem A quantifies and the certified curve extends), the
**Connes-Consani-Moscovici 2023/2025** prolate-wave-operator and zeta-spectral-triple
program (the framework the mu-invariant and Gap 3 dictionary sit inside), and
**Odlyzko's** computed zeros (the ground truth that validates the engine). The
repository's contribution is the prime-threshold-resolved anatomy, the sharp constants,
the exact mu reformulation, and the rigorous certificates with active prime terms - all
modest increments on that foundation, and all clearly labeled as such in the sources.
