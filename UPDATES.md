# UPDATES — dated adjudications after the 2026-07-23 release

*The release documents (`BREAKDOWN.md`, `ATTACK.md`, `GAPS.md`, `LEADS.md`,
`FINDINGS.md`, `FOR-SOLVERS.md`) are frozen as written on 2026-07-23. This file
records what has changed since, and how it modifies the archive's verdicts. Append-only.*

---

## 2026-08-11 — The Claude 2/3 theorem: Lead 6 executed, by a different engine

### The event

On 2026-08-10 Anthropic published **"More than two thirds of the zeros of the Riemann
zeta function lie on the critical line" (Claude; Anthropic, San Francisco, 2026)** —
local files `papers/recent/Claude-Anthropic-2026-*.pdf` (paper, informal note,
explanation appendix, process transcripts). Unconditionally:

- **Theorem A:** lim inf N₀\*(T,2T)/N(T,2T) ≥ 2/3 (distinct on-line zeros; record was
  5/12 = 41.66% by Levinson-method refinement, PRZZ 2020, static since 2020).
- **Theorem B:** ≥ 2/3 simple *and* on the line (record for "simple" was ~40.7%).
- **Theorem C:** ≥ 5/6 of zeros distinct (record 0.6603, Wu 2015).
- **Theorem D:** optimised window (recovering the Montgomery–Taylor kernel exactly):
  0.6725, 0.6725, 0.83625.
- **Theorem E:** all of the above for every fixed primitive Dirichlet L-function.
- Bonus (§7.3): ≥ 85.838% of zeros of ξ′ simple-and-on-line unconditionally (86.864%
  with a quartic window) — Farmer–Gonek–Lee's RH-conditional constant with RH removed.
