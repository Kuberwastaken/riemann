# BRIDGE — the exact implication chain, the audit of the μ-metric diagnosis, and two theorems

*2026-08-11, research-mathematician session. Status labels used throughout, and
only these: [KNOWN] = theorem in the literature; [REPO-PROVED] = proved in this
repository (paper proof and/or machine-checked); [CERTIFIED] = rigorous
computer-assisted enclosure in this repository; [NUMERICAL] = float observation;
[HEURISTIC]; [CONJECTURE]; [GOAL]. Per the standing rule, nothing below is
measured in windows, margins, or infrastructure; the deliverables are the two
theorems (§4, §5), the falsification (§3), and the bottleneck statement (§7).*

---

## 1. The chain, stated exactly

Notation. For L > 0 let V_L^∞ = {f ∈ C_c^∞(ℝ, ℝ) : supp f ⊆ [−L, L],
∫f(u)e^{u/2}du = ∫f(u)e^{−u/2}du = 0}. For f ∈ V_L^∞ put F(r) = ∫f(u)e^{iru}du,
ν_f = (1/π)|F(r)|² dr on [0, ∞) (a probability measure when ‖f‖₂ = 1), and

    W_L(f) = ∫ Ω_W^{(L)} dν_f ,
    Ω_W^{(L)}(r) = Re ψ(¼ + ir/2) − log π − Σ_{2 ≤ n ≤ e^{2L}} 2Λ(n) n^{−1/2} cos(r log n).

(K1) [KNOWN — Weil 1952, Bombieri 2000, Yoshida 1992] RH ⟺ W(g∗g̃) ≥ 0 for all
g ∈ C_c^∞. Quantifiers: every g, every support. Constant: none — the statement
is nonnegativity, and by (K4) below it cannot be improved to a uniform positive
lower bound.

(K2) [KNOWN; the identity layer is REPO-PROVED in Lean via EF_lit] For f ∈ V_L^∞,
W_L(f) equals the zero-side sum Σ_ρ m_ρ ĥ_f(γ_ρ) of the explicit formula
(γ_ρ = (ρ−½)/i, complex in general); under RH each term is m_ρ|F(γ_ρ)|² ≥ 0.

(R1) [REPO-PROVED, Lean, sorry-free] RH ⇒ WeilPositivityAll (forward half of K1).

(C_L) [CONJECTURE, one per L > 0] W_L(f) ≥ 0 for all f ∈ V_L^∞.
  - Dependence on L: (∀L C_L) ⟺ RH by (K1) (any compactly supported g lies in
    some window; the two pole constraints implement the quotient by the pole
    directions).
  - Constant behavior — this is the decisive structural fact: by Theorem S (§4)
    the infimum λ_min(L) of W_L on the unit sphere of V_L^∞ is STRICTLY POSITIVE
    for every fixed L under RH, and by (K4) it is NOT bounded below uniformly:
    λ_min(L) → 0, at a super-exponential measured rate. So every C_L individually
    is a positive-margin statement, but the family has margin exactly zero in the
    limit. Any proof mechanism for the family must be exact in the limit.
  - Status by window: C_L holds for L ≤ ½log 2 [KNOWN — Connes–Consani 2020,
    prime-free window]. Pilot LP certificates exist at L = 0.40, 0.42
    [NUMERICAL — float caps; not proofs]. Nothing at any L > ½log 2 is proved.
  - Simplest kill: a certified negative eigenvalue of W_L for any L would
    disprove C_L — and by (K2)+(R1) contrapositive, would disprove RH. (None
    exists; certified positive enclosures exist on finite families.)

(K4) [CERTIFIED upper bounds + KNOWN mechanism] λ_min(L) admits rigorous upper
bounds 8.11·10⁻⁶, 6.70·10⁻⁷, 3.21·10⁻⁸ at L = 0.64, 0.68, 0.72 (this repo, Arb
enclosures), with measured local decay slopes −62 and −76 ± 5 [NUMERICAL]; the
degeneration mechanism (small eigenvalues from growing windows) is the
Connes–Consani ζ-cycles phenomenon [KNOWN-level, per the archive's reading of
CC 2021; not re-derived here].

