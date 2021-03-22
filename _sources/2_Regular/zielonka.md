(2-sec:zielonka)=
# Zielonka tree

The Zielonka tree is a combinatorial structure associated with a Muller objective which very neatly exposes its properties.
As a warm-up we first present its predecessor the LAR construction, and then show the properties of Zielonka trees.
As we will see, the key feature of the Zielonka tree of a Muller objective $\mathtt{Muller}( \mathcal{F})$ is to characterise its exact memory requirements.

## The latest appearance record

Muller objectives can be reduced to parity objectives, see Section {ref}`1-sec:reductions` for an introduction to reductions between objectives.

````{prf:theorem} Latest Appeareance Record (LAR) construction
:label: 2-thm:LAR

Let $C = [1,d]$ be a set of colours and $\mathtt{Muller}( \mathcal{F})$ a Muller objective.
There exists a deterministic parity automaton $\mathrm{LAR}_\mathcal{F}$ over the alphabet $C$ defining $\mathtt{Muller}( \mathcal{F})$.
It has $d!$ states and has priorities in $[1,2d]$.

````

LAR stands for Latest Appearance Record.
In the literature the number of states is often $d \cdot d!$ instead of $d!$,
the multiplicative factor $d$ is saved since for automata the acceptance conditions are transition based 
instead of state based.

````{admonition} Proof
:class: dropdown tip

We define the automaton $\mathrm{LAR}_\mathcal{F}$.
The set of states is the set of lists of all colours of $C$ without repetitions.
We represent a list by $(c_1,\dots,c_d)$.
The initial state is irrelevant because $\mathtt{Muller}( \mathcal{F})$ is prefix independent.
The transition function is defined as follows: 
$\delta(\ell, c)$ is $\ell'$ obtained from $\ell$ by pushing $c$ to the first position (hence shifting to the right the elements to the left of $c$). 
This is best understood on an example:

$$
\delta( (4, 1, 2, 3), 2) = (2, 4, 1, 3).
$$

Let $j$ be the position of $c$ in $\ell$, the priority of this transition is defined by:

