#!/usr/bin/env python3
"""Prepare and assemble the paragraph-paired English/Chinese paper.

- Restore NJP numbered citations ([1]–[48]) from leftover BibTeX keys.
- Align two background paragraphs with the published NJP wording.
- Convert equation markdown-tables into $$/aligned display math.
- Concatenate section files for pandoc.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEC = ROOT / "paper-bilingual" / "sections"
FIG = ROOT / "paper-bilingual" / "figures"
OUTPUT_DIR = ROOT / "paper-bilingual" / "build"

SECTIONS = [
    "01-front-intro-background.md",
    "02-protocol-alice-security.md",
    "03-bob-security-summary.md",
    "04-appendices-references.md",
]

# NJP 18, 025014 (2016) bibliography order (48 items; arXiv extras Nielsen/Werner omitted).
CITE = {
    "Mayers04": 1,
    "Barrett05": 2,
    "Clauser69": 3,
    "Acin07": 4,
    "Pironio09": 5,
    "McKague09": 6,
    "Masanes11": 7,
    "Reichardt13A": 8,
    "Pironio13B": 9,
    "Vazirani12B": 10,
    "Magniez06": 11,
    "Acin06": 12,
    "Xu10": 13,
    "Lydersen10": 14,
    "Colbeck07": 15,
    "Pironio10A": 16,
    "Pironio13A": 17,
    "Fehr13": 18,
    "Vazirani12A": 19,
    "MillerShi": 20,
    "Coudron": 21,
    "McKague11": 22,
    "Bardyn09": 23,
    "McKague12": 24,
    "Yang12": 25,
    "Yang13": 26,
    "Bamps": 27,
    "Bancal11": 28,
    "Moroder13": 29,
    "Silman11": 30,
    "Lo97": 31,
    "Mayers97": 32,
    "Spekkens01": 33,
    "Chailloux11": 34,
    "Aharon14": 35,
    "Greenberger89": 36,
    "Mermin90": 37,
    "Vaidman99": 38,
    "Gisin07": 39,
    "Kent99": 40,
    "Kent15": 41,
    "Navascues07": 42,
    "Pironio10B": 43,
    "YALMIP": 44,
    "SeDuMi": 45,
    "Popescu94": 46,
    "Buhrman06": 47,
    "Azuma67": 48,
}

KEYS = sorted(CITE, key=len, reverse=True)
KEY_ALT = "|".join(re.escape(k) for k in KEYS)
SEP = r"(?:\s*[;；,，]\s*|\s+and\s+|\s+和\s+)"
CITE_SEQ = re.compile(rf"(?<![A-Za-z])({KEY_ALT})(?:{SEP}({KEY_ALT}))*(?![A-Za-z0-9])")

DISPLAY_TAG = re.compile(r"\$\$[\s\S]*?\\tag\{(\d+)\}\s*\$\$")

# Display equations (6)–(19) taken from the arXiv TeX, with \mid in place of
# raw | so Markdown never treats conditioning bars as table columns.
CANONICAL = {
    6: r"""$$
\begin{aligned}
&\frac{1}{4}\sum_{k,\,l=0,\,1}\Bigl[P(r^{1}=k,\,(k,\,l)\mid s^{1}=0,\,\mathcal{M}^{0})+P(r^{0}=k,\,(k,\,l)\mid s^{0}=0,\,\mathcal{M}^{1})\Bigr. \\
&\Bigl.+P(r^{1}=l,\,(k,\,l)\mid s^{1}=1,\,\mathcal{M}^{0})+P(r^{0}=l,(\,k,\,l)\mid s^{0}=1,\,\mathcal{M}^{1})\Bigr]\,.
\end{aligned}
\tag{6}
$$""",
    7: r"""$$
