(2-sec:muller)=
# Rabin, Streett, and Muller games

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
\newcommand{\NP}{\textrm{NP}}
\newcommand{\coNP}{\textrm{coNP}}
\newcommand{\PSPACE}{\textrm{PSPACE}}
\newcommand{\PTIME}{\textrm{PTIME}}
```
The prefix independent objectives we studied so far are B&uuml;chi, CoB&uuml;chi, and their joint extension the parity objectives.
The definition of the latter may seem a bit arbitrary; the study of Muller objectives will show how parity objectives naturally emerge as a well-behaved class of objectives.


Let us start with a very general class of infinitary objectives, where infinitary means that the objective only considers the set of colours appearing infinitely many times.
For a sequence $\rho$, we let $\Inf(\rho)$ denote the set of colours appearing infinitely many times in $\rho$.
The Muller objective is over the set of colours $C = [1,d]$ and is parametrised by some $\F \subseteq 2^C$, **i.e.** a family of subsets of $C$.
The objective is defined as follows:

$$
\Muller(\F) = \set{ \rho \in C^\omega : \Inf(\rho) \in \F }.
$$

Muller objectives include any objective specifying the set of colours appearing infinitely often.
There are different possible representations for a Muller objective, for instance using logical formulas or circuits.
We will here consider the most natural one which simply consists in listing the elements of $\F$.
Note that $\F$ can have size up to $2^{2^d}$, and each element of $\F$ (which is a subset of $C$)
requires up to $d$ bits to be identified, so the representation of $\F$ can be very large.

We note that the complement of a Muller objective is another Muller objective: 
$C^\omega \setminus \Muller(\F) = \Muller(2^C \setminus \F)$. 
In particular if Eve has a Muller objective then Adam also has a Muller objective.


To define subclasses of Muller objectives we make assumptions on $\F \subseteq 2^C$.
We say that $\F$ is closed under union if whenever $X,Y \in \F$ then $X \cup Y \in \F$.
Let us define Streett objectives as the subclass of Muller objectives given by $\F$ closed under union.
The following purely combinatorial lemma gives a nice characterisation of these objectives.

```{prf:lemma} needs title 2-lem:characterisation_Streett
:label: 2-lem:characterisation_Streett
:nonumber:

A collection $\F \subseteq 2^C$ is closed under union if and only if there exists a set of pairs $(R_i,G_i)_{i \in [1,d]}$
with $R_i,G_i \subseteq C$ such that $X \in \F$ is equivalent to for all $i \in [1,d]$, 
if $X \cap R_i \neq \emptyset$ then $X \cap G_i \neq \emptyset$.

```

We will see in  Section {ref}`2-sec:zielonka` a natural and optimised way to construct these pairs using the Zielonka tree.
In the meantime let us give a direct proof of this result.

```{admonition} Proof
:class: dropdown tip

