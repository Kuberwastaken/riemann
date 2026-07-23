# Classical Analytic Number Theory Progress toward RH

Unconditional partial results that "march toward" the Riemann Hypothesis, organized by
line of attack. Local PDFs live in `papers/analytic-progress/`. Compiled 2026-07-23.

Abbreviations: N(T) = number of nontrivial zeros with 0 < t ≤ T; N_0(T) = those on the
critical line; N(σ,T) = zeros with real part ≥ σ, height ≤ T.

---

## 1. Zeros on the critical line (Hardy → Selberg → Levinson → Conrey → PRZZ)

### Sur les zéros de la fonction ζ(s) de Riemann — G. H. Hardy, 1914, C. R. Acad. Sci. Paris 158, 1012–1014
- Link: volume digitized by Gallica (BnF), Comptes Rendus t. 158 (1914); no stable per-article file.
- Local file: not downloaded (public-domain scan only inside full-volume images).
- The first qualitative result in this direction: infinitely many zeros of ζ lie exactly on
  the line Re(s) = 1/2. Hardy integrates the real-valued Hardy function Z(t) against the
  theta/xi machinery and shows Z(t) changes sign infinitely often. Before this, not a single
  zero had been *proved* to lie on the line (Gram had only computed some numerically).
- Status: bedrock classic; superseded quantitatively by everything below.
- RH-reach: none by itself — "infinitely many" is measure zero of all zeros. Its importance
  is methodological: detecting sign changes of Z(t) via moments is still how all
  critical-line results work.

### The zeros of Riemann's zeta-function on the critical line — G. H. Hardy & J. E. Littlewood, 1921, Mathematische Zeitschrift 10, 283–317
- Links: https://eudml.org/journal/10148 (Math. Z. on GDZ/EuDML); DOI 10.1007/BF01211614
- Local file: `Hardy-Littlewood-1921-critical-line.pdf` (GDZ scan)
- Quantifies Hardy 1914: N_0(T) > cT for some c > 0, by counting sign changes of Z(t) in
  short windows using approximate functional equation techniques. Since N(T) ~ (T/2π)log T,
  this is still a vanishing *proportion* (~1/log T) of all zeros.
- Status: classic, superseded by Selberg.
- RH-reach: the T vs T log T gap illustrates the recurring pattern of this whole line:
  each new idea buys a bounded factor, never the full count.

### On the zeros of Riemann's zeta-function — A. Selberg, 1942, Skr. Norske Vid. Akad. Oslo I, no. 10, 59 pp.
- Link: no free digitization found; reprinted in Selberg's Collected Papers vol. I (Springer).
- Local file: not downloaded (paywalled/print only).
- The first *positive proportion* result: N_0(T) ≫ T log T. Selberg's key invention is the
  mollifier — a short Dirichlet polynomial that damps the wild oscillations of ζ so that
  moments of the mollified Z(t) detect sign changes at a positive density of scales.
- Status: classic; the mollifier idea is the engine of every later record.
- RH-reach: Selberg's proportion was tiny (he never computed it; estimates put it far below
  1%). The method proves κ > 0, but nothing in it pushes κ toward 1 — the mollifier can
  only be taken so long before its own error terms swamp the main term, and that length
  barrier is exactly what all successors fight over.

### More than one third of zeros of Riemann's zeta-function are on σ = 1/2 — N. Levinson, 1974, Advances in Mathematics 13, 383–436
- Links: https://doi.org/10.1016/0001-8708(74)90074-7 ;
  free scan: https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Levinson.pdf
- Local file: `Levinson-1974-one-third.pdf`
- A completely different route to a large proportion: instead of counting sign changes
  directly, Levinson relates zeros of ζ on the line to zeros of a mollified combination of ζ
  and ζ′ and reduces everything to an asymptotic for a mollified second moment, which he
  evaluates. Result: κ ≥ 1/3 (more precisely ~34%). The link to ζ′ rests on the
  Levinson–Montgomery/Speiser circle of ideas (see §8).
- Status: classic; the "Levinson method" is still the framework of the current record.
- RH-reach: intrinsically capped. The proportion obtained is a decreasing function of how
  long a mollifier one can control in the twisted second moment; with mollifier length
  θ < 1/2 one gets ~1/3. Reaching κ → 1 would need θ → ∞ (Farmer's conjecture), far beyond
  any known or plausible mean-value technology.

### More than two fifths of the zeros of the Riemann zeta function are on the critical line — J. B. Conrey, 1989, J. reine angew. Math. (Crelle) 399, 1–26
- Links: https://doi.org/10.1515/crll.1989.399.1 ; https://eudml.org/doc/153151
- Local file: `Conrey-1989-two-fifths.pdf` (GDZ scan of Crelle 399)
- Conrey pushes the mollifier length to θ = 4/7 by invoking the Deshouillers–Iwaniec
  estimates for averages of Kloosterman sums (spectral theory of automorphic forms), and
  gets κ ≥ 2/5 (in fact 40.77%, and ~19% simple zeros via the same machinery at the time).
  This stood as the record for over 20 years.
- Status: classic; still the last big *conceptual* jump in the constant (new input: automorphic
  spectral estimates).
- RH-reach: the jump 1/3 → 2/5 consumed the full strength of Deshouillers–Iwaniec.
  Enlarging θ beyond 4/7 for the needed twisted moments is tied to progress on Kloosterman/
  incomplete-sum estimates that has not materialized in 35+ years. Nothing suggests the
  route continues to 1/2, let alone 1.

### More than 41% of the zeros of the zeta function are on the critical line — H. M. Bui, J. B. Conrey, M. P. Young, 2011, Acta Arithmetica 150, 35–64
- Links: https://arxiv.org/abs/1002.4127
- Local file: `Bui-Conrey-Young-2010-41percent.pdf`
- Refines Conrey's setup with a two-piece mollifier (the second piece built from ζ·(a
  Dirichlet polynomial)), pushing κ ≥ 0.4105 and κ_simple ≥ 0.4058. Most of the gain comes
  from optimizing the shape of the mollifier rather than from new arithmetic input.
