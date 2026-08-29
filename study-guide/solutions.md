# Worked solutions

Attempt every exercise before reading the corresponding subsection. Formula numbers refer to Aharon *et al.*, NJP **18**, 025014 (2016).

---

## Chapter 1

**1.1.** Trace out Bob’s POVM: $\sum_{r^1}\operatorname{Tr}(\rho\,\Pi_{r^0|s^0}^0\otimes\Pi_{r^1|s^1}^1)=\operatorname{Tr}(\rho_A\Pi_{r^0|s^0}^0)$, independent of $s^1$.

**1.2.** Memory and clocks change *which* POVM is used as a function of the box’s own past; they do not create a tensor factor that depends on the *other* box’s current input, provided communication is blocked at measurement time.

**1.3.** Deterministic local assignments $a(x),b(y)$. The combination $a(0)b(0)+a(0)b(1)+a(1)b(0)-a(1)b(1)=a(0)(b(0)+b(1))+a(1)(b(0)-b(1))$ equals $\pm 2$ because one of $b(0)\pm b(1)$ is $0$ and the other is $\pm 2$. Average: $\lvert I\rvert\le 2$.

**1.4.** $\sigma_\theta=\cos\theta\,\sigma_z+\sin\theta\,\sigma_x$. On $|\phi^+\rangle$, $\langle\sigma_z\otimes\sigma_z\rangle=\langle\sigma_x\otimes\sigma_x\rangle=1$, $\langle\sigma_z\otimes\sigma_x\rangle=0$, hence $\langle\sigma_\alpha\otimes\sigma_\beta\rangle=\cos(\alpha-\beta)$. CHSH with Alice $0,\pi/2$ and Bob $\pi/4,-\pi/4$: each correlator has absolute value $1/\sqrt{2}$ and the signs align to $2\sqrt{2}$.

**1.5.** Uniform inputs: each of the four pairs has probability $1/4$. The factor $4$ cancels that, so $\mathbb{E}[I(W)]$ is the CHSH sum.

**1.6.** Bob must test nonlocality without Alice’s help, and must check her opening with a measurement on *his* box. GHZ gives certainty on a relation that involves the revealed bit, so one measurement does both jobs. CHSH never wins with certainty, so a one-shot CHSH test cannot double as a deterministic check. Something else (hiding which round is the check) is required.

**1.7.** For each input pair the PR box has $P(r^0,r^1|s^0,s^1)=\frac12\delta_{r^0\oplus r^1,\,s^0 s^1}$. Marginals are uniform and independent of the other input. CHSH: every pair contributes $+1$, so $I=4$.

**1.8 / 1.9 / 1.10.** See chapters 5, 8, and 9. For 1.10: $Z_{k+1}-Z_k=I(W_{k+1})-\mathbb{E}[I(W_{k+1})\mid\mathbf{W}_k]$, whose absolute value is at most $4+2\sqrt{2}$. Taking $\mathbb{E}[\,\cdot\mid\mathbf{W}_k]$ of $Z_{k+1}$ cancels the increment, so $Z_k$ is a martingale.

---

## Chapter 5

**5.1 table.**

| $c$ | $b$ | $s^c$ | $s^{\bar c}$ | $(s^0,s^1)$ | equality pair? |
|---|---|---|---|---|---|
| 0 | 0 | 2 | 0 | (2,0) | $i=2$: $(2,0)$ |
| 0 | 1 | 3 | 1 | (3,1) | $i=3$: $(3,1)$ |
| 1 | 0 | 2 | 0 | (0,2) | $i=0$: $(0,2)$ |
| 1 | 1 | 3 | 1 | (1,3) | $i=1$: $(1,3)$ |

**5.2.** Box 0 at $0,1$: $\sigma_x,\sigma_z$. Box 1 at $0,1$: $\sigma_{\pi/4},\sigma_{3\pi/4}$. Then

$$
\langle\sigma_x\otimes\sigma_{\pi/4}\rangle=\cos(\pi/2-\pi/4)=1/\sqrt{2},
$$

$$
\langle\sigma_x\otimes\sigma_{3\pi/4}\rangle=\cos(\pi/2-3\pi/4)=1/\sqrt{2},
$$

$$
\langle\sigma_z\otimes\sigma_{\pi/4}\rangle=\cos(0-\pi/4)=1/\sqrt{2},
$$

