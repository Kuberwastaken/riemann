# SHARP-FLOOR: the σ-LP program for T1 (Track D, 2026-08-11)

*Provoked by the Claude 2/3 paper's §7.5(d) (sharp use of finitely many spectral
moments — Chebyshev–Markov–Stieltjes/Christoffel). Everything here is float
pilot numerics on the constrained window space (n = 800–1400 grid, eigsh caps,
HiGHS LP); resolutions ~1e-3. Scripts: `sharp_floor.py`, `sigma_lp.py`,
`sigma_rich.py`, `sigma_t1.py`, `sigma_t1b.py`; raw outputs committed alongside.*

## 1. The question inherited from Theorem A

`PROOF-c0.md` proves G(f) ≥ c₀‖f‖² on the prime-free window by three lemmas:
monotonicity of Ω (M), a **trace cap** on the constrained band mass (T), and a
stochastic-dominance rearrangement (R). The certified constant is 0.349152; the
measured truth is ≈ 0.55; the norm-route target for one-prime T1 is the prime
bar q = (log 2)/√2 = 0.490129 (Lemma 1). FINDINGS.md Tier 5 recorded the
"second-moment ladder" as saturating at 77% of the requirement. This session
re-ran that program with the *sharp* spectral caps.

## 2. Result 1 — the loss is not in Lemma T; Lemma R itself is the wall

Replacing the trace cap by the k-th moment caps (Tr[(B_R|_V)^k])^{1/k}, and by
the EXACT top eigenvalue λ_max(B_R|_V) (constrained prolate), at L₀ = ½log 2
(full resolution, n = 1400, caps every 0.25 up to R = 20):

| cap used | floor |
|---|---|
| trace (= Lemma T, k=1) | 0.3492 *(reproduces the certified 0.349152 — independent validation)* |
| k=2 moment | 0.4279 |
| k=6 moment | 0.4668 |
| **exact λ_max** | **0.4753** |

The moment ladder does NOT structurally saturate at 77% — it converges
geometrically to the exact-cap value (k=6 is within 1.8% of it). But the
exact-cap value itself, i.e. **the ceiling of the entire per-band-cap
rearrangement method, is 0.4753 < 0.4901 at L₀** — and it only decreases with
L. **No refinement of Lemma T can prove T1 through Lemma R.** The missing 0.475
→ 0.55 lives in the coupling across bands: the rearrangement lets a phantom
measure realize the worst band mass at every R simultaneously, which no single
f can do.

## 3. The σ-LP: coupling as linear constraints

For ANY bounded even σ (not necessarily ≥ 0),

    ∫ σ dν_f = ⟨f, σ(D) f⟩ ≤ Λ_σ := λ_max(P_V σ(D) P_V)   (f ∈ V, ‖f‖ = 1),

so any dictionary {σ_j} yields an LP lower bound for inf_f ∫ c dν_f over the
constrained window space, for any cost multiplier c(r): minimize ∫c dν over
ν ≥ 0, ν(total) ≤ 1 (remainder ≥ inf_{r≥Rmax} c), ∫σ_j dν ≤ Λ_j. Indicators
recover §2; the full σ-continuum recovers the exact value. Dictionary: Fejér
pairs σ_{c,a} (closed-form kernels) + cutting-plane unions (§5).

With cost = Ω (the norm route), rich dictionary (84 bumps, widths {1.5,3,6}):
floor(L₀) = **0.4886** — 0.0015 below the bar; floor(0.36) = 0.4507 (0.039
below). The norm route stays marginal-at-best at the window edge and loses fast
inside: **the right vehicle is not the norm route at all.**

Two structural observations with independent value:
- **The valley caps are minuscule** (Λ(σ_{0,3}) ≈ 6·10⁻⁴ at L₀): the two pole
  constraints annihilate low-frequency mass — the Connes–Consani/Sonin
  mechanism, visible as individual LP rows.
- **Certifiability**: on the constrained spectrum the Frobenius caps √Tr[K²]
  are 1.000–1.01 × λ_max for the valley bumps (near-rank-1, TBW < 1). But the
  certified caps MUST carry the rank-2 pole projection (dropping it loses the
  valley mechanism); design in §6.

## 4. Result 2 — the Ω_W identity: aim the LP at T1 itself

For real f, g_f(log 2) = (1/2π)∫|F|²cos(r log 2)dr, hence on the constrained
space the FULL one-prime Weil form is one diagonal multiplier:

    W(f) = (1/2π) ∫ |F(r)|² · Ω_W(r) dr,    Ω_W(r) = Ω(r) − √2 log 2 · cos(r log 2).

