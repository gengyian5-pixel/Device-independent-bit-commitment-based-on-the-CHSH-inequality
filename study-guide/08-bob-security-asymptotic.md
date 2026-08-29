# 8. Bob’s security in the asymptotic limit

Paper analogue: §5.1–5.2. This is the technical core. Goal: a function $C(I)$ such that if the boxes at the commit/reveal step are known to satisfy $\mathbb{E}[I]\ge I_{\mathrm{th}}$, then $P_{\mathrm{cont}}\le C(I_{\mathrm{th}})$, with equality achieved by an explicit strategy.

Chapter 9 reduces the finite-$N$ memory case to this function.

## 8.1 Reduce Alice’s instruments to one four-outcome POVM

Alice, at commit time, holds box $c$ and possibly an ancilla. A fully general strategy:

1. Commit: a two-outcome measurement producing $q$.
2. Reveal: a measurement that depends on $q$ and on the bit she now wishes to open, producing the announced $r^c$.

**Exercise 8.1.** Argue that if she wants to open $0$, Bob requires $q=r^c$, so the reveal measurement for $b=0$ is redundant: she might as well have set $r^c=q$ already. Therefore, in the reveal phase she only ever needs the two measurements associated with opening $1$. Combine those with the commit measurement into a **single four-outcome POVM** $\{M_{kl}^c\}_{k,l\in\{0,1\}}$ on $\mathcal{H}^c$, with the interpretation:

- she sends $q=k$ at commit;
- if she opens $0$, she announces $r^c=k$;
- if she opens $1$, she announces $r^c=l$.

This is the paper’s w.l.o.g. reduction. Write it carefully; referees look at this paragraph.

**Exercise 8.2.** Alice may know $c$ (an extra degree of freedom in the box can encode it). So $\mathcal{M}^0$ and $\mathcal{M}^1$ may differ. The paper notes that the optimum nevertheless uses the same strategy on both boxes, up to a local rotation of Bob’s observables. A protocol that *always* sends the same box would *increase* $P_{\mathrm{cont}}$ (Bob’s random $c$ is essential). Record this as a remark, not as a lemma you must SDP.

## 8.2 Write $P_{\mathrm{cont}}$ as a sum of four families of probabilities

Bob sends each box with probability $1/2$.

**Opening $b=0$** ($s^c=2$): token check forces $r^c=q=k$. Then Bob inputs $s^{\bar c}=0$ and requires $r^{\bar c}=k$. Success probability

$$
p_0=\frac12\sum_{k,l}\Bigl[P\bigl(r^1=k,\,(k,l)\mid s^1=0,\mathcal{M}^0\bigr)+P\bigl(r^0=k,\,(k,l)\mid s^0=0,\mathcal{M}^1\bigr)\Bigr].
$$

**Opening $b=1$** ($s^c=3$): token check allows any $r^c$ (i.e. $r^c=l$). Bob inputs $s^{\bar c}=1$ and requires $r^{\bar c}=l$. Analogous $p_1$.

Then $P_{\mathrm{cont}}=\frac12(p_0+p_1)$, which is the paper’s (6).

**Exercise 8.3.** Derive (6) from the protocol abort conditions without looking. The factor $1/4$ in (6) is $\frac12\times\frac12$: uniform $c$ and uniform intended $b$.

## 8.3 The optimization problem (7)

Maximize (6) over quantum realizations $\mathcal{Q}=\{\mathcal{H}^c,\rho,\{\Pi_{r|s}^c\},\mathcal{M}^c\}_c$ subject to:

- CHSH of the two boxes $\ge I_{\mathrm{th}}$,
- commutativity between operators on different boxes (tensor product, or commutation on a joint Hilbert space),
- POVM constraints: positivity and completeness for both $\Pi$ and $M$.

The paper’s (7) writes this as a single trace:

$$
P_{\mathrm{cont}}=\frac14\max_{\mathcal{Q}}\operatorname{Tr}\Bigl(\rho\sum_{c,k,l}M_{kl}^c\bigl(\Pi_{k|0}^{\bar c}+\Pi_{l|1}^{\bar c}\bigr)\Bigr).
$$

**Exercise 8.4.** Convince yourself that the operator sandwiched with $\rho$ is exactly the event “Bob’s check passes”, averaged over $c$ and over the two openings.

This problem is *not* a fixed-dimension SDP: $\dim\mathcal{H}$ is unknown. Relax it.

## 8.4 NPA hierarchy: what you actually compute

Apply NPA at **level 2** to (7). You obtain an upper bound $P_{\mathrm{cont}}^{\mathrm{SDP2}}(I_{\mathrm{th}})$.

**Exercise 8.5.** List the operators that enter the level-2 moment matrix: products of up to two projectors among $\{\Pi_{r|s}^c,M_{kl}^c\}$. You do not need to code this to reconstruct the paper, but if you want Fig. 1 independently of the analytic strategy, use a package such as `ncpol2sdpa` (Python) or the original MATLAB+YALMIP+SeDuMi stack cited in the paper.

