# EPSILON-N: certified verification of the CCM Theorem 1.1 hypotheses on finite sections

*2026-08-11. Lead 2 of `LEADS.md` executed: the ε_N certification service to the
Connes–Consani–Moscovici program. Pipeline: `epsilonN_certify.py` (reuses the
verified-integration core of `certify.py` by inheritance); outputs
`epsilonN_L*_output.txt`. Everything labeled **certified** is a
computer-assisted rigorous statement in Arb ball arithmetic; float quantities
are heuristics only and are never trusted by the certificates.*

## 1. What CCM assume, verbatim

CCM 2025 ("Zeta Spectral Triples", arXiv:2511.22755) build their self-adjoint
operators D_log^{(λ,N)} from the restriction QW_λ^N of the Weil quadratic form
to the span of the 2N+1 lowest scaling-operator eigenfunctions V_n on
[λ^{-1}, λ]. From their §1 (p. 2):

> "We need to verify that the smallest eigenvalue ε_N of QW_λ^N is simple and
> that the corresponding eigenfunction is 'even', i.e. invariant under the
> symmetry u ↦ u^{-1}."

and Theorem 1.1 opens:

> "Let ε_N be the smallest eigenvalue of QW_λ^N **assumed simple** and ξ the
> corresponding eigenvector **assumed even**, normalized by δ_N(ξ) = 1."

Self-adjointness of D_log^{(λ,N)} — the property that puts their approximate
zeta zeros on the critical line — is then built on the metric
QW_λ^N − ε_N⟨·|·⟩ (Thm 1.1(i)). The two hypotheses are nowhere verified in
the paper (their numerics use them implicitly). Their Prop. 3.4 (quoting
[4, Prop. 2.3]) is what makes finite sections the right objects:

> "The space E is a core for the quadratic form QW_λ [...] In particular, the
> lower bound of QW is the limit, when N → ∞, of the smallest eigenvalue of
> the restriction of QW to the linear span E'_N of the functions V_k with
> |k| ≤ N."

And their eq. (3.19) identifies QW_λ with exactly the form this laboratory
certifies (GAPS.md, Gap 3 resolution): archimedean kernel
2∂_t θ(t) = Re ψ(¼+it/2) − log π (our Ω), pole term 2ℜ(f̂(i/2) conj f̂(−i/2)),
prime terms −Λ(n)⟨f|T(n)f⟩ = −2Λ(n)n^{-1/2}g_f(log n) for real f.

**This document certifies the sign, the simplicity, and the evenness of the
smallest eigenvalue of finite sections of QW_λ in five concrete windows —
the two assumed hypotheses of CCM Theorem 1.1, plus the sign their
Carathéodory–Fejér mechanism is deliberately agnostic about.**

## 2. Dictionary and the two section conventions

Log coordinates: u = log x maps [λ^{-1}, λ] with d*x to [−L, L] with du, where
**L = log λ**; the CCM inversion u ↦ u^{-1} becomes the parity u ↦ −u. Our
sections are the Dirichlet sine spans of `T1-ARCHITECTURE.md`:
φ_k(u) = sin(kπ(u+L)/(2L))/√L, k = 1..N — an orthonormal basis of L²[−L, L]
(CCM's V_n are the periodic exponentials; both families exhaust L² as N → ∞,
and both spans are inversion-invariant, so the hypotheses verified here are
the same-species statements for the sine sections). Two problems per window:

- **[U] unconstrained sections** — the direct analogue of QW_λ^N: the full
  form, pole term included, on span{φ_1..φ_N}. Its smallest eigenvalue is
  the ε_N below (the CCM-convention object).
- **[C] pole-constrained family** — the T1 laboratory convention
  (certify.py): the explicit float projection Q onto the (float-accurate)
  null space of the two pole functionals F(±i/2), with the pole term retained
  in the form so the certificate covers the explicit family exactly as in
  certify.py.

All in-window prime powers n < e^{2L} are included, with the same verified
prime entries, the same analytically-symmetrized digamma kernel with verified
integration on [0, R] plus the same explicit tail bound (here per-entry R),
and the same ball Cholesky as `certify.py` — the verified core is reused by
inheritance, not rewritten.

