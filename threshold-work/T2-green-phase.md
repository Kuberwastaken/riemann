# T2 — Large-a behavior of the boundary-to-boundary Green kernel of A_a (PROVER, independent)

*Task: leading behavior of Γ_a(z; a, −a), kernel of R_a(z) = (A_a − z)^{−1}, z in a fixed
compact K ⊂ ℂ ∖ ℝ; adjudicate the conjectured phase law Γ_a(z; a, −a) ∼ e^{2iaz}·Amp(a);
one-threshold factor and k-resummation at fixed p; amplitude inequality for convergence.
Sources: Suzuki arXiv:2606.09096 (1.3), (2.2), Thm 1.1/1.4/1.5, §7, §8; COLLISION.md §0;
DEAD-ENDS.md. Written independently of the other T-agents' drafts. Labels:
PROVED / DERIVED / HEURISTIC / OPEN. δ_K := dist(K, ℝ) > 0 throughout.*

---

## 0. Normalizations and the exact model symbol

A_a = Friedrichs extension of B_a = D*G_aD (Suzuki Thm 1.1); distribution kernel of A_a
is k(x−y) with k = −g″ (Suzuki §6.1), g as in (1.3)/(2.2):

    g(t) = ½|t|log|t| + A|t| + Σ_{n≤e^{|t|}} Λ(n)n^{−1/2}(|t| − log n) − 4(cosh(t/2) − 1) + r̃(t),
    A = ½(log 2π + C₀ − 1),   r̃ ∈ C², r̃ = O(t²).

FT convention ĝ(ζ) = ∫ g e^{iζt} dt. Distributional (finite-part) transforms:
F[|t|] = −2/ζ², F[|t|log|t|] = (2/ζ²)(log|ζ| − ψ(2)). Hence the **archimedean model
symbol** (singular part ½|t|log|t| + A|t|, no primes, no pole term):

    m₀(ζ) := ζ² ĝ_sing(ζ) = log|ζ| − ψ(2) − 2A = **log(|ζ|/2π)**.       [PROVED]

Cross-checks: (i) m₀/2π is exactly the Riemann–von Mangoldt smooth zero density
(1/2π)log(T/2π); (ii) window scaling reproduces Suzuki Thm 1.4: lowest frequency
|ζ| ≍ 1/a gives λ_a = log(1/a) − log 2π + O(1) — matches his constant −log 2π + ψ(2) − 1.
Prime part of k: −Σ_n Λ(n)n^{−1/2}[δ(t − log n) + δ(t + log n)] (edge kinks of (1.3),
COLLISION §0 dictionary), i.e. symbol −2Σ Λ(n)n^{−1/2}cos(ζ log n); pole part of k:
+2cosh(t/2) = rank-2 |f₊⟩⟨f₋| + |f₋⟩⟨f₊|, f_± = e^{±x/2}. The full symbol is the
boundary distribution 2πΣ_γ δ(ζ − γ) of F(ζ) = −i(ξ′/ξ)(½ − iζ) = Σ_γ (ζ − γ)^{−1}
(Weil explicit formula; poles of the symbol at ζ = ±i/2 are the pole term).

Friedrichs = free compression here: the form closure of C_c^∞(−a,a) in the Q-norm is the
H^log-window space with **no boundary condition** (constants ∈ D(A_a), Suzuki after
Thm 1.1) — log-order operators do not see endpoint constraints. So A_a is the finite
section (truncated Wiener–Hopf) of the convolution k∗ on the window.        [PROVED at
form-domain level, from Suzuki Thm 1.1 + Cor 1.2]

Preliminary obstruction (independent re-derivation): Weyl law for m₀ gives
N_a(Λ) ≈ 4a e^Λ, i.e. λ_j(A_a) ≈ log(j/4a): eigenvalues grow logarithmically, so
Σ_j |λ_j − z|^{−q} = ∞ for every q. **R_a(z) is compact but in no Schatten class, and its
kernel is NOT a continuous function** — the diagonal singularity is ≍ 1/(|x−y| log²|x−y|)
(integrable, unbounded). The premise "continuous Green kernel" in the task is false;
Γ_a(z;·,·) exists as a kernel continuous OFF the diagonal and off the prime lattice
(§2 below), and (a, −a) is the extreme off-diagonal point, so Γ_a(z; a, −a) is
well-defined for 2a outside the singular lattice.                          [PROVED]

