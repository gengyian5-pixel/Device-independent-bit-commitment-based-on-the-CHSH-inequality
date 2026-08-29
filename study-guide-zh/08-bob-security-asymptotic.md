# 8. 渐近极限下 Bob 的安全性

论文对应部分：§5.1–5.2。这是技术核心。目标是得到一个函数 $C(I)$，使得当已知承诺/揭示步骤中的盒子满足 $\mathbb{E}[I]\ge I_{\mathrm{th}}$ 时，有 $P_{\mathrm{cont}}\le C(I_{\mathrm{th}})$，并且存在一个达到等号的显式策略。

第 9 章把有限 $N$、带记忆情形约化到这个函数。

## 8.1 将 Alice 的测量仪器约化为一个四结果 POVM

在承诺时，Alice 持有盒子 $c$，还可能持有一个辅助系统。一个完全一般的策略是：

1. 承诺：进行一次产生 $q$ 的二结果测量。
2. 揭示：进行一次依赖于 $q$ 以及她此时想揭示的比特的测量，产生所宣告的 $r^c$。

**习题 8.1。** 论证：如果她想揭示 $0$，Bob 要求 $q=r^c$，所以针对 $b=0$ 的揭示测量是多余的；她不妨从一开始就令 $r^c=q$。因此，在揭示阶段，她只需要与揭示 $1$ 相关的两次测量。将它们与承诺测量合并为**单个四结果 POVM（positive operator-valued measure，正算符值测度）** $\{M_{kl}^c\}_{k,l\in\{0,1\}}$，它作用于 $\mathcal{H}^c$，其含义为：

- 她在承诺时发送 $q=k$；
- 如果揭示 $0$，她宣告 $r^c=k$；
- 如果揭示 $1$，她宣告 $r^c=l$。

这就是论文的不失一般性（w.l.o.g.）约化。请谨慎写出这一部分；审稿人会仔细检查这一段。

**习题 8.2。** Alice 可能知道 $c$（盒子中的一个额外自由度可以对它编码）。因此，$\mathcal{M}^0$ 和 $\mathcal{M}^1$ 可以不同。论文指出，最优解仍然在两个盒子上使用相同的策略，至多相差 Bob 可观测量的一个局域旋转。一个*总是*发送同一盒子的协议会*增大* $P_{\mathrm{cont}}$（Bob 随机选取 $c$ 至关重要）。将此记录为评注，而不是一个必须用 SDP 证明的引理。

## 8.2 将 $P_{\mathrm{cont}}$ 写成四族概率之和

Bob 以 $1/2$ 的概率发送每个盒子。

**揭示 $b=0$**（$s^c=2$）：令牌检查强制要求 $r^c=q=k$。随后 Bob 输入 $s^{\bar c}=0$，并要求 $r^{\bar c}=k$。成功概率为

$$
p_0=\frac12\sum_{k,l}\Bigl[P\bigl(r^1=k,\,(k,l)\mid s^1=0,\mathcal{M}^0\bigr)+P\bigl(r^0=k,\,(k,l)\mid s^0=0,\mathcal{M}^1\bigr)\Bigr].
$$

**揭示 $b=1$**（$s^c=3$）：令牌检查允许任意 $r^c$（即 $r^c=l$）。Bob 输入 $s^{\bar c}=1$，并要求 $r^{\bar c}=l$。类似地定义 $p_1$。

于是 $P_{\mathrm{cont}}=\frac12(p_0+p_1)$，即论文的式 (6)。

**习题 8.3。** 不查看资料，直接从协议的中止条件推导 (6)。(6) 中的因子 $1/4$ 来自 $\frac12\times\frac12$：均匀选取的 $c$ 和均匀选取的预期揭示比特 $b$。

## 8.3 优化问题 (7)

在满足下列条件的量子实现 $\mathcal{Q}=\{\mathcal{H}^c,\rho,\{\Pi_{r|s}^c\},\mathcal{M}^c\}_c$ 上最大化 (6)：

- 两个盒子的 CHSH 值 $\ge I_{\mathrm{th}}$；
- 不同盒子上的算符彼此对易（张量积形式，或者在联合 Hilbert 空间上对易）；
- POVM 约束：$\Pi$ 和 $M$ 均满足正性与完备性。

论文的式 (7) 将其写成单个迹：

$$
P_{\mathrm{cont}}=\frac14\max_{\mathcal{Q}}\operatorname{Tr}\Bigl(\rho\sum_{c,k,l}M_{kl}^c\bigl(\Pi_{k|0}^{\bar c}+\Pi_{l|1}^{\bar c}\bigr)\Bigr).
$$

**习题 8.4。** 验证：与 $\rho$ 一同取迹的算符恰好对应“Bob 的检查通过”这一事件，并且已经对 $c$ 和两种揭示取了平均。

该问题*不是*固定维数的半定规划（semidefinite program，SDP）：$\dim\mathcal{H}$ 未知。需要对它进行松弛。

## 8.4 NPA 层级：实际计算的内容

对 (7) 应用 **第 2 层** NPA 层级（NPA hierarchy）。得到一个上界 $P_{\mathrm{cont}}^{\mathrm{SDP2}}(I_{\mathrm{th}})$。

**习题 8.5。** 列出进入第 2 层矩矩阵（moment matrix）的算符：集合 $\{\Pi_{r|s}^c,M_{kl}^c\}$ 中投影算符的不超过两个因子的乘积。复现论文并不要求编写代码，但如果希望独立复现图 1，可以使用 `ncpol2sdpa`（Python）等软件包，或论文引用的原始 MATLAB+YALMIP+SeDuMi 工具栈。

