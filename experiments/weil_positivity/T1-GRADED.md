# T1-GRADED: opening the graded-mode architecture (Lead 1)

*2026-08-11, ai-vps session. Status: scaffold with one lemma proven, the assembly
inequality stated, and the single remaining analytic lemma isolated. Everything
labeled [proven] is complete mathematics; [stated] means the statement is precise
but the proof is not written; [open] means open.*

Setting as in `T1-ARCHITECTURE.md`: T = [−L, L] with ½log 2 < L ≤ log 2; sine ONB
φ_j(u) = sin(ω_j(u+L))/√L, ω_j = jπ/(2L); constrained space V (pole functionals
projected); W = G + Q₂ (+Q₃ where active), G = (1/2π)∫|F|²Ω, Ω(r) =
Re ψ(¼+ir/2) − log π, increasing (Lemma M), Ω(0) = −γ − 3log2 − π/2 − log π =
−5.37220…, Ω(r) = log(r/2π) + O(r⁻²) as r → ∞ (so the valley boundary r* with
Ω(r*) = 0 sits at r* ≈ 2π·(1+o(1)); numerically r* = 6.2865). Prime bound
|⟨f, Q₂ f⟩| ≤ q‖f‖², q = (log 2)/√2 = 0.490129 (Lemma 1; valid for all L ≤ log 2,
cross terms included — the prime term needs NO block bookkeeping).

## Lemma H (high-mode band-mass bound) [proven]

*For N ≥ 2, 0 < R < ω_N, and any f = Σ_{j≥N} c_j φ_j with ‖f‖ = 1:*

    ν_f([0,R]) := (1/π)∫₀^R |F(r)|² dr  ≤  ε(N,R) := (8/π²) · log( (N−1) / (N−1−β) ),
    β := 2LR/π  (< N−1).

*Proof.* ν_f([0,R]) = ⟨f, B_R f⟩ ≤ Tr[P⁺_N B_R P⁺_N] = Σ_{j≥N} (1/π)∫₀^R |F_j(r)|² dr,
where P⁺_N projects onto span{φ_j : j ≥ N} — the trace bounds the form because
B_R ⪰ 0 makes all diagonal terms nonnegative (same device as Lemma T). Direct
computation (v = u+L, ω_j·2L = jπ) gives ∫₀^{2L} sin(ω_j v)e^{irv}dv =
ω_j(1−(−1)^j e^{2irL})/(ω_j²−r²), hence the exact magnitude
|F_j(r)| = (2ω_j/√L)·|trig_j(rL)|/|ω_j²−r²|, trig_j = sin (j even), cos (j odd);
for 0 ≤ r < ω_j this gives |F_j(r)|² ≤ 4ω_j²/(L(ω_j+r)²(ω_j−r)²) ≤ (4/L)/(ω_j−r)².
Hence (1/π)∫₀^R |F_j|² ≤ (4/(πL))·[1/(ω_j−R) − 1/ω_j] = (4/(πL))·R/(ω_j(ω_j−R)).
Summing over j ≥ N with ω_j = jπ/(2L):
Σ_{j≥N} R/(ω_j(ω_j−R)) = (2L/π)²·R·Σ_{j≥N} 1/(j(j−β)) and
Σ_{j≥N} 1/(j(j−β)) = (1/β)·Σ_{j≥N}[1/(j−β) − 1/j] ≤ (1/β)·∫_{N−1}^∞ [1/(t−β) − 1/t]dt
= (1/β)·log((N−1)/(N−1−β)). Multiplying out: (4/(πL))·(4L²/π²)·(π/(2L))·log(·) =
(8/π²)·log((N−1)/(N−1−β)). ∎

Remarks. (i) For β ≪ N: ε ≈ (8/π²)·β/(N−1) = 16LR/(π³(N−1)) — the valley mass of
the high block decays like 1/N. (ii) The bound is basis-tied (sine modes) but V-free:
no constraint information is used, so it holds on the constrained high block a
fortiori. (iii) This is the quantitative form of "the kernel singularity is
high-frequency growth of Ω, which is the good direction" (LEADS.md Lead 1, step 3).

## Corollary H′ (single high-block coercivity) [proven]

For unit f ∈ span{φ_j : j ≥ N} and any R < ω_N:

    W(f) ≥ Ω(R)·(1 − ε(N,R)) + Ω(0)·ε(N,R) − q.

*Proof.* Stochastic dominance (Lemma M + Lemma R) with the single cap ν([0,R]) ≤ ε:
worst placement is mass ε at Ω(0), the rest at Ω(R); add the global prime bound. ∎

