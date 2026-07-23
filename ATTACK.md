# If I were to actually attack RH: the deep dive

*Written 2026-07-23 after full absorption of the archive (178 sources, `notes/*.md`,
synthesis in `BREAKDOWN.md`). This document goes deeper: it reduces the problem to its
irreducible core, maps the no-go theorems that fence every route, isolates the handful
of situations in the literature that are genuinely "one theorem from mattering," and
lays out — concretely, lemma by lemma — what a serious attempt would look like.
Claims sourced to the archive are cited by file; everything marked* **[synthesis]**
*is my own cross-category inference and should be treated as a research hypothesis.*

---

## 1. The irreducible core: RH is a boundary-feasible convex problem

Strip away every reformulation and one interface remains. The Riemann–Weil explicit
formula is an *identity* between spectral data and arithmetic data:

```
Σ_ρ ĥ(ρ)  =  ĥ(0)-pole + ĥ(1)-pole  −  Σ_p Σ_{k≥1} (log p) p^{-k/2} [h(p^k) + h(p^{-k})]  +  W_∞(h)
```

for test functions h on (0,∞). Weil 1952: **RH ⟺ the right side is ≥ 0 for every
h = g∗g̃** (with the pole directions projected out — hence the conditions
ĝ(0) = ĝ(i/2) = 0 in Connes–Consani's theorem). If RH holds, the left side is
Σ_ρ |ĝ(ρ)|², manifestly nonnegative; a single off-line pair ρ, 1−ρ̄ makes the form
indefinite. (`notes/criteria.md` §1, `notes/algebraic-geometric.md` §35.)

Three structural facts about this positivity problem, assembled from across the archive,
determine everything:

**(a) It has a signature, not just a sign.** The two pole terms are *positive*
directions that must be quotiented out; what remains must be semidefinite. That is
exactly the signature structure of the Hodge index theorem on an algebraic surface —
one positive direction (the hyperplane/fiber class), negativity on its orthogonal
complement. Weil's function-field proof is literally this statement on C×C. So the
sought inequality is not "W ≥ 0" raw; it is "W has exactly the Hodge signature."
**[synthesis]** The correct target has an *equality structure*: identify the null
directions first, then prove definiteness transverse to them.

**(b) It is boundary-feasible: the interior is empty.** Rodgers–Tao's Λ ≥ 0
(`papers/analytic-progress/Rodgers-Tao-2018-dBN-nonnegative.pdf`) says RH, if true,
is *barely* true; Odlyzko–te Riele's disproof of Mertens and the failure of every
"RH with room to spare" strengthening say the same from the arithmetic side; and
Connes–Consani's ζ-cycles analysis (`ConnesConsani-2021-zeta-cycles.pdf`) exhibits the
mechanism concretely — as the test-function window grows, the Weil form develops
*arbitrarily small eigenvalues* whose eigenvectors are arithmetic combinations of
prolate functions. The primes sit asymptotically in the near-null cone of the form.
Any proof strategy that would certify positivity *with margin* is therefore proving a
false statement. This kills entire strategy classes in advance (soft analysis,
compactness, perturbation from a definite model) and explains post-hoc why de Branges'
conditions — checkably *stronger* than RH — failed against the low zeros
(Conrey–Li, `papers/criteria/Conrey-Li-1998-positivity-deBranges.pdf`).

**(c) The certificate, if it exists, is one convex-duality object away.** A positivity
statement over a cone of test functions is a semi-infinite linear/semidefinite program.
Proving it means exhibiting a *dual certificate*. The three live schools are exactly the
three known languages for such a certificate **[synthesis]**:
- **geometric** — an intersection theory in which the form is a Hodge-index form
  (Weil's proof; the Connes–Consani Riemann–Roch strategy);
- **spectral** — an inner product making the scaling flow unitary, so the form becomes
  a Gram matrix (Hilbert–Pólya; Connes' absorption realization; zeta spectral triples);
- **analytic** — an explicit "magic function" identity certifying the sign pointwise
  (the Viazovska school's solution shape for boundary-tight LP problems; see §7).

These are the same convex program in three dualities. The problem's empty interior is
why only *exact* certificates can work — and the one modern subject that has produced
exact certificates for boundary-tight problems of precisely this shape (Poisson-type
summation pairing + sign constraints) is the modular-forms magic-function method that
solved sphere packing in dimensions 8 and 24. That precedent matters: boundary-tight
does not mean unprovable; it means the certificate is rigid and special, and finding it
is a construction problem, not an estimation problem.

**(d) The Euler product must enter, or the proof is wrong.** The Davenport–Heilbronn
function satisfies a functional equation and has off-line zeros
(`notes/surveys-expository.md` §2): any argument that would apply to it is dead on
arrival — this is the two-minute filter that instantly killed Atiyah 2018. Combined
with (b): a valid proof must use the primes *at the exact step where positivity is
decided*, and must be sharp there. Connes–Consani's own diagnosis agrees: extending
positivity beyond their proven window "is not a matter of estimates but of using the
Euler product" (`notes/algebraic-geometric.md`, overall assessment).

---

## 2. The no-go map

Every fence in the archive, with what it kills. A serious attempt keeps this list taped
to the wall; each lead in §4–§10 must thread all of them.

| No-go theorem | Source | What it kills |
|---|---|---|
| Λ ≥ 0 (RH barely true) | Rodgers–Tao 2018 | any strategy with analytic slack; proofs of any strengthened RH |
| Mertens disproof | Odlyzko–te Riele 1985 | √x-bounded Mertens routes; "clean strong statement" routes |
| Davenport–Heilbronn | classical | any argument generic in the functional equation |
| Conrey–Li positivity failure | math/9812166 | de Branges-type checkable-sufficient-condition programs: soft Hilbert-space positivity provably overshoots RH |
| d_N² ≫ 1/log N floor | Burnol, math/0103058 | incremental Nyman–Beurling: convergence, if true, is as slow as possible; on-line zeros themselves obstruct |
| Li-coefficient accuracy bound | Arias de Reyna 2011 | numerical Keiper–Li programs: numerics structurally cannot see beyond verified height |
| No self-adjoint p on half-line; non-L² eigenfunctions | Bellissard 2017 | BBM-type PT-symmetric shortcuts; boundary-condition Hamiltonians |
| Quantization ambiguity of xp | Regniers–Van der Jeugt 2010 | "quantize xp" as a well-posed instruction; all mean-density-only models |
| Mean density is cheap | Berry–Keating 2011 | any model validated only by the counting function (many operators share it) |
| Pseudo-Laplacian rigidity | Colin de Verdière's construction as analyzed by Bombieri–Garrett | the naive automorphic-spectrum implementations of Hilbert–Pólya: natural self-adjoint extensions can capture at most a constrained fraction of zeros — spacing statistics (GUE) are incompatible with the spectral rigidity such extensions force **[recalled; verify against Garrett's Bristol 2018 talk before load-bearing use]** |
| Jensen asymptotics live below RH | Farmer 2020 | hyperbolicity-asymptotics routes; a large class of "positivity of associated polynomials" routes |
| Λ ≤ ε costs height exp(C/ε) | Polymath15 | computational squeezes on Λ; verification-driven endgames |
| Mollifier ceiling < 50% | Radziwiłł (per PRZZ discussion) | Levinson-method grinding to a majority of zeros |
| Zero-density counts, never excludes | structural (Tao 2024) | any large-values path to literal RH; "exceptions are rare → absent" |
| Positivity half of standard conjectures open even over F_q | Grothendieck 1969 + Milne 2002 | expectations that the motivic route is near; calibrates how hard "geometric positivity" is even with full geometry available |

Two historical *positive* filters complete the map: Deligne won the model case by
**abandoning** the positivity route for Rankin squaring (`Deligne-1974-weil-I.pdf`),
and Viazovska won a boundary-tight certificate problem by **constructing** the dual
object from modular forms. The proof, when it comes, likely resembles one of these two
victory shapes.

---

## 3. The only two mechanisms that have ever killed an RH

Everything in the archive that ever *finished* an RH-type problem used one of two
engines. Understanding exactly why each currently fails over ℚ tells you where the
walls really are.

### 3.1 Engine A: positivity via intersection theory (Weil 1948)

Hodge index on C×C ⇒ Castelnuovo–Severi ⇒ RH for curves over F_q. Status over ℚ:
the entire Connes–Consani program is the attempt to build the surface; see §4, §6.
Its known partial: archimedean positivity in the ratio-2 window. Its known obstacle:
even over F_q, where all the geometry exists, the *general* positivity conjecture
(Hodge standard) is still open — Weil's case worked because for a *surface* the index
theorem is classical. The transplant needs only the surface case too — the analogue of
"Hodge index for the square of a curve," not the full standard conjectures. That scope
limitation is important and often lost: **the target is the easiest instance of
geometric positivity, not the hardest** **[synthesis]**. Sharpened by the genus
computation: Connes–Consani's Riemann–Roch for Spec ℤ̄ gives χ(D) = deg D + 1 — the
arithmetic curve is *genus 0* (`ConnesConsani-2023-riemann-roch-ring-Z.pdf`). The model
surface is then ℙ¹×ℙ¹, where Hodge index is an exercise. If the tropical/adelic square
ever supports an honest intersection form, the inequality being transplanted is, in the
model, *elementary* — all difficulty lives in building the form, none in the final
inequality.

### 3.2 Engine B: amplification with positive coefficients (Rankin/Deligne)

The single-violation excluder. One bad Frobenius eigenvalue α with |α| too large, fed
through even tensor powers, forces Tr(Frob | Sym^{2k}) to blow up — contradicting
positivity of point counts. This is the *only known mechanism in mathematics that
excludes one conspirator rather than many* — precisely the gap Tao identifies as the
heart of RH's difficulty (`notes/surveys-expository.md` §3, verbatim extract).

Its trace over ℚ **[synthesis]**: the 3-4-1 trigonometric inequality behind the
classical zero-free region *is* a degenerate Rankin argument (positivity of the
coefficients of ζ³·ζ⁴(twist)·ζ(twist²)); Vinogradov–Korobov is that mechanism pushed to
its exponential-sum limit; and the reason it caps at a 1/log-width sliver is that over ℚ
we cannot take k → ∞: there is no "Sym^k of ζ" to climb, because ζ is GL(1). The
function-field proof climbs tensor powers of a *variable local system over the base*;
over ℚ the base is Spec ℤ and we have no local systems on it.

Now the deep split, visible only when the categories are laid side by side: over
function fields, Ramanujan (coefficient bounds) and RH (zero locations) are the *same
theorem* — Deligne's weights. Over ℚ they came apart: Deligne proved Ramanujan for
modular forms in 1974 because Shimura-variety geometry realizes *coefficients* as
Frobenius traces — the geometry that exists over ℚ geometrizes the coefficient side of
L-functions. Nothing geometrizes the *zero* side, because the zeros live over the base
Spec ℤ itself. **This is the precise sense in which the missing object is a geometry of
the base, and why fifty years of spectacular Langlands progress never moved RH by an
epsilon: functoriality (the ℚ-world's tensor-power engine, e.g. Newton–Thorne's Sym^k)
amplifies in the coefficient direction, not the base direction** **[synthesis]**. Two
corollaries for strategy:
- Any amplification route to RH must find families over the *base* — and the only
  candidate family structures over Spec ℤ in the archive are Dirichlet/automorphic
  *twist* families (the q-aspect). Which is exactly where Zhang's Landau–Siegel attempt
  and Chen's q-aspect Guth–Maynard live. Landau–Siegel is thus not "adjacent" to RH; it
  is the first nontrivial test of the only single-violation engine, running on the only
  available family (§9).
- The Connes–Consani/Fargues–Fontaine contact (§6) is the first time a *base-geometry*
  program has touched the machinery (perfectoid, diamonds, Bun_G) that made the modern
  coefficient-side revolution possible. That is why it is more than a curiosity.

---

## 4. Lead 1 — the sharpest concrete opening: Weil positivity with the prime 2

**The situation.** Connes–Consani 2020 (`ConnesConsani-2020-weil-positivity-archimedean.pdf`)
prove: for smooth g supported in [2^{-1/2}, 2^{1/2}] with ĝ(0) = ĝ(i/2) = 0,

```
W(g∗g̃) = W_∞(g∗g̃) ≥ Tr(θ(g) S θ(g)*) ≥ 0
```

where S is the projection onto Sonin space — the subspace of L²(ℝ₊) of functions
vanishing on [0,Λ] *together with their Fourier transform* (the uncertainty-principle-
extremal subspace), controlled via prolate spheroidal functions and Toeplitz theory.

**Why the number 2 is not a technical constant** **[synthesis, verified against the
explicit formula]**: if supp g ⊆ [λ^{-1}, λ], then supp g∗g̃ ⊆ [λ^{-2}, λ²]. The
finite-place terms of the Weil distribution sample g∗g̃ exactly at the prime powers
p^k ≥ 2. For λ² < 2 **no prime term is active at all** — the ratio-2 window is
precisely the largest window in which Weil positivity is a purely archimedean
statement. Their theorem is the *complete* solution of the prime-free case. The next
millimeter — any λ² = 2 + δ — activates exactly **one** arithmetic term:

```
W(h) = W_∞(h) − (log 2) · 2^{-1/2} · [h(2) + h(1/2)]
```

**The target theorem (T1):** *there exists δ > 0 such that for all smooth g supported
in [(2+δ)^{-1/2}, (2+δ)^{1/2}] with ĝ(0) = ĝ(i/2) = 0,*
*W_∞(g∗g̃) − (log 2)·2^{-1/2}·[(g∗g̃)(2) + (g∗g̃)(1/2)] ≥ 0.*

This would be the **first Weil-positivity statement in history that defeats a prime** —
the first inequality of the exact RH-equivalent species with arithmetic content. It is
finite, compactly supported, one-prime, and sits directly on top of proven technology:
- The Sonin-trace lower bound gives a *quantitative positive margin* in the closed
  window; the prime deficit is an explicit rank-≤2 perturbation (evaluation functionals
  at x = 2, 1/2). T1 reduces to: *margin decay vs. explicit rank-2 deficit* as δ grows
  from 0. Both sides are in principle computable — the margin from prolate/Toeplitz
  asymptotics (their §§ on hermitian Toeplitz matrices), the deficit from two point
  evaluations of g∗g̃ against the Sonin projection.
- CCM 2023 (`ConnesConsaniMoscovici-2023-prolate-wave-operators.pdf`) proved exactly the
  needed stability: the Sonin mechanism *survives the addition of finite places* — the
  semilocal prolate wave operator exists for {∞, 2}. The framework for T1 is built.
- Groskin 2026 (`papers/criteria/Groskin-2026-truncated-Weil-form.pdf`) bounds the
  archimedean tails of the truncated form — the error-control side of the same
  computation.
- ζ-cycles tells us what failure looks like: if δ can be taken all the way (all primes
  eventually entering), small eigenvalues appear whose eigenvectors are arithmetic
  prolate sums. For a *single* prime and bounded window there is no infinite arithmetic
  interference to hide in — the degeneration mechanism has not yet turned on.
  **[synthesis]** T1 lives strictly below the difficulty phase transition.

**Why T1 is not RH in disguise (the circularity audit):** restricted-support positivity
statements are strictly weaker than RH (RH needs all supports); the prime-free case was
proved unconditionally, and Yoshida's short-interval positivity (reproved in
`papers/criteria/Bombieri-2000-Weil-quadratic-functional.pdf`) shows other genuinely
sub-RH positivity windows exist. T1 extends a proven theorem by a controlled rank-2
perturbation. The RH-hardness enters later, in the *unbounded-support limit* — the
δ → ∞ percolation (each doubling of the window admits the next prime-power stratum:
2 → 3 → 4=2² → 5 → …). A realistic program: T1 (one prime), then T1' (window ratio up
to 3+δ: primes 2, 3), tracking exactly how the Sonin margin absorbs each new term, and
*locating the first prime at which the mechanism fails without new input*. Even the
failure point would be a landmark: it would say quantitatively where the Euler product
must take over from the uncertainty principle.

**My estimate:** T1 is the single most attackable theorem in this entire archive whose
statement is of the exact species equivalent to RH. If I had one year and one
collaborator versed in prolate/Toeplitz asymptotics, this is where it would go.

---

## 5. Lead 2 — zeta spectral triples: the convergence question, handled with tongs

**The situation.** CCM 2025 (`ConnesConsaniMoscovici-2025-zeta-spectral-triples.pdf`,
with the strategy stated in human-readable form in Connes' Feb 2026 "Letter to Riemann,"
`papers/recent/Connes-2026-letter-through-time.pdf`): self-adjoint operators
D^{(λ,N)} built as rank-one perturbations of the scaling operator's spectral triple on
[λ^{-1}, λ], constructed *only* from the finite Euler product over p ≤ λ²;
self-adjointness secured by an extension of Carathéodory–Fejér theory; spectra
numerically converge to the nontrivial zeros; **a proof of convergence is a proof of
RH**. The Letter's companion result: extremizing the restricted Weil form produces
approximate zeros *provably on the critical line*.

**The trap, stated plainly:** "prove the convergence" is RH-complete. Attacking it head
on is attacking RH with extra steps. The correct posture **[synthesis]**:

1. **Map the failure mode first.** Theorem to seek (T2a): *if RH is false, identify
   exactly what the D^{(λ,N)} spectra do* — presumably: spectra still real (they are
   self-adjoint by construction!), still converging on compacta, but converging to a
   set that is *not* the zero multiset (off-line zeros ρ, 1−ρ̄ contributing... what?).
   An unconditional theorem "spec D^{(λ,N)} → Z ∪ (defect set characterized by off-line
   zeros)" would convert the construction into a genuine RH-criterion with *local*
   checkable structure, and would show precisely which spectral quantity feels the
   off-line conspiracy. Without T2a, numerical convergence is uninterpretable as
   evidence.
