# C1 — Lee–Yang / monotone zero motion on Suzuki's W(a,θ;z) family

*Agent C1 (cycle 2, CHALLENGER; mechanism assigned by evaluator E at RESET-1).
Task: formulate the ferromagnetic/Lee–Yang structure of the localized flow
precisely, then run the one-cycle discriminating test: do the (unconditionally
real) zeros of the a-family of characteristic functions move monotonically /
interlace in a and under a single prime-coupling increase Λ(2) → Λ(2)+ε?
Sources: Suzuki arXiv:2606.09096 (Thm 1.5, (1.3)/(1.11), §6), S1-sector.md
(F1)–(F3) + Thm A, T3-redteam.md (rate dictionary). No RH assumed anywhere.
Labels: PROVED / DERIVED / EMPIRICAL / OPEN. Numerics: float Galerkin,
`threshold-work/c1_leeyang.py`, validated against the certified anchors (§4.0).*

---

## 0. Verdict in one line

**The mechanism OPENS — but only in one exact frame.** At λ = 0 (the canonical
metric T_a = A_a) and at the two parity-real extensions θ ∈ {0, π}: the real
zeros z_k(a) of W(a,θ;z) are **strictly decreasing and interlacing in a
without a single exception** (0 mixed steps in 105 fine-grid steps through
both prime thresholds ½log2, ½log3; 0 interlacing violations in 261 checks),
they **converge monotonically from above to the Riemann zeros γ_k**
(z₁(0.61) − γ₁ = 3.7e−8, with (z₁−γ₁)/λ_a ≈ 33–44 across three decades of
λ_a — the same ≈40× constant as S1's crossing-margin law), and the response
to Λ(2) → Λ(2)+ε is **one-signed over all zeros** (all UP at θ = π, all DOWN
at θ = 0). Every naive strengthening is REFUTED with counterexamples: the
A_a-eigenvalue family is NOT monotone (signs −+−+ at first excited levels),
generic θ ∉ {0,π} is NOT one-signed under coupling, λ ≠ 0 frames are NOT
monotone (explicit counterexample at λ = −0.084), and the explicit-formula
guess dz_k/dε ∝ −cos(z_k log 2) is WRONG (sign agreement indistinguishable
from chance). The Lee–Yang structure lives exactly in the characteristic
function of the canonical frame — not in the Hamiltonian spectrum.

## 1. Formulation (deliverable 1)

### 1.1 The zero family

Suzuki Thm 1.5 [P-LIT, unconditional]: for every a > 0, λ < λ_a, and
θ ∈ [0,2π), the minimal operator D_a = i d/dx on the completion H(T_a) of
C_c^∞(−a,a) under ⟨T_a·,·⟩, T_a = A_a − λ, has deficiency indices (1,1);
its self-adjoint extensions D_{a,θ} have as spectrum exactly the zeros of

    W(a,θ;z) = (z−i)·v̂₊(z) + e^{iθ}(z+i)·v̂₋(z),     (Suzuki (1.11))

where (T_a v±)(x) = e^{±x} (deficiency vectors, Suzuki Lemma 6.2) and
v̂±(z) = ∫_{−a}^a v±(x)e^{izx}dx. **All zeros are real, for every a,
unconditionally** — this is the family's "Lee–Yang circle theorem," obtained
for free from self-adjointness. Since J A_a J = A_a (parity), v₋ = Jv₊, so
v̂₋(z) = v̂₊(−z) and on the real axis

    W(a,θ;z) = 2 e^{iθ/2} · Re[ e^{−iθ/2} E(z) ],   E(z) := (z−i) v̂₊(z):

the zeros at level θ are the solutions of phase(E(z)) ≡ (θ+π)/2 (mod π) — a
de Branges phase family. θ = 0 and θ = π are the two extensions for which
W is (up to a constant phase) a real even/odd-symmetric function of z (the
PT-symmetric extensions); Suzuki's conjectural limit (1.2)/Cor 1.6 makes
this family the Hilbert–Pólya candidate: eigenvalues of D_{a,θ} → imaginary
parts of ζ-zeros as a → ∞.

### 1.2 Ferromagnetic partition-function representation [DERIVED]

By S1 (F1)–(F3), the pole-free part of the localized Weil Hamiltonian is a
Dirichlet form: H^♮ = (archimedean Lévy jump form, density
ν(t) = e^{|t|/2}/2sinh|t| > 0, + killing V_a ≥ 0 + scalar Ω(0)) − Σ_{n≤e^{2a}}
(Λ(n)/√n)(τ_{log n} + τ_{log n}*). Feynman–Kac: e^{−tH^♮}(x,y) is the total
weight of paths of a killed jump process on (−a,a) — Lévy jumps with density
ν, plus **prime hops of exact length ±log n at rate Λ(n)/√n each** — with all
path weights ≥ 0 (the hop terms enter the exponent with a minus sign = a
positivity-preserving ferromagnetic coupling; S1 sign census (F3)). The full
operator is A_a = H^♮ + 2w₊⊗w₊ − 2w₋⊗w₋ (w± = cosh, sinh(x/2)): the
**rank-2 pole is the unique non-ferromagnetic vertex**. Since
v₊ = T_a^{−1}e^{x} = ∫₀^∞ e^{λt} e^{−tA_a} e^{x} dt, the characteristic
function is a ferromagnetic path sum with signed rank-2 insertions:

    v̂₊(z) = ∫₀^∞ e^{λt} Σ_{paths, e^{x}-entry → e^{izx}-exit}
             (nonneg. FK weight) × Π (pole insertions ∓2 w±(x_i)w±(y_i)) dt.

This is the precise sense in which the a-family is a Lee–Yang candidate
system: a positive (ferromagnetic) Gibbs-type measure over jump paths, one
rank-2 impurity, and a one-parameter family of boundary phases θ whose
"partition function" W(a,θ;z) has unconditionally real zeros.

**Empirical reinforcement (this work, §4.5): v₊ > 0 pointwise on (−a,a) at
every tested a (min v₊ = 3.38 at a = 0.30, 1.6e4 at a = 0.60)** — the
rank-2 insertions do NOT destroy the positivity of the path measure's
one-point marginal; v̂₊ is the Fourier transform of a positive density.

### 1.3 The exact conjectures

Fix λ = 0 (canonical: T_a = A_a; requires λ_a > 0, true unconditionally in
the range probed and equivalent to localized Weil positivity in general —
this frame-choice is load-bearing, see §4.4) and θ ∈ {0, π}. Let
0 < z_1(a,θ) < z_2(a,θ) < … be the positive zeros of W(a,θ;·).

- **(LY-a) Monotone interlacing a-flow.** For every k, θ ∈ {0,π} and
  0 < a < a′:  z_{k−1}(a) < z_k(a′) ≤ z_k(a). In particular each z_k(a) is
  strictly decreasing in a, hence (if bounded below) convergent to a real
  limit — the monotone-limit replacement for the zero-slack comparison wall.
- **(LY-p) One-signed prime response.** For every prime power n and every k:
  ∂z_k/∂Λ(n) has one sign over all k — at θ = π all zeros move UP, at θ = 0
  all zeros move DOWN (an SU(1,1)-type rotation of the structure function E,
  acting antilinearly: δE ≈ ε·β·E* with a definite angle, see §4.3).

## 2. Numerical construction (deliverable 2 setup)

`threshold-work/c1_leeyang.py`. Sine Galerkin φ_k = sin(w_k(x+a))/√a,
w_k = kπ/2a, k ≤ N = 200 (checks at 140–280). Form matrix of Q_a^W from the
S1 (F2) multiplier frame: archimedean multiplier Ω(ξ) = Reψ(¼+iξ/2) − log π
by panelled Gauss–Legendre in ξ (entire-form s_k(ξ) evaluation, averaged
analytic tail), rank-2 pole and prime hop overlaps in closed form. Then
c₊ = K^{−1}b₊ (b₊[k] = ⟨φ_k, e^x⟩ closed form), v̂₊(z) = Σ c₊ₖ φ̂ₖ(z) with
entire φ̂ₖ, real zeros of W by sign-scan + Brent on
Re[e^{−iθ/2}(z−i)v̂₊(z)], complex zeros counted by argument principle.

**Validation.** (i) N = 24 reproduces the CERTIFIED EPSILON-N enclosure at
a = 0.45 exactly: λ₀ = 1.956770e−5 ∈ [1.9536, 1.9600]e−5; N-monotone
decrease thereafter (1.6814e−5 at N = 200) as Galerkin demands. (ii)
γ_arch(0.10) = 1.2582 vs S1's 1.255. (iii) S1 table anchors at a = 0.30,
0.545 reproduced with the expected variational offsets. (iv) hop closed form
vs quadrature: 1.1e−14. (v) zeros stable to 2.8e−7 under a 2× beefed
quadrature. (vi) reality: argument-principle count = real-zero count at all
probes (a = 0.30, 0.45, 0.56; θ = 0, π) — the finite section preserves
Thm 1.5 reality exactly.

## 3. Test results (deliverable 2)

### 3.1 (LY-a) CONFIRMED — strict monotone interlacing through both thresholds

θ = π, λ = 0, a: 0.20 → 0.6125 (steps 0.01, refined 0.0025 near ½log2 and
½log3), zeros in (0, 60), nearest-neighbor continuity matching:

- **Every matched zero decreases at every step: mixed-sign steps 0/105.**
  No kink, no reversal at a = ½log2 = 0.34657 or ½log3 = 0.54931 (where the
  hop couplings switch on): e.g. z₃: 29.5420 (a=0.3425) → 29.3796 → 29.1875
  across the first threshold; z-count grows 4 → 11 (new zeros enter from
  the right; 13 Riemann zeros < 60).
- θ = 0, fine grid 0.30 → 0.62 step 0.005: **mixed steps 0/64** — the flow
  is monotone for both real extensions (a coarse Δa = 0.05 grid produces
  fake "mixed" steps by matching aliasing; at Δa ≤ 0.01 none survive).
- **Interlacing exact: z_{k−1}(a) < z_k(a+0.01) ≤ z_k(a) violated 0/261.**
- Strictness at the locked end (a = 0.60 → 0.61): dz = −3.5e−8 (k=0),
  −1.3e−5 (k=1), −2.3e−4 (k=2), −9.6e−3 (k=3) — all still strictly down.
- **Monotone convergence FROM ABOVE onto the Riemann zeros**
  (γ = 14.134725…, 21.022040…, 25.010858…, 30.424876…):

  | a | z₁ | z₂ | z₃ | z₄ |
  |---|----|----|----|----|
  | 0.21 | 15.5212 | 27.7280 | 41.4362 | 55.7233 |
  | 0.30 | 14.2592 | 22.6427 | 31.6070 | 41.0826 |
  | 0.45 | 14.1352 | 21.0660 | 25.2799 | 31.5640 |
  | 0.545 | 14.13475 | 21.02271 | 25.02056 | 30.64842 |
  | 0.6125 | 14.13472518 | 21.02205 | 25.01110 | 30.44071 |

  No zero ever crosses below its γ_k in the probed range.
- **Rate law:** (z₁(a) − γ₁)/λ_a = 44.2, 32.9, 36.4, 38.2, 42.3, 44.0 at
  a = 0.50…0.61 while λ_a spans 9.7e−7 → 8.3e−10: **the first zero's excess
  is ≈ 40·λ_a** — numerically the same ≈40× constant as S1's margin law
  1 − 𝔠(a) ≈ 40·ε_odd. Higher zeros converge strictly slower than λ_a
  ((z₂−γ₂)/λ_a drifts 7.2e3 → 1.8e4; k ≥ 2 has its own slower rate):
  the λ_a-proportionality is a first-zero law, not uniform in k.

### 3.2 (LY-p) CONFIRMED at θ ∈ {0,π} in the canonical frame — one-signed, and NOT the explicit-formula law

λ = 0, central differences with ε small enough to keep λ_a > 0
(ε = 1e−6 … 1e−10 as λ_a collapses; shifts 1e−3-scale, three orders above
root-finder noise; linearity checked ±):

- Λ(2)+ε, θ = π: **all zeros move UP at every tested a** (0.45: 8/8 up;
  0.50: 9/9; 0.56: 10/10; 0.60: 11/11). Sample dz_k/dε at a = 0.50:
  +4.3, +404, +2.4e3, +7.5e3, +3.0e4, … (magnitudes grow with k and with
  1/λ_a; the response is dominated by the collapsing ground channel).
- Λ(2)+ε, θ = 0: **all zeros move DOWN** (a = 0.50: 9/9 down,
  dz/dε = −5.4, −158, −516, …).
- Λ(3)+ε (a = 0.56): θ = π all UP (5/5 shown, all matched up), θ = 0 all
  DOWN — same directional pattern as Λ(2).
- The naive explicit-formula prediction sign(dz_k/dε) = sign(−cos(z_k log n))
  FAILS: agreement 3/4, 3/5, 2/5 … — chance level. The response is a
  **coherent one-signed rotation, not an oscillatory kick**.

### 3.3 Where the mechanism DIES — the exact refutation boundary

1. **Hamiltonian spectrum (E3):** dλ_j/dε signs at a = 0.40: −+−+−−−−−+;
   0.50: −+−−−+−−−−; 0.60: −−++−−−−+−. Only the ground state is GKS-monotone
   (dλ₀/dε = −√2·g_{φ₀}(log 2) < 0 since φ₀ is one-signed — S1 Thm A
   territory). **Any Lee–Yang claim about eigenvalues of A_a is dead**; the
   monotone object is the zero set of the characteristic function only.
2. **Generic θ:** at a = 0.50, Λ(2), the per-θ response is one-signed ONLY
   near the two real extensions: θ = 0, 1.25π, 1.5π, 1.75π all DOWN;
   θ = π UP; θ ∈ {0.25π, 0.5π, 0.75π} MIXED. The conjecture must be stated
   at θ ∈ {0, π} (PT-symmetric extensions), not for the whole θ-circle.
3. **λ-frames (E0/E2):** zeros at fixed θ depend strongly on λ (λ: 0 → −0.5
   moves z₁ from 14.135 to 3.84 at a = 0.45; the λ → −∞ limit restores free
   spacing π/a). In the deep frame λ = −0.084 (forced by finite ε = ±0.05
   pushing λ_a < 0), coupling monotonicity FAILS: a = 0.56, θ = π, k = 2:
   z = 14.319 moves DOWN (−0.68/ε) while k = 1: z = 9.802 moves UP (+5.1/ε).
   **The counterexample configuration: (a, θ, λ, ε) = (0.56, π, −0.084,
   ±0.025), zeros k = 1 vs k = 2.** Monotonicity is a property of the
   arithmetic frame λ = 0 exactly — consistent with Suzuki §7 (λ = 0 is the
   frame in which (1.2) is expected) and with the observation that only at
   λ = 0 do the zeros lock onto the γ's.
4. Suzuki's expectation that the zeros are λ-independent (p. 7 remark) is
   FALSE at fixed θ in the finite section: the θ-labeling of extensions is
   λ-relative. (At λ = 0 with λ_a → 0⁺ the θ-dependence itself dies: the
   θ = 0 and θ = π families pinch onto the common zeros of v̂_a — the
   finite-section shadow of the CCM ξ̂_λ collapse.)

## 4. What must be proved next (deliverable 3)

The discriminating test PASSED in the exact frame (λ = 0, θ ∈ {0,π}); the
monotone-limit route is OPEN with three concrete targets, ordered:

- **(C1-T1, inclusion step) [structural, no arithmetic]:** For supp v ⊂
  (−a,a), Q_{a′}^W(v) = Q_a^W(v) (locality of the Weil form — the prime sum
  truncates itself). Hence, at λ = 0, H(A_a) embeds isometrically in
  H(A_{a′}) and D_a ⊂ D_{a′} as symmetric operators with common action
  i d/dx. PROVE: the boundary phase of the (1,1)-deficiency family is
  monotone under this nesting, i.e. ∂_a arg E_a(z) ≥ 0 for real z. This is
  a Weyl-function monotonicity statement for nested symmetric operators —
  no primes enter the STATEMENT; the primes enter in fixing the sign.
- **(C1-T2, positivity input = the FKG/GKS lemma):** PROVE v₊ = A_a^{−1}e^x
  > 0 on (−a,a). Route: A_a^{−1} = (H^♮ + rank-2 pole)^{−1}; e^{−tH^♮} is
  positivity improving (S1 Thm A); control the two signed pole insertions by
  the odd-coupling smallness ‖w₋‖² = sinh a − a (cubically small; S1 B1
  machinery certifies a ≤ 0.42 cheaply, numerics show positivity persists
  to 0.60+). With v₊ > 0, E(z) = (z−i)v̂₊(z) is (z−i)×(Fourier transform of
  a positive measure) — the Lee–Yang-class input for the phase-derivative
  sign in C1-T1, replacing zero-slack comparison with a correlation
  inequality for the FK path measure: ∂_a arg E = (positive-measure pairing)
  ⇔ Cov_{FK}(boundary occupation, e^{izX}-phase) ≥ 0 — the precise GKS-II
  analogue for this system.
- **(C1-T3, the wall in new coordinates — state honestly):** LY-a gives
  monotone convergence z_k(a) ↓ ẑ_k ∈ ℝ for free once C1-T1/T2 hold in the
  λ = 0 frame, and reality of all limit points is then automatic. What it
  does NOT give: (i) that λ_a > 0 for ALL a (the λ = 0 frame's existence IS
  localized Weil positivity — RH-complete globally; unconditional only on
  certified/derived ranges), and (ii) the identification ẑ_k = γ_k
  (Suzuki (1.2)/Cor 1.6 — the CCM convergence wall in de Branges
  coordinates). The route's honest value: it replaces "prove E(λ) → 0"
  by "prove two sign inequalities + identify a monotone limit," and the
  empirical rate (z₁ − γ₁ ≈ 40 λ_a) ties the new coordinates to the S1
  margin functional quantitatively.

**Kill boundaries to respect (do not re-attempt):** eigenvalue-monotonicity
of A_a under prime couplings (mixed signs, §3.3.1); one-signedness for
generic θ (§3.3.2); any λ ≠ 0 formulation (§3.3.3); the −cos(z log n)
response law (§3.2).

## 5. Bookkeeping

- Script: `threshold-work/c1_leeyang.py` (self-contained; `smoke|e0|e1|e2|e3`;
  ~3 min total at N = 200 on 8 vCPU). All numbers above reproduced from it.
- Robustness: N ∈ {140, 200, 260, 280} (zeros shift ≤ 6e−3 at k ≤ 4, signs
  unchanged; coupling one-signedness holds at N = 140 and 260); quadrature
  2× refinement shifts zeros ≤ 2.8e−7; reality verified by winding count.
- Float Galerkin throughout: EMPIRICAL, not certified. The three headline
  sign-claims (monotone a-flow, interlacing, one-signed coupling response at
  θ ∈ {0,π}) come with margins 1e−3…1e−1 — far above the 1e−7 numerical
  noise floor; per-window Arb certification of a monotonicity step would be
  routine S1-style work if wanted.
- Relation to fleet: C2 (FKG vs screening) should target C1-T2's covariance
  inequality directly; the λ-frame counterexample (§3.3.3) is the sharp
  input for any referee attack on the mechanism.
