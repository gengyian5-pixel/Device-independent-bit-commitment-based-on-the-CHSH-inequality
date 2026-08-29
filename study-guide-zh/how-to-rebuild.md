# 如何重新构建（分步说明）

“重新构建”是指从 Markdown 章节重新生成**排版后的学习指南**（HTML + PDF），并可选择重新生成**图 1 和图 3**。编辑章节后，或数学公式无法显示时，就需要执行此操作。

共有三类产物：

| 产物 | 命令 | 输出 |
|---|---|---|
| 完整中文版 HTML + PDF | `bash ../scripts/build_study_guide_zh.sh` | `build/study-guide-zh.html`、`build/study-guide-zh.pdf` |
| 中文入门版 HTML + PDF | `bash ../scripts/build_beginner_zh.sh` | `../study-guide/build/beginner-zh.html`、`../study-guide/build/beginner-zh.pdf` |
| 图 1 和图 3 | `python ../scripts/reconstruct_figures.py` | `../study-guide/figures/*.png` |
| 数学定界符修复 | `python ../scripts/convert_math_delimiters.py *.md` | 就地改写 `.md` 文件 |

请按顺序执行以下步骤。只有当正文明确说明某一步可选时，才可跳过。

---

## 步骤 0：在本目录中打开终端

1. 打开终端（在 Cursor 中选择 **Terminal → New Terminal**）。
2. 进入仓库中的 `study-guide-zh/` 目录；它的上一级目录包含 `scripts/` 和 `study-guide/`：

```bash
pwd
ls
```

你应当看到本中文学习指南的 Markdown 文件。

如果你位于其他目录：

```bash
cd /path/to/Device-independent-bit-commitment-based-on-the-CHSH-inequality/study-guide-zh
```

在此云端工作区中，该路径是 `/workspace/study-guide-zh`。

---

## 步骤 1：检查工具是否已安装

运行：

```bash
which pandoc xelatex python3
pandoc --version | head -1
xelatex --version | head -1
python3 --version
ls /usr/share/javascript/katex/katex.min.js
fc-list : family | grep -E 'DejaVu Serif|TeX Gyre DejaVu Math'
```

**“正常”状态应当如下**

- `pandoc` 输出类似 `/usr/bin/pandoc` 的路径和版本号（3.x 即可）。
- `xelatex` 输出一个路径以及 `XeTeX ... (TeX Live ...)`。
- `python3` 为 3.10 或更高版本。
- KaTeX 文件存在。
- Fontconfig 列出 **DejaVu Serif** 和 **TeX Gyre DejaVu Math**。

如果其中任何一项失败，请执行**步骤 2**。如果全部成功，请跳至**步骤 3**。

---

## 步骤 2：安装工具（仅当步骤 1 失败时）

在 Debian/Ubuntu 上：

```bash
sudo apt-get update
sudo apt-get install -y --no-install-recommends \
  pandoc \
  texlive-xetex \
  texlive-latex-recommended \
  texlive-latex-extra \
  texlive-fonts-recommended \
  texlive-science \
  latexmk \
  fonts-dejavu \
  fonts-lmodern \
  fonts-texgyre \
  fonts-texgyre-math \
  libjs-katex \
  fonts-katex
```

如果只需运行绘图脚本：

```bash
python3 -m pip install -r ../scripts/requirements.txt
```

这会安装 `numpy` 和 `matplotlib`。

若要构建中文入门读物，还需安装 CJK 字体和 XeLaTeX 中文支持：

```bash
sudo apt-get install -y fonts-noto-cjk texlive-lang-chinese
```

然后重复**步骤 1**。

---

## 步骤 3：（可选）重新生成图 1 和图 3

如果你修改了解析公式，或者 `../study-guide/figures/` 中缺少 PNG 文件，请执行此步骤。

```bash
python3 ../scripts/reconstruct_figures.py
```

**预期结果**

```
sanity checks passed:
  theta=pi/4 => phi=0.785398, I=2.828427, C=0.853553
  D=4+2√2=6.828427
wrote .../study-guide/figures/fig1_alice_control.png
wrote .../study-guide/figures/fig3_finite_N.png
```

如果健全性检查失败，则说明脚本中的公式已与论文的公式 (8)–(10) 不一致。不要忽略这一问题。

---

## 步骤 4：（可选）修复数学定界符

HTML/PDF 构建器和 GitHub 预览期望使用：

- 行内数学公式：`$P_{\mathrm{cont}}$`
- 陈列数学公式：

```markdown
$$
P_{\mathrm{cont}}=\cos^2(\theta/2)
$$
```

它们无法可靠地渲染 `\( ... \)` / `\[ ... \]`。

如果你（或编辑器）输入了 LaTeX 风格的定界符，请先转换：

```bash
python3 ../scripts/convert_math_delimiters.py *.md
```

该脚本会就地改写这些文件，并跳过围栏代码块（包括 mermaid）。如果文件已经使用 `$...$`，则会输出 `unchanged`。

检查一个文件：

```bash
grep -n '$P_{\\mathrm{cont}}$' 03-bit-commitment.md | head
```

你应当看到以美元符号作为定界符的数学公式，而不是 `\(` `\)`。

---

## 步骤 5：重新构建 HTML 和 PDF（主要步骤）

