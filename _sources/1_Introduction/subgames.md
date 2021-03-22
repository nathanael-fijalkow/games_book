(1-sec:subgames)=
# Traps and subgames

Let us consider a game $\mathcal{G}$ and a set $X$ of vertices.
Assume that for every $v \in X$ there exists $(v,v') \in E$ such that $v' \in X$,
then we can define the game $\mathcal{G}[X]$ by restricting $\mathcal{G}$ to the vertices in $X$
and say that $\mathcal{G}[X]$ is the subgame of $\mathcal{G}$ induced by $X$.
Formally, the arena is $\mathcal{A}[X]$ with $X$ the set of vertices and $E[X]$ is the set of edges 
such that both incoming and outgoing vertices are in $X$.
The assumption on $X$ ensures that every vertex of $\mathcal{G}[X]$ has an outgoing edge.
Both the colouring function and the conditions are naturally induced from $\mathcal{G}$ to $\mathcal{G}[X]$.

We say that $X$ is a trap for Adam if

*  for every $v \in X \cap  V_\mathrm{Eve}$, there exists $(v,v') \in E$ such that $v' \in X$, and 
*  for every $v \in X \cap  V_\mathrm{Adam}$, for all $(v,v') \in E$ we have $v' \in X$.

Intuitively, a trap for Adam is a subset of vertices which Eve can decide to stay in while Adam cannot force to leave.
The same notion can be defined for Eve.
Traps satisfy the property above so if $X$ is a trap then the game $\mathcal{G}[X]$ described above is well defined, meaning 
that every vertex has an outgoing edge.

````{prf:observation} Traps induce subgames
:label: 1-fact:traps_induce_subgames

Let $\mathcal{G}$ be a game, $X$ a trap for Adam, and $\sigma$ a winning strategy for Eve in the subgame $\mathcal{G}[X]$.
Then $\sigma$ induces a winning strategy in $\mathcal{G}$.

````

````{admonition} Proof
:class: dropdown tip

Any play consistent with $\sigma$ in $\mathcal{G}$ stays forever in $X$ because $X$ is a trap for Adam, hence is winning.

````

The notion of traps is very useful when decomposing games.
We present some simple facts about traps, here stated for Adam but easily transposed for Eve.

````{prf:observation} Traps
:label: 1-fact:traps

Let $\mathcal{G}$ a game.

*  Let $P,Q$ two traps for Adam in the game $\mathcal{G}$, then $P$ is a trap for Adam in the subgame of $\mathcal{G}$ induced by $Q$ 
(but $P \cap Q$ may not be a trap in $\mathcal{G}$).
*  Let $P$ a trap for Eve in the game $\mathcal{G}$ and $Q$ a trap for Adam in the game $\mathcal{G}$, 
then $P \cap Q$ is a trap for Eve in the subgame of $\mathcal{G}$ induced by $Q$.
*  Let $P$ a trap for Adam in the game $\mathcal{G}$ and $Q$ a trap for Adam in the subgame of $\mathcal{G}$ induced by $X$,
then $Q$ is a trap for Adam in $\mathcal{G}$.

````