2. **Prove one-sided containment.** (T2b): every limit point of the spectra is a zero
   (no spurious spectrum) — plausibly provable from the semilocal trace formula
   without RH; the RH-hard direction is completeness (no zero escapes).
3. **Quantify the finite-λ window.** (T2c): explicit height H(λ, N) up to which the
   spectrum provably ε-matches the verified zeros (input: Platt–Trudgian height,
   `Platt-Trudgian-2020-RH-3e12.pdf`). This is honest, finite mathematics with real
   value: it would make the construction *certified* in a range, the first Hilbert–Pólya
   candidate ever with a proven spectral window.

The deep open question the construction poses — and where I would genuinely dig — is
*why rank-one perturbations by finite Euler products are the right deformation class*.
The Carathéodory–Fejér input is a positivity theorem for Toeplitz forms; Toeplitz
positivity is also the engine of Lead 1. **The two leads are the same mathematics from
two duals: T1 asks for positivity of a form; T2 builds operators whose self-adjointness
is that positivity, operatorized** **[synthesis]**. Progress on either transfers.

---

## 6. Lead 3 — the square, its slopes, and the Fargues–Fontaine bridge

**The situation.** The Riemann–Roch strategy
(`ConnesConsani-2018-riemann-roch-strategy-complex-lift.pdf`) needs: the square of the
scaling site, an intersection/Riemann–Roch theory on it, and the Hodge-index inequality.
Have: the square with Frobenius correspondences (char 1); RR with integer dimensions and
Serre duality on the *curve* (χ(D) = deg D + 1 — genus 0); the Jacobian/Picard monoid
(`ConnesConsani-2026-jacobian-of-specz.pdf`); tropical RR on each periodic orbit C_p.
Missing: everything two-dimensional.

