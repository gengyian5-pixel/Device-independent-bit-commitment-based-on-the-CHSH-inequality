# Study guide

Reconstruction workbook for Aharon, Massar, Pironio, and Silman,
*Device-independent bit commitment based on the CHSH inequality*,
NJP **18**, 025014 (2016).

Work in this order:

0. [How to use this guide](00-how-to-use.md)
1. [Prerequisites](01-prerequisites.md)
2. [The research question](02-the-research-question.md)
3. [Bit commitment](03-bit-commitment.md)
4. [Device-independence](04-device-independence.md)
5. [Honest resources](05-honest-resources.md)
6. [The protocol](06-protocol.md)
7. [Alice’s security](07-alice-security.md)
8. [Bob’s security (asymptotic)](08-bob-security-asymptotic.md)
9. [Bob’s security (finite \(N\))](09-bob-security-finite.md)
10. [Appendices A–C](10-appendices.md)
11. [Write the paper](11-write-the-paper.md)

Then:

- [Reconstruction checklist](reconstruction-checklist.md)
- [Equation map](equation-map.md)
- [Worked solutions](solutions.md) — after you have tried the exercises

Rebuild Figs. 1 and 3:

```bash
python scripts/reconstruct_figures.py
```

Output goes to `study-guide/figures/`.
