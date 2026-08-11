# R1 — the CvS prime-cutoff coordinate: S1's obstacle-(a) machinery transplanted to the θ_x family

*2026-08-11, cycle-2 RESERVE agent R1. Target (RESET-1 RESERVE): attack the sole
hypothesis of the published Connes–van Suijlekom theorem (simple + even ground
state ⇒ real ξ̂-zeros) in the prime-cutoff coordinate, with S1's crossing
technology. Sources: papers/criteria/ConnesVanSuijlekom-2025-real-zeros-general.pdf
(arXiv:2511.23257v1, 28 Nov 2025; repo cite CMP 406:312), threshold-work/S1-sector.md,
FRONTIER.md, DEAD-ENDS.md. No RH assumed. Labels: PROVED / DERIVED / HEURISTIC /
NUMERICAL / REFUTED.*

---

## 0. What the paper actually contains [checked against the PDF]

**CvS Theorem 6.1 (= Thm 1.2).** L > 0, 𝒟 a real distribution on [0, L], 𝒟̃ its
even symmetrization on [−L, L] (their (4)), Q the hermitian form
⟨f|g⟩_Q = 𝒟̃(f^∗ ∗ g) on trigonometric polynomials of L²[0, L] (their (6)–(7);
equivalently, Prop A.3(ii): Schwartz kernel 𝒟̃(x−y) on L²([−L/2, L/2])). If Q
defines a lower-bounded essentially self-adjoint operator whose spectral minimum
is a **simple, isolated** eigenvalue with **even** eigenfunction ξ, then every
zero of the entire function ξ̂(z) is real.

Proof route: Carathéodory–Fejér corollary (Toeplitz kernel ⇒ roots on the unit
circle, §2) → continuous kernel case (§3) → finite **Fourier truncations**
q_{i,j} = (b_i − b_j)/(i − j), a_i on the diagonal, i, j ∈ {−N,…,N} (Prop 4.2 —
the divided-difference/spectral-action structure) → real-roots theorem for those
matrices (Thm 5.6, via the anti-commuting parity γ and the rank-one-modified
D′ = D − |Dξ⟩⟨η| made Q-self-adjoint) → Hurwitz. Two remarks we will use:
Remark 2.3 (non-simple case: only the **common** zeros of the kernel
eigenfunctions are forced to the circle — the radical version), Remark 4.3 (one
must start from 𝒟 on [0, L], not from an even distribution on [−L, L]).

**Honesty note [checked, full text].** The paper contains **no θ_x prime-cutoff
family**. Its only truncation family is the *Fourier* truncation {−N,…,N}; its
only zeta content is motivational (§1). "The prime-cutoff θ_x coordinate" of
RESET-1/evaluator D is a *repo-side instantiation*: what the paper publishes is
the criterion for **arbitrary real 𝒟** — and that generality is exactly what
licenses an Euler-cutoff family, because a prime-truncated Weil distribution is
still a real distribution, while CCM 2025 Thm 1.1 (Weil-specific) never covered
it. The genuine literature delta is therefore: *real-zero conclusions become
available for Euler-deficient truncations — objects with no ζ interpretation.*

## 1. The dictionary [PROVED, bookkeeping]

Repo window family (S1 §0) vs CvS coordinates:

| repo (S1 / CCM / Suzuki) | CvS (2511.23257) |
|---|---|
| window (−a, a), operator A-frame on L²(−a,a) | L²([−L/2, L/2]), kernel 𝒟̃(x−y): **L = 2a** (= 2 log λ, CCM λ = e^a) |
| kernel probes t = x−y ∈ (−2a, 2a) | 𝒟̃ on [−L, L] ✓ same reach |
| Weil data: Ω-multiplier part + pole kernel 2cosh(t/2) − Σ_n (Λ(n)/√n)(δ_{log n}+δ_{−log n}) | 𝒟 := restriction of the (one-sided) Weil distribution to [0, L]; symmetrization (4) restores the even kernel; δ₀-coefficient care = Remark 4.3 |
| prime content of the window: n < e^{2a} = λ² | prime powers with log n < L — **window fixes prime content** |
| obstacle (a): ε_even < ε_odd + even-sector simplicity | THE hypothesis of Thm 6.1 (simple + even minimum) |
| CCM ξ̂_λ real-zero mechanism | conclusion of Thm 6.1: ξ̂ has real zeros |
| CCM finite-N sections, N ≥ λ² diagonal | CvS's own Fourier truncation {−N,…,N} (Prop 4.2), a **third, transverse coordinate** |

