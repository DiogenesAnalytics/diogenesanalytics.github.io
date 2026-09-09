---
layout: article
title: The Nature of Value
custom_css: article.css
include_mathjax: true
publish: true
---
## Introduction
Value is one of the most fundamental concepts in human decision-making. People value food, water, shelter, land, money, knowledge, health, relationships, opportunities, and countless other things. Some are tangible resources, some are claims on future resources, and some are entirely intangible. Yet all can influence the decisions an agent makes and the futures it seeks to reach.

Despite the ubiquity of value, its meaning is rarely stated in fundamental terms. In economics, value is often discussed through utility, scarcity, preference, exchange, or market price. In everyday life, something is valuable because someone wants it or is willing to sacrifice something to obtain it. These descriptions capture important aspects of value, but they leave a more fundamental question unanswered:

> **Why does anything have value?**

Consider a simple example. Why does a person buy food? Food has a market price, but its value cannot be explained by that price alone. The person values the food because possessing it changes what the person can do and what future states the person can reach. The same reasoning applies to water, property, money, tools, knowledge, and other resources. An object may have value because of the way possessing it changes the agent's circumstances and possibilities.

This suggests that value may not be an intrinsic property of an object at all. The same object can have different value to different agents, or even different value to the same agent at different points in time. A bottle of water may have little value to someone standing beside a river and extraordinary value to someone stranded in a desert. The physical object is essentially the same; the agent's position is not.

This observation motivates the central question of this article:

> **What is value in terms of an agent's position?**

Within the [Position framework][1], an agent's position represents the state from which its future actions and outcomes emerge. If acquiring some object, resource, capability, or opportunity changes that position, it changes the future possibilities available to the agent. The value of that thing can therefore be understood through the change it produces in the agent's position and the consequences of that change for the agent's future.

The central hypothesis of this article is that **value is fundamentally positional**. The value of something to an agent is determined by the way possessing or acquiring it changes the agent's position and, consequently, the future states available to that agent.

This perspective provides a common foundation for understanding tangible and intangible value. Food, land, money, knowledge, tools, and opportunities differ enormously in their physical and economic characteristics, yet they can all be evaluated according to the same fundamental question:

> **How does this thing change the agent's position?**

The purpose of this article is to develop this relationship formally. We will examine the connection between value and position, distinguish value from market price, and investigate how attainable future states, time, uncertainty, scarcity, and the multidimensional structure of position affect value.

The objective is not to define every concept associated with value, but to establish the more fundamental relationship on which those concepts can subsequently be built. Before concepts such as wealth, assets, and finance can be examined as distinct structures within an agent's position, we must first understand the underlying question:

> **What makes something valuable to an agent?**

[1]: https://diogenesanalytics.com/blog/2026/03/05/universal-decision-making-framework "Towards a Universal Framework for Decision-Making"

## Value and Position
Within the Position framework, an agent's position is represented by

$$
P
$$

Position is the agent-centered representation of the state relevant to decision-making. It contains the dimensions of the agent's state that determine its available actions, constraints, capabilities, and future possibilities. The position itself is distinct from its evaluation.

Let

$$
U(P)
$$

denote the utility of position $P$. Utility evaluates the position according to the structure of its reachable futures. In the [Position framework][1],

$$
U(P)=A(P)-T(P)+D^+(P)-D^-(P),
$$

where advantage, threat, and the structural diversity of favorable and unfavorable paths describe different aspects of the position's future possibilities.

Now consider some object, resource, capability, opportunity, or other feature $x$. An action involving $x$ can change the agent's position. We can represent this transformation as

$$
P'=F(P,a_x),
$$

where $a_x$ is an action through which the agent acquires, accesses, uses, or otherwise obtains some relevant relationship to $x$.

The resulting position $P'$ may differ from $P$ in one or more dimensions. The agent may possess additional resources, gain new capabilities, face different constraints, or acquire opportunities that were not previously available.

The value of $x$ is therefore not determined simply by the existence or characteristics of $x$ itself. What matters is the change in position that results from the agent's interaction with $x$. We can therefore analyze the value of $x$ by examining the resulting change in the evaluation of the agent's position.

The corresponding change in the evaluation of the position is

