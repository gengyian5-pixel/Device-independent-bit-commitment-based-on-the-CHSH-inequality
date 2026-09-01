# III The Protocol / 协议

**English original**

Before we go on to present the protocol, we fix notation. In the following we will consider a pair of four-input, $\{0,\,1,\,2,\,3\}$, two-output, $\{0,\,1\}$, boxes. The random variables designating the input and output corresponding to the $k$th use of box $i$ will be labeled by $S^{i}_{k}$ and $R^{i}_{k}$, respectively, with a specific realization (i.e. a specific value which they may assume) being labeled by lower-case letters $s^{i}_{k}$ and $r^{i}_{k}$. Similarly, the random strings corresponding to $k$ consecutive uses of box $i$ will be labeled by $\mathrm{\mathbf{S}}^{i}_{k}$ and $\mathrm{\mathbf{R}}^{i}_{k}$. We define $W_{k}=\{S^{0}_{k},\,S^{1}_{k},\,R^{0}_{k},\,R^{1}_{k}\}$ and $\mathbf{W}_{k}=\{W_{1},\,\dots,\,W_{k}\}$. We will refer to a specific realization $\mathbf{w}_{k}=\{w_{1},\,\dots,\,w_{k}\}$ as the history of the protocol. Finally, $|0\rangle$ ($|1\rangle$) will be taken to represent the positive (negative) eigenstate of $\sigma_{z}$.

**中文译文**

在介绍协议之前，我们先固定记号。下文将考虑一对具有四个输入 $\{0,\,1,\,2,\,3\}$ 和两个输出 $\{0,\,1\}$ 的盒子。表示盒子 $i$ 第 $k$ 次使用所对应输入和输出的随机变量分别记为 $S^{i}_{k}$ 和 $R^{i}_{k}$，其某个具体实现（即它们可能取的某个具体值）则分别用小写字母 $s^{i}_{k}$ 和 $r^{i}_{k}$ 表示。类似地，与盒子 $i$ 连续使用 $k$ 次相对应的随机字符串记为 $\mathrm{\mathbf{S}}^{i}_{k}$ 和 $\mathrm{\mathbf{R}}^{i}_{k}$。我们定义 $W_{k}=\{S^{0}_{k},\,S^{1}_{k},\,R^{0}_{k},\,R^{1}_{k}\}$ 以及 $\mathbf{W}_{k}=\{W_{1},\,\dots,\,W_{k}\}$。我们把某个具体实现 $\mathbf{w}_{k}=\{w_{1},\,\dots,\,w_{k}\}$ 称为协议的历史。最后，以 $|0\rangle$（$|1\rangle$）表示 $\sigma_{z}$ 的正（负）本征态。

**English original**

The protocol is based on EPR-state correlations. In an ideal implementation, the boxes are supposed to give rise to a violation of $2\sqrt{2}$ of the CHSH inequality in the sense that

**中文译文**

该协议基于 EPR 态关联。在理想实现中，盒子应当使 CHSH 不等式达到 $2\sqrt{2}$ 的违反，即

$$
\sum_{r^{0}_{n},\,r^{1}_{n},\,s^{0}_{n},\,s^{1}_{n}=0,\,1}
(-1)^{r^{0}_{n}\oplus r^{1}_{n}\oplus s^{0}_{n}s^{1}_{n}}
P(r^{0}_{n},\,r^{1}_{n}\mid s^{0}_{n},\,s^{1}_{n})
=2\sqrt{2}\qquad\forall n\,.
\tag{2}
$$

**English original**

In addition, the boxes are supposed to output $r^{0}_{n}=r^{1}_{n}$ given the pairs of inputs $s^{0}_{n}=i$, $s^{1}_{n}=i+2\mod 4$ ($i=0,\,1,\,2,\,3$). These correlations can be quantumly realized by preparing $N$ qubits, each in the $|\phi^{+}\rangle=\frac{1}{\sqrt{2}}(|00\rangle+|11\rangle)$ state. The inputs $0$, $1$, $2$, and $3$ of box $0$ correspond to the measurements $\sigma_{x}$, $\sigma_{z}$, $\sigma_{\pi/4}$, and $\sigma_{3\pi/4}$, respectively, where $\sigma_{\theta}=\cos\theta\sigma_{z}+\sin\theta\sigma_{x}$. The inputs $0$, $1$, $2$, and $3$ of box $1$ correspond to the measurements $\sigma_{\pi/4}$, $\sigma_{3\pi/4}$, $\sigma_{x}$, and $\sigma_{z}$, respectively.

