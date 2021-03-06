(1-sec:reductions)=
# Reductions

Automata and memory structures can be used to construct reductions between games.
Automata operate at the level of objectives, independently of the colouring function and the arena,
while memory structures work at the level of conditions, hence depend on the graph.

## Reductions between objectives using automata

Let $\Omega$ a qualitative objective over the set of colours $C$, and $\Omega'$ a second qualitative objective.
We say that $\Omega$ reduces to $\Omega'$ if there exists a **deterministic** automaton $\mathbf{A}$ over the alphabet $C$ with acceptance objective $\Omega'$ defining $\Omega$, **i.e.** such that $L( \mathbf{A}) = \Omega$.

This implies that we can transform a game $\mathcal{G}$ with objective $\Omega$ into an equivalent one $\mathcal{G} \times  \mathbf{A}$ with objective $\Omega'$ by composing $\mathcal{G}$ with $\mathbf{A}$: 
the automaton reads the sequence of colours from $C$ induced by the play and 
produces a new sequence of colours which is accepted if its satisfies $\Omega'$.

Formally, let $\mathcal{A}$ an arena and

$$
 \mathbf{A} = (Q,q_0,\delta : Q \times C \to Q,\Omega'[ \mathfrak{c}_\mathbf{A}])
$$

a deterministic automaton with $\mathfrak{c}_\mathbf{A} : Q \times C \to C'$.
We construct the arena $\mathcal{A} \times  \mathbf{A}$ as follows.
We first define the graph $G \times Q$ whose set of vertices is $V \times Q$ and set of edges is defined as follows:
for every edge $e = (v,v') \in E$ and state $q \in Q$ there is an edge $e_q$ from $(v,q)$ to $(v',\delta(q, \mathfrak{c}(v)))$:
the second component computes the run of $\mathbf{A}$ on the sequence of colours induced by the play.
The arena is $\mathcal{A} \times  \mathbf{A} = (G \times Q,  V_\mathrm{Eve} \times Q,  V_\mathrm{Adam} \times Q)$.
The colouring function is defined by $\mathfrak{c}'((v,q)) =  \mathfrak{c}_\mathbf{A}(q, \mathfrak{c}(v))$.
The game is $\mathcal{G} \times  \mathbf{A} = ( \mathcal{A} \times  \mathbf{A}, \Omega'[ \mathfrak{c}'])$. 

The following lemma states two consequences to the fact that $\Omega$ reduces to $\Omega'$.

````{prf:lemma} Automata reductions
:label: 1-lem:automata_reduction

If $\Omega$ reduces to $\Omega'$ through the automaton $\mathbf{A}$ with $S$ states, then 
Eve has a winning strategy in $\mathcal{G}$ from $v_0$ if and only if she has a winning strategy in $\mathcal{G} \times  \mathbf{A}$ from $(v_0,q_0)$.

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

Formally, let $\mathcal{A}$ an arena and $\mathcal{M}$ a memory structure.
We construct the arena $\mathcal{A} \times  \mathcal{M}$ as follows.
We first define the graph $G \times M$ whose set of vertices is $V \times M$ and set of edges $E_M$ is defined as follows:
for every edge $e = (v,v') \in E$ and state $m \in M$ there is an edge $e_m$ from $(v,m)$ to $(v',\delta(m,e))$.
The arena is $\mathcal{A} \times  \mathcal{M} = (G \times M,  V_\mathrm{Eve} \times M,  V_\mathrm{Adam} \times M)$.

````{prf:observation} Strategies with memory
:label: 1-fact:strategies_memory

There is a one-to-one correspondence between plays $\pi = v_0 v_1 \dots$ in $\mathcal{A}$ 
and plays $\pi'$ in $\mathcal{A} \times  \mathcal{M}$ from $(v_0,m_0)$:
the play $\pi' = (v_0, m_0) (v_1, m_1) (v_2, m_2) \ldots$
is defined by $m_{i+1} = \delta(m_i, (v_{i},v_{i+1}))$.

````

Let $W$ be a condition on $\mathcal{A}$ and $W'$ a condition on $\mathcal{A} \times   \mathcal{M}$.
We say that $W$ reduces to $W'$ if for all plays $\pi$ in $\mathcal{A}$,
we have

