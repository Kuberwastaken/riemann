# The Riemann Hypothesis: every serious approach, and what could actually work

*Synthesis of the archive in `papers/` and `notes/` (178 primary sources, collected
2026-07-23). Each claim below is grounded in the annotated bibliographies; file paths
point at the primary sources.*

---

## 1. Executive summary

After 166 years, every serious assault on RH belongs to one of six families. Ranked by
how plausibly they could produce a complete proof:

1. **The Weil-transplant / Connes–Consani positivity program** is the only approach
   with (a) a completed model theorem in a parallel universe (RH for function fields),
   (b) an exact win condition (Weil positivity), and (c) unconditional partial results
   that did not exist a decade ago. It has converted RH into a short list of missing
   theorems. The honest caveat: each missing theorem may be RH-hard itself.
2. **The spectral / Hilbert–Pólya program** is almost certainly a *true description*
   of the zeros (the GUE evidence is overwhelming), but 50 years of Hamiltonian-building
   produced constraints on the operator, not the operator. Its real content has merged
   into program 1: the only known candidate space where the primes come *out* rather
   than being put *in* is Connes' adele class space.
3. **Classical analytic number theory** builds quantitative fences (41.7% of zeros on
   the line, zero-density, zero-free regions) that provably cannot close to 100% with
   current machinery — but Guth–Maynard 2024 showed the walls still move when outside
   tools are imported, and it supplies the constraints any real proof must satisfy.
4. **The de Bruijn–Newman heat-flow picture** delivered the deepest structural fact of
   the last decade: Λ ≥ 0, i.e. *RH, if true, is barely true*. This is a filter on
   proofs, not a route to one.
5. **Equivalent criteria** (Li, Nyman–Beurling, Robin, Riesz, …) conserve difficulty:
   the same square-root-cancellation/positivity always resurfaces. Two exceptions
   historically produced real leverage (Weil positivity; Speiser→Levinson).
6. **Claimed proofs** (Atiyah 2018, de Branges, the arXiv/viXra stream) share one
   anatomy: generic machinery that never uses the arithmetic of ζ — which the
   Davenport–Heilbronn counterexample shows *must* fail.

**Bottom line:** if RH is proved in our lifetime, the most probable shape is a
positivity theorem in a new arithmetic geometry (Connes–Consani / Deninger style,
possibly reinforced by the 2026 perfectoid bridge), with the analytic and
random-matrix corpus as constraint-checking scaffolding. The second most probable
shape is an unforeseen import, in the way decoupling entered via Bourgain and
harmonic analysis entered via Guth–Maynard. No visible route is close.

---

## 2. Why RH is hard — the three walls

Any candidate approach must pass three filters. Most fail all three; each serious
program fails exactly one, and it is always the same one dressed differently.

**Wall 1 — Positivity.** RH is equivalent (Weil 1952) to the positivity of the
explicit-formula quadratic functional W(f∗f̃) ≥ 0. Over function fields this exact
positivity is a *theorem* — the Hodge index theorem on the surface C×C (how Weil won,
`papers/algebraic-geometric/Weil-1941-pnas-rh-function-fields.pdf`). Over ℚ, nobody
can prove it beyond restricted test-function support (Connes–Consani 2020: support
ratio ≤ 2, `ConnesConsani-2020-weil-positivity-archimedean.pdf`). Every reformulation
— Li's λₙ ≥ 0, de Branges' space conditions, Jensen-polynomial hyperbolicity — is this
wall relocated. Sobering calibration from the notes: the positivity half of
Grothendieck's standard conjectures is open *even over finite fields*; Deligne won the
model case by going around positivity (Rankin squaring), not through it.

**Wall 2 — The missing arithmetic object.** In every solved analogue (function fields,
Selberg zeta) the zeros are eigenvalues of a natural operator acting on the cohomology
of a geometric object: Frobenius on a curve, the Laplacian on a hyperbolic surface
(`papers/spectral/Marklof-2004-selberg-trace-formula-intro.pdf`). For Spec ℤ the
object — an "F₁-curve" whose closed points are the primes, with a Frobenius flow —
is precisely what the arithmetic site, the scaling site, and Deninger's foliated
dynamical systems are attempts to build. Morishita 2025
(`Morishita-2025-deninger-vs-connes-consani.pdf`) proves the two constructions
essentially converge — evidence they are digging at the same real thing.

**Wall 3 — Sharpness.** Rodgers–Tao 2018 proved the de Bruijn–Newman constant Λ ≥ 0
(`papers/analytic-progress/Rodgers-Tao-2018-dBN-nonnegative.pdf`): under heat flow,
the zeros are *exactly* on the boundary of chaos. RH has no analytic slack. Any proof
strategy that loses an ε anywhere — any soft-analysis, compactness, or generic-bound
argument — is dead on arrival. Combined with Davenport–Heilbronn (functions with ζ's
analytic shape but off-line zeros), this gives the two-part filter for triaging any
claimed proof in minutes: *where is the Euler product used, and where is the argument
sharp?* Atiyah 2018 failed both instantly (`notes/surveys-expository.md`).

