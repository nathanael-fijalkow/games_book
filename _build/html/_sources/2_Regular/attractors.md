(2-sec:attractors)=
# Reachability games

```{math}

\renewcommand{\Game}{\game}

```

Recall that the objective $\mathtt{Reach}$ requires that the colour $Win$ appears at least once and 
$\mathtt{Safe}$ requires the the colour $Lose$ never appears.
We identify the colour $Win$ with $\textsf{col}^{-1}( Win)$ the set of vertices labelled $Win$,
so we write $v \in  Win$ when $\textsf{col}(v) =  Win$, and similarly for $Lose$.

````{prf:theorem} Positional determinacy and complexity of reachability games
:label: 2-thm:reachability

Reachability objectives are uniformly positionally determined for both players.
There exists an algorithm for computing the winning regions of reachability games in linear time and space.
More precisely the time and space complexity are both $O(m)$.

````

The first sentence implies that safety games are also uniformly positionally determined,
and both positional determinacy results hold for infinite games.

The complexity results are stated in the unit cost RAM model with machine word size $w = \log(m)$ with $m$ the number of edges.
We refer to Section {ref}`1-sec:computation` for more details about the model, which is in subtle ways different than the Turing model.
The complexity would be slightly different in the Turing model: an additional $\log(m)$ factor would be incurred for manipulating numbers of order $m$, which the unit cost RAM model allows us to conveniently hide.

In the litterature the complexity $O(n + m)$ is often reported for solving reachability games.
Since we make the assumption that every vertex has an outgoing edge this implies that $n \le m$, so $O(n + m) = O(m)$.

Towards proving {prf:ref}`2-thm:reachability` let us introduce some notations.
Let us consider a reachability game $\Game = ( \mathcal{A},  \mathtt{Reach}[ \textsf{col}])$.
For a subset $F \subseteq V$, we let $Pre_\mathrm{Eve}(F) \subseteq V$ the set of vertices from which Eve can ensure 
that the next vertex is in $F$:

