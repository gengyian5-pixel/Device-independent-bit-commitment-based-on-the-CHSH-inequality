# 0. How to use this guide

## What “build the paper yourself” means

The finished paper is a *report* of a finished argument. This guide is the argument in the order you should *discover* it. If you complete every checkpoint, you will have:

1. The cryptographic definitions and the DI (device-independent) threat model.
2. An honest physical implementation (EPR pairs + four measurement settings per box).
3. The three-phase protocol, including *why* the timing and the private random \(n\) are there.
4. A no-signalling proof that \(P_{\mathrm{gain}}\le 3/4\), with an explicit saturating strategy.
5. An SDP formulation of Alice’s control at a fixed CHSH value \(I\), plus an explicit two-qubit strategy that saturates it at \(P_{\mathrm{cont}}=\cos^2(\theta/2)\).
6. A martingale / Azuma–Hoeffding finite-\(N\) bound that recovers the same number as \(N\to\infty\).
7. The PR-box (post-quantum) protocol and the two “free reveal time” variants.

You can then write the paper from your notes using [11-write-the-paper.md](11-write-the-paper.md).

## Suggested working method

- Keep a notebook with numbered lemmas of *your* making. Do not copy the paper’s numbering until the write-up stage.
- After each chapter, close the guide and try to restate the chapter’s claim in one paragraph without looking.
- Only then open [solutions.md](solutions.md) for that chapter.
- Use the [reconstruction-checklist.md](reconstruction-checklist.md) as a “paper completeness” test before you start writing.

## Recommended order (do not skip)

| Order | Chapter | Paper analogue | Output of the chapter |
|---|---|---|---|
| 1 | [01 Prerequisites](01-prerequisites.md) | implicit | CHSH, Tsirelson, PR boxes, POVMs, martingales |
| 2 | [02 Research question](02-the-research-question.md) | §1 | one-sentence thesis of the paper |
| 3 | [03 Bit commitment](03-bit-commitment.md) | §2.1 | \(P_{\mathrm{cont}}\), \(P_{\mathrm{gain}}\), balance |
| 4 | [04 Device-independence](04-device-independence.md) | §2.2 | the five assumptions and what “sending a box” means |
| 5 | [05 Honest resources](05-honest-resources.md) | §3 intro | measurement table and both families of correlations |
| 6 | [06 Protocol](06-protocol.md) | §3 | the protocol, timing constraints, abort conditions |
| 7 | [07 Alice’s security](07-alice-security.md) | §4 | \(P_{\mathrm{gain}}\le 3/4\) |
| 8 | [08 Bob’s security, \(N=\infty\)](08-bob-security-asymptotic.md) | §5.1–5.2 | \(C(I)\) and the optimal cheating strategy |
| 9 | [09 Bob’s security, finite \(N\)](09-bob-security-finite.md) | §5.3, App. D | the bound (19) |
| 10 | [10 Appendices](10-appendices.md) | Apps. A–C | PR-box protocol; free reveal time |
| 11 | [11 Write the paper](11-write-the-paper.md) | whole | section-by-section writing plan |

## What you should *not* do

- Do not start by optimizing Alice’s four-outcome POVM. First understand why a single two-outcome measurement already saturates the bound.
- Do not treat the random index \(n\) as a technicality. If Bob does not hide \(n\), Alice cheats perfectly.
- Do not confuse “CHSH testing” with “the commit/reveal measurements”. The whole security idea is that the *kept* box cannot tell them apart.

## Notation you should adopt from the start

Fix this now; the paper’s later sections become unreadable if you improvise.

- Two boxes, labelled \(i\in\{0,1\}\).
- Four inputs \(s\in\{0,1,2,3\}\), two outputs \(r\in\{0,1\}\).
- \(k\)-th use of box \(i\): random variables \(S^i_k\), \(R^i_k\); realizations \(s^i_k\), \(r^i_k\).
- \(W_k=\{S^0_k,S^1_k,R^0_k,R^1_k\}\), history \(\mathbf{W}_k=\{W_1,\dots,W_k\}\).
- \(\sigma_\theta=\cos\theta\,\sigma_z+\sin\theta\,\sigma_x\).
- \(|0\rangle,|1\rangle\) are the \(\pm 1\) eigenstates of \(\sigma_z\).
- Alice’s committed bit \(b\); token bit \(q\); one-time-pad bit \(a\).
- Coin \(c\in\{0,1\}\) chooses which box Alice receives; \(\bar c=1-c\) is the box Bob keeps.
