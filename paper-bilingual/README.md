# Paper: English original + Chinese translation / 论文英中逐段对照

Paragraph-by-paragraph bilingual edition of Aharon, Massar, Pironio, and Silman,
*Device-independent bit commitment based on the CHSH inequality*,
*New J. Phys.* **18**, 025014 (2016),
[doi:10.1088/1367-2630/18/2/025014](https://doi.org/10.1088/1367-2630/18/2/025014),
[arXiv:1511.06283](https://arxiv.org/abs/1511.06283).

这是论文本身的英中逐段对照，不是学习指南。每一段先列 **English original**，紧接 **中文译文**。公式与发表稿编号 (1)–(24) 一致；文献引用编号与 NJP 正式发表稿 [1]–[48] 一致。

This is the paper itself, not the study guide. Each block is the English original followed by a Chinese translation. Equation numbers match (1)–(24); citations match the published NJP numbering [1]–[48].

## Read online / 在线阅读

- Combined book: [HTML](build/paper-bilingual.html) · [PDF](build/paper-bilingual.pdf)
- Source sections:
  - [Title, abstract, §§ I–II](sections/01-front-intro-background.md)
  - [§§ III–IV](sections/02-protocol-alice-security.md)
  - [§§ V–VI, figures, acknowledgements](sections/03-bob-security-summary.md)
  - [Appendices A–D and references](sections/04-appendices-references.md)

## Rebuild / 重新构建

From the repository root:

```bash
bash scripts/build_paper_bilingual.sh
```

Requires pandoc, XeLaTeX, KaTeX, Noto CJK SC fonts, and TeX Gyre DejaVu Math (same stack as the bilingual study guide).

## Editorial notes / 编辑说明

- English follows the **published NJP article**. Where the 2015 arXiv source differs—especially the comparison with relativistic bit commitment—the NJP wording is used.
- Figure 3’s caption in the paper uses $I_{\mathrm{th}}=2\sqrt{2}(1-1/\sqrt{N})$, while the surrounding text uses $I_{\mathrm{th}}=2\sqrt{2}-1/\sqrt{N}$. Both forms are kept as in the source.
- Bibliographic fields (author, title, journal, year) are left in English.
- 英文以 NJP 正式发表稿为准。图 3 图注与正文中的 $I_{\mathrm{th}}$ 写法不一致，对照版按原文两种写法并存。参考文献著录项不译。
