(4-sec:notations)=
# Notations

In this chapter all objectives we consider use the set of colours $C = \Z$ the set of integers 
(or $C = \Z \cup \set{\Win}$ for the shortest path objective), 
so a colour is called a weight interpreted as a payoff for Eve.
We will study different quantitative objectives corresponding to different ways of aggregating the weights.
Recall that in a quantitative objective Eve aims at maximising the outcome, while Adam
tries to minimise it.
We let $\ValueE^\game(v)$ and $\ValueA^\game(v)$ be the values for Eve and Adam in the game $\game$: 
this is the best each player can unilaterally guarantee from the vertex $v$, no matter which strategy the other player uses.
All the quantitative objectives we will study in this chapter are Borel, hence determined thanks to \cref{1-cor:borel_determinacy}: 
$\ValueE^\game(v) = \ValueA^\game(v)$ for all vertices $v$. 
We thus let $\Value^\game(v)$ denote this value (and $\Value(v)$ if $\Game$ is clear from the context).

For complexity statements we use the unit cost RAM model as defined in {ref}`Section <1-sec:computation>`.
For each objective we introduce we will discuss what is the relevant machine word size, both we can already make some preliminary remarks.
Let us consider a game $\Game$ with an objective using the set of colours $C = \Z$
and let $W$ denote the largest weight appearing in $\Game$ in absolute value.
Choosing the machine word size $w = \log(m) + \log(W)$ implies that an edge together with its weight can be stored in one machine word and that we can perform arithmetic operations on weights, hence for most objectives we will use the machine word size $w = \log(m) + \log(W)$.
The only exception will be the discounted payoff objectives, which additionally have a discount factor $\lambda \in (0,1)$
that needs to be given in the input.

