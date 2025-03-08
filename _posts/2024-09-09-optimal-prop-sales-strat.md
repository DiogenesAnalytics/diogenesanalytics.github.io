---
layout: article
title: Optimal Property Selling Option
custom_css: article.css
include_mathjax: true
---
## Context
When it comes time to sell your property, there really are only *3 types* of options available for you to use:
1. Agents
2. FSBO
3. Cash Buyers

To clarify, *option 1* simply involves working with a *real estate agent* to handle all the necessary work involved in selling *your* property. *Option 2* is literally **you** sell the property yourself (and handle all the necessary work), hence `FSBO` means *For Sale By Ower*. And finally, *option 3* involves selling the property directly to what is known as a *cash buyer* but is basically a *real estate investment* company. That is really what you are considering *when* you are looking to sell your property.

## Problem Defined
But really, when we look at the underlying differences between these three **types** of options, we see that the differences are only *numerical*:

$$
\begin{align*}
P_{agent} &= C_m \cdot (1 - (c_a + c_{closing})) \\
P_{fsbo} &= C_m \cdot (1 - (c_b + c_{closing})) \\
P_{cash} &= C_m \cdot ( 1 - (d_c + c_{closing}))
\end{align*}
$$

The different $P$ values stand for *profit* made from selling the property (e.g. profit from selling with an *agent* vs. *fsbo* vs. *cash buyer*). The $C_m$ is the *market value* of your property, and the $c_a$ and $c_b$ variables are the *buyer* and *seller* agent commissions. Finally the $d_c$ value is the *discount %* that the *cash buyer* will take (i.e. the *percent difference* between the price they offer you and the market value $C_m$).

We can further simplify things by expressing this in terms of a *system of linear equations*:

$$
\mathbf{P} = C_m \cdot 
\begin{bmatrix} 
1 - (c_a + c_{\text{closing}}) \\
1 - (c_b + c_{\text{closing}}) \\
1 - (d_c + c_{\text{closing}})
\end{bmatrix}
$$

Where $P$ is the *profit vector*:

$$
\mathbf{P} = 
\begin{bmatrix} 
P_{\text{agent}} \\ 
P_{\text{fsbo}} \\ 
P_{\text{cash}} 
\end{bmatrix}
$$

## Maximum Profit
The simplest application of the above *problem definition* is to find the *maximum element* in the *profit vector* $\mathbf{P}$:

$$
\max(\mathbf{P}) = \max
\begin{bmatrix} 
p_1 \\
p_2 \\
p_3 \\
p_4 \\
\vdots
\end{bmatrix}
$$

Now imagine we have *multiple* options: several *agents*, a few *cash buyers*, and of course *fsbo*. We can just collect all those *equations* in a matrix like we did before, and use *linear algebra* to calculate the *profit vector* like so:

$$
\boldsymbol{P} = \boldsymbol{S} \cdot \boldsymbol{C}
$$

Where $\mathbf{C}$ represents the *cost matrix* with $x_i$ and $y_i$ variables representing the *commission/discount percent* and *closing costs* respectively:

$$
\mathbf{C} =
\begin{bmatrix} 
1 -x_1 -y_1 \\
1 -x_2 -y_2 \\
1 -x_3 -y_3 \\
1 -x_4 -y_4 \\
\vdots
\end{bmatrix}
$$


and $\mathbf{S}$ is the *diagonal matrix* representing the different *selling prices* that the property will be sold for (as opposed to $C_m$ which is just the *market value* of the property):

$$
\mathbf{S} =
\begin{bmatrix} 
s_1 & 0 & 0 & 0 & \cdots \\
0 & s_2 & 0 & 0 & \cdots \\
0 & 0 & s_3 & 0 & \cdots \\
0 & 0 & 0 & s_4 & \cdots \\
\vdots & \vdots & \vdots & \vdots & \ddots
\end{bmatrix}
$$

Put it all together and you have:

$$
\begin{align*}
    \begin{bmatrix} 
    p_1 \\
    p_2 \\
    p_3 \\
    p_4 \\
    \vdots
    \end{bmatrix} &=
    \begin{bmatrix} 
    s_1 & 0 & 0 & 0 & \cdots \\
    0 & s_2 & 0 & 0 & \cdots \\
    0 & 0 & s_3 & 0 & \cdots \\
    0 & 0 & 0 & s_4 & \cdots \\
    \vdots & \vdots & \vdots & \vdots & \ddots
    \end{bmatrix}
    \cdot
    \begin{bmatrix} 
    1 -x_1 -y_1 \\
    1 -x_2 -y_2 \\
    1 -x_3 -y_3 \\
    1 -x_4 -y_4 \\
    \vdots
    \end{bmatrix} \\
    &=
     \begin{bmatrix} 
    s_1 & -s_1 x_1 & -s_1 y_1 & \cdots \\
    s_2 & -s_2 x_2 & -s_2 y_2 & \cdots \\
    s_3 & -s_3 x_3 & -s_3 y_3 & \cdots \\
    s_4 & -s_4 x_4 & -s_4 y_4 & \cdots \\
    \vdots & \vdots & \vdots & \ddots
    \end{bmatrix}
\end{align*}
$$

## Profit Maximizing Example
To illustrate this method more clearly, we are going to generate some fake data, apply some linear algebra, and find the best (i.e. **maximum**) profit. First we must generate some fake data to populate the *cost matrix* $\mathbf{C}$:

    1.000 -0.041 -0.018 agent
    1.000 -0.059 -0.020 agent
    1.000 -0.052 -0.023 agent
    1.000 -0.048 -0.021 agent
    1.000 -0.035 -0.019 agent
    1.000 -0.035 -0.024 agent
    1.000 -0.032 -0.017 agent
    1.000 -0.056 -0.019 agent
    1.000 -0.048 -0.020 agent
    1.000 -0.051 -0.022 agent
    1.000 -0.030 -0.027  fsbo
    1.000 -0.294 -0.018  cash
    1.000 -0.266 -0.023  cash
    1.000 -0.142 -0.024  cash
    1.000 -0.136 -0.016  cash


Then create some more *fake data* to populate the *sales price matrix* $\mathbf{S}$ (based on the Q2 2024 *median US house price* of $\textdollar361,282$):

    372036 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 328334 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 0 317787 0 0 0 0 0 0 0 0 0 0 0 0
    0 0 0 406171 0 0 0 0 0 0 0 0 0 0 0
    0 0 0 0 407845 0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 392122 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 341743 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 321049 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 379705 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 355297 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0 323486 0 0 0 0
    0 0 0 0 0 0 0 0 0 0 0 360800 0 0 0
    0 0 0 0 0 0 0 0 0 0 0 0 314721 0 0
    0 0 0 0 0 0 0 0 0 0 0 0 0 402214 0
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 337160


Now calculate the *profit vector* $\mathbf{P}$:

    $350,091 agent
    $302,696 agent
    $294,007 agent
    $377,967 agent
    $385,802 agent
    $369,042 agent
    $325,054 agent
    $296,853 agent
    $353,685 agent
    $329,331 agent
    $304,986  fsbo
    $248,238  cash
    $223,703  cash
    $335,304  cash
    $285,891  cash


The *maximum profit* possible from the above *profit vector* $\mathbf{P}$:

    Max Profit:  $385,802
    Sales Price: $407,845
    Total Costs: $22,044
    Commission:  3.4681%
    Option Type: agent


## Moral
What the above calculations really show, is that regardless of what is the *commission* or *closing costs* involved in the sales options selected for selling your property, it is the *profit* that is the important number (in this calculation). Whatever option you choose, regardless of what *commission* or *discount* the *agent* or *cash buyer* wants, as long as the *sales price* is high enough it may be *favorable*. An *agent* with a higher commission, but also a significantly higher *sales price* (assuming they can indeed find a buyer for that price), could very well be *more profitable* than a agent at a lower commission (and also a lower sales price). Of course, in the actual *decision process* there are more things to consider than just *"profit"* (e.g. *time*, *complexity*, *reputation*, etc). But at as a *first approach* the method outlined can be used to *initially filter* the options for selling your property.
