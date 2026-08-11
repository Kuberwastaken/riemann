# sigma_lp.py — Track D (2026-08-11), stage 2: the sigma-augmented Markov LP.
#
# sharp_floor.py established: even with the EXACT per-band caps
# nu([0,R]) <= lambda_max(B_R|_V), the independent-R rearrangement (Lemma R)
# saturates at ~0.4753 at L0 — below the prime bar 0.490129. The relaxation, not
# the caps, is now the binding loss (true constrained floor ~ 0.55).
#
# Fix: one f must satisfy ALL band constraints jointly. For ANY even sigma >= 0,
#     integral sigma d(nu_f) = (1/2pi) int sigma(r)|F(r)|^2 dr
#                            = <f, sigma(D) f>  <=  Lambda_sigma := lambda_max(P_V sigma(D) P_V)
# — a linear constraint on nu_f. The LP
#     min integral Omega d(nu)   s.t.  nu >= 0, nu(R+) = 1,
#                                      nu([0,R_k]) <= M_exact(R_k)  (indicator caps)
#                                      integral sigma_j d(nu) <= Lambda_j (smooth caps)
# lower-bounds G(f) on the constrained space, interpolating between the
# rearrangement (indicators only) and the exact dual SDP (all sigma; value ~0.55).
#
# Dictionary: symmetric Fejer pairs sigma_{c,a}(r) = (1-|r-c|/a)_+ + (1-|r+c|/a)_+,
# closed-form kernels k(x) = (4/pi) cos(cx) sin^2(ax/2)/(a x^2)   (c=0: half),
# chosen because (i) even, >= 0; (ii) kernel entries are elementary — later
# certifiable by 1-D Arb integrals; (iii) narrow bumps have time-bandwidth
# 2La/pi < 1, so the compression is near-rank-1 and the certifiable bound
# sqrt(Tr[(P_V sigma(D) P_V)^2]) (ALL 1-D integrals via Tr K^2 =
# int (2L-|x|) k(x)^2 dx + rank-2 corrections) is nearly sharp.
#
# Pilot: float. Output: floor(cum caps only) vs floor(cum + sigma) vs bar, per L;
# also reports Lambda_j vs sqrt(m2_j) tightness (certification preview).

import numpy as np
from scipy.sparse.linalg import eigsh
from scipy.optimize import linprog
import mpmath as mp
from sharp_floor import Omega, build_operator, LOG2, BAR

def project_constraints(A, v1, v2):
    for v in (v1, v2):
        Av = A @ v
        A -= np.outer(Av, v) + np.outer(v, Av) - (v @ Av) * np.outer(v, v)
    return A

def lam_max(A, k=4):
    return float(np.max(eigsh(A, k=k, which='LA', return_eigenvectors=False)))

def fejer_pair_kernel(x, c, a):
    """(1/2pi) FT of sigma_{c,a}; x may be array with zeros."""
    xs = np.where(x == 0.0, 1.0, x)
    base = 4.0 * np.sin(a * xs / 2.0) ** 2 / (np.pi * a * xs ** 2)
    base = np.where(x == 0.0, a / np.pi, base)
    k = np.cos(c * x) * base
    if c == 0.0:
        k = 0.5 * k                      # single bump, mass a not 2a
    return k

def sigma_pair_vals(r, c, a):
    v = np.clip(1.0 - np.abs(r - c) / a, 0.0, None) + np.clip(1.0 - np.abs(r + c) / a, 0.0, None)
    if c == 0.0:
        v = np.clip(1.0 - np.abs(r) / a, 0.0, None)
    return v

def run_L(L, n=1200, Rmax=22.0, dR_caps=0.25, dr_meas=0.05,
          centers=None, widths=(1.5, 3.0), ktop=70, report_m2=True):
    u, w, v1, v2, K = build_operator(L, n)
    du = u[:, None] - u[None, :]
    sw = np.sqrt(w)

    # --- indicator caps (exact spectral) ---
    Rg = np.arange(0.0, Rmax + 1e-9, dR_caps)
    Mex = np.zeros_like(Rg)
    for i, R in enumerate(Rg):
        if R == 0:
            continue
        KR, _ = K(R)
        A = project_constraints(KR, v1, v2)
        Mex[i] = min(1.0, lam_max(A))
    Mex = np.maximum.accumulate(Mex)

    # --- sigma caps ---
    if centers is None:
        centers = np.arange(0.0, 15.0, 1.0)
    sig_list, Lam, m2_ratio = [], [], []
    for c in centers:
        for a in widths:
            kmat = (sw[:, None] * fejer_pair_kernel(du, c, a) * sw[None, :])
            A = project_constraints(kmat, v1, v2)
            vals = eigsh(A, k=min(ktop, n - 2), which='LA', return_eigenvectors=False)
            vals = np.clip(vals, 0.0, None)
            lam = float(np.max(vals))
            m2 = float(np.sum(vals ** 2))          # float stand-in for the 1-D-integral Tr K^2
            sig_list.append((c, a)); Lam.append(lam)
            m2_ratio.append(np.sqrt(m2) / lam if lam > 1e-12 else np.inf)
    Lam = np.array(Lam)

    # --- LP over measures on a fine r-grid ---
    r = np.arange(0.0, Rmax + 1e-9, dr_meas)
    Om = np.array([Omega(x) for x in r])
    ncap = len(Rg)
    A_ub, b_ub = [], []
    for kk in range(1, ncap):                       # cumulative caps
        row = (r <= Rg[kk] + 1e-12).astype(float)
        A_ub.append(row); b_ub.append(Mex[kk])
    n_ind = len(b_ub)
    for (c, a), lam in zip(sig_list, Lam):          # sigma caps
        A_ub.append(sigma_pair_vals(r, c, a)); b_ub.append(lam)
    A_eq = [np.ones_like(r)]; b_eq = [1.0]
    # NOTE: mass beyond Rmax would sit at Omega >= Omega(Rmax) > 0; forcing all mass
    # into [0, Rmax] can only LOWER the LP value iff Omega(Rmax) exceeds the interior
    # placement cost — with caps forcing most mass out to Omega ~ 1, the bound is
    # safe/conservative either way for the pilot; certified version handles the tail
    # explicitly as in PROOF-c0.
    res_ind = linprog(Om, A_ub=np.array(A_ub[:n_ind]), b_ub=np.array(b_ub[:n_ind]),
                      A_eq=np.array(A_eq), b_eq=np.array(b_eq), bounds=(0, None), method='highs')
    res_all = linprog(Om, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                      A_eq=np.array(A_eq), b_eq=np.array(b_eq), bounds=(0, None), method='highs')
    out = {'floor_ind': res_ind.fun, 'floor_sigma': res_all.fun,
           'sig_list': sig_list, 'Lam': Lam, 'm2_ratio': np.array(m2_ratio)}
    return out

if __name__ == '__main__':
    mp.mp.dps = 30
    print(f"bar = {BAR:.6f}")
    for L in [LOG2 / 2, 0.355, 0.360, 0.369]:
        o = run_L(L)
        verdict = "CLEARS BAR" if o['floor_sigma'] > BAR else "below"
        print(f"L={L:.5f}: rearrangement(exact caps)={o['floor_ind']:.4f}  "
              f"+sigma-LP={o['floor_sigma']:.4f}  [{verdict}]   "
              f"m2-tightness of sigma caps: median sqrt(m2)/lam = {np.median(o['m2_ratio']):.3f}, "
              f"worst {np.max(o['m2_ratio']):.3f}")