$$
\langle\sigma_z\otimes\sigma_{3\pi/4}\rangle=\cos(0-3\pi/4)=-1/\sqrt{2}.
$$

CHSH $I=\langle A_0B_0\rangle+\langle A_0B_1\rangle+\langle A_1B_0\rangle-\langle A_1B_1\rangle$ with $A_0=\sigma_x$, $A_1=\sigma_z$, $B_0=\sigma_{\pi/4}$, $B_1=\sigma_{3\pi/4}$ equals $2\sqrt{2}$. Operator identity: box 0 input $i$ equals box 1 input $i+2\bmod 4$ by inspection of the table.

---

## Chapter 6

**6.1.** $q=r\oplus ab$. If $b=0$, $q=r$. If $b=1$, $q=r$ or $q=r\oplus 1$ according to $a$. The token check is exactly that disjunction.

**6.3.** $ab=0$ unless $a=b=1$, probability $3/4$. That is Strategy A in §4.

**6.4.** If the kept box is measured only after a delay that never occurs during CHSH testing, Alice programs: CHSH-perfect on the public schedule; deterministic (both openings accepted) on a late measurement.

---

## Chapter 7

**7.1–7.2.** Honest $P(a,b)=1/4$. For $b=0$, $m=r^c$ for both values of $a$, giving the factor $2$ in front of $P(0,0\mid 2,0)+P(1,0\mid 2,1)$. For $b=1$, $m=r$ and $m=r\oplus 1$ produce the four terms $P(0,1\mid 3,0)$, $P(0,1\mid 3,1)$, $P(1,1\mid 3,1)$, $P(1,1\mid 3,0)$.

**7.3.** No-signalling and positivity:

$$
P(0,0\mid 2,0)\le P(r^c=0\mid s^c=2),\qquad P(1,0\mid 2,1)\le P(r^c=1\mid s^c=2),
$$

so their sum is $\le 1$. For each $m\in\{0,1\}$,

$$
P(r=m,g=0\mid s=2,m)+P(g=1\mid m)\le P(g=0\mid m)+P(g=1\mid m)=1,
$$

and $P(g=1\mid m)=\sum_r P(r,1\mid 3,m)$. Adding the cases $m=0$ and $m=1$ yields

$$
A+B\le 2,\qquad A:=P(0,0\mid 2,0)+P(1,0\mid 2,1)\le 1,
$$

where $B$ is the sum of the four $b=1$ terms. Then

$$
P_{\mathrm{gain}}=\frac14\max(2A+B)=\frac14\max\bigl(A+(A+B)\bigr)\le\frac14(1+2)=\frac34.
$$

**7.4.** $q=r^c\oplus ab$ equals $b$ whenever $ab=0$, i.e. with probability $3/4$, if $r^c=b$.

**7.5.** Settings $s^{\bar c}=0$ and $s^c=2$ are the same observable, so when $b=0$ Bob’s outcome equals Alice’s, and $q=r^c$, so he always guesses $2$. When $b=1$ the observables differ by $\pi/2$, so $\langle\sigma\otimes\sigma\rangle=0$ and he is correct half the time. Average $3/4$.

---

## Chapter 8

**8.1.** Opening $0$ requires $q=r^c$. Alice can copy $q$ into the announced $r^c$ without a further measurement. The remaining freedom is: the commit outcome $k=q$, and the opening-$1$ outcome $l$. That is four outcomes.

**8.6.** On $|\phi^+\rangle$, $P(r^A=r^B)=\frac{1+\cos\theta}{2}=\cos^2(\theta/2)$ for relative angle $\theta$.

**8.8.** Each correlator is a cosine of a difference of axes:

$$
\begin{align*}
\langle\sigma_{2\theta}\otimes\sigma_{2\theta-\varphi}\rangle&=\cos\varphi,\\
\langle\sigma_{2\theta}\otimes\sigma_{4\theta-\varphi}\rangle&=\cos(2\theta-\varphi),\\
\langle\sigma_z\otimes\sigma_{2\theta-\varphi}\rangle&=\cos(\varphi-2\theta),\\
\langle\sigma_z\otimes\sigma_{4\theta-\varphi}\rangle&=\cos(\varphi-4\theta).
\end{align*}
$$

CHSH combination $+{+}{+}-$ simplifies (use evenness of cosine) to (9).

