# GAPS: sharp openings found by cross-reading the archive against our results

> **STATUS UPDATE (same day, 12:48 UTC): Gap 1 is CLOSED — Theorem A
> (`experiments/weil_positivity/PROOF-c0.md`) proves the archimedean form is
> coercive on the prime-free window with certified constant c₀ ≥ 0.349152.
> Proof: monotonicity of Ω (2 lines) + trace-identity bound (3 lines) +
> rearrangement; computational ingredients ball-certified to 30 digits.**

*2026-07-23. Response to the directive: look at the references sharply for gaps —
places where what is proven, what is measured, and what is merely assumed fail to
meet. Each gap below is stated as a precise question, with why it is a genuine gap
(not answered anywhere in the 178-source archive), a concrete attack, and what
closing it buys. Ordered by leverage-per-difficulty.*

---

## Gap 1 — Uniform coercivity of the archimedean form on the CC window
**(the single most consequential unstated theorem)**

Connes–Consani (Selecta 2021) prove W_∞(g∗g̃) ≥ Tr(θ(g)Sθ(g)\*) **≥ 0** on the
ratio-2 window. Their bound is *nonnegativity*; nowhere in their papers — or
anywhere in the archive — is there a statement that the form is **coercive**:
W_∞(g∗g̃) ≥ c₀‖g‖² with c₀ > 0 uniform over the window. Our measurements say the
infimum is c₀ ≈ 0.55 at the window's end — enormous, not marginal.

*Why it's a gap:* everyone (including CC's own ζ-cycles paper) studies where
positivity *degrades*; nobody has extracted the quantitative floor where it is
*robust*. Yet the Sonin-trace lower bound is an explicit trace of a positive
operator built from prolate projections — its infimum over the unit sphere is a
bottom-eigenvalue statement about the Λ=1 prolate cell, i.e. exactly the kind of
quantity prolate spectral theory (Slepian–Pollak, Landau) computes.

*Attack:* bound Tr(θ(g)Sθ(g)\*) below by (lowest relevant prolate eigenvalue)·‖θ(g)‖²
and relate ‖θ(g)‖ to ‖g‖ on the window; all objects explicit in CC 2020 §3–4.

*What it buys:* combined with Gap 2 it yields the first **proven** T1(δ₀) — see
next — and it converts our certified curve from "subspace evidence" into a
perturbation of a proven full-space floor.

## Gap 2 — The δ→0 route: three sub-lemmas, two provable on the spot

For the window L = ½log 2 + δ, partition [−L, L] into core (the CC window) and two
edge strips of width 2δ. Then:

- **(2a) Edge coercivity from bandwidth (provable, elementary):** if f is
  supported in the two strips (total width 4δ), then ∫_{|r|≤R}|F|² ≤ 4δR·‖f‖²
  (Cauchy–Schwarz), so with R = 1/(8δ): the archimedean form satisfies
  G(f) ≥ Ω(R)(1 − ½) − (sup Ω₋)·½ ≥ ½log(1/(16πδ)) − 3 — **edge-supported
  functions are log(1/δ)-coercive**. Explicit, five lines, no obstruction.
- **(2b) Prime bound on edges (proven — Lemma 1 refined):**
  |Q₂(f)| ≤ ½·√2·log2·‖f_edge‖², and Lemma 1″ says only edge mass matters.
- **(2c) Core coercivity = Gap 1** (the only missing piece), plus cross-term
  control via the A−B split: write G = A − B with A = (1/π)∫|F|²Ω₊ (PSD ⇒
  Cauchy–Schwarz applies to its cross terms) and B = (1/π)∫|F|²Ω₋
  (0 ⪯ B ⪯ 5.38·I, frequency-localized to |r| < 2π). The spatial-block failure we
  documented (t1_blocks) used raw G-norms; the A−B split restores Cauchy–Schwarz
  and was not tried — **it evades our own refutation.**

