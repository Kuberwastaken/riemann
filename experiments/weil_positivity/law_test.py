#!/usr/bin/env python3
"""
Gap 4 test: does the completed-window lambda_min decay like e^{-4 gamma_1 L}?
High-precision arithmetic-side computation (arb entries at dps 30, tail 1e-12),
eigenvalues in mpmath at dps 40. Reports lambda_min(L) and local log-slopes
against the prediction 4*gamma_1 = 56.539.
"""
import numpy as np, math, time
from flint import ctx, arb
from certify import Certifier
import mpmath as mp

ctx.dps = 30
mp.mp.dps = 40
G1 = 14.134725141734693  # first zeta zero

def lam_min(L, N=16):
    c = Certifier(L, N, tail_target=1e-12)
    t0 = time.time()
    Gm = [[c.G_entry(i, j) for j in range(1, N + 1)] for i in range(1, N + 1)]
    Pm = [[c.prime_entry(i, j) for j in range(1, N + 1)] for i in range(1, N + 1)]
    vp = [c.pole_vec(k, +1) for k in range(1, N + 1)]
    vm = [c.pole_vec(k, -1) for k in range(1, N + 1)]
    vpf = np.array([float(x.mid()) for x in vp])
    vmf = np.array([float(x.mid()) for x in vm])
    _, _, Vt = np.linalg.svd(np.vstack([vpf, vmf]))
    Q = Vt[2:].T
    d = N - 2
    W = mp.matrix(d, d)
    for a_ in range(d):
        for b_ in range(d):
            s = mp.mpf(0)
            for i in range(N):
                for j in range(N):
                    w = Gm[i][j] + Pm[i][j] + vp[i] * vm[j] + vm[i] * vp[j]
                    s += mp.mpf(Q[i, a_]) * mp.mpf(Q[j, b_]) * mp.mpf(str(w.mid()))
            W[a_, b_] = s
    ev = mp.eigsy(W, eigvals_only=True)
    return float(min(ev)), time.time() - t0

if __name__ == '__main__':
    print(f"# lambda_min(L) high-precision; prediction: local slope -4*gamma_1 = -{4*G1:.3f}")
    Ls = [0.64, 0.68, 0.72, 0.76, 0.80]
    vals = []
    for L in Ls:
        v, dt = lam_min(L)
        vals.append(v)
        print(f"L={L:.2f}  lambda_min={v:.6e}   t={dt:.0f}s", flush=True)
    print("# local log-slopes (d log lambda / dL):")
    for k in range(1, len(Ls)):
        if vals[k] > 0 and vals[k-1] > 0:
            slope = (math.log(vals[k]) - math.log(vals[k-1])) / (Ls[k] - Ls[k-1])
            print(f"  [{Ls[k-1]:.2f},{Ls[k]:.2f}]: slope = {slope:+.2f}   (pred {-4*G1:+.2f})")
        else:
            print(f"  [{Ls[k-1]:.2f},{Ls[k]:.2f}]: nonpositive value — subspace/precision floor hit")
