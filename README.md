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

_Last updated: 2026-07-23 10:34 UTC. This section is refreshed regularly; the commit
history and `logs/LOG.md` carry the fine-grained record._

- **Phase:** collection — 4 of 6 research agents still searching/downloading.
- **Complete:**
  - `recent/` ✅ 15 verified PDFs + `notes/recent.md` — 2019–2026 frontier:
    Guth–Maynard ecosystem, Connes–Consani 2025–26 arc (zeta spectral triples,
    Feb 2026 "Letter to Riemann"), Zhang status, Lean/Mathlib formalization.
  - `spectral/` ✅ 34 verified PDFs + `notes/spectral.md` — Hilbert–Pólya program
    end-to-end: Montgomery/Odlyzko GUE, Berry–Keating xp line, BBM 2017 controversy,
    Sierra corpus, Srednicki, Keating–Snaith/CFKRS moments, FHK extremes,
    Katz–Sarnak, Selberg analogy, experimental realizations.
- **In flight:** algebraic-geometric 39 · criteria 44 · analytic-progress 27 ·
  surveys-expository 18 — 177 PDFs on disk total, committed per-artifact as each
  agent lands (avoids truncated mid-download files).
- **Next:** remaining category passes, then `BREAKDOWN.md` — the synthesis of which
  approaches could actually work.

## Logging discipline

- `logs/LOG.md` — append-only narrative work log (UTC timestamps).
- One commit per artifact (paper, notes file, doc) with full citation in the message.
- Everything pushed to GitHub promptly; this repo is the source of truth for progress.
