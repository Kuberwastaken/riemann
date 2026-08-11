/-
RiemannFormal/T1Certificate.lean — the T1 window functional and its conditional
certificate theorem (SHARP-FLOOR.md §§4–6), statement layer.

Status: DEFINITIONS + CONDITIONAL THEOREM, proof complete (sorry-free). The
theorem takes the certified
dictionary as hypotheses: (i) spectral caps ValidCap σ_j Λ_j (in the laboratory
these are λ_max bounds on compressions P_V σ_j(D) P_V — the objects the
frequency-side Nyström pipeline certifies numerically); (ii) the Parseval
normalization for the paper-convention transform (Mathlib Plancherel modulo the
2π-convention translation — to be discharged, tracked as hParseval);
(iii) dual feasibility: y ≥ 0, pointwise Ω_W ≥ c − Σ y_j σ_j, and c ≥ Σ y_j Λ_j.
Conclusion: W1(f) ≥ 0 on the admissible class — full-space one-prime Weil
positivity at the window. With the pilot dictionary at L = 0.40 the float LP
found such (y, c) with slack +0.0349; certifying those caps turns this theorem's
hypotheses into theorems.

Integrability of r ↦ ‖FT f r‖² is not an extra hypothesis: it follows from
hParseval, since a non-integrable function's Bochner integral is 0 ≠ 2π.
-/
import Mathlib

noncomputable section

namespace RiemannFormal

open MeasureTheory Real intervalIntegral
open scoped Real

/-- Archimedean multiplier Ω(r) = Re ψ(¼ + ir/2) − log π (digamma via deriv Γ / Γ). -/
def OmegaArch (r : ℝ) : ℝ :=
  ((deriv Complex.Gamma (1/4 + r/2 * Complex.I)) / Complex.Gamma (1/4 + r/2 * Complex.I)).re
    - Real.log π

/-- The full one-prime multiplier: Ω_W(r) = Ω(r) − √2·log 2·cos(r·log 2)
(the prime-2 term of the Weil form as a cosine multiplier; SHARP-FLOOR.md §4). -/
def OmegaW (r : ℝ) : ℝ :=
  OmegaArch r - Real.sqrt 2 * Real.log 2 * Real.cos (r * Real.log 2)

/-- Paper-convention transform F(r) = ∫ f(u) e^{iru} du. -/
def FT (f : ℝ → ℝ) (r : ℝ) : ℂ :=
  ∫ u, (f u : ℂ) * Complex.exp (Complex.I * r * u)

/-- Admissible test functions at window L: real, L², supported in [−L, L], and
annihilating the two pole directions e^{±u/2}. -/
structure Admissible (L : ℝ) (f : ℝ → ℝ) : Prop where
  memLp : MemLp f 2 volume
  supp : Function.support f ⊆ Set.Icc (-L) L
  pole_plus : ∫ u, f u * Real.exp (u / 2) = 0
  pole_minus : ∫ u, f u * Real.exp (-u / 2) = 0

/-- The window Weil functional, multiplier form: W1(f) = (1/2π)∫ ‖F f‖² Ω_W. -/
def W1 (f : ℝ → ℝ) : ℝ := (1 / (2 * π)) * ∫ r, ‖FT f r‖ ^ 2 * OmegaW r

/-- A certified dictionary row at window L: for every normalized admissible f,
the σ-weighted spectral mass is at most Λ. -/
def ValidCap (L : ℝ) (σ : ℝ → ℝ) (Λ : ℝ) : Prop :=
  ∀ f, Admissible L f → (∫ u, f u ^ 2) = 1 →
    (1 / (2 * π)) * ∫ r, ‖FT f r‖ ^ 2 * σ r ≤ Λ

