# Riemann — a research archive of approaches to the Riemann Hypothesis

An annotated archive of every major serious approach to the Riemann Hypothesis — the
primary papers, expository material, and a synthesis of which routes could actually work —
together with a small numerical and computer-assisted laboratory around Weil positivity.
It was built by a fleet of AI research agents under human direction; it surveys the
problem honestly and proves nothing new about RH. If you are here to *work* on RH, start
with **[`FOR-SOLVERS.md`](FOR-SOLVERS.md)**.

> **178 primary sources** in [`papers/`](papers/), each its own commit · **6 annotated
> bibliographies** in [`notes/`](notes/) · a survey ([`BREAKDOWN.md`](BREAKDOWN.md)), a
> deep-dive attack map ([`ATTACK.md`](ATTACK.md)), and a Weil-positivity experiment
> ([`experiments/`](experiments/)). Collected, analyzed, and prepared for public
> release 2026-07-23.

## The one-paragraph answer

After 166 years, every serious assault on RH belongs to one of six families, and each
serious program fails the same one of three walls — **positivity** (RH ⟺ the Weil
explicit-formula functional is ≥ 0, a theorem over function fields, unproven over ℚ
beyond restricted support), **the missing arithmetic object** (a Frobenius-flowed
"F₁-curve" for Spec ℤ, which the Connes–Consani and Deninger programs are trying to
build), and **sharpness** (Rodgers–Tao's Λ ≥ 0 says RH, if true, is *barely* true, so no
argument with an ε of slack can work). The most probable shape of a future proof is a
positivity theorem in a new arithmetic geometry, with the analytic and random-matrix
corpus as constraint-checking scaffolding — but **no visible route is close**. The full
argument, family by family, is in [`BREAKDOWN.md`](BREAKDOWN.md); the reduction of RH to a
boundary-feasible convex positivity program, the no-go map, and a concrete research
portfolio are in [`ATTACK.md`](ATTACK.md).

## How it was built

This is an **AI-orchestrated research archive**, and says so plainly. Collection ran as
six parallel research agents (one per approach family); reading, verification, and
synthesis were done in separate passes; the numerical experiment and its rigorous
certificates were built and run on a Raspberry Pi 5. Discipline enforced throughout: one
artifact = one git commit (the history is the provenance record); PDFs fetched only from
arXiv and author homepages, each verified as a genuine file; an append-only narrative
work log ([`logs/LOG.md`](logs/LOG.md)). The project's original mathematical output is
modest and honestly tiered in [`FINDINGS.md`](FINDINGS.md) — a few proven elementary
lemmas, rigorous *subspace* positivity certificates, an exact reformulation of the
one-prime target, and several conjectures the project then refuted with its own
instruments. **None of it proves RH, and none of it is claimed to.**

## Headline contents

| Document | What it is |
|---|---|
| **[`FOR-SOLVERS.md`](FOR-SOLVERS.md)** | The entry point for anyone attacking RH with this repo: reading order, the barriers and dead ends already charted, the live openings, reproduction instructions, honest calibration. |
| **[`FINDINGS.md`](FINDINGS.md)** | The honest, tiered ledger of what the project actually produced — apparently-new results with their audit status, proven lemmas, numerical observations, unadjudicated items, and self-refutations with attribution. |
| **[`BREAKDOWN.md`](BREAKDOWN.md)** | The survey: the six families, what each achieved and where it stalls, the three walls, what a real proof must look like, a watch list. |
| **[`ATTACK.md`](ATTACK.md)** | The deep dive: RH as a boundary-feasible convex program, the 15-row no-go map, the only two mechanisms that ever finished an RH-type problem, and a lemma-by-lemma portfolio. |
| **[`GAPS.md`](GAPS.md)** | Six sharp openings found by cross-reading the archive's proofs against the experiment's measurements (one closed, one resolved, one refuted, three open). |
| **[`LEADS.md`](LEADS.md)** | Seven vetted leads, ranked, each checked against the project's own no-go results. |
| **[`experiments/`](experiments/)** | The Weil-positivity laboratory: the numerical regime map, the proven lemmas, and the Arb-certified positivity curve. Start at [`experiments/weil_positivity/NOTE.md`](experiments/weil_positivity/NOTE.md). |
| **[`papers/`](papers/)** · **[`notes/`](notes/)** | 178 primary-source PDFs by approach family, and the annotated bibliography for each. |

## Repository layout

```
papers/                 178 primary sources, by approach family (see papers/README.md)
  spectral/             Hilbert–Pólya, Berry–Keating, Connes realization, RMT, physics    (34)
  analytic-progress/    critical-line proportion, zero-density, zero-free, dBN, Lindelöf   (27)
  algebraic-geometric/  function fields, F₁, the Connes–Consani series, Deninger           (39)
  criteria/             Weil positivity, Li, Nyman–Beurling, Robin, Riesz, de Branges       (45)
  surveys-expository/   Riemann 1859, Clay/Bombieri/Sarnak, failed proofs, media            (18)
  recent/               2019–2026: Guth–Maynard aftermath, CC 2023–26, formalization        (15)
notes/                  6 annotated bibliographies, one per family (see notes/README.md)
experiments/            the Weil-positivity numerical + certified laboratory
BREAKDOWN.md            the synthesis (survey + verdicts + three walls)
ATTACK.md               the deep-dive attack map
GAPS.md · LEADS.md      the openings and the leads
FINDINGS.md             the honest tiered ledger of results
FOR-SOLVERS.md          the resource-kit entry point for would-be solvers
logs/LOG.md             append-only narrative work log
```

## Quickstart

- **Just want the state of play?** Read [`BREAKDOWN.md`](BREAKDOWN.md), then
  [`FINDINGS.md`](FINDINGS.md).
- **Planning to work on RH?** Read [`FOR-SOLVERS.md`](FOR-SOLVERS.md) — it sequences
  everything else.
- **Want to reproduce the computations?** See
  [`experiments/README.md`](experiments/README.md); the engine validates against the
  explicit-formula identity, and the certified results run in ~1 min each on a Raspberry
  Pi 5.
- **Want the sources?** Browse [`papers/`](papers/) with its [`notes/`](notes/)
  companions.

## License

The repository's **original content** — the notes, the analyses (`BREAKDOWN`, `ATTACK`,
`GAPS`, `LEADS`, `FINDINGS`, `FOR-SOLVERS`), the experiment code and writeups, and the
documentation — is released under the **Apache License 2.0** ([`LICENSE`](LICENSE)),
copyright Kuber Mehta.

> **Third-party carve-out.** The PDFs in [`papers/`](papers/) are **not** covered by that
> license. Each is the work of its respective author(s) and remains under its own
> copyright and/or the license under which it was posted (arXiv distribution license,
> publisher terms, author-homepage terms). They are included **solely for research
> convenience**, so the notes and experiment sit next to the sources they cite. No
> ownership or authorship over any collected paper is claimed or implied, and no
> additional rights are granted by their inclusion. Rights-holders who want an item
> removed can open an issue. Details in [`papers/README.md`](papers/README.md).

## Provenance

- [`logs/LOG.md`](logs/LOG.md) — append-only narrative work log (UTC timestamps).
- One commit per artifact (paper, notes file, doc), with citations in the commit
  messages — the git history is the fine-grained audit trail.
- To cite this archive, see [`CITATION.cff`](CITATION.cff).