**中文译文**

此外，当给定输入对 $s^{0}_{n}=i$、$s^{1}_{n}=i+2\mod 4$（$i=0,\,1,\,2,\,3$）时，盒子应当输出 $r^{0}_{n}=r^{1}_{n}$。这些关联可以通过量子方式实现：制备 $N$ 个量子比特，每个量子比特均处于 $|\phi^{+}\rangle=\frac{1}{\sqrt{2}}(|00\rangle+|11\rangle)$ 态。盒子 $0$ 的输入 $0$、$1$、$2$ 和 $3$ 分别对应测量 $\sigma_{x}$、$\sigma_{z}$、$\sigma_{\pi/4}$ 和 $\sigma_{3\pi/4}$，其中 $\sigma_{\theta}=\cos\theta\sigma_{z}+\sin\theta\sigma_{x}$。盒子 $1$ 的输入 $0$、$1$、$2$ 和 $3$ 分别对应测量 $\sigma_{\pi/4}$、$\sigma_{3\pi/4}$、$\sigma_{x}$ 和 $\sigma_{z}$。

**English original**

Since we would also like to consider the noisy case, we do not assume in the following that the parties have perfect resources, i.e. the boxes are expected to give rise to a CHSH violation $I<2\sqrt{2}$ and the outcomes $r^{0}_{n}$, $r^{1}_{n}$ for the pairs of inputs $s^{0}_{n}=i$ and $s^{1}_{n}=i+2\mod 4$ are not perfectly correlated.

**中文译文**

由于我们还希望考虑有噪声的情形，所以下文不假定各方拥有完美资源；也就是说，盒子预期产生的 CHSH 违反为 $I<2\sqrt{2}$，而对于输入对 $s^{0}_{n}=i$ 和 $s^{1}_{n}=i+2\mod 4$，输出 $r^{0}_{n}$、$r^{1}_{n}$ 并非完全关联。

**English original**

We consider a family of protocols. Each protocol in the family is specified by a parameter $N>1$ and a series of fixed times $t_{i}$ ($i=1,\ldots,N+1$) with $t_{i-1}<t_{i}<t_{i+1}$. For a given $N$ and choice of $t_{i}$, the protocol proceeds as follows:

**中文译文**

我们考虑一族协议。该族中的每个协议由参数 $N>1$ 和一系列固定时刻 $t_{i}$（$i=1,\ldots,N+1$）指定，并满足 $t_{i-1}<t_{i}<t_{i+1}$。对于给定的 $N$ 和 $t_{i}$ 的选择，协议按如下步骤进行：

## 1. Random selection / 随机选择

**English original**

Random selection – At time $t^{a}<t_{1}$ Bob picks uniformly at random, and in private,[^2] a number $n\in\{1,\,\dots,\,N\}$ and two input strings $\mathrm{\mathbf{s}}^{0}_{n}\in\{0,\,1\}^{n}$ and $\mathrm{\mathbf{s}}^{1}_{n}\in\{0,\,1\}^{n}$. At each of the $n$ times $t_{i}$ he feeds $s^{0}_{i}$ and $s^{1}_{i}$ into boxes $0$ and $1$, respectively. He uses the corresponding output strings $\mathrm{\mathbf{r}}^{0}_{n}$ and $\mathrm{\mathbf{r}}^{1}_{n}$ to compute the observed CHSH violation

**中文译文**

