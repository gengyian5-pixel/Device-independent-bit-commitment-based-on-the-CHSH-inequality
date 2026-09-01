# Appendices and References / 附录与参考文献

## Appendix A / 附录 A

**English original**

We present a device-independent bit commitment protocol using a PR box [46].

**中文译文**

我们提出一种使用 PR 盒 [46] 的设备无关比特承诺协议。

**English original**

We have seen that reformulating the GHZ-based protocol of [30] to be CHSH-based comes at the price of pseudo-telepathy. Indeed, quantum theory does not allow for pseudo-telepathy in a two-party, two-input setting [39]. However, in a post-quantum world – in which both dishonest and honest parties are restricted only by the no-signaling constraints -- pseudo-telepathy is restored. It is interesting to ask what would happen to our protocol if we were to adapt it to such a world. On the one hand, we might expect such a world to offer less security since a dishonest party would now have access to stronger correlations. On the other hand, we might expect the converse, since the protocol itself can be modified to make use of these stronger correlations. We will see that on the balance this allows for more security.[^5]

**中文译文**

我们已经看到，将 [30] 中基于 GHZ 的协议改写为基于 CHSH 的协议，是以失去伪心灵感应为代价的。事实上，量子理论不允许在双方、双输入的场景中出现伪心灵感应 [39]。然而，在一个后量子世界中——无论不诚实方还是诚实方都只受无信号约束限制——伪心灵感应得以恢复。值得探究的是，如果我们调整协议以适应这样的世界，会发生什么。一方面，我们或许预期这样的世界安全性较低，因为不诚实方现在可以利用更强的关联。另一方面，我们也可能预期相反的结果，因为协议本身可以修改以利用这些更强的关联。我们将看到，总体而言，这会带来更高的安全性。[^5]

**English original**

A PR box is a post-quantum, bipartite, two-input, two-output resource, which achieves the algebraic bound of the CHSH inequality, while at the same time satisfying the no-signaling constraints. Up to local relabeling of the inputs and outputs, the PR box satisfies

**中文译文**

PR 盒是一种后量子的、二分的、双输入双输出资源；它在达到 CHSH 不等式代数界的同时满足无信号约束。在不计输入和输出的局部重新标记时，PR 盒满足

**English original**

$$
r^{0}\oplus r^{1}=s^{0}\cdot s^{1}\,,\qquad r^{i},\,s^{i}\in\{0,\,1\}\,.
\tag{20}
$$

**中文译文**

$$
r^{0}\oplus r^{1}=s^{0}\cdot s^{1}\,,\qquad r^{i},\,s^{i}\in\{0,\,1\}\,.
\tag{20}
$$

**English original**

In the following, it will be convenient to think of the PR box as consisting of a pair of two-input, two-output boxes, one in the possession of Alice, and the other in the possession of Bob.

**中文译文**

下文中，为方便起见，可将 PR 盒视为由一对双输入双输出盒组成，其中一个由 Alice 持有，另一个由 Bob 持有。

**English original**

The PR-based protocol is essentially a simplified version of our earlier protocols with the first step (statistical estimation of the CHSH violation and random selection of the box used to encode Alice’s commitment) omitted, and with the verification of nonlocal correlations and Alice’s commitment being performed at the same time. This last possibility follows from pseudo-telepathy, as in the protocol of [30].

**中文译文**

基于 PR 的协议本质上是我们先前协议的简化版本：省略了第一步（对 CHSH 违反进行统计估计，以及随机选择用于编码 Alice 承诺的盒），并同时执行非局域关联验证与 Alice 的承诺。后一种做法源于伪心灵感应，正如 [30] 的协议一样。

**English original**

We assume that at the start of the protocol Alice has box $0$ and Bob has box $1$ . The protocol proceeds as follows:

**中文译文**

我们假设在协议开始时，Alice 持有盒 $0$，Bob 持有盒 $1$。协议步骤如下：

**English original**

1. Commit phase - Alice inputs into her box the value of the bit she wishes to commit. She then selects uniformly at random a classical bit $a$ , and sends Bob another classical bit, $q=r^{0}\oplus(as^{0})$ , as a token of her commitment.

**中文译文**

1. 承诺阶段——Alice 将她希望承诺的比特值输入自己的盒。随后，她均匀随机地选择一个经典比特 $a$，并向 Bob 发送另一个经典比特 $q=r^{0}\oplus(as^{0})$，作为其承诺的凭证。

**English original**

2. Reveal phase - Alice sends Bob $s^{0}$ and $r^{0}$ . Bob checks whether $q=r^{0}$ or $q=r^{0}\oplus s^{0}$ . If both relations are not satisfied, he aborts. Otherwise, he picks an input $s^{1}$ uniformly at random and verifies that $r^{0}\oplus r^{1}=s^{0}\cdot s^{1}$ . If this last test fails, he aborts.

**中文译文**

2. 揭示阶段——Alice 向 Bob 发送 $s^{0}$ 和 $r^{0}$。Bob 检查 $q=r^{0}$ 或 $q=r^{0}\oplus s^{0}$ 是否成立。如果两个关系均不成立，他就中止协议。否则，他均匀随机地选择一个输入 $s^{1}$，并验证 $r^{0}\oplus r^{1}=s^{0}\cdot s^{1}$。如果最后这项检验失败，他就中止协议。