$$
\Delta U=U(P')-U(P),
$$

or, substituting the transition function,

$$
\boxed{
\Delta U=U(F(P,a_x))-U(P).
}
$$

If

$$
\Delta U>0,
$$

then the action involving $x$ produces an improvement in the evaluated position. If

$$
\Delta U<0,
$$

then it produces a deterioration in the evaluated position. If

$$
\Delta U=0,
$$

then it produces no change in the utility of the position.

This suggests a definition of the value of $x$ to an agent in position $P$ as the change in the utility of the agent's position resulting from the relevant action involving $x$:

$$
\boxed{
V(x\mid P)=U(F(P,a_x))-U(P).
}
$$

This definition makes value fundamentally relational. It does not treat value as an intrinsic property of $x$. Instead, it describes the change in the agent's position, and consequently the change in the evaluation of that position, produced by the agent's interaction with $x$.

Consequently, the same object may have different values to different agents. For two positions $P_A$ and $P_B$,

$$
V(x\mid P_A)\neq V(x\mid P_B)
$$

in general.

Consider water. An agent with abundant and reliable access to water may receive little additional utility from acquiring another quantity of water. An agent facing imminent water scarcity may receive substantial utility from acquiring the same quantity. The physical resource is unchanged; the positions of the agents are different. The resulting changes in utility are therefore different.

The same principle applies to tangible and intangible things alike. Food, land, money, knowledge, skills, information, relationships, and opportunities can all participate in changes to an agent's position. Their physical or conceptual differences do not require separate theories of value. What matters is how interaction with them changes what the agent can do and, consequently, the future positions the agent can reach.

Value is therefore not a property that exists independently of the agent's position or the transitions available within the game. It arises from the relationship between $x$, the agent's position, and the positional transitions that $x$ enables.

The fundamental relationship is therefore:

$$
\boxed{
V(x\mid P)=\Delta U.
}
$$

The remainder of this article examines the implications of this relationship in order to develop a more complete account of the nature of value.

[1]: https://diogenesanalytics.com/blog/2026/03/05/universal-decision-making-framework "Towards a Universal Framework for Decision-Making"

## Intrinsic Value
The claim that value depends upon position raises an important question. Could something possess value independently of its relationship to an agent's position?

At first, this may seem possible. Gold, for example, is often described as valuable in itself. A beautiful painting may be considered valuable because of its beauty. A piece of land may be considered valuable because it is scarce. Such descriptions appear to attribute value to the things themselves rather than to the positions of the agents who possess them.

But describing something as valuable does not explain **why** it is valuable.

Suppose an object $x$ exists, but acquiring, accessing, or using $x$ produces no change in the agent's position and creates no change in the future possibilities available from that position. Then

$$
F(P,a_x)=P.
$$

Consequently,

$$
U(F(P,a_x))-U(P)=0.
$$

Under the proposed definition,

$$
V(x\mid P)=0.
$$

The object may possess physical, aesthetic, or other properties, but those properties have no value to the agent unless they participate in some change that matters to the agent's position.

This does not mean that the properties of an object are irrelevant. They may be precisely what enables the object to produce a particular positional change. Gold's physical properties, for example, may make it useful for particular purposes. A painting's aesthetic properties may produce an experience that matters to an agent. Land's physical location and characteristics may provide access to shelter, production, resources, or other opportunities.

But these properties explain **how** the object can affect position. They do not constitute value independently of that relationship.

The distinction can be seen by considering the same object from different positions. Suppose two agents encounter identical objects $x$, but occupy positions $P_A$ and $P_B$. If value were an intrinsic property of $x$, then its value would have to be independent of the positions from which it is evaluated. We would therefore expect

$$
V(x\mid P_A)=V(x\mid P_B).
$$

But there is no general reason for this equality to hold. Instead,

$$
V(x\mid P_A)\neq V(x\mid P_B)
$$

whenever the same object produces different positional consequences for the two agents.

Water provides a simple example. To an agent with abundant access to clean water, an additional liter may produce little improvement in position. To an agent who is severely dehydrated, the same liter may produce a substantial improvement. The physical properties of the water have not changed. The position into which it is introduced has.

The same principle applies even to things whose value appears particularly independent of circumstances. Gold may be valuable to one agent because it can be exchanged for resources, to another because it is required for a particular productive process, and to another because it satisfies an aesthetic or symbolic objective. Its physical properties remain constant while its value can differ because the positional consequences of those properties differ.

Thus, the properties of an object and the value of an object should be distinguished:

$$
\boxed{
\text{Properties of }x\neq\text{Value of }x.
}
$$

The properties of $x$ describe characteristics of the object. Value describes the positional significance of those characteristics for an agent.

This distinction does not require us to deny that objects have stable physical properties, nor does it require us to deny that some objects are almost universally valuable to humans. It means only that **universality of value does not establish intrinsic value**. If an object produces a similar improvement in position for nearly every human agent, its value may appear intrinsic even though the underlying relationship remains positional.

The apparent value of an object can therefore be understood as a consequence of the object's capacity to participate in positional transitions. Value does not need to be contained within the thing itself.

It is enough that the thing can **change what an agent can do, what states the agent can reach, or how desirable those states are**.

Value is therefore inherently conditional on position. The value of a thing cannot be fully specified without reference to the position from which its consequences are evaluated.

This establishes an important distinction for the remainder of the analysis. The physical or conceptual properties of a thing may remain stable while its value changes as the agent's position changes. The next question is therefore not whether the thing itself has changed, but **what happens to its value when the quantity of that thing available to the agent changes?**


## The Structure of Value
We have defined the value of a thing in terms of the change in the utility of an agent's position that results from acquiring, accessing, or using it:

$$
V(x\mid P) = U(F(P,a_x)) - U(P)
$$

This definition implies that the value of a thing depends not only on the thing itself, but also on the position from which the agent encounters it. The same thing can produce different changes in utility when introduced into different positions.

To see why, consider position as a collection of variables:

$$
P = (x_1, x_2, \ldots, x_n)
$$

Each component represents some aspect of the agent's state that is relevant to its future possibilities. The utility function therefore evaluates the position as a whole:

$$
U(P) = U(x_1, x_2, \ldots, x_n)
$$

A change in any component of position can consequently produce a change in utility.

Suppose, for example, that $x$ represents the quantity of some resource available to the agent. Holding the other components of position constant, changing the quantity of $x$ produces a change in utility:

$$
\Delta U
=
U(x+\Delta x,x_2,\ldots,x_n)
-
U(x,x_2,\ldots,x_n).
$$

The value associated with the additional quantity is therefore not determined by the quantity alone. It is determined by the change in the evaluated position produced by that quantity.

For a small change in $x$, the corresponding change in utility can be approximated by

$$
dU\approx\frac{\partial U}{\partial x}dx.
$$

The quantity

$$
\frac{\partial U}{\partial x}
$$

therefore represents the marginal change in the evaluated position associated with a small change in $x$, holding the other positional variables constant.

This provides a positional interpretation of marginal value. The marginal value of a resource is not a separate property of the resource. It is a local property of the utility function at a particular point in position space.

Consequently, marginal value can change as the agent's position changes.

Suppose that increasing the quantity of $x$ generally improves the agent's position, but that each additional unit produces a progressively smaller improvement. Mathematically,

$$
\frac{\partial U}{\partial x}>0
$$

while

$$
\frac{\partial^2U}{\partial x^2}<0.
$$

The first condition means that additional quantities of $x$ increase the evaluated position. The second means that the rate at which utility increases declines as the quantity increases.

This is the positional foundation of diminishing marginal utility.

The important point is that diminishing marginal value is therefore not a universal law about objects. It is a property of the relationship between a positional variable and the utility function. Some quantities may exhibit diminishing marginal value. Others may exhibit increasing marginal value over some range. Still others may have thresholds at which their effect on position changes abruptly.

The structure of $U(P)$ can therefore be more complicated than a simple relationship between the quantity of one resource and utility. The value of one positional component may depend upon the values of other components.

Suppose position contains two variables, $x$ and $y$:

$$
P = (x,y,\ldots).
$$

The effect of changing $x$ may depend upon the value of $y$. In such a case,

$$
\frac{\partial^2 U}{\partial x\,\partial y}\neq0.
$$

For example, possessing a tool may have little value without the materials required to use it. Possessing the materials may similarly have little value without the tool. The combined effect on position can therefore be greater than the effects of either resource considered independently.

This means that value cannot always be attributed to individual things in isolation. The value of a thing may depend upon the broader configuration of the agent's position.

The same principle explains why the value of an apparently identical object can change over time. If the agent's position changes, then the location at which the agent evaluates the object in position space also changes. Consequently,

$$
P_t\neq P_{t+1}
$$

may imply

$$
V(x\mid P_t)\neq V(x\mid P_{t+1}).
$$

Value is therefore dynamic because position is dynamic.

This gives us a more general understanding of value. Value is not simply a property of objects, nor is it determined solely by their quantities. It emerges from the structure of the utility function over position space.

An object's value depends upon **where the agent is, what else the agent possesses, what the agent can do with the object, and how those possibilities affect the evaluation of the resulting position**.

The next question is therefore a natural one. If the value of a thing depends upon the agent's position and the quantities of resources available within that position, **what happens when the availability of the thing itself is limited?**

That question leads to scarcity.

## Scarcity and Value
The structure of $U(P)$ shows that the value of a thing depends upon the position in which it is evaluated. This provides a basis for understanding one of the most familiar concepts associated with value: scarcity.

Scarcity is often treated as though it were itself a source of value. In economic reasoning, scarce goods are generally understood to command greater value than abundant goods. But scarcity alone cannot explain value. A thing can be extremely scarce and have little or no value to a particular agent. Conversely, an abundant resource can have enormous value when the agent requires it for survival or for some other important objective.

Scarcity therefore should not be identified with value. Rather, scarcity can alter the **positional consequences** of acquiring, possessing, or losing a thing.

Consider a resource $x$. Suppose an agent has abundant access to $x$. An additional unit may produce only a small change in the evaluated position:

$$
\Delta U_x\approx 0.
$$

Now suppose the agent's available supply of $x$ becomes increasingly limited. The agent may lose alternatives, become more vulnerable to threats, or lose the ability to reach certain future states without obtaining additional quantities of $x$. The same unit of $x$ can then produce a substantially larger change in utility:

$$
\Delta U_x\gg0.
$$

The resource itself has not necessarily changed. What has changed is the position of the agent and the structure of the alternatives available from that position.

Water provides an intuitive example. For an agent with reliable access to abundant water, another liter may have little positional significance. For an agent whose available supply is approaching exhaustion, that same liter may determine whether certain future states remain attainable.

We can represent the quantity of a resource available to an agent as one component of position:

$$
P=(x,\ldots).
$$

The value of an additional quantity of $x$ is then the resulting change in utility:

$$
V_x(x\mid P)
=
U(x+\Delta x,\ldots)-U(x,\ldots).
$$

As established earlier, this is a finite positional change. For sufficiently small changes in $x$, the corresponding marginal value is described locally by

$$
\frac{\partial U}{\partial x}.
$$

If the marginal value of the resource increases as its available quantity falls, then for two otherwise comparable positions,

$$
x_1<x_2
\quad\Rightarrow\quad
\left.\frac{\partial U}{\partial x}\right|_{x_1}
>
\left.\frac{\partial U}{\partial x}\right|_{x_2}.
$$

The important point is that scarcity affects value through the structure of the position. A resource can become more consequential as its available quantity falls because the acquisition, retention, or loss of that resource can produce a larger change in the agent's attainable futures.

This also explains why scarcity does not have a uniform effect on all agents. The same resource may be scarce in the environment while having little value to an agent that already possesses sufficient substitutes. Another agent may occupy a position in which that resource is indispensable.

Thus, scarcity must be understood relative to the agent's position.

More generally, suppose an agent can reach a set of future states from position $P$:

$$
\mathcal{F}(P).
$$

If a resource $x$ is abundant, losing one unit may leave this set largely unchanged:

$$
\mathcal{F}(P')\approx\mathcal{F}(P).
$$

If the resource is scarce and consequential, losing the same unit may eliminate entire classes of future states:

$$
\mathcal{F}(P')\subset\mathcal{F}(P).
$$

The positional consequence of the resource is therefore much greater.

This provides a more fundamental interpretation of scarcity:

> **Scarcity matters because limited availability can increase the effect that acquiring, retaining, or losing a resource has on an agent's attainable future states.**

Scarcity is consequently neither necessary nor sufficient for value in the most general sense. A thing need not be scarce to have value, and scarcity by itself does not guarantee value. What matters is whether the limitation changes the agent's position in a way that affects its evaluated future possibilities.

This distinction also means that scarcity is not a fixed property of a thing considered in isolation. A resource may be abundant relative to one agent's requirements and scarce relative to another's. Its environmental availability may remain unchanged while its positional significance differs substantially between agents.

The relationship can therefore be represented as:

$$
\boxed{
\text{Scarcity}
\rightarrow
\text{availability}
\rightarrow
\text{positional consequences}
\rightarrow
\text{value}.
}
$$

This should not be interpreted as a universal causal chain in which scarcity necessarily produces value. Rather, it describes one mechanism through which changes in availability can alter positional consequences and therefore alter value.

Scarcity is thus not value itself. It is one condition that can alter the relationship between a thing and the agent's position.

This distinction prepares us for an even more important problem. An agent does not evaluate resources only according to their present availability. A resource available today may provide benefits tomorrow, while a resource that cannot be obtained until tomorrow may be useless today. The value of a thing therefore depends not only on **how much of it is available**, but also on **when it is available**.

That brings us to the role of time in value.


## Value and Time
Value is inherently related to time because an agent's position is not static. An agent occupies a position at some moment and then moves through a sequence of subsequent positions as actions are taken and circumstances change.

We can represent this sequence as

$$
P_t\rightarrow P_{t+1}\rightarrow P_{t+2}\rightarrow\cdots
$$

with each position evaluated according to the utility associated with its future possibilities:

$$
U(P_t).
$$

A thing can therefore have value not only because of the immediate change it produces in an agent's position, but also because of the subsequent positional transitions that it enables.

Suppose an agent acquires a resource $x$ at time $t$. The immediate effect may be small, while the resource may substantially alter the agent's future possibilities. The resulting sequence might be represented as

$$
P_t
\xrightarrow{a_x}
P_{t+1}
\rightarrow
P_{t+2}
\rightarrow
\cdots
$$

The significance of $x$ therefore cannot necessarily be understood by examining only the immediate positional change. Its acquisition may alter the structure of the future positions that become attainable from the resulting position.

This is particularly clear for things that persist through time. Land, tools, knowledge, infrastructure, and other durable resources can continue to participate in positional transitions long after the initial action that introduced them into the agent's position.

The relevant distinction is therefore between **immediate effect** and **temporal consequence**.

An action may produce a relatively small immediate change in utility while creating substantially different future possibilities:

$$
U(P_{t+1})-U(P_t)\approx0,
$$

while nevertheless producing a substantially different set of future positions from $P_{t+1}$ than would otherwise have been attainable.

The reverse is also possible. An action may produce a substantial immediate improvement while reducing future possibilities. Consumption provides a simple example: consuming a resource may improve the current position while eliminating the ability to use that same resource later.

Thus, the immediate change in utility is not necessarily sufficient to characterize the full positional significance of a thing. What matters is how the resulting position affects subsequent transitions.

The relevant question is therefore:

> **How does obtaining or using the thing alter the agent's position and, through that position, the future states available to the agent?**

This also explains why the timing of an otherwise identical resource can matter.

Suppose an agent can obtain the same resource $x$ either at time $t_1$ or at a later time $t_2$. Even if the physical quantity is identical,

$$
x_{t_1}=x_{t_2},
$$

the two instances need not have equal value:

$$
V(x_{t_1}\mid P_{t_1})
\neq
V(x_{t_2}\mid P_{t_2}).
$$

The reason is not that time itself necessarily gives the resource different properties. Rather, the resource enters different positions and therefore affects different subsequent possibilities.

A resource arriving before a critical decision may preserve or create future states that would otherwise be inaccessible. The same resource arriving after that decision may have little or no ability to affect those states.

Conversely, a resource obtained today may retain value precisely because it remains available for future actions.

This introduces an important distinction between **quantity and persistence**. A thing may retain the same physical quantity while its value depends upon how long it remains available and which future transitions that availability permits.

If an agent retains a resource $x$ rather than consuming or otherwise using it, the resource remains available for future actions. Its positional significance therefore includes not only what the agent can do with it immediately, but also what the agent may be able to do with it in subsequent positions.

In this sense, a persistent resource preserves a set of potential future transitions.

Money provides a simple example. A monetary unit held today can preserve the ability to obtain different resources or opportunities through exchange. Its positional significance therefore depends partly upon the future transitions that remain available while it is held. Those transitions can change as prices, opportunities, or the agent's own position change.

The same principle applies more generally. A resource can retain its quantity while its value changes because the future positions that it can influence have changed. Conversely, a resource whose quantity is consumed may cease to provide certain future transitions even if its immediate use produced substantial benefit.

Time therefore introduces an important dimension to the analysis of value. The relevant question is not simply **what does this thing do to the agent's position?**, but also **when does it do so, how long does its effect persist, and which subsequent positions can that effect influence?**

This follows directly from the temporal structure of Position. An agent does not act merely to change its present position. It acts from the present position in order to influence the positions it may occupy in the future.

Value must therefore be understood across that same temporal structure.

> **A thing has value to the extent that possessing or using it changes the agent's position and, through that position, the future states available to the agent.**

Time does not create value by itself. Rather, time determines **when a positional change occurs, how long its effects persist, and which future states that change can influence**.

This introduces another fundamental complication. Future positions are rarely known with certainty. An agent does not generally know exactly which state it will occupy tomorrow, much less years from now. The value of a thing must therefore be considered in relation not only to the future positions it can affect, but also to the **uncertainty surrounding those futures**.

That brings us to **Value and Uncertainty**.


## Value and Uncertainty

The temporal nature of value introduces another fundamental consideration: the future is not generally known with certainty.

An agent occupying position $P_t$ does not necessarily know which position it will occupy at a later time. An action may therefore lead not to a single future position, but to a set of possible positions:

$$
P_t
\xrightarrow{a}
\left\{
P_{t+1}^{(1)},
P_{t+1}^{(2)},
\ldots,
P_{t+1}^{(n)}
\right\}.
$$

These possible positions may differ substantially in their consequences for the agent. Some may provide favorable opportunities, while others may introduce threats, constraints, or losses of future possibilities.

Uncertainty therefore concerns the relationship between the present position and the possible future positions that may follow from it.

This is already represented within the Position framework. Utility evaluates a position according to the structure of its reachable futures:

$$
U(P)=A(P)-T(P)+D^+(P)-D^-(P),
$$

where $A(P)$ represents accessible positive terminal value, $T(P)$ represents exposure to negative terminal value, and $D^+(P)$ and $D^-(P)$ represent the structural diversity of favorable and unfavorable continuation paths, respectively.

Uncertainty does not therefore require the introduction of a separate utility function. Instead, uncertainty can affect the existing components of the position's evaluation.

An uncertain future may alter the accessibility of favorable outcomes, increase exposure to unfavorable outcomes, or otherwise change the structure of the futures available to the agent. The significance of uncertainty therefore depends upon how the possible future positions affect the evaluation of the current position.

Consequently, two positions that contain similar immediate resources may nevertheless have substantially different utility if the structures of their future possibilities differ.

Consider two agents possessing identical quantities of some resource $x$. One agent may have reliable access to the future resources and opportunities required to maintain its position. The other may face substantial uncertainty about whether those resources will remain available.

The physical quantity of $x$ is identical, but the positions are not:

$$
P_A\neq P_B.
$$

Therefore,

$$
U(P_A)\neq U(P_B)
$$

may hold even when some individual components of the positions are identical.

This also affects the value of things that protect against uncertain outcomes.

Suppose an agent can acquire a resource or arrangement $x$ that reduces its exposure to unfavorable future states. The acquisition may have little immediate effect on the agent's material circumstances, yet substantially improve the structure of its future position by reducing the consequences of unfavorable outcomes.

The value of $x$ can therefore arise from its effect on the future-state structure:

$$
P
\xrightarrow{a_x}
P'
$$

where, for example, the resulting position may have lower exposure to unfavorable terminal outcomes:

$$
T(P')<T(P).
$$

Here, $T(P')$ denotes the threat component of the utility of the resulting position $P'$. Thus, $T(P')<T(P)$ means that the transition from $P$ to $P'$ has reduced the position's exposure to negative terminal value.

Insurance provides an intuitive example. An insurance contract may not increase an agent's immediate material resources at all. Its value instead comes from changing the consequences associated with an adverse future event. By transferring or limiting a potential loss, it can reduce the unfavorable outcomes associated with the agent's position.

The same principle applies to redundancy, reserves, diversification, and other mechanisms through which agents preserve future possibilities or reduce exposure to unfavorable ones.

Uncertainty can also increase the value of optionality. An option preserves the ability to choose among future actions without requiring the agent to commit to one particular future in advance.

If an agent retains several possible courses of action,

$$
\{a_1,a_2,\ldots,a_n\},
$$

then its future position may contain possibilities that would not exist if the agent had already committed to a single course of action.

The value of retaining this flexibility arises because different future circumstances may make different actions preferable. Preserving multiple possible transitions can therefore improve the structure of the agent's future position even before the relevant circumstances are known.

This gives uncertainty an important relationship with value. The value of a thing does not depend merely upon the resources it provides under one particular future. It can also depend upon how the thing changes the range, structure, and consequences of the possible futures available to the agent.

The relevant question is therefore not simply:

> **What will this thing produce?**

but:

> **How does possessing this thing change the agent's position across the possible futures that may occur?**

This distinction is important because uncertainty does not necessarily reduce value. Sometimes uncertainty increases the value of resources that provide flexibility, resilience, or protection against unfavorable outcomes. At other times, uncertainty may reduce the value of an otherwise attractive resource if its benefits depend upon circumstances that may never occur.

The effect therefore depends upon the relationship between the resource and the agent's position.

Uncertainty is consequently not itself a form of value or disvalue. It is a property of the relationship between the present position and its possible futures. Its significance arises from how those possibilities affect the evaluation of the position.

We can therefore extend the structure developed throughout this article:

$$
\boxed{
\text{thing}
\rightarrow
\text{action}
\rightarrow
\text{position}
\rightarrow
\text{future possibilities}
\rightarrow
U(P).
}
$$

Value arises from the effect of the thing on this structure.

This also reinforces an important distinction between value and prediction. An agent does not need to know exactly which future position will occur in order for something to have value. What matters is how the thing changes the structure of the possible futures available from the agent's position.

Time determines **when** a positional transition occurs and which subsequent states it can influence. Scarcity determines **how constrained** access to certain resources or possibilities may be. Uncertainty determines **which future positions may occur and how their consequences may differ**.

Together, these factors influence the way changes in position are evaluated.

We have now developed the principal conditions under which the value of a thing can differ even when the thing itself remains unchanged. Its value can depend upon the agent's position, the quantity already possessed, the availability of alternatives, the timing of the resource, and the uncertainty surrounding the futures in which it can be used.

Yet none of these concepts explains one of the most familiar numbers associated with value.

A thing can be valuable to an agent without having a particular **price**. A thing can have a high price while providing little value to a particular agent. And two things can have very different positional values while trading at similar prices.

We therefore arrive at the central distinction underlying much of economics and finance:

> **What is the relationship between value and price?**

That is the next problem.

## Value and Price
We have defined the value of a thing in terms of the change in the utility of an agent's position resulting from obtaining or using it:

$$
V(x\mid P)=U(F(P,a_x))-U(P).
$$

Value therefore describes the effect of a thing on the evaluated position of the agent. It is inherently dependent upon the position from which the thing is evaluated.

Price is different.

A price is not an evaluation of a thing's effect on an agent's position. It is the quantity of an exchange medium given in exchange for the thing. In modern economies, that exchange medium is usually money.

If an object $x$ exchanges for $m$ units of money, its price can be represented as

$$
p_x=m.
$$

The price therefore describes an exchange relationship between $x$ and money. It does not, by itself, describe the utility that $x$ provides to any particular agent.

This distinction is fundamental:

$$
\boxed{
\text{Value}\neq\text{Price}.
}
$$

Value is determined through the change in the evaluated position produced by a thing. Price is expressed through the quantity of money required to acquire the thing in an exchange.

The distinction becomes clear when considering two different agents.

Suppose an item has a market price of $100. One agent may obtain substantial positional benefit from possessing it, while another may obtain very little. Their valuations can therefore differ:

$$
V(x\mid P_A)>V(x\mid P_B).
$$

Yet both may encounter the same market price:

$$
p_x=\$100.
$$

The price does not change merely because the two agents value the object differently. Instead, their different valuations determine whether either agent has an incentive to participate in the exchange at that price.

For the buyer, acquiring $x$ requires surrendering money. The relevant question is therefore not simply whether $x$ has positive value, but whether the positional benefit produced by acquiring $x$ is greater than the positional cost of giving up the money required to obtain it.

Likewise, the seller does not merely ask whether $x$ has value. The seller compares the positional consequence of retaining $x$ with the positional consequence of receiving the money offered in exchange.

An exchange can therefore occur when the buyer and seller evaluate the two sides of the transaction differently.

For a buyer $B$ and seller $S$, an exchange of $x$ for $m$ can improve both positions when

$$
V(x\mid P_B)>V(m\mid P_B)
$$

and

$$
V(m\mid P_S)>V(x\mid P_S).
$$

The buyer prefers the thing to the money being surrendered, while the seller prefers the money to the thing being surrendered.

This explains an important property of exchange: **a voluntary transaction does not require the buyer and seller to assign the same value to the thing being exchanged.**

In fact, differences in positional value are precisely what make many exchanges possible.

Suppose a seller possesses a resource that has relatively low positional value to the seller but high positional value to a potential buyer. The buyer may therefore be willing to surrender a quantity of money that is more valuable to the seller than the resource being sold.

The transaction changes both positions.

For the buyer,

$$
P_B\rightarrow P_B',
$$

where the buyer gives up money and obtains $x$.

For the seller,

$$
P_S\rightarrow P_S',
$$

where the seller gives up $x$ and obtains money.

If both resulting positions are preferable according to their respective utility functions, the exchange improves both agents' positions.

Price therefore functions as a mechanism through which heterogeneous positional valuations can be reconciled through exchange.

This also explains why market price should not be interpreted as the "true value" of an object. A market price is the outcome of exchanges among agents whose positions, preferences, constraints, alternatives, and expectations may differ.

The same object can consequently have many different positional values while having a single prevailing market price at a particular time and place.

There is another important distinction.

Value, as defined here, is expressed through the utility function:

$$
V(x\mid P)=\Delta U.
$$

Price, by contrast, is expressed in units of money:

$$
p_x=m.
$$

These quantities therefore do not necessarily have the same units. Unless utility has been explicitly calibrated in monetary terms, it would be incorrect to equate a positional value directly with a dollar price.

What economics often calls **willingness to pay** provides a bridge between the two concepts.

Consider an agent in position $P$ deciding whether to acquire $x$ for $m$ units of money. The agent's maximum willingness to pay is the amount of money that leaves the agent indifferent between acquiring $x$ and retaining the money.

The relevant transition can be represented as

$$
P
\xrightarrow{\text{acquire }x,\ \text{pay }m}
P'.
$$

At the maximum willingness to pay,

$$
U(P')=U(P).
$$

The corresponding amount $m$ is the agent's willingness to pay for $x$ in position $P$.

Thus, while value and price are distinct concepts, a monetary valuation can be derived from the underlying positional utility when money provides a sufficiently well-defined measure of positional sacrifice.

This gives us a hierarchy:

$$
\boxed{
\text{Thing}
\rightarrow
\text{Positional effect}
\rightarrow
\text{Utility change}
\rightarrow
\text{Monetary valuation}
\rightarrow
\text{Exchange price}.
}
$$

The first three relationships concern the agent's position directly. Monetary valuation introduces money as the unit in which the agent is willing to express a sacrifice. Market price then emerges through actual exchange among agents.

This distinction also resolves an apparent paradox surrounding things such as land and money.

Land may have a high market price because many agents are willing to surrender substantial quantities of money to acquire it. But the positional value of a particular parcel can differ dramatically between agents. A parcel may be extremely valuable to an agent who needs its location, productive capacity, shelter, or other characteristics, while having little value to someone who has no corresponding use for it.

Money exhibits the opposite appearance. A monetary unit can seem to possess an almost universal value because it is accepted in exchange for an enormous range of resources, goods, services, and opportunities. Yet its value ultimately derives from the positional changes that those future exchanges can produce.

Money therefore does not escape the theory of positional value. Rather, it provides a highly general mechanism through which one form of positional value can be exchanged for another.

This is why price can be extremely useful without being identical to value. Price provides a common exchange denominator that allows agents with different positions to coordinate exchanges. It does not eliminate differences in value; it allows those differences to be acted upon.

Consequently,

$$
\boxed{
\text{price is an exchange quantity, while value is a positional evaluation}.
}
$$

The distinction is especially important when considering changes over time. The market price of a thing can remain constant while its positional value changes for a particular agent. Conversely, its market price can change while its positional value to that agent changes very little.

Price therefore contains information about the conditions under which exchanges are currently occurring. Value describes the consequences of those exchanges for particular positions.

This distinction gives us the conceptual foundation needed to examine money itself. If money serves as the common unit in which prices are expressed and as a medium through which exchanges occur, what exactly gives money its value?

That question leads to the next problem:

> **Why does money have value?**


## Money and Value
We have established that the value of a thing is determined by the change it can produce in an agent's position:

$$
V(x\mid P)=U(F(P,a_x))-U(P).
$$

We have also established that price is an exchange quantity rather than a measure of positional value.

Money introduces an important complication because money itself is one of the things that can be exchanged for other things. It therefore has value, but its value is not primarily derived from the physical properties of the object representing the money.

A dollar bill, for example, is physically only a small piece of paper. Its physical properties do not explain why an agent would surrender food, land, labor, or other valuable resources to obtain it. The relevant property of money is instead its ability to participate in exchange.

Money therefore derives its value from the positional transitions that it enables through exchange.

Suppose an agent possesses an amount of money $M$. That money gives the agent access to some set of potential exchanges. Each exchange can produce a different resulting position:

$$
P
\xrightarrow{a_1}
P_1,
$$

$$
P
\xrightarrow{a_2}
P_2,
$$

$$
\vdots
$$

$$
P
\xrightarrow{a_n}
P_n.
$$

The money therefore has significance not merely because the agent possesses $M$, but because possessing $M$ allows the agent to perform actions that may otherwise be unavailable.

Money consequently acts as a general-purpose mechanism for transforming one position into another through exchange.

This gives money a distinctive form of value. A quantity of food has value because it can directly affect the agent's position. A tool has value because it can enable particular actions. Land has value because it can provide particular resources, capabilities, or opportunities.

Money is different because it can potentially be exchanged for a very large variety of things.

Its value therefore derives from the set of future positional transitions that it enables.

We can represent this conceptually as

$$
M
\rightarrow
\mathcal{E}(M)
\rightarrow
\mathcal{R}(P),
$$

where $\mathcal{E}(M)$ represents the set of exchanges available through the money and $\mathcal{R}(P)$ represents the resulting reachable positions.

The important point is that money does not need to specify which future transition will occur.

An agent holding a dollar does not necessarily know whether that dollar will eventually be exchanged for food, water, transportation, a tool, labor, land, or some other resource. The money preserves the ability to make that choice later.

Money therefore has an important **optionality** that many other resources do not possess.

Possessing a specific resource generally constrains the agent to the uses associated with that resource. Possessing money can leave the agent with a much broader set of possible exchanges.

This can make money valuable even when the agent has no immediate need for any particular good.

The agent is not necessarily valuing the money for what it does in the present position. It may be valuing the **future possibilities that remain available because the money has not yet been spent**.

This provides another interpretation of holding money through time.

Suppose an agent receives $M$ at time $t$ and retains it:

$$
P_t
\xrightarrow{\text{retain }M}
P_{t+1}.
$$

No substantial change in the agent's immediate material circumstances may occur. Nevertheless, the agent continues to possess the ability to exchange $M$ for other resources at a later time.

The money therefore preserves potential future transitions.

This is one reason money can function as a store of value. It allows an agent to preserve some capacity for exchange from the present into the future.

However, the positional significance of holding money does not depend only upon the nominal quantity held. It depends upon the future exchanges that remain available to the agent.

Suppose two agents possess the same amount of money:

$$
M_A=M_B.
$$

The money need not have the same value to both agents because the agents occupy different positions.

One agent may have immediate access to food, water, shelter, transportation, and other necessities. Another may lack one or more of these resources. The same monetary quantity can therefore provide different potential improvements to their respective positions.

In general,

$$
V(M\mid P_A)\neq V(M\mid P_B).
$$

The apparent universality of money therefore does not imply universal positional value.

What is unusually universal about money is its **exchangeability**.

A monetary unit can be used across many different transactions, allowing agents with very different positions to use the same medium to pursue very different future states.

Money therefore functions as a general mechanism for converting one form of economic possibility into another.

An agent can exchange labor for money, money for food, food for energy, energy for productive activity, and productive activity for money again. Money allows these exchanges to occur without requiring every participant to directly exchange one desired resource for another.

The resulting system dramatically expands the set of feasible exchanges.

This gives money a distinctive position within the human game. It is not itself necessarily the ultimate objective of an exchange. Rather, it is a mechanism through which agents acquire the resources, capabilities, and opportunities that can alter their positions.

We can therefore distinguish between **direct positional value** and **exchange-mediated positional value**.

A resource such as food can affect position directly when consumed:

$$
\text{Resource}
\rightarrow
\text{Position}.
$$

Money can affect position through an exchange:

$$
\text{Money}
\rightarrow
\text{Exchange}
\rightarrow
\text{Resource}
\rightarrow
\text{Position}.
$$

The latter relationship does not make money less real as a source of value. It makes money more general. Because money can potentially be exchanged for many different resources, it can preserve a broad range of possible future transitions.

This also explains why money can appear to possess value independently of the things for which it is exchanged.

Because money is accepted across a large network of exchanges, an agent can often treat money as though it were valuable in itself. But the underlying mechanism remains the same.

The agent values the money because the money preserves access to future exchanges, and those exchanges can produce changes in position.

Money is therefore not an exception to positional value. It is an especially general application of it.

The value of money can consequently be represented in the same fundamental terms as the value of anything else:

$$
V(M\mid P)
=
U(F(P,a_M))-U(P),
$$

where $a_M$ represents an action involving the acquisition, retention, or use of money.

The distinctive feature is not the form of the physical object representing the money, but the range of positional transitions that the monetary quantity can enable.

Money therefore has value because it provides **access to exchange**, and access to exchange provides access to a potentially broad set of future positional transitions.

This gives us the conceptual foundation for understanding purchasing power. If the value of money depends upon what can be obtained through exchange, then changes in the quantity of money relative to the things available for exchange can alter the relationship between money and those things.

The next question is therefore:

> **What happens to the purchasing capability represented by money when the quantity of money changes?**

That question leads to the relationship between **money supply and purchasing power**.

## Money, Supply, and Purchasing Power
The value of money arises from the future exchanges that money enables. This means that the value of a monetary quantity cannot be understood solely from the number of monetary units possessed.

What matters is what those units can obtain.

Suppose an agent possesses a quantity of money

$$
M.
$$

That money provides access to a collection of goods, services, resources, and opportunities through exchange. The purchasing capability represented by $M$ therefore depends upon the exchange relationships between money and the things for which it can be exchanged.

We can therefore distinguish between the **quantity of money** and the **purchasing power of money**.

The quantity of money is simply

$$
M.
$$

Purchasing power, by contrast, describes what that quantity of money can command through exchange.

For a particular good or resource $x$, let its market price be

$$
p_x.
$$

At that price, the quantity of $x$ that can be acquired with $M$ units of money is

$$
Q_x^M=\frac{M}{p_x}.
$$

This quantity is not itself the value of the money. Rather, it describes one dimension of the exchange capability provided by the money.

If the price of $x$ increases while $M$ remains constant, then

$$
p_x\uparrow
\quad\Rightarrow\quad
Q_x^M\downarrow.
$$

The monetary quantity has not changed, but the amount of $x$ that it can obtain has decreased.

Conversely,

$$
p_x\downarrow
\quad\Rightarrow\quad
Q_x^M\uparrow.
$$

The same monetary quantity can therefore represent different purchasing capabilities at different points in time.

Purchasing power is consequently not a physical property of money. It is a property of the relationship between money and the things for which money can be exchanged.

For a collection of goods and resources, purchasing power can be represented more generally as a vector of exchange capabilities:

$$
\mathbf{Q}^M =
\left(
\frac{M}{p_1},
\frac{M}{p_2},
\ldots,
\frac{M}{p_n}
\right).
$$

The vector describes what the monetary quantity $M$ can command at the prevailing prices.

This reveals an important distinction between **nominal quantity** and **real purchasing capability**.

An agent can possess more money without having a greater ability to acquire a particular real resource if the price of that resource increases proportionally.

Suppose the quantity of money increases from $M$ to

$$
M'=kM
$$

while the price of a resource increases from $p_x$ to

$$
p_x'=kp_x.
$$

Then

$$
\frac{M'}{p_x'} = \frac{kM}{kp_x} = \frac{M}{p_x}.
$$

The agent possesses more nominal money, but its purchasing capability with respect to $x$ is unchanged.

An increase in monetary units therefore does not, by itself, establish an increase in the agent's positional value.

The relevant question is what those additional units can command.

Now consider the quantity of money in an economy. Let the total quantity of money be

$$
M_E.
$$

Suppose this quantity increases:

$$
M_E\rightarrow M_E+\Delta M_E.
$$

The creation of additional monetary units does not, by itself, create additional land, food, water, labor, productive capacity, or time. Monetary quantity and real resource quantity are therefore not the same thing.

An increase in the quantity of money can change the monetary relationships through which existing resources are exchanged. But this does not imply that every increase in money supply must produce an immediate or proportional increase in every price. Prices are also influenced by production, demand, saving, investment, credit, expectations, the distribution of money, and other conditions within the economic system.

The more fundamental point is simpler:

> **The quantity of money can change independently of the quantity of many of the real resources for which money is exchanged.**

Consider land. Let the physical quantity of a particular parcel be

$$
L.
$$

The creation of additional monetary units does not produce

$$
L+\Delta L.
$$

The parcel remains the same physical resource.

Its market price, however, is an exchange quantity and can change as the conditions of exchange change. Thus,

$$
L=\text{constant}
$$

does not imply

$$
p_L=\text{constant}.
$$

A change in the market price of land therefore does not necessarily indicate a change in the physical quantity or intrinsic properties of the land. Likewise, a change in the quantity of money does not necessarily indicate a corresponding change in the quantity of the underlying resources that money can command.

We can therefore distinguish three related but different concepts:

$$
\boxed{\text{Money quantity}}
$$

$$
\boxed{\text{Real resource quantity}}
$$

and

$$
\boxed{\text{Purchasing power}}.
$$

The first describes the quantity of monetary units.

The second describes the quantity of the underlying real resources.

The third describes the exchange capability created by the relationship between monetary units and those resources, mediated by their prevailing exchange prices and availability.

This distinction explains why money can lose purchasing power without losing its nominal identity.

One dollar remains one dollar:

$$
M=\$1.
$$

But the quantity of real resources obtainable with that dollar can change.

If a dollar could previously obtain a particular quantity of some resource and later obtains less, then the positional significance of holding that dollar has changed even though its nominal quantity has not.

In terms of the Position framework,

$$
P_t\neq P_{t+1}
$$

may occur even when

$$
M_t=M_{t+1},
$$

because the purchasing possibilities associated with $M$ have changed.

The monetary quantity is therefore only one component of the position. Its significance depends upon the surrounding state of the game.

This returns us to the fundamental relationship established earlier:

$$
V(x\mid P)=U(F(P,a_x))-U(P).
$$

For money, the relevant positional change is mediated by exchange:

$$
\text{Money}
\rightarrow
\text{Exchange capability}
\rightarrow
\text{Resources and opportunities}
\rightarrow
\text{Position}.
$$

Consequently, a change in the nominal quantity of money does not by itself determine a change in its value. What matters is the change in the positional possibilities that the money enables.

The fundamental distinction is therefore

$$
\boxed{
\text{Nominal quantity}\neq\text{real purchasing capability}.
}
$$

Money has value because it enables exchange. Purchasing power describes the scope of that exchange capability. And the value of that capability ultimately depends upon how the resulting exchanges alter the agent's position and its future possibilities.

The analysis can therefore stop here. The distinction between value, money, and purchasing power has been established without yet requiring a definition of the economic structures in which those things are held or accumulated.

## Wealth and Value
We have now established that the value of a thing is determined by the effect that obtaining or using it can have on an agent's position:

$$
V(x\mid P)=U(F(P,a_x))-U(P).
$$

We have also distinguished value from price and purchasing power. Value describes the effect of a thing on an agent's evaluated position; price describes an exchange quantity; and purchasing power describes what a monetary quantity can command through exchange.

These distinctions allow us to identify an important boundary.

Many things can have value without necessarily being wealth.

Knowledge can be valuable. Skill can be valuable. Labor can be valuable. Health, relationships, opportunities, and capabilities can all have substantial effects on an agent's future possibilities. Yet it would be too broad to conclude from this that all such things are therefore forms of wealth.

Doing so would risk making wealth equivalent to the entirety of the agent's valuable position:

$$
\text{Wealth}\approx\text{everything of value in }P.
$$

That would eliminate the distinction we are trying to establish.

We therefore need to distinguish the **value of something** from its status as **wealth**.

Value answers the question:

> **How does this thing affect the agent's position?**

Wealth requires an additional question:

> **What kind of valuable structure can be possessed, retained, transferred, exchanged, or otherwise realized as an economic resource over time?**

That second question cannot be answered merely by the definition of value.

Consider knowledge. Knowledge may substantially increase an agent's future possibilities and therefore have substantial value:

$$
V(k\mid P)>0.
$$

But the existence of that value does not by itself establish that the knowledge constitutes wealth. Its economic significance depends upon whether and how that capability can be realized through production, exchange, claims, or other economic processes.

The same distinction applies to labor and skill. A person's ability to perform valuable work can affect future position without being identical to a stock of accumulated economic wealth. The ability may instead be a capability through which value is subsequently realized.

This suggests that there is an important conceptual sequence:

$$
\text{Position}
\rightarrow
\text{Value}
\rightarrow
\text{Economic realization}
\rightarrow
\text{Wealth}.
$$

The precise structure of the final transition is a separate problem.

This also explains why simply defining wealth as a collection of things that affect future positions is insufficient. **Effect on position is the basis of value, not the defining criterion of wealth.**

The distinction becomes especially important when considering money and other economic claims.

Money has value because it enables exchange:

$$
\text{Money}
\rightarrow
\text{Exchange}
\rightarrow
\text{Resources and opportunities}
\rightarrow
\text{Position}.
$$

But the fact that money has value does not mean that all valuable things are money, nor that all valuable things have the same economic structure as money.

Likewise, land, productive equipment, businesses, inventories, and financial claims can have substantial value while differing fundamentally in the way that value is realized and carried through time.

The Value framework therefore establishes the foundation for understanding wealth without yet defining wealth itself.

The essential conclusion is:

$$
\boxed{
\text{Value is more fundamental than wealth.}
}
$$

Value concerns the positional consequences of a thing.

Wealth concerns a particular economic structure through which value can be possessed, retained, transferred, or realized.

The distinction between these concepts must be preserved. Otherwise, defining wealth in terms of value alone simply reproduces the entire position problem under another name.

We can therefore leave the precise definition of wealth to a separate analysis.

For the purposes of the present article, it is sufficient to establish that **not everything valuable is necessarily wealth**. The value framework tells us why something matters to an agent; the wealth framework must determine what additional properties cause a valuable thing to constitute wealth.

That distinction provides the boundary between the present theory of value and the subsequent theory of wealth.

## Conclusion

Value is one of the fundamental concepts underlying decision-making because agents continually choose among actions that lead to different positions and different future possibilities.

The analysis developed in this article suggests that value is fundamentally **positional**.

For an agent in position $P$, the value of a thing $x$ can be expressed as the change in the evaluation of the agent's position resulting from obtaining, accessing, using, or otherwise interacting with $x$:

$$
\boxed{
V(x\mid P)=U(F(P,a_x))-U(P).
}
$$

Value therefore does not reside in an object independently of the agent and its circumstances. The same thing can have different value to different agents, or to the same agent at different times, because the positional consequences of obtaining it can differ.

This also explains why value should not be confused with the properties of the thing itself. Physical, informational, or other properties determine what a thing can do, but those properties become valuable insofar as they produce consequences that matter to the agent's position.

The structure of position also determines how value behaves. The value of an additional quantity depends upon what the agent already possesses, the relationships among different components of position, and the future possibilities that the resulting configuration makes available. Consequently, value need not be additive, constant, or universally diminishing.

Scarcity, time, and uncertainty likewise influence value through their effects on positional consequences. Scarcity can increase the significance of acquiring or retaining a resource when alternatives become constrained. Time determines when positional changes occur and how long their effects persist. Uncertainty affects the range of possible future consequences associated with a position. None of these concepts is value itself. Each changes the circumstances under which positional consequences are evaluated.

The distinction between value and price follows from the same framework.

$$
\boxed{
\text{Value}\neq\text{Price}.
}
$$

Value describes the effect of a thing on an agent's evaluated position. Price describes an exchange quantity. A market price therefore cannot be treated as the intrinsic or universal value of a thing. It reflects the conditions under which agents exchange it, while positional value depends upon the particular position of the agent evaluating it.

Money provides a particularly important example. Money has value because it enables exchange, and exchange provides access to resources, capabilities, and opportunities that can alter position:

$$
\text{Money}
\rightarrow
\text{Exchange}
\rightarrow
\text{Resources and opportunities}
\rightarrow
\text{Position}.
$$

This also explains the distinction between nominal monetary quantity and purchasing power. Possessing more monetary units does not necessarily provide greater positional capability if the resources those units can command have changed correspondingly.

The resulting picture can therefore be summarized as:

$$
\boxed{
\text{Thing}
\rightarrow
\text{Positional consequences}
\rightarrow
\text{Future possibilities}
\rightarrow
\text{Utility}
\rightarrow
\text{Value}.
}
$$

The central result is not that every valuable thing has the same economic form, nor that value can be reduced to money or exchange. It is that value has a common underlying structure across fundamentally different kinds of things.

Food, water, land, knowledge, tools, money, and opportunities may differ enormously in their physical and economic characteristics. Yet each can be evaluated according to the same fundamental question:

> **How does this thing change the agent's position and the future possibilities available from it?**

This provides a foundation for distinguishing value from the economic structures built around it. Wealth, assets, prices, and other economic concepts describe additional structures through which valuable things can be possessed, exchanged, transformed, and realized. They therefore require further analysis rather than being incorporated into the definition of value itself.

The fundamental conclusion is consequently:

$$
\boxed{
\text{Value is the positional significance of a thing to an agent.}
}
$$

More formally,

$$
\boxed{
V(x\mid P)=U(F(P,a_x))-U(P).
}
$$

Value is therefore relational, contextual, dynamic, and ultimately grounded in the structure of the agent's possible futures.

Understanding this relationship provides the conceptual foundation for examining the economic structures through which value is subsequently realized.
