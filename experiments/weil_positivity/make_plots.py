#!/usr/bin/env python3
"""Plots for the Weil-positivity sweep (run after weil_form.py sweep/profiles)."""
import csv, math, os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))

rows = list(csv.DictReader(open(os.path.join(HERE, 'sweep.csv'))))
L = np.array([float(r['L']) for r in rows])
margin = np.array([float(r['margin']) for r in rows])
total = np.array([float(r['total']) for r in rows])
deficit = np.array([float(r['deficit']) for r in rows])
g2 = np.array([float(r['g_log2']) for r in rows])

thresholds = [(n, math.log(n) / 2) for n in
              [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29, 31, 32,
               37, 41, 43, 47, 49, 53] if math.log(n) / 2 <= L.max()]

fig, (ax, ax2) = plt.subplots(2, 1, figsize=(11, 9), sharex=True,
                              gridspec_kw={'height_ratios': [3, 1]})
ax.axhline(0, color='k', lw=0.8)
for n, t in thresholds:
    ax.axvline(t, color='0.85', lw=0.7, zorder=0)
    if n in (2, 3, 4, 5, 7, 11, 19, 31, 53):
        ax.text(t, ax.get_ylim()[1] * 0.0 + 0.92, str(n), fontsize=7,
                ha='center', color='0.4', transform=ax.get_xaxis_transform())
ax.plot(L, margin, 'o-', ms=3, color='tab:blue',
        label=r'archimedean margin  $\lambda_{\min}(G)$ (constrained)')
ax.plot(L, total, 's-', ms=3, color='tab:red',
        label=r'total  $\lambda_{\min}(G+P)$  (RH $\Rightarrow\ \geq 0$)')
ax.plot(L, -deficit, '^-', ms=3, color='tab:green',
        label=r'$-\|P\|$  (prime deficit, lower bound for total$-$margin)')
ax.axvline(math.log(2) / 2, color='orange', lw=1.4, ls='--',
           label=r'$L=\frac{1}{2}\log 2$: prime 2 enters (CC window ends)')
ax.set_ylabel('eigenvalue (L2-normalized f)')
ax.set_title('Weil quadratic form on supp$f \\subset [-L,L]$, pole directions projected out '
             '(N=48 sine basis)\nmargin vs prime deficit across prime-power thresholds')
ax.legend(loc='lower left', fontsize=9)
ax.grid(alpha=0.2)

ax2.axhline(0, color='k', lw=0.8)
ax2.plot(L, g2, 'd-', ms=3, color='tab:purple',
         label=r'$g_{\min}(\log 2)$: minimizer autocorrelation at the $p=2$ lag')
for n, t in thresholds:
    ax2.axvline(t, color='0.85', lw=0.7, zorder=0)
ax2.set_xlabel(r'support half-length $L$   (multiplicative window $[e^{-L}, e^{L}]$, '
               r'$g$ support ratio $e^{4L}$)')
ax2.set_ylabel(r'$g(\log 2)$')
ax2.legend(loc='upper left', fontsize=9)
ax2.grid(alpha=0.2)
fig.tight_layout()
fig.savefig(os.path.join(HERE, 'sweep.png'), dpi=140)
print('wrote sweep.png')

# minimizer profiles
pf = os.path.join(HERE, 'profiles.npz')
if os.path.exists(pf):
    d = np.load(pf)
    Ls = sorted({float(k.split('_')[1]) for k in d.files if k.startswith('lam_')})
    fig, axes = plt.subplots(2, len(Ls), figsize=(3.1 * len(Ls), 6), squeeze=False)
    for i, Lv in enumerate(Ls):
        u, f = d[f'u_{Lv}'], d[f'f_{Lv}']
        r, h = d[f'r_{Lv}'], d[f'h_{Lv}']
        lam = float(d[f'lam_{Lv}'])
        s = np.sign(f[np.argmax(np.abs(f))])
        axes[0][i].plot(u, s * f, color='tab:blue')
        axes[0][i].set_title(f'L={Lv}  $\\lambda_{{\\min}}$={lam:+.4f}', fontsize=9)
        axes[0][i].axhline(0, color='k', lw=0.5)
        axes[0][i].set_xlabel('u')
        axes[1][i].plot(r, h, color='tab:red')
        axes[1][i].axvspan(0, 2 * math.pi, alpha=0.12, color='gray')
        axes[1][i].set_xlabel('r')
        for z in (14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187,
                  43.3271, 48.0052, 49.7738, 52.9703, 56.4462):
            axes[1][i].axvline(z, color='green', lw=0.5, alpha=0.5)
    axes[0][0].set_ylabel('minimizer $f(u)$')
    axes[1][0].set_ylabel('$|F(r)|^2$  (zeros green, $\\Omega<0$ gray)')
    fig.suptitle('Total-form minimizers: profile and spectral density '
                 '(gray = negative archimedean kernel region, green = zeta zeros)')
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, 'profiles.png'), dpi=140)
    print('wrote profiles.png')
