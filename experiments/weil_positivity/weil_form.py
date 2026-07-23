#!/usr/bin/env python3
"""
Numerical exploration of Weil positivity in the critical support window.
Target: T1 of ATTACK.md — the {infinity, 2} semilocal Weil positivity question.

Setup (additive coordinates u = log x):
  f real, smooth-ish, supported in [-L, L];  F(r) = int f(u) e^{iru} du
  h(r) = F(r) F(-r)  (= |F(r)|^2 for real r, real f)
  g(u) = autocorrelation (f star f~)(u) = int f(t) f(t-u) dt,  supp g in [-2L, 2L]

Riemann-Weil explicit formula (Montgomery's normalization):
  sum_gamma h(gamma) = 2 h(i/2)
                       + (1/2pi) int h(r) Omega(r) dr
                       - 2 sum_{n>=2} (Lambda(n)/sqrt(n)) g(log n)
  where Omega(r) = Re psi(1/4 + ir/2) - log pi,  psi = digamma,
  and gamma runs over all nontrivial zeros rho = 1/2 + i*gamma (gamma complex
  iff RH fails), counted with multiplicity, both signs.

Weil positivity: RH  <=>  sum_gamma h(gamma) >= 0 for all such f (all L),
with the pole term killed by the two linear constraints
  v_plus . f = int f(u) e^{u/2} du = 0,   v_minus . f = int f(u) e^{-u/2} du = 0.

Prime thresholds: the term for n = p^k activates when log n < 2L.
The window L < log(2)/2 = 0.34657 is PRIME-FREE: there Weil positivity is the
(proven) Connes-Consani 2020 archimedean theorem. The first arithmetic term is
p = 2, entering at L = 0.34657 as an explicit rank-structured perturbation.

This script:
  1. builds the arithmetic-side matrix of the form in an orthonormal sine basis;
  2. VALIDATES it against the spectral side computed from Odlyzko's 100k zeros
     (the explicit formula is an identity: agreement certifies all conventions);
  3. sweeps L, reporting
        margin(L)  = lambda_min of the archimedean form on the constrained space
        total(L)   = lambda_min of the full form (arch + primes) there
        deficit(L) = operator norm of the prime part there
     -> total >= 0 must hold if RH holds (numerical probe of T1);
     -> margin > deficit means T1 is PERTURBATIVE from CC 2020;
        margin < deficit < still total >= 0 means T1 is CANCELLATIVE (the
        Euler product genuinely enters) — the key structural question;
     -> the L* where margin(L) itself goes negative marks where positivity
        becomes irreducibly arithmetic.

Basis: phi_k(u) = sin(k pi (u+L)/(2L)) / sqrt(L), k = 1..N (orthonormal, L^2).
Fourier transform (exact):
  F_k(r) = e^{-irL} w_k (1 - (-1)^k e^{2iLr}) / (sqrt(L) (w_k^2 - r^2)),
  w_k = k pi/(2L);  removable singularity at r = w_k with limit i L e^{-i w_k L}/sqrt(L).
"""
import numpy as np
import sys, os, csv, math

HERE = os.path.dirname(os.path.abspath(__file__))
LOG2 = math.log(2.0)

# ----------------------------------------------------------------------
# complex digamma, vectorized (recurrence + asymptotic series)
BERN = [1/12, -1/120, 1/252, -1/240, 1/132, -691/32760, 1/12]

def digamma_c(z0):
    z = np.array(z0, dtype=complex)
    acc = np.zeros_like(z)
    for _ in range(16):
        m = np.abs(z) < 14.0
        if not m.any():
            break
        acc[m] -= 1.0 / z[m]
        z[m] += 1.0
    zi = 1.0 / z
    zi2 = zi * zi
    s = np.zeros_like(z)
    p = zi2.copy()
    for c in BERN:
        s += c * p
        p *= zi2
    return acc + np.log(z) - 0.5 * zi - s