论文声称：§5.2 的*解析*策略与第 2 层 SDP 的结果在 $10^{-8}$ 精度内一致，因此第 2 层已经收敛。

## 8.5 达到上界的策略（必须手工推导）

阅读 §5.2 前先猜测其几何结构：

- 使用一个 EPR 对 $|\phi^+\rangle$。
- 对于给定盒子，Bob 的两个检查设置应当是 $zx$ 平面内的两条轴，它们**不一定**相差 $\pi/2$（当 $I<2\sqrt{2}$ 时）。
- 收到另一个盒子的 Alice 应当测量 Bob 两条轴的**中间**方向，使她与任一检查设置之间的夹角相同。于是 $p_0=p_1$。
- 一次二结果测量已经足够（所以四结果 POVM 在最优解处显得多余）。在论文的意义下，她把该结果同时宣告为 $b$ 和 $r^c$：她发送的 $b$ 和 $r^c$ 都等于其测量结果。

**习题 8.6。** 如果两个赤道可观测量（equatorial observables）之间的夹角为 $\theta$，证明

$$
P(\text{equal outcomes})=\cos^2(\theta/2)
$$

在 $|\phi^+\rangle$ 上成立。因此，该策略给出

$$
P_{\mathrm{cont}}=\cos^2(\theta/2).
$$

在 Tsirelson 点，Alice 与两条正交轴中的每一条都相差 $\pi/4$，所以 $\theta=\pi/4$ 且 $P_{\mathrm{cont}}=\cos^2(\pi/8)$。这是从 CHSH 几何中得到的 GHZ 数值。

**习题 8.7。** 复现论文的参数化：

- 盒子 0，输入 0 和 1：$\sigma_{2\theta}$ 和 $\sigma_z$。
- 盒子 1，输入 0 和 1：$\sigma_{2\theta-\varphi}$ 和 $\sigma_{4\theta-\varphi}$。
- 如果 Alice 得到盒子 0，她测量 $\sigma_{3\theta-\varphi}$；如果得到盒子 1，她测量 $\sigma_{\theta}$。

画出图 2：实线轴 = Bob 在盒子 0 上的测量，虚线轴 = Bob 在盒子 1 上的测量，点线轴 = Alice 的测量。它们全都位于 $zx$ 平面内。检查 Alice 的测量始终位于中间位置，半角为 $\theta$。

**习题 8.8。** 利用 $\langle\sigma_\alpha\otimes\sigma_\beta\rangle=\cos(\alpha-\beta)$，计算 Bob 的四个可观测量（两个盒子上的输入均为 $0,1$）的 CHSH 值：

$$
I=\langle\sigma_{2\theta}\otimes\sigma_{2\theta-\varphi}+\sigma_{2\theta}\otimes\sigma_{4\theta-\varphi}+\sigma_z\otimes\sigma_{2\theta-\varphi}-\sigma_z\otimes\sigma_{4\theta-\varphi}\rangle.
$$

将其化简为论文的式 (9)：

$$
I=2\cos(2\theta-\varphi)-\cos(4\theta-\varphi)+\cos\varphi.
$$

**习题 8.9。** 对固定的 $\theta$，在 $I$ 上关于 $\varphi$ 取最大值。证明一个临界点为

$$
\varphi_{\mathrm{opt}}=\arccos\Biggl(2\frac{\cos(2\theta)+\sin^2(2\theta)}{\sqrt{6-2\cos(4\theta)}}\Biggr).
$$

（对 (9) 求导并求解 $\partial I/\partial\varphi=0$。该反余弦形式是一个特解；在 $\theta=\pi/4$ 处检验它，此时必须得到 $\varphi_{\mathrm{opt}}=\pi/4$ 和 $I=2\sqrt{2}$。）

**习题 8.10。** 消去 $\varphi$，得到参数曲线 $(I(\theta),P_{\mathrm{cont}}(\theta))$，其中 $\theta\in(0,\pi/2]$。这就是图 1。在 `scripts/reconstruct_figures.py` 中实现它。

特殊值：

| $\theta$ | $P_{\mathrm{cont}}$ | $I$（取 $\varphi_{\mathrm{opt}}$） | 含义 |
|---|---|---|---|
| $\pi/4$ | $\cos^2(\pi/8)\simeq 0.8536$ | $2\sqrt{2}$ | Tsirelson / GHZ 一致 |
| $\to 0$ | $\to 1$ | $\to$ 某个 $\le 2$ 的值 | Alice 几乎是确定性的；CHSH 不可能仍高于 2 |

**习题 8.11。** 计算 $I$ 在 $\theta\to 0$ 且取 $\varphi_{\mathrm{opt}}$ 时的值。你应当看到，Alice 若要令 $P_{\mathrm{cont}}\to 1$，就必须放弃 Bell 违反，这与预期一致。

## 8.6 如何撰写 §5.1–5.2

论文中的顺序（沿用此结构）：

1. 不失一般性的四结果 POVM。
2. 两种揭示对应的表达式 (6)。
3. SDP (7) 和 NPA 第 2 层。
4. 显式策略、(8)–(10) 和图 2。
5. 说明 (8)–(10) 达到 SDP 上界，因此图 1 是紧的。

不要颠倒第 3 项和第 4 项：SDP 是*上*界；策略是*下*界；二者共同给出精确的量子值。

## 检查点

凭记忆回答：(i) 为什么一个四结果承诺 POVM 就足够；(ii) $P_{\mathrm{cont}}=\cos^2(\theta/2)$；(iii) 习题 8.7 的测量表；(iv) 为什么会出现 $\cos^2(\pi/8)$。
