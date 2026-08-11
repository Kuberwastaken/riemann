# sigma_t1.py — Track D stage 4: the sigma-LP aimed DIRECTLY at T1.
#
# Key identity (elementary, previously unused in this lab's proof routes): for
# real f, g_f(log 2) = (1/2pi) int |F|^2 cos(r log 2) dr, so the FULL one-prime
# constrained Weil form is a single diagonal frequency functional
#     W(f) = (1/2pi) int |F(r)|^2 * Omega_W(r) dr,
#     Omega_W(r) = Omega(r) - sqrt(2) log 2 * cos(r log 2).
# The rearrangement route (Lemma R) required a MONOTONE multiplier and so could
# only handle Omega, pushing the prime into a norm bound with bar 0.490129.
# The sigma-LP needs no monotonicity: run the SAME caps with objective Omega_W
# and the bar moves to 0 — with true headroom lambda_min(W) ~ 0.08-0.3 across
# the mid one-prime window (vs 0.015 of headroom for the norm route at L0).
#
# LP >= 0 at window L  ==>  (up to pilot-level numerics) full-space T1 at L is
# certifiable by this cap dictionary. Certification design: LOG 2026-08-11
# (frequency-side Nystrom with analytic remainders for the caps; interval-hull
# LP columns; certified digamma for Omega_W).

import numpy as np, mpmath as mp, sys
mp.mp.dps = 30
from sigma_lp import run_L, BAR, LOG2
from sharp_floor import Omega
from sigma_rich import rich_centers

S2L2 = float(np.sqrt(2.0) * np.log(2.0))

def omega_w(r):
    return Omega(r) - S2L2 * np.cos(r * LOG2)

if __name__ == '__main__':
    Rmax = 22.0
    tail = Omega(Rmax) - S2L2          # inf over r >= Rmax, since Omega increases
    Ls = [float(x) for x in sys.argv[1:]] or [0.40]
    for L in Ls:
        o = run_L(L, n=1200, Rmax=Rmax, dR_caps=0.25, centers=rich_centers(),
                  widths=(1.5, 3.0, 6.0), ktop=60,
                  objective=omega_w, tail_value=tail)
        v_ind, v_sig = o['floor_ind'], o['floor_sigma']
        print(f"L={L:.5f}: FULL-FORM LP floor: indicators {v_ind:+.4f}  "
              f"+sigma {v_sig:+.4f}   [{'T1 CERTIFIED (pilot) at this window' if v_sig > 0 else 'not yet'}]",
              flush=True)
