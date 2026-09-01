## V Bob’s security

**English original**

This section is divided into three. In Subsections A and B we consider the case where the boxes at the $n+1$ th iteration (i.e. after Bob’s CHSH estimation) are known to be characterized by a fixed Bell violation $I\geq I_{\mathrm{th}}$ . As we will see in Subsection C, this is equivalent to considering the asymptotic limit in which the number of tests Bob carries out tends to infinity. Specifically, in Subsection A we derive an upper bound on Alice’s control, given the CHSH expectation value $I$ , and in Subsection B we present an optimal cheating strategy which saturates it. Finally, in Subsection C we use the bound derived in Subsection A to derive an upper bound on Alice’s control in the general case where Bob carries out an arbitrary number of tests. In the limit that this number tends to infinity we recover the bound of Subsection A.

**中文译文**

本节分为三个部分。在 A、B 两个小节中，我们考虑盒子在第 $n+1$ 次迭代（即 Bob 完成 CHSH 估计之后）时已知具有固定的 Bell 违反值 $I\geq I_{\mathrm{th}}$ 的情形。正如我们将在 C 小节中看到的，这等价于考虑 Bob 所执行的测试次数趋于无穷的渐近极限。具体而言，在 A 小节中，我们在给定 CHSH 期望值 $I$ 的情况下推导 Alice 控制力的一个上界；在 B 小节中，我们给出一种达到该上界的最优作弊策略。最后，在 C 小节中，我们利用 A 小节推导出的界，针对 Bob 执行任意次数测试的一般情形推导 Alice 控制力的一个上界。当测试次数趋于无穷时，我们重新得到 A 小节的界。

### V.1 Alice’s control in the asymptotic limit

**English original**

Most generally, in the commit phase Alice carries out a two-outcome measurement on the systems in her possession: box $c$ , which she received from Bob, and possibly some ancillary system with which the boxes may be entangled. The result of the measurement determines the value of $q$ she sends Bob. In the reveal phase she then performs one out of four possible two-outcome measurements, depending on the value of $q$ and whether she wishes to reveal $0$ or $1$ , in order to determine $r^{c}$ . We note, however, that when she wishes to reveal $0$ the last measurement is redundant because $q$ must equal $r^{c}$ . Alice therefore does not lose anything by always performing in the reveal phase one out of the two measurements corresponding to her wishing to reveal $1$ . This implies that without loss of generality these two measurements may be combined with the measurement in the commit phase to form a single four-outcome measurement in the commit phase. This measurement decides the two values of $r^{c}$ , and simultaneously the value of $q$ . To sum up, in the commit phase Alice carries out a four-element POVM $\mathcal{M}^{c}=\{M_{kl}^{c}\}$ ( $k,\,l=0,\,1$ ) acting on $\mathcal{H}^{c}$ , such that if she wishes to reveal $0$ ( $1$ ) she sends Bob $q=k$ in the commit phase and $r^{c}=k$ ( $r^{c}=l$ ) in the reveal phase.

**中文译文**

在最一般的情况下，Alice 在承诺阶段对她所持有的系统执行一次双结果测量：这些系统包括她从 Bob 处收到的盒子 $c$，以及盒子可能与之纠缠的某个辅助系统。测量结果决定她发送给 Bob 的 $q$ 值。随后在揭示阶段，为确定 $r^{c}$，她根据 $q$ 的值以及她希望揭示 $0$ 还是 $1$，执行四种可能的双结果测量之一。然而我们注意到，当她希望揭示 $0$ 时，最后一次测量是多余的，因为 $q$ 必须等于 $r^{c}$。因此，Alice 若在揭示阶段总是执行与她希望揭示 $1$ 相对应的两种测量之一，并不会有任何损失。这意味着，不失一般性，可以将这两种测量与承诺阶段的测量合并，在承诺阶段形成一次四结果测量。该测量决定 $r^{c}$ 的两个取值，同时也决定 $q$ 的值。总之，在承诺阶段，Alice 在 $\mathcal{H}^{c}$ 上执行一个四元素 POVM $\mathcal{M}^{c}=\{M_{kl}^{c}\}$（$k,\,l=0,\,1$）；若她希望揭示 $0$（$1$），则她在承诺阶段向 Bob 发送 $q=k$，并在揭示阶段发送 $r^{c}=k$（$r^{c}=l$）。

**English original**

Suppose that Alice wishes to reveal $b=0$ ( $s^{c}=2$ ). Bob will first check whether $r^{c}=q$ (since $b=0$ , $r^{c}\oplus b=r^{c}$ ). Bob will then input $s^{\bar{c}}=0$ and verify that $r^{\bar{c}}=r^{c}$ . In this case Alice’s cheating probability equals $\frac{1}{2}\sum_{k,\,l=0,\,1}\left[P(r^{1}=k,\,(k,\,l)|s^{1}=0,\,\mathcal{M}^{0})+P(r^{0}=k,\,(k,\,l)|s^{0}=0,\,\mathcal{M}^{1})\right]$ , where the factor of $\frac{1}{2}$ is due to Bob sending boxes $0$ and $1$ with equal probability. Suppose that Alice wishes to reveal $b=1$ ( $s^{c}=3$ ), then $r^{c}=b$ or $r^{c}=b\oplus 1$ . Bob will input $s^{\bar{c}}=1$ and verify that $r^{\bar{c}}=r^{c}$ . In this case Alice’s cheating probability equals $\frac{1}{2}\sum_{k,\,l=0,\,1}\left[P(r^{1}=l,\,(k,\,l)|s^{1}=1,\,\mathcal{M}^{0})+P(r^{0}=l,\,(k,\,l)|s^{0}=1,\,\mathcal{M}^{1})\right]$ . Alice’s overall cheating probability is therefore given by

