# T1 — the relative det₂ formula across one prime-power threshold (screw frame)

*Cycle-1 agent T1 (operator theory, PROVER). Task: THRESHOLD.md §4/T1.
Conventions: Simon, "Trace Ideals and Their Applications", 2nd ed. (cited [S]);
Gohberg–Krein, "Introduction to the Theory of Linear Nonselfadjoint Operators"
(cited [GK]); Suzuki arXiv:2606.09096 (cited [Su], equation numbers his).
Nothing below assumes RH. No numerics: every constant is exact or symbolic.
Labels: PROVED / DERIVED / HEURISTIC / OPEN per SOLVER.md §7.*

---

## 0. Setting and standing assumptions

- `g` = Suzuki's screw function [Su (1.3)]: continuous, even, real; near 0,
  `g(t) = ½|t|log|t| + A|t| + Σ_{n≤e^{|t|}} Λ(n)n^{−1/2}(|t|−log n) + r(t)`,
  `r ∈ C²` [Su (2.2)]. Away from `t ∈ {0} ∪ {±log m : m prime power}`, `g` is
  C^∞. Global modulus of continuity on `[−2a,2a]`:
  `ω_g(δ) ≤ C(a)·δ(1 + log₊(1/δ))`  (worst point t = 0). [PROVED, from (2.2)]
- Plain compression: `G_a^χ := χ_a G χ_a` on `L²(−a,a)`, kernel `g(x−y)`;
  Suzuki's operator: `G_a := P_a G P_a` [Su (1.5)], `P_a` = orthogonal
  projection onto mean-zero `L²₀(−a,a)` [Su (2.1)]. Since `P_a = χ_a − Q_a`
  with `Q_a = |e_a⟩⟨e_a|`, `e_a = (2a)^{−1/2}1_{[−a,a]}`:
  `G_a = G_a^χ − F_a`, `F_a := Q_aGχ_a + χ_aGQ_a − Q_aGQ_a`, **rank(F_a) ≤ 2**.
  All determinant statements are proved for `G_a^χ` and transported to `G_a`
  through this exact rank-≤2 identity (§5.3, §4.4). [PROVED]
- Threshold data: `n = p^k`, `a_n := ½log n`, `a := a_n + η`, `c_n := Λ(n)n^{−1/2}`.
  `Δ_{n,η}` on `L²(−a,a)` has kernel `k_Δ(x,y) = c_n(|x−y| − log n)₊`,
  supported on the two closed corner triangles
  `T₊ = {x−y ≥ log n}` (near `(a,−a)`) and `T₋ = {y−x ≥ log n}` (near `(−a,a)`),
  each of leg `2η`.
- **Isolation assumption (Iso).** `(log n, log n + 2η]` contains no `log m` for
  any other prime power `m`, i.e. `2η < log(n′/n)`, `n′` the next prime power.
  Then on `[−a,a]²` the g_n-component of the kernel is exactly `k_Δ`, and
  `g^{(n̂)} := g − g_n` generates the "stripped" operators `G_a^{(n̂),χ}`,
  `G_a^{(n̂)}`. Without (Iso) every formula below holds with `Δ` replaced by the
  finite sum of the simultaneously-entering `Δ_{m,η_m}` (all statements are
  additive at the stated orders). [PROVED trivially; see §6.3 for the caveat]
- Spectral parameter: `z ∉ spec(G_a^χ)` (resp. of the operator being resolved);
  `R(z) := (G_a^χ − z)^{−1}`, `R^{(n̂)}(z) := (G_a^{(n̂),χ} − z)^{−1}`,
  `‖R(z)‖ = dist(z, spec)^{−1}` (self-adjointness). Fredholm variable `μ = 1/z`.

---

## 1. The threshold operator: exact structure [all PROVED]

### 1.1 Re-verification of the HS norm (independent, 3 lines)
For a difference kernel on `[−a,a]²`: `∬F(x−y)dxdy = ∫_{−2a}^{2a}F(t)(2a−|t|)dt`.
With `F(t) = c_n²(|t|−log n)₊²`, substituting `σ = |t| − log n` (so `2a − |t| =
2η − σ` **exactly**, since `2a = log n + 2η`):

    ‖Δ_{n,η}‖²_HS = 2c_n²∫₀^{2η} σ²(2η−σ)dσ = 2c_n²·(2η)⁴/12 = (8/3)c_n²η⁴.

