# 1. Prerequisites

Do not open the paper until you can do the exercises in this chapter from memory. Everything later is a cryptographic wrapping of these facts.

## 1.1 Quantum measurements and no-signalling

A two-outcome measurement with setting $s$ on system $i$ is a POVM $\{\Pi_{r|s}^i\}_{r=0,1}$ with $\Pi_{r|s}^i\succeq 0$ and $\sum_r\Pi_{r|s}^i=\mathbb{1}$. For a bipartite state $\rho$ and product measurements,

$$
P(r^0,r^1\mid s^0,s^1)=\operatorname{Tr}\bigl(\rho\,\Pi_{r^0|s^0}^0\otimes\Pi_{r^1|s^1}^1\bigr).
$$

**Exercise 1.1.** Prove the no-signalling identities

$$
\sum_{r^1}P(r^0,r^1\mid s^0,s^1)=P(r^0\mid s^0)
$$

independent of $s^1$, and the symmetric one for Bob. This is the *only* constraint used in §4 of the paper (Alice’s security). Quantum theory is *not* used there.

**Exercise 1.2.** Why does “the boxes may have clocks, gyroscopes, and memory” not violate the formula above, provided that when two boxes are measured they do not communicate? Write one sentence that will become part of your §2.2.

## 1.2 The CHSH inequality

For binary inputs/outputs $x,y,a,b\in\{0,1\}$, the CHSH correlator is

$$
I=\sum_{a,b,x,y=0,1}(-1)^{a\oplus b\oplus xy}\,P(a,b\mid x,y).
$$

Equivalently, if $A_x,B_y$ are $\pm 1$-valued observables ($A_x=1-2a$, etc.),

$$
I=\langle A_0B_0\rangle+\langle A_0B_1\rangle+\langle A_1B_0\rangle-\langle A_1B_1\rangle.
$$

Bounds you must know:

| Theory | Bound on $I$ | Name |
|---|---|---|
| Local hidden variables | $\lvert I\rvert\le 2$ | CHSH / Bell |
| Quantum mechanics | $\lvert I\rvert\le 2\sqrt{2}$ | Tsirelson |
| No-signalling (no QM) | $\lvert I\rvert\le 4$ | algebraic / PR-box |

**Exercise 1.3.** Derive the local bound $I\le 2$ from determinism plus no-signalling (or from the usual CHSH argument).

**Exercise 1.4.** For $|\phi^+\rangle=\frac{1}{\sqrt{2}}(|00\rangle+|11\rangle)$ and observables in the $zx$-plane, prove

$$
\langle\phi^+|\sigma_\alpha\otimes\sigma_\beta|\phi^+\rangle=\cos(\alpha-\beta).
$$

Then recover Tsirelson’s bound by placing Alice at $0,\pi/2$ and Bob at $\pi/4,-\pi/4$ (or an equivalent pair). Write down the four angles you used; you will reuse this geometry in §5.2.

**Exercise 1.5.** A *CHSH indicator* for a single round with uniformly random inputs is

$$
I(W)=4\sum_{a,b,x,y}(-1)^{a\oplus b\oplus xy}\,\delta_{A,a}\delta_{B,b}\delta_{X,x}\delta_{Y,y}.
$$

Show that $\mathbb{E}[I(W)]$ equals the CHSH expression above. Why the prefactor $4$? (This is footnote 3 of the paper.)

## 1.3 Pseudo-telepathy versus statistics

A nonlocal game is *pseudo-telepathic* if there is a quantum (or no-signalling) strategy that wins with probability 1, while every classical strategy wins with probability $<1$.

**Exercise 1.6.** The GHZ game is pseudo-telepathic. CHSH is not: even the Tsirelson strategy wins with probability $\cos^2(\pi/8)\simeq 0.85$, not 1. Why does that matter for *distrustful* cryptography, where Bob must test nonlocality *and* check Alice’s revealed bit, and the two parties will not cooperate?

Write a four-sentence answer. This *is* the motivation of the paper. Compare with [02-the-research-question.md](02-the-research-question.md) after you have written it.

## 1.4 PR boxes

A Popescu–Rohrlich box is the no-signalling resource

$$
r^0\oplus r^1=s^0\cdot s^1,\qquad r^i,s^i\in\{0,1\}
$$

(up to local relabelling). It achieves $I=4$.

**Exercise 1.7.** Verify no-signalling for the PR box, and that the CHSH game is won with certainty. This is why Appendix A can drop sequential testing: verification of the box and of the commitment can be the *same* measurement, as in the GHZ protocol.

