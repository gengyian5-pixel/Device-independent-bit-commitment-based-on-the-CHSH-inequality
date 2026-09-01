#!/usr/bin/env bash
# Build chapter-paired English-original + Chinese-translation HTML and PDF.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/study-guide-bilingual/build"
FIGURES="$ROOT/study-guide/figures"
COMBINED="$(mktemp --suffix=.md)"
trap 'rm -f "$COMBINED"' EXIT
mkdir -p "$OUT"

python3 "$ROOT/scripts/assemble_study_guide_bilingual.py" "$COMBINED"

COMMON=(
  --from markdown+tex_math_dollars+tex_math_double_backslash+raw_tex
  --standalone
  --toc --toc-depth=2
  --resource-path="$ROOT/study-guide:$ROOT/study-guide-zh:$FIGURES"
  -M title="English original + Chinese translation"
  -M subtitle="Device-independent bit commitment based on the CHSH inequality / 基于 CHSH 不等式的设备无关比特承诺"
  -V toc-title="Contents / 目录"
)

echo "Writing bilingual HTML (KaTeX)..."
pandoc "$COMBINED" "${COMMON[@]}" \
  --katex=/usr/share/javascript/katex/ \
  --embed-resources \
  -o "$OUT/study-guide-bilingual.html"

echo "Writing bilingual PDF (XeLaTeX + CJK + Unicode math)..."
pandoc "$COMBINED" "${COMMON[@]}" \
  --pdf-engine=xelatex \
  -V documentclass=article \
  -V classoption=fontset=none \
  -V CJKmainfont="Noto Serif CJK SC" \
  -V mainfont="Noto Serif CJK SC" \
  -V sansfont="Noto Sans CJK SC" \
  -V monofont="Noto Sans Mono CJK SC" \
  -V mathfont="TeX Gyre DejaVu Math" \
  -V geometry:margin=0.85in \
  -V fontsize=10pt \
  -V colorlinks=true \
  --highlight-style=tango \
  -o "$OUT/study-guide-bilingual.pdf"

echo "Wrote:"
ls -lh "$OUT/study-guide-bilingual.html" "$OUT/study-guide-bilingual.pdf"