$$
 \pi \in W \Longleftrightarrow  \pi' \in W'.
$$

Let $\mathcal{M}$ and $\mathcal{M}'$ two memory structure over the same graph, 
we let $\mathcal{M} \times   \mathcal{M}'$ denote the memory structure obtained by direct product.

````{prf:lemma} Memory structure reductions
:label: 1-lem:memory_structure_reduction

If $W$ reduces to $W'$ through the memory structure $\mathcal{M}$, then
Eve has a winning strategy in $\mathcal{G} = (  \mathcal{A},W)$ from $v_0$ if and only if 
she has a winning strategy in $\mathcal{G} \times   \mathcal{M} = (  \mathcal{A} \times   \mathcal{M}, W')$ from $(v_0,m_0)$. 

More specifically, if Eve has a winning strategy in $\mathcal{G} \times   \mathcal{M}$ from $(v,m_0)$ using $\mathcal{M}'$ as memory structure, 
then she has a winning strategy in $\mathcal{G}$ from $v$ using $\mathcal{M} \times   \mathcal{M}'$ as memory structure.
In particular if the strategy in $\mathcal{G} \times   \mathcal{M}$ is memoryless, then the strategy in $\mathcal{G}$ uses $\mathcal{M}$ as memory structure.

````

````{admonition} Proof
:class: dropdown tip

A winning strategy in $\mathcal{G}$ directly induces a winning strategy in $\mathcal{G} \times   \mathcal{M}$ simply by ignoring the additional information
and thanks to the equivalence above because $W$ reduces to $W'$.
For the converse implication, let $\sigma$ be a winning strategy in $\mathcal{G} \times   \mathcal{M}$ using $\mathcal{M}'$ as memory structure.
Recall that $\sigma$ is defined through the function $\sigma : ( V_\mathrm{Eve} \times M) \times M' \to E_M$.

Let $p : E_M \to E$ mapping the edge $e_m$ to $e$.
We construct a strategy $\sigma'$ in $\mathcal{G}$ using $\mathcal{M} \times   \mathcal{M}'$ as memory structure by

$$
\sigma'(v, (m,m')) = p(\sigma((v,m), m')).
$$

The correspondence between plays in $\mathcal{A}$ and $\mathcal{A} \times  \mathcal{M}$ maps plays consistent with $\sigma$ to plays consistent with $\sigma'$,
which together with the fact that $W$ reduces to $W'$ implies that $\sigma'$ is a winning strategy in $\mathcal{G}$ from $v$.

````

To obtain {prf:ref}`1-lem:automata_reduction` as a corollary of {prf:ref}`1-lem:memory_structure_reduction`
we observe that a reduction between objectives using an automaton induces a reduction between the induced conditions using a memory structure.
Formally, let us assume that $\Omega$ reduces to $\Omega'$, 
and let $\mathbf{A} = (Q, q_0, \delta, \Omega'[ \mathfrak{c}_\mathbf{A}])$ such that $L( \mathbf{A}) = \Omega$.
Let $\mathcal{G} = (  \mathcal{A}, \Omega[ \mathfrak{c}])$ a game.

We first define the memory structure $\mathcal{M} = (Q, q_0, \delta')$: the transition function is $\delta' : Q \times E \to Q$, it is defined
by $\delta'(q,(v,v')) = \delta(q,  \mathfrak{c}(v))$.
We then define $\mathfrak{c}'(v,q) =  \mathfrak{c}_\mathbf{A}(q,  \mathfrak{c}(v))$.

We note that $\Omega[ \mathfrak{c}]$ reduces to $\Omega'[ \mathfrak{c}']$: for all plays $\pi$ in $\mathcal{A}$, we have 
$\pi \in \Omega[ \mathfrak{c}]$ if and only if $\pi' \in \Omega'[ \mathfrak{c}']$: this is a reformulation of the fact that $L( \mathbf{A}) = \Omega$.

We construct the game $\mathcal{G}' = (  \mathcal{A} \times   \mathcal{M}, \Omega'[ \mathfrak{c}'])$.
Thanks to {prf:ref}`1-lem:memory_structure_reduction` the two games have the same winner and a strategy in the latter induce a strategy in the former
by composing with the memory structure $\mathcal{M}$, implying {prf:ref}`1-lem:automata_reduction`.