**Concrete attack surface A (finite level).** The scaling site's arithmetic lives on
its periodic orbits C_p. For a finite set S of primes, the "S-truncated square" is a
finite-complexity tropical object (finitely many orbit tori and their products)
**[synthesis]**. Target (T3a): *state and prove a tropical Hodge-index/Castelnuovo
inequality on the S-truncated square, and show it implies the semilocal Weil positivity
for test functions supported on S-units.* The semilocal trace formula is already a
theorem for finite S (Connes 1998, extended 2023) — so the analytic side of the
finite-level dictionary exists. If T3a is provable for |S| = 1, it *is* Lead 1 in
geometric clothing; if provable for all finite S, RH becomes exactly the statement that
the inequality survives the limit — the entire difficulty localized in one compactness
question at the archimedean place. Even a failed attempt at T3a is informative: it
identifies which two-dimensional structure (the intersection pairing? properness? the
moving lemma?) char-1 geometry actually lacks.

**Concrete attack surface B (slopes).** Tropical geometry and the FF-curve both carry
Harder–Narasimhan formalisms. The 2026 bridge
(`ConnesConsani-2026-absolute-geometry-specz.pdf`: points of (Spec ℤ)_{F₁} over
perfectoid fields = untilts, contact with the Fargues–Fontaine curve) suggests the
missing positivity might enter as a *slope inequality* rather than an intersection
inequality **[synthesis]**: HN theory on bundles over the adelic curve, with a
Bogomolov-type inequality on the square. Precedents that make this non-fantastical:
slope/HN methods deliver exactly semistability-positivity in every geometry that has
them (vector bundles on curves, FF-curve isocrystals, Arakelov adelic slopes à la
Bost); and an "arithmetic Bogomolov" on the CC square would be a Hodge-index surrogate
of precisely the needed strength. First test problem (T3b): *define degree and rank
for the Frobenius correspondences on the square and compute the HN polygon of the
graph-of-Frobenius classes* — the objects whose intersection numbers encode
|N_m − (q^m+1)| ≤ 2g q^{m/2} in Weil's proof. If their arithmetic analogues have
computable slopes, the sought inequality has a *statement*, which today it does not.

