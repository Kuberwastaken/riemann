# sharp_floor.py — Track D (2026-08-11): the sharp-moment archimedean floor
#
# Theorem A (PROOF-c0.md) bounds the constrained band mass by the TRACE of the
# constrained prolate compression:  nu([0,R]) <= Tr(B_R|_V)  (Lemma T, the k=1
# moment bound).  This pilot measures how much floor is recovered when that step
# is replaced by sharper spectral information about B_R|_V = P_V (P_T Pi_R P_T) P_V:
#
#   M_trace(R) = min(1, 2LR/pi - rho1(R) - rho2(R))       [Lemma T, as proven]
#   M_mk(R)    = min(1, Tr[(B_R|_V)^k]^{1/k})             [k-moment bound; k=2 is
#                certifiable as ONE 1-D verified integral + rank-2 corrections]
#   M_exact(R) = lambda_max(B_R|_V)                        [the sharp cap; equals the
#                top constrained-prolate eigenvalue; the ceiling of ALL moment methods]
#
# and the floor is re-assembled by the SAME stochastic-dominance rearrangement
# (Lemma M monotonicity + Lemma R), which is untouched:
#
#   G(f) >= sum_k Omega(R_{k-1}) * [M(R_k) - M(R_{k-1})]  + Omega(R_K)(1 - M(R_K)).
#
# Question: does the sharp floor m(L) clear the prime bar (log 2)/sqrt(2) = 0.490129
# anywhere on the one-prime window L in (log2/2, ~0.40]?  Wherever it does, T1 at
# that L reduces to a finite certified computation (norm route, Corollary in
# T1-ARCHITECTURE.md).  Float pilot only — certification is a separate step.
#
# Validation target: the trace-only floor at L0 = log2/2 must reproduce ~0.378
# (PROOF-c0.md numerical evaluation).

import numpy as np
from scipy.sparse.linalg import eigsh
from scipy.linalg import eigh
import mpmath as mp

LOG2 = float(np.log(2.0))
BAR = LOG2 / np.sqrt(2.0)          # 0.490129... the p=2 prime bound (Lemma 1)

def Omega(r):
    # Re psi(1/4 + i r/2) - log pi   (archimedean multiplier; even; increasing on [0,inf))
    return float(mp.re(mp.digamma(mp.mpc(0.25, 0.5 * r)))) - float(mp.log(mp.pi))

def build_operator(L, n):
    """Weighted sinc-kernel machinery on [-L, L] with the two pole constraints
    projected out. Returns grid, weights, constraint ONB (v1,v2) and a function
    K(R) giving the symmetrized kernel matrix of B_R = P_T Pi_R P_T."""
    u = np.linspace(-L, L, n)
    h = u[1] - u[0]
    w = np.full(n, h); w[0] *= 0.5; w[-1] *= 0.5          # trapezoid
    sw = np.sqrt(w)
    du = u[:, None] - u[None, :]
    c1 = sw * np.exp(u / 2.0)                              # pole constraints e^{+-u/2}
    c2 = sw * np.exp(-u / 2.0)
    # orthonormalize
    v1 = c1 / np.linalg.norm(c1)
    v2 = c2 - (v1 @ c2) * v1
    v2 = v2 / np.linalg.norm(v2)
    def K(R):
        M = np.where(du != 0.0, np.sin(R * du) / (np.pi * np.where(du == 0, 1, du)), R / np.pi)
        return (sw[:, None] * M * sw[None, :]), None
    return u, w, v1, v2, K

def constrained_spectrum(KR, v1, v2, ktop=80):
    """Spectrum of P_V B_R P_V (top ktop eigenvalues)."""
    A = KR.copy()
    for v in (v1, v2):
        Av = A @ v
        A -= np.outer(Av, v) + np.outer(v, Av) - (v @ Av) * np.outer(v, v)
        # A <- (I-vv')A(I-vv')  done sequentially for the two (orthonormal) v's
    k = min(ktop, A.shape[0] - 2)
    vals = eigsh(A, k=k, which='LA', return_eigenvectors=False)
    return np.sort(vals)[::-1]

