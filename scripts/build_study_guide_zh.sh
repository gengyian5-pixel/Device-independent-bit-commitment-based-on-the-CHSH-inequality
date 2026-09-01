#!/usr/bin/env bash
# Build the complete Chinese technical study guide as HTML and PDF.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SG="$ROOT/study-guide-zh"
FIGURES="$ROOT/study-guide/figures"
OUT="$SG/build"
mkdir -p "$OUT"

CHAPTERS=(
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
  equation-map.md
  reconstruction-checklist.md
  solutions.md
  unicode-math.md
  how-to-rebuild.md
)

SOURCES=()
for chapter in "${CHAPTERS[@]}"; do
  SOURCES+=("$SG/$chapter")
done

COMMON=(
  --from markdown+tex_math_dollars+tex_math_double_backslash+raw_tex
  --standalone
  --toc --toc-depth=2
  --resource-path="$SG:$FIGURES"
  -M title="CHSH 设备无关比特承诺：完整中文学习指南"
  -M author="Aharon 等（NJP 18, 025014, 2016）论文重建工作簿"
  -V toc-title="目录"
)

echo "Writing complete Chinese HTML (KaTeX)..."
pandoc "${SOURCES[@]}" "${COMMON[@]}" \
  --katex=/usr/share/javascript/katex/ \
  --embed-resources \
  -o "$OUT/study-guide-zh.html"

echo "Writing complete Chinese PDF (XeLaTeX + CJK + Unicode math)..."
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
  -o "$OUT/study-guide-zh.pdf"

echo "Wrote:"
ls -lh "$OUT/study-guide-zh.html" "$OUT/study-guide-zh.pdf"