*What it buys:* T1 for small δ fully proven — the first Weil-positivity theorem
with arithmetic content. All the pieces except (2c) exist today in this repo.

## Gap 3 — The untranslated dictionary: Carathéodory–Fejér ⟷ window positivity

CCM 2025 ("Zeta Spectral Triples") guarantee self-adjointness of their operators
D^{(λ,N)} via an *extension of Carathéodory–Fejér theory* — a positivity theorem
for Toeplitz-type data built from the finite Euler product over p ≤ λ², on the
window [λ^{−1}, λ]. Our μ-invariant reformulation (T1 ⟺
‖G^{−1/2}Q₂G^{−1/2}‖ < 1) is *also* a Toeplitz-metric contraction statement on the
same window with the same data. **Nobody — including CCM — has written the
translation between the two.** Precise question: does the CF-extension theorem of
CCM 2025, specialized to λ² < 3, imply a bound on the spectrum of
G^{−1/2}Q₂G^{−1/2}? If yes, T1 may already be a corollary of a published theorem
and no one has noticed; if no, our certified μ data localizes exactly what their
self-adjointness does *not* control — sharp information either way, obtainable by
a careful reading of one section of one paper against one page of ours.

## Gap 4 — A new empirical law: criticality is approached at rate e^{−4γ₁L}

Our frontier data (L = 0.62 → 0.66) shows the completed-window λ_min decaying
exponentially with local log-slope ≈ 55.6–57.7 — and 4γ₁ = 56.54, where
γ₁ = 14.1347 is the **first zeta zero**. Proposed mechanism: the minimizer is a
Paley–Wiener function of exponential type 2L trying to vanish at the zeros; the
unavoidable residual at the first zero costs |F(γ₁)|² ~ e^{−4γ₁L}. Expected
correction at larger L: interlacing capacity (type 2L supports zero density
2L/π, matching zeta's density only up to height ~2πe^{4L}).

*Status:* fit over a short range with a large prefactor — the local slope, not
the asymptotic form, is what is measured; could be coincidence. *Why it matters
if real:* it is a **two-way bridge**: the distance-to-criticality of the Weil
form would be governed by the lowest zero — turning positivity measurements into
statements about zeros and conversely, a quantitative version of
completion-criticality with the first zero as the rate constant. Test:
high-precision λ_min over L ∈ [0.64, 0.80] (in progress: `law_test.py`).

## Gap 5 — The Deninger function-field consistency test (still nobody has run it)

Deninger's dynamical systems now exist as constructions (2018–24) and Morishita
proved they converge with the CC adelic spaces — yet no one has computed the
leafwise cohomology / transverse index of the *constructed* system for a function
field, where Weil's theorem says what the answer must be. One computation either
validates a 25-year program or locates its gap. (Carried over from ATTACK.md §6;
remains open and remains cheap relative to its leverage.)

## Gap 6 — Is the certification frontier exactly L = log 2?

Certificates are possible while λ_min ≳ 10⁻⁶ (our enclosure floor), which fails
just as L → log 2 ≈ 0.693 — the point where BOTH Lemma 1's regime ends (shift
a = log 2 ≥ L fails) AND the first higher prime power n = 4 enters. Three
structural boundaries — Lemma-1 validity, the n = 4 threshold, and practical
certifiability — appear to coincide at one point. Question: is this coincidence,
or does the k = 2 term of p = 2 (the first "repeated orbit") mark a genuine phase
change in the positivity mechanism? The rescue-cascade data (n = 4 *hurting*
λ_min at L = 1.2) hints the repeated-orbit terms play a different role than
primes. No literature touches the k ≥ 2 structure of Weil positivity separately
from the primes — a genuinely unexamined seam.

---

*Meta-note: Gaps 1–3 are avenues to a fully proven T1; Gap 4 is a candidate new
law; Gaps 5–6 are cheap tests with outsized information value. This document is
the direct product of reading the archive's proofs against this session's
measurements — the gaps live precisely where the two meet.*