- A **sorry-free, axiom-audited Lean 4 formalization of Theorems A–E**
  (github.com/anthropics/zeta-23-lean, tag v1.0, Mathlib 51e6992; only propext /
  Classical.choice / Quot.sound; von Neumann's trace inequality and both directions of
  Sylvester inertia are new Mathlib-level contributions). Authored by an unreleased
  Claude research build in interactive sessions (~60 subagents, adversarial review
  with Davenport–Heilbronn/Epstein controls); human interlocutor Jarred Sumner;
  studied and communicated by Ralph Furman and Levent Alpöge; read by Brian Conrey
  and Dan Goldston; formalization orchestrated by Eric Easley. Companion human paper:
  Goldston–Suriajaya, "Zeta zeros on the critical line," arXiv:2511.20059 (already in
  `papers/analytic-progress/` as GS 2025; their question "what if RH could be removed
  from Montgomery's proof" is exactly what the paper answers).

### The method, compressed (full anatomy in the paper; read §§2–6 — it is short)

Weil's Hermitian form W(f,g) = Σ_ρ m_ρ ĥ_f(γ_ρ) conj(ĥ_g(γ_ρ)) is compressed to the
d×d Gram matrix G̃ of a **Gabor family at critical density**: f_k(u) = φ(u)e^{−iτ_k u},
τ_k equispaced through [T,2T] at spacing 2π/L, φ a tapered window with supp φ =
[−L/2, L/2], L = λ·log(T/2π), λ ≤ 1. Then:

- **(Z) Zero side — pure linear algebra.** Each distinct on-line zero contributes a
  rank-one PSD form; each off-line pair {ρ, 1−ρ̄} contributes a 2×2 block of signature
  (1,1) (functional-equation symmetry). Sylvester inertia under pull-back (no
  independence of the evaluation functionals needed!) + a **rank–trace inequality**
  (‖P+Q‖²_F ≥ c·tr P − c²r/4 + 2c·tr Q − c²b, proved via von Neumann's trace
  inequality — the matrix transplant of Montgomery's integrality step m² ≥ 2m−1,
  and at the regrouped level m² ≥ 3m−2) turn "trace big, Frobenius norm small" into
  "many on-line simple zeros".
- **(P) Prime side — unconditional.** tr G̃ and tr G̃² are Montgomery's first and
  second pair-correlation moments; for bandwidth λ ≤ 1 they evaluate unconditionally
  to N and (1/λ + λ/3)N by Chebyshev–Mertens + the Montgomery–Vaughan generalised
  Hilbert inequality (the BGSTB 2024 de-conditionalization, transcribed to the Gabor
  kernel). No mollifier, no zero-density estimate, no zero-free region.
- Budget at λ=1: 4·(tr = N) − 2·(N) − (‖·‖²_F = 4/3·N) = 2/3·N.

The RH-classical step — "read the zero side as a positive sum over real ordinates" —
is replaced entirely by inertia bookkeeping that is *valid wherever the zeros are*.

### What it changes in this archive

1. **ATTACK.md §8 (T5) / LEADS.md Lead 6 — executed, and the archive's framing was
   right but the engine prediction was wrong in an instructive way.** The archive
   called "de-conditionalized pair correlation" the sharpest classical lead but
   proposed composing it with **Guth–Maynard large-value technology** to control
   Montgomery's F(α,T) past α = 1. The actual solution needed **no new analytic
   input at all**: bandwidth-≤1 pair correlation (already unconditional, BGSTB24)
   plus finite-dimensional linear algebra. The "vertical-to-horizontal bridge" the
   archive asked for (GS's narrow-box hypothesis) was not de-conditionalized — it was
   **bypassed**: inertia does not care where the off-line zeros sit. Lesson for every
   other lead in this repo: before asking for stronger analytic inputs, ask whether a
   finite compression + exact linear algebra already extracts the theorem from the
   inputs we have. (This is also exactly this laboratory's native move — finite
   sections of the same Weil form — executed at T→∞ instead of at the bottom of the
   spectrum.)

2. **BREAKDOWN.md's "41.7%, static since 2020, every result uses Levinson's method" is
   obsolete.** The proportion statistic moved 41.7% → 67.25% in one step, by a
   non-Levinson engine, with a Lean certificate. The claim "mollifier ceiling < 50%
   caps the on-line proportion" survives *for the Levinson route only*; the record
   itself is no longer Levinson-bound.

3. **New no-go rows for the map (ATTACK.md §2), from the paper's own §7.5:**
   - *Bandwidth-one ceiling:* no certificate reading only mean density + bandwidth-≤1
     pair correlation + integrality, holding configuration-by-configuration, can
     certify simple-on-line proportion > **0.68185**. (2/3 is within 0.016 of this.)
     Pushing to 0.70 / 0.80 / 0.90 needs pair-correlation support ≈ 1.04 / 1.26 / 1.70
     — i.e. genuinely new arithmetic (Hardy–Littlewood-strength prime-pair input).
     **Lead 6 therefore mutates, it does not close:** the GM × pair-correlation
     composition the archive proposed is now precisely the question "can large-value
     technology give unconditional F(α) on any interval beyond α = 1, at any
     positive density" — and each ε of support is worth a computable increment of
     proportion through the same inertia certificate.
   - *λ ≤ 1/2 is vacuous* (Prop. 7.4: the certificate is capped by the dimension
     d = λN of the compression), and unconditionally *higher moments add nothing* on
     λ ∈ (1/2, 1) (Rudnick–Sarnak range kλ < 2 permits k ≤ 3 only, and odd moments
     don't move the Christoffel bound). The two-trace certificate is the sharp one.
   - *Degree-one only* (§7.2(ii)): for an individual GL(2) L-function the same
     machinery certifies nothing (Λ* = 1/2 forces c ≤ 1/2). The method is a
     degree-one phenomenon, like every unconditional proportion result.
   - *Insensitivity, restated:* the inputs are insensitive to o(N) off-line zeros and
     are satisfied by Davenport–Heilbronn/Epstein objects (which *under*-certify —
     their coefficients break the mean-value step). "Nothing in the method
     distinguishes two thirds from all." The archive's "counts, never excludes" row
     is confirmed by the strongest counting result in history.

4. **Calibration of this archive's honesty:** the archive's 2026-07-23 frontier note
   said the proportion records were "being attacked by de-conditionalizing pair
   correlation (Goldston–Suriajaya)" and listed it as watch-item #1. The attack
   landed 18 days later, from the AI side, with the GS papers as the load-bearing
   analytic input. The archive missed nothing structural; it (like everyone) missed
   that the missing step was elementary.

### What transfers to this laboratory (Track D verdict, first pass)

The 2/3 paper and this repo's `experiments/weil_positivity/` study **the same
Hermitian form in complementary regimes**: they compress W onto high-frequency Gabor
families at T→∞ with growing support L = λ log T and extract *proportions* from two
moments; we compress W onto fixed small windows [−L, L], L ≈ 0.35–0.7, and try to
certify *strict positivity* (T1), which is of RH-equivalent species. Consequences:

- **Their machinery cannot prove T1** (their own §1.5/§7.5: insensitive to o(N)
  off-line zeros; certificates never exceed what two moments see). This was expected
  and is now sharp.
- **Bombieri's inertia observation** (negative index of truncations counts off-line
  pairs — [Bom00], which they cite as their zero-side ancestor and which is already
  this repo's Weil-form foundation) now has a *positive-index dual with a track
  record*. Our finite-section certificates are inertia statements at the bottom of
  the spectrum; theirs at the bulk. Same form, same bookkeeping, two altitudes.
- **The genuinely transferable tool is §7.5(d): the Chebyshev–Markov–Stieltjes /
  Christoffel-function formalism** — the *sharp* theory of what k spectral moments
  of a Hermitian compression can certify. Our moment ladder for the T1 norm route
  (Tr B, Tr B² — `secmom`, saturated at 77% of the requirement, declared NEGATIVE in
  FINDINGS Tier 5) was a hand-built two-vector ladder, not the CMS-sharp bound. The
  right question, now precisely posed: **compute certified Tr((B|_V)^k) for k up to
  6–8 on the constrained window space and apply the sharp CMS/Christoffel lower
  bound** — does the sharp use of k moments clear the (log 2)/√2 prime bar on
  (½log 2, 0.39], where the true archimedean floor (~0.55 measured) comfortably
  clears it? If the sharp ladder crosses the bar at feasible k, **small-δ T1 becomes
  a finite certified computation**. If it provably cannot, the moment route has a
  real theorem-shaped no-go. Queued as the session's Track D experiment.

### Also ingested 2026-08-11

- **wessorh/hprime "strong resolvent proof"** (`papers/surveys-expository/Wesson-2026-hprime-strong-resolvent.{pdf,tex}`):
  adjudicated as a failed-proof record — see the addendum in
  `notes/surveys-expository.md`. Circular by construction (the operator's diagonal
  *is* the list of zeta ordinates); the repo's own README (Aug 2026) already retracts
  all three of its approaches, which is to its credit. Its instructive value: it is a
  textbook instance of two rows of the no-go map (eigenvalue-matching without a
  canonical attachment mechanism; mean-density-only validation), *and* its final
  sentence correctly identifies its own gap ("proving μ_∞ = μ_ζ"), which **is** the
  Hilbert–Pólya problem.
- **muchmirul.github.io/conjectures/zeta-critical-line**: third-party exposition of
  the Claude 2/3 paper (the "microphones / see-saw / bowls-and-saddles" language).
  Accurate as far as checked; no independent mathematical content; not archived as a
  paper.

---

## 2026-08-11 — Session products (same day, the "real stab" session)

Executed on ai-vps (8 vCPU x86; the lab's move off the Raspberry Pi). Full
narrative in `logs/LOG.md`; one commit per artifact throughout.

1. **Lead 2 EXECUTED (Track A):** all three hypotheses of CCM 2025 Theorem 1.1
   (sign, simplicity, evenness of ε_N) machine-certified in five windows
   (L = 0.45…0.62), both section conventions, with a full-space corollary
   carrying no N→∞ caveat (μ_λ ≤ 6.2646·10⁻¹⁰ for all λ ≥ 1.8589). Corrected
   parity structure of the pole constraints (one per sector; pole term
   negative-definite in the odd sector). `experiments/weil_positivity/EPSILON-N.md`.
2. **Lead 5 REFUTED with structure found (Track B):** k ≥ 2 prime-power orbits
   are load-bearing, not drag — primes-only positivity dies at L* = 0.705 ±
   0.005 (≈ the n=4 threshold + 0.012) while the full sum rides the zero shelf;
   seam law (every truncation fails within ΔL ≈ 0.01 of its first missing
   orbit's threshold); 4-orbit/2-orbit resonance (dropping n=4 costs Λ(2)/√2,
   not Λ(4)/2). The ψ−θ reformulation is dead. `experiments/weil_positivity/ORBIT-DRAG.md`.
3. **Lead 1 OPENED (Track C):** graded-mode scaffold with Lemma H proven
   (high-mode band mass ≤ (8/π²)log((N−1)/(N−1−2LR/π))) and the single
   remaining analytic lemma (shell-coupling decay) isolated; full-space T1
   conditionally reduced to that lemma + one certified low-block computation.
   `experiments/weil_positivity/T1-GRADED.md`.
4. **Track D — the session's centerpiece** (`experiments/weil_positivity/SHARP-FLOOR.md`):
   - The rearrangement route to T1 is conclusively closed: even with EXACT
     per-band spectral caps its ceiling is 0.4753 < 0.4901 at L₀ (the loss is
     Lemma R itself, not the moment order — k=6 moments reach within 1.8% of
     the exact caps).
   - **The Ω_W identity**: the full one-prime (indeed any-window) constrained
     Weil form is a single diagonal frequency functional, Ω_W = Ω −
     √2 log2·cos(r log 2) — the prime is a cosine multiplier, and the monotone-
     rearrangement detour (hence the 0.4901 norm bar) was never necessary.
   - **The σ-LP certificate format**: caps ∫σ dν ≤ λ_max(P_V σ(D) P_V) for a
     dictionary of (signed) multipliers, with self-aimed union caps and signed
     band-vs-tail tradeoff caps encoding the uncertainty principle as LP rows.
   - **Pilot result: the LP crosses zero at L = 0.40 (+0.0046)** — pilot-level
     FULL-SPACE Weil positivity with the prime 2 active at window ratio 2.226,
     where all prior rigorous statements (this repo's certified curve) covered
     14-dimensional families. Certification design (frequency-side Nyström +
     interval LP columns) is written and is standard technology; the margin is
     the open risk. If it survives, this is the first full-space theorem of the
     exact RH-equivalent species with arithmetic content — T1(δ) for δ ≈ 0.23.
5. Norm-route σ-LP at L₀ reached 0.4886 (0.0015 below the bar) — recorded as
   the sharpest measured value of that now-superseded route.

*Everything above is labeled honest-first: pilot numerics are pilot numerics,
certified results say certified, and none of it is RH.*

---

## 2026-08-11 — Session phase 2: the Lean layer opens (same day)

Directive: "explore an RH Lean formal proof." Honest resolution, recorded before
any work: **no proof of RH exists to formalize**; the executable program is the
Anthropic playbook — formalize the strongest true statements available, and
build the formal *reduction* so future increments accumulate toward RH's
formal statement. Products (see `formal/README.md`, `logs/LOG.md`):

- **Infrastructure**: anthropics/zeta-23-lean surveyed — its hypothesis-free
  literature-form Weil explicit formula (`EF_lit_zetaZeroConfig`) is exactly the
  criterion layer's hard core, formalized, Apache-2.0, one day old. Our
  `RiemannFormal` package pins its toolchain/Mathlib and builds against the
  shared cache.
- **The criterion stated formally** (`Criterion.lean`, dev): `WeilPositivityAll`,
  `weil_positivity_of_RH` (RH ⇒ arithmetic side PSD; full proof route via
  EF_lit documented in-file), and `WeilCriterion` as the machine-readable
  reduction target. Compiles once the Zeta23 library is built (in progress).
- **Three theorems proven sorry-free** (axiom-audited): Lemma 1 (the sharp
  half-factor prime bound — the laboratory's first machine-verified result),
  the σ-LP dual assembly, and `T1_of_certificate` — the conditional form of
  full-space one-prime Weil positivity, the formal skeleton of the same-day
  pilot result at L = 0.40 (+0.0349).
- The gap between the pilot and an unconditional Lean theorem is now exactly
  two named objects: the Parseval convention bridge, and Lean-certified
  spectral caps. Both are bounded projects, not open mathematics.
