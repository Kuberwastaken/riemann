#!/usr/bin/env python3
"""
RIGOROUS (computer-assisted, Arb ball-arithmetic) positivity certificate for the
Weil functional on an explicit finite-dimensional family at L = 0.45.

Statement being certified:
  Let phi_k(u) = sin(k pi (u+L)/(2L))/sqrt(L), k=1..N, supp in [-L,L], L=0.45.
  Let Q in R^{N x (N-2)} be the EXPLICIT float matrix below (approximate null space
  of the two pole functionals). For f = phi . Q c (any c in R^{N-2}):
      W(f) := 2 h_f(i/2) + (1/2pi) int h_f(r) Omega(r) dr
              - 2 (log2/sqrt2) g_f(log 2)
          >=  C_LOW * ||f||^2,
  where h_f = |F_f|^2, g_f = autocorrelation, and W(f) = sum over nontrivial zeta
  zeros of h_f(gamma) by the Riemann-Weil explicit formula (valid: h entire,
  O(r^-4) in the strip). All matrix entries are enclosed with Arb verified
  integration + rigorous tail bounds; the final bound via rigorous Cholesky of
  B - C_LOW * S (B = Q^T W Q, S = Q^T Q, exact float Q treated exactly).

Key regularized closed form (removable singularities eliminated):
  F_k(r) = 2 i^{1-k} w_k sincL(r - w_k) / (sqrt(L) (w_k + r)),  w_k = k pi/(2L),
  sincL(x) = sin(L x)/x  (entire).
  For i,j of the SAME parity (opposite parity blocks vanish identically):
  Re[F_i conj F_j](r) = 4 (-1)^{(j-i)/2} w_i w_j sincL(r-w_i) sincL(r-w_j)
                         / (L (w_i+r)(w_j+r)).
Prime and pole entries are 1-D verified integrals of smooth elementary functions.
"""
import numpy as np, math, os, sys, time
from flint import acb, arb, ctx

HERE = os.path.dirname(os.path.abspath(__file__))
ctx.dps = 25

L = 0.45
N = 16
A = math.log(2.0)
R_CUT = 800          # verified integration on [0, R_CUT], rigorous tail bound beyond

def wk(k): return k * math.pi / (2 * L)

def sincL(x):
    """sin(L x)/x on acb balls, safe at 0: sincL(x) = L * sinc(L x)."""
    y = acb(L) * x
    return acb(L) * y.sinc()