**The missing bridge is exactly: an L-uniform proof mechanism for the family
(C_L).** Everything else in the chain is either proved or is the target. The
rest of this document audits the candidate mechanisms and proves what can be
proved about them.

---

## 2. Equality-case analysis: what an exact certificate must satisfy

Fix L, and let f_L be a minimizer of W_L on the unit sphere (existence: §4,
step 1). Let m = c − Σ_j y_j σ_j be any valid dual minorant (y_j ≥ 0,
m ≤ Ω_W^{(L)} pointwise, caps Λ_j ≥ sup_{‖f‖=1} ∫σ_j dν_f) with certificate
value v = c − Σ y_j Λ_j. The two-line computation in §5 forces:

  (E1) ∫ (Ω_W^{(L)} − m) dν_{f_L} ≤ λ_min(L) − v;
  (E2) Σ_j y_j (Λ_j − ∫σ_j dν_{f_L}) ≤ λ_min(L) − v.

So a certificate with v ≥ 0 must be tight against the true minimizer's spectral
measure, and must have every active cap saturated by the true minimizer, with
TOTAL error at most λ_min(L) — a quantity that is strictly positive (§4) but
certified-small and shrinking super-exponentially (K4). Consequences derived,
with labels:

- Why the prime frequencies must appear with the von Mangoldt coefficients
  [derived, not dictionary-chosen]: (E1) forces m to track Ω_W^{(L)} on
  supp ν_{f_L} to L¹(ν_{f_L})-error ≤ λ_min(L). The oscillatory content of
  Ω_W^{(L)} on that support is exactly Σ 2Λ(n)n^{−1/2}cos(r log n); a minorant
  missing any in-window frequency log n by coefficient δ pays ≍ δ·∫|cos(r log n)|dν
  unless the minimizer's measure is itself orthogonal to that frequency —
  which it is not (the minimizer's autocorrelation at lag log n is the prime-n
  term of its Weil functional, nonzero throughout the active window)
  [NUMERICAL for the nonvanishing; the forcing inequality is exact]. So the
  coefficients are the explicit-formula weights, the measure is ν_{f_L}, and
  the convergence mode is L¹(ν_{f_L}) with error ≤ λ_min(L) — never pointwise
  (the pointwise sum diverges as L → ∞).
- The limiting dual object [HEURISTIC, supported by the measured node structure
  of minimizers]: as L grows, ν_{f_L} develops nodes at the zeta ordinates
  (repo measurement; under RH this is the equality structure of (K2)), so the
  exact minorant converges to a one-sided approximant of the explicit-formula
  density with contact exactly on the zero set — a Beurling–Selberg-type
  extremal object with arithmetic coefficients. Known constructions of such
  minorants (Carneiro–Littmann–Vaaler school) are RH-conditional. An
  UNCONDITIONAL construction with the required contact set would be a new kind
  of object; nothing in the archive contains one.

---

## 3. Track A audit: the μ-metric diagnosis is FALSIFIED as bridge mechanism

Claim under audit: "the bottleneck is an exact μ-metric inequality for windowed
prime-shift operators," μ(L) = λ_min(G_L^{−1/2} Q₂ G_L^{−1/2}), T1 ⟺ G_L ≻ 0
∧ μ(L) > −1.

Falsification: the formulation requires G_L ≻ 0 (the archimedean form positive
definite on the constrained window space). This FAILS beyond L* ≈ 0.59:
- [CERTIFIED] Certified Result 5(a) of this repository: at L = 0.62 there is an
  explicit unit vector v with vᵀG v = −0.02776113 ± 5.8·10⁻⁹ < 0. The
  archimedean form is rigorously indefinite there; G^{−1/2} does not exist.
- [NUMERICAL] L* = 0.59 ± 0.01 (N-convergence-corrected sweep).