def Omega(r):
    """Archimedean kernel Re psi(1/4 + ir/2) - log pi (vectorized, r real)."""
    return digamma_c(0.25 + 0.5j * np.asarray(r, float)).real - math.log(math.pi)

# ----------------------------------------------------------------------
def F_basis(r, L, N):
    """F_k(r) for k=1..N at real r (1-D array). Returns (N, len(r)) complex."""
    r = np.asarray(r, float)
    k = np.arange(1, N + 1)[:, None]
    w = k * math.pi / (2 * L)
    sign = (-1.0) ** k
    num = 1.0 - sign * np.exp(2j * L * r)[None, :]
    den = (w * w - r * r)[...]
    out = np.empty((N, r.size), complex)
    with np.errstate(divide='ignore', invalid='ignore'):
        out = np.exp(-1j * r * L)[None, :] * w * num / (math.sqrt(L) * den)
    # removable singularities |r - w_k| tiny -> limit i L e^{-i w_k L}/sqrt(L)
    bad = np.abs(np.abs(r)[None, :] - w) < 1e-8
    if bad.any():
        ki, ri = np.nonzero(bad)
        wk = (ki + 1) * math.pi / (2 * L)
        out[ki, ri] = 1j * L * np.exp(-1j * wk * L) / math.sqrt(L)
    return out

# ----------------------------------------------------------------------
def arch_matrix(L, N):
    """G_ij = (1/pi) * int_0^inf Re[F_i conj(F_j)] Omega(r) dr  (trapezoid, segmented)."""
    segs = [(1e-9, 60.0, 2e-3), (60.0, 400.0, 5e-3),
            (400.0, 4000.0, 0.05), (4000.0, 40000.0, 0.2)]
    G = np.zeros((N, N))
    for a, b, dr in segs:
        r = np.arange(a, b, dr)
        wgt = np.full(r.size, dr)
        wgt[0] *= 0.5
        wgt[-1] *= 0.5
        for lo in range(0, r.size, 60000):
            sl = slice(lo, min(lo + 60000, r.size))
            F = F_basis(r[sl], L, N)
            om = Omega(r[sl]) * wgt[sl]
            G += ((F * om) @ F.conj().T).real
    return G / math.pi

# ----------------------------------------------------------------------
def phi_samples(u, L, N):
    """phi_k(u) sampled, zero outside [-L, L]. Returns (N, len(u))."""
    u = np.asarray(u, float)
    k = np.arange(1, N + 1)[:, None]
    inside = (np.abs(u) <= L)
    vals = np.sin(k * math.pi * (u[None, :] + L) / (2 * L)) / math.sqrt(L)
    return np.where(inside[None, :], vals, 0.0)

def simpson_w(n, h):
    w = np.ones(n)
    w[1:-1:2] = 4.0
    w[2:-1:2] = 2.0
    return w * (h / 3.0)

def overlap_matrix(a, L, N, npts=4097):
    """S_ij(a) = int phi_i(u) phi_j(u-a) du  (a>0), symmetrized."""
    lo, hi = a - L, L
    if hi <= lo:
        return np.zeros((N, N))
    u = np.linspace(lo, hi, npts)
    w = simpson_w(npts, u[1] - u[0])
    Pi = phi_samples(u, L, N)
    Pj = phi_samples(u - a, L, N)
    S = (Pi * w) @ Pj.T
    return 0.5 * (S + S.T)

def prime_matrix(L, N):
    """P = -2 sum_{n=p^k < e^{2L}} (Lambda(n)/sqrt(n)) S(log n); also per-n dict."""
    nmax = int(math.floor(math.exp(2 * L) - 1e-12))
    P = np.zeros((N, N))
    pieces = {}
    for n in range(2, nmax + 1):
        # Lambda(n): log p if n = p^k
        m, p = n, None
        for q in range(2, int(math.isqrt(n)) + 1):
            if m % q == 0:
                p = q
                while m % q == 0:
                    m //= q
                break
        if p is None:
            p, m = n, 1
        if m != 1:
            continue
        lam = math.log(p)
        piece = -2.0 * (lam / math.sqrt(n)) * overlap_matrix(math.log(n), L, N)
        pieces[n] = piece
        P += piece
    return P, pieces