The paper’s claim: the *analytic* strategy of §5.2 matches the level-2 SDP to $10^{-8}$, hence level 2 has already converged.

## 8.5 The saturating strategy (this you must derive by hand)

Guess the geometry before reading §5.2:

- Use one EPR pair $|\phi^+\rangle$.
- Bob’s two check settings on a given box should be two axes in the $zx$-plane, **not necessarily** $\pi/2$ apart if $I<2\sqrt{2}$.
- Alice, who received the other box, should measure **midway** between Bob’s two axes, so that the angle to *either* check setting is the same. Then $p_0=p_1$.
- One two-outcome measurement is enough (so the four-outcome POVM is overkill at the optimum). She announces that outcome as both $b$ and $r^c$ in the sense of the paper: she sends $b$ and $r^c$ equal to her measurement result.

**Exercise 8.6.** If two equatorial observables differ by an angle $\theta$, show that

$$
P(\text{equal outcomes})=\cos^2(\theta/2)
$$

on $|\phi^+\rangle$. Therefore the strategy yields

$$
P_{\mathrm{cont}}=\cos^2(\theta/2).
$$

At Tsirelson, Alice sits $\pi/4$ from each of two orthogonal axes, so $\theta=\pi/4$ and $P_{\mathrm{cont}}=\cos^2(\pi/8)$. That is the GHZ number, obtained from CHSH geometry.

**Exercise 8.7.** Reproduce the paper’s parameterization:

- Box 0, inputs 0 and 1: $\sigma_{2\theta}$ and $\sigma_z$.
- Box 1, inputs 0 and 1: $\sigma_{2\theta-\varphi}$ and $\sigma_{4\theta-\varphi}$.
- If Alice gets box 0, she measures $\sigma_{3\theta-\varphi}$; if box 1, she measures $\sigma_{\theta}$.

Draw Fig. 2: solid axes = Bob on box 0, dashed = Bob on box 1, dotted = Alice. All in the $zx$-plane. Check that Alice is always midway, with half-angle $\theta$.

**Exercise 8.8.** Using $\langle\sigma_\alpha\otimes\sigma_\beta\rangle=\cos(\alpha-\beta)$, compute the CHSH value of Bob’s four observables (inputs $0,1$ on both boxes):

$$
I=\langle\sigma_{2\theta}\otimes\sigma_{2\theta-\varphi}+\sigma_{2\theta}\otimes\sigma_{4\theta-\varphi}+\sigma_z\otimes\sigma_{2\theta-\varphi}-\sigma_z\otimes\sigma_{4\theta-\varphi}\rangle.
$$

Simplify to the paper’s (9):

$$
I=2\cos(2\theta-\varphi)-\cos(4\theta-\varphi)+\cos\varphi.
$$

**Exercise 8.9.** For fixed $\theta$, maximize $I$ over $\varphi$. Show that a critical point is

$$
\varphi_{\mathrm{opt}}=\arccos\Biggl(2\frac{\cos(2\theta)+\sin^2(2\theta)}{\sqrt{6-2\cos(4\theta)}}\Biggr).
$$

(Differentiate (9), solve $\partial I/\partial\varphi=0$. The arccos form is a particular solution; check it against $\theta=\pi/4$, where you must get $\varphi_{\mathrm{opt}}=\pi/4$ and $I=2\sqrt{2}$.)

**Exercise 8.10.** Eliminate $\varphi$ to obtain a parametric curve $(I(\theta),P_{\mathrm{cont}}(\theta))$ for $\theta\in(0,\pi/2]$. This is Fig. 1. Implement it in `scripts/reconstruct_figures.py`.

Special values:

| $\theta$ | $P_{\mathrm{cont}}$ | $I$ (at $\varphi_{\mathrm{opt}}$) | meaning |
|---|---|---|---|
| $\pi/4$ | $\cos^2(\pi/8)\simeq 0.8536$ | $2\sqrt{2}$ | Tsirelson / GHZ match |
| $\to 0$ | $\to 1$ | $\to$ something $\le 2$ | Alice nearly deterministic; CHSH cannot stay above 2 |

**Exercise 8.11.** Evaluate $I$ at $\theta\to 0$ with $\varphi_{\mathrm{opt}}$. You should see that to drive $P_{\mathrm{cont}}\to 1$ Alice must give up Bell violation, as expected.

## 8.6 How to write §5.1–5.2

Order in the paper (copy this structure):

1. W.l.o.g. four-outcome POVM.
2. Expression (6) for the two openings.
3. SDP (7) and NPA level 2.
4. Explicit strategy, (8)–(10), Fig. 2.
5. Statement that (8)–(10) saturate the SDP, hence Fig. 1 is tight.

Do not reverse 3 and 4: the SDP is the *upper* bound; the strategy is the *lower* bound; together they are the exact quantum value.

## Checkpoint

From memory: (i) why a four-outcome commit POVM is enough; (ii) $P_{\mathrm{cont}}=\cos^2(\theta/2)$; (iii) the measurement table of Exercise 8.7; (iv) why $\cos^2(\pi/8)$ appears.
