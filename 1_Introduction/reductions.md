(1-sec:reductions)=
# Reductions

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
Automata and memory structures can be used to construct reductions between games.
Automata operate at the level of objectives, independently of the colouring function and the arena,
while memory structures work at the level of conditions, hence depend on the graph.

## Reductions between objectives using automata

Let $\Omega$ a qualitative objective over the set of colours $C$, and $\Omega'$ a second qualitative objective.
We say that $\Omega$ reduces to $\Omega'$ if there exists a **deterministic** automaton $\Automaton$ over the alphabet $C$ with acceptance objective $\Omega'$ defining $\Omega$, **i.e.** such that $L(\Automaton) = \Omega$.
%The equality $L(\Automaton) = \Omega$ implies that $\WE(\Game) = \WE(\arena,L(\Automaton))$.

This implies that we can transform a game $\Game$ with objective $\Omega$ into an equivalent one $\Game \times \Automaton$ with objective $\Omega'$ by composing $\Game$ with $\Automaton$: 
the automaton reads the sequence of colours from $C$ induced by the play and 
produces a new sequence of colours which is accepted if its satisfies $\Omega'$.

Formally, let $\arena$ an arena and 

$$
\Automaton = (Q,q_0,\delta : Q \times C \to Q,\Omega'[\col_\Automaton])
$$

a deterministic automaton with $\col_\Automaton : Q \times C \to C'$.
We construct the arena $\arena \times \Automaton$ as follows.
We first define the graph $G \times Q$ whose set of vertices is $V \times Q$ and set of edges is defined as follows:
for every edge $e = (v,v') \in E$ and state $q \in Q$ there is an edge $e_q$ from $(v,q)$ to $(v',\delta(q,\col(v)))$:
the second component computes the run of $\Automaton$ on the sequence of colours induced by the play.
The arena is $\arena \times \Automaton = (G \times Q, \VE \times Q, \VA \times Q)$.
The colouring function is defined by $\col'((v,q)) = \col_\Automaton(q,\col(v))$.
The game is $\game \times \Automaton = (\arena \times \Automaton, \Omega'[\col'])$. 

The following lemma states two consequences to the fact that $\Omega$ reduces to $\Omega'$.

````{prf:lemma} Automata reductions
:label: 1-lem:automata_reduction

If $\Omega$ reduces to $\Omega'$ through the automaton $\Automaton$ with $S$ states, then 
Eve has a winning strategy in $\Game$ from $v_0$ if and only if she has a winning strategy in $\Game \times \Automaton$ from $(v_0,q_0)$.

Consequently, the following properties hold:

*  Assume that there exists an algorithm for solving games with objective $\Omega'$ with complexity $T(n,m)$. 
Then there exists an algorithm for solving games with objectives $\Omega$ of complexity $T(n \cdot S, m \cdot S)$.

*  If $\Omega'$ is determined with finite memory strategies of size $m$, then $\Omega$ is determined with finite memory stragies of size $m \cdot S$.

````

Since the next type of reduction extends this one and the two proofs are very similar we will prove this lemma as a corollary of the next one.

Reductions between objectives using automata are very general: 
they operate at the level of objectives and therefore completely ignore the arena.

## Reductions between conditions using memory structures

Reductions between conditions using memory structures extend the previous ones, the main difference being that 
the memory structure reads the sequences of edges and produces a sequence of memory states.
The edges contain more information than the sequence of colours (which is what the automaton reads), 
and this information is dependent on the graph.

Formally, let $\arena$ an arena and $\mem$ a memory structure.
We construct the arena $\arena \times \mem$ as follows.
We first define the graph $G \times M$ whose set of vertices is $V \times M$ and set of edges $E_M$ is defined as follows:
for every edge $e = (v,v') \in E$ and state $m \in M$ there is an edge $e_m$ from $(v,m)$ to $(v',\delta(m,e))$.
The arena is $\arena \times \mem = (G \times M, \VE \times M, \VA \times M)$.

````{prf:observation} Strategies with memory
:label: 1-fact:strategies_memory

