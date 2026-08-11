# sigma_t1c.py — Track D stage 6: signed band-vs-tail tradeoff caps.
#
# Stage-5 residual diagnosis: the LP parks ~0.55 mass in the r~9 valley at the
# union cap and its remaining mass at the 18-dip; a REAL band-concentrated f
# cannot do this — its sinc tails force mass to large r (cost ~ log r), not to
# the cheap dip. Encode as SIGNED sigma rows (validity unchanged):
#     sigma_theta = tent(band) − θ·1_{r > cut}
#     ∫sigma_theta dν ≤ Λ_θ = λ_max(P_V [K_band − θ(I_T − B_cut)] P_V)
# Λ_θ is the uncertainty-limited tradeoff frontier between band concentration
# and tail avoidance. Several θ per occupied slot linearize the frontier.
# (I_T on the frequency side is σ ≡ 1; B_cut is the [0,cut] band operator.)

import numpy as np, mpmath as mp, sys
from scipy.sparse.linalg import eigsh
mp.mp.dps = 30
from sharp_floor import Omega, build_operator
from sigma_lp import sigma_pair_vals, project_constraints
from sigma_rich import rich_centers
from sigma_t1 import omega_w, S2L2
from sigma_t1b import profile_operator, lam_max_profile, solve_lp, clusters_of, tent

def run(L, n=1200, Rmax=22.0, dR_caps=0.25, dr=0.05, rounds=8,
        thetas=(0.25, 0.5, 1.0, 2.0, 4.0), verbose=True):
    u, w, v1, v2, K = build_operator(L, n)
    nI = len(u)
    r = np.arange(0.0, Rmax + 1e-9, dr)
    cost = np.array([omega_w(x) for x in r])
    tail_val = Omega(Rmax) - S2L2
    rows, caps = [], []
    band_ops = {}
    def band_op(R):
        if R not in band_ops:
            KR, _ = K(R)
            band_ops[R] = project_constraints(KR, v1, v2)
        return band_ops[R]
    # indicator caps
    for R in np.arange(dR_caps, Rmax + 1e-9, dR_caps):
        A = band_op(round(float(R), 6))
        lam = min(1.0, float(np.max(eigsh(A, k=6, which='LA', return_eigenvectors=False))))
        rows.append((r <= R + 1e-12).astype(float)); caps.append(lam)
    # Fejer dictionary
    for c in rich_centers():
        for a in (1.5, 3.0, 6.0):
            sig = sigma_pair_vals(r, c, a)
            lam = lam_max_profile(sig, r, u, w, v1, v2)
            rows.append(sig); caps.append(lam)
    val, x = solve_lp(r, cost, rows, caps, tail_val)
    if verbose: print(f"L={L}: round 0 LP = {val:+.4f}", flush=True)
    Ppole = np.eye(nI)
    for v in (v1, v2):
        Ppole -= np.outer(v, v)
    for rd in range(1, rounds + 1):
        cl = sorted(clusters_of(x, r), key=lambda t: -t[2])
        if not cl: break
        added = 0
        # union caps (as stage 5)
        from itertools import combinations
        unions = [cl[:k] for k in range(2, len(cl) + 1)] + [list(p) for p in combinations(cl[:4], 2)]
        for un in unions:
            sig = np.zeros_like(r)
            for (lo, hi, m) in un: sig = np.maximum(sig, tent(r, lo, hi))
            lam = lam_max_profile(sig, r, u, w, v1, v2)
            rows.append(sig); caps.append(lam); added += 1
        # SIGNED band-vs-tail tradeoff caps for each major slot
        for (lo, hi, m) in cl[:4]:
            if m < 0.05: continue
            cut = hi + 2.0
            if cut >= Rmax - 1.0: continue
            sig_band = tent(r, lo, hi)
            K_band = profile_operator(sig_band, r, u, w, v1, v2)
            B_cut = band_op(round(float(np.ceil(cut / dR_caps) * dR_caps), 6))
            for th in thetas:
                A = K_band - th * (Ppole - B_cut)      # P_V(K_band − θ(I−B_cut))P_V
                lam = float(np.max(eigsh(A, k=6, which='LA', return_eigenvectors=False)))
                sig_row = sig_band - th * (r > cut).astype(float)
                rows.append(sig_row); caps.append(lam); added += 1
        val2, x = solve_lp(r, cost, rows, caps, tail_val)
        if verbose:
            occ = ", ".join(f"[{lo:.1f},{hi:.1f}]:{m:.2f}" for lo, hi, m in cl[:5])
            print(f"L={L}: round {rd} LP = {val2:+.4f}  (+{added} caps; slots {occ})", flush=True)
        if abs(val2 - val) < 1e-4: val = val2; break
        val = val2
        if val >= 0: break
    print(f"L={L}: FINAL stage-6 LP floor {val:+.4f}  "
          f"[{'*** T1 CERTIFIED (pilot) ***' if val > 0 else 'still short'}]", flush=True)
    return val

if __name__ == '__main__':
    Ls = [float(x) for x in sys.argv[1:]] or [0.40]
    for L in Ls:
        run(L)