随机选择——在时刻 $t^{a}<t_{1}$，Bob 均匀随机且秘密地[^2-zh]选取一个数 $n\in\{1,\,\dots,\,N\}$，以及两个输入字符串 $\mathrm{\mathbf{s}}^{0}_{n}\in\{0,\,1\}^{n}$ 和 $\mathrm{\mathbf{s}}^{1}_{n}\in\{0,\,1\}^{n}$。在 $n$ 个时刻 $t_{i}$ 中的每一个时刻，他分别将 $s^{0}_{i}$ 和 $s^{1}_{i}$ 输入盒子 $0$ 和盒子 $1$。他利用相应的输出字符串 $\mathrm{\mathbf{r}}^{0}_{n}$ 和 $\mathrm{\mathbf{r}}^{1}_{n}$ 计算观测到的 CHSH 违反：

$$
\bar{I}_{n}\left(\mathrm{\mathbf{w}}_{n}\right)
=\frac{1}{n}\sum_{k=1}^{n}I\left(w_{k}\right)\,.
\tag{3}
$$

**English original**

where

**中文译文**

其中

$$
I(W_{k})
=4\sum_{r^{0}_{k},\,r^{1}_{k},\,s^{0}_{k},\,s^{1}_{k}=0,1}
(-1)^{r^{0}_{k}\oplus r^{1}_{k}\oplus s^{0}_{k}s^{1}_{k}}
\delta_{R^{0}_{k}r^{0}_{k}}
\delta_{R^{1}_{k}r^{1}_{k}}
\delta_{S^{0}_{k}s^{0}_{k}}
\delta_{S^{1}_{k}s^{1}_{k}}\,,
\tag{4}
$$

**English original**

is the CHSH indicator function[^3] at step $k$. Bob then compares $\bar{I}_{n}\left(\mathrm{\mathbf{w}}_{n}\right)$ to some previously agreed threshold $I_{\mathrm{th}}$. If $\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})<I_{\mathrm{th}}$ he aborts the protocol. Otherwise, he flips a classical coin. Denote its outcome by $c$. At time $t^{b}<t_{n+1}$ he sends box $c$ to Alice.

**中文译文**

是第 $k$ 步的 CHSH 指示函数。[^3-zh]随后，Bob 将 $\bar{I}_{n}\left(\mathrm{\mathbf{w}}_{n}\right)$ 与某个预先约定的阈值 $I_{\mathrm{th}}$ 进行比较。若 $\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})<I_{\mathrm{th}}$，他便中止协议。否则，他掷一枚经典硬币，并将其结果记为 $c$。在时刻 $t^{b}<t_{n+1}$，他将盒子 $c$ 发送给 Alice。

## 2. Commit phase / 承诺阶段

**English original**

Commit phase – Let $b$ be the value of the bit Alice wishes to commit. Alice inputs $s^{c}_{n+1}=b+2$ into her box. She selects uniformly at random a classical bit $a$, and at time $t^{c}$ ($t^{b}<t^{c}<t_{n+1}$) sends Bob the classical bit $q=r^{c}_{n+1}\oplus ab$ as a token of her commitment.

**中文译文**

承诺阶段——令 $b$ 为 Alice 希望承诺的比特值。Alice 向她的盒子输入 $s^{c}_{n+1}=b+2$。她均匀随机选取一个经典比特 $a$，并在时刻 $t^{c}$（$t^{b}<t^{c}<t_{n+1}$）将经典比特 $q=r^{c}_{n+1}\oplus ab$ 发送给 Bob，作为她作出承诺的凭据。

## 3. Reveal phase / 揭示阶段

**English original**

Reveal phase – At time $t^{d}$ ($t^{c}<t^{d}<t_{n+1}$) Alice sends Bob $b$ and $r^{c}_{n+1}$. If $b$ and $r^{c}_{n+1}$ are not received before $t_{n+1}$ Bob aborts. Otherwise, Bob checks whether $q=r^{c}_{n+1}$ or $q=r^{c}_{n+1}\oplus b$. If both relations are not satisfied, he aborts. Else at time $t_{n+1}>t^{d}$ he inputs $s^{\bar{c}}_{n+1}=s^{c}_{n+1}-2=b$ into his box and verifies that $r^{\bar{c}}_{n+1}=r^{c}_{n+1}$. If this last test fails, he aborts.

**中文译文**

