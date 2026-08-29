# 5. Honest resources

Paper analogue: the paragraphs of §3 before the numbered protocol. Design the physics *before* you design the cryptography. If the honest correlations are wrong, commit/reveal will not be consistent with CHSH.

## 5.1 Boxes

One pair of boxes. Each box: inputs $\{0,1,2,3\}$, outputs $\{0,1\}$. Think of inputs $0,1$ as the CHSH pair and inputs $2,3$ as “the same observables, on the other box, shifted by $2$”.

## 5.2 Target correlations (ideal)

For every use $n$,

$$
\sum_{r^0,r^1,s^0,s^1=0,1}(-1)^{r^0\oplus r^1\oplus s^0 s^1}\,P(r^0,r^1\mid s^0,s^1)=2\sqrt{2},
$$

and, separately,

$$
r^0=r^1\quad\text{whenever}\quad s^0=i,\; s^1=i+2\pmod{4},\quad i\in\{0,1,2,3\}.
$$

**Exercise 5.1.** Why four “equality” pairs, not one? Because Alice will receive a random box $c\in\{0,1\}$ and will commit $b\in\{0,1\}$, using input $s^c=b+2$. Bob must be able to measure the *matching* observable on the other box, which is input $s^{\bar c}=b$. Check that $(s^c,s^{\bar c})=(b+2,\,b)$ is always one of the four equality pairs, for both values of $c$.

Work through the table (fill every cell):

| $c$ | $b$ | Alice input $s^c$ | Bob input $s^{\bar c}$ | pair $(s^0,s^1)$ | should $r^0=r^1$? |
|---|---|---|---|---|---|
| 0 | 0 |  |  |  |  |
| 0 | 1 |  |  |  |  |
| 1 | 0 |  |  |  |  |
| 1 | 1 |  |  |  |  |

## 5.3 The canonical implementation

Prepare (many copies of) $|\phi^+\rangle=\frac{1}{\sqrt{2}}(|00\rangle+|11\rangle)$. Observables $\sigma_\theta=\cos\theta\,\sigma_z+\sin\theta\,\sigma_x$:

| Input | Box 0 | Box 1 |
|---|---|---|
| 0 | $\sigma_x=\sigma_{\pi/2}$ | $\sigma_{\pi/4}$ |
| 1 | $\sigma_z=\sigma_{0}$ | $\sigma_{3\pi/4}$ |
| 2 | $\sigma_{\pi/4}$ | $\sigma_x$ |
| 3 | $\sigma_{3\pi/4}$ | $\sigma_z$ |

**Exercise 5.2.** Verify:

1. Box 0 on $\{0,1\}$ and box 1 on $\{0,1\}$ is a Tsirelson pair: angles $\pi/2,0$ versus $\pi/4,3\pi/4$. Compute $I$ using Exercise 1.4. You want $+2\sqrt{2}$ with the CHSH sign pattern $(-1)^{xy}$. If you get $-2\sqrt{2}$, a local relabelling of an outcome is needed; decide which one and record it. (The paper’s output labels are chosen so that (2) holds as written.)
2. Box 0 input $i$ equals box 1 input $i+2\bmod 4$, as operators. Therefore equality of outcomes on $|\phi^+\rangle$ is certain (same observable, singlet-free EPR).

**Exercise 5.3.** Draw the four axes in the $zx$-plane. This figure is not in the paper, but it will make Fig. 2 (Alice’s cheating axes) easy later.

## 5.4 Noise

In a real run, $I<2\sqrt{2}$ and the equality pairs are only *approximately* correlated. The protocol therefore uses a threshold $I_{\mathrm{th}}$ and will sometimes abort on honest equality tests. The security theorems are stated in terms of the *observed* $\bar I_n$ and of a function $C(I)$ giving Alice’s control at CHSH value $I$.

**Exercise 5.4.** Decide, for your write-up, whether honest completeness is:

- asymptotic (ideal boxes, $N\to\infty$, $\bar I_n\to 2\sqrt{2}>I_{\mathrm{th}}$), or
- noisy (you would need a gap $I_{\mathrm{honest}}-I_{\mathrm{th}}$ and a Chernoff/Azuma bound on honest abort).

The paper discusses this qualitatively in §3 and does not give a completeness theorem with explicit $\varepsilon(N)$. If you want a stronger paper, adding one is a natural extension; it is *not* required to reconstruct the published result.

## Checkpoint

From memory, write the measurement table and the rule $s^c=b+2$, $s^{\bar c}=b$. Explain in one sentence why those two inputs measure the same observable.
