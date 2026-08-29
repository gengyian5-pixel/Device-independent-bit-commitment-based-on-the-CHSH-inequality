"""Rebuild Figs. 1 and 3 of Aharon et al., New J. Phys. 18, 025014 (2016).

Fig. 1: Alice's control C vs CHSH threshold, from the explicit strategy (8)--(10).
Fig. 3: finite-N upper bound (19) with I_th = 2*sqrt(2)*(1 - 1/sqrt(N)).

Usage:
    python scripts/reconstruct_figures.py
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np

try:
    import matplotlib.pyplot as plt
except ImportError as exc:  # pragma: no cover
    raise SystemExit("matplotlib is required: pip install matplotlib") from exc

OUT_DIR = Path(__file__).resolve().parent.parent / "study-guide" / "figures"
SQRT2 = math.sqrt(2)
TSIRELSON = 2 * SQRT2
COS2_PI8 = math.cos(math.pi / 8) ** 2
D = 4 + 2 * SQRT2  # Azuma difference bound, App. D


def phi_opt(theta: np.ndarray) -> np.ndarray:
    """Equation (10)."""
    num = 2.0 * (np.cos(2.0 * theta) + np.sin(2.0 * theta) ** 2)
    den = np.sqrt(6.0 - 2.0 * np.cos(4.0 * theta))
    arg = np.clip(num / den, -1.0, 1.0)
    return np.arccos(arg)


def chsh_I(theta: np.ndarray, phi: np.ndarray) -> np.ndarray:
    """Equation (9)."""
    return 2.0 * np.cos(2.0 * theta - phi) - np.cos(4.0 * theta - phi) + np.cos(phi)


def control_from_theta(theta: np.ndarray) -> np.ndarray:
    """Equation (8)."""
    return np.cos(theta / 2.0) ** 2


def C_of_I(I_values: np.ndarray) -> np.ndarray:
    """Invert the parametric curve (I(θ), C(θ)) for I in [2, 2√2].

    For I below 2 the explicit strategy is not the interesting branch for
    security plots; we clip to C=1. For I above Tsirelson, C is the GHZ value.
    """
    theta = np.linspace(1e-4, math.pi / 4, 4000)
    phi = phi_opt(theta)
    I_curve = chsh_I(theta, phi)
    C_curve = control_from_theta(theta)
    # I decreases as theta goes from ~0 (local, C~1) to π/4 (Tsirelson, C=cos²(π/8))
    order = np.argsort(I_curve)
    I_sorted = I_curve[order]
    C_sorted = C_curve[order]
    I_clipped = np.clip(I_values, I_sorted[0], I_sorted[-1])
    return np.interp(I_clipped, I_sorted, C_sorted)


def Q_eps(eps: float, N: int, K0: int) -> float:
    """Equation (18)."""
    if eps <= 0:
        return float(max(N - K0, 0))
    alpha = (eps ** 2) / (2.0 * D * D)
    eK = math.exp(-K0 * alpha)
    eN = math.exp(-N * alpha)
    denom = 1.0 - math.exp(-alpha)
    if denom <= 0:
        return 1.0
    return (eK - eN) / denom


def finite_n_bound(N: int, I_th: float, n_eps: int = 80) -> float:
    """Equation (19): min over ε of ((N-1)/N)[C(I_th-ε)+(1-C)Q(ε)] + 1/N."""
    C_th = float(C_of_I(np.array([I_th]))[0])
    K0 = max(int(math.ceil((N - 1) * C_th)), 1)
    # ε cannot exceed the gap down to the local bound in a useful way
    eps_grid = np.linspace(0.0, max(I_th - 2.0, 1e-6), n_eps)
    best = 1.0
    for eps in eps_grid:
        C_eps = float(C_of_I(np.array([I_th - eps]))[0]) if I_th - eps >= 2.0 else 1.0
        q = min(Q_eps(float(eps), N, K0), 1.0)
        val = ((N - 1) / N) * (C_eps + (1.0 - C_eps) * q) + 1.0 / N
        if val < best:
            best = val
    return best


def plot_fig1() -> None:
    theta = np.linspace(1e-3, math.pi / 4, 600)
    phi = phi_opt(theta)
    I = chsh_I(theta, phi)
    C = control_from_theta(theta)

    fig, ax = plt.subplots(figsize=(5.2, 3.8))
    ax.plot(I, C, color="black", lw=1.8)
    ax.axhline(COS2_PI8, color="0.5", ls="--", lw=1, label=r"$\cos^2(\pi/8)$")
    ax.axvline(TSIRELSON, color="0.5", ls=":", lw=1, label=r"$2\sqrt{2}$")
    ax.set_xlabel(r"$I_{\mathrm{th}}$")
    ax.set_ylabel(r"$P_{\mathrm{cont}}=C(I_{\mathrm{th}})$")
    ax.set_title("Fig. 1 reconstruction: Alice's control (asymptotic)")
    ax.set_xlim(2.0, TSIRELSON + 0.05)
    ax.set_ylim(0.82, 1.02)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "fig1_alice_control.png", dpi=160)
    plt.close(fig)


def plot_fig3() -> None:
    # Caption convention in the published figure: I_th = 2√2 (1 - 1/√N)
    Ns = np.unique(np.logspace(1, 5, 24).astype(int))
    bounds = []
    C_vals = []
    for N in Ns:
        I_th = min(max(TSIRELSON * (1.0 - 1.0 / math.sqrt(int(N))), 2.0), TSIRELSON)
        bounds.append(finite_n_bound(int(N), I_th))
        C_vals.append(float(C_of_I(np.array([I_th]))[0]))

    fig, ax = plt.subplots(figsize=(5.2, 3.8))
    ax.plot(np.log10(Ns), bounds, color="black", lw=1.8, label=r"bound (19)")
    ax.plot(np.log10(Ns), C_vals, color="0.35", ls=":", lw=1.4, label=r"$C(I_{\mathrm{th}})$")
    ax.axhline(COS2_PI8, color="0.5", ls="--", lw=1, label=r"$\cos^2(\pi/8)\simeq 0.854$")
    ax.set_xlabel(r"$\log_{10} N$")
    ax.set_ylabel(r"upper bound on $P_{\mathrm{cont}}$")
    ax.set_title(r"Fig. 3 reconstruction: $I_{\mathrm{th}}=2\sqrt{2}(1-1/\sqrt{N})$")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "fig3_finite_N.png", dpi=160)
    plt.close(fig)


def sanity_checks() -> None:
    theta = np.array([math.pi / 4])
    phi = phi_opt(theta)
    I = float(chsh_I(theta, phi)[0])
    C = float(control_from_theta(theta)[0])
    assert abs(float(phi[0]) - math.pi / 4) < 1e-9, phi
    assert abs(I - TSIRELSON) < 1e-9, I
    assert abs(C - COS2_PI8) < 1e-12, C
    # D identity from App. D
    assert abs(D - 1.0 / math.sin(math.pi / 8) ** 2) < 1e-12, D
    print("sanity checks passed:")
    print(f"  theta=pi/4 => phi={float(phi[0]):.6f}, I={I:.6f}, C={C:.6f}")
    print(f"  D=4+2√2={D:.6f}")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    sanity_checks()
    plot_fig1()
    plot_fig3()
    print(f"wrote {OUT_DIR / 'fig1_alice_control.png'}")
    print(f"wrote {OUT_DIR / 'fig3_finite_N.png'}")


if __name__ == "__main__":
    main()
