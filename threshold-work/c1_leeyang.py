#!/usr/bin/env python
"""C1 (cycle 2, CHALLENGER): Lee-Yang / monotone-zero-motion test on Suzuki's
W(a,theta;z) family (arXiv:2606.09096 Thm 1.5).

Construction
------------
Sine Galerkin basis phi_k(x) = sin(w_k(x+a))/sqrt(a), w_k = k*pi/(2a), k=1..N,
orthonormal in L^2(-a,a).  The localized Weil form (S1-sector.md (F2),
= Suzuki (2.7) multiplier frame, verified there to 1e-10):

  Q_a^W(v) = (1/2pi) int Omega(xi)|vhat(xi)|^2 dxi
             + 2<v,w+>^2 - 2<v,w->^2
             - sum_{n<=e^{2a}} (2 Lambda(n)/sqrt(n)) g_v(log n),

  Omega(xi) = Re psi(1/4 + i xi/2) - log pi,  w+- = cosh(x/2), sinh(x/2),
  g_v(t) = int v(x) v(x-t) dx  (zero-extension).

K = Galerkin matrix of Q_a^W;  A_a ~ K;  T_a = A_a - lam (lam < lambda_a).
Deficiency vectors of D_a = i d/dx on H(T_a):  (T_a v+-)(x) = e^{+-x}
(Suzuki Lemma 6.2), so  c_pm = K-solve of b_pm, b_pm[k] = <phi_k, e^{+-x}>.
Characteristic function (Suzuki (1.11)):

  W(a,theta;z) = (z-i) vhat+(z) + e^{i theta} (z+i) vhat-(z),
  vhat-(z) = vhat+(-z)   (parity J A_a J = A_a, u- = J u+).

All zeros real (Thm 1.5, unconditional).  On real z,
  W = 2 e^{i theta/2} Re[ e^{-i theta/2} (z-i) vhat+(z) ],
so zeros = roots of the REAL function  w_th(z) := Re[e^{-i th/2}(z-i)vhat+(z)].

Experiments (see C1-leeyang.md):
  E0  validation vs S1 certified anchors + reality (argument principle)
      + lambda-independence probe.
  E1  zero motion z_k(a) across a-grid through 1/2 log2, 1/2 log3.
  E2  zero motion under Lambda(2) -> Lambda(2)+eps  (and Lambda(3)).
  E3  A_a lowest eigenvalues under the same coupling move (GKS control).

Run:  .venv/bin/python threshold-work/c1_leeyang.py [smoke|e0|e1|e2|all]
"""

import sys
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import digamma
from scipy.optimize import brentq

LOG_PI = np.log(np.pi)


# ----------------------------------------------------------------------
# basis and closed-form vectors
# ----------------------------------------------------------------------

def freqs(a, N):
    return np.arange(1, N + 1) * np.pi / (2.0 * a)


def Omega(xi):
    """Archimedean multiplier Re psi(1/4 + i xi/2) - log pi (vectorized)."""
    return np.real(digamma(0.25 + 0.5j * np.asarray(xi, dtype=float))) - LOG_PI


def exp_overlap(a, N, c):
    """<phi_k, e^{c x}> = (1/sqrt a) * w_k (e^{-ca} - (-1)^k e^{ca})/(c^2+w_k^2)."""
    w = freqs(a, N)
    k = np.arange(1, N + 1)
    sgn = (-1.0) ** k
    return (w * (np.exp(-c * a) - sgn * np.exp(c * a)) / (c * c + w * w)) / np.sqrt(a)


def pole_vectors(a, N):
    """p+ = <phi_k, cosh(x/2)>, p- = <phi_k, sinh(x/2)> (closed form)."""
    pp = 0.5 * (exp_overlap(a, N, 0.5) + exp_overlap(a, N, -0.5))
    pm = 0.5 * (exp_overlap(a, N, 0.5) - exp_overlap(a, N, -0.5))
    return pp, pm


# ----------------------------------------------------------------------
# archimedean (jump + killing + scalar) matrix via multiplier quadrature
# ----------------------------------------------------------------------