## 1. Q1 — the phase law: REFUTED for A_a; the correct law

### 1.1 Full-line arch model, exact large-t law [PROVED]

Γ⁰_∞(z; t) = (2π)^{−1}∫_ℝ e^{iζt}(m₀(ζ) − z)^{−1}dζ. Contour rotation of the two
half-line pieces into ±i[0,∞) (principal log; Jordan arcs vanish for t > 0):
for ℑz ∈ (0, π/2) the rotation of the e^{+iζt} piece crosses the unique first-quadrant
solution ζ_*(z) := 2πe^{z} of m₀(ζ) = z; the jump of (log − z)^{−1} across the
imaginary axis is −iπ/[(L − z)² + π²/4], L = log(ξ/2π). Result, for t > 0:

    Γ⁰_∞(z; t) = 1_{(0,π/2)}(ℑz)·iζ_*(z) e^{iζ_*(z) t}
               + ½∫₀^∞ e^{−ξt} dξ / [(log(ξ/2π) − z)² + π²/4],

and Watson's lemma on the background integral (h slowly varying, |h′/h| = O(1/log t)):

    **Γ⁰_∞(z; 2a) = bg(2a, z)·(1 + O_K(1/log a)) + O_K(e^{−c_K a}),
       bg(2a, z) = (1/4a)·[(log 4πa + z)² + π²/4]^{−1}.**

Named uniform estimates: (U1) |Γ⁰_∞(z;t) − bg(t,z)| ≤ C_K[e^{−c_K t} + (t log³t)^{−1}]
on K, t ≥ t₀(K); (U2) resonance bound |ζ_* e^{2iaζ_*}| ≤ C_K e^{−2a·ι_K},
ι_K := inf_K ℑζ_* = 2π inf_K e^{ℜz}sin(ℑz) > 0 for K in the strip 0 < ℑz < π/2
(for ℑz ≥ π/2 the pole is never crossed / sits in the absorbed background piece and the
same exponential bound holds; ℑz < 0 by conjugation).

### 1.2 Verdict on e^{2iaz}

**REFUTED.** The boundary-to-boundary Green kernel of A_a carries **no factor e^{2iaz}**:

- The only oscillatory-in-a term in the model is the evanescent resonance
  **e^{2ia·ζ_*(z)} = e^{4πi a e^{z}}** — frequency 2πe^{ℜz}, not z — with amplitude
  iζ_*(z) = O_K(1) times exponential damping e^{−2aι_K} off the real axis. A log-symbol
  operator transports at group velocity m₀′(ζ_*) = 1/ζ_*; the accumulated phase across
  the window is 2aζ_*(z), not 2az. The free-transport phase e^{2iaz} would require a
  first-order symbol m(ζ) = ζ.
- The dominant term on K is **non-oscillatory**: bg(2a, z) ≍ 1/(4a log²(4πa)) — the
  amplitude the task asks for is polynomial-log, Amp(a,z) = (4a)^{−1}(log 4πa + z)^{−2}
  ·(1 + O(1/log a)), with z entering polynomially, not through a phase.
- Weyl-phase reading [DERIVED]: each frame's oscillation is e^{iπN(z)} for its counting
  function. For A_a: N_a(z) ≈ 4a e^{z} ⇒ e^{4πiae^z} = e^{2iaζ_*} (the resonance).
  For the first-order objects — Suzuki's D_{a,θ} on H(T_a), CCM's D_log^{(λ)} —
  N(z) ≈ (2a/π)z ⇒ e^{2iaz}. **The e^{2iaz} phase lives exactly in the first-order
  frame**: ĥ_{a,±}(z) = (e^{a(1±iz)} − e^{−a(1±iz)})/(1 ± iz) in Suzuki §8.3 gives
  W(a,θ;z) its e^{±iaz} chiral pieces (ratio e^{2iaz}), = CCM's λ^{−iz} (a = log λ,
  COLLISION §0). It is a deficiency/boundary-form phenomenon of D_a = id/dx, i.e. the
  exponential type of the de Branges space of transforms of L²(−a,a) — NOT a property
  of the resolvent of A_a. The task's question conflates the two resolvents; the phase
  law is true for W(a,θ;z) (trivially, from supp ⊂ [−a,a]) and false for Γ_a.

