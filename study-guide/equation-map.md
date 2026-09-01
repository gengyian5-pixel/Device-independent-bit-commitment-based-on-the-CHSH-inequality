# Equation map (paper → meaning)

Use this as an index while writing. Every display in NJP **18**, 025014 (2016) should appear in your manuscript, in this logical order.

| Eq. | Location | What it is | You derive it in |
|---|---|---|---|
| (1) | §2.2 | Born rule for two isolated boxes | ch. 4 |
| (2) | §3 | Honest CHSH $=2\sqrt{2}$ on inputs $\{0,1\}$ | ch. 5 |
| (3) | §3 | Empirical CHSH $\bar I_n$ | ch. 6 |
| (4) | §3 | Single-round CHSH indicator (prefactor 4) | ch. 1, 6 |
| (5) | §4.1 | $P_{\mathrm{gain}}$ expanded, then $\le 3/4$ | ch. 7 |
| (6) | §5.1 | $P_{\mathrm{cont}}$ as four families of probabilities | ch. 8 |
| (7) | §5.1 | SDP/NPA optimization of (6) at fixed $I_{\mathrm{th}}$ | ch. 8 |
| (8) | §5.2 | $P_{\mathrm{cont}}=\cos^2(\theta/2)$ | ch. 8 |
| (9) | §5.2 | $I(\theta,\varphi)$ for the cheating axes | ch. 8 |
| (10) | §5.2 | $\varphi_{\mathrm{opt}}(\theta)$ | ch. 8 |
| (11) | §5.3 | $P_{\mathrm{cont}}$ averaged over $n$, plus $1/N$ | ch. 9 |
| (12) | §5.3 | Same, written over length-$(N-1)$ histories | ch. 9 |
| (13) | §5.3 | Last good time $K(\mathbf{w}_{N-1})$ | ch. 9 |
| (14) | §5.3 | Bound using $n\le K$ only | ch. 9 |
| (15) | §5.3 | Split at $K_0$, concavity of $C$ | ch. 9 |
| (16) | §5.3 | Bad set $\pi_k(\varepsilon)$ | ch. 9 |
| (17) | App. D | Azuma tail on $\pi_k(\varepsilon)$ | ch. 9 |
| (18) | §5.3 | Sum of tails $Q(\varepsilon)$ | ch. 9 |
| (19) | §5.3 | Final finite-$N$ bound | ch. 9 |
| (20) | App. A | PR-box relation $r^0\oplus r^1=s^0 s^1$ | ch. 10 |
| (21) | App. A | Alice’s control polynomial for PR boxes | ch. 10 |
| (22) | App. D | Martingale increment $\Delta_k$ | ch. 9 |
| (23) | App. D | Bounded differences $\lvert Z_{k+1}-Z_k\rvert\le D$ | ch. 9 |
| (24) | App. D | Azuma–Hoeffding statement | ch. 9 |

Figures:

| Fig. | Content | Script |
|---|---|---|
| 1 | $C(I_{\mathrm{th}})$ from (8)–(10) | `scripts/reconstruct_figures.py` |
| 2 | Cheating measurement axes | draw by hand from ch. 8 |
| 3 | Finite-$N$ bound vs $\log_{10}N$ | `scripts/reconstruct_figures.py` |
