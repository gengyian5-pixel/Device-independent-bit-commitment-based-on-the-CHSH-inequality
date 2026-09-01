# English original + Chinese translation / 英中对照学习指南

This edition places every English study-guide chapter next to its complete Chinese translation.

本版本同时提供每章的英文原文和完整中文译文，适合逐章对照阅读。

## Chapter pairs / 章节对照

| # | English original | 中文译文 |
|---:|---|---|
| 0 | [How to use](../study-guide/00-how-to-use.md) | [如何使用](../study-guide-zh/00-how-to-use.md) |
| 1 | [Prerequisites](../study-guide/01-prerequisites.md) | [预备知识](../study-guide-zh/01-prerequisites.md) |
| 2 | [Research question](../study-guide/02-the-research-question.md) | [研究问题](../study-guide-zh/02-the-research-question.md) |
| 3 | [Bit commitment](../study-guide/03-bit-commitment.md) | [比特承诺](../study-guide-zh/03-bit-commitment.md) |
| 4 | [Device-independence](../study-guide/04-device-independence.md) | [设备无关性](../study-guide-zh/04-device-independence.md) |
| 5 | [Honest resources](../study-guide/05-honest-resources.md) | [诚实资源](../study-guide-zh/05-honest-resources.md) |
| 6 | [The protocol](../study-guide/06-protocol.md) | [协议](../study-guide-zh/06-protocol.md) |
| 7 | [Alice’s security](../study-guide/07-alice-security.md) | [Alice 的安全性](../study-guide-zh/07-alice-security.md) |
| 8 | [Bob’s security: asymptotic](../study-guide/08-bob-security-asymptotic.md) | [Bob 的渐近安全性](../study-guide-zh/08-bob-security-asymptotic.md) |
| 9 | [Bob’s security: finite tests](../study-guide/09-bob-security-finite.md) | [Bob 的有限轮安全性](../study-guide-zh/09-bob-security-finite.md) |
| 10 | [Appendices A–C](../study-guide/10-appendices.md) | [附录 A–C](../study-guide-zh/10-appendices.md) |
| 11 | [Write the paper](../study-guide/11-write-the-paper.md) | [写出论文](../study-guide-zh/11-write-the-paper.md) |

## Reference pairs / 附属资料

| English original | 中文译文 |
|---|---|
| [Equation map](../study-guide/equation-map.md) | [公式索引](../study-guide-zh/equation-map.md) |
| [Reconstruction checklist](../study-guide/reconstruction-checklist.md) | [重建检查表](../study-guide-zh/reconstruction-checklist.md) |
| [Worked solutions](../study-guide/solutions.md) | [习题详解](../study-guide-zh/solutions.md) |
| [Unicode/LaTeX math](../study-guide/unicode-math.md) | [Unicode/LaTeX 数学符号](../study-guide-zh/unicode-math.md) |
| [How to rebuild](../study-guide/how-to-rebuild.md) | [如何重新构建](../study-guide-zh/how-to-rebuild.md) |

## Combined bilingual book / 合并双语电子书

The combined edition presents each English chapter first, immediately followed by its Chinese translation.  
合并版按章节排列：先放英文原文，紧接该章中文译文。

From the repository root / 在仓库根目录运行：

```bash
bash scripts/build_study_guide_bilingual.sh
```

Outputs / 输出：

- `study-guide-bilingual/build/study-guide-bilingual.html`
- `study-guide-bilingual/build/study-guide-bilingual.pdf`

For beginners, first read the separate [plain-language Chinese course](../study-guide/beginner/README.md).  
完全零基础者，建议先读独立的[中文白话教材](../study-guide/beginner/README.md)。
