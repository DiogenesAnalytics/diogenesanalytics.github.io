---
layout: article
title: International Wealth Diversification
custom_css: article.css
include_mathjax: true
publish: false
---
## Introduction

Diversification is a fundamental principle of wealth management. By distributing wealth across different assets, investors seek to reduce dependence on the performance of any individual investment.

However, asset diversification does not necessarily diversify the countries on which wealth depends. An investor can hold equities, bonds, real estate, and cash while maintaining substantial exposure to a single national economy, monetary system, and legal environment.

International wealth diversification addresses this concentration by distributing wealth across different countries. Its objective is to reduce dependence on any single national environment while preserving the purchasing power, accessibility, and security of wealth.

Achieving this requires understanding how individual assets create country exposure, how those exposures interact, and how wealth can be allocated to reduce excessive dependence.

## The Concentration Problem

Consider an investor whose wealth is distributed across several asset classes:

$$
W=\sum_{i=1}^{n}A_i
$$

where $A_i$ represents an individual asset.

Although these assets may have different characteristics, they can remain exposed to the same national conditions. Inflation can erode the purchasing power of cash, economic deterioration can affect equities and real estate, and financial instability or government intervention can disrupt access to multiple types of assets.

This creates a distinction between asset diversification and country diversification:

$$
\operatorname{Diversification}_{\text{assets}}
\not\Rightarrow
\operatorname{Diversification}_{\text{countries}}
$$

To represent this concentration, let the country exposure of an individual asset be:

$$
E(A_i)=
\left(
e_{i,1},e_{i,2},\ldots,e_{i,m}
\right)
$$

where $e_{i,k}$ represents the exposure of asset $i$ to country $k$.

The aggregate country exposure of wealth is then represented as:

$$
E(W)=\sum_{i=1}^{n}E(A_i)
$$

This representation describes the geographic distribution of wealth exposure. It does not, however, establish the risk associated with that exposure.

**Exposure describes what wealth depends on. Risk describes how changes in those dependencies affect wealth.**

This distinction is important because risks associated with different countries are not necessarily independent. Economic deterioration, financial instability, or other common events can affect multiple national environments simultaneously.

Consequently, distributing wealth across countries does not necessarily produce an equivalent reduction in risk. Effective diversification must consider both the concentration of exposure and the relationships between the risks associated with those exposures.

To understand how this concentration arises, we must first examine the different channels through which an asset creates exposure to a country.

## The Dimensions of Diversification

An asset can create country exposure through several distinct channels. These channels are related, but they are not interchangeable: the country generating an asset's economic returns may differ from the country governing its currency, custody, or ownership.

Four dimensions are particularly relevant:

**1. Investment Exposure**

The countries in which an asset generates its economic returns.

Shares in a European company create exposure to the markets in which that company operates and generates revenue. Domestic real estate creates exposure to the local property market and its underlying economic conditions.

Investment exposure is therefore not necessarily determined by the country in which an asset is purchased or held.

**2. Currency Exposure**

The currencies in which an asset is denominated and through which its purchasing power is measured.

Foreign currency deposits and foreign-denominated securities create exposure to different monetary systems. However, currency exposure and investment exposure are distinct: a foreign investment may be denominated in the domestic currency, while a domestic investment may be denominated in a foreign currency.

**3. Institutional Exposure**

The financial institutions and banking systems responsible for holding, administering, or transferring an asset.

A bank deposit, brokerage account, or custodial arrangement creates dependence on the institutions and financial infrastructure through which the asset is accessed. Using multiple institutions within the same country may reduce individual counterparty exposure without meaningfully reducing dependence on that country's financial system.

**4. Jurisdictional Exposure**

The legal jurisdictions governing ownership, custody, and enforcement of property rights.

An asset's legal exposure depends on the laws and courts governing its ownership and custody arrangements. Holding assets under multiple legal jurisdictions can reduce dependence on a single country's legal and regulatory framework.

These dimensions can be represented as:

$$
\mathcal{D}=\{I,C,F,J\}
$$

where $I$ represents investment exposure, $C$ currency exposure, $F$ institutional exposure, and $J$ jurisdictional exposure.

An individual asset can have different country exposures across these dimensions. For example, an investor may own European equities denominated in US dollars through a US brokerage. The investment exposure is European, while the currency and institutional exposures are American. Its precise jurisdictional exposure depends on the legal and custody arrangements governing the investment.

The four dimensions provide a framework for identifying where wealth depends on different national environments. They do not imply that the associated risks are independent or that exposure can be reduced simply by distributing assets across more countries.

## Modeling Country Exposure

Let an investor's wealth consist of $n$ assets:

$$
W=\sum_{i=1}^{n}A_i
$$

Let $\mathcal{K}$ denote the set of $m$ countries to which these assets may create exposure:

$$
\mathcal{K}=\{K_1,K_2,\ldots,K_m\}
$$

Let:

- $i\in\{1,\ldots,n\}$ index assets,
- $k\in\{1,\ldots,m\}$ index countries,
- $d\in\{I,C,F,J\}$ index exposure dimensions.

Define $e_{i,k,d}$ as the exposure coefficient of asset $i$ to country $K_k$ through dimension $d$.

The aggregate portfolio exposure is:

$$
E_{k,d}(W)=\sum_{i=1}^{n}A_i e_{i,k,d}
$$

This produces a country-by-dimension exposure matrix:

$$
\mathbf{E}(W)=
\begin{bmatrix}
E_{1,I} & E_{1,C} & E_{1,F} & E_{1,J}\\
E_{2,I} & E_{2,C} & E_{2,F} & E_{2,J}\\
\vdots & \vdots & \vdots & \vdots\\
E_{m,I} & E_{m,C} & E_{m,F} & E_{m,J}
\end{bmatrix}
$$

Here, $\mathbf{E}(W)\in\mathbb{R}^{m\times4}$ represents the portfolio's aggregate exposure to each country across the four dimensions. Each row corresponds to a country, and each column corresponds to an exposure dimension $\{I,C,F,J\}$. Its entries represent absolute exposure, aggregated across the investor's assets.

The coefficient $e_{i,k,d}$ provides a general representation of an asset's exposure. To quantify that exposure proportionally, we can give the coefficient a more specific interpretation.

### Quantifying Exposure

Define $\alpha_{i,k,d}$ as the proportion of asset $i$ attributable to country $K_k$ through dimension $d$. Where proportional attribution is meaningful, this provides a specific interpretation of the original exposure coefficient:

$$
e_{i,k,d}=\alpha_{i,k,d}
$$

The aggregate exposure becomes:

$$
E_{k,d}(W)=\sum_{i=1}^{n}A_i\alpha_{i,k,d}
$$

This expresses exposure in monetary terms. However, absolute exposure alone does not indicate its significance relative to the investor's total wealth.

To express each asset's contribution as a proportion of total wealth, define a second coefficient:

$$
\beta_{i,k,d}=\frac{A_i\alpha_{i,k,d}}{W}
$$

The normalized aggregate exposure is then:

$$
s_{k,d}(W)=\sum_{i=1}^{n}\beta_{i,k,d}
$$

Equivalently:

$$
s_{k,d}(W)=\frac{E_{k,d}(W)}{W}
$$

The distinction between the two coefficients is important:

- $\alpha_{i,k,d}$ measures the proportion of an individual asset attributable to a particular exposure category.
- $\beta_{i,k,d}$ measures that asset's contribution to the portfolio's exposure to that category relative to total wealth.

Consider an investor with the following portfolio:

| Asset | Value |
|---|---:|
| US equities | $\textdollar400,000$ |
| French equities | $\textdollar300,000$ |
| Japanese equities | $\textdollar300,000$ |
| **Total wealth** | **$\textdollar1,000,000$** |

For simplicity, assume the equities represent economic exposure to their respective countries, are denominated in their respective national currencies, and are held through a US financial institution under US custody arrangements.

We can now construct the exposure coefficients for each dimension.

**Investment exposure**

For this example, assume each asset's investment exposure is entirely attributable to the country in which its underlying economic activity occurs. The asset-level attribution coefficients for investment exposure are represented by an $n\times m$ matrix:

$$
\boldsymbol{\alpha}_I =
\begin{bmatrix}
\alpha_{1,1,I} & \alpha_{1,2,I} & \cdots & \alpha_{1,m,I}\\
\alpha_{2,1,I} & \alpha_{2,2,I} & \cdots & \alpha_{2,m,I}\\
\vdots & \vdots & \ddots & \vdots\\
\alpha_{n,1,I} & \alpha_{n,2,I} & \cdots & \alpha_{n,m,I}
\end{bmatrix}
$$

Each row represents an asset, and each column represents a country. The element $\alpha_{i,k,I}$ is the proportion of asset $i$ attributable to country $K_k$ through investment exposure $I$. Thus, the matrix contains one row for each of the $n$ assets and one column for each of the $m$ countries.

For the portfolio in this example, there are three assets and three countries: the United States, France, and Japan. Since each asset is entirely attributable to a single country, the matrix becomes:

$$
\boldsymbol{\alpha}_I =
\begin{bmatrix}
\alpha_{1,\mathrm{US},I} & \alpha_{1,\mathrm{FR},I} & \alpha_{1,\mathrm{JP},I}\\
\alpha_{2,\mathrm{US},I} & \alpha_{2,\mathrm{FR},I} & \alpha_{2,\mathrm{JP},I}\\
\alpha_{3,\mathrm{US},I} & \alpha_{3,\mathrm{FR},I} & \alpha_{3,\mathrm{JP},I}
\end{bmatrix} =
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
$$

More generally, $\boldsymbol{\alpha}_d$ denotes the $n\times m$ matrix of asset-level attribution coefficients for exposure dimension $d$.

The corresponding $\beta$ coefficients are obtained by weighting each asset's attribution coefficients by that asset's proportion of total wealth. At the individual coefficient level:

$$
\boxed{
\beta_{i,k,d}=\frac{A_i}{W}\alpha_{i,k,d}
}
$$

To express this operation in matrix form, define the diagonal asset-value matrix:

$$
\mathbf{A}=
\begin{bmatrix}
A_1 & 0 & \cdots & 0\\
0 & A_2 & \cdots & 0\\
\vdots & \vdots & \ddots & \vdots\\
0 & 0 & \cdots & A_n
\end{bmatrix}
$$

Here, $\mathbf{A}\in\mathbb{R}^{n\times n}$ is a diagonal matrix containing the monetary value of each asset along its main diagonal. Each diagonal entry $A_i$ corresponds to the value of asset $i$, while all off-diagonal entries are zero. This structure ensures that each asset's value weights only its own attribution coefficients, without affecting the coefficients of any other asset.

