# Start here if you do not know quantum mechanics

You do not need wavefunctions, Hilbert space, or “what is a photon”. This paper can be read as a story about **two black boxes**, a **quiz the boxes play**, and a **sealed envelope**.

The full plain-language path is in Chinese under [`beginner/`](beginner/README.md) (recommended if you read Chinese). This page is the same map in English, compressed.

## The story in one page

Alice wants to **seal** a bit $0$ or $1$ and open it later:

- After sealing she should not be able to change her mind.
- Before opening, Bob should not be able to read the bit.

A perfect seal is impossible in quantum theory. This paper gives an imperfect one, and it is **device-independent**: you never trust what is inside the machines—only the buttons you press and the $0/1$ lights you see.

Each machine is a **box**: you type a setting $0,1,2,3$, it shows a bit. Two boxes may be spookily correlated, but they must obey **no signalling**: looking only at *your* light, you cannot tell which button the other person pressed (otherwise the boxes would be a telegraph).

## A quiz called CHSH

A referee gives Alice and Bob random questions $x,y\in\{0,1\}$. They answer $a,b\in\{0,1\}$ without talking. They win if $a\oplus b=x\cdot y$ (same answers, except when both questions are $1$, when they need opposite answers).

- If they only agreed a table in advance, they win at most **75%** of the time. That is the classical / local bound (the paper’s $I\le 2$).
- Quantum boxes can reach about **85%**, never 100%. That is Tsirelson’s bound $I=2\sqrt{2}$.
- If you keep only “no telegraph” and drop quantum theory, 100% is possible (a PR box, $I=4$). Nature does not give you that.

An older device-independent protocol used a *different* quiz (GHZ) that quantum players **always** win. Then one measurement can both “test the boxes” and “check Alice’s opening”. CHSH cannot always win, so this paper’s trick is: **hide which round is the check**. Bob secretly picks how many quiz rounds to run, always presses buttons at public clock times, and the leftover box cannot tell “another quiz round” from “catching a liar”.

## The protocol as a play

1. **Quiz.** Bob secretly chooses $n$, plays CHSH for $n$ public bell-times, aborts if the score is too low, then mails Alice one of the two boxes.
2. **Seal.** Alice presses a “commit” button that depends on her bit $b$, sees a light $r$, and mails a masked voucher $q=r\oplus (a\cdot b)$ ($a$ is a private coin).
3. **Open.** Before the *next* public bell she must send $b$ and $r$. Bob checks the voucher, then at that bell presses the matching button on the box he kept; the two lights should agree.

If $n$ were public, Alice would make the first $n$ uses look brilliant and the next use obey her. If the last press happened at a weird time, the box’s internal clock would know the exam was over.

## The two cheating numbers

| Cheater | Goal | Best success (many quiz rounds, max CHSH) | Why not better |
|---|---|---|---|
| Bob | Guess $b$ before opening | $3/4$ | No signalling: $q$ is a real mask three quarters of the time |
| Alice | Open whichever bit she wants | $\cos^2(\pi/8)\simeq 0.85$ | The kept box must still look CHSH-like; her best shot is to aim *between* Bob’s two check buttons |

The protocol is **not** balanced ($0.85\neq 0.75$) and **not** perfect. Opening time is **fixed** by the clock (appendices B/C relax that).

## What to read next

Chinese, slow and complete: [`beginner/README.md`](beginner/README.md).

Then the exercise book, starting at [`01-prerequisites.md`](01-prerequisites.md) (Chinese: [`01-prerequisites.zh.md`](01-prerequisites.zh.md)). Translate as you go:

- POVM = the rule that turns a button into a random $0/1$ light
- no-signalling identity = your light’s statistics do not depend on their button
- $I$ = CHSH quiz score
- martingale / Azuma = even a box with a grudge cannot make the running average jump away from its true level too far, too often