**中文译文**

假设 Alice 希望揭示 $b=0$（$s^{c}=2$）。Bob 将首先检查 $r^{c}=q$ 是否成立（因为 $b=0$，所以 $r^{c}\oplus b=r^{c}$）。然后 Bob 输入 $s^{\bar{c}}=0$，并验证 $r^{\bar{c}}=r^{c}$。在这种情况下，Alice 的作弊概率等于 $\frac{1}{2}\sum_{k,\,l=0,\,1}\left[P(r^{1}=k,\,(k,\,l)|s^{1}=0,\,\mathcal{M}^{0})+P(r^{0}=k,\,(k,\,l)|s^{0}=0,\,\mathcal{M}^{1})\right]$，其中因子 $\frac{1}{2}$ 来自 Bob 以相同概率发送盒子 $0$ 和盒子 $1$。假设 Alice 希望揭示 $b=1$（$s^{c}=3$），则 $r^{c}=b$ 或 $r^{c}=b\oplus 1$。Bob 将输入 $s^{\bar{c}}=1$，并验证 $r^{\bar{c}}=r^{c}$。在这种情况下，Alice 的作弊概率等于 $\frac{1}{2}\sum_{k,\,l=0,\,1}\left[P(r^{1}=l,\,(k,\,l)|s^{1}=1,\,\mathcal{M}^{0})+P(r^{0}=l,\,(k,\,l)|s^{0}=1,\,\mathcal{M}^{1})\right]$。因此，Alice 的总体作弊概率为

$$
\begin{aligned}
&\frac{1}{4}\sum_{k,\,l=0,\,1}\Bigl[P(r^{1}=k,\,(k,\,l)\mid s^{1}=0,\,\mathcal{M}^{0})+P(r^{0}=k,\,(k,\,l)\mid s^{0}=0,\,\mathcal{M}^{1})\Bigr. \\
&\Bigl.+P(r^{1}=l,\,(k,\,l)\mid s^{1}=1,\,\mathcal{M}^{0})+P(r^{0}=l,(\,k,\,l)\mid s^{0}=1,\,\mathcal{M}^{1})\Bigr]\,.
\end{aligned}
\tag{6}
$$
**English original**

To obtain Alice’s control, we must maximize the above expression under the constraint that the CHSH expectation value is no less than $I_{\mathrm{th}}$ . This translates to the following optimization problem

**中文译文**

为得到 Alice 的控制力，我们必须在 CHSH 期望值不小于 $I_{\mathrm{th}}$ 的约束下，将上述表达式最大化。这转化为如下优化问题：

$$
\begin{aligned}
P_{\mathrm{cont}}
&= \frac{1}{4}\max_{\mathcal{Q}}\mathrm{Tr}\biggl(\rho\sum_{c,\,k,\,l=0,\,1}M_{kl}^{c}\bigl(\Pi_{k\mid 0}^{\bar{c}}+\Pi_{l\mid 1}^{\bar{c}}\bigr)\biggr) \\
&\mathrm{s.t.}\quad
\mathrm{Tr}\biggl(\rho\sum_{a,\,b,\,x,\,y=0,\,1}(-1)^{a\oplus b\oplus xy}\Pi_{a\mid x}^{0}\Pi_{b\mid y}^{1}\biggr)\geq I_{\mathrm{th}}, \\
&\qquad\bigl[\Pi_{i\mid j}^{c},\,\Pi_{k\mid l}^{\bar{c}}\bigr]=\bigl[M_{ij}^{c},\,\Pi_{k\mid l}^{\bar{c}}\bigr]=\bigl[M_{ij}^{c},\,M_{kl}^{\bar{c}}\bigr]=0, \\
&\qquad\Pi_{i\mid j}^{c}\succeq 0,\quad M_{ij}^{c}\succeq 0,\quad\sum_{i=0,\,1}\Pi_{i\mid j}^{c}=\mathbb{1},\quad\sum_{i,\,j=0,\,1}M_{ij}^{c}=\mathbb{1}.
\end{aligned}
\tag{7}
$$
**English original**

where $\mathcal{Q}=\bigl\{\mathcal{H}^{c},\,\rho,\,\{\Pi_{i|j}^{c}\},\,\mathcal{M}^{c}\bigr\}_{c}$ and $\Pi_{r|s}^{c}$ is the POVM element corresponding to inputting $s$ into box $c$ and obtaining the output $r$ . Problems of this type can be relaxed to a hierarchy of semi-definite programming (SDP) problems, using the method introduced in [42, 43]. This hierarchy provides increasingly tighter upper bounds on the solution of the original problem, which are guaranteed to converge to it at a sufficiently high order. We have solved the second order SDP relaxation of Eq. (7). In the next subsection we present a cheating strategy which saturates it (up to $10^{-8}$ – the numerical accuracy of the SDP solver), implying that the second order relaxation already converges. Fig. 1 presents Alice’s control as a function of the CHSH expectation value.