## 1.5 EPR correlations used as a “commitment token”

The honest protocol needs *two* kinds of correlations from the same pair of boxes:

1. CHSH violation on input pair $\{0,1\}\times\{0,1\}$.
2. Perfect equality $r^0=r^1$ on the “shifted” pairs $(s^0,s^1)=(i,\,i+2\bmod 4)$ for $i=0,1,2,3$.

**Exercise 1.8 (do this before reading §3).** Invent four angles for box 0 and four for box 1, all of the form $\sigma_\theta$, such that:

- inputs $(0,1)$ on both boxes give the Tsirelson CHSH strategy;
- for each $i$, the observable of box 0 at input $i$ equals the observable of box 1 at input $i+2\bmod 4$.

There is a canonical solution (the paper’s). Finding it yourself makes the commit/reveal rule obvious: Alice’s commit input is $b+2$, Bob’s check input is $b$, and they are measuring the *same* observable.

## 1.6 Semidefinite relaxations of quantum correlations

Alice’s control at fixed $I$ is a polynomial optimization problem over unknown Hilbert-space operators. The NPA hierarchy (Navascués–Pironio–Acín) produces a sequence of SDPs whose optima decrease to the true quantum value.

**Exercise 1.9.** Read enough of NPA (PRL **98**, 010401 (2007) or NJP **10**, 073013 (2008)) to answer:

- What is a *behaviour* $P(ab|xy)$?
- What is a *moment matrix* at level $1$ and at level $2$?
- Why does a feasible moment matrix *not* prove that a quantum realization exists, while infeasibility *does* prove that none exists?

You do **not** need to re-derive NPA. You need to know that the paper solves the *level-2* relaxation of (7), and then exhibits an explicit strategy whose $P_{\mathrm{cont}}$ matches the SDP number to $10^{-8}$. Matching means the relaxation has already converged.

## 1.7 Martingales and Azuma–Hoeffding

Let $\{\mathcal{F}_k\}$ be a filtration (think: the history $\mathbf{W}_k$). A process $Z_k$ is a martingale if $\mathbb{E}[Z_{k+1}\mid\mathcal{F}_k]=Z_k$.

**Azuma–Hoeffding.** If $\lvert Z_{k+1}-Z_k\rvert\le D$ almost surely, then for $\varepsilon>0$,

$$
P\bigl(Z_k-Z_0\ge k\varepsilon\bigr)\le\exp\bigl(-k\varepsilon^2/(2D^2)\bigr).
$$

**Exercise 1.10.** Define

$$
\Delta_k=\bar I_k-\frac1k\sum_{n=1}^k\mathbb{E}\bigl[I(W_n)\mid\mathbf{W}_{n-1}\bigr],\qquad Z_k=k\Delta_k.
$$

Prove that $Z_k$ is a martingale. Bound $\lvert Z_{k+1}-Z_k\rvert$ using only $\lvert I(w)\rvert\le 4$ and $\lvert\mathbb{E}[I]\rvert\le 2\sqrt{2}$. You should get $D=4+2\sqrt{2}$. This is Appendix D.

## 1.8 Bit-commitment folklore (one hour of reading)

Read, or at least know the statements of:

- Lo–Chau, PRL **78**, 3410 (1997) and Mayers, PRL **78**, 3414 (1997): no *perfect* quantum bit commitment.
- Spekkens–Rudolph, PRA **65**, 012310 (2001): imperfect BC is possible.
- Chailloux–Kerenidis, FOCS 2011: in any *balanced* quantum BC, $P_{\mathrm{cont}}=P_{\mathrm{gain}}\gtrsim 0.739$.
- Silman *et al.*, PRL **106**, 220501 (2011): DI bit commitment from GHZ, with $P_{\mathrm{cont}}=\cos^2(\pi/8)$, $P_{\mathrm{gain}}=3/4$.
- Kent, PRL **83**, 1447 (1999): *relativistic* BC is perfect, but needs two remote labs for at least one party.

**Exercise 1.11.** In one paragraph, distinguish device-independent BC from relativistic BC. The paper’s point is: one lab per party, no spacelike-separation requirement, shielding instead.

## Checkpoint

You are ready for chapter 2 if you can, without notes:

1. Write the CHSH expression and the three bounds 2, $2\sqrt{2}$, 4.
2. Explain why GHZ is pseudo-telepathic and CHSH is not.
3. State $P_{\mathrm{cont}}$ and $P_{\mathrm{gain}}$ in words.
4. Recite Azuma–Hoeffding.
