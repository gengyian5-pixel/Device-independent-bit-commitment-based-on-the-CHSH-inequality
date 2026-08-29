# How to rebuild (step by step)

“Rebuild” means regenerating the **typeset study guide** (HTML + PDF) from the Markdown chapters, and optionally regenerating **Figures 1 and 3**. You do this after you edit a chapter, or when math is not displaying.

There are three products:

| Product | Command | Output |
|---|---|---|
| Typeset HTML + PDF | `bash scripts/build_study_guide.sh` | `study-guide/build/study-guide.html`, `study-guide/build/study-guide.pdf` |
| Figs. 1 and 3 | `python scripts/reconstruct_figures.py` | `study-guide/figures/*.png` |
| Math-delimiter fix | `python scripts/convert_math_delimiters.py study-guide/*.md` | rewrites the `.md` files in place |

Do the steps below in order. Skip a step only when the text says it is optional.

---

## Step 0. Open a terminal in the repository

1. Open a terminal (in Cursor: **Terminal → New Terminal**).
2. Go to the **root of this repo** — the folder that contains `scripts/` and `study-guide/`:

```bash
pwd
ls
```

You should see `README.md`, `scripts/`, and `study-guide/`.

If you are somewhere else:

```bash
cd /path/to/Device-independent-bit-commitment-based-on-the-CHSH-inequality
```

On this cloud workspace that path is `/workspace`.

---

## Step 1. Check that the tools are installed

Run:

```bash
which pandoc xelatex python3
pandoc --version | head -1
xelatex --version | head -1
python3 --version
ls /usr/share/javascript/katex/katex.min.js
fc-list : family | grep -E 'DejaVu Serif|TeX Gyre DejaVu Math'
```

**What “good” looks like**

- `pandoc` prints a path such as `/usr/bin/pandoc` and a version (3.x is fine).
- `xelatex` prints a path and `XeTeX ... (TeX Live ...)`.
- `python3` is 3.10+.
- The KaTeX file exists.
- Fontconfig lists **DejaVu Serif** and **TeX Gyre DejaVu Math**.

If any of those fail, do **Step 2**. If they all succeed, skip to **Step 3**.

---

## Step 2. Install the tools (only if Step 1 failed)

On Debian/Ubuntu:

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

For the figure script only:

```bash
python3 -m pip install -r scripts/requirements.txt
```

That installs `numpy` and `matplotlib`.

Then repeat **Step 1**.

---

## Step 3. (Optional) Rebuild Figures 1 and 3

Do this if you changed the analytic formulae, or if `study-guide/figures/` is missing the PNGs.

```bash
python3 scripts/reconstruct_figures.py
```

**What should happen**

```
sanity checks passed:
  theta=pi/4 => phi=0.785398, I=2.828427, C=0.853553
  D=4+2√2=6.828427
wrote .../study-guide/figures/fig1_alice_control.png
wrote .../study-guide/figures/fig3_finite_N.png
```

If the sanity checks fail, the formulae in the script no longer match equations (8)–(10) of the paper. Do not ignore that.

---

## Step 4. (Optional) Fix math delimiters

The HTML/PDF builder and GitHub preview expect:

- inline math: `$P_{\mathrm{cont}}$`
- display math:

```markdown
$$
P_{\mathrm{cont}}=\cos^2(\theta/2)
$$
```

They do **not** render `\( ... \)` / `\[ ... \]` reliably.

If you (or an editor) typed the LaTeX-style delimiters, convert them first:

```bash
python3 scripts/convert_math_delimiters.py study-guide/*.md
```

The script rewrites those files in place and skips fenced code blocks (including mermaid). If a file was already using `$...$`, it prints `unchanged`.

Check one file:

```bash
grep -n '$P_{\\mathrm{cont}}$' study-guide/03-bit-commitment.md | head
```

You should see dollar-delimited math, not `\(` `\)`.

---

## Step 5. Rebuild the HTML and PDF (the main step)

From the repo root:

```bash
bash scripts/build_study_guide.sh
```

**What the script does, in order**

