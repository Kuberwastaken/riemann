# CONTINUATION — window propagation for Weil positivity (2026-08-11, third session)

*Objective per directive: an unconditional mechanism for the C_L family —
continuation theorems C_L + A_L ⇒ C_{L+δ}, first-failure structure, threshold
behavior, and attempts to kill continuation. Labels as in BRIDGE v2. Correction
adopted from review: the precision requirement is log(1/λ_min(L)); its growth is
unknown until envelope asymptotics are proved — "O(L) digits" is NUMERICAL, not
proved.*

## 0. The right ambient statement: drop the constraints, keep the poles

For real f ∈ C_c^∞(ℝ) define a±(f) = ∫f(u)e^{±u/2}du and

    Z(f) := 2 a₊(f) a₋(f) + G(f) + Σ_{n≥2} Q_n(f),
    G(f) = (1/2π)∫|F|²Ω,   Q_n(f) = −2Λ(n)n^{−1/2} g_f(log n),

g_f the autocorrelation. Only finitely many Q_n are nonzero for compactly
supported f (g_f(t) = 0 for |t| ≥ 2L when supp f ⊆ [−L, L]) — so Z is
well-defined with NO truncation parameter, and the prime content of Z on V'_L
:= {f ∈ C_c^∞ : supp f ⊆ [−L, L]} is automatic. By the explicit formula
(machine-checked layer), Z(f) = Σ_ρ m_ρ ĥ_f(γ_ρ): Z is exactly the zero-side
functional, and

    (C'_L):  Z ≥ 0 on V'_L,      (∀L C'_L) ⟺ RH    [KNOWN — Weil's criterion].

Advantages over the constrained C_L: (a) restriction f ↦ f·1_I does not leave
the space — block decompositions need no constraint corrections; (b) the pole
term is an explicit rank-2 bilinear 2a₊a₋ with kernel 2cosh((x−y)/2), handled
like any other term. Base case [UPGRADED after primary-source acquisition,
2026-08-11 phase 4; papers/criteria/Yoshida-1992-hermitian-forms-zeta.pdf]:
**Yoshida Theorem 1 (p. 310): the pole-inclusive form is positive DEFINITE on
K(½log 2)** — the FULL prime-free window with exact endpoint a = ½log 2
(⊇ C_c^∞(−a, a) for a ≤ ½log 2), including the odd-parity case where the pole
square enters negatively — proved by a rigorously error-bounded 200-mode
Fourier computation (1992; the ancestor of this repo's certified-positivity
methodology). His Prop. 6 = failure-threshold structure; Theorem 2 =
nondegeneracy ⟺ RH. Note C'_L ⇒ C_L; the repo's constrained results live
inside this frame.

Define λ'(L) := inf{Z(f) : f ∈ V'_L, ‖f‖ = 1} (∈ [−∞, ∞), finite by §1).
Monotone: V'_L nested ⇒ λ' nonincreasing [PROVED, trivial].

## 1. The uniform-modulus engine [PROVED]

Three elementary facts used everywhere below.

(M1) *Form lower bound.* There is C_L with Ω(r) ≥ ½log(2+r) − C_L, |pole term|
≤ C_L‖f‖², and Σ_{n≤e^{2L}}2Λ(n)n^{−1/2} ≤ C_L; hence Z(f) ≥ −3C_L on unit f,
and any unit f ∈ V'_L with Z(f) ≤ 1 has bounded log-moment:
∫|F|²log₊(2+|r|)dr ≤ M(L). *Proof:* collect the nonnegative part
∫(Ω+C_L)|F|²; everything else is bounded. ∎