揭示阶段——在时刻 $t^{d}$（$t^{c}<t^{d}<t_{n+1}$），Alice 将 $b$ 和 $r^{c}_{n+1}$ 发送给 Bob。如果 Bob 未在 $t_{n+1}$ 之前收到 $b$ 和 $r^{c}_{n+1}$，他便中止协议。否则，Bob 检查是否有 $q=r^{c}_{n+1}$ 或 $q=r^{c}_{n+1}\oplus b$。若这两个关系均不成立，他便中止。否则，在时刻 $t_{n+1}>t^{d}$，他向自己的盒子输入 $s^{\bar{c}}_{n+1}=s^{c}_{n+1}-2=b$，并验证 $r^{\bar{c}}_{n+1}=r^{c}_{n+1}$。若最后这项检验失败，他便中止协议。

**English original**

We note that in an honest execution of the protocol, Bob may end up aborting the protocol in the random selection phase even when the settings are ideal. Moreover, Bob will never know if his having to abort is due to Alice having been dishonest or due to the boxes having exhibited a statistically unlikely behavior. This is just a by-product of the statistical nature of the protocol, which is of course absent in the limit that $N\rightarrow\infty$. However, if Bob does not abort the protocol in the random selection phase, then (assuming ideal settings and an honest execution) he will not abort it in the reveal phase and will always learn the correct value of the bit committed by Alice. In contrast, if there are physical imperfections present, such as noise or a misalignment of the measurement axes, then there is a non-vanishing probability that Bob will abort the protocol in the reveal phase even when Alice is honest. This is true of any practical formulation (i.e. a formulation accommodating imperfections), and has nothing to do with the protocol being device-independent.

**中文译文**

我们注意到，在诚实执行协议时，即使设置是理想的，Bob 最终仍可能在随机选择阶段中止协议。此外，Bob 永远无法知道，他之所以不得不中止，是因为 Alice 不诚实，还是因为盒子表现出了统计上不太可能出现的行为。这不过是协议具有统计性质的副产物；当然，在 $N\rightarrow\infty$ 的极限下，这一现象会消失。然而，如果 Bob 在随机选择阶段没有中止协议，那么（假定设置理想且协议被诚实执行）他在揭示阶段将不会中止，并且总能获知 Alice 所承诺比特的正确值。相反，如果存在物理缺陷，例如噪声或测量轴未对准，那么即使 Alice 是诚实的，Bob 在揭示阶段中止协议的概率仍不为零。这适用于任何实际表述（即容纳缺陷的表述），与该协议是否设备无关无关。

**English original**

We have required that Bob’s measurements, including the one in the reveal phase, take place at fixed times $t_{i}$.[^4] This is in order to ensure that the box Bob keeps cannot tell whether it is being measured in the random selection phase or in the reveal phase (unless Bob picked $n=N$). Otherwise, Alice may program the boxes such that in the random selection phase they maximally violate the CHSH inequality, while in the reveal phase they behave deterministically, thereby allowing her to cheat perfectly. Specifically, the intervals $t_{i+1}-t_{i}$ must be sufficiently long to allow the following sequence of operations: (i) the sending of quantum information from Bob to Alice, (ii) Alice’s measurement of the quantum system received from Bob, (iii) the sending of classical information from Alice and its receipt by Bob, and (iv) Bob’s measurement of the quantum system remaining in his possession at $t_{i+1}$.

**中文译文**

我们要求 Bob 的测量（包括揭示阶段中的测量）在固定时刻 $t_{i}$ 进行。[^4-zh]这是为了确保 Bob 保留的盒子无法判断自己是在随机选择阶段还是在揭示阶段被测量（除非 Bob 选取了 $n=N$）。否则，Alice 可以对盒子进行编程，使其在随机选择阶段最大程度地违反 CHSH 不等式，而在揭示阶段则以确定性方式运行，从而使她能够完美作弊。具体而言，时间间隔 $t_{i+1}-t_{i}$ 必须足够长，以允许依次完成以下操作：(i) 将量子信息从 Bob 发送给 Alice；(ii) Alice 测量从 Bob 收到的量子系统；(iii) Alice 发送经典信息且 Bob 接收到该信息；以及 (iv) Bob 在 $t_{i+1}$ 测量仍由他持有的量子系统。

