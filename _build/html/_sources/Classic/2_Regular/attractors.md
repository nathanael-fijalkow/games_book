(2-sec:attractors)=
# A linear time algorithm for reachability games

Recall that the objective $\Reach$ requires that the colour $\Win$ appears at least once and 
$\Safe$ requires the the colour $\Lose$ never appears.
We identify the colour $\Win$ with $\col^{-1}(\Win)$ the set of vertices labelled $\Win$,
so we write $v \in \Win$ when $\col(v) = \Win$, and similarly for $\Lose$.

```{admonition} Theorem
:class: theorem
:name: 2-thm:reachability

Reachability objectives are uniformly positionally determined for both players.
There exists an algorithm for computing the winning regions of reachability games in linear time and space.
More precisely the time and space complexity are both $O(m)$.

```

The first sentence implies that safety games are also uniformly positionally determined,
and both positional determinacy results hold for infinite games.

The complexity results are stated in the unit cost RAM model with machine word size $w = \log(m)$ with $m$ the number of edges.
We refer to  {ref}`Section <1-sec:computation>` for more details about the model, which is in subtle ways different than the Turing model.
The complexity would be slightly different in the Turing model: an additional $\log(m)$ factor would be incurred for manipulating numbers of order $m$, which the unit cost RAM model allows us to conveniently hide.

In the litterature the complexity $O(n + m)$ is often reported for solving reachability games.
Since we make the assumption that every vertex has an outgoing edge this implies that $n \le m$, so $O(n + m) = O(m)$.


Towards proving  {ref}`Theorem <2-thm:reachability>` let us introduce some notations.
Let us consider a reachability game $\Game = (\arena, \Reach[\col])$.
For a subset $F \subseteq V$, we let $\PreE(F) \subseteq V$ the set of vertices from which Eve can ensure 
that the next vertex is in $F$:

$$
\begin{array}{lll}
\PreE(F) & = & \set{v \in V_E : \exists (v,v') \in E,\ v' \in F} \\
        & \cup & \set{v \in V_A : \forall (v,v') \in E,\ v' \in F}.
\end{array}
$$

Let us define the following operator on subsets of vertices:

$$
X \mapsto \Win \cup \PreE(X).
$$

We note that this operator is monotonic when equipping the powerset of vertices with the inclusion preorder:
if $F \subseteq F'$ then $\PreE(F) \subseteq \PreE(F')$.
Hence  {ref}`Theorem <1-thm:kleene>` applies: this operator has a least fixed point 
which we call the attractor of $\Win$ for Eve and write $\AttrE(\Win)$,
and it is computed by the following sequence\footnote{For technical convenience we shift the sequence by one, ignoring the first term which is the empty set}:
we let $\AttrE^0(\Win) = \Win$ and 

$$
\AttrE^{k+1}(\Win) = \AttrE^{k}(\Win)\ \cup\ \PreE(\AttrE^{k}(\Win)).
$$

This constructs a sequence $(\AttrE^{k}(\Win))_{k \in \N}$ of non-decreasing subsets of $V$.
If the game is finite and $n$ is the number of vertices, 
the sequence stabilises after at most $n-1$ steps, **i.e.** $\AttrE^{n-1}(\Win) = \AttrE^{n}(\Win) = \AttrE(\Win)$.

Let us drop the finiteness assumption: if the game is infinite but has finite outdegree, meaning that for any vertex there is a finite number of outgoing edges, then the operator above preserves suprema so thanks to  {ref}`Theorem <1-thm:kleene>` 
we have $\AttrE(\Win) = \bigcup_{k \in \N} \AttrE^k(\Win)$.
In full generality the operator does not preserve suprema and the use of ordinals is necessary:
we define the sequence $(\AttrE^{\alpha}(\Win))$ indexed by ordinals up to the cardinal of $\Game$,
the case of a limit ordinal $\alpha$ being $\AttrE^{\alpha}(\Win) = \bigcup_{\beta < \alpha} \AttrE^{\beta}(\Win)$.
We then show that $\AttrE(\Win)$ is the union of all elements in this sequence.

We do not elaborate further this most general case but note that the overhead is mostly technical, the proof below of  {ref}`Lemma <2-lem:reachability>` can be adapted with little changes using a transfinite induction.

The following lemma shows how the attractor yields a solution to reachability games and directly implies  {ref}`Theorem <2-thm:reachability>`.

```{admonition} Lemma
:class: lemma
:name: 2-lem:reachability

Let $\game$ a reachability game.
Then $\WE(\game) = \AttrE(\Win)$, and:

*  there exists a uniform positional strategy $\sigma$ for Eve called the attractor strategy defined on $\AttrE(\Win) \setminus \Win$
which ensures $\Reach[\Win]$ from any vertex in $\AttrE(\Win)$, 
with the property that for any $k \in \N$ all plays consistent with $\sigma$ from $\AttrE^{k}(\Win)$ reach $\Win$ within $k$ steps 
and remain in $\AttrE(\Win)$ until doing so;
*  there exists a uniform positional strategy $\tau$ for Adam called the counter-attractor strategy defined on $V \setminus \AttrE(\Win)$
which ensures $\Safe[\Win]$ from any vertex in $V \setminus \AttrE(\Win)$,
with the property that all plays consistent with $\tau$ remain in $V \setminus \AttrE(\Win)$.

```



```{admonition} Proof
:class: dropdown tip

We first show that $\AttrE(\Win) \subseteq \WE(\game)$. 
For $v \in \AttrE(\Win)$, the rank of $v$ is the smallest $k \in \N$ such that $v \in \AttrE^{k}(\Win)$. 
We use the rank to define a positional strategy $\sigma$ for Eve.
Let $v \in \VE$ of rank $k+1$, then $v \in \PreE(\AttrE^{k}(\Win))$, 
so there exists $(v,v') \in E$ such that $v' \in \AttrE^{k}(\Win)$, 
define $\sigma(v) = (v,v')$.

We argue that $\sigma$ ensures $\Reach[\Win]$.
By construction in any play consistent with $\sigma$ the rank is either $0$ or decreases by at least one
at each step.
Since $\Win$ is the set of vertices of rank $0$, any play consistent with $\sigma$ from $\AttrE(\Win)$ reaches $\Win$.


We now show that $\WE(\game) \subseteq \AttrE(\Win)$.
For this we actually show 

$$
V \setminus \AttrE(\Win) \subseteq \WA(\game).
$$

Indeed, $\WA(\game) \subseteq V \setminus \WE(\game)$, because Eve and Adam cannot have a winning strategy from the same vertex.
This property is clear and holds for any game, it should not be confused with determinacy.

We define a positional strategy $\tau$ for Adam from $V \setminus \AttrE(\Win)$.
Let $v \in \VA$ in $V \setminus \AttrE(\Win)$, there exists $(v,v') \in E$ such that $v' \in V \setminus \AttrE(\Win)$, 
define $\tau(v) = (v,v')$.
Similarly, if $v \in \VE$ then for all $(v,v') \in E$ we have $v' \in V \setminus \AttrE(\Win)$.
It follows that any play consistent with $\tau$ remain in $V \setminus \AttrE(\Win)$ and in particular
never reaches $\Win$,
in other words $\tau$ ensures $\Safe[\Win]$ from $V \setminus \AttrE(\Win)$.

```

{ref}`Algorithm <2-algo:reachability>` is an efficient implementation of the attractor computation.
Let us emphasise that it does not compute the sequence $(\AttrE^k(\Win))_{k \in \N}$ as suggested in  {ref}`Lemma <2-lem:reachability>`.
In  {ref}`Section <4-sec:shortest_path>` we will generalise this algorithm to a quantitative setting 
and construct an algorithm which does compute (as a special case) the sequence $(\AttrE^k(\Win))_{k \in \N}$,
however with a higher complexity.

We introduce some terminology for analysing the algorithm.
The algorithm uses the set variable $A$ for the current attractor.
At any point during the execution of the algorithm we say that an edge is **winning** if it has been treated, and **undecisive** otherwise.

The data structure contains the following objects:

*  a set $A$ of vertices representing the current attractor,
*  a set $S$ of vertices (the order in which vertices are stored and retrieved from $S$ does not matter),
*  for each vertex of Adam a number of edges.

Recall that we are using the unit cost RAM model, see  {ref}`Section <1-sec:computation>`; 
since the machine word size is $w = \log(m)$, a number of edges can be stored in one machine word.
Hence the space complexity of the data structure of $O(n)$,
which together with the size of the input yields a space complexity $O(m)$.

We note that each vertex is added to $A$ at most once since we check whether it is not already in $A$ and vertices are never removed from $A$.
When we add $v$ to $A$ we also add it to $S$, so each edge is treated at most once. 
This has two consequences: the announced $O(m)$ time complexity, and the fact that for $v \in \VA$,
the value of $\text{number}$-$\text{edges}(v)$ is the number of undecisive outgoing edges of $v$.

Let us write $\game_t$ for the game obtained from $\game$ by removing all winning edges\footnote{We note that in $\game_t$ some vertices may not have outgoing edges violating the definition of games, but in that case they belong to $A$
so this does not affect the reasoning below.}.
The invariant of the algorithm satisfied before each iteration of the repeat loop is the following:

$$
S \subseteq A \text{ and } \AttrE^\game(\Win) = A \cup \AttrE^{\game_t}(S).
$$

The invariant is satisfied initially because $A = S = \Win$ and $\Game_t = \Game$.
To show that it is preserved by one iteration of the repeat loop, let us assume that we choose and remove $v'$ from $S$.
Let us write $\game_{\text{before}}$ for the game before considering $v'$, and $\game_{\text{after}}$ for the game after considering $v'$:
all incoming edges to $v'$ have been removed in $\game_{\text{after}}$.
The set $A$ is replaced by $A' = A \cup \Pre^{\game_{\text{before}}}(v')$, and the set $S$ by 
$S' = (S \cup \Pre^{\game_{\text{before}}}(v')) \setminus \set{v'}$,
so we need to show that $A' \cup \AttrE^{\game_{\text{after}}}(S') = A \cup \AttrE^{\game_{\text{before}}}(S)$.
Both inclusions are easily obtained using a case analysis.