**‖Δ_{n,η}‖_HS = √(8/3)·Λ(n)n^{−1/2}·η², exact** — THRESHOLD.md §1 confirmed. ✓

### 1.2 Block form and exact model reduction
With respect to the end-zones `[a−2η, a]` and `[−a, −a+2η]` (which carry the
whole support), `Δ ≅ [[0, C],[C*, 0]]` where, in coordinates `x = a−s`,
`y = −a+t`, the block `C` on `L²(0,2η)` has kernel `c_n(2η − s − t)₊`.
Rescaling `s = 2ησ` (unitary) gives the **exact unitary reduction**

    C ≅ 4c_nη² · Ĉ₁ ,   Ĉ₁ := integral operator on L²(0,1) with kernel (1−σ−τ)₊.

Consequences (all exact):
- `spec(Δ_{n,η}) \ {0} = { ±4Λ(n)n^{−1/2}η²·s_j(Ĉ₁) : j ≥ 1 }` — the ±-pairing
  of an off-diagonal block operator; in particular **Tr Δ = 0** whenever
  `Δ ∈ 𝔖₁` (independent second proof: the kernel vanishes on the diagonal and
  is continuous, so `Tr = ∫k_Δ(x,x)dx = 0` by [GK Ch. III, Thm 10.1]).
- `‖Δ‖ = 4c_nη²·s₁(Ĉ₁) ≤ (2/√3)c_nη²` (since `s₁ ≤ ‖Ĉ₁‖_HS/√2`-pairing bound;
  `‖Ĉ₁‖²_HS = ∫₀¹w²(1−w)dw = 1/12` — consistency: `2·(4c_nη²)²·(1/12) =
  (8/3)c_n²η⁴` ✓ matches §1.1 by an independent route).
- **Trace class, with trace norm exactly proportional to η²:**
  `‖Δ_{n,η}‖₁ = 8κ₁·Λ(n)n^{−1/2}·η²`, `κ₁ := Σ_j s_j(Ĉ₁) < ∞` an absolute
  constant (finiteness: §2). This **corrects COLLISION.md §4.1**: the guessed
  `O(c_nη²log(1/η))` carries no log — scale invariance forces exact `∝ η²`.
  It also **closes THRESHOLD.md §1's OPEN-minor**: trace-class membership is
  PROVED, not merely plausible.
- Remark (no numerics): the model eigenpairs solve the reflection ODE
  `λφ″(σ) = φ(1−σ)`, `φ(1) = φ′(1) = 0`; the components even/odd about σ = ½
  solve `λψ″ = ±ψ`, so the `s_j(Ĉ₁)` are roots of explicit trig/hyperbolic
  transcendental equations. Not needed below.

### 1.3 Corner mass (needed for §4)

    ∬_{T₊}(x−y−log n)dxdy = ∬_{s,t≥0, s+t≤2η}(2η−s−t)dsdt = (2η)³/6 = (4/3)η³,

so the **total mass** `∬k_Δ = 2·c_n·(4/3)η³ = (8/3)Λ(n)n^{−1/2}η³`. [PROVED]

---

## 2. Singular-value lemma and trace-classness of the family [PROVED]

**Lemma 2.1.** Let `K` be an integral operator on `L²(I)`, `|I| < ∞`, whose
kernel has modulus of continuity `ω` in `x` uniformly in `y`. Then
`s_{2j}(K) ≤ |I|·ω(|I|/j)·j^{−1/2}`.

*Proof.* Partition `I` into `j` cells; let `K_j` (rank ≤ j) have kernel
`k(x_i^*, y)` on cell `i`. Then `‖K − K_j‖²_HS ≤ |I|²ω(|I|/j)²`. Since
`s_{j+i}(K) ≤ s_i(K − K_j)`, we get `Σ_{i>j}s_i(K)² ≤ ‖K−K_j‖²_HS`, hence
`j·s_{2j}(K)² ≤ |I|²ω(|I|/j)²`. ∎  (Classical; cf. [GK Ch. III §10].)

