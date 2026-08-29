# Unicode and LaTeX math

The study guide uses GitHub-style math (`$...$` inline, `$$...$$` display). That renders on GitHub, in Cursor’s markdown preview, and in the built HTML/PDF.

## View rendered math

| How | Command / place |
|---|---|
| GitHub / Cursor preview | open any `study-guide/*.md` file |
| HTML (KaTeX) | `bash scripts/build_study_guide.sh` then open `study-guide/build/study-guide.html` |
| PDF (XeLaTeX + Unicode math font) | same script; open `study-guide/build/study-guide.pdf` |

XeLaTeX is installed with **TeX Live**, **fontspec**, and **unicode-math**. Body text uses DejaVu; formulae use **TeX Gyre DejaVu Math**, so Greek letters, operators, and subscripts are real Unicode glyphs in the PDF.

## Symbol card (visible even in raw text)

Use these when you write notes by hand or in a plain editor.

| Meaning | Unicode | LaTeX |
|---|---|---|
| pi | π | `\pi` |
| theta | θ | `\theta` |
| phi | φ | `\varphi` |
| sigma | σ | `\sigma` |
| rho | ρ | `\rho` |
| psi | ψ | `\psi` |
| alpha | α | `\alpha` |
| epsilon | ε | `\varepsilon` |
| less-or-equal | ≤ | `\le` |
| greater-or-equal | ≥ | `\ge` |
| not-equal | ≠ | `\ne` |
| much-less | $\ll$ | `\ll` |
| approximately | ≈ | `\approx` |
| isomorphic / simeq | ≃ | `\simeq` |
| element of | ∈ | `\in` |
| subset | ⊂ | `\subset` |
| tensor | ⊗ | `\otimes` |
| XOR / plus-mod-2 | ⊕ | `\oplus` |
| times | × | `\times` |
| cdot | · | `\cdot` |
| plus-minus | ± | `\pm` |
| infinity | ∞ | `\infty` |
| square root | √ | `\sqrt` |
| sum | ∑ | `\sum` |
| product | ∏ | `\prod` |
| integral | ∫ | `\int` |
| right arrow | → | `\to` |
| implies | ⇒ | `\Rightarrow` |
| bra / ket | ⟨ ⟩ | `\langle` `\rangle` |
| real numbers | ℝ | `\mathbb{R}` |
| complex numbers | ℂ | `\mathbb{C}` |
| identity | 𝟙 | `\mathbb{1}` |
| empty set | $\emptyset$ | `\emptyset` |
| for all | ∀ | `\forall` |
| exists | ∃ | `\exists` |
| hbar | ℏ | `\hbar` |
| dagger | † | `\dagger` |
| circ / composition | ∘ | `\circ` |
| similar | ∼ | `\sim` |
| proportional | ∝ | `\propto` |

Paper-specific shortcuts:

| Meaning | Unicode-ish | LaTeX |
|---|---|---|
| Alice’s control | P_cont | `$P_{\mathrm{cont}}$` |
| Bob’s information gain | P_gain | `$P_{\mathrm{gain}}$` |
| CHSH value | I | `$I$` |
| Tsirelson bound | 2√2 | `$2\sqrt{2}$` |
| GHZ / midway angle | cos²(π/8) | `$\cos^2(\pi/8)$` |

## Rebuild after editing chapters

```bash
python3 scripts/convert_math_delimiters.py study-guide/*.md   # if you typed \( ... \)
bash scripts/build_study_guide.sh
```
