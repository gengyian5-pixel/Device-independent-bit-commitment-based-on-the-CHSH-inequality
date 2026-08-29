# 11. 撰写论文

仅在完成重构检查清单后使用本章。目标是用你自己的语言写出一篇与 Aharon *et al.*, NJP **18**, 025014 (2016) 具有相同*论断和结构*的稿件。

## 11.1 标题、作者、关键词

- 标题可以保持描述性：设备无关（device-independent, DI）、比特承诺（bit commitment）、CHSH。
- NJP 使用的关键词：量子密码学、设备无关量子信息、比特承诺、非局域性。

## 11.2 摘要（一段）

必须包含：

1. 以往的 DI 比特承诺/掷币（bit commitment/coin flipping, BC/CF）使用 GHZ；在二方 DI 任务中，这一点很独特。
2. GHZ 伪心灵感应（pseudo-telepathy）对于那些证明至关重要。
3. 本工作：CHSH 测试、与 Silman *et al.* 相同的作弊概率、具有记忆的设备。
4. 限制条件：揭示时间固定。
5. 后量子改写：总体安全性更高。

目标长度：约 150–180 个英文单词。除了可能出现的两个数值 $0.8536$ 和 $0.75$，不要加入公式（已发表的摘要没有公式；引言中给出了这些数值）。

## 11.3 第 1 节——引言

段落规划（已发表版本的顺序很好；借用其*顺序*，不要照搬句子）：

1. 一般意义下的密码学假设；量子与经典；设备依赖与 DI。
2. 通过贝尔测试实现 DI；以设备无关量子密钥分发（device-independent quantum key distribution, DIQKD）为旗舰应用；防范黑客攻击的动机。
3. 其他 DI 任务（随机性、自测试、估计、多体纠缠）。
4. 互不信任密码学（distrustful cryptography）带来的额外挑战（目标相互冲突）。
5. Silman11 / Aharon14：GHZ；整个互不信任密码学类别能否实现 DI 仍是开放问题。
6. 使用 GHZ 的原因（伪心灵感应；用相同测量进行测试和检查）。
7. 为什么 CHSH 是接下来很自然的问题（RUV；实验中的 EPR 与 GHZ 对比）。
8. **本工作：**协议、数值、记忆、不完美设备、固定揭示时间、掷币仍然可行、附录 B–C、附录 A。
9. 各节路线图。

至少需要引用：Mayers–Yao；Barrett–Hardy–Kent；Clauser *et al.*；Acín *et al.* 的 DIQKD；Pironio *et al.* 2009；Reichardt–Unger–Vazirani；Lo–Chau；Mayers；Spekkens–Rudolph；Chailloux–Kerenidis；Silman *et al.* 2011；Greenberger–Horne–Zeilinger；Gisin–Méthot–Scarani（不存在二方伪心灵感应）；Kent 的相对论比特承诺。

## 11.4 第 2 节——背景

**2.1 比特承诺。** 各阶段的定义、$P_{\mathrm{cont}}$、$P_{\mathrm{gain}}$、完美性、平衡性、CK 界。

**2.2 设备无关性。** 五项假设；公式 (1)；记忆/时钟；“发送一个盒子”的含义；屏蔽（shielding）与相对论方法的对比。

## 11.5 第 3 节——协议

- 符号说明段落（$S^i_k$、$W_k$、$\sigma_\theta$）。
- 诚实关联式 (2) 和相等的输入对；测量表格。
- 含噪情形。
- 带编号的协议 1–3，其中包含时刻 $t^a,t^b,t^c,t^d,t_i$。
- $\bar I_n$ 和 $I(W_k)$ 的公式 (3)–(4)。
- 完备性讨论（统计性中止与含噪揭示中止）。
- 时序论证（保留的盒不能知道自己将用于揭示）。
- “并非严格意义上的比特承诺”段落 + 指向附录 B–C 的说明。

需要补回的脚注：私下选取的 $n$；指示量中的因子 $4$；区间 $(t_i,t_{i+1}]$。

## 11.6 第 4 节——Alice 的安全性

- Bob 的一般策略；陈列式 (5)；NS $\Rightarrow 3/4$，其中 NS 指无信号条件（no-signalling）。
- 两种饱和策略（经典盒；诚实 EPR + 输入 $0$）。
- 用一句话说明：与 Silman *et al.* 的结果相同。

## 11.7 第 5 节——Bob 的安全性

在第一段中向读者说明三个小节的安排。

**5.1** 四结果正算子值测度（positive operator-valued measure, POVM）；式 (6)；半正定规划（semidefinite program, SDP）(7)；NPA 第 2 层级；图 1（根据 5.2 生成）。

**5.2** 显式策略；式 (8)–(10)；图 2；达到 SDP 的最优值。

**5.3** 记忆；式 (11)–(19)；图 3；极限 $\cos^2(\pi/8)$。将鞅引理移至附录 D。

## 11.8 第 6 节——总结

重申：伪心灵感应并非必需；顺序 CHSH + 隐藏的 $n$ + 固定时刻已经足够；已纳入记忆；实验动机（EPR 与 GHZ 对比）；这些技术应可迁移到无需比特承诺的 DI 掷币以及 DI 不经意传输（oblivious transfer, OT）。

## 11.9 图

| 图 | 内容 | 生成方式 |
|---|---|---|
| 1 | $P_{\mathrm{cont}}$ 关于 $I_{\mathrm{th}}$ 的曲线 | 式 (8)–(10) 的参数图 |
| 2 | $zx$ 平面内的坐标轴 | 示意图（实线 / 虚线 / 点线） |
| 3 | 有限-$N$ 界关于 $\log_{10} N$ 的曲线 | 式 (19) 的数值最小值 |

运行 `python scripts/reconstruct_figures.py`。已发表的图 1 是解析曲线；图 3 是数值上界，而不是实验结果。

## 11.10 必须准确把握的语气和论断

- 不要声称实现了完美比特承诺。
- 不要声称协议是平衡的。
- 不要声称主协议中揭示时间可由 Alice 选择。
- 不要声称有限-$N$ 界是紧的。
- 应当声称，**在无限次测试极限下**，结果与 Silman *et al.* 相同。
- 应当声称使用屏蔽，而不是类空间隔离。
- 应当提到，总是发送同一个盒子会帮助 Alice。

## 11.11 初稿完成之后

1. 对照 [reconstruction-checklist.md](reconstruction-checklist.md) 检查每个带编号的公式。
2. 检查图 1 在 $I=2\sqrt{2}$ 时达到 $\cos^2(\pi/8)$。
3. 检查图 3 的 $I_{\mathrm{th}}(N)$ 与其图注一致。
4. 确认你没有在相对论段落中混用 arXiv 和 NJP 的措辞；选择其中一个版本。
5. 如果使用了 YALMIP/SeDuMi 或 Python SDP 求解器，请添加致谢。