**中文译文**

其中 $\mathcal{Q}=\bigl\{\mathcal{H}^{c},\,\rho,\,\{\Pi_{i|j}^{c}\},\,\mathcal{M}^{c}\bigr\}_{c}$，而 $\Pi_{r|s}^{c}$ 是与向盒子 $c$ 输入 $s$ 并获得输出 $r$ 相对应的 POVM 元素。利用 [42, 43] 中提出的方法，可以将此类问题松弛为一个半正定规划（SDP）问题的层级。该层级为原问题的解提供逐渐收紧的上界，并保证在足够高的阶数上收敛到原问题的解。我们求解了式 (7) 的二阶 SDP 松弛。在下一小节中，我们给出一种达到该松弛上界的作弊策略（误差在 $10^{-8}$ 以内——即 SDP 求解器的数值精度），这表明二阶松弛已经收敛。图 1 给出了 Alice 的控制力随 CHSH 期望值变化的关系。

**English original**

Figure 1: Alice’s control as a function of $I_{\mathrm{th}}$ in the asymptotic limit. The curve was obtained from Eqs. (8)-(10). The curve saturates the second order relaxation of Eq. (7) up to $10^{-8}$ – the numerical accuracy of the SDP solver.

**中文译文**

图 1：渐近极限下 Alice 的控制力随 $I_{\mathrm{th}}$ 变化的关系。该曲线由式 (8)–(10) 得到。该曲线达到式 (7) 的二阶松弛上界，误差在 $10^{-8}$ 以内——即 SDP 求解器的数值精度。

![](figures/fig1.png){ width=70% }


### V.2 Alice’s optimal cheating strategy in the asymptotic limit

**English original**

We present below an optimal cheating strategy, in which it suffices for Alice to perform a single two-outcome measurement, rather than a four-outcome one as described in the previous subsection. The strategy proceeds as follows. Alice prepares the boxes such that each contains one qubit out of a pair in the maximally entangled state $\left|\phi^{+}\right\rangle=\frac{1}{\sqrt{2}}\left(\left|00\right\rangle+\left|11\right\rangle\right)$ . Box $0$ is prepared such that inputting $0$ and $1$ gives rise to the measurements $\sigma_{2\theta}$ and $\sigma_{z}$ , respectively, where $\sigma_{\alpha}=\cos\alpha\sigma_{z}+\sin\alpha\sigma_{x}$ . Box $1$ is prepared such that inputting $0$ and $1$ gives rise to the measurements $\sigma_{2\theta-\varphi}$ and $\sigma_{4\theta-\varphi}$ , respectively. If Alice receives box $0$ ( $1$ ) she measures $\sigma_{3\theta-\varphi}$ ( $\sigma_{\theta}$ ). That is, she always measures along an axis midway between Bob’s measurement axes in $zx$ -plane (see Fig. 2). She then sends Bob values of $b$ and $r^{c}$ equal to the result of her measurement. Pairs of measurements along axes, differing by an angle of $\theta$ , in the $zx$ -plane (since $|\phi^{+}\rangle$ is invariant under rotations in the $zx$ -plane) give rise to correlated outcomes with probability $\cos^{2}\bigl(\frac{\theta}{2}\bigr)$ . Therefore, irrespectively of whether Alice reveals $0$ or $1$ (or, what is the same thing, whether Bob inputs $0$ or $1$ ), her cheating probability equals

**中文译文**

下面我们给出一种最优作弊策略；在该策略中，Alice 只需执行一次双结果测量，而不必执行上一小节所述的四结果测量。该策略如下。Alice 制备盒子，使每个盒子各包含一对处于最大纠缠态 $\left|\phi^{+}\right\rangle=\frac{1}{\sqrt{2}}\left(\left|00\right\rangle+\left|11\right\rangle\right)$ 的量子比特中的一个。盒子 $0$ 被制备成：输入 $0$ 和 $1$ 时分别产生测量 $\sigma_{2\theta}$ 和 $\sigma_{z}$，其中 $\sigma_{\alpha}=\cos\alpha\sigma_{z}+\sin\alpha\sigma_{x}$。盒子 $1$ 被制备成：输入 $0$ 和 $1$ 时分别产生测量 $\sigma_{2\theta-\varphi}$ 和 $\sigma_{4\theta-\varphi}$。如果 Alice 收到盒子 $0$（$1$），她就测量 $\sigma_{3\theta-\varphi}$（$\sigma_{\theta}$）。也就是说，她总是沿 $zx$ 平面中位于 Bob 两条测量轴正中间的轴进行测量（见图 2）。随后，她向 Bob 发送与其测量结果相等的 $b$ 和 $r^{c}$ 值。在 $zx$ 平面内，沿夹角为 $\theta$ 的两条轴进行的一对测量（由于 $|\phi^{+}\rangle$ 在 $zx$ 平面内的旋转下不变）以概率 $\cos^{2}\bigl(\frac{\theta}{2}\bigr)$ 产生相关结果。因此，无论 Alice 揭示 $0$ 还是 $1$（或者等价地，无论 Bob 输入 $0$ 还是 $1$），她的作弊概率均为

$$
P_{\mathrm{cont}}=\cos^{2}\Bigl(\frac{\theta}{2}\Bigr)\,.
\tag{8}
$$
**English original**

