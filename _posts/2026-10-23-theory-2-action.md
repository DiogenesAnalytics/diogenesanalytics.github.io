---
layout: article
title: From Theory to Action
custom_css: article.css
include_mathjax: true
publish: true
---
## Introduction

An agent seeks to improve its position. To do so, it must evaluate available actions and determine which will lead to better positions. But deciding how to improve its position is itself a challenge. The agent may need to develop its reasoning capabilities, acquire information, or investigate alternatives before it can identify the most beneficial course of action. Alternatively, it may already possess sufficient knowledge and reasoning capabilities to act directly.

These are different ways of improving position. Some actions change the external environment directly; others change the agent's knowledge or capabilities, enabling it to make better decisions subsequently. All consume resources, and the value of each depends on the position from which it is taken and the consequences it produces.

Let $P$ denote the agent's current position, $a$ an available action, and $F$ the transition function determining the resulting position:

$$
P' = F(P,a)
$$

If $U(P)$ denotes the utility of position $P$, the change in utility resulting from an action is

$$
\Delta U(P,a) = U(F(P,a)) - U(P)
$$

An action's value is determined by how it changes the position. This applies equally to actions that directly alter external circumstances and those that change the agent's knowledge or capabilities. The latter may produce their greatest benefits through the subsequent actions they enable, but their value still derives from their contribution to improving position.

There is no universally optimal choice between theoretical development, information acquisition, and direct implementation. Further theoretical development may improve the agent's ability to evaluate alternatives; acquiring information may reveal a better course of action; and implementing an already justified decision may produce a greater improvement than further investigation. Which approach is preferable depends on the agent's current position, its available resources, and the opportunities each action creates.

The problem is therefore to determine how best to improve position given the agent's current circumstances. The agent must evaluate the available means of doing so, accounting for both the immediate consequences of an action and the subsequent possibilities it enables. The path from theory to action is not a progression from one objective to another, but a choice among different ways of improving position.

## The Allocation Problem

Let $P$ denote the current position, $\mathcal{A}(P)$ the available actions, and $F(P,a)$ the resulting position:

$$
P' = F(P,a), \qquad a \in \mathcal{A}(P)
$$

Every action changes position. The problem is to select an action that produces a more favorable transition:

$$
a^* = \arg\max_{a \in \mathcal{A}(P)} U(F(P,a))
$$

The available actions include theoretical development, information acquisition, and implementation. Let

$$
\mathcal{A}(P)
=
\mathcal{A}_{T}(P)
\cup
\mathcal{A}_{I}(P)
\cup
\mathcal{A}_{X}(P)
$$

where $\mathcal{A}_{T}$ denotes theoretical development, $\mathcal{A}_{I}$ information acquisition, and $\mathcal{A}_{X}$ implementation.

These categories distinguish the means of changing position, not whether position changes. Each action transforms the position, potentially altering the agent's knowledge, reasoning capabilities, available actions, and subsequent transitions.

Resource constraints further restrict the choice. If $c(a)$ denotes the resources required by action $a$ and $B$ the available resource budget, then the allocation problem is

$$
a^* = \arg\max_{a \in \mathcal{A}(P)} U(F(P,a))
\quad
\text{subject to}
\quad
c(a) \leq B
$$

The best allocation therefore depends on $P$, the available actions, their resource requirements, and their resulting positions. No category is inherently superior; its value depends on the transition it produces from the current position.

## Position-Dependent Value

For any available action $a \in \mathcal{A}(P)$, the change in utility is

$$
\Delta U(P,a) = U(F(P,a)) - U(P)
$$

The value of an action depends on the transition it produces from the current position. This applies equally to theoretical development, information acquisition, and implementation. Each changes position; what differs is the resulting transition and its consequences.

Let $\mathcal{A}(P)$ denote the available actions, partitioned into categories of theoretical development, information acquisition, and implementation. The preferred action is

$$
a^*(P) = \arg\max_{a \in \mathcal{A}(P)} \Delta U(P,a)
$$

subject to the resources available for its execution.

Because both the available actions and their resulting transitions depend on $P$, the preferred allocation can change as the agent's position changes. An investment in reasoning, an acquisition of information, or an immediate implementation may each be optimal in one position and inferior in another.

$$
\boxed{
a^* = a^*(P)
}
$$

There is no universally optimal allocation between theory, information, and implementation. The preferred allocation depends on the current position, the available actions, their resource requirements, and the resulting transitions.

## From Evaluation to Action

The allocation problem is itself a decision problem. The agent must select among actions that change its position in different ways, including actions that alter its reasoning capabilities, acquire information, or change its external circumstances.

Let $\mathcal{A}(P)$ denote the available actions. For each action $a$, the agent evaluates the resulting position:

$$
P' = F(P,a)
$$

The preferred action depends on the relative utility of the resulting positions, subject to the resources required and the subsequent possibilities each transition enables.

This yields a practical principle: **choose the available action that offers the greatest improvement in position, accounting for its resource cost and its consequences for future positions.**

The appropriate choice may be theoretical development, information acquisition, or direct implementation. No category takes precedence by default. The agent should allocate resources according to the opportunities available from its current position, reassessing its choices as that position changes.

## Conclusion

Theoretical development, information acquisition, and implementation are alternative means of changing position. Their relative value depends on the current position, the resources required, and the consequences of the resulting transitions.

No activity is inherently superior. The objective is neither to maximize theoretical sophistication, accumulate information, nor act for its own sake, but to improve position.

**From theory to action is itself a decision problem: choosing how to change position to achieve the greatest improvement.**
