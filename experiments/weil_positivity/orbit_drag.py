#!/usr/bin/env python3
"""
Lead 5 — the repeated-orbit seam: k>=2 prime-power drag on Weil positivity.

The prime side of the constrained Weil form (engine: weil_form.py, N=48
orthonormal sine basis on [-L, L], pole directions projected out) is a sum over
prime POWERS n = p^k < e^{2L} with weights -2 Lambda(n) n^{-1/2} S(log n).
In the Selberg/orbit picture k=1 terms are primitive orbits and k>=2 terms are
repeated orbits; in Chebyshev language the k>=2 part is psi(x) - theta(x).
Nobody in the literature treats the two classes separately inside Weil
positivity. This experiment does, computing over an L-grid:

  lam_full(L)   = lambda_min of G + sum_{n=p^k < e^{2L}} Q_n   (all orbits)
  lam_primes(L) = lambda_min of G + sum_{n=p   < e^{2L}} Q_n   (k=1 only)
  lam_kle2(L)   = lambda_min with k<=2 terms only (primes + prime squares)
  drag(L)       = lam_primes(L) - lam_full(L)
                  (>0: repeated orbits NEEDED for positivity;
                   <0: repeated orbits HURT positivity)

plus single-orbit ablations (drop only n=4 / only 8 / only 9 from the full sum)
at representative L, zero-crossing localization for lam_primes, and an N=64
convergence check.

Usage (venv python):
  orbit_drag.py sanity   # reproduce rescue_cascade.txt rows -> harness check
  orbit_drag.py sweep    # main experiment -> orbit_drag_output.txt
  orbit_drag.py plot     # orbit_drag.png from orbit_drag_output.txt
"""
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from weil_form import (arch_matrix, prime_matrix, pole_vectors,
                       constrained_basis, eig_min)

N_DEFAULT = 48
L_GRID = [round(0.60 + 0.05 * i, 2) for i in range(29)]      # 0.60 .. 2.00
ABLATION_LS = [0.80, 1.20, 1.60, 2.00]
N64_LS = [0.80, 1.40, 2.00]
OUT_TXT = os.path.join(HERE, 'orbit_drag_output.txt')


def pk(n):
    """n = p^k for prime powers n >= 2 -> (p, k)."""
    for q in range(2, int(math.isqrt(n)) + 1):
        if n % q == 0:
            m, k = n, 0
            while m % q == 0:
                m //= q
                k += 1
            assert m == 1, f"{n} is not a prime power"
            return q, k
    return n, 1


def build(L, N):
    G = arch_matrix(L, N)
    _, pieces = prime_matrix(L, N)
    vp, vm = pole_vectors(L, N)
    Q = constrained_basis(vp, vm)
    return G, pieces, Q


def lam(G, pieces, Q, keep):
    M = G.copy()
    for n in keep:
        M = M + pieces[n]
    return float(eig_min(M, Q)[0])


def split(pieces):
    alln = sorted(pieces)
    primes = [n for n in alln if pk(n)[1] == 1]
    kle2 = [n for n in alln if pk(n)[1] <= 2]
    return alln, primes, kle2


def lam_primes_at(L, N=N_DEFAULT):
    G, pieces, Q = build(L, N)
    _, primes, _ = split(pieces)
    return lam(G, pieces, Q, primes)


# ----------------------------------------------------------------------
def cmd_sanity():
    """Recompute rescue_cascade.txt rows with this harness; must match ~1e-5."""
    ref_path = os.path.join(HERE, 'rescue_cascade.txt')
    refs = {}
    with open(ref_path) as fh:
        for line in fh:
            if not line.startswith('L='):
                continue
            head, rest = line.split(':', 1)
            L = float(head[2:])
            vals = {}
            for tok in rest.split():
                key, v = tok.split(':')
                vals[key] = float(v)
            refs[L] = vals
    ok = True
    for L in (0.60, 0.80, 1.20):
        G, pieces, Q = build(L, N_DEFAULT)
        got = {'arch': lam(G, pieces, Q, [])}
        M = G.copy()
        for n in sorted(pieces):
            M = M + pieces[n]
            got[str(n)] = float(eig_min(M, Q)[0])
        line = f"L={L:.2f}:"
        for key, v in got.items():
            ref = refs[L][key]
            err = abs(v - ref)
            ok &= err < 2e-5
            line += f"  {key}:{v:+.5f}(ref{ref:+.5f},d={err:.1e})"
        print(line, flush=True)
    print("SANITY", "PASS" if ok else "FAIL")
    return 0 if ok else 1


