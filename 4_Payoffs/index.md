(4-chap:payoffs)=
# Games with Payoffs

```{image} ./../Illustrations/4.jpg
:alt: illustration
:class: bg-primary mb-1
:width: 400px
:align: center
```


Written by Benjamin Monmege



This chapter considers quantitative objectives defined using payoffs. 
Adding quantities can serve two goals:
the first is for refining qualitative objectives by quantifying how well, how fast, or at what cost a qualitative objective is satisfied,
and the second is to define richer specifications and preferences over outcomes.

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















