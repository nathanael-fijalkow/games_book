(13-sec:references)=
# Bibliographic references

```{math}

\def\payoff{f}

\def\Act{A}
\def\Agt{\mathcal{P}}
\def\move{\textsf{move}}
\def\Out{\textsf{Out}}
\def\Dev{\textsf{Dev}}
\def\maxinf{\text{\rm maxinf}}
\def\pes{\textsf{pes}}
\def\opt{\textsf{opt}}
\def\proj{\textsf{proj}}
\def\devg{\textsf{DevGame}}
\def\Coalition{\mathcal{C}}

```

Most results about equilibria fall into two-categories: they either prove
that equilibria always exist for some class of games, or they characterize
the complexity of finding a particular one.

## Existence results

Several authors have noticed that Nash equilibria always exist in turn-based
game for some classes of objectives, in particular this is true of
$\omega$-regular objectives.
The most general result of that kind, shows that this is true for all objectives
for which there exists finite memory optimal strategies {cite}`LeRoux&Pauly:2018`.

The notion of equilibrium we now call Nash equilibrium was
defined in the article of Nash {cite}`Nash:1950` in which he proves the
existence for a class of normal form game.
The Hawk-dove game we presented as an example in the first part of
this chapter is also called game of chicken.
The first reference to this game was by Smith and Price {cite}`Smith&Price:1973`.
The example of medium of access control we presented as a motivation was
studied from a game theoric point of view in {cite}`MacKenzie&Wicker:2003`.

The notion of subgame perfect equilibria is interesting because in games on
trees (or extensive games), for which they were originaly introduced, they
always exist. This results can be extended to game played on graph.
In particular subgame perfect equilibria always exist in reachability
games {cite}`Brihaye&Bruyere&DePril&Gimbert:2012`.

## Algorithms and complexity results

existence of Nash equilibria by Nash {cite}`Nash:1950,Nash:1951`,
and Kuhn's theorem by Kuhn {cite}`Kuhn:1953`.

The deviator construction and the algorithm presented in this chapter are based on {cite}`Bouyer&Brenguier&Markey&Ummels:2011,Brenguier:2012`.
Algorithms on admissible strategies on infinite games and the complexity of the related problems
were studied in
{cite}`Berwanger:2007,Brenguier&Raskin&Sassolas:2014`.
\todo{Romain: please check the refs}

Imperfect information games in the context of multiplayer games are difficult.
As soon as there are `information forks' interesting problems are indecidable.
Deciding whether two players can ensure an objective against a third player
is undecidable.
As a corollary the Nash equilibrium problem is also undecidable {cite}`Pnueli&Rosner:1990`.
The problem of Nash equilibrium is also undecidable in stochastic games even
with only three players {cite}`Bouyer&Markey&Stan:2014`.

In the first section we presented a polynomial algorithm for
finding pure Nash equilibria in normal form games.
It is actually also possible to find a mixed Nash equilibria in
polynomial time using linear programming.
The same extends to finding memoryless mixed Nash equilibria in concurrent
games, and even resilient equilbria {cite}`Brenguier:2016`,.

Action-graphs are succinct representation of matrix games. Indeed,
representing games with matrices can be costly when the number of
players increases. The size of the matrix is in fact exponential in the
number of players: when each player has two strategies there are
\(2^{\Agt}\) cells in the table.
The action-graph representation is more compact, and the representation can be
exponentially smaller.
Because of that, the algorithm is no longer polynomial.
If there are no constraints on the Nash equilibrium we are looking for, the
complexity of the problem cannot be characterized using classical classes
like  \textrm{NP}-completness because equilibria always
exists and thus the answer to the decision problem would always be true.
The characterization of the complexity was done using the PPAD class {cite}`Daskalakis&Goldberg&Papadimitriou:2009`.

Nash equilibria with LTL objectives is expressible in logics such as
strategy logic {cite}`Chatterjee&Henzinger&Piterman:2010` or ATL$^\ast$ {cite}`Alur&Henzinger&Kupferman:2002`, as well as other extensions of this equilibria.
However, satisfiability in these logic is difficult: it is
2 \textrm{EXP}-complete for ATL$^\ast$ and undecidable for
strategy logic in general.
An decidable fragment of strategy logic has been identified {cite}`Mogavero&Murano&Perelli&Vardi:2012`,
but remains difficult; it is 2 \textrm{EXP}-complete.


```{bibliography}
:style: unsrtalpha
:filter: cited and chap == "13"
```