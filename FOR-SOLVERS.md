# FOR SOLVERS — how to use this repository to attack the Riemann Hypothesis

*You are here because you intend to work on RH and want to stand on what this archive
already mapped instead of re-walking it. This is the entry point: what to read and in
what order, which walls and dead ends are already charted (so you don't spend a year
rediscovering them), which openings are genuinely live, how to reproduce every
computational claim, and an honest word about how hard this actually is.*

**First, calibration.** Nothing in this repository is close to proving RH, and the
archive's considered verdict is that **no currently visible route is close**
([`BREAKDOWN.md`](BREAKDOWN.md) §1, [`ATTACK.md`](ATTACK.md) §11). What the repo offers
is not a head start on a proof; it is a *map of the terrain* — the barriers stated as
theorems, the failure anatomy of every dead end, and a short list of well-posed, sub-RH
problems where honest finite progress is possible. Treat it as a field guide, not a
launch pad.

---

## 1. Reading order

1. **[`README.md`](README.md)** — what the archive is and how it is laid out.
2. **[`BREAKDOWN.md`](BREAKDOWN.md)** — the survey. The six families of approach, what
   each has actually achieved, where each stalls, and the three walls every route hits.
   Read this before forming any opinion about which direction to push.
3. **[`ATTACK.md`](ATTACK.md)** — the deep dive. RH reduced to a boundary-feasible convex
   positivity program; the full **no-go map** (§2) you must keep taped to the wall; the
   only two mechanisms in history that ever finished an RH-type problem (§3); and a
   concrete lemma-by-lemma research portfolio (§10).
4. **[`notes/`](notes/)** — when you need the item-by-item detail behind a claim in the
   two documents above, go to the matching annotated bibliography, then to the PDF in
   [`papers/`](papers/).
5. **[`experiments/weil_positivity/NOTE.md`](experiments/weil_positivity/NOTE.md)** — the
   one place the archive stopped surveying and started computing. Read this, then
   [`RESULTS.md`](experiments/weil_positivity/RESULTS.md),
   [`T1-ARCHITECTURE.md`](experiments/weil_positivity/T1-ARCHITECTURE.md), and
   [`PROOF-c0.md`](experiments/weil_positivity/PROOF-c0.md).
6. **[`FINDINGS.md`](FINDINGS.md)** — the honest ledger of exactly what was and was not
   established (including the conjectures the project killed). Read it so you inherit the
   corrections, not just the claims.
7. **[`GAPS.md`](GAPS.md)** and **[`LEADS.md`](LEADS.md)** — the openings, ranked. These
   are where a new attempt would actually start.

---

## 2. The barriers the archive maps (know these cold before you start)

### The three walls (any approach must pass all three — [`BREAKDOWN.md`](BREAKDOWN.md) §2)

1. **Positivity.** RH ⟺ the Weil explicit-formula quadratic functional is ≥ 0. Over
   function fields this is the Hodge index theorem on a surface (how Weil won); over ℚ
   nobody can prove it beyond restricted test-function support (Connes–Consani 2020:
   support ratio ≤ 2). Every equivalent criterion is this wall relocated.
2. **The missing arithmetic object.** In every solved analogue the zeros are eigenvalues
   of an operator on the cohomology of a geometric object. For Spec ℤ that object — an
   "F₁-curve" with a Frobenius flow — does not yet exist; the arithmetic site, the
   scaling site, and Deninger's dynamical systems are the attempts to build it.
3. **Sharpness.** Rodgers–Tao 2018: the de Bruijn–Newman constant Λ ≥ 0, so RH (if true)
   is *barely* true — there is no analytic slack. Any argument that loses an ε anywhere is
   dead on arrival. Combined with Davenport–Heilbronn (a Dirichlet series with ζ's shape
   but off-line zeros), this gives the two-minute triage: *where is the Euler product
   used, and where is the argument sharp?*

