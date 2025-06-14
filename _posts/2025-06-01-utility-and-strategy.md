---
layout: article
title: Utility Functions and Optimal Strategies - The Ultimate Limit
custom_css: article.css
include_mathjax: true
---
## Introduction
Every game embodies two fundamental questions:

* **What matters?**
* **How to achieve it?**

These questions are formalized in game theory through the concepts of **utility functions** and **strategies**.

A utility function defines the meaning of success. It encodes what outcomes are desirable, what trade-offs are acceptable, and ultimately, what it means to “win” or “do well” in a particular environment. A strategy, by contrast, is a method: an operational answer to the question of how to act in order to *maximize* utility.

At first glance, these may appear as separate concerns: one defines the goal, the other the means. But on closer inspection, they form a tightly bound relationship. In fact, a strategy is only optimal **relative** to a particular utility function. And a utility function only becomes fully meaningful when it gives rise to an optimal strategy that consistently achieves its aims.

Formally, we can represent this as:

* Let $u: \mathcal{O} \to \mathbb{R}$ be the utility function assigning a real-valued score to each possible outcome $o \in \mathcal{O}$.
* Let $\pi$ be a strategy, which prescribes how to act in various situations.
* The **expected utility** of strategy $\pi$ is:

$$
\mathbb{E}_{\pi}[u] = \sum_{o \in \mathcal{O}} P_{\pi}(o) \cdot u(o)
$$

where $P_{\pi}(o)$ is the probability of outcome $o$ occurring when following strategy $\pi$.

An **optimal strategy** $\pi'$ is then one which maximizes this expected utility:

$$
\pi' = \arg\max_{\pi} \mathbb{E}_{\pi}[u]
$$

This article explores the interdependence between utility functions and optimal strategies, arguing that they are not merely coexisting elements within a game, but mutually defining aspects of intelligence. In the same way that a map and a route must correspond to one another, a utility function and an optimal strategy reflect a unified understanding of what matters and how best to achieve it.

Through this lens, we investigate what it means for a utility function to be **ultimate** (i.e., to fully capture the values of a game) and how the emergence of an optimal strategy reveals and validates this function. Together, they form the backbone of intelligent play, whether in structured games, natural evolution, or artificial decision-making systems.

## Utility Functions & Games
At the heart of every intelligent action lies a concept of value. A **utility function** is the formal representation of this value—it tells an agent (i.e. player) what is desirable, what is not, and how different outcomes compare. In the context of games, a utility function defines the purpose of play: whether the goal is to win, to maximize points, to minimize loss, or to achieve some complex tradeoff among multiple objectives.

