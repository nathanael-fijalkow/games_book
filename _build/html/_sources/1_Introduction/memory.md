(1-sec:memory)=
# Memory

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
\newcommand{\Win}{\textrm{Win}} 
\newcommand{\Lose}{\textrm{Lose}} 
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
\newcommand{\UP}{\textrm{UP}}
\newcommand{\coNP}{\textrm{coNP}}
\newcommand{\coUP}{\textrm{coUP}}
\newcommand{\PSPACE}{\textrm{PSPACE}}
\newcommand{\EXPSPACE}{\textrm{EXPSPACE}}
\newcommand{\EXP}{\textrm{EXP}}
\newcommand{\kEXP}{\textrm{kEXP}}
```
A strategy can be a very complicated object, in particular it is infinite.
Indeed, it is a function $\sigma : \Paths \to E$,
which means that in order to choose the next move the strategy considers everything played so far: 
the strategy depends upon the whole play.

An important part of the study of games is to prove that simple strategies suffice for many purposes,
and one aspect that makes strategies simple is that they use little memory.
For understanding a certain class of games a great insight is often to prove the existence of **simple** winning strategies,
as for instance positional or using finite memory.

## Positional strategies

**Positional** strategies carry no memory about the play constructed so far and in choosing an edge only look at the current vertex.
The word memoryless is sometimes used in lieu of positional.
Formally, a positional strategy for Eve is a function 

$$
\sigma : V \to E.
$$

A positional strategy induces a strategy by $\widehat{\sigma}(\pi) = \sigma(\last(\pi))$.

For reasoning about positional strategies it is useful to define the following notion.
Let $\Game$ be a game and $\sigma$ a positional strategy, we define $\Game[\sigma]$ the graph with condition $W$ induced by $\sigma$ on $\Game$.
The set of vertices is $V$ and the set of edges is

$$
E[\sigma] = \set{e = (v,v') \in E : v \in \VA \text{ or } \left( v \in \VE \text{ and } \sigma(v) = e \right)}.
$$

It is equipped with the condition $W$ inherited from $\Game$.

````{prf:observation} Game induced by a positional strategy
:label: 1-fact:game_induced_positional_strategy

Let $\Game$ be a game with condition $W$, $\sigma$ a positional strategy, and $v$ a vertex.
Then the strategy $\sigma$ is winning from $v$ if and only if all infinite paths in $\Game[\sigma]$ from $v$ satisfy $W$.

````

We say that a qualitative objective $\Omega$ is positionally determined (sometimes simply positional) if 
for every game $\game$ with objective $\Omega$ and every vertex $v$,
if Eve has a winning strategy from $v$, then she has a positional winning strategy from $v$.


As we discussed earlier, the task of solving a game does not include constructing winning strategies.
We present a general binary search technique for doing so assuming positional determinacy.

````{prf:lemma} Binary search for constructing positional strategies
:label: 1-lem:constructing_winning_strategy

Let $\Omega$ be a positionally determined qualitative objective.
If there exists an algorithm $A$ for solving games with objective $\Omega$,
then there exists an algorithm for constructing winning strategies for games in this class 
using $n \cdot \log(\frac{m}{n})$ calls to the algorithm $A$.

````


````{admonition} Proof
:class: dropdown tip

Let $\Omega$ be a positionally determined objective and $\Game$ a qualitative game with objective $\Omega$.
We first determine $\WE(\Game)$, which requires one call to a solving algorithm for each vertex.
We fix a vertex $v \in \WE(\Game)$ and determine a winning positional move from $v$.
We let $d(v)$ denote the outdegree of $v$.
We choose a subset of $\lfloor \frac{d(v)}{2} \rfloor$ outgoing edges of $v$, construct the game where we remove these edges,
and solve it using $v$ as initial vertex.
If Eve wins this game from $v$, then there is a positional winning strategy that picks one of the remaining outgoing edges of $v$,
otherwise we need to choose one of the removed edges.
This binary search algorithm requires $O(\log(d(v)))$ calls to a solving algorithm for finding a winning positional move from $v$.
Doing so for all vertices requires 

$$
O\left( \sum_{v \in V} \log d(v) \right) \le n \cdot \log \left( \frac{m}{n} \right)
$$

calls to a solving algorithm.

````

We say that $\Omega$ is positionally determined for both players if both $\Omega$ and its complement $C^\omega \setminus \Omega$ are positionally determined.
If the positional determinacy only holds for Eve we say that such objectives are half-positional. 

Parity objectives are positionally determined for both players; this will be proved in Chapter {ref}`2-chap:regular`.
We illustrate it on {numref}`1-fig:parity_game_example_positional` by annotating {numref}`1-fig:parity_game_example` with the positional winning strategies for both players.

```{figure} ./../FigAndAlgos/1-fig:parity_game_example_positional.png
:name: 1-fig:parity_game_example_positional
:align: center
The example of a parity game given in {numref}`1-fig:parity_game_example` with additional positional winning strategies for both players (corresponding to dashed edges).
```


We say that a quantitative objective $\Phi$ is positionally determined if 
for every game $\game$ with objective $\Phi$ and every vertex $v$,
there exists a positional optimal strategy from $v$.
Let us state the quantitative counterpart of {prf:ref}`1-lem:constructing_winning_strategy`.
The proof is the same.

````{prf:lemma} Binary search for constructive winning strategies, quantitative case
:label: 1-lem:constructing_winning_strategy_quantitative

Let $\Omega$ be a positionally determined quantitative objective.
If there exists an algorithm $A$ for computing the value of games with objective $\Omega$,
then there exists an algorithm for constructing optimal positional strategies for games in this class 
using $n \cdot \log(\frac{m}{n})$ calls to $A$.

````


## Uniformity

A qualitative objective $\Omega$ is uniformly positionally determined if for every game $\game$ with objective $\Omega$, 
Eve has a positional strategy which is winning from $\WE(\game)$, meaning from every vertex in $\WE(\game)$.
Similarly, a quantitative objective $\Phi$ is uniformly positionally determined if for every game with objective $\Phi$, 
Eve has a positional strategy which is optimal from every vertex.

Being uniformly positionally determined is a stronger property than being positionally determined, but in most cases an objective satisfies either both or none, as for example if the objective is prefix independent.

````{prf:lemma} From positional to uniformly positional prefix independent objectives
:label: 1-lem:from_positional_to_uniformly_positional

If an objective is positionally determined and prefix independent then it is uniformly positionally determined.

````


````{admonition} Proof
:class: dropdown tip

Let us consider a game $\game$ with qualitative objective $\Omega$ (the argument is exactly the same for quantitative objectives so we will not repeat it).
For each $v \in \WE(\game)$ let $\sigma_v$ be a positional winning strategy.
Thanks to~\cref{1-fact:winning_prefix_independent_qualitative}
the strategy $\sigma_v$ is winning from all vertices reachable by a play consistent with $\sigma_v$ starting from $v$.
Without loss of generality let us assume that $\sigma_v$ is only defined on these vertices.

We fix $\le$ a total order on the set of vertices.

```{margin}
The argument we give in this proof extends to infinite games whose set of vertices can be well ordered. A well-order is a total order such that every non-empty subset has a least element, which is exactly the property we need in this proof.
```

We let $\sigma$ be the positional strategy defined by $\sigma(u)$ is $\sigma_v(u)$ where $v$ is the least vertex (with respect to $\le$) such that $\sigma_v$ is defined on $u$. We say that $\sigma$ uses $\sigma_v$ at $u$.

We argue that $\sigma$ is winning from $\WE(\game)$. 
Consider a play consistent with $\sigma$ starting from some vertex in $\WE(\game)$ and look at the sequence of strategies it uses.
By definition this sequence is non-increasing (with respect to $\le$), hence it is stationary.
In other words the play is eventually consistent with some strategy $\sigma_v$, implying that this suffix satisfies $\Omega$.
Since $\Omega$ is prefix independent this means that the play itself satisfies $\Omega$, so $\sigma$ is indeed winning.

````


(1-finite memory)=
## Finite memory strategies
Memoryless strategies are sometimes not enough. 
A more powerful class of strategies is **finite memory** strategies.
Intuitively, a finite memory strategy uses a finite state machine called a memory structure 
to store the relevant pieces of information about the play constructed so far.

To define finite memory strategies formally, we fix a graph $G$.
A memory structure is $\mem = (M, m_0, \delta)$: the set $M$ is a set of (memory) states, 
$m_0 \in M$ is the initial state and $\delta : M \times E \to M$ is the update function.
The update function is extended to $\delta^* : E^* \to M$ by 
$\delta^*(\varepsilon) = m_0$ and $\delta^* (\rho e) = \delta(\delta^*(\rho), e)$.
The size of a memory structure is its number of states.
Note that a memory structure is a deterministic automaton over the alphabet $E$ but without specifying the acceptance condition.

We define a strategy using $\mem$ as a function 

$$
\sigma : \VE \times M \to E.
$$

It induces a strategy $\widehat{\sigma}$ via $\widehat{\sigma}(\pi) = \sigma(\last(\pi), \delta^*(\pi))$.
A common abuse of notations is to write $\sigma$ for $\widehat{\sigma}$.

We note that positional strategies correspond to strategies using the trivial memory structure consisting of only one state.


We say that a qualitative objective $\Omega$ is determined with finite memory strategies if 
for every game $\game$ and every vertex $v$,
if Eve has a winning strategy from $v$, then she has a winning strategy from $v$ using finite memory.
There are several variants of this definition covering cases where the memory is constant or bounded, and whether it holds for one or both players,
and uniformly over all vertices or not.


We give in {numref}`1-fig:memory_required` an example of a game where Eve has a winning strategy using two memory states
but no positional winning strategy. 
Let us consider the condition $\Buchi[\set{v_1}] \wedge \Buchi[\set{v_2}]$, meaning that a play is winning if both $v_1$ and $v_2$ are visited infinitely many times. A positional strategy would either always choose to go left to $v_1$ or to the right to $v_2$, hence does not satisfy the condition. 
Some memory is required to switch between the two.

Formally we let $\mem = (\set{m_1,m_2},m_1,\delta)$ defined by 

$$
\begin{array}{lll}
\delta(m_1,(v_0,v_1)) & = & m_2, \\
\delta(m_2,(v_1,v_0)) & = & m_2, \\
\delta(m_2,(v_0,v_2)) & = & m_1, \\
\delta(m_1,(v_2,v_0)) & = & m_1.
\end{array}
$$

Then we define $\sigma(v_0,m_1) = (v_0,v_1)$ and $\sigma(v_0,m_2) = (v_0,v_2)$
inducing the winning strategy $\widehat{\sigma}$ using $\Mem$.

```{figure} ./../FigAndAlgos/1-fig:memory_required.png
:name: 1-fig:memory_required
:align: center
A game where Eve has a winning strategy for $\Buchi(v_1) \wedge \Buchi(v_2)$ using two memory states
but no positional winning strategy.
```

