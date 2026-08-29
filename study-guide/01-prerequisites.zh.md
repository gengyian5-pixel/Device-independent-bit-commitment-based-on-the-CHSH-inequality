# 第 1 节　预备知识

[English](01-prerequisites.md)

在能不看笔记、凭记忆完成本节习题之前，不要打开原论文。后面各节只是把这些事实包进密码学协议里。

## 1.1 量子测量与无信令（no-signalling）

系统 $i$ 上、设置（setting）为 $s$ 的二值测量，是一组 POVM $\{\Pi_{r|s}^i\}_{r=0,1}$，满足 $\Pi_{r|s}^i\succeq 0$ 以及 $\sum_r\Pi_{r|s}^i=\mathbb{1}$。对两体态 $\rho$ 与乘积测量，

$$
P(r^0,r^1\mid s^0,s^1)=\operatorname{Tr}\bigl(\rho\,\Pi_{r^0|s^0}^0\otimes\Pi_{r^1|s^1}^1\bigr).
$$

**习题 1.1。** 证明无信令恒等式

$$
\sum_{r^1}P(r^0,r^1\mid s^0,s^1)=P(r^0\mid s^0)
$$

与 $s^1$ 无关；再写出 Bob 一侧的对称形式。这是论文第 4 节（Alice 的安全性）用到的**唯一**约束。那里**并不**用到量子力学本身。

**习题 1.2。** 为什么“盒子可以带时钟、陀螺仪和记忆”并不破坏上面的公式——只要两只盒子在被测量时彼此不能通信？用一句话写下来，这句话以后会进入你的第 2.2 节。

## 1.2 CHSH 不等式

对二值输入/输出 $x,y,a,b\in\{0,1\}$，CHSH 关联子（correlator）是

$$
I=\sum_{a,b,x,y=0,1}(-1)^{a\oplus b\oplus xy}\,P(a,b\mid x,y).
$$

等价地，若 $A_x,B_y$ 是取值 $\pm 1$ 的可观测量（$A_x=1-2a$ 等），则

$$
I=\langle A_0B_0\rangle+\langle A_0B_1\rangle+\langle A_1B_0\rangle-\langle A_1B_1\rangle.
$$

必须记住的界：

| 理论 | $I$ 的界 | 名称 |
|---|---|---|
| 定域隐变量 | $\lvert I\rvert\le 2$ | CHSH / Bell |
| 量子力学 | $\lvert I\rvert\le 2\sqrt{2}$ | Tsirelson（齐勒尔森） |
| 无信令（不用量子力学） | $\lvert I\rvert\le 4$ | 代数界 / PR 盒 |

**习题 1.3。** 由确定性加上无信令（或用通常的 CHSH 论证）推出定域界 $I\le 2$。

**习题 1.4。** 对 $|\phi^+\rangle=\frac{1}{\sqrt{2}}(|00\rangle+|11\rangle)$ 以及 $zx$ 平面内的可观测量，证明

$$
\langle\phi^+|\sigma_\alpha\otimes\sigma_\beta|\phi^+\rangle=\cos(\alpha-\beta).
$$

然后让 Alice 取角度 $0,\pi/2$，Bob 取 $\pi/4,-\pi/4$（或一组等价的角度），由此恢复 Tsirelson 界。把你用的四个角度写下来；第 5.2 节还会用到这套几何。

**习题 1.5。** 输入均匀随机时，单轮的 *CHSH 指示函数*（indicator）是

$$
I(W)=4\sum_{a,b,x,y}(-1)^{a\oplus b\oplus xy}\,\delta_{A,a}\delta_{B,b}\delta_{X,x}\delta_{Y,y}.
$$

证明 $\mathbb{E}[I(W)]$ 等于上面的 CHSH 表达式。为什么前面有因子 $4$？（这是论文脚注 3。）

## 1.3 伪心灵感应（pseudo-telepathy）对统计性

一个非定域博弈被称为 *伪心灵感应的*，如果存在量子（或无信令）策略以概率 1 取胜，而任何经典策略的胜率都 $<1$。

**习题 1.6。** GHZ 博弈是伪心灵感应的。CHSH 不是：即便 Tsirelson 策略的胜率也只是 $\cos^2(\pi/8)\simeq 0.85$，而不是 1。这对 *互不信任*（distrustful）密码学为什么要紧？在那里 Bob 必须检验非定域性，**同时又**核验 Alice 揭示的比特，而双方不会合作。

用四句话作答。这正是本篇论文的动机。写完后再对照 [02-the-research-question.md](02-the-research-question.md)。

## 1.4 PR 盒

Popescu–Rohrlich 盒是一种无信令资源，满足

$$
r^0\oplus r^1=s^0\cdot s^1,\qquad r^i,s^i\in\{0,1\}
$$

（可差一个局域的输入/输出重标记）。它达到 $I=4$。

**习题 1.7。** 验证 PR 盒满足无信令，并且 CHSH 博弈可以必胜。这就是附录 A 可以丢掉序贯检验的原因：检验盒子与检验承诺可以是**同一次**测量，和 GHZ 协议一样。