Of course the values of $\theta$ and $\varphi$ are restricted by the constraint on the value of the CHSH violation. For the measurements above we have

**中文译文**

当然，$\theta$ 和 $\varphi$ 的取值受到 CHSH 违反值约束的限制。对于上述测量，我们有

$$
I=\langle\phi^{+}|\sigma_{2\theta}\otimes\sigma_{2\theta-\varphi}+\sigma_{2\theta}\otimes\sigma_{4\theta-\varphi}+\sigma_{z}\otimes\sigma_{2\theta-\varphi}-\sigma_{z}\otimes\sigma_{4\theta-\varphi}|\phi^{+}\rangle
=2\cos(2\theta-\varphi)-\cos(4\theta-\varphi)+\cos(\varphi)\,.
\tag{9}
$$
**English original**

For a given value of $\theta$ the maximum violation is obtained for

**中文译文**

对于给定的 $\theta$ 值，最大违反在下式条件下取得：

$$
\varphi_{\mathrm{opt}}=\arccos\biggl(2\frac{\cos(2\theta)+\sin^{2}(2\theta)}{\sqrt{6-2\cos(4\theta)}}\biggr)\,.
\tag{10}
$$
**English original**

By plugging $\varphi_{\mathrm{opt}}$ into Eq. (9), and using Eq. (8) to obtain $\theta$ as a function of $P_{\mathrm{cont}}$ , we obtain $I$ as a function of $P_{\mathrm{cont}}$ . The resulting curve saturates the SDP obtained curve in Fig. 1.

**中文译文**

将 $\varphi_{\mathrm{opt}}$ 代入式 (9)，并利用式 (8) 将 $\theta$ 表示为 $P_{\mathrm{cont}}$ 的函数，我们便得到 $I$ 关于 $P_{\mathrm{cont}}$ 的函数。所得曲线达到图 1 中由 SDP 得到的曲线。

**English original**

Figure 2: Schematic representation of the alignment of the measurement axes in Alice’s optimal cheating strategy. The solid (dashed) axes correspond to Bob’s measurement on box $0$ ( $1$ ). The dotted axes correspond to Alice’s measurements (Alice always measures midway between Bob’s axes). The axes all lie in the $zx$ -plane. $\alpha=2\theta-\varphi_{\mathrm{opt}}$ . $\varphi_{\mathrm{opt}}$ and $\theta$ are related via Eq. (10).

**中文译文**

图 2：Alice 最优作弊策略中测量轴排列方式的示意图。实线（虚线）轴对应 Bob 在盒子 $0$（$1$）上的测量。点线轴对应 Alice 的测量（Alice 总是在 Bob 的两条轴正中间进行测量）。所有轴都位于 $zx$ 平面内。$\alpha=2\theta-\varphi_{\mathrm{opt}}$。$\varphi_{\mathrm{opt}}$ 与 $\theta$ 通过式 (10) 相关联。

![](figures/fig2.png){ width=70% }


### V.3 Alice’s control in the general case of an arbitrary number of tests

**English original**

For any given value of $n$ , Alice’s control is a function of the CHSH expectation value $E(I(W_{n+1})|\mathrm{\mathbf{w}}_{n})$ characterizing the behavior of the devices at step $n+1$ given the history $\mathrm{\mathbf{w}}_{n}$ . Alice’s control can therefore be expressed as

**中文译文**

对于任意给定的 $n$ 值，Alice 的控制力是 CHSH 期望值 $E(I(W_{n+1})|\mathrm{\mathbf{w}}_{n})$ 的函数；该期望值刻画了在给定历史 $\mathrm{\mathbf{w}}_{n}$ 时设备在第 $n+1$ 步的行为。因此，Alice 的控制力可表示为

$$
\begin{aligned}
P_{\mathrm{cont}}
&= \frac{1}{N}\sum_{n=1}^{N-1}\sum_{\{\mathrm{\mathbf{w}}_{n}\}}P(\mathrm{\mathbf{w}}_{n})\Theta(\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})-I_{\mathrm{th}})C\bigl(E(I(W_{n+1})\mid\mathrm{\mathbf{w}}_{n})\bigr) \\
&\qquad +\frac{1}{N}\sum_{\{\mathrm{\mathbf{w}}_{N}\}}P(\mathrm{\mathbf{w}}_{N})\Theta(\bar{I}_{N}(\mathrm{\mathbf{w}}_{N})-I_{\mathrm{th}}) \\
&\leq \frac{1}{N}\sum_{n=1}^{N-1}\sum_{\{\mathrm{\mathbf{w}}_{n}\}}P(\mathrm{\mathbf{w}}_{n})\Theta(\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})-I_{\mathrm{th}})C\bigl(E(I(W_{n+1})\mid\mathrm{\mathbf{w}}_{n})\bigr)+\frac{1}{N}\,.
\end{aligned}
\tag{11}
$$
**English original**

where $\Theta(\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})-I_{\mathrm{th}})$ is the unit step function, ensuring that only histories, such that the observed CHSH violation is no less than the threshold $I_{\mathrm{th}}$ , contribute. The partitioning of the sum into two is due to the fact that the boxes may have internal counters keeping track of the number of times they have been tested. Since the $N+1\,$ th use of the boxes, if occurring at all (i.e. if Bob picks $N$ ), necessarily occurs in the reveal phase, it is never part of the CHSH testing. Therefore, in an optimal cheating strategy Alice will program the boxes such that in their $N+1\,$ th use they behave deterministically.

