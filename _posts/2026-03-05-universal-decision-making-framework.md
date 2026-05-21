---
layout: article
title: Towards a Universal Framework for Decision-Making
custom_css: article.css
include_mathjax: true
---
## Introduction
Decision-making — whether in games, business, or everyday life — is often treated as a process of choosing between discrete, isolated actions. In Chess or Go, we imagine moving a single piece toward a goal. In business, we think in terms of tackling one project or opportunity at a time. While this simplification is useful, it obscures the deeper structure that governs strategic success: the interplay between an agent’s current state, the options available, and the evolution of those states over time.

At the heart of every decision lies **position**: the agent’s state vector $P = [p_1, p_2, \dots, p_n]$, which encodes the resources, capabilities, knowledge, and contextual factors relevant to that agent. In games, position might be the arrangement of pieces on a board; in business, it could combine capital, stability, and skill; in life more broadly, it spans finances, health, social networks, and knowledge. Crucially, a high-quality position is not defined solely by immediate advantage. It is one that **increases access to desirable future outcomes while reducing exposure to undesirable ones**. Unlike classical “system-centered” game trees, which enumerate all players’ possible moves, this framework focuses on the **agent-centered structure of reachable futures**, projecting the global system onto the state space relevant to the decision-maker.

Complementing position is the concept of a **move**. Traditional thinking treats moves as atomic actions — a pawn advances, a knight attacks, a new business venture is launched. In complex environments, however, moves are better understood as **structured transformations of position**, potentially affecting multiple dimensions simultaneously. A single move may alter resources, constraints, capabilities, and strategic structure at once. Moves therefore do not merely produce immediate effects; they transform one position into another, reshaping the set of future states that become reachable under the rules of the system.

This perspective naturally leads to **mixed strategies**. Rather than committing entirely to a single action, an agent may distribute effort or resources across multiple structured transformations. Such allocation can improve the structural quality of the resulting position by balancing exposure and opportunity, preserving flexibility, and expanding access to valuable outcomes. In Chess, controlling the center does not merely improve an immediate tactical situation; it increases structural influence over future possibilities while constraining the opponent’s options. In broader domains, diversified effort can similarly strengthen long-term positioning by improving the structure of reachable successes and limiting paths to failure.

In this article, we propose a generalized framework for reasoning about decision-making across domains. Positions are represented as multi-dimensional vectors encoding the agent’s state. Moves are treated as structured transformations of those vectors. Utility is defined in terms of the relationship between positions and the valued terminal outcomes of the system. Mixed strategies arise as a natural consequence of optimizing this structural relationship under constraints.

By formalizing the relationship between position, transformation, and the structure of reachable futures relative to terminal goals, we lay the foundation for a unified approach to rational action in complex systems — one that accounts for advantage and threat, growth and robustness, across multiple dimensions of strategy, even under imperfect information.

## Game Structure and Terminal Value
Before we can reason rigorously about positions, transformations, and strategies, we must define the environment in which an agent operates and what constitutes success. In this framework, a strategic environment is abstracted as a **game**, which formalizes the possible states of the system, the available actions at each state, the rules governing transitions, and the terminal outcomes that are valued by the agent. By establishing this foundation, we can later define positions as projections of states onto the agent’s accessible and controllable space, and evaluate moves in terms of how they reshape the structure of reachable futures relative to valued outcomes.

Formally, a game is defined as:

$$
\mathcal{G} = (\mathcal{S}, \mathcal{A}, f, \mathcal{S}_T, V)
$$

where:

### State Space

$$
\mathcal{S}
$$

is the set of all admissible system states under the rules of the game. Each state represents a complete configuration permitted by the system’s dynamics.

### Action Structure
For each state $s \in \mathcal{S}$, there exists a set of allowed actions:

$$
\mathcal{A}(s)
$$

These actions define the legally available transformations from that state.

### Transition Function

$$
f : \mathcal{S} \times \mathcal{A} \rightarrow \mathcal{S}
$$

The transition function specifies how the system evolves:

$$
s' = f(s, a)
$$

This determines the structural dynamics of the game. No assumptions about randomness are required at this level — the framework accommodates both deterministic and adversarial dynamics.

### Terminal States

$$
\mathcal{S}_T \subseteq \mathcal{S}
$$