**8.9.** $\partial I/\partial\varphi=2\sin(2\theta-\varphi)-\sin(4\theta-\varphi)-\sin\varphi=0$. The sum-to-product identity $\sin(4\theta-\varphi)+\sin\varphi=2\sin(2\theta)\cos(2\theta-\varphi)$ gives $\tan(2\theta-\varphi)=\sin(2\theta)$ when $\cos(2\theta-\varphi)\ne 0$. The paper’s arccos expression is a closed form for a solution branch. Check: $\theta=\pi/4$ yields $\varphi_{\mathrm{opt}}=\pi/4$ and $I=2\sqrt{2}$. At that point $P_{\mathrm{cont}}=\cos^2(\pi/8)$.

**8.11.** As $\theta\to 0$, Alice and Bob’s axes coincide, $P_{\mathrm{cont}}\to 1$, and the CHSH combination collapses toward a local value $\le 2$.

---

## Chapter 9

**9.1.** Uniform $n$. For $n<N$, control is $C$ of the *conditional* CHSH on the next use, provided the empirical test passed. For $n=N$, the next use is untested: Alice sets control to $1$ on that branch, giving $\le 1/N$.

**9.7.** Azuma–Hoeffding on $Z_k$ with differences $\le D=4+2\sqrt{2}$ yields (17). Summing the geometric series $\sum_{k=K_0}^{N-1}e^{-k\alpha}$ with $\alpha=\varepsilon^2/(2D^2)$ produces $Q(\varepsilon)$.

**9.8.** $\sin(\pi/8)=\sqrt{2-\sqrt{2}}/2$, so $1/\sin^2(\pi/8)=4/(2-\sqrt{2})=4+2\sqrt{2}$ after rationalizing. Coincidence, not a lemma.

**9.9.** Use one formula for both figure and text. Both choices tend to $2\sqrt{2}$ as $N\to\infty$.

**9.10.** Slack sources: (i) replacing $\Theta$ by $1$ on $\{n\le K\}$; (ii) $C\le 1$ on $\pi_k(\varepsilon)$; (iii) Azuma is not tight for this martingale; (iv) the $1/N$ last-round term.

---

## Chapter 10

**10.3.** Honest PR: $g=r^0\oplus r^1=s^0$ when Bob inputs $s^1=1$. The guess is $s^0$ *if* $q=r^0$. That fails only when $s^0=a=1$ (probability $1/4$). Hence $P_{\mathrm{gain}}=3/4$.

**10.5.** Let $\alpha=P(r^0=0\mid s^0=1)$, $q_y=P(r^1=0\mid s^1=y)$. The expression (21) equals

$$
T=1+2\bigl[P(00\mid s^0=1,s^1=0)+P(10\mid s^0=1,s^1=1)\bigr],
$$

and each joint is at most the corresponding marginals, so

$$
T\le 1+2\bigl[\min(\alpha,q_0)+\min(1-\alpha,q_1)\bigr]\le 1+2\cdot 1=3.
$$

Thus $P_{\mathrm{cont}}=T/4\le 3/4$. Equality: Bob’s box always outputs $0$; Alice opens $0$ using $r^0=0$, and opens $1$ using any $r^0$ (the PR test then holds with probability $1/2$ from Bob’s random $s^1$? Wait—if Bob always outputs $0$: opening $0$ succeeds with probability $1$; opening $1$ succeeds iff $r^0\oplus 0=s^0 s^1=s^1$, i.e. $r^0=s^1$. Alice does not know $s^1$, so she succeeds half the time. Average $P_{\mathrm{cont}}=\frac12(1+\frac12)=\frac34$.)

**10.8.** Probability $1/2$ that $d$ matches the bit she wants to open: original $P_{\mathrm{cont}}$. Probability $1/2$ that it does not: Bob skips the nonlocal check and the token can be opened both ways, success $1$. Mix: $\frac12(P_{\mathrm{cont}}+1)$.

**10.10.** Protocol C' uses only pairs $1,\dots,n-1$ for CHSH: fewer tests, Alice knows which, control cannot fall. Protocol C'' additionally gives box $i$ of pair $k$ the history of all previous $i$-boxes: sequential memory, control cannot fall. C'' is the sequential protocol except that reveal time is free and tests on other pairs are simultaneous. Therefore sequential $P_{\mathrm{cont}}$ upper-bounds the large-office value.