# ----------------------------------------------------------------------
def pole_vectors(L, N, npts=4097):
    u = np.linspace(-L, L, npts)
    w = simpson_w(npts, u[1] - u[0])
    Phi = phi_samples(u, L, N)
    vp = Phi @ (w * np.exp(u / 2.0))   # int phi_k e^{+u/2}
    vm = Phi @ (w * np.exp(-u / 2.0))  # int phi_k e^{-u/2}
    return vp, vm

def constrained_basis(vp, vm):
    """Orthonormal basis Q of {f : vp.f = vm.f = 0} (N x (N-2))."""
    A = np.vstack([vp, vm])
    _, _, Vt = np.linalg.svd(A, full_matrices=True)
    return Vt[2:].T

# ----------------------------------------------------------------------
def spectral_matrix(L, N, zeros):
    """W_spec_ij = 2 sum_{gamma>0} Re[F_i(gamma) conj F_j(gamma)] (both zero signs)."""
    W = np.zeros((N, N))
    for lo in range(0, zeros.size, 50000):
        F = F_basis(zeros[lo:lo + 50000], L, N)
        W += 2.0 * (F @ F.conj().T).real
    return W

# ----------------------------------------------------------------------
def load_zeros():
    z = np.loadtxt(os.path.join(HERE, 'zeros1.txt'))
    assert z.size >= 99999 and abs(z[0] - 14.134725142) < 1e-6
    return z

def eig_min(M, Q):
    Mq = Q.T @ M @ Q
    ev = np.linalg.eigvalsh(0.5 * (Mq + Mq.T))
    return ev

def build_all(L, N):
    G = arch_matrix(L, N)
    P, pieces = prime_matrix(L, N)
    vp, vm = pole_vectors(L, N)
    Q = constrained_basis(vp, vm)
    PoleM = np.outer(vp, vm) + np.outer(vm, vp)
    return G, P, pieces, vp, vm, Q, PoleM

# ----------------------------------------------------------------------
def cmd_test():
    import mpmath
    ok = True
    for z in [0.25, 0.25 + 2.5j, 0.25 + 7j, 3.0 + 40j, 0.25 + 0.001j]:
        mine = digamma_c([z])[0]
        ref = complex(mpmath.digamma(z))
        err = abs(mine - ref)
        print(f"digamma({z}) err = {err:.2e}")
        ok &= err < 1e-12
    # psi(1/4) closed form
    ref = -0.5772156649015329 - math.pi / 2 - 3 * math.log(2)
    print(f"psi(1/4) closed-form err = {abs(digamma_c([0.25])[0].real - ref):.2e}")
    # F_k consistency: numerical FT vs closed form
    L, N = 0.45, 12
    u = np.linspace(-L, L, 20001)
    w = simpson_w(u.size, u[1] - u[0])
    Phi = phi_samples(u, L, N)
    for r in [0.3, 5.7, 12 * math.pi / (2 * L) + 1e-12, 41.23]:
        Fnum = (Phi * w) @ np.exp(1j * r * u)
        Fcf = F_basis(np.array([r]), L, N)[:, 0]
        err = np.max(np.abs(Fnum - Fcf))
        print(f"F_k({r:.4f}) closed-form vs quad err = {err:.2e}")
        ok &= err < 1e-8
    print("TEST", "PASS" if ok else "FAIL")

def cmd_validate(Ls=(0.30, 0.45, 0.80, 1.20), N=40):
    zeros = load_zeros()
    print(f"zeros loaded: {zeros.size}, up to height {zeros[-1]:.1f}")
    for L in Ls:
        G, P, pieces, vp, vm, Q, PoleM = build_all(L, N)
        Warith = PoleM + G + P
        Wspec = spectral_matrix(L, N, zeros)
        num = np.linalg.norm(Warith - Wspec)
        den = np.linalg.norm(Warith)
        # tail bound for the spectral side (crude)
        wmax = N * math.pi / (2 * L)
        T = zeros[-1]
        tail = 4 * wmax**2 / L / (3 * T**3) * math.log(T / (2 * math.pi)) / math.pi
        print(f"L={L:.2f} N={N}  ||arith - spec||_F = {num:.3e}  rel = {num/den:.3e} "
              f" (spec tail bound ~{tail:.1e})  primes active: {sorted(pieces)}")