**中文译文**

其中，$\Theta(\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})-I_{\mathrm{th}})$ 是单位阶跃函数，它确保只有观测到的 CHSH 违反不小于阈值 $I_{\mathrm{th}}$ 的历史才有贡献。将求和拆分为两部分，是因为盒子可能带有内部计数器，用来记录它们被测试的次数。盒子的第 $N+1$ 次使用如果发生（即如果 Bob 选择 $N$），必然发生在揭示阶段，因此它从不属于 CHSH 测试的一部分。所以，在最优作弊策略中，Alice 会对盒子进行编程，使其在第 $N+1$ 次使用时表现为确定性行为。

**English original**

For each history $\mathrm{\mathbf{w}}_{n}$ with $n\leq N-2$ we can define the set of all compatible histories $\mathrm{\mathbf{w}}_{N-1}$ that could have occurred had Bob carried out $N-1$ repetitions instead of $n$ . Alice’s control can therefore be re-expressed as

**中文译文**

对于每个满足 $n\leq N-2$ 的历史 $\mathrm{\mathbf{w}}_{n}$，我们可以定义所有相容历史 $\mathrm{\mathbf{w}}_{N-1}$ 的集合；如果 Bob 执行的不是 $n$ 次而是 $N-1$ 次重复，这些历史就可能发生。因此，Alice 的控制力可重新表示为

$$
P_{\mathrm{cont}}\leq\sum_{\{\mathrm{\mathbf{w}}_{N-1}\}}P(\mathrm{\mathbf{w}}_{N-1})\frac{1}{N}\sum_{n=1}^{N-1}\Theta(\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})-I_{\mathrm{th}})C\bigl(E(I(W_{n+1})\mid\mathrm{\mathbf{w}}_{n})\bigr)+\frac{1}{N}\,.
\tag{12}
$$
**English original**

Let $K(\mathrm{\mathbf{w}}_{N-1})$ denote the last repetition, up to and including the $N-1\,$ th repetition, of the compatible history $\mathrm{\mathbf{w}}_{N-1}$ for which the observed CHSH violation is no less than $I_{\mathrm{th}}$ , i.e.

**中文译文**

令 $K(\mathrm{\mathbf{w}}_{N-1})$ 表示在相容历史 $\mathrm{\mathbf{w}}_{N-1}$ 中，截至并包括第 $N-1$ 次重复，观测到的 CHSH 违反不小于 $I_{\mathrm{th}}$ 的最后一次重复，即

$$
K(\mathrm{\mathbf{w}}_{N-1})=\max_{k\leq N-1}\{k\mid \bar{I}_{k}(\mathrm{\mathbf{w}}_{k})\geq I_{\mathrm{th}}\}\,.
\tag{13}
$$
**English original**

We can bound Alice’s control probability as follows:

**中文译文**

我们可以如下界定 Alice 的控制概率：

$$
\begin{aligned}
P_{\mathrm{cont}}
&\leq \sum_{\{\mathrm{\mathbf{w}}_{N-1}\}}P(\mathrm{\mathbf{w}}_{N-1})\frac{1}{N}\sum_{n=1}^{N-1}\Theta(\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})-I_{\mathrm{th}})C\bigl(E(I(W_{n+1})\mid\mathrm{\mathbf{w}}_{n})\bigr)+\frac{1}{N} \\
&= \sum_{k=1}^{N-1}\sum_{\{\mathrm{\mathbf{w}}_{N-1}\mid K(\mathrm{\mathbf{w}}_{N-1})=k\}}P(\mathrm{\mathbf{w}}_{N-1})\frac{1}{N}\sum_{n=1}^{N-1}\Theta(\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})-I_{\mathrm{th}})C\bigl(E(I(W_{n+1})\mid\mathrm{\mathbf{w}}_{n})\bigr)+\frac{1}{N} \\
&\leq \sum_{k=1}^{N-1}\sum_{\{\mathrm{\mathbf{w}}_{N-1}\mid K(\mathrm{\mathbf{w}}_{N-1})=k\}}P(\mathrm{\mathbf{w}}_{N-1})\frac{1}{N}\sum_{n=1}^{k}C\bigl(E(I(W_{n+1})\mid\mathrm{\mathbf{w}}_{n})\bigr)+\frac{1}{N}\,.
\end{aligned}
\tag{14}
$$
**English original**

where we have used the fact that $\Theta(\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})-I_{\mathrm{th}})=0$ for all $n$ such that $K(\mathrm{\mathbf{w}}_{N-1})<n\leq N-1$ ; the inequality being due to the possibility of histories for which $\Theta(\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})-I_{\mathrm{th}})=0$ for at least one value of $n<K(\mathrm{\mathbf{w}}_{N-1})$ .

**中文译文**

这里我们使用了如下事实：对于所有满足 $K(\mathrm{\mathbf{w}}_{N-1})<n\leq N-1$ 的 $n$，都有 $\Theta(\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})-I_{\mathrm{th}})=0$；之所以出现该不等式，是因为可能存在这样的历史：至少对一个满足 $n<K(\mathrm{\mathbf{w}}_{N-1})$ 的 $n$ 值，有 $\Theta(\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})-I_{\mathrm{th}})=0$。

**English original**