Hence: no statement about G-metric contractions of prime shifts can be the
mechanism for C_L beyond the first prime window, because the metric itself
ceases to exist strictly before the two-prime regime begins. For L > L*,
positivity is created by the prime terms collectively (certified rescue pair,
Result 5(b)) — the mechanism is not a perturbation of an archimedean-definite
form in ANY metric derived from G. The μ-inequality survives only as a
formulation of the single-window statement C_L, L < L*, and even there the
stage-9 experiment shows its naive LP shadow (prime-oscillation rows) does not
close C_{0.45}. Diagnosis replaced by §5's theorem.

Red-team of this audit: could a modified metric (e.g. G + εI, or the full W at
a smaller window) restore a contraction formulation past L*? Any such
formulation is a reparametrization of C_L itself (the form being conjugated is
the object under question); the audit's point stands: there is no PROVEN
positive-definite arithmetic-free anchor beyond L*, so "prime shift small in
the archimedean metric" is not a candidate mechanism for the family.

---

## 4. Theorem S (strict window positivity under RH) — a proof, and what it settles

**Theorem S.** Assume RH. For every L > 0, λ_min(L) := inf{W_L(f) : f ∈ V_L^∞,
‖f‖₂ = 1} > 0.

**Proof.** Suppose λ_min(L) = 0 (the form is bounded below since the negative
part of Ω_W^{(L)} is bounded). Take f_n ∈ V_L^∞, ‖f_n‖ = 1, W_L(f_n) → 0.

(1) No mass escape. Ω_W^{(L)}(r) ≥ ½ log(2 + |r|) − C_L for an explicit
C_L < ∞ (Stirling for ψ plus the finite prime sum). Hence for every R,
∫_{|r|>R} |F_n|² dr ≤ 2π (W_L(f_n) + C_L) / (½ log(2+R) − C_L) once the
denominator is positive: the spectral tails are uniformly small. The f_n are
supported in the fixed compact [−L, L] and bounded in L²; uniform spectral
tail-smallness gives L²-precompactness (Kolmogorov–Riesz / Rellich in the
Fourier picture). Pass to a subsequence: f_n → f* in L²; then ‖f*‖ = 1, f* is
supported in [−L, L], and the two pole constraints pass to the limit. In
particular f* ≠ 0.

(2) The limit's transform vanishes on every zero ordinate. F_n → F* uniformly
on compact subsets of ℂ (transforms of an L²-convergent, uniformly compactly
supported sequence). By (K2) (explicit formula, valid for each f_n ∈ C_c^∞
since supp(f_n ∗ f̃_n) ⊆ [−2L, 2L] admits exactly the prime powers n ≤ e^{2L}),
and by RH (all γ_ρ real, all terms nonnegative): for every zero ordinate γ,
m_γ |F_n(γ)|² ≤ W_L(f_n) → 0, hence F*(γ) = 0. So F* vanishes at every
ordinate of every nontrivial zero.

(3) Counting kills F*. F* is entire of exponential type ≤ L with F*|ℝ ∈ L²
(Paley–Wiener class PW_L), and F* ≢ 0. A nonzero function in PW_L has at most
(L/π + o(1))·T zeros in [0, T] (Cartwright/Levinson density; already a Jensen
estimate suffices for an upper bound of the form (L/π)T + O(log T)). But the
number of zeta ordinates in [0, T] is N(T) = (T/2π) log(T/2πe) + O(log T)
(Riemann–von Mangoldt, unconditional), which exceeds (L/π + 1)T for T large
since log T → ∞. Contradiction. ∎

Red-team (Phase 5 checklist). Extremizing sequences: handled — the proof is
exactly about them; compactness prevents the only escape channel (high
frequency), which the log-growth of Ω penalizes. Hidden L-dependence: C_L and
the type bound depend on L; the conclusion is per-L, and NO uniformity in L is
claimed — indeed (K4) forbids it. Circularity: RH is an explicit hypothesis;
the theorem is about the structure of the target, not progress toward RH.
Finite vs full space: the statement is on all of V_L^∞. Equivalent-restatement
check: Theorem S is strictly weaker than RH (it assumes it) — its role is to
settle the repository's open dichotomy, not to advance the chain.

