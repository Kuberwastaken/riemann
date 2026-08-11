# FRONTIER — live implication DAG (maintained under SOLVER.md; recompute after every result)

STATUS KEY: PROVED-REPO / PROVED-LITERATURE / PROVED-CONDITIONAL / NUMERICAL /
HEURISTIC / OPEN / REFUTED / EQUIVALENT-TO-RH.

```
RH
└── CCM/Suzuki convergence theorem            [OPEN, EQUIVALENT-TO-RH]
    │   (CCM §7: e^{a+ibz}·ξ̂_λ(z) → Ξ(z) on substrips |ℑz|<½; ⇒RH via Hurwitz
    │    — CCM p.27. Equivalent coordinates: Suzuki Cor 1.6 (ξ/ξ′ form);
    │    static form: Suzuki §7.7 kernel identity ∫S_xS_y = screw kernel.)
    ├── finite-λ determinant identity          [PROVED-LITERATURE, needs (a)]
    │       det_reg(D_log^(λ,N) − z) = −i λ^{−iz} ξ̂(z)   (CCM Thm 1.1(ii))
    ├── N→∞ at fixed λ                          [PROVED-LITERATURE mod (a)]
    │       (CCM Prop 3.4 core theorem; order of limits: N first, then λ)
    ├── prolate → Ξ convergence                 [PROVED-LITERATURE]
    │       (CCM Lemma 7.3: F(k_λ) → Ξ on closed substrips)
    └── Weil ground state ↔ prolate comparison  [OPEN, EQUIVALENT-TO-RH]
        │   E(λ) := ‖ξ̂_λ − c_λ k̂_λ‖_substrip → 0; no soft version exists
        │   (CCM Cor 3.8 almost-positivity ⟺ RH — COLLISION.md §3)
        ├── prime-threshold determinant evolution  [CURRENT PRIMARY]
        │   ├── single-threshold Schatten classification  [PROVED-REPO,
        │   │     COMPLETE (T1): self-adjoint, HS norm √(8/3)Λ(n)n^{−1/2}η²
        │   │     exact, TRACE CLASS with ‖Δ‖₁ = 8κ₁Λ(n)n^{−1/2}η² exact,
        │   │     traceless, exact unitary model with spectrum
        │   │     ±4Λ(n)n^{−1/2}η²·s_j(Ĉ₁)]
        │   ├── two-part evolution structure  [PROVED-REPO, structural:
        │   │     d(det)/da = Hadamard boundary-variation flow (continuous)
        │   │     + threshold kernel entries (discrete); THRESHOLD.md §2]
        │   ├── relative det₂ update across one threshold  [PROVED-REPO
        │   │     under isolation 2η < gap-to-next-threshold (T1-det2.md):
        │   │     log-det update = Hadamard flow (diagonal-corner ρ) +
        │   │     (8/3)Λ(n)n^{−1/2}η³·ρ(z;a,−a) + exact k=2 term
        │   │     −(4/3)c²η⁴z^{−2} + controlled k≥3; a↦log D_a is C¹ across
        │   │     thresholds — the prime enters at exact order η³.
        │   │     CAVEAT: isolation shrinks like 1/n (twin primes) —
        │   │     accumulation must use the additive multi-threshold form]
        │   ├── leading update = end-to-end resolvent kernel [PROVED (T1),
        │   │     corrected constant/power: (8/3)Λ(n)n^{−1/2}η³·ρ(z;a,−a);
        │   │     n^{−s} phase emergence still conjectural — agent T2]
        │   ├── p^k resummation → local factor             [OPEN — agent T2]
        │   └── infinite accumulation                      [OPEN; RED-TEAM
        │         EQUATION (THRESHOLD.md §3): post-entry growth is LINEAR in a
        │         (η² only at entry) ⇒ bare accumulation diverges like
        │         Σ Λ(n)n^{−1/2}(2a−log n)₊ ~ 4e^a; convergence REQUIRES the
        │         PNT-level pole-vs-prime cancellation inside the flow —
        │         agent T3 red-teams whether det₂ realizes it]
        └── direct kernel estimate (Suzuki §7.7 identity)  [OPEN, orthogonal]

SIDE (enabling, non-RH-complete):
CCM obstacle (a): ε_N simple + even eigenvector
├── small a                        [PROVED-LITERATURE — Suzuki Thm 1.4]
├── five windows L=0.45..0.62      [CERTIFIED-REPO — EPSILON-N.md; ready to
│                                    communicate to CCM (human action: Kuber)]
└── all (λ,N) — sector inequality ε_even < ε_odd   [OPEN — agent S1, parallel]

NEW NO-GO (T1, proved): A_a admits NO determinant of any standard species —
its eigenvalues grow like C_a·log j, so the resolvent lies in no Schatten
class and the spectral zeta has empty convergence domain; determinant theory
exists only in the screw/G frame (compact, trace class) or on CCM's D_log
(linear spectral growth). DEAD-ENDS #12 upgraded from observation to theorem.

ORTHOGONAL RESERVE (not currently primary): de Branges/canonical systems via
Suzuki [14]; CC geometric positivity; zero-density amplification (2/3-paper
frontier: unconditional F(α) beyond bandwidth 1).
```

FRONTIER NODE: relative det₂ update across one threshold (validity + exact
first-order term), because it gates both the p^k resummation and the
accumulation red-team, and its failure mode is itself informative.
