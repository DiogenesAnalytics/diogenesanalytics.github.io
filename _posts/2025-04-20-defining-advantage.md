---
layout: article
title: Defining Advantage
custom_css: article.css
include_mathjax: true
---
## Introduction
*Advantage* is one of those *concepts* that is both very familiar to the average person, yet seemingly *absent* any attempts to *quantitatively* define it. We all roughly know when we are in a *"more advantageous"* position, but struggle to define exactly *"why"* our position is more advantageous (relative to the previous position). In this article, we will attempt to define *mathematically* what is **advantage**.

## Utility Difference
In its simplest form, **advantage** is the *positive difference* in utility $U$ between a currently selected *option* $O_A$ and some *alternate option* $O_B$:

+ Option A has a utility of $U(O_A) = 200$
+ Option B has a utility of $U(O_B) = 150$
+ Option A has a **net advantage** of $U(O_A) - U(O_B) = 50$ utility units over Option B.

Conversely, a **disadvantage** occurs when the currently selected option is *worse* than an alternative. In this case, the difference in utility is negative:

+ Option A has a utility of $U(O_A) = 100$
+ Option C has a utility of $U(O_C) = 300$
+ Option A has a **net disadvantage** of $U(O_A) - U(O_C) = -200$ utility units compared to Option C.

This of course assumes that the options being compared are of the same *option type*. What that means is they come from the same *utility function* (i.e. all [travel options](https://diogenesanalytics.com/blog/2025/03/12/the-travel-problem) calculated from the *travel utility* function).

## Multiple Option Types
If you want to calculate advantage between *different types* of options — such as travel plans, investment decisions, and health strategies simultaneously — you are no longer dealing with a single utility function. Instead, you can think in terms of a **utility vector** that aggregates different utility dimensions:

$$
\vec{V}_{u1} = \begin{bmatrix}
U_{\text{travel}}(O_A) \\
U_{\text{finance}}(O_B) \\
U_{\text{health}}(O_C)
\end{bmatrix}
$$

Here, $\vec{V}_{u1}$ represents the multi-dimensional utility vector associated with a particular decision set, where each component corresponds to a different utility function (or domain).

To compare two such options across multiple dimensions, we can compute the **vector difference**:

$$
\Delta \vec{V} = \vec{V}_{u1} - \vec{V}_{u2}
$$

The resulting vector describes the *direction and magnitude* of advantage (or disadvantage) across each domain. You can also compute a **scalar advantage** by taking the dot product with a weighting vector $\vec{w}$ representing the relative importance of each domain:

$$
A = \vec{w} \cdot \Delta \vec{V}
$$

This scalar $A$ gives you an overall weighted advantage, suitable for decision-making when utility components span different types.

## Game Position
This *mathematical* definition of advantage naturally extends to the context of games, especially competitive ones. In such settings, we can define a concept we will call **position advantage**: the relative utility of a player's current game state compared to alternate possible states.

In other words, a game position has **advantage** if, from a strategic or probabilistic perspective, it leads to higher expected utility (e.g. winning the game, gaining points, achieving a goal) than some other position. Conversely, a **disadvantageous** position is one from which fewer favorable outcomes are accessible or more constraints are imposed.

This connects tightly to ideas in:

* **Game theory**, where utility is tied to payoff matrices and strategic dominance
* **Chess/Go/board games**, where evaluation functions assign heuristic values to positions
* **AI planning**, where state-space search evaluates the "goodness" of a state

We can formalize this idea using expected utility over possible outcomes from a position, denoted $P$:

$$
\text{Advantage}(P) = \mathbb{E}[U \mid P] - \mathbb{E}[U \mid P_{\text{baseline}}]
$$

Where:

* $\mathbb{E}[U \mid P]$ is the expected utility from current position $P$
* $P_{\text{baseline}}$ could be a prior position, an opponent's position, or a neutral reference state

This definition makes clear: **advantage is not about winning outright**, but about *increasing the expected value* of outcomes from your current position, relative to some reference.

## Moral
Regardless of what is the *utility function* used to calculate the various *options* available (or in a game what we might call *positions*) **advantage** (or **disadvantage**) is merely the *difference* between the two *options* / *positions*. The whole of *decision making* and *game theory* can ultimately be reduced down to determining which *option(s* / *position(s)* relative to my current *option* / *position* *maximize* the *positive utility difference*.
