---
layout: article
title: Foreign Environment Access
custom_css: article.css
include_mathjax: true
publish: true
---
## Introduction
An agent does not necessarily need to change its current environment in order to benefit from another environment. It may instead seek to establish a relationship with an environment that it does not currently occupy.

This possibility creates a particular problem within the broader environment problem. An agent may exist within an environment $E_0$ while other environments $E_1,E_2,\ldots,E_n$ remain outside its current reach. The question is therefore not simply how an agent acts within its environment, but what actions it can perform with respect to environments beyond the one it currently occupies.

Consider an agent in $E_0$ that acquires property in $E_1$ without physically entering $E_1$. The agent has established a relationship with $E_1$ even though it has not changed its current environment. Similarly, an agent may be able to enter an environment without being able to reside there, reside there without being able to work there, or conduct activities within an environment without maintaining a physical presence there.

These cases suggest that environmental access cannot be defined solely in terms of physical presence or entry. An agent may have access to an environment through actions that can be performed locally or remotely and that establish different relationships with that environment.

This raises a fundamental question:

> **What does it mean for an agent to have access to a foreign environment?**

A useful starting point is to consider the actions available to the agent with respect to an environment. Let

$$
\mathcal{A}_E(P)
$$

denote the set of actions available to an agent at position $P$ with respect to environment $E$.

Under this representation, access is not initially treated as a single binary property. It is expressed through the actions that the agent is able to perform with respect to an environment. An agent may therefore have access to an environment through one action while lacking access through another:

$$
a_1\in\mathcal{A}_E(P)
\quad\text{while}\quad
a_2\notin\mathcal{A}_E(P).
$$

An agent may, for example, be able to enter an environment without being able to reside there, acquire property without being able to reside in that property, or conduct an economic transaction without being able to establish a continuing presence.

The conditions governing these actions can differ substantially between environments and between agents. Access may depend on legal authorization, financial resources, physical mobility, knowledge, relationships, time, or other properties of the agent and its circumstances. The relative importance of these conditions cannot, however, be assumed in advance. They must be identified by examining the mechanisms through which particular actions become possible.

This also means that access can change when the agent's position changes. If an agent acquires a condition necessary to perform an action with respect to an environment, then an action that was previously unavailable may become available:

$$
a\notin\mathcal{A}_E(P_t)
\quad\rightarrow\quad
a\in\mathcal{A}_E(P_{t+1}).
$$

The importance of this change is that the newly available action may create positions that were not previously reachable. Thus, if

$$
a\in\mathcal{A}_E(P),
$$

then the environment has become relevant to the agent's decision space through the action $a$.

Foreign environmental access therefore provides a concrete setting in which to investigate a broader question from the environment problem:

$$
\text{How does access to an environment change the actions available to an agent?}
$$

and, consequently,

$$
\text{How do those additional actions change the positions reachable by the agent?}
$$

This question is particularly important because the agent need not physically occupy the foreign environment for such a change to occur. An agent may remain in $E_0$ while acquiring the ability to perform actions with respect to $E_1$. Its current physical environment can therefore remain unchanged while its available actions, and potentially its reachable positions, change.

The problem becomes even more interesting when an agent can maintain relationships with multiple environments simultaneously. An agent may occupy $E_0$ while possessing different sets of available actions with respect to $E_1$ and $E_2$:

$$
\mathcal{A}_{E_1}(P)
\neq
\mathcal{A}_{E_2}(P).
$$

Its environmental circumstances are therefore not determined solely by the environment it currently occupies. They may also depend on the actions it can perform with respect to environments outside its current one.

The objective of this investigation is consequently not to define a final representation of environmental access in advance. It is to examine concrete cases of foreign environmental access, identify the mechanisms that make particular actions possible, and determine whether those mechanisms reveal a systematic relationship between environmental access, available actions, and the positions reachable by an agent.

The investigation therefore begins with a working hypothesis: **access to a foreign environment can be examined through the actions an agent is able to perform with respect to that environment.**


## The Foreign Environment
An agent operates within some current environment $E_0$. Other environments may exist outside of the environment the agent currently occupies:

$$
E_0,E_1,E_2,\ldots,E_n.
$$

The distinction between these environments is not necessarily geographic or political. A foreign environment is simply an environment that is not the agent's current environment.