Let $\F$ closed under union.
We note that for any $S \notin \F$, either no subsets of $S$ are in $\F$ or there exists a maximal subset $S'$ of $S$ in $\F$:
indeed it is the union of all subsets of $S$ in $\F$.
It directly follows that for a subset $X$ we have the following equivalence:
$X \in \F$ if and only if for any $S \notin \F$, if $X \subseteq S$ then $X \subseteq S'$.
This is rewritten equivalently as: if $X \cap (C \setminus S') \neq \emptyset$ then $X \cap (C \setminus S) \neq \emptyset$.
Hence a suitable set of pairs satisfying the required property is 
$\set{(C \setminus S', C \setminus S) : S \notin \F}$.

```

Thanks to this lemma we can give a direct alternative definition of Streett objectives.
There is a parameter $d$ controlling the number of pairs.
The set of colours is $C = \set{G_1,R_1,\dots,G_d,R_d}$ and

$$
\Streett = \set{ \rho \in C^\omega : \forall i \in [1,d],\ R_i \in \Inf(\rho) \implies G_i \in \Inf(\rho) }.
$$

It is customary to call $R_i$ the $i$\textsuperscript{th} request and $G_i$ the corresponding response;
with this terminology the Streett objective requires that every request made infinitely many times must be responded to infinitely many times.

The Rabin objectives are the complement of the Streett objectives: 

$$
\Rabin = \set{ \rho \in C^\omega : \exists i \in [1,d],\ R_i \in \Inf(\rho) \wedge G_i \notin \Inf(\rho) }.
$$



## McNaughton algorithm: an exponential time algorithm for Muller games

```{prf:theorem} Muller games
:label: 2-thm:muller
:nonumber:

Muller objectives are determined with finite memory strategies of size $d!$ (See \cref{2-rmk:finite_infinit) for the case of infinite games.}.
There exists an algorithm for computing the winning regions of Muller games in exponential time,
and more specifically of complexity $O(m d (dn)^d)$, and in polynomial space, and more specifically $O(dm)$.

```

The presentation of the recursive algorithm for computing the winning regions of Muller games follows the exact same lines as for parity games:
indeed, the Muller objective extends the parity objective, and specialising the algorithm for Muller games to parity games
yields the algorithm we presented above.

The following lemma induces the recursive algorithm for computing the winning regions of Muller games.

```{prf:lemma} needs title 2-lem:Muller_even
:label: 2-lem:Muller_even
:nonumber:

Let $\Game$ be a Muller game such that $C \in \F$.
For each $c \in C$, let $\Game_c$ be the subgame of $\Game$ induced by $V \setminus \AttrE(c)$.

*  If for all $c \in C$, we have $\WA(\Game_c) = \emptyset$, then $\WE(\Game) = V$.
*  If there exists $c \in C$ such that $\WA(\Game_c) \neq \emptyset$,
let $\Game'$ be the subgame of $\Game$ induced by $V \setminus \AttrA( \WA(\Game_c) )$,
then $\WE(\Game) = \WE(\Game')$.

```


```{admonition} Proof
:class: dropdown tip

We prove the first item.

For each $c \in C$, let $\sigma_c$ be an attractor strategy ensuring to reach $c$ from $\AttrE(c)$,
and consider a winning strategy for Eve from $V \setminus \AttrE(c)$ in $\Game_c$, it induces a strategy $\sigma'_c$ in $\Game$.
We construct a strategy $\sigma$ in $\Game$ which will simulate the strategies above in turn; to do so it uses $C$ as top-level memory states.
(We note that the strategies $\sigma'_c$ may use memory as well, so $\sigma$ may actually use more memory than just $C$.)
The strategy $\sigma$ with memory $c$ simulates $\sigma_c$ from $\AttrE(c)$ and $\sigma'_c$ from $V \setminus \AttrE(c)$,
and if it ever reaches $c$ it updates its memory state to $c + 1$ and $1$ if $c = d$.
Any play consistent with $\sigma$ either updates its memory state infinitely many times, 
or eventually remains in $V \setminus \AttrE(c)$ and is eventually consistent with $\sigma'_c$.
In the first case it sees each colour infinitely many times, and since $C \in \F$ the play satisfies $\Muller(\F)$, 
and in the other case since $\sigma'_c$ is winning the play satisfies $\Muller(\F)$.
Thus $\sigma$ is winning from $V$.

We now look at the second item.

Let $\tau_a$ denote an attractor strategy from $\AttrA(\WA(\Game_c)) \setminus \WA(\Game_c)$.
Consider a winning strategy for Adam from $\WA(\Game_c)$ in $\Game_c$, it induces a strategy $\tau_c$ in $\Game$.
Since $V \setminus \AttrE(c)$ is a trap for Eve, this implies that $\tau_c$ is a winning strategy in $\Game$.
Consider now a winning strategy in the game $\Game'$ from $\WA(\Game')$, it induces a strategy $\tau'$ in $\Game$.
The set $V \setminus \AttrA( \WA(\Game_c) )$ may not be a trap for Eve, so we cannot conclude that $\tau'$ is a winning strategy in $\Game$,
and it indeed may not be.
We construct a strategy $\tau$ in $\Game$ as the (disjoint) union of the strategy $\tau_a$ on $\AttrA(\WA(\Game_c)) \setminus \WA(\Game_c)$,
the strategy $\tau_c$ on $\WA(\Game_c)$ and the strategy $\tau'$ on $\WA(\Game')$.
We argue that $\tau$ is winning from $\AttrA( \WA(\Game_c) ) \cup \WA(\Game')$ in $\Game$.
Indeed, any play consistent with this strategy in $\Game$ either stays forever in $\WA(\Game')$ hence is consistent with $\tau'$
or enters $\AttrA( \WA(\Game_c) )$, so it is eventually consistent with $\tau_c$.
In both cases this implies that the play is winning.
Thus we have proved that $\AttrA( \WA(\Game_c) ) \cup \WA(\Game') \subseteq \WA(\Game)$.

We now show that $\WE(\Game') \subseteq \WE(\Game)$, which implies the converse inclusion.
Consider a winning strategy from $\WE(\Game')$ in $\Game'$, it induces a strategy $\sigma$ in $\Game$.
Since $\Game'$ is a trap for Adam, any play consistent with $\sigma$ stays forever in $\WE(\Game')$, 
implying that $\sigma$ is winning from $\WE(\Game')$ in $\Game$.

```

To get the full algorithm we need the analogous lemma for the case where $C \notin \F$.
We do not prove it as it is the exact dual of the previous lemma, and the proof is the same swapping the two players.

```{prf:lemma} needs title 2-lem:Muller_odd
:label: 2-lem:Muller_odd
:nonumber:

Let $\Game$ be a Muller game such that $C \notin \F$.
For each $c \in C$, let $\Game_c$ be the subgame of $\Game$ induced by $V \setminus \AttrA(c)$.

*  If for all $c \in C$, we have $\WE(\Game_c) = \emptyset$, then $\WA(\Game) = V$.
*  If there exists $c \in C$ such that $\WE(\Game_c) \neq \emptyset$,
let $\Game'$ be the subgame of $\Game$ induced by $V \setminus \AttrE( \WE(\Game_c) )$,
then $\WA(\Game) = \WA(\Game')$.

```

The algorithm is presented in pseudocode in  {numref}`2-algo:mcnaughton`.
We only give the case where $C \in \F$, the other case being symmetric.
The base case is when there is only one colour $c$, in wich case Eve wins everywhere if $\F = \set{c}$
and Adam wins everywhere if $\F = \emptyset$.

We now perform a complexity analysis of the algorithm.

Let us start with time complexity and write $f(n,d)$ for the number of recursive calls performed by the algorithm on Muller games with $n$ vertices and $d$ colours.
We have $f(n,1) = f(0,d) = 0$, with the general induction:

$$
f(n,d) \le d \cdot f(n,d-1) + f(n-1,d) + d + 1.
$$

The term $d \cdot f(n,d-1)$ corresponds to the recursive call to $\Game_c$ for each $c \in C$,
the term $f(n-1,d)$ to the recursive call to $\Game'$.
We obtain $f(n,d) \le d n \cdot f(n,d-1) + (d+1)n$,
so $f(n,d) \le (d+1)n (1 + dn + (dn)^2 + \dots + (dn)^{d-2}) = O((dn)^d)$.
In each recursive call we perform $d+1$ attractor computations so the number of operations in one recursive call is $O(dm)$.
Thus the overall time complexity is $O(m d (dn)^d)$.

The proofs of  {prf:ref}`2-lem:Muller_even` and  {prf:ref}`2-lem:Muller_odd` also imply that Muller games are determined with finite memory of size $d!$.
We do not make it more precise here because an improved analysis of the memory requirements will be conducted in  Section {ref}`2-sec:zielonka`
using a variant of this algorithm.

```{figure} ./../2-algo:mcnaughton.png
:name: 2-algo:mcnaughton
:align: center
A recursive algorithm for computing the winning regions of Muller games.
```

## Positional determinacy for Rabin games

```{prf:theorem} needs title 2-thm:Rabin_positional_determinacy
:label: 2-thm:Rabin_positional_determinacy
:nonumber:

Rabin games are uniformly positionally determined.

```

 {prf:ref}`2-thm:Rabin_positional_determinacy` holds for infinite games.
However the proof we give here only applies to finite games and does not easily extend to infinite ones.
A different approach is required to obtain the positionality result for infinite games, see  {prf:ref}`2-thm:characterisation_Zielonka_tree`.

```{admonition} Proof
:class: dropdown tip

We proceed by induction over the following quantity: total outdegree of vertices controlled by Eve minus number of vertices controller by Eve.
Since we assume that every vertex has an outgoing edge, the base case is when each vertex of Eve has only one successor. 
In that case Eve has only one strategy and it is positional, so the property holds.
    
In the inductive step, we consider a Rabin game $\game$ where Eve has a winning strategy $\sigma$.
Let $v \in \VE$ with at least two successors. 
We partition the outgoing edges of $v$ in two non-empty subsets which we call $E^v_1$ and $E^v_2$.
Let us define two games $\game_1$ and $\game_2$: the game $\game_1$ is obtained from $\game$ by removing the edges from $E^v_2$, and symmetrically for $\game_2$.

We claim that Eve has a winning strategy in either $\game_1$ or $\game_2$.
Let us assume towards contradiction that this is not the case: then there exist $\tau_1$ and $\tau_2$ two strategies for Adam
which are winning in $\game_1$ and $\game_2$ respectively.
We construct a strategy $\tau$ for Adam in $\game$ as follows: it has two modes, $1$ and $2$. The initial mode is $1$, and the strategy simulates $\tau_1$ from the mode $1$ and $\tau_2$ from the mode $2$. Whenever $v$ is visited, the mode is adjusted: if the outgoing edge is in $E^v_1$ then the new mode is $1$, otherwise it is $2$.
To be more specific: when simulating $\tau_1$ we play ignoring the parts of the play using mode $2$, so removing them yields a play consistent with $\tau_1$. The same goes for $\tau_2$.

Consider a play $\play$ consistent with $\sigma$ and $\tau$. 
Since $\sigma$ is winning, the play $\play$ is winning. It can be decomposed following which mode the play is in:

$$
\begin{array}{ccccccccc}
\text{mode } 1 & \overbrace{v_0 \cdots v}^{\play_1^0} & & 
\overbrace{v \cdots v}^{\play_1^1} & & \ \cdots \\
\text{mode } 2 && \underbrace{v \cdots v}_{\play_2^0} 
& & \underbrace{v \cdots v}_{\play_2^1} & \ \cdots
\end{array}
$$

where $\play_1 = \play_1^0 \play_1^1 \cdots$ is consistent with $\tau_1$ and $\play_2 = \play_2^0 \play_2^1 \cdots$ is consistent with $\tau_2$.
Since $\tau_1$ and $\tau_2$ are winning strategies for Adam, $\play_1$ and $\play_2$ do not satisfy $\Rabin$.


There are two cases: the decomposition is either finite or infinite.
If it is finite we get a contradiction: since $\play$ is winning and $\Rabin$ is prefix independent any suffix of $\play$ is winning as well, contradicting that it is consistent with either $\tau_1$ or $\tau_2$ hence cannot be winning.

In the second case to get a contradiction we observe the following property of the Rabin objective:
let $(\rho_1^\ell)_{\ell \in \N}$ and $(\rho_2^\ell)_{\ell \in \N}$ such that:

$$
\begin{array}{lccccccccccc}
& \rho_1 & = & \rho_1^0 & & \rho_1^1 & & \cdots & \rho_1^\ell & & \cdots & \notin \Rabin \\
\text{and} & \rho_2 & = & & \rho_2^0 & & \rho_2^1 & \cdots & & \rho_2^\ell & \cdots & \notin \Rabin, \\ 
\text{then: } & \rho_1 \Join \rho_2 & = & \rho_1^0 & \rho_2^0 & \rho_1^1 & \rho_2^1 & \cdots & \rho_1^\ell & \rho_2^\ell & \cdots & \notin \Rabin.
\end{array}
$$

Indeed, since neither $\rho_1$ nor $\rho_2$ satisfy $\Rabin$, in both for all $i \in [1,d]$ if $R_i \in \Inf(\rho)$, then $G_i \in \Inf(\rho)$.
Since $\Inf(\rho_1~\Join~\rho_2) = \Inf(\rho_1) \cup \Inf(\rho_2)$, this implies that $\rho_1 \Join \rho_2$ does not satisfy $\Rabin$.

This directly yields a contradiction: neither $\play_1$ nor $\play_2$ satisfy $\Rabin$, yet their shuffle $\play$ does.

```

The proof of  {prf:ref}`2-thm:Rabin_positional_determinacy` yields a stronger result: every prefix independent submixing objective is positionally determined over finite arenas, where the submixing property is defined as follows for the objective $\Omega$:

$$
\begin{array}{lccccccccccc}
\text{if} & \rho_1 & = & \rho_1^0 & & \rho_1^1 & & \cdots & \rho_1^\ell & & \cdots & \notin \Omega \\
\text{and} & \rho_2 & = & & \rho_2^0 & & \rho_2^1 & \cdots & & \rho_2^\ell & \cdots & \notin \Omega, \\ 
\text{then: } & \rho_1 \Join \rho_2 & = & \rho_1^0 & \rho_2^0 & \rho_1^1 & \rho_2^1 & \cdots & \rho_1^\ell & \rho_2^\ell & \cdots & \notin \Omega.
\end{array}
$$



```{prf:theorem} needs title 2-thm:submixing_positional
:label: 2-thm:submixing_positional
:nonumber:

Every prefix independent submixing objective is uniformly positionally determined over finite arenas.

```


## The complexity of solving Rabin games

```{prf:theorem} needs title 2-thm:Rabin_complexity
:label: 2-thm:Rabin_complexity
:nonumber:

Solving Rabin games is $\NP$-complete.

```

In order to simplify the reduction for proving {prf:ref}`2-thm:Rabin_complexity` let us make some remarks about colouring functions.
We defined colouring functions as $\col : V \to C$, meaning that we label vertices.
Let us discuss here three more general definitions and how to reduce them to the vertex colouring functions
in the case of Rabin games.

*  Partial colouring functions: $\col : V \to C \cup \set{\emptyset}$.

We introduce a new Rabin pair $(R,G)$ and colour all uncoloured vertices by $G$.
The Rabin condition will never be satisfied because of this new addition 
since the colour $R$ does not appear at all in the game.

*  Edge colouring functions: $\col : E \to C$.

We reduce from an edge colouring function to a partial vertex colouring function as illustrated in {numref}`2-fig:reduction_edge_colouring`:
we add a dummy vertex for each edge and colour it with the colour of its edge, leaving already existing vertices without colours. 

```{figure} ./../2-fig:reduction_edge_colouring.png
:name: 2-fig:reduction_edge_colouring
:align: center
Reduction from edge colouring to partial vertex colouring.
```

*  Multiset colouring functions: $\col : V \to 2^C$.

We reduce from a multiset colouring function to a vertex colouring function as illustrated in {numref}`2-fig:reduction_multiset_colouring`: 
for each vertex $v$ coloured by a set $S$ we add a dummy vertex for each colour $c \in S$ and replace $v$ by the line of dummy vertices.

```{figure} ./../2-fig:reduction_multiset_colouring.png
:name: 2-fig:reduction_multiset_colouring
:align: center
Reduction from multiset edge colouring to vertex colouring, here for two colours.
```

The three reductions described above yield equivalent Rabin games which are at most polynomially larger.
We note that they are not general reductions in the sense that they use properties of the Rabin objecttives.
In the reduction below we use these more general definitions to simplify the presentation.

```{admonition} Proof
:class: dropdown tip

The proof that solving Rabin games is in $\NP$ follows the same lines as for solving parity games: the algorithm guesses a positional strategy and checks whether it is indeed winning. This requires proving that solving Rabin games where Adam control all vertices can be done in polynomial time, which is indeed true and easy to see so we will not elaborate further on this.

To prove the $\NP$-hardness we reduce the satisfiability problem for boolean formulas in conjunctive normal form ($\SAT$) to solving Rabin games. 

Let $\Phi$ be a formula in conjunctive normal form with $n$ variables $x_1 \ldots x_n$ and $m$ clauses $C_1 \dots C_m$, where each $C_j$ is of the form $\ell_{j_1} \vee \ell_{j_2} \vee \ell_{j_3}$:

$$
\Phi = \bigwedge_{j=1}^m \ell_{j_1} \vee \ell_{j_2} \vee \ell_{j_3}.
$$

A literal $\ell$ is either a variable $x$ or its negation $\bar{x}$, and we write $\bar{\ell}$ for the negation of a literal.
The question whether $\Phi$ is satisfiable reads: does there exist a valuation $\mathbf{v} : \set{x_1,\dots,x_n} \to \set{0,1}$
satisfying $\Phi$.

We construct a Rabin game $\game$ with $m+1$ vertices (one per clause, all controlled by Eve, plus a unique vertex controlled by Adam), 
$4m$ edges ($4$ per clause), and $2n$ Rabin pairs (one per literal).
We will show that the formula $\Phi$ is satisfiable if and only if Eve has a winning strategy in the Rabin game $\game$.

We first describe the Rabin condition. 
There is a Rabin pair $(R_\ell,G_\ell)$ for each literal $\ell$, so the Rabin condition requires that there exists a literal $\ell$ such that $R_\ell$ is visited infinitely many times and $G_\ell$ is not.
Let us now describe the arena. 
A play consists in an infinite sequence of rounds, where in each round first Adam chooses a clause and second Eve chooses a literal in this clause. 
When Eve chooses a literal $\ell$ she visits $R_\ell$ and $G_{\bar{\ell}}$.
This completes the description of the Rabin game $\game$, it is illustrated in  {numref}`2-fig:hardness_Rabin`.
Let us now prove that this yields a reduction from $\SAT$ to solving Rabin games.


Let us first assume that $\Phi$ is satisfiable, and let $\mathbf{v}$ be a satisfying assignment: there is a literal $\ell$ in each clause satisfied by $\mathbf{v}$. 
Let $\sigma$ be the memoryless strategy choosing such a literal in each clause. 
We argue that in any play consistent with $\sigma$ there is at least one litteral $\ell$ that Eve chooses infinitely many times without ever choosing $\bar{\ell}$: this implies that $R_\ell$ is visited infinitely often and $G_\ell$ is not.
Indeed, some clause is chosen infinitely many times, so the corresponding literal chosen by Eve is also chosen infinitely many times.
Since all the literals chosen by Eve satisfy the same assignment $\mathbf{v}$ she does not choose both a literal and its negation, so she never chooses $\bar{\ell}$. 
It follows that $\sigma$ is a winning strategy for Eve.

Conversely, let us assume that Eve has a winning strategy.
Thanks to  {prf:ref}`2-thm:Rabin_positional_determinacy` she has a positional winning strategy $\sigma$. 
We argue that $\sigma$ cannot choose some literal $\ell$ in some clause $C$ and the literal $\bar{\ell}$ in another clause $C'$.
If this would be the case, consider the strategy of Adam alternating between the two clauses $C$ and $C'$ and play it against $\sigma$:
both $\ell$ and $\bar{\ell}$ are chosen infinitely many times, and no other literals.
Hence $R_\ell, G_\ell, R_{\bar{\ell}}$, and $G_{\bar{\ell}}$ are all visited infinitely many times, 
implying that this play does not satisfy $\Rabin$, contradicting that $\sigma$ is winning.

There exists a valuation $\mathbf{v}$ which satisfies each literal chosen by Eve, implying that it satisfies $\Phi$ which is then satisfiable.

```


```{figure} ./../2-fig:hardness_Rabin.png
:name: 2-fig:hardness_Rabin
:align: center
The Rabin game for $\Phi = (x \vee y \vee z) \bigwedge (x \vee \bar{y
```

## The complexity of solving Muller games
    

```{prf:theorem} needs title 2-thm:complexity_Muller
:label: 2-thm:complexity_Muller
:nonumber:

Solving Muller games is $\PSPACE$-complete.

```

As for the previous reduction, in the Muller game constructed in the reduction below we label edges rather than vertices,
and some edges have more than one colour.
As for Rabin games this can be reduced to the original definition of colouring functions (labelling vertices with exactly one colour each) with a polynomial increase in size.

```{admonition} Proof
:class: dropdown tip

The $\PSPACE$ algorithm was constructed in  {prf:ref}`2-thm:muller`.

To prove the $\PSPACE$-hardness we reduce the evaluation of quantified boolean formulas in disjunctive normal form ($\QBF$) to solving Muller games. 

Let $\Psi$ be a quantified boolean formula in disjunctive normal form with $n$ variables $x_1 \ldots x_n$ and $m$ clauses $C_1 \dots C_m$, where each $C_j$ is of the form $\ell_{j_1} \wedge \ell_{j_2} \wedge \ell_{j_3}$:

$$
\Psi = \exists x_1,\forall x_2,\ldots,\exists x_n,\ \Phi(x_1,\dots,x_n) \text{ and } 
\Phi(x_1,\dots,x_n) = \bigvee_{j=1}^m \ell_{j_1} \wedge \ell_{j_2} \wedge \ell_{j_3}.
$$


We construct a Muller game $\Game$ with $m+1$ vertices (one per clause, all controlled by Adam, plus a unique vertex controlled by Eve), $4m$ edges ($4$ per clause), and $2n$ colours (one per literal).
We will show that the formula $\Psi$ evaluates to true if and only if Eve has a winning strategy in the Muller game $\Game$.

We first describe the Muller condition. 
The set of colours is the set of literals.
We let $x$ denote the lowest quantified variable such that $x$ or $\bar{x}$ is visited infinitely many times. 
The Muller condition requires that:

*  either $x$ is existential and only one of $x$ and $\bar{x}$ is visited infinitely many times,
*  or $x$ is universal and both $x$ and $\bar{x}$ are visited infinitely many times,

and for all variables $y$ quantified after $x$, both $y$ and $\bar{y}$ are visited infinitely many times.
Formally, let $S_{> i} = \set{x_q, \bar{x_q} : q > p}$ and:

$$
\F = \set{ S_{> p},\ \set{x_p} \cup S_{> p},\ \set{\bar{x_p}} \cup S_{> p} : x_p \text{ existential}} \cup \set{ S_{\ge p} : x_p \text{ universal}}.
$$

Note that $\F$ contains $O(n)$ elements.

Let us now describe the arena. A play consists in an infinite sequence of rounds, where in each round first Eve chooses
a clause and second Adam chooses a literal $\ell$ in this clause corresponding to some variable $x_p$, 
and visits the colour $\ell$ as well as each colour in $S_{> p}$.

The reduction is illustrated in {numref}`2-fig:hardness_Muller`.
Note that the edges from the vertex controlled by Eve to the other ones do not have a colour,
which does not fit our definitions.
For this reason we introduce a new colour $c$ and colour all these edges by $c$.
We define a new Muller objective by adding $c$ to each set in $\F$: 
since every play in the game visit $c$ infinitely many times, the two games are equivalent.
We note that this construction works for this particular game but not in general.


For a valuation $\mathbf{v} : \set{x_1,\dots,x_n} \to \set{0,1}$ and $p \in [1,n]$,
we write $\Psi_{\mathbf{v},p}$ for the formula obtained from $\Psi$ by fixing the variables $x_1,\dots,x_{p-1}$
to $\mathbf{v}(x_1),\dots,\mathbf{v}(x_{p-1})$ and quantifying only over the remaining variables.
Let us say that a valuation $\mathbf{v}$ is **positive** if for every $p \in [1,n]$, the formula $\Psi_{\mathbf{v},p}$ evaluates to true,
and similarly a valuation is **negative** if for every $p \in [1,n]$, the formula $\Psi_{\mathbf{v},p}$ evaluates to false.


Let us first assume that $\Psi$ evaluates to true. 
We construct a winning strategy $\sigma$ for Eve.
It uses **positive** valuations over the variables $x_1,\ldots,x_n$ as memory states. 
Note that the fact that $\Psi$ evaluates to true implies that there exists a positive valuation. 
Let us choose an arbitrary positive valuation as initial valuation.
We first explain what the strategy $\sigma$ does and then how to update its memory.

Assume that the current valuation is $\mathbf{v}$, since it is positive there exists a clause satisfying $\mathbf{v}$, the strategy $\sigma$ chooses such a clause. 
Therefore, any literal that Adam chooses is necessarily true under $\mathbf{v}$.

The memory is updated as follows: 
assume that the current valuation is $\mathbf{v}$ and that Adam chose a literal corresponding to the variable $x_p$. 
If $x_p$ is existential the valuation is unchanged.
If $x_p$ is universal, we construct a new positive valuation as follows. 
We swap the value of $x_p$ in $\mathbf{v}$ and write $\mathbf{v}[x_p]$ for this new valuation. 
Since $\mathbf{v}$ is positive and $x_p$ is universally quantified, the formula $\Psi_{\mathbf{v}[x_p],p+1}$ evaluates to true,
so there exists a positive valuation $\mathbf{v}_{p+1} : \set{x_{p+1},\dots,x_n} \to \set{0,1}$ for this formula.
The new valuation is defined as follows:

$$
\mathbf{v}'(x_q) = 
\begin{cases}
\mathbf{v}(x_q) & \text{ if } q < p, \\[.5em]
\overline{\mathbf{v}(x_q)} & \text{ if } q = p, \\
\mathbf{v}_{p+1}(x_q) & \text{ if } q > p,
\end{cases}
$$

it is positive by construction.

Let $\play$ be a play consistent with $\sigma$ and $x_p$ be the lowest quantified variable chosen infinitely many times by Adam. 
First, all colours in $S_{> p}$ are visited infinitely many times (when visiting $x$ or $\bar{x}$).
Let us look at the sequence $(\mathbf{v}_i(x_p))_{i \in \N}$ where $\mathbf{v}_i$ is the valuation in the $i$\textsuperscript{th} round.
If $x_p$ is existential, the sequence is ultimately constant as it can only change when a lower quantified variable is visited.
If $x_p$ is universal, the value changes each time the variable $x_p$ is chosen.
Since any literal that Adam chooses is necessarily true under the current valuation, 
this implies that in both cases $\play$ satisfies $\Muller(\F)$.


For the converse implication we show that if $\Psi$ evaluates to false, then there exists a winning strategy $\tau$ for Adam.
The construction is similar but using **negative** valuations.
The memory states are negative valuations. The initial valuation is any negative valuation.
If the current valuation is $\mathbf{v}$ and Eve chose the clause $C$, since the valuation is negative $\mathbf{v}$ does not satisfy $C$,
the strategy $\tau$ chooses a literal in $C$ witnessing this failure. 
The memory is updated as follows: assume that the current valuation is $\mathbf{v}$ and that the strategy $\tau$ chose a literal corresponding to the variable $x_p$. 
If $x_p$ is universal the valuation is unchanged.
If $x_p$ is existential, we proceed as above to construct another negative valuation where the value of $x_p$ is swapped.

Let $\play$ be a play consistent with $\tau$ and $x$ be the lowest quantified variable chosen infinitely many times by Adam. 
As before, we look at the sequence $(\mathbf{v}_i(x))_{i \in \N}$ where $\mathbf{v}_i$ is the valuation in the $i$\textsuperscript{th} round.
If $x$ is existential, the value changes each time the variable $x$ is chosen.
If $x$ is universal, the sequence is ultimately constant.
Since any literal that Adam chooses is necessarily false under the current valuation, 
this implies that in both cases $\play$ does not satisfy $\Muller(\F)$.

```


```{figure} ./../2-fig:hardness_Muller.png
:name: 2-fig:hardness_Muller
:align: center
The Muller game for $\Psi = \exists x, \forall y, \exists z, (x \wedge y \wedge z) \bigvee (x \wedge \bar{y
```