**English original**

As mentioned earlier, since the reveal time cannot be chosen at will, strictly speaking, the protocol is not a bit commitment protocol. Nevertheless, depending on the application, it may still be used as a primitive. For example, our protocol may be used to implement coin flipping. The restriction on the reveal time can be lifted at the price of increasing Alice’s control (see Appendix B), or by working in the large office scenario (see Appendix C).

**中文译文**

如前所述，由于无法任意选择揭示时间，严格来说，该协议并不是一个比特承诺协议。尽管如此，视具体应用而定，它仍可用作一种原语。例如，我们的协议可用于实现掷硬币。可以通过增加 Alice 的控制力这一代价来取消对揭示时间的限制（见附录 B），也可以通过在“大办公室”情景下工作来取消这一限制（见附录 C）。

[^2]: **English original** It is crucial that $n$ is chosen privately and randomly by Bob in order for him to be able to ascertain that in the $n+1$th use the boxes are CHSH violating. Otherwise, dishonest Alice can prepare the boxes such that they are CHSH violating only in the first $n$ uses.

[^2-zh]: **中文译文** 为了使 Bob 能够确定盒子在第 $n+1$ 次使用时违反 CHSH，不公开且随机地选择 $n$ 至关重要。否则，不诚实的 Alice 可以制备盒子，使它们仅在前 $n$ 次使用中违反 CHSH。

[^3]: **English original** The factor of $4$ in (4) is just a normalization taking into account that Bob picks all four possible input pairs with equal probability. With this definition the expected value $E(I(W_{k}))=\sum_{r^{0}_{k},\,r^{1}_{k},\,s^{0}_{k},\,s^{1}_{k}=0,1}(-1)^{r^{0}_{k}\oplus r^{1}_{k}\oplus s^{0}_{k}s^{1}_{k}}P(r^{0}_{k}\,r^{1}_{k}\mid s^{0}_{k}\,s^{1}_{k})$ is the usual CHSH expression.

[^3-zh]: **中文译文** (4) 中的因子 $4$ 只是一个归一化因子，它考虑到了 Bob 以相同概率选取全部四种可能的输入对。采用此定义，期望值 $E(I(W_{k}))=\sum_{r^{0}_{k},\,r^{1}_{k},\,s^{0}_{k},\,s^{1}_{k}=0,1}(-1)^{r^{0}_{k}\oplus r^{1}_{k}\oplus s^{0}_{k}s^{1}_{k}}P(r^{0}_{k}\,r^{1}_{k}\mid s^{0}_{k}\,s^{1}_{k})$ 就是通常的 CHSH 表达式。

[^4]: **English original** In fact, it is sufficient to only require that measurement $i+1$ takes place at any time during the interval $(t_{i},\,t_{i+1}]$, so long as this time is large enough to allow for the commit and reveal phases to be completed in the remainder of the interval.

[^4-zh]: **中文译文** 实际上，只需要求测量 $i+1$ 在区间 $(t_{i},\,t_{i+1}]$ 内的任意时刻进行即可，只要这一时刻足够早，使得承诺阶段和揭示阶段能够在该区间的剩余时间内完成。

# IV Alice’s security / Alice 的安全性

**English original**

In the following, when considering the $n+1$th measurement of the boxes, i.e. the measurements taking place in the commit and reveal phases, we drop the subscript $n+1$ on the $s^{i}_{n+1}$ and $r^{i}_{n+1}$.

**中文译文**

下文在考虑盒子的第 $n+1$ 次测量，即承诺阶段和揭示阶段中进行的测量时，我们省略 $s^{i}_{n+1}$ 和 $r^{i}_{n+1}$ 的下标 $n+1$。

## IV.1 Bob’s information gain / Bob 的信息增益

**English original**