### The no-go map (dead ends already charted — [`ATTACK.md`](ATTACK.md) §2)

A 15-row table of fences with sources, each labeled with exactly what it kills — from
"Λ ≥ 0 kills any strategy with analytic slack" to "de Branges-type checkable-sufficient
conditions provably overshoot RH (Conrey–Li)" to "quantize xp is not even well-posed
(Regniers–Van der Jeugt)." **Do not start any route without checking it against this
table.** The two historical *positive* filters that complete the map: Deligne won the
model case by *abandoning* positivity for Rankin squaring; Viazovska won a boundary-tight
certificate problem by *constructing* the dual object from modular forms. The proof, when
it comes, likely resembles one of those two shapes.

### Dead ends this project charted itself (in [`FINDINGS.md`](FINDINGS.md) Tier 5)

Save yourself the trips: **all spatial-decomposition routes to the one-prime target T1
are closed** (sharp blocks refuted numerically; smooth/IMS localization costs 1/δ²
against a log(1/δ) gain). **The two-vector moment ladder saturates at 77% of what T1
needs.** **The clean `e^{−4γ₁L}` criticality-rate law is false** (the decay accelerates
past 4γ₁). T1 must be won globally in the spectral variable, not by any spatial or
low-moment argument.

---

## 3. The live openings (where a new attempt would actually start)

Ranked, with the repo's own difficulty/cost estimates. Full statements in
[`LEADS.md`](LEADS.md) and [`GAPS.md`](GAPS.md); the strategic framing in
[`ATTACK.md`](ATTACK.md) §4–§10.

### The central target: T1 — one-prime Weil positivity
The sharpest concrete opening in the entire archive: *prove Weil positivity for test
functions supported just past the ratio-2 window, where exactly one prime (p=2) is
active.* It would be the **first Weil-positivity statement in history with arithmetic
content**, it is finite and compactly supported, and it sits directly on proven
Connes–Consani technology. This repo reduced it to a single sharp inequality —
`μ(L) = λ_min(G^{−1/2}Q₂G^{−1/2}) > −1` (T1-ARCHITECTURE §v2) — and produced rigorous
certificates on finite-dimensional families all the way through it (FINDINGS Tier 1), but
the full-space theorem is **open**. The known-good route forward is:

- **Lead 1 — the graded-mode architecture** ([`LEADS.md`](LEADS.md) Lead 1): dyadic
  Fourier-mode blocks + a certified finite section + an explicit high-block coercivity
  lemma (the kernel singularity *is* high-frequency growth — the good direction) +
  Cotlar–Stein for the cross terms. The first full-space T1 architecture with no step
  that collides with a known no-go. Estimated 2–4 weeks of constant-chasing for a strong
  analyst. **This is the successor project.**

### Finishable in the existing laboratory (days–weeks)
- **Lead 2 — ε_N certification service to CCM 2025.** Certify the sign, simplicity, and
  evenness of the smallest eigenvalue that CCM's Zeta-Spectral-Triples theorem *assumes* —
  the repo's finite-section certificates are exactly the right objects (Gap 3 inverted the
  dictionary). Directly useful to the leading live RH program; entirely within the
  existing pipeline.
- **Lead 3 — the certified razor corridor**, extended to a curve of windows: a certified,
  window-by-window quantitative "RH is barely true."
- **Lead 5 — the repeated-orbit seam.** Nobody in the 178 sources treats the k ≥ 2
  prime-power terms (n = 4, 8, 9, …) separately, yet they *hurt* positivity while primes
  rescue it. Primes-only vs. full prime-power λ_min curves are runnable today and may
  reformulate RH as *primes-only positivity + an explicitly bounded ψ−θ correction*.

### Cheap tests with outsized information value
- **Gap 5 — the Deninger function-field consistency test.** Run the whole transplant
  program in the one world where the answer is known (a function-field base) and check it
  reproduces Weil's theorem. **Nobody has done this**; its absence is itself a finding.
  One computation validates a 25-year program or locates its gap.

