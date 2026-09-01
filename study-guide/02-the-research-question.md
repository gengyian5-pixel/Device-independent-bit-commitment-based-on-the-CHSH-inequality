# 2. The research question

This chapter is the paper’s §1. Write your own introduction *after* you can answer the questions below in complete sentences.

## 2.1 What problem is open?

By 2015, device-independent (DI) cryptography based on *CHSH testing of bipartite boxes* was known for:

- DIQKD,
- randomness expansion / amplification,
- self-testing,
- entanglement estimation / quantification.

Two bipartite *distrustful* tasks—bit commitment and coin flipping—had DI protocols, but only from **tripartite GHZ** correlations (Silman *et al.* 2011; Aharon *et al.* 2014). No CHSH-based DI protocol was known.

**Exercise 2.1.** Distrustful cryptography means the parties do not trust each other and may have conflicting goals. Why is “certify nonlocality” harder here than in QKD? Write the obstruction in one sentence. (Hint: in QKD, Alice and Bob cooperate against Eve. Here Alice may be Eve.)

**Exercise 2.2.** In the GHZ protocol, Bob uses *the same measurements* both to test nonlocality and to check the revealed bit. Why is that possible? Why does the same trick fail for CHSH?

## 2.2 The thesis you must prove

Formulate the paper as a single claim:

> There exists a DI bit-commitment protocol whose only Bell test is sequential CHSH on a pair of boxes, which in the limit of infinitely many tests achieves the same cheating probabilities as the GHZ protocol of Silman *et al.*, even when the devices have long-term quantum memory.

Add the two caveats the paper is honest about:

1. The reveal time is *fixed* by the protocol (so strictly speaking this is a BC-like primitive, not BC with Alice-chosen reveal time).
2. For noisy devices the honest abort probability in the reveal phase is nonzero—true of any practical BC, DI or not.

**Exercise 2.3.** Why is a fixed reveal time still useful? Give the coin-flipping reduction in two sentences.

## 2.3 The one idea that makes CHSH work

GHZ gives *certainty*. CHSH gives *statistics*. So Bob cannot test the box in one shot and simultaneously get a deterministic check of Alice’s bit.

The replacement idea:

> Hide from the devices *which round* is the commit/reveal round.

Concretely:

- Bob chooses a private uniform $n\in\{1,\dots,N\}$.
- He CHSH-tests for $n$ rounds at publicly scheduled times $t_1,\dots,t_n$.
- He sends Alice one box, they commit/reveal, and he measures the kept box at the *next* scheduled time $t_{n+1}$.

Unless $n=N$, the kept box sees “another measurement at the usual time”, not “the verification of a commitment”.

**Exercise 2.4.** Suppose $n$ is *public*, or Alice’s boxes contain a counter that is allowed to change behaviour on use number $N+1$. Describe a perfect cheating strategy for Alice. This is why the $1/N$ term appears in the finite-$N$ bound.

**Exercise 2.5.** Suppose the time gaps $t_{i+1}-t_i$ are shorter than (send box to Alice) + (Alice measures) + (Alice’s classical message returns) + (Bob measures). What can Alice’s remaining box infer, and how does she cheat?

## 2.4 What “same security as GHZ” means numerically

Silman *et al.* 2011:

$$
P_{\mathrm{cont}}=\cos^2(\pi/8)\simeq 0.8536,\qquad P_{\mathrm{gain}}=3/4.
$$

You will re-obtain both numbers. Note that this protocol is *not* balanced ($0.85\neq 0.75$), and is therefore *not* trying to meet the Chailloux–Kerenidis $0.739$ bound, which applies only to balanced BC.

**Exercise 2.6.** Is $P_{\mathrm{cont}}=\cos^2(\pi/8)$ an accident of GHZ geometry, or a Tsirelson-type angle? After chapter 8 you should see it is the correlation probability of two equatorial observables $\pi/4$ apart on $|\phi^+\rangle$.

## 2.5 Post-quantum subplot

The paper also asks: if honest *and* dishonest parties are limited only by no-signalling, can one do better? Appendix A uses a PR box, restores pseudo-telepathy, and gets a *balanced* protocol with $P_{\mathrm{cont}}=P_{\mathrm{gain}}=3/4$, which is better for Alice’s security *and* for balance, though still not the CK lower bound (that bound is quantum-specific).

**Exercise 2.7.** Why might one have expected *worse* security in a PR-box world? Why might one have expected *better*? The paper’s answer is “on balance, better”. You should be able to say that in the introduction in three sentences.

## 2.6 Outline you should impose on the paper

When you write §1, end with this roadmap (the paper’s):

- §2 definitions (BC + DI assumptions)
- §3 protocol
- §4 Alice’s security ($P_{\mathrm{gain}}$)
- §5 Bob’s security ($P_{\mathrm{cont}}$, asymptotic then finite)
- §6 summary
- App. A PR-box
- App. B free reveal time, worse $P_{\mathrm{cont}}$
- App. C large-office, free reveal time, same $P_{\mathrm{cont}}$
- App. D Azuma–Hoeffding lemma

## Checkpoint

Write, in at most 250 words, an abstract. Then compare with the published abstract. Yours should mention: GHZ-only previous work, CHSH protocol, memory, same numbers, fixed reveal time, post-quantum appendix.
