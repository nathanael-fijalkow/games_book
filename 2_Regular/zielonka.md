(2-sec:zielonka)=
# The Zielonka tree

```{math}
\newcommand{\F}{\mathcal{F}} 
\newcommand{\LAR}{\mathrm{LAR}}
\newcommand{\Zielonka}{\mathrm{Zielonka}}
\newcommand{\depth}{\mathrm{depth}}
\newcommand{\support}{\mathrm{supp}}
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
\newcommand{\NL}{\textrm{NL}}
\newcommand{\PTIME}{\textrm{PTIME}}
\newcommand{\NP}{\textrm{NP}}
\newcommand{\coNP}{\textrm{coNP}}
\newcommand{\PSPACE}{\textrm{PSPACE}}
```
The Zielonka tree is a combinatorial structure associated with a Muller objective which very neatly exposes its properties.
As a warm-up we first present its predecessor the LAR construction, and then show the properties of Zielonka trees.
As we will see, the key feature of the Zielonka tree of a Muller objective $\Muller(\F)$ is to characterise its exact memory requirements.

## The latest appearance record

Muller objectives can be reduced to parity objectives, see~Section {ref}`1-sec:reductions` for an introduction to reductions between objectives.

```{prf:theorem} needs title 2-thm:LAR
:label: 2-thm:LAR
:nonumber:

Let $C = [1,d]$ be a set of colours and $\Muller(\F)$ a Muller objective.
There exists a deterministic parity automaton $\LAR_\F$ over the alphabet $C$ defining $\Muller(\F)$.
It has $d!$ states and has priorities in $[1,2d]$.

```

LAR stands for Latest Appearance Record.
In the literature the number of states is often $d \cdot d!$ instead of $d!$,
the multiplicative factor $d$ is saved since for automata the acceptance conditions are transition based 
instead of state based.

```{admonition} Proof
:class: dropdown tip

We define the automaton $\LAR_\F$.
The set of states is the set of lists of all colours of $C$ without repetitions.
We represent a list by $(c_1,\dots,c_d)$.
The initial state is irrelevant because $\Muller(\F)$ is prefix independent.
The transition function is defined as follows: 
$\delta(\ell, c)$ is $\ell'$ obtained from $\ell$ by pushing $c$ to the first position (hence shifting to the right the elements to the left of $c$). 
This is best understood on an example: 

$$
\delta( (4, 1, 2, 3), 2) = (2, 4, 1, 3).
$$

Let $j$ be the position of $c$ in $\ell$, the priority of this transition is defined by:

$$
\col((\ell,c,\ell')) =
\begin{cases}
2 j      & \text{ if } \ell([1,j]) \in \F, \\
2 j - 1  & \text{ otherwise.}
\end{cases}
$$


We now show that the automaton $\LAR_\F$ defines $\Muller(\F)$.
Let $\rho = c_0 c_1 \dots$ be an infinite word over the alphabet $C$. 
Let us consider the run of $\LAR_\F$ over $\rho$:

$$
(\ell_0,c_0,\ell_1) (\ell_1,c_1,\ell_2) \dots
$$

Let us write $j_i$ for the position of $c_i$ in $\ell_i$.
We consider $\Inf(\rho)$ the set of colours appearing infinitely many times and write $j$ for its cardinal.
From some point onwards the lists $\ell_i$ are of the form 

$$
(\underbrace{c_1,\dots,c_j}_{\Inf(\rho)} ,\ \underbrace{c_{j + 1},\dots,c_d}_{C \setminus \Inf(\rho)}).
$$

From this point on $j_i$ is smaller than or equal to $j$, and it reaches $j$ infinitely many times.
It follows that the largest priority appearing infinitely many times in the run is $2 j$ if $\Inf(\rho) \in \F$
and $2 j - 1$ if $\Inf(\rho) \notin \F$.
Thus $\rho$ is accepted by $\LAR_\F$ if and only if $\Inf(\rho) \in \F$, as desired.

```


## The Zielonka tree

 {prf:ref}`2-thm:LAR` implies a reduction from Muller games to parity games as explained in Section {ref}`1-sec:reductions`.
