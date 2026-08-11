# dual_read.py — Track D stage 8: READ THE STALLED DUAL CERTIFICATE.
#
# The LP dual at the stall is the framework's best pointwise minorant
#   g(r) = tail − λ_mass − Σ_j λ_j σ_j(r)  ≤  Ω_W(r)   (λ = −HiGHS marginals ≥ 0)
# with floor = value of the LP. g is the LP's approximation to the "magic
# function" an EXACT certificate would need: an arithmetic-side function
# touching Ω_W with zero slack precisely on the spectral support of the true
# minimizers (which, as L grows, develop nodes at the zeta zeros — the
# zeta-cycles mechanism). Where g must detach from Ω_W is exactly what the
# current cap dictionary cannot express — the measured shape of the missing
# mathematics. Output: the tight set, the detachment profile, and the dual
# weights by cap family, dumped for analysis.

import numpy as np, mpmath as mp, sys
from scipy.optimize import linprog
mp.mp.dps = 30
from sigma_t1c import run

L = float(sys.argv[1]) if len(sys.argv) > 1 else 0.45
val, st = run(L, verbose=True)
rows, caps, r, cost, tail = st['rows'], st['caps'], st['r'], st['cost'], st['tail']
A_ub = np.vstack(rows + [np.ones_like(r)])
b_ub = np.array(caps + [1.0])
res = linprog(cost - tail, A_ub=A_ub, b_ub=b_ub, bounds=(0, None), method='highs')
lam = -res.ineqlin.marginals            # >= 0
lam_mass = lam[-1]
lam_rows = lam[:-1]
g = tail - lam_mass - lam_rows @ np.vstack(rows)   # minorant on the r-grid
slack = cost - g
tight = slack < 0.01
# contiguous tight intervals
iv, cur = [], None
for i, t in enumerate(tight):
    if t and cur is None: cur = [r[i], r[i]]
    elif t: cur[1] = r[i]
    elif cur is not None: iv.append(tuple(cur)); cur = None
if cur is not None: iv.append(tuple(cur))
print(f"\n=== DUAL READ, L={L} ===")
print(f"LP value {val:+.5f}; dual check: tail - lam_mass - lam.b = "
      f"{tail - lam_mass - float(lam_rows @ np.array(caps)):+.5f}")
print(f"active rows (lambda > 1e-6): {int(np.sum(lam_rows > 1e-6))} of {len(lam_rows)}; "
      f"lambda_mass = {lam_mass:.4f}")
print(f"tight set (slack < 0.01): {[(round(a,2), round(b,2)) for a, b in iv]}")
print(f"max slack on [0, 12]: {float(np.max(slack[r <= 12])):.3f} at r = "
      f"{float(r[r <= 12][np.argmax(slack[r <= 12])]):.2f}")
print(f"minorant at the second-valley floor r=9.06: g = {float(np.interp(9.06, r, g)):+.4f} "
      f"vs Omega_W = {float(np.interp(9.06, r, cost)):+.4f}")
np.savez('dual_read_L%.2f.npz' % L, r=r, cost=cost, g=g, lam=lam_rows, caps=np.array(caps))
print("dumped dual_read_L%.2f.npz" % L, flush=True)