def F_pair_re(i, j, r):
    """Re[F_i conj F_j](r) for same-parity i,j (acb)."""
    wi, wj = acb(wk(i)), acb(wk(j))
    sgn = (-1) ** (((j - i) // 2) % 2)
    return (acb(4 * sgn) * wi * wj * sincL(r - wi) * sincL(r - wj)
            / (acb(L) * (wi + r) * (wj + r)))

def Omega_acb(r):
    """Analytic continuation of Re psi(1/4 + ir/2) - log pi off the real axis:
    the symmetrization (psi(1/4+ir/2) + psi(1/4-ir/2))/2 - log pi, which is
    analytic in r (poles only at imaginary r) and real on the real path.
    Keeping the integrand analytic is REQUIRED for Arb's rigorous integration."""
    ir2 = acb(0, 0.5) * r
    q = acb(0.25)
    return ((q + ir2).digamma() + (q - ir2).digamma()) / acb(2) - acb(arb.pi().log())

def G_entry(i, j):
    """(1/pi) int_0^inf Re[F_i conj F_j] Omega dr, verified + tail bound."""
    if (i + j) % 2 == 1:
        return arb(0)
    f = lambda r, _: F_pair_re(i, j, r) * Omega_acb(r)
    val = acb.integral(f, 0, R_CUT).real / arb.pi()
    # tail: |sincL(x)| <= 1/|x| for |x| >= wk(1) region; for r >= R_CUT > 2 w_N:
    # |Re[FiFj]| <= 4 wi wj / (L (r-wi)(r-wj)(wi+r)(wj+r)) and |Omega(r)| <= log r.
    # int_R^inf log r / (r-wN)^4 dr <= (log R + 1/3) / (3 (R-wN)^3) for R-wN >= 3.
    wi, wj = wk(i), wk(j)
    wN = wk(N)
    tailmag = (4 * wi * wj / L) * (math.log(R_CUT) + 0.34) / (3 * (R_CUT - wN) ** 3) / math.pi
    return val + arb(0, tailmag)

def prime_entry(i, j):
    """-2 (log2/sqrt2) * S_sym(a)_ij, S(a)_ij = int_{a-L}^{L} phi_i(u) phi_j(u-a) du."""
    def phi(k, u):
        return (acb(wk(k)) * (u + acb(L))).sin() / arb(L).sqrt()
    coeff = -2 * A / math.sqrt(2)
    f1 = lambda u, _: phi(i, u) * phi(j, u - acb(A))
    f2 = lambda u, _: phi(j, u) * phi(i, u - acb(A))
    S = (acb.integral(f1, A - L, L).real + acb.integral(f2, A - L, L).real) / arb(2)
    return arb(coeff) * S

def pole_vec_entry(k, sign):
    f = lambda u, _: (acb(wk(k)) * (u + acb(L))).sin() / arb(L).sqrt() * (acb(sign * 0.5) * u).exp()
    return acb.integral(f, -L, L).real

def main():
    t0 = time.time()
    print(f"# Certified Weil positivity, L={L}, N={N}, R_CUT={R_CUT}, dps={ctx.dps}")
    Gm = [[arb(0)] * N for _ in range(N)]
    for i in range(1, N + 1):
        for j in range(i, N + 1):
            e = G_entry(i, j)
            Gm[i - 1][j - 1] = e
            Gm[j - 1][i - 1] = e
        print(f"G row {i} done  t={time.time()-t0:.0f}s", flush=True)
    Pm = [[arb(0)] * N for _ in range(N)]
    for i in range(1, N + 1):
        for j in range(i, N + 1):
            e = prime_entry(i, j)
            Pm[i - 1][j - 1] = e
            Pm[j - 1][i - 1] = e
    print(f"prime matrix done t={time.time()-t0:.0f}s", flush=True)
    vp = [pole_vec_entry(k, +1) for k in range(1, N + 1)]
    vm = [pole_vec_entry(k, -1) for k in range(1, N + 1)]
    print(f"pole vectors done t={time.time()-t0:.0f}s", flush=True)

    # float midpoints -> explicit Q (approximate constraint null space)
    vpf = np.array([float(x.mid()) for x in vp])
    vmf = np.array([float(x.mid()) for x in vm])
    _, _, Vt = np.linalg.svd(np.vstack([vpf, vmf]))
    Q = Vt[2:].T                                  # N x (N-2), EXACT float matrix
    print("Q chosen (exact float); constraint residuals:",
          float(np.abs(Q.T @ vpf).max()), float(np.abs(Q.T @ vmf).max()))

    # rigorous W = G + P + pole outer products, then B = Q^T W Q in ball arithmetic
    def to_arb(x): return arb(float(x))
    B = [[arb(0)] * (N - 2) for _ in range(N - 2)]
    S = [[arb(0)] * (N - 2) for _ in range(N - 2)]
    for a_ in range(N - 2):
        for b_ in range(a_, N - 2):
            s = arb(0); ssum = arb(0)
            for i in range(N):
                qa = to_arb(Q[i, a_])
                ssum += qa * to_arb(Q[i, b_])
                for j in range(N):
                    qb = to_arb(Q[j, b_])
                    w_ij = Gm[i][j] + Pm[i][j] + vp[i] * vm[j] + vm[i] * vp[j]
                    s += qa * qb * w_ij
            B[a_][b_] = s; B[b_][a_] = s
            S[a_][b_] = ssum; S[b_][a_] = ssum
    print(f"B assembled t={time.time()-t0:.0f}s", flush=True)

    # float eigen estimate, then certify B - c S >= 0 by rigorous Cholesky
    Bf = np.array([[float(B[i][j].mid()) for j in range(N - 2)] for i in range(N - 2)])
    Sf = np.array([[float(S[i][j].mid()) for j in range(N - 2)] for i in range(N - 2)])
    from scipy.linalg import eigh
    lam = eigh(Bf, Sf, eigvals_only=True)[0]
    print(f"float generalized lambda_min = {lam:.6f}")

    def cholesky_pd(M):
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

    c = 0.9 * lam
    while c > 1e-6:
        M = [[B[i][j] - arb(c) * S[i][j] for j in range(N - 2)] for i in range(N - 2)]
        if cholesky_pd(M):
            print(f"CERTIFIED: W >= {c:.6f} * ||f||^2 on the explicit {N-2}-dim family "
                  f"(L={L}, prime-2 active, beyond CC ratio-2 window).")
            print(f"total time {time.time()-t0:.0f}s")
            return
        c *= 0.7
        print(f"  retry with c={c:.6f}", flush=True)
    print("certification failed down to c=1e-6 (enclosures too wide)")

if __name__ == '__main__':
    main()
