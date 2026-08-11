# S1 — the sector inequality: CCM obstacle (a) as a pole-vs-ferromagnet problem

*2026-08-11, S1 side-track (parallel prover). Target: for the localized Weil
form A_a on L²(−a,a) (screw frame; parity commutes since g is even), prove or
obstruct* ε_even(a) < ε_odd(a) *for all a > 0, plus simplicity in the even
sector — the analytic content of CCM's named obstacle (a). Sources:
COLLISION.md §2.1, EPSILON-N.md (P1–P4 and the five certified windows), Suzuki
arXiv:2606.09096 §§1–2 (screw expansion (2.2), Thm 1.4). No RH assumed.
Labels: PROVED / DERIVED / HEURISTIC / OPEN. Numerics: float Galerkin in the
repo's sine basis, anchored to the certified enclosures (details §4).*

---

## 0. Setting

Screw frame (Suzuki (1.3)–(1.6)): Q_a^W(v) = ⟨B_a v, v⟩, B_a = D*G_a D on
L²(−a,a); sine sections φ_k(u) = sin(w_k(u+a))/√a, w_k = kπ/2a; parity split
per EPSILON-N (P1)–(P4). ε_even, ε_odd := sector ground values; the CCM
hypothesis is ε_even < ε_odd + even-sector simplicity. Multiplier frame (CCM
(3.19)): archimedean symbol Ω(ξ) = Re ψ(¼+iξ/2) − log π; pole term
2ℜ(v̂(i/2) v̂(−i/2)); prime terms −(2Λ(n)/√n)·g_v(log n), g_v = autocorrelation.

## 1. Exact structural decomposition [PROVED, elementary]

**(F1) Lévy–Khintchine form of the archimedean symbol.** From
ψ(z) = −γ + Σ_{n≥0}(1/(n+1) − 1/(n+z)) and
1 − b²/(b²+ξ²/4) = ∫(1−cos ξt)·b e^{−2b|t|}dt (b = n+¼):

    Ω(ξ) − Ω(0) = ∫_ℝ (1 − cos ξt) ν(t) dt,
    ν(t) = Σ_{n≥0} e^{−2(n+¼)|t|} = e^{|t|/2} / (2 sinh|t|)  > 0,

with Ω(0) = ψ(¼) − log π. ν is strictly decreasing in |t|, ν(t) ~ 1/(2|t|) at
0 (log-multiplier), ~ e^{−|t|/2} at ∞. This is the classical explicit-formula
archimedean density read as a **Lévy jump density**; identity verified
numerically to 1e−10 at ξ = 0.5…40.

**(F2) The localized Weil form, exactly.** For real v ∈ C_c^∞(−a,a):

    Q_a^W(v) = Ω(0)‖v‖² + ½∬_{ℝ²} (v(x)−v(y))² ν(x−y) dxdy
               + 2⟨v,w₊⟩² − 2⟨v,w₋⟩²  −  Σ_{n<e^{2a}} (2Λ(n)/√n) g_v(log n),

where w±(x) = cosh(x/2), sinh(x/2) on (−a,a). The plane integral splits as
window jump form + killing potential V_a(x) = ∫_{|y|>a} ν(x−y)dy ≥ 0
(log-divergent at ±a; integrable — consistent with constants ∈ D(A_a)).
The pole operator has kernel 2cosh((x−y)/2) = 2w₊⊗w₊ − 2w₋⊗w₋ — **exactly**
the −4(e^{t/2}+e^{−t/2}−2) term of the screw function (1.3) under −g″; this
re-derives (P4): pole = +rank-one (even sector) ⊕ −rank-one (odd sector),
‖w₊‖² = a + sinh a, ‖w₋‖² = sinh a − a.

**(F3) Sign census.** In the Hamiltonian: jump part (kernel ν > 0) and killing
are Dirichlet-form ("ferromagnetic") terms; the prime terms are **negative
coefficients times translations** — also ferromagnetic (positivity-preserving
hops with positive amplitude); the **only positivity-breaking term is the
rank-two pole** (positive kernel entering with the repulsive sign).

## 2. Theorem A [PROVED]: the primes can never break simple+even

Let H_a^♮ := Friedrichs operator of Q^♮ := Q_a^W − pole term (archimedean +
all primes, no pole). Discrete spectrum (bounded rank-2 perturbation of A_a).

**(A1) Rearrangement.** For every v in the form domain, Q^♮(|v|) ≤ Q^♮(v) with
defect

    Q^♮(v) − Q^♮(|v|) ≥ 4 ν(2a) ‖v₊‖₁‖v₋‖₁ + Σ_n (2Λ(n)/√n)(g_{|v|}−g_v)(log n)
                       ≥ 4 ν(2a) ‖v₊‖₁‖v₋‖₁ ,   ν(2a) = e^a/(2 sinh 2a),

