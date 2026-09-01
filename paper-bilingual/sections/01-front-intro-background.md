# Device-Independent Bit Commitment based on the CHSH Inequality / 基于 CHSH 不等式的设备无关比特承诺

**English original**

N. Aharon<sup>1,2</sup>, S. Massar<sup>3</sup>, S. Pironio<sup>3</sup>, and J. Silman<sup>3</sup>

**中文译文**

N. Aharon<sup>1,2</sup>、S. Massar<sup>3</sup>、S. Pironio<sup>3</sup> 和 J. Silman<sup>3</sup>

**English original**

Affiliation: <sup>1</sup>School of Physics and Astronomy, Tel-Aviv University, Tel-Aviv 69978, Israel; <sup>2</sup>Racah Institute of Physics, The Hebrew University of Jerusalem, Jerusalem 91904, Israel; <sup>3</sup>Laboratoire d’Information Quantique, Université Libre de Bruxelles (ULB), 1050 Bruxelles, Belgium

**中文译文**

单位：<sup>1</sup>以色列特拉维夫大学物理与天文学学院，特拉维夫 69978；<sup>2</sup>以色列耶路撒冷希伯来大学拉卡物理研究所，耶路撒冷 91904；<sup>3</sup>比利时布鲁塞尔自由大学（ULB）量子信息实验室，布鲁塞尔 1050

**English original**