However this does not improve over the results we already obtained for Muller games in  {prf:ref}`2-thm:muller`,
neither algorithmically nor for the memory requirements.
One weakness of the LAR construction is that its size depends only on the number of colours, and not on the properties of $\F$.
The Zielonka tree is an improved take on the LAR.

```{prf:definition} Zielonka tree
:label: definition:zielonka_tree
:nonumber:

Let $\Muller(\F)$ be a Muller objective over the set of colours $C$.
The Zielonka tree $T_\F$ of $\Muller(\F)$ is a rooted tree with nodes labelled by subsets of colours, 
it is constructed inductively as follows:

*  the root is labelled $C$,
*  the children of a node labelled $S$ are the maximal subsets $S_1, \dots, S_k$ of $S$ such that 
$S_i \in \Muller(\F) \Longleftrightarrow S \notin \Muller(\F)$.

```


 {numref}`2-fig:Zielonka_tree_example` represents the Zielonka tree for $\Muller(\F)$ with 

$$
\F = \set{\set{2}, \set{3}, \set{4}, \set{1,2}, \set{1,3}, \set{1,3,4}, \set{2,3,4}, \set{1,2,3,4}}.
$$

We note that there are two nodes labelled $\set{1}$; in general there may be several nodes with the same label.
Also, not all branches have the same length.

```{figure} ./../2-fig:Zielonka_tree_example.png
:name: 2-fig:Zielonka_tree_example
:align: center
The Muller tree for $\Muller(\F)$. By convention nodes labelled by a set in $\F$ are represented by a circle
and the others by a square.
The numbers on the right hand side and the dashed nodes (describing a branch) are both used in the proof of  {prf:ref
```

The first use of the Zielonka tree is to induce an improved reduction from Muller to parity objectives.
A branch in a tree is a path from the root to a leaf.

```{prf:theorem} needs title 2-thm:reduction_parity_Zielonka_tree
:label: 2-thm:reduction_parity_Zielonka_tree
:nonumber:

Let $C = [1,d]$ be a set of colours and $\Muller(\F)$ a Muller objective.
There exists a deterministic parity automaton $\Zielonka_\F$ over the alphabet $C$ defining $\Muller(\F)$.
Its number of states is the number of branches of $T_\F$ and its parity condition uses $d$ priorities.

```

Here again we take advantage of the fact that the acceptance conditions on automata are transition based;
using stated based transitions we would have add a multiplicative factor $d$.

