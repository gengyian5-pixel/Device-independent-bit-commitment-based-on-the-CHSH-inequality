# 3. Bit commitment

Paper analogue: §2.1. This chapter is short on purpose. Get the definitions exact; every later formula is an instance of them.

## 3.1 The primitive

Two remote parties. Alice has a bit \(b\in\{0,1\}\). A protocol has two phases:

1. **Commit.** Alice sends Bob a token (here: a classical bit \(q\)). After this, she should be unable to change \(b\).
2. **Reveal.** Alice sends information that lets Bob output a bit \(\hat b\). He should accept \(\hat b=b\) if both were honest, and he should have learned (almost) nothing about \(b\) before this phase.

Classical BC with unbounded computation is impossible (the commit token is either independent of \(b\), so Alice opens both ways, or it determines \(b\), so Bob reads it). Quantum BC cannot be *perfect* (Lo–Chau, Mayers) but can be *imperfect* (Spekkens–Rudolph).

## 3.2 Cheating probabilities

Assume Alice is equally likely to want to open \(0\) or \(1\) after commit (worst-case / uniform).

- \(p_0\): probability that dishonest Alice, after commit, successfully opens \(0\) (Bob does not abort and outputs \(0\)).
- \(p_1\): likewise for \(1\).
- **Alice’s control**

  \[
  P_{\mathrm{cont}}=\frac12(p_0+p_1).
  \]

- **Bob’s information gain** \(P_{\mathrm{gain}}\): probability that dishonest Bob, using the commit token and his systems, correctly guesses \(b\) *before* reveal.

Perfect BC: \(P_{\mathrm{cont}}=P_{\mathrm{gain}}=1/2\).

**Balanced** BC: \(P_{\mathrm{cont}}=P_{\mathrm{gain}}\). Chailloux–Kerenidis: any balanced *quantum* BC satisfies \(P_{\mathrm{cont}}=P_{\mathrm{gain}}\gtrsim 0.739\), and this is saturable.

**Exercise 3.1.** This paper’s asymptotic numbers are \(0.8536\) and \(0.75\). Is the protocol balanced? Should you mention the \(0.739\) bound in the introduction, and if so, how (as a comparison, not as a target)?

**Exercise 3.2.** \(P_{\mathrm{cont}}\) is *not* “Alice guesses Bob’s measurement”. It is “Alice can *choose* which bit to open after commit, and be accepted”. Keep this distinction when you design her POVM in chapter 8: she may use different openings for \(b=0\) and \(b=1\), and \(P_{\mathrm{cont}}\) averages them.

## 3.3 Completeness versus soundness (honest abort)

Two different abort events appear in §3:

1. Bob aborts in the *random-selection / CHSH-test* phase because \(\bar I_n<I_{\mathrm{th}}\). This can happen even with ideal boxes (statistical fluctuation) or because Alice is cheating. Bob cannot tell which. As \(N\to\infty\) with a gap between \(I_{\mathrm{th}}\) and the honest \(I\), this probability vanishes.
2. Bob aborts in the *reveal* phase because the token \(q\) is inconsistent or the two boxes disagree. With ideal honest boxes this does not happen, once the CHSH test passed. With noise, it happens with positive probability even if Alice is honest.

**Exercise 3.3.** Write two sentences for the paper explaining that (2) is an implementation issue shared by every practical BC protocol, not a DI artefact.

## 3.4 Coin flipping as a consumer of this primitive

A (weak) coin flip can be built from BC: Alice commits a bit \(b_A\); Bob sends a bit \(b_B\); Alice reveals; the coin is \(b_A\oplus b_B\).

**Exercise 3.4.** Why does a *fixed* reveal time not break this reduction? (Bob can send \(b_B\) at a time that is still before the scheduled reveal.)

## Checkpoint

Define \(P_{\mathrm{cont}}\) and \(P_{\mathrm{gain}}\) without looking. State the Lo–Chau/Mayers no-go in one sentence, and Spekkens–Rudolph/Chailloux–Kerenidis in one sentence each.