(Verified numerically to discretization accuracy; the analogous identity holds
for every prime power, Ω_W = Ω − Σ 2Λ(n)n^{−1/2}cos(r log n), so this
formulation covers every window.) Lemma R needed a monotone multiplier — the
sole reason the prime ever went through a norm bound. The LP does not: run the
same caps with cost Ω_W and **the target is 0**, with true headroom
λ_min(W|_V) ≈ 0.25 (L = 0.40) and 0.0807 (L = 0.45) — an order of magnitude
more room than the norm route ever had.

The Ω_W landscape explains all previous difficulty at a glance: the prime
deepens the archimedean valley at r ≲ 2.7 (cos ≈ 1), *creates a positive bump
at the half-period r ≈ 4.5* (cos ≈ −1), and cuts a second negative valley
around r ≈ 9.06 = 2π/log 2 (depth ≈ −0.6) plus shrinking dips at its
multiples — the beat lattice of the prime against the archimedean growth.

## 5. Result 3 — per-slot caps are not enough; union caps are the uncertainty principle as LP rows

With per-slot caps only, the T1-direct LP gives −0.17 (L=0.40) and −0.21
(L=0.45): the phantom measure occupies SEVERAL disjoint cheap slots at once
(the 9-valley, the 18-dip, …) at their individual caps. A real f cannot: joint
mass in a union of slots is capped by Λ of the union compression, which is
time-bandwidth-limited (≈ λ₀ of the union's TBW), typically far below the sum
of per-slot caps. `sigma_t1b.py` runs a self-aiming cutting-plane loop: solve,
cluster the optimal measure, add nested-union and pairwise-union tent caps for
the occupied slots, repeat.

Stage-5 (unions only): −0.0775 (L=0.40), −0.1199 (L=0.45) — half the phantom
gone, plateau at the single-slot cap of the 9-valley paired with cheap-dip
parking. Stage-6 adds SIGNED tradeoff rows σ = tent(band) − θ·1_{out-of-band}
(both right-tail and out-of-widened-band families, θ-ladder 0.1…4): the cap
λ_max(P_V[K_band − θ(I − B_out)]P_V) is the uncertainty-limited frontier
between in-band concentration and out-of-band leakage — precisely the physics
the phantom violated (a real band-concentrated f carries heavy FAR tails at
cost ~ log r; the phantom parked them in the 18-dip at +0.077).

**Stage-6 verdict (L = 0.40, four cutting-plane rounds):**

    round 0  −0.1747   (per-slot caps)
    round 2  −0.0227   (+ unions + tradeoffs)
    round 4  **+0.0046 — the LP certifies W ≥ 0 on the full constrained space**

i.e. **pilot-level full-space T1 at window ratio e^{0.8} = 2.226** — beyond the
Connes–Consani ratio-2 window with the prime 2 active, on the whole constrained
space (contrast: Certified Results 1–4 were 14-dimensional families). Margin
+0.0046 against cap-discretization ~10⁻³ (n = 1200 trapezoid): a margin-chasing
run (target +0.03) and the L = 0.42, 0.45 probes are in
`sigma_t1c3_output.txt`. Honest status: float pilot; the theorem requires the
certified pipeline of §6 with a total error budget below the final margin.

## 6. Certification design (if/where the LP clears 0)

All caps are eigenvalue upper bounds for explicit compressions; the certified
pipeline is: (i) frequency-side Nyström with analytic-remainder bounds for
Λ_σ — for σ supported in [0, R*], the compression factors through the band and
becomes an analytic kernel √(σσ′)[sin(L(r−r′))/π(r−r′) − rank-2 pole term] on a
compact box — certified to many digits with modest grids (standard rigorous-
Fredholm; all within Arb, same toolchain as certify.py); (ii) Lemma-T trace
caps (already-certified species) for the large-R indicators; (iii) interval-
hulled LP columns on cell decompositions + certified digamma for Ω_W (acb has
digamma); (iv) the explicit tail row at Rmax. The LP value is then a rigorous
lower bound for inf W on the constrained space: **wherever it is > 0, that is
full-space T1 at that window, machine-certified.**

## 7. Relation to the 2/3 paper, honestly stated

What transferred was not the inertia bookkeeping (which cannot see o(N)
off-line zeros and cannot prove positivity) but the *discipline of asking what
finitely many certifiable spectral quantities can and cannot certify* — §7.5(d)
of that paper, turned on the fixed-window Weil form. Result 1 is the negative
half (their "sharp given two traces" mirrored by our "rearrangement ceiling");
Results 2–3 are the positive half: the certificate format (LP over band
measures with compression caps) that the fixed-window problem actually wants.
Nothing here bears on RH beyond the fixed windows treated; T1 at any L < ½log 3
is strictly weaker than RH and is exactly the frontier ATTACK.md §4 declared
"the single most attackable theorem of the RH-equivalent species".
