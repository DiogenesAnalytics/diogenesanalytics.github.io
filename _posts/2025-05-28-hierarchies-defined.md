---
layout: article
title: Hierarchies as Expanding Sets - A Threshold Theory of Access
custom_css: article.css
include_mathjax: true
---
## Introduction
When most people hear the word *"hierarchy,"* they think of power structures: who is on top, who is on bottom, and what authority each level has over the one below. But hierarchies can be understood in another, deeper way: not as systems of control, but as *structures of access*. In this view, hierarchies define a set of *thresholds* and each threshold, once crossed, expands the range of possibilities available to you.

This article explores a theory of hierarchies as **threshold-based systems** that expand access to **cumulative sets of options**: tools, choices, or states of being. As you rise through levels, your *option space* expands. What you could not do before becomes possible, not because the world changed, but because *you did*.

## Structure of Access
A **hierarchy** $\mathcal{H}$ can be defined as an ordered sequence of discrete levels:

$$
\mathcal{H} = \langle L_0, L_1, \dots, L_n \rangle
$$

Each level $L_i$ is associated with a **set of options** $S_i \subseteq \mathcal{G}$, where $\mathcal{G}$ represents the global option space (i.e., the set of all possible options).

$$
L_i \mapsto S_i \subseteq \mathcal{G}
$$

At any level $L_k$, the total accessible option set $\mathcal{O}_k$ is the **cumulative union** of all option sets up to and including that level:

$$
\mathcal{O}_k = \bigcup_{i=0}^{k} S_i
$$

This cumulative nature ensures that moving up the hierarchy never removes access: it only expands the available set.

$$
\mathcal{O}_0 = S_0,\quad \mathcal{O}_1 = S_0 \cup S_1,\quad \dots,\quad \mathcal{O}_k = \mathcal{O}_{k-1} \cup S_k
$$

This forms a nested chain of subsets:

$$
\mathcal{O}_0 \subseteq \mathcal{O}_1 \subseteq \dots \subseteq \mathcal{O}_n \subseteq \mathcal{G}
$$

Transitioning from one level to the next is **not automatic**. It is gated by a **requirement function**:

$$
R_k : \mathcal{X}_k \to \{ \text{True}, \text{False} \}
$$

where $\mathcal{X}_k$ represents an abstract space of qualifications, conditions, or variables relevant at level $k$. These can include mastery, knowledge, ability, experience, resources, or internal psychological states—depending on the domain.

This formulation recognizes that advancement depends on satisfying **criteria that may not be directly tied to the option sets themselves**, but instead on some contextual or internal factors:

$$
\text{Advance from } L_k \to L_{k+1} \quad \text{if and only if} \quad R_k(x_k) = \text{True}, \quad x_k \in \mathcal{X}_k
$$

Each new level adds something new but never subtracts. The structure is **cumulative**, building a broader and broader landscape of possibilities as you climb. In this way, a hierarchy becomes not a *ladder of power*, but a *tree of expansion*.

## Visualizing Hierarchies
This structure can be visually represented as a chain or tree, where each node is a level $L_i$, branching out as options accumulate:

```
L0 (S0) 
  |
L1 (S1) 
  |
L2 (S2)
  |
...
  |
Ln (Sn)
```

At each level, the union of all sets $S_i$ for $i \le k$ defines the total available options $\mathcal{O}_k$.

## Implications
This formal structure helps us move beyond the abstract idea of *"levels"* and instead see hierarchies as **architectures of expanding access**. Rather than limiting or ranking individuals, hierarchies, when viewed as cumulative systems, reveal how growth can open up new domains of possibility.

A few important implications follow:

* **Cumulative Access**: Advancing in a hierarchy never removes prior options, it only adds. You retain what you have already
  unlocked.
  <br><br>
* **Non-Automatic Advancement**: Movement from one level to the next is conditional. The requirement function $R_k$ ensures
  that progression depends on meeting specific qualifications or developmental thresholds. These may include skills, maturity,
  experience, or even transformation of worldview.
  <br><br>
