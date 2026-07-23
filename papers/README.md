# `papers/` — the primary-source archive

178 primary sources on the Riemann Hypothesis, organized by approach family. Every
file is a genuine PDF fetched from arXiv or an author's homepage (no pirate mirrors),
verified with `file` and spot-checked with `pdftotext` at collection time. Filenames
are kebab-case `author-year-topic.pdf`. Each PDF is its own git commit with a full
citation in the commit message — the git history is the provenance record.

For the annotated, one-entry-per-item reading of everything here, see the matching
file in [`../notes/`](../notes/); for the synthesis of what it all adds up to, see
[`../BREAKDOWN.md`](../BREAKDOWN.md).

## Third-party works — copyright notice

> **The papers in this directory are NOT covered by this repository's Apache-2.0
> license.** Each is the work of its respective author(s) and remains under its own
> copyright and/or the license under which it was posted (arXiv non-exclusive
> distribution license, publisher terms, author homepage terms, etc.). They are
> collected here solely for research convenience — to keep the annotated
> bibliographies, the synthesis, and the numerical experiment next to the sources
> they cite. No claim of ownership or authorship over any paper in `papers/` is made
> or implied, and no additional rights are granted by their inclusion here. If you
> are a rights-holder and want an item removed, open an issue. The Apache-2.0 license
> in [`../LICENSE`](../LICENSE) applies only to the repository's *original* content
> (the notes, analyses, experiment code, and documentation).

Paywalled classics that could not be legally redistributed are **not** in this
directory; they are cited by DOI / reference in the notes instead (see the tail of
[`../BREAKDOWN.md`](../BREAKDOWN.md) §7 for the citation-only list).

## Categories

| Directory | Count | What lives here | Notes file |
|---|---|---|---|
| [`spectral/`](spectral/) | 34 | Hilbert–Pólya, Berry–Keating `H=xp`, Connes spectral realization, random-matrix theory (Montgomery, Odlyzko, Keating–Snaith, CFKRS, FHK), Katz–Sarnak, Selberg trace formula, physics/experimental realizations, the BBM 2017 controversy end-to-end | [`spectral.md`](../notes/spectral.md) |
| [`analytic-progress/`](analytic-progress/) | 27 | Unconditional partial results: proportion of zeros on the line (Hardy–Littlewood 1921 → PRZZ 41.7%), zero-density (Guth–Maynard 2024 + frontier), zero-free regions (through BTY 2026), de Bruijn–Newman (Rodgers–Tao), Lindelöf, computational verification, Zhang Landau–Siegel | [`analytic-progress.md`](../notes/analytic-progress.md) |
| [`algebraic-geometric/`](algebraic-geometric/) | 39 | The "transplant Weil's proof" dream: function fields (Weil, Deligne), standard conjectures, **F₁** geometry, the complete Connes–Consani arithmetic/scaling-site series 2014→2026, Deninger's dynamical program, Morishita 2025 | [`algebraic-geometric.md`](../notes/algebraic-geometric.md) |
| [`criteria/`](criteria/) | 45 | Equivalent reformulations: Weil positivity, Li/Keiper–Li, Nyman–Beurling / Báez-Duarte, Robin/Lagarias/Nicolas, Riesz/Hardy–Littlewood, Redheffer/Farey/Speiser/Salem, and the de Branges saga (Apology, 2017 claim, Conrey–Li refutation) | [`criteria.md`](../notes/criteria.md) |
| [`surveys-expository/`](surveys-expository/) | 18 | Riemann's 1859 memoir, the Clay/Bombieri/Sarnak/Conrey surveys, the famous failed proofs as primary sources (Atiyah 2018, de Branges), the Jensen-polynomials story with its rebuttals, media coverage | [`surveys-expository.md`](../notes/surveys-expository.md) |
| [`recent/`](recent/) | 15 | 2019–2026 developments: the Guth–Maynard ecosystem, Connes–Consani zeta spectral triples + "Letter to Riemann", Jacobian / absolute geometry of Spec ℤ, Lean/Mathlib formalization, claimed-proof audit | [`recent.md`](../notes/recent.md) |

A handful of items appear in more than one category (e.g. the Connes–Consani
positivity and zeta-cycles papers sit in both `algebraic-geometric/` and `spectral/`
or `criteria/`) because they are load-bearing for more than one line of attack; the
178 count is of files on disk.
