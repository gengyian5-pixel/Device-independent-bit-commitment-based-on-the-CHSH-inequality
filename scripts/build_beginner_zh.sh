#!/usr/bin/env bash
# Build the Chinese no-quantum-mechanics guide as HTML and PDF.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SG="$ROOT/study-guide"
BG="$SG/beginner"
OUT="$SG/build"
mkdir -p "$OUT"

SOURCES=(
  "$BG/README.md"
  "$BG/01-from-zero.zh.md"
  "$BG/02-chsh-game.zh.md"
  "$BG/03-bit-commitment.zh.md"
  "$BG/04-protocol.zh.md"
  "$BG/05-cheating.zh.md"
  "$BG/06-variants-and-next.zh.md"
  "$BG/07-math-bridge.zh.md"
  "$BG/08-workbook.zh.md"
  "$BG/glossary.zh.md"
)

COMMON=(
  --from markdown+tex_math_dollars+tex_math_double_backslash+raw_tex
  --standalone
  --toc --toc-depth=2
  --resource-path="$SG:$BG:$SG/figures"
  -M title="CHSH 设备无关比特承诺：零量子力学起点"
  -M author="Aharon 等（NJP 18, 025014, 2016）论文自学指南"
)

echo "Writing Chinese HTML (KaTeX)..."
pandoc "${SOURCES[@]}" "${COMMON[@]}" \
  --katex=/usr/share/javascript/katex/ \
  --embed-resources \
  -o "$OUT/beginner-zh.html"

echo "Writing Chinese PDF (XeLaTeX + CJK + Unicode math)..."
pandoc "${SOURCES[@]}" "${COMMON[@]}" \
  --pdf-engine=xelatex \
  -V documentclass=article \
  -V classoption=fontset=none \
  -V CJKmainfont="Noto Serif CJK SC" \
  -V mainfont="Noto Serif CJK SC" \
  -V sansfont="Noto Sans CJK SC" \
  -V monofont="Noto Sans Mono CJK SC" \
  -V mathfont="TeX Gyre DejaVu Math" \
  -V geometry:margin=1in \
  -V fontsize=11pt \
  -V colorlinks=true \
  --highlight-style=tango \
  -o "$OUT/beginner-zh.pdf"

echo "Wrote:"
ls -lh "$OUT/beginner-zh.html" "$OUT/beginner-zh.pdf"
