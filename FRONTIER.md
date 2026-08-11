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
        │   │     (8/3)Λ(n)n^{−1/2}η³·ρ(z;a,−a)]
        │   ├── e^{2iaz} phase in Γ_a(z;a,−a)   [REFUTED (T2): symbol of the
        │   │     singular part is log(|ζ|/2π) (RvM density, cross-checked vs
        │   │     Suzuki Thm 1.4); only oscillation e^{4πia·e^z}, damped off ℝ;
        │   │     the e^{2iaz}=λ^{−2iz·(1/2)} phase lives in the FIRST-ORDER
        │   │     frame (deficiency elements of D_a; CCM's λ^{−iz}), never in
        │   │     A_a's resolvent]
        │   ├── p^k resummation through A_a-resolvent  [KILLED with equations
        │   │     (T2): yields the p-local factor of −ζ′/ζ at s=½, REAL and
        │   │     UNTWISTED (log p/(√p−1)); exact residual vs the Euler ansatz
        │   │     = the missing character p^{ikz}; the z-twist provably enters
        │   │     via characters e^{izx} (division by ĝ, ĝ(z)=z^{−2}ξ′/ξ(½−iz)),
        │   │     not via Green profiles → DEAD-ENDS #13]
        │   ├── amplitude/screening inequality  [PROVED-shape (T2): uniform
        │   │     convergence needs |𝒜_n| ≤ C_K n^{−1/2}ω(ε_n), ∫ω<∞ — an
        │   │     extra √n of screening the Born amplitude misses by exactly
        │   │     √n; forced unconditionally by ‖R‖≤1/|ℑz| yet invisible at
        │   │     every finite perturbative order — the non-perturbative core,
        │   │     same arithmetic content as E(λ)/(CCM-b)]
        │   ├── p^k resummation → local factor             [OPEN — agent T2]
        │   └── infinite accumulation                      [REFUTED (T3,
        │         threshold-work/T3-redteam.md): KILL A — entry det₂ product
        │         converges absolutely (total entry mass 0.17057) and carries
        │         O(a·e^{−a}) of the prime content: entries CANNOT carry Ξ;
        │         KILL B — totals diverge at every Schatten order,
        │         Tr(S^{2m}) ≥ (c·e^a/a³)^{2m} unconditionally; det₂'s removed
        │         linear term IS the arithmetic-bearing term. → DEAD-ENDS #14.
        │         CONSTRUCTIVE: divergence is a rank-3 defect (pole directions
        │         e^{±x/2} + constants = the s(s−1) factor); Schur compression
        │         tames e^a → O(a²log a); POST-REPAIR DICTIONARY [PROVED,
        │         classical]: E(t) = O(t) under RH, Ω(e^{(Θ−½−ε)t}) if RH
        │         fails ⇒ subexponential compressed bookkeeping ⟺ RH, rate
        │         e^{(2Θ−1)a}; toy check 0.496 vs 0.5. NO SUB-RH FLOOR —
        │         THRESHOLD §3's PNT-strength guess corrected to RH-strength.]
        └── direct kernel estimate (Suzuki §7.7 identity)  [OPEN, orthogonal]

SIDE — CCM obstacle (a), DECOMPOSED by S1 (threshold-work/S1-sector.md):
├── pole-free part simple+even at EVERY a  [PROVED-REPO — S1 Thm A:
│     Lévy–Khintchine (ν(t)=e^{|t|/2}/2sinh|t|>0, jump Dirichlet form) +
│     ferromagnetic primes; parity gap ≥ ν(2a)‖v_o‖₁²; the primes can NEVER
│     break simple+even — only the rank-two pole can]
├── exact crossing criterion  [PROVED-REPO: ε_even<ε_odd ⟺ 𝔠(a) :=
│     2⟨(H♮_o−ε_even)^{−1}w₋, w₋⟩ < 1; crossing ⟺ 𝔠=1; per-window
│     Arb-certifiable far cheaper than sign certificates]
├── theorem-with-range a ≤ 0.32  [DERIVED, mod ONE open archimedean lemma
│     γ_arch ≥ 1.2; extendable to 0.42 by cheap certification]
├── five windows L=0.45..0.62  [CERTIFIED-REPO — EPSILON-N.md; outreach to
│     CCM = human action (Kuber)]
└── ∀a version  [STATUS CORRECTED: RH-MARGINAL — margin law
      1−𝔠(a) ≈ 40·ε_odd(a), and odd-Weil positivity ∀a ⟹ RH (Yoshida
      Prop 1). Non-RH-complete at any FIXED a only. At a crossing, CCM
      Thm 1.1 fails and Suzuki Thm 1.5 is the surviving frame.]

NEW NO-GO (T1, proved): A_a admits NO determinant of any standard species —
its eigenvalues grow like C_a·log j, so the resolvent lies in no Schatten
class and the spectral zeta has empty convergence domain; determinant theory
exists only in the screw/G frame (compact, trace class) or on CCM's D_log
(linear spectral growth). DEAD-ENDS #12 upgraded from observation to theorem.

ORTHOGONAL RESERVE (not currently primary): de Branges/canonical systems via
Suzuki [14]; CC geometric positivity; zero-density amplification (2/3-paper
frontier: unconditional F(α) beyond bandwidth 1).
```

FRONTIER NODE (recomputed after T1+T2+T3 — cycle-1 synthesis): the
**rank-3-compressed first-order determinant flow**: run the a-evolution on the
first-order frame (T1: only frame with a determinant; T2: only frame with the
z-phase) AFTER Schur-compressing the three defect directions {e^{x/2},
e^{−x/2}, 1} (T3: the exact repair — CCM's L²₀ handles one of three; complete
it). Status: EQUIVALENT-TO-RH with a PROVED rate dictionary (subexponential
bookkeeping ⟺ RH, e^{(2Θ−1)a}); per SOLVER §8, next decomposition: (i) derive
the compressed flow's exact evolution equation (Hadamard part now carries all
arithmetic — T3 KILL A); (ii) the non-perturbative √n screening (T2's Q3) as
the flow's stability condition; (iii) N ≥ λ² finite-section diagonal (T3's
order-of-limits: obstacle (a) needed on all (λ, N ≥ λ²) — deprioritizes
window-extension permanently). Pending: S1 (sector inequality; its scope now
set by (iii)).

---
CYCLE 1 CLOSED (2026-08-11): T1 one-threshold formula + A_a-no-determinant;
T2 phase refutation + untwisted local factors + √n screening; T3 double kill
of accumulation + rank-3 repair + RH-rate dictionary; S1 pole-free simple-even
theorem + exact crossing criterion + RH-marginality of ∀a obstacle (a).
NEXT SESSION: execute SOLVER §13 GLOBAL RESET first (rerank without sunk
cost; the recomputed primary is the rank-3-compressed first-order flow, but
the reset must weigh it against the orthogonal reserve with fresh eyes),
then open cycle 2 on the reranked frontier node.

---
POST-RESET-1 STATE (see RESET-1.md for the full adjudication):
PRIMARY = §7.7 defect formula (D(x,y) as explicit zero-sum; D ⪰ 0 suffices;
one-cycle = computation, non-RH-complete). CHALLENGER = Lee–Yang/FKG
ferromagnetic-flow mechanism (monotone real-zero motion replacing zero-slack
comparison). RESERVE = CvS prime-cutoff obstacle-(a) (published CMP frame;
S1 crossing tech ports). Incumbent rank-3 flow demoted to cartography.
Literature deltas (evaluator D): Suzuki [14] v3 (CJM, unconditional surrogate
spaces + HP section); Connes–van Suijlekom CMP 406:312 (general simple-even ⇒
real ξ̂-zeros; θ_x prime-cutoff coordinate); Śliwiński 2601.12133 (PROVEN
1/(4 ln λ) dissonance floor — CCM eigenvalue convergence at best inverse-log);
Kim et al 2607.24830 (first A_a numerics; replicates the rate dictionary;
γ_arch input; W(a,0;z) real zeros); CCM "Prolate→Cohomology" in prep
(collision risk on geometric route); S1's LK mechanism = Suzuki §5 technique
(novelty limited to every-a extension + parity gap + crossing criterion);
Groskin certification budget overlaps the five-window niche (outreach urgency
UP). Cycle-2 fleet: P1 (Gram explicit formula + convergence), P2 (off-line
pair + sign), C1 (Lee–Yang toy), C2 (FKG vs screening), R1 (CvS sector), L1
(route-everyone-missed); hostile referee follows on their artifacts.

R1 ADJUDICATED: (correction) the θ_x prime-cutoff family is OUR instantiation
licensed by CvS's general theorem, not in their paper. PROVED: S1 Thm A
transplants to all (a,x) (pole-free simple+even; gap ≥ ν(2a)‖v_o‖₁²; λ^♮
monotone in x); the 𝔠-criterion transplants verbatim. INVERSION (float,
S1-anchored): with the pole, every Euler-deficient truncation crosses to an
ODD ground state (a*₁=0.3737 arch+pole; a*₂=0.5606 +{2}; a*₃=0.7014 +{2,3});
evenness restored only at full Euler content — simple+even is a matched-filter
property of window vs Euler content on the λ² diagonal. ROUTE KILL →
DEAD-ENDS #15. YIELDS: unconditional Lee–Yang family indexed by (a,x) (new to
literature; feeds C1); N₀-quantifier collapse — continuum simple+even ⇒ all
Fourier truncations N ≥ N₀(a,δ): the five certified windows lift to the whole
N-diagonal; effective N₀(a,δ) = concrete non-RH-complete follow-up (replaces
T3's order-of-limits obstacle).

C1 ADJUDICATED — CHALLENGER MECHANISM OPENS (empirical, builder validated
against certified enclosures): (LY-a) monotone-from-above interlacing zero
flow in a CONFIRMED (0/261 violations through both thresholds), converging
onto the Riemann zeros with (z₁−γ₁) ≈ (33–44)·λ_a — the SAME ~40× constant as
S1's margin law: cross-frame invariant, now [CONJECTURE] in its own right.
(LY-p) coherent one-signed prime response at θ∈{0,π} (antilinear E-rotation).
REFUTATION BOUNDARY: only the pinned frame (λ=0, θ∈{0,π}) works — generic θ
mixed, λ≠0 counterexample at (0.56, π, −0.084); A_a's higher eigenvalues not
monotone; Suzuki's expected λ-independence of W-zeros is FALSE at fixed θ
[falsifiable literature correction]. NEW OPEN NODES (sign-inequality-shaped,
not estimates): (C1-T1) ∂_a arg E_a(z) ≥ 0 via H(A_a) ↪ H(A_{a′}) chain
nesting; (C1-T2) v₊ = A_a^{−1}e^x > 0 via positivity-improving e^{−tH♮} +
cubically-small odd pole coupling (numerically: min v₊ ∈ [3.4, 1.6e4] on
a ∈ [0.30, 0.60]). HONEST WALL (C1-T3): pinned-frame global existence =
localized Weil positivity; limit identification = Cor 1.6 — the trade is
E(λ)→0 for two sign inequalities + one monotone limit.

P2 ADJUDICATED — **ABANDONMENT CONDITION FIRED; CHALLENGER AUTO-PROMOTED.**
Closed form: D(x,y) = 2Im[r_p 𝒫_x(p)𝒫ˢ_y(p)] + (x↔y), supported on the SHADOW
ZEROS of ξ+ξ′ (E_ξ = A+iA′; naive quadruple block cancels identically, Thm D0,
1e-13-validated). Sign: signature (2,2) = exact Bombieri-inertia mirror; (1,1)
per parity; no one-sidedness anywhere; D ⪰ 0 ⟺ D ≡ 0 ⟺ RH (⟺ E_ξ ∈
Hermite–Biehler with explicit defect kernel). Rate dictionary e^{(2Θ−1)a}
rederived (third frame). Static sector → HARD-WALL-COORDINATES → DEAD-ENDS #16.
NEW PRIMARY (auto): the Lee–Yang sign-inequality program — prove
(C1-T2) v₊ = A_a^{−1}e^x > 0 (positivity-improving semigroup + small odd pole
coupling), then (C1-T1) ∂_a arg E_a(z) ≥ 0 (chain nesting + FKG covariance);
limit identification (C1-T3/Cor 1.6) remains the wall behind them.
NEW NODE (salvage): shadow-zero location ℑp as real-analytic RH order
parameter — feeds the promoted route's monotone-flow picture.
METRICS: chain relocated again, not shortened — counter 2/3. One more
no-shortening cycle forces the next rerank; the promoted route's advantage is
that its nodes are SIGN INEQUALITIES, not estimates.
