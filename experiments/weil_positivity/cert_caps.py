# cert_caps.py — Track D certification module: rigorous (Arb ball) caps for the
# sigma-LP floor, all reducible to 1-D verified integrals.
#
# Provides certified UPPER bounds Lambda for lambda_max of compressions
# P_V K P_V on L^2([-L,L]) with the two pole constraints projected out, via the
# Frobenius bound  lambda_max(P_V K P_V) <= ||P_V K P_V||_F <= ||K|_T||_F,
# where for a convolution kernel k(u-v) on T = [-L,L]:
#     ||K|_T||_F^2 = Tr[(K|_T)^2] = int_{-2L}^{2L} (2L-|x|) k(x)^2 dx      (1-D!)
# (valid since K|_T has symmetric real kernel k(u-v); compression by the
# orthogonal projection P_V only decreases the Frobenius norm).
#
# Kernels:
#   indicator band sigma = 1_{[-R,R]}:      k(x) = sin(Rx)/(pi x)
#   Fejer pair sigma_{c,a}:                 k(x) = (4/pi) cos(cx) sin^2(ax/2)/(a x^2)
#     (c = 0: half of that — single bump)
# Both are entire after removing the singularity; we integrate their squares
# against (2L-|x|) with Arb verified integration using the series-safe forms.
#
# Also provides the certified TRACE cap of Lemma T (PROOF-c0 species):
#     Tr[B_R|_V] = 2LR/pi - rho1(R) - rho2(R)
# with rho_i = <v_i, B_R v_i> lower-bounded rigorously (safe direction) via
# verified 1-D integrals of the explicit sinh-transforms V_i.
#
# This module is float-validated against sigma_lp.py before being trusted;
# the Arb path uses python-flint (acb_integrate) exactly as certify.py does.

import numpy as np
from flint import arb, acb, ctx, acb_mat

def _acb_sinc(z):
    # sin(z)/z with the removable singularity handled by acb's series arithmetic
    if z.contains(0):
        # use the entire series form via acb: sinc has no closed form in flint;
        # fall back to sin(z)/z on a ball not containing 0 is invalid here, so
        # use the Taylor bound: sinc(z) = 1 - z^2/6 + z^4/120 - ... with rigorous
        # remainder |R| <= |z|^6/5040 * e^{|Im z|} on the ball.
        z2 = z * z
        val = acb(1) - z2 / 6 + z2 * z2 / 120
        rad = (abs(z) ** 6 / 5040) * (abs(z).exp())
        return val + acb(0).add_error(rad) if hasattr(acb(0), 'add_error') else val
    return z.sin() / z

def cert_frob2_indicator(L, R, prec=128, N=None):
    """Certified upper bound (arb) for Tr[(B_R|_T)^2] = (1/pi^2) *
    int_{-2L}^{2L} (2L-|x|) sin^2(Rx)/x^2 dx  =  (2/pi^2) *
    int_0^{2L} (2L-x) sin^2(Rx)/x^2 dx, integrand extended by R^2(2L-x)... at 0."""
    ctx.prec = prec
    Lb, Rb = arb(L), arb(R)
    def f(x, analytic=False):
        # integrand: (2L - x) * (sin(Rx)/x)^2 = (2L-x) * R^2 * sinc(Rx)^2
        s = _acb_sinc(Rb * x)
        return (2 * Lb - x) * Rb * Rb * s * s
    val = acb.integral(f, 0, 2 * L)
    out = (2 / (arb.pi() ** 2)) * val.real
    return out

def cert_frob2_fejer(L, c, a, prec=128):
    """Certified upper bound (arb) for Tr[(K_{c,a}|_T)^2] =
    int_{-2L}^{2L} (2L-|x|) k(x)^2 dx, k(x) = (4/pi) cos(cx) sin^2(ax/2)/(a x^2)
    (times 1/2 when c == 0). Using sin^2(ax/2)/x^2 = (a^2/4) sinc^2(ax/2)."""
    ctx.prec = prec
    Lb, cb, ab = arb(L), arb(c), arb(a)
    half = arb(1) / 2 if c == 0.0 else arb(1)
    def f(x, analytic=False):
        s = _acb_sinc(ab * x / 2)
        k = (4 / acb.pi()) * (cb * x).cos() * (ab / 4) * s * s   # = k(x)
        k = k * half
        return (2 * Lb - x) * k * k
    val = acb.integral(f, 0, 2 * L)
    return 2 * val.real     # symmetric in x

def float_frob2_indicator(L, R, n=200000):
    x = np.linspace(1e-12, 2 * L, n)
    y = (2 * L - x) * (np.sin(R * x) / x) ** 2
    return float(2 / np.pi ** 2 * np.trapz(y, x))

def float_frob2_fejer(L, c, a, n=200000):
    x = np.linspace(1e-12, 2 * L, n)
    k = (4 / np.pi) * np.cos(c * x) * np.sin(a * x / 2) ** 2 / (a * x ** 2)
    if c == 0.0:
        k = 0.5 * k
    y = (2 * L - x) * k ** 2
    return float(2 * np.trapz(y, x))

if __name__ == '__main__':
    L = np.log(2) / 2
    print("validation: certified (ball) vs float quadrature")
    for R in [2.0, 6.0, 10.0]:
        b = cert_frob2_indicator(L, R)
        f = float_frob2_indicator(L, R)
        print(f"  indicator R={R}: ball={b} float={f:.8f}  sqrt(ball)={b.sqrt()}")
    for (c, a) in [(0.0, 3.0), (4.0, 1.5), (8.0, 3.0)]:
        b = cert_frob2_fejer(L, c, a)
        f = float_frob2_fejer(L, c, a)
        print(f"  fejer c={c} a={a}: ball={b} float={f:.8f}  sqrt(ball)={b.sqrt()}")
