# Recent Developments on the Riemann Hypothesis, 2019–2026 (fresh sweep, compiled 2026-07-23)

Scope: the newest material — Guth–Maynard and its aftermath, Connes–Consani 2023–2026, Landau–Siegel status, Jensen polynomials, formalization, AI-assisted mathematics, verification records, and mid-2026 items the other category notes may predate. All local files are in `/root/dev/Riemann/papers/recent/`.

---

## 1. Guth–Maynard, "New large value estimates for Dirichlet polynomials"
- **Who/when:** Larry Guth (MIT) and James Maynard (Oxford), arXiv 2405.20552, May 2024; published in **Annals of Mathematics (2025)**.
- **Links:** https://arxiv.org/abs/2405.20552
- **Local file:** `Guth-2024-large-values-dirichlet.pdf` (52 pp.)
- **Summary:** The anchor result of this whole period. They prove new bounds on how often a Dirichlet polynomial of length N can take values of size near N^{3/4} — the critical regime for zero-density questions — by recasting the large-values problem in terms of the eigenvalues/eigenvectors of an associated matrix and exploiting additive structure (difference sets, additive energy) of the set of large values. Consequences: the zero-density estimate N(σ,T) ≪ T^{30(1-σ)/13+o(1)}, the first improvement at σ = 3/4 over Ingham (1940) / Huxley's 12/5 exponent in over 80 years, and asymptotics for primes in all short intervals [x, x + x^{17/30+ε}] (previous record exponent 7/12).
- **Status/reception:** Fully refereed and published in the Annals; universally accepted; covered by Quanta and Scientific American in 2024; already a heavily cited platform for follow-up work (see items 2–6).
- **RH significance:** Not a proof technique for RH itself, but the strongest unconditional progress in decades on "almost all zeros are where RH says they are" in the key part of the critical strip; it moved a frontier (density estimates at σ=3/4) that had been static since 1940 and re-energized classical analytic approaches.

## 2. Bin Chen, "Large value estimates for Dirichlet polynomials, and the density of zeros of Dirichlet's L-functions"
- **Who/when:** Bin Chen (Ghent University), arXiv 2507.08296, July 2025.
- **Links:** https://arxiv.org/abs/2507.08296
- **Local file:** `Chen-2025-zero-density-L-functions.pdf` (50 pp.)
- **Summary:** The first substantial transplant of the Guth–Maynard method from ζ(s) to the family of Dirichlet L-functions: proves Σ_{χ mod q} N(σ,T,χ) ≪ (qT)^{7(1-σ)/3+ε}, improving Huxley's 12/5 exponent for this averaged family (7/3 ≈ 2.333, vs. GM's 30/13 ≈ 2.308 for ζ alone). Key innovation is a sharp bound for sums over affine transformations with GCD twists arising when the GM machinery meets character sums. Corollaries: new results on the least prime in arithmetic progressions to prime-power moduli and on least Goldbach numbers in progressions.
- **Status/reception:** Preprint under review; treated as the natural "GRH-adjacent" extension of GM in subsequent literature.
- **RH significance:** Direct evidence that the GM breakthrough is a method, not a one-off — it generalizes across the q-aspect, i.e., toward the Grand Riemann Hypothesis family picture.

## 3. Gafni–Tao, "On the number of exceptional intervals to the prime number theorem in short intervals"
- **Who/when:** Ayla Gafni (Mississippi) and Terence Tao (UCLA), arXiv 2505.24017, May 2025.
- **Links:** https://arxiv.org/abs/2505.24017
- **Local file:** `Gafni-2025-exceptional-intervals.pdf` (~30 pp.)
- **Summary:** Establishes an explicit machine translating any zero-density estimate into bounds on the size of the exceptional set of x for which the PNT in intervals [x, x+x^θ] fails, with modest computer assistance. Plugging in Guth–Maynard (PNT in short intervals known for all x when θ > 17/30, for almost all x when θ > 2/15) yields the best known exceptional-set bounds across the range of θ. A worked example of how the 2024 estimates propagate through the literature.
- **Status/reception:** Preprint; discussed on Tao's blog; uncontroversial.
- **RH significance:** Quantifies exactly how much of "RH-strength" prime distribution is already unconditionally available — the gap between GM-world and RH-world made numerically explicit.

