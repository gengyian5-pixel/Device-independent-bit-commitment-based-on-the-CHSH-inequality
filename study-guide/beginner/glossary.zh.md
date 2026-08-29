# 术语表：看到英文或符号时怎么翻译

| 原文 / 符号 | 推荐中文 | 本指南里的白话 |
|---|---|---|
| bit | 比特 | 只能取 0 或 1 |
| bit commitment | 比特承诺 | 先封存、后打开 |
| commit phase | 承诺阶段 | Alice 先交凭证 $q$ |
| reveal phase | 揭示阶段 | Alice 后交 $b,r$ |
| concealing | 隐藏性 | Bob 不能提前偷看 |
| binding | 绑定性 | Alice 不能事后改口 |
| distrustful cryptography | 互不信任密码学 | Alice 和 Bob 可能互相作弊 |
| device-independent (DI) | 设备无关 | 不依赖内部实现；仍需量子理论、可信随机数、隔离、无泄漏、无损失等假设 |
| black box | 黑盒子 | 只有按钮和灯 |
| input / setting $s$ | 输入 / 设置 | 按哪个按钮 |
| output $r$ | 输出 | 哪盏灯亮 |
| correlation | 关联 | 两边答案怎样一起变化 |
| marginal | 边际分布 | 把另一边结果全部加掉，只看本地 |
| no-signalling | 无信令 | 本地统计不受远方按钮影响 |
| local hidden variable | 定域隐变量 | 两边靠事先约好的答案表 |
| Bell inequality | 贝尔不等式 | 所有定域答案表必须满足的界 |
| CHSH | CHSH 不等式 / 博弈 | 两人、不通信、四种题目的游戏 |
| CHSH violation | 违反 CHSH | 分数超过经典界 2 |
| Tsirelson bound | Tsirelson 界 | 量子 CHSH 上限 $2\sqrt2$ |
| pseudo-telepathy | 伪心灵感应 | 量子策略必胜、经典不能必胜 |
| GHZ | GHZ 态 / 博弈 | 旧协议用的三方必赢关联 |
| EPR pair | EPR 对 | 两个纠缠量子比特 |
| PR box | PR 盒 | 无信令但超量子的 CHSH 必胜盒 |
| quantum state $\rho$ | 量子态 | 系统的完整统计描述 |
| observable | 可观测量 | 一种二值测量方向 |
| POVM $\Pi_{r|s}$ | 正算符值测度 | 输入 $s$ 得输出 $r$ 的一般测量事件 |
| Pauli $\sigma_x,\sigma_z$ | Pauli 矩阵 | 两个基本测量方向 |
| tensor product $\otimes$ | 张量积 | 把左右系统合并描述 |
| trace $\operatorname{Tr}$ | 迹 | 从态和测量算出概率 |
| ancilla | 辅助系统 | 作弊者保留、可与盒子纠缠的额外系统 |
| control $P_{\mathrm{cont}}$ | Alice 的控制率 | 她事后想开哪边就能开的平均成功率 |
| information gain $P_{\mathrm{gain}}$ | Bob 的信息增益 | 他在揭示前猜中 $b$ 的概率 |
| balanced protocol | 平衡协议 | 两个作弊率相等 |
| completeness | 完备性 | 双方诚实时协议成功 |
| soundness / security | 可靠性 / 安全性 | 作弊成功受到限制 |
| abort | 中止 | 检查不通过，协议作废 |
| threshold $I_{\mathrm{th}}$ | 阈值 | CHSH 及格线 |
| history $\mathbf W_k$ | 历史 | 前 $k$ 轮所有输入输出 |
| i.i.d. | 独立同分布 | 每轮彼此独立且同一种分布 |
| conditional expectation | 条件期望 | 已知过去后的最佳平均预测 |
| martingale | 鞅 | 知道过去后，下一步没有可预测净收益 |
| Azuma–Hoeffding | Azuma–Hoeffding 不等式 | 有界鞅大幅偏离的概率界 |
| SDP | 半定规划 | 变量是正半定矩阵的凸优化 |
| NPA hierarchy | NPA 层次 | 从外面逐层逼近量子关联集合 |
| relaxation | 松弛 | 放宽限制以得到可算的上界 |
| asymptotic | 渐近 | 通常指 $N\to\infty$ |
| finite-size bound | 有限尺寸界 | 有限测试轮数时的安全上界 |

## 常用符号

| 符号 | 读法 | 意义 |
|---|---|---|
| $\oplus$ | 异或 / 模 2 加 | 相同得 0，不同得 1 |
| $\mid$ | 条件于 | 左边事件在右边条件下 |
| $\sum$ | 求和 | 把列出的可能性加起来 |
| $\mathbb E$ | 期望 | 长期平均 |
| $\langle AB\rangle$ | $AB$ 的期望 / 关联 | 两个 $\pm1$ 输出乘积的平均 |
| $\succeq0$ | 正半定 | 保证对应概率非负 |
| $\mathbb1$ | 单位算符 | 所有结果之和 |
| $\bar c$ | $c$ 的反值 | $\bar c=1-c$ |
| $\bar I_n$ | $I$ 横线 $n$ | 前 $n$ 轮经验平均 |
| $\Theta(x)$ | 阶跃函数 | $x\ge0$ 时 1，否则 0 |
| $C(I)$ | 控制函数 | 给定 CHSH 分数时 Alice 的最大控制率 |
| $\varepsilon$ | epsilon | 允许的统计偏差 |

## 三个最容易混淆的词

1. **相关不等于通信。** 两边答案高度相关，并不代表 Alice 可以选择 Bob 看见的本地概率。
2. **可达策略不等于最优证明。** 做到 85% 只是下界；还要 SDP 上界排除 86%。
3. **“安全”不等于作弊率很小。** 本文作弊率 75% / 85% 都不低；“安全结论”是它们有严格上界，而不是完美承诺。

