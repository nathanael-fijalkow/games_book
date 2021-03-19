(9-sec:state_space_representation)=
# State-Space Representation

```{math}

\renewcommand{\Game}{\game}

```

We introduce a data structure to represent sets of clock
valuations and manipulate them efficiently in order to compute
successors and predecessors in a given timed game. This will allow us
to use a fixpoint characterization of the winning states analogous to
that in finite games as in Chapter {ref}`2-chap:regular`.

A **zone** is any subset of $\mathbb{R}_{\geq 0}^ \mathcal{C}$ that can be defined
using a clock constraint (hence a zone is convex).  We will see that
sets of states that appear when exploring the state space of a timed
game can be represented using zones.  We use the
**difference-bound matrices** to represent zones:
this is one of the main data structures used in timed-automata
verification {cite}`Dil90,BM83`. The idea is to store, in a matrix,
upper bounds on clocks and on differences of pairs of clocks.

Formally, given a clock
set $\mathcal{C}=\{x_1,\ldots,x_m\}$, we define $\mathcal{C}_0 =  \mathcal{C} \cup \{x_0\}$
where $x_0$ is seen as a
special clock which is always $0$.

A difference-bound matrix (DBM) is a $| \mathcal{C}_0|\times | \mathcal{C}_0|$
matrix with coefficients in $\{\mathord\leq,\mathord<\} \times
\mathbb{Z}$.  For any DBM $M$, the $(i,j)$-component of the matrix $M$
will be written $(\prec^M_{i,j}, M_{i,j})$ where $\prec^M_{i,j}$ is
the inequality in $\{\mathord\leq,\mathord<\}$, and $M_{i,j}$ the
integer coefficient. A DBM $M$ defines the zone

$$
  [M] = \Bigl\{v\in  \mathbb{R}_{\geq 0}^{ \mathcal{C}}\Bigm|
  \bigwedge_{0\leq i,j \leq | \mathcal{C}_0|} v(x_i)-v(x_j) \prec^M_{i,j} M_{i,j}\Bigr\},
$$

where $v(x_0) = 0$.

````{prf:example} NEEDS TITLE AND LABEL 
  Consider the clock set $\mathcal{C}=\{x_1,x_2\}$
  and the zone $Z$ defined by 
  $x_1\leq 1 \land x_1-x_2 \leq 0 \land x_2\leq 3\land x_2-x_1 \leq 2$, which can be
  written as the following DBM:

$$
    M=\begin{pmatrix}
      (\leq,0) &(\leq,0) &(\leq,0)\\
      (\leq,1) &(\leq,0) &(\leq,0)\\
      (\leq,3) &(\leq,2) &(\leq,0)
    \end{pmatrix}
    \qquad
  \tikz[scale=.45]{ 
    \path[use as bounding box] (-1,1.2) -- (2,4);
    \begin{scope}
      \draw[latex'-latex'] (3.5,0) node[right] {$x_1$}
        -| (0,3.8) node[left] {$x_2$};
      \begin{scope}
        \path[clip] (0,0) -- (3.5,0) [rounded corners=12mm]
          -- (3.5,3.9) [rounded corners=0mm] -| (0,0);
        \draw[dgrey,fillarea] (0,0) -- (1,1) |- (0,3) -- cycle;
        \begin{scope}[opacity=.3]
          \foreach \x in {-4,...,4}
                 {\draw (\x,0) -- +(9,9);
                   \draw (0,\x) -- +(9,0);
                   \draw (\x,0) -- +(0,9);}
        \end{scope}
        
      \end{scope}
    \end{scope}

    }
  $$

  For instance, $M[2,0]=(\leq, 3)$ represents the
  constraint $x_2-x_0\leq 3$, i.e., $x_2\leq 3$.

  The diagram to the right of the figure represents the set $[M]$.

  Consider the clock set $\mathcal{C}=\{x_1,x_2\}$
  and the zone $Z$ defined by 
  $x_1\leq 1 \land x_1-x_2 \leq 0 \land x_2\leq 3\land x_2-x_1 \leq 2$, which can be
  written as the following DBM:

$$
    M=\begin{pmatrix}
      (\leq,0) &(\leq,0) &(\leq,0)\\
      (\leq,1) &(\leq,0) &(\leq,0)\\
      (\leq,3) &(\leq,2) &(\leq,0)
    \end{pmatrix}
    \qquad
  \tikz[scale=.45]{ 
    \path[use as bounding box] (-1,1.2) -- (2,4);
    \begin{scope}
      \draw[latex'-latex'] (3.5,0) node[right] {$x_1$}
        -| (0,3.8) node[left] {$x_2$};
      \begin{scope}
        \path[clip] (0,0) -- (3.5,0) [rounded corners=12mm]
          -- (3.5,3.9) [rounded corners=0mm] -| (0,0);
        \draw[dgrey,fillarea] (0,0) -- (1,1) |- (0,3) -- cycle;
        \begin{scope}[opacity=.3]
          \foreach \x in {-4,...,4}
                 {\draw (\x,0) -- +(9,9);
                   \draw (0,\x) -- +(9,0);
                   \draw (\x,0) -- +(0,9);}
        \end{scope}
        
      \end{scope}
    \end{scope}

    }
  $$

  For instance, $M[2,0]=(\leq, 3)$ represents the
  constraint $x_2-x_0\leq 3$, i.e., $x_2\leq 3$.

  The diagram to the right of the figure represents the set $[M]$.

