# Device-independent bit commitment based on the CHSH inequality

Study materials for reconstructing Aharon, Massar, Pironio, and Silman,
*New J. Phys.* **18**, 025014 (2016), [doi:10.1088/1367-2630/18/2/025014](https://doi.org/10.1088/1367-2630/18/2/025014),
[arXiv:1511.06283](https://arxiv.org/abs/1511.06283).

## Start here

Read [`study-guide/00-how-to-use.md`](study-guide/00-how-to-use.md) and then work through the numbered chapters in order.

The guide is a reconstruction workbook, not a paraphrase of the paper. Each chapter tells you **what to derive**, **why it is needed**, and **how to check yourself**. Worked solutions live in [`study-guide/solutions.md`](study-guide/solutions.md); use them only after you have attempted the exercises. An equation-by-equation index is in [`study-guide/equation-map.md`](study-guide/equation-map.md).

## Target numbers (so you know what you are aiming at)

In the infinite-test limit the protocol matches the GHZ-based protocol of Silman *et al.*, PRL **106**, 220501 (2011):

| Quantity | Symbol | Value |
|---|---|---|
| Alice’s control (cheating probability) | \(P_{\mathrm{cont}}\) | \(\cos^2(\pi/8)\simeq 0.8536\) |
| Bob’s information gain | \(P_{\mathrm{gain}}\) | \(3/4 = 0.75\) |

The price is that Alice cannot choose the reveal time freely. Appendices B and C of the paper remove that restriction in two different ways.

## Repository layout

```
study-guide/          reconstruction workbook
  00-how-to-use.md
  01-prerequisites.md
  02-the-research-question.md
  03-bit-commitment.md
  04-device-independence.md
  05-honest-resources.md
  06-protocol.md
  07-alice-security.md
  08-bob-security-asymptotic.md
  09-bob-security-finite.md
  10-appendices.md
  11-write-the-paper.md
  reconstruction-checklist.md
  solutions.md
scripts/
  reconstruct_figures.py   rebuild Figs. 1 and 3 from the analytic formulae
```
