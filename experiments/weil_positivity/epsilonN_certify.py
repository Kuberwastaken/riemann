#!/usr/bin/env python3
"""
epsilonN_certify.py — certified sign, SIMPLICITY and PARITY SECTOR of the
lowest eigenvalue eps_N of finite sections of the Weil form: rigorous
verification, in concrete windows, of the two unverified hypotheses of
Connes-Consani-Moscovici 2025 (arXiv:2511.22755) Theorem 1.1 ("Let eps_N be
the smallest eigenvalue of QW_lambda^N *assumed simple* and xi the
corresponding eigenvector *assumed even*"), for the finite sections this
laboratory certifies.  Their Prop. 3.4 states the full-space infimum of
QW_lambda is the N->infty limit of exactly such finite-section eigenvalues.

Usage: epsilonN_certify.py L [N] [dps] [tail_target]

Family (T1-ARCHITECTURE.md conventions): phi_k(u) = sin(k pi (u+L)/(2L))/sqrt(L),
k = 1..N — an orthonormal basis of L^2[-L, L]; all in-window prime powers
n < e^{2L} included.  W(f) = 2 h_f(i/2) + (1/2pi) int h_f(r) Omega(r) dr
- 2 sum_n (Lambda(n)/sqrt n) g_f(log n).  The verified-integration core
(analytically symmetrized digamma kernel, rigorous tails, verified prime/pole
entries, ball Cholesky) is REUSED from certify.py by inheritance — only the
per-entry integration cutoff R (chosen so each entry's rigorous tail bound is
below tail_target) is new.

EXACT PARITY STRUCTURE (proofs in EPSILON-N.md; verified numerically here):
  (P1) phi_k(-u) = (-1)^{k+1} phi_k(u): k odd -> even sector, k even -> odd.
  (P2) Archimedean entries vanish for i+j odd (already exact in certify.py).
  (P3) Prime entries vanish for i+j odd: the symmetrized autocorrelation form
       b_a(f,g) = (1/2) int [f(u)g(u-a) + g(u)f(u-a)] du satisfies
       b_a(f(-.), g(-.)) = b_{-a}(f,g) = b_a(f,g), so opposite-parity entries
       equal their own negative.
  (P4) The pole rank-two term:  vp_k = int phi_k e^{u/2},  vm_k = int phi_k e^{-u/2}
       obey vm_k = (-1)^{k+1} vp_k (change of variables u -> -u), hence with
       v+_k = int phi_k cosh(u/2) (= 0 for k even),
       v-_k = int phi_k sinh(u/2) (= 0 for k odd):
         vp (x) vm + vm (x) vp  =  2 (v+ (x) v+  -  v- (x) v-)   [exact identity]
       i.e. the pole term is +2 v+ v+^T on the even sector and -2 v- v-^T on
       the odd sector.  NOTE: the two pole constraints are NOT both even-sector
       functionals; span{vp, vm} = span{v+, v-} = one constraint per sector.
Consequently W = W_even (+) W_odd EXACTLY, and both the unconstrained sections
and the pole-constrained family block-diagonalize by parity.

Two certified problems per window:
  [U] UNCONSTRAINED sections (CCM convention: pole term active inside the
      form, S = I since phi_k is orthonormal): eps_N^U = lambda_min(W_N).
  [C] POLE-CONSTRAINED family (certify.py / T1 convention): per sector an
      EXPLICIT float matrix Q orthogonal (to float accuracy) to that sector's
      pole vector; B = Q^T W_sector Q with the pole term retained in W so the
      certificate covers the explicit family exactly as in certify.py.

Certification method per symmetric ball matrix pencil (M, S):
  1. float spectral decomposition Y of (mid M, mid S)  [heuristic only];
  2. ball matrices D = Y^T M Y, E = Y^T S Y (Y exact float, products in Arb);
  3. delta = rigorous row-sum bound on ||E - I||_2 (Gershgorin for symmetric
     matrices); require delta < 1/2;
  4. Gershgorin discs of D: disc_i = [lo(D_ii) - R_i, hi(D_ii) + R_i] with
     R_i = sum_{j != i} sup|D_ij| — each connected component ("cluster") of
     k discs contains exactly k eigenvalues of D;
  5. pencil correction: eigenvalues of (M,S) = eigenvalues of (D,E) and, with
     ||E - I|| <= delta, Courant-Fischer with the pointwise monotone bounds
     h(t) = t/(1+delta) [t>=0], t/(1-delta) [t<0]   (lower)
     H(t) = t/(1-delta) [t>=0], t/(1+delta) [t<0]   (upper)
     gives lambda_i(M,S) in [h(lambda_i(D)), H(lambda_i(D))];
  6. if the lowest cluster is not a singleton, refine once by
     re-diagonalizing mid(D) and folding the rotation into Y (Jacobi-type);
  7. independent sign certificate: ball Cholesky of M - c S (chol_pd copied
     verbatim from certify.py), same c on both sectors.
All float post-processing of ball endpoints uses directed bounds
(arb.upper/lower/abs_upper) inflated by a relative slop 1e-13 — strictly
conservative.  Soundness rests on Arb; float eigenvectors are never trusted.
"""
import math
import os
import sys
import time

