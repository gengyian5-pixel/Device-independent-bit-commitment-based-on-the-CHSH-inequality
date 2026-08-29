# 4. Device-independence

Paper analogue: §2.2. Your security proofs are only as strong as this model. Write it *before* the protocol, exactly as the paper does.

## 4.1 The five assumptions

Reproduce these in your own words, then freeze them.

1. **Boxes.** Each device is a black box: classical input $s$, classical output $r$. An input always produces an output (no losses).
2. **Quantum theory.** Honest *and* dishonest parties are limited by QM. (Appendix A relaxes this to no-signalling only.)
3. **No communication between boxes, on demand.** The parties can prevent the two boxes from talking to each other when they choose. This can be shielding, not spacelike separation.
4. **Private randomness.** Each party has a trusted RNG for the protocol’s random choices ($n$, inputs, coins, Alice’s pad $a$).
5. **Honest lab leakage.** Nothing leaks out of an honest party’s laboratory.

**Exercise 4.1.** Which of these is used in Alice’s security (§4) but not in Bob’s, and vice versa? Make a table. Example: Alice does *not* test CHSH, so Bob’s cheating strategy is an entangled ancilla plus a guess from $q$; assumption 3 between Alice’s box and Bob’s ancilla is *not* imposed after he sent her the box.

**Exercise 4.2.** Losses are excluded. What would a dishonest party do if a box were allowed to output “no-click”? (You do not need a full loss-tolerant analysis; you need to know why the paper assumes no losses.)

## 4.2 The only constraint on honest boxes

If an honest party holds both boxes and isolates them,

$$
P(r^0,r^1\mid s^0,s^1)=\operatorname{Tr}\bigl(\rho\,\Pi_{r^0|s^0}^0\otimes\Pi_{r^1|s^1}^1\bigr).
$$

A dishonest party chooses $\rho$ and the POVMs. The boxes may depend on time, location, past inputs/outputs, and any stored quantum memory.

**Exercise 4.3.** Write the *memory* generalization: the POVM at step $k$ may depend on $(s_1,r_1,\dots,s_{k-1},r_{k-1})$. This is the setting of Reichardt–Unger–Vazirani, and it is why sequential CHSH testing plus Azuma is needed rather than i.i.d. Chernoff.

## 4.3 What “sending a box” means

The paper is explicit: nobody posts a laboratory apparatus in the mail.

**Exercise 4.4.** Write the operational meaning: a quantum channel carries a system such that, in an honest run, the state and the POVM elements that used to describe Alice’s box now describe Bob’s box (or vice versa). Dishonestly, the sender may send anything, including a system entangled with an ancilla they keep.

This is why Bob, when cheating, can keep an ancilla entangled with the box he sends Alice.

## 4.4 Not relativistic bit commitment

Relativistic BC (Kent) gives *perfect* commitment using spacelike separation and (at least) two remote secure labs for one party.

**Exercise 4.5.** List three differences with this protocol:

- number of labs per party;
- whether measurements must be spacelike related;
- whether the no-communication assumption is implemented by relativity or by shielding.

Include this comparison in §2.2 of your write-up. The published NJP text emphasizes shielding; the arXiv text is slightly shorter on this point. Follow NJP.

## 4.5 What DI does *not* protect against

DI does not remove:

- a leaky honest lab,
- a dishonest RNG,
- communication between boxes that the parties failed to prevent,
- the need for a quantum channel.

It *does* remove: known Hilbert-space dimension, promised observables, promised state, calibration of detectors (except losses, which are simply forbidden here).

## Checkpoint

Recite the five assumptions. Explain “sending a box” in one sentence. Explain why shielding is enough for assumption 3 even though many measurements in the protocol are *not* spacelike related.
