# T3 RED-TEAM — kill report on the prime-threshold determinant-accumulation program

*Agent T3 (COUNTEREXAMPLE HUNTER), first SOLVER cycle. Target: THRESHOLD.md §§2–3,
FRONTIER node "infinite accumulation". Labels per SOLVER.md §7. No RH assumptions
anywhere; every unconditional input is named (Rosser–Schoenfeld, Baker–Harman–Pintz,
classical explicit formula, Laplace-transform analyticity). Numerics: toy model per
mandate, script archived in session scratchpad (`t3_toy.py`), all numbers quoted
below reproduced from that run; matrices used ONLY for the toy.*

## 0. Verdict

**The accumulation program as stated is dead, in both of its readings, with
equations.** Precisely:

- **(Kill A — the entries are empty.)** The threshold entries Δ_{n,η} carry, in
  total HS mass, an exponentially vanishing fraction O(a e^{−a}) of the prime
  content of G_a. The entry-indexed det₂ product converges absolutely and is
  arithmetically trivial (its log is uniformly O(1) on compacts off the spectrum);
  it cannot converge to any Ξ-related limit. All arithmetic lives in the Hadamard
  flow. (§4, Thm 4.2.)
- **(Kill B — the post-entry content diverges at every order ≥ 2.)** The total
  accumulated prime operator P_a = Σ_n Δ_{n,a−½log n} has ‖P_a‖ ≥ 11.7·e^a/a
  (a ≥ 8, unconditional, Rosser–Schoenfeld constant). For the resolvent-dressed
  accumulation, every even-order term of the det₂ series satisfies
  |Tr S^{2m}|/2m ≥ ‖S‖^{2m}/2m with ‖S‖ ≥ c·e^a/poly(a): the series diverges and
  **no det_p regularization for any fixed p can repair it** — the divergence is
  not of trace-subtraction type. (§3, Thm 3.2.)
- **(det₂ audit.)** det₂'s removed linear term absorbs exactly NOTHING of the
  divergence — the bare entries are traceless (removal vacuous), and in the
  dressed form the removed term Tr(R_aΔ_{n,η}) is precisely THRESHOLD §2's
  candidate Euler-phase term: **det₂ deletes the arithmetic, not the divergence.**
  (§3.1.)
- **(Exact missing renormalization.)** The divergence is a **rank-3 defect**: the
  pole kernel −4(e^{t/2}+e^{−t/2}−2) is exactly the rank-3 operator
  −4|u₊⟩⟨u₋| − 4|u₋⟩⟨u₊| + 8|1⟩⟨1|, u_±(x) = e^{±x/2}, and off the 3-dim space
  span{e^{x/2}, e^{−x/2}, 1} the entire prime content is E-sized (poly under RH):
  ‖Q P_a Q‖ ≤ ‖G_a‖ + O(a² log a). The repair, if any, is a rank-3 Schur
  complement/compression by the two ξ-pole directions e^{±x/2} (the s(s−1) factor
  of ξ) plus constants — not any Schatten regularization. (§5, Thm 5.2.)
- **(Sharpest necessary condition — the program has no sub-RH floor.)** After the
  rank-3 renormalization the surviving prime input is the ledger residue
  E(t) = Σ_{n≤e^t} Λ(n)n^{−1/2}(t−log n) − (4e^{t/2}−2t−4), whose exact
  exponential rate is Θ−½ with Θ := sup ℜρ: E(t) = O(t) under RH, and
  E(t) = Ω(e^{(Θ−½−ε)t}) unconditionally whenever Θ > ½ (Laplace-analyticity
  argument, §6). Hence: **the renormalized evolution's bookkeeping is
  subexponential iff RH.** THRESHOLD §3's guess "floor is PNT-strength" is too
  optimistic: the floor is RH-strength in both directions — consistent with CCM
  Cor 3.8, now with the exact rate dictionary (toy-verified: injected zero at
  θ = 0.75 produces measured growth slope 0.496 vs predicted 2θ−1 = 0.5). (§6.)