Multiplying $\mathbf{A}$ by the asset-level attribution matrix $\boldsymbol{\alpha}_d$ therefore scales each row of that matrix by the corresponding asset's value. Dividing by total wealth $W$ converts those values into proportions of the investor's total wealth:

$$
\boxed{
\boldsymbol{\beta}_d=\frac{1}{W}\mathbf{A}\boldsymbol{\alpha}_d
}
$$

Expanding this matrix operation gives:

$$
\boldsymbol{\beta}_d =
\begin{bmatrix}
\frac{A_1}{W}\alpha_{1,1,d} & \frac{A_1}{W}\alpha_{1,2,d} & \cdots & \frac{A_1}{W}\alpha_{1,m,d}\\
\frac{A_2}{W}\alpha_{2,1,d} & \frac{A_2}{W}\alpha_{2,2,d} & \cdots & \frac{A_2}{W}\alpha_{2,m,d}\\
\vdots & \vdots & \ddots & \vdots\\
\frac{A_n}{W}\alpha_{n,1,d} & \frac{A_n}{W}\alpha_{n,2,d} & \cdots & \frac{A_n}{W}\alpha_{n,m,d}
\end{bmatrix} =
\begin{bmatrix}
\beta_{1,1,d} & \beta_{1,2,d} & \cdots & \beta_{1,m,d}\\
\beta_{2,1,d} & \beta_{2,2,d} & \cdots & \beta_{2,m,d}\\
\vdots & \vdots & \ddots & \vdots\\
\beta_{n,1,d} & \beta_{n,2,d} & \cdots & \beta_{n,m,d}
\end{bmatrix}
$$

For the investment exposure example, the resulting matrix is:

$$
\boldsymbol{\beta}_I=
\begin{bmatrix}
0.40 & 0 & 0\\
0 & 0.30 & 0\\
0 & 0 & 0.30
\end{bmatrix}
$$

Each entry represents the normalized contribution of an individual asset to a country's investment exposure. For example, $\beta_{1,1,I}=0.40$ means that the first asset contributes an amount equal to $40\%$ of total wealth to US investment exposure.

Aggregating these asset-level contributions gives the portfolio's normalized investment exposure profile:

$$
\mathbf{s}_I=
\begin{bmatrix}
0.40\\
0.30\\
0.30
\end{bmatrix}
$$

In general, $\mathbf{s}_d$ is an $m$-dimensional column vector containing the aggregate normalized exposure to each of the $m$ countries through dimension $d$:

$$
\mathbf{s}_d=
\begin{bmatrix}
s_{1,d}\\
s_{2,d}\\
\vdots\\
s_{m,d}
\end{bmatrix}
$$

To obtain this vector, we sum the normalized contributions of all $n$ assets for each country. Define $\mathbf{1}_n$ as an $n$-dimensional column vector of ones:

$$
\mathbf{1}_n=
\begin{bmatrix}
1\\
1\\
\vdots\\
1
\end{bmatrix}
$$

The matrix $\boldsymbol{\beta}_d$ has assets in rows and countries in columns. Transposing it places countries in rows and assets in columns. Multiplication by $\mathbf{1}_n$ then sums across the asset columns, collapsing the asset dimension and leaving one aggregate exposure value for each country:

$$
\begin{aligned}
\mathbf{s}_d
&=\boldsymbol{\beta}_d^T\mathbf{1}_n\\[6pt]
&=
\begin{bmatrix}
\beta_{1,1,d} & \beta_{2,1,d} & \cdots & \beta_{n,1,d}\\
\beta_{1,2,d} & \beta_{2,2,d} & \cdots & \beta_{n,2,d}\\
\vdots & \vdots & \ddots & \vdots\\
\beta_{1,m,d} & \beta_{2,m,d} & \cdots & \beta_{n,m,d}
\end{bmatrix}
\begin{bmatrix}
1\\
1\\
\vdots\\
1
\end{bmatrix}\\[6pt]
&=
\begin{bmatrix}
\displaystyle\sum_{i=1}^{n}\beta_{i,1,d}\\
\displaystyle\sum_{i=1}^{n}\beta_{i,2,d}\\
\vdots\\
\displaystyle\sum_{i=1}^{n}\beta_{i,m,d}
\end{bmatrix}\\[6pt]
&=
\begin{bmatrix}
s_{1,d}\\
s_{2,d}\\
\vdots\\
s_{m,d}
\end{bmatrix}
\end{aligned}
$$

The resulting vector has one entry for each country. Each entry $s_{k,d}$ is the sum of the normalized contributions from all assets to the investor's exposure to country $K_k$ through dimension $d$. In other words, the original asset-by-country matrix has been reduced to a country-level exposure vector: the asset-level contributions have been aggregated, leaving the portfolio's total exposure to each country.

The progression can be summarized as:

$$
\boxed{
\underbrace{\boldsymbol{\alpha}_d}_{\text{Asset attribution}}
\quad\longrightarrow\quad
\underbrace{\boldsymbol{\beta}_d}_{\text{Wealth-weighted contribution}}
\quad\longrightarrow\quad
\underbrace{\mathbf{s}_d}_{\text{Aggregate portfolio exposure}}
}
$$

The investor therefore has $40\%$ of total wealth attributable to US investment exposure, $30\%$ to French investment exposure, and $30\%$ to Japanese investment exposure.

**Currency exposure**