## 4. Turnage-Butterbaugh, "A decades-long breakthrough in zero-density estimates and primes in short intervals"
- **Who/when:** Caroline L. Turnage-Butterbaugh (Carleton College), arXiv 2607.04632, **July 2026** (three weeks old at compile time).
- **Links:** https://arxiv.org/abs/2607.04632
- **Local file:** `TurnageButterbaugh-2026-zero-density-survey.pdf` (~25 pp.)
- **Summary:** Expository account (apparently commissioned, Bulletin-style) placing Guth–Maynard in the century-long history of zero-density theorems from Bohr–Landau and Carlson through Ingham, Huxley, and Jutila, and explaining the implications for primes in short intervals. Useful as the current canonical "what just happened and why it matters" reference.
- **Status/reception:** Brand new; expository, so low risk.
- **RH significance:** Survey value only, but it certifies mainstream consensus that GM is the biggest RH-adjacent advance since 1940.

## 5. Guth, "Large value estimates in number theory, harmonic analysis, and computer science"
- **Who/when:** Larry Guth, arXiv 2503.07410, March 2025 (survey, likely for proceedings/ICM-adjacent volume).
- **Links:** https://arxiv.org/abs/2503.07410
- **Local file:** `Guth-2025-large-value-survey.pdf` (~30 pp.)
- **Summary:** Guth's own survey connecting the GM large-values problem to restriction/Kakeya-type questions in harmonic analysis and to problems in theoretical computer science, laying out what he sees as the structural obstacles to pushing the exponents further (toward the Density Hypothesis, which would give exponent 2).
- **Status/reception:** Expository; valued as a roadmap by the community.
- **RH significance:** States the open problems whose solutions would be the next steps toward the Density Hypothesis — the realistic medium-term milestone short of RH itself.

## 6. Ecosystem of Guth–Maynard follow-ups (2024–2026, bundled entry)
- **Who/when/links:** among the ~40 citing works:
  - Le Duc Hieu, "Arithmetic progressions of primes in short intervals beyond the 17/30 barrier," arXiv 2509.04883 (Sept 2025) — pushes AP-in-short-interval results past the GM exponent.
  - Chourasiya–Simonič, "An explicit form of Ingham's zero density estimate," arXiv 2507.15184 (July 2025); Starichkova, arXiv 2411.01845; Chourasiya, "An explicit version of Carlson's theorem," arXiv 2412.02068 — the *explicit/effective* wing catching up with the qualitative theory.
  - Michael Harm, "Refinements for primes in short arithmetic progressions," arXiv 2507.15334 (2025) — GM twisted by characters, hybrid ranges.
  - Dong–Song–Wang–Zhang–Zhao, "Large values of Dirichlet polynomials with multiplicative coefficients," arXiv 2509.09771 (Sept 2025).
- **Local file:** none (bundled; anchor papers above suffice).
- **Summary:** A rapidly forming subfield: extending GM to character twists, making it explicit, and harvesting arithmetic corollaries (Goldbach in progressions, Piatetski-Shapiro primes in short intervals, Diophantine approximation with primes, smooth numbers).
- **Status/reception:** Mixed maturity, all serious; none yet improves the core 30/13 exponent for ζ itself — that number has held since May 2024.
- **RH significance:** Breadth of uptake is itself the story: GM created a genuinely new lever on the critical strip and the community is systematically pulling it.

## 7. Connes–Consani–Moscovici, "Zeta Spectral Triples"
- **Who/when:** Alain Connes, Caterina Consani, Henri Moscovici, arXiv 2511.22755, November 2025.
- **Links:** https://arxiv.org/abs/2511.22755
- **Local file:** `Connes-2025-zeta-spectral-triples.pdf`
- **Summary:** Proposes a concrete strategy toward RH via spectral realization: self-adjoint operators built as rank-one perturbations of the spectral triple of the scaling operator on [λ^{-1}, λ], constructed *only* from Euler products over primes p ≤ λ². Their spectra match the low nontrivial zeros of ζ(1/2+is) with striking numerical accuracy even for small cutoffs. Builds on "Spectral triples and zeta-cycles" (Enseign. Math. 2023; arXiv 2106.01715) and the 2025 Comm. Math. Phys. extension of Carathéodory–Fejér theory ("Quadratic Forms, Real Zeros and Echoes of the Spectral Action").
- **Status/reception:** Preprint; the numerics are impressive and the framework is taken seriously as the modern incarnation of Hilbert–Pólya, but convergence of the finite-prime approximations to the full spectrum is exactly the unproven step.
- **RH significance:** This — with item 9 — is the closest thing to an active, articulated *proof program* for RH itself currently running: realize the zeros as spectrum of operators built from finitely many primes, then prove convergence.

