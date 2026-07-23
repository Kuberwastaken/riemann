# Certified positivity of truncated Weil functionals in low support windows

*Research note, 2026-07-23. All artifacts in `experiments/weil_positivity/` of
https://github.com/Kuberwastaken/reimann; every result reproducible by the commands
in §7. Status: unpublished working note; Lemmas proven; certified results are
computer-assisted (Arb ball arithmetic); everything else clearly labeled numerical.*

## Summary

Weil's criterion states that the Riemann Hypothesis is equivalent to positivity of
the explicit-formula functional W on autocorrelations of test functions of arbitrary
support. We study W on supports [−L, L] as L crosses the prime thresholds
½log p^k, and obtain: (1) a complete numerical regime map of the positivity
mechanism, validated against the explicit-formula identity to 10⁻⁵–10⁻⁷ using the
first 100,000 zeros; (2) two elementary sharp lemmas bounding the prime terms
(disjoint-support ½-factor); (3) an exact reformulation of the first open case
("T1") as a relative operator inequality μ(L) > −1, with the extremal structure
identified; (4) rigorous, ball-arithmetic-certified coercivity of the full Weil
functional on explicit 14-dimensional families at L = 0.45, 0.50, 0.545 (one prime)
and L = 0.60 (primes {2,3}) — the last being, to our knowledge, the first rigorous
multi-prime Weil-positivity statement; and (5) two structural discoveries at the
numerical level: *just-in-time rescue* (each truncation of the prime sum goes
indefinite almost immediately beyond its window and is restored by the next prime)
and *completion-criticality* (with all in-window primes included, λ_min sits at 0 to
5–6 digits at every window size — the finite-window face of the de Bruijn–Newman
Λ = 0 sharpness).

## 1. Setup

For real f with supp f ⊆ [−L, L], F(r) = ∫f(u)e^{iru}du, h = |F|², g = f⋆f̃, the
Riemann–Weil formula (Montgomery normalization) gives

  Σ_γ h(γ) = 2h(i/2) + (1/2π)∫h(r)Ω(r)dr − 2Σ_{n≥2}(Λ(n)/√n)g(log n),
  Ω(r) = Re ψ(¼ + ir/2) − log π,