Defining $K_{0}=\lceil(N-1)C(I_{\mathrm{th}})\rceil$ , we have

**中文译文**

定义 $K_{0}=\lceil(N-1)C(I_{\mathrm{th}})\rceil$，则有

$$
\begin{aligned}
P_{\mathrm{cont}}
&\leq \sum_{k=1}^{K_{0}-1}\sum_{\{\mathrm{\mathbf{w}}_{N-1}\mid K(\mathrm{\mathbf{w}}_{N-1})=k\}}P(\mathrm{\mathbf{w}}_{N-1})\frac{k}{N} \\
&\qquad +\sum_{k=K_{0}}^{N-1}\sum_{\{\mathrm{\mathbf{w}}_{N-1}\mid K(\mathrm{\mathbf{w}}_{N-1})=k\}}P(\mathrm{\mathbf{w}}_{N-1})\frac{k}{N}C\Bigl(\frac{1}{k}\sum_{n=1}^{k}E(I(W_{n+1})\mid\mathrm{\mathbf{w}}_{n})\Bigr)+\frac{1}{N} \\
&\leq \sum_{k=1}^{K_{0}-1}\sum_{\{\mathrm{\mathbf{w}}_{N-1}\mid K(\mathrm{\mathbf{w}}_{N-1})=k\}}P(\mathrm{\mathbf{w}}_{N-1})\frac{(N-1)C(I_{\mathrm{th}})}{N} \\
&\qquad +\sum_{k=K_{0}}^{N-1}\sum_{\{\mathrm{\mathbf{w}}_{N-1}\mid K(\mathrm{\mathbf{w}}_{N-1})=k,\,\mathrm{\mathbf{w}}_{N-1}\notin\pi_{k}(\varepsilon)\}}P(\mathrm{\mathbf{w}}_{N-1})\frac{N-1}{N}C\Bigl(\frac{1}{k}\sum_{n=1}^{k}E(I(W_{n+1})\mid\mathrm{\mathbf{w}}_{n})\Bigr) \\
&\qquad +\sum_{k=K_{0}}^{N-1}\sum_{\{\mathrm{\mathbf{w}}_{N-1}\mid K(\mathrm{\mathbf{w}}_{N-1})=k,\,\mathrm{\mathbf{w}}_{N-1}\in\pi_{k}(\varepsilon)\}}P(\mathrm{\mathbf{w}}_{N-1})\frac{N-1}{N}C\Bigl(\frac{1}{k}\sum_{n=1}^{k}E(I(W_{n+1})\mid\mathrm{\mathbf{w}}_{n})\Bigr)+\frac{1}{N} \\
&\qquad \forall\,\varepsilon\geq 0\,.
\end{aligned}
\tag{15}
$$
**English original**

where in the second sum in the first line we have used the concavity of $C$ , in the first sum in the second line the fact that $K_{0}-1\leq(N-1)C(I_{\mathrm{th}})$ , and where $\pi_{k}\left(\varepsilon\right)$ is the set of all histories satisfying

**中文译文**

其中，在第一行的第二个求和中我们使用了 $C$ 的凹性；在第二行的第一个求和中使用了 $K_{0}-1\leq(N-1)C(I_{\mathrm{th}})$ 这一事实；而 $\pi_{k}\left(\varepsilon\right)$ 是满足下式的所有历史的集合：

$$
\bar{I}_{k}\left(\mathbf{w}_{k}\right)-\frac{1}{k}\sum_{n=1}^{k}E\left(I\left(W_{n}\right)\mid\mathbf{w}_{n-1}\right)\geq\varepsilon\,.
\tag{16}
$$
**English original**

In Appendix D we show that the probability of occurrence of $\pi_{k}(\varepsilon)$ is bounded by

**中文译文**

在附录 D 中，我们证明 $\pi_{k}(\varepsilon)$ 的发生概率满足如下界：

$$
P\left(\pi_{k}\left(\varepsilon\right)\right)\leq\exp\biggl(-\frac{k\varepsilon^{2}}{2D^{2}}\biggr)\,,
\tag{17}
$$
**English original**

where $D=4+2\sqrt{2}$ , and so

**中文译文**

其中 $D=4+2\sqrt{2}$，因此

$$
\sum_{k=K_{0}}^{N-1}P\left(\pi_{k}\left(\varepsilon\right)\right)\leq\frac{\exp\bigl(-\frac{K_{0}\varepsilon^{2}}{2D^{2}}\bigr)-\exp\bigl(-\frac{N\varepsilon^{2}}{2D^{2}}\bigr)}{1-\exp\left(-\frac{\varepsilon^{2}}{2D^{2}}\right)}=Q(\varepsilon)\,.
\tag{18}
$$
**English original**

Figure 3: Upper bound on Alice’s control as a function of $\log_{10}N$ . The curve presents the results of numerical solutions of Eq. (19) for different values of $N$ , given $I_{\mathrm{th}}=2\sqrt{2}(1-\frac{1}{\sqrt{N}})$ . In the limit $N\rightarrow\infty$ Alice’s control tends to the asymptote $\cos^{2}\bigl(\frac{\pi}{8}\bigr)\simeq 0.854$ (represented by the dashed curve).

**中文译文**