There is a one-to-one correspondence between plays $\pi = v_0 v_1 \dots$ in $\arena$ 
and plays $\pi'$ in $\arena \times \mem$ from $(v_0,m_0)$:
the play $\pi' = (v_0, m_0) (v_1, m_1) (v_2, m_2) \ldots$
is defined by $m_{i+1} = \delta(m_i, (v_{i},v_{i+1}))$.

````

Let $W$ be a condition on $\arena$ and $W'$ a condition on $\arena \times \Mem$.
We say that $W$ reduces to $W'$ if for all plays $\play$ in $\arena$,
we have 

$$
\play \in W \Longleftrightarrow \play' \in W'.
$$

%meaning on sequences of pairs composed of a vertex and a memory state. 
Let $\Mem$ and $\Mem'$ two memory structure over the same graph, 
we let $\Mem \times \Mem'$ denote the memory structure obtained by direct product.

````{prf:lemma} Memory structure reductions
:label: 1-lem:memory_structure_reduction

If $W$ reduces to $W'$ through the memory structure $\mem$, then
Eve has a winning strategy in $\Game = (\Arena,W)$ from $v_0$ if and only if 
she has a winning strategy in $\Game \times \Mem = (\Arena \times \Mem, W')$ from $(v_0,m_0)$. 

More specifically, if Eve has a winning strategy in $\Game \times \Mem$ from $(v,m_0)$ using $\Mem'$ as memory structure, 
then she has a winning strategy in $\Game$ from $v$ using $\Mem \times \Mem'$ as memory structure.
In particular if the strategy in $\Game \times \Mem$ is memoryless, then the strategy in $\Game$ uses $\Mem$ as memory structure.

````

````{admonition} Proof
:class: dropdown tip

A winning strategy in $\Game$ directly induces a winning strategy in $\Game \times \Mem$ simply by ignoring the additional information
and thanks to the equivalence above because $W$ reduces to $W'$.
For the converse implication, let $\sigma$ be a winning strategy in $\Game \times \Mem$ using $\Mem'$ as memory structure.
Recall that $\sigma$ is defined through the function $\sigma : (\VE \times M) \times M' \to E_M$.Let $p : E_M \to E$ mapping the edge $e_m$ to $e$.
We construct a strategy $\sigma'$ in $\Game$ using $\Mem \times \Mem'$ as memory structure by

$$
\sigma'(v, (m,m')) = p(\sigma((v,m), m')).
$$

The correspondence between plays in $\arena$ and $\arena \times \mem$ maps plays consistent with $\sigma$ to plays consistent with $\sigma'$,
which together with the fact that $W$ reduces to $W'$ implies that $\sigma'$ is a winning strategy in $\Game$ from $v$.

````

To obtain  {prf:ref}`1-lem:automata_reduction` as a corollary of  {prf:ref}`1-lem:memory_structure_reduction`
we observe that a reduction between objectives using an automaton induces a reduction between the induced conditions using a memory structure.
Formally, let us assume that $\Omega$ reduces to $\Omega'$, 
and let $\Automaton = (Q, q_0, \delta, \Omega'[\col_\Automaton])$ such that $L(\Automaton) = \Omega$.
Let $\Game = (\Arena, \Omega[\col])$ a game.

We first define the memory structure $\Mem = (Q, q_0, \delta')$: the transition function is $\delta' : Q \times E \to Q$, it is defined
by $\delta'(q,(v,v')) = \delta(q, \col(v))$.
We then define $\col'(v,q) = \col_\Automaton(q, \col(v))$.

We note that $\Omega[\col]$ reduces to $\Omega'[\col']$: for all plays $\play$ in $\Arena$, we have 
$\play \in \Omega[\col]$ if and only if $\play' \in \Omega'[\col']$: this is a reformulation of the fact that $L(\Automaton) = \Omega$.

We construct the game $\Game' = (\Arena \times \Mem, \Omega'[\col'])$.
Thanks to  {prf:ref}`1-lem:memory_structure_reduction` the two games have the same winner and a strategy in the latter induce a strategy in the former
by composing with the memory structure $\Mem$, implying  {prf:ref}`1-lem:automata_reduction`.
