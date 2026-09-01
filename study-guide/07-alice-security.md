# 7. Alice’s security (bound on Bob’s information gain)

Paper analogue: §4. This is the easier proof. It uses **only no-signalling**, not Tsirelson’s bound, not CHSH testing. That is why it survives unchanged in Appendix A (PR boxes) and in Appendices B–C.

Convention in this chapter: drop the subscript $n+1$. Alice holds box $c$ and inputs $s^c\in\{2,3\}$. Bob does not hold a “CHSH partner” he can trust; he may have kept an ancilla.

## 7.1 Bob’s most general cheat

Alice is honest: she picks $b,a$ uniformly, inputs $s^c=b+2$, sends $q=r^c\oplus ab$.

Bob prepared the box entangled with an ancilla. After seeing $q$, he measures the ancilla with a two-outcome measurement that may depend on $q$.

Notation:

- $m\in\{0,1\}$: which measurement he performs; he will set $m=q$.
- $g\in\{0,1\}$: his guess for $s^c$ (equivalently for $b=s^c-2$).

The joint law $P(r^c,g\mid s^c,m)$ may depend on all four arguments because of entanglement.

**Exercise 7.1.** Write $P_{\mathrm{gain}}$ as an average over $a,b,r^c$ of the probability that $g=b$. You should obtain the first line of the paper’s (5):

$$
P_{\mathrm{gain}}=\max_{\mathcal{S}}\sum_{r^c,b,a}P(r^c\mid s^c=b+2)\,P\bigl(g=b\mid r^c,s^c=b+2,m=r^c\oplus ab\bigr),
$$

and then, using $P(a,b)=1/4$, the second line with a factor $1/4$ and a sum over $r^c,b$ only.

**Exercise 7.2.** Rewrite each term as a joint probability $P(r^c,g=\cdots\mid s^c,m=\cdots)$. Expand the sum over $r^c,b\in\{0,1\}$. You should find only six types of terms, which the paper groups as

$$
\frac14\max\bigl[2P(0,0\mid 2,0)+2P(1,0\mid 2,1)+P(0,1\mid 3,0)+P(1,1\mid 3,1)+P(0,1\mid 3,1)+P(1,1\mid 3,0)\bigr],
$$

where $P(r,g\mid s,m)$ is abbreviated $P(r,g\mid s,m)$.

(The published algebra is easy to scramble. Do it on paper with a $2\times 2\times 2$ table of $(b,r,a)$.)

## 7.2 No-signalling and normalization

Outputs of Alice’s box cannot depend on Bob’s later choice of $m$, and Bob’s guess $g$ cannot depend on Alice’s input $s^c$ if he does not measure a system that she still holds—wait: they *are* entangled, so $P(r,g\mid s,m)$ *can* depend on both. The NS constraints are the *marginals*:

$$
\sum_g P(r,g\mid s,m)=P(r\mid s)\qquad\text{(independent of $m$)},
$$

$$
\sum_r P(r,g\mid s,m)=P(g\mid m)\qquad\text{(independent of $s$)}.
$$

**Exercise 7.3.** Using NS and positivity, prove

$$
P(0,0\mid 2,0)+P(1,0\mid 2,1)\le 1
$$

and

$$
P(m,0\mid 2,m)+P(0,1\mid 3,m)+P(1,1\mid 3,m)\le 1
$$

(the paper’s form; equivalently a bound on the remaining four terms). Conclude $P_{\mathrm{gain}}\le 3/4$.

Hint for the first inequality: discard the restriction on $g$ and use Alice’s no-signalling marginal,

$$
P(0,0\mid2,0)\le P(r=0\mid s=2),\qquad
P(1,0\mid2,1)\le P(r=1\mid s=2).
$$

The two right-hand sides sum to $1$. For the second family, use Bob’s no-signalling marginal:

$$
P(m,0\mid2,m)\le P(g=0\mid m),\qquad
P(0,1\mid3,m)+P(1,1\mid3,m)=P(g=1\mid m).
$$

Their sum is at most $1$. Apply this once for $m=0$ and once for $m=1$, then regroup the six terms in (5). See [solutions.md](solutions.md) §7 if stuck after 20 minutes.

## 7.3 Saturating strategies (you must exhibit one)

The bound is useless for the paper unless it is tight: otherwise you have not “matched Silman *et al.*”.

### Strategy A (device-independent, classical box)

Prepare Alice’s box so that $r^c=s^c-2$ deterministically (a classical box: output equals “the committed bit”). Guess $b=q$.

**Exercise 7.4.** Show that $q=r^c$ iff $ab=0$, which has probability $3/4$. When $q=r^c$, $q=b$. When $ab=1$, $q=b\oplus 1$. Thus $P_{\mathrm{gain}}=3/4$.

### Strategy B (device-dependent, honest boxes)

Prepare the honest EPR boxes. Bob keeps box $\bar c$, inputs $0$. Observe that honest settings $s^{\bar c}=0$ and $s^c=2$ are the *same* observable. Treat $q$ as Alice’s output. If $r^{\bar c}=q$, guess she input $2$; else guess $3$.

**Exercise 7.5.** Show: if Alice input $2$ ($b=0$), Bob is always correct (ideal equality, and $q=r^c$). If Alice input $3$, Bob’s observable is orthogonal (in the $zx$-plane, $\pi/2$ from Alice’s), so the guess is right with probability $1/2$. Average: $3/4$.

**Exercise 7.6.** Why include Strategy B in the paper at all, if A already saturates? Because it shows that even a Bob who follows the honest *state* preparation, and only cheats in the guess, already reaches the DI optimum. Security is not coming from “Bob cannot hold an EPR pair”.

## 7.4 What this section does *not* use

- The value of $I_{\mathrm{th}}$.
- The number of tests $N$.
- Quantum theory beyond NS (Strategy A is classical).

So Alice’s security is the robust half of the paper. All the heavy machinery is Bob’s security.

## Checkpoint

Prove $P_{\mathrm{gain}}\le 3/4$ on a whiteboard, then give Strategy A in three sentences. If you cannot expand (5) without the paper, redo Exercise 7.2.
