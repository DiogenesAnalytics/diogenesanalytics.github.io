---
layout: article
title: The Illusion of Simplicity - How Limited Options Distort Utility
custom_css: article.css
include_mathjax: true
---
## Introduction
Imagine you are facing a choice between three options in a game, a business decision, or even your lunch menu. You evaluate them using a utility function like:

$$
U = \frac{A \cdot B}{C \cdot D}
$$

Where each variable represents a meaningful factor:

* **A**: benefit (e.g. points gained, profit, flavor)
* **B**: bonus multiplier (e.g. synergy, customer satisfaction)
* **C**: cost
* **D**: difficulty or risk

Here is your set of options:

| Option | A (Benefit) | B (Bonus) | C (Cost) | D (Difficulty) | Utility $U = \frac{AB}{CD}$        |
| ------ | ----------- | --------- | -------- | -------------- | ---------------------------------- |
| 1      | 10          | **2**     | 5        | **1**          | $\frac{10 \cdot 2}{5 \cdot 1} = 4$ |
| 2      | 9           | **2**     | 3        | **1**          | $\frac{9 \cdot 2}{3 \cdot 1} = 6$  |
| 3      | 12          | **2**     | 8        | **1**          | $\frac{12 \cdot 2}{8 \cdot 1} = 3$ |

Now observe: even though $B = 2$ and $D = 1$ for every option, the utility values still differ, because $A$ and $C$ vary. But because $B$ and $D$ are **constant**, we can simplify the function:

$$
U = \frac{A \cdot 2}{C \cdot 1} = 2 \cdot \left(\frac{A}{C}\right)
$$

Since the multiplier (i.e. [scalar](https://en.wikipedia.org/wiki/Scalar_(mathematics))) $2$ is the same for every option, it does not affect *which option is best*. So you can mentally reduce the utility to:

$$
\text{Effective comparison: } U = \frac{A}{C}
$$

Now your decision *feels* simpler: you are just comparing benefit-to-cost ratios, even though the original function was more complex.

But here is the key insight:

    The available options create a local illusion of simplicity by flattening the
    utility landscape.


This *illusion of simplicity* happens when the set of options **lacks variability** across certain dimensions. You are not making a simpler decision because the world got easier — you are just looking at a flatter part of it.

## Local Simplicity vs Global Complexity
What you have encountered is a phenomenon we might call **local utility flattening**. The full utility function still depends on four variables. But in your current **local context**, some of those variables are not changing, so they **drop out of your attention**.

This gives the illusion that the decision is simpler or that only some factors *"matter."* But it is only because the other variables are currently **not offering any contrast**.

If tomorrow, new options appear where $B$ or $D$ vary wildly, you will suddenly need to re-engage with the full complexity of the utility function again.

## The Psychology of Constrained Choice
This illusion of simplicity has real *psychological effects*:

* **Cognitive ease**: Fewer active variables makes the choice feel simpler and faster.
  <br><br>
* **Overconfidence**: Decision-makers may assume they *"understand the system,"* when they are really just operating in a *low-contrast* **slice** of it.
  <br><br>
* **Misattribution**: The simplicity is mistaken as a trait of the system, not the context.

## Moral
Always remember:

    A utility function only simplifies when you narrow the space of variation


That simplification is not *"real"* in the global sense — it is a *local phenomenon*. And mistaking a local simplification for a structural one can lead to flawed strategies or design choices.

In life, games, and systems thinking:

    What seems simple might just be temporarily flat.