### Alice’s security / Alice 的安全性

**English original**

We recall that in the quantum case (both in the GHZ-based and CHSH-based formulations) Alice’s security relies only on the no-signaling constraints. Since we are still working in a non-signaling setting, Alice’s security will remain unchanged, i.e. Bob’s information gain is upper-bounded by $\frac{3}{4}$ . The proof proceeds exactly as in Subsection IV.A, except that the instead of inputting $2$ and $3$ , Alice inputs $0$ and $1$ .

**中文译文**

回顾量子情形（无论基于 GHZ 还是基于 CHSH 的表述），Alice 的安全性仅依赖于无信号约束。由于我们仍在无信号场景中讨论，Alice 的安全性保持不变，即 Bob 的信息增益上界为 $\frac{3}{4}$。证明与第 IV.A 小节完全相同，唯一的区别是 Alice 输入 $0$ 和 $1$，而不是输入 $2$ 和 $3$。

**English original**

One optimal strategy for Bob is to assume that $q=r^{0}$ , and input $s^{1}=1$ , obtaining an output $r^{1}$ . He then guesses $g=r^{0}\oplus r^{1}$ . When $s^{0}=0$ , $q=r^{0}$ and Bob’s guess, $g=r^{0}\oplus r^{1}=s^{0}$ , is correct. When $s^{0}=1$ and $a=0$ , $q=r^{0}$ and Bob’s guess, $g=r^{0}\oplus r^{1}=s^{0}$ , is again correct. However, when $s^{0}=1$ and $a=1$ , $q=r^{0}\oplus 1$ and Bob’s guess, $g=r^{0}\oplus r^{1}\oplus 1=s^{0}\oplus 1$ , is wrong. Since Alice is honest she picks $a$ uniformly at random, implying that $P_{\mathrm{gain}}=\frac{3}{4}$ .

**中文译文**

Bob 的一种最优策略是假设 $q=r^{0}$，并输入 $s^{1}=1$，得到输出 $r^{1}$。然后他猜测 $g=r^{0}\oplus r^{1}$。当 $s^{0}=0$ 时，$q=r^{0}$，且 Bob 的猜测 $g=r^{0}\oplus r^{1}=s^{0}$ 正确。当 $s^{0}=1$ 且 $a=0$ 时，$q=r^{0}$，Bob 的猜测 $g=r^{0}\oplus r^{1}=s^{0}$ 仍然正确。然而，当 $s^{0}=1$ 且 $a=1$ 时，$q=r^{0}\oplus 1$，Bob 的猜测 $g=r^{0}\oplus r^{1}\oplus 1=s^{0}\oplus 1$ 是错误的。由于 Alice 是诚实的，她均匀随机地选择 $a$，这意味着 $P_{\mathrm{gain}}=\frac{3}{4}$。

### Bob’s security / Bob 的安全性

**English original**

Recall that in a device-independent scenario dishonest Alice can prepare the boxes in any state she wishes, possibly entangled with ancillary systems in her possession. Since in the commit phase Alice sends a classical bit $q$ as a token of her commitment, without receiving any information from Bob, without loss of generality we may assume that she decides on the value of $q$ before the start of the protocol, and accordingly prepares the boxes to maximize $P_{\mathrm{cont}}$ . Furthermore, since Alice’s cheating probability is invariant under the simultaneous relabeling $q\rightarrow q\oplus 1$ and $r^{0}\rightarrow r^{0}\oplus 1$ , no value of $q$ is preferable, and we may assume that she sends $q=0$ .

**中文译文**

回顾设备无关场景，不诚实的 Alice 可以按自己的意愿将盒制备为任意状态，这些盒还可能与她持有的辅助系统纠缠。由于在承诺阶段，Alice 在未从 Bob 接收任何信息的情况下发送经典比特 $q$ 作为承诺凭证，因此不失一般性，可以假设她在协议开始前就决定 $q$ 的值，并据此制备盒以最大化 $P_{\mathrm{cont}}$。此外，由于 Alice 的作弊概率在同时重新标记 $q\rightarrow q\oplus 1$ 和 $r^{0}\rightarrow r^{0}\oplus 1$ 下不变，因此没有哪个 $q$ 值更有利，我们可以假设她发送 $q=0$。

**English original**

Suppose now that Alice wishes to reveal $0$ . Since $s^{0}=0$ , it follows that Alice must send $r^{0}=0$ as Bob will first check whether $r^{0}=0$ or not. Bob will then test whether the PR box correlations, Eq. (20), are satisfied: Bob will uniformly at random pick a value of $s^{1}$ and verify that $r^{1}=0$ . Alice’s control in this case equals $\frac{1}{2}\left[P\left(r^{1}=0|s^{1}=0\right)+P\left(r^{1}=0|s^{1}=1\right)\right]$ . Suppose now that Alice wishes to reveal $1$ , then both values of $r^{1}$ are possible, and the only relevant test is whether the PR box correlations are satisfied. Alice’s control in this case equals $\frac{1}{2}\sum_{r^{0}=0,\,1}\left[P\left(r^{0},\,r^{1}=r^{0}|s^{0}=1,\,s^{1}=0\right)+P\left(r^{0},\,r^{1}=r^{0}\oplus 1|s^{0}=1,\,s^{1}=1\right)\right]$ . Alice’s overall control is obtained by maximizing

