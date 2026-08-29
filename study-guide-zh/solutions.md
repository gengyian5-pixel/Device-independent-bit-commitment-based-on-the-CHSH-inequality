# 习题详解

请先尝试每一道练习，再阅读相应小节。公式编号指 Aharon *等人*，NJP **18**, 025014 (2016)。

---

## 第 1 章

**1.1.** 对 Bob 的 POVM 求迹：$\sum_{r^1}\operatorname{Tr}(\rho\,\Pi_{r^0|s^0}^0\otimes\Pi_{r^1|s^1}^1)=\operatorname{Tr}(\rho_A\Pi_{r^0|s^0}^0)$，结果与 $s^1$ 无关。

**1.2.** 记忆和时钟会依据盒子自身的历史改变所使用的 POVM；只要测量时通信被阻断，它们并不会产生一个依赖于*另一个*盒子当前输入的张量因子。

**1.3.** 考虑确定性的局域赋值 $a(x),b(y)$。组合式 $a(0)b(0)+a(0)b(1)+a(1)b(0)-a(1)b(1)=a(0)(b(0)+b(1))+a(1)(b(0)-b(1))$ 等于 $\pm 2$，因为 $b(0)\pm b(1)$ 中一个为 $0$，另一个为 $\pm 2$。取平均可得：$\lvert I\rvert\le 2$。

**1.4.** $\sigma_\theta=\cos\theta\,\sigma_z+\sin\theta\,\sigma_x$。在 $|\phi^+\rangle$ 上，$\langle\sigma_z\otimes\sigma_z\rangle=\langle\sigma_x\otimes\sigma_x\rangle=1$，$\langle\sigma_z\otimes\sigma_x\rangle=0$，因此 $\langle\sigma_\alpha\otimes\sigma_\beta\rangle=\cos(\alpha-\beta)$。Alice 取 $0,\pi/2$、Bob 取 $\pi/4,-\pi/4$ 时，每个 CHSH 关联量的绝对值都是 $1/\sqrt{2}$，且符号组合得到 $2\sqrt{2}$。

**1.5.** 输入均匀分布：四个输入对中每一个的概率均为 $1/4$。因子 $4$ 与之抵消，所以 $\mathbb{E}[I(W)]$ 就是 CHSH 和。

**1.6.** Bob 必须在没有 Alice 协助的情况下检验非局域性，并且必须通过测量*自己的*盒子检查她的开启。GHZ 能确保一个涉及所揭示比特的关系成立，因此一次测量可以同时完成这两项任务。CHSH 不可能以概率一获胜，所以单次 CHSH 检验无法兼作确定性的检查。还需要其他机制（隐藏哪一轮是检查轮）。

**1.7.** 对每个输入对，PR 盒满足 $P(r^0,r^1|s^0,s^1)=\frac12\delta_{r^0\oplus r^1,\,s^0 s^1}$。边缘分布均匀，且与另一个输入无关。对于 CHSH，每个输入对都贡献 $+1$，故 $I=4$。

**1.8 / 1.9 / 1.10.** 见第 5、8、9 章。对于 1.10：$Z_{k+1}-Z_k=I(W_{k+1})-\mathbb{E}[I(W_{k+1})\mid\mathbf{W}_k]$，其绝对值至多为 $4+2\sqrt{2}$。对 $Z_{k+1}$ 取 $\mathbb{E}[\,\cdot\mid\mathbf{W}_k]$ 会抵消该增量，因此 $Z_k$ 是一个鞅。

---

## 第 5 章

**5.1 表。**

| $c$ | $b$ | $s^c$ | $s^{\bar c}$ | $(s^0,s^1)$ | 是否为相等输入对？ |
|---|---|---|---|---|---|
| 0 | 0 | 2 | 0 | (2,0) | $i=2$：$(2,0)$ |
| 0 | 1 | 3 | 1 | (3,1) | $i=3$：$(3,1)$ |
| 1 | 0 | 2 | 0 | (0,2) | $i=0$：$(0,2)$ |
| 1 | 1 | 3 | 1 | (1,3) | $i=1$：$(1,3)$ |

**5.2.** 盒子 0 在输入 $0,1$ 时分别测量 $\sigma_x,\sigma_z$。盒子 1 在输入 $0,1$ 时分别测量 $\sigma_{\pi/4},\sigma_{3\pi/4}$。于是

$$
\langle\sigma_x\otimes\sigma_{\pi/4}\rangle=\cos(\pi/2-\pi/4)=1/\sqrt{2},
$$

$$
\langle\sigma_x\otimes\sigma_{3\pi/4}\rangle=\cos(\pi/2-3\pi/4)=1/\sqrt{2},
$$

$$
\langle\sigma_z\otimes\sigma_{\pi/4}\rangle=\cos(0-\pi/4)=1/\sqrt{2},
$$