### 1.3 Transfer to the window and the remaining pieces

- Friedrichs/finite-section correction [DERIVED]: Schur complement on the exterior
  half-lines gives Γ_a^{arch}(z; a,−a) = E₊(z)E₋(z)·bg(2a,z)(1 + o(1)); the edge
  factors are the half-line Wiener–Hopf renormalizations of the symbol log(|ζ|/2π) − z,
  a-independent to leading order, |E_±| ≤ C_K. (U3) two-sided comparability
  c_K ≤ |Γ_a^{arch}(a,−a)|/bg(2a,z) ≤ C_K: upper bound DERIVED; the lower-bound
  constant (non-cancellation in the WH factorization) OPEN. Slow kernel decay
  1/(t log²t) makes the finite-section expansion parameter 1/log a, not e^{−ca}:
  all corrections enter at relative O(1/log a).
- Zeta-pole term [DERIVED]: Woodbury on V = |f₊⟩⟨f₋| + |f₋⟩⟨f₊|. With
  R₀f_± ≈ c_± f_± + edge layers, c_± = (log(1/4π) − z)^{−1} (even continuation of m₀
  to ζ = ±i/2), the 2×2 Gram matrix has diagonal ≍ e^a and anti-diagonal ≍ a; the
  endpoint correction telescopes to (c₊ + c₋)e^{−a}(1 + O(a e^{−a})). (U4):
  |δΓ_pole(a,−a)| ≤ C_K a e^{−a}. The naive e^{a/2}·e^{a/2} corner enhancement is
  annihilated by the e^{−2a} of the inverse Gram matrix.

## 2. Prime thresholds at the endpoint corner [DERIVED at Born level; structure stable]

Born-1 in the prime part of the symbol: (m − z)^{−1} = (m₀ − z)^{−1}
+ 2Σ_n Λ(n)n^{−1/2}cos(ζ log n)(m₀ − z)^{−2} + … . With F₂ := IFT[(m₀ − z)^{−2}]
= ∂_z Γ⁰_∞:

    δΓ_n(a, −a) = Λ(n)n^{−1/2}·[F₂(2a − log n) + F₂(2a + log n)],
    F₂(t) = −(log 2πt + z)/(t[(log 2πt + z)² + π²/4]²) ≈ −1/(t(log 2πt + z)³)  (t → ∞),
    F₂(ε) = +2/(ε|log 2πε|³)·(1 + O(1/|log ε|))                                (ε → 0⁺).

- **One-threshold endpoint factor** (a = ½log n + η, i.e. overlap 2η of the window with
  its log n-translate): δΓ_n(a,−a) = Λ(n)n^{−1/2}·(η|log η|³)^{−1}(1 + o(1)).
  The conjectured factor Λ(n)n^{−1/2}·η²·e^{2iaz} is wrong twice: the amplitude is the
  corner singularity 1/(η|log η|³), not the HS mass η² (COLLISION §4's η² is the
  ‖ΔG_n‖_HS of the g-kernel update — a different, integrated object); and there is
  **no character n^{iz}**: the z-dependence of the threshold factor is polynomial,
  through (log(·) + z)^{−3}.
- **Dense singular lattice** [PROVED for the kernel's singular support]: the resolvent
  kernel has integrable singularities on displacement hyperplanes
  x − y = ±(log n₁ ± log n₂ ± …); the endpoint displacement 2a hits this set on a dense
  (spacing ~ e^{−2a}) set of a. The pointwise endpoint value is therefore only
  meaningful for a off e^{−a}-neighborhoods of the lattice, or after local averaging.
- **Norm-forced screening** [PROVED]: (U6) for unit-L²-normalized bumps χ_± at ±a,
  |⟨R_a(z)χ_−, χ₊⟩| ≤ 1/|ℑz|. But the unit-averaged Born-1 prime sum is
  ≈ Σ_{log n∈(2a−2,2a)} Λ(n)n^{−1/2}·O(1) ≈ 4e^{a} (U5: PNT,
  Σ_{log n ≤ u}Λ(n)n^{−1/2} = 2e^{u/2}(1 + O(e^{−c√u}))). Contradiction by a factor
  ≍ e^{a}|ℑz| ⇒ **perturbation theory in the primes fails at every finite order at the
  endpoint; nonperturbative cancellation must reduce the accumulated threshold mass by
  exactly the factor e^{a} = √(n_max)**. This is the Green-kernel shadow of the same √n
  that makes E(λ) (COLLISION §3) hard; consistent with DEAD-ENDS #12 (and the divergence
  is driven by the k = 1, p ≍ e^{2a} bulk mass, not only by near-threshold corners).