**Corollary 2.2.**
(i) `Δ_{n,η}`: Lipschitz kernel ⇒ `s_j = O(j^{−3/2})` ⇒ `Δ ∈ 𝔖₁`, `κ₁ < ∞`.
(ii) `G_a^χ`: `ω_g(δ) = O(δ log(1/δ))` ⇒ `s_j(G_a^χ) = O(j^{−3/2}log j)` ⇒
**`G_a^χ ∈ 𝔖₁`**; adding the rank-2 `F_a` (§0), **`G_a ∈ 𝔖₁`**; same for the
stripped operators. Hence the **genus-0 entire Fredholm determinants**

    D_a(μ) := det(I − μG_a^χ),   D_a^{(n̂)}(μ) := det(I − μG_a^{(n̂),χ})

exist for all `μ ∈ ℂ` (Bombieri-2000-§7 species; cf. COLLISION.md §1). [PROVED]

---

## 3. Deliverable 1 — which determinant exists for which object

Conventions [S]: for `T ∈ 𝔖₁`, `det(I+T) = Π(1+λ_j(T))`, multiplicative,
`|det(I+T)| ≤ e^{‖T‖₁}` [S Ch. 3]. For `T ∈ 𝔖₂`,
`det₂(I+T) := det((I+T)e^{−T}) = Π(1+λ_j)e^{−λ_j}`, `|det₂(I+T)| ≤ e^{‖T‖₂²/2}`,
`det₂(I+T) ≠ 0 ⟺ I+T invertible`, and **for `T ∈ 𝔖₁`:
`det₂(I+T) = det(I+T)·e^{−Tr T}`** [S Ch. 9]. Plemelj–Smithies: for `‖T‖ < 1`,
`log det(I+T) = Σ_{k≥1}(−1)^{k+1}Tr(T^k)/k` (`T ∈ 𝔖₁`); the same series from
`k = 2` equals `log det₂(I+T)` (`T ∈ 𝔖₂`; each `T^k ∈ 𝔖₁` for `k ≥ 2`).
Perturbation determinant of a pair `A = B + V`:
`det((A−z)(B−z)^{−1}) = det(I + V(B−z)^{−1})`, defined iff `V(B−z)^{−1} ∈ 𝔖₁`.
ζ-regularized determinant: `det_ζ(A−z) := exp(−∂_s ζ_{A−z}(s)|_{s=0})`, needing
`ζ_A(s) = Σλ_j^{−s}` to converge in some half-plane and continue to `s = 0`.

**3.1 The compact frame (G-side): everything exists.** [PROVED]
`G_a ∈ 𝔖₁` (Cor 2.2) ⇒ `det(I − μG_a)` entire of genus 0; `det₂` exists a
fortiori; for the threshold pair, `Δ ∈ 𝔖₁` and `R^{(n̂)}(z)` bounded ⇒ the
perturbation determinant `det(I + R^{(n̂)}(z)Δ)` exists in **det₁** sense, and
its det₂ regularization differs by the explicit factor `e^{Tr(R^{(n̂)}Δ)}`.
ζ-regularization is NOT available for `G_a` (eigenvalues accumulate at 0:
`Σ|μ_j|^{−s}` diverges in every right half-plane).

**3.2 The unbounded frame (A_a-side): NO standard determinant exists.**
Sharpened no-go, the frame-selection theorem of this cycle:

**Proposition 3.2.** `λ_j(A_a) ≤ C_a·log(j+2)` for all j. [PROVED, given
Su (2.7)–(2.8)] *Proof sketch.* By [Su (2.7)/(2.8)],
`Q_W^a(v) = (2π)^{−1}∫(log|z| − log 2π)|v̂|²dz + O_a(1)‖v‖²` on the form core
`E = span{e_k = e^{iπkx/a}}` [Su, proof of Thm 1.1]. For `v ∈ E_j :=
span{e_k : |k| ≤ j}`: on `|z| ≤ 2πj/a` the log-weight is `≤ log(2πj/a)`; on
`|z| > 2πj/a`, `|v̂(z)|² ≤ 16(2j+1)‖v‖²/(2a·z²)` (each `ê_k(z) =
2(−1)^k sin(az)/(z − πk/a)`, `|z − πk/a| ≥ |z|/2`, Cauchy–Schwarz), and
`∫_{2πj/a}^∞ z^{−2}log z dz = O(a log j/j)`, so the tail is `O(log j)·‖v‖²`.
Min–max over the `(2j+1)`-dimensional `E_j` gives the bound. ∎