\begin{aligned}
P_{\mathrm{cont}}
&= \frac{1}{4}\max_{\mathcal{Q}}\mathrm{Tr}\biggl(\rho\sum_{c,\,k,\,l=0,\,1}M_{kl}^{c}\bigl(\Pi_{k\mid 0}^{\bar{c}}+\Pi_{l\mid 1}^{\bar{c}}\bigr)\biggr) \\
&\mathrm{s.t.}\quad
\mathrm{Tr}\biggl(\rho\sum_{a,\,b,\,x,\,y=0,\,1}(-1)^{a\oplus b\oplus xy}\Pi_{a\mid x}^{0}\Pi_{b\mid y}^{1}\biggr)\geq I_{\mathrm{th}}, \\
&\qquad\bigl[\Pi_{i\mid j}^{c},\,\Pi_{k\mid l}^{\bar{c}}\bigr]=\bigl[M_{ij}^{c},\,\Pi_{k\mid l}^{\bar{c}}\bigr]=\bigl[M_{ij}^{c},\,M_{kl}^{\bar{c}}\bigr]=0, \\
&\qquad\Pi_{i\mid j}^{c}\succeq 0,\quad M_{ij}^{c}\succeq 0,\quad\sum_{i=0,\,1}\Pi_{i\mid j}^{c}=\mathbb{1},\quad\sum_{i,\,j=0,\,1}M_{ij}^{c}=\mathbb{1}.
\end{aligned}
\tag{7}
$$""",
    8: r"""$$
P_{\mathrm{cont}}=\cos^{2}\Bigl(\frac{\theta}{2}\Bigr)\,.
\tag{8}
$$""",
    9: r"""$$
I=\langle\phi^{+}|\sigma_{2\theta}\otimes\sigma_{2\theta-\varphi}+\sigma_{2\theta}\otimes\sigma_{4\theta-\varphi}+\sigma_{z}\otimes\sigma_{2\theta-\varphi}-\sigma_{z}\otimes\sigma_{4\theta-\varphi}|\phi^{+}\rangle
=2\cos(2\theta-\varphi)-\cos(4\theta-\varphi)+\cos(\varphi)\,.
\tag{9}
$$""",
    10: r"""$$
\varphi_{\mathrm{opt}}=\arccos\biggl(2\frac{\cos(2\theta)+\sin^{2}(2\theta)}{\sqrt{6-2\cos(4\theta)}}\biggr)\,.
\tag{10}
$$""",
    11: r"""$$
\begin{aligned}
P_{\mathrm{cont}}
&= \frac{1}{N}\sum_{n=1}^{N-1}\sum_{\{\mathrm{\mathbf{w}}_{n}\}}P(\mathrm{\mathbf{w}}_{n})\Theta(\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})-I_{\mathrm{th}})C\bigl(E(I(W_{n+1})\mid\mathrm{\mathbf{w}}_{n})\bigr) \\
&\qquad +\frac{1}{N}\sum_{\{\mathrm{\mathbf{w}}_{N}\}}P(\mathrm{\mathbf{w}}_{N})\Theta(\bar{I}_{N}(\mathrm{\mathbf{w}}_{N})-I_{\mathrm{th}}) \\
&\leq \frac{1}{N}\sum_{n=1}^{N-1}\sum_{\{\mathrm{\mathbf{w}}_{n}\}}P(\mathrm{\mathbf{w}}_{n})\Theta(\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})-I_{\mathrm{th}})C\bigl(E(I(W_{n+1})\mid\mathrm{\mathbf{w}}_{n})\bigr)+\frac{1}{N}\,.
\end{aligned}
\tag{11}
$$""",
    12: r"""$$
P_{\mathrm{cont}}\leq\sum_{\{\mathrm{\mathbf{w}}_{N-1}\}}P(\mathrm{\mathbf{w}}_{N-1})\frac{1}{N}\sum_{n=1}^{N-1}\Theta(\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})-I_{\mathrm{th}})C\bigl(E(I(W_{n+1})\mid\mathrm{\mathbf{w}}_{n})\bigr)+\frac{1}{N}\,.
\tag{12}
$$""",
    13: r"""$$
K(\mathrm{\mathbf{w}}_{N-1})=\max_{k\leq N-1}\{k\mid \bar{I}_{k}(\mathrm{\mathbf{w}}_{k})\geq I_{\mathrm{th}}\}\,.
\tag{13}
$$""",
    14: r"""$$