since (|v(x)|−|v(y)|)² ≤ (v(x)−v(y))² and g_{|v|} ≥ g_v pointwise (both prime
and jump terms improve under |·|; killing/scalar unchanged).

**(A2) Ground state of H_a^♮ is simple, one-signed, and EVEN, for every a>0.**
Equality in (A1) forces ‖v₊‖₁‖v₋‖₁ = 0, so every ground state is one-signed;
two orthogonal one-signed ground states have disjoint supports and their
difference is a sign-changing ground state with strictly positive defect —
contradiction; simple. Parity symmetry then gives Pu = ±u, and a one-signed
odd function is 0: even.

**(A3) Pole-free parity gap.** γ^♮(a) := λ^♮_{o,1} − λ^♮_{e,1} ≥
ν(2a)‖v_o‖₁² > 0 for every a > 0 (apply (A1) to an odd minimizer v_o,
‖v_o₊‖₁ = ‖v_o₋‖₁ = ½‖v_o‖₁).

**Consequence.** The prime terms — at *every* window length, all primes — are
structurally incapable of breaking ground-state simplicity or evenness of the
pole-free operator. **CCM obstacle (a) is exactly a competition between the
rank-two pole term and the pole-free parity gap γ^♮(a).** (Also: e^{−tH^♮} ≥
e^{−tH^arch} ≥ 0 entrywise by Trotter, so the semigroup is positivity
improving — the standard PF route agrees; (A1)–(A3) keep it elementary.)

## 3. Theorem B [PROVED]: rank-one reduction and the exact crossing condition

Sector operators: H_e = H^♮_e + 2w₊⊗w₊, H_o = H^♮_o − 2w₋⊗w₋. Let
G_e(z) = ⟨(H^♮_e − z)^{−1}w₊, w₊⟩, G_o(z) = ⟨(H^♮_o − z)^{−1}w₋, w₋⟩
(Aronszajn–Krein). Then:

- ε_even ∈ [λ^♮_{e,1}, λ^♮_{e,2}]: the root of G_e(ε) = −½ in the first gap
  (or λ^♮_{e,1} if ⟨φ^♮, w₊⟩ = 0). In particular **ε_even ≥ λ^♮_{e,1}**.
- ε_odd = min(λ^♮_{o,1}, root of G_o(ε) = ½ below λ^♮_{o,1}); G_o is strictly
  increasing on (−∞, λ^♮_{o,1}).

**(B0) Exact criterion.** ε_even < ε_odd ⟺ ε_even < λ^♮_{o,1} and
𝔠(a) := 2G_o(ε_even) < 1. **A parity crossing at a is exactly 𝔠(a) = 1**,
i.e. ∃ε with G_e(ε) = −½ and G_o(ε) = +½ simultaneously. 𝔠 is the
parity-defect functional of this problem; 1 − 𝔠(a) is the crossing margin.

- **(B1) sufficient:** λ^♮_{o,1}(a) − ε_even(a) > 2(sinh a − a)
  [since 𝔠 ≤ 2‖w₋‖²/(λ^♮_{o,1} − ε_even)].
- **(B2) sufficient, a ≤ ½log 2 (prime-free window), fully archimedean:**
  γ_arch(a) := μ_o^arch − μ_e^arch > 4 sinh a
  [ε_even ≤ μ_e^arch + 2‖w₊‖², ε_odd ≥ μ_o^arch − 2‖w₋‖²;
  2(a+sinh a) + 2(sinh a −a) = 4 sinh a].
- **(B3) even-sector simplicity, sufficient:** μ^arch/♮_{e,2} − μ^arch/♮_{e,1}
  > 2(a + sinh a) (the +rank-one lifts ε_{even,1} by ≤ 2‖w₊‖² and lowers no
  min-max value).

Variational form of the same mechanism (via (A1) at the odd minimizer v_o of
the FULL form): ε_odd − ε_even ≥ ν(2a)‖v_o‖₁² − 2⟨|v_o|,w₊⟩² − 2⟨v_o,w₋⟩², so
**any crossing requires the pole overlaps of the odd ground state to consume
the entire rearrangement defect** — a necessary condition falsifiable window
by window.

## 4. Quantitative ranges [HEURISTIC numerics, certified anchors]

