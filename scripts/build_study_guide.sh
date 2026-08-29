#!/usr/bin/env bash
# Build a KaTeX HTML copy and a Unicode-font PDF of the study guide.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SG="$ROOT/study-guide"
OUT="$SG/build"
mkdir -p "$OUT"

CHAPTERS=(
  00-how-to-use.md
  00-no-quantum.md
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
  unicode-math.md
  how-to-rebuild.md
)

SOURCES=()
for ch in "${CHAPTERS[@]}"; do
  SOURCES+=("$SG/$ch")
done

COMMON=(
  --from markdown+tex_math_dollars+tex_math_double_backslash+raw_tex
  --standalone
  --toc --toc-depth=2
  --resource-path="$SG:$SG/figures"
  -M title="Study guide: device-independent bit commitment from CHSH"
  -M author="Reconstruction workbook for Aharon, Massar, Pironio, Silman (NJP 18, 025014, 2016)"
)

echo "Writing HTML (KaTeX)..."
pandoc "${SOURCES[@]}" "${COMMON[@]}" \
  --katex=/usr/share/javascript/katex/ \
  --embed-resources \
  -o "$OUT/study-guide.html"

echo "Writing PDF (XeLaTeX + Unicode math font)..."
pandoc "${SOURCES[@]}" "${COMMON[@]}" \
  --pdf-engine=xelatex \
  -V documentclass=article \
  -V geometry:margin=1in \
  -V fontsize=11pt \
  -V mainfont="DejaVu Serif" \
  -V sansfont="DejaVu Sans" \
  -V monofont="DejaVu Sans Mono" \
  -V mathfont="TeX Gyre DejaVu Math" \
  -V colorlinks=true \
  --highlight-style=tango \
  -o "$OUT/study-guide.pdf"

echo "Wrote:"
ls -lh "$OUT/study-guide.html" "$OUT/study-guide.pdf"