Assembled Q1 answer (a off the lattice; statuses as marked):

    Γ_a(z; a, −a) = E₊E₋·(1/4a)[(log 4πa + z)² + π²/4]^{−1}(1 + O(1/log a))   [arch]
                  + O_K(e^{−2aι_K})·e^{4πiae^{z}}-resonance                    [only phase]
                  + O_K(a e^{−a})                                              [pole]
                  + screened prime-threshold sum: Born-divergent, ≤ O_K(1) on unit
                    average by (U6); true size OPEN (arithmetically heavy observable).

## 3. Q2 — k-resummation at fixed p: NOT a z-twisted Euler factor; exact residual

Hypothesized (pattern) object: Σ_k Λ(p^k)p^{−k(1/2−iz)}·w_k = log p/(p^{1/2−iz} − 1)
for flat weights — the p-local factor of −ζ′/ζ at s = ½ − iz. Derivation with the
ACTUAL factors of §2, T_p(a,z) := Σ_{k=1}^{K_p} Λ(p^k)p^{−k/2}[F₂(2a − k log p)
+ F₂(2a + k log p)], K_p = ⌊2a/log p⌋:

- Bulk terms: F₂(2a ∓ κ)/F₂(2a) = 1 ± κ/2a + 3κ·(±1)/(2a(log 4πa + z)) + O(κ²/a²);
  **the linear tilts cancel in the ± pair**, so
  [F₂(2a − κ) + F₂(2a + κ)] = 2F₂(2a)(1 + O(κ²/a²)).
- Near-threshold terms k ≈ K_p: bounded by Λ(p^k)p^{−K_p/2}F₂(ε_K) = O(a e^{−a/2}) for
  p-regular a (dist(2a, ℤ log p) ≥ e^{−a/2}).

    **T_p(a,z) = 2F₂(2a; z)·[log p/(p^{1/2} − 1)]·(1 + O_p(a^{−2})) + O(a e^{−a/2}).**

So the resummation DOES close to a p-local Euler-type object — but it is the local
factor of −ζ′/ζ **at s = ½, real and untwisted**; the spectral variable z sits entirely
in the universal prefactor F₂(2a; z), never as p^{ikz}. Exact residual against the
ansatz (same normalization):

    T_p − 2F₂(2a)·log p/(p^{1/2−iz} − 1)
      = 2F₂(2a)·Σ_k Λ(p^k) p^{−k/2}(1 − p^{ikz}) + O_p(a^{−2}·F₂(2a)) + O(a e^{−a/2}),
      = 2F₂(2a)·log p·[1/(√p − 1) − 1/(p^{1/2−iz} − 1)] + (same errors),

nonzero for every z ∉ (2π/log p)ℤ: **the missing ingredient is precisely the
multiplicative character p^{ikz}, i.e. the phase refuted in Q1.** [DERIVED]
Where the twisted object genuinely lives: on the frequency side —
1/ĝ(z) = z²ξ(1/2 − iz)/ξ′(1/2 − iz) (Suzuki §8.3) contains the s = ½ − iz Euler
structure, and it is reached by objects built on the characters e^{izx}
(eigenfunctions of D_a*: (T_a v_z)(x) = e^{−izx}, Thm 1.5 proof), where translation by
log n yields n^{iz} exactly. Euler factors come from translations acting on characters
(first-order frame), not from translations acting on the radial Green profile
(A_a frame). The two frames' objects are related by v̂_{a,±} = ĥ_{a,±}/ĝ — division by
ĝ, not resolvent composition.

## 4. Q3 — the amplitude inequality controlling convergence on K