# ----------------------------------------------------------------------
def cmd_sweep(N=N_DEFAULT):
    lines = []

    def emit(s=''):
        print(s, flush=True)
        lines.append(s)

    emit(f"# orbit_drag sweep  N={N}  basis/constraints identical to weil_form.py")
    emit(f"# lam_full: all n=p^k<e^2L | lam_primes: k=1 only | lam_kle2: k<=2 | "
         f"drag = lam_primes - lam_full")
    emit(f"# {'L':>5} {'#pp':>4} {'#pr':>4}  {'lam_arch':>10} {'lam_full':>10} "
         f"{'lam_primes':>11} {'lam_kle2':>10} {'drag':>10}  k>=2 orbits active")
    grid_primes = []
    t0 = time.time()
    for L in L_GRID:
        G, pieces, Q = build(L, N)
        alln, primes, kle2 = split(pieces)
        la = lam(G, pieces, Q, [])
        lf = lam(G, pieces, Q, alln)
        lp = lam(G, pieces, Q, primes)
        l2 = lam(G, pieces, Q, kle2)
        grid_primes.append((L, lp))
        higher = [n for n in alln if pk(n)[1] >= 2]
        emit(f"  {L:5.2f} {len(alln):4d} {len(primes):4d}  {la:+10.6f} {lf:+10.6f} "
             f"{lp:+11.6f} {l2:+10.6f} {lp - lf:+10.6f}  {higher}")
    emit(f"# grid done in {time.time() - t0:.0f}s")

    # ---- zero crossings of lam_primes, localized by bisection -----------
    emit()
    emit("# lam_primes zero crossings (bisection to ~0.004 in L)")
    for (L1, v1), (L2, v2) in zip(grid_primes, grid_primes[1:]):
        if v1 == 0 or v1 * v2 > 0:
            continue
        a, fa, b, fb = L1, v1, L2, v2
        for _ in range(4):
            m = 0.5 * (a + b)
            fm = lam_primes_at(m, N)
            emit(f"#   bisect L={m:.4f}  lam_primes={fm:+.6f}")
            if fa * fm <= 0:
                b, fb = m, fm
            else:
                a, fa = m, fm
        emit(f"  crossing: lam_primes changes sign in L=[{a:.4f}, {b:.4f}] "
             f"({fa:+.6f} -> {fb:+.6f})")

    # ---- single-orbit ablations ----------------------------------------
    emit()
    emit("# single-orbit ablations: lambda_min of the FULL sum minus one orbit")
    emit(f"# {'L':>5}  {'full':>10} {'drop n=4':>10} {'drop n=8':>10} "
         f"{'drop n=9':>10} {'k<=2 only':>10} {'primes':>10}")
    for L in ABLATION_LS:
        G, pieces, Q = build(L, N)
        alln, primes, kle2 = split(pieces)
        lf = lam(G, pieces, Q, alln)
        cols = [f"{lf:+10.6f}"]
        for drop in (4, 8, 9):
            if drop in pieces:
                cols.append(f"{lam(G, pieces, Q, [n for n in alln if n != drop]):+10.6f}")
            else:
                cols.append(f"{'--':>10}")
        cols.append(f"{lam(G, pieces, Q, kle2):+10.6f}")
        cols.append(f"{lam(G, pieces, Q, primes):+10.6f}")
        emit(f"  {L:5.2f}  " + ' '.join(cols))

    # ---- N=64 convergence check ----------------------------------------
    emit()
    emit("# N=64 convergence check (same quantities, larger basis)")
    emit(f"# {'L':>5}  {'lam_full48':>11} {'lam_full64':>11} {'lam_prim48':>11} "
         f"{'lam_prim64':>11}")
    for L in N64_LS:
        vals = {}
        for NN in (N, 64):
            G, pieces, Q = build(L, NN)
            alln, primes, _ = split(pieces)
            vals[NN] = (lam(G, pieces, Q, alln), lam(G, pieces, Q, primes))
        emit(f"  {L:5.2f}  {vals[N][0]:+11.6f} {vals[64][0]:+11.6f} "
             f"{vals[N][1]:+11.6f} {vals[64][1]:+11.6f}")

    with open(OUT_TXT, 'w') as fh:
        fh.write('\n'.join(lines) + '\n')
    print(f"wrote {OUT_TXT}")


# ----------------------------------------------------------------------
def cmd_plot():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    Ls, lf, lp, dr = [], [], [], []
    with open(OUT_TXT) as fh:
        for line in fh:
            t = line.split()
            if line.startswith('#') or len(t) < 8:
                continue
            try:
                Ls.append(float(t[0]))
            except ValueError:
                continue
            lf.append(float(t[4]))
            lp.append(float(t[5]))
            dr.append(float(t[7]))
            if len(Ls) >= len(L_GRID):
                break

    ink, grid_c = '#1a1a24', '#d9d9e0'
    c_full, c_primes, c_drag = '#5b6ee1', '#c15b3f', '#3d8a63'
    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(7.2, 6.4), sharex=True,
        gridspec_kw={'height_ratios': [3, 2], 'hspace': 0.12})
    for ax in (ax1, ax2):
        ax.axhline(0, color=ink, lw=0.8, zorder=1)
        ax.grid(axis='y', color=grid_c, lw=0.6, zorder=0)
        for s in ('top', 'right'):
            ax.spines[s].set_visible(False)
        ax.tick_params(colors=ink, labelsize=9)
    ax1.plot(Ls, lf, color=c_full, lw=1.8, marker='o', ms=3.5, zorder=3,
             label=r'$\lambda_{\min}^{\rm full}$ (all $p^k$)')
    ax1.plot(Ls, lp, color=c_primes, lw=1.8, marker='s', ms=3.5, zorder=3,
             label=r'$\lambda_{\min}^{\rm primes}$ ($k=1$ only)')
    ax1.set_ylabel(r'$\lambda_{\min}$ (constrained, $N=48$)', fontsize=10,
                   color=ink)
    ax1.legend(frameon=False, fontsize=9, loc='lower left')
    ax1.set_title('Repeated-orbit drag: primes-only vs full prime-power '
                  'Weil form', fontsize=11, color=ink)
    ax2.plot(Ls, dr, color=c_drag, lw=1.8, marker='o', ms=3.5, zorder=3)
    ax2.set_ylabel(r'drag $\Delta=\lambda^{\rm primes}-\lambda^{\rm full}$',
                   fontsize=10, color=ink)
    ax2.set_xlabel(r'window half-length $L$', fontsize=10, color=ink)
    fig.savefig(os.path.join(HERE, 'orbit_drag.png'), dpi=160,
                bbox_inches='tight')
    print("wrote orbit_drag.png")


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'sweep'
    if cmd == 'sanity':
        sys.exit(cmd_sanity())
    elif cmd == 'sweep':
        cmd_sweep()
    elif cmd == 'plot':
        cmd_plot()
    else:
        print(__doc__)