Float Galerkin, repo sine basis, N = 24/sector-split, Simpson 96 pts/period,
tails ≤ 1e−10 (`scratchpad/sector_scan.py`; reproduces the certified [U]
window a = 0.45: ε_even = 1.9568e−5 ∈ [1.9536, 1.9600]e−5, gap 2.888e−3 =
certified 2.888e−3 ✓). Selected values:

| a | γ_arch | γ^♮ | λ^♮_{o,1} | ε_even | ε_odd | 2(sh a −a) | 𝔠(a) | 1−𝔠 |
|---|---|---|---|---|---|---|---|---|
| 0.10 | 1.255 | 1.255 | 1.343 | 4.7e−1 | 1.3e0 | 3.3e−4 | 0.0003 | ~1 |
| 0.30 | 1.347 | 1.347 | 0.243 | 8.6e−3 | 2.4e−1 | 9.0e−3 | 0.032 | 0.97 |
| 0.3465 | 1.367 | 1.367 | 0.0977 | 1.5e−3 | 8.6e−2 | 1.4e−2 | 0.12 | 0.88 |
| 0.42 | 1.398 | 1.634 | 0.0250 | 8.8e−5 | 8.9e−3 | 2.5e−2 | 0.65 | 0.35 |
| 0.45 | 1.410 | 1.768 | 0.0207 | 2.0e−5 | 2.9e−3 | 3.1e−2 | 0.862 | 1.4e−1 |
| 0.545 | 1.447 | 2.145 | 0.0178 | 8.8e−8 | 2.3e−5 | 5.5e−2 | 0.99897 | 1.0e−3 |
| 0.62 | 1.475 | 2.470 | 1.5e−3 | 5.2e−10 | 1.8e−7 | 8.1e−2 | 0.9999927 | 7.3e−6 |
| 0.70 | 1.503 | 2.822 | 8.5e−6 | ~5e−13 | ~4.5e−10 | 1.2e−1 | 1−1.7e−8 | 1.7e−8 |
| 0.80 | 1.536 | 3.267 | 2.2e−9 | float floor | float floor | 1.8e−1 | 1−3.6e−12 | — |

Findings:

1. **B2 holds for a ≤ ~0.325** (γ_arch > 4 sinh a fails first at ≈ 0.33);
   γ_arch(a) ≈ 1.20 + 0.53a near 0; model constant **γ* = γ_arch(0⁺) ≈ 1.20**.
   Suzuki cross-check: μ_e^arch − log(1/a) → m₁ ≈ −2.20 ⇒ μ₁ = m₁ + log 2π −
   ψ(2) + 1 ≈ 0.06 > 0, consistent with Thm 1.4.
2. **B1 holds for a ≤ 0.42 and fails at a ≥ 0.43** (𝔠̄ = 2‖w₋‖²/(λ^♮_{o,1} −
   ε_even): 0.95 at 0.42, 1.11 at 0.43). So the coarse-criterion theorem range
   is a₁ ≈ 0.42 — past the first prime (½log2 = 0.3466), short of the first
   certified window 0.45.
3. **B3 (even simplicity) holds for a ≤ ~0.46** (μ_{e,2}−μ_{e,1} ≈ 1.9 vs
   2(a+sinh a)); beyond, only the exact even-block gap certifies it (repo
   already does).
4. **Why B1 dies: λ^♮_{o,1} collapses to the zero floor** (2.1e−2 → 2.2e−9
   over a = 0.45 → 0.80) while the odd pole budget 2(sinh a −a) grows. Since
   the odd minimizer decouples from w₋ (β₁² = ⟨φ^♮_{o,1},w₋⟩²: 8.8e−3 at 0.45
   → 5e−17 at 0.80 — kink at a = ½log3 when prime 3 enters), λ^♮_{o,1} ≈
   inf_odd Q_W: **the pole-free odd minimum IS the odd-sector Weil infimum
   riding zero from above** — the quantity whose positivity for all a implies
   RH (Yoshida Prop. 1). No coarse bound survives contact with it.
5. **Margin law:** 1 − 𝔠(a) ≈ (37–48)·ε_odd(a) across a = 0.45…0.70 — the
   crossing margin is proportional to the odd Weil infimum itself. The sector
   inequality is safe exactly to the extent odd Weil positivity has slack:
   RH-marginal, admitting no ε-weakened version (cf. CCM Cor 3.8 caution).
6. **Trend against crossing:** ε_odd/ε_even is monotone INCREASING (2.9 at
   0.10 → 149 at 0.45 → 343 at 0.62 → 780 at 0.70): the even sector sinks
   faster; in ratio terms the parity gap widens while shrinking absolutely.

## 5. Deliverable statements

