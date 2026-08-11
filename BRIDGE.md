# BRIDGE v2 — after referee audit (2026-08-11, second pass)

*This file replaces BRIDGE v1 (in git history). v1's Theorem S proof contained a
genuine gap (multiplicity vs distinct ordinates), its attainment claims were
unproved, and its no-go corollaries N1–N3 overclaimed what Theorem R implies —
one is refuted below by an explicit countermodel. Every claim now carries
exactly one label:* **PROVED / PROVED-RH (conditional on RH) / PROVED-CERT
(conditional on a repo Arb certificate) / MISSING-LEMMA (plausible, proof
incomplete) / HEURISTIC / NUMERICAL / CONJECTURE / RETRACTED**.

## 0. Audit verdict summary

| v1 claim | v2 status |
|---|---|
| Theorem S: RH ⇒ λ_min(L) > 0 ∀L | **PROVED-RH** after repair (distinct-zeros input added: Farmer 1995) |
| Minimizer exists; λ_min attained; "true minimizer f_L" | **MISSING-LEMMA** (sketch in §4.3); all uses rewritten with ε-minimizers |
| λ_min(L) = E(L) over Paley–Wiener class | **PROVED-RH** only with E defined over the same smooth core (§4.4) |
| Theorem R (slack identities) | **PROVED** (unconditional, elementary) |
| N1: no fixed finite dictionary certifies all C_L | **RETRACTED as consequence; OPEN as question** — countermodel §6.1 shows it does not follow from Theorem R |
| N2: no fixed-precision cap method certifies all C_L | **RETRACTED as stated.** Correct version: Theorem R eliminates fixed nonvanishing slack, not approximation itself (§5.2) |
| N3: only exact arithmetic cap identities can work | **RETRACTED** (interval/asymptotic evaluation with L-dependent precision is not excluded; needs only poly(L) digits if the measured λ_min decay rate is right) |
| N4: the triple (P_T, Π_R, τ_{log 2}) is THE bottleneck | **RETRACTED as "forced"; relabeled: promising research object** |
| μ-metric falsified as bridge mechanism | **PROVED-CERT** (stands; §3) |
| Prime frequencies forced in tight minorants | **MISSING-LEMMA** (the forcing inequality is exact; the nonvanishing input is numerical) |

## 1. The chain (unchanged in substance; labels tightened)

Notation as in v1 §1: V_L^∞, F, ν_f, W_L, Ω_W^{(L)}.

- (K1) [KNOWN] RH ⟺ W(g∗g̃) ≥ 0 for all g ∈ C_c^∞ (Weil/Bombieri/Yoshida).
- (K2) [KNOWN; identity layer machine-checked in this repo] explicit-formula
  identity; under RH the zero side is a nonnegative convergent sum.
- (R1) [PROVED, Lean] RH ⇒ WeilPositivityAll.
- (C_L) [CONJECTURE ∀L > ½log 2] W_L ≥ 0 on V_L^∞; (∀L C_L) ⟺ RH.
- (K4) [CERTIFIED at three windows] λ_min(L) ≤ 8.11e−6 / 6.70e−7 / 3.21e−8 at
  L = 0.64 / 0.68 / 0.72; [NUMERICAL] super-exponential decay rate;
  [KNOWN-cited, unverified here] λ_min(L) → 0 (ζ-cycles mechanism).

The missing bridge: an L-uniform proof mechanism for (C_L). All audited results
below are about what such a mechanism can and cannot look like.

## 2. Equality analysis (rewritten with ε-minimizers)

For any valid certificate (§5) with value v and any unit f with
W_L(f) ≤ λ_min(L) + ε: the minorant slack against ν_f and the weighted cap
slack are each ≤ λ_min(L) + ε − v [PROVED, = Theorem R]. The further inference
"tight minorants must contain the prime frequencies with the von Mangoldt
coefficients" requires a lower bound on |∫cos(r log n) dν_f| along ε-minimizers:
[NUMERICAL at measured windows; MISSING-LEMMA in general]. The limiting
contact-at-zeros picture: [HEURISTIC].

## 3. μ-metric falsification (stands)

[PROVED-CERT] The μ-metric formulation requires G_L ≻ 0 on the constrained
space; Certified Result 5(a) exhibits a unit vector with
vᵀG v = −0.02776113 ± 5.8·10⁻⁹ at L = 0.62; supports and constraints embed
upward, so G_L is non-PSD for every L ≥ 0.62. Hence no G-metric contraction
statement about prime shifts can be the mechanism for the family (C_L); the
μ-inequality concerns only the first window. (Red-teamed in v1 §3; unchanged.)

## 4. Theorem S, repaired

**Theorem S** [PROVED-RH]. Assume RH. For every L > 0,
λ_min(L) := inf{W_L(f) : f ∈ V_L^∞, ‖f‖₂ = 1} > 0.