## 3. Exact parity structure (the constraint/parity interaction, stated precisely)

All proofs are 2–4 lines and are exact mathematics for the exact family φ_k.
The pipeline uses ball enclosures of the frequencies w_k = kπ/(2L), so the
certified matrices enclose the true ones; with double-precision frequencies
the statements below would hold only to ~10⁻¹⁶. (Verified numerically at the
head of every output file: the relevant balls all contain 0.)

- **(P1)** φ_k(−u) = (−1)^{k+1} φ_k(u): sin(w_k(L∓u)) = sin(kπ/2 ∓ w_k u),
  expand. So k odd ⇒ even parity, k even ⇒ odd parity: an N/2 + N/2 split.
- **(P2)** The archimedean form commutes with parity; entries with i+j odd
  vanish (already exact zeros in certify.py: for opposite parity, F_i F̄_j is
  pointwise purely imaginary).
- **(P3)** The prime form commutes with parity: for real f the
  autocorrelation satisfies g_{f(−·)}(a) = g_f(−a) = g_f(a); polarizing, the
  symmetrized bilinear form b_a obeys b_a(f(−·), g(−·)) = b_a(f, g), so
  opposite-parity entries equal their own negatives, i.e. vanish.
- **(P4) The two pole constraints are NOT both even-sector functionals.**
  With vp_k = ∫φ_k e^{u/2}, vm_k = ∫φ_k e^{−u/2}: change of variables gives
  vm_k = (−1)^{k+1} vp_k. Hence span{vp, vm} = span{v₊, v₋} where
  v₊_k = ∫φ_k cosh(u/2) (supported on k odd — one even-sector constraint) and
  v₋_k = ∫φ_k sinh(u/2) (supported on k even — one odd-sector constraint).
  Moreover the pole rank-two term decomposes exactly:
  vp⊗vm + vm⊗vp = 2(v₊⊗v₊ − v₋⊗v₋) —
  **positive rank-one in the even sector, negative rank-one in the odd.**

Consequently W_N = W_even ⊕ W_odd exactly, in both conventions; the
constrained space splits as (even ∩ ker v₊) ⊕ (odd ∩ ker v₋) with dimensions
(N/2 − 1) + (N/2 − 1); and "the minimizing eigenvector is even" is the exact
statement λ_min(even block) < λ_min(odd block) — evenness is certified as a
strict inequality between two rigorously enclosed numbers, not as an
approximate symmetry of a float vector.

## 4. Certification method

Per parity block (ball matrix M, Gram S): float spectral decomposition Y of
(mid M, mid S) — heuristic; ball congruences D = YᵀMY, E = YᵀSY; rigorous
row-sum bound δ ≥ ‖E − I‖; Gershgorin discs of D (a connected component of k
discs contains exactly k eigenvalues); pencil correction
λ_i(M,S) ∈ [λ_i(D)/(1+δ), λ_i(D)/(1−δ)] (sign-adjusted endpoints; valid by
Courant–Fischer applied to pointwise monotone Rayleigh-quotient bounds); one
Jacobi-type refinement (re-diagonalize mid D, fold into Y) if the lowest disc
is not isolated. Independent sign certificate: ball Cholesky of M − cS
(verbatim `chol_pd` from certify.py) at a ladder of c, the same c on both
sectors. All ball→float post-processing uses directed bounds
(arb upper/lower/abs_upper) inflated by a relative 10⁻¹³.

Certified claims per window: (a) **sign** of ε_N — enclosure and Cholesky
floor; (b) **simplicity** — the lowest disc is a singleton strictly below
every other disc in both sectors, with a certified gap to λ₂; (c)
**evenness** — the minimizer's sector, by strict inequality between the two
sector minima.

## 5. Certified results

