#!/usr/bin/env python3
"""
Rigorous certification of the RESCUE PHENOMENON at L=0.62 (N=24 family):
  (a) the archimedean form G has a certified NEGATIVE direction on the family
      (explicit vector v with rigorous enclosure of v^T G v < 0), while
  (b) the total Weil form W = G + P (primes {2,3}) + poles is certified >= c > 0
      on the entire family.
Together: on this explicit 22-dimensional family of compactly supported test
functions, positivity of the Weil functional is CREATED by the prime terms —
machine-verified, not just observed. Uses the Certifier pipeline of certify.py.
"""
import numpy as np, math, time
from flint import acb, arb, ctx
from certify import Certifier

ctx.dps = 25
L, N = 0.62, 24

def main():
    t0 = time.time()
    c = Certifier(L, N, tail_target=5e-8)
    print(f"# rescue certification L={L} N={N} R_CUT={c.R_CUT:.0f} primes={c.primes}")
    Gm = [[arb(0)] * N for _ in range(N)]
    for i in range(1, N + 1):
        for j in range(i, N + 1):
            e = c.G_entry(i, j)
            Gm[i - 1][j - 1] = e; Gm[j - 1][i - 1] = e
        print(f"G row {i}/{N} t={time.time()-t0:.0f}s", flush=True)
    Pm = [[arb(0)] * N for _ in range(N)]
    for i in range(1, N + 1):
        for j in range(i, N + 1):
            e = c.prime_entry(i, j)
            Pm[i - 1][j - 1] = e; Pm[j - 1][i - 1] = e
    vp = [c.pole_vec(k, +1) for k in range(1, N + 1)]
    vm = [c.pole_vec(k, -1) for k in range(1, N + 1)]
    print(f"prime+pole done t={time.time()-t0:.0f}s", flush=True)

    vpf = np.array([float(x.mid()) for x in vp])
    vmf = np.array([float(x.mid()) for x in vm])
    _, _, Vt = np.linalg.svd(np.vstack([vpf, vmf]))
    Q = Vt[2:].T
    d = N - 2

    # ---- (a) certified negative archimedean direction -------------------
    # float minimizer of Q^T G Q, lifted to R^N, then v^T G v + pole part? NO —
    # the claim is about G alone (pole term is part of W, not G). But the family
    # is the constrained one, where the pole form is (nearly) zero anyway.
    Gf = np.array([[float(Gm[i][j].mid()) for j in range(N)] for i in range(N)])
    Mq = Q.T @ Gf @ Q
    w_, V = np.linalg.eigh(0.5 * (Mq + Mq.T))
    v = Q @ V[:, 0]
    v = v / np.linalg.norm(v)
    quad = arb(0)
    for i in range(N):
        vi = arb(float(v[i]))
        for j in range(N):
            quad += vi * arb(float(v[j])) * Gm[i][j]
    print(f"(a) v^T G v enclosure: {quad}  (float est {w_[0]:.6f})")
    neg_ok = (quad < 0)
    print(f"(a) CERTIFIED negative archimedean direction: {bool(neg_ok)}")

    # ---- (b) certified positivity of the total form ---------------------
    B = [[arb(0)] * d for _ in range(d)]
    S = [[arb(0)] * d for _ in range(d)]
    Wb = [[Gm[i][j] + Pm[i][j] + vp[i] * vm[j] + vm[i] * vp[j]
           for j in range(N)] for i in range(N)]
    for a_ in range(d):
        qa_col = [arb(float(Q[i, a_])) for i in range(N)]
        for b_ in range(a_, d):
            qb_col = [arb(float(Q[j, b_])) for j in range(N)]
            s = arb(0); ssum = arb(0)
            for i in range(N):
                ssum += qa_col[i] * qb_col[i]
                row = Wb[i]
                acc = arb(0)
                for j in range(N):
                    acc += qb_col[j] * row[j]
                s += qa_col[i] * acc
            B[a_][b_] = s; B[b_][a_] = s
            S[a_][b_] = ssum; S[b_][a_] = ssum
        print(f"B col {a_+1}/{d} t={time.time()-t0:.0f}s", flush=True)
    Bf = np.array([[float(B[i][j].mid()) for j in range(d)] for i in range(d)])
    Sf = np.array([[float(S[i][j].mid()) for j in range(d)] for i in range(d)])
    from scipy.linalg import eigh
    lam = eigh(Bf, Sf, eigvals_only=True)[0]
    print(f"(b) float generalized lambda_min = {lam:.8f}")

    def chol_pd(M):
        n = len(M)
        Lc = [[arb(0)] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                s = M[i][j]
                for k in range(j):
                    s -= Lc[i][k] * Lc[j][k]
                if i == j:
                    if not (s > 0):
                        return False
                    Lc[i][j] = s.sqrt()
                else:
                    Lc[i][j] = s / Lc[j][j]
        return True

    cc = 0.9 * lam
    while cc > 1e-9:
        M = [[B[i][j] - arb(cc) * S[i][j] for j in range(d)] for i in range(d)]
        if chol_pd(M):
            print(f"(b) CERTIFIED: W >= {cc:.9f} ||f||^2 on the explicit {d}-dim family.")
            break
        cc *= 0.7
        print(f"  retry c={cc:.9f}", flush=True)
    else:
        print("(b) certification FAILED")
        return
    if neg_ok:
        print(f"\nRESCUE CERTIFIED (L={L}, primes {c.primes}): archimedean form has a "
              f"rigorously negative direction ({quad}) on a family where the full "
              f"Weil form is rigorously >= {cc:.2e}. Positivity is created by the "
              f"prime terms. t={time.time()-t0:.0f}s")

if __name__ == '__main__':
    main()