- Status: published; superseded by Feng and PRZZ.
- RH-reach: emblematic of the post-1989 regime — years of work for fractions of a percent.
  The marginal return per unit of mollifier complexity is sharply decreasing.

### Zeros of the Riemann zeta function on the critical line — S. Feng, 2012, J. Number Theory 132, 511–542
- Links: https://arxiv.org/abs/1003.0059
- Local file: `Feng-2010-zeros-critical-line.pdf`
- Introduces mollifiers whose coefficients involve Λ^{⋆k} convolution pieces, claiming
  κ ≥ 0.4128. Some intermediate steps in the published computation were later regarded as
  needing repair (see the discussion in Robles et al., arXiv:1403.5786, and in PRZZ); the
  PRZZ paper reworks and supersedes this line rigorously.
- Status: published, but partially patched by successors; superseded by PRZZ.
- RH-reach: same structural cap as all Levinson-type results (mollifier length barrier).

### More than five-twelfths of the zeros of ζ are on the critical line — K. Pratt, N. Robles, A. Zaharescu, D. Zeindler, 2020, Research in the Mathematical Sciences 7, art. 2 (arXiv 1802.10521)
- Links: https://arxiv.org/abs/1802.10521
- Local file: `Pratt-2018-five-twelfths.pdf`
- The current record: κ ≥ 5/12 ≈ 41.72% of zeros on the line, and ≥ 40.75% on the line and
  simple. Uses Feng-type Λ^{⋆k} mollifiers evaluated rigorously via
  ratios-of-zeta-functions technology (CFKRS), with heavy symbolic computation to optimize
  the many free parameters. Dedicated to the 30th anniversary of Conrey's 2/5 paper — a telling
  measure of the pace: ~1 percentage point in 30 years.
- Status: published; still the record as of mid-2026 (confirmed by Goldston–Suriajaya's
  Nov 2025 survey, which cites PRZZ as current best).
- RH-reach: essentially none beyond incremental percent-scale gains. Radziwiłł and others
  have quantified that with any mollifier of the currently reachable lengths, the Levinson
  approach provably cannot get near 100%; even crossing 50% ("most zeros on the line")
  appears to require a breakthrough on mollified moments equivalent to major progress on
  exponential sums. The method also cannot distinguish "on the line" from "very near the
  line" for the remaining ~58%.

### Pair correlation of zeros of the Riemann zeta function I: proportions of simple zeros and critical zeros — S. Baluyot, D. A. Goldston, A. I. Suriajaya, C. L. Turnage-Butterbaugh, 2025 (arXiv 2501.14545)
- Links: https://arxiv.org/abs/2501.14545
- Local file: `Baluyot-2025-pair-correlation-proportions.pdf`
- First use of Montgomery's pair-correlation method to control the *horizontal* distribution
  of zeros: assuming only that all zeros in [T,2T] lie in a box of width b/log T around the
  critical line (a hypothesis much weaker than RH), they recover Montgomery's "2/3 simple"
  and prove "2/3 on the critical line", plus an unconditional-flavored "1/3 simple and
  critical".
- Status: preprint (v2 Nov 2025); conditional on the narrow-box hypothesis, so not a new
  unconditional record — but a genuinely new mechanism for critical-line statements.
- RH-reach: interesting because it converts *vertical* statistics into *horizontal*
  information — a rare bridge. But its hypothesis (all zeros within o(1/log T) of the line)
  is itself far beyond anything provable today.

### Zeta zeros on the critical line — D. A. Goldston & A. I. Suriajaya, 2025–26 survey (arXiv 2511.20059)
- Links: https://arxiv.org/abs/2511.20059
- Local file: `Goldston-Suriajaya-2025-zeta-zeros-critical-line.pdf`
- Short survey/companion explaining how removing RH from Montgomery's pair-correlation
  argument would simultaneously give 2/3 of zeros simple *and on the line*; snapshots the
  state of the art (PRZZ 41.7%; Platt–Trudgian verification height) as of early 2026.
- Status: preprint; useful as a current-state reference.
- RH-reach: expository; underlines that the community views pair correlation, not more
  mollifier optimization, as the plausible next lever for the critical-line proportion.

---

## 2. Zero-density estimates (Ingham → Huxley → Bourgain → Guth–Maynard)

Density estimates bound N(σ,T) ≪ T^{A(σ)(1-σ)+o(1)}: RH says N(σ,T)=0 for σ>1/2; the
"density hypothesis" A(σ) ≤ 2 already gives many RH-grade consequences (e.g. primes in
intervals x^{1/2+ε}).