import numpy as np
from scipy.linalg import eigh

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from certify import Certifier  # noqa: E402  (verified-integration core, reused)
from flint import acb, arb, ctx  # noqa: E402

SLOP = 1e-13


# ---------- lossless ball serialization (for multiprocessing) ----------
def ball_ser(x):
    """arb ball -> ints (exact: mid and rad are dyadic)."""
    mm, me = x.mid().man_exp()
    rm, re = x.rad().man_exp()
    return (int(mm), int(me), int(rm), int(re))


def ball_deser(t):
    """ints -> arb ball containing the original (radius inflated ~1e-9 rel)."""
    mm, me, rm, re = t
    mid = arb(mm) * arb(2) ** int(me)
    rad = float(arb(rm) * arb(2) ** int(re))
    return mid + arb(0, rad * (1 + 1e-9) + 1e-300)


_W = None  # per-process certifier


def _init_worker(L, N, dps, tail_target):
    global _W
    ctx.dps = dps
    _W = EpsN(L, N, tail_target)


def _entry_job(ij):
    i, j = ij
    return ball_ser(_W.G_entry(i, j) + _W.prime_entry(i, j))


# ---------- sound float bounds from balls ----------
def fub(x):
    u = float(x.upper())
    return u + abs(u) * SLOP


def flb(x):
    l = float(x.lower())
    return l - abs(l) * SLOP


def fub_abs(x):
    u = float(x.abs_upper())
    return u + abs(u) * SLOP


# ---------- ball linear algebra helpers ----------
def ball_congruence(Y, M):
    """D = Y^T M Y with Y an exact float matrix (n x k), M a ball matrix."""
    n, k = Y.shape
    Yb = [[arb(float(Y[i, j])) for j in range(k)] for i in range(n)]
    C = [[arb(0)] * k for _ in range(n)]  # C = M Y
    for i in range(n):
        for j in range(k):
            s = arb(0)
            for l in range(n):
                s += M[i][l] * Yb[l][j]
            C[i][j] = s
    D = [[arb(0)] * k for _ in range(k)]
    for i in range(k):
        for j in range(i, k):
            s = arb(0)
            for l in range(n):
                s += Yb[l][i] * C[l][j]
            D[i][j] = s
            D[j][i] = s
    return D


def mid_matrix(M):
    return np.array([[float(M[i][j].mid()) for j in range(len(M))]
                     for i in range(len(M))])


def clusters(discs):
    """Merge sorted Gershgorin discs into connected components.
    Returns list of (count, LO, HI); component of k discs holds exactly k
    eigenvalues."""
    out = []
    for lo, hi in sorted(discs):
        if out and lo <= out[-1][2]:
            cnt, l0, h0 = out[-1]
            out[-1] = (cnt + 1, l0, max(h0, hi))
        else:
            out.append((1, lo, hi))
    return out


def pencil_correct(t, delta, side):
    """Endpoint transform for eigenvalues of (D, I+Delta), ||Delta||<=delta."""
    if side == 'lo':
        v = t / (1 + delta) if t >= 0 else t / (1 - delta)
        return v - abs(v) * SLOP
    v = t / (1 - delta) if t >= 0 else t / (1 + delta)
    return v + abs(v) * SLOP


