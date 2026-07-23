# Riemann — approaches to the Riemann Hypothesis

A research archive of every major serious approach to the Riemann Hypothesis: the primary
papers, expository material, and blog/media coverage, organized by approach family, with
notes on each item and a synthesis of which routes could actually work.

## Layout

```
papers/
  spectral/             Hilbert–Pólya, Berry–Keating, Connes spectral realization,
                        random matrix theory, physics models
  analytic-progress/    unconditional partial results: zeros on the line, zero-density
                        (Guth–Maynard), zero-free regions, de Bruijn–Newman, Lindelöf,
                        computational verification
  algebraic-geometric/  function fields (Weil, Deligne), F1 geometry, Connes–Consani
                        arithmetic/scaling site, Deninger's program
  criteria/             equivalent reformulations: Weil positivity, Li, Nyman–Beurling,
                        Robin/Lagarias, Riesz, de Branges saga
  surveys-expository/   authoritative surveys (Bombieri, Sarnak, Conrey), Riemann's 1859
                        paper, famous failed proofs (Atiyah, de Branges), blog coverage
  recent/               2019–2026 developments: Guth–Maynard follow-ups, Connes–Consani
                        zeta cycles, Jensen polynomials, formalization, new claims
notes/                  per-category annotated bibliographies (one entry per item:
                        citation, links, summary, status, assessment)
BREAKDOWN.md            the synthesis: taxonomy of approaches, what each has actually
                        achieved, where each stalls, and which could plausibly work
```

## Status — live

_Last updated: 2026-07-23 16:23 UTC. This section is refreshed regularly; the commit
history and `logs/LOG.md` carry the fine-grained record._

