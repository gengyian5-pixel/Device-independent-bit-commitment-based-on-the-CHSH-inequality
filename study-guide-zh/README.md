# CHSH 设备无关比特承诺：完整中文学习指南

本目录是 `study-guide/` 的完整简体中文版本，目标是帮助你从背景知识一直重建到有限轮安全证明和附录。

## 从哪里开始

- **完全没学过量子力学：**先读 [中文零基础教材](../study-guide/beginner/README.md)，再回到本指南。
- **已学线性代数、概率或基础量子：**直接从 [00 如何使用](00-how-to-use.md) 开始。
- **只想查某个公式：**打开 [公式索引](equation-map.md)。
- **想确认能否独立重建：**使用 [重建检查表](reconstruction-checklist.md)。
- **做完题再核对：**打开 [习题详解](solutions.md)。

## 主线章节

| 顺序 | 章节 | 目标 |
|---:|---|---|
| 0 | [如何使用本指南](00-how-to-use.md) | 学习方法、顺序与统一记号 |
| 1 | [预备知识](01-prerequisites.md) | CHSH、PR 盒、POVM、NPA、鞅 |
| 2 | [研究问题](02-the-research-question.md) | 论文为什么需要把 GHZ 换成 CHSH |
| 3 | [比特承诺](03-bit-commitment.md) | 控制率、信息增益、平衡性 |
| 4 | [设备无关性](04-device-independence.md) | 五项假设与“发送盒子”的含义 |
| 5 | [诚实资源](05-honest-resources.md) | EPR 态、四个测量输入、目标关联 |
| 6 | [协议](06-protocol.md) | 随机测试、承诺、揭示、时序 |
| 7 | [Alice 的安全性](07-alice-security.md) | 用无信令证明 $P_{\mathrm{gain}}\le3/4$ |
| 8 | [Bob 的渐近安全性](08-bob-security-asymptotic.md) | SDP 上界与最优作弊策略 |
| 9 | [Bob 的有限轮安全性](09-bob-security-finite.md) | 记忆攻击、鞅与 Azuma |
| 10 | [附录 A–C](10-appendices.md) | PR 盒与自由揭示时间变体 |
| 11 | [写出论文](11-write-the-paper.md) | 逐节组织自己的论文 |

## 辅助资料

- [公式索引（论文式 (1)–(24)）](equation-map.md)
- [重建检查表](reconstruction-checklist.md)
- [习题详解](solutions.md)
- [Unicode / LaTeX 数学符号卡](unicode-math.md)
- [重新构建指南](how-to-rebuild.md)

## 中文电子书

从仓库根目录运行：

```bash
bash scripts/build_study_guide_zh.sh
```

生成：

- `study-guide-zh/build/study-guide-zh.html`
- `study-guide-zh/build/study-guide-zh.pdf`

这套完整指南与较短的零基础教材不同：零基础教材先建立直觉；本指南保留原技术学习路线、所有习题和证明结构。