Let 𝒜_n(a,z) be the per-threshold endpoint amplitude in any bookkeeping of the
accumulated sum S(a,z) = Σ_{p^k ≤ e^{2a}} Λ(n)n^{−1/2}𝒜_n(a,z). By (U5) the Λ-weighted
threshold density is d(Σ_{log n≤u}Λ(n)n^{−1/2}) ≈ e^{u/2}du, so with ε_n := 2a − log n:

    Σ_n Λ(n)n^{−1/2}φ(ε_n) = e^{a}·∫₀^{2a} φ(ε)e^{−ε/2}dε·(1 + O(e^{−c√a})).

**Absolute-convergence criterion (uniform in a, z ∈ K):**

    |𝒜_n(a,z)| ≤ C_K · n^{−1/2} · ω(2a − log n)   with   ∫₀^∞ ω(ε) dε < ∞
    (equivalently |𝒜_n| ≤ C_K e^{−a} e^{ε_n/2} ω(ε_n); note n^{−1/2} = e^{−a}e^{ε_n/2}),

i.e. **each threshold must arrive with one extra factor n^{−1/2} beyond its
explicit-formula weight Λ(n)n^{−1/2}** — total per-prime-power weight Λ(n)/n, the
"one-line" weight. Sufficiency: immediate from the display above (S ≤ C_K·∫ω).
Necessity holds for positive/one-signed amplitudes; with oscillating signs, conditional
convergence via arithmetic sign equidistribution is not excluded — OPEN.  [DERIVED]

Adjudication of the actual kernel: the Born amplitude 𝒜_n = F₂(ε_n) + F₂(2a + log n)
satisfies |𝒜_n| ≍ min(1/(ε_n log³ε_n), 1/(a log³a)) — it **fails the criterion by
exactly the factor n^{1/2}** (both in the corner regime and in bulk mass). Unconditional
counterweight: by (U6) the criterion's CONCLUSION (bounded averaged endpoint kernel)
holds anyway — self-adjointness forces the screening that perturbation theory cannot
see. The mechanism of that √n-screening is the same open arithmetic core as (CCM-b)/
E(λ) (COLLISION §3); nothing here softens it, per DEAD-ENDS #10.

## 5. Status summary

| item | status |
|---|---|
| m₀(ζ) = log(|ζ|/2π) for the singular part of (2.2) | PROVED |
| R_a(z) in no Schatten class; kernel discontinuous on diagonal; λ_j ≈ log(j/4a) | PROVED |
| Model law Γ⁰_∞(z;2a) = bg(2a,z)(1+O(1/log a)) + evanescent e^{4πiae^z} (U1,U2) | PROVED |
| **Phase law e^{2iaz} for Γ_a(z;a,−a): REFUTED**; phase belongs to W(a,θ;z)/λ^{−iz} (first-order frame); A_a's only oscillation is e^{2iaζ_*(z)}, ζ_* = 2πe^z, damped e^{−2aι_K} | PROVED (model) / DERIVED (window) |
| Window transfer, edge factors E_± (U3); pole term O(ae^{−a}) (U4) | DERIVED (constants OPEN) |
| One-threshold endpoint factor Λ(n)n^{−1/2}/(η log³(1/η)), no n^{iz}; dense singular lattice | DERIVED / PROVED (supp) |
| Born endpoint prime sum diverges ≍ e^a; screening forced by ‖R_a‖ ≤ 1/|ℑz| (U6) | PROVED |
| k-resummation → 2F₂(2a;z)·log p/(√p − 1): untwisted s = ½ local factor; residual = missing character p^{ikz}, computed exactly | DERIVED |
| Q3 inequality |𝒜_n| ≤ C_K n^{−1/2}ω(2a − log n), ∫ω < ∞ (⇔ weight Λ(n)/n); actual Born amplitude fails by √n | DERIVED |
| True (screened) size of the prime part of Γ_a(z;a,−a); necessity of Q3 under sign cancellation; exact E_± | OPEN |

*Consequence for the program: the endpoint Green kernel of A_a is an arithmetically
heavy observable in the wrong frame — its phase content (e^{4πiae^z}) is the Weyl phase
of a log-symbol operator and cannot reproduce the λ^{−iz}·ξ̂-structure; the e^{2iaz}/
Euler-factor structure is exclusively a property of the first-order (D_a / de Branges /
CCM D_log) objects, reached by division by ĝ, not by resolvent composition. Threshold
bookkeeping for (CCM-b) should therefore stay in the ĝ-division / det₂-screw frame
(COLLISION §4), never pass through Γ_a.*