* **Expanding Possibility Space**: Each new level grants access to options that were previously out of reach. These might not
  just be *"better"* options, but categorically new forms of action, perception, or decision-making.
  <br><br>
* **Hierarchy as Tree of Expansion**: Rather than imagining a hierarchy as a vertical ladder where those *"above"* dominate
  those *"below,"* it is more fruitful to think of it as a **branching structure**: each level growing the accessible space
  outward. The higher you go, the more expansive your world becomes.

## Utility Reflects Access
The structural insights above do more than reshape how we understand progression: they also challenge how we think about utility. It is tempting to assume that value comparisons remain stable as we grow. But this is rarely true. Utility, like access, is **hierarchical**: its shape depends on what you can see, do, and choose, that is, your available options $S_k \subseteq \mathcal{G}$, where $\mathcal{G}$ is the global option space.

In [*The Illusion of Simplicity*](https://diogenesanalytics.com/blog/2025/05/27/utility-mirage), we explored how utility functions $U_k: S_k \to \mathbb{R}$ often appear deceptively simple when the option space $S_k$ is constrained. Key variables remain constant across $S_k$, so trade-offs appear clean, and value comparisons seem straightforward.

However, the hierarchy model developed here reveals a deeper dynamic.

At each level $L_k$, the accessible option set $S_k$ grows cumulatively:

$$
S_0 \subseteq S_1 \subseteq S_2 \subseteq \cdots \subseteq S_n \subseteq \mathcal{G}
$$

Crossing a threshold from level $L_k$ to $L_{k+1}$ does not merely add more options:

$$
S_{k} \subset S_{k+1}
$$

It often introduces a **qualitatively different decision space**, where new variables or dimensions become relevant: variables that were previously fixed, irrelevant, or invisible in $S_k$ now vary within $S_{k+1}$.

This corresponds to a structural shift in utility: the dimensionality of the utility function $U_k$ increases as you advance through levels. More formally, if $U_k$ depends on a set of variables $V_k$, then

$$
V_k \subset V_{k+1}
$$

and the utility function changes from

$$
U_k : S_k \to \mathbb{R}
$$

to a more complex

$$
U_{k+1} : S_{k+1} \to \mathbb{R}
$$

where $U_{k+1}$ incorporates additional dimensions or factors not captured by $U_k$.

As $k \to n$, the accessible option set $S_k$ approaches the global option space:

$$
\lim_{k \to n} S_k = \mathcal{G}
$$

and the utility function $U_k$ converges toward the full global utility

$$
\lim_{k \to n} U_k = U : \mathcal{G} \to \mathbb{R}
$$

which accounts for **all** relevant variables and trade-offs.

**Example:**

+ In personal finance, an individual at a subsistence level $L_0$ might treat time and money as roughly interchangeable
  variables within $S_0$, with a simple utility function $U_0$. But at higher economic levels $L_k$, additional variables such
  as *opportunity cost*, *compound interest*, and *strategic investment* enter the utility calculation, increasing the
  dimensionality of $V_k$ and complexity of $U_k$.

This ties back to the central illusion: what once felt like a flat, well-understood utility landscape was just a **2D slice** of a higher-dimensional topology, one that only reveals its depth at higher levels of access.

In this light, hierarchies do not just expand what you can do: they **transform what matters**.

## Moral
Understanding hierarchies as structures of access helps clarify how growth and progression work in complex systems. Each level represents a meaningful threshold, once crossed, it expands the total set of options available without revoking previous ones. Advancement depends not just on time or effort, but on satisfying specific requirements appropriate to the domain.

This framework is broadly applicable: from skill development and education to software permissions and institutional roles. It highlights how systems can be designed to guide progression in a structured, cumulative, and meaningful way, ensuring that with each step forward, the landscape of possibility expands.