**Deninger consistency test (T3c).** Deninger's dynamical systems now exist as
constructions (`Deninger-2018-dynamical-systems-arithmetic-schemes.pdf`), and Morishita
2025 proved they converge with the CC adelic spaces
(`Morishita-2025-deninger-vs-connes-consani.pdf`). Run the whole program in the one
world where the answer is known: *compute the leafwise cohomology and transverse index
of Deninger's constructed system for a function-field base, and verify it reproduces
Weil's theorem.* If it does, the transplant is a machine and the ℚ-case is "only" an
analytic limit; if it does not, twenty years of axiomatics have a gap that must be
found now, not after more construction. To my knowledge the archive contains no such
verification — its absence is itself a finding. **[synthesis]**

---

## 7. Lead 4 — the magic-function route: certificates, interpolation, and SDP

This is the lead the archive *implies* but nowhere states.

**The shape-match.** The Cohn–Elkies linear program for sphere packing: find f with
f(0) = f̂(0) = 1, f̂ ≥ 0, f ≤ 0 outside radius r ⇒ density bound. Viazovska: in d = 8
the bound is *tight*, and the extremal certificate is an explicit modular-form
construction; likewise d = 24, and universal optimality (CKMRV 2019/2022) via Fourier
interpolation at ±√n nodes. Structure of Weil positivity: a Poisson-type summation
identity (the explicit formula — literally adelic Poisson summation in Weil's and
Connes' treatments) pairing a spectral set against the arithmetic node set
{p^{k/2}} ∪ {p^{-k/2}}, with a sign question on a cone of test functions. **The Weil
cone is a Cohn–Elkies-type program whose nodes are prime powers instead of lattice
vectors** **[synthesis]**. Riemann's ξ is even entire of order 1 with a theta-integral
representation — squarely inside the function classes the interpolation school
manipulates; and the Seip school (Bondarenko–Radchenko–Seip, ≈2020) has already
constructed **Fourier interpolation formulas whose node set is the zeta zeros** —
crystalline summation structure attached to exactly our spectral set.

**Why this could matter and not just rhyme:** the two obstacles that make Weil
positivity "boundary-feasible" — no margin, exact certificates only — are the *native
habitat* of the magic-function method, which has now repeatedly produced exact,
margin-zero certificates where decades of soft analysis could not. And the certificate
format automatically satisfies the Euler-product filter: the nodes are the prime powers;
a certificate is *by construction* an arithmetic object.

**Concrete program (T4).**
1. (T4a) Pose the ratio-(2+δ) positivity of Lead 1 as a finite-dimensional SDP:
   truncate to a prolate basis (the natural basis per CC 2020), impose the two point
   evaluations at 2^{±1}, search numerically for the dual certificate. Modern SDP +
   rigorous rounding (as in the Cohn school's certified computations and the
   Chirre–Gonçalves–de Laat-style numerically-assisted bounds in analytic number
   theory) could *certify T1 for concrete δ* — a computer-assisted but rigorous first
   arithmetic Weil-positivity theorem. This is a months-scale project with existing
   software technology, and nobody in the 178-source archive has done it. It is the
   single cheapest high-value experiment available. **[synthesis]**
2. (T4b) Look for the exact certificate as a modular/automorphic object: the
   archimedean kernel of the explicit formula is built from Γ-factors (digamma), the
   functional equation from theta; the suspicion that the extremal function for the
   Weil cone at criticality is theta/Eisenstein-adjacent is exactly the d = 8 story
   transposed. A place to start: the extremal problems already solved by the
   Carneiro–Littmann–Vaaler school (extremal majorants of Beurling–Selberg type *for
   the explicit formula*, used to bound zero-counting quantities under RH) — that
   literature is the LP-primal side of our problem and its extremal functions are
   theta-built. The missing move is running it *unconditionally on the dual side*.
3. (T4c) Connect to Lead 2: a dual certificate for the truncated form is precisely
   what makes D^{(λ,N)} self-adjoint with controlled spectrum (Carathéodory–Fejér *is*
   a certificate theorem). A T4a certificate would likely convert directly into a
   spectral window statement (T2c).

---

## 8. Lead 5 — pair correlation as the live classical lever

The one classical place where a *new mechanism* (not parameter-grinding) can move a
headline number. Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh
(`Baluyot-2025-pair-correlation-proportions.pdf`): Montgomery's pair-correlation
machinery, de-conditionalized — a narrow-box hypothesis (all zeros within O(b/log T)
of the line) already weaker than RH yields 2/3 on the line, vs. the unconditional
41.7% record (PRZZ). The gap between the hypothesis they need and what is provable is
the *form factor* F(α,T): Montgomery controls |α| < 1 on RH; unconditional control is
partial.

**Concrete target (T5): unconditional (or nearly-so) control of F(α,T) past any fixed
|α| < 1, using Guth–Maynard large-value technology.** The form factor is a mean square
of a Dirichlet-polynomial-like sum over zeros; the GM method is precisely a machine for
such objects in the critical regime, and the Tao–Trudgian–Yang database
(`Tao-Trudgian-Yang-2025-exponent-database.pdf`) already tracks "zero additive energy"
— the α > 1 obstruction in disguise. **The two most active classical technologies of
the decade (GM large values; de-conditionalized pair correlation) have not yet been
composed; their composition is the plausible route past 41.7% and toward
"most zeros on the line," which would be the first majority statement in history**
**[synthesis]**. Secondary classical dials, quantified in the archive: any improvement
on Deshouillers–Iwaniec bilinear Kloosterman estimates mechanically lifts the mollifier
length θ and the PRZZ constant; Guth's stated harmonic-analysis obstructions
(`Guth-2025-large-values-survey.pdf`) mark the Density Hypothesis path. None of this
reaches RH (§2, "counts, never excludes") — its role in the attack is constraint
tightening and, in the T5 case, testing whether the vertical-to-horizontal bridge can
be made unconditional.

---

## 9. Lead 6 — Landau–Siegel as the test of Engine B

Per §3.2, the exceptional-zero problem is where the only single-violation-excluding
mechanism meets the only available base-family. Zhang's manuscript
(`Zhang-2022-Landau-Siegel.pdf`) is stalled — v1, acknowledged gaps in the
discrete-mean sections, no revision in four years — but the *strategy class*
(amplification over the family of real characters with positive-coefficient
constructions) is the correct species, the same species as Goldfeld–Gross–Zagier's
effective class-number solution. A repaired discrete-mean framework would: (i) remove
GRH's most notorious near-counterexample; (ii) validate an amplification template that
is the ℚ-side's closest cousin of Rankin squaring; (iii) make effective vast tracts of
multiplicative number theory. If I were allocating a classical-side team, auditing and
rebuilding Zhang's §§8–15 (the discrete-mean evaluations experts flagged) would be its
second project after T5 — with the explicit-ANT/Lean pipeline (§11) as the audit
instrument, since a 111-page computation-dense manuscript is exactly what the
formalization layer now exists to adjudicate.

---

## 10. What I would actually run: the portfolio

| Track | First concrete lemma | Kills/It builds | Horizon |
|---|---|---|---|
| **T1** {∞,2} Weil positivity | Sonin-margin vs. rank-2 prime deficit as explicit Toeplitz computation | first arithmetic positivity of RH species | 1–2 yr |
| **T4a** SDP certificate | prolate-basis truncation of T1; certified numerics | machine-checkable T1; template for prime-by-prime percolation | months |
| **T2b/T2c** spectral triples, one-sided | no-spurious-spectrum from semilocal trace formula; certified window vs. Platt–Trudgian height | first proven spectral window for a Hilbert–Pólya candidate | 1–2 yr |
| **T3a** finite-level tropical Hodge index | |S|=1 case: intersection form on the 2-truncated square | geometric dual of T1; locates the missing 2-dim structure | 2–5 yr |
| **T3c** Deninger function-field test | leafwise cohomology of the constructed system for F_q(t) | validates or falsifies the dynamical transplant | 1–3 yr |
| **T5** GM × pair correlation | F(α,T) beyond fixed α<1 via large-value estimates | >41.7%, path to majority-on-line | 1–3 yr |
| **T3b** slopes on the square | HN polygon of Frobenius correspondences; FF-bridge dictionary | a *statement* for the missing inequality | 3–10 yr |
| **L–S audit** | rebuild Zhang §§8–15 in the explicit-ANT pipeline | Engine B validation; effective GRH neighborhood | 2–5 yr |

Cross-cutting design rules enforced on every track (from §1–§2): (i) *null-space
first* — target degenerate-positive statements with characterized equality cases,
never margin-positive ones; (ii) every argument must fail on Davenport–Heilbronn —
if a draft doesn't visibly consume the Euler product at the decisive inequality, it is
wrong; (iii) sharpness audit against Λ = 0; (iv) the GUE/class-C phenomenology
(`notes/spectral.md` §8) is a consistency check any candidate operator/geometry must
pass, never an input; (v) formalize load-bearing computational lemmas (the Mathlib
zeta/L-library, `Loeffler-2025-zeta-L-functions-lean.pdf`, makes this real).

---

## 11. Honest verdict

Nothing in the 178 sources is "very close" to RH in the finishing sense — the two
statements that are literally one theorem from RH (global Weil positivity; zeta-
spectral-triple convergence) are one *RH-hard* theorem from RH. But the archive
supports a sharper claim than the standard counsel of despair: for the first time
since 1859 there exists a **well-posed, finite, plausibly sub-RH-hard theorem of the
exact RH-equivalent species** — the one-prime positivity T1 — sitting on proven
technology (Sonin/prolate positivity + semilocal stability), with a cheap certified-
numerics pilot (T4a) available immediately, a geometric dual (T3a) and an operator
dual (T2) that transfer progress both ways, and a classical program (T5) that can
independently move the oldest headline number in the subject. The realistic best case
for a decade of the portfolio above is not a proof of RH; it is (a) Weil positivity
percolated through the first several primes with the failure mode of the uncertainty-
principle mechanism precisely located, (b) a certified spectral window for a concrete
self-adjoint arithmetic operator family, (c) a stated (maybe proven at finite level)
tropical Hodge-index theorem, and (d) a majority of zeros on the line. That would
transform the problem's status from "no visible route" to "one identified analytic
limit" — which is how hard problems actually end: not with a lightning bolt, but with
the difficulty cornered into one place. The lightning bolt precedents (Deligne's
squaring, Viazovska's function) both struck *after* their fields had done exactly that
cornering. RH's cornering is, on the evidence of this archive, finally underway — at
the archimedean–arithmetic boundary, ratio 2, where the first prime is waiting.
