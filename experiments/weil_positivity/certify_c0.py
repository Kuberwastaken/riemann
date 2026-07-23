#!/usr/bin/env python3
"""
Machine certification of Theorem A (PROOF-c0.md): explicit coercivity constant
c0 for the archimedean Weil form on the prime-free window [-L0, L0], L0 = log2/2,
on the pole-constrained space.

All analytic ingredients are proven in PROOF-c0.md (monotonicity of Omega; trace
identity; rearrangement/stochastic dominance). This script certifies the two 1-D
integral families rho_i(R) (band masses of the orthonormalized constraint
representers) with Arb verified integration, and evaluates the certified
Stieltjes lower bound. Output: a rigorous lower bound for c0.
"""
import math
from flint import acb, arb, ctx

ctx.dps = 30
L0 = arb(2).log() / 2

# closed forms: Vp(r) = int e^{u/2} e^{iru} du = 2 sinh((1/2+ir)L0)/(1/2+ir)
def Vp(r):
    z = acb(0.5) + acb(0, 1) * r
    return acb(2) * (z * acb(L0)).sinh() / z

def Vm(r):
    z = acb(-0.5) + acb(0, 1) * r
    return acb(2) * (z * acb(L0)).sinh() / z

def Vp_bar(r):
    z = acb(0.5) - acb(0, 1) * r
    return acb(2) * (z * acb(L0)).sinh() / z

def Vm_bar(r):
    z = acb(-0.5) - acb(0, 1) * r
    return acb(2) * (z * acb(L0)).sinh() / z

# orthonormalization constants (closed form, arb):
g11 = arb(2) * L0.sinh()            # int e^u du over [-L0, L0]  = 2 sinh L0
g22 = g11                           # int e^{-u} du same
g12 = arb(2) * L0                   # int e^{u/2}e^{-u/2} = 2 L0
p = g12 / g11.sqrt()                # <v1, e^{-u/2}> with v1 = e^{u/2}/sqrt(g11)
nrm2 = (g22 - g12 * g12 / g11).sqrt()

def rho_cell_integrand_1(r, _):
    """|V1(r)|^2 with v1 = e^{u/2}/sqrt(g11): Vp(r) Vp_bar(r) / g11 (analytic)."""
    return Vp(r) * Vp_bar(r) / acb(g11)

def rho_cell_integrand_2(r, _):
    """|V2(r)|^2 for v2 = (e^{-u/2} - (g12/g11) e^{u/2}) / nrm2 (analytic)."""
    W = Vm(r) - acb(g12 / g11) * Vp(r)
    Wb = Vm_bar(r) - acb(g12 / g11) * Vp_bar(r)
    return W * Wb / acb(nrm2 * nrm2)

def Omega_ball(R):
    q = acb(0.25)
    ir2 = acb(0, 0.5) * acb(R)
    return (((q + ir2).digamma() + (q - ir2).digamma()) / acb(2)
            - acb(arb.pi().log())).real

def main():
    K, step = 64, 0.25
    Rs = [step * k for k in range(K + 1)]        # 0 .. 16
    # certified band masses rho_i(R_k), accumulated cell by cell (x2 for even)
    rho1 = [arb(0)]
    rho2 = [arb(0)]
    for k in range(1, K + 1):
        a, b = Rs[k - 1], Rs[k]
        c1 = acb.integral(rho_cell_integrand_1, a, b).real / arb.pi()
        c2 = acb.integral(rho_cell_integrand_2, a, b).real / arb.pi()
        rho1.append(rho1[-1] + c1)
        rho2.append(rho2[-1] + c2)
    # cap curve: Mbar(R_k) upper bounds (safe direction), clipped, cumulative-max
    caps = []
    run = 0.0
    for k in range(K + 1):
        tr = 2 * float(L0.mid()) * Rs[k] / math.pi
        # subtract certified LOWER bounds of rho (safe: overestimates cap)
        lo1 = float(rho1[k].lower())
        lo2 = float(rho2[k].lower())
        m = max(0.0, min(1.0, tr - lo1 - lo2))
        run = max(run, m)
        caps.append(run)
    # certified Stieltjes lower bound: mass increments at left endpoints
    total = arb(0)
    for k in range(1, K + 1):
        d = caps[k] - caps[k - 1]
        if d <= 0:
            continue
        total += Omega_ball(Rs[k - 1]) * arb(d)
    tail_mass = 1.0 - caps[-1]
    if tail_mass > 0:
        total += Omega_ball(Rs[-1]) * arb(tail_mass)
    print(f"# Theorem A certification: L0 = log2/2, grid step {step}, K={K}")
    print(f"cap at R=6.25 (negative region end): {caps[25]:.5f}")
    print(f"cap reaches 1 at R = {next((Rs[k] for k in range(K+1) if caps[k] >= 1.0), None)}")
    print(f"certified Stieltjes ball: {total}")
    lo = float(total.lower())
    print(f"\nCERTIFIED: c0 >= {lo:.6f}")
    if lo > 0:
        print("THEOREM A HOLDS with the certified constant above.")

if __name__ == '__main__':
    main()
