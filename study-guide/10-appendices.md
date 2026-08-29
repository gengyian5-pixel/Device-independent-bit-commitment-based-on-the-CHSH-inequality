# 10. Appendices A–C (and what to do with D)

Appendix D was already the lemma for chapter 9. Here you reconstruct the three *protocol* variants.

## 10.1 Appendix A — PR-box bit commitment

### Why this appendix exists

Two opposing intuitions:

- Dishonest parties get stronger correlations \(\Rightarrow\) worse security.
- Honest parties get pseudo-telepathy back \(\Rightarrow\) GHZ-style “test and check with the same measurement”, no sequential CHSH, possibly better security.

You will find \(P_{\mathrm{gain}}\le 3/4\) (unchanged, still NS) and \(P_{\mathrm{cont}}\le 3/4\) (improved, and now balanced).

Do **not** assume the PR box is trusted hardware (that would be Buhrman *et al.* 2006, which gets *perfect* BC if dishonest parties cannot tamper). Here Alice prepares any no-signalling box.

### Protocol (write it yourself)

Alice holds box 0, Bob box 1. Two inputs, two outputs. Honest PR correlation \(r^0\oplus r^1=s^0 s^1\).

1. **Commit.** Alice inputs \(s^0=b\), samples pad \(a\), sends \(q=r^0\oplus a s^0\).
2. **Reveal.** Alice sends \(s^0,r^0\). Bob checks the token (\(q=r^0\) or \(q=r^0\oplus s^0\)). Then he picks uniform \(s^1\) and checks the PR equation. Abort if either fails.

**Exercise 10.1.** Why is sequential testing gone? Because the PR equation is *certain*. One random \(s^1\) both tests the box and tests consistency of the revealed \((s^0,r^0)\). That is the GHZ trick, restored.

### Alice’s security

**Exercise 10.2.** Repeat §4 with inputs \(\{0,1\}\) instead of \(\{2,3\}\). Same NS bound \(P_{\mathrm{gain}}\le 3/4\).

**Exercise 10.3.** Saturating strategy: assume \(q=r^0\), input \(s^1=1\), guess \(g=r^0\oplus r^1\). Check the three cases \((s^0,a)=(0,\ast),(1,0),(1,1)\). You should get exactly \(3/4\).

### Bob’s security

Alice can prepare any NS box, possibly after deciding \(q\) (she sends \(q\) without receiving anything). Relabelling \(q\to q\oplus 1\), \(r^0\to r^0\oplus 1\) is a symmetry, so set \(q=0\).

**Exercise 10.4.** If she opens \(0\), she must send \(r^0=0\). Bob then checks \(r^1=0\) for random \(s^1\). Success probability \(\frac12[P(r^1=0\mid s^1=0)+P(r^1=0\mid s^1=1)]\).

If she opens \(1\), both values of \(r^0\) are allowed; Bob checks the PR equation. Write that probability, add the two openings with weight \(1/2\), and obtain the paper’s (21).

**Exercise 10.5.** Using only NS and positivity, prove (21) \(\le 3/4\). Then give the saturating strategy: Bob’s box is classical, \(P(r^1=0\mid s^1)=1\) for both \(s^1\).

### How to discuss this in §6 / App. A

The “supra-quantum structure allows for greater security” claim is: \(P_{\mathrm{cont}}\) dropped from \(0.85\) to \(0.75\), the protocol is balanced, and one no longer needs \(N\to\infty\). \(P_{\mathrm{gain}}\) did not get worse.

---

## 10.2 Appendix B — free reveal time, worse \(P_{\mathrm{cont}}\)

### The modification

Bob still CHSH-tests \(n\) rounds, still sends box \(c\). **But** at time \(t_{n+1}\) he *already* inputs a random bit \(d\) into the kept box, *before* Alice has revealed (in fact, he can do this even before she has committed, as long as it is at \(t_{n+1}\)). Alice may reveal at any later time. Bob’s equality check is performed **only if** \(d\) happens to equal the revealed \(b\).