Tao's summary of the difficulty (June 2024, captured verbatim in the notes): the
explicit-formula dictionary converts RH into prohibiting *one extremely bad
conspiracy* among primes, while all known techniques only rule out *many somewhat bad*
ones — and a single conspiracy can hide below every moment/average that current
analysis can compute.

---

## 3. Family-by-family verdicts

### 3.1 Weil transplant → Connes–Consani (and Deninger) — `papers/algebraic-geometric/`, 39 papers

**The idea.** RH is a theorem for curves over finite fields. Build the geometry in
which Spec ℤ is a curve, take the "square", prove a Riemann–Roch / Hodge-index
inequality there, and Weil positivity — hence RH — follows exactly as in 1948.

**Scoreboard (proved, unconditionally):** the semilocal trace formula; spectral
realization of zeros as an absorption spectrum (Connes 1998); the arithmetic site
whose points over ℝ₊ᵐᵃˣ recover the adele class space (2014/15); the scaling site as
a tropical curve with Riemann–Roch on its periodic orbits C_p (2016); integer-valued
Riemann–Roch with Serre duality for Spec ℤ̄, χ(D) = deg D + 1 (2022/23); **Weil
positivity at the archimedean place for test functions of support ratio ≤ 2** via
prolate/Sonin spaces (2020) with semilocal stability (2023); a concrete operator
family from finite Euler products whose spectra match the low zeros to high precision
(zeta spectral triples, 2025); and the Jacobian/Picard monoid of the arithmetic curve
plus a bridge from the adele class space to the Fargues–Fontaine curve of p-adic Hodge
theory (2026).

**Missing:** positivity beyond support ratio 2 (their own ζ-cycles analysis shows the
extension *must* use the Euler product, not just estimates — Wall 1 meeting the
arithmetic-input requirement head-on); any Riemann–Roch/Hodge theory on the *square*
of the site; convergence of the zeta-spectral-triple spectra (numerically overwhelming,
unproven — proving it would be RH).

**Verdict: the most serious live program.** It is cumulative (each paper builds on the
last, 2014→2026 without a retraction), it has an exact win condition, and it keeps
absorbing neighboring structures (Deninger's systems, arithmetic topology, now
perfectoid geometry). Two risks. First, each missing theorem is plausibly RH-hard —
this may be profound reformulation rather than approach. Second, the model case
warns that the positivity route was *not* how even Deligne won; a "Rankin-squaring
shortcut" in the new geometry, if one exists, has not been found. Probability-weighted,
still the best bet on the board.

### 3.2 Hilbert–Pólya / spectral / RMT — `papers/spectral/`, 34 papers

**What is established beyond reasonable doubt:** the zeros behave exactly like
eigenvalues of a GUE random matrix — Montgomery's pair correlation (1973), Odlyzko's
numerics at height 10²⁰, the Keating–Snaith/CFKRS moment dictionary, and the
Fyodorov–Hiary–Keating extreme-value conjecture *proved* at leading order (Arguin–
Belius–Bourgade–Radziwiłł–Soundararajan). The hypothetical operator is sharply
constrained: chaotic, no time-reversal symmetry, periodic orbits = prime powers with
period log pᵏ, mean counting (E/2π)(log(E/2π)−1) + 7/8, Altland–Zirnbauer class C
resolving the orbit sign anomaly (Srednicki).