**What it settles.** FINDINGS Tier 3 left open whether completion-criticality
is exact (λ_min = 0 at completed windows) or positivity below numerical
resolution. Under RH: strictly positive, always. Moreover the argument gives
the exact variational identity λ_min(L) = E(L) := min{Σ_γ m_γ |F(γ)|² :
F ∈ PW_L, ‖f‖ = 1, pole constraints} — the "criticality envelope" (Gap 4's
surviving problem) IS the Paley–Wiener zero-energy extremal problem, and the
measured super-exponential decay is the interlacing-capacity phenomenon in
exact form. [The identity is proved; the decay RATE remains NUMERICAL.]

---

## 5. Theorem R (certificate rigidity) and the no-go corollary

**Theorem R.** Fix L. Let {(σ_j, Λ_j)}_{j≤m} be any finite family with each σ_j
bounded measurable and each cap VALID: ∫σ_j dν_f ≤ Λ_j for every unit f ∈ V_L^∞.
Let y_j ≥ 0 and c ∈ ℝ satisfy c − Σ y_j σ_j ≤ Ω_W^{(L)} pointwise on [0, ∞),
and set v = c − Σ_j y_j Λ_j (the certified lower bound: W_L ≥ v on the unit
sphere). Then for every unit f with W_L(f) ≤ λ_min(L) + ε:

  (i) 0 ≤ ∫(Ω_W^{(L)} − (c − Σ y_j σ_j)) dν_f ≤ λ_min(L) + ε − v;
  (ii) 0 ≤ Σ_j y_j (Λ_j − ∫σ_j dν_f) ≤ λ_min(L) + ε − v.

**Proof.** W_L(f) = ∫Ω_W dν_f = ∫(Ω_W − m)dν_f + c − Σ y_j ∫σ_j dν_f
= ∫(Ω_W − m)dν_f + Σ y_j(Λ_j − ∫σ_j dν_f) + v. Both bracketed quantities are
nonnegative (pointwise minorant; valid caps with y ≥ 0), and their sum is
W_L(f) − v ≤ λ_min(L) + ε − v. ∎

**Corollary (no-go for slack-bearing certificate families).** Suppose RH. Any
family of certificates {D_L} with values v_L ≥ 0 must satisfy: total minorant
slack against the true minimizers, and total cap slack on active rows, both
≤ λ_min(L) — which is > 0 (Theorem S) but ≤ 3.21·10⁻⁸ already at L = 0.72
[CERTIFIED] and decreasing super-exponentially [NUMERICAL]. In particular:

1. No L-independent finite dictionary with L-independent cap values certifies
   the family (its slack is bounded below by a positive constant while the
   allowance → 0).
2. Any certifying family must EVALUATE its active caps to accuracy λ_min(L):
   estimation with any fixed relative precision fails beyond an explicit L.
   Every cap-production method in this repository (trace bounds, Frobenius
   bounds, float eigensolvers, Nyström-certified enclosures at fixed precision)
   carries slack bounded below per-method; each is therefore individually
   eliminated as the engine of an L-uniform proof. This converts the observed
   stall at L ∈ (0.42, 0.45) from an empirical failure into a structural one.
3. What is NOT ruled out — stated precisely, because it is the honest fork:
   caps whose values are produced by EXACT ARITHMETIC IDENTITIES (zero slack by
   construction) rather than by estimation. No such identity for any cap
   containing a prime frequency exists in the archive or, to this session's
   knowledge, in the literature. [Interpretive addendum, labeled HEURISTIC:
   by (E1)–(E2) the exact cap values encode the minimizers' spectral data,
   which encodes the zeros (§2); so "exact arithmetic caps" is a demand that
   arithmetic compute spectral data equivalent to zero locations — the
   Hilbert–Pólya demand in LP coordinates.]

