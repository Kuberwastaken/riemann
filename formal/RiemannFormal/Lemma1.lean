/-
RiemannFormal/Lemma1.lean — Lemma 1 of experiments/weil_positivity/T1-ARCHITECTURE.md:
the sharp half-factor prime bound.

  For real f ∈ L²(ℝ) with supp f ⊆ [−L, L] and shift a ≥ L:
      |∫ f(t)·f(t−a) dt| ≤ ½ ∫ f².

This is the bound |g_f(a)| ≤ ½‖f‖² whose consequence ‖Q_p‖ ≤ (log p)/√p underpins the
laboratory's prime-term estimates (the p = 2 instance is the 0.490129… bar). Sharp:
equality approached by "dipole" configurations (two ±-aligned bumps at separation a).

Paper proof (5 lines): the integrand is supported in I₊ := [a−L, L]; write the integral
as ⟨f·1_{I₊}, τ_a(f·1_{I₋})⟩ with I₋ := I₊ − a = [−L, L−a]; Cauchy–Schwarz; translation
invariance; AM–GM; and I₊, I₋ are a.e.-disjoint since a ≥ L, so
‖f·1_{I₊}‖² + ‖f·1_{I₋}‖² ≤ ‖f‖².
-/
import Mathlib

open MeasureTheory Set Real

namespace RiemannFormal

/-- **Lemma 1 (sharp half-factor bound).** For `f ∈ L²(ℝ)` supported in `[−L, L]` and
`a ≥ L`, the autocorrelation at lag `a` satisfies `|g_f(a)| ≤ ½‖f‖₂²`. -/
theorem lemma1_half_factor
    (f : ℝ → ℝ) (L a : ℝ) (ha : L ≤ a)
    (hf2 : MemLp f 2 volume)
    (hsupp : Function.support f ⊆ Icc (-L) L) :
    |∫ t, f t * f (t - a)| ≤ (1 / 2) * ∫ t, f t ^ 2 := by
  sorry

end RiemannFormal