def analyze(M, S, label, refine=True):
    """Rigorous eigenvalue cluster enclosures of the pencil (M, S).
    S may be None (identity). Returns (clusters, delta, note)."""
    m = len(M)
    Mf = mid_matrix(M)
    Sf = mid_matrix(S) if S is not None else None
    _, Y = eigh(Mf, Sf)
    note = ''
    for attempt in range(3):
        D = ball_congruence(Y, M)
        if S is not None:
            E = ball_congruence(Y, S)
        else:
            # E = Y^T Y in ball arithmetic (Y is float-orthogonal only)
            E = ball_congruence(Y, [[arb(1) if i == j else arb(0)
                                     for j in range(m)] for i in range(m)])
        delta = max(
            sum(fub_abs(E[i][j] - (arb(1) if i == j else arb(0)))
                for j in range(m))
            for i in range(m))
        discs = []
        for i in range(m):
            R = sum(fub_abs(D[i][j]) for j in range(m) if j != i)
            discs.append((flb(D[i][i]) - R, fub(D[i][i]) + R))
        cl = clusters(discs)
        if cl[0][0] == 1 and (len(cl) == 1 or cl[0][2] < cl[1][1]):
            break
        if not refine or attempt == 2:
            note = ' [lowest cluster NOT isolated after refinement]'
            break
        _, Z = eigh(mid_matrix(D))
        Y = Y @ Z
        note = ' [refined x%d]' % (attempt + 1)
    if not delta < 0.5:
        raise RuntimeError('%s: delta=%g too large' % (label, delta))
    corr = [(cnt, pencil_correct(lo, delta, 'lo'),
             pencil_correct(hi, delta, 'hi')) for cnt, lo, hi in cl]
    return corr, delta, note


def chol_pd(M):
    """Ball Cholesky positive-definiteness test (verbatim from certify.py)."""
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


def sign_certificate(blocks, lam_float):
    """Largest c (from 0.98*lam_float, shrinking) with all blocks M - c S
    certified PD by ball Cholesky. blocks = [(M, S or None), ...]."""
    if not lam_float > 0:
        return None
    c = 0.98 * lam_float
    while c > 1e-12:
        ok = True
        for M, S in blocks:
            n = len(M)
            if S is None:
                A = [[M[i][j] - (arb(c) if i == j else arb(0))
                      for j in range(n)] for i in range(n)]
            else:
                A = [[M[i][j] - arb(c) * S[i][j] for j in range(n)]
                     for i in range(n)]
            if not chol_pd(A):
                ok = False
                break
        if ok:
            return c
        c *= 0.7
    return None