$$
\langle\sigma_z\otimes\sigma_{3\pi/4}\rangle=\cos(0-3\pi/4)=-1/\sqrt{2}.
$$

令 $A_0=\sigma_x$、$A_1=\sigma_z$、$B_0=\sigma_{\pi/4}$、$B_1=\sigma_{3\pi/4}$，则 CHSH $I=\langle A_0B_0\rangle+\langle A_0B_1\rangle+\langle A_1B_0\rangle-\langle A_1B_1\rangle$ 等于 $2\sqrt{2}$。算符恒等关系：检查表格即可看出，盒子 0 的输入 $i$ 与盒子 1 的输入 $i+2\bmod 4$ 对应同一算符。

---

## 第 6 章

**6.1.** $q=r\oplus ab$。若 $b=0$，则 $q=r$。若 $b=1$，则根据 $a$ 的取值，$q=r$ 或 $q=r\oplus 1$。令牌检查恰好就是这两个条件的析取。

**6.3.** 除非 $a=b=1$，否则 $ab=0$，其概率为 $3/4$。这就是 §4 中的策略 A。

**6.4.** 如果仅在 CHSH 检验中从未出现的延迟之后才测量保留的盒子，Alice 可以这样编程：在公开时序下达到完美 CHSH；在延迟测量中采取确定性行为（两个开启值都被接受）。

---

## 第 7 章

**7.1–7.2.** 诚实情形下 $P(a,b)=1/4$。当 $b=0$ 时，对 $a$ 的两个取值都有 $m=r^c$，由此产生 $P(0,0\mid 2,0)+P(1,0\mid 2,1)$ 前的因子 $2$。当 $b=1$ 时，$m=r$ 和 $m=r\oplus 1$ 产生四项 $P(0,1\mid 3,0)$、$P(0,1\mid 3,1)$、$P(1,1\mid 3,1)$、$P(1,1\mid 3,0)$。

**7.3.** 由无信号条件和正性：

$$
P(0,0\mid 2,0)\le P(r^c=0\mid s^c=2),\qquad P(1,0\mid 2,1)\le P(r^c=1\mid s^c=2),
$$

所以两者之和 $\le 1$。对每个 $m\in\{0,1\}$，

$$
P(r=m,g=0\mid s=2,m)+P(g=1\mid m)\le P(g=0\mid m)+P(g=1\mid m)=1,
$$

且 $P(g=1\mid m)=\sum_r P(r,1\mid 3,m)$。将 $m=0$ 与 $m=1$ 两种情形相加，得到

$$
A+B\le 2,\qquad A:=P(0,0\mid 2,0)+P(1,0\mid 2,1)\le 1,
$$

其中 $B$ 是 $b=1$ 时四项之和。于是

$$
P_{\mathrm{gain}}=\frac14\max(2A+B)=\frac14\max\bigl(A+(A+B)\bigr)\le\frac14(1+2)=\frac34.
$$

**7.4.** 若 $r^c=b$，则只要 $ab=0$，也就是以 $3/4$ 的概率，就有 $q=r^c\oplus ab$ 等于 $b$。

**7.5.** 设置 $s^{\bar c}=0$ 和 $s^c=2$ 对应同一可观测量，所以当 $b=0$ 时，Bob 的结果与 Alice 的结果相同；又因为 $q=r^c$，所以他总是猜中 $2$。当 $b=1$ 时，两可观测量相差 $\pi/2$，因此 $\langle\sigma\otimes\sigma\rangle=0$，他有一半概率猜对。平均值为 $3/4$。

---

## 第 8 章

**8.1.** 开启 $0$ 要求 $q=r^c$。Alice 可以直接把 $q$ 复制到所公布的 $r^c$，无需再做测量。剩余的自由度为：承诺阶段的结果 $k=q$，以及开启 $1$ 时的结果 $l$。因此共有四种结果。

**8.6.** 在 $|\phi^+\rangle$ 上，相对角度为 $\theta$ 时，$P(r^A=r^B)=\frac{1+\cos\theta}{2}=\cos^2(\theta/2)$。

**8.8.** 每个关联量都是两测量轴之差的余弦：

$$
\begin{align*}
\langle\sigma_{2\theta}\otimes\sigma_{2\theta-\varphi}\rangle&=\cos\varphi,\\
\langle\sigma_{2\theta}\otimes\sigma_{4\theta-\varphi}\rangle&=\cos(2\theta-\varphi),\\
\langle\sigma_z\otimes\sigma_{2\theta-\varphi}\rangle&=\cos(\varphi-2\theta),\\
\langle\sigma_z\otimes\sigma_{4\theta-\varphi}\rangle&=\cos(\varphi-4\theta).
\end{align*}
$$

符号为 $+{+}{+}-$ 的 CHSH 组合利用余弦的偶性可化简为 (9)。

