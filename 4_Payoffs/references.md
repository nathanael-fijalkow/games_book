(4-sec:references)=
# Bibliographic references

```{math}

```

One player variants due to Karp {cite}`Karp:1978`

{prf:ref}`4-thm:shortest path-positive`
{cite}`Khachiyan&al:2008`

NP and coNP: {cite}`Puri:1995`?

This chapter has been the occasion to start revealing a ladder of
reductions going up from parity games to discounted payoff games,
going through mean payoff games: it shows that parity games are the
simplest fragment of games from a computational perspective, in
$\textrm{UP}\cap  \textrm{coUP}$. In Chapter {ref}`6-chap:stochastic`, the last reduction from
discounted payoff games to simple stochastic games will complete the
computational landscape.

Mean payoff games have been first studied by Ehrenfeucht and Mycielski
in {cite}`Ehrebfeucht&Mycielski:1979` where positional determinacy is
shown. It is much later that Zwick and
Paterson {cite}`Zwick&Paterson:1996` first obtained the
pseudopolynomial value iteration algorithm to solve them, while
introducing discounted payoff games (that had been first studied in a
probabilistic setting as will be studied in Chapter {ref}`5-chap:MDP` and
Chapter {ref}`6-chap:stochastic`).

We have followed the proof of Ehrenfeucht and
Mycielski {cite}`Ehrebfeucht&Mycielski:1979` to prove the positional
determinacy of mean payoff games. In 2004, Bj\orklund, Sandberg and
Vorobyov {cite}`Bjorklund&Sandberg&Vorobyov:2004` claimed a simpler
proof that works directly, with no back-and-forth reasoning between
the first cycle objective and the original mean payoff one: however,
their proof technique has been shown incorrect by Aminof and
Rubin {cite}`Aminof&Rubin:2017`, who also correct it by studying
further the first-cycle games.

We gave several algorithms to solve mean payoff games, apart from the
one of Zwick and Paterson {cite}`Zwick&Paterson:1996`.

The **strategy improvement technique** is due to Bj\orklund and
Vorobyov {cite}`Bjorklund&Vorobyov:2007`, presented via the new notion
of **longest shortest path problem (LSP)**. Other solutions to
obtain a strategy iteration algorithm for mean payoff games work by
adding gain and bias variables to the system, as may be studied
in {cite}`Filar&Vrieze:1996` for concurrent mean payoff games.  Strategy
improvement methods (for parity games or payoff games) are very close
to the simplex method to solve linear programs. A more thorough
comparison can be found in {cite}`Allamigeon&Benchimol&al:2014`.  Lifshits and
Pavlov {cite}`Lifshits&Pavlov:2007` use the potential techniques of strategy
improvement for mean payoff games, with a reweighting of the arena in
order to obtain a $O(mn2^{n}\log W)$ algorithm (it may
then be useful if weights are much bigger than the number of
vertices).

The **value iteration algorithm** has been developed by Brim,
Chaloupka, Doyen, Gentilini, and
Raskin {cite}`Brim&Chaloupka&Doyen&Gentilini&Raskin:2011`. They also
introduce and solve the so-called **energy games**, that will be
studied more carefully in Chapter {ref}`12-chap:counters`. As for the strategy
improvement algorithm, it is paired with a binary search to compute
the values of the game (and not only decide whether Eve can guarantee
a positive mean payoff). Comin and Rizzi {cite}`Comin&Rizzi:2017` have
improved it to obtain a $O(n^2 m W)$ upper-bound, without
the $\log(n)+\log(W)$ term due to binary search.

We have motivated our study of quantitative games with the
$\mathtt{ShortestPath}$ objective, a very natural generalisation of both
(qualitative) reachability games and shortest path problems in
classical graph theory. The longest shortest path problem (LSP) of
Bj\"orklund and Vorobyov {cite}`Bjorklund&Vorobyov:2007`, though a
priori close, is indeed quite different. The requirement is there to
find the best possible **positional** strategy of Eve, so that the
length of the shortest path from every vertex to a target is as large
as possible (over all positional strategies). Because of the fact they
introduce these games to solve mean payoff games with a combinatorial
strongly subexponential strategy improvement algorithm, the definition
of what is a path from a vertex $v$ to a target is very different from
the one in shortest path games: in particular, if $v$ appears in a
cycle (even if it cannot reach the target), the length they consider
is $-\infty$ if the cycle has negative weight, $+\infty$ if the cycle
has positive weight, and $0$ if the cycle has weight zero. This is
thus an orthogonal generalisation, that is dedicated to the study of a
strategy iteration algorithm for mean payoff games: contrary to what
we have shown before for discounted payoff games, the situation is
much more complex for mean payoff games since the min-max operator
does not have a unique solution anymore, making difficult the search
for the accurate fixed point (as in the case of total payoff games).

As we have seen, shortest path games are solvable in polynomial time
when only non-negative weights appear on transitions, but no
polynomial solution is known (as for mean payoff or parity games) for
the general case. The best known at the time this chapter is written
is a polynomial time fragment consisting of **divergent
  shortest path games** {cite}`Busatto&Monmege&Reynier:2017` in which
the arena is supposed to contain no cycles of weight 0: this a priori
weak property indeed partition the strongly connected components of
the arena into the ones where all cycles are positive, and the ones
where all cycles are negative; in each of these components, it is
shown why the value iteration algorithm converges in polynomial
time. {prf:ref}`4-thm:-infty-MP` shows a polynomial time reduction between
the detection of vertices of optimal value $-\infty$ in a
shortest path game and the detection of vertices of negative optimale
value in the corresponding mean payoff games: however it is still open
to know the computational complexity of solving shortest path games
that are supposed to have no vertices of value $-\infty$.


```{bibliography}
:style: unsrtalpha
:filter: cited and chap == "4"
```