Terminal states are states in which the game ends. Once a terminal state is reached, no further actions are possible. These states represent the completed outcomes of the system, whether success, failure, or a neutral resolution.

### Terminal Value Function
Strategic reasoning requires a goal structure. This is encoded via a **terminal value function**:

$$
V : \mathcal{S}_T \rightarrow \mathbb{R}
$$

which assigns a real-valued evaluation to each terminal state. The value function formalizes what constitutes success or failure in the game, providing the objective against which positions, moves, and strategies can be measured.

## Position and Reachability
With the game structure formalized, we now shift focus from the global system to the **agent’s perspective**. While the game defines all possible states and transitions, an agent rarely has access to the full system state, nor can it act on all aspects simultaneously. What matters for strategic reasoning is the **position** — the subset of state information that is both **observable and controllable**, and that captures the agent’s capacity to influence outcomes.

### Position
A **position** is the agent-centered representation of the current state:

$$
P = [p_1, p_2, \dots, p_n]
$$

This vector encodes all dimensions relevant to decision-making, such as:

* resources and assets
* constraints and commitments
* capabilities and skills
* knowledge and information
* environmental/contextual factors that can be acted upon

Key points:

* $P$ is generally a **projection** of the full system state $s \in \mathcal{S}$ onto the agent’s actionable and informational subspace.
* It represents the **structurally relevant** aspects of the system for strategic choice.
* The position defines the agent’s **location within the game’s state space**, establishing a concrete basis for evaluating moves and strategies.

### Reachability
Given a position $P$, the game rules determine which terminal states are structurally attainable through valid sequences of actions. This set, called the **reachability set**, is defined as:

$$
\mathcal{R}(P) \subseteq \mathcal{S}_T
$$

$\mathcal{R}(P)$ contains all terminal states that can be reached starting from $P$, assuming only the structural constraints of the game.

Crucially:

* Reachability is **deterministic and structural** — it depends solely on the transition function $f$, the action sets $\mathcal{A}(s)$, and the current position.
* No probabilistic assumptions are introduced at this stage. The set captures **what is possible**, not how likely it is.

The position $P$ therefore determines reachability $\mathcal{R}(P)$, which in turn determines which terminal values are accessible via the value function $V$:

$$
P \rightarrow \mathcal{R}(P) \rightarrow V(\mathcal{R}(P))
$$

This chain establishes the foundation for evaluating strategic quality: any subsequent measure of **advantage, threat, path diversity, or utility** will be defined in terms of the reachable terminal states, effectively translating the global game structure into the agent-relevant decision space.

## Advantage, Threat, and Path Structure
Having defined **position** $P$ and its **reachability set**

$$
\mathcal{R}(P) \subseteq \mathcal{S}_T,
$$

we now turn to **evaluating the strategic quality of a position**. While reachability tells us which terminal states are structurally accessible, not all outcomes are equally desirable. The structure of $\mathcal{R}(P)$ — which states can be reached and by how many distinct paths — determines the **advantage, risk, and robustness** of the agent’s current state.

### Advantage
Define the set of structurally **desirable terminal states**:

$$
O^+(P) = { o \in \mathcal{R}(P) : V(o) > 0 }.
$$

The **advantage** of position $P$ is the total accessible positive value:

$$
A(P) = \sum_{o \in O^+(P)} V(o).
$$

Advantage quantifies **how much desirable terminal value the position makes structurally available**, independent of any probabilities. It captures **accessibility**, not likelihood.

### Threat
Similarly, define the set of structurally **undesirable terminal states**:

$$
O^-(P) = { o \in \mathcal{R}(P) : V(o) < 0 }.
$$

The **threat exposure** of position $P$ is:

$$
T(P) = \sum_{o \in O^-(P)} |V(o)|.
$$

Threat measures the total magnitude of negative terminal value reachable from the position. Reducing threat corresponds to structurally eliminating access to harmful outcomes.

### Path Structure
Terminal values alone do not fully capture **strategic robustness**. A position with many distinct ways to reach success is stronger than one where only a single precise sequence leads to a positive outcome.

Let

$$
\Pi(P) = {\pi_1, \pi_2, \dots, \pi_k}
$$

be the set of all **valid continuation paths** from $P$ to terminal states, with each path terminating in

