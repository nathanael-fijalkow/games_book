(1-sec:strategy_improvement)=
# Strategy improvement algorithms

```{math}

\renewcommand{\Game}{\game}

```

Value iteration algorithms manipulate value functions and never construct any strategy, at least explicitly.
This is a key difference with strategy improvement algorithms (also called policy iteration algorithms) whose fundamental idea is to maintain and improve a strategy.
We assume that the games we consider in this section are positionally determined, therefore all strategies are assumed to be positional.

Let us consider a game $\mathcal{G}$ and set as a goal to construct an optimal strategy for Eve.
As for value iteration algorithms we work with a value function: 
the key idea behind strategy improvement is to use $val^{\sigma}$ to improve the strategy $\sigma$ 
by **switching** an edge, which is an operation that creates a new strategy.
This involves defining the notion of **switchable edge**:
the edge $(v,u)$ is switchable if

$$
\delta(  val^{\sigma}(u), \textsf{col}(v)) > \delta(  val^{\sigma}(v'), \textsf{col}(v)) \text{ where } \sigma(v) = (v,v').
$$

Intuitively: according to $val^{\sigma}$, playing $(v,u)$ is better than playing $\sigma(v)$.

Given a strategy $\sigma$ and an edge $e = (v,u)$ we use $\sigma[v \to e]$ to denote the strategy playing $e$ from $v$ and all other vertices follow $\sigma$.
Let us write $\sigma \le \sigma'$ if for all vertices $v$ we have $val^{\sigma}(v) \le   val^{\sigma'}(v)$,
and $\sigma < \sigma'$ if additionally $\neg (\sigma' \le \sigma)$.

The difficulty is that $e = (v,u)$ being switchable does not mean that it is a better move than $\sigma(v)$ in any context,
but only according to the value function $val^{\sigma}$, so it is not clear that $\sigma[v \to e]$ is better than $\sigma$.
Strategy improvement algorithms depend on the following two principles.

````{prf:property} Progress
:label: 1-property:progress

Let $\sigma$ be a strategy and let $e = (v,u)$ be a switchable edge. 
Then $\sigma < \sigma[v \to e]$.

````

````{prf:property} Optimality
:label: 1-property:optimality

Let $\sigma$ be a strategy that has no switchable edges, then $\sigma$ is optimal.

````

The algorithm is the following: start at an initial strategy $\sigma_0$. 
In each round $i$ compute $val^{\sigma_i}$ and look for a switchable edge.
If there exists a switchable edge $e_i = (v_i,v'_i)$, let $\sigma_{i+1} = \sigma_i[v_i \to e_i]$ and iterate to the next round.
Otherwise, return the optimal strategy $\sigma_i$.

The algorithm computes a sequence of strategies 
$\sigma_0 < \sigma_1 < \sigma_2 < \dots$.
Note that any such sequence must be finite, since at each step we strictly increase in the ordering and there are only finitely many (positional) strategies.

If both progress and optimality principles hold as stated this yields a strategy improvement algorithm computing the optimal strategy.
Unfortunately such ideal properties rarely hold and it is often necessary to state and prove weaker properties,
we refer to Chapter {ref}`3-chap:parity,4-chap:payoffs` for examples.

````{prf:remark} NEEDS TITLE AND LABEL 
In the description above we did not specify which switchable edge to choose.
Actually strategy improvement algorithms often switch more than one edge at a time, making this question worse: 
which subset of the switchable edges should be chosen? 
Many possible rules for choosing this set have been studied, as for instance the **greedy all-switches** rule.

In the description above we did not specify which switchable edge to choose.
Actually strategy improvement algorithms often switch more than one edge at a time, making this question worse: 
which subset of the switchable edges should be chosen? 
Many possible rules for choosing this set have been studied, as for instance the **greedy all-switches** rule. 

````