## 8. Connes–Consani–Moscovici, "Zeta zeros and prolate wave operators"
- **Who/when:** arXiv 2310.18423, October 2023 (v2 May 2024); published in J. Operator Theory / related venue.
- **Links:** https://arxiv.org/abs/2310.18423
- **Local file:** `Connes-2023-prolate-wave-operators.pdf` (30 pp.)
- **Summary:** Integrates two discoveries into the semilocal trace-formula framework: the ultraviolet spectrum of the prolate spheroidal wave operator (suitably extended to a self-adjoint operator on L²) matches the squares of the zeta zeros, and a semilocal analogue of the prolate operator ties this to the adele class space. The prolate operator — a differential operator commuting with the truncated Fourier transform — supplies the "cutoff" geometry that the Hilbert–Pólya dream always lacked.
- **Status/reception:** Published, mainstream-visible (PNAS precursors 2021–2022); regarded as genuine structural insight though far from a proof.
- **RH significance:** Supplies the missing candidate operator family in the spectral approach; the positivity required (Weil positivity) is reformulated as properties of these operators.

## 9. Connes solo, "The Riemann Hypothesis: Past, Present and a Letter Through Time"
- **Who/when:** Alain Connes, arXiv 2602.04022, **February 2026**.
- **Links:** https://arxiv.org/abs/2602.04022
- **Local file:** `Connes-2026-letter-through-time.pdf` (42 pp.)
- **Summary:** A commissioned survey of 165 years of RH work — classical analytic, geometric (Weil/Deligne), physical/spectral — that also contains an original contribution framed as a "Letter to Riemann" written using only mathematics available in Riemann's time: extremizing (a restriction of) Weil's quadratic form produces approximations to the zeros which provably lie exactly on the critical line, with a proposed route to RH via convergence of these finite-rank approximations (finite Euler products → full zeta). Effectively the human-readable companion to item 7.
- **Status/reception:** New; already picked up citations within months; the survey part is authoritative, the strategy part is a program, not a proof.
- **RH significance:** The clearest statement in print of what the noncommutative-geometry school believes the proof of RH will look like: Weil positivity + spectral realization + a convergence theorem.

## 10. Connes–Consani, the Riemann–Roch program on Spec Z (2022–2026)
- **Who/when/links:** the arc runs: "Riemann–Roch for Spec Z-bar" (arXiv 2205.01391, 2022) → "Riemann–Roch for the ring Z" (arXiv 2306.00456; C. R. Acad. Sci. 2024) → "Knots, primes and the adele class space" (2401.08401) and "Knots, primes and class field theory" (2501.06560, Jan 2025) → **"On the Jacobian of Spec Z-bar" (arXiv 2602.15941, Feb 2026)** → **"On the Absolute Geometry of Spec Z" (arXiv 2606.06604, June 2026)**.
- **Local files:** `Connes-2026-jacobian-speczbar.pdf`, `Connes-2026-absolute-geometry-specz.pdf`
- **Summary:** The "Riemann–Roch strategy": build enough genuine geometry over the absolute base F₁ so that Weil's 1940s function-field proof of RH (via Riemann–Roch on the square of the curve) can be imitated for Spec Z. The 2026 Jacobian paper interprets the adele class space (specifically its "Riemann sector") as the Picard/Jacobian of the arithmetic curve Spec Z-bar, with elements realized as rank-1 torsion-free abelian groups with rigidifying data extending Arakelov metrized line bundles. The June 2026 "Absolute Geometry" paper constructs (Spec Z)_{F₁} by pulling back the F₁-structure sheaf of the arithmetic site, and connects it to Scholze-style p-adic geometry: points over perfectoid fields classified by untilts — an explicit bridge between the F₁/topos program and modern p-adic Hodge theory.
- **Status/reception:** Steady, serious output; a small expert audience follows closely; no claim that the Weil-proof imitation is near completion — key ingredients (a genuine intersection theory on the "square", the analogue of Serre duality) remain open.
- **RH significance:** The only active program attacking RH by the route that actually *worked* in the one setting where RH is a theorem (function fields). The 2026 papers show real technical consolidation (Jacobian, Picard, Riemann–Roch inequalities now exist in some form over F₁), and the new perfectoid connection could bring fresh manpower.

