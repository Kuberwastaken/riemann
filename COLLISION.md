# COLLISION — reconciliation with Yoshida–Bombieri–CC–CCM–Suzuki (2026-08-11, fourth session)

*Directive: stop rediscovering known variational structure; identify the smallest
genuinely open convergence theorem whose proof would imply RH. Sources read at
theorem level: Suzuki arXiv:2606.09096 (read directly, §§1–2, 7–8); CCM
arXiv:2511.22755 (referee extraction, page-referenced); Bombieri 2000 and
Yoshida 1992 (extraction agents; plus Suzuki's precise citations [1,2,17]).
Labels as in BRIDGE v2.*

## 0. Normalization dictionary (repo ⟷ literature)

| repo object | literature object | dictionary |
|---|---|---|
| window half-length L | Suzuki's a; CCM's λ | a = L; λ = e^L (CCM work on [λ⁻¹, λ] ⊂ ℝ₊*, u = e^x; L_CCM := 2 log λ = 2·(our L over the multiplicative window)) |
| Z(f) (pole-inclusive zero-side functional) | Q_W(v) = W(v ∗ ṽ) (Suzuki (1.1)-(1.2)); CCM's QW_λ (3.19) | identical content: CCM (3.19) = archimedean ∫\|f̂\|²·2∂θ/2π + pole 2ℜ(f̂(i/2)·conj f̂(−i/2)) − Σ_{n≤λ²}Λ(n)⟨f\|T(n)f⟩; our Ω_W-multiplier form is its additive-variable Fourier rewriting; our prime cosine = their T(n) |
| C'_L | Q_W ≥ 0 on C_c^∞(−a, a) | Yoshida [17]: RH ⟺ (∀a) this positivity |
| λ'(L) | Suzuki's λ_a (1.7) = CCM's μ_λ (Cor 3.7) | identical (infimum of Rayleigh quotient on the localized form) |
| monotonicity of λ' | CCM (3.27) | identical |
| the form's s.a. realization | A_a = Friedrichs ext. of B_a = D*G_a D (Suzuki Thm 1.1); CCM Thm 3.6 A_λ | our "radical operator" is A_a |
| first-failure state f* | ground state φ of A_λ at the degenerate a (CCM Cor 3.7 + Suzuki Thm 1.3 + Yoshida Thm 2) | identical |
| prime-shift radical equation | A_{a*} φ = 0, written distributionally | change of variables of a known object |
| our kernel K (distribution) | −g″ where g = Suzuki's screw function (1.3) | g is the second antiderivative: continuous, with prime kinks Λ(n)n^{−1/2}(\|t\|−log n)₊ and ½\|t\|log\|t\| singular part (2.2) |
| threshold edge-locality (CONTINUATION Thm 5.1) | the (\|t\|−log n)₊ kinks of g | second derivative of a visible feature of (1.3) |
| σ-LP multiplier caps | §8 of Suzuki: the Q_G-frame (continuous-kernel integral operators) | our frame is the Fourier dual of Q_G |

## 1. Adjudication of CONTINUATION.md (and residual BRIDGE items)

| repo claim | verdict |
|---|---|
| Prop 2.2 (continuity of λ'(L)) | **KNOWN EXACTLY** — Suzuki Thm 1.3 (June 2026), proved via the screw expansion (2.2); he explicitly notes Bombieri's [1, Thm 5]/[2, Thm 4.4] even/odd continuity claim had incomplete details. Our uniform-modulus proof (M1–M3) is an independent alternate proof — minor value only |
| threshold continuity (Prop 2.1) | **KNOWN** — visible in the screw function's (\|t\|−log n)₊ structure |
| Thm 3.1 (first-failure zero mode) | **KNOWN AFTER COMBINATION** — ground-state existence: CCM Thm 3.6/Cor 3.7; degeneracy-at-first-failure: Suzuki Thm 1.3 + Yoshida Thm 2 (nondegeneracy ⟺ RH); Suzuki states the corollary explicitly after Thm 1.3 |
| the density lemma (D) | **KNOWN EXACTLY** — Suzuki Cor 1.2 (minimizer lies in the form-closure of C_c^∞; λ_a = inf over C_c^∞); CCM Prop 3.4 (E is a core; full-space bound = lim of finite-section eigenvalues) |
| prime-shift convolution equation | **KNOWN EXACTLY** — Bombieri 2000 Lemma 1/(4.2) (Euler–Lagrange equation λf = L[f] on the support, L = the full explicit-formula kernel), additive form (8.3): λ(¼+Δ)F = 𝓛[F] on (−t, t); his Lemmas 6–7 give the ∑_ρ f̃(ρ)x^{−ρ} representation and regularity of extremals; pole terms appear exactly as our rank-2 boundary correction (his A + Bx^{−1} / (8.14)–(8.15)) |
| Thm 4.1 (Schur continuation) | **UNPROVED** (L-A open; **L-B is KNOWN** — Bombieri 2000 Thm 12: small-support positivity with constant log(1/\|I\|) − log log(1+1/\|I\|) − O(1), the exact shell-coercivity species) and now **of limited interest**: its reach-audit conclusion (iteration ⟺ margin persistence) is subsumed by CCM Cor 3.8 (μ_λ ↓ 0 ⇒ RH) — the literature already owns the endpoint |
| Thm 5.1 (edge-locality) | **KNOWN AFTER CHANGE OF VARIABLES** (screw kinks); the explicit edge-to-edge factorization retains minor expository value |
| BRIDGE Thm S (RH ⇒ λ' > 0 ∀L) | **COROLLARY OF KNOWN RESULTS** (CCM Cor 3.7 ground state + Yoshida Thm 2 nondegeneracy under RH); our PW/Jensen/Farmer counting proof is an independent elementary proof of the nondegeneracy step |
| BRIDGE almost-positivity remark (λ_a ≥ −φ(a), φ→0 ⟺ RH) | **KNOWN EXACTLY** — CCM Cor 3.8 (the nontrivial direction), converse trivial |
| Track-A ε_N certificates (five windows) | **SURVIVES as relevant**: they verify CCM's §8 named obstacle (a) ("simple-even") at L = 0.45…0.62 — beyond Suzuki Thm 1.4's small-a regime, below no known general result |
| σ-LP experiments, Ω_W identity | instruments; the Ω_W identity is the standard Fourier form of (3.19) — **KNOWN in substance** |

Bombieri 2000 additions to the audit (referee extraction, page-referenced):
his Lemma 3 is the log-weighted compactness bound (our M1/M2 engine — "hinges
on the special structure of the prime at infinity"); Thm 3 is attainment on
L²(E) (our compactness step); Thm 5 is even/odd continuity-in-M (details
incomplete per Suzuki); Thms 8–9 are the negative-index = off-line-pairs
counts; Thm 10–11 + the p. 224 Corollary are the first-failure trichotomy (RH,
or infinitely many off-line zeros, or an explicit ℓ²-linear dependence of
x^{−ρ} on the interval); §13 even contains the exponential λ_N → 0 numerics
(completion-criticality's ancestor, 2000). His §7 Fredholm determinant
D(Λ; t) = det(I − ΛH(Γ; t)) with uniform-on-compacts truncation convergence is
zero-side determinant technology predating both modern programs.

**Summary: essentially every structural theorem of the last two repo sessions
exists in the 2000–2026 literature (Bombieri 2000 alone contains the extremal
equation, the compactness engine, the inertia counts, the first-failure
trichotomy, and the small-support quantitative positivity).** What survives:
the concrete certificates (obstacle (a) at five windows), the alternate
proofs, and the instruments.

## 2. The actual RH frontier, stated exactly (Phase 1)

### 2.1 CCM route (all page references to arXiv:2511.22755)

Proved at finite level [KNOWN]:
- Thm 1.1: for ε_N (smallest eigenvalue of QW_λ^N) ASSUMED simple with even
  eigenvector ξ: D_log^(λ,N) := D_log^(λ) − |D_log^(λ)ξ⟩⟨δ_N| is self-adjoint
  on E'_N ⊕ E_N^⊥ (inner product QW_λ^N − ε_N⟨·|·⟩ on E'_N), and
  **det_reg(D_log^(λ,N) − z) = −i λ^(−iz) ξ̂(z)**, entire, all zeros real =
  spec D_log^(λ,N). No sign condition on ε_N.
- Lemma 7.3: with k_λ := E(h_λ) the prolate surrogate (h_λ the lowest even
  eigenfunction of PW_λ = −∂_x(λ²−x²)∂_x + (2πλx)²; E(f)(u) = u^{1/2}Σ_{n≥1}f(nu)),
  suitably normalized F-transforms of k_λ converge to Ξ uniformly on closed
  substrips of |ℑz| < ½.

Missing (their §7–8, exact form):
- **(CCM-a)** For all (λ, N) [or all large]: ε_N is simple with even
  eigenvector. [Their named obstacle (a). Known: small a (Suzuki Thm 1.4);
  five certified windows (this repo). Open in general. NOT RH-complete on its
  face — a spectral non-degeneracy statement.]
- **(CCM-b)** ξ_λ ≈ k_λ strongly enough that, for some constants a, b:
  e^{a+ibz}·ξ̂_λ(z) → Ξ(z) uniformly on closed substrips of |ℑz| < ½ (order:
  N → ∞ at fixed λ — proved to converge to −iλ^{−iz}ξ̂_λ(z) modulo (a) — then
  λ → ∞). Their words: "the main remaining obstacle to our approach to RH."
  Multiplicities and RH then follow via Hurwitz. [RH-complete as a whole:
  its truth implies RH.]

### 2.2 Suzuki route

- Thm 1.5 [KNOWN, unconditional]: W(a,θ;z) built from deficiency
  eigenfunctions of D_a in H(T_a) is entire with all zeros real
  (= spec of the extension D_{a,θ}), for EVERY a — no simplicity/evenness
  hypotheses.
- **(S-c) Cor 1.6 [open]**: choose θ(a), φ(a,z) with
  e^{φ(a,z)}W(a,θ(a);z) → z²·ξ(1/2−iz)/ξ′(1/2−iz) uniformly on compacts ⇒ RH.
  (The reciprocal-log-derivative of CCM's target: the two conjectures are the
  same convergence problem in de Branges coordinates — structure function vs
  Weyl function; both encode "limits of real-zero functions" + Hurwitz.)
- **(S-d) The static form** [Suzuki §7.7, from his [14]]: the single identity
  ∫_ℝ S_x(z)S_y(z) dz = g(x−y) − g(x) − g(−y) + g(0), both sides defined
  unconditionally (S_x expressible without reference to the zeros), would give
  A_∞ > 0 and hence RH outright. **No limits, no windows: one kernel identity.**
  This is the zero-slack "arithmetic SOS" object earlier repo sessions groped
  toward, already isolated in the literature. [RH-complete; the sharpest known
  static formulation.]

### 2.3 Are the routes one problem?

Yes at the level of content: both assert that the localized real-zero
characteristic functions (ξ̂_λ / W(a,θ;z)) converge to the ξ-object; (S-d) is
the a = ∞ Gram-factorization these limits would produce. Differences are the
coordinates (function vs reciprocal log-derivative) and hypotheses (CCM need
(a); Suzuki's Thm 1.5 is hypothesis-free — a genuine advantage of his frame).

## 3. The single hard error term (Phase 3)

With Thm 1.1(ii) and Lemma 7.3 PROVED, the CCM chain has exactly one analytic
gap: **the ground-state comparison**

    E(λ) := ‖ ξ̂_λ − c_λ·k̂_λ ‖_{sup on closed substrips of |ℑz|<½}  → 0  (λ → ∞),

with both ξ_λ (Weil ground state) and k_λ (prolate surrogate) unconditionally
defined. Classification of its pieces: prolate side — PROVED (Lemma 7.3);
determinant identity — PROVED (finite level, modulo (a)); N → ∞ at fixed λ —
PROVED-modulo-(a) (Prop 3.4); **the ξ_λ-vs-k_λ comparison — GENUINELY OPEN**,
and it is where the arithmetic (the prime terms deforming the prolate operator
into the Weil operator) must finally be controlled. Red-team caution
(Phase 6): E(λ) → 0 implies RH, so this is not a "sub-RH" estimate; and by CCM
Cor 3.8 any almost-positivity softening (μ_λ ≥ −φ, φ → 0) is already
RH-equivalent — there is no ε-weakened version of the bottleneck that is
genuinely weaker. The only non-RH-complete open piece in either chain is
**(CCM-a) simple-even**, and it is required to even define the finite objects.

## 4. Phase 5 — the prime-threshold update, in the right frame [derived this session]

In the screw frame (Suzuki §8: the compact operator G_a with continuous kernel
g(x−y)), the term entering at a = ½log n is the kernel

    Δg_n(x,y) = Λ(n)n^{−1/2}·(|x−y| − log n)₊ ,

supported on two corner triangles of leg 2η at a = ½log n + η. Facts:
1. Δg_n is the positive part of an explicit rank-two kernel
   (Λ(n)n^{−1/2}(x − y − log n) is rank 2; the corner indicator breaks finite
   rank). Not finite rank; **Hilbert–Schmidt with exactly computable norm**:
   ‖ΔG_n‖_HS = (8/3)^{1/2}·Λ(n)n^{−1/2}·η²·(1 + O(η/a)), and trace class with
   ‖·‖₁ = O(Λ(n)n^{−1/2} η² log(1/η)) (Lipschitz kernel on O(η)-triangles).
2. In the DIFFERENTIATED (Weil-form/multiplier) frame the same update is
   −Λ(n)n^{−1/2}(R_n + R_n*) with R_n the edge-to-edge restricted shift — a
   scaled partial isometry, non-compact. **The screw function is exactly the
   renormalization in which prime-threshold perturbation theory is Fredholm**;
   det₂-update formulas (Hilbert–Schmidt perturbation determinants) are
   well-defined there and are NOT in the differentiated frame. This explains
   structurally why the literature's operator programs (CCM first-order D_log;
   Suzuki's G_a) both avoid the raw Weil frame.
3. Accumulating the updates over prime powers rebuilds the prime part of g and
   telescopes the (conjectural) determinant into an ordered product of
   det₂-corner-updates; the convergence of that product to a ξ-object is the
   SAME single limit as §3 — no shortcut, but a possibly useful bookkeeping
   for attacking (CCM-b) prime-by-prime. Whether the n-th det₂ factor relates
   to (1 − n^{−s})-type local factors is NOT established here; only the
   trace-ideal frame in which the question is well-posed. [POTENTIALLY NEW
   COORDINATE FORM; modest.]

## 5. Report

**A.** Dictionary: §0 (a = L, λ = e^L; Z = Q_W = QW_λ; λ' = λ_a = μ_λ;
K = −g″; edge-locality = screw kinks).
**B.** Known already: continuity (Suzuki 1.3), ground state (CCM 3.6/3.7),
density/core (Suzuki Cor 1.2, CCM 3.4), first-failure degeneracy (Suzuki after
1.3 + Yoshida Thm 2), almost-positivity endpoint (CCM Cor 3.8), monotonicity
(CCM 3.27), small-a positivity (Yoshida Lemma 2), small-a simple-even (Suzuki
1.4), edge/threshold structure (screw function (1.3)/(2.2)).
**C.** Genuinely surviving from this repo: the five-window certified
verification of CCM's obstacle (a) (unique evidence between Suzuki's small-a
theorem and nothing); the alternate uniform-modulus and PW/Jensen/Farmer
proofs; the Phase-5 trace-ideal observation (§4); the laboratory itself.
**D.** The exact convergence theorem that would imply RH: (CCM-b) with (CCM-a)
— e^{a+ibz}ξ̂_λ(z) → Ξ(z) on substrips (equivalently Suzuki Cor 1.6; static
form: the §7.7 kernel identity).
**E.** Strongest part proved this session: none of the frontier itself; the
session's proved content is the adjudication (§1), the dictionary (§0), and
the trace-ideal threshold computation (§4.1).
**F.** Single remaining explicit estimate: E(λ) := ‖ξ̂_λ − c_λ k̂_λ‖_{substrip}
→ 0 — the Weil-vs-prolate ground-state comparison, with the red-team caveat
that it is RH-complete and admits no genuinely weaker ε-version (Cor 3.8).
The narrowest NON-RH-complete open statement in either chain: **(CCM-a)
simple-even for all (λ, N)** — partially certified in this repo.
**G.** Threshold determinant update: obtained in the screw frame (§4): exact
HS norm, positive-part-of-rank-two structure, det₂ well-posedness, and the
frame-dependence theorem-shaped observation (Fredholm in screw coordinates,
non-compact in Weil coordinates).
**H.** Strongest reason the convergence program may fail: the comparison
ξ_λ ≈ k_λ is precisely where the prime deformation must be controlled at
zero slack; by Cor 3.8 there is no soft version; and the analogous historical
pattern (every RH-equivalent estimate resisting all approximation methods)
applies in full. Additionally (CCM-a) could fail at some (λ, N) — parity
symmetry-breaking of the finite ground state — which would force a
reformulation of the determinant route (Suzuki's hypothesis-free Thm 1.5 frame
would then be the survivor).
