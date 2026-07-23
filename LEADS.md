# LEADS: actual good leads to go after

*2026-07-23, after the full-send. These survive everything we refuted today —
each was checked against the session's no-go results (spatial/IMS routes closed,
moment ladder saturated at 77%, CF shortcut nonexistent) before making the list.
Ranked by (probability of success) × (value if it lands) ÷ (cost).*

---

## Lead 1 — The graded-mode architecture for full-space T1 (the new one)

Every failed route to T1 died on the same cross-term: spatial splits die on the
1/|x| kernel singularity; naive mode splits die on the unbounded archimedean
cross terms. **The fix that survives scrutiny:** the singularity of the kernel is
exactly high-frequency *growth* of Ω — which in a frequency-graded decomposition
is the *good* direction. Architecture:

1. Split the window space into dyadic Fourier-mode blocks (in u, on [−L, L]).
2. **Low block** (modes ≤ N₀): finite-dimensional — certify W ⪰ c·I by ball
   Cholesky (we already do this routinely; Certified Results 1–7).
3. **High blocks**: an explicit coercivity lemma — a function orthogonal to the
   first N₀ modes has spectral mass below any R₀ bounded by an explicit
   ε(N₀, R₀) (integration by parts / Bernstein), so G ⪰ (1−ε)Ω(R₀) − ‖B‖,
   growing with the block index; the bounded parts (Ω₋ part, primes) are ≤ 6.5
   globally (5.38 + Lemma 1′).
4. **Cross terms**: the A-part (positive multiplier Ω₊) couples dyadic blocks
   with decay in frequency separation (Fourier-localized profiles overlap like
   1/Δω²) — **Cotlar–Stein summable**; the B and prime parts are globally
   bounded operators.

No step collides with a no-go: this is the standard machinery (dyadic + almost
orthogonality + certified finite section) by which rigorous-numerics proofs
certify infinite-dimensional operator inequalities. Estimated cost: 2–4 weeks of
careful constant-chasing for a strong analyst (or a long, disciplined session
series). Value: **full-space T1** — the first Weil-positivity theorem with
arithmetic content. This is the successor to the moment ladder, and unlike the
ladder it does not saturate: the finite section absorbs whatever the explicit
lemmas cannot.

## Lead 2 — The ε_N certification service to the CCM program (finishable now)

From the Gap-3 reading: CCM 2025 Theorem 1.1 *assumes* the smallest eigenvalue
ε_N of QW_λ^N is simple with even eigenfunction; their Prop. 3.4 makes our
finite-section eigenvalues exactly the right objects. Deliverable: certified
sign + simplicity (eigenvalue-gap ball bound) + evenness of ε_N across a λ-grid.
Directly useful to the leading live RH program; novel; entirely within our
existing pipeline. Cost: days. This is also the natural *contact surface* for
sharing the whole laboratory with the people best placed to use it.

## Lead 3 — The certified razor corridor (partially done today)

`razor_certificate.txt`: at window [e^{−0.7}, e^{0.7}] the full Weil-form
infimum is **certified ≤ 1.187×10⁻⁷** while RH asserts ≥ 0. Extend to a curve of
windows: a certified quantitative version of "RH is barely true," window by
window — the arithmetic-side counterpart of Λ = 0, and (combined with Lead 1
style lower bounds) a certified two-sided pincer on the exact boundary where RH
lives. Cost: hours per window. Publishable as part of the note.

## Lead 4 — Derive the criticality rate (the 4γ₁ law) from extremal theory

If the pending law test confirms slope ≈ 4γ₁: prove it. The mechanism is a clean
extremal problem in Paley–Wiener space — minimize the completed-window form over
type-2L functions; the residual is forced at the lowest zeros because zeta's
zero density exceeds the interlacing capacity of type-2L functions beyond height
~e^{4L}. A proved rate law would be a *new quantitative bridge between the Weil
form and the position of γ₁* — the first theorem in which the lowest zero
controls the positivity landscape rather than vice versa. Cost: open-ended but
well-posed; the numerics (once law_test lands) will say whether the exponent is
exactly 4γ₁ or has corrections.

## Lead 5 — The repeated-orbit seam (unexamined by anyone)

Measured today: prime-power terms with k ≥ 2 (n = 4, 8, 9, …) *hurt* positivity
while primes rescue it. Nobody in the 178-source archive treats the k ≥ 2 terms
separately. Concrete experiment (runnable in our lab today): λ_min curves for
primes-only vs full prime-power sums → quantify the "repeated-orbit drag";
if primes-only positivity extends strictly further, RH admits a reformulation as
*primes-only positivity + an explicitly bounded k ≥ 2 correction* — and the k ≥ 2
tail is exactly the ψ−θ (Chebyshev) discrepancy, an object with independent
classical control. Cheap to explore, genuinely unexamined.

## Lead 6 — For human analysts: Guth–Maynard × pair correlation (from ATTACK.md)

Unchanged and still the sharpest classical lead: unconditional control of
Montgomery's F(α, T) past α = 1 via GM large-value technology, feeding the
Baluyot–Goldston bridge → first majority-of-zeros-on-the-line theorem. Not
executable in this laboratory; belongs to the analytic community.

## Lead 7 — Formalize Theorem A in Lean via CI (x86 runners)

Local aarch64 blocks mathlib cache, but the repo's GitHub Actions run on x86:
a Lean project formalizing Theorem A (its three lemmas are Mathlib-friendly:
digamma monotonicity, trace identity, stochastic dominance) would make it the
first machine-formalized quantitative statement adjacent to Weil positivity —
and would stress-test the proof independently of its author. Cost: 1–2 weeks of
Lean work; high credibility value.

---

*Meta: Leads 2, 3, 5 are finishable in this laboratory. Lead 1 is the real
successor project — the first full-space T1 architecture with no known
obstruction. Leads 4, 6, 7 are well-posed exports. None of these is a route to
RH itself in any near horizon; they are the honest frontier.*