$$
 \mathfrak{c}((\ell,c,\ell')) =
\begin{cases}
2 j      & \text{ if } \ell([1,j]) \in  \mathcal{F}, \\
2 j - 1  & \text{ otherwise.}
\end{cases}
$$

We now show that the automaton $\mathrm{LAR}_\mathcal{F}$ defines $\mathtt{Muller}( \mathcal{F})$.
Let $\rho = c_0 c_1 \dots$ be an infinite word over the alphabet $C$. 
Let us consider the run of $\mathrm{LAR}_\mathcal{F}$ over $\rho$:

$$
(\ell_0,c_0,\ell_1) (\ell_1,c_1,\ell_2) \dots
$$

Let us write $j_i$ for the position of $c_i$ in $\ell_i$.
We consider $\mathtt{Inf}(\rho)$ the set of colours appearing infinitely many times and write $j$ for its cardinal.
From some point onwards the lists $\ell_i$ are of the form

$$
(\underbrace{c_1,\dots,c_j}_{ \mathtt{Inf}(\rho)} ,\ \underbrace{c_{j + 1},\dots,c_d}_{C \setminus  \mathtt{Inf}(\rho)}).
$$

From this point on $j_i$ is smaller than or equal to $j$, and it reaches $j$ infinitely many times.
It follows that the largest priority appearing infinitely many times in the run is $2 j$ if $\mathtt{Inf}(\rho) \in  \mathcal{F}$
and $2 j - 1$ if $\mathtt{Inf}(\rho) \notin  \mathcal{F}$.
Thus $\rho$ is accepted by $\mathrm{LAR}_\mathcal{F}$ if and only if $\mathtt{Inf}(\rho) \in  \mathcal{F}$, as desired.

````

## The Zielonka tree

{prf:ref}`2-thm:LAR` implies a reduction from Muller games to parity games as explained in Section {ref}`1-sec:reductions`.
However this does not improve over the results we already obtained for Muller games in {prf:ref}`2-thm:muller`,
neither algorithmically nor for the memory requirements.
One weakness of the LAR construction is that its size depends only on the number of colours, and not on the properties of $\mathcal{F}$.
The Zielonka tree is an improved take on the LAR.

````{prf:definition} Zielonka tree
:label: definition:zielonka_tree

Let $\mathtt{Muller}( \mathcal{F})$ be a Muller objective over the set of colours $C$.
The Zielonka tree $T_\mathcal{F}$ of $\mathtt{Muller}( \mathcal{F})$ is a rooted tree with nodes labelled by subsets of colours, 
it is constructed inductively as follows:

*  the root is labelled $C$,
*  the children of a node labelled $S$ are the maximal subsets $S_1, \dots, S_k$ of $S$ such that 
$S_i \in  \mathtt{Muller}( \mathcal{F}) \Longleftrightarrow S \notin  \mathtt{Muller}( \mathcal{F})$.

````

{numref}`2-fig:Zielonka_tree_example` represents the Zielonka tree for $\mathtt{Muller}( \mathcal{F})$ with

$$
 \mathcal{F} =  \left\{  \left\{ 2 \right\ \right\},  \left\{ 3 \right\},  \left\{ 4 \right\},  \left\{ 1,2 \right\},  \left\{ 1,3 \right\},  \left\{ 1,3,4 \right\},  \left\{ 2,3,4 \right\},  \left\{ 1,2,3,4 \right\}}.
$$

We note that there are two nodes labelled $\left\{ 1 \right\}$; in general there may be several nodes with the same label.
Also, not all branches have the same length.

```{figure} ./../FigAndAlgos/2-fig:Zielonka_tree_example.png
:name: 2-fig:Zielonka_tree_example
:align: center
The Muller tree for $\mathtt{Muller}( \mathcal{F})$. By convention nodes labelled by a set in $\mathcal{F}$ are represented by a circle
and the others by a square.
The numbers on the right hand side and the dashed nodes (describing a branch) are both used in the proof of {prf:ref}`2-thm:reduction_parity_Zielonka_tree`.
```

The first use of the Zielonka tree is to induce an improved reduction from Muller to parity objectives.
A branch in a tree is a path from the root to a leaf.

````{prf:theorem} Reduction from Muller to parity games using the Zielonka tree automaton
:label: 2-thm:reduction_parity_Zielonka_tree

Let $C = [1,d]$ be a set of colours and $\mathtt{Muller}( \mathcal{F})$ a Muller objective.
There exists a deterministic parity automaton $\mathrm{Zielonka}_\mathcal{F}$ over the alphabet $C$ defining $\mathtt{Muller}( \mathcal{F})$.
Its number of states is the number of branches of $T_\mathcal{F}$ and its parity condition uses $d$ priorities.

````

Here again we take advantage of the fact that the acceptance conditions on automata are transition based;
using stated based transitions we would have add a multiplicative factor $d$.

````{admonition} Proof
:class: dropdown tip

Without loss of generality $C \in  \mathcal{F}$ (otherwise we consider the complement $\mathtt{Muller}(2^C \setminus  \mathcal{F})$).
We number the levels of $T_\mathcal{F}$ from the leaves to the root such that nodes labelled by sets in $\mathcal{F}$ are even
and the other ones odd (this will be used for defining the parity condition).
See {numref}`2-fig:Zielonka_tree_example` for a possible numeration of the levels (on the right hand side), the other options being shifts of this numeration by an even number.

The set of states of $\mathrm{Zielonka}_\mathcal{F}$ is the set of branches of $T_\mathcal{F}$.
We represent a branch by $(S_1,\dots,S_k)$
where $S_1$ is the set labelling the root and $S_k$ the set labelling a leaf. Note that $k \le d$.
For the sake of simplicity we identify nodes with their labels, which is an abuse since two different nodes may have the same label
but will be convenient and harmless in our reasoning.

The initial state is irrelevant because $\mathtt{Muller}( \mathcal{F})$ is prefix independent.
We define the support $\mathrm{supp}(b,c)$ of a branch $b$ and a colour $c$ to be the lowest node of $b$ which contains $c$.
The transition function is defined as follows: 
$\delta(b,c)$ is the next branch (in the lexicographic order from left to right and in a cyclic way) which coincides with $b$ up to $\mathrm{supp}(b,c)$.
The priority of this transition is given by the level on which $\mathrm{supp}(b,c)$ sits.

This is best understood on an example: on {numref}`2-fig:Zielonka_tree_example`
consider the branch $b$ represented by dashed nodes, reading the colour $2$ we consider branches starting with $( \left\{ 1,2,3,4 \right\},  \left\{ 1,2,3 \right\})$
because $\mathrm{supp}(b,2) =  \left\{ 1,2,3 \right\}$.
The next branch after $b$ is $( \left\{ 1,2,3,4 \right\},  \left\{ 1,2,3 \right\}, \left\{ 1,2 \right\}, \left\{ 1 \right\})$ (because we cycle: the node after $\left\{ 1,3 \right\}$ is $\left\{ 1,2 \right\}$).
The priority of this transition is $3$ corresponding to the level where $\left\{ 1,2,3 \right\}$ sits.

We now show that the automaton $\mathrm{Zielonka}_\mathcal{F}$ defines $\mathtt{Muller}( \mathcal{F})$.
Let $\rho = c_0 c_1 \dots$ be an infinite word over the alphabet $C$.
Let us consider the run of $\mathrm{Zielonka}_\mathcal{F}$ over $\rho$:

$$
(b_0,c_0,b_1) (b_1,c_1,b_2) \dots
$$

We consider $\mathtt{Inf}(\rho)$ the set of colours appearing infinitely many times.
Let us look at the largest prefix $(S_1,\dots,S_p)$ of a branch which is eventually common to all the branches $b_i$.
We make two claims:

*  $\mathtt{Inf}(\rho)$ is included in $S_p$;
*  $\mathtt{Inf}(\rho)$ is not included in any child of $S_p$.

For the first claim, let $c \in  \mathtt{Inf}(\rho)$, since eventually the branch $b_i$ starts with $(S_1,\dots,S_p)$,
the support of $b_i$ and $c$ is lower than or equal to $S_p$, meaning that $c \in S_p$.

For the second claim, we first note that by maximality of $(S_1,\dots,S_p)$ the support of $b_i$ and $c_i$ is infinitely many times $S_p$.
Indeed from some point onwards it is lower than or equal to $S_p$, and if it would be eventually strictly lower then the corresponding child of $S_p$ would be common to all branches $b_i$ from there on.
This implies that all children of $S_p$ appear infinitely many times in the branches $b_i$: each time the support of $b_i$ and $c_i$ is $S_p$, the branch switches to the next child of $S_p$.
Now since each child $S_{p+1}$ of $S_p$ is left infinitely many times this implies that there exists $c \in  \mathtt{Inf}(\rho)$ with $c \notin S_{p+1}$.
Hence $\mathtt{Inf}(\rho)$ is not included in $S_{p+1}$.

By definition of the Zielonka tree, this implies that $\mathtt{Inf}(\rho) \in  \mathcal{F}$ if and only if $S_p \in  \mathcal{F}$,
thus $\rho$ is accepted by $\mathrm{Zielonka}_\mathcal{F}$ if and only if $\mathtt{Inf}(\rho) \in  \mathcal{F}$, as desired.

````

Since {prf:ref}`2-thm:reduction_parity_Zielonka_tree` is a reduction from Muller to parity objectives,
it implies a reduction from Muller games to parity games as explained in Section {ref}`1-sec:reductions`,
improving over {prf:ref}`2-thm:LAR`. 
Since solving parity games is in $\textrm{NP} \cap  \textrm{coNP}$,
if we represent the Muller condition by a Zielonka tree then the automaton constructed in {prf:ref}`2-thm:reduction_parity_Zielonka_tree`
is of polynomial size, implying the following result.

````{prf:theorem} Complexity of solving Muller games represented by the Zielonka tree
:label: 2-thm:complexity_Muller_games_representation_Zielonka_tree

Solving Muller games where the condition is represented by a Zielonka tree is in $\textrm{NP} \cap  \textrm{coNP}$.

````

As observed above different nodes of the Zielonka tree may be labelled by the same set of colours.
Hence it is tempting to represent a Muller condition not with its Zielonka tree but rather with the Zielonka DAG (Directed Acyclic Graph)
where nodes labelled by the same set of colours are identified.
However with this representation solving Muller games is again $\textrm{PSPACE}$-complete:

````{prf:theorem} Complexity of solving Muller games represented by the Zielonka DAG
:label: 2-thm:Muller_games_DAG

Solving Muller games where the condition is represented by a Zielonka DAG is $\textrm{PSPACE}$-complete.

````

The algorithm presented in {prf:ref}`2-thm:muller` runs in polynomial space for this representation.
To obtain the $\textrm{PSPACE}$-hardness we observe that in the reduction from QBF constructed in {prf:ref}`2-thm:complexity_Muller`,
the Muller objective is of polynomial size when represented by a Zielonka DAG (but of exponential size when represented by a Zielonka tree).

## The exact memory requirements

The second and most interesting use of the Zielonka tree is for characterising the memory requirements.

Note that a node in the Zielonka tree $T_\mathcal{F}$ represents another Muller objective, over the set of colours labelling this node.
For instance in {numref}`2-fig:Zielonka_tree_example` the node labelled $\left\{ 1,2,3 \right\}$ corresponds to $\mathtt{Muller}( \mathcal{F}')$ with
$\mathcal{F}' =  \left\{  \left\{ 2 \right\ \right\},  \left\{ 3 \right\},  \left\{ 1,2 \right\},  \left\{ 1,3 \right\}}$.

````{prf:definition} Memory requirements for Muller objectives
:label: 2-def:memory_requirements_Muller_objectives

Let $\mathtt{Muller}( \mathcal{F})$ be a Muller objective over the set of colours $C$.
We define $m_\mathcal{F}$ by induction:

*  if the tree consists of a single leaf, then $m_\mathcal{F} = 1$;
*  otherwise, let $\mathcal{F}_1,\dots, \mathcal{F}_k$ be the Muller objectives defined by the children of the root,
there are two cases:

    *  if $C \in  \mathcal{F}$, then $m_\mathcal{F}$ is the **sum** of $m_{ \mathcal{F}_1},\dots,m_{ \mathcal{F}_k}$;
    *  if $C \notin  \mathcal{F}$, then $m_\mathcal{F}$ is the **maximum** of $m_{ \mathcal{F}_1},\dots,m_{ \mathcal{F}_k}$.

````

For the Muller objective represented in {numref}`2-fig:Zielonka_tree_example`, we have $m_\mathcal{F} = 3$.
In the following result we consider **partial** colouring functions: $\mathfrak{c} : V \to C \cup  \left\{ \emptyset \right\}$,
meaning that some vertices can be left uncolored (formally, labelled $\emptyset$).

````{prf:theorem} Memory requirements for Muller games
:label: 2-thm:characterisation_Zielonka_tree

Muller objectives $\mathtt{Muller}( \mathcal{F})$ are determined with finite memory strategies of size $m_\mathcal{F}$
for games with **partial colouring functions**.
This bound is tight: there exists a game with objective $\mathtt{Muller}( \mathcal{F})$ where Eve wins using $m_\mathcal{F}$ memory states
but not with less.

````

Let us show on an example that the assumption of partial colouring functions is necessary.
Let $\mathcal{F} =  \left\{   \left\{ 1,2 \right\ \right\} }$: the objective $\mathtt{Muller}( \mathcal{F})$ requires that both $1$ and $2$ are seen infinitely many times.
The Zielonka tree $T_\mathcal{F}$ has three nodes $\left\{ 1,2 \right\},  \left\{ 1 \right\}$, and $\left\{ 2 \right\}$, and $m_\mathcal{F} = 2$.
Indeed $\mathtt{Muller}( \mathcal{F})$ is determined with finite memory strategies of size $2$:
intuitively the memory structure is used to remember which colour was last seen.
A game with a partial colouring function where two memory states is necessary is presented in {numref}`2-fig:lower_bound_zielonka`.
However, $\mathtt{Muller}( \mathcal{F})$ is positionally determined for games with total colouring functions (as we have defined them originally):
intuitively since every vertex has colour either $1$ or $2$, there is no need to remember which colour was last seen.

```{figure} ./../FigAndAlgos/2-fig:lower_bound_zielonka.png
:name: 2-fig:lower_bound_zielonka
:align: center
A game with a partial colouring function 
where Eve has a winning strategy for $\mathtt{Muller}( \mathcal{F})$ with $\mathcal{F} =  \left\{   \left\{ 1,2 \right\ \right\} }$ using two memory states
but no positional winning strategy.
```

We will not construct the lower bound, meaning the game where Eve needs $m_\mathcal{F}$ memory states to win.
However, we will now prove the upper bound.
To this end we revisit the recursive algorithm presented in {prf:ref}`2-lem:Muller_even` and {prf:ref}`2-lem:Muller_odd`.
This algorithm was removing colours one by one and rely on the recursive solutions.
We show that we can adapt the algorithm to follow instead the structure of the Zielonka tree: 
for solving a Muller game, it is enough to recursively solve the induced Muller games
corresponding to the children of the root of the Zielonka tree.
The following lemma is an improved variant of {prf:ref}`2-lem:Muller_even`.

````{prf:lemma} Fixed point characterisation of the winning regions for Muller games using the Zielonka tree
:label: 2-lem:McNaughton_Zielonka_even

Let $\mathcal{G}$ be a Muller game with objective $\mathtt{Muller}( \mathcal{F})$ such that $C \in  \mathcal{F}$.
Let $C_1, \dots, C_k$ be the maximal subsets of $C$ such that $C_i \notin  \mathcal{F}$.
We let $\mathcal{F}_1,\dots, \mathcal{F}_k$ be the corresponding induced Muller objectives,
and define $\mathcal{G}_i$ be the subgame of $\mathcal{G}$ induced by $V \setminus  \textrm{Attr}_\mathrm{Eve}(C \setminus C_i)$
with objective $\mathtt{Muller}( \mathcal{F}_i)$.

*  If for all $i \in [1,k]$, we have $W_\mathrm{Adam}(  \mathcal{G}_i) = \emptyset$, then $W_\mathrm{Eve}(  \mathcal{G}) = V$.
*  If there exists $i \in [1,k]$ such that $W_\mathrm{Adam}(  \mathcal{G}_i) \neq \emptyset$,
let $\mathcal{G}'$ be the subgame of $\mathcal{G}$ induced by $V \setminus  \textrm{Attr}_\mathrm{Adam}(  W_\mathrm{Adam}(  \mathcal{G}_i) )$,
then $W_\mathrm{Eve}(  \mathcal{G}) =  W_\mathrm{Eve}(  \mathcal{G}')$.

````

We will prove the memory requirement at the same time inductively.
Note that by duality, the case where $C \notin  \mathcal{F}$ corresponds to the memory requirement for Adam when $C \in  \mathcal{F}$:

$$
m_{2^C \setminus  \mathcal{F}} = \max_{i \in [1,k]} m_{2^{C_i} \setminus  \mathcal{F}_i}.
$$

````{admonition} Proof
:class: dropdown tip

We prove the first item.

For each $i \in [1,k]$, let $\sigma_i$ be an attractor strategy ensuring to reach $C_i$ from $\textrm{Attr}_\mathrm{Eve}(C_i)$,
and consider a winning strategy for Eve from $V \setminus  \textrm{Attr}_\mathrm{Eve}(C_i)$ in $\mathcal{G}_i$, it induces a strategy $\sigma'_i$ in $\mathcal{G}$.
We construct a strategy $\sigma$ in $\mathcal{G}$ which will simulate the strategies above in turn; to do so it uses $[1,k]$ as top-level memory states.
(We will look at more closely at the memory structure at the end of the proof.)
The strategy $\sigma$ with memory $i$ simulates $\sigma_i$ from $\textrm{Attr}_\mathrm{Eve}(C_i)$ and $\sigma'_i$ from $V \setminus  \textrm{Attr}_\mathrm{Eve}(C_i)$,
and if it ever reaches a vertex in $C_i$ it updates its memory state to $i + 1$ and $1$ if $i = k$.
Any play consistent with $\sigma$ either updates its memory state infinitely many times, 
or eventually remains in $V \setminus  \textrm{Attr}_\mathrm{Eve}(C_i)$ and is eventually consistent with $\sigma'_i$.
In the first case it sees a colour from each $C_i$ infinitely many times, so by definition of the $C_i$'s and since $C \in  \mathcal{F}$ 
the play satisfies $\mathtt{Muller}( \mathcal{F})$, 
and in the other case since $\sigma'_i$ is winning the play satisfies $\mathtt{Muller}( \mathcal{F})$.
Thus $\sigma$ is winning from $V$.

Let us now discuss how many memory states are necessary to implement the strategy $\sigma$.
By induction hypothesis, each of the strategies $\sigma'_i$ uses $m_{ \mathcal{F}_i}$ memory states.
Using a disjoint union of the memory structures we implement $\sigma$ using $\sum_{i \in [1,k]} m_{ \mathcal{F}_i}$ memory states,
corresponding to the definition of $m_\mathcal{F}$.

We now look at the second item.

Consider a winning strategy for Adam from $W_\mathrm{Adam}(  \mathcal{G}_i)$ in $\mathcal{G}_i$, it induces a strategy $\tau_i$ in $\mathcal{G}$.
Since $V \setminus  \textrm{Attr}_\mathrm{Eve}(C_i)$ is a trap for Eve, this implies that $\tau_i$ is a winning strategy in $\mathcal{G}$.
Let $\tau_a$ denote an attractor strategy from $\textrm{Attr}_\mathrm{Adam}( W_\mathrm{Adam}(  \mathcal{G}_i)) \setminus  W_\mathrm{Adam}(  \mathcal{G}_i)$.
Consider now a winning strategy in the game $\mathcal{G}'$ from $W_\mathrm{Adam}(  \mathcal{G}')$, it induces a strategy $\tau'$ in $\mathcal{G}$.
The set $V \setminus  \textrm{Attr}_\mathrm{Adam}(  W_\mathrm{Adam}(  \mathcal{G}_i) )$ may not be a trap for Eve, so we cannot conclude that $\tau'$ is a winning strategy in $\mathcal{G}$,
and it indeed may not be.
We construct a strategy $\tau$ in $\mathcal{G}$ as the (disjoint) union of the strategy $\tau_a$ on $\textrm{Attr}_\mathrm{Adam}( W_\mathrm{Adam}(  \mathcal{G}_i)) \setminus  W_\mathrm{Adam}(  \mathcal{G}_i)$,
the strategy $\tau_i$ on $W_\mathrm{Adam}(  \mathcal{G}_i)$ and the strategy $\tau'$ on $W_\mathrm{Adam}(  \mathcal{G}')$.
We argue that $\tau$ is winning from $\textrm{Attr}_\mathrm{Adam}(  W_\mathrm{Adam}(  \mathcal{G}_i) ) \cup  W_\mathrm{Adam}(  \mathcal{G}')$ in $\mathcal{G}$.
Indeed, any play consistent with this strategy in $\mathcal{G}$ either stays forever in $W_\mathrm{Adam}(  \mathcal{G}')$ hence is consistent with $\tau'$
or enters $\textrm{Attr}_\mathrm{Adam}(  W_\mathrm{Adam}(  \mathcal{G}_i) )$, so it is eventually consistent with $\tau_i$.
In both cases this implies that the play is winning.
Thus we have proved that $\textrm{Attr}_\mathrm{Adam}(  W_\mathrm{Adam}(  \mathcal{G}_c) ) \cup  W_\mathrm{Adam}(  \mathcal{G}') \subseteq  W_\mathrm{Adam}(  \mathcal{G})$.

We now show that $W_\mathrm{Eve}(  \mathcal{G}') \subseteq  W_\mathrm{Eve}(  \mathcal{G})$, which implies the converse inclusion.
Consider a winning strategy from $W_\mathrm{Eve}(  \mathcal{G}')$ in $\mathcal{G}'$, it induces a strategy $\sigma$ in $\mathcal{G}$.
Since $\mathcal{G}'$ is a trap for Adam, any play consistent with $\sigma$ stays forever in $W_\mathrm{Eve}(  \mathcal{G}')$, 
implying that $\sigma$ is winning from $W_\mathrm{Eve}(  \mathcal{G}')$ in $\mathcal{G}$.

Let us now discuss how many memory states are necessary to implement the strategy $\tau$.
By induction hypothesis, the strategy $\tau_i$ uses $m_{2^{C_i} \setminus  \mathcal{F}_i}$ memory states
and the strategy $\tau'$ uses $\max_{j \neq i} m_{2^{C_j} \setminus  \mathcal{F}_j}$ memory states.
Since $\tau$ is a disjoint union of strategies the memory can be reused so we can implement $\tau$ using $\max_{i \in [1,k]} m_{2^{C_i} \setminus  \mathcal{F}_i}$ memory states, corresponding to the definition of $m_{2^C \setminus  \mathcal{F}}$.

````

The corresponding lemma when $C \notin  \mathcal{F}$ is stated below, its proof is analogous to the previous one by swapping the two players.

````{prf:lemma} Dual fixed point characterisation of the winning regions for Muller games using the Zielonka tree
:label: 2-lem:McNaughton_Zielonka_odd

Let $\mathcal{G}$ be a Muller game such that $C \notin  \mathcal{F}$.
Let $C_1, \dots, C_k$ be the maximal subsets of $C$ such that $C_i \in  \mathcal{F}$.
We let $\mathcal{F}_1,\dots, \mathcal{F}_k$ be the corresponding induced Muller objectives,
and define $\mathcal{G}_i$ be the subgame of $\mathcal{G}$ induced by $V \setminus  \textrm{Attr}_\mathrm{Adam}(C \setminus C_i)$ with objective $\mathtt{Muller}( \mathcal{F}_i)$.

*  If for all $i \in [1,k]$, we have $W_\mathrm{Eve}(  \mathcal{G}_i) = \emptyset$, then $W_\mathrm{Adam}(  \mathcal{G}) = V$.
*  If there exists $i \in [1,k]$ such that $W_\mathrm{Eve}(  \mathcal{G}_i) \neq \emptyset$,
let $\mathcal{G}'$ be the subgame of $\mathcal{G}$ induced by $V \setminus  \textrm{Attr}_\mathrm{Eve}(  W_\mathrm{Eve}(  \mathcal{G}_i) )$,
then $W_\mathrm{Adam}(  \mathcal{G}) =  W_\mathrm{Adam}(  \mathcal{G}')$.

````

## Revisiting Streett, Rabin, and parity objectives

Let us look at the Streett, Rabin, and parity objectives under the new light shed by {prf:ref}`2-thm:characterisation_Zielonka_tree`.
It is instructive to look at the Zielonka tree of a Rabin objective, illustrated in {numref}`2-fig:Zielonka_tree_Rabin`.
It has a simple recursive structure: the Zielonka tree of the Rabin objective for $d$ pairs contains $d$ copies
of the Zielonka tree of the Rabin objective for $d-1$ pairs.
Naturally, this implies that $m_{ \mathtt{Rabin}} = 1$, so {prf:ref}`2-thm:characterisation_Zielonka_tree` induces the positional determinacy result
stated in {prf:ref}`2-thm:Rabin_positional_determinacy`.
Note that the two proofs are very different: the proof of {prf:ref}`2-thm:characterisation_Zielonka_tree` is by induction over the Zielonka tree and can be extended to infinite games, while the proof of {prf:ref}`2-thm:submixing_positional` applies only to finite games but gives a general sufficient condition for positionality.

```{figure} ./../FigAndAlgos/2-fig:Zielonka_tree_Rabin.png
:name: 2-fig:Zielonka_tree_Rabin
:align: center
The (beginning of the) Zielonka tree for $\mathtt{Rabin}$ with three pairs: 
$C =  \left\{ G_1,R_1,G_2,R_2,G_3,R_3 \right\}$.
```

Recall that we defined Streett objectives using closure under union, and Rabin objectives as the complement of Streett objectives.

````{prf:theorem} Characterisation of positionally determined Muller objectives
:label: 2-thm:characterisation_positionally_determined_Muller_objectives

Let $\mathtt{Muller}( \mathcal{F})$ be a Muller objective.

*  $\mathtt{Muller}( \mathcal{F})$ is positionally determined if and only if $\mathtt{Muller}( \mathcal{F})$ is a Rabin objective;
*  $\mathtt{Muller}( \mathcal{F})$ is positionally determined for both players if and only if $\mathtt{Muller}( \mathcal{F})$ is a parity objective.

````

This theorem gives a characterisation of Rabin and parity objectives: they form the class of Muller objectives which are respectively positional and positional for both players.

````{admonition} Proof
:class: dropdown tip

Thanks to {prf:ref}`2-thm:characterisation_Zielonka_tree` the objective $\mathtt{Muller}( \mathcal{F})$ is positionally determined if and only if $m_\mathcal{F} = 1$, which is equivalent to saying that all nodes labelled $S \in  \mathcal{F}$ in the Zielonka tree of $\mathcal{F}$ have at most one child. Indeed, for such nodes the number $m$ is obtained as the sum of the numbers for the children, so there can be at most one, and conversely if this is the case then $m_\mathcal{F} = 1$.
This characterisation of the Zielonka tree is equivalent to the complement of $\mathcal{F}$ being closed under union:

*  Assume that the complement of $\mathcal{F}$ is closed under union and let $S \in  \mathcal{F}$ be a node in the Zielonka tree of $\mathcal{F}$.
Let $S_1,\dots,S_k$ be the children of $S$, by definition they are the maximal subsets of $S$ such that $S_i \notin  \mathcal{F}$.
The union $\bigcup_i S_i$ is a subset of $S$ and by closure under union of the complement of $\mathcal{F}$ it is in the complement of $\mathcal{F}$, 
implying by maximality that it is one of the children, so they are all equal and $k = 1$.
*  Conversely, assume that all nodes labelled $S \in  \mathcal{F}$ in the Zielonka tree of $\mathcal{F}$ have at most one child.
Let $S_1,S_2 \notin  \mathcal{F}$, towards contradiction assume that $S_1 \cup S_2 \in  \mathcal{F}$.
By definition of the Zielonka tree, if $S_1 \cup S_2$ is included into a node $S \notin  \mathcal{F}$, 
then $S_1 \cup S_2$ is included into one of its children. 
Starting from the root and applying this we find a node $S \in  \mathcal{F}$ such that $S_1 \cup S_2 \subseteq S$
and $S_1 \cup S_2 \not\subseteq S'$ with $S'$ the only child of $S$ 
(the case where $S$ does not have any children is easy and treated separately).
By definition of the Zielonka tree, since $S_1,S_2 \notin  \mathcal{F}$ and $S_1,S_2 \subseteq S$, then $S_1,S_2 \subseteq S'$, implying that 
$S_1 \cup S_2 \subseteq S'$, a contradiction.

We have proved the first equivalence: $\mathtt{Muller}( \mathcal{F})$ is positionally determined if and only if the complement of $\mathcal{F}$ is closed under union, which is the definition of Rabin objectives.

For the second equivalence, we already have that $\mathtt{Muller}( \mathcal{F})$ is positionally determined for both players if and only if all nodes in the Zielonka tree of $\mathcal{F}$ have at most one child. The Zielonka tree is in this case a chain:

$$
S_1 \subseteq S_2 \subseteq S_3 \subseteq S_4 \subseteq \cdots \subseteq S_{2d-1} \subseteq S_{2d} \subseteq C,
$$

with $S_{2i} \in  \mathcal{F}$ and $S_{2i-1} \notin  \mathcal{F}$.
Then $X \in  \mathcal{F}$ is equivalent to asking that the largest $i \in [1,d]$ such that if $X \cap S_i \neq \emptyset$ is even.
Assigning priority $i$ to $S_i$ we get that $X \in  \mathtt{Muller}( \mathcal{F})$ if and only if 
the largest priority appearing infinitely many times in $X$ is even: 
this is the definition of the parity objective over the set of priorities $[1,2d]$.
Conversely, we observe that the Zielonka tree of a parity objective is indeed a chain.

````

