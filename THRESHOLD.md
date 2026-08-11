# THRESHOLD — the prime-threshold determinant evolution (first SOLVER cycle)

*Phase 0 audit done by the PI from first principles before any delegation.
Labels per SOLVER.md §7.*

## 1. Phase-0 audit of the trace-ideal claim [the claim SURVIVES, sharpened]

Frames and dictionary (COLLISION.md §0): screw frame = Suzuki's G_a on
L²(−a,a), kernel g(x−y); Weil frame = the form on f = Dv; CCM frame = the
multiplicative picture, λ = e^a. The prime-power n component of the screw
kernel is g_n(t) = Λ(n)n^{−1/2}(|t| − log n)₊ (Suzuki (1.3)); consistency
check [PROVED]: −g_n″ = Λ(n)n^{−1/2}(δ_{log n} + δ_{−log n}), so
⟨G_n v′, v′⟩ = −2Λ(n)n^{−1/2} g_v(log n) = Q_n(v) — the Weil prime term, ✓.

**Threshold operator.** For a = a_n + η, a_n = ½log n, define Δ_{n,η} on
L²(−a, a) by the kernel k(x,y) = Λ(n)n^{−1/2}(|x−y| − log n)₊.

Verified [PROVED-REPO]:
- kernel continuous, piecewise-C¹; support = two corner triangles
  {(x,y) : |x−y| ≥ log n} of leg 2η; symmetric (function of |x−y|) ⇒
  self-adjoint; real.
- NOT finite rank: on the corners k = Λn^{−1/2}(±(x−y) − log n), the positive
  part of an explicit rank-two kernel; the corner indicator destroys finite
  rank. Compact (continuous kernel, bounded domain).
- **Hilbert–Schmidt with EXACT norm** (independent re-derivation; the
  previous session's formula confirmed and sharpened — it is exact, no
  O(η/a) correction):
  ‖Δ_{n,η}‖²_HS = 2[Λ(n)n^{−1/2}]²∫₀^{2η}σ²(2η−σ)dσ = (8/3)[Λ(n)n^{−1/2}]²η⁴,
  i.e. **‖Δ_{n,η}‖_HS = √(8/3)·Λ(n)n^{−1/2}·η², exactly** (the pair-density
  2a − t equals 2η − σ exactly on the support).
- **Traceless**: the kernel vanishes on the diagonal (|x−x| − log n < 0), so
  if Δ is trace class, Tr Δ_{n,η} = 0; in every finite section the matrix
  trace is 0 exactly. [Trace-class membership: plausible via Lipschitz-kernel
  factorization; left OPEN-minor — the det₂ machinery needs only HS.]
- Raw-Weil-frame contrast [PROVED-REPO]: the same update there is
  −Λ(n)n^{−1/2}(R_n + R_n*), R_n the edge-to-edge restricted shift: a scaled
  partial isometry with infinite-dimensional initial space — non-compact.
  DEAD-ENDS #12.

## 2. The evolution has exactly two parts [structural, PROVED at the level stated]

The screw kernel g is a-independent; the family varies ONLY through the
domain [−a, a] and through which kinks of g the domain spans. Hence for any
determinant-type functional of A_a (or G_a):

    d/da (evolution) = (i) HADAMARD BOUNDARY-VARIATION FLOW — the continuous
    part, driven by the boundary values of the Green kernel as the interval
    endpoints move (classical Hadamard variation; this is where Suzuki's
    Thm 1.3 continuity lives), PLUS
    (ii) THRESHOLD ENTRIES — at a = ½log n the kernel component g_n begins to
    intersect the domain; its operator is Δ_{n,η} above, entering with
    ‖·‖_HS = √(8/3)Λ(n)n^{−1/2}η².

First-order one-threshold update [DERIVED-HEURISTIC, to be made rigorous by
agent T1]: for the relative perturbation determinant with resolvent R_a(z),

    Tr(R_a(z)Δ_{n,η}) = Λ(n)n^{−1/2}·∬_corners R_a(z;x,y)(|x−y|−log n)dxdy
                      ≈ 4Λ(n)n^{−1/2}·η²·G_a(z; a, −a)·(1 + O(η)),

the END-TO-END Green kernel between the two boundary points: *the prime p^k
measures the operator's boundary-to-boundary transport at the exact scale
where the window first spans log p^k.* If G_a(z; a, −a) carries the free
phase e^{2iaz} (to be established/refuted by agent T2), then at 2a = log n
the factor n^{iz} appears and Λ(n)n^{−1/2}·n^{±iz} = Λ(n)n^{−s},
s = ½ ∓ iz — the Euler-phase shape. HEURISTIC until the Green asymptotics
are proved; forbidden as pattern-matching per the directive — T2's task is
the derivation.

## 3. RED-TEAM EQUATION [the honest obstruction, PROVED at the level stated]

The η² suppression exists ONLY at entry. Once the window has traversed past
the threshold, the n-component's weight in g on the domain grows LINEARLY:
its restriction has kernel values up to Λ(n)n^{−1/2}(2a − log n). The bare
accumulated prime content of G_a is

    Σ_{n ≤ e^{2a}} Λ(n)n^{−1/2}(2a − log n)₊  ~  4e^{a}   (PNT),

which diverges exponentially in a and is cancelled in g ONLY against the
archimedean/pole term −4(e^{t/2}+e^{−t/2}−2) — the cancellation IS the prime
number theorem, and its quality is the PNT error term (RH-strength at the
sharpest). Therefore: **no term-by-term accumulation of threshold updates can
converge; any valid determinant evolution must couple the discrete prime
entries against the continuous Hadamard flow so that the PNT cancellation
happens inside the flow.** The convergence question is thereby reorganized —
not dissolved — into: does the det₂ evolution realize the pole-vs-prime
cancellation automatically (agent T3's target), or does it require it as an
input (in which case the route's floor is PNT-strength and its target remains
RH-strength, consistent with the wall's known height)?

## 4. Cycle assignments (SOLVER §4)

- T1 (operator theory, PROVER): validity of the relative det₂ formula across
  one threshold for the Friedrichs family A_a — domains, HS hypotheses,
  Hadamard variation for A_a; deliver the exact one-threshold update or its
  precise failure point.
- T2 (PROVER, independent): large-a asymptotics of G_a(z; a, −a) from the
  screw kernel's structure; establish or refute the e^{2iaz} phase and the
  p^k-resummation; forbidden from assuming §2's heuristic.
- T3 (COUNTEREXAMPLE HUNTER): kill the accumulation program — make §3's
  divergence rigorous against det₂ (does det₂'s removed linear term contain
  exactly the divergent part?); toy models mandatory.
- S1 (side, parallel): obstacle (a) as the sector inequality
  ε_even(λ,N) < ε_odd(λ,N) — seek a global proof mechanism (Dirichlet-form /
  Perron–Frobenius-type positivity improvement in the screw frame), not more
  windows.
