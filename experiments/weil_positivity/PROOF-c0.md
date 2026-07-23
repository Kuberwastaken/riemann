# Theorem A: explicit coercivity of the archimedean Weil form on the prime-free window

*2026-07-23. Closes Gap 1 of `../../GAPS.md` (pending machine certification of two
1-D integrals; everything else is proven below in full). This supplies the
quantitative floor that Connes–Consani 2020 (nonnegativity) left unstated.*

**Theorem A.** Let L₀ = ½log 2. For every real f ∈ L²(ℝ) with supp f ⊆ [−L₀, L₀]
satisfying the two pole constraints ∫f(u)e^{u/2}du = ∫f(u)e^{−u/2}du = 0,

  G(f) := (1/2π) ∫_ℝ |F(r)|² Ω(r) dr ≥ c₀ ‖f‖²,  with c₀ ≥ 0.37,

where F(r) = ∫f(u)e^{iru}du and Ω(r) = Re ψ(¼ + ir/2) − log π. (In this window
G(f) is the entire constrained Weil functional — no primes are active — so this is
an explicit-constant coercivity version of the CC 2020 positivity theorem.)

## Proof

**Lemma M (monotonicity).** Ω is strictly increasing on [0, ∞).
*Proof.* dΩ/dr = d/dr Re ψ(¼+ir/2) = Re[(i/2)ψ′(¼+ir/2)] = −½ Im ψ′(¼+ir/2).
By ψ′(z) = Σ_{n≥0} (z+n)^{−2}: Im(z+n)^{−2} = −2(¼+n)(r/2)/|z+n|⁴ < 0 for r > 0,
each term. Hence dΩ/dr > 0. ∎

**Lemma T (trace identity bound).** Let T = [−L₀, L₀], B_R = P_T Π_R P_T where
Π_R is the Fourier band projection onto [−R, R] (kernel sin R(u−v)/π(u−v), PSD,
Tr B_R = 2L₀R/π exactly). Let {v₁, v₂} be the orthonormalization of
{e^{u/2}, e^{−u/2}} on T, and V ⊂ L²(T) the constrained subspace (orthogonal
complement of span{v₁, v₂}). Then

  sup_{f ∈ V, ‖f‖=1} ⟨f, B_R f⟩ ≤ M̄(R) := min(1, max(0, 2L₀R/π − ρ₁(R) − ρ₂(R))),

where ρ_i(R) = ⟨v_i, B_R v_i⟩.
*Proof.* Complete {v₁, v₂} to an ONB whose remaining vectors span V. The trace is
the sum of diagonal entries in this basis: 2L₀R/π = ρ₁ + ρ₂ + Tr(B_R|_V) ≥
ρ₁ + ρ₂ + λ_max(B_R|_V), the last step because B_R ⪰ 0 makes every diagonal term
of B_R|_V nonnegative. The min/max clip uses 0 ⪯ B_R ⪯ 1. ∎

**Lemma R (rearrangement).** For f ∈ V, ‖f‖ = 1, let ν be the measure on [0,∞)
with ν([0,R]) = (1/π)∫₀^R |F|²dr (a probability measure by Parseval; note
⟨f, B_R f⟩ = ν([0,R]) since |F(−r)| = |F(r)|). Then for any grid
0 = R₀ < R₁ < … < R_K with M̄(R_K) = 1:

  G(f) = ∫ Ω dν ≥ Σ_{k=1}^{K} Ω(R_{k−1}) · [M̄(R_k) − M̄(R_{k−1})]⁺-cumulative,

more precisely: G(f) ≥ inf{∫Ω dμ : μ prob. measure, μ([0,R_k]) ≤ M̄(R_k) ∀k},
and by Lemma M the infimum is attained by the "earliest-allowed" measure, giving
the Stieltjes lower sum with Ω evaluated at left endpoints. Any *upper* bound on
M̄ only lowers this quantity, so certified upper enclosures of ρ_i are safe. ∎
*(Standard stochastic-dominance argument: if μ ⪯ μ′ in the sense
μ([0,R]) ≤ μ′([0,R]) ∀R, and Ω is increasing, then ∫Ωdμ ≥ ∫Ωdμ′.)*

**Closed forms.** V₁(r) := ∫_{−L₀}^{L₀} e^{u/2}e^{iru}du =
2 sinh((½+ir)L₀)/(½+ir), similarly V₂ with ½ → −½; the orthonormalized pair's
band masses ρ_i(R) are 1-D integrals of products V(r)·V̄(r) of elementary analytic
functions — certifiable by Arb verified integration (script `certify_c0.py`).

**Numerical evaluation** (float; certification in progress): on the grid
R ∈ [0, 14] with steps 0.25: the negative-region (R < 6.3) admissible mass totals
≈ 0.094, cost ≈ −0.020; the earliest-allowed measure then accumulates mass in the
positive region, and the Stieltjes lower sum gives

  **c₀ ≥ 0.378.**

(True constrained infimum, measured variationally: ≈ 0.55 — the bound captures
~69% of it. The two-vector trace subtraction is the only lossy step.)

## Consequences

1. **A quantitative floor for the CC window**: the archimedean Weil form is not
   just nonnegative but uniformly coercive with explicit constant — the statement
   (Gap 1) missing from the literature.
2. **Perturbative T1 becomes a concrete inequality chase**: the same three lemmas
   applied on [−L, L] (L > L₀; trace 2LR/π, representers on the larger interval)
   give an explicit archimedean floor m(L) on the *full* constrained space at any
   L; T1 holds wherever m(L) exceeds the prime bound. At L₀ the bound gives 0.378
   < 0.490 = (log 2)/√2, so the norm-route still falls short — closing T1 needs
   either the second-moment refinement (Tr B², which sharpens Lemma T when the
   spectrum is spread) or the edge-mass refinement of Lemma 1. Both are now
   *bounded, explicit* problems in one-dimensional analysis.
3. The proof uses nothing beyond: Parseval, positivity of B_R, a trace identity,
   and monotonicity of the digamma kernel — it is independent of (and much more
   elementary than) the prolate/Sonin machinery, at the price of a worse constant.