## 11. Yitang Zhang, "Discrete mean estimates and the Landau–Siegel zero" — status as of mid-2026
- **Who/when:** Yitang Zhang, arXiv 2211.02515, November 2022.
- **Links:** https://arxiv.org/abs/2211.02515
- **Local file:** `Zhang-2022-landau-siegel.pdf` (111 pp.)
- **Summary:** Claims L(1,χ) ≫ (log D)^{-2022} for real primitive characters — far weaker than "no Siegel zeros" but vastly stronger than anything provable by known methods, and enough to make Siegel-zero constants effective. Status nearly four years on: **still v1 on arXiv; no revision; not published; not accepted by the community.** Experts identified concrete problems in the manuscript (issues in the key discrete-mean computations were discussed publicly in 2022–2023); Zhang has not produced a corrected version, and by 2024–2026 expert engagement had effectively ended without validation. Prediction-market/community consensus treats the proof as incomplete.
- **Status/reception:** Unresolved-negative. Not retracted, but no expert currently vouches for it.
- **RH significance:** Landau–Siegel is the "dark twin" of RH (a Siegel zero is the one hypothetical violation of GRH with the most dramatic consequences). Had the paper held up it would have been the largest GRH-adjacent event of the decade; as of mid-2026 it is a cautionary tale rather than a result.

## 12. Jensen polynomials / Jensen–Pólya program after Griffin–Ono–Rolen–Zagier
- **Who/when/links:** GORZ, "Jensen polynomials for the Riemann zeta function and suitable arithmetic sequences," PNAS 2019 (arXiv 1902.07321) — hyperbolicity of J^{d,n} for all d ≤ 8 and all d for n large. Follow-ups: Griffin–Ono–Rolen–Thorner–Tripp–Wagner, "Jensen polynomials for the Riemann xi-function," Adv. Math. 2022 (effective n(d)); Ono et al.'s "Jensen–Pólya program for various L-functions"; Bal–Haraldson–Males–Thompson-type work on Wright's circle method, e.g. arXiv 2301.02492, published in Integers 25 (2025); connections to finite free probability, e.g. arXiv 2410.06403 (universality for roots of derivatives of entire functions, 2024).
- **Local file:** `Bal-2023-jensen-wright-circle.pdf` (representative of the 2023–2025 wave).
- **Summary:** The 2019 result (density-1 hyperbolicity, low-degree cases, GUE random-matrix limit of the renormalized Jensen polynomials) spawned a durable industry, but the post-2022 momentum has flowed toward partition-type sequences, Turán inequalities, and free-probability universality rather than toward closing the gap for ζ itself. Nobody has extended "all n" hyperbolicity beyond small degree ranges in a way that approaches RH; the GUE-limit phenomenon is now understood as fairly universal (hence less specifically "about" RH).
- **Status/reception:** Established, refereed line of work; consensus that it is beautiful evidence-for-RH machinery but structurally unable, in current form, to reach RH (hyperbolicity of *all* Jensen polynomials is needed, and the asymptotic method inherently loses finitely many n per degree).
- **RH significance:** Confirms RH-consistent behavior in yet another direction (Turán/Laguerre inequalities to high degree) — evidence, not pathway, and the community now largely says so explicitly.

## 13. Goldston–Suriajaya, pair correlation without RH: "Zeta Zeros on the Critical Line" and the Pair Correlation series
- **Who/when:** Daniel A. Goldston and Ade Irma Suriajaya (+ collaborators), "Pair Correlation of Zeros I: Proportions of Simple Zeros and Critical Zeros," arXiv 2501.14545 (Jan 2025), and the expository/synthesis note "Zeta Zeros on the Critical Line," arXiv 2511.20059 (Nov 2025).
- **Links:** https://arxiv.org/abs/2511.20059 , https://arxiv.org/abs/2501.14545
- **Local file:** `Goldston-2025-zeta-zeros-critical-line.pdf`
- **Summary:** Montgomery's 1973 pair-correlation method assumed RH. This series shows what survives when RH is weakened or removed: e.g., assuming only that zeros lie in a narrow box around the critical line, pair correlation yields ≥ 67.25% of zeros on the line and ≥ 34.5% simple-and-on-the-line; under hypotheses weaker than RH, ≥ 61.7% simple. The 2511 note shows that removing RH from Montgomery's simple-zeros argument would automatically also prove 2/3 of zeros are on the critical line.
- **Status/reception:** Serious, incremental, refereed-track work by established authors; unconditional records (41.7% on the line, Pratt–Robles–Zaharescu–Zeindler 2020) remain unbeaten.
- **RH significance:** Maps precisely which "percentage" statements are within reach of de-conditionalized pair correlation — one of the few live routes to improving the 41.7% record.