从 `study-guide-zh/` 目录运行：

```bash
bash ../scripts/build_study_guide_zh.sh
```

**脚本依次执行以下操作**

1. 根据 `scripts/` 的位置确定仓库根目录。
2. 如果 `study-guide/build/` 不存在，则创建它。
3. 按以下顺序连接各章节：`00` … `11`，然后是 `equation-map.md`、`reconstruction-checklist.md`、`unicode-math.md`。（**不**包含 `solutions.md`，这样构建出的读物仍是一本练习册。）
4. 运行 **Pandoc → HTML**，使用 `/usr/share/javascript/katex/` 中的本地 KaTeX 文件，并嵌入 CSS/字体，使 HTML 自包含。
5. 运行 **Pandoc → XeLaTeX → PDF**，其中：
   - 正文字体：DejaVu Serif
   - 数学字体：TeX Gyre DejaVu Math（Unicode：π、≤、⊕、下标等）
6. 输出两个文件的大小。

**预期结果**

```
Writing HTML (KaTeX)...
Writing PDF (XeLaTeX + Unicode math font)...
Wrote:
-rw-r--r-- ... study-guide-zh/build/study-guide-zh.html
-rw-r--r-- ... study-guide-zh/build/study-guide-zh.pdf
```

PDF 步骤需要几秒钟。如果失败，终端会显示 XeLaTeX 错误；请参阅下方的**故障排除**。

确认文件是新生成的：

```bash
ls -lh build/study-guide-zh.html build/study-guide-zh.pdf
```

时间戳应显示为“刚刚”。

---

## 步骤 6：打开重新构建的文件

**HTML（检查数学公式是否已渲染的最快方式）**

```bash
xdg-open build/study-guide-zh.html
```

或者在 Cursor 中：右键单击 `build/study-guide-zh.html` → Open。你应当看到目录和排版后的公式（希腊字母、分数、下标），而不是原始的 `$...$`。

**PDF**

```bash
xdg-open build/study-guide-zh.pdf
```

或者从文件树中打开它。搜索 `P_cont`，或查看第 1 章：CHSH 以及 $\le$、$\otimes$、$\pi$ 应当显示为真正的字形。

**Markdown 预览（此方式无需重新构建）**

在 Cursor 中打开任意 `study-guide-zh/*.md` 文件。GitHub 风格的 `$...$` 数学公式应当在预览中渲染。如果你只能看到美元符号，请使用步骤 5 生成的 HTML/PDF。

---

## 编辑章节后

典型流程：

1. 编辑例如 `study-guide-zh/08-bob-security-asymptotic.md`。
2. 如果你粘贴了 `\( ... \)`，运行步骤 4。
3. 运行步骤 5（`bash ../scripts/build_study_guide_zh.sh`）。
4. 重新加载 HTML 或 PDF（某些查看器会缓存文件；如果 PDF 看起来仍是旧版，请关闭后重新打开）。

除非修改了绘图脚本，否则**无需**执行步骤 3。

---

## 故障排除

| 症状 | 可能的原因 | 解决方法 |
|---|---|---|
| `pandoc: command not found` 或 `xelatex: command not found` | 未安装 TeX/Pandoc | 步骤 2 |
| `katex.min.js: does not exist` | 缺少 KaTeX 软件包 | `sudo apt-get install libjs-katex fonts-katex` |
| `Missing character: There is no … in font DejaVu Serif` | Unicode 符号位于**文本**中，而不是数学环境中 | 将其放入 `$...$`（数学字体）中，或替换为 LaTeX（`\emptyset`、`\ll`） |
| HTML 显示原始 `$P_cont$` | 文件仍使用 `\(` `\)` | 执行步骤 4，然后执行步骤 5 |
| PDF 构建成功，但打开的是旧版本 | 查看器缓存 | 关闭 PDF，然后重新打开 `build/study-guide-zh.pdf` |
| `python3: No module named matplotlib` | 缺少绘图依赖 | `pip install -r ../scripts/requirements.txt` |
| 绘图脚本中的健全性检查失败 | `reconstruct_figures.py` 中的公式与 (8)–(10) 不一致 | 修复前不要重新生成图 |
| 构建缓慢 / XeLaTeX 卡住 | 第一次运行 TeX 时可能会生成格式文件 | 等待；后续运行会更快 |

若要检查 PDF 是否确实包含 Unicode 数学字符（而不是原始 TeX 源码）：

```bash
pdftotext -f 1 -l 5 build/study-guide-zh.pdf - | head
```

你应看到斜体字母和诸如 n、P、≤、∞ 的符号，而不是 `\mathrm` 和 `\le`。

---

## 一次性操作步骤（全部执行）

在 `study-guide-zh/` 目录中安装工具后，运行：

```bash
python3 ../scripts/convert_math_delimiters.py *.md
python3 ../scripts/reconstruct_figures.py
bash ../scripts/build_study_guide_zh.sh
ls -lh build/study-guide-zh.html build/study-guide-zh.pdf
```

然后打开 `build/study-guide-zh.pdf`。

对于详细的中文入门版：

```bash
bash ../scripts/build_beginner_zh.sh
```

然后打开 `../study-guide/build/beginner-zh.pdf`。