The invariant implies the correctness of the algorithm: when $S$ is empty we obtain that $A = \AttrE(\Win)$.

```{admonition} Remark
:class: remark

We note that in the complexity analysis the cost of manipulating (and in particular decrementing) the counters for the number of edges is constant, which holds in the unit cost RAM model of computation.
The same algorithm analysed in the Turing model of computation would have an additional $O(\log(n))$ multiplicative factor in the time complexity to take this into account.

```

\begin{algorithm}
 \KwData{A reachability game.}
 \SetKwFunction{FTreat}{Treat}
 \SetKwFunction{FAttr}{Attractor}
 \SetKwProg{Fn}{Function}{:}{}
 \DontPrintSemicolon
 
\Fn{\FAttr{}}{
$A \leftarrow \Win$

$S \leftarrow \Win$ 

\For{$v \in \VA$}{
        $\text{number}$-$\text{edges}(v) \leftarrow $ number of outgoing edges of $v$
}    


\Repeat{$S$ empty}{
Choose some $v'$ in $S$ and remove it from $S$

        \For{$e$ incoming edge to $v'$}{
\FTreat($e$)    
        }
}

\Return{$A$}
}


\Fn{\FTreat{$e$}}{
$v \leftarrow \Ing(e)$

\If{$v \in \VA$ and $v \notin A$}{
$\text{number}$-$\text{edges}(v) \leftarrow \text{number}$-$\text{edges}(v) - 1$

\If{$\text{number}$-$\text{edges}(v) = 0$}{
Add $v$ to $A$

Add $v$ to $S$
}
}

\If{$v \in \VE$ and $v \notin A$}{
Add $v$ to $A$

Add $v$ to $S$
}
}
\caption{The linear time algorithm for reachability games.}
\label{2-algo:reachability}
\end{algorithm}


The notion of attractors induces a common way of constructing traps as stated in the following very useful lemma.

```{admonition} Lemma
:class: lemma
:name: 2-lem:attractors_trap

Let $\Game$ a game and $F \subseteq V$ a subset of edges.
Then $V \setminus \AttrE(F)$ is a trap for Eve and symmetrically $V \setminus \AttrA(F)$ is a trap for Adam.

```

