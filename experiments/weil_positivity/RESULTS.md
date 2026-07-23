# Results: numerical anatomy of Weil positivity in the critical window

*Experiment T4a of `../../ATTACK.md`, executed 2026-07-23 on valerie (Pi 5).
Engine: `weil_form.py` (N=48 orthonormal sine basis on [−L, L], pole directions
projected out by the two constraints ĝ(0) = ĝ(i/2) = 0). Every matrix was validated
against the explicit-formula identity: arithmetic side (digamma kernel + Λ(n) terms +
poles) vs spectral side (sum over Odlyzko's first 100,000 zeros) agree to relative
Frobenius error 3×10⁻⁵ … 3×10⁻⁷ across the whole sweep — all conventions certified
by the identity itself.*

Quantities per L (all on the constrained subspace, L²-normalized f):

- **margin(L)** = λ_min of the archimedean form G (kernel Ω(r) = Re ψ(¼+ir/2) − log π)
- **total(L)** = λ_min of the full Weil form G + P (RH ⟹ total ≥ 0 for every L)
- **deficit(L)** = ‖P‖ (operator norm of the prime part −2Σ Λ(n)n^{−1/2} S(log n))

![sweep](sweep.png)
![profiles](profiles.png)

## The four regimes

| Regime | Range of L | What happens |
|---|---|---|
| **I — prime-free** (CC 2020's window) | L < ½log 2 ≈ 0.3466 | margin = total > 0, decaying 1.105 (L=0.20) → 0.55 (window end). Connes–Consani's archimedean positivity theorem confirmed and quantified. |
| **II — perturbative** | 0.3466 < L ≲ 0.39 | p=2 active; **margin > deficit** (e.g. L=0.35: 0.544 vs 0.048). Here T1 follows from a CC-type margin bound plus an operator-norm bound — no new mechanism needed. |
| **III — cancellative** | 0.39 ≲ L ≲ 0.59 | **deficit > margin > 0, yet total > 0.** At L=0.45: margin 0.291, deficit 0.490, total +0.072. The p=2 term could kill positivity by norm but doesn't: its negative directions (autocorrelation concentrated at lag log 2) systematically avoid the archimedean soft cone. Norm-perturbation proofs of T1 are DEAD here; the required lemma is this direction-avoidance. |
| **IV — arithmetic rescue / criticality** | L ≳ 0.59 | **margin < 0 < deficit-scale, total = 0 to 6–7 digits.** By L=2.0: margin −1.354, deficit 3.498, total −0.000000. The archimedean form alone is deeply indefinite; the prime terms lift the soft directions back to exactly zero. Positivity is irreducibly arithmetic beyond L* ≈ 0.59. |

## Quantitative landmarks

- **Margin at the end of the proven window:** ≈ 0.55 (L², N=48; converged to ±0.003 —
  N=24/48/72 give 0.2967/0.2908/0.2887 at L=0.45).
- **Perturbative/cancellative boundary: L ≈ 0.39** — *before* the p=3 threshold
  (½log 3 ≈ 0.549). The single prime 2 already forces the structural mechanism.
- **The p=2 deficit saturates at (log 2)/√2 ≈ 0.4901** for L ≳ 0.40 (the shift-overlap
  norm reaching ½), i.e. the prime-2 term's worst case is an explicit constant.
- **Archimedean-dominance boundary: L\* = 0.59 ± 0.01** (margin zero-crossing;
  N-convergence corrected). For all larger windows, purely archimedean positivity is
  false and the Euler product carries the load.
- **Criticality pinning:** for L ∈ [0.68, 2.00] (24 prime powers active), |total| < 10⁻⁶
  while margin and deficit grow to −1.35 and 3.50: a two-orders-of-magnitude conspiracy
  holding the infimum at exactly 0. This is the de Bruijn–Newman Λ = 0 / ζ-cycles
  boundary-feasibility picture rendered live.
- **Minimizer anatomy** (profiles.png): in regime I the minimizer is a single smooth
  bump whose spectral density sits just outside the negative-Ω region (near the first
  zero's height); entering regime IV the minimizers develop *nodes at the actual zeta
  zeros* — at L=1.1 the spectral density vanishes at γ₁ = 14.13 with lobes on both
  sides; by L=1.9 it interlaces the first several zeros. The near-null vectors are
  compact-support functions whose Fourier transforms try to vanish on the zero set —
  the concrete, visible form of the ζ-cycles small-eigenvalue mechanism.
- **Arithmetic tuning:** the minimizer's autocorrelation at the p=2 lag, g(log 2),
  is smooth and positive in regimes II–III (peaking ≈ 0.24 near L=0.45) and becomes
  rapidly sign-alternating in regime IV — the minimizers actively tune their prime-lag
  correlations against the Λ(n) weights.

## What this says about T1 (the {∞,2} positivity target)

1. **T1 with small δ is real:** in (0.3466, ≈0.39) the existing CC margin beats the
   full operator norm of the prime term. A proof needs only (a) a proven quantitative
   lower bound for the archimedean margin slightly beyond the ratio-2 window — the
   Sonin-trace mechanism is exactly this — and (b) the explicit bound
   ‖P₂‖ ≤ (log 2)/√2. This looks like honest, finishable mathematics.
2. **T1 in the full one-prime window (up to ½log 3) requires the cancellation lemma:**
   prove that on the archimedean soft cone (near-minimizers of G), the p=2 quadratic
   form is small — equivalently, low-Ω-concentrated functions have small
   autocorrelation at lag log 2. This is a statement about prolate-type functions and
   a single shift — well-posed, finite, and *the* structural content of T1. Its
   generalization prime-by-prime is the whole game; the numerics say it is true with
   room at p=2.
3. **No numerical experiment tests RH itself here** — all heights involved carry
   verified zeros, so total ≥ 0 is guaranteed-by-data in the computed range. The value
   is the *decomposition*: where perturbation ends, where cancellation begins, where
   archimedean positivity dies, and what the null vectors look like.

## Reproduce

```
experiments/.venv/bin/python weil_form.py test      # digamma + FT self-tests
experiments/.venv/bin/python weil_form.py validate  # explicit-formula identity check
experiments/.venv/bin/python weil_form.py sweep     # ~12 min on a Pi 5 -> sweep.csv
experiments/.venv/bin/python weil_form.py profiles  # minimizer profiles -> profiles.npz
experiments/.venv/bin/python make_plots.py          # sweep.png, profiles.png
```
