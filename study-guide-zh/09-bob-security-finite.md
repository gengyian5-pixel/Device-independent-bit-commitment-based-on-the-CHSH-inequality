# 9. 有限次测试下 Bob 的安全性

论文对应部分：§5.3 和附录 D。目标：如果设备具有**任意记忆（arbitrary memory）**，Alice 的控制力仍然受到某个界的约束，且当 $N\to\infty$ 时，该界趋于 $C(I_{\mathrm{th}})$。

这是论文中 Reichardt–Unger–Vazirani 风格的部分，但简化了许多：你只需要对 CHSH 指示量构造一个鞅（martingale），而不需要完整的自测试定理（self-testing theorem）。

## 9.1 为什么不能使用 i.i.d. 假设

不诚实的 Alice 可以编程实现：

- 一个计数器：“在第 $N+1$ 次使用时，忽略 CHSH 并输出一个确定性的承诺”；
- 依赖历史的测量：在某些路径上让 CHSH 测试失败，再在另一些路径上补偿；
- 一种使第 $n+1$ 轮预期 CHSH 值*不等于*经验值 $\bar I_n$ 的策略。

因此，你不能直接把 $\bar I_n$ 代入 $C(\cdot)$ 就认为万事大吉。你需要证明：除去一个很小的概率，经验 CHSH 值 $\approx$ *下一轮*的条件期望 CHSH 值，而且这一结论对所有策略一致成立。

## 9.2 将 $P_{\mathrm{cont}}$ 表示为对 $n$ 和历史的平均

Bob 从 $\{1,\dots,N\}$ 中均匀选取 $n$。当 $n=N$ 时，第 $N+1$ 次使用永远不会接受 CHSH 测试，因此 Alice 可以在该分支上令 $C=1$。于是

$$
P_{\mathrm{cont}}=\frac1N\sum_{n=1}^{N-1}\sum_{\mathbf{w}_n}P(\mathbf{w}_n)\,\Theta(\bar I_n-I_{\mathrm{th}})\,C\bigl(\mathbb{E}[I(W_{n+1})\mid\mathbf{w}_n]\bigr)+\frac1N\sum_{\mathbf{w}_N}P(\mathbf{w}_N)\,\Theta(\bar I_N-I_{\mathrm{th}}).
$$

第二个求和 $\le 1/N$。这就是式 (11)。

**练习 9.1。** 根据协议和 $C(I)$ 的定义推导式 (11)。将单位阶跃函数（unit step）$\Theta$ 解释为“Bob 在阶段 1 中没有中止”。

**练习 9.2。** 为什么 $n=N$ 项不是 $C(I_{\mathrm{th}})/N$？因为 Alice 在第 $N+1$ 次使用时完全不受约束。

## 9.3 将每个短历史提升为长度为 $(N-1)$ 的历史

对每个满足 $n\le N-2$ 的 $\mathbf{w}_n$，考虑与之相容的扩展 $\mathbf{w}_{N-1}$。将该界改写为对 $\mathbf{w}_{N-1}$ 的平均，其中被平均的量为

$$
\frac1N\sum_{n=1}^{N-1}\Theta(\bar I_n-I_{\mathrm{th}})\,C\bigl(\mathbb{E}[I(W_{n+1})\mid\mathbf{w}_n]\bigr)+\frac1N.
$$

这就是式 (12)。

**练习 9.3。** 仔细写出这一求和次序变换。关键是得到一条*单一*样本路径，从而可以在其上标记经验 CHSH 值最后一次仍高于阈值的时刻。

## 9.4 最后一个良好时刻 $K$

$$
K(\mathbf{w}_{N-1})=\max\{k\le N-1:\bar I_k(\mathbf{w}_k)\ge I_{\mathrm{th}}\}
$$

（如果需要约定，当该集合为空时令 $K=0$；这些历史通过 $\Theta$ 贡献 $0$。）

于是，对所有 $n>K$ 都有 $\Theta(\bar I_n-I_{\mathrm{th}})=0$，因此关于 $n$ 的内层求和最多进行到 $K$。那些在到达 $K$ *之前*曾低于 $I_{\mathrm{th}}$ 的历史只会使真实的 $P_{\mathrm{cont}}$ 更小，所以对 $n\le K$ 去掉 $\Theta$ 可得到上界：

$$
P_{\mathrm{cont}}\le\sum_k\sum_{\mathbf{w}:K(\mathbf{w})=k}P(\mathbf{w})\,\frac1N\sum_{n=1}^k C\bigl(\mathbb{E}[I(W_{n+1})\mid\mathbf{w}_n]\bigr)+\frac1N.
$$

这就是式 (14)。

**练习 9.4。** 从式 (12) 推出式 (14)。论文中之所以是不等式，是因为某些 $n<K$ 可能满足 $\Theta=0$。

## 9.5 在 $K_0=\lceil(N-1)C(I_{\mathrm{th}})\rceil$ 处分拆并使用凹性

$C(I)$ 是凹函数（图 1 是凹的；你可以直接依据图像，也可以注意到：半正定规划（semidefinite program, SDP）的最优值作为线性约束的函数时，对该约束是凹的）。对于 $k\ge K_0$，

$$
\frac1k\sum_{n=1}^k C(\mathbb{E}_n)\le C\Bigl(\frac1k\sum_{n=1}^k\mathbb{E}[I(W_{n+1})\mid\mathbf{w}_n]\Bigr).
$$

对于 $k<K_0$，用 $C\le 1$ 作界，然后有 $k/N\le(N-1)C(I_{\mathrm{th}})/N$。