Assume, for this simplified example, that the assets have corresponding exposure to USD, EUR, and JPY, associated respectively with the United States, France, and Japan. Their currency attribution coefficients are:

$$
\boldsymbol{\alpha}_C=
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
$$

The normalized contributions are:

$$
\boldsymbol{\beta}_C=
\begin{bmatrix}
0.40 & 0 & 0\\
0 & 0.30 & 0\\
0 & 0 & 0.30
\end{bmatrix}
$$

Thus:

$$
\mathbf{s}_C=
\begin{bmatrix}
0.40\\
0.30\\
0.30
\end{bmatrix}
$$

In this example, investment and currency exposures happen to have identical distributions. This is not necessarily the case in practice. An asset can generate returns from one country while being denominated in another country's currency.

The country associations used here are a simplifying representation. Currencies are not countries: the euro, for example, is shared by multiple countries, while the US dollar is used beyond the United States. A more general representation of currency exposure will be introduced below.

**Institutional exposure**

All three assets are held through the same US financial institution. At the country level, this means that each asset is attributable to the United States through the institutional dimension:

$$
\boldsymbol{\alpha}_F=
\begin{bmatrix}
1 & 0 & 0\\
1 & 0 & 0\\
1 & 0 & 0
\end{bmatrix}
$$

The normalized contributions are:

$$
\boldsymbol{\beta}_F=
\begin{bmatrix}
0.40 & 0 & 0\\
0.30 & 0 & 0\\
0.30 & 0 & 0
\end{bmatrix}
$$

Aggregating across the three assets gives:

$$
\mathbf{s}_F = \boldsymbol{\beta}_F^T\mathbf{1}_3 = 
\begin{bmatrix}
0.40+0.30+0.30\\
0\\
0
\end{bmatrix} =
\begin{bmatrix}
1\\
0\\
0
\end{bmatrix}
$$

The entries of $\mathbf{s}_F$ correspond to the United States, France, and Japan, respectively. Thus, the value $1$ in the first position indicates that $100\%$ of the portfolio's wealth is exposed to the US financial system through the institutional dimension. The zeros indicate that none of the portfolio's institutional exposure is attributed to France or Japan.

The entire portfolio is therefore exposed to the US financial system through its institutional arrangements, despite its international investment and currency diversification.

This country-level representation captures dependence on the US financial system. It does not, by itself, distinguish exposure to an individual financial institution from exposure to other institutions operating within the same country.

**Jurisdictional exposure**

Assuming all three assets are held under US custody arrangements and governed by US law for the relevant ownership and custody relationships, their jurisdictional attribution coefficients are:

$$
\boldsymbol{\alpha}_J=
\begin{bmatrix}
1 & 0 & 0\\
1 & 0 & 0\\
1 & 0 & 0
\end{bmatrix}
$$

The normalized contributions are:

$$
\boldsymbol{\beta}_J=
\begin{bmatrix}
0.40 & 0 & 0\\
0.30 & 0 & 0\\
0.30 & 0 & 0
\end{bmatrix}
$$

Aggregating gives:

$$
\mathbf{s}_J= \boldsymbol{\beta}_J^T\mathbf{1}_3 =
\begin{bmatrix}
1\\
0\\
0
\end{bmatrix}
$$

As with institutional exposure, the entries correspond to the United States, France, and Japan. The vector indicates that the entire portfolio's jurisdictional exposure is attributed to the United States under the stated assumptions, with no corresponding exposure attributed to France or Japan.

The portfolio therefore has complete US jurisdictional exposure under these assumptions.

**Combining the exposure profiles**

The four aggregate exposure profiles can be combined into a single portfolio-level matrix, with countries as rows and exposure dimensions as columns:

$$
\mathbf{S}(W)=
\begin{bmatrix}
\vert & \vert & \vert & \vert\\
\mathbf{s}_I & \mathbf{s}_C & \mathbf{s}_F & \mathbf{s}_J\\
\vert & \vert & \vert & \vert
\end{bmatrix}
$$

For the example portfolio:

$$
\mathbf{S}(W)=
\begin{bmatrix}
0.40 & 0.40 & 1.00 & 1.00\\
0.30 & 0.30 & 0 & 0\\
0.30 & 0.30 & 0 & 0
\end{bmatrix}
$$

Here, the rows represent the United States, France, and Japan, while the columns represent investment, currency, institutional, and jurisdictional exposure, respectively.

This matrix is the normalized counterpart of the absolute exposure matrix $\mathbf{E}(W)$. Its entries express each country's exposure through each dimension as a proportion of total wealth. Where proportional attribution applies:

$$
\boxed{
\mathbf{S}(W)=\frac{\mathbf{E}(W)}{W}
}
$$

The matrix illustrates an important distinction: the investor has diversified investment and currency exposure across three countries, but remains entirely dependent on the US financial system and US custody arrangements.

The numerical example also demonstrates the relationship between the two coefficients. The $\alpha$ matrices describe how each individual asset is attributed across exposure categories. The $\beta$ matrices express each asset's contribution relative to total wealth. Aggregating the latter produces the portfolio's normalized exposure profiles, which can then be combined into $\mathbf{S}(W)$.

Normalization establishes total wealth as a common denominator across dimensions. It does not, however, guarantee that equal normalized values represent equivalent forms of dependence. Institutional and jurisdictional exposures, for example, may overlap, so their values need not sum to $100\%$.

## Applying the Framework