As explored in my earlier piece [*Reasoning About Utility*](https://diogenesanalytics.com/blog/2025/02/26/reasoning-about-utility), utility is not merely a mechanical scoring mechanism: it is the formal encoding of **what matters**. Whether we're dealing with a chess engine, an animal foraging for food, or a human navigating a strategic dilemma, the utility function determines what "success" looks like.

In simple games, the utility function may be clearly defined by the rules themselves, such as winning a race or capturing the king. But in more complex or open-ended scenarios, utility becomes more elusive. It may evolve over time, shift based on experience, or remain partially hidden to the player. Yet, behind any coherent behavior lies some notion of value being pursued.

Formally, the utility function $u$ maps the space of possible outcomes $\mathcal{O}$ to the real numbers $\mathbb{R}$:

$$
u : \mathcal{O} \to \mathbb{R}
$$

where each outcome’s utility reflects its value to the agent.

This brings us to the concept of an **ultimate utility function** $u^*$, a hypothetical, complete, and final specification of what truly matters in a given environment. In principle, such a function would fully describe the agent’s values, preferences, and tradeoffs without ambiguity.

In practice, agents often begin with incomplete or evolving approximations $u_t$ of this ultimate utility, refining their understanding over time $t$:

$$
\lim_{t \to \infty} u_t = u^*
$$

It is this evolving relationship between partial utility approximations and the ideal of an ultimate utility function that makes the dynamics of learning and intelligence so interesting. And as we will see next, whatever form the utility function takes, partial or perfect, it plays a defining role in shaping an agent’s strategy.

## Strategies & Optimality
If the utility function $u$ defines *what matters*, then a **strategy** $\pi$ defines *how to act* to achieve the best possible outcome. Formally, a strategy is a mapping from the information available to the agent, such as game states or history, to actions:

$$
\pi: \mathcal{S} \to \mathcal{A}
$$

where $\mathcal{S}$ is the set of possible states (or observations) and $\mathcal{A}$ is the set of available actions.

Given a strategy $\pi$ and a game environment with probabilistic transitions, the distribution over possible outcomes $P_{\pi}$ is induced by the policy. The expected utility of $\pi$ is:

$$
\mathbb{E}_{\pi}[u] = \sum_{o \in \mathcal{O}} P_{\pi}(o) \cdot u(o)
$$

The **optimal strategy** $\pi'$ relative to utility $u$ is one that maximizes this expectation:

$$
\pi' = \arg\max_{\pi} \mathbb{E}_{\pi}[u]
$$

This optimal strategy can be unique or one among many strategies achieving the maximum expected utility.

Note that the optimal strategy depends *entirely* on the utility function $u$. Change the utility function, even slightly, and the optimal strategy, or the set of optimal strategies $\Pi' = \{ \pi \mid \pi = \arg\max_{\pi} \mathbb{E}_{\pi}[u] \}$ when there are more than one, may change, sometimes dramatically. Hence, the **optimal strategy is relative to the utility**: it is defined in direct response to what the utility function values. This relativity means that any refinement or evolution in the agent’s understanding of what it cares about necessarily reshapes how it acts optimally.

## Interdependence of Utility and Strategy
So far, we have treated the utility function $u$ and the optimal strategy $\pi'$ as distinct components: one defines what matters, the other dictates how best to act. But in practice — and in theory — they are deeply interdependent.

A strategy \$\pi\$ is only **optimal** relative to a particular utility function $u$. Change $u$, and the optimal strategy $\pi'$ may change. Conversely, the utility function $u$ is only **validated** through the success of the optimal strategy it produces. If $u$ prescribes a value system that yields poor outcomes when followed optimally, we are forced to question whether it truly captures what matters.

This interdependence can be formalized through the expected utility:

$$
\mathbb{E}_\pi[u] = \sum_{o \in \mathcal{O}} P_\pi(o) \cdot u(o)
$$

An optimal strategy $\pi'$ is defined as:

$$
\pi' = \arg\max_\pi \mathbb{E}_\pi[u]
$$

But this equation is only meaningful if $u(o)$ accurately encodes the agent's values, and $P_\pi(o)$ accurately reflects the outcomes induced by following $\pi'$. If the agent's utility is misaligned with reality, or if the policy fails to reflect it in action, then the agent's behavior will fail to achieve its intended goals.

In learning systems — biological, artificial, or otherwise — this creates a **feedback loop**: utility functions are revised based on the observed success of strategies, and strategies are refined to better optimize utility. Over time, this co-evolution can converge toward more coherent, aligned systems of value and behavior.

This mutual constraint between $u$ and its optimal strategy $\pi'$ implies that neither is independently primary. Instead, **they define each other**. Just as a route validates a map, the success of $\pi'$ gives semantic weight to $u$ by demonstrating that its values can be effectively pursued in the world.

In this light, we can understand intelligent behavior not as the blind execution of a fixed plan, but as the **dynamic interplay** between value and action. The utility function determines what success looks like. The strategy tests whether that notion of success is achievable. Together, they form a closed loop of meaning, optimality, and adaptation.

## Ultimate Utility / Strategy
If every optimal strategy is defined *relative* to a utility function, and every utility function is only meaningful when it gives rise to a strategy that achieves its aims, then we are naturally led to a deeper question:

> Is there such a thing as an **ultimate utility function**—and correspondingly, an **ultimate strategy**?

Let’s formalize this.

Suppose an agent is not born knowing its utility function $u$, but instead begins with a sequence of approximations $u_1, u_2, \dots$ that become increasingly refined as it learns more about the environment, its values, or the consequences of its actions. This sequence converges (in some topology) to a limiting function $u^{\ast}$, which we call the **ultimate utility function** — the final and complete specification of what the agent ultimately cares about:

$$
\lim_{i \to \infty} u_i = u^{\ast} \,.
$$

For each $u_i$, the corresponding **optimal strategy** $\pi_i'$ maximizes expected utility under $u_i$:

$$
\pi_i' = \arg\max_{\pi} \mathbb{E}_{\pi}[u_i] \,.
$$

As the utility functions converge, their optimal strategies also converge to a limiting strategy $\pi^{\ast}$:

$$
\lim_{i \to \infty} \pi_i' = \pi^{\ast} \,.
$$

By definition, the **ultimate strategy** $\pi^{\ast}$ is the optimal strategy for the **ultimate utility function** $u^{\ast}$:

$$
\pi^{\ast} = \arg\max_{\pi} \mathbb{E}_{\pi}[u^{\ast}] \,.
$$

Thus,

* $u^{\ast}$ is the **ultimate utility**, and
* $\pi^{\ast}$ is the **ultimate strategy**.

This convergence can be interpreted in multiple domains:

* In **machine learning**, agents often refine both value functions and policies over time.
* In **biological evolution**, fitness functions are shaped by ecological constraints, and behaviors (strategies) evolve accordingly.
* In **human cognition**, ethical and personal values are refined through reflection and experience, with strategies for action adapting in tandem.

Crucially, this formulation reveals that *learning* and *optimization* are not independent processes: refining $u$ changes what it means to be optimal, and changing $\pi'$ affects what outcomes are experienced — thus influencing how $u$ should be updated.

In this sense, intelligence is not merely about solving a fixed optimization problem, but about *jointly discovering what to optimize and how to do it*. The two must co-evolve. The closer an agent gets to understanding its true utility $u^{\ast}$, the more coherent and effective its optimal strategy $\pi'$ becomes (converging closer and closer to $\pi^{\ast}$). And vice versa: observing the performance of different strategies helps shape a clearer picture of what truly matters.

Ultimately, the alignment of $u^{\ast}$ and $\pi^{\ast}$ is the hallmark of mature intelligence — whether in an artificial agent, a living organism, or a rational decision-making system. It represents the convergence of *value* and *action*, of *goal* and *means*, into a unified whole.

## Moral
Utility functions and strategies are often treated as distinct components of rational behavior: one specifying goals, the other prescribing actions. But as we have seen, they are fundamentally intertwined. A utility function without a strategy is inert: it expresses values but cannot act. A strategy without a utility function is blind: it acts without direction or justification.

Optimal behavior emerges only when the two are aligned. The utility function defines what is worth pursuing, and the strategy operationalizes that pursuit in the context of the environment's constraints and dynamics. Formally, the optimal strategy $\pi'$ is that which maximizes the expected utility under $u$, and conversely, the value of a utility function is only validated when it gives rise to a strategy that achieves its aims.

This interdependence reaches its culmination in the idea of an **ultimate utility function** $u^{\ast}$ and an **ultimate strategy** $\pi^{\ast}$: a pair that co-evolve toward a point of mutual consistency, where the agent’s conception of what matters and its way of acting are in complete harmony.

This is what it means to **master** a system. Mastery is not just skillful action, nor is it merely having clear goals: it is the internal unification of purpose and practice. To master a game is to converge on the pair $(u^{\ast}, \pi^{\ast})$: to know what truly matters, and to act accordingly with unerring precision.

Viewed through this lens, intelligence itself can be seen as the ongoing process of converging toward this ideal, refining both the values that guide decisions and the methods by which they are pursued. Whether in human deliberation, machine learning, or natural evolution, the dance between utility and strategy defines the arc of progress. It is not just about doing the best we can with what we believe, it is about learning what is worth believing in, and how best to act on it.