**Exercise 10.6.** Write the three phases with coins \(c,d\). Check that \(t_{i+1}-t_i\) no longer needs to contain Alice’s round-trip: Bob measures the kept box on a clock, independently of Alice. Intervals may be arbitrarily short.

### Security

**Exercise 10.7.** Alice’s security is unchanged (\(P_{\mathrm{gain}}\)).

**Exercise 10.8.** For Bob’s security: with probability \(1/2\), \(d\neq b\) and Bob skips the last test, so he accepts any opening that merely satisfies the *classical* token check. A dishonest Alice can then open both bits (the token \(q=r\oplus ab\) is designed to be openable both ways). With probability \(1/2\), \(d=b\) and the situation is the original protocol. Conclude

\[
P_{\mathrm{cont}}\;\longmapsto\;\frac12\bigl(P_{\mathrm{cont}}+1\bigr).
\]

Asymptotically this is \(\frac12(\cos^2(\pi/8)+1)\simeq 0.927\). State this number in your notes; the paper leaves it in functional form.

---

## 10.3 Appendix C — large office: free reveal time, same \(P_{\mathrm{cont}}\)

### Resources

\(N+1\) *pairs* of boxes, pairwise isolated from each other (not only the two boxes of a pair, but different pairs as well). Impractical; it is an existence argument.

### Protocol (write it yourself)

1. Bob picks private \(n\in\{1,\dots,N+1\}\) and coin \(c\), sends box \(c\) of pair \(n\).
2. Alice commits as usual on that box.
3. Alice reveals at a time of her choosing.
4. Bob, *in parallel*, CHSH-tests **all other pairs** and, simultaneously, measures the kept box of pair \(n\) with input \(b\). Abort on equality failure or if the CHSH average over the \(N\) tested pairs is below \(I_{\mathrm{th}}\).

**Exercise 10.9.** Why does free reveal time not let the kept box “know” it is special? Because the CHSH tests are on *other* pairs, and the check measurement on pair \(n\) is simultaneous with those tests—no extra delayed measurement on a box that already saw \(n\) CHSH rounds.

### Reduction to the sequential bound

You need not re-prove Azuma. Argue by two relaxations, each of which can only *help* Alice:

1. Estimate CHSH using only pairs \(1,\dots,n-1\) (Alice knows the numbering). Worse for Bob, so \(P_{\mathrm{cont}}\) does not decrease.
2. Give every box in pair \(k\) full memory of all previous same-side boxes. This recreates a sequential memory process. Worse for Bob again.

Then \(P_{\mathrm{cont}}\) is at most that of the original sequential protocol. Timing issues disappear because tests are simultaneous.

**Exercise 10.10.** Write this comparison argument as three paragraphs. It is the entire App. C security proof.

---

## 10.4 What *not* to put in the appendices

- Do not redo §4 in App. B/C beyond one sentence (“unchanged”).
- Do not derive a new finite-\(N\) rate for App. C; the paper explicitly refuses to.
- Do not claim App. B intervals can be short *and* \(P_{\mathrm{cont}}\) stays \(\cos^2(\pi/8)\). That is App. C’s job.

## Checkpoint

State the three appendix trade-offs in a table:

| Variant | Reveal time | Extra resources | \(P_{\mathrm{gain}}\) | \(P_{\mathrm{cont}}\) |
|---|---|---|---|---|
| Main protocol | fixed | 1 pair, sequential | \(3/4\) | \(C(I_{\mathrm{th}})+o(1)\) |
| App. A | free (single shot) | PR box | \(3/4\) | \(3/4\) |
| App. B | free | 1 pair | \(3/4\) | \(\frac12(C+1)\) |
| App. C | free | \(N+1\) pairs in parallel | \(3/4\) | \(\le\) sequential bound |