## 1. Setup and standing facts

Screw frame (COLLISION.md §0; Suzuki arXiv:2606.09096). From Suzuki (1.3):

    g(t) = −4(e^{t/2} + e^{−t/2} − 2)                       [pole term]
           + Σ_{n ≤ e^{|t|}} Λ(n) n^{−1/2} (|t| − log n)     [prime term]
           + (archimedean part: ½|t|log|t| + A|t| + r(t), A = 0.7075…,
              r ∈ C², r(t) = O(t²); Suzuki (2.2))

G_a = P_a^{proj} G P_a^{proj} on L²(−a,a), continuous kernel g(x−y), compact,
self-adjoint. B_a = D*G_aD, A_a = Friedrichs(B_a) (Suzuki Thm 1.1). The threshold
update at a = ½log n + η is Δ_{n,η}, kernel Λ(n)n^{−1/2}(|x−y|−log n)₊, with
‖Δ_{n,η}‖_HS = √(8/3)·Λ(n)n^{−1/2}·η² exactly (THRESHOLD §1; independently
re-verified numerically here to 6 digits: n = 2, η = 0.25 gives 0.050024 both ways).

**Prime-content operator.** P_a := integral operator on L²(−a,a) with kernel
k_P(x−y), k_P(t) = Σ_n Λ(n)n^{−1/2}(|t|−log n)₊. Identity [PROVED, kernels add]:

    P_a = Σ_{n ≤ e^{2a}} Δ_{n, a−½log n}     (the operator sum of ALL threshold
                                              updates present at scale a).

**Ledger sums.** S_k(a) := Σ_{n≤e^{2a}} Λ(n)n^{−1/2}(2a−log n)^k. By PNT
(Mellin: ∫₀¹ v^{−1/2} log^k(1/v) dv = k!·2^{k+1}), S_k(a) ~ k!·2^{k+1}·e^a:

    S₁ ~ 4e^a,   S₂ ~ 16e^a,   S₃ ~ 96e^a.

Numerically (exact sieve sums to e^{12} = 162 756): S₁/e^a = 3.79, 3.91 and
S₃/e^a = 66.4, 78.8 at a = 5, 6 — slow log-corrected approach, as expected.

**Unconditional Chebyshev input.** ψ(x) > 0.84x for x ≥ 101 (Rosser–Schoenfeld
1962; verified directly here: min_{101≤x≤162756} ψ(x)/x = 0.9527, attained at
x = 222).

## 2. ATTACK 1 — rigorous post-entry linear growth: operator-norm lower bound

**Proposition 2.1 [PROVED].** ⟨1, P_a 1⟩ = S₃(a)/3 exactly.
*Proof.* ∬_{[−a,a]²}(|x−y|−c)₊ dxdy = 2∫_c^{2a}(2a−t)(t−c)dt = (2a−c)³/3 for
0 ≤ c ≤ 2a; sum over n with c = log n. ∎

**Proposition 2.2 [PROVED].** For every a with 2a ≥ log 101,

    S₃(a) ≥ 0.84 · J(2a − log 101) · e^a,   J(T) := ∫₀^T e^{−w/2}(w³/2 + 3w²) dw,

J increasing, J(∞) = 96. In particular S₃(a) ≥ 70.2·e^a for a ≥ 8 (J(11.38) = 83.6).
*Proof.* Stieltjes: S₃ = ∫₁^{e^{2a}} u^{−1/2}(2a−log u)³ dψ(u). Integrate by
parts; both boundary terms vanish (weight vanishes at u = e^{2a}, ψ(1) = 0);
−d/du[u^{−1/2}(2a−log u)³] = u^{−3/2}[½(2a−log u)³ + 3(2a−log u)²] ≥ 0. Insert
ψ(u) > 0.84u on [101, e^{2a}], drop [1,101) (integrand ≥ 0), substitute u = e^v,
then w = 2a−v. ∎