The preceding model provides a general representation of an investor's wealth exposure across investment, currency, institutional, and jurisdictional dimensions. We can apply this model to different asset configurations to demonstrate how individual assets can depend on multiple economic, financial, and legal environments.

Consider several hypothetical investors, each with total wealth:

$$
W=\textdollar1,000,000
$$

The examples use different asset compositions and ownership arrangements to illustrate distinct exposure characteristics.

For proportional attribution, the normalized exposure matrix is:

$$
\mathbf S(W)=\frac{\mathbf E(W)}{W}
$$

Each entry $s_{k,d}$ represents the contribution of country $K_k$ to exposure dimension $d$, expressed relative to total wealth.

Where exposure is represented by overlapping dependencies rather than proportional allocations, the same normalization can be applied, but the resulting entries are not necessarily bounded by one or sum to one. We will distinguish these cases explicitly.

### The Multinational Company

Consider an investor with the following portfolio:

| Asset | Value |
|---|---:|
| US-listed multinational equities | $\textdollar250,000$ |
| US Treasury securities | $\textdollar450,000$ |
| French government bonds | $\textdollar200,000$ |
| Japanese equities | $\textdollar100,000$ |
| **Total** | **$\textdollar1,000,000$** |

The multinational corporation is listed in the US, but its economic activity is distributed across four markets:

| Economic market | Attribution |
|---|---:|
| United States | 40% |
| France | 25% |
| Japan | 20% |
| United Kingdom | 15% |

The company's $\textdollar250,000$ market value therefore contributes the following amounts to investment exposure:

$$
\begin{aligned}
E_{\mathrm{US},I}&=\textdollar250,000(0.40)=\textdollar100,000\\
E_{\mathrm{FR},I}&=\textdollar250,000(0.25)=\textdollar62,500\\
E_{\mathrm{JP},I}&=\textdollar250,000(0.20)=\textdollar50,000\\
E_{\mathrm{UK},I}&=\textdollar250,000(0.15)=\textdollar37,500
\end{aligned}
$$

Adding the remaining investments, the aggregate investment exposure is:

| Country | Multinational equities | Other investments | Total exposure |
|---|---:|---:|---:|
| United States | $\textdollar100,000$ | $\textdollar450,000$ | $\textdollar550,000$ |
| France | $\textdollar62,500$ | $\textdollar200,000$ | $\textdollar262,500$ |
| Japan | $\textdollar50,000$ | $\textdollar100,000$ | $\textdollar150,000$ |
| United Kingdom | $\textdollar37,500$ | $\textdollar0$ | $\textdollar37,500$ |
| **Total** | **$\textdollar250,000$** | **$\textdollar750,000$** | **$\textdollar1,000,000$** |

The normalized investment exposure profile is:

$$
\mathbf s_I=
\begin{bmatrix}
0.5500\\
0.2625\\
0.1500\\
0.0375
\end{bmatrix}
$$

Now consider currency exposure. Assume, for simplicity, that the multinational's economic currency sensitivities follow the same distribution as its geographic revenue attribution. The remaining assets are denominated in their respective national currencies.

The currency exposures are therefore:

| Currency | Exposure |
|---|---:|
| USD | $\textdollar550,000$ |
| EUR | $\textdollar262,500$ |
| JPY | $\textdollar150,000$ |
| GBP | $\textdollar37,500$ |
| **Total** | **$\textdollar1,000,000$** |

This produces:

$$
\mathbf s_C=
\begin{bmatrix}
0.5500\\
0.2625\\
0.1500\\
0.0375
\end{bmatrix}
$$

The numerical distributions happen to coincide because of our assumptions. The currency categories are nevertheless distinct from countries: EUR, for example, is shared across multiple countries.

Finally, assume all four positions are held through a US brokerage institution under US custody arrangements.

The country-indexed institutional and jurisdictional profiles are:

$$
\mathbf s_F=
\begin{bmatrix}
1\\0\\0\\0
\end{bmatrix},
\qquad
\mathbf s_J=
\begin{bmatrix}
1\\0\\0\\0
\end{bmatrix}
$$

Here, the jurisdictional assumption concerns the relevant brokerage and custody arrangements, not every legal relationship associated with the underlying securities.

The resulting country-indexed matrix, with rows ordered US, France, Japan, and UK, is:

$$
\mathbf S(W)=
\begin{bmatrix}
0.5500&0.5500&1&1\\
0.2625&0.2625&0&0\\
0.1500&0.1500&0&0\\
0.0375&0.0375&0&0
\end{bmatrix}
$$

The first two columns represent country proxies for the corresponding currency categories in this example. The separate currency table provides the more precise classification.

**Observation:** A multinational company's listing location does not necessarily represent its underlying economic exposure. Furthermore, investment exposure, currency exposure, and the infrastructure through which securities are held can produce substantially different geographic distributions.

### The Cross-Border Custody Chain

Consider a second investor with the following portfolio:

| Asset | Value |
|---|---:|
| US equities | $\textdollar500,000$ |
| US Treasury securities | $\textdollar320,000$ |
| Japanese equities | $\textdollar180,000$ |
| **Total** | **$\textdollar1,000,000$** |

The Japanese equities are held through a cross-border custody arrangement involving:

- A US brokerage institution maintaining the investor's account.
- A UK global custodian providing international custody services.
- A Japanese central securities depository maintaining the underlying securities infrastructure.