**中文译文**

现在假设 Alice 希望揭示 $0$。由于 $s^{0}=0$，Alice 必须发送 $r^{0}=0$，因为 Bob 首先会检查 $r^{0}=0$ 是否成立。随后，Bob 将检验 PR 盒关联式 (20) 是否成立：Bob 均匀随机地选取一个 $s^{1}$ 值，并验证 $r^{1}=0$。在这种情况下，Alice 的控制力等于 $\frac{1}{2}\left[P\left(r^{1}=0|s^{1}=0\right)+P\left(r^{1}=0|s^{1}=1\right)\right]$。现在假设 Alice 希望揭示 $1$，那么 $r^{1}$ 的两个值都可能出现，唯一相关的检验是 PR 盒关联是否成立。在这种情况下，Alice 的控制力等于 $\frac{1}{2}\sum_{r^{0}=0,\,1}\left[P\left(r^{0},\,r^{1}=r^{0}|s^{0}=1,\,s^{1}=0\right)+P\left(r^{0},\,r^{1}=r^{0}\oplus 1|s^{0}=1,\,s^{1}=1\right)\right]$。Alice 的总体控制力通过最大化下式得到：

**English original**

$$
\begin{aligned}
&\frac{1}{4}\left[P(r^{1}=0|s^{1}=0)+P(r^{1}=0|s^{1}=1)\right.\\
&\quad+\sum_{r^{0}=0,\,1}\bigl(P(r^{0},\,r^{1}=r^{0}\mid s^{0}=1,\,s^{1}=0)+\left.P(r^{0},\,r^{1}=r^{0}\oplus 1\mid s^{0}=1,\,s^{1}=1)\bigl)\right]\\
&=\frac{1}{4}\left[P(r^{1}=0|s^{1}=0)+P(r^{1}=0|s^{1}=1)\right.\\
&\quad+P(r^{0}=0,\,r^{1}=0\mid s^{0}=1,\,s^{1}=0)+P(r^{0}=0,\,r^{1}=1\mid s^{0}=1,\,s^{1}=1)\\
&\quad+P(r^{0}=1,\,r^{1}=1\mid s^{0}=1,\,s^{1}=0)+\left.P(r^{0}=1,\,r^{1}=0\mid s^{0}=1,\,s^{1}=1)\right]
\end{aligned}
\tag{21}
$$

**中文译文**

$$
\begin{aligned}
&\frac{1}{4}\left[P(r^{1}=0|s^{1}=0)+P(r^{1}=0|s^{1}=1)\right.\\
&\quad+\sum_{r^{0}=0,\,1}\bigl(P(r^{0},\,r^{1}=r^{0}\mid s^{0}=1,\,s^{1}=0)+\left.P(r^{0},\,r^{1}=r^{0}\oplus 1\mid s^{0}=1,\,s^{1}=1)\bigl)\right]\\
&=\frac{1}{4}\left[P(r^{1}=0|s^{1}=0)+P(r^{1}=0|s^{1}=1)\right.\\
&\quad+P(r^{0}=0,\,r^{1}=0\mid s^{0}=1,\,s^{1}=0)+P(r^{0}=0,\,r^{1}=1\mid s^{0}=1,\,s^{1}=1)\\
&\quad+P(r^{0}=1,\,r^{1}=1\mid s^{0}=1,\,s^{1}=0)+\left.P(r^{0}=1,\,r^{1}=0\mid s^{0}=1,\,s^{1}=1)\right]
\end{aligned}
\tag{21}
$$

**English original**

and is easily seen to be no greater than $\frac{3}{4}$ .

**中文译文**

并且很容易看出，其值不超过 $\frac{3}{4}$。

**English original**

Alice’s optimal strategy is to prepare Bob’s box such that $P(r^{1}=0|s^{1}=0)=P(r^{1}=0|s^{1}=1)=1$ , i.e. a classical box.

**中文译文**

Alice 的最优策略是将 Bob 的盒制备为满足 $P(r^{1}=0|s^{1}=0)=P(r^{1}=0|s^{1}=1)=1$ 的盒，即一个经典盒。

[^5]: **English original:** The authors of [47] presented a perfect bit commitment protocol, assuming that honest parties have access to PR boxes and dishonest parties cannot tamper with them. We do not make these assumptions.  
      **中文译文：** [47] 的作者提出了一种完美比特承诺协议，其假设诚实方可以使用 PR 盒，且不诚实方无法篡改这些盒。我们不作这些假设。

## Appendix B / 附录 B

**English original**

In this appendix we consider a modification of the protocol, such that the reveal time can be chosen at will. This comes at the price of increasing Alice’s control. The protocol proceeds as follows:

**中文译文**

本附录考虑对协议的一种修改，使揭示时间可以任意选择。其代价是增大 Alice 的控制力。协议步骤如下：

**English original**

