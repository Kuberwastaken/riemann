# Orbit drag: primes-only vs full prime-power Weil positivity (Lead 5)

*Executed 2026-08-11 on ai-vps. Engine: `weil_form.py` unchanged (N=48 orthonormal
sine basis on [−L, L], pole directions projected out by the two constraints);
harness: `orbit_drag.py`; data: `orbit_drag_output.txt`; figure: `orbit_drag.png`.
Harness sanity: the three `rescue_cascade.txt` rows (L = 0.60, 0.80, 1.20) are
reproduced to < 5×10⁻⁶ per entry (`orbit_drag.py sanity`).*

## Question

The prime side of the Weil form is a sum over prime powers n = p^k < e^{2L} with
weights −2Λ(n)n^{−1/2}S(log n). Selberg-orbit language: k = 1 terms are primitive
orbits, k ≥ 2 terms are repeated orbits; Chebyshev language: the k ≥ 2 sub-sum is
the quadratic-form face of ψ − θ. LEADS.md Lead 5 conjectured, from the single
observation that adding n = 4 at L = 1.20 lowers λ_min, that the k ≥ 2 terms
*hurt* positivity — so that primes-only positivity might extend strictly further
than full positivity, giving RH a "primes-only + bounded k ≥ 2 correction"
reformulation. This experiment measures that directly:

- **λ_full(L)** — λ_min of G + Σ_{n=p^k} Q_n (all orbits), constrained subspace
- **λ_primes(L)** — same with k = 1 terms only
- **λ_k≤2(L)** — same with k ≤ 2 terms only (primes + prime squares)
- **drag Δ(L) = λ_primes − λ_full**

## Main table (N = 48; resolution ~10⁻⁵)

| L | λ_arch | λ_full | λ_primes | λ_k≤2 | drag Δ | k≥2 orbits in window |
|------|----------|-----------|-----------|-----------|-----------|----|
| 0.60 | −0.000385 | +0.000078 | +0.000078 | +0.000078 | 0 | — |
| 0.65 | −0.081888 | +0.000003 | +0.000003 | +0.000003 | 0 | — |
| 0.70 | −0.157622 | +0.000000 | +0.000000 | +0.000000 | +0.000000 | 4 |
| 0.75 | −0.228417 | +0.000000 | −0.055546 | +0.000000 | −0.055546 | 4 |
| 0.80 | −0.294947 | +0.000000 | −0.095220 | +0.000000 | −0.095220 | 4 |
| 0.85 | −0.357767 | +0.000000 | −0.143677 | +0.000000 | −0.143677 | 4 |
| 0.90 | −0.417339 | +0.000000 | −0.261406 | +0.000000 | −0.261406 | 4 |
| 0.95 | −0.474052 | +0.000000 | −0.315976 | +0.000000 | −0.315976 | 4 |
| 1.00 | −0.528239 | −0.000000 | −0.329369 | −0.000000 | −0.329369 | 4 |
| 1.05 | −0.580186 | −0.000000 | −0.337204 | −0.000010 | −0.337204 | 4, 8 |
| 1.10 | −0.630142 | −0.000000 | −0.347832 | −0.101605 | −0.347832 | 4, 8, 9 |
| 1.20 | −0.724929 | −0.000000 | −0.476465 | −0.174086 | −0.476465 | 4, 8, 9 |
| 1.30 | −0.814054 | −0.000000 | −0.635663 | −0.188280 | −0.635663 | 4, 8, 9 |
| 1.40 | −0.898675 | −0.000000 | −0.700660 | −0.242254 | −0.700660 | …, 16 |
| 1.50 | −0.979728 | −0.000000 | −0.714161 | −0.296509 | −0.714161 | …, 16 |
| 1.60 | −1.057978 | −0.000000 | −0.747665 | −0.335619 | −0.747665 | …, 16 |
| 1.70 | −1.134059 | −0.000000 | −0.756376 | −0.349083 | −0.756376 | …, 25, 27 |
| 1.80 | −1.208497 | −0.000000 | −0.808425 | −0.378733 | −0.808425 | …, 32 |
| 1.90 | −1.281728 | −0.000000 | −0.970274 | −0.423458 | −0.970274 | …, 32 |
| 2.00 | −1.354111 | −0.000000 | −1.011218 | −0.465515 | −1.011218 | …, 49 |

