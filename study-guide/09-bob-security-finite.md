# 9. Bob’s security for finitely many tests

Paper analogue: §5.3 and Appendix D. Goal: if the devices have **arbitrary memory**, Alice’s control is still bounded by something that tends to $C(I_{\mathrm{th}})$ as $N\to\infty$.

This is the Reichardt–Unger–Vazirani-style part of the paper, but much lighter: you only need a martingale on the CHSH indicators, not a full self-testing theorem.

## 9.1 Why i.i.d. is illegal

A dishonest Alice can program:

- a counter: “on use $N+1$, ignore CHSH and output a deterministic commitment”;
- history-dependent measurements: fail CHSH on some paths, compensate on others;
- a strategy whose expected CHSH on round $n+1$ is *not* equal to the empirical $\bar I_n$.

So you cannot plug $\bar I_n$ into $C(\cdot)$ and call it a day. You need: empirical CHSH $\approx$ conditional expected CHSH on the *next* round, except with small probability, uniformly over strategies.

## 9.2 Express $P_{\mathrm{cont}}$ as an average over $n$ and histories

Bob picks $n$ uniformly in $\{1,\dots,N\}$. For $n=N$, use $N+1$ is never CHSH-tested, so Alice can make $C=1$ on that branch. Hence

$$
P_{\mathrm{cont}}=\frac1N\sum_{n=1}^{N-1}\sum_{\mathbf{w}_n}P(\mathbf{w}_n)\,\Theta(\bar I_n-I_{\mathrm{th}})\,C\bigl(\mathbb{E}[I(W_{n+1})\mid\mathbf{w}_n]\bigr)+\frac1N\sum_{\mathbf{w}_N}P(\mathbf{w}_N)\,\Theta(\bar I_N-I_{\mathrm{th}}).
$$

The second sum is $\le 1/N$. This is (11).

**Exercise 9.1.** Derive (11) from the protocol and from the definition of $C(I)$. Identify the unit step $\Theta$ as “Bob did not abort in Phase 1”.

**Exercise 9.2.** Why is the $n=N$ term not $C(I_{\mathrm{th}})/N$? Because Alice is not constrained at all on use $N+1$.

## 9.3 Lift every short history to a length-$(N-1)$ history

For each $\mathbf{w}_n$ with $n\le N-2$, consider compatible extensions $\mathbf{w}_{N-1}$. Rewrite the bound as an average over $\mathbf{w}_{N-1}$ of

$$
\frac1N\sum_{n=1}^{N-1}\Theta(\bar I_n-I_{\mathrm{th}})\,C\bigl(\mathbb{E}[I(W_{n+1})\mid\mathbf{w}_n]\bigr)+\frac1N.
$$

This is (12).

**Exercise 9.3.** Write this change of summation carefully. The point is to have a *single* sample path on which you can mark the last time the empirical CHSH was still above threshold.

## 9.4 The last good time $K$

$$
K(\mathbf{w}_{N-1})=\max\{k\le N-1:\bar I_k(\mathbf{w}_k)\ge I_{\mathrm{th}}\}
$$

(and, if you need a convention, $K=0$ when the set is empty; those histories contribute $0$ through $\Theta$).

Then $\Theta(\bar I_n-I_{\mathrm{th}})=0$ for all $n>K$, so the inner sum over $n$ runs at most up to $K$. Histories that dipped below $I_{\mathrm{th}}$ *before* $K$ only make the true $P_{\mathrm{cont}}$ smaller, so dropping $\Theta$ for $n\le K$ upper-bounds:

$$
P_{\mathrm{cont}}\le\sum_k\sum_{\mathbf{w}:K(\mathbf{w})=k}P(\mathbf{w})\,\frac1N\sum_{n=1}^k C\bigl(\mathbb{E}[I(W_{n+1})\mid\mathbf{w}_n]\bigr)+\frac1N.
$$

This is (14).

**Exercise 9.4.** Produce (14) from (12). The paper’s inequality is because some $n<K$ may have $\Theta=0$.

## 9.5 Split at $K_0=\lceil(N-1)C(I_{\mathrm{th}})\rceil$ and use concavity

$C(I)$ is concave (Fig. 1 is concave; you may take this from the plot, or note that an SDP value as a function of a linear constraint is concave in the constraint). For $k\ge K_0$,

$$
\frac1k\sum_{n=1}^k C(\mathbb{E}_n)\le C\Bigl(\frac1k\sum_{n=1}^k\mathbb{E}[I(W_{n+1})\mid\mathbf{w}_n]\Bigr).
$$

For $k<K_0$, bound $C\le 1$ and then $k/N\le(N-1)C(I_{\mathrm{th}})/N$.

**Exercise 9.5.** This split looks like magic. Its only purpose is: the “small $k$” contribution cannot exceed about $C(I_{\mathrm{th}})$ because there are few such terms, even if Alice sets $C=1$ there. Check the arithmetic of the first sum in (15).

