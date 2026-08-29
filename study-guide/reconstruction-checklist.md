# Reconstruction checklist

Tick only what you have derived yourself. When everything is ticked, go to [11-write-the-paper.md](11-write-the-paper.md).

## Definitions

- [ ] \(P_{\mathrm{cont}}=\frac12(p_0+p_1)\) and \(P_{\mathrm{gain}}\) written in words and symbols
- [ ] Five DI assumptions listed
- [ ] Formula (1) for product measurements
- [ ] “Sending a box” defined operationally
- [ ] Shielding vs relativistic BC: three differences

## Honest physics

- [ ] Measurement table (box 0 / box 1, inputs 0–3)
- [ ] CHSH value \(2\sqrt{2}\) verified with \(\langle\sigma_\alpha\otimes\sigma_\beta\rangle=\cos(\alpha-\beta)\)
- [ ] Equality pairs \((i,i+2\bmod 4)\) verified
- [ ] Commit/reveal rule \(s^c=b+2\), \(s^{\bar c}=b\) matches those pairs for all \(c,b\)

## Protocol

- [ ] Private uniform \(n\in\{1,\dots,N\}\) and why it must be private
- [ ] Indicator \(I(W_k)\) with prefactor 4, and \(\bar I_n\)
- [ ] Abort if \(\bar I_n<I_{\mathrm{th}}\)
- [ ] Coin \(c\), send box \(c\) at \(t^b<t_{n+1}\)
- [ ] \(q=r^c\oplus ab\) at \(t^c\)
- [ ] Reveal \((b,r^c)\) before \(t_{n+1}\)
- [ ] Token check: \(q=r\) or \(q=r\oplus b\)
- [ ] Check measurement at \(t_{n+1}\) with input \(b\) on the kept box
- [ ] Timing constraint: interval long enough for the round trip
- [ ] Honest completeness (ideal and noisy) discussed

## Alice’s security (§4)

- [ ] Display (5) expanded from the protocol
- [ ] NS inequalities written
- [ ] \(P_{\mathrm{gain}}\le 3/4\)
- [ ] Strategy A (deterministic box, guess \(q\))
- [ ] Strategy B (honest EPR, Bob inputs \(0\))

## Bob’s security, asymptotic (§5.1–5.2)

- [ ] Four-outcome POVM reduction
- [ ] Formula (6) for \(p_0,p_1\)
- [ ] Optimization (7) including CHSH constraint and commutators
- [ ] NPA level-2 mentioned as an upper bound
- [ ] Strategy: angles \(2\theta\), \(z\), \(2\theta-\varphi\), \(4\theta-\varphi\); Alice \(3\theta-\varphi\) / \(\theta\)
- [ ] \(P_{\mathrm{cont}}=\cos^2(\theta/2)\)
- [ ] Formula (9) for \(I(\theta,\varphi)\)
- [ ] \(\varphi_{\mathrm{opt}}\) as in (10); check \(\theta=\pi/4\Rightarrow I=2\sqrt{2}\)
- [ ] Fig. 1 reproduced
- [ ] Statement that the strategy saturates the SDP

## Bob’s security, finite \(N\) (§5.3, App. D)

- [ ] Formula (11) with the \(1/N\) last-round term
- [ ] Definition of \(K(\mathbf{w}_{N-1})\)
- [ ] Concavity split at \(K_0=\lceil(N-1)C(I_{\mathrm{th}})\rceil\)
- [ ] Bad set \(\pi_k(\varepsilon)\)
- [ ] Martingale \(Z_k\) and \(D=4+2\sqrt{2}\)
- [ ] Azuma bound (17) and sum \(Q(\varepsilon)\)
- [ ] Final bound (19)
- [ ] Limit \(N\to\infty\) recovers \(C(I_{\mathrm{th}})\)
- [ ] Fig. 3 reproduced; caption consistent with the choice of \(I_{\mathrm{th}}(N)\)

## Appendices

- [ ] App. A protocol, both bounds \(=3/4\), classical saturating strategy for Alice
- [ ] App. B: random \(d\), \(P_{\mathrm{cont}}\to\frac12(P_{\mathrm{cont}}+1)\), short intervals allowed
- [ ] App. C: \(N+1\) pairs, reduction to sequential bound in two relaxations
- [ ] Trade-off table (fixed time vs control vs number of boxes vs PR boxes)

## Writing

- [ ] Abstract contains GHZ history, CHSH result, memory, numbers or equivalent, reveal-time caveat, post-quantum remark
- [ ] No claim of perfect or balanced quantum BC in the main protocol
- [ ] All numbered equations (1)–(24) have a counterpart in your notes