**Corollary 2.3 [PROVED].** For a ≥ 8, with 1 = the constant function, ‖1‖² = 2a:

    ‖P_a‖_op ≥ ⟨1,P_a 1⟩/‖1‖² = S₃(a)/(6a) ≥ 11.7 · e^a / a ,
    ‖P_a‖_HS ≥ ‖P_a‖_op ≥ 11.7 · e^a / a .

Conversely [DERIVED, RS upper bound ψ(x) < 1.04x]: k_P(t) ≤ 4.2e^{t/2} for t
large, hence ‖P_a‖_HS² = ∫(2a−|t|)k_P(t)²dt ≤ 70.6·a·e^{2a}, so

    11.7·e^a/a  ≤  ‖P_a‖_op ≤ ‖P_a‖_HS  ≤  8.4·√a·e^a        (a ≥ 8):

**the total prime content of G_a is ≍ e^a in both operator and HS norm.**
(Toy grid measurement, §7: ‖P_a‖_op/e^a = 1.07, 2.18, 3.02, 3.52 at a = 2..5,
climbing toward the asymptotic regime — the exponential rate is exact, rate
constant 1 in a, i.e. e^{a·1}: growth rate = 1 per unit a, prefactor ≍ poly(a).)

**What this forces [PROVED, consequences of Cor 2.3].** In ANY determinant-type
evolution over the screw family, the following objects diverge like e^a·poly(a)
unless cancelled against the pole sector (the "archimedean cancellation" of
THRESHOLD §3 is precisely pole-vs-prime; the genuine archimedean Γ-part
½|t|log|t| + A|t| is ‖·‖_op ≤ 2a·sup ≤ O(a² log a) and can cancel nothing
exponential):

1. the boundary data of the Hadamard flow: k_P(±2a) = S₁(a) ~ 4e^a;
2. the flow's prime drift: dS₁/da = 2Σ_{n≤e^{2a}}Λ(n)n^{−1/2} ≥ 3.3·e^a (a ≥ 8);
3. every quadratic-form ledger: ⟨1,P_a1⟩ ≥ 23.4·e^a;
4. the relative det₂ input: ‖P_a‖_HS ≥ 11.7e^a/a.

det₂'s removed linear term does none of this work: see §3.1.

## 3. ATTACK 2 — det₂ cancellation audit and the divergence theorem

### 3.1 What det₂ actually removes [PROVED]

log det₂(I+T) = Σ_{k≥2} (−1)^{k+1} Tr(T^k)/k; det₂(I+T) = det(I+T)e^{−Tr T} when
T is trace class. Two audits:

- **Bare entry:** Tr Δ_{n,η} = 0 (kernel vanishes on the diagonal — THRESHOLD §1).
  The det₂ subtraction is **vacuous** for bare threshold entries.