## 9.6 Typicality: empirical CHSH versus conditional expectations

Define the bad set $\pi_k(\varepsilon)$ of $k$-histories with

$$
\bar I_k(\mathbf{w}_k)-\frac1k\sum_{n=1}^k\mathbb{E}[I(W_n)\mid\mathbf{w}_{n-1}]\ge\varepsilon.
$$

On the complement, the argument of $C$ in the concave bound is at least $\bar I_k-\varepsilon\ge I_{\mathrm{th}}-\varepsilon$ (because $K=k$ implies $\bar I_k\ge I_{\mathrm{th}}$), hence $C(\cdots)\le C(I_{\mathrm{th}}-\varepsilon)$ if $C$ is decreasing in a way… **wait**: $C(I)$ is *decreasing* in $I$ (more nonlocality, less control). So an *upper* bound on $C$ needs a *lower* bound on $I$. Yes: on good histories, average conditional CHSH $\ge\bar I_k-\varepsilon\ge I_{\mathrm{th}}-\varepsilon$, so $C\le C(I_{\mathrm{th}}-\varepsilon)$.

On bad histories, bound $C\le 1$.

**Exercise 9.6.** Assemble these into the first two displays of (19). Minimize over $\varepsilon\ge 0$. You should reach

$$
P_{\mathrm{cont}}\le\frac{N-1}N\min_{\varepsilon\ge 0}\Bigl[C(I_{\mathrm{th}}-\varepsilon)+\bigl(1-C(I_{\mathrm{th}}-\varepsilon)\bigr)Q(\varepsilon)\Bigr]+\frac1N,
$$

where $Q(\varepsilon)$ bounds $\sum_{k=K_0}^{N-1}P(\pi_k(\varepsilon))$.

## 9.7 Appendix D: Azuma–Hoeffding

**Exercise 9.7.** Complete Exercise 1.10: $Z_k=k\Delta_k$ is a martingale with bounded differences $D=4+2\sqrt{2}$. Apply Azuma to get

$$
P(\pi_k(\varepsilon))\le\exp\bigl(-k\varepsilon^2/(2D^2)\bigr).
$$

Sum a geometric series from $k=K_0$ to $N-1$:

$$
Q(\varepsilon)=\frac{\exp(-K_0\varepsilon^2/(2D^2))-\exp(-N\varepsilon^2/(2D^2))}{1-\exp(-\varepsilon^2/(2D^2))}.
$$

The paper also notes $D=(1-\cos^2(\pi/8))^{-1}$. **Exercise 9.8.** Check this numerical coincidence: $4+2\sqrt{2}\stackrel{?}{=}1/\sin^2(\pi/8)$. (It is a curiosity, not used later.)

## 9.8 The limit $N\to\infty$

Choose $\varepsilon=\varepsilon(N)$ decaying *slower* than $N^{-1/2}$ (e.g. $N^{-1/3}$). Then $Q(\varepsilon)\to 0$, and the bound tends to $C(I_{\mathrm{th}})$. For $I_{\mathrm{th}}\to 2\sqrt{2}$, this is $\cos^2(\pi/8)$.

For Fig. 3 the paper uses (there is a **published inconsistency** between the figure caption and the main text)

- caption: $I_{\mathrm{th}}=2\sqrt{2}\,(1-1/\sqrt{N})$,
- text: $I_{\mathrm{th}}=2\sqrt{2}-1/\sqrt{N}$.

**Exercise 9.9.** Plot both. They differ at finite $N$ but have the same limit. In your paper, pick one and use it in both the caption and the text. Numerically minimize (19) over $\varepsilon$ as in `scripts/reconstruct_figures.py`.

The Azuma tail is conservative ($D=4+2\sqrt{2}$ is a crude diameter). Expect the bound (19) to sit well above $C(I_{\mathrm{th}})$ until $N$ is huge; overlaying $C(I_{\mathrm{th}})$ on Fig. 3 makes that gap visible. The published Fig. 3 is the numerical min of (19), not an experiment.

**Exercise 9.10.** The paper says the finite-$N$ bound is probably not tight because $Q(\varepsilon)\ne 0$. Do you agree? Where is the slack?

## 9.9 How to write §5.3 without drowning the reader

The published proof is one long chain of inequalities. When you reconstruct it, keep the *narrative* visible:

1. Average over $n$; isolate the untested last-round cheat $1/N$.
2. Look at a full path of length $N-1$; mark last time the test would have passed.
3. Concavity + split small/large $K$.
4. Martingale typicality: $\bar I$ cannot greatly exceed the mean of future-step expectations.
5. Azuma $\Rightarrow Q(\varepsilon)\to 0$.

If a reader remembers only those five bullets, they can rebuild (11)–(19).

## Checkpoint

Write the five-bullet narrative. Reproduce $D=4+2\sqrt{2}$ and the form of (19) without looking. Run `python scripts/reconstruct_figures.py` and confirm Fig. 3 approaches $\cos^2(\pi/8)$.
