# A proof architecture for T1, with one lemma proven

*2026-07-23, follow-up to `RESULTS.md`. Everything here is exact mathematics unless
explicitly labeled numerical.*

Throughout: a = log 2, f ∈ L²(ℝ) real with supp f ⊆ [−L, L], autocorrelation
g(u) = ∫ f(t) f(t−u) dt, so g(0) = ‖f‖². The prime-2 term of the Weil form is
Q₂(f) = −2 (log 2) 2^{−1/2} g(log 2) = −√2 log 2 · g(log 2).

## Lemma 1 (the ½-factor; rigorous)

**If L ≤ a, then |g(a)| ≤ ½ ‖f‖², hence |Q₂(f)| ≤ (log 2)/√2 · ‖f‖² ≈ 0.490129 ‖f‖².**

*Proof.* The integrand of g(a) = ∫ f(t) f(t−a) dt is supported where t ∈ [−L, L] and
t − a ∈ [−L, L], i.e. t ∈ I₊ := [a−L, L] (empty unless a ≤ 2L). Writing
f₊ = f·1_{I₊} and f₋ = f·1_{I₋} with I₋ := I₊ − a = [−L, L−a], we have
g(a) = ⟨f₊, τ_a f₋⟩ where τ_a is the (unitary) shift. Since L ≤ a, the intervals
I₊ ⊆ [a−L, L] and I₋ ⊆ [−L, L−a] are disjoint up to a null set
(a−L ≥ L−a ⟺ a ≥ L). Hence by Cauchy–Schwarz and disjointness,
|g(a)| ≤ ‖f₊‖‖f₋‖ ≤ ½(‖f₊‖² + ‖f₋‖²) ≤ ½‖f‖². ∎

Remarks.
- **Sharp**: equality is approached by "dipoles" f = f₊ + f₋ with f₊ = ±τ_a f₋ and
  all mass in I₊ ∪ I₋. The sweep measured the deficit saturating at 0.490129 —
  exactly (log 2)/√2 — so the lemma matches the observed saturation and the observed
  value certifies the numerics.
- **Lemma 1′ (general form, same proof).** For any prime power n = p^k with
  log n ≥ L, the term Q_n(f) = −2Λ(n)n^{−1/2}g_f(log n) obeys
  |Q_n(f)| ≤ Λ(n)n^{−1/2}‖f‖². Hence for L ≤ log 2 (where *every* in-window prime
  power has log n ≥ log 2 ≥ L), the **total** prime part obeys
  ‖P‖ ≤ Σ_{2 ≤ n < e^{2L}} Λ(n)n^{−1/2} — an explicit constant per window
  (0.4901 for one prime; 1.1244 for {2,3}; etc.), rigorous for the entire regime
  probed by the sweep up to L = log 2.
- **Coverage**: L ≤ log 2 ≈ 0.6931 covers the entire one-prime window
  (L < ½log 3 ≈ 0.5493) and all of regime III.
- **Refinement used below**: the proof actually gives the stronger
  |g(a)| ≤ ½ ‖f‖²_{I₊ ∪ I₋} — only *edge mass* is exposed to the prime.

## Corollary (perturbative T1; conditional on a margin bound)

If the constrained archimedean form obeys G(f) ≥ m(L)‖f‖² with m(L) > (log 2)/√2,
then Weil positivity holds for all admissible f supported in [−L, L]. Numerically
m(L) crosses 0.4901 at L ≈ 0.369, so a *proven* CC-type margin bound of that
strength would settle T1 for L ∈ (½log 2, ≈0.369) outright. (The CC 2020 Sonin-trace
lower bound is a statement of exactly this species at L = ½log 2; the missing step is
its quantitative extension to slightly larger L.)

## The core/dipole decomposition (exact geometry)

For L ∈ (a/2, a) partition [−L, L] into
- **core** C = (−(a−L), a−L) — half-length a − L,
- **edges** E₋ = [−L, −(a−L)], E₊ = [a−L, L] — width 2L − a each,
  centered at ∓a/2, i.e. **separated by exactly the prime lag log 2**.

Three exact facts:
1. **The prime term lives entirely on the edges**: I₊ = E₊, I₋ = E₋ in Lemma 1's
   notation, so Q₂(f) = −√2 log 2 ⟨f_{E₊}, τ_a f_{E₋}⟩ depends only on the edge
   components — a pure "2-adic dipole" transfer between two strips at separation
   log 2. |Q₂(f)| ≤ (log 2)/√2 · ‖f_edge‖².
2. **The core is always inside the proven window**: supp f_core has half-length
   a − L < ½log 2 throughout the one-prime window (since L > a/2), so the
   autocorrelation of f_core is supported in (−log 2, log 2): the core block of the
   Weil form is purely archimedean and of the exact species covered by the
   Connes–Consani 2020 mechanism.