N = 24 (sectors 12+12; constrained family 22-dim), dps = 25, per-entry tail
target 10⁻⁹ (escalated to 10⁻¹¹ at L = 0.60 and 3·10⁻¹² at L = 0.62 to
resolve the [U] sign; verified integration there runs to R ≈ 1.5·10⁵ and
2.2·10⁵). All windows include all in-window prime powers. Enclosures are
certified; "gap" is the certified lower bound on λ₂ − λ₁ over the union of
both sectors. Runtimes: 38–47 s per window at tail 10⁻⁹, 91/97 s for the two
escalations (7 worker processes, 8-vCPU VPS).

### [U] Unconstrained sections — the CCM-convention ε_N. λ = e^L.

| L | primes | certified ε_N enclosure | sign | simple | gap λ₂−λ₁ ≥ | sector | Cholesky floor |
|---|---|---|---|---|---|---|---|
| 0.450 | {2} | [1.9536e-5, 1.9600e-5] | + | yes | 2.8878e-3 | **EVEN** | 1.9177e-5 |
| 0.500 | {2} | [1.0578e-6, 1.1123e-6] | + | yes | 2.4294e-4 | **EVEN** | 1.0578e-6 |
| 0.545 | {2} | [5.9952e-8, 1.1899e-7] | + | yes | 2.2535e-5 | **EVEN** | 5.9952e-8 |
| 0.600 | {2,3} | [1.7416e-9, 2.4101e-9] | + | yes | 7.0625e-7 | **EVEN** | 1.4241e-9 |
| 0.620 | {2,3} | [4.1816e-10, 6.2646e-10] | + | yes | 1.7827e-7 | **EVEN** | 2.5081e-10 |

### [C] Pole-constrained family — T1 convention (22-dim explicit family)

| L | certified ε enclosure | sign | simple | gap λ₂−λ₁ ≥ | sector | Cholesky floor |
|---|---|---|---|---|---|---|
| 0.450 | [7.65437e-2, 7.65438e-2] | + | yes | 4.5122e-1 | **EVEN** | 7.5013e-2 |
| 0.500 | [1.50109e-2, 1.50110e-2] | + | yes | 2.0282e-1 | **EVEN** | 1.4711e-2 |
| 0.545 | [1.38311e-3, 1.38320e-3] | + | yes | 5.7828e-2 | **EVEN** | 1.3555e-3 |
| 0.600 | [8.2536e-5, 8.2626e-5] | + | yes | 4.3516e-3 | **EVEN** | 8.0930e-5 |
| 0.620 | [2.2868e-5, 2.2963e-5] | + | yes | 1.4990e-3 | **EVEN** | 2.2457e-5 |

### Cross-checks (L = 0.545)

- **N = 16 validation**: [C] ε ∈ [1.42792e-3, 1.42797e-3] — reproduces
  certify.py's independently computed float λ_min 0.001428 on the same
  14-dim family and sharpens the published Cholesky constant 0.001285.
- **N = 32**: [U] ε ∈ [5.957e-8, 1.365e-7]; [C] ε ∈ [1.32719e-3, 1.32733e-3]
  — tracks Certified Result 6's 30-dim scaling value (float ≈ 1.33e-3).
- **N-saturation**: ε barely moves through N = 16 → 24 → 32 in both
  conventions — the low spectrum of the sections is already converged in the
  family dimension; the window length L, not N, is the active parameter.
- The [C] values reproduce the certified positivity curve (N = 16, certify.py)
  and rescue_certify's L = 0.62 constant (2.0624e-5 ≤ our [2.2868e-5,
  2.2963e-5] with the Cholesky ladder accounting for the difference).

## 6. Relation to CCM Theorem 1.1 — precisely

**Certified: for the sine-basis finite sections of QW_λ at λ = e^L in the
five windows above, the smallest eigenvalue ε_N is (i) strictly positive,
(ii) simple with an explicit certified spectral gap, and (iii) even — its
eigenvector lies in the sector invariant under u ↦ u^{-1}.** These are the
hypotheses CCM Theorem 1.1 assumes, verified for concrete finite sections in
the concrete windows where this laboratory's certified positivity curve
lives — including both two-prime windows past the Connes–Consani ratio-2
regime.

