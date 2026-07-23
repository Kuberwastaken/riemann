#!/usr/bin/env python3
"""
Block constants for the T1 core/dipole architecture (see T1-ARCHITECTURE.md).

For L in the one-prime window (1/2 log2, 1/2 log3), partition [-L,L] into
core C = (-(a-L), a-L) and edges E-+ (a = log 2), build sector sine bases,
project into the pole-constraint space, and compute on the constrained span:
    lam_c  = min eig of archimedean G on the core sector
    lam_e  = min eig of G on the edge sector
    x      = operator norm of the core-edge block of G
    q      = operator norm of the prime-2 form Q2 on the edge sector
             (Lemma 1: q <= log2/sqrt2 = 0.490129, only edge mass exposed)
2x2 sufficient criterion for Weil positivity in the window:
    lam_c > 0  and  min eig [[lam_c, -x], [-x, lam_e - q]] >= 0.
Caveat (documented): projecting sector bases into the constraint null space mixes
sectors by a rank-2 perturbation; this is a numerical test of the architecture,
not a proof. Reference column: exact constrained lambda_min(G + Q2) (full space).
"""
import numpy as np, math, os
import weil_form as wf

HERE = os.path.dirname(os.path.abspath(__file__))
A = math.log(2.0)
N = 48

def sector_basis_coeffs(alpha, beta, K, L, N, npts=4001):
    """Coefficients in the global sine basis of K sector sines on [alpha,beta]."""
    u = np.linspace(alpha, beta, npts)
    w = wf.simpson_w(npts, u[1] - u[0])
    Phi = wf.phi_samples(u, L, N)                       # (N, npts)
    k = np.arange(1, K + 1)[:, None]
    Psi = np.sin(k * math.pi * (u[None, :] - alpha) / (beta - alpha)) \
        * math.sqrt(2.0 / (beta - alpha))               # (K, npts)
    return (Phi * w) @ Psi.T                            # (N, K)

def proj_span(B, Pc, floor=1e-8):
    """Orthonormal basis of Pc*span(B) (constraint-projected sector span)."""
    Bt = Pc @ B
    U, s, _ = np.linalg.svd(Bt, full_matrices=False)
    return U[:, s > floor * s.max()]

def run():
    q_theory = math.log(2) / math.sqrt(2)
    print(f"# a=log2, q_theory=(log2)/sqrt2={q_theory:.6f}   N={N}")
    print("# L      lam_c     lam_e      x        q_meas   crit2x2   total_exact")
    for L in (0.370, 0.400, 0.430, 0.460, 0.490, 0.520, 0.545):
        c = A - L                                      # core half-length
        G = wf.arch_matrix(L, N)
        P, pieces = wf.prime_matrix(L, N)
        Q2 = pieces.get(2, np.zeros((N, N)))
        vp, vm = wf.pole_vectors(L, N)
        V = np.stack([vp, vm], axis=1)
        Pc = np.eye(N) - V @ np.linalg.solve(V.T @ V, V.T)
        Qfull = wf.constrained_basis(vp, vm)
        total = wf.eig_min(G + P, Qfull)[0]

        Bc = sector_basis_coeffs(-c, c, 12, L, N)
        Bem = sector_basis_coeffs(-L, -c, 8, L, N)
        Bep = sector_basis_coeffs(c, L, 8, L, N)
        Uc = proj_span(Bc, Pc)
        Ue = proj_span(np.hstack([Bem, Bep]), Pc)
        lam_c = np.linalg.eigvalsh(Uc.T @ G @ Uc)[0]
        lam_e = np.linalg.eigvalsh(Ue.T @ G @ Ue)[0]
        x = np.linalg.norm(Uc.T @ G @ Ue, 2)
        q = np.linalg.norm(Ue.T @ Q2 @ Ue, 2)
        M2 = np.array([[lam_c, -x], [-x, lam_e - q]])
        crit = np.linalg.eigvalsh(M2)[0]
        print(f"{L:.3f}  {lam_c:+.6f} {lam_e:+.6f} {x:.6f}  {q:.6f}  "
              f"{crit:+.6f}  {total:+.6f}")

if __name__ == '__main__':
    run()