**θ_x family (defined here, licensed by CvS generality).** Fix the window
a (L = 2a); for x ≥ 1 let

    𝒟_x := Ω-part + pole part − Σ_{n ≤ x} (Λ(n)/√n) δ_{log n}   on [0, 2a],
    Q_{a,x}(v) = Q^arch+pole_a(v) − Σ_{n ≤ x, log n < 2a} (2Λ(n)/√n) g_v(log n).

Coordinates: the repo's window family is the **diagonal** x = e^{2a} of the
(a, x) quarter-plane (window growth automatically adds primes); the θ_x family
is **horizontal motion** (fixed window, Euler content varies). Two structural
facts, both elementary and both load-bearing:

- **(D1) Finite path, one-sided saturation.** x ↦ Q_{a,x} is piecewise constant
  with jumps exactly at prime powers, and Q_{a,x} = Q_a^W for ALL x ≥ e^{2a}
  (δ_{log n} with log n ≥ 2a never meets the autocorrelation support). Euler
  *excess* is invisible; only Euler *deficit* x < e^{2a} is a new object. The
  whole family at window a has ≤ π*(e^{2a}) + 1 distinct members.
- **(D2) No continuity in x.** Because the path is piecewise constant, there is
  no Hurwitz/degeneracy argument along x; the honest continuous coordinate is
  the **coupling interpolation** s ∈ [0,1] of the entering prime,
  Q_{a,x⁻,s} := Q_{a,x⁻} − s·(2Λ(n)/√n) g_v(log n) — the frame in which the
  Lee–Yang/FKG challenger (C1/C2) operates.

## 2. Theorem R1.A [PROVED]: S1 Thm A transplants verbatim to every truncation

**Statement.** For every a > 0 and every x ≥ 1 let H^♮_{a,x} be the Friedrichs
operator of Q^♮_{a,x} := Q_{a,x} − pole term. Then H^♮_{a,x} has a simple,
one-signed, **even** ground state, and pole-free parity gap
γ^♮(a,x) ≥ ν(2a)‖v_o‖₁² > 0 (v_o the odd minimizer, ν(t) = e^{|t|/2}/(2 sinh|t|)).

**Proof.** S1 (F1)–(F2) are x-independent (archimedean Lévy–Khintchine + pole
algebra). The sign census (F3) and the rearrangement (A1) are **termwise in n**:
each prime term is a negative coefficient times a symmetrized translation, and
g_{|v|}(log n) ≥ g_v(log n) pointwise for each n separately; restricting the sum
to n ≤ x only *drops nonnegative defect terms*, so

  Q^♮_{a,x}(v) − Q^♮_{a,x}(|v|) ≥ 4ν(2a)‖v₊‖₁‖v₋‖₁ + Σ_{n≤x}(2Λ(n)/√n)(g_{|v|}−g_v)(log n)
                                ≥ 4ν(2a)‖v₊‖₁‖v₋‖₁.

(A2)–(A3) then run word for word: one-signed ⇒ simple ⇒ even; the odd minimizer
gives the gap. ∎

**(R1.A′) Monotonicity [PROVED].** λ^♮_{e,1}(a, x) is non-increasing in x: test
the new form on the previous (one-signed) ground state; g_φ(log n) ≥ 0 for
one-signed φ. No such statement for the odd sector — and in fact the numerics of
§4 show λ^♮_{o,1}(a, x) *increases* when a prime enters (odd functions
anti-correlate under the shift, g_{v_o}(log n) < 0, so the prime term is a
positive form on odd states). **The ferromagnetic primes repair parity in both
sectors at once: they lower the even floor and raise the odd floor.** At
a = 0.45: prime 2 moves λ^♮_{e,1} from −1.585 to −1.762 and λ^♮_{o,1} from
−0.172 to +0.021; the pole-free parity gap grows γ_arch = 1.412 → γ^♮ = 1.768.

So: for every Euler truncation, the pole-free operator is a ferromagnetic
(jump-Dirichlet + positive-amplitude-hop) form, the primes can never break
simple+even, and **CvS's hypothesis at every (a, x) is exactly the rank-two pole
vs the truncated parity gap γ^♮(a,x)** — obstacle (a) decomposes identically in
the new coordinate.

## 3. Theorem R1.B [PROVED]: the crossing criterion 𝔠_x

The pole is x-independent (it is the s(s−1)/ξ-pole part, not Euler content), so
S1 Thm B (Aronszajn–Krein on the sector rank-ones ±2w_±⊗w_±) transplants with
H^♮ replaced by H^♮_{a,x}:

  ε_even(a,x) < ε_odd(a,x) ⟺ ε_even(a,x) < λ^♮_{o,1}(a,x) and
  **𝔠_x(a) := 2⟨(H^♮_o(a,x) − ε_even(a,x))^{−1} w₋, w₋⟩ < 1.**

