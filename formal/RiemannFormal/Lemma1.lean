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
  -- the two windows: the integrand lives on I₊; its translate lives on I₋
  set Ip : Set ℝ := Icc (a - L) L with hIp
  set Im : Set ℝ := Icc (-L) (L - a) with hIm
  -- translation is measure preserving, so f(· − a) ∈ L² as well
  have hf2a : MemLp (fun t => f (t - a)) 2 volume :=
    hf2.comp_measurePreserving (measurePreserving_sub_right volume a)
  -- integrability of the product (Hölder 2·2 → 1) and of the squares
  have hprod : Integrable (fun t => f t * f (t - a)) volume :=
    hf2.integrable_mul hf2a
  have hsq : Integrable (fun t => f t ^ 2) volume := by
    have h := hf2.integrable_mul hf2
    have he : (f * f) = fun t => f t ^ 2 := by funext t; simp [pow_two]
    rwa [he] at h
  have hsqa : Integrable (fun t => f (t - a) ^ 2) volume := by
    have h := hf2a.integrable_mul hf2a
    have he : ((fun t => f (t - a)) * fun t => f (t - a)) = fun t => f (t - a) ^ 2 := by
      funext t; simp [pow_two]
    rwa [he] at h
  have hind1 : Integrable (Ip.indicator fun s => f s ^ 2) volume :=
    hsq.indicator measurableSet_Icc
  have hind2 : Integrable (Ip.indicator fun s => f (s - a) ^ 2) volume :=
    hsqa.indicator measurableSet_Icc
  have hind3 : Integrable (Im.indicator fun s => f s ^ 2) volume :=
    hsq.indicator measurableSet_Icc
  -- pointwise AM–GM bound, with the support bookkeeping folded into indicators
  have hptw : ∀ t, |f t * f (t - a)|
      ≤ (1 / 2) * (Ip.indicator (fun s => f s ^ 2) t + Ip.indicator (fun s => f (s - a) ^ 2) t) := by
    intro t
    by_cases ht : t ∈ Ip
    · rw [Set.indicator_of_mem ht, Set.indicator_of_mem ht, abs_mul]
      nlinarith [two_mul_le_add_sq |f t| |f (t - a)|, sq_abs (f t), sq_abs (f (t - a)),
        abs_nonneg (f t), abs_nonneg (f (t - a))]
    · have hz : f t * f (t - a) = 0 := by
        rw [hIp, Set.mem_Icc, not_and_or, not_le, not_le] at ht
        rcases ht with h | h
        · have hz' : f (t - a) = 0 := by
            by_contra hne
            have hmem := hsupp (Function.mem_support.mpr hne)
            rw [Set.mem_Icc] at hmem
            linarith [hmem.1]
          rw [hz', mul_zero]
        · have hz' : f t = 0 := by
            by_contra hne
            have hmem := hsupp (Function.mem_support.mpr hne)
            rw [Set.mem_Icc] at hmem
            linarith [hmem.2]
          rw [hz', zero_mul]
      rw [Set.indicator_of_notMem ht, Set.indicator_of_notMem ht, hz, abs_zero]
      norm_num
  -- integrable majorant
  have hmaj : Integrable
      (fun t => (1 / 2) * (Ip.indicator (fun s => f s ^ 2) t + Ip.indicator (fun s => f (s - a) ^ 2) t))
      volume := (hind1.fun_add hind2).const_mul _
  -- translate the second indicator integral onto I₋
  have hshift : ∀ t : ℝ, Ip.indicator (fun s => f (s - a) ^ 2) t
      = Im.indicator (fun u => f u ^ 2) (t - a) := by
    intro t
    by_cases ht : t ∈ Ip
    · have hm : t - a ∈ Im := by
        rw [hIp, Set.mem_Icc] at ht
        rw [hIm, Set.mem_Icc]
        constructor <;> linarith [ht.1, ht.2]
      rw [Set.indicator_of_mem ht, Set.indicator_of_mem hm]
    · have hm : t - a ∉ Im := by
        intro hmem
        apply ht
        rw [hIm, Set.mem_Icc] at hmem
        rw [hIp, Set.mem_Icc]
        constructor <;> linarith [hmem.1, hmem.2]
      rw [Set.indicator_of_notMem ht, Set.indicator_of_notMem hm]
  have hD : (∫ t, Ip.indicator (fun s => f (s - a) ^ 2) t)
      = ∫ u, Im.indicator (fun s => f s ^ 2) u := by
    simp_rw [hshift]
    exact integral_sub_right_eq_self (Im.indicator fun s => f s ^ 2) a
  -- a ≥ L makes I₊ and I₋ intersect in at most {0}: indicator sum ≤ 1 a.e.
  have hE : (∫ t, Ip.indicator (fun s => f s ^ 2) t) + (∫ t, Im.indicator (fun s => f s ^ 2) t)
      ≤ ∫ t, f t ^ 2 := by
    rw [← integral_add hind1 hind3]
    refine integral_mono_ae (hind1.fun_add hind3) hsq ?_
    have h0 : ∀ᵐ t : ℝ, t ∉ ({0} : Set ℝ) := compl_mem_ae_iff.mpr (measure_singleton 0)
    filter_upwards [h0] with t ht0
    by_cases h1 : t ∈ Ip <;> by_cases h2 : t ∈ Im
    · exfalso
      apply ht0
      rw [hIp, Set.mem_Icc] at h1
      rw [hIm, Set.mem_Icc] at h2
      have : t = 0 := le_antisymm (by linarith [h2.2]) (by linarith [h1.1])
      simp [this]
    · simp [Set.indicator_of_mem h1, Set.indicator_of_notMem h2]
    · simp [Set.indicator_of_notMem h1, Set.indicator_of_mem h2]
    · simp [Set.indicator_of_notMem h1, Set.indicator_of_notMem h2, sq_nonneg]
  -- assemble
  calc |∫ t, f t * f (t - a)|
      ≤ ∫ t, |f t * f (t - a)| := abs_integral_le_integral_abs
    _ ≤ ∫ t, (1 / 2) * (Ip.indicator (fun s => f s ^ 2) t
          + Ip.indicator (fun s => f (s - a) ^ 2) t) :=
        integral_mono hprod.abs hmaj hptw
    _ = (1 / 2) * ((∫ t, Ip.indicator (fun s => f s ^ 2) t)
          + ∫ t, Ip.indicator (fun s => f (s - a) ^ 2) t) := by
        rw [integral_const_mul, integral_add hind1 hind2]
    _ = (1 / 2) * ((∫ t, Ip.indicator (fun s => f s ^ 2) t)
          + ∫ t, Im.indicator (fun s => f s ^ 2) t) := by rw [hD]
    _ ≤ (1 / 2) * ∫ t, f t ^ 2 := by linarith [hE]

end RiemannFormal
