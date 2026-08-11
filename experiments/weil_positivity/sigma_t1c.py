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
from sharp_floor import Omega, build_operator, LOG2
from sigma_lp import sigma_pair_vals, project_constraints
from sigma_rich import rich_centers
from sigma_t1 import omega_w, S2L2
from sigma_t1b import profile_operator, lam_max_profile, solve_lp, clusters_of, tent

def run(L, n=1200, Rmax=22.0, dR_caps=0.25, dr=0.05, rounds=14,
        thetas=(0.1, 0.2, 0.35, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0), verbose=True):
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
    # stage-9: COSINE-MODULATED caps — the prime's own oscillation as a basis
    # element (dual_read: the minorant's forced detachment sits on the
    # inter-valley ridges, i.e. exactly the cos(r log 2) beat; these sigma are
    # >= 0, even, and their operators are windowed prime-shift bounds — the
    # mu-invariant objects of T1-ARCHITECTURE, entering the LP as rows).
    for c in (7.0, 8.0, 9.0, 10.0, 12.0, 17.0, 18.0, 19.0):
        for sgn in (1.0, -1.0):
            sig = sigma_pair_vals(r, c, 3.0) * (1.0 + sgn * np.cos(r * LOG2))
            lam = lam_max_profile(sig, r, u, w, v1, v2)
            rows.append(sig); caps.append(lam)
    sig = np.clip(1.0 - r / 21.0, 0.0, None) * (1.0 + np.cos(r * LOG2))
    rows.append(sig); caps.append(lam_max_profile(sig, r, u, w, v1, v2))
    sig = np.clip(1.0 - r / 21.0, 0.0, None) * (1.0 - np.cos(r * LOG2))
    rows.append(sig); caps.append(lam_max_profile(sig, r, u, w, v1, v2))
    val, x = solve_lp(r, cost, rows, caps, tail_val)
    if verbose: print(f"L={L}: round 0 LP = {val:+.4f}", flush=True)
    Ppole = np.eye(nI)
    for v in (v1, v2):
        Ppole -= np.outer(v, v)
    # stage-7a: ORACLE caps — sigma shaped as the negative part of (Omega_W − c),
    # i.e. sigma_c = max(c − Omega_W, 0): compactly supported, even, pointwise-defined;
    # a single row already gives floor ≥ c − Λ_c, and inside the LP it carries the
    # exact SHAPE of the cost's negative set (the two valleys + dips jointly).
    for c_or in (0.05, 0.15, 0.30, 0.60):
        sig = np.maximum(c_or - cost, 0.0)
        lam = lam_max_profile(sig, r, u, w, v1, v2)
        rows.append(sig); caps.append(lam)
    val, x = solve_lp(r, cost, rows, caps, tail_val)
    if verbose: print(f"L={L}: round 0+oracle LP = {val:+.4f}", flush=True)
    stalls = 0
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
        # SIGNED tradeoff caps for each major slot: (a) right-tail penalized,
        # (b) ALL out-of-widened-band mass penalized (both-side forcing)
        for (lo, hi, m) in cl[:4]:
            if m < 0.05: continue
            sig_band = tent(r, lo, hi)
            K_band = profile_operator(sig_band, r, u, w, v1, v2)
            cut = hi + 2.0
            if cut < Rmax - 1.0:
                B_cut = band_op(round(float(np.ceil(cut / dR_caps) * dR_caps), 6))
                for th in thetas:
                    A = K_band - th * (Ppole - B_cut)   # P_V(K_band − θ·1_{r>cut})P_V
                    lam = float(np.max(eigsh(A, k=6, which='LA', return_eigenvectors=False)))
                    rows.append(sig_band - th * (r > cut).astype(float))
                    caps.append(lam); added += 1
            sig_wide = tent(r, max(lo - 2.0, 0.0), min(hi + 2.0, Rmax))
            K_wide = profile_operator(sig_wide, r, u, w, v1, v2)
            for th in thetas:
                A = K_band - th * (Ppole - K_wide)      # P_V(K_band − θ(1−σ_wide))P_V
                lam = float(np.max(eigsh(A, k=6, which='LA', return_eigenvectors=False)))
                rows.append(sig_band - th * (1.0 - sig_wide))
                caps.append(lam); added += 1
        # stage-7b: JOINT two-slot signed tradeoffs — concentrate on slots A∪B while
        # penalizing everything outside both (the bimodal phantom's exact shape)
        if len(cl) >= 2:
            (lo1, hi1, _), (lo2, hi2, _) = cl[0], cl[1]
            sig_ab = np.maximum(tent(r, lo1, hi1), tent(r, lo2, hi2))
            K_ab = profile_operator(sig_ab, r, u, w, v1, v2)
            wide_ab = np.maximum(tent(r, max(lo1 - 2, 0), min(hi1 + 2, Rmax)),
                                 tent(r, max(lo2 - 2, 0), min(hi2 + 2, Rmax)))
            K_wab = profile_operator(wide_ab, r, u, w, v1, v2)
            for th in thetas:
                A = K_ab - th * (Ppole - K_wab)
                lam = float(np.max(eigsh(A, k=6, which='LA', return_eigenvectors=False)))
                rows.append(sig_ab - th * (1.0 - wide_ab))
                caps.append(lam); added += 1
        val2, x = solve_lp(r, cost, rows, caps, tail_val)
        if verbose:
            occ = ", ".join(f"[{lo:.1f},{hi:.1f}]:{m:.2f}" for lo, hi, m in cl[:5])
            print(f"L={L}: round {rd} LP = {val2:+.4f}  (+{added} caps; slots {occ})", flush=True)
        stalls = stalls + 1 if abs(val2 - val) < 1e-4 else 0
        val = val2
        if stalls >= 3 or val >= 0.03: break     # chase certification margin, not just the sign
    print(f"L={L}: FINAL stage-6 LP floor {val:+.4f}  "
          f"[{'*** T1 CERTIFIED (pilot) ***' if val > 0 else 'still short'}]", flush=True)
    return val, dict(rows=rows, caps=caps, r=r, cost=cost, tail=tail_val, x=x)

if __name__ == '__main__':
    Ls = [float(x) for x in sys.argv[1:]] or [0.40]
    for L in Ls:
        run(L)[0] if True else None