γ over all nontrivial zeros (both signs, multiplicity; complex iff RH fails).
RH ⟺ the right side ≥ 0 for all such f and all L, with the two pole directions
removed (constraints ∫f e^{±u/2} = 0). The prime power n enters iff log n < 2L;
[−L, L] is prime-free iff L < ½log 2. In the prime-free window positivity is the
archimedean theorem of Connes–Consani (Selecta 2021). Our engine (`weil_form.py`,
N = 48 orthonormal sine modes) computes both sides independently; they agree to
relative Frobenius error 3·10⁻⁵ … 3·10⁻⁷ throughout (Odlyzko's 100k zeros), which
certifies all conventions.

## 2. The regime map (numerical; `RESULTS.md`)

margin(L) = λ_min of the archimedean form (constrained), total(L) = λ_min of the
full form, deficit(L) = norm of the prime part:

| regime | L | behavior |
|---|---|---|
| prime-free | < 0.3466 | margin = total: 1.105 → 0.55 |
| perturbative | 0.3466–0.39 | margin > deficit; norm-perturbation suffices |
| cancellative | 0.39–0.59 | deficit > margin > 0, total > 0: the prime's negative directions avoid the archimedean soft cone |
| criticality | > 0.59 | margin < 0; total pinned at 0 to 10⁻⁶ out to L = 2 (margin −1.35, deficit 3.50) |

Minimizers develop Fourier nodes at the actual zeros (node at γ₁ = 14.13 by
L = 1.1; interlacing by L = 1.9): the near-null cone consists of compact-support
functions whose transforms attempt to vanish on the zero set.

## 3. Lemmas (proven)

**Lemma 1.** supp f ⊆ [−L, L], a ≥ L ⇒ |g(a)| ≤ ½‖f‖².
*Proof.* g(a) = ⟨f·1_{[a−L,L]}, τ_a(f·1_{[−L,L−a]})⟩; the two windows are disjoint
for a ≥ L; Cauchy–Schwarz + AM–GM on disjoint masses. ∎
Sharp (dipole extremals); hence ‖Q₂‖ ≤ (log 2)/√2 = 0.490129…, matching the
measured saturation to six digits.

**Lemma 1′.** For every in-window prime power with log n ≥ L (all of them, if
L ≤ log 2): ‖Q_n‖ ≤ Λ(n)/√n; total prime norm ≤ Σ_{2≤n<e^{2L}} Λ(n)/√n.

**Refutation (numerical).** The spatial core/dipole 2×2 block criterion fails
everywhere (cross-coupling 0.68–1.62): no spatial-norm argument can prove T1.

## 4. The sharp invariant and its extremal

Where the constrained archimedean form G ≻ 0 (L < 0.59), set
μ(L) = λ_min(G^{−1/2}Q₂G^{−1/2}). Then T1 (positivity through the one-prime
window) ⟺ μ > −1: *the prime transfer is a strict contraction in the archimedean
metric*. Measured: μ = −0.31 (L=0.37) → −0.9917 (L=0.545). The extremal is a mixed
core/dipole mode with spectral mass in the band (2π, γ₁) realizing ≈83% of its
Lemma-1-allowed prime correlation; the sharpened analytic target is the
uncertainty-type statement: *a function of support ≤ log 3 cannot be spectrally
concentrated below γ₁ and simultaneously saturate its lag-log 2 autocorrelation.*
At L = 0.58 (two-prime window): μ = −1.05, i.e. G + Q₂ alone is indefinite while
G + Q₂ + Q₃ ≥ 0 — see §6.

## 5. Certified results (rigorous, computer-assisted)

Pipeline (`certify.py`): regularized closed form
F_k(r) = 2i^{1−k}w_k sincL(r−w_k)/(√L(w_k+r)) (no removable singularities); the
archimedean kernel used as its analytic symmetrization
(ψ(¼+ir/2)+ψ(¼−ir/2))/2 − log π (required for the soundness of Arb's rigorous
integration); verified integration on [0, R] with explicit tail bounds; prime and
pole entries by verified 1-D quadrature; exact-float family matrix Q; final bound
by Cholesky executed in ball arithmetic. For every f in the explicit
14-dimensional families:

| L | primes | certified W ≥ c‖f‖² |
|---|---|---|
| 0.450 | {2} | c = 0.072606 |
| 0.500 | {2} | c = 0.014842 |
| 0.545 | {2} | c = 0.001285 (full-space N=48 value: 0.001272) |
| 0.600 | {2,3} | c = 0.000076 |

Equivalently, by §1's identity: Σ_ρ ĥ_f(ρ) ≥ c‖f‖² over the actual nontrivial
zeros, for every member of each family. These are subspace statements — T1 proper
(all of L²[−L, L]) remains open; the L = 0.545 certificate nearly attains the
full-space infimum, so the family is not the bottleneck there.

## 6. Structural discoveries (numerical)

**Just-in-time rescue.** Truncations of the prime sum go indefinite essentially
immediately beyond their own window (μ(0.58) = −1.05); the next prime term
restores positivity. **Completion-criticality.** With all in-window primes, λ_min
lands at 0 within 10⁻⁵ at *every* window (L = 0.6, 0.8, 1.0, 1.2 tested), while
every proper truncation is strictly indefinite (to −0.5) and individual terms are
non-monotone (adding n = 4 at L = 1.2 lowers λ_min). The explicit-formula weights
are exactly the weights that complete every window to the boundary of positivity.
Together these say: Weil positivity is an irreducibly collective property of the
full Euler product — the quadratic-form counterpart of the convergence mechanism
in the Connes–Consani–Moscovici zeta-spectral-triple program, and a natural
induction structure (window-to-window propagation with zero slack) for any future
proof.

## 7. Reproducibility

```
experiments/.venv/bin/python weil_form.py test|validate|sweep|profiles
experiments/.venv/bin/python make_plots.py
experiments/.venv/bin/python t1_blocks.py
experiments/.venv/bin/python certify.py <L> [N]     # certified results, ~1 min each
experiments/.venv/bin/python rescue_certify.py      # rescue certification (L=0.62)
```
Data: `sweep.csv`, `t1_mu.txt`, `rescue_cascade.txt`, `certify_*_output.txt`.
Environment: Python venv (numpy/scipy/mpmath/python-flint 0.9.0), Raspberry Pi 5.

## Relation to prior work

The prime-free-window positivity is Connes–Consani (Selecta 27 (2021) 77); the
small-eigenvalue degeneration at large support is their ζ-cycles phenomenon
(Enseign. Math. 69 (2023)); our contribution is the prime-threshold-resolved
anatomy (regimes, sharp constants, the μ reformulation, extremal structure) and
the rigorous certificates with active prime terms, which we have not found
elsewhere in the literature collected in this repository (178 sources; see
`../../notes/` and `../../BREAKDOWN.md`).