\begin{aligned}
P_{\mathrm{cont}}
&\leq \sum_{\{\mathrm{\mathbf{w}}_{N-1}\}}P(\mathrm{\mathbf{w}}_{N-1})\frac{1}{N}\sum_{n=1}^{N-1}\Theta(\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})-I_{\mathrm{th}})C\bigl(E(I(W_{n+1})\mid\mathrm{\mathbf{w}}_{n})\bigr)+\frac{1}{N} \\
&= \sum_{k=1}^{N-1}\sum_{\{\mathrm{\mathbf{w}}_{N-1}\mid K(\mathrm{\mathbf{w}}_{N-1})=k\}}P(\mathrm{\mathbf{w}}_{N-1})\frac{1}{N}\sum_{n=1}^{N-1}\Theta(\bar{I}_{n}(\mathrm{\mathbf{w}}_{n})-I_{\mathrm{th}})C\bigl(E(I(W_{n+1})\mid\mathrm{\mathbf{w}}_{n})\bigr)+\frac{1}{N} \\
&\leq \sum_{k=1}^{N-1}\sum_{\{\mathrm{\mathbf{w}}_{N-1}\mid K(\mathrm{\mathbf{w}}_{N-1})=k\}}P(\mathrm{\mathbf{w}}_{N-1})\frac{1}{N}\sum_{n=1}^{k}C\bigl(E(I(W_{n+1})\mid\mathrm{\mathbf{w}}_{n})\bigr)+\frac{1}{N}\,.
\end{aligned}
\tag{14}
$$""",
    15: r"""$$
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
$$""",
    16: r"""$$
\bar{I}_{k}\left(\mathbf{w}_{k}\right)-\frac{1}{k}\sum_{n=1}^{k}E\left(I\left(W_{n}\right)\mid\mathbf{w}_{n-1}\right)\geq\varepsilon\,.
\tag{16}
$$""",
    17: r"""$$
P\left(\pi_{k}\left(\varepsilon\right)\right)\leq\exp\biggl(-\frac{k\varepsilon^{2}}{2D^{2}}\biggr)\,,
\tag{17}
$$""",
    18: r"""$$
