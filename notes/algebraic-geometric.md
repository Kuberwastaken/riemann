# RH via Algebraic Geometry, Function Fields, F1, and Noncommutative/Arithmetic Geometry
## The "transplant Weil's proof" dream

All local files live in `/root/dev/Riemann/papers/algebraic-geometric/`.

The organizing idea of this whole family: RH **has already been proved once** — for zeta
functions of curves over finite fields (Weil 1948), and then for all varieties over finite
fields (Deligne 1974). Both proofs are geometric: the zeros are eigenvalues of a Frobenius
operator acting on a cohomology, and RH is a *positivity* statement (Castelnuovo–Severi /
Hodge index for Weil; weight monodromy + Rankin squaring for Deligne). The dream is to
build the geometry in which Spec Z becomes a "curve over F1", construct the surface
Spec Z x_F1 Spec Z, find the Frobenius flow, and re-run the proof. Weil's 1952 explicit
formula is the bridge: RH for Riemann zeta is *equivalent* to positivity of the Weil
distribution, which is exactly the shape of statement the geometric proof would deliver.

---

## A. The model theorem: RH over function fields

### 1. Weil, "On the Riemann hypothesis in function-fields" (1941)
- **Authors/venue:** André Weil; Proc. Nat. Acad. Sci. USA 27 (1941), 345–347.
- **Links:** https://www.pnas.org/doi/10.1073/pnas.27.7.345 ; Europe PMC PMC1078336.
- **Local file:** `Weil-1941-pnas-rh-function-fields.pdf`
- **Summary:** The three-page announcement of the proof of RH for all curves over finite
  fields, sketching the intersection-theoretic argument on the surface C x C: the number of
  points is expressed via intersection numbers with the graph of Frobenius, and the
  Castelnuovo–Severi inequality (negativity of the intersection form on the orthogonal
  complement of the fibers, i.e., Hodge index) gives |N_m − (q^m + 1)| ≤ 2g q^{m/2}.
  Context: Artin's 1921/1924 thesis had defined zeta functions for (quadratic) function
  fields and conjectured their RH; F. K. Schmidt (1931) generalized the zeta function and
  proved rationality and the functional equation via Riemann–Roch; Hasse (1933–36) proved
  the genus-1 case (elliptic curves) via the endomorphism ring. Weil's full proofs required
  him to rebuild the foundations of algebraic geometry over arbitrary fields, published as
  *Sur les courbes algébriques et les variétés qui s'en déduisent* (Hermann, Actualités
  Sci. Ind. 1041, 1948) — the 1948 book is not freely available; citation recorded here.
- **Status:** Theorem (1941/1948). The founding result of the entire family.
- **Assessment:** This is the proof everyone wants to transplant. The two essential
  ingredients — a two-dimensional ambient space C x C over the field of constants, and a
  positivity theorem for divisor classes on it — are precisely what number fields lack:
  Spec Z has no visible field of constants, so "Spec Z x Spec Z" collapses to Spec Z.

### 2. Weil, "Numbers of solutions of equations in finite fields" (1949)
- **Authors/venue:** André Weil; Bull. Amer. Math. Soc. 55 (1949), 497–508.
- **Links:** AMS (bot-blocked); mirror https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/weil.pdf
- **Local file:** `Weil-1949-numbers-of-solutions.pdf`
- **Summary:** The paper stating the **Weil conjectures**: for a smooth projective variety
  over F_q, the zeta function is rational, satisfies a functional equation, and its
  reciprocal roots have absolute value q^{i/2} ("RH"), with degrees given by Betti numbers
  of a complex lift. Verified for diagonal hypersurfaces via Gauss/Jacobi sums. The
  explicit suggestion that a good cohomology theory ("Weil cohomology") with a Lefschetz
  fixed-point formula for Frobenius would explain everything launched Grothendieck's
  program (étale cohomology, motives).
- **Status:** All conjectures proved (Dwork 1960 rationality; Grothendieck et al.
  1960s rationality + functional equation via l-adic cohomology; Deligne 1974 RH).
- **Assessment:** The template: RH as an eigenvalue bound for Frobenius on cohomology.
  Every program below is an attempt to manufacture the analogous operator for Spec Z.

### 3. Bombieri, "Counting points on curves over finite fields (d'après S. A. Stepanov)" (1973)
- **Authors/venue:** Enrico Bombieri; Séminaire Bourbaki 1972/73, exposé 430, p. 234–241.
- **Links:** https://www.numdam.org/article/SB_1972-1973__15__234_0.pdf
- **Local file:** `Bombieri-1973-stepanov-bourbaki.pdf`
- **Summary:** Bombieri's streamlined exposition of Stepanov's 1969 elementary method:
  an auxiliary polynomial with a high-order zero forced along the Frobenius graph yields
  the bound N ≤ q + 1 + (2g+1)q^{1/2} in a few pages, using only Riemann–Roch on the curve
  itself (no surface, no Jacobian, no l-adic cohomology). Combined with the functional
  equation and Galois-descent tricks this reproves Weil's RH for curves in full.
