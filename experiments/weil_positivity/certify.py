#!/usr/bin/env python3
"""
Parametric rigorous certification of Weil-functional positivity on explicit
finite families (generalizes certify_L045.py; see T1-ARCHITECTURE.md).

Usage: certify.py L [N]
Certifies  W(f) >= c ||f||^2  for all f in the explicit (N-2)-dim family at
support half-length L, where W includes ALL prime powers n < e^{2L}:
  W(f) = 2 h_f(i/2) + (1/2pi) int h_f(r) Omega(r) dr
         - 2 sum_n (Lambda(n)/sqrt n) g_f(log n).
All entries carry Arb ball enclosures (verified integration + rigorous tails);
final bound by ball-arithmetic Cholesky. Lemma 1' (same proof as Lemma 1): for
L <= log 2, every in-window prime power n satisfies log n >= L, so
||Q_n|| <= Lambda(n)/sqrt(n) and the total prime norm is <= sum Lambda(n)/sqrt n.
"""
import numpy as np, math, sys, time
from flint import acb, arb, ctx

ctx.dps = 25

def lambda_vN(n):
    m, p = n, None
    for q in range(2, int(math.isqrt(n)) + 1):
        if m % q == 0:
            p = q
            while m % q == 0:
                m //= q
            break
    if p is None:
        p, m = n, 1
    return math.log(p) if m == 1 else 0.0

class Certifier:
    def __init__(self, L, N, tail_target=1e-6):
        self.L, self.N = L, N
        wN = self.wk(N)
        # choose R_CUT so the worst-entry tail bound is below tail_target
        R = 400.0
        while (4 * wN * wN / L) * (math.log(R) + 0.34) / (3 * (R - wN) ** 3) / math.pi > tail_target:
            R *= 1.3
        self.R_CUT = R
        self.primes = [n for n in range(2, int(math.floor(math.exp(2 * L) - 1e-12)) + 1)
                       if lambda_vN(n) > 0]

    def wk(self, k):
        return k * math.pi / (2 * self.L)

    def sincL(self, x):
        return acb(self.L) * (acb(self.L) * x).sinc()

    def F_pair_re(self, i, j, r):
        wi, wj = acb(self.wk(i)), acb(self.wk(j))
        sgn = (-1) ** (((j - i) // 2) % 2)
        return (acb(4 * sgn) * wi * wj * self.sincL(r - wi) * self.sincL(r - wj)
                / (acb(self.L) * (wi + r) * (wj + r)))

    @staticmethod
    def Omega(r):
        ir2 = acb(0, 0.5) * r
        q = acb(0.25)
        return ((q + ir2).digamma() + (q - ir2).digamma()) / acb(2) - acb(arb.pi().log())

    def G_entry(self, i, j):
        if (i + j) % 2 == 1:
            return arb(0)
        f = lambda r, _: self.F_pair_re(i, j, r) * self.Omega(r)
        val = acb.integral(f, 0, self.R_CUT).real / arb.pi()
        wi, wj, wN = self.wk(i), self.wk(j), self.wk(self.N)
        tail = (4 * wi * wj / self.L) * (math.log(self.R_CUT) + 0.34) \
            / (3 * (self.R_CUT - wN) ** 3) / math.pi
        return val + arb(0, tail)

    def phi(self, k, u):
        return (acb(self.wk(k)) * (u + acb(self.L))).sin() / arb(self.L).sqrt()

    def prime_entry(self, i, j):
        L = self.L
        tot = arb(0)
        for n in self.primes:
            a = math.log(n)
            if a >= 2 * L:
                continue
            coeff = -2 * lambda_vN(n) / math.sqrt(n)
            f1 = lambda u, _: self.phi(i, u) * self.phi(j, u - acb(a))
            f2 = lambda u, _: self.phi(j, u) * self.phi(i, u - acb(a))
            S = (acb.integral(f1, a - L, L).real + acb.integral(f2, a - L, L).real) / arb(2)
            tot += arb(coeff) * S
        return tot

    def pole_vec(self, k, sign):
        f = lambda u, _: self.phi(k, u) * (acb(sign * 0.5) * u).exp()
        return acb.integral(f, -self.L, self.L).real

    def run(self):
        t0 = time.time()
        L, N = self.L, self.N
        print(f"# certify L={L} N={N} R_CUT={self.R_CUT:.0f} primes={self.primes} dps={ctx.dps}")
        Gm = [[arb(0)] * N for _ in range(N)]
        for i in range(1, N + 1):
            for j in range(i, N + 1):
                e = self.G_entry(i, j)
                Gm[i - 1][j - 1] = e; Gm[j - 1][i - 1] = e
            print(f"G row {i}/{N} t={time.time()-t0:.0f}s", flush=True)
        Pm = [[arb(0)] * N for _ in range(N)]
        for i in range(1, N + 1):
            for j in range(i, N + 1):
                e = self.prime_entry(i, j)
                Pm[i - 1][j - 1] = e; Pm[j - 1][i - 1] = e
        vp = [self.pole_vec(k, +1) for k in range(1, N + 1)]
        vm = [self.pole_vec(k, -1) for k in range(1, N + 1)]
        print(f"prime+pole done t={time.time()-t0:.0f}s", flush=True)

        vpf = np.array([float(x.mid()) for x in vp])
        vmf = np.array([float(x.mid()) for x in vm])
        _, _, Vt = np.linalg.svd(np.vstack([vpf, vmf]))
        Q = Vt[2:].T
        d = N - 2
        B = [[arb(0)] * d for _ in range(d)]
        S = [[arb(0)] * d for _ in range(d)]
        Wb = [[Gm[i][j] + Pm[i][j] + vp[i] * vm[j] + vm[i] * vp[j]
               for j in range(N)] for i in range(N)]
        for a_ in range(d):
            for b_ in range(a_, d):
                s = arb(0); ssum = arb(0)
                for i in range(N):
                    qa = arb(float(Q[i, a_]))
                    ssum += qa * arb(float(Q[i, b_]))
                    for j in range(N):
                        s += qa * arb(float(Q[j, b_])) * Wb[i][j]
                B[a_][b_] = s; B[b_][a_] = s
                S[a_][b_] = ssum; S[b_][a_] = ssum
        Bf = np.array([[float(B[i][j].mid()) for j in range(d)] for i in range(d)])
        Sf = np.array([[float(S[i][j].mid()) for j in range(d)] for i in range(d)])
        from scipy.linalg import eigh
        lam = eigh(Bf, Sf, eigvals_only=True)[0]
        print(f"float generalized lambda_min = {lam:.8f}")

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

        c = 0.9 * lam
        while c > 1e-9:
            M = [[B[i][j] - arb(c) * S[i][j] for j in range(d)] for i in range(d)]
            if chol_pd(M):
                print(f"CERTIFIED: W >= {c:.8f} ||f||^2 on the explicit {d}-dim family "
                      f"(L={L}, primes {self.primes}). t={time.time()-t0:.0f}s")
                return c
            c *= 0.7
            print(f"  retry c={c:.8f}", flush=True)
        print("certification FAILED (enclosures too wide or subspace min <= 0)")
        return None

if __name__ == '__main__':
    L = float(sys.argv[1]) if len(sys.argv) > 1 else 0.50
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 16
    Certifier(L, N).run()