This distinction matters because an agent may interact with an environment without occupying it. An agent located in $E_0$ may own property in $E_1$, exchange resources with agents in $E_1$, communicate with institutions in $E_1$, or perform other actions with respect to $E_1$ while remaining physically within $E_0$.

Thus,

$$
\text{current environment}\neq\text{all environments with which the agent can interact}.
$$

The agent's relationship to $E_1$ may therefore extend beyond physical presence.

Consider an agent in $E_0$ and a foreign environment $E_1$. The agent may initially have no actions available with respect to $E_1$:

$$
\mathcal{A}_{E_1}(P)=\varnothing.
$$

A change in the agent's position may then make one or more actions available:

$$
\mathcal{A}_{E_1}(P')
=
\{a_1,a_2,\ldots\}.
$$

The important question is not simply whether the agent has entered $E_1$. The question is whether the agent has acquired the ability to perform actions with respect to $E_1$ that were previously unavailable.

For example, physical entry may be one such action:

$$
a_{\mathrm{enter}}\in\mathcal{A}_{E_1}(P).
$$

But an agent may also acquire property in $E_1$ without entering it:

$$
a_{\mathrm{purchase}}\in\mathcal{A}_{E_1}(P).
$$

The two actions establish different relationships with the same environment. Neither therefore provides a complete representation of what it means to have access to $E_1$.

This suggests that the relevant object of analysis is not simply the boundary between the agent and the foreign environment. It is the set of relationships the agent can establish with that environment through available actions.

For two foreign environments $E_1$ and $E_2$, the available actions may differ:

$$
\mathcal{A}_{E_1}(P)
\neq
\mathcal{A}_{E_2}(P).
$$

An agent may therefore have different relationships with different environments while occupying only one of them.

The same environment may also present different possibilities to different agents. If agents $A_1$ and $A_2$ occupy positions $P_1$ and $P_2$, then

$$
\mathcal{A}_{E}(P_1)
\neq
\mathcal{A}_{E}(P_2)
$$

may hold even when both agents are outside $E$.

Foreign environmental access is therefore relational. It depends not only on the environment itself, but on the position of the agent relative to that environment.

This gives us the basic structure of the problem:

$$
P
\rightarrow
\mathcal{A}_E(P)
\rightarrow
\text{relationship with }E.
$$

The investigation can therefore proceed without assuming that access means entry, residence, ownership, or any other particular relationship. Instead, these are concrete cases through which the structure of foreign environmental access can be examined.

The next question is therefore what the available actions themselves tell us about access to a foreign environment.


## Access as Action
If a foreign environment is an environment outside the one an agent currently occupies, then access to that environment must describe some relationship between the agent and that environment.

The simplest way to examine that relationship is through the actions available to the agent.

Let

$$
\mathcal{A}_E(P)
$$

denote the set of actions available to an agent at position $P$ with respect to environment $E$.

Under this representation, access is not initially a binary property. Instead, it is expressed through the actions that an agent can perform with respect to an environment.

Consider an agent in $E_0$ and a foreign environment $E_1$. The agent may be unable to enter $E_1$:

$$
a_{\mathrm{enter}}\notin\mathcal{A}_{E_1}(P).
$$

Yet the same agent may be able to perform another action with respect to $E_1$:

$$
a_{\mathrm{purchase}}\in\mathcal{A}_{E_1}(P).
$$

The agent therefore has some ability to act with respect to $E_1$ despite remaining outside it.

Physical presence is consequently not a necessary condition for an action to be available with respect to an environment:

$$
\text{physical presence}
\neq
\text{ability to act with respect to }E.
$$

The same distinction appears when considering different forms of physical access. An agent may be able to enter an environment without being able to reside there:

$$
a_{\mathrm{enter}}\in\mathcal{A}_E(P)
\quad\text{while}\quad
a_{\mathrm{reside}}\notin\mathcal{A}_E(P).
$$

It may be able to reside there without being able to work there:

$$
a_{\mathrm{reside}}\in\mathcal{A}_E(P)
\quad\text{while}\quad
a_{\mathrm{work}}\notin\mathcal{A}_E(P).
$$

Or it may be able to acquire property without being able to establish a physical presence:

$$
a_{\mathrm{purchase}}\in\mathcal{A}_E(P)
\quad\text{while}\quad
a_{\mathrm{enter}}\notin\mathcal{A}_E(P).
$$

These cases suggest that access is not naturally represented as a single yes-or-no condition. An agent can have one form of access to an environment while lacking another.

We can therefore represent access through the set

$$
\mathcal{A}_E(P)
=
\{a_1,a_2,\ldots,a_n\}.
$$

The contents of this set depend on both the environment and the agent's position. Thus,

$$
\mathcal{A}_{E_1}(P)
\neq
\mathcal{A}_{E_2}(P)
$$

may hold for two different environments, while

$$
\mathcal{A}_E(P_1)
\neq
\mathcal{A}_E(P_2)
$$

may hold for two different positions relative to the same environment.

This is important because the actions available with respect to an environment are not properties of the environment alone. They arise from the relationship between the agent, its position, and the environment.

The distinction between **available** and **performed** actions is also important. If

$$
a\in\mathcal{A}_E(P),
$$

then $a$ is available to the agent. It does not follow that the agent performs $a$.

An agent may therefore possess the ability to enter an environment without entering it, possess the ability to acquire property without acquiring it, or possess the ability to work without actually working.

Access concerns the possibility of action, not the exercise of that possibility.

This gives us a useful working representation:

$$
\boxed{
\text{Access to }E
=
\text{the actions available to an agent with respect to }E
}
$$

The representation is deliberately provisional. It does not claim that every possible action should be treated as an equivalent form of access, nor does it establish that access itself is a dimension of position.

It gives us something more useful at this stage: a way to examine the problem.

If a change in the agent's position causes an action with respect to $E$ to become available, then

$$
a\notin\mathcal{A}_E(P_t)
\quad\rightarrow\quad
a\in\mathcal{A}_E(P_{t+1}).
$$

The foreign environment has therefore become relevant to the agent's decision space even though the agent may remain outside that environment.

The next question is whether these newly available actions merely expand the agent's immediate choices or whether they change the set of positions the agent can ultimately reach.


## Access and Reachable Positions

The significance of access is not simply that it gives an agent more actions. The more important question is what those actions make possible.

Let the set of positions reachable from $P$ under the available actions be

$$
\mathcal{R}(P)
=
\left\{
F(P,a)
\mid
a\in\mathcal{A}(P)
\right\}.
$$

Now consider a foreign environment $E$. The actions available with respect to that environment form part of the agent's available actions:

$$
\mathcal{A}_E(P)\subseteq\mathcal{A}(P).
$$

If an agent acquires access to $E$, an action that was previously unavailable may become available:

$$
a\notin\mathcal{A}_E(P_t)
\quad\rightarrow\quad
a\in\mathcal{A}_E(P_{t+1}).
$$

The important question is then whether the newly available action changes the positions that the agent can reach.

Suppose that before the change,

$$
a\notin\mathcal{A}(P_t),
$$

and after the change,

$$
a\in\mathcal{A}(P_{t+1}).
$$

The transition associated with $a$ may now be available:

$$
F(P_{t+1},a).
$$

If that transition leads to a position that was not previously reachable, then the agent's future possibilities have changed.

Formally, if

$$
F(P_{t+1},a)\notin\mathcal{R}(P_t),
$$

then the newly available action has created access to a position that could not previously be reached from $P_t$.

This is the central significance of foreign environmental access.

Consider again an agent in $E_0$ and a foreign environment $E_1$. The agent may acquire the ability to perform an action with respect to $E_1$ while remaining in $E_0$. That action may subsequently allow the agent to reach a position that was unavailable before the relationship with $E_1$ was established.

The sequence is therefore not necessarily

$$
E_0\rightarrow E_1.
$$

It may instead be

$$
P_t
\rightarrow
\mathcal{A}_{E_1}(P_t)
\rightarrow
P_{t+1}
\rightarrow
\mathcal{R}(P_{t+1}).
$$

Physical movement into the foreign environment is only one possible transition within this larger structure.

For example, an agent may acquire property in $E_1$ while remaining in $E_0$. The immediate transition does not necessarily change the agent's physical environment:

$$
E_0\rightarrow E_0.
$$

Yet the action may change the agent's position by establishing a new relationship with $E_1$:

$$
P_t\rightarrow P_{t+1}.
$$

The resulting position may then permit actions that were previously unavailable.

This reveals an important distinction. **Changing environments and changing access to environments are not necessarily the same transition.**

An agent may move from one environment to another:

$$
E_0\rightarrow E_1,
$$

but it may also remain in $E_0$ while changing the actions available with respect to $E_1$:

$$
\mathcal{A}_{E_1}(P_t)
\rightarrow
\mathcal{A}_{E_1}(P_{t+1}).
$$

The latter can therefore alter future possibilities without requiring an immediate change in the agent's current environment.

This also means that access to multiple environments can produce a larger decision space. If an agent has access to $E_1$ and $E_2$, then actions with respect to both environments may become available:

$$
\mathcal{A}_{E_1}(P)\cup\mathcal{A}_{E_2}(P)
\subseteq
\mathcal{A}(P).
$$

The resulting set of actions may permit transitions into positions that could not be reached when those environmental relationships were unavailable.

The relevant question is therefore not whether foreign environmental access is valuable in itself. It is whether access changes the structure of the agent's possible futures.

We can express the central relationship as

$$
\boxed{
\text{Access to }E
\rightarrow
\text{Available Actions}
\rightarrow
\text{Reachable Positions}
}
$$

This relationship gives us a way to analyze foreign environmental access without reducing it to physical entry, residence, ownership, or any other single form of access.

The problem is therefore to understand how an agent acquires these different forms of access, what conditions make them possible, and how changes in access alter the actions and future positions available to the agent.

## Mechanisms of Access
If access to a foreign environment can be represented through the actions available to an agent with respect to that environment, then the next question is what makes those actions available.

For an agent at position $P$, an action $a$ is available with respect to environment $E$ when the conditions necessary for performing that action are satisfied:

$$
a\in\mathcal{A}_E(P).
$$

Those conditions may arise from different properties of the agent, the environment, or the relationship between them.

Consider physical entry into an environment. The ability to enter may depend on physical mobility, transportation, authorization, or other conditions. Acquiring property may instead depend on financial resources, legal eligibility, information, and an available mechanism for completing the transaction. Establishing residence may depend on yet another set of conditions.

The mechanisms that produce access are therefore not necessarily the same for every action.

For an action $a$ with respect to environment $E$, we can represent its requirements as a set of conditions:

$$
C(a,E)=\{c_1,c_2,\ldots,c_n\}.
$$

The action is available when the relevant conditions are satisfied:

$$
C(a,E)\subseteq P.
$$

This representation should not be interpreted as saying that every condition is literally a component of the position vector. The purpose is simply to identify the conditions that must be satisfied for a particular action to become possible.

Different actions may therefore require different conditions:

$$
C(a_1,E)\neq C(a_2,E).
$$

An agent may possess everything necessary for one form of access while lacking what is necessary for another.

For example,

$$
C(a_{\mathrm{purchase}},E)
\neq
C(a_{\mathrm{reside}},E).
$$

An agent may therefore be able to purchase property in a foreign environment without being able to reside there. Likewise, an agent may be able to enter an environment without being able to work there.

The environment itself can also affect the conditions required for an action. Thus,

$$
C(a,E_1)\neq C(a,E_2)
$$

may hold even when the action $a$ is conceptually the same.

The ability to perform an economic transaction, for example, may depend on different institutional arrangements in different environments. Physical access may depend on different transportation networks. Establishing a relationship with an institution may depend on different procedures and requirements.

This gives foreign environmental access a fundamentally relational structure. The availability of an action depends on the interaction between the agent, its position, and the environment:

$$
(P,E)\rightarrow\mathcal{A}_E(P).
$$

A change in any of these conditions may therefore change the actions available to the agent.

If an agent acquires a condition required for an action, then the available action set may change:

$$
a\notin\mathcal{A}_E(P_t)
\quad\rightarrow\quad
a\in\mathcal{A}_E(P_{t+1}).
$$

Conversely, if a necessary condition is lost,

$$
a\in\mathcal{A}_E(P_t)
\quad\rightarrow\quad
a\notin\mathcal{A}_E(P_{t+1}).
$$

Access is therefore not necessarily static. It can expand or contract as the agent's circumstances change.

The mechanisms through which access changes can consequently be understood as transitions in the conditions governing available actions:

$$
C(a,E)
\rightarrow
\mathcal{A}_E(P).
$$

The practical problem is then to identify which conditions matter for the particular form of access being considered.

This is important because the same foreign environment can present very different access problems depending on what the agent is trying to do. The conditions required to visit an environment may differ from those required to live there, work there, own property there, conduct business there, or maintain a continuing relationship with it.

Foreign environmental access is therefore not one problem with one universal mechanism. It is a collection of related access problems, each defined by a particular action and the conditions required to make that action available.

The investigation can consequently proceed by examining concrete forms of access and identifying the mechanisms that make each possible.


## Forms of Foreign Environmental Access
The actions through which an agent relates to a foreign environment can take different forms. These forms should not be treated as levels of access arranged along a single scale. They represent different relationships that an agent may establish with an environment.

The most direct form is physical entry. An agent may have the ability to enter $E$:

$$
a_{\mathrm{enter}}\in\mathcal{A}_E(P).
$$

Entry establishes physical presence, but it does not necessarily establish any further relationship with the environment. An agent may be able to enter an environment while being unable to remain there for an extended period.

This gives us a distinction between entry and continued presence. Let

$$
a_{\mathrm{remain}}\in\mathcal{A}_E(P)
$$

represent the ability to remain within an environment. It is entirely possible that

$$
a_{\mathrm{enter}}\in\mathcal{A}_E(P)
\quad\text{while}\quad
a_{\mathrm{remain}}\notin\mathcal{A}_E(P).
$$

Residence represents a more specific form of continued presence. An agent may be able to establish a residence in an environment even though other actions remain unavailable.

Similarly, the ability to work within an environment constitutes another distinct form of access:

$$
a_{\mathrm{work}}\in\mathcal{A}_E(P).
$$

The ability to enter or reside in $E$ does not necessarily imply the ability to work there:

$$
a_{\mathrm{reside}}\in\mathcal{A}_E(P)
\quad\not\Rightarrow\quad
a_{\mathrm{work}}\in\mathcal{A}_E(P).
$$

Foreign environmental access can also exist without physical presence.

An agent may be able to acquire property located in $E$:

$$
a_{\mathrm{purchase}}\in\mathcal{A}_E(P).
$$

The agent may remain physically within $E_0$ while establishing a relationship with $E$ through the acquisition and control of a resource located there.

Likewise, an agent may be able to exchange resources with agents or institutions in $E$:

$$
a_{\mathrm{exchange}}\in\mathcal{A}_E(P).
$$

The agent therefore does not need to occupy $E$ in order to perform an action with respect to it.

These examples demonstrate that the forms of access are not necessarily ordered. An agent can possess one form while lacking another:

$$
a_{\mathrm{purchase}}\in\mathcal{A}_E(P)
\quad\text{while}\quad
a_{\mathrm{reside}}\notin\mathcal{A}_E(P),
$$

or

$$
a_{\mathrm{reside}}\in\mathcal{A}_E(P)
\quad\text{while}\quad
a_{\mathrm{work}}\notin\mathcal{A}_E(P).
$$

Access is therefore better represented as a collection of possible relationships than as a single quantity.

For an environment $E$, we can write:

$$
\mathcal{A}_E(P)
=
\{
a_{\mathrm{enter}},
a_{\mathrm{remain}},
a_{\mathrm{reside}},
a_{\mathrm{work}},
a_{\mathrm{purchase}},
a_{\mathrm{exchange}},
\ldots
\}.
$$

The particular elements of this set will depend on the agent, the environment, and the conditions governing each action.

This also means that two agents can have substantially different relationships with the same environment. For agents at positions $P_1$ and $P_2$,

$$
\mathcal{A}_E(P_1)
\neq
\mathcal{A}_E(P_2)
$$

may hold even though both agents are considering the same environment.

The distinction between these forms is important because each can alter the agent's possibilities in a different way. The ability to enter an environment creates different possibilities from the ability to reside there. The ability to reside creates different possibilities from the ability to work. The ability to own property or conduct transactions can create relationships with an environment without requiring physical presence at all.

The foreign environmental access problem therefore cannot be reduced to the question of whether an agent "has access" to an environment. The relevant question is:

$$
\boxed{
\text{Which actions can the agent perform with respect to }E?
}
$$

This gives us a more precise object for the remainder of the investigation. Rather than asking whether access exists, we can examine which forms of access are available, what conditions make them available, and how those forms change over time.

The next question is whether these forms of access persist once they have been established, or whether continued access requires the agent to continually satisfy the conditions that produced it.


## Persistence of Access
The availability of an action with respect to a foreign environment does not necessarily persist through time.

At position $P_t$, an agent may have access to an environment through some action:

$$
a\in\mathcal{A}_E(P_t).
$$

At a later position $P_{t+1}$, that same action may no longer be available:

$$
a\notin\mathcal{A}_E(P_{t+1}).
$$

Access can therefore change even when the environment itself has not changed.

This creates an important distinction between **acquiring access** and **maintaining access**.

An agent may acquire the ability to perform an action with respect to $E$ through some transition:

$$
P_t\rightarrow P_{t+1},
$$

such that

$$
a\notin\mathcal{A}_E(P_t)
\quad\text{and}\quad
a\in\mathcal{A}_E(P_{t+1}).
$$

The newly available action may then remain available, or it may depend on conditions that must continue to be satisfied.

For example, an agent may acquire the ability to enter an environment but possess that ability only for a limited period. Likewise, an agent may establish a residence, employment relationship, ownership relationship, or other form of access that depends on conditions continuing to hold.

The important distinction is therefore between an action becoming available and that action remaining available.

We can represent continued access as:

$$
a\in\mathcal{A}_E(P_t)
\quad\text{and}\quad
a\in\mathcal{A}_E(P_{t+1}).
$$

If the action remains available across successive positions, the relationship with the environment persists:

$$
a\in\mathcal{A}_E(P_t)
\cap
\mathcal{A}_E(P_{t+1})
\cap
\mathcal{A}_E(P_{t+2})
\cap\cdots.
$$

But persistence may require the agent to continue satisfying particular conditions.

Let

$$
C(a,E)
$$

represent the conditions associated with an action. If those conditions change through time, then the availability of the action may change with them:

$$
C_t(a,E)\rightarrow C_{t+1}(a,E).
$$

An agent may therefore need to perform additional actions to preserve access.

This produces a different type of transition:

$$
\text{Access}
\rightarrow
\text{Maintenance Action}
\rightarrow
\text{Continued Access}.
$$

Maintaining access can consequently become part of the foreign environmental access problem itself.

The same distinction applies to different forms of access. Entry may be temporary. Residence may require continued conditions. Employment may depend on an ongoing relationship. Property ownership may persist independently of physical presence. A remote relationship with an environment may therefore persist even when the agent never physically enters it.

Persistence is consequently not a property of access in general. It is a property that must be examined for each particular form of access and the conditions supporting it.

For two forms of access $a_1$ and $a_2$, it may be the case that

$$
a_1\in\mathcal{A}_E(P_t)
\quad\text{and}\quad
a_1\in\mathcal{A}_E(P_{t+1}),
$$

while

$$
a_2\in\mathcal{A}_E(P_t)
\quad\text{and}\quad
a_2\notin\mathcal{A}_E(P_{t+1}).
$$

The agent can therefore maintain one relationship with an environment while losing another.

This gives us a more complete picture of foreign environmental access. Access is not simply something that an agent either possesses or lacks. It consists of particular actions that may become available, remain available, or cease to be available as the agent's position and circumstances change.

The foreign environmental access problem therefore includes both acquisition and maintenance:

$$
\boxed{
\text{Acquire Access}
\rightarrow
\text{Maintain Access}
\rightarrow
\text{Available Actions}
}
$$

The next question is therefore how an agent should approach these competing forms of access when maintaining them consumes resources and when different environments provide different future possibilities.


## The Foreign Environmental Access Problem
The preceding sections establish that foreign environmental access is not a single condition. An agent may have different forms of access to the same environment, those forms may require different conditions, and access may need to be maintained over time.

The agent therefore faces a decision problem.

At position $P_t$, let the agent have access to a set of foreign environments:

$$
E_1,E_2,\ldots,E_n.
$$

For each environment $E_i$, the agent has some set of available actions:

$$
\mathcal{A}_{E_i}(P_t).
$$

The agent may therefore choose among actions that establish, expand, maintain, or relinquish relationships with different environments.

The difficulty is that access is not free. Acquiring an action may require resources, and maintaining that action may require additional resources over time.

Let the cost of acquiring access through action $a$ be

$$
c_{\mathrm{acquire}}(a,E),
$$

and the cost of maintaining that access be

$$
c_{\mathrm{maintain}}(a,E).
$$

An agent with limited resources cannot necessarily establish every possible relationship with every environment.

The problem is therefore not simply:

$$
\text{Which environment is best?}
$$

It is:

$$
\text{Which forms of access should the agent acquire and maintain?}
$$

This distinction becomes important when an agent can maintain relationships with multiple environments simultaneously.

Suppose the agent can establish access to $E_1$ or $E_2$. The resulting positions may differ:

$$
P_t
\xrightarrow{a_1}
P_{t+1}^{(1)}
$$

and

$$
P_t
\xrightarrow{a_2}
P_{t+1}^{(2)}.
$$

Each resulting position may then provide different actions with respect to other environments:

$$
\mathcal{A}_{E_i}(P_{t+1}^{(1)})
\neq
\mathcal{A}_{E_i}(P_{t+1}^{(2)}).
$$

An access decision can therefore affect not only the immediate relationship established with an environment, but also the subsequent access options available to the agent.

This creates the possibility of sequential access decisions.

An agent may first establish one form of access:

$$
P_t
\rightarrow
P_{t+1},
$$

which then makes another form of access available:

$$
a_2\in\mathcal{A}_E(P_{t+1}).
$$

The second action may then produce another position:

$$
P_{t+1}
\rightarrow
P_{t+2}.
$$

Foreign environmental access can therefore become a path through the agent's decision tree rather than a single decision.

The agent must also consider the possibility of losing access. If maintaining a relationship with $E$ requires continuing conditions, then failing to maintain those conditions may remove actions from the available set:

$$
a\in\mathcal{A}_E(P_t)
\quad\rightarrow\quad
a\notin\mathcal{A}_E(P_{t+1}).
$$

Maintaining access therefore has an opportunity cost. Resources devoted to preserving one environmental relationship cannot necessarily be devoted simultaneously to establishing another.

This creates a tradeoff between current access and alternative future possibilities.

An agent may consequently face a choice such as:

$$
\text{Maintain access to }E_1
\quad\text{or}\quad
\text{acquire access to }E_2.
$$

Alternatively, it may be possible to maintain both:

$$
\mathcal{A}_{E_1}(P)
\cup
\mathcal{A}_{E_2}(P).
$$

Whether this is desirable depends on the positions and future possibilities produced by those relationships.

The foreign environmental access problem can therefore be expressed as a problem of allocating resources among relationships with environments:

$$
\boxed{
\text{Acquire, maintain, expand, or relinquish access}
}
$$

subject to the conditions required for the relevant actions.

The objective is not necessarily to maximize the amount of access. More access can require more resources, and an additional form of access is useful only insofar as it changes the agent's available actions and future possibilities in a desirable way.

The problem can therefore be summarized as:

$$
\boxed{
\text{Position}
\rightarrow
\text{Access Decisions}
\rightarrow
\text{Available Actions}
\rightarrow
\text{Reachable Positions}
}
$$

The foreign environmental access problem establishes which relationships with foreign environments an agent can acquire and maintain, and how those relationships affect its available actions and reachable positions.

The next problem is to determine **which foreign environments, and which forms of access to them, are most valuable to the agent's position.**

## Conclusion
An agent's relationship with a foreign environment is not determined solely by whether it can physically enter that environment. Access consists of the actions the agent can perform with respect to it, whether those actions involve entry, residence, work, ownership, exchange, or remote interaction.

These actions depend on conditions that may differ between environments and between agents. Access may be acquired, expanded, maintained, or lost, and maintaining one form of access may consume resources that could otherwise be used to establish another.

The central problem is therefore to determine which relationships with foreign environments are worth establishing and maintaining. This cannot be decided by examining environments in isolation or by maximizing the number of available relationships. It requires examining how each form of access changes the agent's available actions, the positions those actions make reachable, and the resources required to preserve those possibilities.

Foreign environmental access is therefore a problem of choosing which relationships to establish and maintain in light of their costs, the actions they make possible, and the future positions they allow the agent to reach.
