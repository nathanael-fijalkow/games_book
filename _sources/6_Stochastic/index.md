(6-chap:stochastic)=
# Stochastic Games

```{image} ./../Illustrations/6.jpg
:alt: illustration
:class: bg-primary mb-1
:width: 400px
:align: center
```

```{math}

\renewcommand{\Game}{\game}

```


Written by Nathalie Bertrand, Patricia Bouyer-Decitre



In this chapter, we introduce and review results on stochastic games
with two players. On the one hand, they extend 2-player games with
random vertices; on the other hand, they extend Markov decision
processes with a second player. 

When equipped with a simple reachability objective, the objective of
Eve is to maximize the probability of the set of plays that reach the
target, while here opponent has the opposite objective. Such games are
positionally determined: optimal positional pure strategies exist (see Section {ref}`6-sec:values`). 
Perhaps surprisingly, stochastic games
with reachability objectives are central, in the sense that many more
complex objectives (discounted payoff, mean-payoff, parity) reduce to
them (see Section {ref}`6-sec:relations`). We therefore review several
algorithms to solve stochastic reachability games, based on the value
iteration or strategy improvement principles (see Section {ref}`6-sec:algos`) that are also used for other classes of
games.