- **Status:** Theorem; the standard "elementary" proof (cf. also Schmidt's version in
  Bombieri's later writings).
- **Assessment:** Important calibration point: RH in the function-field world is so robust
  it even has elementary proofs. Nothing remotely analogous — not even the elementary
  route — is known to start for Q, which suggests the missing ingredient is structural
  (the geometry), not technical.

### 4. Hindry, "La preuve par André Weil de l'hypothèse de Riemann pour une courbe sur un corps fini" (2012)
- **Authors/venue:** Marc Hindry; Journées mathématiques X-UPS 2012 ("Henri Cartan &
  André Weil"), Éditions de l'École polytechnique / Centre Mersenne.
- **Links:** https://proceedings.centre-mersenne.org/articles/10.5802/xups.2012-02/
- **Local file:** `Hindry-2012-weil-proof-expose.pdf`
- **Summary:** A modern, self-contained exposition (in French) of Weil's proof via
  intersection theory on C x C, including the Castelnuovo–Severi inequality, the
  Mattuck–Tate/Grothendieck simplification deriving it from Riemann–Roch on the surface,
  and the historical background (Artin, Schmidt, Hasse). One of the best pedagogical
  entries into exactly the argument Connes–Consani are trying to transplant.
- **Status:** Expository.
- **Assessment:** Reading this next to Connes–Consani's "Riemann–Roch strategy" papers
  makes the transplant plan concrete: every step (surface, correspondences, RR, Hodge
  index) has an intended tropical/adelic counterpart.

### 5. Milne, "The Riemann Hypothesis over Finite Fields: From Weil to the Present Day" (2015)
- **Authors/venue:** James S. Milne; arXiv:1509.00797; published in *The Legacy of
  Bernhard Riemann After One Hundred and Fifty Years* (ALM 35, 2016).
- **Links:** https://arxiv.org/abs/1509.00797 ; https://www.jmilne.org
- **Local file:** `Milne-2015-RH-finite-fields.pdf`
- **Summary:** The definitive 67-page historical-mathematical survey of the whole arc:
  Artin's thesis, Schmidt, Hasse's elliptic proofs, Weil's two 1948 proofs (intersection
  theory on C x C; positivity via the Rosati involution on the Jacobian), the Weil
  conjectures, Grothendieck's étale cohomology and standard conjectures, and Deligne's
  proofs. Milne emphasizes throughout that in every proof RH is ultimately a positivity
  statement (Castelnuovo–Severi, Rosati positivity, Deligne's weights).
- **Status:** Survey of theorems.
- **Assessment:** The best single map of the terrain that any transplant must reproduce.

---

## B. Deligne and the Weil conjectures — the model result

### 6. Deligne, "La conjecture de Weil : I" (1974)
- **Authors/venue:** Pierre Deligne; Publ. Math. IHÉS 43 (1974), 273–307.
- **Links:** http://www.numdam.org/item/PMIHES_1974__43__273_0/
- **Local file:** `Deligne-1974-weil-I.pdf`
- **Summary:** The proof of the last and hardest Weil conjecture: for X smooth projective
  over F_q the Frobenius eigenvalues on H^i have absolute value q^{i/2}. The proof
  combines Grothendieck's l-adic machinery with two new inputs: the monodromy theory of
  Lefschetz pencils (Kazhdan–Margulis big monodromy) and the "Rankin squaring" trick
  imported from analytic number theory (even tensor powers of a local system force
  eigenvalue bounds because a certain L-function has nonnegative coefficients).
  Spectacularly, it bypasses the standard conjectures entirely.
- **Status:** Theorem. Fields Medal 1978.
- **Assessment:** The model result the whole category aspires to. Its lesson cuts both
  ways: positivity of *coefficients* (Rankin) substituted for positivity of an
  *intersection form* — i.e., even in char p, the "Weil-style" positivity route was
  abandoned for a sneakier one. Transplanters should remember that the successful proof
  did not follow the standard-conjectures script either.

### 7. Deligne, "La conjecture de Weil : II" (1980)
- **Authors/venue:** Pierre Deligne; Publ. Math. IHÉS 52 (1980), 137–252.
- **Links:** http://www.numdam.org/item/PMIHES_1980__52__137_0/
- **Local file:** `Deligne-1980-weil-II.pdf`
- **Summary:** The vast generalization: weights of Frobenius on the cohomology of
  arbitrary constructible l-adic sheaves on arbitrary schemes over F_q, with the theory of
  weights, the key "target theorem" on pushforwards (weights do not increase), and the
  equidistribution theorem for Frobenius conjugacy classes. This is the version that
  powers modern applications (exponential sums, the geometric Langlands-adjacent world,
  perverse sheaves via BBD).
- **Status:** Theorem.
- **Assessment:** Shows what a mature cohomological theory of weights looks like — the
  gold standard that a hypothetical "absolute cohomology of Spec Z" (Deninger's H^1) would
  have to match.

### 8. Katz, "An overview of Deligne's proof of the Riemann hypothesis for varieties over finite fields" (1976)
- **Authors/venue:** Nicholas M. Katz; in *Mathematical Developments Arising from Hilbert
  Problems*, Proc. Symp. Pure Math. 28, AMS 1976, 275–305.
- **Links:** https://web.math.princeton.edu/~nmk/old/DeligneRHOverview.pdf
- **Local file:** `Katz-1976-overview-deligne-proof.pdf` (scanned, no text layer)
- **Summary:** The classic expository account of Weil I written for the Hilbert-problems
  volume: the history of Hilbert's 8th problem in char p, the formal structure of the
  l-adic proof, Lefschetz pencils, monodromy, and the squaring argument, with Katz's
  characteristic clarity about what each ingredient is really doing.
- **Status:** Expository.
- **Assessment:** Still the best first read on Weil I; makes clear how much of the proof
  is about *families* (pencils) — a mechanism with no obvious Spec Z analogue.

---

## C. Standard conjectures and motives — why the classical dream stalls

### 9. Grothendieck, "Standard conjectures on algebraic cycles" (1969)
- **Authors/venue:** Alexander Grothendieck; in *Algebraic Geometry* (Bombay Colloquium
  1968), Oxford Univ. Press 1969, 193–199.
- **Links:** https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/StandardConjs.pdf
- **Local file:** `Grothendieck-1969-standard-conjectures.pdf`
- **Summary:** Grothendieck's program to prove the Weil conjectures "the right way": the
  Lefschetz standard conjecture (algebraicity of the inverse Lefschetz operator) and the
  Hodge standard conjecture (positive-definiteness of the intersection pairing on primitive
  algebraic classes). Together with the formalism of pure motives they would yield RH over
  finite fields by Weil's positivity argument, abstractly — Serre's 1960 "Kähler analogue"
  (Ann. Math. 71) proves exactly this shape of theorem for complex Kähler manifolds.
- **Status:** Open (over 55 years). Known in special cases (abelian varieties in char 0
  for Lefschetz-type; Milne has shown Hodge-standard consequences for abelian varieties
  over finite fields). Deligne proved RH without them.
- **Assessment:** The historical high-water mark of the "conceptual" route — and its
  cautionary tale: even in char p, where everything is in place, the positivity conjecture
  (Hodge standard) resists. The number-field dream needs an *additional* miracle on top:
  a site over which Spec Z x Spec Z is two-dimensional.

### 10. Milne, "Polarizations and Grothendieck's standard conjectures" (2002)
- **Authors/venue:** J. S. Milne; Ann. of Math. 155 (2002), 599–610.
- **Links:** https://www.jmilne.org/math/articles/2002aS.pdf
- **Local file:** `Milne-2002-polarizations-standard-conjectures.pdf`
- **Summary:** Proves that the Hodge standard conjecture holds for abelian varieties over
  finite fields if one admits the Tate conjecture-flavored "rationality" of certain Weil
  classes; more precisely it reduces the Hodge standard conjecture for abelian varieties
  in char p to a statement about polarizations of abelian motives. A rare piece of genuine
  progress on the positivity half of the standard conjectures.
- **Status:** Theorem (conditional reduction).
- **Assessment:** Illustrates the state of the art on "motivic positivity": partial,
  conditional, and confined to abelian varieties — sobering for anyone hoping the motivic
  route will soon reach Spec Z.

### 11. Milne, "Motives — Grothendieck's Dream" (2012)
- **Authors/venue:** J. S. Milne; expository note (xnotes), jmilne.org; also in *Open
  problems and surveys of contemporary mathematics* (2013).
- **Links:** https://www.jmilne.org/math/xnotes/MOT.pdf
- **Local file:** `Milne-2012-motives-grothendiecks-dream.pdf`
- **Summary:** A short survey of the category of motives as the universal cohomology,
  what the standard conjectures would buy (semisimplicity, weights, RH over F_q), and the
  modern workarounds. Ends with the number-field horizon: the motivic formalism explains
  the shape of the conjectures on special values and zeros but does not by itself provide
  the "absolute" cohomology of Spec Z.
- **Status:** Expository.
- **Assessment:** Good on *why the classical dream stalls*: motives over F_q have a
  Frobenius; motives over Q have instead a conjectural "motivic Galois group" flow — a
  ghost of Deninger's flow — with no construction in sight.

---

## D. The field with one element (F1)

*Background citation (no free PDF): J. Tits, "Sur les analogues algébriques des groupes
semi-simples complexes", Colloque d'algèbre supérieure Bruxelles 1956 (1957) — the origin
of the F1 idea: Chevalley groups over "F1" should be Weyl groups.*

### 12. Manin, "Lectures on zeta functions and motives (according to Deninger and Kurokawa)" (1995)
- **Authors/venue:** Yuri I. Manin; Astérisque 228 (1995), 121–163 (Columbia lectures 1991/92).
- **Links:** http://www.numdam.org/item/AST_1995__228__121_0/
- **Local file:** `Manin-1995-lectures-zeta-motives.pdf`
- **Summary:** The charter document of modern F1-ology. Manin synthesizes Deninger's
  regularized-determinant formulas and Kurokawa's absolute tensor products into the dream:
  Riemann zeta should be the zeta of a motive over F1; Spec Z is a curve over F1; the
  Gamma factor is the zeta of the "infinite-dimensional projective space over F1"; RH
  would follow from a Weil-style argument on Spec Z x_F1 Spec Z. Proposes zeta functions
  of F1-motives (s-shifted factors s, s−1, ...) matching Soulé's later computations.
- **Status:** Programmatic; the individual computations are theorems, the program is open.
- **Assessment:** Sets the precise target all F1 formalisms have since been measured
  against — and none has hit: producing Riemann zeta itself (not just rational
  combinations of s-factors) as a cohomological zeta over F1.

### 13. Soulé, "Les variétés sur le corps à un élément" (2004)
- **Authors/venue:** Christophe Soulé; Moscow Math. J. 4 (2004), 217–244; arXiv:math/0304444.
- **Links:** https://arxiv.org/abs/math/0304444
- **Local file:** `Soule-2003-varietes-F1.pdf`
- **Summary:** The first serious *definition* of varieties over F1: functors on flat
  finite rings with a universality condition against complex algebras, an associated zeta
  function defined via the counting function N(q) evaluated "at q = 1" (regularized), and
  the theorem that smooth toric varieties are defined over F1 with zeta functions equal to
  products of factors 1/(s−i). Conjectures that objects over F1 base-change to Z.
- **Status:** Theorems for toric-type varieties; the class of F1-varieties turned out
  disappointingly small (later work by Connes–Consani, Deitmar: essentially toric).
- **Assessment:** Honest progress that exposed the core problem: every rigid descent-to-F1
  formalism captures only combinatorial (toric/monoidal) geometry, far short of the
  arithmetic of Spec Z; the zeta functions produced are rational, never transcendental.

### 14. Deitmar, "Schemes over F1" (2005)
- **Authors/venue:** Anton Deitmar; in *Number Fields and Function Fields — Two Parallel
  Worlds*, Progr. Math. 239, Birkhäuser 2005; arXiv:math/0404185.
- **Links:** https://arxiv.org/abs/math/0404185
- **Local file:** `Deitmar-2004-schemes-over-F1.pdf`
- **Summary:** Develops F1-schemes as monoid schemes (prime spectra of commutative
  monoids, glued), with base extension to Z sending a monoid A to Z[A]. Clean and minimal;
  Deitmar later proved that connected integral F1-schemes of finite type whose
  base-change is a variety are exactly toric varieties — a no-go theorem for this naive
  approach.
- **Status:** Theory complete; scope provably limited (toric).
- **Assessment:** Valuable as the sharpest negative result: monoids alone cannot see
  addition, hence cannot see Spec Z as a curve. Any successful F1 must smuggle in additive
  structure (Borger's Λ-rings, Connes–Consani's Γ-rings/S-algebras do exactly this).

### 15. Borger, "Λ-rings and the field with one element" (2009)
- **Authors/venue:** James Borger; arXiv:0906.3146.
- **Links:** https://arxiv.org/abs/0906.3146
- **Local file:** `Borger-2009-lambda-rings-F1.pdf`
- **Summary:** Proposes that descent data from Z to F1 *is* a Λ-ring structure: a
  commutative ring with commuting Frobenius lifts at all primes (equivalently a
  coaction of the big Witt vector functor). F1-algebras are Λ-rings; the base-change
  adjoints produce Witt vectors and arithmetic jet spaces (Buium's p-jets globalized).
  This makes "Frobenius over Z" an actual structure rather than a metaphor and connects
  to Bost–Connes (the BC system is essentially the Λ-structure on Z[Q/Z], as shown by
  Connes–Consani–Marcolli and later Yalkinoglu).
- **Status:** Rigorous framework; widely considered the most structurally satisfying F1;
  no route to RH articulated from it yet.
- **Assessment:** Supplies the missing "Frobenius on Spec Z" in one precise sense
  (commuting Frobenius lifts), but there is no accompanying cohomology with a Lefschetz
  formula, hence no trace-formula bridge to zeta zeros so far.

### 16. Lorscheid, "F1 for everyone" (2018)
- **Authors/venue:** Oliver Lorscheid; Jahresber. Dtsch. Math.-Ver. 120 (2018), 83–116;
  arXiv:1801.05337.
- **Links:** https://arxiv.org/abs/1801.05337
- **Local file:** `Lorscheid-2018-F1-for-everyone.pdf`
- **Summary:** The standard modern survey of the F1 landscape: motivations (Tits'
  q -> 1, Manin's RH dream, torified geometry), then a comparative tour of all the
  formalisms — Soulé, Deitmar monoid schemes, Durov's generalized rings, Haran's
  non-additive geometry, Borger's Λ-rings, Connes–Consani's several versions, Toën–Vaquié,
  and Lorscheid's own blueprints (which interpolate between monoids and rings and support
  Tits' dream about Chevalley groups). Ends with a sober appraisal of the RH motivation.
- **Status:** Survey.
- **Assessment:** The place to see, side by side, that a dozen inequivalent F1's exist and
  that the RH application has migrated away from "counting F1-points" toward the
  Connes–Consani topos/tropical program.

---

## E. Quantum statistical mechanics of Q — the Bost–Connes system

### 17. Bost–Connes, "Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory" (1995)
- **Authors/venue:** Jean-Benoît Bost, Alain Connes; Selecta Math. (N.S.) 1 (1995), 411–457.
- **Links:** https://alainconnes.org/wp-content/uploads/bostconnesscan.pdf
- **Local file:** `BostConnes-1995-hecke-algebras.pdf`
- **Summary:** Constructs a C*-dynamical system (a Hecke algebra from the inclusion of
  the ax+b groups over Z and Q with its canonical time evolution) whose partition function
  is ζ(β): unique KMS state for 0 < β ≤ 1, spontaneous symmetry breaking at β = 1, and
  extremal KMS_∞ states parametrized by a principal homogeneous space under
  Gal(Q^ab/Q), on which the Galois group acts through values of the states on an
  arithmetic subalgebra — recovering class field theory for Q from quantum statistical
  mechanics.
- **Status:** Theorem; the founding object of the arithmetic-QSM subfield.
- **Assessment:** Not an attack on RH per se, but the ancestor of the adele class space:
  the dual system of the BC system is exactly Connes' 1998 space. It also anchors the
  F1 connection (BC = Λ-structure on roots of unity). Its "phase transition at β = 1"
  remains the most suggestive physics-flavored fact about ζ in this program.

### 18. Connes–Marcolli, "Quantum statistical mechanics of Q-lattices" (2004)
- **Authors/venue:** Alain Connes, Matilde Marcolli; "From physics to number theory via
  noncommutative geometry, Part I", in *Frontiers in Number Theory, Physics and Geometry
  I* (Springer 2006); arXiv:math/0404128.
- **Links:** https://arxiv.org/abs/math/0404128
- **Local file:** `ConnesMarcolli-2004-qlattices-QSM.pdf`
- **Summary:** Reinterprets BC as the system of 1-dimensional Q-lattices up to scaling and
  constructs the GL(2) analogue (2-dimensional Q-lattices), whose KMS_∞ states realize the
  Galois theory of the modular field; also develops the relation between the BC "dual
  system" and the adele class space, making precise how the spectral realization of zeta
  zeros lives on the dual of the BC system.
- **Status:** Theorems (GL2 phase transition analysis partly with Laca et al. later).
- **Assessment:** Cements the QSM leg of the program and its Galois-theoretic credibility;
  the direct RH content is inherited from, not added to, the 1998 trace formula picture.

---

## F. Connes' spectral realization and trace formula (1998) — the anchor

### 19. Connes, "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function" (1998)
- **Authors/venue:** Alain Connes; Selecta Math. (N.S.) 5 (1999), 29–106; arXiv:math/9811068.
- **Links:** https://arxiv.org/abs/math/9811068
- **Local file:** `Connes-1998-trace-formula.pdf`
- **Summary:** Introduces the adele class space X_Q = Q^x \ A_Q with the scaling action of
  the idele class group C_Q, and proves: (i) a spectral realization of the critical zeros
  of ζ (and of all Hecke L-functions) as an *absorption* spectrum in a suitable Sobolev
  completion of function spaces on X_Q — zeros appear in the cokernel/kernel rather than
  as eigenvalues in the naive sense; (ii) a semi-local Lefschetz-type trace formula
  (finitely many places) whose distributional terms are exactly the local terms of the
  Weil explicit formula; and (iii) the statement that validity of the analogous *global*
  trace formula is equivalent to RH. Answers the Hilbert–Pólya question in a twisted
  form: the flow replacing Frobenius is the scaling flow of C_Q on X_Q, and the explicit
  formula becomes a Lefschetz trace formula, with periodic orbits at the places of Q.
- **Status:** Semi-local trace formula: theorem (also proved in all-place semi-local form
  later; the delicate global version is what positivity is about). Spectral realization:
  theorem.
- **Assessment:** The single most load-bearing paper of the noncommutative program: it
  converts RH into a positivity/trace statement about a concrete flow. The obstruction it
  exposes is equally concrete: the global trace formula requires controlling the
  interference of all places at once, which is exactly Weil positivity — nothing less.

### 20. Connes, "An essay on the Riemann Hypothesis" (2015)
- **Authors/venue:** Alain Connes; in *Open Problems in Mathematics* (Nash & Rassias eds.,
  Springer 2016); arXiv:1509.05576.
- **Links:** https://arxiv.org/abs/1509.05576
- **Local file:** `Connes-2015-essay-on-RH.pdf`
- **Summary:** Connes' own comparative survey — the best insider account of this whole
  category. Organizes RH attacks into: the "Riemann–Weil explicit formula + positivity"
  route, the Hilbert–Pólya spectral route, and the geometric route through F1; explains
  the arithmetic/scaling site discoveries as the search for the geometry underlying his
  1998 trace formula; states the three-step "Riemann–Roch strategy" (curve = scaling
  site, surface = its square, positivity via a tropical Hodge index theorem) and
  candidly lists what is missing at each step.
- **Status:** Survey/program.
- **Assessment:** Required reading for the assessment question; notably frank that the
  archimedean place and the passage from semi-local to global are where all known
  approaches meet the same wall.

---

## G. The Connes–Consani program: sites, Riemann–Roch, Weil positivity, spectral triples

### 21. Connes–Consani, "The Arithmetic Site / Le Site Arithmétique" (2014)
- **Authors/venue:** C. R. Math. Acad. Sci. Paris 352 (2014), 971–975; arXiv:1405.4527.
- **Links:** https://arxiv.org/abs/1405.4527
- **Local file:** `ConnesConsani-2014-arithmetic-site.pdf` (announcement note)
- **Summary:** Defines the arithmetic site: the topos of sets with an action of the
  multiplicative monoid N^x ("N-hat"), with structure sheaf the tropical semiring Z_max
  (characteristic 1). Main theorem: the points of the arithmetic site over the tropical
  reals R_+^max are canonically the adele class space Q^x \ A_Q / Z-hat^x, i.e., precisely
  the noncommutative space of the 1998 trace formula, and the Frobenius automorphisms
  Fr_λ of R_+^max induce the scaling flow. Zeta appears as the Hasse–Weil counting
  function of this site.
- **Status:** Theorems.
- **Assessment:** The conceptual pivot of the last decade: the mysterious adele class
  space is revealed as the points of an explicit (semi)ringed topos of char 1 — giving,
  for the first time, an actual "geometry over F1-like scalars" whose points know zeta.

### 22. Connes–Consani, "Geometry of the Arithmetic Site" (2015/2016)
- **Authors/venue:** Adv. Math. 291 (2016), 274–329; arXiv:1502.05580.
- **Links:** https://arxiv.org/abs/1502.05580
- **Local file:** `ConnesConsani-2015-geometry-arithmetic-site.pdf`
- **Summary:** The full development of the announcement: proofs of the points theorem,
  the square of the arithmetic site with its Frobenius correspondences (composition laws
  of correspondences hold up to controlled defects), and the counting function whose
  Hasse–Weil-style zeta over F1 is riemann zeta completed — establishing the site as a
  candidate "curve" whose square supports correspondences as in Weil's proof.
- **Status:** Theorems.
- **Assessment:** Delivers a genuine (2-dimensional!) square with Frobenius
  correspondences — the first formalism where "Spec Z x Spec Z" does not collapse. The
  open end is that the square lives in characteristic 1, and the needed cohomological /
  positivity tools there must be built from scratch.

### 23. Connes–Consani, "Geometry of the Scaling Site" (2016)
- **Authors/venue:** Selecta Math. (N.S.) 23 (2017), 1803–1850; arXiv:1603.03191
  (announcement: C. R. Math. 354 (2016), 1–6).
- **Links:** https://arxiv.org/abs/1603.03191
- **Local file:** `ConnesConsani-2016-scaling-site.pdf`
- **Summary:** Extends scalars of the arithmetic site to R_+^max: the scaling site is the
  topos [0,∞) ⋊ N^x, a "curve" over the tropical semifield with structure sheaf of
  piecewise-affine convex functions. Its periodic orbits C_p (one for each prime, of
  length log p) carry a full tropical theory of divisors: degree, Jacobian J(C_p),
  and a Riemann–Roch theorem on each C_p with the expected shape (dim H^0(D) −
  dim H^1(D) = deg D + ...), where dimensions are real-valued (continuous dimensions à la
  von Neumann).
- **Status:** Theorems (RR on the periodic orbits).
- **Assessment:** The "curve" of the strategy now exists and has Riemann–Roch on its
  closed orbits. The gap: RR on the orbits is the analogue of RR on the fibers, not yet
  the Castelnuovo–Severi-grade statement on the *square* that Weil's argument consumes.

### 24. Connes–Consani, "The Riemann–Roch strategy: Complex lift of the Scaling Site" (2018)
- **Authors/venue:** in *Advances in Noncommutative Geometry* (Springer 2019), 53–125;
  arXiv:1805.10501.
- **Links:** https://arxiv.org/abs/1805.10501
- **Local file:** `ConnesConsani-2018-riemann-roch-strategy-complex-lift.pdf`
- **Summary:** States the transplant plan in full: adapt Weil's proof in the
  Mattuck–Tate–Grothendieck form (deduce RH from Riemann–Roch on the square via the
  Hodge index inequality). New step: "tropical descent" from a Riemann–Roch theorem over
  C to existence results in characteristic 1, using Bohr–Jessen–Tornehave almost-periodic
  function theory. Main construction: a complex lift of the adele class space as a moduli
  space of elliptic curves with "triangular structure" (noncommutativity generated by
  isogenies), tightly related to the GL(2)-system, with a lift of the Frobenius
  correspondences via the Witt construction in characteristic 1.
- **Status:** Program + partial constructions (the lift exists; the descended RR does not yet).
- **Assessment:** This is the clearest published statement of exactly which theorem would
  imply RH in their framework: a Riemann–Roch inequality on the square of the scaling
  site strong enough to run the Castelnuovo–Severi argument. Everything since 2020 can be
  read as building the pieces (integer-dimension cohomology, Serre duality, Jacobian).

### 25. Connes–Consani, "Weil positivity and trace formula: the archimedean place" (2020)
- **Authors/venue:** Selecta Math. (N.S.) 27 (2021), art. 77; arXiv:2006.13771.
- **Links:** https://arxiv.org/abs/2006.13771
- **Local file:** `ConnesConsani-2020-weil-positivity-archimedean.pdf`
- **Summary:** The direct attack on the positivity bridge. Using the Hilbert-space
  framework of the semi-local trace formula at the single archimedean place, they prove
  (Theorem 1): for any smooth g supported in [2^{-1/2}, 2^{1/2}] with Fourier transform
  vanishing at i/2 and 0, W_∞(g * g^*) ≥ Tr(θ(g) S θ(g)^*) ≥ 0 — i.e., **unconditional
  Weil positivity at the archimedean place for test functions of support ratio ≤ 2**,
  with the positive lower bound given by the trace of the scaling action compressed onto
  Sonin space (the orthogonal complement of the phase-space cutoff projections at Λ = 1).
  The control uses prolate spheroidal wave functions and hermitian Toeplitz matrix theory;
  they emphasize all ingredients make sense in the general semi-local case, where full
  Weil positivity implies RH.
- **Status:** Theorem (restricted support, one place); the conceptual mechanism
  ("positivity = quantum-mechanical absorption into Sonin space") is the paper's real claim.
- **Assessment:** The furthest anyone has ever pushed an *unconditional* positivity result
  of the exact kind that is equivalent to RH. The crux is now quantitative: extend the
  support interval (each doubling of support ratio adds a prime's worth of interference)
  and add the finite places without losing the trace lower bound.

### 26. Connes–Consani, "Spectral triples and ζ-cycles" (2021)
- **Authors/venue:** L'Enseignement Math. 69 (2023), 93–148; arXiv:2106.01715.
- **Links:** https://arxiv.org/abs/2106.01715
- **Local file:** `ConnesConsani-2021-zeta-cycles.pdf`
- **Summary:** Studies what happens when the support bound S grows: the Weil quadratic
  form acquires very small eigenvalues, whose eigenvectors are finite arithmetic sums of
  prolate spheroidal functions — quantifying exactly how positivity degrades outside the
  proven range. Introduces "ζ-cycles": circles of length L = 2 log S whose conditioned
  spectral triple has low-lying spectrum matching the low critical zeros; reproduces the
  first 31 zeros numerically with astronomically small probability of coincidence, and
  proves the main structural theorem relating ζ-cycles to the 1998 spectral realization.
- **Status:** Theorems + strong numerics.
- **Assessment:** Both encouraging (the zeros demonstrably emerge from finite, local,
  computable data) and clarifying about the obstruction: the small eigenvalues encode the
  primes entering the window, so global positivity must *use* the primes, not fight them.

### 27. Connes–Consani, "Riemann–Roch for Spec Z-bar" (2022)
- **Authors/venue:** Bull. Sci. Math. 187 (2023), art. 103295; arXiv:2205.01391.
- **Links:** https://arxiv.org/abs/2205.01391
- **Local file:** `ConnesConsani-2022-riemann-roch-speczbar.pdf`
- **Summary:** Proves a genuine Riemann–Roch theorem for Arakelov divisors on the
  compactification of Spec Z with **integer-valued** Euler characteristic: they define
  cohomologies H^0(D), H^1(D) with integer dimensions (via a universal arithmetic theory
  over the sphere spectrum using Segal's Γ-rings), establish Serre duality, and prove
  χ(D) = deg' D + log' 2 -type formula paralleling Weil's adelic proof for function fields
  including Pontryagin duality. Sharpened in "Riemann–Roch for the ring Z"
  (C. R. Math. 362 (2024), 229–235; arXiv:2306.00456; local file
  `ConnesConsani-2023-riemann-roch-ring-Z.pdf`) where, over the absolute base S, the
  formula becomes exactly χ(D) = deg D + 1 — Spec Z-bar behaves as a genus-0 curve.
- **Status:** Theorems.
- **Assessment:** A real milestone: the first Riemann–Roch over "the absolute point" with
  integer dimensions, replacing the asymptotic Arakelov-theoretic analogues (Lang,
  Gillet–Soulé, van der Geer–Schoof h^0). Still one-dimensional: it is RR for the curve,
  and the strategy needs RR + Hodge index for the square.

### 28. Connes–Consani–Moscovici, "Zeta zeros and prolate wave operators" (2023)
- **Authors/venue:** arXiv:2310.18423 (v2 May 2024; final version on alainconnes.org, 2024).
- **Links:** https://arxiv.org/abs/2310.18423
- **Local file:** `ConnesConsaniMoscovici-2023-prolate-wave-operators.pdf`
- **Summary:** Integrates the two discoveries (low-zero spectral realization; UV behavior
  of zeros from Sonin space — cf. their PNAS 119 (2022) note "The UV prolate spectrum
  matches the zeros of zeta", citation recorded) into the semi-local trace formula by
  constructing a semi-local analogue of the prolate wave operator; proves stability of the
  semi-local Sonin space as the finite set of places grows and relates everything to de
  Branges spaces of entire functions and the metaplectic representation of Mp(2,R).
- **Status:** Theorems (structural); the RH-relevant spectral identification remains
  conjectural.
- **Assessment:** Technically the deepest of the operator-theoretic papers: it shows the
  archimedean mechanism survives adding finite places — the precise property the 2020
  positivity proof needs in order to scale up.

### 29. Connes–Consani, "Knots, Primes and the adele class space" (2024) and "Knots, primes and class field theory" (2025)
- **Authors/venue:** arXiv:2401.08401; arXiv:2501.06560.
- **Links:** https://arxiv.org/abs/2401.08401 ; https://arxiv.org/abs/2501.06560
- **Local files:** `ConnesConsani-2024-knots-primes-adele-class-space.pdf`,
  `ConnesConsani-2025-knots-primes-class-field-theory.pdf`
- **Summary:** Shows the scaling site with its periodic orbits C_p (length log p) is a
  geometric realization of the Mazur–Morishita "primes as knots" analogy: the adele class
  space X_Q^ab -> X_Q plays the role of the maximal abelian cover, and the preimage of C_p
  is the mapping torus of Frobenius at p acting on the abelianized étale fundamental group
  of Spec Z_(p) — exhibiting the "linking of p with the other primes". The 2025 sequel
  extends this to a geometric generalization of class field theory for global fields.
- **Status:** Theorems.
- **Assessment:** Not directly an RH attack, but strong evidence that the scaling site is
  "the right space": it independently reproduces arithmetic topology and class field
  theory. Also the meeting point with Deninger's program (see Morishita below).

### 30. Connes–Consani–Moscovici, "Zeta Spectral Triples" (2025)
- **Authors/venue:** arXiv:2511.22755 (Nov 2025).
- **Links:** https://arxiv.org/abs/2511.22755
- **Local file:** `ConnesConsaniMoscovici-2025-zeta-spectral-triples.pdf`
- **Summary:** States an explicit strategy toward RH via spectral realization: construct
  self-adjoint operators D_log^(λ,N) as rank-one perturbations of the spectral triple of
  the scaling operator on [λ^{-1}, λ], built only from the Euler product over primes
  p ≤ λ^2; self-adjointness is guaranteed by an extension of the Carathéodory–Fejér
  theorem for Toeplitz matrices. Numerically the spectra converge to the nontrivial zeros
  as N, λ -> ∞, and they prove the framework results; "a rigorous proof of this
  convergence would establish the Riemann Hypothesis". Regularized determinants of the
  operators are computed and shown to control the analytic picture.
- **Status:** Program + theorems (self-adjointness, structure) + numerics; the
  convergence statement equivalent to RH is open.
- **Assessment:** The current sharp end of the Hilbert–Pólya side of the program: for the
  first time there is a *concrete, finitely-constructed* operator family whose spectral
  convergence is precisely equivalent to RH. The risk, as always, is that proving
  convergence may secretly require the positivity one is trying to establish.

### 31. Connes–Consani, "On the Jacobian of Spec Z" (2026) and "On the Absolute Geometry of Spec Z and the Fargues–Fontaine curve" (2026)
- **Authors/venue:** arXiv:2602.15941 (to appear J. Noncommut. Geom.); arXiv:2606.06604.
- **Links:** https://arxiv.org/abs/2602.15941 ; https://arxiv.org/abs/2606.06604
- **Local files:** `ConnesConsani-2026-jacobian-of-specz.pdf`,
  `ConnesConsani-2026-absolute-geometry-specz.pdf`
- **Summary:** The Jacobian paper interprets the adele class space (its "Riemann sector")
  as the monoidal extension of the Picard group of Spec Z: points are torsion-free rank-1
  abelian groups with rigidifying data extending metrized line bundles of Arakelov theory,
  and the adelic product becomes tensor product — a Picard/Jacobian monoid incorporating
  the singular strata needed for the spectral realization of L-functions. The absolute
  geometry paper constructs the absolute F1-arithmetic curve (Spec Z)_F1 by pulling back
  the F1-structure sheaf of the arithmetic site, and shows its points over a perfectoid
  field parametrize untilts (realizing Scholze's heuristic and connecting to the
  Fargues–Fontaine curve), while its complex points at each p form torsors over Weil
  groups.
- **Status:** Theorems (structural); newest layer of the program.
- **Assessment:** Strategically significant: Weil's proof needs the Jacobian (his second
  1948 proof ran through it), and the absolute curve now connects the char-1 world with
  p-adic (Fargues–Fontaine, perfectoid) geometry — the two most fertile modern geometries
  of Spec Z are being glued into one object. Whether this supplies the missing positivity
  is entirely open.

---

## H. Deninger's program: cohomology, regularized determinants, foliated dynamics

*Background citations (no free PDFs located): C. Deninger, "On the Γ-factors attached to
motives" (Invent. Math. 104, 1991); "Local L-factors of motives and regularized
determinants" (Invent. Math. 107, 1992); "Motivic L-functions and regularized
determinants" (Motives, PSPM 55, 1994); E. Leichtnam, "An invitation to Deninger's work
on arithmetic zeta functions" (Contemp. Math. 387, 2005, 201–236).*

### 32. Deninger, "Some analogies between number theory and dynamical systems on foliated spaces" (1998)
- **Authors/venue:** Christopher Deninger; Doc. Math. Extra Vol. ICM I (1998), 163–186;
  arXiv:math/9809110.
- **Links:** https://arxiv.org/abs/math/9809110
- **Local file:** `Deninger-1998-icm-analogies-dynamical.pdf`
- **Summary:** The ICM plenary statement of the program. Deninger postulates an
  infinite-dimensional cohomology H^i for arithmetic schemes with an R-action ("Frobenius
  flow" θ) such that ζ(s) = det_∞((s − θ)/2π | H^1) / [det_∞ on H^0, H^2]-type formulas
  hold, the explicit formula becomes a Lefschetz trace formula, and RH follows from a
  Hodge-index-style positivity on H^1. He shows the expected properties force the
  underlying space to look like a foliated 3-dimensional dynamical system: primes p as
  closed orbits of length log p, the leafwise cohomology of a codimension-1 foliation
  carrying the flow.
- **Status:** Program; the formalism's internal consistency is proved, the spaces are
  conjectural.
- **Assessment:** The cleanest axiomatization of "what a proof would look like": everyone
  (including Connes–Consani, whose scaling site has exactly the predicted orbit structure)
  is effectively hunting Deninger's site. The crux he isolated — a Kähler-type positivity
  (analogue of the Hodge index theorem) on leafwise H^1 — is the same crux as Weil
  positivity.

### 33. Deninger, "Dynamical systems for arithmetic schemes" (2018–2024)
- **Authors/venue:** arXiv:1807.06400 (v4, Feb 2024, 119 pp.).
- **Links:** https://arxiv.org/abs/1807.06400
- **Local file:** `Deninger-2018-dynamical-systems-arithmetic-schemes.pdf`
- **Summary:** After twenty years, an actual construction: a functor X ↦ (X_∞, φ^t) from
  arithmetic schemes to dynamical systems, built from rational Witt vectors / ideles,
  whose periodic orbits correspond to the closed points x with lengths log N(x); for
  Spec Z the system's orbit structure matches the ICM-1998 predictions. The spaces are
  infinite-dimensional and not yet the conjectured 3-manifold-like foliated spaces, but
  they are genuinely functorial and support the beginnings of transverse index theory
  (continued in later work with Kucharczyk and others, e.g. "Primes, knots and periodic
  orbits", arXiv:2301.11643, local file `Deninger-2023-primes-knots-periodic-orbits.pdf`,
  which surveys the dynamical picture and its arithmetic-topology interface).
- **Status:** Construction is a theorem; the required cohomological properties
  (finite-dimensionality of leafwise H^1 in the appropriate sense, trace formula,
  positivity) remain open.
- **Assessment:** Deninger's program moved from pure axiomatics to a concrete candidate
  space — major progress — but the analytic core (a Lefschetz trace formula with the
  right archimedean terms, then positivity) is untouched. The bet is that "analysis on
  the right infinite-dimensional foliated space" is easier than "algebra over F1"; nobody
  knows.

### 34. Morishita, "On a relation between Deninger's foliated dynamical systems and Connes–Consani's adelic spaces" (2025)
- **Authors/venue:** Masanori Morishita; arXiv:2508.15971 (v5, Jan 2026).
- **Links:** https://arxiv.org/abs/2508.15971
- **Local file:** `Morishita-2025-deninger-vs-connes-consani.pdf`
- **Summary:** Proves a precise relation between Deninger's conjectural foliated
  dynamical systems for abelian number fields and the Connes–Consani adelic spaces
  (scaling site and its abelian cover), fitting both into the knots-primes dictionary of
  arithmetic topology and giving a geometric view of class field theory that both
  programs share.
- **Status:** Theorem-level comparison by the founder of arithmetic topology.
- **Assessment:** Evidence that the two main living programs in this category are looking
  at the *same* conjectural geometry from two sides (topos/char-1 vs. foliations/analysis)
  — which raises confidence in the target space while also implying they will likely hit
  the same final wall (archimedean positivity).

---

## I. The bridge: Weil's explicit formula and positivity; outside commentary

### 35. Weil's explicit formula and positivity criterion (1952) — citation entry
- **Citations:** A. Weil, "Sur les 'formules explicites' de la théorie des nombres
  premiers", Comm. Sém. Math. Univ. Lund (1952), 252–265; and "Sur les formules
  explicites de la théorie des nombres", Izv. Akad. Nauk SSSR 36 (1972). No free scan
  located. Modern exposition: E. Bombieri, "Remarks on Weil's quadratic functional in
  the theory of prime numbers, I", Rend. Mat. Acc. Lincei (9) 11 (2000), 183–233
  (citation recorded); also Appendix B–C of `ConnesConsani-2020-weil-positivity-archimedean.pdf`
  and Section 2 of `Connes-2015-essay-on-RH.pdf`, both downloaded.
- **Summary:** Weil rewrote the Riemann–von Mangoldt explicit formula as a distributional
  identity: sum over zeros of f-hat evaluated at the zeros = sum over places v of local
  terms W_v(f), and proved: **RH holds iff the Weil distribution is nonpositive on the
  cone of functions g * g-bar-sharp** (positivity criterion). Over function fields the
  same criterion holds and is *provable* — it is exactly the Castelnuovo–Severi
  inequality in disguise. This is the precise sense in which RH is a positivity statement
  and the exact interface through which the geometric programs must deliver.
- **Assessment:** The one non-negotiable bridge: any transplant of Weil's proof must
  output this positivity. Connes–Consani are the only group with unconditional partial
  results directly on it (support ratio ≤ 2 at the archimedean place).

### 36. Sarnak, "Problems of the Millennium: The Riemann Hypothesis" (2004)
- **Authors/venue:** Peter Sarnak; Clay Mathematics Institute Annual Report (2004).
- **Links:** https://www.claymath.org/library/annual_report/xSarnak_RH.pdf (also E.
  Bombieri's official Clay problem description, claymath.org, citation recorded).
- **Local file:** `Sarnak-2004-clay-RH.pdf`
- **Summary:** Sarnak's commentary on the state of RH attacks: reviews the function-field
  proofs as the strongest evidence, discusses the Hilbert–Pólya / random-matrix
  (GUE) phenomenology, the Katz–Sarnak function-field symmetry philosophy, and comments
  skeptically but respectfully on the noncommutative-geometry route — his much-quoted
  position being that a proof will need a genuinely new idea beyond the frameworks then
  on offer, while endorsing explicit-formula positivity as the right target.
- **Status:** Survey/commentary.
- **Assessment:** Useful outside calibration: the analytic community's consensus view
  that the geometric programs have reproduced the *language* of the function-field proof
  but not yet any inequality with new arithmetic content — a bar the 2020 archimedean
  positivity theorem has since begun to test.

---

## Other formalisms noted (citations only, deliberately not downloaded)
- N. Durov, "New approach to Arakelov geometry" (arXiv:0704.2030) — generalized rings; F1 as the free monad.
- M. J. Shai Haran, "Non-additive geometry" (Compositio 143, 2007) — another F1; also his "The mysteries of the real prime".
- N. Kurokawa, absolute zeta functions and absolute tensor products (multiple papers) — the q -> 1 calculus feeding Manin's lectures.
- K. Kedlaya / T. Scholze-adjacent analogies (Fargues–Fontaine as "the curve") enter this story only via `ConnesConsani-2026-absolute-geometry-specz.pdf`.
- Mochizuki/IUT: out of scope (abc, not RH).

---

## Overall assessment

**Is the Weil-transplant the most structurally promising route?** Structurally, yes — it
is the only family of approaches with a completed model theorem (RH for function fields,
proved twice over: Weil geometrically, Bombieri–Stepanov elementarily, Deligne in vast
generality) and with an exact, theorem-level statement of what "winning" means: Weil's
1952 positivity criterion, which is *provably equivalent* to RH and *provably true* in
the function-field case for geometric reasons (Hodge index on C x C). No other RH
program (random matrices, de Branges, arithmetic quantum chaos) possesses such a bridge.
What is missing has, however, been the same for seventy years, and the last decade has
made it precise rather than smaller. One needs: (1) the curve — now essentially
delivered: the arithmetic/scaling site (equivalently, in another language, Deninger's
conjectured foliated space, which Morishita has shown is the same target) has Spec Z-like
points, prime periodic orbits of length log p, a Frobenius scaling flow, class field
theory, and a knots-primes dictionary; (2) the surface with correspondences — partially
delivered: the square of the arithmetic site exists in characteristic 1 with Frobenius
correspondences, and Riemann–Roch has been proved for the "curve" (integer-dimension RR
for Spec Z-bar, 2022–2023, χ(D) = deg D + 1 over the sphere spectrum) but *not* for the
square; and (3) the positivity engine — the Castelnuovo–Severi / Hodge-index analogue —
which does not yet exist in characteristic 1 or on any candidate square, and which the
explicit formula says must ultimately absorb the archimedean place. The recurring lesson
from Deligne (who won by abandoning the positivity route for Rankin squaring) is worth
weight here: even the model case suggests the final step may require a trick orthogonal
to the standard-conjectures script, and the standard conjectures themselves — the
positivity half especially — remain open even over finite fields, which is the single
most sobering fact in this whole category.

**Where Connes–Consani actually stand.** Proved, unconditionally: the semi-local trace
formula (1998, extended 2023) whose spectral side realizes the critical zeros as an
absorption spectrum; the identification of the adele class space as the points of an
explicit topos (2014–2016); tropical Riemann–Roch on each periodic orbit C_p (2016); an
integer-valued Riemann–Roch with Serre duality for the Arakelov-compactified Spec Z
(2022, sharpened 2023 to χ(D) = deg D + 1); the Jacobian/Picard-monoid structure of the
adele class space (2026); and — the key partial result on the crux — **Weil positivity at
the archimedean place for test functions supported in [1/√2, √2]** (support ratio ≤ 2,
Fourier transform vanishing at 0 and i/2), with the stronger operator-theoretic lower
bound W_∞(g * g^*) ≥ Tr(θ(g)Sθ(g)^*) via compression onto Sonin space (Selecta 2021),
plus semi-local stability of the Sonin mechanism when finite places are added (2023) and
a concrete operator family (2025 "Zeta Spectral Triples") whose spectral convergence to
the zeros — currently overwhelming numerically but unproven — would *by itself* establish
RH. Not proved, and the honest measure of the distance: positivity for support ratio
beyond 2 (where their own ζ-cycles analysis shows small eigenvalues encoding the primes
must be confronted, so the extension is not a matter of estimates but of using the Euler
product), any Riemann–Roch or Hodge-index statement on the square of the scaling site,
and the global (all places, all supports) trace formula. My read: this is the most
serious, most self-critical, and most cumulative RH program in existence — it has
converted a metaphysical dream into a short list of missing theorems — but each of those
missing theorems (positivity past ratio 2; tropical Hodge index; spectral convergence of
D_log) is plausibly RH-hard in itself, and there is as yet no demonstration that the new
geometric structures make any one of them easier than the original problem. Expected
verdict for the foreseeable future: profound reformulation, genuine partial positivity,
no proof imminent — with the caveat that this is the one program where a single further
inequality would actually finish the job.