def floor_from_caps(Rgrid, Mcaps, Om):
    """Stochastic-dominance lower bound: mass M(R_1) at Omega(R_0), increments at
    left endpoints, remainder at Omega(R_K)."""
    M = np.clip(np.maximum.accumulate(np.clip(Mcaps, 0.0, 1.0)), 0.0, 1.0)
    total = Om[0] * M[1] if len(M) > 1 else 0.0
    for k in range(2, len(M)):
        total += Om[k - 1] * max(M[k] - M[k - 1], 0.0)
    total += Om[-1] * (1.0 - M[-1])
    return total

def run(L, n=1400, Rmax=20.0, dR=0.25, ktop=80, verbose=False):
    u, w, v1, v2, K = build_operator(L, n)
    Rg = np.arange(0.0, Rmax + 1e-9, dR)
    Om = np.array([Omega(r) for r in Rg])
    M_tr, M_ex, M_m2, M_m4, M_m6 = [np.zeros_like(Rg) for _ in range(5)]
    lam2_frac = np.zeros_like(Rg)
    for i, R in enumerate(Rg):
        if R == 0.0:
            continue
        KR, _ = K(R)
        rho1 = v1 @ (KR @ v1); rho2 = v2 @ (KR @ v2)
        M_tr[i] = min(1.0, max(0.0, 2 * L * R / np.pi - rho1 - rho2))
        lam = constrained_spectrum(KR, v1, v2, ktop=ktop)
        lam = np.clip(lam, 0.0, 1.0)
        M_ex[i] = lam[0]
        m2 = float(np.sum(lam ** 2)); m4 = float(np.sum(lam ** 4)); m6 = float(np.sum(lam ** 6))
        M_m2[i] = min(1.0, np.sqrt(m2)); M_m4[i] = min(1.0, m4 ** 0.25); M_m6[i] = min(1.0, m6 ** (1.0 / 6))
        lam2_frac[i] = lam[1] / lam[0] if lam[0] > 0 else 0.0
        if verbose and abs(R - round(R)) < 1e-9:
            print(f"  R={R:5.2f} Om={Om[i]:+.3f} trace-cap={M_tr[i]:.4f} m2={M_m2[i]:.4f} "
                  f"m4={M_m4[i]:.4f} m6={M_m6[i]:.4f} exact={M_ex[i]:.4f} l2/l1={lam2_frac[i]:.3f}")
    floors = {name: floor_from_caps(Rg, Mc, Om) for name, Mc in
              [('trace', M_tr), ('m2', M_m2), ('m4', M_m4), ('m6', M_m6), ('exact', M_ex)]}
    # combined cap: every bound is valid, so the pointwise min is valid
    M_comb2 = np.minimum(M_tr, M_m2)     # what a k<=2 certification could use
    floors['trace^m2'] = floor_from_caps(Rg, M_comb2, Om)
    M_comball = np.minimum.reduce([M_tr, M_m2, M_m4, M_m6, M_ex])
    floors['best'] = floor_from_caps(Rg, M_comball, Om)
    return floors

if __name__ == '__main__':
    mp.mp.dps = 30
    print(f"prime bar (log2)/sqrt2 = {BAR:.6f}")
    print("floors m(L): G(f) >= m(L)||f||^2 on the constrained space, by cap used")
    print(f"{'L':>8} | {'trace':>8} {'tr^m2':>8} {'m2':>8} {'m4':>8} {'m6':>8} {'exact':>8} {'best':>8} | verdict(best)")
    L0 = LOG2 / 2
    for L in [L0, 0.355, 0.360, 0.369, 0.380, 0.390, 0.400]:
        f = run(L)
        verdict = "CLEARS BAR" if f['best'] > BAR else ("clears w/ exact only" if f['exact'] > BAR else "below bar")
        print(f"{L:8.5f} | {f['trace']:8.4f} {f['trace^m2']:8.4f} {f['m2']:8.4f} {f['m4']:8.4f} "
              f"{f['m6']:8.4f} {f['exact']:8.4f} {f['best']:8.4f} | {verdict}")
