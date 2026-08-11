# P2 — The off-line defect of the Suzuki §7.7 identity, in closed form

Cycle-2 PRIMARY, agent P2 (independent of P1). Reset target parts (ii)-closed-form + (iii)
of RESET-1. Sources: Suzuki 2606.09096 (§7.7, §8; "S26" below) and Suzuki arXiv:2301.00421 v3
("S14"; repo copy `papers/criteria/Suzuki-2023-hilbert-space-weil-distribution-v3.pdf`);
Suzuki JLMS 108 (2023) 1448–1487 ("Aspects") cited through S14/S26. Labels:
PROVED / DERIVED (rigorous modulo an explicitly named import) / HEURISTIC / NUMERICAL.

## 0. Objects and conventions (all unconditional)

z-coordinates: s = 1/2 − iz, zeros of ξ(1/2 − iz) form the multiset Γ, closed under
γ ↦ γ̄ and γ ↦ −γ. A zero ρ = β + iτ_ρ of ζ maps to z = −τ_ρ + i(β − 1/2).

- A(z) := ξ(1/2 − iz) — entire, EVEN, real on ℝ (functional equation), zero set Γ.
- B(z) := ξ′(1/2 − iz) (d/ds). E(z) := A(z) + B(z) = E_ξ of S14 (1.3). E^♯ = A − B.
- S14 (1.5)–(1.6): the screw line S_t(z) = (i(1+Θ)/2)·P_t^♯(z), Θ = E^♯/E,
  P_t as in S14 (3.2) (unconditionally = the arithmetic form (1.6), S14 Prop 3.1):
  P_t(z) = Σ_γ m_γ (e^{−iγt} − 1)/(γ(z − γ)). S_t ∈ L²(ℝ) unconditionally (S14 Prop 1.2).
- Screw kernel G_g(x,y) := g(x−y) − g(x) − g(−y) + g(0), g = g_ξ (S26 (1.3) = S14 (4.3)).
- The §7.7 target identity (true under RH, S14 Thm 4.2 with the π of S14 (4.4)):
  (1/π)⟨S_x, S_y⟩_{L²(ℝ)} = G_g(x,y).
- DEFECT: **D(x,y) := G_g(x,y) − (1/π)⟨S_x, S_y⟩_{L²(ℝ)}** (well-defined without RH:
  Cauchy–Schwarz + Prop 1.2; the T→∞ convergence of the Gram integral is absolute).
