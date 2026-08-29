# Device-independent bit commitment based on the CHSH inequality

Study materials for reconstructing Aharon, Massar, Pironio, and Silman,
*New J. Phys.* **18**, 025014 (2016), [doi:10.1088/1367-2630/18/2/025014](https://doi.org/10.1088/1367-2630/18/2/025014),
[arXiv:1511.06283](https://arxiv.org/abs/1511.06283).

## Start here

**No quantum mechanics?** Read the plain-language path first:

- English: [`study-guide/00-no-quantum.md`](study-guide/00-no-quantum.md)
- 中文（详细零基础教材）：[`study-guide/beginner/README.md`](study-guide/beginner/README.md)
- 中文电子书：[HTML](study-guide/build/beginner-zh.html) · [PDF](study-guide/build/beginner-zh.pdf)

Then read [`study-guide/00-how-to-use.md`](study-guide/00-how-to-use.md) and work through the numbered chapters. Chapter 1 also has a Chinese translation: [`study-guide/01-prerequisites.zh.md`](study-guide/01-prerequisites.zh.md).

The guide is a reconstruction workbook, not a paraphrase of the paper. Each chapter tells you **what to derive**, **why it is needed**, and **how to check yourself**. Worked solutions live in [`study-guide/solutions.md`](study-guide/solutions.md); use them only after you have attempted the exercises. An equation-by-equation index is in [`study-guide/equation-map.md`](study-guide/equation-map.md).

## How to see the math

Chapters use GitHub-style math (`$...$` inline, `$$...$$` display). That renders in GitHub and in Cursor’s markdown preview.

To get a typeset copy with Unicode math fonts (XeLaTeX + TeX Gyre DejaVu Math), follow the numbered steps in [`study-guide/how-to-rebuild.md`](study-guide/how-to-rebuild.md). The short version is:

```bash
bash scripts/build_study_guide.sh
bash scripts/build_beginner_zh.sh
```

Then open:

- [`study-guide/build/study-guide.html`](study-guide/build/study-guide.html) — KaTeX in the browser
- [`study-guide/build/study-guide.pdf`](study-guide/build/study-guide.pdf) — printable PDF

A Unicode symbol card (π, ≤, ⊕, ⊗, …) is in [`study-guide/unicode-math.md`](study-guide/unicode-math.md).

## Target numbers (so you know what you are aiming at)

In the infinite-test limit the protocol matches the GHZ-based protocol of Silman *et al.*, PRL **106**, 220501 (2011):

| Quantity | Symbol | Value |
|---|---|---|
| Alice’s control (cheating probability) | $P_{\mathrm{cont}}$ | $\cos^2(\pi/8)\simeq 0.8536$ |
| Bob’s information gain | $P_{\mathrm{gain}}$ | $3/4 = 0.75$ |

The price is that Alice cannot choose the reveal time freely. Appendices B and C of the paper remove that restriction in two different ways.

## Repository layout

```
study-guide/          reconstruction workbook
  00-no-quantum.md     start here with no QM (English)
  beginner/            白话零基础（中文，不需要量子力学）
  ...
  unicode-math.md
  build/
    study-guide.html
    study-guide.pdf
scripts/
  reconstruct_figures.py
  convert_math_delimiters.py
  build_study_guide.sh
```