### Well-posed exports (belong to specialist communities, not this box)
- **Lead 4** — derive the true super-exponential criticality envelope from Paley–Wiener
  extremal theory (the corrected target after the 4γ₁ law was refuted).
- **Lead 6** — Guth–Maynard large-value technology × de-conditionalized pair correlation:
  the plausible classical route past the 41.7% critical-line record toward a first
  majority-on-the-line theorem. The sharpest lever classical analysis has had in 50 years.
- **Lead 7** — formalize Theorem A in Lean via the repo's x86 CI (its three lemmas are
  Mathlib-friendly): the first machine-formalized quantitative statement adjacent to Weil
  positivity, and an independent stress-test of the proof.

---

## 4. Reproducing the computational results

Every empirical and certified claim comes from committed, deterministic scripts in
[`experiments/weil_positivity/`](experiments/weil_positivity/). The virtual environment
is git-ignored; recreate it (`numpy`, `scipy`, `mpmath`, and `python-flint` 0.9.0 for the
Arb-certified pipelines), then:

```
# numerical engine — validated against the explicit-formula identity
experiments/.venv/bin/python weil_positivity/weil_form.py test        # self-tests
experiments/.venv/bin/python weil_positivity/weil_form.py validate    # identity check (arith vs 100k zeros)
experiments/.venv/bin/python weil_positivity/weil_form.py sweep       # the four-regime map, ~12 min on a Pi 5
experiments/.venv/bin/python weil_positivity/weil_form.py profiles    # minimizer profiles
experiments/.venv/bin/python weil_positivity/make_plots.py            # figures

# rigorous (Arb ball-arithmetic) certificates
experiments/.venv/bin/python weil_positivity/certify.py <L> [N]       # the certified positivity curve, ~1 min/point
experiments/.venv/bin/python weil_positivity/certify_c0.py            # Theorem A (archimedean coercivity floor)
experiments/.venv/bin/python weil_positivity/rescue_certify.py        # the rescue phenomenon, L=0.62
```

See [`experiments/README.md`](experiments/README.md) for the file-by-file map and
[`experiments/weil_positivity/NOTE.md`](experiments/weil_positivity/NOTE.md) §7 for the
data files each command produces. Built and run on a Raspberry Pi 5; nothing here needs a
cluster.

**What reproduction does and does not buy you.** The `validate` step certifies the
engine's conventions against ground truth (Odlyzko's zeros); the `certify.py` /
`certify_c0.py` / `rescue_certify.py` outputs are rigorous *within their stated finite
families or windows*. **None of them tests RH itself** — every height involved carries a
verified zero, so positivity is guaranteed-by-data in the computed range. The value is the
decomposition, the sharp constants, and the certified subspace statements — not evidence
for or against RH.

---

## 5. Honest calibration

From [`ATTACK.md`](ATTACK.md) §11, unedited in spirit: the two statements that are
literally one theorem from RH — global Weil positivity, and convergence of the
zeta-spectral-triple spectra — are each *one RH-hard theorem* from RH. What is genuinely
new is that there now exists a **well-posed, finite, plausibly sub-RH-hard theorem of the
exact RH-equivalent species** (T1, one-prime positivity) sitting on proven technology,
with a geometric dual (finite-level tropical Hodge index) and an operator dual (spectral
triples) that transfer progress both ways. The realistic best case for a decade of the
whole portfolio is *not* a proof of RH; it is cornering the difficulty into one identified
analytic limit — which is how hard problems actually end. The lightning-bolt precedents
(Deligne's squaring, Viazovska's function) both struck *after* their fields had done
exactly that cornering.

If you take one thing from this repository: **the difficulty of RH is not distributed —
it is concentrated at the archimedean–arithmetic boundary, at support ratio 2, where the
first prime is waiting.** That is where this archive points, and where the one attackable
theorem of the right species lives.
