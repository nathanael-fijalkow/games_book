(1-sec:subgames)=
# Traps and subgames

```{math}
\newcommand{\Eve}{\textrm{Eve}}
\newcommand{\Adam}{\textrm{Adam}}
\newcommand{\set}[1]{\left\{ #1 \right\}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Zinfty}{\Z \cup \set{\pm \infty}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\Rinfty}{\R \cup \set{\pm \infty}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\Qinfty}{\Q \cup \set{\pm \infty}}
\newcommand{\argmax}{\textrm{argmax}}
\newcommand{\argmin}{\textrm{argmin}}
\newcommand{\Op}{\mathbb{O}}
\newcommand{\Prob}{\mathbb{P}} \newcommand{\dist}{\mathcal{D}} \newcommand{\Dist}{\dist} \newcommand{\supp}{\textrm{supp}} 
\newcommand{\game}{\mathcal{G}} \renewcommand{\Game}{\game} \newcommand{\arena}{\mathcal{A}} \newcommand{\Arena}{\arena} 
\newcommand{\col}{\textsf{col}} \newcommand{\Col}{\col} 
\newcommand{\mEve}{\mathrm{Eve}}
\newcommand{\mAdam}{\mathrm{Adam}}
\newcommand{\mRandom}{\mathrm{Random}}
\newcommand{\vertices}{V} \newcommand{\VE}{V_\mEve} \newcommand{\VA}{V_\mAdam} \newcommand{\VR}{V_\mRandom} 
\newcommand{\ing}{\textrm{In}}
\newcommand{\Ing}{\ing}
\newcommand{\out}{\textrm{Out}}
\newcommand{\Out}{\out}
\newcommand{\dest}{\Delta} 
\newcommand{\WE}{W_\mEve} \newcommand{\WA}{W_\mAdam} 
\newcommand{\Paths}{\textrm{Paths}} \newcommand{\play}{\pi} \newcommand{\first}{\textrm{first}} \newcommand{\last}{\textrm{last}} 
\newcommand{\mem}{\mathcal{M}} \newcommand{\Mem}{\mem} 
\newcommand{\Pre}{\textrm{Pre}} \newcommand{\PreE}{\textrm{Pre}_\mEve} \newcommand{\PreA}{\textrm{Pre}_\mAdam} \newcommand{\Attr}{\textrm{Attr}} \newcommand{\AttrE}{\textrm{Attr}_\mEve} \newcommand{\AttrA}{\textrm{Attr}_\mAdam} \newcommand{\rank}{\textrm{rank}}
\renewcommand{\Win}{\textrm{Win}} 
\renewcommand{\Lose}{\textrm{Lose}} 
\newcommand{\Value}{\textrm{val}} 
\newcommand{\ValueE}{\textrm{val}_\mEve} 
\newcommand{\ValueA}{\textrm{val}_\mAdam}
\newcommand{\val}{\Value} 
\newcommand{\Automaton}{\mathbf{A}} 
\newcommand{\Safe}{\mathtt{Safe}}
\newcommand{\Reach}{\mathtt{Reach}} 
\newcommand{\Buchi}{\mathtt{Buchi}} 
\newcommand{\CoBuchi}{\mathtt{CoBuchi}} 
\newcommand{\Parity}{\mathtt{Parity}} 
\newcommand{\Muller}{\mathtt{Muller}} 
\newcommand{\Rabin}{\mathtt{Rabin}} 
\newcommand{\Streett}{\mathtt{Streett}} 
\newcommand{\MeanPayoff}{\mathtt{MeanPayoff}} 
\newcommand{\DiscountedPayoff}{\mathtt{DiscountedPayoff}}
\newcommand{\Energy}{\mathtt{Energy}}
\newcommand{\TotalPayoff}{\mathtt{TotalPayoff}}
\newcommand{\ShortestPath}{\mathtt{ShortestPath}}
\newcommand{\Sup}{\mathtt{Sup}}
\newcommand{\Inf}{\mathtt{Inf}}
\newcommand{\LimSup}{\mathtt{LimSup}}
\newcommand{\LimInf}{\mathtt{LimInf}}
\newcommand{\NP}{\textrm{NP}}
\newcommand{\coNP}{\textrm{coNP}}
\newcommand{\PSPACE}{\textrm{PSPACE}}
\newcommand{\PTIME}{\textrm{PTIME}}
```
Let us consider a game $\Game$ and a set $X$ of vertices.
Assume that for every $v \in X$ there exists $(v,v') \in E$ such that $v' \in X$,
then we can define the game $\Game[X]$ by restricting $\Game$ to the vertices in $X$
and say that $\Game[X]$ is the subgame of $\Game$ induced by $X$.
Formally, the arena is $\Arena[X]$ with $X$ the set of vertices and $E[X]$ is the set of edges 
such that both incoming and outgoing vertices are in $X$.
The assumption on $X$ ensures that every vertex of $\Game[X]$ has an outgoing edge.
Both the colouring function and the conditions are naturally induced from $\Game$ to $\Game[X]$.


We say that $X$ is a trap for Adam if

*  for every $v \in X \cap \VE$, there exists $(v,v') \in E$ such that $v' \in X$, and 
*  for every $v \in X \cap \VA$, for all $(v,v') \in E$ we have $v' \in X$.

Intuitively, a trap for Adam is a subset of vertices which Eve can decide to stay in while Adam cannot force to leave.
The same notion can be defined for Eve.
Traps satisfy the property above so if $X$ is a trap then the game $\Game[X]$ described above is well defined, meaning 
that every vertex has an outgoing edge.

```{prf:observation} Traps induce subgames
:label: 1-fact:traps_induce_subgames
:nonumber:

Let $\Game$ be a game, $X$ a trap for Adam, and $\sigma$ a winning strategy for Eve in the subgame $\Game[X]$.
Then $\sigma$ induces a winning strategy in $\Game$.

```

```{admonition} Proof
:class: dropdown tip

Any play consistent with $\sigma$ in $\Game$ stays forever in $X$ because $X$ is a trap for Adam, hence is winning.

```

The notion of traps is very useful when decomposing games.
We present some simple facts about traps, here stated for Adam but easily transposed for Eve.

```{prf:observation} Traps
:label: 1-fact:traps
:nonumber:

Let $\Game$ a game.

*  Let $P,Q$ two traps for Adam in the game $\Game$, then $P$ is a trap for Adam in the subgame of $\Game$ induced by $Q$ 
(but $P \cap Q$ may not be a trap in $\Game$).
*  Let $P$ a trap for Eve in the game $\Game$ and $Q$ a trap for Adam in the game $\Game$, 
then $P \cap Q$ is a trap for Eve in the subgame of $\Game$ induced by $Q$.
*  Let $P$ a trap for Adam in the game $\Game$ and $Q$ a trap for Adam in the subgame of $\Game$ induced by $X$,
then $Q$ is a trap for Adam in $\Game$.

```