A full-space corollary with **no N→∞ caveat**: span{φ_k} ⊂ L²([λ^{-1},λ],
d*u), so each certified upper edge bounds CCM's full-space infimum µ_λ
(their Cor. 3.7) from above, and their monotonicity (3.27), µ_λ ≤ µ_λ' for
λ ≥ λ', propagates it forward:

> **µ_λ ≤ 6.2646·10⁻¹⁰ for every λ ≥ e^{0.62} ≈ 1.8589** (no lower bound on
> µ_λ is claimed).

Their Cor. 3.8 states that µ_λ → 0 as λ → ∞ implies RH; the certified
sections show µ_λ is within 10⁻⁹ of its conjectured limit 0 already at
λ < 2, from above.

Honest caveats:

1. **Finite sections only.** CCM's hypotheses concern their QW_λ^N on the
   V_n-span. We verify the same-species hypotheses for the sine sections at
   explicit (L, N). Prop. 3.4's lim-inf mechanism makes both section families
   compute the same full-space infimum, but nothing here controls simplicity
   or evenness *in the limit* N → ∞, nor identifies our N with theirs.
2. **Basis convention.** Their sections are (2N+1)-dimensional periodic
   exponential spans; ours are N-dimensional Dirichlet sine spans. Both are
   inversion-invariant subspaces of the same Hilbert space carrying the same
   form (their eq. 3.19), so "simple + even minimizer" is the identical
   structural hypothesis; the numerical values of ε_N differ between
   conventions.
3. **Explicit dyadic data.** As in certify.py, the prime lag is the double
   fl(log n) and the window half-length the double fl(L); the certified
   statement is about the explicit form with these dyadic constants (the
   perturbation to the ideal constants is ~10⁻¹⁶, far below every certified
   margin, but is not itself certified).
4. The certified positivity of ε_N is machine-checked finite-section Weil
   positivity — it is not new evidence for RH beyond the known zero
   verifications, and is not claimed to be.

## 7. Findings and surprises

- **The unconstrained sections ride the zero boundary.** ε_N^U falls five
  orders of magnitude across the grid (1.96e-5 → 5e-10) with local log-slope
  d(log ε)/dL ≈ 58 → 69 — the same accelerating-decay envelope as the
  full-space completed-window curve (Gap 4 refutation data). The sections
  see the full-space infimum riding 0; certifying the sign at L = 0.62 means
  certifying a 4·10⁻¹⁰ eigenvalue of a matrix with O(1) entries — done with
  per-entry tails of 3·10⁻¹², the tightest certificate in this repo.
- **CCM's simplicity hypothesis is true but asymptotically marginal.** The
  certified gap λ₂ − λ₁ shrinks four orders of magnitude across the grid
  (2.9e-3 → 1.8e-7). λ₂ is always the *odd-sector ground state*, and both
  sector minima plunge toward 0 with λ₂/λ₁ rising toward ≈ 350: the even
  and odd sectors approach the zero boundary together. Extrapolating, the
  spectral gap CCM's construction rests on closes as λ grows — their
  hypotheses hold in every window we can reach, but with vanishing margin.
  This is quantitative information their program will need.
- **Evenness holds despite a structural handicap.** By (P4) the pole term is
  *negative* rank-one in the odd sector and positive rank-one in the even
  sector — a mechanism that could have made the minimizer odd. Certified: it
  never does; the even-sector minimum stays 2–4 orders below the odd one in
  [C] and a factor ~350 below in [U].
- **The pole constraints are what keep the laboratory's curve large.**
  ε^C / ε^U ≈ 4·10³ – 4·10⁴ per window: the CCM ε_N is tiny *because* the
  unconstrained sections contain near-null directions approaching the
  full-space infimum; the two pole constraints (one per parity sector — the
  precise statement (P4), correcting the naive expectation that both
  constraints are even) remove exactly those directions.
- **Correction found during verification:** the working hypothesis that
  "ĝ(0) and ĝ(i/2) constraints are even-sector functionals" is FALSE as
  stated — the constraint pair splits one-per-sector (P4). The even/odd
  block decomposition claimed in Lead 2 survives, but with dimensions
  (N/2 − 1) + (N/2 − 1) rather than (N/2 − 2) + N/2.
