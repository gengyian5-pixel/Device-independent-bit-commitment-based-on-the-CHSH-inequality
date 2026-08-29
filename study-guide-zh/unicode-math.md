# Unicode 与 LaTeX 数学公式

本学习指南使用 GitHub 风格的数学公式（行内公式为 `$...$`，陈列公式为 `$$...$$`）。它们可在 GitHub、Cursor 的 Markdown 预览以及构建出的 HTML/PDF 中渲染。

## 查看渲染后的数学公式

| 方式 | 命令 / 位置 |
|---|---|
| GitHub / Cursor 预览 | 打开任意 `study-guide-zh/*.md` 文件 |
| HTML（KaTeX） | 运行 `bash ../scripts/build_study_guide.sh`，然后打开 `../study-guide/build/study-guide.html` |
| PDF（XeLaTeX + Unicode 数学字体） | 使用同一脚本；打开 `../study-guide/build/study-guide.pdf` |

XeLaTeX 随 **TeX Live**、**fontspec** 和 **unicode-math** 一同安装。正文字体使用 DejaVu；公式使用 **TeX Gyre DejaVu Math**，因此 PDF 中的希腊字母、运算符和下标都是真正的 Unicode 字形。

## 符号速查表（即使查看原始文本也清晰可见）

手写笔记或使用纯文本编辑器时可采用这些符号。

| 含义 | Unicode | LaTeX |
|---|---|---|
| 圆周率 pi | π | `\pi` |
| theta | θ | `\theta` |
| phi | φ | `\varphi` |
| sigma | σ | `\sigma` |
| rho | ρ | `\rho` |
| psi | ψ | `\psi` |
| alpha | α | `\alpha` |
| epsilon | ε | `\varepsilon` |
| 小于或等于 | ≤ | `\le` |
| 大于或等于 | ≥ | `\ge` |
| 不等于 | ≠ | `\ne` |
| 远小于 | $\ll$ | `\ll` |
| 约等于 | ≈ | `\approx` |
| 同构 / simeq | ≃ | `\simeq` |
| 属于 | ∈ | `\in` |
| 子集 | ⊂ | `\subset` |
| 张量积 | ⊗ | `\otimes` |
| XOR / 模 2 加法 | ⊕ | `\oplus` |
| 乘 | × | `\times` |
| 点乘 | · | `\cdot` |
| 正负 | ± | `\pm` |
| 无穷 | ∞ | `\infty` |
| 平方根 | √ | `\sqrt` |
| 求和 | ∑ | `\sum` |
| 连乘 | ∏ | `\prod` |
| 积分 | ∫ | `\int` |
| 右箭头 | → | `\to` |
| 蕴含 | ⇒ | `\Rightarrow` |
| 左矢 / 右矢括号 | ⟨ ⟩ | `\langle` `\rangle` |
| 实数 | ℝ | `\mathbb{R}` |
| 复数 | ℂ | `\mathbb{C}` |
| 恒等算符 | 𝟙 | `\mathbb{1}` |
| 空集 | $\emptyset$ | `\emptyset` |
| 对所有 | ∀ | `\forall` |
| 存在 | ∃ | `\exists` |
| 约化普朗克常数 hbar | ℏ | `\hbar` |
| 厄米共轭 dagger | † | `\dagger` |
| 圆圈 / 复合 | ∘ | `\circ` |
| 相似 | ∼ | `\sim` |
| 成正比 | ∝ | `\propto` |

论文专用速记：

| 含义 | 近似 Unicode 写法 | LaTeX |
|---|---|---|
| Alice 的控制能力 | P_cont | `$P_{\mathrm{cont}}$` |
| Bob 的信息增益 | P_gain | `$P_{\mathrm{gain}}$` |
| CHSH 值 | I | `$I$` |
| Tsirelson 界 | 2√2 | `$2\sqrt{2}$` |
| GHZ / 中间角 | cos²(π/8) | `$\cos^2(\pi/8)$` |

## 编辑章节后重新构建

```bash
python3 ../scripts/convert_math_delimiters.py *.md   # 如果你输入了 \( ... \)
bash ../scripts/build_study_guide.sh
```