def cmd_sweep(L_lo=0.20, L_hi=2.00, N=48, out='sweep.csv'):
    zeros = load_zeros()
    thresholds = sorted(math.log(n) / 2 for n in
                        [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29,
                         31, 32, 37, 41, 43, 47, 49, 53] if math.log(n) / 2 < L_hi)
    Ls = sorted(set(
        [round(x, 4) for x in np.arange(L_lo, L_hi + 1e-9, 0.05)] +
        [round(t - 0.01, 4) for t in thresholds if t - 0.01 > L_lo] +
        [round(t + 0.01, 4) for t in thresholds if t + 0.01 < L_hi]))
    rows = []
    for L in Ls:
        G, P, pieces, vp, vm, Q, PoleM = build_all(L, N)
        Warith = PoleM + G + P
        Wspec = spectral_matrix(L, N, zeros)
        val = np.linalg.norm(Warith - Wspec) / np.linalg.norm(Warith)
        ev_arch = eig_min(G, Q)
        ev_tot = eig_min(G + P, Q)
        Pq = Q.T @ P @ Q
        deficit = np.linalg.norm(Pq, 2) if pieces else 0.0
        # minimizer diagnostics: autocorrelation at log 2 of the total-form minimizer
        Mq = Q.T @ (G + P) @ Q
        w_, V = np.linalg.eigh(0.5 * (Mq + Mq.T))
        fmin = Q @ V[:, 0]
        g2 = float(fmin @ overlap_matrix(LOG2, L, N) @ fmin) if 2 * L > LOG2 else 0.0
        rows.append(dict(L=L, margin=ev_arch[0], margin2=ev_arch[1],
                         total=ev_tot[0], total2=ev_tot[1], deficit=deficit,
                         n_primes=len(pieces), g_log2=g2, validation=val))
        print(f"L={L:.4f}  margin={ev_arch[0]:+.6f}  total={ev_tot[0]:+.6f} "
              f" deficit={deficit:.6f}  primes={len(pieces)}  g(log2)={g2:+.4f} "
              f" val={val:.1e}", flush=True)
    with open(os.path.join(HERE, out), 'w', newline='') as fh:
        wcsv = csv.DictWriter(fh, fieldnames=list(rows[0]))
        wcsv.writeheader()
        wcsv.writerows(rows)
    print("wrote", out)

def cmd_profiles(Ls=(0.30, 0.45, 0.70, 1.10, 1.50, 1.90), N=48, out='profiles.npz'):
    data = {}
    for L in Ls:
        G, P, pieces, vp, vm, Q, PoleM = build_all(L, N)
        Mq = Q.T @ (G + P) @ Q
        w_, V = np.linalg.eigh(0.5 * (Mq + Mq.T))
        fmin = Q @ V[:, 0]
        u = np.linspace(-L, L, 1200)
        data[f'u_{L}'] = u
        data[f'f_{L}'] = fmin @ phi_samples(u, L, N)
        r = np.linspace(0, 60, 3000)
        F = F_basis(r, L, N)
        data[f'r_{L}'] = r
        data[f'h_{L}'] = np.abs(fmin @ F) ** 2
        data[f'lam_{L}'] = w_[0]
    np.savez(os.path.join(HERE, out), **data)
    print("wrote", out)

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'test'
    if cmd == 'test':
        cmd_test()
    elif cmd == 'validate':
        cmd_validate()
    elif cmd == 'sweep':
        cmd_sweep()
    elif cmd == 'profiles':
        cmd_profiles()
    else:
        print(__doc__)