**练习 9.5。** 这一分拆看起来像魔法。它唯一的目的在于：即使 Alice 在这些项上令 $C=1$，“小 $k$”部分的贡献也不会超过约 $C(I_{\mathrm{th}})$，因为这样的项很少。检查式 (15) 中第一个求和的算术运算。

## 9.6 典型性：经验 CHSH 值与条件期望

将满足下式的 $k$-历史组成的坏集合定义为 $\pi_k(\varepsilon)$：

$$
\bar I_k(\mathbf{w}_k)-\frac1k\sum_{n=1}^k\mathbb{E}[I(W_n)\mid\mathbf{w}_{n-1}]\ge\varepsilon.
$$

在其补集上，凹性上界中 $C$ 的自变量至少为 $\bar I_k-\varepsilon\ge I_{\mathrm{th}}-\varepsilon$（因为 $K=k$ 意味着 $\bar I_k\ge I_{\mathrm{th}}$），因此，如果 $C$ 以某种方式递减，就有 $C(\cdots)\le C(I_{\mathrm{th}}-\varepsilon)$……**等等**：$C(I)$ 关于 $I$ 是*递减*的（非局域性越强，控制力越弱）。所以，要得到 $C$ 的一个*上界*，需要 $I$ 的一个*下界*。没错：在良好历史上，条件 CHSH 的平均值 $\ge\bar I_k-\varepsilon\ge I_{\mathrm{th}}-\varepsilon$，因此 $C\le C(I_{\mathrm{th}}-\varepsilon)$。

在坏历史上，使用 $C\le 1$ 作界。

**练习 9.6。** 将这些结果组合成式 (19) 的前两个陈列公式。对 $\varepsilon\ge 0$ 最小化。你应得到

$$
P_{\mathrm{cont}}\le\frac{N-1}N\min_{\varepsilon\ge 0}\Bigl[C(I_{\mathrm{th}}-\varepsilon)+\bigl(1-C(I_{\mathrm{th}}-\varepsilon)\bigr)Q(\varepsilon)\Bigr]+\frac1N,
$$

其中 $Q(\varepsilon)$ 是 $\sum_{k=K_0}^{N-1}P(\pi_k(\varepsilon))$ 的上界。

## 9.7 附录 D：Azuma–Hoeffding 不等式

**练习 9.7。** 完成练习 1.10：$Z_k=k\Delta_k$ 是差分有界（bounded differences）的鞅，其中 $D=4+2\sqrt{2}$。应用 Azuma 不等式得到

$$
P(\pi_k(\varepsilon))\le\exp\bigl(-k\varepsilon^2/(2D^2)\bigr).
$$

从 $k=K_0$ 到 $N-1$ 对几何级数求和：

$$
Q(\varepsilon)=\frac{\exp(-K_0\varepsilon^2/(2D^2))-\exp(-N\varepsilon^2/(2D^2))}{1-\exp(-\varepsilon^2/(2D^2))}.
$$

论文还指出 $D=(1-\cos^2(\pi/8))^{-1}$。**练习 9.8。** 验证这一数值上的巧合：$4+2\sqrt{2}\stackrel{?}{=}1/\sin^2(\pi/8)$。（这只是一个有趣的巧合，后文不会使用。）

## 9.8 极限 $N\to\infty$

选择一个比 $N^{-1/2}$ 衰减得*更慢*的 $\varepsilon=\varepsilon(N)$（例如 $N^{-1/3}$）。于是 $Q(\varepsilon)\to 0$，该界趋于 $C(I_{\mathrm{th}})$。当 $I_{\mathrm{th}}\to 2\sqrt{2}$ 时，它等于 $\cos^2(\pi/8)$。

对于图 3，论文采用了以下表达式（图注与正文之间存在一处**已发表的不一致**）：

- 图注：$I_{\mathrm{th}}=2\sqrt{2}\,(1-1/\sqrt{N})$，
- 正文：$I_{\mathrm{th}}=2\sqrt{2}-1/\sqrt{N}$。

**练习 9.9。** 将两者都绘制出来。它们在有限 $N$ 时不同，但具有相同的极限。在你的论文中，选择其中一个，并在图注和正文中统一使用。按照 `scripts/reconstruct_figures.py`，在数值上对式 (19) 关于 $\varepsilon$ 最小化。

Azuma 尾界较为保守（$D=4+2\sqrt{2}$ 是一个粗略的直径）。可以预期，在 $N$ 极大之前，界 (19) 会远高于 $C(I_{\mathrm{th}})$；在图 3 上叠加 $C(I_{\mathrm{th}})$ 可以清楚显示这一差距。已发表的图 3 是式 (19) 的数值最小值，而不是实验结果。

**练习 9.10。** 论文称，因为 $Q(\varepsilon)\ne 0$，有限-$N$ 界很可能不是紧的。你同意吗？松弛出现在哪里？

## 9.9 如何撰写 §5.3 而不让读者淹没在细节中

已发表的证明是一长串不等式。当你重构它时，要让*叙事主线*保持清晰：

1. 对 $n$ 取平均；单独处理未经测试的最后一轮作弊项 $1/N$。
2. 考察一条长度为 $N-1$ 的完整路径；标记测试最后一次能够通过的时刻。
3. 利用凹性，并对小/大 $K$ 进行分拆。
4. 鞅的典型性：$\bar I$ 不可能大幅超过未来各步期望的均值。
5. Azuma $\Rightarrow Q(\varepsilon)\to 0$。

如果读者只记住这五点，他们就能重新推导式 (11)–(19)。

## 检查点

写出上述五点叙事主线。不查看资料，重新写出 $D=4+2\sqrt{2}$ 和式 (19) 的形式。运行 `python scripts/reconstruct_figures.py`，并确认图 3 趋于 $\cos^2(\pi/8)$。