/-- **T1, conditional certificate form.** If a finite dictionary of certified caps,
nonnegative dual weights with pointwise feasibility Ω_W ≥ c − Σ y·σ, budget
c ≥ Σ y·Λ, and the (convention-translated) Parseval identity are given, then the
window Weil functional is nonnegative on normalized admissible functions.
The analytic content lives entirely in the hypotheses; the proof is the σ-LP
dual assembly (SigmaLPAssembly.lean) transported along the spectral measure. -/
theorem T1_of_certificate
    {m : ℕ} (L c : ℝ) (σ : Fin m → ℝ → ℝ) (Λ y : Fin m → ℝ)
    (hcaps : ∀ j, ValidCap L (σ j) (Λ j))
    (hy : ∀ j, 0 ≤ y j)
    (hpt : ∀ r, c - ∑ j, y j * σ j r ≤ OmegaW r)
    (hbudget : ∑ j, y j * Λ j ≤ c)
    (hParseval : ∀ f, Admissible L f → (∫ u, f u ^ 2) = 1 →
      (1 / (2 * π)) * ∫ r, ‖FT f r‖ ^ 2 = 1)
    (hInt : ∀ f, Admissible L f → Integrable (fun r => ‖FT f r‖ ^ 2 * OmegaW r) volume)
    (hIntσ : ∀ f, Admissible L f → ∀ j, Integrable (fun r => ‖FT f r‖ ^ 2 * σ j r) volume)
    (f : ℝ → ℝ) (hf : Admissible L f) (hnorm : (∫ u, f u ^ 2) = 1) :
    0 ≤ W1 f := by
  -- ‖FT f ·‖² is integrable: otherwise its Bochner integral would be the junk
  -- value 0, contradicting the Parseval normalization (1/2π)·∫ = 1.
  have hFT2 : Integrable (fun r => ‖FT f r‖ ^ 2) volume := by
    by_contra h
    have h0 := integral_undef h
    have hP := hParseval f hf hnorm
    rw [h0, mul_zero] at hP
    exact zero_ne_one hP
  have hIntσf : ∀ j, Integrable (fun r => ‖FT f r‖ ^ 2 * σ j r) volume := hIntσ f hf
  -- rewrite the certificate integrand in subtracted form
  have hre : (fun r => ‖FT f r‖ ^ 2 * (c - ∑ j, y j * σ j r))
      = fun r => c * ‖FT f r‖ ^ 2 - ∑ j, y j * (‖FT f r‖ ^ 2 * σ j r) := by
    funext r
    rw [mul_sub, Finset.mul_sum]
    congr 1
    · ring
    · exact Finset.sum_congr rfl fun j _ => by ring
  have hSumInt : Integrable (fun r => ∑ j, y j * (‖FT f r‖ ^ 2 * σ j r)) volume :=
    integrable_finsetSum _ fun j _ => (hIntσf j).const_mul (y j)
  have hRHSInt : Integrable (fun r => ‖FT f r‖ ^ 2 * (c - ∑ j, y j * σ j r)) volume := by
    rw [hre]
    exact (hFT2.const_mul c).sub hSumInt
  -- pointwise feasibility times the nonnegative weight ‖FT f r‖²
  have h1 : ∫ r, ‖FT f r‖ ^ 2 * (c - ∑ j, y j * σ j r) ≤ ∫ r, ‖FT f r‖ ^ 2 * OmegaW r :=
    integral_mono hRHSInt (hInt f hf) fun r =>
      mul_le_mul_of_nonneg_left (hpt r) (by positivity)
  -- split the certificate integral by linearity
  have h2 : ∫ r, ‖FT f r‖ ^ 2 * (c - ∑ j, y j * σ j r)
      = c * (∫ r, ‖FT f r‖ ^ 2) - ∑ j, y j * ∫ r, ‖FT f r‖ ^ 2 * σ j r := by
    rw [hre, integral_sub (hFT2.const_mul c) hSumInt, MeasureTheory.integral_const_mul,
      integral_finsetSum _ fun j _ => (hIntσf j).const_mul (y j)]
    congr 1
    exact Finset.sum_congr rfl fun j _ => MeasureTheory.integral_const_mul _ _
  have hP : (0 : ℝ) < 1 / (2 * π) := by positivity
  -- caps: Σ y·(spectral mass) ≤ Σ y·Λ
  have hcapsum : ∑ j, y j * ((1 / (2 * π)) * ∫ r, ‖FT f r‖ ^ 2 * σ j r) ≤ ∑ j, y j * Λ j :=
    Finset.sum_le_sum fun j _ => mul_le_mul_of_nonneg_left (hcaps j f hf hnorm) (hy j)
  -- distribute (1/2π) over the split integral
  have hdist : (1 / (2 * π)) * (c * (∫ r, ‖FT f r‖ ^ 2) - ∑ j, y j * ∫ r, ‖FT f r‖ ^ 2 * σ j r)
      = c * ((1 / (2 * π)) * ∫ r, ‖FT f r‖ ^ 2)
        - ∑ j, y j * ((1 / (2 * π)) * ∫ r, ‖FT f r‖ ^ 2 * σ j r) := by
    rw [mul_sub, Finset.mul_sum]
    congr 1
    · ring
    · exact Finset.sum_congr rfl fun j _ => by ring
  -- assemble: W1 f ≥ (1/2π)·(certificate integral) = c·1 − Σ y·caps ≥ c − Σ y·Λ ≥ 0
  have hW : (1 / (2 * π)) * (∫ r, ‖FT f r‖ ^ 2 * (c - ∑ j, y j * σ j r)) ≤ W1 f :=
    mul_le_mul_of_nonneg_left h1 (le_of_lt hP)
  rw [h2, hdist, hParseval f hf hnorm, mul_one] at hW
  linarith [hcapsum, hbudget]

end RiemannFormal