1. Random selection – At time $t^{a}<t_{1}$ Bob picks uniformly at random, and in private, a number $n\in\{1,\,\dots,\,N\}$ and two input strings $\mathrm{\mathbf{s}}^{0}_{n}\in\{0,\,1\}^{n}$ and $\mathrm{\mathbf{s}}^{1}_{n}\in\{0,\,1\}^{n}$ . At each of the $n$ times $t_{i}$ he feeds $s^{0}_{i}$ and $s^{1}_{i}$ into boxes $0$ and $1$ , respectively. He uses the corresponding output strings $\mathrm{\mathbf{r}}^{0}_{n}$ and $\mathrm{\mathbf{r}}^{1}_{n}$ to compute the observed CHSH violation, $\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})$ , and compares it to some previously agreed threshold $I_{\mathrm{th}}$ . If $\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})<I_{\mathrm{th}}$ , he aborts the protocol. Otherwise, he flips two classical coins. Denote their outcomes by $c$ and $d$ . At time $t^{b}<t_{n+1}$ he sends box $c$ to Alice. At time $t_{n+1}$ , he inputs $s_{n+1}^{\bar{c}}=d$ into box $\bar{c}$ .

**中文译文**

1. 随机选择——在时刻 $t^{a}<t_{1}$，Bob 私下均匀随机地选取一个数 $n\in\{1,\,\dots,\,N\}$ 和两个输入串 $\mathrm{\mathbf{s}}^{0}_{n}\in\{0,\,1\}^{n}$、$\mathrm{\mathbf{s}}^{1}_{n}\in\{0,\,1\}^{n}$。在 $n$ 个时刻 $t_i$ 中的每一个时刻，他分别将 $s^{0}_{i}$ 和 $s^{1}_{i}$ 输入盒 $0$ 和盒 $1$。他使用相应的输出串 $\mathrm{\mathbf{r}}^{0}_{n}$ 和 $\mathrm{\mathbf{r}}^{1}_{n}$ 计算观测到的 CHSH 违反 $\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})$，并将其与事先约定的阈值 $I_{\mathrm{th}}$ 比较。如果 $\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})<I_{\mathrm{th}}$，他就中止协议。否则，他抛掷两枚经典硬币，将结果记为 $c$ 和 $d$。在时刻 $t^{b}<t_{n+1}$，他将盒 $c$ 发送给 Alice。在时刻 $t_{n+1}$，他把 $s_{n+1}^{\bar{c}}=d$ 输入盒 $\bar{c}$。

**English original**

2. Commit phase – Let $b$ be the value of the bit Alice wishes to commit. Alice inputs $s^{c}_{n+1}=b+2$ into her box. She then selects uniformly at random a classical bit $a$ , and at time $t^{c}>t^{b}$ sends Bob the classical bit $q=r^{c}_{n+1}\oplus ab$ as a token of her commitment.

**中文译文**

2. 承诺阶段——令 $b$ 为 Alice 希望承诺的比特值。Alice 将 $s^{c}_{n+1}=b+2$ 输入她的盒。随后，她均匀随机地选择一个经典比特 $a$，并在时刻 $t^{c}>t^{b}$ 向 Bob 发送经典比特 $q=r^{c}_{n+1}\oplus ab$，作为其承诺的凭证。

**English original**

3. Reveal phase – At any time of her choosing $t>t^{c}$ Alice sends Bob $b$ and $r^{c}_{n+1}$ . Bob checks whether $q=r^{c}_{n+1}$ or $q=r^{c}_{n+1}\oplus b$ . If both relations are not satisfied, he aborts. Otherwise, if $s^{\bar{c}}_{n+1}=s^{c}_{n+1}-2$ (i.e. $d=b-2$ ) he verifies that $r^{\bar{c}}_{n+1}=r^{c}_{n+1}$ . If this last test fails, he aborts.

**中文译文**

3. 揭示阶段——在 Alice 选择的任意时刻 $t>t^{c}$，她向 Bob 发送 $b$ 和 $r^{c}_{n+1}$。Bob 检查 $q=r^{c}_{n+1}$ 或 $q=r^{c}_{n+1}\oplus b$ 是否成立。如果两个关系均不成立，他就中止协议。否则，如果 $s^{\bar{c}}_{n+1}=s^{c}_{n+1}-2$（即 $d=b-2$），他就验证 $r^{\bar{c}}_{n+1}=r^{c}_{n+1}$。如果最后这项检验失败，他就中止协议。

### Alice’s security / Alice 的安全性

**English original**

Clearly, the analysis of Alice’s security remains the same as in the original protocol.

**中文译文**

显然，对 Alice 安全性的分析与原协议相同。

### Bob’s security / Bob 的安全性

**English original**

Bob’s random choice of the $n+1\,$ th input into box $\bar{c}$ implies that half the time he will not be able to carry out the last test in the reveal phase and will accept whatever value dishonest Alice reveals, independently of her cheating strategy. The remaining half of the time, Bob’s actions will precisely be identical to those analyzed previously (in particular, the last input is introduced into box $\bar{c}$ at time $t_{n+1}$ , and thus, unless $n=N$ , this box cannot tell whether it is measured in the random selection phase or the reveal phase). Alice’s control is therefore modified as follows: $P_{\mathrm{cont}}\rightarrow\frac{1}{2}(P_{\mathrm{cont}}+1)$ .

**中文译文**