````

We now define elementary operations on DBMs which are used to explore
the state space of timed games. We start by giving set-theoretic
definitions and then comment on their computation with DBMs.

Let $\sf Post_{\geq 0}(Z)$ denote the zone describing the
**time-successors** of $Z$, and $\sf Pre_{\geq 0}(Z)$ the
**time-predecessors** of $Z$. Formally,
\begin{xalignat*}1
     \sf Post_{\geq 0}(Z)&= \{v \in  \mathbb{R}_{\geq 0}^{ \mathcal{C}}
    \mid \exists t\geq 0.\  v-t \in Z\}
    \\
     \sf Pre_{\geq 0}(Z) &=
    \{v \in  \mathbb{R}_{\geq 0}^{ \mathcal{C}} \mid \exists t \geq 0.\ v + t \in Z\}.
\end{xalignat*}

Given $R\subseteq \mathcal{C}$, we also define
\begin{xalignat*}1
   \mathsf{Reset}_R(Z) &= \{v \in  \mathbb{R}_{\geq 0}^{ \mathcal{C}} \mid \exists v' \in Z.\
  v=v'[R\leftarrow 0]\} \\
   \sf Unreset_R(Z) &= \{ v \in  \mathbb{R}_{\geq 0}^{ \mathcal{C}} \mid \exists v' \in Z.\
  v' = v[R \leftarrow 0]\}.
\end{xalignat*}

These operations, together with intersection, suffice to describe
one-step successors and predecessors by an edge of a timed automaton.
For instance, given edge $e=(\ell,g,R,\ell')$ and
set $S \subseteq  \mathbb{R}_{\geq 0}^ \mathcal{C}$, the set of states that are reached
after letting time elapse and taking edge $e$ can be obtained as

$$
   \sf Post_e(S) =  \mathsf{Reset}_R( \sf Post_{\geq 0}(S)\cap G),
$$

where $G$ denotes the zone corresponding to the guard $g$.
Similarly, we can compute the predecessors of $S$ by edge $e$ as

$$
 \sf Pre_e(S) =  \sf Pre_{\geq 0}(G \cap  \sf Unreset_R(S)).

$$

We illustrate these constructions on {numref}`9-fig:opzones`.

```{figure} ./../FigAndAlgos/9-fig:opzones.png
:name: 9-fig:opzones
:align: center
Operations on zones
```

It is not hard to prove that the above operations preserve zones: if $S$ is a
zone, then so is the result of any of these operations. Moreover, each
single operation can be computed in time $O(| \mathcal{C}|^3)$ using the
DBM representation. The underlying algorithms often modify some
elements of the matrix and run an all-pairs shortest path algorithm,
namely the Floyd-Roy-Warshall algorithm, on a graph whose adjacency
matrix is the given DBM.  Computing the shortest paths renders the DBM
**canonical**; in fact, this allows one to compute the tightest
constraints on all differences of clock pairs, and this can be shown
to yield a unique representation of a given zone.

Let us call the above operations **basic operations** on DBMs {cite}`BY04`.

````{prf:theorem} Complexity of basic operations on DBMs
:label: 9-thm:complexity_basic_operations_DBMs

  Given a DBM of size $n\times n$, any basic operation yields a DBM
  and can be computed in time $O(n^3)$.

````

Observe that a DBM always describes a convex subset
of $\mathbb{R}_{\geq 0}^ \mathcal{C}$ since it is a conjunction of convex clock
constraints. However, the set of winning states is in general
non-convex in timed games. The simple arena
of {numref}`9-fig:non-convex` provides an example: if  Eve's objective
is to reach $\ell_1$, then it should just avoid the configurations
satisfying $1\leq x_1,x_2\leq 2$. But this set of predecessors is then
non-convex as shown in {numref}`9-fig:non-convex`.

We thus have to work with unions of zones, also called
**federations** of zones, or **federations** for short.

```{figure} ./../FigAndAlgos/9-fig:non-convex.png
:name: 9-fig:non-convex
:align: center
Winning configurations (in $\ell$)
    for  Eve to ensure reaching $\ell_1$.

```

One particular operation that we need is complementation.
The complement of a convex set is of course not convex in general, but
we can still compute, in polynomial time, the complement of a DBM $M$,
written $M^c$, as a federation of DBMs.

````{prf:theorem} Complement of DBMs
:label: 9-thm:complement_DBM

  The complement of a DBM of size $n\times n$ can be computed as a
  federation of at most $n(n-1)$ DBMs.

````

The above theorem is seen easily as follows. Since a DBM represents a
conjunction of constraints, the complement is computed easily as the
disjunction of the complement of each elementary constraint appearing
in it.  For instance, the complement of $x_1\leq 1 \land x_2 \geq 2$ is
$x_1>1 \lor x_2<2$, which can be represented as the federation of two
zones.

In the rest of this chapter, we describe two algorithms to solve timed
games using the DBM data structure and the operations introduced
above. Our algorithms are extensions of those used for finite games,
but we explore the set of zones instead of the set of vertices, and
predecessor and successor operations are replaced by their zone-based
counterparts.

As for finite games, we are interested in computing a fixpoint to
determine whether a given configuration is winning for  Eve. We start
by introducing the zone-based counterparts of the controllable predecessors operator
which
is the main tool in the algorithms.
