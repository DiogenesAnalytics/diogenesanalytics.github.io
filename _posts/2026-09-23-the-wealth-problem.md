---
layout: article
title: The Wealth Problem
custom_css: article.css
include_mathjax: true
publish: true
---
## Introduction

Having wealth does not end the problem of wealth.

The previous article [*Defining Wealth*][1] examined what distinguishes wealth from the many other things that can matter to an agent. Something can have value without being wealth. Something can affect an agent's position without being wealth. A capability, a piece of knowledge, or an opportunity may be valuable and may change what an agent can do without itself constituting an economically realizable resource controlled by the agent.

The investigation led to the following definition:

$$
\boxed{
\text{Wealth is an economically realizable resource that an agent can control and retain through time.}
}
$$

This definition provides the starting point for the present problem.

Wealth is not merely something that has value. It is a resource that an agent can control and retain. A house, a quantity of money, a piece of land, equipment, inventory, or an economic claim can constitute wealth because the agent can exercise control over the resource and retain it as a resource through time.

The temporal aspect is particularly important.

If an agent can retain a resource through time, then the resource can exist at one point in time and still be available at a later point. What the agent possesses at the later time therefore depends on what happened to the resources it possessed earlier.

A resource may remain under the agent's control. It may be consumed. It may be exchanged for another resource. It may be transferred to another agent. It may be used in production. It may be transformed into another form of wealth. It may be impaired or destroyed. The agent may also take actions intended to prevent some of these outcomes.

The problem therefore begins with the transition of wealth through time.

At time $t$, an agent possesses some collection of wealth resources. At a later time $t+1$, it possesses another collection:

$$
W_t\rightarrow W_{t+1}.
$$

Here, $W_t$ denotes the collection of wealth resources controlled by the agent at time $t$, rather than a numerical measure of their economic value. The resources may be heterogeneous, and the transition between $W_t$ and $W_{t+1}$ may involve changes in both the resources themselves and their economic circumstances.

This creates a decision problem.

The agent must determine what should happen to the resources it controls. It may retain them for future use, consume them, exchange them, transfer them, use them to produce other resources, or take actions intended to preserve them against loss.

These possibilities are not equivalent.

Exchanging one resource for another may change the form of wealth without necessarily increasing or reducing its economic value. Using a resource in production may result in additional economic resources. Consuming a resource may remove it from the agent's wealth. A resource may also lose some or all of its economic significance without the agent choosing to do so.

The problem is therefore not simply how to acquire wealth.

It is how an agent should manage the wealth it already controls as that wealth changes through time.

This raises the central question:

> **How should an agent manage wealth through time?**

Answering this question requires a model of how wealth changes. We must characterize the transitions that resources can undergo, establish how those transitions affect the collection of resources controlled by the agent, and determine how the resulting wealth can be compared with the initial wealth.

In particular, we must distinguish changes in the resources themselves from changes in their economic valuation, and changes in the form of wealth from changes in its economic magnitude.

These distinctions provide the foundation for determining what it means for wealth to grow, what it means for wealth to be preserved, and how an agent's decisions affect the wealth available to it through time.

[1]: https://diogenesanalytics.com/blog/2026/09/21/defining-wealth "Defining Wealth"

## The Transition of Wealth

If wealth is an economically realizable resource that an agent can control and retain through time, then wealth is necessarily temporal.

A resource controlled by an agent at one point in time may still be controlled by that agent later. But it may also be different in some respect. It may have changed form, been combined with another resource, generated another resource, been exchanged, transferred, consumed, impaired, or ceased to exist.

The most general representation of this is simply:

$$
w_t\rightarrow w_{t+1}.
$$

Here, $w_t$ represents a wealth resource at time $t$, and $w_{t+1}$ represents the corresponding resource at a later time.

The notation does not yet specify what happened between the two states. That is important. A transition from $w_t$ to $w_{t+1}$ does not, by itself, tell us whether wealth increased, decreased, or remained unchanged.

Consider a piece of land.

It may remain the same physical property:

$$
w_t=w_{t+1}.
$$

It may instead be exchanged for another resource:

$$
w_t\rightarrow w'_{t+1}.
$$

The agent may use the land to produce another resource while continuing to control the land:

$$
w_t\rightarrow\{w_t,w'_{t+1}\}.
$$

Or the land may be destroyed or otherwise cease to be an economically realizable resource:

$$
w_t\rightarrow\varnothing.
$$

These are different transitions, but they all belong to the same general problem: determining what happens to wealth through time.

The transition is also not determined solely by the wealth resource itself. It occurs through the interaction of the agent's actions with conditions outside the agent's control. A more complete representation is therefore:

$$
w_t\xrightarrow{a_t,e_t}w_{t+1},
$$

where $a_t$ represents the agent's action and $e_t$ represents the relevant external conditions.

The same resource can therefore undergo different transitions depending on what the agent does and what occurs around it.

But the resource itself is only one part of the transition.

The previous article [*The Nature of Value?*][2] established that value is positional:

$$
V(x\mid P)=U(F(P,a_x))-U(P).
$$

Consequently, the value of a wealth resource cannot necessarily be treated as a fixed property of the resource. If either the resource or the agent's position changes, its value to the agent may change as well.

The transition of a resource and the transition of its value are therefore distinct:

$$
w_t\rightarrow w_{t+1}
$$

and

$$
V_t\rightarrow V_{t+1},
$$

where $V_t$ and $V_{t+1}$ denote the resource's value to the agent at the respective times.

The resource may change:

$$
w_t\neq w_{t+1},
$$

while its value to the agent remains unchanged:

$$
V_t=V_{t+1}.
$$

Conversely, the resource may remain substantially unchanged while its value changes:

$$
w_t=w_{t+1}
$$

while

$$
V_t\neq V_{t+1}.
$$

Both may change simultaneously.

This distinction matters because a change in the resource is not necessarily a change in its value, and a change in value is not necessarily a change in the resource.

There is another distinction that follows directly from the definition of wealth.

Wealth requires both economic realizability and control. A transition can therefore affect not only the resource and its value, but also whether the resource remains wealth for the agent at all.

For example, an agent may transfer a resource to another agent:

$$
w_t^A\rightarrow w_{t+1}^B.
$$

The resource may continue to exist and may retain economic value, but it is no longer wealth controlled by agent $A$.

Likewise, a resource may remain physically intact while losing its economic realizability. Conversely, an economically realizable resource may become newly controlled by an agent:

$$
w\notin W_t^A
\rightarrow
w\in W_{t+1}^A.
$$

Thus, the transition of wealth is not simply a change in the market value of an object. It concerns the changing relationship between resources and the agent who controls them.

At this point, several distinct aspects of the transition have appeared:

$$
\boxed{
\begin{aligned}
\text{resource} &: \quad w_t\rightarrow w_{t+1}\\
\text{value} &: \quad V_t\rightarrow V_{t+1}\\
\text{control} &: \quad C_t\rightarrow C_{t+1}\\
\text{economic realizability} &: \quad E_t\rightarrow E_{t+1}.
\end{aligned}
}
$$

These aspects need not change together.

A resource can persist while its value changes. A resource can change form while preserving its value. A resource can retain its economic value while leaving the agent's control. A resource can remain under the agent's control while becoming economically unrealizable.

This gives us a more precise starting point for the wealth problem.

The question is not initially whether wealth has “grown” or “declined.” Those are conclusions about a transition that require us to specify what changed and how the resulting state is being compared with the initial state.

The more fundamental object is the transition of the agent's wealth:

$$
W_t\rightarrow W_{t+1}.
$$

The individual resource transitions determine how this collection changes. To model the wealth problem, we must therefore characterize the possible resource transitions and establish how they affect the collection of resources controlled by the agent.

Only then can we determine which transitions constitute accumulation, transformation, appreciation, depreciation, preservation, consumption, loss, or growth.

The next question is therefore not yet **how to grow wealth**, but:

> **What kinds of transitions can wealth undergo?**

[2]: https://diogenesanalytics.com/blog/2026/08/17/what-is-value "The Nature of Value"

## Resource Transitions

The transition

$$
w_t\rightarrow w_{t+1}
$$

describes what happens to a wealth resource through time. To understand the wealth problem, we must first characterize the different ways in which this transition can occur.

The simplest possibility is that the resource persists.

An agent controls a resource at time $t$ and continues to control the same resource at time $t+1$:

$$
w_t\rightarrow w_{t+1}.
$$

A piece of land, for example, may remain under the agent's control without any fundamental change in the resource itself.

This is **persistence**. The resource remains available to the agent through time.

But a resource does not necessarily remain in the same form.

An agent may exchange one resource for another:

$$
w_t\rightarrow w'_{t+1}.
$$

For example, an agent may exchange money for equipment. The original resource is no longer controlled by the agent, but another economically realizable resource is acquired in its place.

This is a **transformation** of wealth. The resource held by the agent changes, although the transition alone does not establish whether the agent's wealth has increased or decreased.

The transition becomes different when the original resource remains while an additional resource is acquired:

$$
w_t\rightarrow\{w_t,w'_{t+1}\}.
$$

A rental property may remain under the agent's control while generating rental income. The property persists, while an additional economic resource becomes available.

This is an **addition** to the agent's collection of wealth resources.

The important feature is that the transition does not replace the original resource. The resulting collection contains something that was not present before.

The opposite transition is possible as well:

$$
w_t\rightarrow\varnothing.
$$

The resource may be consumed, destroyed, or otherwise cease to be an economically realizable resource controlled by the agent.

This is a **removal** of the resource from the agent's wealth.

These mechanisms can have different causes, even though they produce the same structural result: the original resource is no longer available afterward.

A resource can also leave one agent while continuing to exist as wealth for another:

$$
w_t^A\rightarrow w_{t+1}^B.
$$

This is a **transfer**.

The resource itself has not necessarily been destroyed or consumed. Instead, control has changed. What was wealth for agent $A$ can become wealth for agent $B$.

The reverse process, from the perspective of the receiving agent, is **acquisition**.

A resource that was not previously controlled by an agent can enter that agent's wealth:

$$
w\notin W_t^A
\rightarrow
w\in W_{t+1}^A.
$$

This is an **acquisition**. Acquisition describes a resource entering the collection controlled by the agent, regardless of whether it was newly produced, exchanged for another resource, or transferred from another agent.

These transitions can also occur together.

An agent might exchange one resource for another:

$$
w_1^A\rightarrow w_2^A.
$$

It might produce an additional resource while retaining the resources used in production:

$$
W_t^A\rightarrow W_t^A\cup\{w'_{t+1}\}.
$$

It might transfer one resource while acquiring another. In that case, the agent loses control of one resource and gains control of another within the same overall transition.

These examples illustrate an important distinction. **Transformation, addition, removal, transfer, and acquisition describe different aspects of resource transitions, and a single event may involve more than one of them.** They are not necessarily mutually exclusive categories.

The important point is that these are descriptions of **resource transitions**, not yet measurements of whether wealth has increased or decreased.

Consider the transformation:

$$
\textdollar100{,}000\text{ cash}\rightarrow \textdollar100{,}000\text{ land}.
$$

The resource controlled by the agent has changed. But the transition alone does not establish whether the agent has more or less wealth.

Likewise, consider:

$$
\text{land}\rightarrow\text{land}+\text{rent}.
$$

An additional resource has appeared while the original resource remains. This establishes a particular structure of transition, but determining whether the agent's wealth has increased requires a way to compare the resulting collection of resources with the original collection.

The same issue appears when a resource remains unchanged but its economic circumstances change.

A property may remain the same property while becoming more or less economically valuable. Thus, the transition of the resource itself does not completely determine the transition in its economic significance.

We can therefore distinguish the resource transition from the change in its value to the agent:

$$
w_t\rightarrow w_{t+1}
$$

and

$$
V_t\rightarrow V_{t+1},
$$

where $V_t$ and $V_{t+1}$ denote the resource's value to the agent at the respective times.

The two transitions are related, but neither determines the other in general.

This gives us a useful preliminary classification:

$$
\boxed{
\begin{aligned}
\text{Persistence} &: \quad w_t\rightarrow w_{t+1}\\
\text{Transformation} &: \quad w_t\rightarrow w'_{t+1}\\
\text{Addition} &: \quad w_t\rightarrow\{w_t,w'_{t+1}\}\\
\text{Removal} &: \quad w_t\rightarrow\varnothing\\
\text{Transfer} &: \quad w_t^A\rightarrow w_{t+1}^B\\
\text{Acquisition} &: \quad w\notin W_t^A\rightarrow w\in W_{t+1}^A.
\end{aligned}
}
$$

These categories describe structural changes that can occur to resources under an agent's control. They do not yet tell us whether the agent's wealth has grown, declined, or remained unchanged.

That question requires something additional.

The agent may move from one collection of heterogeneous resources to another:

$$
W_t\rightarrow W_{t+1}.
$$

To determine whether this represents an increase or decrease in wealth, the two collections must be comparable. In particular, we need a way to evaluate different resources and determine how their combined economic significance changes when the collection changes.

The next problem is therefore:

> **How can different collections of wealth resources be compared?**

## A Common Standard for Wealth

We have established that an agent may move from one collection of wealth resources to another:

$$
W_t\rightarrow W_{t+1}.
$$

But these collections may contain completely different resources.

An agent might begin with:

$$
W_1=\{\text{cash},\text{land},\text{equipment}\}
$$

and later possess:

$$
W_2=\{\text{securities},\text{inventory},\text{property}\}.
$$

The resources in these collections are heterogeneous. There is no obvious comparison between the collections simply from their composition.

We cannot determine that one collection contains more wealth than another by counting its resources. Nor can we determine it merely by identifying whether individual resources have been added or removed.

To compare the collections, we need some common basis.

Suppose we could represent each resource in terms of a common wealth asset $x$. If the resources can be exchanged for quantities of $x$, then each collection can be represented in terms of that asset.

For example, if the resources in $W_1$ can be exchanged for quantities $x_1,x_2,\ldots,x_n$, their combined monetary equivalent can be expressed as:

$$
x(W_1)=x_1+x_2+\cdots+x_n.
$$

Likewise, if the resources in $W_2$ can be exchanged for quantities $x'_1,x'_2,\ldots,x'_m$, their combined equivalent is:

$$
x(W_2)=x'_1+x'_2+\cdots+x'_m.
$$

Under these conditions, the collections can be compared:

$$
x(W_1)>x(W_2),
$$

$$
x(W_1)=x(W_2),
$$

or

$$
x(W_1)<x(W_2).
$$

The problem of comparing heterogeneous wealth therefore becomes a problem of representing heterogeneous resources in terms of a common wealth asset.

But such a conversion cannot simply be assumed.

To convert one resource into another requires an exchange relationship:

$$
w\leftrightarrow x.
$$

An exchange establishes that the two resources can be exchanged under some set of conditions. The quantity of $x$ obtainable for $w$ depends on those conditions.

This brings the problem back to value.

The previous article [*The Nature of Value*][2] established that value is positional:

$$
V(x\mid P)=U(F(P,a_x))-U(P).
$$

This function measures the change in an agent's utility associated with acquiring $x$ from position $P$. It explains why the value of an acquisition depends on the position of the agent making it.

However, the value of an acquisition to an agent and the monetary amount obtainable by exchanging a resource are different quantities. The former concerns the effect on the agent's position; the latter concerns an exchange relationship between resources.

For example, the same quantity of money may have different values to two agents because their positions differ. Yet both agents may be able to exchange a given quantity of land for approximately the same monetary amount under the same market conditions.

We therefore need a common basis for determining the monetary equivalents of heterogeneous resources.

Suppose:

$$
W_1\in P_1
$$

and

$$
W_2\in P_2.
$$

If we evaluate the utility associated with each collection relative to its respective owner's position, the resulting values need not be directly comparable:

$$
V(W_1\mid P_1)
\qquad\text{and}\qquad
V(W_2\mid P_2).
$$

A difference between these values could arise from differences in the collections, differences in the owners' positions, or both.

For the purpose of comparing their economic magnitudes, we need a common reference for valuation.

Let that reference be the market position:

$$
P_m.
$$

This is a reference representation of the economic conditions under which resources can be exchanged, rather than a literal agent whose utility is being evaluated.

The market establishes exchange relationships between resources. For a resource $w$, let

$$
p_m(w)
$$

denote the monetary amount obtainable for that resource under the reference market conditions represented by $P_m$.

The value of $p_m(w)$ depends on the resource and the conditions of exchange. It is not the resource's intrinsic value, nor is it the positional utility value $V(w\mid P)$ defined earlier.

The market reference is useful because it provides a common basis for expressing heterogeneous resources in monetary terms.

There remains a further requirement.

The common representation must itself be a form of wealth.

The [previous article][1] established that wealth is an economically realizable resource that an agent can control and retain through time. Money satisfies this definition. Money is therefore not merely a unit of measurement imposed from outside wealth. It is itself one form that wealth can take.

We can therefore use money as the common wealth asset into which heterogeneous resources are represented.

For a resource $w$, the market may establish an exchange relationship of the form:

$$
w\leftrightarrow p_m(w),
$$

where $p_m(w)$ is the monetary equivalent of the resource under the reference market conditions.

For a collection of resources

$$
W=\{w_1,w_2,\ldots,w_n\},
$$

we can define its monetary valuation as:

$$
\boxed{
M(W\mid P_m)=\sum_{i=1}^{n}p_m(w_i)
}
$$

This expression assumes that the monetary values of the individual resources can be added. In practice, the result may depend on quantities held, transaction costs, and the conditions under which the resources can be sold. The function $M$ therefore represents a valuation under specified market conditions, not a guarantee that the entire collection can be liquidated for exactly that amount.

The purpose of this representation is not to claim that the resources are intrinsically equal to money. It expresses their combined monetary equivalent under a common reference.

Two heterogeneous collections can therefore be represented as:

$$
M(W_1\mid P_m)
$$

and

$$
M(W_2\mid P_m).
$$

They can now be compared because both have been represented in terms of the same wealth asset.

We can determine:

$$
M(W_1\mid P_m)>M(W_2\mid P_m),
$$

$$
M(W_1\mid P_m)=M(W_2\mid P_m),
$$

or

$$
M(W_1\mid P_m)<M(W_2\mid P_m).
$$

The comparison is no longer between heterogeneous collections of assets. It is between their monetary valuations under the same reference conditions.

This gives us the basis that was missing from the original resource transition.

An agent may move from:

$$
W_t\rightarrow W_{t+1}
$$

while the composition of the two collections changes completely. But if both collections can be valued under the same market conditions, their relative monetary magnitudes can be determined:

$$
M(W_t\mid P_m)
\qquad\text{and}\qquad
M(W_{t+1}\mid P_m).
$$

The market reference therefore does not provide an absolute measure of value. It provides a common basis for expressing heterogeneous forms of wealth in monetary terms.

The choice of $P_m$ is consequently a valuation convention grounded in economic exchange, rather than an intrinsic property of wealth itself.

What matters for comparison is not that $P_m$ is the only possible reference position, but that the reference conditions are sufficiently well specified and applied consistently to the collections being compared.

We can now return to the question that began this investigation.

If:

$$
W_t\rightarrow W_{t+1},
$$

then the two wealth states can be compared through:

$$
M(W_t\mid P_m)
\qquad\text{and}\qquad
M(W_{t+1}\mid P_m).
$$

Only now do we have a common basis for determining whether the transition represents an increase, decrease, or no change in the monetary valuation of wealth.

The next question is therefore:

> **When does a transition from $W_t$ to $W_{t+1}$ constitute growth in wealth?**

[1]: https://diogenesanalytics.com/blog/2026/09/21/defining-wealth "Defining Wealth"

[2]: https://diogenesanalytics.com/blog/2026/08/17/what-is-value "The Nature of Value"

## Wealth Growth

The preceding section established a common basis for comparing collections of wealth resources. By representing heterogeneous collections in monetary terms under common reference conditions, we can compare collections that would otherwise be difficult to evaluate directly.

Let the wealth controlled by an agent at time $t$ be represented by $W_t$. Its monetary representation under the market conditions at that time is:

$$
M_t=M(W_t\mid P_{m,t}).
$$

At a later time, the agent controls another collection of resources, $W_{t+1}$, represented by:

$$
M_{t+1}=M(W_{t+1}\mid P_{m,t+1}).
$$

The monetary representation of each collection reflects both the resources controlled by the agent and the market conditions under which those resources are valued.

We can compare these representations to determine how the agent's measured wealth has changed.

If:

$$
M_{t+1}>M_t,
$$

the agent's measured wealth has increased.

If:

$$
M_{t+1}=M_t,
$$

the agent's measured wealth has remained unchanged.

And if:

$$
M_{t+1}<M_t,
$$

the agent's measured wealth has decreased.

We can summarize these conditions as:

$$
\boxed{
\begin{aligned}
\Delta M>0 &\Rightarrow \text{measured wealth growth}\\
\Delta M=0 &\Rightarrow \text{measured wealth preservation}\\
\Delta M<0 &\Rightarrow \text{measured wealth decline}
\end{aligned}
}
$$

where:

$$
\Delta M=M_{t+1}-M_t.
$$

These conditions provide a way to distinguish growth, preservation, and decline under the chosen monetary valuation. But they also reveal an important distinction: the change in a collection of resources is not necessarily the same as the change in the wealth represented by that collection.

Consider an agent who exchanges $\textdollar100{,}000$ in cash for a parcel of land.

The resource transition is:

$$
\textdollar100{,}000\text{ cash}
\rightarrow
\text{land}.
$$

The collection of resources has changed. The agent no longer holds the original cash and instead controls a different wealth resource.

Suppose, however, that the land is equivalent to $\textdollar100{,}000$ in monetary wealth under the same reference conditions. Then:

$$
M(W_t\mid P_m)=\textdollar100{,}000
$$

and:

$$
M(W_{t+1}\mid P_m)=\textdollar100{,}000.
$$

The composition of wealth has changed, but its measured quantity has not.

The agent has transformed its wealth without increasing or decreasing it under the chosen reference.

Now consider a different transition. The agent retains the land while acquiring rental income:

$$
\text{land}
\rightarrow
\text{land}+\text{rental income retained}.
$$

An additional resource has appeared. But whether the agent's wealth has grown depends on the resulting collection, not simply on the fact that something has been added.

Rental income that remains under the agent's control can increase its wealth. But that increase may be offset by maintenance costs, taxes, or other losses. Alternatively, the property itself might decline in market value. The resulting collection could represent more wealth, the same amount, or less.

The structure of the resource transition does not determine the outcome.

The same principle applies to removal. An agent might sell one resource and use the proceeds to acquire another. The original resource disappears from the collection, but the transition need not constitute a decline in wealth. Conversely, an agent might retain every resource it owns while their market valuations fall.

We must therefore distinguish two questions:

$$
\boxed{
\begin{aligned}
\text{Resource transition} &: \quad W_t\rightarrow W_{t+1}\\
\text{Change in measured wealth} &: \quad \Delta M
\end{aligned}
}
$$

The first describes the transition between collections of resources. The second describes how the monetary valuations of those collections compare.

There is, however, an important qualification.

The comparison depends on the market conditions used for valuation. Because those conditions can change, the monetary representation of a resource may change even if the resource itself remains unchanged.

For example, a parcel of land may remain physically identical while its market valuation rises or falls. Its monetary representation changes despite the absence of a corresponding transformation in the physical resource.

To distinguish changes in the resources held from changes in their market valuations, we can evaluate both collections under the same reference conditions:

$$
\Delta M^{(t)}
=
M(W_{t+1}\mid P_{m,t})
-
M(W_t\mid P_{m,t}).
$$

Here, both collections are valued under the market reference conditions at time $t$. This comparison isolates the difference between the two collections under that common reference, rather than incorporating subsequent changes in market valuation.

By contrast, the change between the monetary valuations prevailing at the two times is:

$$
\Delta M
=
M(W_{t+1}\mid P_{m,t+1})
-
M(W_t\mid P_{m,t}).
$$

This measures the change in the agent's wealth at the market valuations prevailing at each time. It can reflect both changes in the resources controlled and changes in the market conditions under which they are valued.

Consequently, an increase in measured wealth does not necessarily mean that the agent acquired additional resources, improved their productive capacity, or made a successful decision. It may instead reflect a change in the market's valuation of resources already controlled.

Likewise, a decrease in measured wealth does not necessarily mean that the agent made a poor decision. An agent may deliberately consume wealth to obtain something else of value, or accept a reduction in measured wealth in exchange for an improvement in its position.

The distinction between wealth and value remains essential.

$$
\text{Wealth}\neq\text{Value}.
$$

The monetary comparison provides a way to determine how a collection of wealth resources changes in measured magnitude under a common reference. It does not establish how desirable that change is to the agent.

We can therefore distinguish the growth of measured wealth from the improvement of position:

$$
\Delta M>0
$$

does not necessarily imply:

$$
U(P_{t+1})>U(P_t).
$$

And the reverse need not hold either. An agent's position may improve even as its measured wealth declines.

This brings us to the central result.

**Wealth growth, as measured monetarily, is an increase in the monetary representation of wealth, not merely a change in the resources that constitute it.** By comparing successive collections under a consistent valuation, we can determine whether the agent controls more, less, or the same amount of measured wealth, even when the composition of those collections changes.

But this still leaves the central management problem unresolved.

The agent does not merely observe transitions after they occur. It chooses actions that influence which transitions occur and which resources it will control in the future.

The next question is therefore:

> **How should an agent choose among the possible transitions of its wealth?**

## The Wealth Management Problem

We have established what wealth is, how collections of wealth resources can be compared, and how wealth can grow, diminish, or remain unchanged over time.

But these concepts do not, by themselves, tell an agent how to manage its wealth.

The agent must choose among possible transitions in its wealth, and those transitions have different consequences. One may preserve wealth while limiting its growth. Another may offer substantial growth while exposing the agent to significant losses. A third may sacrifice some potential growth in exchange for greater liquidity, allowing the agent to respond to future opportunities or obligations.

The problem is therefore not simply to maximize wealth. It is to determine how wealth should be managed through time.

Consider cash.

Cash is a form of wealth that offers considerable liquidity. An agent can generally deploy it quickly to meet obligations or acquire other resources. But cash may lose purchasing power through inflation, diminishing the quantity of goods and services it can command over time.

Other wealth resources present different trade-offs. Some may offer greater growth potential but be difficult to convert into cash quickly. Others may preserve purchasing power under certain conditions while exposing the agent to fluctuations in market value. Still others may offer attractive returns while introducing risks that threaten a substantial portion of the agent's wealth.

No single property adequately determines how an agent should hold its wealth.

The agent must therefore consider several interrelated concerns.

First, it must consider the preservation of wealth. A transition that diminishes wealth reduces the resources available for future use. A sufficiently large loss may impair the agent's ability to meet its obligations, pursue opportunities, or recover from subsequent losses.

Second, it must consider the growth of wealth. Preserving the existing collection of resources is not necessarily sufficient. The agent may seek to increase its wealth, both in magnitude and in the rate at which it grows.

Third, it must consider liquidity. Wealth that cannot be deployed when needed may be less useful than wealth that can be converted into the resources required to meet an obligation or pursue an opportunity. Maintaining liquidity, however, may involve sacrificing some potential growth.

These concerns can conflict. An action that increases the potential growth of wealth may also increase the risk of loss. An action that preserves liquidity may limit the resources committed to longer-term growth. An action that reduces one form of risk may introduce another.

The agent must therefore manage the relationships among these properties rather than optimize each independently.

There is also a broader consideration. The agent does not acquire and retain wealth for its own sake alone. Wealth matters because of what it enables the agent to do and the positions it can help the agent attain.

As established in [*The Nature of Value*][1], the value of a resource depends on the position in which it is evaluated. A resource that is useful in one position may be less useful in another. Consequently, a wealth-management decision cannot be evaluated completely by its effect on the measured quantity of wealth alone.

An agent may rationally exchange wealth for another resource, consume wealth to meet an important need, or accept lower expected growth to preserve the ability to respond to future circumstances. Such decisions may reduce measured wealth while improving the agent's position.

The wealth problem must therefore distinguish the management of wealth from the broader objective of improving position. The former concerns how the agent preserves, deploys, and grows its wealth. The latter concerns how those decisions contribute to the agent's overall circumstances and future possibilities.

We can now state the problem.

**The wealth problem is the problem of managing wealth through time by balancing its preservation, growth, liquidity, and other relevant properties while mitigating the risks of loss and ruin, in light of the agent's broader objectives.**

This formulation does not prescribe a universal allocation of wealth or a single strategy. The appropriate balance depends on the agent's position, obligations, available opportunities, and tolerance for risk. The same resource may warrant different treatment in different positions, and the same management strategy may produce different outcomes under different environmental conditions.

The problem is therefore a decision problem over possible wealth transitions.

At time $t$, let $P_t$ represent the agent's position and $W_t$ the collection of wealth resources it controls. The agent has a set of available actions:

$$
a_t\in A(P_t,W_t,E_t),
$$

where $E_t$ represents the relevant environmental conditions and $A(P_t,W_t,E_t)$ is the set of actions available under those conditions.

An action changes the resources the agent controls and may also change its broader position:

$$
W_{t+1}=G(W_t,a_t,E_t),
$$

$$
P_{t+1}=F(P_t,a_t,E_t).
$$

The function $G$ describes the resulting transition in the agent's wealth resources. The function $F$ describes the resulting transition in its overall position. Both depend on the chosen action and the relevant environment.

Each available action therefore leads to a possible next wealth state and position. These outcomes can differ in their monetary magnitude, liquidity, exposure to loss, and consequences for what the agent can do afterward.

The management problem is to choose an action from the available alternatives while accounting for these consequences and the agent's broader objectives.

The central question is now precise:

> **How can the competing consequences of possible wealth transitions be represented and evaluated so that an agent can make coherent wealth-management decisions?**

[1]: https://diogenesanalytics.com/blog/2026/08/17/what-is-value "The Nature of Value"

## Wealth Maximization

We begin by considering the objective of maximizing wealth.

At time $t$, let an agent control a collection of wealth resources $W_t$. The agent can choose among available actions, each of which may change the resources it controls and the wealth those resources represent.

Let $A(P_t,W_t,E_t)$ denote the set of actions available to the agent given its current position, wealth, and environmental conditions. The resulting collection of wealth resources depends on the action taken and the relevant environmental conditions:

$$
W_{t+1}=F_W(W_t,a_t,E_t),
$$

where $a_t\in A(P_t,W_t,E_t)$ and $E_t$ represents the environmental conditions relevant to the transition.

As established in the preceding sections, the resources within a collection may differ substantially in their form and properties. We therefore require a common measure to compare the wealth represented by different collections.

Let $M(W\mid P_m)$ denote the monetary wealth equivalent of collection $W$ under the specified market reference conditions $P_m$. We can use this measure to compare the wealth associated with the outcomes of alternative actions.

The immediate wealth-maximization problem is then to choose an available action that produces the greatest measured wealth in the next state:

$$
\boxed{
a_t^*=
\underset{a_t\in A(P_t,W_t,E_t)}{\operatorname{argmax}}
\ M\left(F_W(W_t,a_t,E_t)\mid P_m\right)
}
$$

This formulation establishes a clear objective. Given a current collection of wealth resources, a set of available actions, and the conditions under which those actions produce their consequences, the agent seeks the action that maximizes the measured wealth of the resulting collection.

The formulation is deliberately limited to the next transition. It compares the resulting wealth states without yet accounting for how the choice affects subsequent transitions.

To represent that limitation, consider two actions, $a_1$ and $a_2$, such that:

$$
M(W_{t+1}^{(1)}\mid P_m)
>
M(W_{t+1}^{(2)}\mid P_m).
$$

The first action produces more measured wealth at time $t+1$. But suppose it also leaves the agent with fewer resources available to meet an obligation at time $t+2$, or exposes the agent to a greater possibility of ruin before then. The action that produces the greater immediate wealth may consequently leave the agent worse positioned in the future.

A one-step comparison does not capture these differences. It evaluates the wealth of the resulting collection, not the sequence of transitions that follows from choosing it.

A further limitation concerns the measure itself. Maximizing monetary wealth does not necessarily maximize the value of the resulting position. An action may increase wealth while worsening other aspects of the agent's circumstances, just as an action that reduces wealth may improve them.

Wealth maximization therefore provides a starting point for modeling the wealth problem, but it does not, by itself, fully specify how wealth should be managed through time.

The next step is to examine the limitations of wealth maximization as a decision-making objective and determine what additional considerations are required to evaluate wealth transitions over time.

## The Limits of Wealth Maximization

Wealth maximization provides a clear objective, but its scope is limited. It evaluates the consequences of an action according to the measured wealth of the resulting collection of resources. It does not necessarily account for every consequence that matters to the agent.

Consider an agent that owns a property and has $\textdollar20{,}000$ in available cash. The property requires a repair costing $\$5{,}000$. The agent can either perform the repair now or postpone it.

Let $W_t$ represent the agent's current wealth collection. If the agent performs the repair, its cash decreases by $\textdollar5{,}000$, but the repair may preserve the property's value and prevent further deterioration. If the agent postpones the repair, it retains the cash for now, but the property's condition may deteriorate, eventually requiring a more expensive repair.

The immediate cash consequences are clear:

$$
C_{t+1}=
\begin{cases}
\$15{,}000 & \text{repair now},\\
\$20{,}000 & \text{postpone repair}.
\end{cases}
$$

But cash is only one component of the agent's wealth. To compare the two actions, we must consider the resulting collections of resources rather than cash alone.

Let $W_{t+1}^{(r)}$ denote the wealth collection after repairing the property and $W_{t+1}^{(p)}$ the collection after postponing the repair. Their measured wealth is:

$$
M_r=M(W_{t+1}^{(r)}\mid P_m)
$$

and

$$
M_p=M(W_{t+1}^{(p)}\mid P_m).
$$

The difference depends on the effects of each action on the property and on any subsequent costs. If postponing the repair causes sufficient deterioration, it is possible that:

$$
M_r>M_p.
$$

In that case, spending cash now preserves more measured wealth than retaining it. Even when the repair does not increase measured wealth, it may preserve the property's usefulness or prevent losses that would otherwise occur.

The immediate cash comparison therefore does not determine which action is preferable. The relevant comparison must account for the resulting wealth collections and, when the consequences extend beyond the next period, the subsequent transitions as well.

The same distinction arises when an agent chooses between alternative investments, maintains liquid reserves, or uses wealth to satisfy an obligation. The action that produces the greatest immediate monetary wealth need not produce the greatest wealth over a longer period, and the action that produces the greatest wealth need not produce the best overall outcome.

These differences expose two limitations of the immediate wealth-maximization model.

First, **the outcome depends on the time horizon**. An action that maximizes measured wealth at $t+1$ may produce a different result from an action evaluated over several subsequent periods. Resources may generate additional resources, incur costs, lose value, or enable actions that would otherwise be unavailable. Consequently, the wealth associated with an action cannot always be evaluated adequately by considering only its immediate result.

Second, **wealth is not the only component of the agent's position that matters**. An action may affect the agent's obligations, capabilities, knowledge, access to opportunities, and exposure to future losses. Some of these effects may influence future wealth, while others matter independently of their monetary consequences.

The second limitation is more fundamental than the first. Extending the time horizon can improve the evaluation of future wealth, but it does not resolve the problem of treating wealth as the ultimate objective. Even if an agent could determine which action would maximize its wealth over a specified period, that action would not necessarily maximize the value of the position it would occupy.

The distinction follows from the nature of value itself.

As established in [*The Nature of Value*][1], the value of a resource depends on how acquiring or using it changes the agent's position. The relevant question is not merely how much wealth an action produces, but what the action enables, what it costs, and how it changes the agent's circumstances and future possibilities.

We can therefore distinguish two objectives.

**Wealth maximization** evaluates actions according to their effect on measured wealth.

**Positional utility maximization** evaluates actions according to their effect on the agent's overall position.

Using the established utility function, the second objective can be expressed as a comparison between the positions resulting from alternative actions:

$$
U(P_{t+1})=U(F(P_t,a_t,E_t)).
$$

The first objective may be useful when the agent is specifically trying to increase its wealth. But it cannot serve as a universal decision rule, because the agent may have reasons to accept less wealth in exchange for a more valuable position.

This does not mean that wealth maximization and positional utility maximization are necessarily in conflict. An increase in wealth may improve the agent's position, and an action that maximizes wealth may also maximize positional utility. The distinction is that wealth maximization evaluates one particular consequence of an action, while positional utility considers its broader effects.

The immediate problem is therefore to establish what wealth maximization leaves unresolved. An agent must account for the consequences of losing wealth, the resources that remain available afterward, and its ability to use those resources when circumstances require it.

[1]: https://diogenesanalytics.com/blog/2026/08/17/what-is-value "The Nature of Value"

## Risk and Wealth Preservation

Maximizing measured wealth does not, by itself, establish how an agent should manage the possibility of loss. An action that offers greater growth may also expose the agent to losses that diminish its existing wealth or threaten its ability to pursue future objectives.

Consider two agents facing the same potential loss. The first holds $\textdollar100{,}000$ in wealth, while the second holds $\textdollar12{,}000$. Both suffer a loss of $\textdollar10{,}000$, leaving them with $\textdollar90{,}000$ and $\textdollar2{,}000$, respectively.

Let $M(W\mid P_m)$ denote the measured wealth of collection $W$ under the common market reference conditions $P_m$. The change in measured wealth is:

$$
\Delta M_t =
M(W_{t+1}\mid P_m)-M(W_t\mid P_m).
$$

For both agents:

$$
\Delta M_t=-\textdollar10{,}000.
$$

The relative losses, however, differ:

$$
\frac{\textdollar10{,}000}{\textdollar100{,}000}=10\%
$$

and

$$
\frac{\textdollar10{,}000}{\textdollar12{,}000}\approx83.3\%.
$$

For both agents, the monetary loss is identical. Its consequences, however, depend on their positions. If the second agent must pay an obligation of $\textdollar5{,}000$, its remaining wealth of $\textdollar2{,}000$ may be insufficient to meet that obligation, whereas the first agent may retain ample resources.

The same loss can therefore produce different consequences depending on the wealth remaining, the agent's obligations, and the actions still available to it.

Wealth preservation concerns maintaining the resources required to continue pursuing objectives through time. It does not require avoiding every loss. An agent may rationally accept a loss or expose resources to risk in pursuit of growth. The relevant question is whether the resulting position preserves the agent's ability to meet its obligations and pursue future objectives.

A sufficiently severe loss may produce **ruin**: a position in which the agent can no longer meet critical obligations or continue pursuing its objectives through its existing resources and available actions.

Ruin does not necessarily mean that monetary wealth has reached zero. An agent may retain valuable assets yet lack the resources needed to meet an immediate obligation. Conversely, an agent with little wealth may remain viable if its obligations are limited and its future access to resources is secure.

We can represent this constraint by letting $L_t$ denote the resources required to meet an obligation at time $t$, and $Q_t$ the resources that the agent can actually deploy to meet it by the required time. The obligation can be met when:

$$
Q_t\geq L_t.
$$

If:

$$
Q_t<L_t,
$$

the agent cannot meet the obligation using the resources available within the required time. Whether this constitutes ruin depends on the obligation's significance and whether other feasible actions remain available.

This distinction matters because $M(W_t\mid P_m)$ measures the monetary equivalent of the agent's wealth collection, whereas $Q_t$ concerns the resources that can actually be deployed when required. The two quantities need not be equal. An agent may own assets with substantial monetary value but be unable to convert them into the required resources quickly enough.

The significance of a loss is therefore not determined by its monetary magnitude alone. It also depends on how the loss changes the agent's subsequent position and the constraints under which it must act.

This creates a trade-off between wealth growth and the preservation of future options. An action that offers substantial growth may also expose the agent to a loss that restricts its subsequent choices. Conversely, excessive caution may prevent the agent from pursuing opportunities that would improve its position.

The agent must therefore evaluate wealth transitions in relation to both their measured outcomes and their consequences for future action. Maximizing measured wealth alone does not determine which risks are acceptable.

Risk matters because a transition can diminish wealth, threaten critical obligations, or eliminate future possibilities. The appropriate decision depends on the agent's position and objectives, not simply on the potential gain or loss.

But even when an agent accounts for the consequences of loss, another constraint remains. Its wealth may be sufficient in measured value yet unavailable in the form or within the time required to act.

The agent must therefore consider not only the wealth it controls and the risks to which it is exposed, but also its ability to deploy that wealth when needed.

## Liquidity and the Ability to Act

Equal measured wealth does not imply equal ability to act. An agent holding $\textdollar50{,}000$ in cash and another holding a property worth $\textdollar50{,}000$ may have equivalent measured wealth but different abilities to meet immediate obligations or pursue time-sensitive opportunities.

$$
M(W_t^{(1)}\mid P_m) = M(W_t^{(2)}\mid P_m)
\not\Rightarrow
A(P_t^{(1)},W_t^{(1)},E_t) =
A(P_t^{(2)},W_t^{(2)},E_t).
$$

**Liquidity** is the ability to deploy wealth in the form and within the time required for an action. It depends on the resources held, the action to be performed, the environmental conditions, and the time available.

Let $A_\tau(P_t,W_t,E_t)$ denote the actions feasible within time $\tau$, given the agent's position, wealth, and environment. An obligation or opportunity requiring action $a$ is feasible only if:

$$
a\in A_\tau(P_t,W_t,E_t),
$$

and its other resource and execution constraints are satisfied.

Illiquidity can therefore constrain action without reducing measured wealth. An agent may possess sufficient wealth to satisfy an obligation but lack the ability to deploy it before the obligation is due.

Liquidity also competes with other uses of wealth. Cash provides immediate access but may sacrifice investment returns and purchasing power. Less-liquid holdings may offer income, utility, or growth while restricting the actions available within a given time.

The management problem is consequently not to maximize liquidity independently, but to preserve sufficient access to resources while pursuing other objectives.

Risk and liquidity interact. Losses diminish available resources, while illiquidity can prevent an agent from meeting obligations even when its measured wealth remains unchanged. A loss can also reduce the set of feasible actions, while an inability to deploy wealth in time can turn an otherwise manageable obligation into a critical constraint.

Wealth management must therefore account for measured wealth, risk, and the constraints governing its deployment. These considerations are interdependent: an action can increase measured wealth while reducing liquidity, preserve liquidity while limiting growth, or reduce exposure to one risk while increasing exposure to another.

The remaining question is how to evaluate these considerations jointly in relation to the agent's position.

That requires a broader decision criterion: **positional utility maximization**.

## Positional Utility Maximization

We have established three considerations in wealth management: the amount of wealth an agent controls, the risks to which it is exposed, and its ability to deploy resources when needed. These considerations interact, and their importance depends on the agent's position.

As established in [*Towards a Universal Framework for Decision Making*][1], an agent's position $P_t$ contains the information relevant to its decision-making. An action transforms that position according to:

$$
P_{t+1}=F(P_t,a_t,E_t),
$$

where $E_t$ represents the relevant environmental conditions.

The utility of a position is:

$$
U(P)=A(P)-T(P)+D^+(P)-D^-(P),
$$

where $A(P)$ represents advantages, $T(P)$ costs, $D^+(P)$ the structural diversity of paths to success, and $D^-(P)$ the structural diversity of paths to failure.

The agent can therefore evaluate an action by the utility of the resulting position:

$$
U(P_{t+1})=U\bigl(F(P_t,a_t,E_t)\bigr).
$$

For a single transition, positional utility maximization selects an available action that maximizes the utility of the resulting position:

$$
\boxed{
a_U^*=
\underset{a_t\in\mathcal{A}(P_t,W_t,E_t)}{\operatorname{argmax}}
\ U\bigl(F(P_t,a_t,E_t)\bigr)
}
$$

Wealth maximization instead selects the action that maximizes the measured wealth of the resulting collection:

$$
\boxed{
a_W^*=
\underset{a_t\in\mathcal{A}(P_t,W_t,E_t)}{\operatorname{argmax}}
\ M\bigl(F_W(W_t,a_t,E_t)\mid P_m\bigr)
}
$$

Both objectives evaluate the consequences of an action, but they evaluate different outcomes.

The distinction is that:

$$
\underset{a_t}{\operatorname{argmax}}
\ M\bigl(F_W(W_t,a_t,E_t)\mid P_m\bigr)
\quad\not\equiv\quad
\underset{a_t}{\operatorname{argmax}}
\ U\bigl(F(P_t,a_t,E_t)\bigr).
$$

The objectives may identify the same action, but need not. Wealth contributes to positional utility through the resources and opportunities it provides, while its management also affects costs, obligations, risks, and available future actions.

Consequently, the same wealth transition can have different utility in different positions:

$$
U\bigl(F(P_1,a,E)\bigr)
\neq
U\bigl(F(P_2,a,E)\bigr),
$$

even when the action produces the same measured change in wealth.

An agent with substantial reserves may be able to accept a risky investment that would threaten another agent's ability to meet critical obligations. Likewise, an agent facing an immediate obligation may rationally retain liquid resources rather than commit them to an investment with greater growth potential.

The relevant decision depends not only on the wealth transition but also on the position from which the action is taken and the position it produces.

**The wealth-management objective is therefore to select wealth transitions according to their contribution to positional utility, rather than to maximize measured wealth independently of the agent's circumstances.**

This formulation establishes the objective for an individual transition. It does not yet specify how an agent should evaluate sequences of transitions over time, account for uncertain outcomes, or enforce constraints on obligations and ruin. Those considerations must be incorporated into the broader management problem.

We can now bring the wealth transition, its constraints, and the agent's positional utility together into a unified mathematical formulation of the wealth-management problem.

[1]: https://diogenesanalytics.com/blog/2026/03/05/universal-decision-making-framework "Towards a Universal Framework for Decision Making"

## The Unified Wealth Management Model

We have established that wealth management involves more than maximizing the measured quantity of wealth. An agent must choose among possible wealth transitions while accounting for their consequences for its position, its ability to meet obligations, and its future options.

We can now bring these considerations together into a single decision problem.

At time $t$, let the agent's state be represented by its position $P_t$ and its collection of wealth resources $W_t$. The environment is represented by $E_t$. The agent selects an action from the set of actions available to it:

$$
a_t\in\mathcal{A}(P_t,W_t,E_t).
$$

The action produces a transition in the agent's wealth:

$$
W_{t+1}=F_W(W_t,a_t,E_t),
$$

and a corresponding transition in its position:

$$
P_{t+1}=F(P_t,a_t,E_t).
$$

The two transitions describe different aspects of the same decision. The first determines which wealth resources the agent controls after the action. The second determines the resulting position, including the advantages, costs, and future possibilities associated with that outcome.

The agent must choose actions in light of both.

### The objective

The utility of a position is:

$$
U(P)=A(P)-T(P)+D^+(P)-D^-(P).
$$

The agent therefore seeks to select actions that improve its position according to this utility function, rather than maximizing measured wealth independently of its consequences.

For a planning horizon ending at time $T$, the decision problem can be expressed as:

$$
\boxed{
\begin{aligned}
\max_{a_t,\ldots,a_{T-1}}\quad & U(P_T)\\
\text{subject to}\quad
&W_{k+1}=F_W(W_k,a_k,E_k),\\
&P_{k+1}=F(P_k,a_k,E_k),\\
&a_k\in\mathcal{A}(P_k,W_k,E_k),
\qquad k=t,\ldots,T-1.
\end{aligned}
}
$$

This formulation assumes that the relevant environmental conditions and transitions are known and that the agent evaluates the resulting position at the end of the planning horizon. It provides a deterministic starting point for the wealth-management problem.

The objective is not to maximize the monetary value of the final wealth collection directly. Instead, the monetary representation of wealth contributes to the position from which utility is evaluated. Wealth matters because of the resources it provides, the obligations it enables the agent to meet, and the future actions it makes possible.

### The constraints

The objective alone does not determine which transitions are feasible or acceptable. The agent must also account for the constraints imposed by its obligations and its ability to deploy resources.

Let $Q_k$ denote the resources that can be deployed to meet an obligation at time $k$, and let $L_k$ denote the resources required to meet that obligation. A necessary condition for meeting it is:

$$
Q_k\geq L_k.
$$

This condition must hold at the time the obligation falls due. A wealth collection may have substantial monetary value while failing to satisfy the condition if its resources cannot be converted into the required form in time.

The agent must also avoid transitions that leave it unable to continue pursuing its objectives. Let $\mathcal{S}_{\mathrm{viable}}$ denote the set of positions from which the agent can continue to meet its critical obligations and retain feasible paths toward its objectives. The viability constraint is:

$$
P_k\in\mathcal{S}_{\mathrm{viable}}.
$$

The precise definition of this set depends on the agent's obligations, available resources, environment, and feasible actions. It cannot be inferred from monetary wealth alone.

These constraints distinguish a desirable outcome from a feasible one. An action may offer substantial potential utility yet be unavailable because it violates a critical obligation or leaves the agent in a nonviable position.

The unified problem must therefore select the best available transition without disregarding the conditions required for the agent to continue operating.

### The resulting decision problem

The wealth-management problem can now be stated as the selection of a sequence of feasible actions that produces the most desirable resulting position while respecting the constraints imposed by obligations and viability.

The model combines three elements:

- **Wealth transitions** determine which resources the agent controls through time.
- **Constraints** determine which transitions remain feasible and which outcomes must be avoided.
- **Positional utility** evaluates the resulting position in light of the agent's broader objectives.

These elements are interdependent. A transition can increase measured wealth while violating an obligation, preserve wealth while restricting future actions, or reduce wealth while improving the agent's position. The appropriate decision depends on the resulting position and the constraints governing the transitions available afterward.

The model also makes clear why wealth maximization is insufficient as a universal objective. Maximizing measured wealth considers one property of the resulting collection. Wealth management must instead account for how the collection affects the agent's position, the constraints it faces, and the actions it can take in the future.

This gives us a general mathematical structure for the wealth-management problem. It does not prescribe a universal allocation of resources or a single strategy. Those depend on the agent's position, objectives, obligations, and environment.

The remaining challenge is to determine how the model should account for uncertainty in future transitions. An agent rarely knows with certainty which consequences an action will produce, and a strategy that is optimal under one assumed sequence of outcomes may fail under another.

The next step is therefore to examine how uncertainty changes the wealth-management problem.

## The Limits of the Model

The unified model establishes the wealth-management problem as a constrained optimization over a sequence of actions. It specifies how wealth and position change, which actions are available, and how the resulting position is evaluated.

However, formulating the problem does not establish how to solve it.

The agent must still determine which sequence of actions produces the greatest positional utility over the planning horizon. That requires more than evaluating individual actions. Each action changes the wealth collection and the resulting position, which in turn determine the actions available at subsequent times.

The decision must therefore account for the relationship between successive transitions:

$$
\begin{aligned}
P_{k+1}&=F(P_k,a_k,E_k),\\
W_{k+1}&=F_W(W_k,a_k,E_k),\\
a_k&\in\mathcal{A}(P_k,W_k,E_k).
\end{aligned}
$$

The difficulty is that an action's consequences extend beyond the immediate transition. An action that improves the current position may restrict future actions, while an action that reduces current wealth may create opportunities that improve the eventual position. The value of a decision must therefore be evaluated in relation to the transitions that follow it.

The model also depends on having sufficiently defined transition functions, feasible action sets, and utility evaluations. Without these, the optimization problem cannot produce a determinate solution.

We have thus established the structure of the wealth-management problem, but not a general procedure for solving it.

The next step is to develop the transition model itself. We must determine how individual wealth-management actions change the resources an agent controls, how those changes affect its position, and how the resulting transitions can be used to derive an optimal sequence of actions.

This moves the investigation from defining the wealth problem toward solving it.

## Conclusion

We have defined wealth as a collection of economically realizable resources that an agent can control and retain through time. We have examined how these resources change through actions and environmental conditions, how their monetary value can be measured, and why maximizing that value alone is insufficient to determine the best course of action.

Wealth management is ultimately a problem of choosing transitions. Each action changes the resources an agent controls and can alter its obligations, available options, and ability to act in the future. The consequences must therefore be evaluated in relation to the agent's resulting position.

We can express the problem as selecting a sequence of feasible actions that maximizes positional utility over a planning horizon:

$$
\begin{aligned}
\max_{a_t,\ldots,a_{T-1}}\quad & U(P_T)\\
\text{subject to}\quad
&W_{k+1}=F_W(W_k,a_k,E_k),\\
&P_{k+1}=F(P_k,a_k,E_k),\\
&a_k\in\mathcal{A}(P_k,W_k,E_k).
\end{aligned}
$$

This formulation establishes the objective, transitions, and constraints of the wealth-management problem. It does not yet provide a general method for finding the optimal sequence of actions.

To develop such a method, we must first construct a model that describes how specific actions change the resources an agent controls and the position that results. With that model, we can begin evaluating alternative decisions, comparing their consequences, and identifying strategies that improve the agent's position under the conditions it faces.

The purpose of this investigation is not merely to maximize wealth, but to understand how wealth can be managed as a means of improving position. The next step is to develop the transition model needed to reason about actual wealth-management scenarios.
