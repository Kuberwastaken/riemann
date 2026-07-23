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

_Last updated: 2026-07-23 10:44 UTC. This section is refreshed regularly; the commit
history and `logs/LOG.md` carry the fine-grained record._

- **Phase:** **complete** — collection (6/6 agents) and synthesis done.
  **→ Read [`BREAKDOWN.md`](BREAKDOWN.md)** for the full analysis: the three walls,
  family-by-family verdicts, what a successful proof must look like, and the watch list.
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
- **Next:** `BREAKDOWN.md` — the synthesis of which approaches could actually work.

## Logging discipline

- `logs/LOG.md` — append-only narrative work log (UTC timestamps).
- One commit per artifact (paper, notes file, doc) with full citation in the message.
- Everything pushed to GitHub promptly; this repo is the source of truth for progress.
