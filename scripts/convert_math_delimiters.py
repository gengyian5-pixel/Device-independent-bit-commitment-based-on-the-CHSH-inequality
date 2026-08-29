#!/usr/bin/env python3
"""Convert LaTeX \\( \\) / \\[ \\] delimiters to GitHub/KaTeX $ / $$ form.

Leaves fenced code blocks (including mermaid) untouched.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

FENCE = re.compile(r"(```.*?```|~~~.*?~~~)", re.DOTALL)
DISPLAY = re.compile(r"\\\[(.*?)\\\]", re.DOTALL)
INLINE = re.compile(r"\\\((.*?)\\\)", re.DOTALL)


def convert_chunk(text: str) -> str:
    text = DISPLAY.sub(lambda m: "\n$$\n" + m.group(1).strip() + "\n$$\n", text)
    text = INLINE.sub(lambda m: "$" + m.group(1) + "$", text)
    # Collapse extra blank lines introduced around display math
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def convert_markdown(text: str) -> str:
    parts = FENCE.split(text)
    out = []
    for i, part in enumerate(parts):
        if i % 2 == 1 or part.startswith("```") or part.startswith("~~~"):
            out.append(part)
        else:
            out.append(convert_chunk(part))
    return "".join(out)


def main(paths: list[str]) -> None:
    for raw in paths:
        path = Path(raw)
        original = path.read_text(encoding="utf-8")
        updated = convert_markdown(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print(f"converted {path}")
        else:
            print(f"unchanged {path}")


if __name__ == "__main__":
    main(sys.argv[1:])