**THEOREM S1.A [PROVED].** For every a > 0 the pole-free localized Weil
operator H_a^♮ has a simple, one-signed, even ground state, and pole-free
parity gap γ^♮(a) ≥ ν(2a)‖v_o‖₁² > 0. The prime terms are ferromagnetic and
can never break simplicity/evenness by themselves; obstacle (a) reduces to
the explicit rank-two pole vs γ^♮(a).

**THEOREM S1.B [PROVED].** ε_even < ε_odd ⟺ ε_even < λ^♮_{o,1} and 𝔠(a) < 1,
with 𝔠 the explicit odd-resolvent functional of §3; sufficient criteria
B1/B2/B3 as stated. In the prime-free window: γ_arch(a) > 4 sinh a ⟹ sector
inequality (+ B3 ⟹ simplicity).

**THEOREM-WITH-RANGE [DERIVED, modulo one archimedean constant].** If
γ_arch(a) ≥ 1.2 on (0, 0.33] — a prime-free, pole-free special-function bound;
numerically γ_arch ∈ [1.21, 1.37] there, and Suzuki's Thm 1.4 machinery
(screw expansion (2.2) + Dirichlet-form theory, applied per sector) is
expected to yield γ_arch(a) = γ* + O(a), γ* ≈ 1.20 — then ε_even(a) < ε_odd(a)
and even-sector simplicity hold for all 0 < a ≤ 0.32. The certifiable-per-
window criteria B1/B3 extend the range to a ≤ 0.42 (Arb-certifiable with O(1)
margins — cheap compared to the repo's 3e−12-tail sign certificates; a
concrete follow-up task). OPEN: an analytic lower bound for γ_arch(a).

**CROSSING CHARACTERIZATION [PROVED] + prediction [HEURISTIC].** A parity
crossing at finite a is exactly 𝔠(a) = 1 (equivalently G_e(ε) = −½ and
G_o(ε) = +½ at a common ε; equivalently the odd ground state's pole overlaps
consume its rearrangement defect). At a crossing the ground space is
even ⊕ odd, CCM Thm 1.1's normalization δ_N(ξ) = 1 and the reality mechanism
for ξ̂ fail, and the surviving frame is Suzuki Thm 1.5 (hypothesis-free).
Data: 1 − 𝔠 ∝ ε_odd > 0 with ε_odd/ε_even growing — **no crossing below
a ≈ 0.70 (float floor), and the margin is predicted to stay a fixed multiple
(~40×) of the odd-sector Weil infimum**. Falsifiable window-by-window: 𝔠(a)
is a matrix-resolvent evaluation certifiable by the existing Arb pipeline.

**Where each assigned approach precisely stops.**
1. *Small-a extension:* the log(1/a) singular dominance cancels in the parity
   difference; what actually protects evenness is the O(1) model parity gap
   γ* vs the pole coupling 4 sinh a (and NOT smallness of primes — Thm A shows
   primes are never the obstruction). Stops at a ≈ 0.33 (B2), extendable to
   0.42 (B1).
2. *Perron–Frobenius/relative bound:* PF survives all primes forever (Thm A);
   the literal relative-bound version P(a) = 2Σ Λ(n)/√n dies instantly at
   a = ½log2 (P = 0.98 ≳ gap scale) because it is parity-blind; the
   parity-aware version is B1, dying at 0.43 for the structural reason in
   §4.4 (odd Weil infimum riding zero), not for lack of better constants.
3. *Crossing functional:* exact (𝔠), margins ∝ ε_odd — deciding it for all a
   is RH-adjacent in difficulty; per-window certification is routine.

## 6. Bookkeeping

- Numerics: `sector_scan.py` (session scratchpad; float, HEURISTIC — anchors
  reproduce EPSILON-N certified enclosures at a = 0.45 exactly, and the gap
  2.888e−3). Not committed; recipe fully specified in §4.
- Consistency with EPSILON-N (P4) verified: pole = 2cosh((x−y)/2) kernel;
  "evenness despite the structural handicap" now has a mechanism: the odd
  pole coupling is cubically small (sinh a − a) at small a, and the odd
  minimizer actively decouples from w₋ at larger a.
- Proposed next certificates (same Arb core): (i) B1/B3 enclosures on a grid
  a ≤ 0.42; (ii) 𝔠(a) < 1 with certified margin at a = 0.45, 0.50, 0.545
  (margins 1e−1…1e−3, far cheaper than the ε_N sign certificates); (iii) a
  certified lower bound for γ_arch on (0, 0.33] to upgrade THEOREM-WITH-RANGE
  to PROVED.