图 3：Alice 控制力的上界随 $\log_{10}N$ 变化的关系。在给定 $I_{\mathrm{th}}=2\sqrt{2}(1-\frac{1}{\sqrt{N}})$ 时，该曲线给出了针对不同 $N$ 值对式 (19) 进行数值求解的结果。在 $N\rightarrow\infty$ 的极限下，Alice 的控制力趋于渐近线 $\cos^{2}\bigl(\frac{\pi}{8}\bigr)\simeq 0.854$（以虚线表示）。

![](figures/fig3.png){ width=70% }


**English original**

Making use of this last inequality, we finally get that

**中文译文**

利用最后这个不等式，我们最终得到

$$
\begin{aligned}
P_{\mathrm{cont}}
&\leq \frac{N-1}{N}\sum_{k=1}^{K_{0}-1}\sum_{\{\mathrm{\mathbf{w}}_{N-1}\mid K(\mathrm{\mathbf{w}}_{N-1})=k\}}P(\mathrm{\mathbf{w}}_{N-1})C(I_{\mathrm{th}}) \\
&\qquad +\frac{N-1}{N}\min_{\varepsilon\geq 0}\Biggl[\sum_{k=K_{0}}^{N-1}\sum_{\{\mathrm{\mathbf{w}}_{N-1}\mid K(\mathrm{\mathbf{w}}_{N-1})=k,\,\mathrm{\mathbf{w}}_{N-1}\notin\pi_{k}(\varepsilon)\}}P(\mathrm{\mathbf{w}}_{N-1})C(\bar{I}_{k}(\mathrm{\mathbf{w}}_{k})-\varepsilon) \\
&\qquad\qquad +\sum_{k=K_{0}}^{N-1}\sum_{\{\mathrm{\mathbf{w}}_{N-1}\mid K(\mathrm{\mathbf{w}}_{N-1})=k,\,\mathrm{\mathbf{w}}_{N-1}\in\pi_{k}(\varepsilon)\}}P(\mathrm{\mathbf{w}}_{N-1})\Biggr]+\frac{1}{N} \\
&\leq \frac{N-1}{N}\min_{\varepsilon\geq 0}\Biggl[\sum_{k=1}^{K_{0}-1}\sum_{\{\mathrm{\mathbf{w}}_{N-1}\mid K(\mathrm{\mathbf{w}}_{N-1})=k\}}P(\mathrm{\mathbf{w}}_{N-1})C(I_{\mathrm{th}}-\varepsilon) \\
&\qquad\qquad +\sum_{k=K_{0}}^{N-1}\sum_{\{\mathrm{\mathbf{w}}_{N-1}\mid K(\mathrm{\mathbf{w}}_{N-1})=k\}}P(\mathrm{\mathbf{w}}_{N-1})C(I_{\mathrm{th}}-\varepsilon) \\
&\qquad\qquad +\sum_{k=K_{0}}^{N-1}\sum_{\{\mathrm{\mathbf{w}}_{N-1}\mid K(\mathrm{\mathbf{w}}_{N-1})=k,\,\mathrm{\mathbf{w}}_{N-1}\in\pi_{k}(\varepsilon)\}}P(\mathrm{\mathbf{w}}_{N-1})\bigl(1-C(I_{\mathrm{th}}-\varepsilon)\bigr)\Biggr]+\frac{1}{N} \\
&\leq \frac{N-1}{N}\min_{\varepsilon\geq 0}\Bigl[C(I_{\mathrm{th}}-\varepsilon)+\bigl(1-C(I_{\mathrm{th}}-\varepsilon)\bigr)Q(\varepsilon)\Bigr]+\frac{1}{N}\,.
\end{aligned}
\tag{19}
$$
**English original**

Note that if we choose the behavior of $\varepsilon$ such that in the limit $N\rightarrow\infty$ it decays more slowly than $N^{-1/2}$ , then $\lim_{N\rightarrow\infty}Q(\varepsilon)\rightarrow 0$ and the bound tends to $C(I_{\mathrm{th}})$ . For finite $N$ it seems unlikely that the bound is saturable, since $Q(\varepsilon)$ is non-vanishing. Fig. 3 presents the results of numerical solutions of Eq. (19) for different values of $N$ for $I_{\mathrm{th}}=2\sqrt{2}-\frac{1}{\sqrt{N}}$ . In particular, in the limit $N\rightarrow\infty$ Alice’s control tends to $\cos^{2}\left(\frac{\pi}{8}\right)$ , recovering the result of [30].

**中文译文**

注意，如果我们选择 $\varepsilon$ 的变化方式，使其在 $N\rightarrow\infty$ 的极限下比 $N^{-1/2}$ 衰减得更慢，那么 $\lim_{N\rightarrow\infty}Q(\varepsilon)\rightarrow 0$，且该界趋于 $C(I_{\mathrm{th}})$。对于有限的 $N$，由于 $Q(\varepsilon)$ 非零，该界似乎不太可能达到。图 3 给出了在 $I_{\mathrm{th}}=2\sqrt{2}-\frac{1}{\sqrt{N}}$ 时，针对不同 $N$ 值对式 (19) 进行数值求解的结果。特别地，在 $N\rightarrow\infty$ 的极限下，Alice 的控制力趋于 $\cos^{2}\left(\frac{\pi}{8}\right)$，从而重新得到 [30] 的结果。

## VI Summary

**English original**