## 14. Trudgian–Yang, "Toward optimal exponent pairs" and the explicit-zeta ecosystem
- **Who/when:** Tim Trudgian, Andrew Yang, arXiv 2306.05599 (2023, v3), published; plus the surrounding explicit-estimates literature.
- **Links:** https://arxiv.org/abs/2306.05599
- **Local file:** `Trudgian-2023-exponent-pairs.pdf` (38 pp.)
- **Summary:** Systematizes all known exponent pairs and optimizes over them computationally, improving bounds for ζ in the critical strip, moments on the critical line, and divisor problems. Emblematic of a 2020s trend: turning the sprawling exponent-pair/van der Corput literature into a machine-searchable database (also the seed of the ANTEDB — Analytic Number Theory Exponent Database — effort of Tao, Trudgian, Yang, 2024–2025).
- **Status/reception:** Published, widely used as a reference for current record exponents.
- **RH significance:** Infrastructure: the subconvexity/growth exponents for ζ(1/2+it) feed directly into zero-density and verification work; the database mindset is what made the GM aftermath propagate so quickly.

## 15. Formalization: PNT+ project, "Formalizing zeta and L-functions in Lean," and Tao's explicit-ANT network
- **Who/when/links:**
  - PrimeNumberTheoremAnd (Kontorovich–Tao, launched Jan 2024): PNT formalized in Lean 4 via Wiener–Ikehara in 2024; goals include PNT with classical error term and PNT in arithmetic progressions / Chebotarev. https://github.com/AlexKontorovich/PrimeNumberTheoremAnd
  - Loeffler–Stoll (et al.), "Formalizing zeta and L-functions in Lean," arXiv 2503.00959, published in Annals of Formalized Mathematics 1 (2025): Mathlib now contains ζ, Dirichlet L-functions, analytic continuation, functional equation, nonvanishing on Re s = 1 — i.e., **the statement of RH is now a first-class formal object in Mathlib**.
  - Tao's "integrated explicit analytic number theory network" (2025–2026): crowdsourced formalization of explicit ANT results (Fiori–Kadiri–Swidinsky explicit PNT etc.), partially hosted inside PNT+; Simons Foundation coverage June 2026.