Bob 随机选择盒 $\bar{c}$ 的第 $n+1$ 个输入，这意味着有一半时间他无法执行揭示阶段的最后一项检验，并且无论不诚实的 Alice 采用何种作弊策略，他都会接受她揭示的任何值。在其余一半时间里，Bob 的操作与先前分析的操作完全相同（特别是，最后一个输入在时刻 $t_{n+1}$ 被送入盒 $\bar{c}$；因此，除非 $n=N$，该盒无法判断自己是在随机选择阶段还是揭示阶段被测量）。因此，Alice 的控制力修改为：$P_{\mathrm{cont}}\rightarrow\frac{1}{2}(P_{\mathrm{cont}}+1)$。

## Appendix C / 附录 C

**English original**

In this appendix we consider the large office scenario, where Bob has a large number of pairs of boxes, and where the boxes in each pair can not only be prevented from communicating with one another, but also with the other pairs. While impractical, this scenario allows us to modify the protocol such that the reveal time can be chosen at will while maintaining the same level of security.

**中文译文**

本附录考虑“大办公室”场景，其中 Bob 拥有大量盒对，并且不仅能阻止每一对中的盒相互通信，也能阻止它们与其他盒对通信。尽管不切实际，这一场景使我们能够修改协议，使揭示时间可以任意选择，同时维持相同的安全水平。

**English original**

Before we begin, we adapt the notation to this new scenario. We consider $N+1$ pairs[^6] of four-input, $\{0,\,1,\,2,\,3\}$ , two-output, $\{0,\,1\}$ , boxes. The random variables designating the input and output of the $i\,$ th box ( $i\in\{0,\,1\}$ ) of the $k\,$ th pair will be labeled by $S^{i}_{k}$ and $R^{i}_{k}$ , respectively, with a specific realization being labeled by lower-case letters $s^{i}_{k}$ and $r^{i}_{k}$ . We also define $W_{k}=\{S^{0}_{k},\,S^{1}_{k},\,R^{0}_{k},\,R^{1}_{k}\}$ and $\mathbf{W}_{n}=\{W_{1},\,\dots,\,W_{n}\}$ . Finally, we define the random strings $\mathbf{S}^{i}_{\bar{n}}=\{S^{i}_{1},\,\dots,\,S^{i}_{n-1},\,S^{i}_{n+1},\,\dots,\,S^{i}_{N+1}\}$ , $\mathbf{R}^{i}_{\bar{n}}=\{R^{i}_{1},\,\dots,\,R^{i}_{n-1},\,R^{i}_{n+1},\,\dots,\,R^{i}_{N+1}\}$ , and $\mathbf{W}_{\bar{n}}=\{W_{1},\,\dots,\,W_{n-1},\,W_{n+1},\,\dots,\,W_{N+1}\}$ .

**中文译文**

开始之前，我们先使记号适应这一新场景。考虑 $N+1$ 对[^6]四输入 $\{0,\,1,\,2,\,3\}$、双输出 $\{0,\,1\}$ 的盒。表示第 $k$ 对中第 $i$ 个盒（$i\in\{0,\,1\}$）的输入和输出的随机变量，分别记为 $S^{i}_{k}$ 和 $R^{i}_{k}$；其具体实现值以小写字母 $s^{i}_{k}$ 和 $r^{i}_{k}$ 表示。我们还定义 $W_{k}=\{S^{0}_{k},\,S^{1}_{k},\,R^{0}_{k},\,R^{1}_{k}\}$ 和 $\mathbf{W}_{n}=\{W_{1},\,\dots,\,W_{n}\}$。最后，定义随机串 $\mathbf{S}^{i}_{\bar{n}}=\{S^{i}_{1},\,\dots,\,S^{i}_{n-1},\,S^{i}_{n+1},\,\dots,\,S^{i}_{N+1}\}$、$\mathbf{R}^{i}_{\bar{n}}=\{R^{i}_{1},\,\dots,\,R^{i}_{n-1},\,R^{i}_{n+1},\,\dots,\,R^{i}_{N+1}\}$ 以及 $\mathbf{W}_{\bar{n}}=\{W_{1},\,\dots,\,W_{n-1},\,W_{n+1},\,\dots,\,W_{N+1}\}$。

**English original**

The protocol proceeds as follows:

**中文译文**

协议步骤如下：

**English original**

1. Random selection – Bob picks uniformly at random and in private a number $n\in\{1,\,\dots,\,N+1\}$ and a classical bit $c$ . He sends box $c$ of the $n\,$ th pair to Alice.

**中文译文**

1. 随机选择——Bob 私下均匀随机地选取一个数 $n\in\{1,\,\dots,\,N+1\}$ 和一个经典比特 $c$。他将第 $n$ 对中的盒 $c$ 发送给 Alice。

**English original**

2. Commit phase – Let $b$ be the value of the bit Alice wishes to commit. Alice inputs $s^{c}_{n}=b+2$ into her box. She then selects uniformly at random a classical bit $a$ , and sends Bob the classical bit $q=r^{c}_{n+1}\oplus ab$ as a token of her commitment.

**中文译文**

2. 承诺阶段——令 $b$ 为 Alice 希望承诺的比特值。Alice 将 $s^{c}_{n}=b+2$ 输入她的盒。随后，她均匀随机地选择一个经典比特 $a$，并向 Bob 发送经典比特 $q=r^{c}_{n+1}\oplus ab$，作为其承诺的凭证。

**English original**