- **Dressed entry:** T = R_a(z)Δ_{n,η}. The removed term is Tr(R_aΔ_{n,η}) ≈
  4Λ(n)n^{−1/2}η²·G_a(z;a,−a) — **exactly the end-to-end Green term that
  THRESHOLD §2 identifies as the source of the conjectural n^{−s} Euler phase
  (agent T2's target).** So in a det₂ accumulation the candidate arithmetic
  enters only at order Λ(n)², while the divergence (which sits at k ≥ 2, §3.2)
  is untouched. det₂ removes the signal and keeps the noise.

### 3.2 Divergence theorem for the accumulated content [PROVED]

**Theorem 3.2.** Let z be real with z < min spec(G_a) and R = (G_a − z)^{−1} ≥ 0.
Set S := R^{1/2} P_a R^{1/2} (self-adjoint, ≥ similar to R P_a). Then

    ‖S‖_op ≥ ⟨1, P_a 1⟩ / ⟨1, (G_a − z) 1⟩ = (S₃(a)/3) / (∫(2a−|t|)g(t)dt − 2az),

and for every m ≥ 1:  Tr(S^{2m}) ≥ ‖S‖_op^{2m}  (S^{2m} ≥ 0 PSD).
*Proof.* Test vector φ = R^{−1/2}1: ⟨φ,Sφ⟩ = ⟨1,P_a1⟩, ‖φ‖² = ⟨1,(G_a−z)1⟩. ∎

**Size of the denominator (the g-dichotomy, §6):** |⟨1,G_a1⟩| ≤ 4a²·sup_{[0,2a]}|g|,
and sup|g| ≤ C·a log a + sup|E| with E the pole-vs-prime residue of §6. Hence:

- under RH-quality bounds (sup|E| ≤ Ca): for |z| ≤ poly(a),
  **‖S‖ ≥ c·e^a/a³ and Tr(S^{2m})/2m ≥ (c e^a/a³)^{2m}/2m → ∞ for every m**;
- unconditionally (zero-free region, sup|E| ≤ Ce^{a}e^{−c√{2a}}):
  ‖S‖ ≥ c·e^{c√{2a}}/poly(a) → ∞ still.

**Consequences [PROVED]:**
(i) the det₂ series for the accumulated prime content diverges — and since every
even-order trace individually blows up like ‖S‖^{2m}, **subtracting any finite
number of orders (det₃, det₄, …, det_p) fails identically**;
(ii) the poisoned z-region: for ANY z ∈ ℂ, ‖R(z)P_a‖ ≥ ‖P_a1‖/(‖G_a−z‖·‖1‖) ≥
(S₃/6a)/(‖G_a‖+|z|); under RH-quality bounds the sufficient-convergence condition
‖R(z)P_a‖ < 1 fails on the entire disc **|z| ≲ e^a/a³** — every fixed compact is
poisoned for large a. With λ_a → 0 (certified λ_{0.72} ≤ 3.2×10⁻⁸), spec(A-frame)
clusters at 0, so dist(z, spec) ≤ |z| + 3.2×10⁻⁸ there: convergence near z ≈ 0
would need dist ≳ e^a — impossible by ~e^a·10⁸ already in the certified window's
continuation;
(iii) the divergence is **normalization-independent**: CCM-b/Suzuki-1.6 allow only
exp(affine-in-a) normalizations of the determinant VALUE; series divergence is
unaffected. **Paradox worth recording: the truer RH is (the smaller g and λ_a),
the smaller the denominator ⟨1,(G_a−z)1⟩ and the FASTER the separated series
diverges (e^{2a}/poly vs e^{c√a}). The program's own success condition maximizes
the failure of its bookkeeping.**

### 3.3 The resolvent-amplitude condition for the entry-sliced sum [PROVED; honest negative]

For the entry-sliced accumulation (η_n = ½ log(n⁺/n), n⁺ = next prime power),
the second-order sum is Σ_n [√(8/3)Λ(n)n^{−1/2}η_n²·M_n]², M_n = the resolvent
amplitude at the n-th entry. Exact convergence condition: Σ Λ(n)²n^{−1}η_n⁴M_n² < ∞.
With Baker–Harman–Pintz gaps (p⁺−p ≪ p^{0.525}, hence η_n ≪ n^{−0.475},
unconditional; prime powers interlace primes, so their gaps are no larger):

    terms ≪ (log n)²·n^{−29/10}·M_n²   ⇒   converges for every M_n ≪ n^{19/20−ε}.

So: **the resolvent-blowup weapon does NOT kill the entry-sliced product at any
fixed z off the spectrum** — amplitudes up to n^{0.95} are tolerated, and at fixed
z with dist(z, spec) = d > 0 the amplitudes are bounded by 1/d. What the certified
collapse λ_{0.72} ≤ 3.2×10⁻⁸ does destroy is UNIFORMITY on compacts meeting the
limiting spectral bottom: uniform control within 3.2×10⁻⁸ of the ground state
already requires amplitudes ≥ 3×10⁷ at window a = 0.72 (vs the n^{0.95} budget
= 3.9 at n = e^{1.44}); as λ_a → 0 the naive dressed product loses local-uniform
convergence at exactly the points where the Ξ-zeros must appear. [The failure of
uniformity at det-zeros is in principle a removable phenomenon; OPEN-minor.] The
entry product's fatal defect is not blowup — it is emptiness (§4).

## 4. Kill A — the entry-ledger deficit theorem

**Theorem 4.1 [PROVED].** With entry slices η_n as above,

    C₀ := Σ_n √(8/3)·Λ(n)n^{−1/2}·η_n²  <  ∞    (BHP: terms ≪ log n · n^{−1.45}).

Numerically C₀ = 0.17057 (converged by n ≤ 1.6×10⁵; BHP tail negligible). Against
the total accumulated ledger Σ_n ‖Δ_{n,a−½log n}‖_HS = (√(8/3)/4)·S₂(a) ~ 6.53·e^a:

    (entry-slice HS mass)/(total prime HS mass) ≤ C₀·a/(11.7 e^a) = O(a e^{−a}).

Measured (toy, a = 2..6): ratio = 1.3e−2, 2.5e−3, 6.7e−4, 2.1e−4, 7.0e−5. ∎

**Theorem 4.2 [PROVED at the level stated].** In the interleaved evolution
(THRESHOLD §2: Hadamard flow between thresholds, det₂ entry factors at
thresholds), the entry factors satisfy Σ_n |log det₂(I + R Δ_{n,η_n})| ≤
C(K)·Σ_n ‖RΔ_{n,η_n}‖²_HS < ∞ uniformly in a, on any compact K with
dist(K, spec) ≥ δ > 0. Hence the entry product converges absolutely to a bounded,
eventually-nonvanishing factor, and **all unbounded arithmetic content of the
evolution — everything that could converge to a Ξ-object — resides in the
Hadamard flow factor**, whose prime drift is ≥ 3.3e^a per unit a (§2) and is
finite only in the pre-cancelled combination with the pole term.

**Corollary 4.3 [PROVED] — the Euler-factor correspondence fails by order
counting.** A local factor −log(1−n^{−s}) enters at first order in Λ(n)n^{−1/2}.
After det₂ (which removes the first-order trace, §3.1), the n-th entry factor
contributes O(Λ(n)²n^{−1}η_n⁴·M²) — second order in Λ, fourth order in the gap
η_n ≈ log n/(2n). Even keeping det₁ (granting trace-classness), the first-order
sum Σ_n 4Λ(n)n^{−1/2}η_n²·G_a(z;a,−a) is ABSOLUTELY convergent for all z on
compacts (it is ≤ (4/√(8/3))·C₀·sup|G_a|) — an absolutely convergent
"Euler product" is analytic and zero-free where defined and encodes no zeros of
ζ. The n-th det₂ factor does not, and cannot, relate to (1−n^{−s}): COLLISION §4.3's
open question is answered NO in the entry-sliced reading.

## 5. The exact missing renormalization: rank-3 pole compression

**Lemma 5.1 [PROVED, one line].** The pole kernel is exactly rank 3:

    −4(e^{(x−y)/2} + e^{−(x−y)/2} − 2) = −4 u₊(x)u₋(y) − 4 u₋(x)u₊(y) + 8·1(x)1(y),

u_±(x) = e^{±x/2}. Its three nonzero eigenvalues are ≈ {−4e^a, +4e^a, O(a)}; its
kernel sup is 8e^a-sized, but its RANGE is span{e^{x/2}, e^{−x/2}, 1}. The vectors
e^{±x/2} are the test-function shadows of the poles s = 1, s = 0 of ξ — the
s(s−1) factor; the constants direction is CCM's û(0) mode.

**Theorem 5.2 [PROVED].** Let Q = orthogonal projection onto
span{e^{x/2}, e^{−x/2}, 1}^⊥ in L²(−a,a). Then Q(pole)Q = 0 exactly, so

    Q P_a Q = Q G_a Q − Q (archimedean part) Q,
    ‖Q P_a Q‖ ≤ ‖G_a‖ + C a² log a ≤ C′a²log a + 2a·sup_{[0,2a]}|E|,

with E the §6 residue. Under RH-quality bounds this is poly(a); unconditionally
≤ e^{a}e^{−c√{2a}}·poly. **The entire e^a divergence of the prime content is a
rank-3 defect, living exactly in the pole sector.** Toy measurement (a = 5):
‖P_a‖ = 522.1 vs ‖QP_aQ‖ = 6.42 — a collapse by a factor 81, growing with a
(factor 29 at a = 2, 42 at a = 3, 58 at a = 4).

**Consequence — deliverable (ii), the missing renormalization [PROVED at the
level stated].** No trace-ideal subtraction repairs the accumulation (§3.2), but a
**rank-3 subtraction does**: formulate the evolution for the compression QG_aQ
(equivalently, a 3×3 Schur complement of the pole sector), and the prime input
becomes E-sized. This is not new machinery to the literature — it is the
completion of two shadows already present: CCM's restriction to L²₀ = {û(0) = 0}
removes the |1⟩ direction (1 of 3), and Suzuki §8's corrected kernel
g(t−u) − g(t) − g(−u) + g(0) is the screw-theoretic finite-rank correction. What
the accumulation program is missing is the e^{±x/2} pair — **the s(s−1) factor of
ξ implemented as a rank-2 compression**. Any repaired determinant evolution must
carry it; and after carrying it, §6 applies.

## 6. Kill B sharpened — the necessary condition and the exact rate dictionary

Define the pole-vs-prime residue (all classical; Suzuki (1.3) organizes g so that
this is the only unbounded ledger):

    E(t) := Σ_{n≤e^t} Λ(n)n^{−1/2}(t − log n)  −  (4e^{t/2} − 2t − 4).

**Proposition 6.1 [PROVED, classical explicit formula].** Inserting
ψ(u) = u − Σ_ρ u^ρ/ρ − log 2π − ½log(1−u^{−2}) and integrating
∫₀^t e^{(ρ−½)v}(t−v)dv = [e^{(ρ−½)t} −1 −(ρ−½)t]/(ρ−½)²:

    E(t) = − Σ_ρ [e^{(ρ−½)t} − 1 − (ρ−½)t]/(ρ−½)²  +  O(t),

the linear terms cancelling over conjugate pairs. Under RH: |E(t)| ≤ 2Σ_γ γ^{−2}
+ O(t) = **O(t)**. Unconditionally (classical zero-free region): E(t) ≪
e^{t/2}e^{−c√t}.

**Proposition 6.2 [PROVED].** The Laplace transform, for ℜs > Θ−½ (Θ := sup ℜρ):

    ∫₀^∞ E(t)e^{−st}dt = −(1/s²)·(ζ′/ζ)(s+½) − 4/(s−½) + 2/s² + 4/s,

in which the pole of −ζ′/ζ at s+½ = 1 exactly cancels −4/(s−½) [this identity IS
the program's pole-vs-prime cancellation, in transform coordinates]; the rightmost
singularities are at s = ρ−½, ℜs = Θ−½. Consequently, if some zero has ℜρ = θ > ½,
then E(t) = O(e^{(θ−½−δ)t}) is impossible for any δ > 0 (a Laplace integral of an
O(e^{βt}) function is analytic on ℜs > β, contradicting the singularity):

    E(t) = Ω(e^{(Θ−½−ε)t}) for every ε > 0;  E(t) = O(t) ⟺ under RH.

**The exponential rate of the residual ledger is exactly Θ − ½, two-sided.**

**Theorem 6.3 — sharpest necessary condition [PROVED at the level stated].** Let
D(a,z) be any determinant evolution over the screw family in which the prime and
pole contents are booked through structures that are separately finite (any
entry-indexed product, any Neumann-type dressing, any finite-order trace
subtraction). Then its ledger carries the two drifts ±(4+o(1))e^a of §2 and §5
separately and diverges at rate e^a/poly(a) (Cor 2.3 + Thm 3.2). If instead the
pole sector is removed by the rank-3 compression of §5 (the only repair, §3.2),
the surviving prime input has size sup_{t≤2a}|E(t)|, whose exact rate is
e^{(Θ−½)·2a}. Therefore, for the compressed evolution, with any normalization
e^{φ(a,z)}, φ affine in a (the CCM-b/Suzuki-1.6 class):

    (bookkeeping bounded by e^{o(a)} for all a)  ⟺  Θ = ½  ⟺  RH,

and an off-line zero at θ announces itself as oscillatory blowup at rate
e^{(2θ−1)a(1−ε)} — not absorbable by smooth affine normalization (the Ω-term
oscillates with frequency γ₀·2a). **There is no sub-RH regime in which the
accumulation converges and something weaker than RH is extracted; and there is no
super-RH obstruction either — the wall is exactly the wall.** This is the
threshold-program-specific instance of CCM Cor 3.8's no-softening phenomenon, now
with the rate dictionary attached.

*Toy verification of the dictionary:* injecting a fake zero ρ₀ = 0.75 + 14i as a
kernel perturbation ε(e^{(θ−½)|t|}cos(γ|t|)−1) produces measured log-slopes of
‖G_a^{bad}‖: 0.894, 0.642, **0.496** at a = 3, 4, 5 → predicted 2θ−1 = 0.5. ✓

## 7. ATTACK 3 — the toy model (mandatory), definition and results

**Definition.** Reduced screw kernel on L²(−a,a): k_full = k_pole + k_P with
k_pole(t) = −4(e^{|t|/2}+e^{−|t|/2}−2), k_P(t) = Σ_{n≤e^{|t|}}Λ(n)n^{−1/2}(|t|−log n),
true prime data (sieve to e^{12} = 162 756), archimedean ½|t|log|t| part omitted
(it is poly(a)-bounded and irrelevant to every e^a ledger; §2). Midpoint grid,
M = 1000, operator ≈ h·[k(x_i−x_j)] (Toeplitz); all determinant/norm statements
below are matrix-exact for the discretized operator.

**Results (measured):**

| a | ‖P_a‖ | ‖pole‖ | ‖full‖ | ‖QP_aQ‖ | entry/total HS |
|---|--------|--------|--------|---------|----------------|
| 2 | 7.88 | 14.79 | 7.19 | 0.274 | 1.3e−2 |
| 3 | 43.8 | 61.9 | 19.4 | 1.03 | 2.5e−3 |
| 4 | 164.7 | 199.1 | 38.4 | 2.82 | 6.7e−4 |
| 5 | 522.1 | 576.5 | 64.5 | 6.42 | 2.1e−4 |

Readings: (i) **cancellation**: the coupled ‖full‖ is polynomially small (fits
≈ 2.6a²) while both pieces are e^a-exponential — the PNT cancellation is real and
is destroyed by any separated bookkeeping; (ii) **rank-3 localization**: Q-collapse
by growing factors 29 → 81; (iii) **entry deficit**: ratio → 0 like e^{−a} with
C₀ = 0.1706; (iv) **divergence**: with z = −2‖full‖−1 (poly-sized), S =
R^{1/2}P_aR^{1/2} has ‖S‖ = 0.93, 2.06, 3.93, 7.32 at a = 2..5 — through the
convergence barrier ‖S‖ = 1 between a = 2 and 3, monotonically worsening, so every
det₂-series even term ‖S‖^{2m} diverges with a, exactly as Thm 3.2 predicts (the
measured slope is depressed below 1 by the poly(a) denominators; the analytic
bound governs the limit); (v) the exact-HS spot check and the bad-zero rate check
(§1, §6) both pass.

## 8. ATTACK 4 — order of limits: finite section vs threshold product

**Claim [DERIVED, Nyquist-type; not fully rigorous, stated as the precise
obstruction].** In an N-mode finite section on (−a,a) (mesh/bandwidth scale
2a/N), the entry Δ_{n,η} is distinguishable from a smooth flow correction only
if 2a/N ≲ 2η_n, i.e. N ≳ a/η_n ≈ 2a·n/log n. Over all thresholds n ≤ e^{2a} = λ²:

    N_min(a) ≈ 2a·e^{2a}/(2a) = e^{2a} = λ²  — **one section dimension per
    integer ≤ λ².**

Below N_min the late entries alias into the flow (their finite-section HS norm is
suppressed to ~ (Nη_n/a)·√(8/3)Λ(n)n^{−1/2}η_n²); the two iterated limits
(N → ∞ then product-over-n, vs product-over-n at fixed N) differ in their entry
ledgers by exactly the aliased mass. Consequences: (a) no threshold-product
statement is formulable at fixed CCM N — it requires diagonal sequences
N(λ) ≳ λ²; (b) on such diagonals, CCM's obstacle (a) [simple-even] is needed for
ALL (λ, N(λ)) with N(λ) ≥ λ² — a regime in which the repo's five certified
windows (λ ≤ e^{0.72}, small N) provide no evidence; (c) the CCM determinant
identity (Thm 1.1, fixed finite N) and the threshold-entry structure (N = ∞
objects with exact η² HS norms) never coexist at finite parameters: the program's
two ingredients live at incompatible ends of the (λ, N) square unless N ≥ λ² is
imposed from the start.

## 9. Deliverables, labeled

- **(i) Rigorous kill with equations:** Thm 3.2 + Cor 2.3 [PROVED]:
  ‖P_a‖ ≥ 11.7e^a/a (a ≥ 8, RS constant), Tr(S^{2m}) ≥ ‖S‖^{2m} → ∞ for every m,
  under every det_p; plus Thm 4.1/4.2 [PROVED]: entry ledger C₀ = 0.1706 < ∞
  carries O(ae^{−a}) of the prime mass — the accumulation program is dead in both
  readings (empty entries / divergent totals). Cor 4.3 [PROVED]: no Euler-factor
  correspondence for det₂ entry factors; det₂ removes the Euler-phase term itself.
- **(ii) Exact missing renormalization:** Thm 5.2 [PROVED]: rank-3 compression of
  span{e^{x/2}, e^{−x/2}, 1} (the s(s−1) poles + constants) — the completion of
  CCM's L²₀ and Suzuki §8's corrected kernel. No Schatten-class subtraction works.
- **(iii) Sharpest necessary condition:** Thm 6.3 [PROVED at stated level, via
  Props 6.1–6.2, classical]: after the rank-3 repair the surviving prime input is
  E(t) with exact two-sided rate e^{(Θ−½)t}, Θ = sup ℜρ; subexponential
  bookkeeping of the compressed evolution ⟺ RH. The route's floor is RH-strength
  exactly — not PNT-strength as THRESHOLD §3 conjectured; the program can neither
  shortcut the wall nor even approach it prime-by-prime.
- **OPEN-minor:** complex-z spectral radius of R(z)P_a off the real axis (norm
  bound proved everywhere, radius proved on real rays); removability of the
  uniformity loss at collapsing det-zeros (§3.3); rigorization of the Nyquist
  aliasing bound (§8).

**Status for FRONTIER.md:** node "infinite accumulation" → REFUTED as stated
(both readings); node "p^k resummation → local factor" → REFUTED for det₂ entry
factors (Cor 4.3); surviving successor node: "rank-3-compressed evolution"
(= pole-Schur-complement flow), whose convergence question is Thm 6.3:
RH-complete, with the rate dictionary e^{(2θ−1)a} attached. Agent T2's Green-phase
derivation is unaffected as analysis but its arithmetic payload (first-order
Euler phases) is exactly the det₂-removed term — T2 should target the FLOW's
boundary transport, not the entries.