B1_x/B3_x hold with truncated quantities; B2 is the x = 1 member. Along x the
family is discrete (D2): a parity flip at a prime entry needs **no** degeneracy
at any member — 𝔠_x can jump across 1. In the coupling interpolation s the flip
is an honest crossing 𝔠 = 1 at some s*(a) ∈ (0,1] (eigenvalues analytic in s).

## 4. The fixed-window verdict [NUMERICAL, float Galerkin; anchors reproduce S1]

Independent rebuild of the S1 §4 recipe (sine basis 24+24, arch operator
assembled in frequency space from Ω(ξ) = Re ψ(¼+iξ/2) − log π; recipe in §6).
Anchors: γ_arch(0.45) = 1.4124 (S1: 1.410); full-content 𝔠: 0.034/0.872/
0.99900/0.9999932/1−1.1e−8 at a = 0.30/0.45/0.545/0.62/0.70 (S1: 0.032/0.862/
0.99897/0.9999927/1−1.7e−8); margin law reproduced: 1−𝔠 = 6.77e−6 vs
40·ε_odd = 6.7e−6 at a = 0.62. ε_even(0.45) = 1.85e−5 vs certified
[1.9536, 1.9600]e−5 (−5%; float, K-converged to 3 digits at K = 48→80).

**θ_x phase table** (✓ = ε_even < ε_odd; ✗ = CROSSED, odd ground state):

| a | x=1 (arch+pole) | x=2 | x=3 | x=4 (full) |
|---|---|---|---|---|
| 0.30 | ✓ 𝔠=0.034 | — | — | — |
| 0.35 | ✓ 0.1499 | ✓ 0.1488 | — | — |
| 0.38 | **✗** | ✓ 0.329 | — | — |
| 0.45 | ✗ | ✓ 0.872 | — | — |
| 0.55 | ✗ | ✓ 0.9992286 | ✓ 0.9992285 | — |
| 0.62 | ✗ | **✗** (ε_e−ε_o = +0.212) | ✓ 1−6.8e−6 | — |
| 0.70 | ✗ | ✗ | ✓ 1−6e−9 | ✓ 1−1.1e−8 |
| 0.80 | ✗ | ✗ | **✗** (+0.206) | ✓ (float floor) |

Deficit-crossing thresholds (bisection, K-robust 48→80):

  **a*₁ = 0.3737** = ½log2 + 0.0271  (arch+pole loses evenness)
  **a*₂ = 0.5606** = ½log3 + 0.0113  (arch+pole+{2} loses)
  **a*₃ = 0.7014** = ½log4 + 0.0083  (arch+pole+{2,3} loses)

Coupling interpolation at a = 0.62 (prime 3, s ∈ [0,1]): crossing at
**s* = 0.999414** — the even phase occupies the last 6·10⁻⁴ of the true von
Mangoldt coupling.

**Findings.**

1. **Every Euler-deficient truncation crosses.** For a > a*₁ the θ_x path
   *starts* in the crossed (odd-ground) phase, and for a beyond the a*_k
   ladder every proper truncation is crossed — with O(10⁻¹) gaps, not
   marginally. Evenness is restored **only at full Euler content**, and only in
   the final sliver s > s*(a) of the last prime's coupling.
2. **The window and the Euler product must match exactly.** Deficit tolerance
   δ_k = a*_k − ½log n_{k+1} shrinks: 0.027, 0.011, 0.008. Excess is invisible
   (D1); deficit kills. Obstacle (a) in this coordinate reads: *simple+even is
   an exact-matched-filter property of window vs Euler content on the diagonal
   x = e^{2a} = λ²* — the same λ² diagonal that T3 forced for the finite-section
   order of limits. [HEURISTIC mechanism for δ_k: the deficient family inherits
   the endpoint margin ≈ 40·ε_odd(½log n_{k+1}) and burns it at the missing
   threshold's T1-cubic rate Λ(n)n^{−1/2}η³, η = a − ½log n; for k = 1 the
   arch+pole family's own collapse (μ^arch_{o,1} ↓ 0 near a ≈ 0.38) dominates.]
3. **Does the fixed window tame the RH-marginality? NO — it inverts and
   relocates it.** The ∀x-at-fixed-a statement is not RH-marginal; it is simply
   **FALSE** for every a > a*₁ ≈ 0.374 (witness x = 1). The marginality
   (1−𝔠 ≈ 40·ε_odd) is not a growing-window artifact: it is the value at the
   *endpoint* of every horizontal path, and the θ_x coordinate shows the
   approach to that endpoint is from the crossed side. The S1 narrative inverts
   with the pole present: in the a-family "the primes are never the
   obstruction"; in the x-family **the primes are the rescue** — each entering
   prime lowers 𝔠 (0.1499→0.1488 at a=0.35; 0.99922859→0.99922851 at 0.55) and
   the last one flips the phase.
4. **KILL (route-level): Euler continuation as a proof strategy for obstacle
   (a).** Any scheme that feeds primes in one at a time (in x, or continuously
   in coupling s) and propagates simple+even from the archimedean end dies at
   a*₁ = 0.374: the intermediate objects have odd ground states, robustly, and
   the even phase reappears only within O(1−s*) → 0 of full coupling. Same
   arithmetic content as T2's √n-screening invisibility, seen in a new
   coordinate. (Constructively for C1/C2: the s-crossing is an honest
   Lee–Yang-style degeneracy point; its motion s*(a) → 1⁻ is the object their
   monotone-zero machinery should track.)

## 5. Provable range and unconditional yield for CvS

- **∀x at fixed a** [strongest range]: TRUE for a ≤ a*₁ ≈ 0.374; PROVED for
  a ≤ ½log2 = 0.3466 modulo S1's one archimedean lemma (family is constant in
  x there, S1 THEOREM-WITH-RANGE applies: a ≤ 0.32 analytic, ≤ 0.3466 by the
  existing per-window criteria); the strip (0.3466, a*₁) is a two-member check,
  B1_x-certifiable by the Arb pipeline. **REFUTED beyond a*₁** — no ε-weakening
  exists (the x = 1 member fails outright).