**Proof.** Suppose not: take f_n ∈ V_L^∞, ‖f_n‖ = 1, W_L(f_n) → 0.

*Step 1 (uniform spectral tails).* Stirling for ψ plus the finite prime sum
give an explicit C_L with Ω_W^{(L)}(r) ≥ ½log(2+r) − C_L =: g(r) for all r ≥ 0.
Since ν_n := ν_{f_n} is a probability measure and ∫g dν_n ≤ W_L(f_n) ≤ 1
(eventually), while g ≥ −C_L everywhere:
ν_n((R, ∞)) ≤ (1 + C_L) / (½log(2+R) − C_L) for all R with positive
denominator — uniformly in n, tending to 0 as R → ∞.

*Step 2 (compactness).* The f_n share the compact support [−L, L] (spatial
tightness) and have uniformly decaying Fourier tails (Step 1). By the
Fréchet–Kolmogorov/Fourier compactness criterion — precisely: R. L. Pego,
*Compactness in L² and the Fourier transform*, Proc. Amer. Math. Soc. 95
(1985), 252–254, Theorem 1: a bounded S ⊂ L²(ℝ) is precompact iff S is
L²-equitight in space and in frequency — a subsequence converges strongly in
L²: f_n → f*, ‖f*‖ = 1, supp f* ⊆ [−L, L] (a.e. limit), and both pole
constraints pass to the limit (inner products against e^{±u/2} ∈ L²[−L, L]).
In particular f* ≠ 0. (f* need not be smooth; it is used only through F*.)

*Step 3 (F* vanishes at every zero ordinate).* F_n → F* uniformly on compact
subsets of ℂ (Cauchy–Schwarz against e^{izu} on [−L, L]). For f_n ∈ C_c^∞ with
the pole constraints, the explicit formula (K2) applies to k_n = f_n ∗ f̃_n
(supp ⊆ [−2L, 2L], so exactly the prime powers n ≤ e^{2L} appear, and the pole
terms vanish since F_n(±i/2) = 0), giving W_L(f_n) = Σ_ρ m_ρ|F_n(γ_ρ)|² under
RH — a convergent sum of nonnegative terms. Hence for each fixed ordinate γ:
m_γ|F_n(γ)|² ≤ W_L(f_n) → 0, so F*(γ) = lim F_n(γ) = 0. Under RH distinct
zeros have distinct real ordinates, so F* vanishes on the set of distinct
ordinates.

*Step 4 (counting, repaired).* F* is entire with |F*(z)| ≤ √(2L)·e^{L|z|} and
F* ≢ 0. If F*(0) ≠ 0 (else divide by z^k, which changes nothing below), Jensen's
formula on the disc |z| ≤ 2T gives for the number n(T) of zeros in |z| ≤ T:
n(T) ≤ [log max_{|z|=2T}|F*| − log|F*(0)|] / log 2 ≤ (2L/log 2)·T + O(1) —
LINEAR in T, self-contained, no Cartwright theory needed.
The distinct ordinates in (0, T] number N_d(T). **v1 gap:** N(T) counts with
multiplicity; N(T)/max-multiplicity gives only a linear lower bound for N_d and
does NOT contradict a linear upper bound for all L. **Repair:** unconditionally
N_d(T) ≥ 0.6395·N(T) (D. W. Farmer, *Counting distinct zeros of the Riemann
zeta-function*, Electron. J. Combin. 2 (1995), R1; alternatively ≥ (5/6 − o(1))·N(T)
by the 2026 Claude paper's Theorem C, or, staying RH-conditional, Montgomery
1973 gives ≥ (2/3)·N(T) simple). Hence
N_d(T) ≫ T log T, which exceeds (2L/log 2)T + O(1) for T large — contradiction. ∎

*Audit notes.* Fourier convention: F(z) = ∫f(u)e^{izu}du, type ≤ L, matching
the Jensen bound as computed; ν_f normalized to a probability measure by
Plancherel (∫_ℝ|F|² = 2π‖f‖²). The proof uses RH twice: reality of ordinates
(Step 3) and, if Montgomery is chosen, the distinct-count (Step 4) — with
Farmer the counting input is unconditional.

### 4.3 Attainment [MISSING-LEMMA]

Existence of a minimizer (in the L²-closure V̄_L, with
W_L(f*) = λ_min(L)) is *plausible* via: (a) the Step-1/2 compactness applied to
a genuine minimizing sequence; (b) lower semicontinuity of the form (split
Ω_W = Ω⁺ − Ω⁻, Ω⁻ bounded with compact support: dominated convergence on the
compact part, Fatou on the rest); (c) density of V_L^∞ in V̄_L in form topology
via dilation f(·/λ), mollification at scale < (1−λ)L, and re-projection of the
two pole constraints against fixed smooth dual vectors. Steps (a), (b) are
complete; (c) is routine but has two unwritten details (form-continuity of the
constraint re-projection; domination for the dilation limit). Until (c) is
written, no statement in this file uses an attained minimizer: everything is
phrased with ε-minimizers, for which Theorem R is already exact.