**Corollary 3.3** (A-side no-go). [PROVED given Prop 3.2]
(i) `ζ_{A_a}(s)`: since `λ_j ≤ C_a log(j+2)`, `Σ_j λ_j^{−σ} ≥ Σ_j(C_a log j)^{−σ}
= ∞` for every `σ > 0`, and terms do not vanish for `σ ≤ 0`: the spectral zeta
function has **empty domain of convergence**. Heat-kernel route fails too:
`Tr e^{−tA_a} ≥ Σ_j e^{−tC_a log j} = Σ_j j^{−C_a t} = ∞` for `t < 1/C_a`, so
the Mellin integral `∫₀^∞ t^{s−1}Tr e^{−tA_a}dt` diverges at `t = 0` for all s.
**No ζ-regularized determinant of `A_a` exists.**
(ii) `(A_a − z)^{−1} ∉ 𝔖_p` for ANY `p < ∞`: `Σ_j|λ_j − z|^{−p} ≥
Σ_j(C_a log j + |z| + |λ_{min}|)^{−p} = ∞`. So `det`, `det₂`, and every
higher `det_p` of resolvent-type perturbations of `A_a` fail.
(iii) Perturbation determinants for the pair `(A_a-with-g_n, A_a-without)`:
the form perturbation is the non-compact partial-isometry pair
(DEAD-ENDS #12), and sandwiching by resolvents cannot repair it — by (ii) the
resolvents provide no trace-ideal decay at all.

**3.3 CCM clarification.** CCM's `det_reg(D_log^{(λ,N)} − z) = −iλ^{−iz}ξ̂(z)`
(COLLISION.md §2.1) is attached to their **first-order log-Dirac operator**
`D_log`, whose spectrum grows linearly (zero-counting `~ (log λ/π)T`), where
ζ-regularization is viable. It is NOT a determinant of `A_λ = A_a`. Cor 3.3
shows this was forced, not a stylistic choice. **Conclusion of Deliverable 1:
the unique determinant notion available for the threshold-evolution program is
Fredholm det₁ (equivalently det₂ + explicit trace factor) in the screw/G_a
frame.** This upgrades DEAD-ENDS #12 from "the Weil frame fails" to "every
frame except the compact screw frame fails, provably, on the A-side too."

---

## 4. Deliverable 2 — the domain-fixed det₂ formula [PROVED, with a CORRECTION]

Fixed interval `[−a,a]`, `a = a_n + η` under (Iso). Pair:
`G_a^χ` (full kernel) vs `G_a^{(n̂),χ} = G_a^χ − Δ_{n,η}` (kernel `g − g_n`).

### 4.1 The factorization and hypotheses
Exact algebra: `(G_a^χ − z) = (G_a^{(n̂),χ} − z)(I + R^{(n̂)}(z)Δ)`. Hypotheses:
`Δ ∈ 𝔖₁ ⊂ 𝔖₂` (PROVED §2); `R^{(n̂)}(z)` bounded for `z` off `spec(G_a^{(n̂),χ})`
— and since `‖Δ‖ ≤ (2/√3)c_nη²`, for fixed `z ∉ spec(G_a^χ)` and
`η < η₀(z)` both resolvents exist with `‖R^{(n̂)}(z)‖ ≤ ‖R(z)‖/(1 − ‖R(z)‖‖Δ‖)`.
Hence the perturbation determinant

    𝒟_n(z) := det(I + R^{(n̂)}(z)Δ) = det((G_a^χ − z)(G_a^{(n̂),χ} − z)^{−1})

exists in det₁ sense; `det₂(I + R^{(n̂)}Δ) = 𝒟_n(z)e^{−Tr(R^{(n̂)}(z)Δ)}`;
`𝒟_n(z) ≠ 0 ⟺ z ∉ spec(G_a^χ)`. Orientation note: the brief's literal
`det₂(I + R(z)Δ)` with `R(z) = (G_a − z)^{−1}` (full resolvent) is the exact
reciprocal direction: `det(I − R(z)Δ) = 𝒟_n(z)^{−1}` (multiplicativity on
`I + 𝔖₁` [S Ch. 3]), and `Tr(R(z)Δ) = Tr(R^{(n̂)}(z)Δ) + O(η⁴)` (resolvent
identity `R − R^{(n̂)} = −RΔR^{(n̂)}`, so the difference is
`−Tr(RΔR^{(n̂)}Δ) ≤ ‖R‖‖R^{(n̂)}‖‖Δ‖²_HS`). All leading-order statements below
hold verbatim for either orientation up to overall sign. [PROVED]

### 4.2 The removed k = 1 term — exact leading order (CORRECTING THRESHOLD.md §2)
Key identity: `R(z) = −z^{−1}I + z^{−1}R(z)G` (resolvent algebra), so with
`Tr Δ = 0` (§1.2) the delta-diagonal part contributes **nothing**:

    Tr(R(z)Δ) = z^{−1}Tr(R(z)GΔ) = ∬ ρ(z;x,y)·k_Δ(y,x)dxdy,

where `ρ(z;·,·) := z^{−1}·(kernel of R(z)G) = kernel of R(z) + z^{−1}I` is the
**continuous part of the resolvent kernel**. Continuity of `ρ` on the closed
square [PROVED]: iterate once more, `RG = −z^{−1}G − z^{−2}G² + z^{−2}G(RG)G`;
`G`, `G²` have continuous kernels and the sandwich `G·(bounded)·G` has kernel
`⟨k_x, T k_y⟩` continuous since `x ↦ g(x−·)` is `L²`-continuous. (Trace ↔
kernel-integral interchange: `RG ∈ 𝔖₂`, `Δ ∈ 𝔖₂`, and `Tr(ST) = ∬S(x,y)T(y,x)`
for HS pairs [S Ch. 3]; no Mercer needed.) In the eigenbasis `G^χ_aφ_j = μ_jφ_j`:
`ρ(z;x,y) = Σ_j [μ_j/(z(μ_j − z))]φ_j(x)φ_j(y)` (L²-sense; continuity as above).

By parity (`g` even ⇒ `[G, parity] = 0`) and symmetry, `ρ(z;a,−a) = ρ(z;−a,a)`,
and the two corners contribute equally. Freezing `ρ` at the corner and using
the exact corner mass (§1.3), with error controlled by the modulus of
continuity `ω_ρ(δ) = O(δ log(1/δ))` (inherited from `ω_g` through the three
displayed terms of `RG`):

**Theorem 4.2 (one-threshold trace term).** [PROVED] For fixed `z` off the
spectrum, as `η → 0⁺` under (Iso):

    Tr(R(z)Δ_{n,η}) = (8/3)·Λ(n)n^{−1/2}·η³·ρ(z; a, −a)
                      + O(Λ(n)n^{−1/2}·η⁴·log(1/η)),

and identically with `R^{(n̂)}, ρ^{(n̂)}` (difference `O(η⁴)`).

**Correction of THRESHOLD.md §2.** The Phase-0 claim
`Tr(RΔ) ≈ 4Λ(n)n^{−1/2}η²·G_a(z;a,−a)` is **wrong in both the power and the
constant**: the correct leading term is `(8/3)c_nη³ρ(z;a,−a)`. Reason: the
trace is an L¹-pairing against the corner kernel, whose total mass is
`(8/3)c_nη³` (§1.3), not the HS norm `√(8/3)c_nη²`; and `η²` would require the
resolvent kernel to blow up like `η^{−1}` at the corner, refuted by the proved
continuity of `ρ`. The Phase-0 *mechanism* — "the prime `p^k` measures
boundary-to-boundary transport `ρ(z; a, −a)` at the exact scale where the
window first spans `log p^k`" — **survives intact**; only the weight changes:
`η³`, constant `8/3`. T2's Euler-phase target is unchanged in substance: if
`ρ(z;a,−a)` carries `e^{2iaz}`, the factor is `Λ(n)n^{−1/2}n^{±iz}·(8/3)η³`.

### 4.3 The k ≥ 2 series — exact k = 2 term and full bounds [PROVED]
For `‖R^{(n̂)}Δ‖ < 1` (holds for `η < η₀(z)`):

    log det₂(I + R^{(n̂)}(z)Δ) = Σ_{k≥2} (−1)^{k+1} Tr((R^{(n̂)}(z)Δ)^k)/k .

- **k = 2, exact leading order:** using `R = −z^{−1} + z^{−1}RG` and
  `Tr Δ² = ‖Δ‖²_HS = (8/3)c_n²η⁴` exactly, plus corner-localization
  (`∬|kernel of Δ²| ≤ 16c_n²η⁵`, since each column mass of `k_Δ` is
  `≤ 2c_nη²` on a support of length `4η`):

      Tr((R^{(n̂)}Δ)²) = z^{−2}(8/3)Λ(n)²n^{−1}η⁴·(1 + O(η)),
      hence the k=2 term  = −(4/3)Λ(n)²n^{−1}η⁴z^{−2}(1 + O(η)).

- **k ≥ 3, trace-ideal bounds** (Hölder in 𝔖-ideals, [S Ch. 2]):

      ‖(R^{(n̂)}Δ)^k‖₁ ≤ ‖R^{(n̂)}Δ‖²_HS·‖R^{(n̂)}Δ‖^{k−2}
                       ≤ ‖R^{(n̂)}‖^k·(8/3)c_n²η⁴·((2/√3)c_nη²)^{k−2},

  so `|Σ_{k≥3}| ≤ (8/3)c_n²η⁴·‖R‖²·(‖R‖‖Δ‖)/(3(1−‖R‖‖Δ‖)) = O(c_n³η⁶)`. Total:

      log det₂(I + R^{(n̂)}(z)Δ) = −(4/3)Λ(n)²n^{−1}η⁴z^{−2} + O(η⁵).

**Structural consequence.** The det₂-regularized update is `O(η⁴)`; the entire
`O(η³)` threshold response sits in the removed trace term. det₂ thus cleanly
splits "arithmetic entry" (k = 1, linear in `Λ(n)n^{−1/2}`, corner-transport
coefficient) from "self-interaction" (k ≥ 2, quadratic and higher). [PROVED]

### 4.4 The P_a-compressed frame (Suzuki's actual G_a) [PROVED]
On `L²₀(−a,a)` with `Δ_P := P_aΔP_a`, `G_P := P_aG^{(n̂)}P_a`:
- `Δ_P` is **not traceless**: `Tr Δ_P = −⟨e_a, Δe_a⟩ = −(2a)^{−1}∬k_Δ =
  −(4/3)Λ(n)n^{−1/2}η³/a` — the mean-removal converts corner mass into trace,
  at the same η³ order, suppressed by `1/a = 2/(log n + 2η)`.
- HS/trace norms change only at `O(η^{5/2})`: `‖Q_aΔ‖²_HS ≤ 16c_n²η⁵/(2a)`.
- Trace term: `Tr(R_PΔ_P) = Tr((P_aR_PP_a)Δ)`; the kernel of `P_a` is
  `δ(x−y) − (2a)^{−1}`, so the delta part now leaves a residue and

      Tr(R_P(z)Δ_P) = (8/3)Λ(n)n^{−1/2}η³·[ σ_P(z;a,−a) + (2az)^{−1} ]
                      + O(c_nη⁴log(1/η)),

  `σ_P := kernel of z^{−1}P_a(R_PG_P)P_a` (continuous, same sandwich proof).
  The mean-removal shifts the corner-transport coefficient by the universal
  `(2az)^{−1}` — exactly computable, no new analytic difficulty.

---

## 5. Deliverable 3 — Hadamard variation for the growing interval [PROVED]

Fixed continuous kernel `k(x,y)` on growing `[−a,a]`; `K_a := χ_aKχ_a`,
`D(a;μ) := det(I − μK_a)` (exists: §2 applies whenever `k` has Dini-type
modulus; for bare continuity use that `K_a ∈ 𝔖₁` is part of the hypothesis —
satisfied here by Cor 2.2).

### 5.1 Derivation (classical, done cleanly from the Fredholm series)
Fredholm expansion, absolutely convergent for all μ by Hadamard's inequality
(`|det[k(x_i,x_j)]_{m×m}| ≤ m^{m/2}‖k‖_∞^m`):

    D(a;μ) = Σ_{m≥0} ((−μ)^m/m!) ∫_{[−a,a]^m} det[k(x_i,x_j)]_{i,j≤m} dx₁…dx_m.

Each `F_m(a) := ∫_{[−a,a]^m}det[…]` is C¹ with, by symmetry of the integrand
under simultaneous permutation and Leibniz' rule,
`F_m′(a) = m[∫_{[−a,a]^{m−1}}det[…]|_{x₁=a} + ∫_{[−a,a]^{m−1}}det[…]|_{x₁=−a}]`.
The differentiated series is dominated by `Σ_m (|μ|^m/m!)·2m·m^{m/2}‖k‖^m(2a)^{m−1}`,
convergent for every μ (as `m^{m/2}/m! ≤ (e/√m)^m`), uniformly on compacts in
`a` — so term-by-term differentiation is legitimate. Resumming yields the first
Fredholm minor `D₁(x,y;μ,a)`, and Fredholm's classical identity
`D₁(x,y)/D = Γ_a(x,y;μ) := kernel of K_a(I−μK_a)^{−1}` (continuous up to the
closed square, same sandwich argument as §4.2) gives, wherever `D ≠ 0`:

**Theorem 5.1 (Hadamard boundary-variation).**

    (d/da) log det(I − μK_a) = −μ[ Γ_a(a, a; μ) + Γ_a(−a, −a; μ) ].

*(Check at order μ: `−μ[k(a,a)+k(−a,−a)] = (d/da)(−μ∫_{−a}^a k(x,x)dx)` ✓.)*

### 5.2 Resolvent-variable form — one language for both parts
With `z = 1/μ`: `(I − μK_a)^{−1} = −zR_a(z)`, so `−μΓ_a = kernel of K_aR_a(z)`
and, with the SAME `ρ` as §4.2 (`ρ_a = z^{−1}·kernel(R_aK_a)`):

    (d/da) log D_a(z) = z[ ρ_a(z; a, a) + ρ_a(z; −a, −a) ] .

**The continuous flow reads the resolvent kernel at the two DIAGONAL corners
`(±a, ±a)`; the prime-threshold term (§4.2) reads it at the ANTI-DIAGONAL
corner `(a, −a)`.** One function `ρ` carries the whole evolution. [PROVED]

### 5.3 P_a-dressing of the determinant [DERIVED, elementary]
`det(I − μG_a) = det(I − μG_a^χ)·det(I + μ(I − μG_a^χ)^{−1}F_a)`, and since
`rank F_a ≤ 2` (range ⊆ span{e_a, χ_aGe_a}), the second factor is the 2×2
determinant `det(δ_{ij} + μ⟨ψ_i, (I−μG_a^χ)^{−1}ϕ_j⟩)` with explicit
`ϕ_j, ψ_i ∈ {e_a, χ_aGe_a, …}` built from `g` and constants; every entry is a
continuous (indeed differentiable where `ρ` is) function of `a`. Thus the
Hadamard formula transfers to Suzuki's `G_a` with an explicitly computable
rank-2 correction term; no new analytic content. (Note `G_a1 = 0`, so on
`L²(−a,a)` the determinant of `I − μG_a` equals its restriction to `L²₀`.)

---

## 6. Deliverable 4 — the assembled one-threshold update [PROVED as stated]

Under (Iso), for fixed `z ∉ spec(G^χ_{a_n})` and `0 < η < η₀(z)` (so that all
resolvents below exist), split the move `a_n → a_n + η` into (domain growth
with stripped kernel) + (kernel entry at fixed final domain) — exact, since
`Δ_{n,0} = 0` makes the two paths agree at the corner of the square:

    log D_{a_n+η}(z) − log D_{a_n}(z)
      = [ log D^{(n̂)}_{a_n+η} − log D^{(n̂)}_{a_n} ]      (I: Hadamard flow)
      + [ log D_{a_n+η} − log D^{(n̂)}_{a_n+η} ]           (II: threshold entry)

    (I)  = ∫_{a_n}^{a_n+η} z[ ρ^{(n̂)}_a(z;a,a) + ρ^{(n̂)}_a(z;−a,−a) ] da
           (Thm 5.1/§5.2; this is the continuous part, where [Su Thm 1.3]'s
            compact-embedding continuity machinery lives)

    (II) = log 𝒟_n(z) = Tr(R^{(n̂)}(z)Δ) + log det₂(I + R^{(n̂)}(z)Δ)
         = (8/3)Λ(n)n^{−1/2}η³·ρ^{(n̂)}(z; a_n+η, −a_n−η)
           + O(Λ(n)n^{−1/2}η⁴log(1/η))                     (k = 1, Thm 4.2)
           − (4/3)Λ(n)²n^{−1}η⁴z^{−2}(1 + O(η))            (k = 2, §4.3)
           + O(Λ(n)³n^{−3/2}η⁶‖R‖³)                        (k ≥ 3, §4.3)

Hypotheses checked: `G^χ ∈ 𝔖₁` (Cor 2.2); `Δ ∈ 𝔖₁` with all norms exact (§1);
resolvent bounds and invertibility of `I + R^{(n̂)}Δ` (§4.1); trace↔kernel
interchange in 𝔖₂ (§4.2); term-by-term differentiation (§5.1). In the P_a
frame add §4.4's `(2az)^{−1}` shift and the rank-2 dressing (§5.3).

**Corollary 6.1 (threshold regularity).** [DERIVED] `a ↦ log D_a(z)` is C¹
across `a = a_n`: part (II) is `O(η³)`, with `d(II)/dη → 0` as `η → 0⁺`. The
prime enters at exact order `η³` with coefficient
`(8/3)Λ(n)n^{−1/2}ρ(z;a_n,−a_n)` — a singularity first visible in the third
a-derivative (third-derivative-jump statement modulo differentiability of the
`O(η⁴log(1/η))` error, hence DERIVED not PROVED).

**6.2 Consequence for T3 (accumulation bookkeeping).** The corrected per-prime
entry weight is `η³` (not `η²`), and post-entry the same object is governed by
the Hadamard flow, not by re-summed entry terms; THRESHOLD.md §3's red-team
divergence equation is unaffected in substance but its "entry suppression"
should read `η³`. The det₂ split localizes the *linear-in-Λ* content entirely
in the removed trace — so T3's question "does det₂'s removed term contain
exactly the divergent part?" is now precise: the divergent accumulation is
`Σ_n (8/3)Λ(n)n^{−1/2}η_n³ρ(z;·)` + Hadamard flow, and the PNT cancellation
must occur between `ρ`'s archimedean drift and the prime sum inside (I)+(II).

**6.3 Caveat (twin thresholds).** (Iso) requires `2η < log(n′/n) ≈ (n′−n)/n`.
Along twin primes `n′ − n = 2`, admissible η shrinks like `1/n`. Any
accumulation scheme that keeps `η` fixed per prime MUST use the additive
multi-threshold version (§0), where simultaneously-entering `Δ_m` simply add
at the stated orders. This is a real constraint on prime-by-prime telescoping.

---

## 7. Deliverable 5 — failure points and what survives

1. **THRESHOLD.md §2 corrected** (not failed): trace term is
   `(8/3)Λ(n)n^{−1/2}η³ρ(z;a,−a)`, not `4Λ(n)n^{−1/2}η²·Green`. Mechanism
   (end-to-end corner transport) survives; T2's phase question intact.
2. **COLLISION.md §4.1 sharpened**: `‖Δ‖₁ = 8κ₁c_nη²` exactly ∝ η² (no log);
   trace-class OPEN-minor of THRESHOLD.md §1 closed (PROVED).
3. **A_a-frame determinant program: PRECISE FAILURE** (Cor 3.3): empty
   ζ-convergence domain and `(A_a−z)^{−1} ∉ 𝔖_p ∀p` — no det of any standard
   species exists for `A_a`. The weaker statement that survives is exactly the
   G-frame theory of §§4–6 (and CCM's det_reg on `D_log`, a different operator).
4. **No failure in the main chain**: Deliverables 2–4 close as PROVED under
   (Iso) with explicit constants; the only DERIVED items are the rank-2
   P_a-dressing bookkeeping (§5.3, elementary) and the third-derivative-jump
   phrasing (Cor 6.1); the only genuinely OPEN items exported: the large-`a`
   behavior of `ρ(z;a,−a)` (T2) and the summability of the assembled flow
   (T3), both outside T1's mandate.
