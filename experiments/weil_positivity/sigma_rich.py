# sigma_rich.py — Track D stage 3: rich-dictionary sigma-LP at full pilot
# resolution, with LP-measure diagnostics to aim further dictionary refinement.
# Smoke result (n=800, dR=0.5, 30 bumps): ind-only 0.4678, +sigma 0.4837 vs bar
# 0.490129; certifiable m2 caps tight to 0.1-1% in the valley. This run: n=1200,
# dR_caps=0.25, ~84 bumps incl. widths 6 and half-step centers through the valley
# and the Omega transition.

import numpy as np, mpmath as mp
from scipy.optimize import linprog
mp.mp.dps = 30
from sigma_lp import run_L, sigma_pair_vals, BAR, LOG2
from sharp_floor import Omega

def rich_centers():
    return np.concatenate([np.arange(0.0, 10.01, 0.5), np.arange(11.0, 16.01, 1.0)])

def run_and_report(L, n=1200, dR_caps=0.25, widths=(1.5, 3.0, 6.0), ktop=60):
    o = run_L(L, n=n, dR_caps=dR_caps, centers=rich_centers(), widths=widths, ktop=ktop)
    print(f"L={L:.5f}  bar={BAR:.6f}")
    print(f"  indicator-only floor : {o['floor_ind']:.4f}")
    print(f"  + sigma dictionary   : {o['floor_sigma']:.4f}   "
          f"[{'CLEARS BAR' if o['floor_sigma'] > BAR else 'below by %.4f' % (BAR - o['floor_sigma'])}]")
    print(f"  m2 tightness: median {np.median(o['m2_ratio']):.3f}, "
          f"max {np.max(o['m2_ratio']):.3f}")
    return o

if __name__ == '__main__':
    import sys
    Ls = [float(x) for x in sys.argv[1:]] or [LOG2 / 2]
    for L in Ls:
        run_and_report(L)
