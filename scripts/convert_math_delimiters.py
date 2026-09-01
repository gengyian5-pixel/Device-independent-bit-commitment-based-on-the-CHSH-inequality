#!/usr/bin/env python3
"""Convert LaTeX \\( \\) / \\[ \\] delimiters to GitHub/KaTeX $ / $$ form.

Leaves fenced code blocks (including mermaid) and `inline code` untouched.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

FENCE = re.compile(r"(```.*?```|~~~.*?~~~)", re.DOTALL)
INLINE_CODE = re.compile(r"(`[^`]+`)")
DISPLAY = re.compile(r"(?<!`)\\\[(.*?)\\\](?!`)", re.DOTALL)
INLINE = re.compile(r"(?<!`)\\\((.*?)\\\)(?!`)")


def convert_math_only(text: str) -> str:
    text = DISPLAY.sub(lambda m: "\n$$\n" + m.group(1).strip() + "\n$$\n", text)
    text = INLINE.sub(lambda m: "$" + m.group(1) + "$", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def convert_chunk(text: str) -> str:
    """Convert math in prose; leave `inline code` unchanged."""
    parts = INLINE_CODE.split(text)
    out = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            out.append(part)
        else:
            out.append(convert_math_only(part))
    return "".join(out)


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