- **NEW — [`LEADS.md`](LEADS.md)**: seven vetted post-no-go leads, headed by the
  graded-mode architecture for full-space T1 (the first route surviving every
  refutation) and the certified razor corridor (Weil-form infimum at the L=0.7
  window certified ≤ 1.19e-7 vs RH's ≥ 0).
- **THEOREM A (proven + certified)**: the archimedean Weil form on the
  prime-free window is *coercive* with certified constant **c₀ ≥ 0.349152** —
  the quantitative floor missing from the literature (CC 2020 prove only ≥ 0),
  via an elementary trace-identity + rearrangement proof
  ([`PROOF-c0.md`](experiments/weil_positivity/PROOF-c0.md)). Gap 1 of GAPS.md: closed.
- **[`GAPS.md`](GAPS.md)**: six sharp openings found by cross-reading the archive's
  proofs against this session's measurements — incl. the unstated coercivity theorem
  hiding in Connes–Consani 2020, a three-lemma route to a fully proven T1(δ₀), the
  unchecked Carathéodory–Fejér dictionary with CCM 2025, and a candidate new law:
  criticality approached at rate e^(−4γ₁L) (first zeta zero as rate constant; test running).
- **NEW — Certified Result 5, the rescue phenomenon machine-verified**
  (`experiments/weil_positivity/rescue_certify.py`): on one explicit 22-dim family
  at L=0.62, a certified negative archimedean direction (vᵀGv = −0.02776 ± 6e-9)
  AND certified total-form coercivity (W ≥ 2.06e-5·‖f‖², primes {2,3}) — rigorous
  proof that on this family, Weil positivity is *created by the prime terms*.
  Consolidated writeup: [`experiments/weil_positivity/NOTE.md`](experiments/weil_positivity/NOTE.md).

- **NEW — Certified Result 1**: rigorous (Arb ball-arithmetic, verified integration +
  certified Cholesky) — **W(f) ≥ 0.0726‖f‖² on an explicit 14-dim family at L=0.45**,
  prime-2 term active, beyond the CC ratio-2 window, in the regime where
  norm-perturbation provably fails. First rigorous Weil-positivity statement with an
  active prime beyond ratio 2 (finite family; full-space version = open target T1).
  `experiments/weil_positivity/certify.py L` reproduces each point in ~1 min. Now a
  **certified curve**: c = 0.0726 (L=0.45) · 0.0148 (0.50) · 0.00129 (0.545) ·
  **0.000076 at L=0.60 with primes {2,3}** — the first rigorous multi-prime
  Weil-positivity statement, certified into the criticality zone.
- **T1 architecture increment** (`experiments/weil_positivity/T1-ARCHITECTURE.md`):
  **Lemma 1 proven** (sharp ½-factor bound on the prime-2 term, ‖Q₂‖ ≤ (log 2)/√2 —
  explains the measured saturation exactly); spatial block criterion honestly refuted;
  T1 reduced to a single sharp invariant μ(L) = λ_min(G^{−1/2}Q₂G^{−1/2}) > −1
  (measured headroom 0.69 → 0.008 across the one-prime window); and a new observed
  phenomenon: **just-in-time rescue** — G+Q₂ goes indefinite at L=0.58 but the p=3
  term restores positivity (Euler-product collectivity load-bearing from the second
  prime).

- **NEW — first experiment executed:** `experiments/weil_positivity/` — the Weil
  quadratic form built numerically in the critical support window (engine validated
  against the explicit-formula identity via Odlyzko's 100k zeros), mapping the four
  regimes of positivity: prime-free → perturbative (T1 provable-looking for small δ)
  → cancellative (the true T1 lemma identified) → arithmetic-rescue criticality
  (total pinned at 0 to 10⁻⁶ while margin −1.35 / prime norm 3.5; minimizers develop
  Fourier nodes at the actual zeta zeros). See
  [`experiments/weil_positivity/RESULTS.md`](experiments/weil_positivity/RESULTS.md)
  and `ATTACK.md` §12.

- **Phase:** **complete** — collection (6/6 agents), synthesis, and deep-dive done.
  **→ Read [`BREAKDOWN.md`](BREAKDOWN.md)** for the survey: the three walls,
  family-by-family verdicts, what a successful proof must look like, and the watch list.
  **→ Read [`ATTACK.md`](ATTACK.md)** for the deep dive: RH as a boundary-feasible
  convex program, the no-go map, the two engines that ever killed an RH, and a concrete
  research portfolio (the one-prime Weil-positivity target T1, SDP certificates,
  spectral-triple windows, finite-level tropical Hodge index, GM × pair-correlation).
- **Archive:** **178 verified PDFs (161 MB)** + **6 annotated bibliographies
  (~2000 lines)**, every artifact its own commit:
  - `spectral/` 34 — Hilbert–Pólya end-to-end: Montgomery/Odlyzko GUE, Berry–Keating,
    BBM 2017 controversy, Sierra, Srednicki, moments (Keating–Snaith/CFKRS), FHK,
    Katz–Sarnak, Selberg analogy, experimental realizations.
  - `analytic-progress/` 27 — critical-line proportions (HL 1921 → PRZZ 41.7%),
    zero-density (Guth–Maynard + 2025–26 frontier, ANTEDB), zero-free regions
    (incl. BTY 2026 record), de Bruijn–Newman, Lindelöf, verification, Zhang.
  - `algebraic-geometric/` 39 — Weil 1941 → Deligne (numdam) → standard conjectures →
    F₁ corpus → Bost–Connes → complete Connes–Consani 2014–2026 series → Deninger →
    Morishita 2025 (the two programs converge).
  - `criteria/` 45 — Weil positivity, Li/Keiper–Li, Nyman–Beurling/Báez-Duarte,
    Robin/Lagarias/Nicolas, Riesz/HL, Redheffer/Farey/Speiser/Salem, de Branges saga.
  - `surveys-expository/` 18 — Riemann 1859, Clay/Bombieri/Sarnak/Conrey, Atiyah +
    de Branges primary sources, Jensen-polynomials story with rebuttals.
  - `recent/` 15 — 2019–2026: GM ecosystem, CC zeta spectral triples + "Letter to
    Riemann", formalization (RH now stated in Mathlib), claimed-proof audit.
- **Next:** ATTACK.md §10 portfolio — small-δ T1 proof attempt (Sonin margin vs the
  explicit (log 2)/√2 bound), the lag-log 2 cancellation lemma, rigorous
  interval-arithmetic certificates for the sweep's regime boundaries.

## Logging discipline

- `logs/LOG.md` — append-only narrative work log (UTC timestamps).
- One commit per artifact (paper, notes file, doc) with full citation in the message.
- Everything pushed to GitHub promptly; this repo is the source of truth for progress.