def _s_matrix(a, N, xi):
    """s_k(xi) = sin(a xi + k pi/2)/(w_k^2 - xi^2), stable form:
    s_k(xi) = (-1)^{k+1} a sinc(a(xi-w_k)/pi)/(xi+w_k).  xi >= 0 array."""
    w = freqs(a, N)[:, None]
    k = np.arange(1, N + 1)[:, None]
    x = xi[None, :]
    return ((-1.0) ** (k + 1)) * a * np.sinc(a * (x - w) / np.pi) / (x + w)


def arch_matrix(a, N, n_near=48, gl_near=12, gl_osc=12, xi_mult=2.5,
                tail_hi=1.0e6, tail_panels=40, tail_gl=10):
    """A[j,k] = (1/2pi) int_R Omega phi_j-hat conj(phi_k-hat) dxi.
    phi_j-hat conj(phi_k-hat) = (4/a) i^{j-k} w_j w_k s_j s_k;  real part only
    for j=k mod 2 with factor (-1)^{(j-k)/2}; zero across parity.
    Dense GL panels on [0, Xi1] + averaged analytic tail on [Xi1, inf)."""
    w = freqs(a, N)
    Xi1 = xi_mult * w[-1] + 8.0 / a

    # panels: fine near 0 (Omega analyticity radius ~ 1/2), quarter-period after
    edges = list(np.linspace(0.0, 4.0, n_near + 1))
    step = np.pi / (2.0 * a)
    x = edges[-1]
    while x < Xi1:
        x = min(x + step, Xi1)
        edges.append(x)
    nodes_l, wts_l = [], []
    xg, wg = leggauss(gl_near)
    for i in range(len(edges) - 1):
        lo, hi = edges[i], edges[i + 1]
        if i >= n_near and gl_osc != gl_near:
            xg, wg = leggauss(gl_osc)
        mid, hl = 0.5 * (lo + hi), 0.5 * (hi - lo)
        nodes_l.append(mid + hl * xg)
        wts_l.append(hl * wg)
    xi = np.concatenate(nodes_l)
    wts = np.concatenate(wts_l)

    S = _s_matrix(a, N, xi)                       # (N, Nxi)
    om = Omega(xi) * wts
    M = (S * om[None, :]) @ S.T                   # int Omega s_j s_k dxi on [0,Xi1]

    # averaged tail: s_j s_k ~ (1/2)(-1)^{(j-k)/2}/((xi^2-w_j^2)(xi^2-w_k^2));
    # with the i^{j-k} prefactor the sign squares away:
    # A_tail[j,k] = (w_j w_k/(pi a)) int_{Xi1}^{inf} Omega/((xi^2-w_j^2)(xi^2-w_k^2))
    t_edges = np.geomspace(Xi1, tail_hi, tail_panels + 1)
    xg, wg = leggauss(tail_gl)
    tn, tw = [], []
    for i in range(tail_panels):
        lo, hi = t_edges[i], t_edges[i + 1]
        mid, hl = 0.5 * (lo + hi), 0.5 * (hi - lo)
        tn.append(mid + hl * xg)
        tw.append(hl * wg)
    txi = np.concatenate(tn)
    tom = Omega(txi) * np.concatenate(tw)
    U = 1.0 / (txi[None, :] ** 2 - w[:, None] ** 2)   # (N, Ntail)
    Mtail = 0.5 * (U * tom[None, :]) @ U.T

    jj = np.arange(1, N + 1)
    par = (jj[:, None] - jj[None, :])
    same = (par % 2 == 0)
    sgn = np.where(same, (-1.0) ** (par // 2), 0.0)

    pref = (4.0 * np.outer(w, w) / a) / (2.0 * np.pi) * 2.0   # x2: even integrand
    A = pref * (sgn * M + same * Mtail)                        # tail sign is +1
    return 0.5 * (A + A.T)


# ----------------------------------------------------------------------
# prime hop overlap matrix (closed form)
# ----------------------------------------------------------------------

def hop_matrix(a, N, t):
    """G_t[j,k] = (1/2) int [phi_j(x) phi_k(x-t) + phi_k(x) phi_j(x-t)] dx,
    0 <= t < 2a.  int phi_j(x) phi_k(x-t) dx = (1/a) I(j,k),
    I = int_0^{L-t} sin(w_j(u+t)) sin(w_k u) du, L = 2a."""
    L = 2.0 * a
    M = L - t
    if M <= 0:
        return np.zeros((N, N))
    w = freqs(a, N)
    wj = w[:, None]
    wk = w[None, :]
    beta = wj * t

    dm = wj - wk
    dp = wj + wk
    # int_0^M sin(wj u + beta) sin(wk u) du
    #  = 1/2 [ (sin(dm M + beta) - sin beta)/dm - (sin(dp M + beta) - sin beta)/dp ]
    with np.errstate(divide="ignore", invalid="ignore"):
        term1 = (np.sin(dm * M + beta) - np.sin(beta)) / dm
    diag = np.isclose(dm, 0.0)
    term1 = np.where(diag, M * np.cos(beta), term1)
    term2 = (np.sin(dp * M + beta) - np.sin(beta)) / dp
    I = 0.5 * (term1 - term2)
    C = I / a                      # int phi_j(x) phi_k(x-t) dx
    return 0.5 * (C + C.T)


def vonmangoldt_upto(x):
    """[(n, Lambda(n))] for n <= x, n prime power."""
    out = []
    n = 2
    while n <= x:
        m, p = n, None
        for q in range(2, int(np.sqrt(n)) + 1):
            if m % q == 0:
                p = q
                break
        if p is None:
            out.append((n, np.log(n)))
        else:
            while m % p == 0:
                m //= p
            if m == 1:
                out.append((n, np.log(p)))
        n += 1
    return out


# ----------------------------------------------------------------------
# full form matrix
# ----------------------------------------------------------------------

_ARCH_CACHE = {}


def K_matrix(a, N, dLam=None, arch_kw=None):
    """Galerkin matrix of Q_a^W.  dLam: {n: eps} coupling perturbations
    Lambda(n) -> Lambda(n)+eps (applied whether or not log n < 2a fits;
    hop matrix is zero if it does not fit)."""
    key = (round(a, 12), N, tuple(sorted((arch_kw or {}).items())))
    if key not in _ARCH_CACHE:
        _ARCH_CACHE[key] = arch_matrix(a, N, **(arch_kw or {}))
    K = _ARCH_CACHE[key].copy()

    pp, pm = pole_vectors(a, N)
    K += 2.0 * np.outer(pp, pp) - 2.0 * np.outer(pm, pm)

    coup = {}
    for n, lam in vonmangoldt_upto(np.exp(2.0 * a) + 1e-12):
        if np.log(n) < 2.0 * a:
            coup[n] = lam
    if dLam:
        for n, eps in dLam.items():
            coup[n] = coup.get(n, 0.0) + eps
    for n, lam in coup.items():
        t = np.log(n)
        if t < 2.0 * a and abs(lam) > 0:
            K -= (2.0 * lam / np.sqrt(n)) * hop_matrix(a, N, t)
    return 0.5 * (K + K.T)


# ----------------------------------------------------------------------
# W(a,theta;z) and its real zeros
# ----------------------------------------------------------------------

def phik_hat(a, N, z):
    """phi_k-hat(z) = (-2i/sqrt a) i^k w_k s_k(z), entire; z real/complex array.
    Stable near +w_k via sinc; near -w_k use parity s_k(-z)=(-1)^{k+1}s_k(z)."""
    z = np.atleast_1d(np.asarray(z, dtype=complex))
    w = freqs(a, N)[:, None]
    k = np.arange(1, N + 1)[:, None]
    zz = z[None, :]
    use_ref = np.real(zz) < 0.0
    zs = np.where(use_ref, -zz, zz)          # Re zs >= 0: near +w_k only
    sk = ((-1.0) ** (k + 1)) * a * _csinc(a * (zs - w)) / (zs + w)
    sk = np.where(use_ref, ((-1.0) ** (k + 1)) * sk, sk)
    return (-2.0j / np.sqrt(a)) * (1.0j ** k) * w * sk   # (N, Nz)


def _csinc(x):
    """sin(x)/x for complex x, stable at 0."""
    x = np.asarray(x, dtype=complex)
    small = np.abs(x) < 1.0e-8
    xs = np.where(small, 1.0, x)
    return np.where(small, 1.0 - x * x / 6.0, np.sin(xs) / xs)


class WFamily:
    """v+ = T^{-1} e^x in the Galerkin section; evaluates W(a,theta;z)."""

    def __init__(self, a, N, lam=0.0, dLam=None, arch_kw=None):
        self.a, self.N, self.lam = a, N, lam
        K = K_matrix(a, N, dLam=dLam, arch_kw=arch_kw)
        evals, evecs = np.linalg.eigh(K)
        self.evals, self.evecs = evals, evecs
        if evals[0] - lam <= 0:
            raise ValueError(f"lam={lam} not below lambda_min={evals[0]:.3e}")
        bp = exp_overlap(a, N, +1.0)
        self.c_plus = evecs @ ((evecs.T @ bp) / (evals - lam))

    def vhat_plus(self, z):
        return self.c_plus @ phik_hat(self.a, self.N, z)

    def W(self, theta, z):
        z = np.atleast_1d(np.asarray(z, dtype=complex))
        return ((z - 1j) * self.vhat_plus(z)
                + np.exp(1j * theta) * (z + 1j) * self.vhat_plus(-z))

    def w_real(self, theta, z):
        """real root function on real z: Re[e^{-i th/2}(z-i) vhat+(z)]."""
        z = np.atleast_1d(np.asarray(z, dtype=float))
        A = (z - 1j) * self.vhat_plus(z.astype(complex))
        return np.real(np.exp(-0.5j * theta) * A)

    def real_zeros(self, theta, zmax=30.0, dz=0.01, zmin=1.0e-6):
        grid = np.arange(zmin, zmax, dz)
        vals = self.w_real(theta, grid)
        roots = []
        s = np.sign(vals)
        idx = np.nonzero(s[:-1] * s[1:] < 0)[0]
        f = lambda x: float(self.w_real(theta, np.array([x]))[0])
        for i in idx:
            roots.append(brentq(f, grid[i], grid[i + 1], xtol=1.0e-12))
        return np.array(roots)

    def winding_count(self, theta, zmax, imh=3.0, npts=4000):
        """# zeros inside rectangle [-zmax,zmax]x[-imh,imh] via argument
        principle on W(theta; .)."""
        c = []
        c.append(np.linspace(-zmax - 1j * imh, zmax - 1j * imh, npts))
        c.append(np.linspace(zmax - 1j * imh, zmax + 1j * imh, npts // 4))
        c.append(np.linspace(zmax + 1j * imh, -zmax + 1j * imh, npts))
        c.append(np.linspace(-zmax + 1j * imh, -zmax - 1j * imh, npts // 4))
        zs = np.concatenate(c)
        Wv = self.W(theta, zs)
        ph = np.unwrap(np.angle(Wv))
        return (ph[-1] - ph[0] + np.angle(Wv[0] / Wv[-1])) / (2 * np.pi), \
            np.round((ph[-1] - ph[0]) / (2 * np.pi))


# ----------------------------------------------------------------------
# experiments
# ----------------------------------------------------------------------

def smoke(N=200):
    """Validation vs S1 table anchors (float Galerkin there: N=24/sector)."""
    print("== SMOKE: S1 anchors ==")
    for a, ee, eo in [(0.30, 8.6e-3, 2.4e-1), (0.45, 1.9568e-5, 2.9e-3),
                      (0.545, 8.8e-8, 2.3e-5)]:
        K = K_matrix(a, N)
        ev = np.linalg.eigvalsh(K)[:4]
        print(f" a={a}: lam0={ev[0]:.4e} (S1 eps_even {ee:.3e}), "
              f"lam1={ev[1]:.4e} (S1 eps_odd {eo:.3e})")
    # gamma_arch at a=0.10: pole-free & prime-free parity gap
    a = 0.10
    A = arch_matrix(a, N)
    ev_e = np.linalg.eigvalsh(A[0::2, 0::2])[:1]   # k odd = even functions
    ev_o = np.linalg.eigvalsh(A[1::2, 1::2])[:1]
    print(f" a=0.10 gamma_arch = {ev_o[0]-ev_e[0]:.4f}  (S1: 1.255)")
    # hop matrix sanity vs quadrature
    a, t = 0.45, np.log(2.0)
    G = hop_matrix(a, 8, t)
    xs, ws2 = leggauss(4000)
    lo, hi = -a + t, a
    x = 0.5 * (lo + hi) + 0.5 * (hi - lo) * xs
    wq = 0.5 * (hi - lo) * ws2
    w = freqs(a, 8)
    P1 = np.sin(np.outer(w, x + a)) / np.sqrt(a)
    P2 = np.sin(np.outer(w, x - t + a)) / np.sqrt(a)
    Cq = P1 @ (P2 * wq).T
    Gq = 0.5 * (Cq + Cq.T)
    print(f" hop closed-form vs quad, max err = {np.abs(G-Gq).max():.2e}")


def e0(N=200):
    print("== E0: reality + lambda-independence ==")
    for a in (0.30, 0.45, 0.56):
        F = WFamily(a, N, lam=0.0)
        for th in (0.0, np.pi):
            zr = F.real_zeros(th, zmax=30.0)
            nreal = 2 * len(zr) + (1 if th == 0.0 else 0)  # z=0 zero at th=0
            wind, _ = F.winding_count(th, 30.0)
            print(f" a={a} th={th:.2f}: real zeros in (0,30): {len(zr)}, "
                  f"total count vs winding {nreal} ~ {wind:.2f}")
        # lambda-independence probe
        z0 = WFamily(a, N, lam=0.0).real_zeros(np.pi, 30.0)
        z1 = WFamily(a, N, lam=-0.05).real_zeros(np.pi, 30.0)
        z2 = WFamily(a, N, lam=-0.5).real_zeros(np.pi, 30.0)
        m = min(len(z0), len(z1), len(z2))
        d01 = np.abs(z0[:m] - z1[:m]).max()
        d02 = np.abs(z0[:m] - z2[:m]).max()
        print(f" a={a}: max zero shift lam 0->-0.05: {d01:.3e}, "
              f"0->-0.5: {d02:.3e}")


def match_zeros(prev, cur):
    """continuity matching: for each prev zero, nearest current zero."""
    out = np.full(len(prev), np.nan)
    used = set()
    for i, z in enumerate(prev):
        j = int(np.argmin(np.abs(cur - z)))
        if j not in used:
            out[i] = cur[j]
            used.add(j)
    return out


def e1(N=200, theta=np.pi, lam=0.0, zmax=60.0, fname=None):
    print(f"== E1: zero motion in a (theta={theta:.3f}, lam={lam}) ==")
    grid = []
    x = 0.20
    while x < 0.6201:
        grid.append(round(x, 4))
        if 0.335 <= x < 0.360 or 0.540 <= x < 0.560:
            x += 0.0025
        else:
            x += 0.01
    rows = []
    prev = None
    for a in grid:
        try:
            F = WFamily(a, N, lam=lam)
        except ValueError as ex:
            print(f" a={a}: SKIP ({ex})")
            continue
        zr = F.real_zeros(theta, zmax=zmax)
        lam0 = F.evals[0]
        rows.append((a, lam0, zr))
        if prev is not None:
            zprev = rows[-2][2]
            m = match_zeros(zprev, zr)
            dz = m - zprev
            good = ~np.isnan(dz)
            sgns = np.sign(dz[good])
            n_up = int((sgns > 0).sum())
            n_dn = int((sgns < 0).sum())
            flag = "" if n_up == 0 or n_dn == 0 else "  <-- MIXED"
            z14 = " ".join(f"{z:8.4f}" for z in zr[:4])
            print(f" a={a:6.4f} lam0={lam0:9.3e} nz={len(zr):2d} "
                  f"dz: up={n_up} dn={n_dn} max|dz|={np.nanmax(np.abs(dz)):.4f}"
                  f"  z1-4: {z14}{flag}")
        prev = zr
    if fname:
        np.save(fname, np.array(rows, dtype=object), allow_pickle=True)
    return rows


def e2(N=200, theta=np.pi, zmax=30.0):
    print("== E2: coupling motion Lambda(n) -> Lambda(n)+eps ==")
    eps_list = [-0.05, -0.025, 0.0, 0.025, 0.05]
    for (a, n) in [(0.40, 2), (0.45, 2), (0.50, 2), (0.56, 2), (0.60, 2),
                   (0.56, 3), (0.60, 3)]:
        # pick lam uniformly below all perturbed lambda_min
        lam_min = np.inf
        Ks = {}
        for eps in eps_list:
            K = K_matrix(a, N, dLam={n: eps})
            Ks[eps] = K
            lam_min = min(lam_min, np.linalg.eigvalsh(K)[0])
        lam = min(0.0, lam_min - 0.05)
        if lam_min <= lam:
            lam = lam_min - 0.05
        base = None
        print(f"--- a={a}, prime n={n}, lam={lam:.3f}, "
              f"min lambda_0 over eps = {lam_min:.3e}")
        table = {}
        for eps in eps_list:
            F = WFamily.__new__(WFamily)
            F.a, F.N, F.lam = a, N, lam
            evals, evecs = np.linalg.eigh(Ks[eps])
            F.evals, F.evecs = evals, evecs
            bp = exp_overlap(a, N, +1.0)
            F.c_plus = evecs @ ((evecs.T @ bp) / (evals - lam))
            zr = F.real_zeros(theta, zmax=zmax)
            table[eps] = zr
            if eps == 0.0:
                base = zr
        m = base
        print("  k    z_k(0)      dz/deps(-)   dz/deps(+)   "
              "-cos(z log n)  lam0(eps=0)")
        lam0 = np.linalg.eigvalsh(Ks[0.0])[0]
        for k in range(min(len(m), 9)):
            zk = m[k]
            zm = match_zeros(np.array([zk]), table[-0.025])[0]
            zp = match_zeros(np.array([zk]), table[+0.025])[0]
            dm = (zk - zm) / 0.025
            dp = (zp - zk) / 0.025
            pred = -np.cos(zk * np.log(n))
            print(f"  {k}  {zk:9.5f}  {dm:+.5e}  {dp:+.5e}   {pred:+.4f}"
                  + (f"      {lam0:.3e}" if k == 0 else ""))
        # sign-agreement census over all matched zeros, eps = +-0.05
        zp5 = match_zeros(m, table[0.05])
        dz5 = zp5 - m
        good = ~np.isnan(dz5)
        pred = -np.cos(m[good] * np.log(n))
        agree = np.sign(dz5[good]) == np.sign(pred)
        n_up = int((dz5[good] > 0).sum())
        n_dn = int((dz5[good] < 0).sum())
        print(f"  eps=+0.05: up={n_up} dn={n_dn} "
              f"(one-signed? {'YES' if n_up==0 or n_dn==0 else 'NO'}); "
              f"sign agrees with -cos(z log n): {agree.sum()}/{good.sum()}")


def e3(N=200):
    print("== E3: A_a eigenvalue response to Lambda(2)+eps (GKS control) ==")
    for a in (0.40, 0.50, 0.60):
        K0 = K_matrix(a, N)
        Kp = K_matrix(a, N, dLam={2: 0.05})
        e0v = np.linalg.eigvalsh(K0)[:10]
        epv = np.linalg.eigvalsh(Kp)[:10]
        d = (epv - e0v) / 0.05
        sgn = ["-" if x < 0 else "+" for x in d]
        print(f" a={a}: dlam_j/deps signs (j=0..9): {''.join(sgn)}   "
              f"dlam0/deps={d[0]:+.4e}")
        # exact first-order check for ground state: -sqrt(2)/... :
        w0 = np.linalg.eigh(K0)[1][:, 0]
        G2 = hop_matrix(a, N, np.log(2.0))
        pred = -(2.0 / np.sqrt(2.0)) * (w0 @ G2 @ w0)
        print(f"   first-order prediction dlam0/deps = {pred:+.4e} "
              f"(autocorr g_v0(log2) = {(w0 @ G2 @ w0):+.4e})")


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    if what in ("smoke", "all"):
        smoke()
    if what in ("e0", "all"):
        e0()
    if what in ("e1", "all"):
        e1()
    if what in ("e2", "all"):
        e2()
    if what in ("e3", "all"):
        e3()