(Full 0.05-grid in `orbit_drag_output.txt`; the omitted rows interpolate
smoothly. λ_full: |λ| < 10⁻⁶ at every grid point with L ≥ 0.70.)

![orbit_drag](orbit_drag.png)

## Findings

**1. Lead 5's hypothesis is refuted — with the sign reversed.** Primes-only
positivity does not extend further than full positivity; it *collapses almost
immediately* once the first repeated orbit exists. λ_primes stays pinned on the
zero shelf (|λ| < 10⁻⁶) through L ≈ 0.703, is measurably negative by L = 0.706
(−1×10⁻⁶) and clearly so by 0.7125 (−2.2×10⁻⁵): the departure point is
**L\* = 0.705 ± 0.005**, only ~0.012 beyond the n = 4 threshold
½log 4 = log 2 ≈ 0.6931. From there λ_primes falls monotonically (all 26 grid
steps strictly decreasing) to **−1.011 at L = 2.00**. Since λ_full ≈ 0
throughout, the drag Δ = λ_primes − λ_full is negative and monotone: the
repeated orbits are not a drag on positivity — **they are load-bearing
rescuers**, exactly like the primes in the rescue cascade. (The n = 4-at-L = 1.20
observation that seeded the lead was a fact about cascade *ordering*, not about
the orbit's net role.)

**2. The seam is a hierarchy: every k-truncation fails just past its first
missing orbit.** λ_k≤2 repeats the pattern one level up: it is pinned at 0
while it coincides with the full form, first goes negative at the n = 8
threshold ½log 8 ≈ 1.0397 (at L = 1.05 it reads −1.0×10⁻⁵, its first negative
grid value), and decays to −0.4655 by L = 2.00. So *truncation-in-k behaves
exactly like the truncation-in-n cascade of T1-ARCHITECTURE.md*: any proper
sub-sum of the explicit-formula orbit sum loses positivity within ~0.01 of the
threshold where it first differs from the complete sum, and never recovers.

**3. Completion-criticality is a full-sum phenomenon only.** λ_full = 0 to
< 10⁻⁶ at *every* grid L in [0.70, 2.00] — mid-window as much as at completed
windows. λ_primes and λ_k≤2 share the pinning only trivially, on the range where
they equal the full sum (plus the ~0.01 overhang). Answer to the question posed:
completion-criticality is **not** a primes-only phenomenon; it is the signature
of the complete Λ(n) weight system and of nothing smaller.

**4. Single-orbit ablations saturate the norm bound — with one telling
anomaly.** Since λ_full ≈ 0, dropping one orbit obeys
λ_min(full − Q_n) ≥ −‖Q_n‖, and the saturated orbit norm is
‖Q_n‖ = Λ(n)/√n (shift-overlap norm → ½; cf. RESULTS.md for n = 2). Measured
(N = 48):

| L | full | drop n=4 | drop n=8 | drop n=9 | k≤2 only | primes only |
|------|-----------|-----------|-----------|-----------|-----------|-----------|
| 0.80 | +0.000000 | −0.095220 | — | — | +0.000000 | −0.095220 |
| 1.20 | −0.000000 | −0.345944 | −0.174086 | −0.185453 | −0.174086 | −0.476465 |
| 1.60 | −0.000000 | −0.468974 | −0.245011 | −0.365249 | −0.335619 | −0.747665 |
| 2.00 | −0.000000 | −0.490124 | −0.245065 | −0.366204 | −0.465515 | −1.011218 |

At L = 2.00: drop-8 → −0.245065 vs −Λ(8)/√8 = −0.245053; drop-9 → −0.366204 vs
−Λ(9)/√9 = −0.366204 (match within resolution). The bound is *exactly*
saturated: the ablated form's minimizer is the dropped orbit's own extremal
vector, and the complete-sum form vanishes on it — the full form's near-null
space is rich enough to contain every single orbit's worst direction. The
anomaly: drop-4 → −0.490124 ≈ −Λ(2)/√2 = −0.490129, i.e. the *n = 2 norm*, not
−Λ(4)/√4 = −0.3466 (which it does sit near at L = 1.20 before deepening).
Removing the 4-orbit frees a direction worth the full primitive-2-orbit norm:
lags log 2 and log 4 live on the same log-2 lattice, and the comb that beats
against Q₂ is only disciplined when Q₄ is present. Repeated orbits of p
resonate with the primitive orbit of p; orbits of distinct primes don't show
this (8- and 9-drops are pure single-orbit effects at large L).

**5. Magnitude: the ψ − θ term carries an O(L) share of the positivity
budget.** In counting terms ψ(x) − θ(x) = Σ_{k≥2} θ(x^{1/k}) ≍ √x is
negligible. But the explicit-formula weight Λ(n)n^{−1/2} exactly cancels that
sparsity: the in-window k ≥ 2 weight mass is Σ_{p^k<e^{2L}, k≥2} Λ(n)/√n ≈
Σ_{p<e^L} log p/p ~ L (Mertens) — it *grows* with the window. The measured drag
tracks this: |Δ| grows ≈ linearly beyond L ≈ 1.2 (−0.48 → −1.01 over
L = 1.2 → 2.0), running at ≈ 49% of the crude norm bound
Σ_{k≥2}‖Q_n‖ = 2.065 at L = 2.00. In the Weil-positivity metric the Chebyshev
discrepancy is **not a small correction**: RH-positivity genuinely lives in ψ
(von Mangoldt weights), not in θ (primes alone).

## Verdict on the Lead-5 reformulation

The strong form — "RH ⟺ primes-only positivity + explicitly bounded k ≥ 2
correction" with primes-only positivity extending *further* — is dead:
primes-only positivity is simply **false** for L ≳ 0.705 (unconditional
numerics; all heights involved carry verified zeros). What the data leaves
standing is the reversed and sharper statement:

- the primes-only form is bounded below by −Σ_{k≥2}‖Q_n‖ = −Σ Λ(n)/√n
  (a ~L-growth, θ-vs-ψ bound), and empirically sits at about half that bound;
- the k ≥ 2 terms must supply the *entire* lift back to zero, and do — to
  < 10⁻⁶, at every L;
- **seam law (new, quantitative):** every k-level truncation of the orbit sum
  rides the null boundary exactly while it coincides with the full sum, then
  fails within ΔL ≈ 0.01 of its first missing orbit's threshold. Positivity is
  a property of the complete weight system Λ(n)n^{−1/2} and of no sub-system —
  now measured across the k-hierarchy, not just the n-cascade.

## Numerical caveats

- N = 48 finite section, λ resolution ~10⁻⁵ (harness validated against
  `rescue_cascade.txt` to < 5×10⁻⁶ per entry).
- N = 64 convergence: λ_primes shifts by ≤ 5×10⁻⁴ (0.80: −0.095220 → −0.095704;
  1.40: −0.700660 → −0.701190; 2.00: −1.011218 → −1.011384); λ_full stays 0
  within 3×10⁻⁶. No conclusion above depends on shifts of this size; the exact
  ablation-saturation matches are quoted at the 10⁻⁵ resolution limit.
- "λ_full = 0" means |λ_full| < 10⁻⁶: exact criticality vs positivity below
  resolution is not distinguishable here (same caveat as RESULTS.md).
- The L\* = 0.705 departure point is a detachment from a ~10⁻⁶ shelf, localized
  by bisection to [0.703, 0.713] at the 10⁻⁵ level.

## Reproduce

```
.venv/bin/python orbit_drag.py sanity   # rescue_cascade rows, PASS/FAIL
.venv/bin/python orbit_drag.py sweep    # ~2 min -> orbit_drag_output.txt
.venv/bin/python orbit_drag.py plot     # -> orbit_drag.png
```
