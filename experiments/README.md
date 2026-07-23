# `experiments/` — the numerical + certified laboratory

Where the archive stops surveying and starts computing. One experiment lives here so
far: [`weil_positivity/`](weil_positivity/), a study of the **Weil explicit-formula
quadratic functional** in the critical support window — the object whose positivity is
equivalent to RH (Weil 1952). It grew out of target **T1** in
[`../ATTACK.md`](../ATTACK.md) §4/§10 (the first Weil-positivity statement that "defeats
a prime").

The engine builds the form numerically and — critically — validates it against the
Riemann–Weil explicit-formula *identity* (arithmetic side vs. a sum over Odlyzko's first
100,000 zeros) to relative error 10⁻⁵–10⁻⁷, so all conventions are certified by the
identity itself. A second pipeline re-derives selected results **rigorously** in Arb
ball arithmetic (verified integration + certified Cholesky) via `python-flint`.

> **Nothing here proves RH, and none of it is claimed to.** Every rigorous ("certified")
> result is a statement about an explicit finite-dimensional family of test functions or
> a single window — not a full-space theorem. The value is the *anatomy*: where each
> mechanism turns on, what the sharp constants are, and which sub-statements are provable
> today. See [`../FINDINGS.md`](../FINDINGS.md) for the honest tiering and
> [`../FOR-SOLVERS.md`](../FOR-SOLVERS.md) for how to build on it.

## Reading order

1. [`weil_positivity/NOTE.md`](weil_positivity/NOTE.md) — the consolidated, paper-style
   research note (setup, regime map, lemmas with proofs, the μ reformulation, the
   certified-positivity curve, the structural discoveries, reproducibility). **Start here.**
2. [`weil_positivity/RESULTS.md`](weil_positivity/RESULTS.md) — the numerical regime map
   in full: the four regimes of positivity and the quantitative landmarks.
3. [`weil_positivity/T1-ARCHITECTURE.md`](weil_positivity/T1-ARCHITECTURE.md) — the proof
   architecture for T1: Lemma 1/1′/1″ (proven), the μ-invariant reformulation, the
   certified results 1–6, the just-in-time-rescue and completion-criticality discoveries,
   and the honest no-go analysis of every spatial route.
4. [`weil_positivity/PROOF-c0.md`](weil_positivity/PROOF-c0.md) — Theorem A: elementary
   proof of explicit coercivity of the archimedean form on the prime-free window
   (certified constant c₀ ≥ 0.349152), the quantitative floor CC 2020 left unstated.

## What's in `weil_positivity/`

| Kind | Files |
|---|---|
| **Writeups** | `NOTE.md`, `RESULTS.md`, `T1-ARCHITECTURE.md`, `PROOF-c0.md` |
| **Engine** | `weil_form.py` (the validated numerical form), `make_plots.py`, `zeros1.txt` (Odlyzko zeros) |
| **Certification pipelines** (Arb / `python-flint`) | `certify.py`, `certify_L045.py`, `certify_c0.py`, `rescue_certify.py` |
| **Structural probes** | `t1_blocks.py` (spatial-block route, refuted), `law_test.py` (the 4γ₁ law, refuted) |
| **Data / outputs** | `sweep.csv`, `t1_mu.txt`, `rescue_cascade.txt`, `mu_extremal.txt`, `razor_certificate.txt`, `*_output.txt`, `profiles.npz` |
| **Figures** | `sweep.png`, `profiles.png` |

## Reproduce

The virtual environment (`experiments/.venv/`) is git-ignored; recreate it with the
dependencies below, then:

```
experiments/.venv/bin/python weil_positivity/weil_form.py test      # digamma + FT self-tests
experiments/.venv/bin/python weil_positivity/weil_form.py validate  # explicit-formula identity check
experiments/.venv/bin/python weil_positivity/weil_form.py sweep     # ~12 min on a Pi 5 -> sweep.csv
experiments/.venv/bin/python weil_positivity/weil_form.py profiles  # minimizer profiles -> profiles.npz
experiments/.venv/bin/python weil_positivity/make_plots.py          # sweep.png, profiles.png
experiments/.venv/bin/python weil_positivity/certify.py <L> [N]     # certified positivity, ~1 min each
experiments/.venv/bin/python weil_positivity/rescue_certify.py      # rescue certification (L=0.62)
```

Environment: Python venv with `numpy`, `scipy`, `mpmath`, and `python-flint` 0.9.0
(the last supplies Arb; needed only for the certified pipelines). Built and run on a
Raspberry Pi 5. All scripts are deterministic.
