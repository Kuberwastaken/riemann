# formal/ — the Lean layer ("RH in Lean = the criterion + the increments")

Started 2026-08-11 after the Claude 2/3 paper shipped a sorry-free Lean 4
formalization whose infrastructure (the Weil explicit formula for Mathlib's ζ in
literature form — `Zeta23.WeilEF.EF_lit_zetaZeroConfig`, hypothesis-free — plus
Γ′/Γ estimates and the PSD/inertia linear algebra) is Apache-2.0 and pinned to
the same Mathlib revision this package uses.

**Honesty first: no proof of RH exists, so no formalization of RH is possible.**
What is possible, and is this directory's program:

1. **The criterion** (`Criterion.lean`, imports Zeta23): Weil positivity ⟺ RH —
   the formal reduction that every future positivity increment plugs into.
   *Status 2026-08-11:* **the forward direction is PROVEN sorry-free** —
   `weil_positivity_of_RH : RiemannHypothesis → WeilPositivityAll` (axiom audit:
   propext/Classical.choice/Quot.sound only), via `EF_lit_zetaZeroConfig` and
   Zeta23's `weilTest` machinery. Formal contrapositive now available: a
   certified strictly-negative arithmetic side at any C²c test function would
   disprove RH. The converse (Bombieri's argument) is the declared open half,
   stated as `WeilCriterion`.
2. **The increments** (this package, Mathlib-only) — *status 2026-08-11: all
   three PROVEN, sorry-free, axiom-audited (propext/Classical.choice/Quot.sound
   only), statements as designed with no added hypotheses*:
   - `Lemma1.lean` — the sharp half-factor bound |g_f(a)| ≤ ½‖f‖² (the
     laboratory's prime-norm bar). **Proven** — indicator support bookkeeping +
     pointwise AM–GM + translation invariance + a.e.-disjointness.
   - `SigmaLPAssembly.lean` — the σ-LP dual assembly inequality, the glue step
     of the T1 certificate (SHARP-FLOOR.md). **Proven.**
   - `T1Certificate.lean` — Ω_W and the admissible class defined concretely;
     T1 at a window as a **conditional** theorem: finitely many named
     spectral-cap hypotheses + Parseval ⊢ full-space Weil positivity.
     **Proven** (integrability of ‖FT f‖² derived from Parseval, not assumed).
     Remaining to make the L = 0.40 instance unconditional: discharge hParseval
     (Mathlib Plancherel, 2π-convention translation) and the caps themselves
     (frequency-side Nyström certification, transported).
3. **The frontier, machine-readable**: the open analytic statements (Lemma X of
   T1-GRADED.md; the caps; the unbounded-support limit) stated as `Prop`s with
   documentation, never as `sorry`s in committed proofs of record.

Build (standalone): `elan` auto-selects the toolchain (v4.33.0-rc2);
`lake exe cache get` fetches prebuilt Mathlib (rev 51e6992, the zeta-23-lean
pin); `lake build`.

Build (current dev arrangement on ai-vps, disk-constrained): the modules are
symlinked into a local clone of anthropics/zeta-23-lean as an extra `lean_lib`
(`RiemannFormal`, globs restricted to the Mathlib-only modules) so one Mathlib
checkout+cache serves both this layer and the future `Criterion.lean` imports of
`Zeta23.*`. Build with `cd <zeta-23-lean clone> && lake build RiemannFormal`.
`Criterion.lean` stays out of the build globs until `lake build Zeta23`
completes (hours).

Files under active proof development may contain `sorry` and say so at the top;
anything announced as *proven* in the repo's logs must build sorry-free.