\sum_{k=K_{0}}^{N-1}P\left(\pi_{k}\left(\varepsilon\right)\right)\leq\frac{\exp\bigl(-\frac{K_{0}\varepsilon^{2}}{2D^{2}}\bigr)-\exp\bigl(-\frac{N\varepsilon^{2}}{2D^{2}}\bigr)}{1-\exp\left(-\frac{\varepsilon^{2}}{2D^{2}}\right)}=Q(\varepsilon)\,.
\tag{18}
$$""",
    19: r"""$$
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
$$""",
}


def restore_citations(text: str) -> str:
    """Replace leftover BibTeX keys with NJP numbers; skip the reference list."""
    split = re.split(r"(?m)^(## References\b.*)$", text, maxsplit=1)
    body = split[0]
    tail = "".join(split[1:]) if len(split) > 1 else ""

    body = body.replace("YALMIP YALMIP", "YALMIP [44]")
    body = body.replace("SeDuMi SeDuMi", "SeDuMi [45]")

    def repl(match: re.Match[str]) -> str:
        found = re.findall(KEY_ALT, match.group(0))
        nums = ", ".join(str(CITE[k]) for k in found)
        return f"[{nums}]"

    body = CITE_SEQ.sub(repl, body)
    return body + tail


def njp_wording(text: str) -> str:
    """Prefer published NJP wording where it differs from the arXiv extract."""
    old_boxes_en = (
        "In the following, we will consider situations where boxes are sent from one party "
        "to the other. By this, we do not mean that actual measurement devices are sent "
        "(though it is easier to present and formulate our results in this way). Instead, "
        "what we mean is that quantum states, or classical information, encoding instructions "
        "for the measurement devices, are exchanged between the parties, such that in an honest "
        "execution of the protocol the same state $\\rho$ and the POVM elements $\\Pi_{r^{i}|s^{i}}$ "
        "characterizing the behavior, say, of Alice’s box before the transmission of quantum "
        "information, will characterize the behavior of Bob’s box after receiving the transmission."
    )
    new_boxes_en = (
        "In the following, we will consider situations where boxes are sent from one party "
        "to the other. By this, it is not meant that actual measurement devices are sent "
        "(though it is easier to present and formulate our results in this way). In fact, we "
        "do not assume anything beyond Alice and Bob having access to a quantum channel—as is "
        "necessarily required in quantum cryptography. What is meant is that whenever a box is "
        "sent, quantum information encoding instructions for the measurement devices (as well as "
        "the quantum state of the boxes) is exchanged between the parties, such that in an honest "
        "execution of the protocol the same state $\\rho$ and the POVM elements $\\Pi_{r^{i}|s^{i}}$ "
        "characterizing the behavior, say, of Alice’s box before the transmission of quantum "
        "information, will characterize the behavior of Bob’s box after receiving the transmission."
    )
    old_boxes_zh = (
        "下文将考虑把黑箱从一方发送给另一方的情形。我们并不是说实际发送测量设备（尽管以这种方式陈述和表述结果更为方便）。"
        "我们的意思是，双方交换量子态，或交换编码了测量设备指令的经典信息，使得在诚实执行协议时，例如，在传输量子信息之前刻画 Alice 黑箱行为的同一个状态 $\\rho$ 和 POVM 元素 $\\Pi_{r^{i}|s^{i}}$，也将刻画 Bob 接收传输之后其黑箱的行为。"
    )
    new_boxes_zh = (
        "下文将考虑把盒子从一方发送给另一方的情形。这并非指实际发送测量设备（尽管以这种方式陈述和表述结果更为方便）。"
        "事实上，我们除了假设 Alice 和 Bob 拥有量子信道——这是量子密码学所必需的——之外，不作其他假设。"
        "所谓发送盒子，是指每当发送一个盒子时，双方交换编码了测量设备指令的量子信息（以及盒子的量子态），"
        "使得在诚实执行协议时，例如，在传输量子信息之前刻画 Alice 盒子行为的同一个状态 $\\rho$ 和 POVM 元素 $\\Pi_{r^{i}|s^{i}}$，"
        "也将刻画 Bob 接收传输之后其盒子的行为。"
    )
    old_rel_en = (
        "Finally, we wish to emphasize that spacelike related measurements are not necessary "
        "in order to prevent the boxes from communicating (i.e. assumption 3). We may equally "
        "well shield each box (see Pironio09; Pironio10A for a discussion of this point). This "
        "observation is important because $(i)$ in our protocol many of the measurements are not "
        "spacelike related; $(ii)$ relativistic causality is by itself sufficient for perfect bit "
        "commitment (whether purely classical Kent99 or quantum Kent15), albeit at the cost of "
        "assigning at least one party two remote secure labs."
    )
    new_rel_en = (
        "Finally, we wish to comment on the differences in the assumptions underlying our "
        "protocol as compared to relativistic bit commitment protocols [40, 41]. Indeed, "
        "relativistic causality is by itself sufficient for perfect bit commitment (whether purely "
        "classical [40] or quantum [41]), but this comes at the cost of extra resources. In "
        "relativistic bit commitment at least one of the parties must be assigned two remote secure "
        "labs, which allow for implementing spacelike related measurements. In contrast, in our "
        "protocol each party is assigned a single secure lab. Moreover, we do not impose any "
        "relativistic constraints. In particular, we do not require any measurements be spacelike "
        "related. In fact, many of the measurements in our protocol are not spacelike related. This "
        "does not come at the expense of preventing the boxes from communicating (i.e. assumption 3), "
        "since spacelike related measurements are not the only way to achieve this. An alternative "
        "way, and an experimentally easier one, is simply shield each of the boxes (see [5, 16] for "
        "a discussion of this point)."
    )
    old_rel_zh = (
        "最后，我们要强调，为阻止黑箱相互通信（即假设 3），并不一定需要让测量彼此具有类空关系。"
        "我们同样可以屏蔽每个黑箱（关于这一点的讨论见 Pironio09; Pironio10A）。"
        "这一观察很重要，因为：$(i)$ 在我们的协议中，许多测量之间并不具有类空关系；"
        "$(ii)$ 相对论因果性本身足以实现完美比特承诺（无论是纯经典方案 Kent99 还是量子方案 Kent15），"
        "尽管代价是要为至少一方配置两个彼此远离的安全实验室。"
    )
    new_rel_zh = (
        "最后，我们想说明本协议所依据的假设与相对论比特承诺协议 [40, 41] 的差异。"
        "的确，相对论因果性本身足以实现完美比特承诺（无论纯经典 [40] 还是量子 [41]），但这需要额外资源。"
        "在相对论比特承诺中，至少一方必须被分配两个彼此远离的安全实验室，以便实现类空相关的测量。"
        "相比之下，在我们的协议中，每一方只被分配一个安全实验室。此外，我们不施加任何相对论约束。"
        "特别是，我们不要求任何测量具有类空关系。事实上，本协议中的许多测量并不具有类空关系。"
        "这并不妨碍阻止盒子相互通信（即假设 3），因为类空相关测量并非实现这一点的唯一途径。"
        "另一种在实验上更容易的办法是简单地屏蔽每个盒子（关于这一点的讨论见 [5, 16]）。"
    )
    replacements = [
        (old_boxes_en, new_boxes_en),
        (old_boxes_zh, new_boxes_zh),
        (old_rel_en, new_rel_en),
        (old_rel_zh, new_rel_zh),
    ]
    for old, new in replacements:
        if old in text:
            text = text.replace(old, new)
    return text


def fix_reference_list(text: str) -> str:
    """Drop unused arXiv-only bibitems so numbers match NJP [44]–[48]."""
    old = """- (44) M.A. Nielsen and C.L. Chuang, Quantum Information and Quantum Computation (Cambridge University Press, 2000).
