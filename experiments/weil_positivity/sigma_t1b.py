# sigma_t1b.py — Track D stage 5: cutting-plane union caps for the T1-direct LP.
#
# Stage-4 diagnosis: with per-slot caps the LP exploits SEVERAL disjoint cheap
# slots of Omega_W at once (the r~9 valley + the narrow dips near 18.1, 27.2 =
# the cos(r log 2) beat lattice), which no single supp-[-L,L] function can do:
# joint mass in a UNION of slots is capped by lambda_max of the union
# compression (time-bandwidth limited), typically far below the sum of the
# per-slot caps. Constraint validity is unchanged — for ANY bounded even sigma,
# int sigma d(nu_f) = <f, sigma(D) f> <= lambda_max(P_V sigma(D) P_V) on V.
#
# This script runs a self-aiming cutting-plane loop:
#   round 0: indicator caps + Fejer dictionary (as stage 4)
#   round k: solve LP -> cluster the solution measure -> for the occupied
#            clusters build union tents (all nested unions by decreasing mass,
#            plus the full union) -> add caps Lambda = lambda_max(compression)
#            -> re-solve.  Stop when the LP value stops improving or >= 0.
#
# Operator build for arbitrary profiles uses the uniform-grid trick:
# u_i - u_j = (i-j)h exactly, so any convolution kernel needs only 2n-1 values
# k(x_m) = (1/pi) int_0^Rmax sigma(r) cos(r x_m) dr  (sigma even, one-sided).

import numpy as np, mpmath as mp, sys
from scipy.sparse.linalg import eigsh
from scipy.optimize import linprog
mp.mp.dps = 30
from sharp_floor import Omega, build_operator, LOG2
from sigma_lp import sigma_pair_vals, project_constraints
from sigma_rich import rich_centers
from sigma_t1 import omega_w, S2L2

def profile_operator(sig_vals, rgrid, u, w, v1, v2):
    """P_V K_sigma P_V for sigma given as values on rgrid (one-sided, even)."""
    n = len(u); h = u[1] - u[0]
    xs = np.arange(-(n - 1), n) * h
    # k(x) = (1/pi) int_0^Rmax sigma(r) cos(r x) dr
    kv = np.trapezoid(sig_vals[None, :] * np.cos(np.outer(xs, rgrid)), rgrid, axis=1) / np.pi
    idx = np.arange(n)
    Kmat = kv[idx[:, None] - idx[None, :] + n - 1]
    sw = np.sqrt(w)
    Kmat = sw[:, None] * Kmat * sw[None, :]
    return project_constraints(Kmat, v1, v2)

def lam_max_profile(sig_vals, rgrid, u, w, v1, v2, k=6):
    A = profile_operator(sig_vals, rgrid, u, w, v1, v2)
    return float(np.max(eigsh(A, k=k, which='LA', return_eigenvectors=False)))

def solve_lp(r, cost, rows, caps, tail_val):
    A_ub = np.vstack(rows + [np.ones_like(r)])
    b_ub = np.array(caps + [1.0])
    res = linprog(cost - tail_val, A_ub=A_ub, b_ub=b_ub, bounds=(0, None), method='highs')
    return res.fun + tail_val, res.x

def clusters_of(measure, r, thresh=0.02, gap=1.0):
    """Contiguous clusters of the LP measure with mass >= thresh."""
    pts = r[measure > 1e-9]; ms = measure[measure > 1e-9]
    if len(pts) == 0: return []
    cl, cur, m = [], [pts[0], pts[0]], ms[0]
    for p, q in zip(pts[1:], ms[1:]):
        if p - cur[1] <= gap: cur[1] = p; m += q
        else:
            if m >= thresh: cl.append((cur[0], cur[1], m))
            cur, m = [p, p], q
    if m >= thresh: cl.append((cur[0], cur[1], m))
    return cl

def tent(r, lo, hi, ramp=1.0):
    return np.clip(np.minimum((r - (lo - ramp)) / ramp, ((hi + ramp) - r) / ramp), 0.0, 1.0)

def run(L, n=1200, Rmax=22.0, dR_caps=0.25, dr=0.05, rounds=5, verbose=True):
    u, w, v1, v2, K = build_operator(L, n)
    r = np.arange(0.0, Rmax + 1e-9, dr)
    cost = np.array([omega_w(x) for x in r])
    tail_val = Omega(Rmax) - S2L2
    rows, caps, names = [], [], []
    # indicator caps
    for R in np.arange(dR_caps, Rmax + 1e-9, dR_caps):
        KR, _ = K(R)
        A = project_constraints(KR, v1, v2)
        lam = min(1.0, float(np.max(eigsh(A, k=6, which='LA', return_eigenvectors=False))))
        rows.append((r <= R + 1e-12).astype(float)); caps.append(lam); names.append(f"ind{R:.2f}")
    # Fejer dictionary
    for c in rich_centers():
        for a in (1.5, 3.0, 6.0):
            sig = sigma_pair_vals(r, c, a)
            lam = lam_max_profile(sig, r, u, w, v1, v2)
            rows.append(sig); caps.append(lam); names.append(f"fej{c:.1f}w{a:.0f}")
    val, x = solve_lp(r, cost, rows, caps, tail_val)
    if verbose: print(f"L={L}: round 0 LP = {val:+.4f}", flush=True)
    for rd in range(1, rounds + 1):
        cl = clusters_of(x, r)
        if not cl: break
        cl_sorted = sorted(cl, key=lambda t: -t[2])
        added = 0
        # nested unions by decreasing mass + full union + all pairs of top-4
        unions = [cl_sorted[:k] for k in range(2, len(cl_sorted) + 1)]
        from itertools import combinations
        unions += [list(p) for p in combinations(cl_sorted[:4], 2)]
        for un in unions:
            sig = np.zeros_like(r)
            for (lo, hi, m) in un: sig = np.maximum(sig, tent(r, lo, hi))
            lam = lam_max_profile(sig, r, u, w, v1, v2)
            rows.append(sig); caps.append(lam); added += 1
            names.append("un:" + "+".join(f"[{lo:.0f},{hi:.0f}]" for lo, hi, _ in un))
        val2, x = solve_lp(r, cost, rows, caps, tail_val)
        if verbose:
            occ = ", ".join(f"[{lo:.1f},{hi:.1f}]:{m:.2f}" for lo, hi, m in cl_sorted[:5])
            print(f"L={L}: round {rd} LP = {val2:+.4f}  (+{added} union caps; slots {occ})", flush=True)
        if val2 < val + 1e-4 and val2 < 0: val = val2; break
        val = val2
        if val >= 0: break
    print(f"L={L}: FINAL LP floor {val:+.4f}  "
          f"[{'*** T1 CERTIFIED (pilot) ***' if val > 0 else 'still short'}]", flush=True)
    return val

if __name__ == '__main__':
    Ls = [float(x) for x in sys.argv[1:]] or [0.40, 0.45]
    for L in Ls:
        run(L)
