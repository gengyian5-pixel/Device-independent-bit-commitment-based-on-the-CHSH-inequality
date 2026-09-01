#!/usr/bin/env bash
# Build paragraph-paired English-original + Chinese-translation paper (HTML + PDF).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/paper-bilingual/build"
FIGURES="$ROOT/paper-bilingual/figures"
COMBINED="$(mktemp --suffix=.md)"
trap 'rm -f "$COMBINED"' EXIT
mkdir -p "$OUT"

# Copy paper figures from the arXiv source tarball when present.
if [[ -d /tmp/paper-source-files ]]; then
  mkdir -p "$FIGURES"
  for f in fig1.png fig2.png fig3.png; do
    if [[ -f "/tmp/paper-source-files/$f" && ! -f "$FIGURES/$f" ]]; then
      cp "/tmp/paper-source-files/$f" "$FIGURES/$f"
    fi
  done
fi

python3 "$ROOT/scripts/assemble_paper_bilingual.py" "$COMBINED"

COMMON=(
  --from markdown+tex_math_dollars+tex_math_double_backslash+raw_tex+link_attributes
  --standalone
  --toc --toc-depth=2
  --resource-path="$ROOT/paper-bilingual:$FIGURES"
  -M title="Device-independent bit commitment based on the CHSH inequality"
  -M subtitle="English original + Chinese translation / 英中逐段对照"
  -V toc-title="Contents / 目录"
)

echo "Writing bilingual paper HTML (KaTeX)..."
pandoc "$COMBINED" "${COMMON[@]}" \
  --katex=/usr/share/javascript/katex/ \
  --embed-resources \
  -o "$OUT/paper-bilingual.html"

echo "Writing bilingual paper PDF (XeLaTeX + CJK + Unicode math)..."
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
  -o "$OUT/paper-bilingual.pdf"

echo "Wrote:"
ls -lh "$OUT/paper-bilingual.html" "$OUT/paper-bilingual.pdf"