Alice only receives a single box from Bob and does not verify the CHSH violation. Bob’s most general cheating strategy is therefore to prepare Alice’s box in an entangled state with an ancillary system in his possession. Since in the commit phase Bob receives from Alice a single classical bit $q$, Bob will perform one out of a pair of two-outcome measurements on his ancillary system to infer Alice’s input $s^{c}$ (and consequently the committed bit $b=s^{c}-2$). We denote Bob’s binary input and output by $m$ and $g$, where $m=0$ ($m=1$) corresponds to the measurement he carries out when Alice sends $q=0$ ($q=1$), and $g$ is his guess of $s^{c}$. The probability $P\left(g\mid r^{c},\,s^{c},\,m\right)$ of obtaining the output $g$, given the input $m$, explicitly depends on Alice’s input-output pair $s^{c}$ and $r^{c}$ (or, what is the same thing, on $b$ and $r^{c}$) because Bob’s ancillary system and Alice’s box are entangled. Bob’s information gain is therefore given by:

**中文译文**

Alice 只从 Bob 那里接收一个盒子，并不验证 CHSH 违反。因此，Bob 最一般的作弊策略是使 Alice 的盒子与他所持有的辅助系统处于纠缠态。由于在承诺阶段 Bob 从 Alice 那里接收单个经典比特 $q$，Bob 将在其辅助系统上进行一对二结果测量中的一个，以推断 Alice 的输入 $s^{c}$（进而推断所承诺的比特 $b=s^{c}-2$）。我们用 $m$ 和 $g$ 分别表示 Bob 的二元输入和输出，其中 $m=0$（$m=1$）对应于 Alice 发送 $q=0$（$q=1$）时他所进行的测量，而 $g$ 是他对 $s^{c}$ 的猜测。给定输入 $m$ 时得到输出 $g$ 的概率 $P\left(g\mid r^{c},\,s^{c},\,m\right)$ 明确依赖于 Alice 的输入—输出对 $s^{c}$ 和 $r^{c}$（或者等价地说，依赖于 $b$ 和 $r^{c}$），这是因为 Bob 的辅助系统与 Alice 的盒子相纠缠。因此，Bob 的信息增益为：

$$
\begin{aligned}
P_{\mathrm{gain}}
&=\max_{\mathcal{S}}\sum_{r^{c},\,b,\,a=0,\,1}
P\left(r^{c}\mid s^{c}=b+2\right)
P\left(g=b\mid r^{c},\,s^{c}=b+2,\,m=r^{c}\oplus ab\right)\\
&=\frac{1}{4}\max_{\mathcal{S}}\sum_{r^{c},\,b=0,\,1}
P\left(r^{c}\mid s^{c}=b+2\right)
\Bigl[
P\left(g=b\mid r^{c},\,s^{c}=b+2,\,m=r^{c}\right)\\
&\hspace{8em}+
P\left(g=b\mid r^{c},\,s^{c}=b+2,\,m=r^{c}\oplus b\right)
\Bigr]\\
&=\frac{1}{4}\max_{\mathcal{S}}\sum_{r^{c},\,b=0,\,1}
\Bigl[
P\left(r^{c},\,g=b\mid s^{c}=b+2,\,m=r^{c}\right)\\
&\hspace{8em}+
P\left(r^{c},\,g=b\mid s^{c}=b+2,\,m=r^{c}\oplus b\right)
\Bigr]\\
&=\frac{1}{4}\max_{\mathcal{S}}\Bigl[
2P\left(0,\,0\mid 2,\,0\right)
+2P\left(1,\,0\mid 2,\,1\right)
+P\left(0,\,1\mid 3,\,0\right)\\
&\hspace{8em}+
P\left(1,\,1\mid 3,\,1\right)
+P\left(0,\,1\mid 3,\,1\right)
+P\left(1,\,1\mid 3,\,0\right)
\Bigr]\,.
\end{aligned}
\tag{5}
$$

**English original**