### 4.4 The envelope identity, correctly scoped

[PROVED-RH] λ_min(L) = inf{Σ_γ m_γ|F_f(γ)|² : f ∈ V_L^∞, ‖f‖ = 1} — the same
smooth core on both sides; this is the explicit formula read as an identity of
infima. Extending the right side to all of PW_L is MISSING-LEMMA (needs §4.3(c)
plus lower semicontinuity of the zero-side sum). The super-exponential decay of
this quantity remains NUMERICAL.

## 5. Theorem R and what it actually implies

**Theorem R** [PROVED, unconditional]. Fix L. Let (σ_j, Λ_j)_{j≤m} be bounded
measurable functions with valid caps (∫σ_j dν_f ≤ Λ_j for every unit
f ∈ V_L^∞), y_j ≥ 0, c ∈ ℝ with c − Σy_jσ_j ≤ Ω_W^{(L)} pointwise on [0, ∞),
v := c − Σy_jΛ_j. Then W_L ≥ v on the unit sphere, and for every unit f with
W_L(f) ≤ λ_min(L) + ε:
(i) 0 ≤ ∫(Ω_W^{(L)} − c + Σy_jσ_j) dν_f ≤ λ_min(L) + ε − v;
(ii) 0 ≤ Σ_j y_j(Λ_j − ∫σ_j dν_f) ≤ λ_min(L) + ε − v.
Proof: expand W_L(f) as the sum of the two bracketed nonnegative quantities
plus v. ∎

### 5.1 Consequences that survive audit

- [PROVED] **Necessary tightness**: any certificate with v ≥ 0 has minorant
  slack and weighted cap slack ≤ λ_min(L) against every ε-minimizer.
- [PROVED, trivial] **Fixed-total-slack families fail**: if a family of
  certificates has lim inf_L (total slack against some ε_L-minimizer, ε_L → 0)
  > 0 while λ_min(L) → 0, then v_L < 0 for large L. (Conditional on
  λ_min(L) → 0, i.e. on the cited ζ-cycles input.)
- [DEFINITIONAL, clarifying] **Two separated obstructions.** Certification at
  window L = (I) *dictionary completeness*: the exact-cap LP value
  v_D(L) := sup over feasible (y, c) using true caps must be ≥ 0 — a question
  about contact geometry of the finite family D; PLUS (II) *cap precision*:
  approximate caps Λ̃_j = Λ_j + ε_j certify iff Σ_j y_j ε_j ≤ v_D(L). The
  observed stall at L = 0.45 was an (I)-failure at float level, not a
  (II)-failure. v1 conflated these.

### 5.2 The retraction, stated plainly

**Theorem R eliminates fixed nonvanishing slack, not approximation itself.**
From (II): adaptive-precision certified evaluation with
Σ_j y_j(L) ε_j(L) ≤ v_D(L) is fully compatible with Theorem R. If the measured
decay λ_min(L) ≈ e^{−cL·(60…80)/…} is right, the required precision is
log(1/λ_min(L)) = O(L) DIGITS — polynomial in L. The architecture is therefore
NOT information-theoretically excluded from verifying any single window;
what no finite computation supplies is the ∀L quantifier, and nothing proved
here precludes an analytic, L-uniform cap family either. v1's N2/N3 are
retracted accordingly.

## 6. Countermodels (mandatory audit artifacts)