- MODEL (the reset's hypothesis): Γ = Γ_c ∪ Q, Γ_c ⊂ ℝ (critical zeros), one off-line
  quadruple Q = {ω, ω̄, −ω, −ω̄}, ω = τ + iδ, τ > 0, 0 < δ < 1/2 (δ = β − 1/2);
  all zeros simple (m ≡ 1; the m_γ ≥ 2 case needs Jordan-chain bases in S14 (3.5) and
  is outside this memo's scope — model hypothesis, stated).

Imports (DEAD-ENDS #11 discipline — imported, not re-derived):
[I1] Zero expansion of the screw kernel, unconditional ("Aspects" (1.9), quoted at S14 (4.6)):
     G_g(x,y) = Σ_γ m_γ (e^{iγx} − 1)(e^{−iγy} − 1)/γ². Cross-check: S14 (4.10)
     ⟨Dψ₁,Dψ₂⟩_g = ⟨ψ₁,ψ₂⟩_W is applied in S14's proof of Thm 4.4 in the RH-FALSE branch,
     so the zero side of G_g is unconditional in Suzuki's own usage. [P-LIT]
[I2] Contour technique for model-space Gram integrals: S14 §4.1 / [15, Prop 3.2]
     (T_n-contours between zero ordinates; arc decay). [P-LIT technique]
[I3] Bombieri 2000 inertia bookkeeping (number of negative squares of the Weil form =
     number of off-line zeros in the upper half-plane): calibration only. [P-LIT]

## 1. Two exact algebraic identities [PROVED, elementary]

(1a) A′(z) = −iB(z), i.e. **E = A + iA′ and E^♯ = A − iA′ exactly.**
     (d/dz ξ(1/2−iz) = −i ξ′(1/2−iz).) Hence on ℝ: A real, iA′ real-to-imag,
     |E|² = EE^♯ = A² + |A′|² > 0 away from multiple real zeros.
(1b) 1 + Θ = 2A/E and |1 + Θ(z)|² = 4A(z)²/(E E^♯)(z) on ℝ, so the Gram integrand is
     S_x conj(S_y) = A²/(EE^♯) · Σ_{γ,γ′} m m a_γ(x) conj(a_{γ′}(y)) /((z−γ)(z−γ̄′)),
     with a_γ(x) := (e^{iγx} − 1)/γ (so S_x = Σ_γ m_γ a_γ(x)·iA/(E·(z−γ))).
(1c) At EVERY simple zero γ₀ ∈ Γ (real or not): H := A/E satisfies H(γ₀) = 0 and
     **H′(γ₀) = A′(γ₀)/E(γ₀) = A′/(iA′) = −i.** Universal; this single constant
     generates all order-1 Gram entries below.

## 2. The shadow zeros of E [PROVED in the model]

THEOREM S (Speiser-type count for ξ + ξ′). In the model, E has EXACTLY two zeros in
ℂ⁺(z) (⇔ ℜs > 1/2): one, p, within O(1) of ω (image of the E-zero near ρ̄₀), and −p̄.
All other E-zeros lie in ℂ⁻ ∪ ℝ-closure.

Proof. E = 0 ⇔ 1 + (ξ′/ξ)(s) = 0. On ℜs = 1/2, ξ′/ξ is purely imaginary (functional
equation + real coefficients), so ℜ(1 + ξ′/ξ) ≡ 1 there; at on-line zeros indent right:
ξ′/ξ ≈ m/(s−s₀) has ℜ > 0 on the right semicircle. In ℜs > 1/2 write ξ′/ξ(s) =
Σ_ρ 1/(s−ρ) (symmetric pairing; no constant). Every on-line term has ℜ > 0; the two
members of the quadruple with ℜρ < 1/2 give ℜ > 0; only ρ₀ = 1/2+δ+iτ and ρ̄₀ can give
negative real part, bounded by 1/dist. Hence ℜ(1 + ξ′/ξ) > 0 everywhere in ℜs > 1/2
at distance > 2 from {ρ₀, ρ̄₀}: no zeros there, and winding on the boundary of each
remaining disk is 0, so (argument principle) #E-zeros = #ξ-poles-of-ξ′/ξ = 1 per disk. ∎

Notes. (i) The same boundary argument run on the full half-plane gives, for any zero
configuration: #{E-zeros, ℜs>1/2} = #{ξ-zeros, ℜs>1/2} — an unconditional Speiser/
Levinson–Montgomery-type equivalence for ξ+ξ′; in particular **E ∈ Hermite–Biehler ⟺ RH**
(⇐ is Lagarias 2006 Thm 1; ⇒ closes via §4 below). [PROVED modulo standard far-field care]
(ii) Location: solving 2w/(w²+δ²) + c = i locally (w = z−τ, c the regular part of A′/A,
|c| ≍ log τ) puts p at height ℑp ≍ δ²... /(1+|c|-corrections); only ℑp > 0 and uniqueness
are load-bearing. [DERIVED-perturbative; existence/uniqueness PROVED]
(iii) Residue r_p := Res_{z=p} A/E = A(p)/E′(p) = −iA(p)/(A(p) + A″(p)) ≠ 0; the
reflection z ↦ −z̄ maps E-zeros to E-zeros with Res_{−p̄} = −r̄_p. [PROVED]

## 3. The Gram matrix without RH [DERIVED (import I2); NUMERICAL to 1e-13]

Let N(γ,γ′) := (1/π)∫_ℝ A²/(EE^♯) · dz/((z−γ)(z−γ̄′)), so that
(1/π)⟨S_x,S_y⟩ = Σ_{γ,γ′} m m a_γ(x) conj(a_{γ′}(y)) N(γ,γ′) (absolute convergence:
Σ m/|γ|² < ∞, |N| uniformly bounded by Cauchy–Schwarz on the diagonal).

Split A²/(EE^♯) = (1/2)(H + H^♯), close H upward, H^♯ downward (|H| ≤ 1 on ℝ always;
in the model |H| ≤ C off two small disks around p, −p̄ and H → 0 at i∞ like 1/log; I2).
With PV/half-residue bookkeeping at real Γ-points and (1c), every case reduces to:

THEOREM N. N(γ,γ′) = N₀(γ,γ′) + R(γ, γ̄′) + conj(R(γ′, γ̄)), where
  R(a,b) := i·r_p/((p−a)(p−b)) − i·r̄_p/((p̄+a)(p̄+b))    (the shadow/Blaschke term),
  N₀ := δ_{γγ′} on Γ_c × Γ_c;  N₀(ω,ω̄) = N₀(ω̄,ω) = N₀(−ω,−ω̄) = N₀(−ω̄,−ω) = 1;
  N₀ = 0 for ALL other pairs (including the quadruple DIAGONAL: N₀(ω,ω) = 0).

Mechanism: H vanishes at every Γ-point (1c), so simple poles at zeros never contribute;
only double points do, always through H′ = −i, producing exactly the entries N₀ = 1;
under RH this collapses to Suzuki's Prop 4.1 orthonormality (calibration check: real
diagonal = 1 = 1/m_γ ✓). The pattern N₀(ω,ω̄) = 1, N₀(ω,ω) = 0 is the hyperbolic
[[0,1],[1,0]] block — the Gram integral couples each off-line zero to its CONJUGATE,
not to itself.

## 4. Order-1 cancellation and the closed form [DERIVED; NUMERICAL to 1e-13]

Pairing [I1] against Theorem N term by term:
G_g's γ-term is a_γ(x)·conj(a_{γ̄}(y)); the N₀-part of the Gram reproduces EXACTLY these
terms — for real γ via δ_{γγ′}, for the quadruple via the ω ↔ ω̄ off-diagonal 1's. Hence:

**THEOREM D0 (order-1 cancellation). The naive off-line block cancels identically:
with R ≡ 0 the defect would be ZERO. The quadruple's direct spectral contribution to
D is invisible; the entire defect is the shadow-zero term.**

What remains is rank ≤ 4. With 𝒫_x(z) := Σ_γ m_γ a_γ(x)/(z−γ) (= P_{−x}(z), a value of
the unconditional S14 resolvent family) and 𝒫^♯_x(p) := conj(𝒫_x(p̄)):

**MAIN CLOSED FORM.  D(x,y) = 2 ℑ[ r_p 𝒫_x(p) 𝒫^♯_y(p) ] + 2 ℑ[ r_p 𝒫_y(p) 𝒫^♯_x(p) ],**

real and symmetric; diagonal **D(x,x) = 4 ℑ[ r_p 𝒫_x(p) 𝒫^♯_x(p) ]**. Under RH there is
no p and D ≡ 0 (consistent with S14 Thm 4.2). Several quadruples: sum the same expression
over their shadow pairs (p_j, −p̄_j). On test functions u (real, and u ∈ L²₀ ⇔ û(0)=0):
⟨Du,u⟩ = 4 ℑ[ r_p Λ₊(u) conj(Λ₋(u)) ],  Λ₊(u) = Σ_γ û(γ)/(γ(p−γ)),  Λ₋ = same at p̄.

## 5. (iii) Sign structure [DERIVED + NUMERICAL]

- D factors through u ↦ (Λ₊(u), Λ₋(u)) ∈ ℂ²; on that reduction it is the Hermitian
  form with matrix [[0, −2i r_p],[2i r̄_p, 0]], eigenvalues **±2|r_p|**: an EXACT
  indefinite block. Over real u: rank 4, **signature (2,2)** — precisely Bombieri's
  count [I3] for one quadruple (2 off-line zeros in the upper half-plane).
- Parity restriction FAILS to rescue one-sidedness: on even u, Λ₋ = conj(Λ₊) and
  ⟨Du,u⟩ = 4ℑ[r_p Λ₊²] — signature (1,1); odd u: −4ℑ[r_p Λ₊²] — (1,1). [NUMERICAL ✓]
- Support restriction FAILS: on windows inside the prime-free range (0, log 2) and on
  L²₀ the block stays (2,2) (evaluation functionals remain surjective — generic
  nondegeneracy [DERIVED]; toy check ✓).
- The only one-sided fragments: (a) D(x,x) = 4ℑ[r_p A′/A(p) conj(A′/A(p̄))]·x² + O(x³)
  near 0 — a fixed sign, but invisible to the form (rank-2 indefiniteness is
  support-independent); (b) nothing else found.
- Growth: for x → ∞, 𝒫_x(p) and 𝒫^♯_x(p) each pick up e^{δx} from the lower quadruple
  members, so D(x,x) oscillates at frequency 2τ inside an envelope **e^{2δ|x|} =
  e^{(2β−1)|x|}** — the T3/e^{(2Θ−1)a} rate dictionary reappears verbatim in the static
  frame (third independent derivation of the same dictionary). [DERIVED]

## 6. Numerical validation [NUMERICAL]

Toy with the exact structure (§1 identities are structure-only): A = Π(z²−γ²) with
Γ_c-part {±1, ±2.5}, quadruple ω = 1.7+0.3i; E = A + iA′. Results: E-roots in ℂ⁺:
exactly {±1.63147 + 0.06478i} (note ℑp ≈ δ²·O(1), off-line-ness partially hidden);
all 12 tested Gram entries match Theorem N to ≤ 8e-14; D(x,y) matches the MAIN CLOSED
FORM at all tested points to ≤ 7e-13; inertia of D on 10 points (2,2); even sector
(1,1); odd sector (1,1); mean-zero subspace (2,2); window (0,0.69) (2,2); full screw
form G_g: (2,6) — exactly two negative directions, the Bombieri mirror. Script:
session scratchpad `p2_check.py` (throwaway; results recorded here).

## 7. Verdict against RESET-1's ABANDONMENT CONDITION

The off-line contribution IS "an indefinite (1,1)-type block exactly mirroring Bombieri
inertia bookkeeping" — (1,1) per parity sector, (2,2) total = Bombieri's count — and NO
exploitable one-sidedness survives parity restriction, prime-free-window restriction,
or L²₀. Moreover the sharpened outcome-B target collapses: D ⪰ 0 ⟺ D ≡ 0 ⟺ E has no
zeros with ℜs > 1/2 ⟺ (Theorem S note (i)) no ξ-zeros with ℜs > 1/2 ⟺ RH. Zero slack,
zero softening — the defect-positivity surrogate is RH restated, in yet another
coordinate system that reproduces the same e^{(2Θ−1)a} dictionary.

**ABANDONMENT TRIGGERED. Static sector: HARD-WALL-COORDINATES. CHALLENGER (Lee–Yang/
FKG) auto-promotes per RESET-1.**

Salvage (genuinely new, keep): (1) Theorem D0 — the naive quadruple block cancels
identically between screw kernel and Gram; the RH-falsity signal lives ENTIRELY at the
shadow zeros of ξ + ξ′, not at the zeros of ξ. Any future positivity attack on the
static identity is an attack on "ξ+ξ′ HB", full stop. (2) The universal constants
A′ = −iB, H′|_Γ = −i, and the exact rank-4 formula — reusable for C1/C2: the shadow
zero p is a REAL-ANALYTIC function of the zero configuration and its ℑp > 0 ⟺ RH-false
is a possible Lee–Yang-style order parameter (hand-off to CHALLENGER). (3) The
RH ⟺ E_ξ ∈ HB equivalence with an explicit defect kernel quantifying the failure.