3. **Only two inequalities remain.** Writing the constrained Weil form in blocks
   (core, edge): W(f) ≥ λ_c‖f_c‖² − 2x‖f_c‖‖f_e‖ + (λ_e − q)‖f_e‖² with
   q = (log 2)/√2, x = ‖G_{ce}‖, λ_c = archimedean core coercivity,
   λ_e = archimedean edge coercivity. **T1 in this window ⟸
   λ_c > 0, and λ_c(λ_e − q) ≥ x²** — a 2×2 criterion in three archimedean-only
   constants. The prime has been completely absorbed into the explicit constant q.

This converts T1 from "extend Weil positivity past the prime" into "prove a
coercivity/off-diagonal bound for the archimedean form relative to a fixed geometric
partition" — no arithmetic left except the number log 2 in the geometry. The
multi-prime generalization is visible: each prime power p^k contributes a dipole
transfer at separation k log p with constant (log p)/p^{k/2}, acting on edge strips
of the corresponding partition; the ζ-cycles "arithmetic prolate" eigenvectors are
the multi-prime dipole modes.

## Numerical status — v1 (spatial blocks) REFUTED as a proof route

`t1_blocks.txt`: the block constants across the window. Outcome: the 2×2 criterion
**fails everywhere** (composite eigenvalue −0.58 … −1.04) even though the exact total
is positive — the archimedean core–edge coupling x ≈ 0.68–1.62 swamps any block-norm
argument, and by L = 0.545 even λ_e − q < 0 (the dipole sector alone is *not*
archimedean-dominated). Conclusions: (i) Lemma 1's sharpness is confirmed in-sector
(q_meas = 0.490129 to six digits); (ii) the positivity mechanism is genuinely
non-local in the spatial partition — norm bounds on spatial blocks cannot prove T1.
An honest refutation of the naive architecture; the decomposition's *geometry*
(prime lives on the log 2 dipole; core is CC-species) remains exact and useful.

## v2 — the sharp invariant: prime transfer in the archimedean metric

On the constrained space, wherever G ≻ 0 (true for L < L* ≈ 0.59), define
**μ(L) = λ_min( G^{−1/2} Q₂ G^{−1/2} )**. Then exactly:

**T1 on the window ⟺ G ≻ 0 and μ(L) > −1** — a single relative operator
inequality: *the prime-2 transfer, measured in the metric defined by the archimedean
form, is a strict contraction.* Measured values (`t1_mu.txt`, N=48):

| L | 0.370 | 0.400 | 0.430 | 0.460 | 0.490 | 0.520 | 0.545 |
|---|---|---|---|---|---|---|---|
| μ | −0.308 | −0.510 | −0.674 | −0.808 | −0.908 | −0.970 | −0.9917 |
| headroom 1+μ | 0.692 | 0.490 | 0.326 | 0.192 | 0.092 | 0.030 | **0.0083** |

The invariant holds across the entire one-prime window with headroom shrinking to
0.8% at the p=3 threshold. This is the sharp quantitative form of T1: prove
‖G^{−1/2} Q₂ G^{−1/2}‖ < 1. In CC's language this is precisely a Sonin-space
statement (their trace lower bound is a bound on G from below; what is needed is the
companion upper bound on the prime transfer in that metric).

## Discovery: just-in-time rescue by the next prime

At L = 0.580 (past the p=3 threshold): μ = **−1.050** — with G ≻ 0 this means
**G + Q₂ alone is indefinite** — yet the full form G + Q₂ + Q₃ has
λ_min = +0.000245 ≥ 0. The p=3 term restores the positivity that the p=2-truncated
form has already lost. So: *single-prime truncations of the Weil form go indefinite
almost immediately beyond their own window, and each successive prime term arrives
just in time to rescue positivity.* Collective interference among the prime terms is
load-bearing from the second prime onward — the quadratic-form face of "the Euler
product must enter," and of the convergence mechanism behind the CCM zeta spectral
triples (finite Euler products ↔ truncated forms; their spectral convergence ↔ the
rescue cascade continuing forever). A proof of RH along this axis is exactly the
statement that the rescue cascade never fails.

## Completion-criticality (rescue cascade, quantified)

`rescue_cascade.txt`: λ_min of G + Σ_{n≤m} Q_n as prime powers accumulate, per L:

```
L=0.60: arch −0.00039 → +2: −0.04300 → +3: +0.00008
L=0.80: arch −0.29495 → +2: −0.24677 → +3: −0.09522 → +4: +0.00000
L=1.00: arch −0.52824 → … → +5: −0.09489 → +7: −0.00000
L=1.20: arch −0.72493 → … → +8: −0.18545 → +9: −0.00000 → +11: −0.00000
```