```{admonition} Proof
:class: dropdown tip

Without loss of generality $C \in \F$ (otherwise we consider the complement $\Muller(2^C \setminus \F)$).
We number the levels of $T_\F$ from the leaves to the root such that nodes labelled by sets in $\F$ are even
and the other ones odd (this will be used for defining the parity condition).
See  {numref}`2-fig:Zielonka_tree_example` for a possible numeration of the levels (on the right hand side), the other options being shifts of this numeration by an even number.

The set of states of $\Zielonka_\F$ is the set of branches of $T_\F$.
We represent a branch by $(S_1,\dots,S_k)$
where $S_1$ is the set labelling the root and $S_k$ the set labelling a leaf. Note that $k \le d$.
For the sake of simplicity we identify nodes with their labels, which is an abuse since two different nodes may have the same label
but will be convenient and harmless in our reasoning.

The initial state is irrelevant because $\Muller(\F)$ is prefix independent.
We define the support $\support(b,c)$ of a branch $b$ and a colour $c$ to be the lowest node of $b$ which contains $c$.
The transition function is defined as follows: 
$\delta(b,c)$ is the next branch (in the lexicographic order from left to right and in a cyclic way) which coincides with $b$ up to $\support(b,c)$.
The priority of this transition is given by the level on which $\support(b,c)$ sits.

This is best understood on an example: on  {numref}`2-fig:Zielonka_tree_example`
consider the branch $b$ represented by dashed nodes, reading the colour $2$ we consider branches starting with $(\set{1,2,3,4}, \set{1,2,3})$
because $\support(b,2) = \set{1,2,3}$.
The next branch after $b$ is $(\set{1,2,3,4}, \set{1,2,3},\set{1,2},\set{1})$ (because we cycle: the node after $\set{1,3}$ is $\set{1,2}$).
The priority of this transition is $3$ corresponding to the level where $\set{1,2,3}$ sits.

We now show that the automaton $\Zielonka_\F$ defines $\Muller(\F)$.
Let $\rho = c_0 c_1 \dots$ be an infinite word over the alphabet $C$.
Let us consider the run of $\Zielonka_\F$ over $\rho$:

$$
(b_0,c_0,b_1) (b_1,c_1,b_2) \dots
$$

We consider $\Inf(\rho)$ the set of colours appearing infinitely many times.
Let us look at the largest prefix $(S_1,\dots,S_p)$ of a branch which is eventually common to all the branches $b_i$.
We make two claims:

*  $\Inf(\rho)$ is included in $S_p$;
*  $\Inf(\rho)$ is not included in any child of $S_p$.

For the first claim, let $c \in \Inf(\rho)$, since eventually the branch $b_i$ starts with $(S_1,\dots,S_p)$,
the support of $b_i$ and $c$ is lower than or equal to $S_p$, meaning that $c \in S_p$.

For the second claim, we first note that by maximality of $(S_1,\dots,S_p)$ the support of $b_i$ and $c_i$ is infinitely many times $S_p$.
Indeed from some point onwards it is lower than or equal to $S_p$, and if it would be eventually strictly lower then the corresponding child of $S_p$ would be common to all branches $b_i$ from there on.
This implies that all children of $S_p$ appear infinitely many times in the branches $b_i$: each time the support of $b_i$ and $c_i$ is $S_p$, the branch switches to the next child of $S_p$.
Now since each child $S_{p+1}$ of $S_p$ is left infinitely many times this implies that there exists $c \in \Inf(\rho)$ with $c \notin S_{p+1}$.
Hence $\Inf(\rho)$ is not included in $S_{p+1}$.

By definition of the Zielonka tree, this implies that $\Inf(\rho) \in \F$ if and only if $S_p \in \F$,
thus $\rho$ is accepted by $\Zielonka_\F$ if and only if $\Inf(\rho) \in \F$, as desired.

```

Since  {prf:ref}`2-thm:reduction_parity_Zielonka_tree` is a reduction from Muller to parity objectives,
it implies a reduction from Muller games to parity games as explained in Section {ref}`1-sec:reductions`,
improving over  {prf:ref}`2-thm:LAR`. 
Since solving parity games is in $\NP \cap \coNP$,
if we represent the Muller condition by a Zielonka tree then the automaton constructed in  {prf:ref}`2-thm:reduction_parity_Zielonka_tree`
is of polynomial size, implying the following result.

```{prf:theorem} needs title and label 
Solving Muller games where the condition is represented by a Zielonka tree is in $\NP \cap \coNP$.
 
:label: 
Solving Muller games where the condition is represented by a Zielonka tree is in $\NP \cap \coNP$.

:nonumber:

Solving Muller games where the condition is represented by a Zielonka tree is in $\NP \cap \coNP$.

```

As observed above different nodes of the Zielonka tree may be labelled by the same set of colours.
Hence it is tempting to represent a Muller condition not with its Zielonka tree but rather with the Zielonka DAG (Directed Acyclic Graph)
where nodes labelled by the same set of colours are identified.
However with this representation solving Muller games is again $\PSPACE$-complete:

```{prf:theorem} needs title 2-thm:Muller_games_DAG
:label: 2-thm:Muller_games_DAG
:nonumber:

Solving Muller games where the condition is represented by a Zielonka DAG is $\PSPACE$-complete.

```

The algorithm presented in  {prf:ref}`2-thm:muller` runs in polynomial space for this representation.
To obtain the $\PSPACE$-hardness we observe that in the reduction from QBF constructed in  {prf:ref}`2-thm:complexity_Muller`,
the Muller objective is of polynomial size when represented by a Zielonka DAG (but of exponential size when represented by a Zielonka tree).

## The exact memory requirements

The second and most interesting use of the Zielonka tree is for characterising the memory requirements.

