(4-sec:qualitative)=
# Refining qualitative objectives with quantities

In this section we define quantitative objectives extending the qualitative objectives $\Safe$, $\Reach$, $\Buchi$, and $\CoBuchi$.

The four quantitative objectives we will define in this section return as outcome some weight in the sequence (for instance, the maximum weight).
This is in contrast with the $\MeanPayoff$ and $\DiscountedPayoff$ objectives that we will study later,
which perform **arithmetic operations** on the sequence of weights.

A first way to compute a payoff from a sequence of weights $\rho \in \Z^\omega$ is to consider the maximum weight in the sequence:

$$
\Sup(\rho) = \sup_i \rho_i.
$$

This extends the qualitative objective $\Reach[\Win]$ in the following sense: 
the objective $\Reach[\Win]$ corresponds to the quantitative objective $\Sup$ using two weights: $0$ for $\Lose$ and $1$ for $\Win$.
The outcome of a sequence is $1$ if and only if the sequence contains $\Win$.
It refines $\Reach[\Win]$ by specifying (numerical) preferences.

The dual objective is to consider the smallest weight:

$$
\Inf(\rho) = \inf_i \rho_i.
$$

The qualitative objective $\Safe[\Win]$ corresponds to the quantitative objective $\Inf$
using two weights: $0$ for $\Win$ and $1$ for $\Lose$.
The outcome of a sequence is $0$ if and only if the sequence does not contain $\Lose$.

Similarly the following quantitative objectives refine $\Buchi$ and $\CoBuchi$:

$$
  \LimSup(\rho) = \limsup_i \rho_i,\qquad 
  \LimInf(\rho) = \liminf_i \rho_i.
$$


The analyses and algorithms for solving games with $\Reach$, $\Safe$, $\Buchi$, and $\CoBuchi$ objectives extend to these four quantitative objectives.

```{admonition} Theorem
:class: theorem
:name: 4-thm:sup-inf-limsup-liminf

Games with objectives $\Sup$ and $\LimSup$ are uniformly positionally determined for both players.
There exists an algorithm for computing the value function of both games in polynomial time and space.
More precisely, let $k$ be the number of different weights in the game,
the time complexity is $O(m)$ for objective $\Sup$ and $O(knm)$ for objective $\LimSup$,
and for both algorithms the space complexity is $O(m)$.

```


```{admonition} Proof
:class: dropdown tip

We sketch the algorithm for the objective $\Sup$, the cae $\LimSup$ is similar.
Let $c_1 < \dots < c_k$ be the ordered enumeration of all weights in the game.
The set of vertices of value $c_k$ is $\AttrE(c_k)$, which can be computed in linear time.
We then construct the subgame $\Game'$ of $\Game$ induced by $V \setminus \AttrE(c_k)$,
and continue recursively: $\Game'$ has one less weight.

A naive complexity analysis yields a time complexity $O(km)$, but it is easily refined to $O(m)$ 
by revisiting the attractor computation and showing that each edge in the whole game is treated at most once
throughout the recursive attractor computations.
This complexity analysis does not extend to $\LimSup$ objectives, where the complexity is multiplied by $k$.

```