## 1.5 当作“承诺凭证”的 EPR 关联

诚实协议需要**同一对**盒子提供两类关联：

1. 在输入对 $\{0,1\}\times\{0,1\}$ 上违反 CHSH。
2. 在“平移”输入对 $(s^0,s^1)=(i,\,i+2\bmod 4)$（$i=0,1,2,3$）上，输出完全相等：$r^0=r^1$。

**习题 1.8（读第 3 节之前做）。** 为盒子 0 和盒子 1 各发明四个角度，都写成 $\sigma_\theta$ 的形式，使得：

- 两边的输入 $(0,1)$ 给出 Tsirelson 的 CHSH 策略；
- 对每个 $i$，盒子 0 在输入 $i$ 下的可观测量，等于盒子 1 在输入 $i+2\bmod 4$ 下的可观测量。

有一套标准答案（论文里的那套）。自己找出来之后，承诺/揭示规则就会变得显然：Alice 的承诺输入是 $b+2$，Bob 的核验输入是 $b$，他们测的是**同一个**可观测量。

## 1.6 量子关联的半定松弛

固定 $I$ 时，Alice 的控制率是未知 Hilbert 空间算符上的多项式优化。NPA 层次（Navascués–Pironio–Acín）给出一串 SDP，其最优值递减并收敛到真正的量子值。

**习题 1.9。** 读适量 NPA（PRL **98**, 010401 (2007) 或 NJP **10**, 073013 (2008)），能回答：

- 什么是 *行为*（behaviour）$P(ab|xy)$？
- 第 $1$ 级和第 $2$ 级的 *矩矩阵*（moment matrix）是什么？
- 为什么一个可行的矩矩阵**不能**证明存在量子实现，而不可行却**能**证明不存在量子实现？

你**不必**重推 NPA。你需要知道：论文解的是 (7) 的 **第 2 级**松弛，然后给出一个显式策略，其 $P_{\mathrm{cont}}$ 与 SDP 数值在 $10^{-8}$ 内吻合。吻合意味着松弛已经收敛。

## 1.7 鞅与 Azuma–Hoeffding 不等式

设 $\{\mathcal{F}_k\}$ 是一个滤子（可以把它想成历史 $\mathbf{W}_k$）。过程 $Z_k$ 是鞅，如果 $\mathbb{E}[Z_{k+1}\mid\mathcal{F}_k]=Z_k$。

**Azuma–Hoeffding。** 若几乎必然有 $\lvert Z_{k+1}-Z_k\rvert\le D$，则对 $\varepsilon>0$，

$$
P\bigl(Z_k-Z_0\ge k\varepsilon\bigr)\le\exp\bigl(-k\varepsilon^2/(2D^2)\bigr).
$$

**习题 1.10。** 定义

$$
\Delta_k=\bar I_k-\frac1k\sum_{n=1}^k\mathbb{E}\bigl[I(W_n)\mid\mathbf{W}_{n-1}\bigr],\qquad Z_k=k\Delta_k.
$$

证明 $Z_k$ 是鞅。只用 $\lvert I(w)\rvert\le 4$ 和 $\lvert\mathbb{E}[I]\rvert\le 2\sqrt{2}$ 给出 $\lvert Z_{k+1}-Z_k\rvert$ 的界。你应得到 $D=4+2\sqrt{2}$。这就是附录 D。

## 1.8 比特承诺的“典故”（约一小时阅读）

阅读、或至少记住以下命题：

- Lo–Chau, PRL **78**, 3410 (1997) 与 Mayers, PRL **78**, 3414 (1997)：不存在 *完美* 的量子比特承诺。
- Spekkens–Rudolph, PRA **65**, 012310 (2001)：不完美的比特承诺是可能的。
- Chailloux–Kerenidis, FOCS 2011：在任何 *平衡* 的量子比特承诺中，$P_{\mathrm{cont}}=P_{\mathrm{gain}}\gtrsim 0.739$。
- Silman 等, PRL **106**, 220501 (2011)：基于 GHZ 的设备无关比特承诺，$P_{\mathrm{cont}}=\cos^2(\pi/8)$，$P_{\mathrm{gain}}=3/4$。
- Kent, PRL **83**, 1447 (1999)：*相对论* 比特承诺可以完美，但至少一方需要两座相距足够远的安全实验室。

**习题 1.11。** 用一段话区分设备无关比特承诺与相对论比特承诺。本文的要点是：每方一座实验室，不要求类空分隔，改用屏蔽（shielding）。

## 检查点

不看笔记能做到下面几条，就可以进入第 2 节：

1. 写出 CHSH 表达式以及三个界：$2$、$2\sqrt{2}$、$4$。
2. 说明为什么 GHZ 是伪心灵感应的，而 CHSH 不是。
3. 用自己的话陈述 $P_{\mathrm{cont}}$ 和 $P_{\mathrm{gain}}$。
4. 背出 Azuma–Hoeffding 不等式。