Red-team. The theorem is elementary and unconditional; the corollary's parts
1–2 use Theorem S (RH-conditional) and (K4)-certified smallness — for the
purpose of a no-go against PROVING RH this conditioning is legitimate (if RH is
false the certificates' target is false anyway). Part 3 is where the content
lives and is labeled. Could a certificate avoid the frame by using non-diagonal
information (not of the form ∫σ dν)? Yes in principle — quadratic-form caps
tied to non-multiplier operators fall outside Theorem R's scope; that is Track
C's opening, recorded in §7. The no-go is exactly scoped: it eliminates the
σ-LP/multiplier-cap architecture as an estimation-based route, which is the
architecture this repository built and the one under audit.

---

## 6. Track B consolidation: the exact object, characterized

Assembling §2, §4, §5: the exact certificate at window L is the spectral
decomposition of the constrained operator P_V Ω_W^{(L)}(D) P_V at its bottom;
its dual expression is a minorant touching Ω_W^{(L)} on the minimizer's
spectral support with contact error ≤ λ_min(L); in the L → ∞ limit the contact
set is (under RH, measured) the zero set, and the object is an unconditional
arithmetic construction of a Beurling–Selberg-type minorant interpolating the
explicit-formula density at its own zeros. Every route to such an object in
the literature presupposes the zeros (RH-conditional extremal theory) or
constructs the spectrum directly (Hilbert–Pólya program). The LP/certificate
frame therefore does not sidestep the classical difficulty; it reproduces it
with cleaner bookkeeping. This is the honest content of the observed log p
dual residuals: they are the shadow of the interpolation conditions.

---

## 7. Report

**A. Proved.** Theorem S (strict window positivity + attainment structure under
RH; settles the exact-criticality dichotomy; identifies the criticality
envelope with the PW zero-energy extremal, exactly). Theorem R (certificate
rigidity, unconditional) with its no-go corollary parts 1–2 (conditional
exactly as labeled).

**B. Disproved.** (a) The μ-metric prime-shift inequality as the bridge
mechanism (falsified by the repo's own certified indefiniteness at L = 0.62 —
the metric does not exist where the mechanism is needed). (b) Exact
completion-criticality (under RH; Theorem S). (c) Slack-bearing certificate
families as an L-uniform proof engine (Theorem R corollary 1–2).

**C. Conjectural.** The C_L family for every L > ½log 2 (equivalently RH); the
decay rate of λ_min(L); the node-convergence of minimizer spectra to the zero
set (measured, unproved); the nonexistence of exact arithmetic cap identities
(if provable, it would close the certificate route entirely).

**D. The single narrowest unresolved statement.** Exact joint spectral theory
of the triple (P_T, Π_R, τ_{log 2}) — the window projection, a band projection,
and the single prime shift: produce an exact (closed-form arithmetic, not
estimated) evaluation of the extremal spectral data of one nontrivial
compression mixing τ_{log 2} with band-limiting on a window. This is a
well-posed problem in the harmonic analysis of three non-commuting projections/
shifts; it is manifestly NOT an RH restatement (it concerns one prime, one
window, no zeros).

**E. Why it matters.** By Theorem R, any certificate proof of C_L beyond the
stall REQUIRES caps evaluated to accuracy λ_min(L); by §5.3 only exact
identities can supply them; the minimal such identity involves exactly this
triple. Solving it either revives the certificate architecture with exact
inputs (and its generalization to all τ_{log p} becomes the program), or its
provable intractability upgrades the no-go from "estimation fails" to "the
architecture fails," forcing the spectral-realization routes. Either outcome
moves the chain: it is the fork the whole frame now rests on.

**F. Strongest reason the route may still fail.** The interpretive half of
§5.3: exact arithmetic caps may be equivalent to knowing the zeros — the
shifts τ_{log p} for all p generate (by rational independence of the log p) a
system whose joint spectral data plausibly has no closed form short of the
zeros themselves; in that case every certificate is circular, positivity
cannot be established by any estimation-or-evaluation route, and the only exit
is constructing the spectral realization itself — which is the original
problem, unsolved for 166 years. Nothing in this session reduces that
possibility; Theorem R makes it sharper.
