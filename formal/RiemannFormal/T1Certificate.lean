/-
RiemannFormal/T1Certificate.lean — the T1 window functional and its conditional
certificate theorem (SHARP-FLOOR.md §§4–6), statement layer.

Status: DEFINITIONS + CONDITIONAL THEOREM. The theorem takes the certified
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

Not imported by the root module until it compiles.
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
  sorry

end RiemannFormal