- **Local file:** `Loeffler-2025-zeta-L-functions-lean.pdf`
- **Summary:** In two years analytic number theory went from nearly-unformalizble folklore to: PNT done, zeta/L-function library in Mathlib, error-term and progressions work in flight, and a professional pipeline (blueprints + AI assistance) for explicit estimates. Tao has repeatedly flagged this as the substrate for future large-scale collaborative ANT.
- **Status/reception:** All verified-by-construction (Lean); mainstream, growing fast.
- **RH significance:** Nobody is formalizing a proof of RH (there isn't one), but the entire scaffolding a future proof would need — and the tools to *check* a controversial 100-page claimed proof, Zhang-style — now exists. This changes how the endgame of any future RH claim would play out.

## 16. AI-assisted mathematics touching RH (2024–2026)
- **Who/when/links:**
  - AlphaProof (DeepMind): IMO silver 2024; Nature paper "Olympiad-level formal mathematical reasoning with RL," Nov 2025 (s41586-025-09833-y). Gemini Deep Think: IMO gold-level, 2025.
  - **Math, Inc. "Gauss" agent (Szegedy et al., Sept 2025): autonomously completed the Kontorovich–Tao *Strong* Prime Number Theorem formalization (PNT with classical error term, requiring the zero-free region machinery) in ~3 weeks — a task where human experts had ~18 months of partial progress; ~25k lines of Lean, ~1.1k theorems.** https://www.math.inc/gauss
  - DeepMind "Formal Conjectures" benchmark (arXiv 2605.13171, 2026): open-source Lean formalizations of open problems including RH variants, as an autoformalization/verification benchmark.
  - Early 2026: cluster of Erdős problems closed with AI involvement (Lean-verified); Tao publicly noting AI now completes formalization tasks in hours.
  - Noise item: a Grok-3 "proved RH" social-media flap (Feb 2025) — false alarm, no mathematical content.
- **Local file:** none (announcements/benchmarks, not papers about RH).
- **Summary:** No AI system has produced anything resembling progress on RH itself, and expert consensus is that RH is far beyond current systems. What HAS happened: AI became a serious *formalization* workhorse on RH-adjacent material (strong PNT), and RH is now a standard formal benchmark statement.
- **Status/reception:** Formalization achievements are machine-verified, hence solid; all "AI proves RH" claims to date are noise.
- **RH significance:** Changes the tooling landscape, not the mathematics. Realistic near-term role: verifying explicit ANT at scale and stress-testing claimed proofs.

## 17. Claimed proofs 2023–2026: status honest assessment
- **Summary:** No claimed proof of RH in 2023–2026 has received genuine positive expert engagement. The steady stream of Zenodo/SSRN/viXra/ResearchGate claims (e.g., the SSRN and figshare "definitive proof" items surfacing in 2025 searches, the self-documented "chronology" datasets on Mendeley) has attracted zero mathematical uptake. Nothing at the level of even the Atiyah 2018 episode (a famous mathematician forcing a public expert response) has occurred in this window. The de Branges program remains in its decades-long limbo without new expert review.
- **RH significance:** Nil; recorded here so the orchestrator knows the absence is a checked fact, not an omission.

## 18. Computational verification: no new rigorous record since 2020
- **Who/when/links:** Platt–Trudgian, "The Riemann hypothesis is true up to 3·10^12," arXiv 2004.09765, Bull. LMS 2021 — still the rigorous record (12,363,153,437,138 zeros, all on the line, all simple, verified with interval arithmetic). Gourdon–Demichel's 10^13 (2004) remains the larger but non-rigorous computation.
- **Local file:** none (predates window; the fact of "no successor" is the finding).
- **Summary:** Extensive searching (2024–2026) finds no published successor to Platt–Trudgian; claims of "20 trillion zeros" circulating on aggregator sites are traceable to non-rigorous computations or to sloppy summaries, not to a new refereed verification. Effort has shifted from raising the height to *using* verified heights in explicit estimates (Chourasiya–Simonič, explicit Carlson/Ingham, ANTEDB), where a verified height enters as a hypothesis.
- **RH significance:** The empirical frontier is static and was never going to decide RH; its real function today is as input to explicit zero-free regions and explicit PNT error terms.

## 19. Books and surveys 2023–2026
- **Who/when/links:**
  - Kevin Broughan, *Equivalents of the Riemann Hypothesis, Vol. 3: Further Steps towards Resolving the Riemann Hypothesis*, Cambridge Univ. Press (Encyclopedia of Mathematics 187), 2023 — covers Nicolas, Rodgers–Tao (Λ ≥ 0), Dobner, Polymath15, Matiyasevich; includes decidability-flavored material.
  - Connes' 2026 survey (item 9) — currently the best single state-of-the-art overview.
  - Turnage-Butterbaugh 2026 (item 4) — best entry point for the zero-density story.
  - Guth's 2025 survey (item 5) and Goldston–Suriajaya 2025 (item 13) — specialist surveys.
  - MDPI Symmetry "A Brief Survey on the RH and Some Attempts to Prove It" (Feb 2025) — exists; low-tier venue; use with caution.
- **Local files:** covered under items 4, 5, 9, 13.
- **RH significance:** The survey literature has visibly reorganized around two poles: the GM/zero-density pole and the Connes spectral/F₁ pole — an accurate map of where the field thinks the action is.

---

## The frontier as of mid-2026

Two directions own the momentum. The first is the **Guth–Maynard axis**: a genuinely new technique (large-value estimates via additive structure and matrix/eigenvalue analysis) that broke an 84-year-old barrier and, in the two years since, has been extended to Dirichlet L-function families (Chen's 7/3), made explicit (Chourasiya–Simonič and the ANTEDB/explicit-ANT ecosystem), and systematically harvested for prime-distribution corollaries (Gafni–Tao, short-interval APs past 17/30, Goldbach in progressions). Notably, the core exponent 30/13 for ζ has *not* moved since May 2024 — the current phase is consolidation and transplantation, with the Density Hypothesis (exponent 2) as the openly stated next target; Guth's 2025 survey frames the obstructions in harmonic-analysis terms, which is where a further breakthrough would likely come from. On the classical side more broadly, the percentage-of-zeros records are being attacked by de-conditionalizing pair correlation (Goldston–Suriajaya), and everything explicit is being databased and, increasingly, formalized. Landau–Siegel, by contrast, is stalled: Zhang's 2022 claim never recovered from the problems experts found, and as of mid-2026 no one vouches for it.

The second pole is the **Connes(–Consani–Moscovici) program**, which in 2025–2026 has been unusually productive and unusually concrete: zeta spectral triples whose finite-Euler-product operators numerically reproduce the low zeros (Nov 2025), the "Letter to Riemann" survey articulating the full strategy — Weil positivity + spectral realization + convergence of finite-prime approximations (Feb 2026) — and the F₁-geometry arc reaching the Jacobian of Spec Z-bar (Feb 2026) and a perfectoid/untilt bridge to Scholze-style p-adic geometry (June 2026). It remains a program with a well-identified missing theorem (convergence / positivity in the limit), but it is the only articulated end-to-end route to RH itself currently being executed, and its new contact with p-adic Hodge theory is the most plausible source of an influx of new techniques and people. Meanwhile, the quiet structural change of the period is the formalization/AI layer: RH is now a formal Mathlib statement, strong PNT was autoformalized by an AI agent in weeks, and Tao's explicit-ANT network is turning the field's numerical backbone into verified, reusable infrastructure — none of which proves RH, but all of which changes how the next serious claim, human or machine, will be vetted. Realistic near-term milestones to watch: any improvement of 30/13 or a density-hypothesis-range result; a proof of convergence in the zeta-spectral-triple construction; a revived, corrected Landau–Siegel manuscript; and the first fully formalized zero-density theorem.

---

## 20. [ADDED 2026-08-11] Claude (Anthropic), "More than two thirds of the zeros of the Riemann zeta function lie on the critical line"
- **Who/when:** Claude (a large language model, Anthropic, San Francisco), announced 2026-08-10 with research page anthropic.com/research/riemann-zeta; result found in interactive sessions with Jarred Sumner; studied/communicated by Ralph Furman and Levent Alpöge; read by Brian Conrey and Dan Goldston.
- **Links:** paper + informal note + explanation appendix + process transcripts on Anthropic's CDN; Lean 4 formalization github.com/anthropics/zeta-23-lean (tag v1.0, sorry-free, axiom-audited).
- **Local files:** `Claude-Anthropic-2026-two-thirds-critical-line.pdf`, `-informal-note.pdf`, `-explanation-appendix.pdf`, `-process-transcripts.pdf`.
- **Summary:** Unconditionally: ≥ 2/3 of zeta zeros are on the critical line (lim inf, dyadic windows), ≥ 2/3 simple-and-on-line, ≥ 5/6 distinct; 0.6725/0.6725/0.83625 with the optimal (Montgomery–Taylor) window; analogues for every fixed primitive Dirichlet L-function; ≥ 85.8% of ξ′ zeros simple-and-on-line. Method: compress Weil's Hermitian form onto a Gabor family at critical density over [T,2T] (window support L = λ log(T/2π), λ ≤ 1); zero side = Sylvester inertia (off-line pair ⇒ signature (1,1) block) + a rank–trace inequality via von Neumann's trace inequality (matrix analogue of m² ≥ 2m−1, m² ≥ 3m−2); prime side = Montgomery's first/second pair-correlation moments, unconditional at bandwidth ≤ 1 (BGSTB 2024 + Montgomery–Vaughan). Replaces RH's only role in Montgomery's argument (reading the zero side termwise by sign) with coordinate-free linear algebra. Method ceiling proved: 0.68185 from bandwidth-one data.
- **Status/reception:** Lean-certified statements (no hypotheses, standard axioms only); endorsed by the named human experts; previous record 5/12 (PRZZ 2020) via Levinson — this is the largest single advance in the statistic's history and the first non-Levinson record since 1942.
- **RH significance:** None directly (their own §1.5: insensitive to o(N) off-line zeros; Davenport–Heilbronn-proof). Structurally large: it validates finite-compression + exact-linear-algebra extraction over new-analytic-input acquisition, moves the Lead-6 frontier to "unconditional pair correlation beyond bandwidth 1", and confirms this archive's "counts, never excludes" wall from the counting side. Full adjudication: `UPDATES.md`.