*New J. Phys.* **18**, 025014 (2016); doi:[10.1088/1367-2630/18/2/025014](https://doi.org/10.1088/1367-2630/18/2/025014); [arXiv:1511.06283](https://arxiv.org/abs/1511.06283).

**中文译文**

《新物理学杂志》**18**, 025014 (2016)；doi:[10.1088/1367-2630/18/2/025014](https://doi.org/10.1088/1367-2630/18/2/025014)；[arXiv:1511.06283](https://arxiv.org/abs/1511.06283)。


## Abstract / 摘要

**English original**

Bit commitment and coin flipping occupy a unique place in the device-independent landscape, as the only device-independent protocols thus far suggested for these tasks are reliant on tripartite GHZ correlations. Indeed, we know of no other bipartite tasks, which admit a device-independent formulation, but which are not known to be implementable using only bipartite nonlocality. Another interesting feature of these protocols is that the pseudo-telepathic nature of GHZ correlations – in contrast to the generally statistical character of nonlocal correlations, such as those arising in the violation of the CHSH inequality – is essential to their formulation and analysis. In this work, we present a device-independent bit commitment protocol based on CHSH testing, which achieves the same security as the optimal GHZ-based protocol. The protocol is analyzed in the most general settings, where the devices are used repeatedly and may have long-term quantum memory. We also recast the protocol in a post-quantum setting where both honest and dishonest parties are restricted only by the impossibility of signaling, and find that overall the supra-quantum structure allows for greater security.

**中文译文**

比特承诺（bit commitment）与抛硬币（coin flipping）在设备无关（device-independent）研究图景中占据独特地位，因为迄今为这些任务提出的设备无关协议都依赖三方 GHZ 关联。事实上，我们不知道还有其他这样的双方任务：它们可以采用设备无关表述，却尚不知能否仅利用双方非定域性来实现。这些协议的另一个有趣特征是，GHZ 关联的伪心灵感应（pseudo-telepathic）性质——不同于非定域关联通常所具有的统计性质，例如违反 CHSH 不等式时产生的关联——对协议的构造与分析至关重要。在本文中，我们提出一种基于 CHSH 测试的设备无关比特承诺协议，它达到了最优 GHZ 协议同等的安全性。我们在最一般的情形下分析该协议，其中设备会被反复使用，并且可能具有长期量子存储器。我们还在后量子（post-quantum）情形下重新表述该协议；在这一情形中，无论诚实方还是不诚实方都仅受不可信号传递原则约束，并发现总体而言，超量子结构能够提供更高的安全性。

## I Introduction / I 引言

**English original**

The security of cryptographic protocols, whether quantum or classical, depends on the satisfaction of certain assumptions. These include the integrity of each party’s lab and their having a trusted source of randomness to make the random choices called for by the protocol. Beyond these, classical protocols will also usually include assumptions regarding the computational power of dishonest parties. The security of quantum protocols, in contrast, is based only on the validity of quantum theory. Nevertheless, to harness this validity, assumptions regarding the implementation must be made. Most protocols make many such assumptions, including regarding the internal workings of the devices used in the implementation, e.g. specifying the Hilbert space dimension of the quantum systems used and the bases of the measurements performed. Protocols of this type are said to be device-dependent. Clearly, it is desirable to base security on a minimum number of assumptions, as this facilitates its evaluation. The aim of the device-independent approach to quantum cryptography [1, 2] is to do just that by doing away with a maximum number of assumptions regarding the implementation.

**中文译文**

无论量子还是经典密码协议，其安全性都依赖若干假设得到满足。这些假设包括各方实验室的完整性，以及各方拥有可信随机源，以作出协议所要求的随机选择。除此之外，经典协议通常还会包含关于不诚实方计算能力的假设。相比之下，量子协议的安全性仅以量子理论的有效性为基础。然而，要利用这种有效性，就必须对具体实现作出假设。大多数协议都会作出许多此类假设，其中包括对实现所用设备内部工作机制的假设，例如规定所用量子系统的希尔伯特空间维数和所执行测量的基。此类协议被称为设备依赖（device-dependent）协议。显然，安全性所依据的假设越少越好，因为这样更便于评估安全性。量子密码学设备无关方法 [1, 2] 的目标正是尽可能摒除有关实现的假设。

**English original**

More specifically, a cryptographic protocol is said to be device-independent if its security can be guaranteed without making assumptions about the internal workings of the devices used in its implementation. This can be achieved by carrying out Bell tests on entangled systems. The level of security is then deduced from the observed amount of nonlocality. In particular, each device is treated as a black box with knobs and registers for selecting and displaying (classical) inputs and outputs. For instance, in device-independent quantum key-distribution a high violation of the CHSH inequality [3] guarantees that an eavesdropper will have no information about the (post-processed) key [2, 4, 5, 6, 7, 8, 9, 10]. In contrast, in the (device-dependent) entanglement-based version of the BB84 protocol it has been shown that if the source dispenses qudits instead of qubits then security can be utterly compromised [11, 12]. Indeed, recent hacking attacks on quantum key-distribution systems, such as those of [13, 14], exploit device-dependent modes of failure and would not be successful in device-independent settings.

**中文译文**

更具体地说，如果无须对实现协议所用设备的内部工作机制作出假设就能保证协议安全，那么该密码协议就称为设备无关协议。这可以通过对纠缠系统执行贝尔测试（Bell test）来实现，随后根据观测到的非定域性大小推断安全程度。具体而言，每台设备都被视为一个黑箱，带有用于选择和显示（经典）输入与输出的旋钮和寄存器。例如，在设备无关量子密钥分发中，对 CHSH 不等式 [3] 的高度违反可保证窃听者无法获得关于（后处理）密钥的任何信息 [2, 4, 5, 6, 7, 8, 9, 10]。相比之下，已有研究表明，在（设备依赖的）基于纠缠的 BB84 协议版本中，如果信号源发放的是量子多能级系统而非量子比特，安全性就可能彻底遭到破坏 [11, 12]。事实上，近期针对量子密钥分发系统的黑客攻击，例如 [13, 14] 中的攻击，利用的正是设备依赖型失效模式；在设备无关情形下，这些攻击不会成功。

**English original**

In addition to quantum key-distribution, device-independent protocols have been introduced for diverse tasks such as randomness generation [15, 16, 17, 18, 19, 20, 21], the self-testing of quantum computers [1, 11, 22, 8], state estimation [23, 24, 25, 26, 27], genuine multipartite entanglement certification [28], and entanglement quantification [29]. However, until recently it was not known whether the scope of the device-independent approach also covers protocols in the distrustful cryptography class, where the parties do not trust each other and may have conflicting goals. Problems in this class present us with an extra challenge in device-independent settings as compared to tasks such as quantum-key distribution. Namely, how to allow remote distrustful parties to certify the presence of nonlocality without collaborating. In [30] it was shown that imperfect bit commitment<sup>1</sup> admits a device-independent formulation, and, since bit commitment may serve as a primitive for coin flipping, so does coin flipping (a device-independent coin flipping protocol, not based on bit commitment, was also introduced in [35]). Whether these results extend to all problems in the distrustful cryptography class remains an open question.

**中文译文**

除量子密钥分发之外，人们还针对多种任务提出了设备无关协议，例如随机数生成 [15, 16, 17, 18, 19, 20, 21]、量子计算机自测试 [1, 11, 22, 8]、量子态估计 [23, 24, 25, 26, 27]、真正多方纠缠认证 [28] 和纠缠量化 [29]。然而，直到最近，人们仍不知道设备无关方法的适用范围是否也涵盖互不信任密码学（distrustful cryptography）这一类协议；在这类协议中，各方互不信任，并且目标可能相互冲突。与量子密钥分发等任务相比，这一类问题在设备无关情形下带来了额外挑战，即如何让彼此不信任的远程参与方在不合作的情况下认证非定域性的存在。[30] 表明，不完美比特承诺<sup>1</sup>可以采用设备无关表述；又因为比特承诺可以作为抛硬币的密码学原语，所以抛硬币同样可以采用设备无关表述（[35] 还提出了一种不基于比特承诺的设备无关抛硬币协议）。这些结果能否推广到互不信任密码学类的所有问题，仍是一个开放问题。

**English original**

A notable feature of the protocols of [30, 35] is that they are based on GHZ correlations [36, 37]. Indeed, bit commitment and coin flipping are the only examples we have of bipartite tasks, which admit a device-independent formulation, but which are not known to admit one based on CHSH testing (i.e. sequential tests of the CHSH inequality), or, more generally, on some other bipartite Bell inequality testing. This is especially interesting in light of Reichardt et al.’s recent demonstration [8] that CHSH testing can provide the basis for many device-independent applications in the most general settings where the devices have long-term quantum memory.

**中文译文**

[30, 35] 中协议的一个显著特征是，它们以 GHZ 关联 [36, 37] 为基础。事实上，在我们已知的双方任务实例中，只有比特承诺和抛硬币可以采用设备无关表述，却尚不知能否采用基于 CHSH 测试（即对 CHSH 不等式的序贯测试）的设备无关表述，或者更一般地，采用基于其他双方贝尔不等式测试的设备无关表述。Reichardt 等人最近证明 [8]，在设备具有长期量子存储器这一最一般情形下，CHSH 测试可以作为许多设备无关应用的基础；鉴于这一结果，上述现象尤其值得关注。

**English original**

In [30, 35], the pseudo-telepathic nature of GHZ correlations is exploited to circumvent the unique difficulties associated with distrustful cryptography, specifically, the fact that different parties have conflicting goals and do not trust each other. Quantum pseudo-telepathy is the term coined for the phenomenon of always winning in nonlocal games, which classically (i.e. without sharing entanglement) can only be won part of the time. A famous example is the GHZ game [38]. In particular, pseudo-telepathy entails perfect correlations. In [30] pseudo-telepathy is used to allow Bob to verify the presence of nonlocal correlations (GHZ correlations) and at the same time to verify Alice’s commitment (that the token of her commitment is consistent with the value of the bit she reveals). Crucially, Bob uses the same measurements to verify both the presence of nonlocality and the commitment.

**中文译文**

在 [30, 35] 中，研究者利用 GHZ 关联的伪心灵感应性质，规避互不信任密码学特有的困难，尤其是不同参与方目标相互冲突且彼此不信任这一事实。“量子伪心灵感应”（quantum pseudo-telepathy）一词指的是这样一种现象：在非定域博弈中总能获胜，而在经典情形下（即不共享纠缠时）只能在部分情况下获胜。GHZ 博弈 [38] 是一个著名例子。特别地，伪心灵感应意味着完美关联。在 [30] 中，伪心灵感应使 Bob 能够验证非定域关联（GHZ 关联）的存在，同时验证 Alice 的承诺（即她的承诺凭据与她所揭示的比特值一致）。关键在于，Bob 使用同一组测量来同时验证非定域性的存在和承诺。

**English original**

Unfortunately, pseudo-telepathy is absent in the CHSH setting [39], and so it is a priori unclear whether bipartite distrustful cryptographic tasks can be based on CHSH testing – which is the case for all other examples of bipartite tasks that are known to admit a device-independent formulation. Beyond a theoretical interest, this question is also practically motivated, since manipulating tripartite entanglement, as would be required in a GHZ-based protocol, is obviously more difficult than manipulating EPR pairs, as would be required in a CHSH-based protocol.

**中文译文**

遗憾的是，CHSH 情形中不存在伪心灵感应 [39]，因此先验上并不清楚双方互不信任密码学任务能否以 CHSH 测试为基础——而对于所有其他已知可采用设备无关表述的双方任务实例，情况正是如此。除了理论意义外，这一问题也有实际动机，因为基于 GHZ 的协议需要操控三方纠缠，这显然比基于 CHSH 的协议所需的 EPR 对更难操控。

**English original**

In this work we present a device-independent bit commitment protocol, based on CHSH testing, which achieves the same security as that of [30]: (In the limit of an infinite number of tests) Alice’s control equals $\cos^{2}(\frac{\pi}{8})\simeq 0.8536$ , while Bob’s information gain equals $0.75$ . This shows that pseudo-telepathy is not only inessential for device-independent distrustful cryptography, but that its absence does not necessarily impact security. Specifically, we show how to guarantee that the devices have no way of telling whether they are used as part of the nonlocality testing phase or the verification of the commitment; this being the crucial element on which security hinges.

**中文译文**

在本文中，我们提出一种基于 CHSH 测试的设备无关比特承诺协议，它达到了与 [30] 相同的安全性：（在测试次数趋于无穷的极限下）Alice 的控制概率等于 $\cos^{2}(\frac{\pi}{8})\simeq 0.8536$，而 Bob 的信息获取概率等于 $0.75$。这表明，对于设备无关的互不信任密码学而言，伪心灵感应不仅不是必不可少的，而且缺少它也未必影响安全性。具体而言，我们说明了如何保证设备无法判断自身是用于非定域性测试阶段，还是用于承诺验证；这正是安全性所依赖的关键要素。

**English original**

Our security analysis covers the case of imperfect devices (i.e. the CHSH inequality is not maximally violated) and is carried out in the most general settings where memory effects (the dependence of a measurement outcome not only on the setting, but also on previous settings and outcomes) are taken into account.

**中文译文**

我们的安全性分析涵盖设备不完美的情形（即 CHSH 不等式未达到最大违反），并且是在把记忆效应纳入考虑的最一般情形下进行的；所谓记忆效应，是指测量结果不仅依赖当前设置，还依赖先前的设置与结果。

**English original**

It should be noted that in our protocol the reveal time is fixed and cannot be chosen at will by Alice. Strictly speaking, the protocol is thus not a bit commitment protocol. Nevertheless, depending on the application, it may still be used as a primitive. For example, our protocol can be used to implement coin flipping. The restriction on the reveal time can be lifted at the price of increasing Alice’s cheating probability (see Appendix B), or by working in the large office scenario where instead of a pair of boxes there are many pairs (see Appendix C).

**中文译文**

应当指出，在我们的协议中，揭示时间是固定的，Alice 不能任意选择。因此，严格来说，该协议并不是比特承诺协议。不过，视具体应用而定，它仍可用作一种密码学原语。例如，我们的协议可用于实现抛硬币。可以通过提高 Alice 的作弊概率（见附录 B）来解除对揭示时间的限制，或者在“大办公室情形”（large office scenario）下工作，即使用多对黑箱而不是一对黑箱（见附录 C）。

**English original**

We also study the problem in a post-quantum world where both dishonest and honest parties are restricted only by the impossibility of signaling. This helps us identify the contribution of different resources to security. On the one hand, we might expect such a world to offer less security since a dishonest party would have access to stronger correlations. On the other hand, we might expect the converse, since the protocol itself could be modified to make use of these stronger correlations (in particular, pseudo-telepathy is restored in this setting). It turns out that on the balance this allows for more security.

**中文译文**

我们还在一个后量子世界中研究这一问题，其中不诚实方和诚实方都只受不可信号传递原则的约束。这有助于我们辨明不同资源对安全性的贡献。一方面，我们可能预期这样的世界安全性更低，因为不诚实方可以利用更强的关联。另一方面，我们也可能预期恰好相反，因为可以修改协议本身以利用这些更强的关联（尤其是伪心灵感应在此情形下得以恢复）。结果表明，总体权衡之下，这使安全性得以提高。

**English original**

The paper is structured as follows. We begin in Section II by defining the problem of bit commitment, and making explicit exactly what we mean by device-independence. Next, in Section III, we present the protocol, followed by the proofs of Alice’s and Bob’s securities in Sections IV and V, respectively. We conclude with a summary in Section VI. In Appendix A we present the post-quantum version of our protocol. Appendices B and C present modifications of the protocol where Alice can freely choose the reveal time.

**中文译文**

本文结构如下。首先，我们在第二节定义比特承诺问题，并明确说明“设备无关”的确切含义。接下来，我们在第三节介绍协议，随后分别在第四节和第五节证明 Alice 与 Bob 的安全性。第六节给出总结。附录 A 介绍协议的后量子版本。附录 B 和附录 C 给出协议的修改版本，在这些版本中 Alice 可以自由选择揭示时间。

## II Background / II 背景

### II.1 Bit commitment / II.1 比特承诺

**English original**

Bit commitment is a cryptographic primitive comprising two remote, distrustful parties. Party $\mathcal{A}$ , usually referred to as Alice, commits a bit to party $\mathcal{B}$ , usually referred to as Bob, such that following her commitment Alice cannot change its value and Bob is unable to learn it until she chooses to reveal it. Classically, if the dishonest party’s computational power is unlimited, they can cheat perfectly. Quantumly, the dishonest party cannot cheat perfectly [33], though perfect bit commitment is still impossible [31, 32].

**中文译文**

比特承诺是一种涉及两个彼此远离且互不信任参与方的密码学原语。参与方 $\mathcal{A}$（通常称为 Alice）向参与方 $\mathcal{B}$（通常称为 Bob）承诺一个比特，使得 Alice 在作出承诺后不能更改其值，而 Bob 在 Alice 选择揭示之前无法得知该值。在经典情形下，如果不诚实方的计算能力不受限制，就能完美作弊。在量子情形下，不诚实方无法完美作弊 [33]，不过完美比特承诺仍然是不可能的 [31, 32]。

**English original**

A bit commitment protocol consists of two phases: the commit phase in which Alice sends Bob some token of her commitment, and the reveal phase in which Alice reveals to Bob the value of the committed bit. The probability with which dishonest Alice is able to control the value of the bit she wants to reveal following the commit phase, without being caught cheating by Bob, is referred to as Alice’s control, which we will denote by $P_{\mathrm{cont}}=\frac{1}{2}(p_{0}+p_{1})$ . Here $p_{0}$ ( $p_{1}$ ) is Alice’s probability of successfully revealing $0$ ( $1$ ) and the factor of $\frac{1}{2}$ is due to the implicit assumption that she is equally likely to wish to reveal $0$ as $1$ . Similarly, dishonest Bob’s probability of correctly learning the value of the bit before the reveal phase is referred to as Bob’s information gain, which we will denote by $P_{\mathrm{gain}}$ . In a perfect bit commitment protocol $P_{\mathrm{cont}}=P_{\mathrm{gain}}=\frac{1}{2}$ . A protocol is said to be balanced if $P_{\mathrm{cont}}=P_{\mathrm{gain}}$ . Quantumly, in any balanced protocol $P_{\mathrm{cont}}=P_{\mathrm{gain}}\gtrsim 0.739$ , with the bound being saturable [34].

**中文译文**

比特承诺协议由两个阶段组成：承诺阶段（commit phase），Alice 在该阶段向 Bob 发送某种承诺凭据；以及揭示阶段（reveal phase），Alice 在该阶段向 Bob 揭示所承诺比特的值。承诺阶段结束后，不诚实的 Alice 在不被 Bob 发现作弊的情况下控制自己想要揭示的比特值的概率，称为 Alice 的控制概率，记作 $P_{\mathrm{cont}}=\frac{1}{2}(p_{0}+p_{1})$。这里，$p_{0}$（$p_{1}$）是 Alice 成功揭示 $0$（$1$）的概率；因隐含假设她想要揭示 $0$ 和 $1$ 的可能性相同，故有因子 $\frac{1}{2}$。类似地，不诚实的 Bob 在揭示阶段之前正确获知比特值的概率，称为 Bob 的信息获取概率，记作 $P_{\mathrm{gain}}$。在完美比特承诺协议中，$P_{\mathrm{cont}}=P_{\mathrm{gain}}=\frac{1}{2}$。如果 $P_{\mathrm{cont}}=P_{\mathrm{gain}}$，则称协议是平衡的。在量子情形下，任何平衡协议均有 $P_{\mathrm{cont}}=P_{\mathrm{gain}}\gtrsim 0.739$，且该界可以达到 [34]。

### II.2 Device-independence / II.2 设备无关性

**English original**

In this subsection we make more concrete exactly what we mean by device-independence. We make the following standard assumptions.

**中文译文**

在本小节中，我们将更具体地说明“设备无关性”（device-independence）的确切含义。我们作出以下标准假设。

1. **English original**

   Alice and Bob have access to boxes, each with a knob for selecting a classical input $s$ and a register for displaying a classical output $r$ . Entering an input always results in an output (i.e. we do not consider losses).

   **中文译文**

   Alice 和 Bob 可以使用若干黑箱，每个黑箱都有一个用于选择经典输入 $s$ 的旋钮和一个用于显示经典输出 $r$ 的寄存器。输入总会产生输出（即我们不考虑损耗）。

2. **English original**

   Alice and Bob, whether honest or dishonest, are restricted by quantum theory.

   **中文译文**

   无论诚实与否，Alice 和 Bob 都受量子理论约束。

3. **English original**

   The boxes may be prevented at will from communicating with one another.

   **中文译文**

   可以根据需要阻止各黑箱彼此通信。

4. **English original**

   Alice and Bob each have a trusted source of randomness.

   **中文译文**

   Alice 和 Bob 各自拥有可信随机源。

5. **English original**

   No information leaks out of an honest party’s lab.

   **中文译文**

   诚实方的实验室不会泄露任何信息。

**English original**

Suppose now that an honest party has a pair of boxes $0$ and $1$ . Assumptions 2 and 3 imply that the probability of outputting $r^{0}$ and $r^{1}$ when inputting $s^{0}$ and $s^{1}$ into boxes $0$ and $1$ , respectively, is given by

$$
P\left(r^{0},\,r^{1}|s^{0},\,s^{1}\right)=\mathrm{Tr}\left(\rho\,\Pi_{r^{0}|s^{0}}\otimes\Pi_{r^{1}|s^{1}}\right)\,,
\tag{1}
$$

**中文译文**

现在假设某个诚实方拥有编号为 $0$ 和 $1$ 的一对黑箱。由假设 2 和 3 可知，分别向黑箱 $0$ 和 $1$ 输入 $s^{0}$ 和 $s^{1}$ 时，输出 $r^{0}$ 和 $r^{1}$ 的概率由上式给出。

**English original**

where $\rho$ is some joint quantum state and $\Pi_{r^{i}|s^{i}}$ is the POVM element corresponding to inputting $s^{i}$ and outputting $r^{i}$ . This is the only constraint on the boxes’ behavior. Specifically, a dishonest party may choose the state $\rho$ and the POVM elements $\Pi_{r^{i}|s^{i}}$ as best suits them. The boxes may also have internal memories, clocks, gyroscopes, etc., allowing a dishonest party to program them such that their behavior depends on their location, their past trajectories, the time at which inputs are fed, or any other aspect of their past history.

**中文译文**

其中，$\rho$ 是某个联合量子态，$\Pi_{r^{i}|s^{i}}$ 是与输入 $s^{i}$ 并输出 $r^{i}$ 相对应的正算符值测度（POVM）元素。这是对黑箱行为的唯一约束。具体而言，不诚实方可以按最有利于自己的方式选择状态 $\rho$ 和 POVM 元素 $\Pi_{r^{i}|s^{i}}$。黑箱还可以具有内部存储器、时钟、陀螺仪等，从而使不诚实方能够对其进行编程，使其行为依赖于所在位置、以往轨迹、输入被送入的时间，或其过往历史的任何其他方面。

**English original**

In the following, we will consider situations where boxes are sent from one party to the other. By this, it is not meant that actual measurement devices are sent (though it is easier to present and formulate our results in this way). In fact, we do not assume anything beyond Alice and Bob having access to a quantum channel—as is necessarily required in quantum cryptography. What is meant is that whenever a box is sent, quantum information encoding instructions for the measurement devices (as well as the quantum state of the boxes) is exchanged between the parties, such that in an honest execution of the protocol the same state $\rho$ and the POVM elements $\Pi_{r^{i}|s^{i}}$ characterizing the behavior, say, of Alice’s box before the transmission of quantum information, will characterize the behavior of Bob’s box after receiving the transmission.

**中文译文**

下文将考虑把盒子从一方发送给另一方的情形。这并非指实际发送测量设备（尽管以这种方式陈述和表述结果更为方便）。事实上，我们除了假设 Alice 和 Bob 拥有量子信道——这是量子密码学所必需的——之外，不作其他假设。所谓发送盒子，是指每当发送一个盒子时，双方交换编码了测量设备指令的量子信息（以及盒子的量子态），使得在诚实执行协议时，例如，在传输量子信息之前刻画 Alice 盒子行为的同一个状态 $\rho$ 和 POVM 元素 $\Pi_{r^{i}|s^{i}}$，也将刻画 Bob 接收传输之后其盒子的行为。

**English original**

Finally, we wish to comment on the differences in the assumptions underlying our protocol as compared to relativistic bit commitment protocols [40, 41]. Indeed, relativistic causality is by itself sufficient for perfect bit commitment (whether purely classical [40] or quantum [41]), but this comes at the cost of extra resources. In relativistic bit commitment at least one of the parties must be assigned two remote secure labs, which allow for implementing spacelike related measurements. In contrast, in our protocol each party is assigned a single secure lab. Moreover, we do not impose any relativistic constraints. In particular, we do not require any measurements be spacelike related. In fact, many of the measurements in our protocol are not spacelike related. This does not come at the expense of preventing the boxes from communicating (i.e. assumption 3), since spacelike related measurements are not the only way to achieve this. An alternative way, and an experimentally easier one, is simply shield each of the boxes (see [5, 16] for a discussion of this point).

**中文译文**

最后，我们想说明本协议所依据的假设与相对论比特承诺协议 [40, 41] 的差异。的确，相对论因果性本身足以实现完美比特承诺（无论纯经典 [40] 还是量子 [41]），但这需要额外资源。在相对论比特承诺中，至少一方必须被分配两个彼此远离的安全实验室，以便实现类空相关的测量。相比之下，在我们的协议中，每一方只被分配一个安全实验室。此外，我们不施加任何相对论约束。特别是，我们不要求任何测量具有类空关系。事实上，本协议中的许多测量并不具有类空关系。这并不妨碍阻止盒子相互通信（即假设 3），因为类空相关测量并非实现这一点的唯一途径。另一种在实验上更容易的办法是简单地屏蔽每个盒子（关于这一点的讨论见 [5, 16]）。

---

#### Footnote 1 / 脚注 1

**English original**

While quantum mechanics does not allow for perfect bit commitment [31, 32], imperfect bit commitment is nevertheless possible [33, 34].

**中文译文**

尽管量子力学不允许完美比特承诺 [31, 32]，但不完美比特承诺仍然是可能的 [33, 34]。