Distrustful cryptography presents unique challenges in device-independent settings, which are absent in non-distrustful cryptographic tasks, such as quantum key-distribution. In particular, since the parties do not trust each other and may have conflicting goals, they cannot work together to certify the presence of nonlocality. In [30, 35] this problem was circumvented by making use of the pseudo-telepathic nature of GHZ correlations, but pseudo-telepathy is absent in a CHSH setting. In this work we have shown that pseudo-telepathy is not essential for doing device-independent distrustful cryptography. This was achieved by reformulating the device-independent bit commitment protocol of [30], such that it relies on sequential testing of the CHSH inequality (instead of the single-shot testing of GHZ correlations), but (in the asymptotic limit) nevertheless achieves the same security. The security analysis was therefore carried out in the most general settings, where the devices may have long-term quantum memory.

**中文译文**

不互信密码学在设备无关情形下面临独特的挑战，而这些挑战并不存在于量子密钥分发等非不互信密码任务中。特别是，由于双方互不信任且目标可能相互冲突，他们无法合作认证非局域性的存在。在 [30, 35] 中，这一问题通过利用 GHZ 关联的伪心灵感应性质得以规避，但在 CHSH 情形中不存在伪心灵感应。在本工作中，我们证明了开展设备无关不互信密码学并不必须依赖伪心灵感应。我们通过重新表述 [30] 的设备无关比特承诺协议实现了这一点：使其依赖对 CHSH 不等式的序贯测试（而非对 GHZ 关联的单次测试），但在渐近极限下仍能达到相同的安全性。因此，安全性分析是在最一般的情形下进行的，其中设备可能具有长期量子存储器。

**English original**

Strictly speaking, the protocol we have presented is not a bit commitment protocol since Alice cannot choose the reveal time at will. This by itself is not necessarily a problem. For example, it does not prevent the protocol from being used to implement coin flipping. However, if we would like Alice to have the freedom to choose the reveal time, then we can do so either, as shown in Appendix B, at the price of increasing her control, or, as shown in Appendix C, at the price of using additional resources, i.e. by working in the large office scenario, where the parties have access to many pairs of boxes, which can be measured in parallel.

**中文译文**

严格来说，我们给出的协议并不是一个比特承诺协议，因为 Alice 不能随意选择揭示时间。这一点本身未必构成问题。例如，它并不妨碍该协议被用于实现抛硬币。然而，如果我们希望 Alice 可以自由选择揭示时间，那么可以采用两种方式做到这一点：或者如附录 B 所示，以增加她的控制力为代价；或者如附录 C 所示，以使用额外资源为代价，即在大型办公室情形下工作，其中双方可以使用许多对能够并行测量的盒子。

**English original**

Our work opens the door for real-life implementation of device-independent bit commitment and coin flipping. The protocol of [30] requires the ability to reliably produce particles in a GHZ state and to store, manipulate, and transmit them while maintaining their coherence. The protocol presented here, on the other hand, only requires manipulation of bipartite entanglement which is simpler given state-of-the-art technology.

**中文译文**

我们的工作为设备无关比特承诺和抛硬币的实际实现打开了大门。[30] 的协议要求能够可靠地产生处于 GHZ 态的粒子，并在保持其相干性的同时对其进行存储、操纵和传输。相比之下，本文给出的协议只需操纵二体纠缠；以当前最先进的技术而言，这更为简单。

**English original**

Finally, we point out that the techniques developed in this work are not especially tailored for device-independent bit commitment, and we expect them to be useful, and possibly even essential, for other distrustful cryptographic tasks, such as non-bit commitment-based device-independent coin flipping, and device-independent oblivious transfer.

**中文译文**

最后，我们指出，本工作所发展的技术并非专门针对设备无关比特承诺而定制；我们预计，这些技术对于其他不互信密码任务也会有用，甚至可能不可或缺，例如不基于比特承诺的设备无关抛硬币，以及设备无关不经意传输。

###### Acknowledgements.

**English original**

S.P., S.M., and J.S. acknowledge financial support from the European Union under the projects QCS, QALGO, and DIQIP, and from the F.R.S.-FNRS under the project DIQIP. S.P. acknowledges support from the Brussels-Capital Region through a BB2B grant. S.P. is a Research Associate of the Fonds de la Recherche Scientifique F.R.S.- FNRS (Belgium). J.S. was a postdoctoral researcher of the Fonds de la Recherche Scientifique F.R.S.- FNRS (Belgium) at the time this research was carried out. N.A acknowledges support from the BSF (grant no. 32/08) and the Niedersachsen-Israeli Research Cooperation Program. The Matlab toolboxes [44] [44] and [45] [45] were used to solve the SDP problem Eq. (7).

**中文译文**

S.P.、S.M. 和 J.S. 感谢欧盟通过 QCS、QALGO 和 DIQIP 项目提供的资助，以及 F.R.S.-FNRS 通过 DIQIP 项目提供的资助。S.P. 感谢布鲁塞尔首都大区通过一项 BB2B 资助提供的支持。S.P. 是科学研究基金会 F.R.S.-FNRS（比利时）的研究员。开展本项研究时，J.S. 是科学研究基金会 F.R.S.-FNRS（比利时）的博士后研究员。N.A 感谢 BSF（资助编号 32/08）和下萨克森—以色列研究合作计划的支持。求解式 (7) 的 SDP 问题时使用了 Matlab 工具箱 [44] [44] 和 [45] [45]。