$$
o(\pi_j) \in \mathcal{R}(P).
$$

Partition paths according to outcome value:

$$
\Pi^+(P) = { \pi \in \Pi(P) : V(o(\pi)) > 0 },
\quad
\Pi^-(P) = { \pi \in \Pi(P) : V(o(\pi)) < 0 }.
$$

### Structural Diversity
To measure robustness and fragility, define the **structural diversity of paths**:

$$
D^+(P) = \log |\Pi^+(P)|,
\quad
D^-(P) = \log |\Pi^-(P)|.
$$

* $D^+(P)$ counts how many **distinct structural paths lead to success**.
* $D^-(P)$ counts how many **distinct paths lead to failure**.

A strong position simultaneously **increases $D^+$ while reducing $D^-$**, capturing robustness purely in terms of the game’s structure.

### Unified Position Utility
Combining all components, we define the **scalar utility** of a position:

$$
U(P) = A(P) - T(P) + D^+(P) - D^-(P).
$$

This function encodes:

* access to positive terminal value ($A(P)$)
* exposure to negative terminal value ($T(P)$)
* structural richness of success paths ($D^+(P)$)
* structural fragility of failure paths ($D^-(P)$)

$U(P)$ provides a complete **ranking of positions** purely from structural considerations, forming the evaluative machinery that underlies all subsequent strategy analysis.

## Strategies and Position Transformation
Up to now, we have formalized **how positions are evaluated**: we know the game structure, the agent’s position $P$, the reachable terminal states $\mathcal{R}(P)$, and the components of position utility $U(P)$.

The next question is: **how does an agent actively change its position?** Evaluating positions is only part of the story. Strategic intelligence lies in selecting actions — or more generally, **allocations of effort and resources** — that transform the current state into a more favorable one.

### Strategy as Structured Allocation
In complex environments, actions are rarely isolated atomic events. Agents must allocate **limited resources** — time, attention, capital, effort — across multiple actions and dimensions simultaneously.

A **strategy** is therefore a structured allocation of resources:

$$
S
$$

which specifies how resources are distributed across available actions.

In matrix form:

$$
S =
\begin{bmatrix}
s_{1,1} & \dots & s_{1,m} \\
\vdots & \ddots & \vdots \\
s_{n,1} & \dots & s_{n,m}
\end{bmatrix}
$$

* rows correspond to dimensions of the position vector $P = [p_1, \dots, p_n]$
* columns correspond to available actions
* entries $s_{i,j}$ represent the fraction of resources allocated to action $j$ affecting dimension $i$

This representation generalizes the concept of a move to a **multi-dimensional, multi-channel allocation of effort**.

### Pure (Atomic) Strategy as a Degenerate Case
Classical atomic moves are a **special case of strategy**, where all resources are concentrated in a single action along a single dimension. For example:

$$
S_{\text{pure}} =
\begin{bmatrix}
0 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 0
\end{bmatrix}
$$

Or, more generally:

$$
S_{\text{pure}} = e_{i,j},
$$

where $e_{i,j}$ is a matrix with a single nonzero entry.

> Pure moves are **degenerate strategies** — they represent extreme concentration of resources.

### General (Mixed) Strategy
In contrast, a **mixed strategy** spreads resources across multiple actions and dimensions:

$$
S_{\text{mixed}} =
\begin{bmatrix}
0.4 & 0.2 & 0 \\
0.1 & 0 & 0 \\
0.3 & 0 & 0
\end{bmatrix}
$$

Here, the agent allocates effort in a coordinated, multi-dimensional manner, **reshaping multiple aspects of its position simultaneously**.

Mixed strategies are not optional; in complex environments, they are **structurally necessary** to manipulate the future space effectively.

### Strategy-Induced Transformation
Given a position $P$ and strategy $S$, the environment produces a new position:

$$
P' = f(P, S).
$$

The function $f$ encodes:

* game rules
* interactions between dimensions
* structural constraints
* deterministic or adversarial system dynamics

This transformation **formalizes how resource allocation reshapes the agent’s state**.

### Effect on Reachability Structure
Since utility depends on the reachable terminal states:

$$
\mathcal{R}(P),
$$

applying a strategy modifies the reachability set:

$$
\mathcal{R}(P) \rightarrow \mathcal{R}(P').
$$

Consequently, strategy indirectly reorganizes:

* advantage $A(P)$
* threat $T(P)$
* success diversity $D^+(P)$
* failure diversity $D^-(P)$
* overall utility $U(P)$

In this sense, **strategy is the mechanism through which the agent reshapes the space of future possibilities**, not merely the immediate payoff.

### Strategic Optimization
The rational objective is to select the strategy that maximizes the resulting position’s utility:

$$
U(P) = A(P) - T(P) + D^+(P) - D^-(P),
$$

yielding the **optimal strategy**:

$$
S^* = \arg\max_S U(f(P, S)).
$$

If the environment has stochastic elements, an expectation operator can be included, but in deterministic settings, the formula above suffices.

Optimal strategy therefore corresponds to the **resource allocation that most effectively restructures reachable futures** toward desirable outcomes while constraining undesirable ones.

## Applications in Chess & Go
We now illustrate how the framework can be applied in practice. The purpose of these examples are not to compute the utility function

$$
U(P) = A(P) - T(P) + D^+(P) - D^-(P)
$$

exactly, since such quantities are generally not tractable in complex games. Instead, the goal is to demonstrate how the framework can be used to reason about competing strategic transformations of a position by analyzing how candidate moves reshape the structure of reachable futures.

In practical decision-making environments, many legal actions are typically available. However, only a small subset correspond to coherent structural transformations of the current position. The framework therefore acts primarily as a method for comparing strategically meaningful transformations rather than exhaustively evaluating all possible actions.

### Chess Example
**Figure 1** below shows the following initial [FEN](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) Chess position:

```
r2q1rk1/pp2bppp/2np1n2/2p1p3/2P1P3/2NP1NP1/PP2PPBP/R1BQ1RK1 w - - 0 1
```

*White* to move.


    
![png](/assets/images/2026-03-05-universal-decision-making-framework_files/2026-03-05-universal-decision-making-framework_8_0.png)
    


This is a quiet but strategically rich middlegame position. There are no immediate tactical combinations, but several natural plans are available.

A strong human player would likely consider moves such as:

| Move      | Strategic Idea                                               |
| --------- | ------------------------------------------------------------ |
| `h3`      | reduce tactical pressure and secure kingside structure       |
| `Rb1`     | begin queenside expansion and pressure the b-file            |
| `Nd2`     | improve coordination and prepare central/queenside expansion |

The question is:

> Which transformation of the position makes the most structural sense?


    
![png](/assets/images/2026-03-05-universal-decision-making-framework_files/2026-03-05-universal-decision-making-framework_10_0.png)
    


**Figure 2** shows the move:

> h3

Its purpose is straightforward:

* prevent future piece intrusion on `g4`
* slightly improve king safety
* reduce tactical volatility

Structurally:

* threat exposure decreases slightly
* positional stability improves
* White’s active possibilities do not meaningfully expand

In terms of the framework:

* $T(P)$ improves modestly,
* $A(P)$ and $D^+(P)$ change very little.

This is a safe move, but also somewhat passive. It improves the position defensively without significantly increasing White’s future opportunity structure.


    
![png](/assets/images/2026-03-05-universal-decision-making-framework_files/2026-03-05-universal-decision-making-framework_12_0.png)
    


**Figure 3** shows the move:

> Rb1

which is more active in comparison to `h3`.

The idea is to:

* pressure the queenside
* prepare potential b-pawn expansion
* increase rook activity

This move expands White’s future options and creates additional long-term pressure channels.

Structurally:

* $D^+(P)$ increases
* White gains additional strategic continuations
* $A(P)$ improves slightly through increased activity

However, the move does little to improve central coordination immediately, and Black’s counterplay structure remains largely intact.

So while the move increases future opportunity, it does not strongly restrict the opponent.


    
![png](/assets/images/2026-03-05-universal-decision-making-framework_files/2026-03-05-universal-decision-making-framework_14_0.png)
    


**Figure 4** shows the move:

> Nd2

which is less flashy, but structurally deeper.

The knight improves coordination between White’s pieces and supports several future plans simultaneously:

* central expansion via `e4` or `c5` pressure
* queenside expansion
* reinforcement of key central squares
* and potential rerouting toward `c4` or `e4`

At the same time, the move reduces structural weaknesses by improving piece harmony and limiting Black’s future activity.

Unlike the previous candidates, this move improves multiple dimensions of the position simultaneously.

Structurally:

* $A(P)$ improves through increased future central and queenside opportunities
* $D^+(P)$ increases because White’s continuation structure becomes richer
* $T(P)$ decreases slightly due to improved coordination
* Black’s counterplay remains constrained

### Structural Comparison
The important point is that none of these moves are “bad.” Each corresponds to a coherent strategic transformation.

However, they differ in *how broadly* they improve the structure of reachable futures.

| Move  | Primary Effect                            |
| ----- | ----------------------------------------- |
| `h3`  | stabilization                             |
| `Rb1` | expansion of future activity              |
| `Nd2` | coordinated multi-dimensional improvement |

The framework therefore favors `Nd2`, not because it wins material or creates an immediate tactic, but because it produces the most coherent overall transformation of the position.

In particular, `Nd2`:

* improves future flexibility
* strengthens coordination
* preserves structural stability
* supports multiple future plans
* restricts the opponent’s ability to generate active counterplay

Thus, although the utility function

$$
U(P) = A(P) - T(P) + D^+(P) - D^-(P)
$$

cannot be computed exactly, the framework still allows meaningful comparative reasoning about which transformation most effectively improves the structure of reachable futures.

That is the central idea of the framework:

> strategic decisions are evaluated not only by immediate effects, but by how they reshape the geometry of future possibility.

### Go Example
We now consider a similar example in Go. As in the Chess example, the purpose is not to numerically evaluate the utility function

$$
U(P) = A(P) - T(P) + D^+(P) - D^-(P)
$$

but rather to demonstrate how the framework can organize strategic reasoning about competing positional transformations.

Go is particularly well suited to this interpretation because strategic play frequently revolves around:

* expansion of influence
* restriction of opponent development
* stabilization of territory
* management of future flexibility

These concepts correspond naturally to the structural components of the framework.

*Black* to move.


    
![png](/assets/images/2026-03-05-universal-decision-making-framework_files/2026-03-05-universal-decision-making-framework_18_0.png)
    


The position shown in **Figure 5** is strategically open. Both players possess developing influence structures, but much of the board remains unresolved.

Black currently has stronger influence toward the left-center region, while White possesses developing influence on the right side. Several reasonable strategic continuations are available.

In particular, Black may choose to:

1. aggressively expand central influence
2. directly restrict White’s future development
3. consolidate existing territorial structure

We now examine one representative move from each strategic direction.


    
![png](/assets/images/2026-03-05-universal-decision-making-framework_files/2026-03-05-universal-decision-making-framework_20_0.png)
    


**Figure 6** shows the expanding move at `((3,4))`.

This move strengthens Black’s central influence and increases future development potential toward the middle of the board. The move is active and flexible, preserving multiple future continuations.

Structurally, the move:

* enlarges Black’s future territorial framework
* improves connectivity between existing stones
* increases future attacking and expansion opportunities

Within the framework, this transformation primarily improves:

$$
A(P)
\quad\text{and}\quad
D^+(P)
$$

by increasing Black’s future positional flexibility and influence potential.

However, the move does not directly interfere with White’s existing developmental structure.


    
![png](/assets/images/2026-03-05-universal-decision-making-framework_files/2026-03-05-universal-decision-making-framework_22_0.png)
    


**Figure 7** shows the restricting move at `((5,5))`.

Rather than purely expanding Black’s own influence, this move directly interferes with White’s future development on the right side of the board.

Structurally, the move:

* limits White’s future territorial expansion
* reduces White’s ability to form a large connected framework
* constrains future invasion and reduction opportunities
* while still maintaining Black’s own flexibility

Within the framework, this transformation primarily acts on:

$$
D^-(P)
$$

by reducing the diversity and effectiveness of favorable continuations available to the opponent.

At the same time, the move also preserves substantial future development potential for Black.


    
![png](/assets/images/2026-03-05-universal-decision-making-framework_files/2026-03-05-universal-decision-making-framework_24_0.png)
    


**Figure 8** shows the consolidating move at `((1,2))`.

This move reinforces Black’s existing territorial structure on the left side and reduces future invasion risk. Unlike the previous candidates, it does not aggressively seek expansion or confrontation.

Structurally, the move:

* improves local stability
* secures existing territory
* reduces future vulnerability
* does little to influence the broader balance of the board

Within the framework, this transformation primarily improves:

$$
T(P)
$$

by reducing the likelihood of future destabilization or invasion.

However, the move is comparatively passive and leaves White’s broader development potential largely unchanged.

### Structural Comparison
All three candidate moves correspond to coherent strategic transformations of the position.

However, they differ in the overall quality of the future structures they create.

| Move    | Primary Structural Effect              |
| ------- | -------------------------------------- |
| ((3,4)) | expansion of influence and flexibility |
| ((5,5)) | restriction of opponent development    |
| ((1,2)) | territorial stabilization              |

Among these candidates, the move at `((5,5))` appears structurally strongest.

Unlike the purely expanding move, it simultaneously:

* develops Black’s influence
* constrains White’s future framework
* preserves future flexibility
* limits the White’s future continuation structure

The move therefore improves multiple structural dimensions at once while avoiding significant positional concessions.

The framework thus favors this move not because of immediate tactical gain, but because it most coherently reshapes the structure of reachable futures in Black’s favor.

As in the Chess example, the framework does not mechanically compute an optimal action. Rather, it provides a structured method for comparing how competing transformations reorganize future positional possibilities.

## Conclusion
This article has developed a structural framework for decision-making grounded in the relationship between positions, transformations, and reachable futures in a game-theoretic environment.

We began by defining a game $\mathcal{G} = (\mathcal{S}, \mathcal{A}, f, \mathcal{S}_T, V)$, which formalizes the space of admissible states, the available actions, the transition dynamics, and the terminal evaluation of outcomes. Within this structure, we introduced the notion of a **position** $P$ as an agent-centered projection of the full system state, capturing only those dimensions relevant to action and evaluation.

From this foundation, we defined **reachability** $\mathcal{R}(P)$, characterizing the set of terminal outcomes accessible from a given position. This allowed us to shift focus from isolated actions to the structure of future possibilities induced by a position.

We then introduced a decomposition of positional quality into four structural components:

* $A(P)$: accessible positive terminal value (i.e. *advantage*)
* $T(P)$: exposure to negative terminal value (i.e. *threat*)
* $D^+(P)$: structural diversity of successful continuations
* $D^-(P)$: structural diversity of failing continuations

Together, these define a scalar utility function:

$$
U(P) = A(P) - T(P) + D^+(P) - D^-(P),
$$

which serves not as a probabilistic expectation, but as a structural ordering over positions based on the geometry of their reachable futures.

We further extended the framework to **strategies**, defined as structured allocations of effort or resources that induce transformations of position. Rather than treating moves as atomic actions, strategies were formalized as transformations:

$$
P' = f(P, S),
$$

allowing us to interpret decision-making as the selection of transformations that reshape the structure of reachable outcomes.

### Core Insight
The central contribution of this framework is the shift in perspective from *action selection* to *structure transformation*. Decisions are not evaluated primarily by immediate outcomes, but by how they reorganize the space of future possibilities.

Under this view:

* advantage $A(P)$ corresponds to the expansion of accessible favorable futures
* threat $T(P)$ corresponds to exposure to undesirable terminal outcomes
* and structural diversity $D^+(P)$ and $D^-(P)$ capture the robustness or fragility of a position’s continuation space

Importantly, these quantities are defined independently of probability. They describe what is *structurally available*, not what is *likely to occur*.

### Implications
This formulation provides a unified language for reasoning about strategy across domains such as games, economics, and sequential decision problems. By grounding evaluation in reachability structure rather than outcome prediction, it becomes possible to compare decisions based on how they reshape the topology of future states.

This perspective also naturally explains why effective strategies often prioritize:

* restricting an opponent’s viable continuation space
* preserving flexibility in one’s own position
* increasing the number of structurally distinct paths to favorable outcomes

### Closing Statement
Rather than treating decision-making as a sequence of isolated choices, this framework models it as the evolution of a structured state space under transformation. In doing so, it provides a basis for analyzing strategy in terms of geometry, constraint, and reachability, offering a structural alternative to purely probabilistic or heuristic approaches to rational action.
