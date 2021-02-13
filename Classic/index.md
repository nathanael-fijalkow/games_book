(2-part:index)=
# Classic

The first part of this book is called Classic: the results presented in these three chapters form the backbone for our understanding of two player zero sum games with perfect information.


The topic of  {ref}`Chapter <2-chap:regular>` is games with regular objectives, where regular means defined by automata.
The simplest case is reachability and safety objectives: their solution using the attractor computation is the most important and fundamental result in this book, it will be used as an ingredient and a tool in almost all algorithms.
The rest of the chapter studies infinitary objectives, meaning which depend on the set of colours visited infinitely many times.
The algorithms constructed in this chapter are all fixed point algorithms manipulating sets of vertices,
showing the tight connection between games and fixed point computations.


The next chapter ( {ref}`Chapter <3-chap:parity>`) is entirely devoted to parity games.
One of the most important open question in the field of games on graphs is the complexity of solving parity games:
it is known to be in $\NP$ and in $\coNP$, making it very unlikely to be for instance $\NP$-complete as this would imply that $\NP = \coNP$.
The best algorithms to date have quasipolynomial time complexity; we present three algorithms with this complexity.
In particular we give the first instantiations of value iteration and strategy improvement algorithms as generically defined in 
 {ref}`Section <1-sec:value_iteration>` and  {ref}`Section <1-sec:strategy_improvement>`.


The last chapter ( {ref}`Chapter <4-chap:payoffs>`) focusses on quantitative objectives defined by numerical payoff which includes mean payoff and discounted payoff.
They both share (part of) the complexity status of parity games: solving them is known to be in $\NP$ and in $\coNP$,
but not known to be in polynomial time. Together with the complexity of parity games, these are the most important open problems in the area of games on graphs.

These three classes of games are related in the following sense:
parity games reduce in polynomial time to mean payoff games, which themselves reduce in polynomial time to discounted payoff games.
The reductions operate at the level of the conditions and preserve the structure of the underlying graphs, 
suggesting that parity games is a special case of mean payoff games, and similarly for mean payoff games and discounted payoff games.

The best algorithms for mean payoff and discounted payoff games are subexponential (and use randomisation): the quasipolynomial time algorithms for parity games have not (yet?) been extended to mean payoff and discounted payoff games.
