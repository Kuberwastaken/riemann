# Work log — Riemann Hypothesis research archive

Append-only, chronological. All times UTC. Every session action that changes this repo
gets an entry; commits reference this log implicitly (GitHub history is the fine-grained
record, this file is the narrative).

---

## 2026-07-23

- **~09:55** — Project started. Created `~/dev/Riemann` skeleton: `papers/{spectral, analytic-progress, algebraic-geometric, criteria, surveys-expository, recent}/`, `notes/`. `git init` (branch `main`), repo-local identity set (global git identity is unset on this box).
- **~10:00** — Launched six parallel research agents, one per approach family:
  1. *spectral* — Hilbert–Pólya program: Montgomery pair correlation, Berry–Keating H=xp, Connes spectral realization, Bender–Brody–Müller, Sierra models, random-matrix moments (Keating–Snaith/CFKRS), Fyodorov–Hiary–Keating, Katz–Sarnak, Selberg trace formula analogy, experimental realizations.
  2. *analytic-progress* — zeros on the critical line (Hardy → Selberg → Levinson → Conrey → Pratt–Robles–Zaharescu–Zeindler), zero-density incl. Guth–Maynard 2024, zero-free regions, de Bruijn–Newman (Rodgers–Tao, Polymath15), Lindelöf (Bourgain 13/84), computational verification (Platt–Trudgian 3·10¹²), Zhang Landau–Siegel.
  3. *algebraic-geometric* — Weil 1948 function-field proof, Deligne Weil conjectures, standard conjectures, F₁ geometry (Manin, Soulé, Borger, Lorscheid), Connes–Consani arithmetic/scaling site + Weil positivity, Deninger program, Bost–Connes.
  4. *criteria* — Weil positivity, Li's criterion (+ Bombieri–Lagarias), Nyman–Beurling + Báez-Duarte, Robin/Lagarias/Nicolas, Balazard–Saias–Yor, Riesz, Redheffer, Franel–Landau, Speiser, de Branges saga + Conrey–Li refutation.
  5. *surveys-expository* — Clay official statement (Bombieri), Sarnak 2004, Conrey Notices 2003, Katz–Sarnak BAMS, Riemann 1859 (Wilkins translation), Edwards/Titchmarsh refs, Atiyah 2018 post-mortem, de Branges claims, Jensen-polynomials story (Griffin–Ono–Rolen–Zagier), Tao/Woit/Quanta coverage.
  6. *recent* — 2019–mid-2026 sweep: Guth–Maynard follow-ups, Connes–Consani zeta cycles/prolate operators, Zhang status, Lean formalization (PrimeNumberTheorem+), AI-assisted efforts, new verification records, serious new claims.
- **~10:05** — First commit `2394a53` (scaffold: README + .gitignore).
- **~10:15** — Remote wired: `origin` → https://github.com/Kuberwastaken/reimann (private, was empty). Pushed `main`. GitHub is the source of truth for progress from here on.
- **~10:20** — Download progress check: ~50 PDFs on disk (~30 MB) across 5 of 6 categories; agents still running, `notes/` not yet written (agents write notes after collection).
- **10:24** — Operating directives locked in (from user):
  - **Model policy:** outreach/fetch agents run on Sonnet/Opus to save costs; Fable is reserved for analysis, reading, and synthesis. (The six initial agents were launched before this directive on the session default; all future agents follow the policy.)
  - **Logging:** very regular logs — this file, per-artifact commits, README status refreshed regularly, everything pushed so GitHub stays current.
  - **Observability cron:** recurring job every ~20 min: inventory stable new files, verify PDFs, commit one-per-file, refresh README status + this log, push.
- **10:25** — Paper count at this entry: spectral 31, algebraic-geometric 29, analytic-progress 23, criteria 23, surveys-expository 16, recent 0 (agent still searching) — 122 PDFs total. Commit-per-artifact pass will run once agents finish writing (committing mid-download risks truncated files).
