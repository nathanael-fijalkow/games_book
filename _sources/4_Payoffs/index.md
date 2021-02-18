(4-chap:payoffs)=
# Games with Payoffs

```{image} ./../Illustrations/4.jpg
:alt: illustration
:class: bg-primary mb-1
:width: 400px
:align: center
```

```{math}
\newcommand{\R}{\mathbb{R}}
```


Written by Benjamin Monmege



This chapter considers quantitative objectives defined using payoffs. 
Adding quantities can serve two goals:
the first is for refining qualitative objectives by quantifying how well, how fast, or at what cost a qualitative objective is satisfied,
and the second is to define richer specifications and preferences over outcomes.

%objectives, the set of colours on edges is $\mathbb{R}. The goal of adding

%classical games. We may thus use quantities in order to refine

%costly a qualitative objective is satisfied. Quantitative objectives

%$\omega$-regular (like mean payoff for instance) or other quantitative

*  We start in Section {ref}`4-sec:qualitative` by studying extensions of the classical qualitative objectives. Among two strategies in a reachability game that guarantee to reach a target in ten steps or in a billion steps, we would certainly prefer the first one from a pragmatic point of view.

*  We study **mean payoff games** in Section {ref}`4-sec:mean_payoff`. 
We present two algorithms for solving them, the first based on **strategy improvement** and the second on a **value iteration** for the related class of energy games.
Along the way we show that parity games reduce to mean payoff games.

*  We study **discounted payoff games** in Section {ref}`4-sec:discounted_payoff`.
We construct a strategy improvement algorithm for computing the value function.
We also show that mean payoff games reduce to discounted payoff games, so the previous algorithm yields an algorithm for computing the value function of a mean payoff game.

*  We study **shortest path games** in Section {ref}`4-sec:shortest_path`.
They extend reachability games by requiring that Eve reaches her target with minimal cost, 
which if the weights are all equal means **as soon as possible**.

*  We study **total payoff games** in Section {ref}`4-sec:total_payoff`.

%\item We start in Section {ref}`4-sec:shortest_path` by studying extensions of the

%  of colours. Among two strategies in a reachability game that

%  steps, we would certainly prefer the first one in a pragmatic point

%  **shortest-path games** where a player wants to reach a winning

%\item A way to solve shortest-path games in full generality is to use

%  motivation. We introduce and study them in Section {ref}`4-sec:mean_payoff`. We solve

%  **value iteration**. We can then use a binary search algorithm to

%\item Another very natural payoff consists in discounting the future,

%  **discounted-payoff games** in Section {ref}`4-sec:discounted_payoff`. We obtain as a

%  algorithm to compute the values of a mean-payoff game.

%  shortest-path objective in Section {ref}`4-sec:shortest_path-bis`, and use the obtained

%\end{itemize}















%
%
%