**What 50 years failed to produce:** the operator. Every explicit Hamiltonian either
lacks arithmetic (xp and all regularizations — Berry–Keating, Sierra's corpus), inserts
it by hand at the RH-hard step (BBM 2017's boundary condition; refuted as non-self-
adjoint by Bellissard, conceded in the reply — the full controversy is on disk), or is
rigorous-but-local (Srednicki's local RH). The Regniers–Van der Jeugt no-go moral:
"quantize xp" is not even well-posed. Self-adjointness alone is vacuous — *any* real
sequence is some operator's spectrum; all content lives in the word "natural".

**Verdict: true picture, not a proof program in itself.** Its viable continuation *is*
§3.1 — the adele class space is the unique known candidate where primes appear as
periodic orbits rather than inputs. Physics-side activity (cold atoms, trapped-ion
realizations of the first 80 zeros) is evidence-gathering and outreach, not distance-
to-proof. If a Hamiltonian is ever written down, it will be read off from the new
geometry, not guessed.

### 3.3 Classical analytic progress — `papers/analytic-progress/`, 27 papers

**The fences, current positions:** ≥ 5/12 ≈ 41.7% of zeros on the critical line
(PRZZ 2020, end of the Hardy→Selberg→Levinson→Conrey chain); zero-density
N(σ,T) ≤ T^{30(1−σ)/13} at σ = 3/4 (Guth–Maynard 2024 — first improvement on Ingham
since 1940); zero-free region shape unimproved since Vinogradov–Korobov 1958 (2020s
work, incl. the BTY 2026 record 1/(4.896 log t), is constant-optimization); Lindelöf
stuck at Bourgain's 13/84; rigorous verification to height 3·10¹² (Platt–Trudgian).

**Why it cannot close:** mollifier/Levinson technology has a proven exchange rate and
a structural ceiling well below 50% (Radziwiłł's analysis; mollifier length capped by
Deshouillers–Iwaniec technology frozen since the 1980s). Zero-density counts
hypothetical exceptions; it can grind toward the Density Hypothesis but "exceptions
are rare" never becomes "exceptions are absent". Verification can never finish, and
Polymath15 quantified the exchange rate as exponentially bad (Λ ≤ ε costs height
exp(C/ε)).

**What Guth–Maynard actually changed:** not the distance to RH, but the *mobility of
the walls* — an import from harmonic analysis broke an 84-year-old bound, spawned a
follow-up ecosystem (q-aspect 7/3, ANTEDB systematization, PNT in x^{17/30}), and
re-opened the question of what else large-value technology can reach. The one new
lever on the proportion record in 50 years: pair-correlation → horizontal-distribution
bridges (Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh 2025: a narrow-box hypothesis
strictly weaker than RH already gives 2/3 on the line).

**Verdict: will not prove RH; defines the terrain.** Its realistic ceiling is the
Density Hypothesis (way-station, huge for applications), plus constraints every
candidate proof must satisfy. Fund it, watch it, don't expect RH from it.

### 3.4 de Bruijn–Newman — `papers/analytic-progress/`, Rodgers–Tao + Polymath15

0 ≤ Λ ≤ 0.2. RH ⟺ Λ = 0, and the lower bound says the zeros sit exactly at the
boundary: heat flow forward creates order, backward creates violations arbitrarily
fast. **Verdict:** a completed research arc whose product is Wall 3 — the sharpness
filter. No further route to RH here; the remaining content is the (exponentially
losing) computational squeeze.

### 3.5 Equivalent criteria — `papers/criteria/`, 45 papers

The complete audit (Li/Keiper–Li, Nyman–Beurling/Báez-Duarte with both Burnol lower
bounds, Robin/Lagarias/Nicolas, Balazard–Saias–Yor, Riesz/Hardy–Littlewood, Redheffer,
Franel–Landau, Speiser, Salem, Sondow) supports one law: **equivalences conserve
difficulty.** The same Möbius/Λ square-root cancellation reappears as λₙ ≥ 0 growth
control (Arias de Reyna: Li numerics can't outrun verified zero height), as the d_N
distance floor ≳ 1/log N (Burnol — the Nyman–Beurling program's own unconditional
negative result), as σ(n) vs e^γ n log log n at the last 20-free integers, as Riesz
coefficient decay. Historical exceptions that *did* pay: Weil positivity (became
§3.1's win condition) and Speiser's criterion (became Levinson's method, hence the
41.7%). The de Branges episode is the boundary case that proves the law: the one
program with *checkable* sufficient conditions saw them checked — Conrey–Li showed the
positivity demanded strictly more than RH and is simply false for ζ (primary sources
on disk: the Apology, the 2017 89-page proof, the refutation). Positivity soft enough
to prove is false; positivity weak enough to be true is RH.

**Verdict: a criterion is a lens, not a lever.** Useful for translating a future idea
into checkable form; produces no independent route.

### 3.6 Jensen polynomials / hyperbolicity — `papers/surveys-expository/`

GORZ 2019 (hyperbolicity of degree ≤ 8 Jensen polynomials, density-1 asymptotics) +
Bombieri's sympathetic PNAS commentary + Farmer's decisive rebuttal ("not a plausible
route": the results follow from zero-density facts far weaker than what's known, and
the asymptotic regime structurally cannot see the low-lying conspiracy that is the
whole problem). **Verdict: closed.** A case study in press-release-driven optimism —
the "revived abandoned approach" framing was Emory PR.

### 3.7 Claimed proofs & the failure anatomy — `papers/surveys-expository/`

Atiyah 2018 (Todd function is locally polynomial — self-contradictory as "weakly
analytic"; argument never touches ζ's arithmetic, so Davenport–Heilbronn kills it);
de Branges (see §3.5); Stieltjes 1885 (claimed Mertens, disproved by Odlyzko–te Riele
1985 — on disk); Rademacher 1943 (flaw found by Siegel; *Time* ran the retraction).
Stable anatomy across a century: (1) generic machinery, no Euler product at the
decisive step; (2) proves-too-much (would apply to Davenport–Heilbronn); (3) violates
sharpness (an ε of slack somewhere); (4) announcement-first sociology. The
formalization layer (§4) is about to make this anatomy mechanically checkable.

---

## 4. Wildcards (mid-2026)

- **Formalization + AI.** The RH statement, ζ, and L-functions are now in Mathlib;
  strong PNT was autoformalized by an AI system in weeks; Tao's explicit-ANT pipeline
  is converting the constant-optimization literature into verified infrastructure.
  Zero mathematical progress on RH itself — but the *vetting economics* of the next
  serious claimed proof change completely. Watch for the first formalized zero-density
  theorem.
- **Landau–Siegel.** Zhang's 2022 claim remains unaccepted and unrevised (v1, known
  gaps). A correct Landau–Siegel result would remove RH's most notorious real-axis
  shadow and validate discrete-mean technology adjacent to the density program.
- **The perfectoid bridge.** Connes–Consani's 2026 identification of structure linking
  the adele class space to the Fargues–Fontaine curve is the first contact between the
  RH program and the most productive machinery in modern arithmetic geometry
  (Scholze-school). If that contact becomes functorial transfer, the "square of
  Spec ℤ" problem may inherit tools nobody has aimed at RH before. Speculative; the
  single most interesting new opening in the archive.
- **Arithmetic topology.** Knots/primes realized concretely on the scaling site
  (CC 2024/25) + Morishita's convergence theorem — a second independent derivation of
  the same geometry raises confidence the object is real.

---

## 5. What a successful proof will probably look like

Filter any future claim through these five predictions:

1. **It proves a positivity statement** (Weil-functional or Hodge-index type) in a
   geometry where Spec ℤ is a curve — or finds that geometry's Rankin-squaring
   shortcut around positivity, as Deligne did in the model case.
2. **The Euler product / primes-as-orbits structure is load-bearing** at the decisive
   step — the argument visibly fails for Davenport–Heilbronn.
3. **It is sharp** — no lossy estimate at the critical inequality (Λ = 0 leaves no
   room); equality cases are geometric (an adjunction/duality), not analytic.
4. **It recovers the GUE phenomenology** as the spectral shadow of the geometry
   (the quantum-chaos corpus becomes its consistency check, as monodromy did for
   Katz–Sarnak in function fields).
5. **It formalizes.** Given the 2025–26 infrastructure, a real proof will be in Lean
   within a couple of years of announcement; a claim whose authors resist
   formalization is, going forward, self-labeling.

Conversely, instant-reject signals: soft/compactness arguments, criteria-shuffling
(proving an equivalence rather than the positivity inside it), asymptotic-regime-only
results, any step that works for generic Dirichlet series.

---

## 6. Watch list

| Signal | Where | Why it matters |
|---|---|---|
| Positivity beyond support ratio 2 | Connes–Consani | The single missing theorem closest to RH |
| Any RR/Hodge statement on the *square* of the scaling site | Connes–Consani | Wall 2 falling |
| Convergence proof for zeta spectral triples | CCM | Numerically overwhelming; a proof = RH |
| Improvement of 30/13, or Density Hypothesis at σ near 3/4 | post-Guth–Maynard | Tests whether the harmonic-analysis import has more fuel |
| Proportion > 5/12 via pair-correlation bridges | Goldston school | First new lever on the record in 50 years |
| Corrected Landau–Siegel manuscript | Zhang or successors | Adjacent breakthrough; validates discrete-mean tech |
| Fargues–Fontaine ↔ adele class space functoriality | CC + Scholze school | New tools entering the arena |
| First formalized zero-density theorem | Lean/Mathlib community | Verification economics of future claims |

---

## 7. Index

| Category | Papers | Notes |
|---|---|---|
| Spectral / Hilbert–Pólya / RMT | `papers/spectral/` (34) | `notes/spectral.md` |
| Classical analytic progress | `papers/analytic-progress/` (27) | `notes/analytic-progress.md` |
| Algebraic-geometric programs | `papers/algebraic-geometric/` (39) | `notes/algebraic-geometric.md` |
| Equivalent criteria | `papers/criteria/` (45) | `notes/criteria.md` |
| Surveys, failed proofs, media | `papers/surveys-expository/` (18) | `notes/surveys-expository.md` |
| Recent (2019–2026) | `papers/recent/` (15) | `notes/recent.md` |

Paywalled classics recorded citation-only in the notes: Hardy 1914, Selberg 1942,
Ingham 1940, Huxley 1972, Weil 1948 (book), Weil 1952, Li 1997, Newman 1976,
Levinson–Montgomery 1974, Robin 1984, Balazard–Saias–Yor 1999, Iwaniec/Edwards/
Titchmarsh/Broughan (books).
