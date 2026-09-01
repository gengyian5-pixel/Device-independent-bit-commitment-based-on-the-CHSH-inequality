#!/usr/bin/env python3
"""Assemble paired English/Chinese Markdown without changing source files."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EN_DIR = ROOT / "study-guide"
ZH_DIR = ROOT / "study-guide-zh"
OUTPUT_DIR = ROOT / "study-guide-bilingual" / "build"

PAIRS = [
    ("00-how-to-use.md", "0. How to use / 如何使用"),
    ("01-prerequisites.md", "1. Prerequisites / 预备知识"),
    ("02-the-research-question.md", "2. Research question / 研究问题"),
    ("03-bit-commitment.md", "3. Bit commitment / 比特承诺"),
    ("04-device-independence.md", "4. Device-independence / 设备无关性"),
    ("05-honest-resources.md", "5. Honest resources / 诚实资源"),
    ("06-protocol.md", "6. The protocol / 协议"),
    ("07-alice-security.md", "7. Alice’s security / Alice 的安全性"),
    (
        "08-bob-security-asymptotic.md",
        "8. Bob’s security (asymptotic) / Bob 的渐近安全性",
    ),
    (
        "09-bob-security-finite.md",
        "9. Bob’s security (finite tests) / Bob 的有限轮安全性",
    ),
    ("10-appendices.md", "10. Appendices A–C / 附录 A–C"),
    ("11-write-the-paper.md", "11. Write the paper / 写出论文"),
    ("equation-map.md", "Equation map / 公式索引"),
    ("reconstruction-checklist.md", "Reconstruction checklist / 重建检查表"),
    ("solutions.md", "Worked solutions / 习题详解"),
    ("unicode-math.md", "Unicode and LaTeX math / Unicode 与 LaTeX 数学"),
    ("how-to-rebuild.md", "How to rebuild / 如何重新构建"),
]

HEADING = re.compile(r"^(#{1,6})(\s+)", re.MULTILINE)
LINK = re.compile(r"(\[[^\]]*\]\()([^)#]+)((?:#[^)]*)?\))")


def rewrite_links(text: str, source_dir: Path) -> str:
    """Make local links resolve from study-guide-bilingual/build."""

    def replace(match: re.Match[str]) -> str:
        target = match.group(2)
        if "://" in target or target.startswith(("mailto:", "/", "#")):
            return match.group(0)
        absolute = (source_dir / target).resolve()
        relative = os.path.relpath(absolute, OUTPUT_DIR)
        return match.group(1) + relative + match.group(3)

    return LINK.sub(replace, text)


def demote_headings(text: str) -> str:
    """Reserve H1 for the pair and H2 for language labels."""

    return HEADING.sub(lambda m: "#" * min(len(m.group(1)) + 2, 6) + m.group(2), text)


def chapter(path: Path) -> str:
    text = path.read_text(encoding="utf-8").strip()
    if path.name == "unicode-math.md":
        # Route glyphs absent from the CJK body font through unicode-math.
        replacements = {
            "⟨ ⟩": r"$\langle\ \rangle$",
            "ℝ": r"$\mathbb{R}$",
            "ℂ": r"$\mathbb{C}$",
            "𝟙": r"$\mathbb{1}$",
            "∘": r"$\circ$",
            "∼": r"$\sim$",
        }
        for plain, math in replacements.items():
            text = text.replace(plain, math)
    # Pandoc wraps $$...$$ in a display environment; align* nested inside it
    # is invalid LaTeX, while aligned is explicitly designed for this use.
    text = text.replace(r"\begin{align*}", r"\begin{aligned}")
    text = text.replace(r"\end{align*}", r"\end{aligned}")
    return demote_headings(rewrite_links(text, path.parent))


def assemble() -> str:
    sections = [
        "# English original + Chinese translation / 英中对照学习指南",
        "",
        "Each pair contains the English source first and its complete Chinese translation second.",
        "",
        "每组先列英文原文，再列完整中文译文。数学公式保持一致。",
        "",
    ]
    for filename, title in PAIRS:
        en = EN_DIR / filename
        zh = ZH_DIR / filename
        if not en.exists() or not zh.exists():
            raise FileNotFoundError(f"Missing pair: {en} / {zh}")
        sections.extend(
            [
                "\\newpage",
                "",
                f"# {title}",
                "",
                "## English original",
                "",
                chapter(en),
                "",
                "## 中文译文",
                "",
                chapter(zh),
                "",
            ]
        )
    return "\n".join(sections)


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: assemble_study_guide_bilingual.py OUTPUT.md")
    output = Path(sys.argv[1])
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(assemble(), encoding="utf-8")
    print(f"Wrote bilingual source: {output}")


if __name__ == "__main__":
    main()