3. Reveal phase – Alice sends Bob $b$ and $r^{c}_{n}$ . Bob checks whether $q=r^{c}_{n}$ or $q=r^{c}_{n}\oplus b$ . If both relations are not satisfied, he aborts. Otherwise, he picks uniformly at random two input strings $\mathrm{\mathbf{s}}^{0}_{\bar{n}}\in\{0,\,1\}^{N}$ and $\mathrm{\mathbf{s}}^{1}_{\bar{n}}\in\{0,\,1\}^{N}$ , which he feeds into the corresponding boxes. At the same time he feeds $s^{\bar{c}}_{n}=s^{c}_{n}-2=b$ into box $\bar{c}$ of the $n\,$ th pair. If $r^{\bar{c}}_{n+1}\neq r^{c}_{n+1}$ , he aborts. Else, he uses the corresponding output strings $\mathrm{\mathbf{r}}^{0}_{\bar{n}}$ and $\mathrm{\mathbf{r}}^{1}_{\bar{n}}$ to compute the observed CHSH violation $\bar{I}_{\bar{n}}(\mathbf{w}_{\bar{n}})=\frac{1}{N}\sum_{k\neq n}I(w_{k})$ and compares it to some previously agreed threshold $I_{\mathrm{th}}$ . If this last test fails, he aborts.

**中文译文**

3. 揭示阶段——Alice 向 Bob 发送 $b$ 和 $r^{c}_{n}$。Bob 检查 $q=r^{c}_{n}$ 或 $q=r^{c}_{n}\oplus b$ 是否成立。如果两个关系均不成立，他就中止协议。否则，他均匀随机地选择两个输入串 $\mathrm{\mathbf{s}}^{0}_{\bar{n}}\in\{0,\,1\}^{N}$ 和 $\mathrm{\mathbf{s}}^{1}_{\bar{n}}\in\{0,\,1\}^{N}$，并将其送入相应的盒。同时，他将 $s^{\bar{c}}_{n}=s^{c}_{n}-2=b$ 输入第 $n$ 对的盒 $\bar{c}$。如果 $r^{\bar{c}}_{n+1}\neq r^{c}_{n+1}$，他就中止协议。否则，他使用相应的输出串 $\mathrm{\mathbf{r}}^{0}_{\bar{n}}$ 和 $\mathrm{\mathbf{r}}^{1}_{\bar{n}}$ 计算观测到的 CHSH 违反 $\bar{I}_{\bar{n}}(\mathbf{w}_{\bar{n}})=\frac{1}{N}\sum_{k\neq n}I(w_{k})$，并将其与事先约定的阈值 $I_{\mathrm{th}}$ 比较。如果最后这项检验失败，他就中止协议。

### Alice’s security / Alice 的安全性

**English original**

Clearly, the analysis of Alice’s security remains the same as in the original protocol.

**中文译文**

显然，对 Alice 安全性的分析与原协议相同。

### Bob’s security / Bob 的安全性

**English original**

We will not derive here the dependence of Alice’s control on the number of pairs $N+1$ . Instead, we will show that it is upper-bounded by that of the original protocol (Section III). To see this, consider another protocol, identical to the one above in all except that instead of using the inputs and outputs of all the pairs (bar the one chosen for the commitment) to estimate the CHSH violation, Bob uses only those of the first $n-1$ pairs (Alice is of course aware of this and of the numbering of the pairs). Clearly, the new protocol can only increase Alice’s control.

**中文译文**

这里我们不推导 Alice 的控制力对盒对数 $N+1$ 的依赖关系。相反，我们将证明它的上界为原协议（第 III 节）中的控制力。为说明这一点，考虑另一个协议：除了 Bob 不使用所有盒对（用于承诺的那一对除外）的输入和输出来估计 CHSH 违反，而只使用前 $n-1$ 对的输入和输出以外，该协议与上述协议完全相同（Alice 当然知道这一点，也知道各盒对的编号）。显然，新协议只可能增大 Alice 的控制力。

**English original**

Now we note that this protocol would be identical to that of the sequential case, up to the fact that the reveal time can be chosen at will,[^7] if box $i$ of pair $k$ were to have full information about the inputs and outputs of all the $i\,$ th boxes of the first $k-1$ pairs. Clearly, such a modification can only increase Alice’s control.

**中文译文**

现在注意到，如果第 $k$ 对的盒 $i$ 拥有前 $k-1$ 对中所有第 $i$ 个盒的输入和输出的完整信息，那么除揭示时间可以任意选择这一点外，[^7]该协议将与顺序情形的协议相同。显然，这种修改只可能增大 Alice 的控制力。

**English original**

We therefore conclude that Alice’s control in the sequential case provides an upper bound on her control in the large office scenario.

**中文译文**

因此我们得出结论：顺序情形下 Alice 的控制力为她在大办公室场景中的控制力提供了一个上界。

[^6]: **English original:** In the original protocol the maximum number of uses of each box equals $N+1$ ( $n\in\{1,\,N\}$ for the CHSH estimation and $1$ for the commitment).  
      **中文译文：** 在原协议中，每个盒的最大使用次数等于 $N+1$（用于 CHSH 估计的次数为 $n\in\{1,\,N\}$，用于承诺的次数为 $1$）。