# ---------- the certifier ----------
class EpsN(Certifier):
    """Certifier with (i) BALL frequencies w_k = k pi/(2L) — L is the exact
    dyadic double defining the window, so the certified family is EXACTLY
    phi_k(u) = sin(k pi (u+L)/(2L))/sqrt(L) and the parity facts (P1)-(P4)
    are exact mathematics for it (with double frequencies they would hold
    only to ~1e-16); (ii) per-entry integration cutoff R.  The integrand
    formulas are verbatim from certify.py."""

    def __init__(self, L, N, tail_target=1e-9):
        super().__init__(L, N, tail_target)
        self.tail_target = tail_target
        self.R_used = []
        self.Lb = arb(self.L)  # exact

    def wkb(self, k):
        return arb(k) * arb.pi() / (2 * self.Lb)  # ball enclosure of k pi/(2L)

    def F_pair_re(self, i, j, r):
        # same formula as certify.py, ball frequencies
        wi, wj = acb(self.wkb(i)), acb(self.wkb(j))
        sgn = (-1) ** (((j - i) // 2) % 2)
        return (acb(4 * sgn) * wi * wj * self.sincL(r - wi) * self.sincL(r - wj)
                / (acb(self.L) * (wi + r) * (wj + r)))

    def phi(self, k, u):
        # same formula as certify.py, ball frequency
        return (acb(self.wkb(k)) * (u + acb(self.L))).sin() / arb(self.L).sqrt()

    def R_entry(self, i, j):
        """Smallest R with the (recomputed, rigorous) tail bound <= target."""
        wN = self.wk(self.N)
        pref = (4 * self.wk(i) * self.wk(j) / self.L) / (3 * math.pi
                                                         * self.tail_target)
        R = max(400.0, wN + 10.0)
        for _ in range(60):
            R2 = wN + (pref * (math.log(R) + 0.34)) ** (1.0 / 3)
            if R2 <= R * (1 + 1e-9):
                break
            R = R2
        return max(R * 1.001, 400.0, wN + 10.0)

    def G_entry(self, i, j):
        """Same as certify.py but with per-entry cutoff; tail bound formula
        identical (recomputed from the R actually used, so rigor does not
        depend on how R was chosen). Integral split into chunks (additive)."""
        if (i + j) % 2 == 1:
            return arb(0)
        R = self.R_entry(i, j)
        self.R_used.append(R)
        f = lambda r, _: self.F_pair_re(i, j, r) * self.Omega(r)
        val = arb(0)
        a = 0.0
        while a < R:
            b = min(a + 4000.0, R)
            val += acb.integral(f, a, b).real
            a = b
        val /= arb.pi()
        wi, wj, wN = self.wk(i), self.wk(j), self.wk(self.N)
        tail = (4 * wi * wj / self.L) * (math.log(R) + 0.34) \
            / (3 * (R - wN) ** 3) / math.pi
        return val + arb(0, tail)

    def pole_even(self, k):
        f = lambda u, _: self.phi(k, u) * (acb(0.5) * u).cosh()
        return acb.integral(f, -self.L, self.L).real

    def pole_odd(self, k):
        f = lambda u, _: self.phi(k, u) * (acb(0.5) * u).sinh()
        return acb.integral(f, -self.L, self.L).real

    def pole_exp(self, k, sign):
        f = lambda u, _: self.phi(k, u) * (acb(sign * 0.5) * u).exp()
        return acb.integral(f, -self.L, self.L).real

    def build_sector(self, I, sgn, t0, pool=None):
        """Ball matrix of W restricted to the sector spanned by {phi_k: k in I}
        (sgn=+1 even sector, -1 odd), plus that sector's pole vector."""
        m = len(I)
        A = [[arb(0)] * m for _ in range(m)]
        name = 'even' if sgn > 0 else 'odd'
        pairs = [(I[a], I[b]) for a in range(m) for b in range(a, m)]
        if pool is None:
            vals = {}
            for n_, (i, j) in enumerate(pairs):
                vals[(i, j)] = self.G_entry(i, j) + self.prime_entry(i, j)
                if (n_ + 1) % m == 0:
                    print("  sector %s entry %d/%d t=%.0fs"
                          % (name, n_ + 1, len(pairs), time.time() - t0),
                          flush=True)
        else:
            order = sorted(pairs, key=lambda p: -self.R_entry(*p))
            out = pool.map(_entry_job, order, chunksize=1)
            vals = {p: ball_deser(t) for p, t in zip(order, out)}
            self.R_used += [self.R_entry(*p) for p in pairs]
            print("  sector %s: %d entries done (pool) t=%.0fs"
                  % (name, len(pairs), time.time() - t0), flush=True)
        for a in range(m):
            for b in range(a, m):
                A[a][b] = vals[(I[a], I[b])]
                A[b][a] = A[a][b]
        v = [self.pole_even(k) if sgn > 0 else self.pole_odd(k) for k in I]
        W = [[A[a][b] + arb(2 * sgn) * v[a] * v[b] for b in range(m)]
             for a in range(m)]
        return W, v


def fmt_cl(cl):
    return ' | '.join('%d in [%.10e, %.10e]' % c for c in cl[:3]) \
        + (' | ...' if len(cl) > 3 else '')


def summarize(cle, clo, tag):
    """Combine per-sector certified clusters into the global statement."""
    lo1 = min(cle[0][1], clo[0][1])
    hi1 = min(cle[0][2], clo[0][2])
    print("%s eps_N enclosure (Gershgorin): [%.10e, %.10e]" % (tag, lo1, hi1))
    sign = 'POSITIVE' if lo1 > 0 else ('NEGATIVE' if hi1 < 0 else 'UNDECIDED')
    print("%s certified sign (Gershgorin): %s" % (tag, sign))
    if cle[0][2] < clo[0][1]:
        sect, own, other = 'EVEN', cle, clo
    elif clo[0][2] < cle[0][1]:
        sect, own, other = 'ODD', clo, cle
    else:
        print("%s sector of minimizer: UNRESOLVED (lowest clusters overlap)"
              % tag)
        return lo1, hi1
    print("%s sector of minimizer: %s (certified: min %s cluster [%.6e, %.6e]"
          " < other-sector min >= %.6e)"
          % (tag, sect, sect.lower(), own[0][1], own[0][2], other[0][1]))
    if own[0][0] != 1:
        print("%s SIMPLICITY: FAILED to certify (lowest cluster has %d discs)"
              % (tag, own[0][0]))
        return lo1, hi1
    lam2_lb = other[0][1]
    lam2_ub = other[0][2]
    if len(own) > 1:
        lam2_lb = min(lam2_lb, own[1][1])
        lam2_ub = min(lam2_ub, own[1][2])
    if own[0][2] < lam2_lb:
        print("%s SIMPLICITY: certified. lambda_2 in [%.10e, %.10e];"
              " certified gap lambda_2 - lambda_1 >= %.10e"
              % (tag, lam2_lb, lam2_ub, lam2_lb - own[0][2]))
    else:
        print("%s SIMPLICITY: FAILED to certify (lambda_2 lower bound %.3e"
              " <= lambda_1 upper bound %.3e)" % (tag, lam2_lb, own[0][2]))
    return lo1, hi1


def main():
    L = float(sys.argv[1]) if len(sys.argv) > 1 else 0.50
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 24
    dps = int(sys.argv[3]) if len(sys.argv) > 3 else 25
    tail_target = float(sys.argv[4]) if len(sys.argv) > 4 else 1e-9
    ctx.dps = dps
    t0 = time.time()
    C = EpsN(L, N, tail_target)
    print("# epsilonN_certify L=%g N=%g dps=%d tail_target=%.1e primes=%s"
          % (L, N, dps, tail_target, C.primes))
    print("# CCM dictionary: lambda = e^L = %.6f (interval [1/lambda, lambda],"
          " evenness = invariance under u -> 1/u)" % math.exp(L))

    # --- numerical verification of the exact parity facts (P3), (P4) ---
    p12 = C.prime_entry(1, 2)
    pe2 = C.pole_even(2)
    po1 = C.pole_odd(1)
    vp1 = C.pole_exp(1, +1)
    vm2 = C.pole_exp(2, -1)
    ck1 = vp1 - (C.pole_even(1) + C.pole_odd(1))
    ck2 = vm2 - (C.pole_even(2) - C.pole_odd(2))
    print("parity checks (all balls must contain 0):")
    print("  prime cross-parity entry (1,2): %s  contains0=%s"
          % (p12.str(5), p12.contains(arb(0))))
    print("  v+_2 (cosh, k even): %s  contains0=%s"
          % (pe2.str(5), pe2.contains(arb(0))))
    print("  v-_1 (sinh, k odd):  %s  contains0=%s"
          % (po1.str(5), po1.contains(arb(0))))
    print("  vp_1-(v+_1+v-_1): %s  contains0=%s" % (ck1.str(5),
                                                    ck1.contains(arb(0))))
    print("  vm_2-(v+_2-v-_2): %s  contains0=%s" % (ck2.str(5),
                                                    ck2.contains(arb(0))))
    ok_par = all([p12.contains(arb(0)), pe2.contains(arb(0)),
                  po1.contains(arb(0)), ck1.contains(arb(0)),
                  ck2.contains(arb(0))])
    print("  parity structure verified: %s" % ok_par)

    # --- build sector ball matrices ---
    idx_e = [k for k in range(1, N + 1) if k % 2 == 1]  # even sector
    idx_o = [k for k in range(1, N + 1) if k % 2 == 0]  # odd sector
    nprocs = int(os.environ.get('EPSN_PROCS', '1'))
    pool = None
    if nprocs > 1:
        import multiprocessing as mp
        pool = mp.get_context('fork').Pool(
            nprocs, initializer=_init_worker, initargs=(L, N, dps, tail_target))
        print("# using %d worker processes" % nprocs)
    We, ve = C.build_sector(idx_e, +1, t0, pool)
    Wo, vo = C.build_sector(idx_o, -1, t0, pool)
    if pool is not None:
        pool.close()
        pool.join()
    print("entries done t=%.0fs; R_entry range [%.0f, %.0f]"
          % (time.time() - t0, min(C.R_used), max(C.R_used)), flush=True)

    # ================= [U] unconstrained sections (CCM convention) ========
    print("\n[U] UNCONSTRAINED %dx%d sections (pole term inside the form; "
          "dim %d = %d even + %d odd)" % (N, N, N, len(idx_e), len(idx_o)))
    cle, de, ne = analyze(We, None, 'U-even')
    clo, do, no = analyze(Wo, None, 'U-odd')
    print("U even sector: delta=%.2e%s  clusters: %s" % (de, ne, fmt_cl(cle)))
    print("U odd  sector: delta=%.2e%s  clusters: %s" % (do, no, fmt_cl(clo)))
    encU = summarize(cle, clo, '[U]')
    lamUf = min(np.linalg.eigvalsh(mid_matrix(We))[0],
                np.linalg.eigvalsh(mid_matrix(Wo))[0])
    cU = sign_certificate([(We, None), (Wo, None)], lamUf)
    print("[U] ball-Cholesky sign certificate: "
          + ("W_N >= %.10e on the FULL %d-dim section" % (cU, N)
         if cU else "none (lambda_min <= 0 or enclosures too wide)"))
    if encU is not None and cU is not None:
        print("[U] COMBINED certified enclosure: eps_N in [%.10e, %.10e]"
              % (max(encU[0], cU), encU[1]))

    # ================= [C] pole-constrained family (certify.py convention) =
    print("\n[C] POLE-CONSTRAINED family (explicit float Q per sector; "
          "dim %d = %d + %d)" % (N - 2, len(idx_e) - 1, len(idx_o) - 1))
    res = {}
    for name, W, v, m in (('even', We, ve, len(idx_e)),
                          ('odd', Wo, vo, len(idx_o))):
        vf = np.array([float(x.mid()) for x in v])
        _, _, Vt = np.linalg.svd(vf.reshape(1, -1))
        Q = Vt[1:].T  # m x (m-1), exact float
        resid = max(fub_abs(sum(arb(float(Q[i, a])) * v[i] for i in range(m)))
                    for a in range(m - 1))
        B = ball_congruence(Q, W)
        Qb = [[arb(float(Q[i, j])) for j in range(m - 1)] for i in range(m)]
        S = [[sum(Qb[l][i] * Qb[l][j] for l in range(m))
              for j in range(m - 1)] for i in range(m - 1)]
        cl, dl, nt = analyze(B, S, 'C-' + name)
        res[name] = (B, S, cl)
        print("C %s sector: constraint residual <= %.1e  delta=%.2e%s"
              % (name, resid, dl, nt))
        print("  clusters: %s" % fmt_cl(cl))
    encC = summarize(res['even'][2], res['odd'][2], '[C]')
    lamCf = min(eigh(mid_matrix(res['even'][0]), mid_matrix(res['even'][1]),
                     eigvals_only=True)[0],
                eigh(mid_matrix(res['odd'][0]), mid_matrix(res['odd'][1]),
                     eigvals_only=True)[0])
    cC = sign_certificate([(res['even'][0], res['even'][1]),
                           (res['odd'][0], res['odd'][1])], lamCf)
    print("[C] ball-Cholesky sign certificate: "
          + ("W >= %.10e ||f||^2 on the explicit %d-dim family" % (cC, N - 2)
         if cC else "none (lambda_min <= 0 or enclosures too wide)"))
    if encC is not None and cC is not None:
        print("[C] COMBINED certified enclosure: eps_N in [%.10e, %.10e]"
              % (max(encC[0], cC), encC[1]))

    print("\ntotal time %.0f s  (dps=%d, tail_target=%.1e)"
          % (time.time() - t0, dps, tail_target))


if __name__ == '__main__':
    main()
