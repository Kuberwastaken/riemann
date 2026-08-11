/-
RiemannFormal/Criterion.lean — the criterion layer (requires the Zeta23 library to be
built; NOT imported by the root module yet; `weil_positivity_of_RH` is sorry-free).

Layer 1 of the program (formal/README.md): wire this laboratory to the actual zeros of
Mathlib's ζ through the hypothesis-free literature-form explicit formula of
anthropics/zeta-23-lean (`Zeta23.WeilEF.EF_lit_zetaZeroConfig`):

  ∀ k C²c:  Σ'_{ρ nontrivial} m_ρ · paperFT k (γ_ρ)  =  literatureRHS k,

where γ_ρ = (ρ − 1/2)/i is real exactly on the critical line.

Target A (`weil_positivity_of_RH`): under RH every γ_ρ is real, and for the
autocorrelation k = f ⋆ f̃ the zero-side summand is m_ρ‖paperFT f (γ_ρ)‖² ≥ 0 — so the
ARITHMETIC side is nonnegative: RH ⇒ Weil positivity, formally. Contrapositive: a
certified strictly-negative arithmetic side at any C²c test function would disprove RH.

Target B (the converse, Bombieri 2000/Yoshida 1992: positivity for ALL such k ⇒ RH) is
the deep half; stated here as the criterion Prop so the reduction is machine-readable.
The laboratory's T1-type theorems (T1Certificate.lean) certify positivity on
restricted-support subfamilies — strictly weaker than `WeilPositivityAll`, feeding it.
-/
import Zeta23.WeilEF.Main
import Zeta23.ZeroSide
import RiemannFormal.T1Certificate

noncomputable section

namespace RiemannFormal

open Zeta23 MeasureTheory Complex

/-- Autocorrelation k = f ⋆ f̃, k(u) = ∫ f(t) conj(f(t − u)) dt. -/
def autocorr (f : ℝ → ℂ) (u : ℝ) : ℂ := ∫ t, f t * (starRingEnd ℂ) (f (t - u))

/-- Weil positivity for all autocorrelations of C²c test functions (the full criterion
predicate; restricted-support versions are what the laboratory certifies). -/
def WeilPositivityAll : Prop :=
  ∀ f : ℝ → ℂ, ContDiff ℝ 2 f → HasCompactSupport f →
    0 ≤ (Zeta23.EF.literatureRHS (autocorr f)).re

/-- **Target A: RH makes the arithmetic side of the explicit formula PSD.**
Proof route: autocorr f is C²c (convolution regularity); EF_lit_zetaZeroConfig turns
literatureRHS (autocorr f) into the zero sum; RH ⇒ γ_ρ real (γ_ρ = (ρ−1/2)/i);
paperFT (autocorr f) γ = ‖paperFT f γ‖² at real γ (Fubini + translation); a convergent
sum of nonnegative reals is nonnegative. -/
theorem weil_positivity_of_RH (hRH : RiemannHypothesis) : WeilPositivityAll := by
  intro f hf hfs
  -- `autocorr f` is literally Zeta23's Weil test function `f ⋆ f̃` (unfold the convolution).
  have hac : autocorr f = EF.weilTest f f := by
    funext u
    simp only [autocorr, EF.weilTest, convolution_def, ContinuousLinearMap.mul_apply',
      EF.tilde, neg_sub]
  -- C²c regularity of the autocorrelation, via the library's convolution lemmas.
  have hk2 : ContDiff ℝ 2 (autocorr f) := by
    rw [hac]; exact EF.weilTest_contDiff hf hf.continuous hfs
  have hkc : HasCompactSupport (autocorr f) := by
    rw [hac]; exact EF.weilTest_hasCompactSupport hfs hfs
  -- The hypothesis-free explicit formula for k = autocorr f.
  obtain ⟨hSum, hEq⟩ := Zeta23.WeilEF.EF_lit_zetaZeroConfig (autocorr f) hk2 hkc
  -- Under RH every γ_ρ is real, so each summand is m_ρ‖paperFT f γ_ρ‖², a nonnegative real.
  have hterm : ∀ ρ : zetaZeroConfig.carrier,
      (zetaZeroConfig.mult ρ : ℂ) * paperFT (autocorr f) (gammaOf ρ)
        = (((zetaZeroConfig.mult ρ : ℝ) * Complex.normSq (paperFT f (gammaOf ρ)) : ℝ) : ℂ) := by
    intro ρ
    have hz : IsNontrivialZero (ρ : ℂ) := ρ.2
    have hre : (ρ : ℂ).re = 1 / 2 := RH_implies_on_line hRH hz
    have hγ : gammaOf (ρ : ℂ) = ((ρ : ℂ).im : ℂ) := ZeroSide.gammaOf_of_re_eq_half hre
    have hconj : (starRingEnd ℂ) (gammaOf (ρ : ℂ)) = gammaOf (ρ : ℂ) := by
      rw [hγ, Complex.conj_ofReal]
    rw [hac, EF.paperFT_weilTest hf.continuous hf.continuous hfs hfs, hconj,
      Complex.mul_conj]
    push_cast
    ring
  have hnonneg : ∀ ρ : zetaZeroConfig.carrier,
      0 ≤ ((zetaZeroConfig.mult ρ : ℂ) * paperFT (autocorr f) (gammaOf ρ)).re := by
    intro ρ
    rw [hterm ρ, Complex.ofReal_re]
    exact mul_nonneg (Nat.cast_nonneg _) (Complex.normSq_nonneg _)
  -- A convergent sum of nonnegative reals is nonnegative.
  rw [← hEq, Complex.re_tsum hSum]
  exact tsum_nonneg hnonneg

/-- The Weil positivity criterion, as a machine-readable reduction target
(⇐ is Target A's converse — Bombieri's argument — the deep open half to formalize;
⇒ is Target A). Stated as a Prop; not claimed. -/
def WeilCriterion : Prop := WeilPositivityAll ↔ RiemannHypothesis

end RiemannFormal