$$
\begin{array}{lll}
 Pre_\mathrm{Eve}(F) & = &  \left\{ v \in V_E : \exists (v,v') \in E,\ v' \in F \right\} \\
        & \cup &  \left\{ v \in V_A : \forall (v,v') \in E,\ v' \in F \right\}.
\end{array}
$$

Let us define the following operator on subsets of vertices:

$$
X \mapsto  Win \cup  Pre_\mathrm{Eve}(X).
$$

We note that this operator is monotonic when equipping the powerset of vertices with the inclusion preorder:
if $F \subseteq F'$ then $Pre_\mathrm{Eve}(F) \subseteq  Pre_\mathrm{Eve}(F')$.
Hence {prf:ref}`1-thm:kleene` applies: this operator has a least fixed point 
which we call the attractor of $Win$ for Eve and write $Attr_\mathrm{Eve}( Win)$,
and it is computed by the following sequence: we let $Attr_\mathrm{Eve}^0( Win) =  Win$ and

$$
 Attr_\mathrm{Eve}^{k+1}( Win) =  Attr_\mathrm{Eve}^{k}( Win)\ \cup\  Pre_\mathrm{Eve}( Attr_\mathrm{Eve}^{k}( Win)).

```{margin}
For technical convenience we shift the sequence by one, ignoring the first term which is the empty set
```

$$

This constructs a sequence $( Attr_\mathrm{Eve}^{k}( Win))_{k \in  \mathbb{N}}$ of non-decreasing subsets of $V$.
If the game is finite and $n$ is the number of vertices, 
the sequence stabilises after at most $n-1$ steps, **i.e.** $Attr_\mathrm{Eve}^{n-1}( Win) =  Attr_\mathrm{Eve}^{n}( Win) =  Attr_\mathrm{Eve}( Win)$.

Let us drop the finiteness assumption: if the game is infinite but has finite outdegree, meaning that for any vertex there is a finite number of outgoing edges, then the operator above preserves suprema so thanks to {prf:ref}`1-thm:kleene` 
we have $Attr_\mathrm{Eve}( Win) = \bigcup_{k \in  \mathbb{N}}  Attr_\mathrm{Eve}^k( Win)$.
In full generality the operator does not preserve suprema and the use of ordinals is necessary:
we define the sequence $( Attr_\mathrm{Eve}^{\alpha}( Win))$ indexed by ordinals up to the cardinal of $\Game$,
the case of a limit ordinal $\alpha$ being $Attr_\mathrm{Eve}^{\alpha}( Win) = \bigcup_{\beta < \alpha}  Attr_\mathrm{Eve}^{\beta}( Win)$.
We then show that $Attr_\mathrm{Eve}( Win)$ is the union of all elements in this sequence.

We do not elaborate further this most general case but note that the overhead is mostly technical, the proof below of {prf:ref}`2-lem:reachability` can be adapted with little changes using a transfinite induction.

The following lemma shows how the attractor yields a solution to reachability games and directly implies {prf:ref}`2-thm:reachability`.

````{prf:lemma} Characterisation of the winning region of reachability games using attractors
:label: 2-lem:reachability

Let $\mathcal{G}$ a reachability game.
Then $W_\mathrm{Eve}( \mathcal{G}) =  Attr_\mathrm{Eve}( Win)$, and:

*  there exists a uniform positional strategy $\sigma$ for Eve called the attractor strategy defined on $Attr_\mathrm{Eve}( Win) \setminus  Win$
which ensures $\mathtt{Reach}[ Win]$ from any vertex in $Attr_\mathrm{Eve}( Win)$, 
with the property that for any $k \in  \mathbb{N}$ all plays consistent with $\sigma$ from $Attr_\mathrm{Eve}^{k}( Win)$ reach $Win$ within $k$ steps 
and remain in $Attr_\mathrm{Eve}( Win)$ until doing so;
*  there exists a uniform positional strategy $\tau$ for Adam called the counter-attractor strategy defined on $V \setminus  Attr_\mathrm{Eve}( Win)$
which ensures $\mathtt{Safe}[ Win]$ from any vertex in $V \setminus  Attr_\mathrm{Eve}( Win)$,
with the property that all plays consistent with $\tau$ remain in $V \setminus  Attr_\mathrm{Eve}( Win)$.

````

````{admonition} Proof
:class: dropdown tip

We first show that $Attr_\mathrm{Eve}( Win) \subseteq  W_\mathrm{Eve}( \mathcal{G})$. 
For $v \in  Attr_\mathrm{Eve}( Win)$, the rank of $v$ is the smallest $k \in  \mathbb{N}$ such that $v \in  Attr_\mathrm{Eve}^{k}( Win)$. 
We use the rank to define a positional strategy $\sigma$ for Eve.
Let $v \in  V_\mathrm{Eve}$ of rank $k+1$, then $v \in  Pre_\mathrm{Eve}( Attr_\mathrm{Eve}^{k}( Win))$, 
so there exists $(v,v') \in E$ such that $v' \in  Attr_\mathrm{Eve}^{k}( Win)$, 
define $\sigma(v) = (v,v')$.

We argue that $\sigma$ ensures $\mathtt{Reach}[ Win]$.
By construction in any play consistent with $\sigma$ the rank is either $0$ or decreases by at least one
at each step.
Since $Win$ is the set of vertices of rank $0$, any play consistent with $\sigma$ from $Attr_\mathrm{Eve}( Win)$ reaches $Win$.

We now show that $W_\mathrm{Eve}( \mathcal{G}) \subseteq  Attr_\mathrm{Eve}( Win)$.
For this we actually show

$$
V \setminus  Attr_\mathrm{Eve}( Win) \subseteq  W_\mathrm{Adam}( \mathcal{G}).
$$

Indeed, $W_\mathrm{Adam}( \mathcal{G}) \subseteq V \setminus  W_\mathrm{Eve}( \mathcal{G})$, because Eve and Adam cannot have a winning strategy from the same vertex.
This property is clear and holds for any game, it should not be confused with determinacy.

We define a positional strategy $\tau$ for Adam from $V \setminus  Attr_\mathrm{Eve}( Win)$.
Let $v \in  V_\mathrm{Adam}$ in $V \setminus  Attr_\mathrm{Eve}( Win)$, there exists $(v,v') \in E$ such that $v' \in V \setminus  Attr_\mathrm{Eve}( Win)$, 
define $\tau(v) = (v,v')$.
Similarly, if $v \in  V_\mathrm{Eve}$ then for all $(v,v') \in E$ we have $v' \in V \setminus  Attr_\mathrm{Eve}( Win)$.
It follows that any play consistent with $\tau$ remain in $V \setminus  Attr_\mathrm{Eve}( Win)$ and in particular
never reaches $Win$,
in other words $\tau$ ensures $\mathtt{Safe}[ Win]$ from $V \setminus  Attr_\mathrm{Eve}( Win)$.

````

{numref}`2-algo:reachability` is an efficient implementation of the attractor computation.
Let us emphasise that it does not compute the sequence $( Attr_\mathrm{Eve}^k( Win))_{k \in  \mathbb{N}}$ as suggested in {prf:ref}`2-lem:reachability`.
In Section {ref}`4-sec:shortest_path` we will generalise this algorithm to a quantitative setting 
and construct an algorithm which does compute (as a special case) the sequence $( Attr_\mathrm{Eve}^k( Win))_{k \in  \mathbb{N}}$,
however with a higher complexity.

We introduce some terminology for analysing the algorithm.
The algorithm uses the set variable $A$ for the current attractor.
At any point during the execution of the algorithm we say that an edge is **winning** if it has been treated, and **undecisive** otherwise.

The data structure contains the following objects:

*  a set $A$ of vertices representing the current attractor,
*  a set $S$ of vertices (the order in which vertices are stored and retrieved from $S$ does not matter),
*  for each vertex of Adam a number of edges.

Recall that we are using the unit cost RAM model, see Section {ref}`1-sec:computation`; 
since the machine word size is $w = \log(m)$, a number of edges can be stored in one machine word.
Hence the space complexity of the data structure of $O(n)$,
which together with the size of the input yields a space complexity $O(m)$.

We note that each vertex is added to $A$ at most once since we check whether it is not already in $A$ and vertices are never removed from $A$.
When we add $v$ to $A$ we also add it to $S$, so each edge is treated at most once. 
This has two consequences: the announced $O(m)$ time complexity, and the fact that for $v \in  V_\mathrm{Adam}$,
the value of $\text{number}$-$\text{edges}(v)$ is the number of undecisive outgoing edges of $v$.

Let us write $\mathcal{G}_t$ for the game obtained from $\mathcal{G}$ by removing all winning edges\footnote{We note that in $\mathcal{G}_t$ some vertices may not have outgoing edges violating the definition of games, but in that case they belong to $A$
so this does not affect the reasoning below.}.
The invariant of the algorithm satisfied before each iteration of the repeat loop is the following:

$$
S \subseteq A \text{ and }  Attr_\mathrm{Eve}^ \mathcal{G}( Win) = A \cup  Attr_\mathrm{Eve}^{ \mathcal{G}_t}(S).
$$

The invariant is satisfied initially because $A = S =  Win$ and $\Game_t = \Game$.
To show that it is preserved by one iteration of the repeat loop, let us assume that we choose and remove $v'$ from $S$.
Let us write $\mathcal{G}_{\text{before}}$ for the game before considering $v'$, and $\mathcal{G}_{\text{after}}$ for the game after considering $v'$:
all incoming edges to $v'$ have been removed in $\mathcal{G}_{\text{after}}$.
The set $A$ is replaced by $A' = A \cup  Pre^{ \mathcal{G}_{\text{before}}}(v')$, and the set $S$ by 
$S' = (S \cup  Pre^{ \mathcal{G}_{\text{before}}}(v')) \setminus  \left\{ v' \right\}$,
so we need to show that $A' \cup  Attr_\mathrm{Eve}^{ \mathcal{G}_{\text{after}}}(S') = A \cup  Attr_\mathrm{Eve}^{ \mathcal{G}_{\text{before}}}(S)$.
Both inclusions are easily obtained using a case analysis.

The invariant implies the correctness of the algorithm: when $S$ is empty we obtain that $A =  Attr_\mathrm{Eve}( Win)$.

````{prf:remark} NEEDS TITLE AND LABEL 
We note that in the complexity analysis the cost of manipulating (and in particular decrementing) the counters for the number of edges is constant, which holds in the unit cost RAM model of computation.
The same algorithm analysed in the Turing model of computation would have an additional $O(\log(n))$ multiplicative factor in the time complexity to take this into account.

We note that in the complexity analysis the cost of manipulating (and in particular decrementing) the counters for the number of edges is constant, which holds in the unit cost RAM model of computation.
The same algorithm analysed in the Turing model of computation would have an additional $O(\log(n))$ multiplicative factor in the time complexity to take this into account.

````

```{figure} ./../FigAndAlgos/2-algo:reachability.png
:name: 2-algo:reachability
:align: center
The linear time algorithm for reachability games.
```

The notion of attractors induces a common way of constructing traps as stated in the following very useful lemma.

````{prf:lemma} Attractors induce traps
:label: 2-lem:attractors_trap

Let $\Game$ a game and $F \subseteq V$ a subset of edges.
Then $V \setminus  Attr_\mathrm{Eve}(F)$ is a trap for Eve and symmetrically $V \setminus  Attr_\mathrm{Adam}(F)$ is a trap for Adam.

````