- (45) R.F. Werner, Phys. Rev. A 40, 4277 (1989).
- (46) J. Löfberg, YALMIP: A Toolbox for Modeling and Optimization in MATLAB. Available at http://users.isy.liu.se/johanl/yalmip.
- (47) J.F. Sturm and I. Pólik, SeDuMi: a package for conic optimization. Available at http://sedumi.ie.lehigh.edu.
- (48) S. Popescu and D. Rohrlich, Found. Phys. 24, 379 (1994).
- (49) H. Buhrman et al., Proc. R. Soc. A 462, 1919 (2006).
- (50) K. Azuma, Tohoku Math. J. 19, 357 (1967)."""
    new = """- [44] J. Löfberg, YALMIP: A Toolbox for Modeling and Optimization in MATLAB. Available at http://users.isy.liu.se/johanl/yalmip.
- [45] J.F. Sturm and I. Pólik, SeDuMi: a package for conic optimization. Available at http://sedumi.ie.lehigh.edu.
- [46] S. Popescu and D. Rohrlich, Found. Phys. 24, 379 (1994).
- [47] H. Buhrman et al., Proc. R. Soc. A 462, 1919 (2006).
- [48] K. Azuma, Tohoku Math. J. 19, 357 (1967)."""
    text = text.replace(old, new)
    text = re.sub(r"^- \((\d+)\) ", r"- [\1] ", text, flags=re.MULTILINE)
    return text


def insert_journal_line(text: str) -> str:
    marker = (
        "单位：<sup>1</sup>以色列特拉维夫大学物理与天文学学院，特拉维夫 69978；"
        "<sup>2</sup>以色列耶路撒冷希伯来大学拉卡物理研究所，耶路撒冷 91904；"
        "<sup>3</sup>比利时布鲁塞尔自由大学（ULB）量子信息实验室，布鲁塞尔 1050"
    )
    extra = """
**English original**