**6.1 Fixed dictionary, zero slack, λ_L → 0** (kills "N1 follows from R").
State space [0, 1]; achievable measures at stage L: the single ν_L = δ_{b}
with b fixed; cost Ω_L(r) = r − a_L, a_L = b − λ_L, λ_L → 0⁺. Then
λ_min(L) = λ_L → 0. Dictionary: the single fixed σ(r) = −r with the single
fixed EXACT cap Λ = −b. Certificate at stage L: y = 1, c = −a_L (weights may
depend on L): minorant c − yσ = r − a_L = Ω_L, pointwise with equality;
v = c − yΛ = b − a_L = λ_L ≥ 0. A fixed one-element dictionary with a fixed
exact cap certifies every stage with slack identically zero. Conclusion: no
theorem of the R type can rule out fixed finite dictionaries without ADDITIONAL
problem-specific input (cap inexactness, or contact sets not representable in
the dictionary's span).

**6.2 Adaptive precision tracks any decay.** Same toy; cap known only as
Λ̃(L) = −b + ε(L). Certification: v = λ_L − ε(L) ≥ 0 iff ε(L) ≤ λ_L. Nothing
prevents certified interval evaluation of b to accuracy λ_L; the digit cost is
log(1/λ_L). Arbitrarily fast decay of λ_L raises cost, never impossibility.

**6.3 Dual weights absorb cap error.** Two-element dictionary: σ_a exact,
σ_b with error ε_b. Any certificate with y_b(L) → 0 fast enough has
Σy_jε_j = y_b(L)ε_b → 0 ≤ v_D(L). The correct error functional is Σy_jε_j,
never max_j ε_j — sloppy caps are harmless wherever their dual weight vanishes.

## 7. N-statuses and the corrected bottleneck

| statement | status after audit |
|---|---|
| N1 (no fixed finite dictionary, all L) | **OPEN** — not a consequence of R (§6.1); would need a lower bound on the best-achievable dictionary slack for THIS Ω_W-family |
| N2 (no fixed-precision method) | **FALSE as stated**; true content is §5.1(II)+§5.2 |
| N3 (exact identities necessary) | **RETRACTED** — non-exact alternatives not excluded |
| N4 (the shift triple is THE bottleneck) | **RETRACTED as forced**; remains a promising object |

**Corrected narrowest forced questions** (ranked by logical necessity, per the
corrected chain — every certificate route needs both, and every route of any
kind needs the first):

1. **(Route C) Effective asymptotics for λ_min(L) under RH** — the envelope
   E(L) of §4.4. Every budget in §5.1 is stated relative to λ_min(L); today it
   is known only as three certified upper bounds and a float slope. A proven
   two-sided estimate (under RH; via the Paley–Wiener zero-energy extremal —
   interlacing capacity vs zero density) would convert every "→ 0" above into
   explicit form and would decide whether the poly(L)-digit feasibility claim
   of §5.2 is real. This is a well-posed extremal problem NOT equivalent to RH
   (it presupposes RH), attackable with de Branges/PW space methods.
2. **(Route B/D gate) Dictionary completeness at the stall**: determine whether
   v_D(0.45) ≥ 0 for SOME finite multiplier-cap dictionary with exact caps —
   i.e. whether the stall is a completeness ceiling of the multiplier frame or
   an artifact of the families tried. (Discriminating experiment: §8.G.)
3. **(Route A, contingent) A slack lower-bound theorem** — only worth
   attacking if 2 shows a plateau: prove the analogue of N1 for this Ω_W-family
   by exhibiting contact structure not representable by finitely many bounded
   multipliers (the missing "additional input" of §6.1).
4. (Route E, demoted) Exact spectral theory of (P_T, Π_R, τ_{log 2}):
   promising, not forced.
5. (Route F) Abandoning multiplier caps: premature before 2 is answered.

## 8. Required final report

**A.** Theorem S survives with its original statement, PROVED-RH, with the
repaired proof above (Farmer 1995 distinct-zeros input; self-contained Jensen
counting; Pego compactness).
**B.** Gaps found in v1's proof: (i) multiplicity/distinct-ordinates conflation
(fatal as written for large L; repaired); (ii) attainment claims unproved
(downgraded to MISSING-LEMMA §4.3, all uses rewritten with ε-minimizers);
(iii) E(L) identity mis-scoped (fixed, §4.4); (iv) tail-bound constants
(cosmetic; verified).
**C.** Theorem R survives verbatim, PROVED; of its v1 corollaries only
necessary-tightness and fixed-total-slack-failure survive; the two-obstruction
decomposition is the useful new formulation.
**D.** N1 OPEN; N2 FALSE as stated; N3 RETRACTED; N4 RETRACTED as forced.
**E.** Countermodels §6.1–6.3 (fixed exact dictionary with zero slack;
adaptive precision tracking any decay; dual-weight error absorption).
**F.** Corrected narrowest bottleneck: effective two-sided asymptotics for the
envelope E(L) = λ_min(L) under RH (rank 1), then dictionary completeness at the
stall (rank 2). The shift-triple is demoted to rank 4.
**G.** The discriminating experiment: at L = 0.45, compute v_D with
high-precision (near-exact) caps for a nested sequence of dictionaries chosen
by cutting planes, tracking v_D against the certified bracket for λ_min(0.45).
If v_D ↑ crosses 0: the frame is complete-in-principle and Route D (adaptive
precision) + Route C (envelope asymptotics) carry the program; if v_D plateaus
strictly below 0 across dictionary families: Route A (a real N1-type theorem)
becomes the target, with the plateau data pointing at the non-representable
contact structure. Either outcome is a theorem-shaped fact about the frame.

*Session verdict: v1's no-go was overstated; the audit that found this is the
session's result, per the directive's own success criterion.*