### On the estimation of N(σ,T) — A. E. Ingham, 1940, Quart. J. Math. Oxford 11
- Link: https://doi.org/10.1093/qmath/os-11.1.201 (paywalled)
- Local file: not downloaded.
- Proves N(σ,T) ≪ T^{3(1-σ)/(2-σ)} log^5 T. At σ=3/4 this gives exponent 3/5, which stood
  for 84 years until Guth–Maynard. Combined with the Vinogradov–Korobov region it yields
  the still-standard PNT in intervals of length x^{7/12+ε} (with Huxley's refinement).
- Status: classic; at σ = 3/4 unimproved from 1940 to 2024.
- RH-reach: zero-density is the "measure-theoretic RH": it shows exceptions to RH are rare,
  but by construction it can never show they are absent — the method counts large values of
  Dirichlet polynomials and always concedes a positive-exponent count.

### On the difference between consecutive primes — M. N. Huxley, 1972, Inventiones Math. 15, 164–170
- Link: https://eudml.org/doc/142137 ; DOI 10.1007/BF01418933
- Local file: not downloaded (paywalled; EuDML/GDZ scan exists).
- Establishes N(σ,T) ≪ T^{12(1-σ)/5+o(1)} uniformly (Halász–Montgomery large-value method),
  i.e. density exponent A ≤ 12/5 = 2.4, and deduces the PNT in intervals x^{7/12+ε}. Both the
  12/5 and the 7/12 were the benchmarks for 52 years.
- Status: classic; superseded by Guth–Maynard 2024.
- RH-reach: as with Ingham — the large-value machinery (mean values + Halász) hits a natural
  wall at the "N^{3/4} value, N=T^{4/5} length" configuration, precisely the case
  Guth–Maynard finally moved.

### Density hypothesis in restricted ranges — M. Jutila 1977 (σ ≥ 11/14); J. Bourgain 2000, "On large values estimates for Dirichlet polynomials and the density hypothesis for the Riemann zeta function", IMRN 2000:3, 133–146 (σ ≥ 25/32)
- Link: https://doi.org/10.1155/S1073792800000091 (paywalled)
- Local file: not downloaded.
- Bourgain proved the density hypothesis A(σ) ≤ 2 for σ ≥ 25/32 = 0.78125, improving
  Jutila's 11/14, by combining large-value estimates with bounds toward Lindelöf and
  ingredients from his ℓ^2-decoupling world.
- Status: published; ranges since improved via Guth–Maynard-era tooling (see ANTEDB).
- RH-reach: shows the density hypothesis itself is attackable in pieces, but the density
  hypothesis is strictly weaker than both Lindelöf and RH.

### New large value estimates for Dirichlet polynomials — L. Guth & J. Maynard, 2024, arXiv 2405.20552 (to appear/published, Annals of Mathematics, 2026)
- Links: https://arxiv.org/abs/2405.20552 ; Oxford abstract page
  https://www.maths.ox.ac.uk/node/67928
- Local file: `Guth-Maynard-2024-large-values.pdf`
- THE 2024 breakthrough. For the critical configuration (Dirichlet polynomial of length
  N = T^{4/5} taking values of size N^{3/4}), the number of large values improves from
  Montgomery/Huxley/Ingham's R ≤ T^{3/5+o(1)} to R ≤ T^{13/25+o(1)}. The proof converts the
  large-value problem into an additive-energy/Fourier problem about the matrix of phases
  n^{it_r}, then runs an iterative "raise-to-a-power and resample" argument blending
  harmonic analysis (Guth) with analytic number theory (Maynard). Consequences:
  N(σ,T) ≤ T^{15(1-σ)/(3+5σ)+o(1)}, hence the clean uniform bound
  N(σ,T) ≤ T^{30(1-σ)/13+o(1)} — density exponent 30/13 ≈ 2.31, first improvement over
  Huxley's 12/5 since 1972, and at σ=3/4 first improvement over Ingham since 1940. Downstream:
  asymptotic PNT in all intervals of length x^{17/30+ε} (beating Huxley's 7/12) and in
  almost all intervals of length x^{2/15+ε} (beating 1/6).
- Coverage: Quanta, "'Sensational' Proof Delivers New Insights Into Prime Numbers"
  (2024-07-15), https://www.quantamagazine.org/sensational-proof-delivers-new-insights-into-prime-numbers-20240715/ ;
  Science news piece
  https://www.science.org/content/article/sensational-breakthrough-marks-step-toward-revealing-hidden-structure-prime-numbers ;
  Tao's Mastodon threads https://mathstodon.xyz/@tao/112557248794707738 and
  .../112557249982780815 ("a remarkable breakthrough… though still very far from fully
  resolving this conjecture"); Tao's expository blog post "A computation-outsourced
  discussion of zero density theorems for the Riemann zeta function" (2024-07-07),
  https://terrytao.wordpress.com/2024/07/07/a-computation-outsourced-discussion-of-zero-density-theorems-for-the-riemann-zeta-function/
- Status: refereed (Annals); universally accepted; already spawning a follow-up literature
  (below).
- RH-reach: the most honest appraisal is Tao's — it improves the *exceptional set* bound,
  not the boundary. Even the full density hypothesis (A=2 everywhere), let alone 30/13,
  leaves N(σ,T) potentially of size T^{c} for every σ < 1: the method inherently counts
  rather than excludes. What it does change is the conversion rate between exponential-sum
  progress and prime-distribution consequences, and it broke a psychological 80-year
  stalemate.

### Large value estimates in number theory, harmonic analysis, and computer science — L. Guth, 2025 survey (arXiv 2503.07410)
- Links: https://arxiv.org/abs/2503.07410
- Local file: `Guth-2025-large-values-survey.pdf`
- Guth's own lecture-notes-style survey placing the Guth–Maynard theorem in the wider
  context of superlevel-set problems (restriction theory, Kakeya, communication complexity),
  with open problems and simplified proofs.
- Status: survey preprint (likely for proceedings).
- RH-reach: valuable as a map of which harmonic-analysis inputs might still improve
  large-value estimates; explicitly frames Montgomery's large-value conjecture (which would
  give the density hypothesis) as the target.

### New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach — T. Tao, T. Trudgian, A. Yang, 2025 (arXiv 2501.16779) + the ANTEDB
- Links: https://arxiv.org/abs/2501.16779 ; database https://github.com/teorth/expdb
- Local file: `Tao-Trudgian-Yang-2025-exponent-database.pdf`
- Builds the Analytic Number Theory Exponent Database and machine-optimizes the known web of
  implications, yielding four new exponent pairs, new zero-density estimates (improving the
  post-Guth–Maynard frontier in some σ-ranges), and new additive-energy bounds for zeta
  zeros. Effectively industrializes the bookkeeping Tao began in his July 2024 blog post.
- Status: preprint + living database; community-maintained.
- RH-reach: none directly, but it guarantees any future kernel improvement (a new exponent
  pair, a new large-value bound) instantly propagates to best-possible density/short-interval
  consequences. It also makes visible exactly where the current frontier is slack.

### Large value estimates for Dirichlet polynomials, and the density of zeros of Dirichlet's L-functions — Bin Chen, 2025 (arXiv 2507.08296)
- Links: https://arxiv.org/abs/2507.08296
- Local file: `Chen-2025-large-values-Dirichlet-L.pdf`
- Extends the Guth–Maynard method to the q-aspect: Σ_{χ mod q} N(σ,T,χ) ≲ (qT)^{7(1-σ)/3+ε},
  improving Huxley's 12/5 exponent for Dirichlet L-functions to 7/3, with applications to
  the least prime in arithmetic progressions to prime-power modulus and least Goldbach
  numbers in progressions.
- Status: preprint (July 2025).
- RH-reach: shows the GM technique transfers to families (GRH-flavored exceptional-set
  bounds); same structural ceiling as for ζ.

### Adjacent 2024–26 short-interval progress
- Runbo Li, "Primes in almost all short intervals" (arXiv 2407.05651, v6 2025) — local file
  `Li-2024-primes-almost-all-short-intervals.pdf`: sharpens Jia's sieve-based result to show
  almost all intervals [n, n+n^{1/21.5}] contain primes (existence, not asymptotics; Harman
  sieve + Watt mean values — a parallel track to GM's asymptotic x^{2/15}).
- Le Duc Hieu, "Arithmetic progressions of primes in short intervals beyond the 17/30
  barrier" (arXiv 2509.04883, 2025) — not downloaded: uses the GM zero-density bounds to get
  k-term APs of primes in [x, x+x^θ] for θ > 17/30.
- Status: preprints; illustrate how quickly 17/30 and 2/15 became the new baseline numbers.

---

## 3. Zero-free regions (de la Vallée Poussin → Vinogradov–Korobov → explicit records)

### Classical region — C. de la Vallée Poussin, 1899, Mém. Couronnés Acad. Roy. Belgique 59
- Link: public-domain; scans on archive.org (Mémoires couronnés series).
- Local file: not downloaded.
- ζ(σ+it) ≠ 0 for σ ≥ 1 − c/log t. This is what upgrades the PNT to the error term
  O(x exp(−c√(log x))). Structurally it comes from 3+4cos θ+cos 2θ ≥ 0 plus a bound for
  ζ near the 1-line.
- Status: classic; constant c repeatedly improved (see Mossinghoff–Trudgian line below).
- RH-reach: a 1/log t sliver where RH wants the whole strip σ > 1/2. No refinement of the
  trigonometric-polynomial trick can widen the *shape* of the region, only the constant.

### Vinogradov–Korobov region — I. M. Vinogradov and N. M. Korobov, 1958 (Izv. Akad. Nauk SSSR / Uspekhi Mat. Nauk)
- Modern treatment: K. Ford, "Vinogradov's integral and bounds for the Riemann zeta
  function", Proc. LMS 85 (2002) 565–633 (explicit constant 57.54).
- Local file: not downloaded (originals not freely digitized).
- Zero-free for σ ≥ 1 − c/((log t)^{2/3}(log log t)^{1/3}), via Vinogradov's method for
  exponential sums; gives the best-known PNT error O(x exp(−c(log x)^{3/5}(log log x)^{−1/5})).
  Unimproved in *shape* since 1958 — one of the most famous stuck constants in the subject.
- Status: still the asymptotic record, 68 years on.
- RH-reach: this is the strongest statement humanity can prove about where zeros are NOT,
  and it is still a region of vanishing width. The exponential-sum route (Vinogradov, then
  decoupling) has never produced a zero-free strip of positive width; getting ANY σ_0 < 1
  with no zeros to its right would already be a historic event ("quasi-RH") and is believed
  to need entirely new ideas.

### Nonnegative trigonometric polynomials and a zero-free region for the Riemann zeta-function — M. J. Mossinghoff & T. S. Trudgian, 2015, J. Number Theory 157, 329–349 (arXiv 1410.3926)
- Links: https://arxiv.org/abs/1410.3926
- Local file: `Mossinghoff-Trudgian-2014-zero-free.pdf`
- Optimizes the nonnegative trigonometric polynomial in de la Vallée Poussin's argument
  (LP/semidefinite optimization over polynomial families), proving no zeros for
  σ ≥ 1 − 1/(5.573412 log|t|), |t| ≥ 2 — for decades-scale heights this classical-shape
  region beats Vinogradov–Korobov.
- Status: published; superseded by MTY 2022 and BTY 2026.
- RH-reach: pure constant-chasing (important for explicit PNT applications, e.g. primality
  ranges and verification interfaces), no structural progress possible by design.

### Explicit zero-free regions for the Riemann zeta-function — M. J. Mossinghoff, T. S. Trudgian, A. Yang, 2024, Res. Number Theory (arXiv 2212.06867)
- Links: https://arxiv.org/abs/2212.06867
- Local file: `Mossinghoff-Trudgian-Yang-2022-explicit-zero-free.pdf`
- Sharpened the classical constant to 1/(5.558691 log|t|), plus the best explicit
  Vinogradov–Korobov-type and intermediate regions of its time; a one-stop reference for
  which region is widest at which height.
- Status: published; classical-type constant now superseded by BTY 2026.

### Explicit bounds for ζ and a new zero-free region — C. Bellotti, 2023–24 (arXiv 2306.10680)
- Links: https://arxiv.org/abs/2306.10680
- Local file: `Bellotti-2023-explicit-zeta-bounds-zero-free.pdf`
- Proves |ζ(σ+it)| ≤ 70.7|t|^{4.438(1−σ)^{3/2}} log^{2/3}|t| in the strip and deduces an
  explicit Vinogradov–Korobov zero-free region with constant 54.004 (48.07 asymptotically),
  improving Ford's 57.54; her companion work makes the VK region the widest known explicit
  region for t > exp(482036).
- Status: published (2024); current explicit VK record holder.
- RH-reach: brings the "asymptotically best" region into the explicitly usable range —
  matters for making Guth–Maynard-type consequences numerically effective, not for RH itself.

### Zero-free regions inspired by work of Heath-Brown — C. Bellotti, T. Trudgian, A. Yang, 2026 (arXiv 2603.21490)
- Links: https://arxiv.org/abs/2603.21490
- Local file: `Bellotti-Trudgian-Yang-2026-zero-free-Heath-Brown.pdf`
- March 2026: imports Heath-Brown's Linnik-constant machinery to prove ζ(σ+it) ≠ 0 for
  σ ≥ 1 − 1/(4.896 log t), t ≥ 3 — a substantial jump on the 5.5587 constant, the largest
  single improvement in the classical-shape region in decades (dedicated to Heath-Brown's
  "diamond jubilee").
- Status: new preprint from the group that owns this record; likely to hold.
- RH-reach: same as above — the frontier of *explicit* zero-free width is now ~1/(4.9 log t);
  RH is infinitely far beyond any such region.

---

## 4. The de Bruijn–Newman constant Λ (RH ⟺ Λ ≤ 0; now 0 ≤ Λ ≤ 0.2)

### Fourier transforms with only real zeros — C. M. Newman, 1976, Proc. AMS 61, 245–251
- Link: https://doi.org/10.1090/S0002-9939-1976-0434982-5 (AMS site; free access blocked to
  our fetcher, so citation only).
- Local file: not downloaded.
- Defines the heat-flow deformation H_t of the Riemann ξ-function; de Bruijn (1950) had
  shown H_t has only real zeros for t ≥ 1/2, and Newman shows some H_t has a non-real zero,
  defining Λ and conjecturing Λ ≥ 0: "the Riemann hypothesis, if true, is only barely so" —
  the universe should not have wiggle room to spare.
- Status: classic; conjecture proved by Rodgers–Tao 2018.
- RH-reach: reframes RH as the boundary case t = 0 of a dynamical statement, which is what
  makes both the lower and upper bound programs below possible.

### The de Bruijn–Newman constant is non-negative — B. Rodgers & T. Tao, 2020, Forum of Math, Pi 8, e6 (arXiv 1801.05914)
- Links: https://arxiv.org/abs/1801.05914 ; Tao's announcement post
  https://terrytao.wordpress.com/2018/01/19/the-de-bruijn-newman-constant-is-non-negative/
- Local file: `Rodgers-Tao-2018-dBN-nonnegative.pdf`
- Proves Newman's conjecture Λ ≥ 0. If Λ < 0, the zeros at time 0 would have had to relax
  (backwards heat flow) into an impossibly rigid "equilibrium" local configuration; but the
  known statistics of zeta zeros (from unconditional pair-correlation-type results plus
  numerics-free arguments) contradict that rigidity. Upgrades the earlier numerical lower
  bounds (Csordas–Odlyzko–Smith–Varga: Λ > −1.15×10^{-11}, from Lehmer pairs) to the sharp 0.
- Status: published, accepted.
- RH-reach: this is a *negative* result for RH-optimism in a precise sense — RH is
  equivalent to Λ ≤ 0, and now Λ ≥ 0 is a theorem, so RH ⟺ Λ = 0 exactly: there is no
  "soft landing" where RH holds with room to spare. Any proof of RH must be sharp against
  this obstruction; conversely a single Lehmer-type near-violation becoming an actual
  violation would disprove RH.

### Effective approximation of heat flow evolution of the Riemann ξ function, and a new upper bound for the de Bruijn–Newman constant — D. H. J. Polymath (Polymath15), 2019, Res. Math. Sci. 6 (arXiv 1904.12438)
- Links: https://arxiv.org/abs/1904.12438 ; project threads
  https://terrytao.wordpress.com/tag/polymath15/ ; wiki
  https://michaelnielsen.org/polymath1/index.php?title=De_Bruijn-Newman_constant
- Local file: `Polymath15-2019-dBN-upper-bound.pdf`
- Massively collaborative (Tao-led) project: rigorous effective approximations to H_t plus
  interval-arithmetic zero-tracking give Λ ≤ 0.22, crushing the previous best Λ < 1/2
  (de Bruijn 1950; strict inequality Ki–Kim–Lee 2009). The paper's Table 1 conditional rows
  convert any RH verification height into a Λ bound.
- Status: published. Combined with Platt–Trudgian's verification height 3·10^12, its own
  table yields the current record Λ ≤ 0.2 (stated as Corollary 2 in Platt–Trudgian).
- RH-reach: the upper bound can never reach 0 by this route — pushing Λ ≤ ε requires
  verifying RH to height roughly exp(C/ε), a doubly-losing exchange rate. The dBN program
  measures the gap to RH (currently the interval [0, 0.2]) more honestly than any other
  metric, and simultaneously proves that closing it needs a non-computational idea.

---

## 5. Lindelöf hypothesis progress (the "poor man's RH")

LH: ζ(1/2+it) ≪ t^ε, i.e. μ(1/2)=0. RH ⇒ LH; LH ⇒ density hypothesis and "almost RH"
statements (e.g. N(σ,T+1)−N(σ,T) = o(log T) for σ > 1/2, Backlund). It is the natural
"analytic shadow" of RH: about the size of ζ on the line rather than the location of zeros.

### History of μ(1/2): convexity 1/4 → Hardy–Littlewood/Weyl 1/6 → … → Bourgain 13/84
- Weyl-method bound μ(1/2) ≤ 1/6 ≈ 0.1667 (Hardy–Littlewood 1920s, via Weyl differencing);
  a century of exponent-pair grinding (van der Corput, Phillips, Titchmarsh, …, Huxley
  32/205 ≈ 0.15610 in 2005) shaved this by less than 0.011 in total.

### Decoupling, exponential sums and the Riemann zeta function — J. Bourgain, 2017, J. Amer. Math. Soc. 30, 205–224 (arXiv 1408.5794)
- Links: https://arxiv.org/abs/1408.5794
- Local file: `Bourgain-2014-decoupling-zeta.pdf`
- Applies Bourgain–Demeter ℓ^2-decoupling (2015 Annals) to the relevant exponential sums,
  proving ζ(1/2+it) ≪ t^{13/84+ε}, 13/84 ≈ 0.1548. Still the record as of mid-2026 (explicit
  versions of the weaker 1/6-type bounds exist, e.g. Patel–Yang, for computational use).
- Status: published; record.
- RH-reach: decoupling is sharp for the model problems it solves, so further gains need new
  arithmetic input, not better harmonic analysis of the same sums. The distance from 13/84
  to 0 dwarfs the distance travelled since 1921. Even full LH would not locate a single
  zero — it bounds all moments (Lindelöf ⟺ all even moments are T^{1+ε}) yet is compatible
  with zeros off the line arbitrarily close to s=1.

### Moments of ζ on the critical line
- 2nd moment: Hardy–Littlewood 1918 (asymptotic known).
- 4th moment: A. E. Ingham 1926 (Proc. LMS) main term T log^4 T/(2π²); D. R. Heath-Brown,
  "The fourth power moment of the Riemann zeta function", Proc. LMS (3) 38 (1979) 385–422 —
  full asymptotic expansion. Paywalled; citation only.
- 12th moment: Heath-Brown, Quart. J. Math. 29 (1978) 443–462: ∫|ζ(1/2+it)|^{12} ≪ T^{2+ε} —
  equivalent in strength to μ(1/2) ≤ 1/6 on average and a key ingredient in density work.
- No asymptotic is known for any moment beyond the 4th; the 6th and 8th are the concrete
  wall. CFKRS random-matrix predictions give the conjectural answers, but proofs are absent.
- RH-reach: LH is equivalent to bounding ALL even moments; being stuck at the 4th since
  1926 is the cleanest quantitative demonstration of where mean-value technology stops.

---

## 6. Computational verification (Turing → Odlyzko → Gourdon → Platt–Trudgian)

### Some calculations of the Riemann zeta-function — A. M. Turing, 1953, Proc. LMS (3) 3, 99–117; exposition: A. R. Booker, "Turing and the Riemann hypothesis", Notices AMS 53 (2006) 1208–1211
- Links: Turing paper https://doi.org/10.1112/plms/s3-3.1.99 (paywalled);
  Booker (free) https://www.ams.org/notices/200610/fea-booker.pdf
- Local file: `Booker-2006-Turing-RH.pdf` (Turing original: citation only)
- Turing ran the Manchester Mark 1 to check zeros up to t ≈ 1540 and, more importantly,
  invented Turing's method: using the average of the argument function S(t), one can certify
  that ALL zeros up to height T have been found on the line, without any computation off the
  line. Every subsequent verification rests on this.
- Status: classic; method still standard (with explicit error constants by Trudgian).
- RH-reach: verification can only ever fail to disprove RH; but Turing-certified heights are
  now load-bearing inputs to theorems (Λ ≤ 0.2; explicit PNT error bounds; ternary Goldbach).

### Odlyzko's large-height computations — A. M. Odlyzko, 1987–1992+
- "On the distribution of spacings between zeros of the zeta function", Math. Comp. 48
  (1987) 273–308 — local file `Odlyzko-1987-zero-spacings.pdf`.
- "The 10^20-th zero of the Riemann zeta function and 175 million of its neighbors" (1992,
  famously unpublished) — local file `Odlyzko-1992-10to20th-zero.pdf`. Author's page:
  https://www-users.cse.umn.edu/~odlyzko/
- Using the Odlyzko–Schönhage algorithm (multi-evaluation of ζ in T^{1/2+ε} time), computed
  hundreds of millions of zeros near heights 10^{20} (later 10^{21}, 10^{22}), verifying RH
  locally and matching GUE pair-correlation/spacing predictions to stunning accuracy — the
  empirical backbone of the random-matrix picture (Montgomery–Odlyzko law).
- Status: classic; the statistical evidence, more than the verification, changed the field.
- RH-reach: no finite computation approaches RH; but the GUE match is the strongest
  heuristic evidence both for RH and for the Hilbert–Pólya spectral dream.

### The 10^13 first zeros, and zeros at heights 10^24 — X. Gourdon (with P. Demichel), 2004
- Link: http://numbers.computation.free.fr/Constants/Miscellaneous/zetazeros1e13-1e24.pdf
- Local file: `Gourdon-2004-1e13-zeros.pdf`
- Verified RH for the first 10^13 zeros and sampled billions of zeros at heights up to
  10^{24} using an optimized Odlyzko–Schönhage implementation. Long the "record", though
  unpublished and (unlike Platt's work) not done in rigorous interval arithmetic.
- Status: accepted as heuristic record; superseded in rigor by Platt–Trudgian.

### The Riemann hypothesis is true up to 3·10^12 — D. Platt & T. Trudgian, 2021, Bull. LMS 53, 792–797 (arXiv 2004.09765)
- Links: https://arxiv.org/abs/2004.09765
- Local file: `Platt-Trudgian-2020-RH-3e12.pdf`
- The rigorous record: all 12,363,153,437,138 zeros with 0 < t ≤ 3,000,175,332,800 lie
  exactly on the critical line and are simple — computed with interval arithmetic end-to-end
  and Turing-method certification. Corollary 2: Λ ≤ 0.2 (via Polymath15's Table 1). Also
  feeds every modern explicit estimate (e.g. explicit PNT, Bellotti-type regions).
- Status: published; still the rigorous record as of mid-2026.
- RH-reach: none in principle (RH concerns all heights; known "law of small numbers"
  phenomena like Lehmer pairs and the slow growth of S(t) mean surprises could in theory
  appear far beyond any computable height) — but indispensable as a component of hybrid
  computational-analytic theorems.

---

## 7. Landau–Siegel zeros (Zhang 2022)

### Discrete mean estimates and the Landau-Siegel zero — Yitang Zhang, 2022 (arXiv 2211.02515)
- Links: https://arxiv.org/abs/2211.02515 ; Nature news
  https://www.nature.com/articles/d41586-022-03689-2
- Local file: `Zhang-2022-Landau-Siegel.pdf`
- Claims L(1,χ) ≫ (log D)^{-2022} for real primitive characters mod D (effectively
  computable constant) — equivalently, no Landau–Siegel zero closer to 1 than
  c(log D)^{-2024}-scale. This would be epochal: Siegel zeros are the great effective
  obstruction in multiplicative number theory (Siegel's 1935 bound is ineffective), and
  their nonexistence in this quantitative form would make huge swaths of the subject
  effective and settle exceptional-character pathologies. Note (as Nature's correction
  emphasized): even as claimed, it is a weakened form of the "no Siegel zeros" conjecture,
  not the full statement.
- Status as of mid-2026: NOT accepted. Experts identified serious problems in the 111-page
  manuscript within weeks (concentrated in the discrete-mean evaluations, §§8–15); Zhang has
  reportedly acknowledged issues; no revised version has ever been posted (v1 remains the
  only version on arXiv), no journal acceptance, and community trackers/prediction markets
  treat the claim as unproven. The result should be cited as an open claim, not a theorem.
- RH-reach: tangential but deep — Siegel zeros are "almost-counterexamples" to GRH on the
  real axis. Ironically, their *existence* would imply striking things (twin primes via
  Heath-Brown), and their nonexistence is a *consequence* of GRH; either resolution
  illuminates RH's neighborhood. Zhang's discrete-mean strategy, if ever repaired, targets
  only the real zero near s=1, not zeros on the critical strip's interior at height.

---

## 8. Speiser's theorem and ζ′ as proxy

### Geometrisches zur Riemannschen Zetafunktion — A. Speiser, 1935, Math. Ann. 110, 514–521
- Links: https://doi.org/10.1007/BF01448042 ; GDZ scan (downloaded)
- Local file: `Speiser-1935-geometrisches.pdf`
- Proves RH is equivalent to: ζ′(s) has no zeros in the open left half-strip 0 < σ < 1/2.
  A purely geometric/function-theoretic reformulation moving the problem from ζ to its
  derivative.
- Status: classic equivalence; the basis of the Levinson method's accounting.
- RH-reach: reformulation, not reduction — but it created a genuinely useful proxy (below).

### Zeros of the derivatives of the Riemann zeta-function — N. Levinson & H. L. Montgomery, 1974, Acta Mathematica 133, 49–65
- Links: https://doi.org/10.1007/BF02392141 ; free at Project Euclid (blocked to our
  fetcher): https://projecteuclid.org/journals/acta-mathematica/volume-133/issue-none/Zeros-of-the-derivatives-of-the-Riemann-zeta-function/10.1007/BF02392141.full
- Local file: not downloaded (Cloudflare-blocked; citation only).
- The quantitative Speiser theorem: ζ and ζ′ have (up to O(log T)) the same number of zeros
  with σ < 1/2 up to height T; more generally studies zeros of ζ^{(k)}. This is what lets
  Levinson count zeros of ζ on the line by controlling a mollified ζ + ζ′ combination, and
  it underlies later work on zeros of ζ′ clustering toward the line (Soundararajan, Ki,
  Suriajaya) and the Farmer–Ki program linking Siegel zeros to real zeros of ζ′ near 1
  (cf. arXiv 1002.1616).
- Status: classic, standard tool.
- RH-reach: proxy results inherit the limits of what feeds them; but "zeros of ζ′ left of
  the line" is one of the few RH-equivalent quantities for which partial unconditional
  results (density-type bounds) keep improving, so it remains a live indirect route.

---

## 9. Overall assessment

What the classical analytic program has actually achieved is a dense system of
*quantitative fences* around RH, none of which touches it. On the line itself, the
Hardy→Selberg→Levinson→Conrey→PRZZ chain took 106 years to go from "infinitely many" to
41.7%, and the machinery that produced each step is provably running out: Levinson-type
methods trade mollifier length for proportion at a known exchange rate, mollifier length is
capped by mean-value/Kloosterman technology frozen since Deshouillers–Iwaniec, and
structural analyses (Radziwiłł) show the current framework cannot approach 100% — probably
not even 50% — no matter how the parameters are tuned. Zero-free regions have not improved
in shape since Vinogradov–Korobov (1958); the 2022–26 flurry (Mossinghoff–Trudgian–Yang,
Bellotti, Bellotti–Trudgian–Yang's 1/(4.896 log t)) is constant-optimization, essential for
explicit consequences but not directionally different. Verification (Platt–Trudgian's
rigorous 3·10^12, Gourdon's 10^13, Odlyzko's height-10^{20+} samples) can never prove RH,
though it now functions as a theorem-grade input to hybrid results. The de Bruijn–Newman
program delivered the deepest structural message of the period: Rodgers–Tao's Λ ≥ 0 says RH,
if true, is *exactly* critical — a proof must be sharp, with no analytic slack — while
Polymath15's Λ ≤ 0.2 shows the computational route to the other side has an exponentially
bad exchange rate. Lindelöf progress (Bourgain's 13/84) measures the same wall from the
moment side: a century of exponential-sum refinement, decoupling included, has consumed
about 40% of the gap from 1/4 to the Weyl exponent and left the gap to 0 essentially intact,
with moments stuck at the 4th since 1926. Zhang's Landau–Siegel claim, which would at least
have removed RH's most notorious real-axis shadow, remains unaccepted and unrevised.

Guth–Maynard is the one genuine phase change in decades, and it is important to say
precisely what it changes. It does not move zeros onto the line, widen any zero-free
region, or improve Lindelöf; it improves the *census of hypothetical exceptions*, breaking
Ingham's 84-year-old σ=3/4 bound (T^{3/5} → T^{13/25}) and Huxley's 52-year-old density
exponent (12/5 → 30/13), with immediate downstream records (PNT in x^{17/30}, almost-all
intervals x^{2/15}, q-aspect analogues, and a now-systematized frontier via Tao–Trudgian–
Yang's exponent database). Its deeper significance is methodological: it shows the
large-values problem — the exact bottleneck between exponential sums and zero statistics —
is not frozen, and that imports from harmonic analysis (energy iteration, decoupling-adjacent
ideas) can still move number-theoretic walls that internal refinement could not. The sober
consensus, Tao's included, stands: these methods bound exceptions and can plausibly grind
toward the density hypothesis, but they count zeros rather than forbid them, so the step
from "exceptions are rare" to "exceptions are absent" — RH itself — is not reachable by any
currently visible refinement of this program. If RH falls to analysis at all, the likeliest
contributions of this line are (i) the density hypothesis as a way-station, (ii) the
Λ = 0 sharpness constraint as a filter on candidate proofs, and (iii) pair-correlation-to-
horizontal-distribution bridges (Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh) as the
first genuinely new lever on the critical-line proportion since Levinson.