[^7]: **English original:** Unlike in the sequential case, timing issues do not arise here since the measurements for the CHSH estimation and on box $\bar{c}$ of pair $n$ are simultaneous.  
      **中文译文：** 与顺序情形不同，这里不会出现时序问题，因为用于 CHSH 估计的测量与对第 $n$ 对的盒 $\bar{c}$ 所作的测量是同时进行的。

## Appendix D / 附录 D

**English original**

Let

**中文译文**

令

**English original**

$$
\Delta_{k}(\mathrm{\mathbf{W}}_{k})=\bar{I}_{k}(\mathrm{\mathbf{W}}_{k})-\frac{1}{k}\sum_{n=1}^{k}E(I(W_{n})|\mathrm{\mathbf{W}}_{n-1})=\frac{1}{k}\sum_{n=1}^{k}\bigl(I(W_{n})-E(I(W_{n})|\mathrm{\mathbf{W}}_{n-1})\bigr)\,,\qquad k\leq N-1\,.
\tag{22}
$$

**中文译文**

$$
\Delta_{k}(\mathrm{\mathbf{W}}_{k})=\bar{I}_{k}(\mathrm{\mathbf{W}}_{k})-\frac{1}{k}\sum_{n=1}^{k}E(I(W_{n})|\mathrm{\mathbf{W}}_{n-1})=\frac{1}{k}\sum_{n=1}^{k}\bigl(I(W_{n})-E(I(W_{n})|\mathrm{\mathbf{W}}_{n-1})\bigr)\,,\qquad k\leq N-1\,.
\tag{22}
$$

**English original**

It is straightforward to show that $Z_{k}(\mathrm{\mathbf{W}}_{k})=k\Delta_{k}(\mathrm{\mathbf{W}}_{k})$ is a martingale (i.e. $E(Z_{k+1}(\mathrm{\mathbf{W}}_{k+1})|\mathrm{\mathbf{W}}_{k}))=Z_{k}(\mathrm{\mathbf{W}}_{k})$ ). Moreover, for any history $\mathbf{w}_{k}$ we have that

**中文译文**

不难证明，$Z_{k}(\mathrm{\mathbf{W}}_{k})=k\Delta_{k}(\mathrm{\mathbf{W}}_{k})$ 是一个鞅（即 $E(Z_{k+1}(\mathrm{\mathbf{W}}_{k+1})|\mathrm{\mathbf{W}}_{k}))=Z_{k}(\mathrm{\mathbf{W}}_{k})$）。此外，对于任意历史 $\mathbf{w}_{k}$，有

**English original**

$$
\bigl|Z_{k+1}\left(\mathbf{w}_{k+1}\right)-Z_{k}\left(\mathbf{w}_{k}\right)\bigr|\leq{D}\,,
\tag{23}
$$

**中文译文**

$$
\bigl|Z_{k+1}\left(\mathbf{w}_{k+1}\right)-Z_{k}\left(\mathbf{w}_{k}\right)\bigr|\leq{D}\,,
\tag{23}
$$

**English original**

where $D=4+2\sqrt{2}=\left(1-\cos^{2}(\frac{\pi}{8})\right)^{-1}$ ; the $4$ coming from the $I\left(\mathrm{\mathbf{w}}_{k+1}\right)$ term and the $2\sqrt{2}$ from the $E\left(I\left(W_{k+1}\mid\mathrm{\mathbf{w}}_{k}\right)\right)$ term. The Azuma-Hoeffding inequality [48] then tells us that

**中文译文**

其中 $D=4+2\sqrt{2}=\left(1-\cos^{2}(\frac{\pi}{8})\right)^{-1}$；其中的 $4$ 来自 $I\left(\mathrm{\mathbf{w}}_{k+1}\right)$ 项，$2\sqrt{2}$ 来自 $E\left(I\left(W_{k+1}\mid\mathrm{\mathbf{w}}_{k}\right)\right)$ 项。于是，Azuma-Hoeffding 不等式 [48] 告诉我们

**English original**

$$
P(\pi_{k}(\varepsilon))\leq\exp\Bigl(-\frac{k\varepsilon^{2}}{2D^{2}}\Bigr)\,,\qquad k\leq N-1\,,
\tag{24}
$$

**中文译文**

$$
P(\pi_{k}(\varepsilon))\leq\exp\Bigl(-\frac{k\varepsilon^{2}}{2D^{2}}\Bigr)\,,\qquad k\leq N-1\,,
\tag{24}
$$

**English original**

where $\pi_{k}\left(\varepsilon\right)$ is defined to be the union of all histories $\mathrm{\mathbf{w}}_{k}$ satisfying $\Delta_{k}\left(\mathbf{w}_{k}\right)\geq\varepsilon$ .

**中文译文**

其中，$\pi_{k}\left(\varepsilon\right)$ 定义为所有满足 $\Delta_{k}\left(\mathbf{w}_{k}\right)\geq\varepsilon$ 的历史 $\mathrm{\mathbf{w}}_{k}$ 的并集。

## References / 参考文献

**English original**

