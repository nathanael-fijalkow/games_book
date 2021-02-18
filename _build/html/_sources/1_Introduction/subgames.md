(1-sec:subgames)=
# Traps and subgames


```{math}
\newcommand{\Arena}{\arena}
\newcommand{\VE}{V_\mEve}
\newcommand{\VA}{V_\mAdam}
\newcommand{\mEve}{\mathrm{Eve}}
\newcommand{\mAdam}{\mathrm{Adam}}
```

Let us consider a game $\Game$ and a set $X$ of vertices.
Assume that for every $v \in X$ there exists $(v,v') \in E$ such that $v' \in X$,
then we can define the game $\Game[X]$ by restricting $\Game$ to the vertices in $X$
and say that $\Game[X]$ is the subgame of $\Game$ induced by $X$.
Formally, the arena is $\arenaX]$ with $X$ the set of vertices and $E[X]$ is the set of edges 
such that both incoming and outgoing vertices are in $X$.
The assumption on $X$ ensures that every vertex of $\Game[X]$ has an outgoing edge.
Both the colouring function and the conditions are naturally induced from $\Game$ to $\Game[X]$.


We say that $X$ is a trap for Adam if

*  for every $v \in X \cap V_\mathrm{Eve} there exists $(v,v') \in E$ such that $v' \in X$, and 
*  for every $v \in X \cap V_\mathrm{Adam} for all $(v,v') \in E$ we have $v' \in X$.

Intuitively, a trap for Adam is a subset of vertices which Eve can decide to stay in while Adam cannot force to leave.
The same notion can be defined for Eve.
Traps satisfy the property above so if $X$ is a trap then the game $\Game[X]$ described above is well defined, meaning 
that every vertex has an outgoing edge.

````{prf:observation} Traps induce subgames
:label: 1-fact:traps_induce_subgames

Let $\Game$ be a game, $X$ a trap for Adam, and $\sigma$ a winning strategy for Eve in the subgame $\Game[X]$.
Then $\sigma$ induces a winning strategy in $\Game$.

````

````{admonition} Proof
:class: dropdown tip

Any play consistent with $\sigma$ in $\Game$ stays forever in $X$ because $X$ is a trap for Adam, hence is winning.

````

The notion of traps is very useful when decomposing games.
We present some simple facts about traps, here stated for Adam but easily transposed for Eve.

````{prf:observation} Traps
:label: 1-fact:traps

Let $\Game$ a game.

*  Let $P,Q$ two traps for Adam in the game $\Game$, then $P$ is a trap for Adam in the subgame of $\Game$ induced by $Q$ 
(but $P \cap Q$ may not be a trap in $\Game$).
*  Let $P$ a trap for Eve in the game $\Game$ and $Q$ a trap for Adam in the game $\Game$, 
then $P \cap Q$ is a trap for Eve in the subgame of $\Game$ induced by $Q$.
*  Let $P$ a trap for Adam in the game $\Game$ and $Q$ a trap for Adam in the subgame of $\Game$ induced by $X$,
then $Q$ is a trap for Adam in $\Game$.

````