1. Resolves the repo root from the location of `scripts/`.
2. Creates `study-guide/build/` if it does not exist.
3. Concatenates the chapters in this order: `00` … `11`, then `equation-map.md`, `reconstruction-checklist.md`, `unicode-math.md`. (`solutions.md` is **not** included, so the built book stays a workbook.)
4. Runs **Pandoc → HTML**, using the local KaTeX files at `/usr/share/javascript/katex/` and embedding CSS/fonts so the HTML is self-contained.
5. Runs **Pandoc → XeLaTeX → PDF**, with:
   - body font: DejaVu Serif
   - math font: TeX Gyre DejaVu Math (Unicode: π, ≤, ⊕, subscripts, …)
6. Prints the sizes of the two output files.

**What should happen**

```
Writing HTML (KaTeX)...
Writing PDF (XeLaTeX + Unicode math font)...
Wrote:
-rw-r--r-- ... study-guide/build/study-guide.html
-rw-r--r-- ... study-guide/build/study-guide.pdf
```

The PDF step takes a few seconds. If it fails, the terminal will show a XeLaTeX error; see **Troubleshooting** below.

Confirm the files are new:

```bash
ls -lh study-guide/build/study-guide.html study-guide/build/study-guide.pdf
```

The timestamps should be “just now”.

---

## Step 6. Open the rebuilt files

**HTML (fastest way to check that math rendered)**

```bash
xdg-open study-guide/build/study-guide.html
```

Or in Cursor: right-click `study-guide/build/study-guide.html` → Open. You should see a table of contents and typeset formulae (Greek letters, fractions, subscripts), not raw `$...$`.

**PDF**

```bash
xdg-open study-guide/build/study-guide.pdf
```

Or open it from the file tree. Search for `P_cont` or look at Chapter 1: CHSH and \(\le\), \(\otimes\), \(\pi\) should be real glyphs.

**Markdown preview (no rebuild needed for this one)**

Open any `study-guide/*.md` in Cursor. GitHub-style `$...$` math should render in preview. If you only see the dollar signs, use the HTML/PDF from Step 5.

---

## After you edit a chapter

Typical loop:

1. Edit e.g. `study-guide/08-bob-security-asymptotic.md`.
2. If you pasted `\( ... \)`, run Step 4.
3. Run Step 5 (`bash scripts/build_study_guide.sh`).
4. Reload the HTML or PDF (some viewers cache; close and reopen the PDF if it looks old).

You do **not** need Step 3 unless you changed the figure script.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `pandoc: command not found` or `xelatex: command not found` | TeX/Pandoc not installed | Step 2 |
| `katex.min.js: does not exist` | KaTeX package missing | `sudo apt-get install libjs-katex fonts-katex` |
| `Missing character: There is no … in font DejaVu Serif` | A Unicode symbol is in **text**, not math | Put it in `$...$` (math font) or replace with LaTeX (`\emptyset`, `\ll`) |
| HTML shows raw `$P_cont$` | File still uses `\(` `\)` | Step 4, then Step 5 |
| PDF succeeded but an old version opens | Viewer cache | Close the PDF, reopen `study-guide/build/study-guide.pdf` |
| `python3: No module named matplotlib` | Figure deps missing | `pip install -r scripts/requirements.txt` |
| Sanity check in figure script fails | Formulae in `reconstruct_figures.py` do not match (8)–(10) | Do not rebuild figures until that is fixed |
| Build is slow / XeLaTeX hangs | First TeX run can generate formats | Wait; later runs are faster |

To see whether the PDF actually contains Unicode math (not raw TeX source):

```bash
pdftotext -f 1 -l 5 study-guide/build/study-guide.pdf - | head
```

You want characters such as `𝑛`, `𝑃`, `≤`, `∞`, not `\mathrm` and `\le`.

---

## One-shot recipe (everything)

From the repo root, after tools are installed:

```bash
python3 scripts/convert_math_delimiters.py study-guide/*.md
python3 scripts/reconstruct_figures.py
bash scripts/build_study_guide.sh
ls -lh study-guide/build/study-guide.html study-guide/build/study-guide.pdf
```

Then open `study-guide/build/study-guide.pdf`.
