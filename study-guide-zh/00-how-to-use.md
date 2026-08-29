# 0. 如何使用本指南

**如果你不了解量子力学，**请从这里开始，而不是从第 1 节开始：

- 英文：[00-no-quantum.md](../study-guide/00-no-quantum.md)
- 更长的中文白话路径：[beginner/README.md](../study-guide/beginner/README.md)

然后再回到下表。

## “自己构建论文”是什么意思

完成的论文是对一套完整论证的*报告*。本指南则按照你应该*发现*这套论证的顺序来讲解。如果你完成每一个检查点，就会掌握：

1. 密码学定义和设备无关（device-independent，DI）威胁模型。
2. 一种诚实的物理实现（EPR 对 + 每个盒子四种测量设置）。
3. 三阶段协议，包括时序安排和私有随机数 $n$ *为何*存在。
4. 一份证明 $P_{\mathrm{gain}}\le 3/4$ 的无信令（no-signalling）证明，以及一个显式的达到该界的策略。
5. 在固定 CHSH 值 $I$ 下 Alice 控制力的半定规划（semidefinite programming，SDP）表述，以及一个在 $P_{\mathrm{cont}}=\cos^2(\theta/2)$ 处达到该界的显式双量子比特策略。
6. 一个鞅（martingale）/ Azuma–Hoeffding 有限 $N$ 界；当 $N\to\infty$ 时，它恢复同一个数值。
7. PR 盒（后量子）协议，以及两个“自由揭示时间”变体。

然后，你可以使用自己的笔记，按照 [11-write-the-paper.md](11-write-the-paper.md) 写出论文。

## 如何查看数学符号

各章使用 `$inline$` 和 `$$display$$` 数学格式（GitHub / KaTeX / MathJax）。它们应当能在 GitHub 和 Cursor 预览中正确渲染。如果你想要完整排版的版本：

- HTML：[build/study-guide.html](../study-guide/build/study-guide.html)
- 使用 Unicode 数学字体的 PDF：[build/study-guide.pdf](../study-guide/build/study-guide.pdf)
- 符号卡片：[unicode-math.md](../study-guide/unicode-math.md)（π、θ、≤、⊕、⊗、√、∞、……）
- 完整的重新构建步骤：[how-to-rebuild.md](../study-guide/how-to-rebuild.md)

编辑后重新构建：

```bash
bash scripts/build_study_guide.sh
```

## 建议的学习方法

- 准备一本笔记本，记录由*你自己*提出并编号的引理。到撰写阶段之前，不要照抄论文中的编号。
- 每学完一章，先合上指南，尝试不看内容，用一段话复述该章的论点。
- 只有这样做完之后，才打开该章对应的 [solutions.md](../study-guide/solutions.md)。
- 在开始写作之前，用 [reconstruction-checklist.md](../study-guide/reconstruction-checklist.md) 作为“论文完整性”测试。

## 推荐顺序（不要跳过）

| 顺序 | 章节 | 论文对应部分 | 本章产出 |
|---|---|---|---|
| 1 | [01 预备知识](01-prerequisites.md) | 隐含内容 | CHSH、Tsirelson 界、PR 盒、POVM、鞅 |
| 2 | [02 研究问题](02-the-research-question.md) | §1 | 用一句话概括论文主旨 |
| 3 | [03 比特承诺](03-bit-commitment.md) | §2.1 | $P_{\mathrm{cont}}$、$P_{\mathrm{gain}}$、平衡性 |
| 4 | [04 设备无关性](04-device-independence.md) | §2.2 | 五项假设，以及“发送一个盒子”的含义 |
| 5 | [05 诚实资源](05-honest-resources.md) | §3 引言 | 测量表和两类关联 |
| 6 | [06 协议](06-protocol.md) | §3 | 协议、时序约束、中止条件 |
| 7 | [07 Alice 的安全性](07-alice-security.md) | §4 | $P_{\mathrm{gain}}\le 3/4$ |
| 8 | [08 Bob 的安全性，$N=\infty$](08-bob-security-asymptotic.md) | §5.1–5.2 | $C(I)$ 和最优作弊策略 |
| 9 | [09 Bob 的安全性，有限 $N$](09-bob-security-finite.md) | §5.3、附录 D | 界 (19) |
| 10 | [10 附录](10-appendices.md) | 附录 A–C | PR 盒协议；自由揭示时间 |
| 11 | [11 写出论文](11-write-the-paper.md) | 全文 | 逐节写作计划 |

## 你*不应该*做什么

- 不要一开始就优化 Alice 的四结果 POVM。先理解为什么一次二结果测量就已经能够达到该界。
- 不要把随机索引 $n$ 当成技术细节。如果 Bob 不隐藏 $n$，Alice 就能完美作弊。
- 不要混淆“CHSH 测试”和“承诺/揭示测量”。整个安全性思路在于，*保留的*盒子无法区分二者。

## 你从一开始就应该采用的记号

现在就固定这些记号；如果临时自创记号，论文后面的章节将难以阅读。

- 两个盒子，标记为 $i\in\{0,1\}$。
- 四个输入 $s\in\{0,1,2,3\}$，两个输出 $r\in\{0,1\}$。
- 第 $k$ 次使用盒子 $i$：随机变量 $S^i_k$、$R^i_k$；实现值 $s^i_k$、$r^i_k$。
- $W_k=\{S^0_k,S^1_k,R^0_k,R^1_k\}$，历史 $\mathbf{W}_k=\{W_1,\dots,W_k\}$。
- $\sigma_\theta=\cos\theta\,\sigma_z+\sin\theta\,\sigma_x$。
- $|0\rangle,|1\rangle$ 是 $\sigma_z$ 的 $\pm 1$ 本征态。
- Alice 承诺的比特 $b$；凭证比特 $q$；一次性密码本比特 $a$。
- 硬币 $c\in\{0,1\}$ 决定 Alice 收到哪个盒子；$\bar c=1-c$ 是 Bob 保留的盒子。
