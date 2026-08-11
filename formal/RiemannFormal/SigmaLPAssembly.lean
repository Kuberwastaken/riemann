/-
RiemannFormal/SigmaLPAssembly.lean — the σ-LP dual assembly theorem
(experiments/weil_positivity/SHARP-FLOOR.md §§3–6).

Abstract form. ν is the (probability) spectral measure of a test function; Ω is any cost
multiplier (for the one-prime Weil form, Ω_W(r) = Re ψ(¼+ir/2) − log π − √2·log 2·cos(r log 2));
each dictionary row σ_j carries a cap ∫σ_j dν ≤ Λ_j (in the application, Λ_j is a certified
upper bound on λ_max of the compression P_V σ_j(D) P_V — those spectral facts live OUTSIDE
this lemma and enter as hypotheses). If nonnegative weights y_j give the pointwise lower
bound Ω ≥ c − Σ y_j σ_j on all of ℝ, then

    ∫ Ω dν  ≥  c − Σ y_j Λ_j.

This 15-line inequality is the entire "assembly" step of the T1 certificate: with a
concrete certified dictionary it turns finitely many spectral caps + one pointwise
1-D inequality + arithmetic into full-space Weil positivity on a window.
-/
import Mathlib

open MeasureTheory

namespace RiemannFormal

/-- **σ-LP dual assembly.** If `ν` is a probability measure, `Ω ≥ c − Σ y j • σ j`
pointwise with `y ≥ 0`, and each `∫ σ j dν ≤ Λ j`, then `∫ Ω dν ≥ c − Σ y j * Λ j`. -/
theorem sigma_lp_assembly
    {m : ℕ} (ν : Measure ℝ) [IsProbabilityMeasure ν]
    (Ω : ℝ → ℝ) (c : ℝ) (σ : Fin m → ℝ → ℝ) (Λ y : Fin m → ℝ)
    (hy : ∀ j, 0 ≤ y j)
    (hpt : ∀ r, c - ∑ j, y j * σ j r ≤ Ω r)
    (hcap : ∀ j, ∫ r, σ j r ∂ν ≤ Λ j)
    (hΩ : Integrable Ω ν) (hσ : ∀ j, Integrable (σ j) ν) :
    c - ∑ j, y j * Λ j ≤ ∫ r, Ω r ∂ν := by
  have hyσ : ∀ j : Fin m, Integrable (fun r => y j * σ j r) ν :=
    fun j => (hσ j).const_mul (y j)
  have hsum : Integrable (fun r => ∑ j, y j * σ j r) ν :=
    integrable_finsetSum _ fun j _ => hyσ j
  have hlhs : Integrable (fun r => c - ∑ j, y j * σ j r) ν :=
    (integrable_const c).sub hsum
  -- ∫ (c − Σ yσ) dν ≤ ∫ Ω dν by the pointwise bound
  have hmono : ∫ r, (c - ∑ j, y j * σ j r) ∂ν ≤ ∫ r, Ω r ∂ν :=
    integral_mono hlhs hΩ hpt
  -- ∫ (c − Σ yσ) dν = c − Σ y ∫σ (probability measure + linearity)
  have hsplit : ∫ r, (c - ∑ j, y j * σ j r) ∂ν = c - ∑ j, y j * ∫ r, σ j r ∂ν := by
    rw [integral_sub (integrable_const c) hsum]
    have hc : ∫ _ : ℝ, c ∂ν = c := by simp
    rw [hc]
    congr 1
    rw [integral_finsetSum _ fun j _ => hyσ j]
    exact Finset.sum_congr rfl fun j _ => integral_const_mul (y j) (σ j)
  -- caps: Σ y ∫σ ≤ Σ y Λ since y ≥ 0
  have hcaps : ∑ j, y j * ∫ r, σ j r ∂ν ≤ ∑ j, y j * Λ j :=
    Finset.sum_le_sum fun j _ => mul_le_mul_of_nonneg_left (hcap j) (hy j)
  linarith

end RiemannFormal