- **Endpoint member (the Weil application)**: the θ_x coordinate adds no slack —
  it is S1's 𝔠(a) < 1, RH-marginal as before. Unchanged.
- **Unconditional CvS yield**: for every pair (a, x) in the even phase —
  all x at a ≤ 0.374; x ≥ 2 for a ≤ 0.5606; x ≥ 3 for a ≤ 0.7014; the five
  certified full windows a = 0.45–0.62 (EPSILON-N) — Thm 6.1 applies and gives
  **entire functions ξ̂_{a,x} with all zeros real**, including Euler-deficient
  members with no ζ-interpretation: an unconditional Lee–Yang family indexed by
  (window, Euler content), new to the literature. Certifying the phase table's
  ✓-cells (finite resolvent evaluations) is cheap Arb work.
- **The N-quantifier collapses [DERIVED, from CvS's own proof].** The Thm 6.1
  approximation step (min-max with the isolation gap δ) shows: continuum
  simple+even at window a ⇒ simple+even for **all Fourier truncations
  N ≥ N₀(a, δ)**. So S1's per-window continuum certificate automatically covers
  CvS's entire N-diagonal — the "(λ, N ≥ λ²) obstacle-(a) scope" of RESET-1
  needs only the continuum criterion plus an effective N₀ (a concrete,
  non-RH-complete follow-up: extract N₀ explicitly from their ε < δ/2
  argument). At a crossing, Remark 2.3 is the published fallback (radical
  version: common zeros of the degenerate pair are still real) — the CvS-side
  analogue of S1's "Suzuki Thm 1.5 surviving frame".

## 6. Bookkeeping

- Numerics: `cvs_theta_scan.py` + `refine.py` (session scratchpad; float,
  HEURISTIC; not committed, per S1 precedent). Recipe: sine basis
  φ_k = sin(w_k(u+a))/√a, w_k = kπ/2a, K = 48 (24/sector; K-checked to 80);
  arch matrix in frequency space, A_{jk} = (4w_jw_k/aπ)∫₀^∞ Ω(ξ)·
  trig_j(aξ)trig_k(aξ)/((w_j²−ξ²)(w_k²−ξ²))dξ with trig = cos (even sector,
  k odd), sin (odd sector, k even) — removable singularities, graded trapezoid
  grid to ξ = 10⁵, complex digamma for Ω; prime blocks by the closed-form
  overlap ∫_ℓ^{2a} sin(w_j t)sin(w_k(t−ℓ))dt/a symmetrized (parity leak
  ≤ 8e−15); pole vectors by quadrature; 𝔠_x = 2w₋ᵀ(H^♮_o − ε_even)^{−1}w₋.
- Consistency: margin law 1−𝔠 ≈ 40·ε_odd independently reproduced (§4);
  γ_arch, λ^♮_{o,1}, ε-table match S1 §4 to 1–8% (float).
- Proposed next certificates: (i) the two-member strip (0.3466, a*₁) and the
  a*_k enclosures; (ii) the ✓-cells of the phase table (unconditional CvS
  real-zero family); (iii) effective N₀(a, δ) from the Thm 6.1 proof.
- FRONTIER/DEAD-ENDS updates left to the coordinator: candidate entries —
  RESERVE status report (θ_x = reparametrization, no new slack; route-level
  kill of Euler continuation for a > 0.374; unconditional Lee–Yang family +
  N-collapse as the positive yield).