**8.9.** $\partial I/\partial\varphi=2\sin(2\theta-\varphi)-\sin(4\theta-\varphi)-\sin\varphi=0$。和差化积恒等式 $\sin(4\theta-\varphi)+\sin\varphi=2\sin(2\theta)\cos(2\theta-\varphi)$ 在 $\cos(2\theta-\varphi)\ne 0$ 时给出 $\tan(2\theta-\varphi)=\sin(2\theta)$。论文中的反余弦表达式是一个解分支的闭式形式。检查：$\theta=\pi/4$ 时，$\varphi_{\mathrm{opt}}=\pi/4$ 且 $I=2\sqrt{2}$。此时 $P_{\mathrm{cont}}=\cos^2(\pi/8)$。

**8.11.** 当 $\theta\to 0$ 时，Alice 与 Bob 的测量轴重合，$P_{\mathrm{cont}}\to 1$，而 CHSH 组合趋向一个局域值 $\le 2$。

---

## 第 9 章

**9.1.** $n$ 均匀分布。当 $n<N$ 时，只要经验检验通过，控制能力就是下一次使用中*条件* CHSH 值所对应的 $C$。当 $n=N$ 时，下一次使用未经检验：Alice 在该分支上把控制能力设为 $1$，从而贡献 $\le 1/N$。

**9.7.** 对差分 $\le D=4+2\sqrt{2}$ 的 $Z_k$ 应用 Azuma–Hoeffding 不等式，得到 (17)。对等比级数 $\sum_{k=K_0}^{N-1}e^{-k\alpha}$ 求和，其中 $\alpha=\varepsilon^2/(2D^2)$，便得到 $Q(\varepsilon)$。

**9.8.** $\sin(\pi/8)=\sqrt{2-\sqrt{2}}/2$，所以有理化后 $1/\sin^2(\pi/8)=4/(2-\sqrt{2})=4+2\sqrt{2}$。这只是巧合，并非引理。

**9.9.** 图和正文应使用同一个公式。两种选择在 $N\to\infty$ 时都趋于 $2\sqrt{2}$。

**9.10.** 松弛来源：(i) 在 $\{n\le K\}$ 上将 $\Theta$ 替换为 $1$；(ii) 在 $\pi_k(\varepsilon)$ 上使用 $C\le 1$；(iii) Azuma 界对这个鞅并不紧；(iv) 末轮项 $1/N$。

---

## 第 10 章

**10.3.** 诚实 PR 策略：当 Bob 输入 $s^1=1$ 时，$g=r^0\oplus r^1=s^0$。若 $q=r^0$，则猜测值就是 $s^0$。只有当 $s^0=a=1$ 时失败（概率为 $1/4$）。因此 $P_{\mathrm{gain}}=3/4$。

**10.5.** 令 $\alpha=P(r^0=0\mid s^0=1)$，$q_y=P(r^1=0\mid s^1=y)$。表达式 (21) 等于

$$
T=1+2\bigl[P(00\mid s^0=1,s^1=0)+P(10\mid s^0=1,s^1=1)\bigr],
$$

并且每个联合概率都不大于相应的边缘概率，所以

$$
T\le 1+2\bigl[\min(\alpha,q_0)+\min(1-\alpha,q_1)\bigr]\le 1+2\cdot 1=3.
$$

因此 $P_{\mathrm{cont}}=T/4\le 3/4$。取等策略：Bob 的盒子始终输出 $0$；Alice 用 $r^0=0$ 开启 $0$，并用任意 $r^0$ 开启 $1$（此时由于 Bob 的 $s^1$ 随机，PR 检验以 $1/2$ 的概率成立吗？等等——如果 Bob 始终输出 $0$：开启 $0$ 以概率 $1$ 成功；开启 $1$ 成功当且仅当 $r^0\oplus 0=s^0 s^1=s^1$，即 $r^0=s^1$。Alice 不知道 $s^1$，所以她以一半概率成功。平均 $P_{\mathrm{cont}}=\frac12(1+\frac12)=\frac34$。）

**10.8.** $d$ 与她希望开启的比特一致的概率为 $1/2$：此时成功概率是原来的 $P_{\mathrm{cont}}$。两者不一致的概率为 $1/2$：此时 Bob 跳过非局域性检查，令牌可向两个值开启，成功概率为 $1$。混合后为 $\frac12(P_{\mathrm{cont}}+1)$。

**10.10.** 协议 C' 仅使用第 $1,\dots,n-1$ 对盒子进行 CHSH 检验：检验更少，而且 Alice 知道检验的是哪些盒子，因此控制能力不会降低。协议 C'' 还让第 $k$ 对盒子中的盒子 $i$ 获得此前所有 $i$ 号盒子的历史：这构成序贯记忆，控制能力同样不会降低。除揭示时间可以自由选择、且其他盒子对上的检验同时进行之外，C'' 就是序贯协议。因此，序贯情形的 $P_{\mathrm{cont}}$ 上界也是大型办公室情形的上界。