where $\mathcal{S}$ denotes the set of all cheating strategies. Note that since Alice is honest she picks $b$ and $a$ fully at random and so for any pair $b$ and $a$ $P(b,\,a)=\frac{1}{4}$. From normalization and the no-signaling constraints (i.e. $\sum_{r^{1}=0,\,1}P(r^{0},\,r^{1}\mid s^{0},\,0)=\sum_{r^{1}=0,\,1}P(r^{0},\,r^{1}\mid s^{0},\,1)$ and $\sum_{r^{0}=0,\,1}P(r^{0},\,r^{1}\mid 2,\,s^{1})=\sum_{r^{0}=0,\,1}P(r^{0},\,r^{1}\mid 3,\,s^{1})$) we obtain that $P(s^{1},\,0\mid 2,\,s^{1})+P(0,\,1\mid 3,\,s^{1})+P(1,\,1\mid 3,\,s^{1})\leq 1$ and $P\left(0,\,0\mid 2,\,0\right)+P\left(1,\,0\mid 2,\,1\right)\leq 1$, implying that $P_{\mathrm{gain}}\leq\frac{3}{4}$.

**中文译文**

其中，$\mathcal{S}$ 表示所有作弊策略的集合。注意，由于 Alice 是诚实的，她完全随机地选取 $b$ 和 $a$，所以对于任意一对 $b$ 和 $a$，都有 $P(b,\,a)=\frac{1}{4}$。根据归一化条件和无信号约束（即 $\sum_{r^{1}=0,\,1}P(r^{0},\,r^{1}\mid s^{0},\,0)=\sum_{r^{1}=0,\,1}P(r^{0},\,r^{1}\mid s^{0},\,1)$ 以及 $\sum_{r^{0}=0,\,1}P(r^{0},\,r^{1}\mid 2,\,s^{1})=\sum_{r^{0}=0,\,1}P(r^{0},\,r^{1}\mid 3,\,s^{1})$），可得 $P(s^{1},\,0\mid 2,\,s^{1})+P(0,\,1\mid 3,\,s^{1})+P(1,\,1\mid 3,\,s^{1})\leq 1$ 和 $P\left(0,\,0\mid 2,\,0\right)+P\left(1,\,0\mid 2,\,1\right)\leq 1$，这意味着 $P_{\mathrm{gain}}\leq\frac{3}{4}$。

## IV.2 Bob’s optimal cheating strategy / Bob 的最优作弊策略

**English original**

Bob’s optimal cheating strategy is to prepare Alice’s box such that $r^{c}=s^{c}-2$ and guess $b=q$. Since Alice is honest $q$ equals $r^{c}$ (and thus equals $b=s^{c}-2$) $75\%$ of the time. Alternately, Bob can employ a device-dependent strategy (i.e. where Alice’s measurements are those prescribed by the protocol). In this strategy Bob actually prepares the boxes as prescribed by the protocol. Noting that the measurement settings which correspond to $s^{\bar{c}}=0$ and $s^{c}=2$ are identical, Bob inputs $0$ into his box. Since $q$ equals Alice’s outcome $75\%$ of the time, Bob always treats it as her output. If his outcome equals $q$ Bob guesses that Alice input $2$, otherwise, he guesses that she input $3$. Whenever Alice inputs $2$, Bob’s guess is correct. Whenever Alice inputs $3$, Bob’s guess is correct only half of the time. Bob’s information gain is thus seen to equal the optimum, as well as the result of [30].

**中文译文**

Bob 的最优作弊策略是制备 Alice 的盒子，使得 $r^{c}=s^{c}-2$，并猜测 $b=q$。由于 Alice 是诚实的，$q$ 在 $75\%$ 的情况下等于 $r^{c}$（因而等于 $b=s^{c}-2$）。或者，Bob 可以采用一种设备依赖策略（即 Alice 的测量是协议规定的那些测量）。在该策略中，Bob 实际上按照协议规定制备盒子。注意到与 $s^{\bar{c}}=0$ 和 $s^{c}=2$ 相对应的测量设置相同，Bob 向他的盒子输入 $0$。由于 $q$ 在 $75\%$ 的情况下等于 Alice 的测量结果，Bob 总是把它当作她的输出。如果他的测量结果等于 $q$，Bob 就猜测 Alice 输入了 $2$；否则，他猜测她输入了 $3$。每当 Alice 输入 $2$ 时，Bob 的猜测都是正确的。每当 Alice 输入 $3$ 时，Bob 的猜测仅有一半时间正确。因此可见，Bob 的信息增益等于最优值，也等于 [30] 的结果。
