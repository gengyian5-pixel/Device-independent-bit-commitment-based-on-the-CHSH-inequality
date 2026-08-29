# 11. Write the paper

Use this chapter only after the reconstruction checklist is done. The goal is to produce a manuscript with the same *claims and structure* as Aharon *et al.*, NJP **18**, 025014 (2016), in your own words.

## 11.1 Title, authors, keywords

- Title can stay descriptive: device-independent, bit commitment, CHSH.
- Keywords used by NJP: quantum cryptography, device-independent quantum information, bit commitment, nonlocality.

## 11.2 Abstract (one paragraph)

Must contain:

1. Previous DI BC/CF used GHZ; unique among bipartite DI tasks in that respect.
2. GHZ pseudo-telepathy was essential to those proofs.
3. This work: CHSH testing, same cheating probabilities as Silman *et al.*, devices with memory.
4. Caveat: fixed reveal time.
5. Post-quantum recasting: overall more security.

Target length: ~150–180 words. Do not put formulae other than perhaps the two numbers $0.8536$ and $0.75$ (the published abstract is formula-free; the introduction has the numbers).

## 11.3 Section 1 — Introduction

Paragraph plan (the published order is good; steal the *order*, not the sentences):

1. Cryptographic assumptions in general; quantum vs classical; device-dependent vs DI.
2. DI via Bell tests; DIQKD as the flagship; hacking motivation.
3. Other DI tasks (randomness, self-testing, estimation, multipartite entanglement).
4. Distrustful cryptography as the extra challenge (conflicting goals).
5. Silman11 / Aharon14: GHZ; open question whether the whole distrustful class is DI.
6. Why GHZ was used (pseudo-telepathy; same measurements for test and check).
7. Why CHSH is the natural next question (RUV; experimental EPR vs GHZ).
8. **This work:** protocol, numbers, memory, imperfect devices, fixed reveal time, coin-flipping still OK, Apps. B–C, App. A.
9. Roadmap of sections.

Citations you need (minimum): Mayers–Yao; Barrett–Hardy–Kent; Clauser *et al.*; Acín *et al.* DIQKD; Pironio *et al.* 2009; Reichardt–Unger–Vazirani; Lo–Chau; Mayers; Spekkens–Rudolph; Chailloux–Kerenidis; Silman *et al.* 2011; Greenberger–Horne–Zeilinger; Gisin–Méthot–Scarani (no bipartite pseudo-telepathy); Kent relativistic BC.

## 11.4 Section 2 — Background

**2.1 Bit commitment.** Definitions of phases, $P_{\mathrm{cont}}$, $P_{\mathrm{gain}}$, perfect, balanced, CK bound.

**2.2 Device-independence.** Five assumptions; formula (1); memory/clocks; meaning of “send a box”; shielding vs relativity.

## 11.5 Section 3 — Protocol

- Notation paragraph ($S^i_k$, $W_k$, $\sigma_\theta$).
- Honest correlations (2) and the equality pairs; measurement table.
- Noisy case.
- Numbered protocol 1–3 with times $t^a,t^b,t^c,t^d,t_i$.
- Formulae (3)–(4) for $\bar I_n$ and $I(W_k)$.
- Completeness discussion (statistical abort vs noisy reveal abort).
- Timing argument (the kept box must not know it is in reveal).
- “Not strictly BC” paragraph + pointer to Apps. B–C.

Footnotes to restore: private $n$; factor $4$ in the indicator; interval $(t_i,t_{i+1}]$.

## 11.6 Section 4 — Alice’s security

- General Bob strategy; display (5); NS $\Rightarrow 3/4$.
- Two saturating strategies (classical box; honest EPR + input $0$).
- One sentence: matches Silman *et al.*

## 11.7 Section 5 — Bob’s security

Tell the reader the three-subsection plan in the first paragraph.

**5.1** Four-outcome POVM; (6); SDP (7); NPA level 2; Fig. 1 (produced from 5.2).

**5.2** Explicit strategy; (8)–(10); Fig. 2; saturation of the SDP.

**5.3** Memory; (11)–(19); Fig. 3; limit $\cos^2(\pi/8)$. Move the martingale lemma to App. D.

## 11.8 Section 6 — Summary

Restate: pseudo-telepathy is not essential; sequential CHSH + hidden $n$ + fixed times suffice; memory included; experimental motivation (EPR vs GHZ); techniques should transfer to DI coin flipping without BC and to DI OT.

## 11.9 Figures

| Figure | Content | How to produce |
|---|---|---|
| 1 | $P_{\mathrm{cont}}$ vs $I_{\mathrm{th}}$ | parametric plot of (8)–(10) |
| 2 | axes in the $zx$-plane | schematic (solid / dashed / dotted) |
| 3 | finite-$N$ bound vs $\log_{10} N$ | numerical min of (19) |

Run `python scripts/reconstruct_figures.py`. The published Fig. 1 is the analytic curve; Fig. 3 is a numerical upper bound, not an experiment.

## 11.10 Tone and claims to get right

- Do not claim perfect BC.
- Do not claim the protocol is balanced.
- Do not claim Alice-chosen reveal time in the main protocol.
- Do not claim the finite-$N$ bound is tight.
- Do claim matching Silman *et al.* **in the infinite-test limit**.
- Do claim shielding instead of spacelike separation.
- Do mention that always sending the same box would help Alice.

## 11.11 After the draft exists

1. Check every numbered equation against [reconstruction-checklist.md](reconstruction-checklist.md).
2. Check that Fig. 1 saturates $\cos^2(\pi/8)$ at $I=2\sqrt{2}$.
3. Check that Fig. 3’s $I_{\mathrm{th}}(N)$ matches its caption.
4. Verify you did not mix arXiv and NJP wording on the relativistic paragraph; pick one version.
5. Acknowledgements if you used YALMIP/SeDuMi or a Python SDP solver.