*New J. Phys.* **18**, 025014 (2016); doi:[10.1088/1367-2630/18/2/025014](https://doi.org/10.1088/1367-2630/18/2/025014); [arXiv:1511.06283](https://arxiv.org/abs/1511.06283).

**中文译文**

《新物理学杂志》**18**, 025014 (2016)；doi:[10.1088/1367-2630/18/2/025014](https://doi.org/10.1088/1367-2630/18/2/025014)；[arXiv:1511.06283](https://arxiv.org/abs/1511.06283)。
"""
    if "*New J. Phys.*" not in text and marker in text:
        text = text.replace(marker, marker + "\n" + extra, 1)
    return text


def insert_figures(text: str) -> str:
    pairs = [
        (
            "图 1：渐近极限下 Alice 的控制力随 $I_{\\mathrm{th}}$ 变化的关系。该曲线由式 (8)–(10) 得到。该曲线达到式 (7) 的二阶松弛上界，误差在 $10^{-8}$ 以内——即 SDP 求解器的数值精度。",
            "\n\n![](figures/fig1.png){ width=70% }\n",
            "figures/fig1.png",
        ),
        (
            "图 2：Alice 最优作弊策略中测量轴排列方式的示意图。实线（虚线）轴对应 Bob 在盒子 $0$（$1$）上的测量。点线轴对应 Alice 的测量（Alice 总是在 Bob 的两条轴正中间进行测量）。所有轴都位于 $zx$ 平面内。$\\alpha=2\\theta-\\varphi_{\\mathrm{opt}}$。$\\varphi_{\\mathrm{opt}}$ 与 $\\theta$ 通过式 (10) 相关联。",
            "\n\n![](figures/fig2.png){ width=70% }\n",
            "figures/fig2.png",
        ),
        (
            "图 3：Alice 控制力的上界随 $\\log_{10}N$ 变化的关系。在给定 $I_{\\mathrm{th}}=2\\sqrt{2}(1-\\frac{1}{\\sqrt{N}})$ 时，该曲线给出了针对不同 $N$ 值对式 (19) 进行数值求解的结果。在 $N\\rightarrow\\infty$ 的极限下，Alice 的控制力趋于渐近线 $\\cos^{2}\\bigl(\\frac{\\pi}{8}\\bigr)\\simeq 0.854$（以虚线表示）。",
            "\n\n![](figures/fig3.png){ width=70% }\n",
            "figures/fig3.png",
        ),
    ]
    for caption, image, marker in pairs:
        if marker in text:
            continue
        if caption in text:
            text = text.replace(caption, caption + image, 1)
    return text


def fix_tagged_equations(text: str) -> str:
    """Replace broken table-derived displays (6)–(19) with TeX-faithful math."""

    def repl(match: re.Match[str]) -> str:
        n = int(match.group(1))
        return CANONICAL.get(n, match.group(0))

    return DISPLAY_TAG.sub(repl, text)


def latex_compat(text: str) -> str:
    text = text.replace(r"\begin{align*}", r"\begin{aligned}")
    text = text.replace(r"\end{align*}", r"\end{aligned}")
    text = text.replace(r"\mathds{1}", r"\mathbb{1}")
    return text


def prepare_section(path: Path) -> str:
    original = path.read_text(encoding="utf-8")
    text = original
    text = njp_wording(text)
    text = restore_citations(text)
    text = fix_reference_list(text)
    text = insert_journal_line(text)
    text = insert_figures(text)
    text = fix_tagged_equations(text)
    text = latex_compat(text)
    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"updated {path.relative_to(ROOT)}")
    else:
        print(f"unchanged {path.relative_to(ROOT)}")
    return text


FRONT = """# Device-independent bit commitment based on the CHSH inequality / 基于 CHSH 不等式的设备无关比特承诺

This bilingual edition pairs each English paragraph of Aharon, Massar, Pironio, and Silman, *New J. Phys.* **18**, 025014 (2016) with a Chinese translation. Citation numbers follow the published article, [1]–[48]. Formulas are kept in LaTeX.

本双语版将 Aharon、Massar、Pironio 与 Silman 发表于 *New J. Phys.* **18**, 025014 (2016) 的论文逐段英中对照。引用编号与正式发表文本 [1]–[48] 一致。公式保留 LaTeX。

The English text follows the published NJP article; where the 2015 arXiv source differs (notably the comparison with relativistic bit commitment), the NJP wording is used. Bibliographic fields are left in English.

英文以 NJP 正式发表稿为准；当 2015 年 arXiv 稿与之不同时（尤其是与相对论比特承诺的比较），采用 NJP 表述。参考文献著录项保持英文。

"""


def assemble() -> str:
    chunks = [FRONT]
    for name in SECTIONS:
        path = SEC / name
        if not path.exists():
            raise FileNotFoundError(path)
        chunks.append(prepare_section(path).strip())
        chunks.append("\n\n\\newpage\n")
    return "\n".join(chunks).rstrip() + "\n"


def remaining_keys(text: str) -> list[str]:
    """Flag leftover cite keys. Toolbox names YALMIP/SeDuMi may remain on purpose."""
    body = re.split(r"(?m)^## References", text, maxsplit=1)[0]
    skip = {"YALMIP", "SeDuMi"}
    found = []
    for key in KEYS:
        if key in skip:
            continue
        if re.search(rf"(?<![A-Za-z]){re.escape(key)}(?![A-Za-z0-9])", body):
            found.append(key)
    return found


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: assemble_paper_bilingual.py OUTPUT.md")
    output = Path(sys.argv[1])
    output.parent.mkdir(parents=True, exist_ok=True)
    combined = assemble()
    leftover = remaining_keys(combined)
    if leftover:
        raise SystemExit(f"unreplaced citation keys: {leftover}")
    output.write_text(combined, encoding="utf-8")
    print(f"Wrote bilingual paper source: {output}")


if __name__ == "__main__":
    main()