The remaining US securities are held directly through the US brokerage institution.

Assume the investments are denominated in their respective national currencies.

Investment exposure is straightforward:

$$
\mathbf E_I=
\begin{bmatrix}
\textdollar820,000\\
\textdollar180,000\\
0
\end{bmatrix}
$$

Currency exposure is:

$$
\mathbf E_C=
\begin{bmatrix}
\textdollar820,000\\
\textdollar180,000\\
0
\end{bmatrix}
$$

The row order is US, Japan, UK. For currency exposure, these country entries are proxies for USD and JPY respectively.

The more interesting result concerns institutional exposure.

The entire $\textdollar1,000,000$ portfolio depends on the US brokerage institution. However, the $\textdollar180,000$ Japanese equity position also depends on the UK custodian and Japanese securities infrastructure.

Using binary dependency indicators:

$$
e_{i,k,F}=
\begin{cases}
1 & \text{if asset }i\text{ depends on country }k\\
0 & \text{otherwise}
\end{cases}
$$

The aggregate institutional exposure becomes:

$$
\mathbf E_F=
\begin{bmatrix}
\textdollar1,000,000\\
\textdollar180,000\\
\textdollar180,000
\end{bmatrix}
$$

The same assumptions apply to the relevant jurisdictional relationships:

$$
\mathbf E_J=
\begin{bmatrix}
\textdollar1,000,000\\
\textdollar180,000\\
\textdollar180,000
\end{bmatrix}
$$

The resulting matrix is:

$$
\mathbf S(W)=
\begin{bmatrix}
0.82&0.82&1.00&1.00\\
0.18&0.18&0.18&0.18\\
0&0&0.18&0.18
\end{bmatrix}
$$

Rows represent the US, Japan, and UK; columns represent investment, currency, institutional, and jurisdictional exposure.

Notice that the institutional and jurisdictional columns do not sum to one:

$$
\sum_k s_{k,F}=1.36
$$

$$
\sum_k s_{k,J}=1.36
$$

This is intentional. The Japanese equity position depends simultaneously on three national environments. Its $\textdollar180,000$ contribution is therefore attributed to each relevant dependency rather than divided among them.

**Observation:** A portfolio's institutional and jurisdictional exposure can exceed its total wealth when multiple environments are necessary to hold, administer, transfer, or enforce ownership of the same assets. These are overlapping dependencies, not additional assets or separate allocations of wealth.

### The International Real Estate Structure

Consider a third investor with the following portfolio:

| Asset | Value |
|---|---:|
| US equities | $\textdollar300,000$ |
| US Treasury securities | $\textdollar250,000$ |
| German rental property held through a Luxembourg company | $\textdollar450,000$ |
| **Total** | **$\textdollar1,000,000$** |

The German property is owned through a Luxembourg holding company. Assume:

- The property is located in Germany and generates rental income in EUR.
- The Luxembourg company owns the property.
- The company maintains a Luxembourg bank account for rental proceeds.
- The investor holds the company's shares through a US brokerage account.
- The US securities are held through the same brokerage institution.

The investment exposure is:

$$
\mathbf E_I=
\begin{bmatrix}
\textdollar550,000\\
\textdollar450,000\\
0
\end{bmatrix}
$$

The corresponding currency exposure is:

$$
\mathbf E_C=
\begin{bmatrix}
\textdollar550,000\\
\textdollar450,000
\end{bmatrix}
$$

Here the currency categories are USD and EUR, not US and Germany. The values represent simplified currency attribution based on the assumed denominations and economic sensitivities.

Institutional exposure involves both the US brokerage institution and the Luxembourg bank:

$$
\mathbf E_F=
\begin{bmatrix}
\textdollar1,000,000\\
\textdollar450,000
\end{bmatrix}
$$

The US brokerage institution holds the investor's securities and company shares, while the Luxembourg bank holds the company's rental proceeds.

Jurisdictional exposure involves three legal environments:

- US law governing the brokerage relationship.
- German law governing the property and associated ownership rights.
- Luxembourg law governing the holding company and its corporate ownership structure.

The corresponding jurisdictional exposure is:

$$
\mathbf E_J=
\begin{bmatrix}
\textdollar1,000,000\\
\textdollar450,000\\
\textdollar450,000
\end{bmatrix}
$$

For clarity, the country-indexed absolute exposure matrix is:

$$
\mathbf E(W)=
\begin{bmatrix}
\textdollar550,000&0&\textdollar1,000,000&\textdollar1,000,000\\
\textdollar450,000&0&0&\textdollar450,000\\
0&0&\textdollar450,000&\textdollar450,000
\end{bmatrix}
$$

Rows represent the US, Germany, and Luxembourg; columns represent investment, currency, institutional, and jurisdictional exposure.

The currency column is zero because neither USD nor EUR is a country. Currency exposure is represented separately:

$$
\mathbf E_C=
\begin{bmatrix}
\textdollar550,000\\
\textdollar450,000
\end{bmatrix}
\quad
\begin{matrix}
\text{USD}\\
\text{EUR}
\end{matrix}
$$

Dividing the country-indexed matrix by total wealth gives:

$$
\mathbf S(W)=
\begin{bmatrix}
0.55&0&1.00&1.00\\
0.45&0&0&0.45\\
0&0&0.45&0.45
\end{bmatrix}
$$

The currency profile, using the same denominator, is:

$$
\mathbf s_C=
\begin{bmatrix}
0.55\\
0.45
\end{bmatrix}
\quad
\begin{matrix}
\text{USD}\\
\text{EUR}
\end{matrix}
$$

The property is a single $\textdollar450,000$ investment, but its ownership and administration involve Germany, Luxembourg, and the United States.

**Observation:** An asset's investment location, currency, financial infrastructure, and legal structure can span several different environments. The country in which an asset is physically located does not necessarily capture the full extent of its dependencies.

### Assets Without a Single Country Attribution

Consider a fourth investor with the following portfolio:

| Asset | Value |
|---|---:|
| US Treasury securities | $\textdollar400,000$ |
| US bank deposits | $\textdollar350,000$ |
| International equity fund | $\textdollar175,000$ |
| Bitcoin held through self-custody | $\textdollar75,000$ |
| **Total** | **$\textdollar1,000,000$** |

Assume the international equity fund has investment exposure distributed across four markets:

| Market | Attribution |
|---|---:|
| United States | 30% |
| France | 25% |
| Germany | 25% |
| Japan | 20% |

The fund's investment contributions are:

$$
\begin{aligned}
E_{\mathrm{US},I}&=\textdollar175,000(0.30)=\textdollar52,500\\
E_{\mathrm{FR},I}&=\textdollar175,000(0.25)=\textdollar43,750\\
E_{\mathrm{DE},I}&=\textdollar175,000(0.25)=\textdollar43,750\\
E_{\mathrm{JP},I}&=\textdollar175,000(0.20)=\textdollar35,000
\end{aligned}
$$

Adding the US Treasury securities, the country-attributable investment exposure is:

$$
\begin{aligned}
E_{\mathrm{US},I}&=\textdollar452,500\\
E_{\mathrm{FR},I}&=\textdollar43,750\\
E_{\mathrm{DE},I}&=\textdollar43,750\\
E_{\mathrm{JP},I}&=\textdollar35,000
\end{aligned}
$$

The bank deposit represents a financial claim on the US bank rather than a direct investment in the US economy. We therefore account for it through institutional exposure rather than assigning it an investment exposure to the US market.

Bitcoin presents a different problem. It has no issuing country or national economy to which its investment exposure can be directly attributed. Its value and operation instead depend on a decentralized network that spans national boundaries.

Assigning this exposure to a particular country would be arbitrary. Excluding it entirely, however, would leave an important dependency of the investor's wealth unrepresented.

We can accommodate this by extending the investment exposure categories beyond countries. Let $\mathcal X_I$ denote the categories relevant to investment exposure, including both national markets and non-national categories:

$$
\mathcal X_I=
\{
\mathrm{US},
\mathrm{FR},
\mathrm{DE},
\mathrm{JP},
\mathrm{Bitcoin\ Network}
\}
$$

The Bitcoin position is then represented as:

$$
E_{\mathrm{Bitcoin\ Network},I}
=
\textdollar75,000
$$

The complete investment exposure profile becomes:

$$
\mathbf E_I=
\begin{bmatrix}
\textdollar452,500\\
\textdollar43,750\\
\textdollar43,750\\
\textdollar35,000\\
\textdollar75,000
\end{bmatrix}
$$

Rows represent the United States, France, Germany, Japan, and the Bitcoin network, respectively.

Normalizing by total wealth gives:

$$
\mathbf s_I=
\begin{bmatrix}
0.4525\\
0.04375\\
0.04375\\
0.0350\\
0.0750
\end{bmatrix}
$$

The remaining exposures require their own classifications:

- **Currency:** The Treasury securities and bank deposits are denominated in USD. The international equity fund has exposure to several underlying currencies. Bitcoin's USD market quotation does not, by itself, establish that Bitcoin is economically equivalent to a USD-denominated asset.
- **Institutional:** The Treasury securities and equity fund are held through a US brokerage institution, while the bank deposit depends on the US bank holding the deposit. The Bitcoin position has no financial custodian if genuinely held through self-custody.
- **Jurisdictional:** The conventional financial assets depend on the relevant account, custody, issuer, and securities arrangements. The Bitcoin position remains subject to the legal environment governing the investor's ownership, taxation, and enforcement of property rights.

This example illustrates why exposure categories must be appropriate to the dependency being measured. Countries remain useful categories, but they are not sufficient to represent every investment exposure. The same mathematical framework can accommodate a network or other non-national category without changing the underlying exposure calculation:

$$
E_{x,d}(W)=\sum_{i=1}^{n}A_i e_{i,x,d}
$$

Here, $x$ identifies the exposure category and $d$ identifies the dimension through which the asset depends on that category.

**Observation:** Some assets depend on markets, networks, and infrastructures that transcend national boundaries. A comprehensive exposure model must accommodate these categories rather than force every dependency into a country classification.

### Interpreting the Examples

The four examples demonstrate different properties of the framework:

- **Multinational Company:** Economic exposure can differ substantially from an asset's listing location.
- **Cross-Border Custody Chain:** A single asset can depend simultaneously on multiple financial institutions and jurisdictions.
- **International Real Estate Structure:** Investment, currency, institutional, and jurisdictional exposure can involve entirely different environments.
- **Bitcoin Self-Custody:** Some exposure categories cannot be adequately represented through national boundaries or conventional financial institutions.

Together, these examples demonstrate why an asset's geographic classification is insufficient to characterize its international exposure.

They also illustrate two distinct forms of exposure attribution.