Numerically: with M := β (i.e. R = ω_M), the block j ≥ N is positive with margin μ_H
once log(ω_M/2π)·(1−ε) − 5.373·ε − 0.4901 ≥ μ_H, ε = (8/π²)log((N−1)/(N−1−M)).
E.g. L = 0.36 (note R = ω_M ⟺ β = M): (N, M) = (200, 12): ω_M = 52.4, Ω ≈ 2.12,
ε = (8/π²)log(199/187) ≈ 0.050 ⇒ margin ≈ +1.25.
Even (N, M) = (60, 8): ω_8 = 34.9, Ω ≈ 1.71, ε ≈ 0.118 ⇒ margin ≈ +0.38. The high
block standing alone is comfortably coercive with N in the tens. **All difficulty
is in the coupling.**

## The assembly [stated]

Split f = x + y, x ∈ V_lo = span{φ_j : j < N₀} ∩ V, y ∈ V_hi. The prime term is
global (no cross bookkeeping). B := (1/π)∫|F|²Ω₋ satisfies, by Lemma H applied at
R = r*: B(y) ≤ 5.373·ε(N₀, r*)‖y‖², so the B-cross absorbs with weight t:
B(f) ≤ (1+t)B(x) + (1+1/t)B(y). The A-cross (A := (1/2π)∫|F|²Ω₊, PSD, unbounded)
is the crux: a two-block absorption costs a multiple of λ_max(A|V_lo) ≈ Ω(ω_{N₀})
against a low-block margin of order 10⁻²–10⁻¹ — it fails, exactly as the spatial
2×2 criterion failed (t1_blocks). The graded fix is a DYADIC shell decomposition
{S_m} of the high modes with a Schur/Cotlar–Stein bound on the shell-coupling
matrix of A, which requires:

**Lemma X (shell-coupling decay) [open — the single remaining analytic lemma].**
*For dyadic shells S_m = {2^m ≤ j < 2^{m+1}} (m ≥ m₀ := log₂ N₀) and unit
x ∈ span S_m, y ∈ span S_{m′}, m′ ≥ m + 2:*

    |A(x, y)| ≤ C_X · √(Ω(ω_{2^m}) · Ω(ω_{2^{m′}})) · 2^{−(m′−m)}

*(or any summable-in-(m′−m) majorant with sub-geometric Ω-growth).* The mechanism:
F_x is concentrated on [ω_{2^m}(1−O(1)), ω_{2^{m+1}}] with 1/(ω_j−r)² sine tails
(the same tails as Lemma H), F_y likewise; the Ω₊-weighted overlap integral picks
up Ω at the geometric midpoint times the tail product, which integrates to
2^{−(m′−m)}·polylog. This is an explicit one-dimensional oscillatory-tail estimate
of the same species as Lemma H — longer, but with no conceptual obstruction. What
must be tracked: the log-growth of Ω across shells (harmless: √(Ω_m Ω_{m′})·2^{−Δ}
is summable against any polylog), and the sine-mode tails INSIDE the window
(no smooth cutoff is available — this is where the constant chase lives).

**Assembly theorem (conditional on Lemma X) [stated].** With Schur weights
w_m = 2^{−m/2}√(Ω(ω_{2^m})), Lemma X gives A ⪰ Σ_m (1−δ_m) A|S_m with
Σ-summable δ_m ≤ C_X·c₀ < 1. Combined with H′ per shell, B-absorption, and a
certified low-block floor g_lo(N₀, L) (ball Cholesky, existing pipeline):

    T1(L) holds if   g_lo(N₀, L) > q + 5.373(t + s(N₀)) + [Schur budget C_X terms],

with every quantity except C_X computable today. Crude budget estimate: the
certification threshold lands at N₀ in the range 10²–10³ for L near ½log 2
(entry computation 10⁴–10⁶ verified 1-D integrals — heavy but feasible on this
hardware), decreasing as the constants are sharpened.

## Honest status

- Lemma H + H′: proven above, elementary, and independently useful (they are the
  certified-tail half of any future full-space statement, including the σ-LP
  certification of `sigma_lp.py`).
- Lemma X: precisely stated, believed provable by the same tail technique,
  NOT proven here. It is the entire remaining analytic content of Lead 1's step 4.
- The assembly is a conditional reduction: **full-space T1(L) ⟸ Lemma X + one
  finite certified computation.** No claim beyond that; in particular nothing here
  touches RH, and the reduction is only as good as the constant C_X, which is
  where the "2–4 weeks of constant-chasing" (LEADS.md) genuinely lives.
- Interaction with Track D (same session): the σ-augmented LP targets the norm
  route at small δ WITHOUT any decomposition; this architecture targets all
  L ≤ log 2. The two share Lemma H's tail technology and the same certification
  pipeline; whichever lands first, the other inherits its constants.
