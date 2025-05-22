---
layout: article
title: Survival of the Fittest - The Ultimate Game of Life
custom_css: article.css
include_mathjax: true
---
## Introduction
From [Conway’s elegant Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) to [Hasbro’s symbolic board game](https://en.wikipedia.org/wiki/The_Game_of_Life), "life" has long been the subject of abstract simulation. In this article we proposes a new game, **Survival of the Fittest**, grounded not in entertainment or [cellular automata](https://en.wikipedia.org/wiki/Cellular_automaton), but in the biological imperatives that shape all living systems: survival and reproduction.

## The Cost of Living
To model the game of life, we must first ask: What do organisms need in order to survive, thrive, and reproduce? What resources do they pursue, and how do these shape their behaviors?

At a minimum, every living system depends on a combination of critical inputs - energy, water, shelter, safety, and, eventually, access to mates. These needs are not arbitrary; they reflect universal *needs* that any organism must navigate in order to persist in its environment.

These survival requirements are not reducible to a single objective. Rather:

    Organisms must simultaneously manage multiple forms of scarcity.


## Fitness Defined
In our Survival of the Fittest game, we can then think of fitness as a [vector](https://en.wikipedia.org/wiki/Vector_(mathematics_and_physics)), where each dimension tracks how well an organism is doing in a particular domain relevant to survival or reproduction. This leads us to a powerful mathematical abstraction: representing fitness as a [utility vector](https://diogenesanalytics.com/blog/2025/04/20/defining-advantage#multiple-option-types), with each dimension capturing the current utility *earned* by securing a specific resource or advantage critical to survival and reproduction:

$$
\mathbf{F} = \begin{bmatrix}
u_1 \\
u_2 \\
\vdots \\
u_n
\end{bmatrix}
$$

These components (i.e. $u_1, u_2, \dots, u_n$) could be anything. But as an example here are some possible choices:

* Quantity of energy reserves (from food)
* Access to water
* Quality of shelter
* Size and control of territory
* Mating opportunities and success
* etc ...

The **overall fitness** is simply the weighted sum of these utilities, which represents the *total utility* or *fitness utility* $U_f$:

$$
U_f = w \cdot F = \sum_{i=1}^n w_i \cdot u_i
$$

where weights $w_i \geq 0$ represent the relative importance of each utility dimension in the organism's environment and evolutionary context (this can by default simply be $w_i = 1$).

## The Goal of Life
Now with *fitness* defined as a *utility vector* $F$ the actual *"goal"* of the game can be defined very simply:

$$
\max_{\pi} \; U_f(\pi)
$$

where:

* $\pi$ is the **policy** (aka *strategy*) the organism follows.
* $U_f(\pi)$ is the fitness utility resulting from that strategy.

In other words the **goal** is to maximize the *fitness utility* $U_f$.

## A Hierarchy of Needs
So organisms are ultimately seeking to improve their *strategy* $\pi$ (what is often called a **policy**) in order to maximize $U_f$. This tells us *what* the players in the game are trying to achieve.

But it does **not** yet tell us *how* to think about good strategies.

What *constraints* shape the order in which different utilities can be pursued? How do organisms allocate effort across competing needs?

A useful starting point comes from a familiar framework in psychological theory: [Maslow's Hierarchy of Needs](https://en.wikipedia.org/wiki/Maslow%27s_hierarchy_of_needs). Though originally developed to describe human motivation, Maslow’s core insight is far more general:

    Certain needs must be satisfied before others can be meaningfully pursued.


This hierarchy reflects a deep truth about biological systems: **not all resources are equally actionable at all times**. For example, a dehydrated organism will not—and arguably cannot—rationally pursue reproductive opportunities before first securing water.

## Basic Strategy
Thus, Maslow's hierarchy can be reinterpreted as a **dependency structure** on fitness components. Instead of treating each fitness dimension as an independent axis, we now recognize that some components of the utility vector are **prerequisites** for others.

This transforms our view of strategy:

* Organisms are not simply optimizing over a flat space of utility values.
* They are navigating a **constrained optimization problem** shaped by the *dependency relationships among needs*.

In game-theoretic terms, this implies that the policy $\pi$ must respect a **partial ordering** of the fitness dimensions in $F = [u_1, u_2, ..., u_n]$.

We can represent these constraints as a **graph of prerequisites**, which models the conditional dependencies between need types. For example:

```
  Energy → Safety → Territory → Mating
             ↓
          Shelter
```

This kind of structure imposes a universal scaffolding on all players in the game: **before you can play for higher-order fitness, you must win the lower levels first**.

This means not every policy $\pi$ is valid: only those that **respect the prerequisite relationships** encoded in the dependency graph are admissible.

We can formalize this:

Let:

* $F = [u_1, u_2, \dots, u_n]$: the fitness utility vector.
  <br><br>
* $G = (V, E)$: a **directed acyclic graph** (DAG) over the set of needs $V = \{u_1, u_2, \dots, u_n\}$, where $(u_i \rightarrow u_j) \in E$ means that utility $u_i$ must be satisfied *before* utility $u_j$ becomes actionable.
  <br><br>
* $\Pi$: the space of all possible strategies (policies).
  <br><br>
* $\Pi_G \subseteq \Pi$: the subset of strategies **admissible under the dependency graph**.

Then:

$$
\pi^* = \arg\max_{\pi \in \Pi_G} U_f(\pi)
$$

In words: the optimal policy is the one that **maximizes total fitness utility**, but only among the strategies that **respect the dependency structure** of the *needs graph* $G$.

This is no longer a vanilla optimization. It is a **constrained maximization problem**, where the constraint is **structural**: strategies must obey the **causal or functional precedence** encoded in the hierarchy of needs.

This reframes the game in a profound way:

* The goal is still to **maximize the total fitness utility** $U_f$. That hasn’t changed.
  <br><br>
* But what *has* changed is our understanding of **how** to reach that maximum.
  <br><br>
* The components of the fitness vector $F$ are not all equally accessible at all times.
  <br><br>
* **Some utilities are conditional on others** — you can’t pursue higher-order gains until foundational needs are met.
  <br><br>
* Therefore, **maximizing $U_f$** requires **finding a policy that respects the dependency graph** $G$ over fitness dimensions.

## Conclusion
The "Survival of the Fittest" is not a chaotic scramble for resources, but a highly structured optimization problem. Organisms aren't just maximizing fitness in the abstract — they are doing so under real, biological constraints shaped by interdependent needs. By formalizing fitness as a utility vector and representing dependencies between needs as a directed acyclic graph, we reveal a deeper logic to evolutionary strategy:

    Success in the game of life requires more than maximizing — it requires sequencing.


This reframing has powerful implications. It unites psychological theory (Maslow), evolutionary biology (fitness landscapes), and game theory (policy optimization) into a single mathematical perspective. And it shows that fitness is not merely about acquiring resources, but about acquiring them in the right order, at the right time, under the right constraints.

In this light, life becomes a constrained utility-maximization game — one where the optimal strategy must navigate not just scarcity, but structure. Understanding that structure may be the key to modeling intelligence, adaptation, and survival itself.