Where an asset's value can be proportionally distributed across categories, we use:

$$
\beta_{i,k,d}=\frac{A_i\alpha_{i,k,d}}{W}
$$

Where an asset simultaneously depends on multiple environments, we use:

$$
s_{k,d}(W)=\frac{1}{W}
\sum_{i=1}^{n}A_i e_{i,k,d}
$$

The first measures the proportional contribution of an asset to an exposure category. The second measures the wealth-weighted presence of a dependency. Because dependencies can overlap, the resulting values need not sum to one.

This distinction allows the framework to represent both the distribution of wealth across exposure categories and the multiple environments on which individual assets depend.

The resulting model provides a systematic means of identifying and comparing international wealth dependencies without assuming that every exposure is mutually exclusive, proportional, or attributable to a single country.

It is a framework for representing exposure, not a complete measure of institutional, legal, or financial risk.

## Conclusion

Diversification is often evaluated by examining the number of assets in a portfolio, the markets in which they are invested, or the geographic distribution of their underlying investments. These measures capture important aspects of portfolio composition, but they do not necessarily reveal the environments on which an investor's wealth depends.

An investor may hold securities across multiple countries while relying on a single financial institution, currency, or legal jurisdiction. Conversely, assets held through the same institution or jurisdiction may provide exposure to different economic environments. Asset diversification and international wealth diversification are therefore distinct objectives.

The framework developed here represents these dependencies across four dimensions:

$$
\mathcal D=\{I,C,F,J\}
$$

where $I$, $C$, $F$, and $J$ denote investment, currency, institutional, and jurisdictional exposure, respectively. For each dimension, the framework identifies the exposure of individual assets to relevant categories and aggregates those exposures across the investor's wealth:

$$
E_{k,d}(W)=\sum_{i=1}^{n}A_i e_{i,k,d}
$$

Here, $A_i$ is the value of asset $i$, and $e_{i,k,d}$ represents its exposure to country $K_k$ through dimension $d$. Where proportional attribution is meaningful, normalized aggregate exposure is given by:

$$
s_{k,d}(W)=\sum_{i=1}^{n}\frac{A_i\alpha_{i,k,d}}{W}
$$

Together, these representations allow an investor to identify concentrations that would otherwise remain obscured by conventional portfolio classifications. They also accommodate overlapping dependencies, where the same wealth may depend on multiple countries through a particular dimension.

The resulting perspective changes the question from *How diversified are my assets?* to *Which environments does my wealth depend on, and to what extent?*

The Bitcoin example from the [previous section](#assets-without-a-single-country-attribution) illustrated a further limitation of country-based exposure classification. Although the framework can represent Bitcoin as investment exposure to a decentralized network, that exposure cannot be meaningfully attributed to a particular country. More generally, the environments and systems on which wealth depends need not coincide with national boundaries.

This observation suggests generalizing the set of exposure categories beyond countries. Let $\mathcal X$ denote the broader set of categories to which wealth may be exposed, with countries represented as a subset:

$$
\mathcal K\subseteq\mathcal X
$$

The country index $k$ can then be replaced by a general category index $x$, giving:

$$
e_{i,x,d}
$$

where $e_{i,x,d}$ represents the exposure of asset $i$ to category $x$ through dimension $d$. For example:

$$
e_{i,\text{Bitcoin network},I}
$$

represents investment exposure to the Bitcoin network, while:

$$
e_{i,\text{USD},C}
$$

represents currency exposure to the US dollar.

The aggregate exposure equation retains its original form:

$$
E_{x,d}(W)=\sum_{i=1}^{n}A_i e_{i,x,d}
$$

And, where proportional attribution is meaningful:

$$
s_{x,d}(W)=\sum_{i=1}^{n}\frac{A_i\alpha_{i,x,d}}{W}
$$

The relevant categories can also vary by dimension. Investment exposure may be attributed to countries, economic markets, or networks; currency exposure to currencies; institutional exposure to financial institutions; and jurisdictional exposure to legal jurisdictions. Let $\mathcal X_d\subseteq\mathcal X$ denote the categories applicable to dimension $d$. The generalized model is then defined over:

$$
x\in\mathcal X_d,\qquad d\in\mathcal D
$$

The same reasoning can be applied to the dimensions themselves. The four dimensions developed in this article constitute the set:

$$
\mathcal D=\{I,C,F,J\}
$$

Other distinct forms of dependency may warrant additional dimensions. We can represent this possibility by defining a broader dimension set $\mathcal D^*$ such that:

$$
\mathcal D\subseteq\mathcal D^*
$$

The fully generalized exposure model is therefore:

$$
\boxed{
E_{x,d}(W)=\sum_{i=1}^{n}A_i e_{i,x,d},
\qquad
x\in\mathcal X_d,\ d\in\mathcal D^*
}
$$

The framework developed in this article is recovered by restricting the categories to countries and the dimensions to the original four:

$$
x\in\mathcal K,\qquad d\in\mathcal D
$$

This generalization preserves the central mathematical structure while allowing the framework to represent dependencies on a broader range of environments, institutions, and systems. The categories identify *what* an asset depends on; the dimensions identify *how* it depends on them.

Ultimately, the objective is not simply to measure how wealth is distributed across countries, but to identify the full range of environments and systems on which that wealth depends. This provides a broader basis for understanding international diversification and a foundation for extending the framework to additional forms of exposure.