- [1] D. Mayers and A. Yao, Quantum Inf. Comput. 4, 273 (2004).
- [2] J. Barrett, L. Hardy, and A. Kent, Phys. Rev. Lett. 95, 010503 (2005).
- [3] J.F. Clauser et al., Phys. Rev. Lett. 23, 880 (1969).
- [4] A. Acín et al., Phys. Rev. Lett. 98, 230501 (2007).
- [5] S. Pironio et al., New J. Phys. 11, 045021 (2009).
- [6] M. McKague, New J. Phys. 11, 103037 (2009).
- [7] Ll. Masanes, S. Pironio, and A. Acín, Nat. Commun. 2, 238 (2011).
- [8] B.W. Reichardt, F. Unger, and U. Vazirani, Nature 496, 456 (2013); B.W. Reichardt, F. Unger, and U. Vazirani, arXiv:1209.0448.
- [9] S. Pironio et al., Phys. Rev. X 3, 031007 (2013).
- [10] U. Vazirani and T. Vidick, arXiv:1210.1810.
- [11] F. Magniez et al., in Proceedings of the 33rd International Colloquium on Automata, Languages and Programming (Springer, 2006), p. 72.
- [12] A. Acín, N. Gisin, and Ll. Masanes, Phys. Rev. Lett. 97, 120405 (2006).
- [13] F. Xu, B. Qi, and H.-K. Lo, New J. Phys. 12, 113026 (2010).
- [14] L. Lydersen et al., Nat. Photonics 4, 686 (2010).
- [15] R. Colbeck, PhD dissertation, Univ. Cambridge (2007), arXiv:0911.3814; R. Colbeck and A. Kent, J. Phys. A 44, 095305 (2011).
- [16] S. Pironio et al., Nature 464, 1021 (2010).
- [17] S. Pironio and S. Massar, Phys. Rev. A 87, 012336 (2013).
- [18] S. Fehr, R. Gelles, and C. Schaffner, Phys. Rev. A 87, 012335 (2013).
- [19] U. Vazirani and T. Vidick, Phil. Trans. R. Soc. A 370, 3432 (2012).
- [20] C. A. Miller and Y. Shi, arXiv:1402.0489.
- [21] M. Coudron and H. Yuen, arXiv:1310.6755.
- [22] M. McKague and M. Mosca, in Proceedings of the 5th Conference on the Theory of Quantum Computation, Communication, and Cryptography (Springer, 2011), p. 113.
- [23] C.-E. Bardyn et al., Phys. Rev. A 80, 062327 (2009).
- [24] M. McKague, T.H. Yang, and V. Scarani, J. Phys. A 45, 455304 (2012).
- [25] T.-H. Yang and M. Navascués, Phys. Rev. A 87, 050102(R) (2013).
- [26] T.-H. Yang et al., Phys. Rev. Lett. 113, 040401 (2014).
- [27] C. Bamps and S. Pironio, Phys. Rev. A 91, 052111 (2015).
- [28] J.-D. Bancal et al., Phys. Rev. Lett. 106, 250404 (2011).
- [29] T. Moroder et al., Phys. Rev. Lett. 111, 030501 (2013).
- [30] J. Silman et al., Phys. Rev. Lett. 106, 220501 (2011).
- [31] H.-K. Lo and H.F. Chau, Phys. Rev. Lett. 78, 3410 (1997).
- [32] D. Mayers, Phys. Rev. Lett. 78, 3414 (1997).
- [33] R.W. Spekkens and T. Rudolph, Phys. Rev. A 65, 012310 (2001).
- [34] A. Chailloux and I. Kerenidis, in Proceedings of the 52nd Annual Symposium on Foundations of Computer Science (CS Press, 2011), p. 354.
- [35] N. Aharon et al., in Proceedings of the 6th Conference on the Theory of Quantum Computation, Communication, and Cryptography (Springer, 2014), p. 1.
- [36] D.M. Greenberger, M.A. Horne, and A. Zeilinger, in Bell’s Theorem, Quantum Theory, and Conceptions of the Universe (Kluwer, 1989), p. 74.
- [37] N.D. Mermin, Phys. Today 43, 9 (1990).
- [38] L. Vaidman, Found. Phys. 29, 615 (1999).
- [39] N. Gisin. A.A. Méthot, and V. Scarani, Int. J. Quant. Inf. 5, 525 (2007).
- [40] A. Kent, Phys. Rev. Lett. 83, 1447 (1999).
- [41] E. Adlam and A. Kent, Phys. Rev. A 92, 022315 (2015).
- [42] M. Navascués, S. Pironio, and A. Acín, Phys. Rev. Lett. 98, 010401 (2007); M. Navascués, S. Pironio, and A. Acín, New J. Phys. 10, 073013 (2008).
- [43] S. Pironio, M. Navascués, and A. Acín, SIAM J. Optim. 20, 2157 (2010).
- [44] J. Löfberg, YALMIP: A Toolbox for Modeling and Optimization in MATLAB. Available at http://users.isy.liu.se/johanl/yalmip.
- [45] J.F. Sturm and I. Pólik, SeDuMi: a package for conic optimization. Available at http://sedumi.ie.lehigh.edu.
- [46] S. Popescu and D. Rohrlich, Found. Phys. 24, 379 (1994).
- [47] H. Buhrman et al., Proc. R. Soc. A 462, 1919 (2006).
- [48] K. Azuma, Tohoku Math. J. 19, 357 (1967).

**中文译文**

以上参考文献的作者、题名、期刊、出版信息及链接均按英文原文保留，不作翻译。