Note that a node in the Zielonka tree $T_\F$ represents another Muller objective, over the set of colours labelling this node.
For instance in  {numref}`2-fig:Zielonka_tree_example` the node labelled $\set{1,2,3}$ corresponds to $\Muller(\F')$ with
$\F' = \set{\set{2}, \set{3}, \set{1,2}, \set{1,3}}$.

```{prf:definition} needs title and label 
Let $\Muller(\F)$ be a Muller objective over the set of colours $C$.
We define $m_\F$ by induction:

*  if the tree consists of a single leaf, then $m_\F = 1$;
*  otherwise, let $\F_1,\dots,\F_k$ be the Muller objectives defined by the children of the root,
there are two cases:
\begin{itemize}
*  if $C \in \F$, then $m_\F$ is the **sum** of $m_{\F_1},\dots,m_{\F_k}$;
*  if $C \notin \F$, then $m_\F$ is the **maximum** of $m_{\F_1},\dots,m_{\F_k}$.

\end{itemize}
 
:label: 
Let $\Muller(\F)$ be a Muller objective over the set of colours $C$.
We define $m_\F$ by induction:

*  if the tree consists of a single leaf, then $m_\F = 1$;
*  otherwise, let $\F_1,\dots,\F_k$ be the Muller objectives defined by the children of the root,
there are two cases:
\begin{itemize}
*  if $C \in \F$, then $m_\F$ is the **sum** of $m_{\F_1},\dots,m_{\F_k}$;
*  if $C \notin \F$, then $m_\F$ is the **maximum** of $m_{\F_1},\dots,m_{\F_k}$.

\end{itemize}

:nonumber:

Let $\Muller(\F)$ be a Muller objective over the set of colours $C$.
We define $m_\F$ by induction:

*  if the tree consists of a single leaf, then $m_\F = 1$;
*  otherwise, let $\F_1,\dots,\F_k$ be the Muller objectives defined by the children of the root,
there are two cases:
\begin{itemize}
*  if $C \in \F$, then $m_\F$ is the **sum** of $m_{\F_1},\dots,m_{\F_k}$;
*  if $C \notin \F$, then $m_\F$ is the **maximum** of $m_{\F_1},\dots,m_{\F_k}$.

\end{itemize}

```

For the Muller objective represented in  {numref}`2-fig:Zielonka_tree_example`, we have $m_\F = 3$.
In the following result we consider **partial** colouring functions: $\col : V \to C \cup \set{\emptyset}$,
meaning that some vertices can be left uncolored (formally, labelled $\emptyset$).

```{prf:theorem} needs title 2-thm:characterisation_Zielonka_tree
:label: 2-thm:characterisation_Zielonka_tree
:nonumber:

Muller objectives $\Muller(\F)$ are determined with finite memory strategies of size $m_\F$
for games with **partial colouring functions** (See \cref{2-rmk:finite_infinit) for the case of infinite games.}.
This bound is tight: there exists a game with objective $\Muller(\F)$ where Eve wins using $m_\F$ memory states
but not with less.

```

Let us show on an example that the assumption of partial colouring functions is necessary.
Let $\F = \set{ \set{1,2} }$: the objective $\Muller(\F)$ requires that both $1$ and $2$ are seen infinitely many times.
The Zielonka tree $T_\F$ has three nodes $\set{1,2}, \set{1}$, and $\set{2}$, and $m_\F = 2$.
Indeed $\Muller(\F)$ is determined with finite memory strategies of size $2$:
intuitively the memory structure is used to remember which colour was last seen.
A game with a partial colouring function where two memory states is necessary is presented in {numref}`2-fig:lower_bound_zielonka`.
However, $\Muller(\F)$ is positionally determined for games with total colouring functions (as we have defined them originally):
intuitively since every vertex has colour either $1$ or $2$, there is no need to remember which colour was last seen.

```{figure} ./../2-fig:lower_bound_zielonka.png
:name: 2-fig:lower_bound_zielonka
:align: center
A game with a partial colouring function 
where Eve has a winning strategy for $\Muller(\F)$ with $\F = \set{ \set{1,2
```



We will not construct the lower bound, meaning the game where Eve needs $m_\F$ memory states to win.
However, we will now prove the upper bound.
To this end we revisit the recursive algorithm presented in  {prf:ref}`2-lem:Muller_even` and  {prf:ref}`2-lem:Muller_odd`.
This algorithm was removing colours one by one and rely on the recursive solutions.
We show that we can adapt the algorithm to follow instead the structure of the Zielonka tree: 
for solving a Muller game, it is enough to recursively solve the induced Muller games
corresponding to the children of the root of the Zielonka tree.
The following lemma is an improved variant of  {prf:ref}`2-lem:Muller_even`.

```{prf:lemma} needs title 2-lem:McNaughton_Zielonka_even
:label: 2-lem:McNaughton_Zielonka_even
:nonumber:

Let $\Game$ be a Muller game with objective $\Muller(\F)$ such that $C \in \F$.
Let $C_1, \dots, C_k$ be the maximal subsets of $C$ such that $C_i \notin \F$.
We let $\F_1,\dots,\F_k$ be the corresponding induced Muller objectives,
and define $\Game_i$ be the subgame of $\Game$ induced by $V \setminus \AttrE(C \setminus C_i)$
with objective $\Muller(\F_i)$.

*  If for all $i \in [1,k]$, we have $\WA(\Game_i) = \emptyset$, then $\WE(\Game) = V$.
*  If there exists $i \in [1,k]$ such that $\WA(\Game_i) \neq \emptyset$,
let $\Game'$ be the subgame of $\Game$ induced by $V \setminus \AttrA( \WA(\Game_i) )$,
then $\WE(\Game) = \WE(\Game')$.

```

We will prove the memory requirement at the same time inductively.
Note that by duality, the case where $C \notin \F$ corresponds to the memory requirement for Adam when $C \in \F$:

$$
m_{2^C \setminus \F} = \max_{i \in [1,k]} m_{2^{C_i} \setminus \F_i}.
$$



```{admonition} Proof
:class: dropdown tip

We prove the first item.

For each $i \in [1,k]$, let $\sigma_i$ be an attractor strategy ensuring to reach $C_i$ from $\AttrE(C_i)$,
and consider a winning strategy for Eve from $V \setminus \AttrE(C_i)$ in $\Game_i$, it induces a strategy $\sigma'_i$ in $\Game$.
We construct a strategy $\sigma$ in $\Game$ which will simulate the strategies above in turn; to do so it uses $[1,k]$ as top-level memory states.
(We will look at more closely at the memory structure at the end of the proof.)
The strategy $\sigma$ with memory $i$ simulates $\sigma_i$ from $\AttrE(C_i)$ and $\sigma'_i$ from $V \setminus \AttrE(C_i)$,
and if it ever reaches a vertex in $C_i$ it updates its memory state to $i + 1$ and $1$ if $i = k$.
Any play consistent with $\sigma$ either updates its memory state infinitely many times, 
or eventually remains in $V \setminus \AttrE(C_i)$ and is eventually consistent with $\sigma'_i$.
In the first case it sees a colour from each $C_i$ infinitely many times, so by definition of the $C_i$'s and since $C \in \F$ 
the play satisfies $\Muller(\F)$, 
and in the other case since $\sigma'_i$ is winning the play satisfies $\Muller(\F)$.
Thus $\sigma$ is winning from $V$.

Let us now discuss how many memory states are necessary to implement the strategy $\sigma$.
By induction hypothesis, each of the strategies $\sigma'_i$ uses $m_{\F_i}$ memory states.
Using a disjoint union of the memory structures we implement $\sigma$ using $\sum_{i \in [1,k]} m_{\F_i}$ memory states,
corresponding to the definition of $m_\F$.


We now look at the second item.

Consider a winning strategy for Adam from $\WA(\Game_i)$ in $\Game_i$, it induces a strategy $\tau_i$ in $\Game$.
Since $V \setminus \AttrE(C_i)$ is a trap for Eve, this implies that $\tau_i$ is a winning strategy in $\Game$.
Let $\tau_a$ denote an attractor strategy from $\AttrA(\WA(\Game_i)) \setminus \WA(\Game_i)$.
Consider now a winning strategy in the game $\Game'$ from $\WA(\Game')$, it induces a strategy $\tau'$ in $\Game$.
The set $V \setminus \AttrA( \WA(\Game_i) )$ may not be a trap for Eve, so we cannot conclude that $\tau'$ is a winning strategy in $\Game$,
and it indeed may not be.
We construct a strategy $\tau$ in $\Game$ as the (disjoint) union of the strategy $\tau_a$ on $\AttrA(\WA(\Game_i)) \setminus \WA(\Game_i)$,
the strategy $\tau_i$ on $\WA(\Game_i)$ and the strategy $\tau'$ on $\WA(\Game')$.
We argue that $\tau$ is winning from $\AttrA( \WA(\Game_i) ) \cup \WA(\Game')$ in $\Game$.
Indeed, any play consistent with this strategy in $\Game$ either stays forever in $\WA(\Game')$ hence is consistent with $\tau'$
or enters $\AttrA( \WA(\Game_i) )$, so it is eventually consistent with $\tau_i$.
In both cases this implies that the play is winning.
Thus we have proved that $\AttrA( \WA(\Game_c) ) \cup \WA(\Game') \subseteq \WA(\Game)$.

We now show that $\WE(\Game') \subseteq \WE(\Game)$, which implies the converse inclusion.
Consider a winning strategy from $\WE(\Game')$ in $\Game'$, it induces a strategy $\sigma$ in $\Game$.
Since $\Game'$ is a trap for Adam, any play consistent with $\sigma$ stays forever in $\WE(\Game')$, 
implying that $\sigma$ is winning from $\WE(\Game')$ in $\Game$.

Let us now discuss how many memory states are necessary to implement the strategy $\tau$.
By induction hypothesis, the strategy $\tau_i$ uses $m_{2^{C_i} \setminus \F_i}$ memory states
and the strategy $\tau'$ uses $\max_{j \neq i} m_{2^{C_j} \setminus \F_j}$ memory states.
Since $\tau$ is a disjoint union of strategies the memory can be reused so we can implement $\tau$ using $\max_{i \in [1,k]} m_{2^{C_i} \setminus \F_i}$ memory states, corresponding to the definition of $m_{2^C \setminus \F}$.

```

The corresponding lemma when $C \notin \F$ is stated below, its proof is analogous to the previous one by swapping the two players.

```{prf:lemma} needs title 2-lem:McNaughton_Zielonka_odd
:label: 2-lem:McNaughton_Zielonka_odd
:nonumber:

Let $\Game$ be a Muller game such that $C \notin \F$.
Let $C_1, \dots, C_k$ be the maximal subsets of $C$ such that $C_i \in \F$.
We let $\F_1,\dots,\F_k$ be the corresponding induced Muller objectives,
and define $\Game_i$ be the subgame of $\Game$ induced by $V \setminus \AttrA(C \setminus C_i)$ with objective $\Muller(\F_i)$.

*  If for all $i \in [1,k]$, we have $\WE(\Game_i) = \emptyset$, then $\WA(\Game) = V$.
*  If there exists $i \in [1,k]$ such that $\WE(\Game_i) \neq \emptyset$,
let $\Game'$ be the subgame of $\Game$ induced by $V \setminus \AttrE( \WE(\Game_i) )$,
then $\WA(\Game) = \WA(\Game')$.

```


## Revisiting Streett, Rabin, and parity objectives

Let us look at the Streett, Rabin, and parity objectives under the new light shed by  {prf:ref}`2-thm:characterisation_Zielonka_tree`.
It is instructive to look at the Zielonka tree of a Rabin objective, illustrated in  {numref}`2-fig:Zielonka_tree_Rabin`.
It has a simple recursive structure: the Zielonka tree of the Rabin objective for $d$ pairs contains $d$ copies
of the Zielonka tree of the Rabin objective for $d-1$ pairs.
Naturally, this implies that $m_{\Rabin} = 1$, so  {prf:ref}`2-thm:characterisation_Zielonka_tree` induces the positional determinacy result
stated in  {prf:ref}`2-thm:Rabin_positional_determinacy`.
Note that the two proofs are very different: the proof of  {prf:ref}`2-thm:characterisation_Zielonka_tree` is by induction over the Zielonka tree and can be extended to infinite games, while the proof of  {prf:ref}`2-thm:submixing_positional` applies only to finite games but gives a general sufficient condition for positionality.

```{figure} ./../2-fig:Zielonka_tree_Rabin.png
:name: 2-fig:Zielonka_tree_Rabin
:align: center
The (beginning of the) Zielonka tree for $\Rabin$ with three pairs: 
$C = \set{G_1,R_1,G_2,R_2,G_3,R_3
```

Recall that we defined Streett objectives using closure under union, and Rabin objectives as the complement of Streett objectives.

```{prf:theorem} needs title and label 
Let $\Muller(\F)$ be a Muller objective.

*  $\Muller(\F)$ is positionally determined if and only if $\Muller(\F)$ is a Rabin objective;
*  $\Muller(\F)$ is positionally determined for both players if and only if $\Muller(\F)$ is a parity objective.

 
:label: 
Let $\Muller(\F)$ be a Muller objective.

*  $\Muller(\F)$ is positionally determined if and only if $\Muller(\F)$ is a Rabin objective;
*  $\Muller(\F)$ is positionally determined for both players if and only if $\Muller(\F)$ is a parity objective.

:nonumber:

Let $\Muller(\F)$ be a Muller objective.

*  $\Muller(\F)$ is positionally determined if and only if $\Muller(\F)$ is a Rabin objective;
*  $\Muller(\F)$ is positionally determined for both players if and only if $\Muller(\F)$ is a parity objective.

```

This theorem gives a characterisation of Rabin and parity objectives: they form the class of Muller objectives which are respectively positional and positional for both players.

```{admonition} Proof
:class: dropdown tip

Thanks to  {prf:ref}`2-thm:characterisation_Zielonka_tree` the objective $\Muller(\F)$ is positionally determined if and only if $m_\F = 1$, which is equivalent to saying that all nodes labelled $S \in \F$ in the Zielonka tree of $\F$ have at most one child. Indeed, for such nodes the number $m$ is obtained as the sum of the numbers for the children, so there can be at most one, and conversely if this is the case then $m_\F = 1$.
This characterisation of the Zielonka tree is equivalent to the complement of $\F$ being closed under union:

*  Assume that the complement of $\F$ is closed under union and let $S \in \F$ be a node in the Zielonka tree of $\F$.
Let $S_1,\dots,S_k$ be the children of $S$, by definition they are the maximal subsets of $S$ such that $S_i \notin \F$.
The union $\bigcup_i S_i$ is a subset of $S$ and by closure under union of the complement of $\F$ it is in the complement of $\F$, 
implying by maximality that it is one of the children, so they are all equal and $k = 1$.
*  Conversely, assume that all nodes labelled $S \in \F$ in the Zielonka tree of $\F$ have at most one child.
Let $S_1,S_2 \notin \F$, towards contradiction assume that $S_1 \cup S_2 \in \F$.
By definition of the Zielonka tree, if $S_1 \cup S_2$ is included into a node $S \notin \F$, 
then $S_1 \cup S_2$ is included into one of its children. 
Starting from the root and applying this we find a node $S \in \F$ such that $S_1 \cup S_2 \subseteq S$
and $S_1 \cup S_2 \not\subseteq S'$ with $S'$ the only child of $S$ 
(the case where $S$ does not have any children is easy and treated separately).
By definition of the Zielonka tree, since $S_1,S_2 \notin \F$ and $S_1,S_2 \subseteq S$, then $S_1,S_2 \subseteq S'$, implying that 
$S_1 \cup S_2 \subseteq S'$, a contradiction.

We have proved the first equivalence: $\Muller(\F)$ is positionally determined if and only if the complement of $\F$ is closed under union, which is the definition of Rabin objectives.

For the second equivalence, we already have that $\Muller(\F)$ is positionally determined for both players if and only if all nodes in the Zielonka tree of $\F$ have at most one child. The Zielonka tree is in this case a chain:

$$
S_1 \subseteq S_2 \subseteq S_3 \subseteq S_4 \subseteq \cdots \subseteq S_{2d-1} \subseteq S_{2d} \subseteq C,
$$

with $S_{2i} \in \F$ and $S_{2i-1} \notin \F$.
Then $X \in \F$ is equivalent to asking that the largest $i \in [1,d]$ such that if $X \cap S_i \neq \emptyset$ is even.
Assigning priority $i$ to $S_i$ we get that $X \in \Muller(\F)$ if and only if 
the largest priority appearing infinitely many times in $X$ is even: 
this is the definition of the parity objective over the set of priorities $[1,2d]$.
Conversely, we observe that the Zielonka tree of a parity objective is indeed a chain.

```