Three exact-looking regularities (numerical, N=48, resolution ~10⁻⁵):
1. **Every proper truncation is strictly indefinite** — often by large margins
   (−0.1 … −0.5) — including the two-prime truncations well inside their windows.
2. **Individual prime powers are non-monotone**: adding n=4 at L=1.20 *lowers*
   λ_min (−0.409 → −0.490); adding n=2 at L=0.60 lowers it. There is no term-by-term
   positivity mechanism; only the complete sum works.
3. **Adding the LAST in-window prime power lands λ_min at 0 to 5–6 digits, at every
   window tested** ("completion-criticality"): the explicit-formula weights
   (log p)p^{−k/2} are exactly the weights that complete each window to the boundary
   of positivity. Consistent with exact criticality (inf = 0 for each L ≳ 0.6) or
   with positivity that is merely below our 10⁻⁵ resolution; either way the
   one-parameter family of completed-window forms rides the null boundary uniformly
   in L — a finite-window face of Λ = 0 sharpness, and a natural induction target:
   positivity propagates from window to window with zero slack, each threshold
   crossing paid for exactly by the arriving prime.

## Certified Result 1 (rigorous, computer-assisted; Arb ball arithmetic)

**Statement.** Let L = 0.45, φ_k(u) = sin(kπ(u+L)/(2L))/√L for k = 1…16 (supported
in [−L, L]), and let Q ∈ ℝ^{16×14} be the explicit matrix computed in
`certify_L045.py` (approximate null space of the two pole functionals; stored
exactly as float64). Then for every f in the 14-dimensional family
{Σ c_a (Qφ)_a : c ∈ ℝ^{14}}:

W(f) := 2h_f(i/2) + (1/2π)∫ h_f(r)Ω(r)dr − √2 log 2 · g_f(log 2) **≥ 0.072606 ‖f‖²**,

where the window admits exactly one prime power (n = 2, since e^{2L} ≈ 2.46).
By the Riemann–Weil explicit formula (valid for these test functions: h entire,
O(r⁻⁴) in the strip), the left side equals Σ_ρ ĥ_f(ρ) over the nontrivial zeta
zeros — so the zero-sum functional is certifiably coercive on this family.

**Method** (all steps carry rigorous enclosures): archimedean entries by Arb
verified integration of the regularized closed form (sinc representation removes
the removable singularities; the kernel is used in its *analytic symmetrization*
(ψ(¼+ir/2)+ψ(¼−ir/2))/2 − log π, required for soundness of Arb's integration) on
[0, 800] plus an explicit tail bound; prime and pole entries by verified 1-D
integration; the final bound by Cholesky factorization executed in ball arithmetic
(all pivots certified positive). Float eigenvalue estimate 0.080673; certified
constant 0.072606. Runtime 56 s on a Raspberry Pi 5. Output: `certify_L045_output.txt`.

**What it is and is not.** It is — to our knowledge — the first *rigorous*
positivity statement for the Weil functional in a window with an active prime term
beyond the ratio-2 (Connes–Consani) regime, in the cancellative zone where
norm-perturbation arguments provably fail (deficit 0.490 > margin 0.291 here). It
is NOT T1: the family is 14-dimensional, not all of L²[−L, L]; extending the
certificate to the full space is exactly the open analytic content (the
sharpened target below). Soundness rests on Arb/python-flint and the ~150-line
pipeline, all committed.

**Sharpened analytic target from the μ-extremal structure** (`mu_extremal.txt`):
the worst relative direction is a mixed core/dipole mode with spectral mass parked
in the "cheap band" r ∈ (2π, γ₁) — above the negative archimedean valley, below the
first zero — realizing ≈83% of its Lemma-1-allowed prime correlation. T1 reduces to
an uncertainty-type statement: *a function of support 2L ≤ log 3 cannot be spectrally
concentrated below γ₁ and simultaneously saturate its autocorrelation at lag log 2.*

## Honest status

- Lemma 1: proven, sharp, confirmed by two independent numerical measurements.
- Certified Result 1: rigorous on an explicit 14-dim family (above).
- v1 spatial-block criterion: refuted (documented above) — real information about
  where the difficulty is NOT.
- v2 invariant μ: exact reformulation of T1; numerically true with quantified
  headroom; open as a theorem. The needed inequality is archimedean-metric control
  of a single explicit rank-structured operator.
- Just-in-time rescue + completion-criticality: new observed structure — truncations
  are indefinite, completions are critical, term-by-term monotonicity is false. The
  object to control is the *completed-window* family as a whole (equivalently the
  multi-prime μ), not individual prime perturbations.
- Nothing here proves RH, and none of it is claimed to.