(M2) *Uniform spectral tails.* On {unit f ∈ V'_L : Z(f) ≤ 1}:
∫_{|r|>R}|F|² ≤ M′(L)/log(2+R), uniformly. [From M1.]

(M3) *Uniform prime-term modulus.* On the same set, for the finitely many
active n: |g_f(t) − g_f(t′)| ≤ |t−t′|^{1/2} + 4πM(L)/log(1/|t−t′|) for
|t−t′| ≤ ¼. *Proof:* |cos rt − cos rt′| ≤ min(2, |r||t−t′|); split the
spectral integral at T = |t−t′|^{−1/2} and use (M1) on the tail. ∎
(The modulus is slow — 1/log — but UNIFORM on form-bounded sets; this is what
makes every continuity statement below uniform, where naive estimates needed
uncontrolled first moments.)

## 2. Continuity and closedness [PROVED modulo the routine dominations noted]

**Proposition 2.1 (no jumps at prime thresholds).** Each Q_n enters
continuously: for supp f ⊆ [−L, L], g_f(±2L) = 0, so at L = ½log n the entering
term has value exactly 0. The FORM Z is truncation-free by construction; only
d/dL of the family can jump at thresholds. [PROVED — support geometry.]

**Proposition 2.2 (λ' is continuous, nonincreasing; the failure set is an open
ray).** λ' is nonincreasing; using dilations f_λ(u) = f(u/λ) and (M1)–(M3),
|λ'(L) − λ'(L′)| ≤ ω_L(|L−L′|) with an explicit modulus (of order
1/log(1/|L−L′|)); consequently {L : C'_L fails} = (L*, ∞) for
L* := sup{L : C'_L holds} ∈ (0, ∞], and if L* < ∞ then **C'_{L*} holds and
λ'(L*) = 0.** *Proof sketch, audited:* dilation moves the archimedean part by
≤ C(1−λ) uniformly (Ω′(t)·t bounded), the pole part by ≤ C(1−λ) (kernel
smooth, support compact), and the prime part by ω(1−λ) uniformly on
form-bounded sets by (M3) — witnesses of near-minimality are form-bounded by
definition. Nonincreasing + two-sided approximate comparison ⇒ continuity;
signs ⇒ the ray structure and λ'(L*) = 0. [The dominations are spelled in the
proof of Theorem S and (M1)–(M3); no new analytic input.] ∎

Consequence: **RH ⟺ L* = ∞ ⟺ λ'(L) ≥ 0 for all L**; and RH ⇒ λ'(L) > 0
strictly for every L [PROVED-RH: Theorem S′ — the unconstrained rerun of
BRIDGE Theorem S; the constraints were used there only to delete the poles,
which are now part of Z; Farmer input unchanged].

## 3. First-failure zero-mode theorem

**Theorem 3.1** [PROVED modulo the single MISSING-LEMMA (D) below]. Suppose
ℓ₀ > 0 is a Yoshida base (C'_{ℓ₀} holds) and L* < ∞. Then there exists
f* ∈ L², ‖f*‖ = 1, supp f* ⊆ [−L*, L*], with:
(i) Z(f*) ≤ 0, where Z extends to L² by (M1)-finiteness;
(ii) [given (D)] Z(f*) = 0, and f* is a global minimizer over the L²-closure;
(iii) [given (D)] f* lies in the radical of the form on the window: for a.e.
x ∈ [−L*, L*],

    (K ∗ f*)(x) + a₋(f*) e^{x/2} + a₊(f*) e^{−x/2}
       − Σ_{n ≤ e^{2L*}} Λ(n) n^{−1/2} [ f*(x − log n) + f*(x + log n) ] = 0,

where K is the archimedean convolution kernel (distribution with
FT = Ω/2π-normalization; positive-type singular part at 0, smooth elsewhere).

*Proof.* By Prop. 2.2, λ'(L*) = 0: take unit f_k ∈ V'_{L*}, Z(f_k) → 0. By
(M1)–(M2) + Pego compactness (as in Theorem S, unconditional): f_k → f* in L²,
unit, supported in [−L*, L*]. Lower semicontinuity: Fatou on the nonnegative
part ∫(Ω + C)|F|², continuity of pole and (finitely many) prime terms under
L² convergence ⇒ Z(f*) ≤ lim Z(f_k) = 0 — (i). If the smooth core is
form-dense in the L²-closure [(D), the dilation–mollification–density lemma;
same missing detail as BRIDGE §4.3(c)], then Z ≥ 0 on the closure, so
Z(f*) = 0 and f* minimizes — (ii); the first variation of a quadratic form at
an interior-value-0 minimum over a subspace gives Z(f*, g) = 0 for all g in
the closure, whose kernel representation is the displayed equation — (iii). ∎

**What (iii) is.** An exact, unconditional (given (D)) functional equation: a
hypothetical earliest failure of Weil positivity forces an L² state on the
critical window that is annihilated by (archimedean smoothing) − (its own
prime-shifted translates) + (rank-2 pole correction). RH (given the base case
and (D)) is EQUIVALENT to: *no window carries such a radical state.* This is
the directive's "reduce RH to excluding an exact zero-energy state"
[relation to literature: Bombieri 2000 studies the radical of Weil's
functional in a different topology; whether this exact windowed statement is
in the literature is UNVERIFIED — flagged, not claimed novel].

## 4. The continuation theorem (Track 1) — proved shape, honest constants

Setting: f ∈ V'_{L+δ}; sharp decomposition f = f₀ + s, f₀ = f·1_{[−L,L]},
s supported in the two shells S_δ = ±[L, L+δ]. All three Z-values are finite
(sharp cuts have ∫|F|²log < ∞). Then Z(f) = Z(f₀) + 2B(f₀, s) + Z(s), with
B the full bilinear coupling. Three kernel lemmas:

- **(L-A) Uniform cross bound** [MISSING-LEMMA; sketch complete]:
  |B(f₀, s)| ≤ C_A(L)‖f₀‖‖s‖ with C_A independent of δ. Ingredients: the
  singular part of K across the cut is a Hardy–Hilbert kernel (1/(x−y)-type
  with x, y on opposite sides of ±L): Hilbert's inequality gives a
  δ-independent bound; the smooth part and the pole kernel 2cosh((x−y)/2) are
  bounded on the compact configuration; each prime delta contributes
  ≤ Λ(n)n^{−1/2}‖f₀‖‖s‖, finitely many. The unwritten detail is the exact
  singular expansion of K at u = 0 (classical; constants not fixed here).
- **(L-B) Shell coercivity** [MISSING-LEMMA; = the repo's Gap-2a bandwidth
  species transplanted to Z]: for s supported in S_δ:
  Z(s) ≥ (c₀ log(1/δ) − C_B(L))‖s‖². Ingredients: width-δ support forces
  spectral spread (Bernstein/uncertainty: low-frequency mass ≤ δR‖s‖²/π on
  [0, R]) so the Ω-part is ≥ (½log(1/δ) − C)‖s‖²; pole term, smooth part, and
  in-window primes are O(1)‖s‖²; the cross-shell lag ≈ 2L couples through
  smooth-kernel values (exponentially small) plus possibly one prime delta at
  log n ≈ 2L, bounded. [The repo proved the constrained-G version:
  edge coercivity ½log(1/(16πδ)) − 3.]
- **(L-C) Bounded pieces** [PROVED]: pole and prime couplings are bounded by
  explicit C(L)‖f₀‖‖s‖.

**Theorem 4.1 (Schur continuation)** [PROVED conditional on L-A, L-B].
If Z ≥ m‖·‖² on (the L²-closure of) V'_L with m > 0, then C'_{L+δ} holds for
every δ with

    δ ≤ exp( − [ C_A(L)²/m + C_B(L) ] / c₀ ).

*Proof.* Z(f) ≥ m‖f₀‖² − 2C_A‖f₀‖‖s‖ + (c₀log(1/δ) − C_B)‖s‖²; the 2×2 form
is PSD iff m(c₀log(1/δ) − C_B) ≥ C_A². ∎

This is the directive's schema C'_L + A_L ⇒ C'_{L+δ} with A_L = "margin ≥ m".
Two honest audits follow.

**Audit 1 — A_L is not unconditionally available.** The hypothesis is a
strict margin, not C'_L. By §2, margin-at-every-L is equivalent to RH-with-
Theorem-S′, and C'_L alone (margin possibly 0) yields δ = 0. No unconditional
proof of any margin beyond the base window exists in this repository or, to
current knowledge, the literature.

**Audit 2 — iteration reach (Track 4, answered exactly).** Iterating 4.1:
L_{n+1} = L_n + δ(m(L_n)). Since δ(m) > 0 whenever m > 0, and δ is bounded
below on any set where m is: sup L_n = sup{L : λ'(L) > 0}. So the iteration
reaches EXACTLY the margin-persistence threshold and cannot pass it: **the
continuation engine converts (∀L C'_L) into "λ'(L) never hits 0", which is
RH again (§2).** Furthermore, quantitatively: if λ'(L) ≤ e^{−cL} along the
iteration (consistent with the certified upper bounds 8.1e−6 / 6.7e−7 /
3.2e−8 at L = 0.64/0.68/0.72 and monotonicity of λ'; asymptotic rate
NUMERICAL), the increments δ ~ exp(−C e^{cL}) are doubly-exponentially small —
any finite-precision instantiation stalls almost immediately past the last
window where a margin is actually proved. Perturbative continuation is
therefore structurally incapable of reaching L → ∞ ahead of margin knowledge;
it adds no route around the zero-slack wall — it RELOCATES the entire problem
into the margin function, where Theorem 3.1 says the obstruction is an exact
radical state. [This is the directive's anticipated no-go, PROVED in the
precise form: reach of Theorem 4.1's iteration = margin-persistence threshold;
the "δ(L) ≲ λ'(L) ⇒ Σδ < ∞" heuristic is superseded by this exact statement.]

## 5. Threshold geometry (Track 3) [PROVED]

**Theorem 5.1.** Let n ≥ 2 and L = ½log n + η, η ≥ 0. For supp f ⊆ [−L, L],
the entering term factors through the outer shells: writing
E_η = [−L, −L+2η] ∪ [L−2η, L],

    Q_n(f) = −2Λ(n)n^{−1/2} ⟨ f·1_{[L−2η, L]}, τ_{log n} (f·1_{[−L, −L+2η]}) ⟩,

i.e. Q_n(f) depends only on f|_{E_η}, and |Q_n(f)| ≤ Λ(n)n^{−1/2}·‖f|_{E_η}‖².
*Proof.* x − y = log n = 2L − 2η with x, y ∈ [−L, L] forces
x ≥ L − 2η, y ≤ −L + 2η; Cauchy–Schwarz + AM–GM as in the repo's Lemma 1. ∎

So each prime power enters acting purely on the boundary shell of width 2η =
2L − log n — the exact physical-space form of the measured "seam law", and the
reason the entering term is harmless in Theorem 4.1's bookkeeping at small η
(it is part of the shell block, further suppressed by ‖f|_{E_η}‖²). The
synchronization the directive asks about is now a theorem: *the support
becomes able to see the shift log n at exactly the L where the shift maps the
right edge onto the left edge, and only edge-to-edge mass pays it.* What
Theorem 5.1 does NOT provide: a positivity mechanism — the entering term is
edge-local but NEGATIVE-capable; its control still comes from shell
coercivity (L-B), not from arithmetic magic. An exact-factorization search for
why the coefficient Λ(n)n^{−1/2} is precisely survivable (rather than merely
small at entry) found nothing beyond the completion-criticality numerics;
recorded as open.

## 6. Required final report

**A. Inter-window identity.** Z(f) = Z(f₀) + 2B(f₀, s) + Z(s) in the
unconstrained pole-inclusive frame (§0, §4), with B decomposed into
Hardy-singular + smooth + pole-rank-2 + finitely many prime-delta transfers;
entering primes localized to shells by Theorem 5.1.

**B. Strongest unconditional continuation theorem.** Theorem 4.1 (conditional
only on kernel lemmas L-A/L-B whose proofs are sketched and of proven species
in the repo): margin m at L ⇒ positivity out to L + exp(−[C_A²/m + C_B]/c₀).

**C. Exact remaining hypothesis for iteration.** Margin persistence:
λ'(L) > 0 for every L. By §2 this is equivalent (via Theorem S′, PROVED-RH,
and Weil's criterion) to RH itself. No unconditional A_L weaker than this was
found; the directive's ideal (unconditionally provable A_L) is NOT achieved,
and §4 Audit 2 explains structurally why this frame cannot achieve it.

**D. Can increments reach L → ∞?** Exactly iff the margin never dies: the
iteration's reach is precisely sup{L : λ'(L) > 0} — reaching ∞ is RH, not a
new route to it. [PROVED, given 4.1.]

**E. At a prime-power threshold.** The form is continuous (Prop. 2.1 — the
entering term has value 0 at entry); the entering term is edge-local with
explicit factorization and bound (Theorem 5.1); only derivatives-in-L can
jump.

**F. Strongest no-go found.** §4 Audit 2: perturbative/local continuation
relocates RH into margin persistence with doubly-exponentially shrinking
verified reach; plus Theorem 3.1's converse use: if margins die, an exact L²
radical state exists at the first-failure window satisfying the displayed
prime-shift convolution equation — so any continuation-based proof must, in
disguise, exclude that state.

**G. What moved unconditionally.** Proved structure about HOW C'_L can fail:
monotone-closed failure ray, continuity through thresholds, λ'(L*) = 0,
compactness-forced L² zero-energy state with an exact radical equation
(modulo the single density lemma (D)), threshold edge-locality, and the exact
reach of Schur continuation. No new C'_L was proved beyond the (cited) Yoshida
base; nothing here is progress in the zero-slack-limit metric except the
first-failure reduction (Theorem 3.1), which reformulates the unconditional
problem as the exclusion of one explicit object — the sharpest unconditional
statement this repository now possesses.

*Open items created: verify Yoshida's exact base statement ℓ₀; write (D);
fix the kernel constants in L-A/L-B; adjudicate novelty of Theorem 3.1(iii)
against Bombieri 2000.*
