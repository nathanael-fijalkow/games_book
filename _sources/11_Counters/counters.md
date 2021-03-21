(11-sec:counters)=
# Vector games

```{math}

\newcommand{\capp}[2][C]{\overline{\vec #2}^{#1}}

```

 A vector system is a finite directed graph with a partition of
the vertices and weighted edges.  Formally, it is a tuple
$\mathcal{V}=( \mathcal{L}, A, \mathcal{L}_\mathrm{Eve}, \mathcal{L}_\mathrm{Adam}, k)$ where $k\in\mathbb{N}$ is a
dimension, $\mathcal{L}$ is a finite set of locations partitioned into the
locations controlled by Eve and Adam, i.e.,
$\mathcal{L}= \mathcal{L}_\mathrm{Eve}\uplus  \mathcal{L}_\mathrm{Adam}$, and
$A\subseteq  \mathcal{L}\times\mathbb{Z}^ k\times \mathcal{L}$ is a finite set of
weighted actions.  We write $\ell \xrightarrow{\,\vec u,} \ell'$
rather than $( \ell,\vec u, \ell')$ for actions in $A$.  A
vector addition system with states is a vector system where
$\mathcal{L}_\mathrm{Adam}=\emptyset$, i.e., it corresponds to the one-player case.

````{prf:example} vector system
:label: 11-ex:mwg

  {numref}`11-fig:mwg` presents a vector system of
  dimension two with locations $\{ \ell, \ell'\}$ where $\ell$ is
  controlled by Eve and $\ell'$ by Adam.

````

```{figure} ./../FigAndAlgos/11-fig:mwg.png
:name: 11-fig:mwg
:align: center
A vector system.
```

The intuition behind a vector system is that it
maintains $k$ counters $\mathtt{c}_1,\dots,\mathtt{c}_k$ assigned
to integer values.  An action $\ell \xrightarrow{\,\vec u,} \ell'\in A$ then
updates each counter by adding the corresponding entry of $\vec u$,
that is for all $1\leq j\leq k$, the action performs the update
$\mathtt{c}_j := \mathtt{c}_j+\vec u(j)$.

  Before we proceed any further, let us fix some notations
for vectors in $\mathbb{Z}^ k$.  We write $\vec 0$ for the zero vector
with $\vec 0(j)  \stackrel{\!\,\!\,\textrm{def}}{=} 0$ for all $1\leq j\leq k$.  For all
$1\leq j\leq k$, we write $\vec e_j$ for the unit vector with
$\vec e_j(j)  \stackrel{\!\,\!\,\textrm{def}}{=} 1$ and $\vec e_{j}(j')  \stackrel{\!\,\!\,\textrm{def}}{=} 0$ for all $j'\neq j$.
Addition and comparison are defined componentwise, so that for
instance $\vec u\leq\vec u'$ if and only if for all $1\leq j\leq k$,
$\vec u(j)\leq\vec u'(j)$.  We write
$w( \ell \xrightarrow{\,\vec u,} \ell')  \stackrel{\!\,\!\,\textrm{def}}{=}\vec u$ for the weight of an
action and $w(\pi)  \stackrel{\!\,\!\,\textrm{def}}{=}\sum_{1\leq j\leq |\pi|} w(\pi_j)$
for the cumulative weight of a finite sequence of actions
$\pi\in A^\ast$.  For a vector $\vec u\in\mathbb{Z}^ k$, we use its
infinity norm $\|\vec u\|  \stackrel{\!\,\!\,\textrm{def}}{=}\max_{1\leq j\leq k}|\vec u(j)|$,
hence $\|\vec 0\|=0$ and $\|\vec e_j\|=\|-\vec e_j\|=1$, and we let
$\| \ell \xrightarrow{\,\vec u,} \ell'\|  \stackrel{\!\,\!\,\textrm{def}}{=}\| w( \ell \xrightarrow{\,\vec
  u,} \ell')\|=\|\vec u\|$
and $\| A\|  \stackrel{\!\,\!\,\textrm{def}}{=}\max_{a\in A}\| w(a)\|$.  Unless stated
otherwise, we assume that all our vectors are represented in binary,
hence $\| A\|$ may be exponential in the size of $\mathcal{V}$.

## Arenas and Games

 A vector system gives rise to an infinite graph
$G_\mathbb{N}  \stackrel{\!\,\!\,\textrm{def}}{=}(V,E)$ over the set of vertices
$V  \stackrel{\!\,\!\,\textrm{def}}{=}( \mathcal{L}\times\mathbb{N}^ k)\uplus\{ \bot\}$.  The vertices of the
graph are either **configurations** $\ell(\vec v)$ consisting of a
location $\ell\in  \mathcal{L}$ and a vector of non-negative integers
$\vec v\in\mathbb{N}^ k$---such a vector represents a valuation of the
counters $\mathtt{c}_1,\dots,\mathtt c_k$---, or the
sink $\bot$.

 Consider an action in $a=( \ell \xrightarrow{\,\vec u,} \ell')$ in $A$: we
see it as a partial function
$a{:}\, \mathcal{L}\times\mathbb{N}^ k\, \mathrel{\ooalign{\hfil$\mapstochar\mkern5mu$\hfil\cr$\to$\cr}}  \mathcal{L}\times\mathbb{N}^ k$ with domain
$\mathrm{dom}\, a  \stackrel{\!\,\!\,\textrm{def}}{=}\{ \ell(\vec v)\mid \vec v+\vec u\geq\vec 0\}$ and image
$a( \ell(\vec v))  \stackrel{\!\,\!\,\textrm{def}}{=}  \ell'(\vec v+\vec u)$; let also
$\mathrm{dom}\, A  \stackrel{\!\,\!\,\textrm{def}}{=}\bigcup_{a\in A} \mathrm{dom}\, a$.  This allows us to define
the set $E$ of edges as a set of pairs

$$

  E&  \stackrel{\!\,\!\,\textrm{def}}{=}\{( \ell(\vec v),a( \ell(\vec v)))\mid a\in A\text{ and
     } \ell(\vec v)\in \mathrm{dom}\, a\}\\
                               
  &\:\cup\:\{( \ell(\vec v), \bot)\mid \ell(\vec v)\not\in \mathrm{dom}\, A\}\cup\{( \bot, \bot)\}\;,

$$

where $\textrm{In}((v,v'))  \stackrel{\!\,\!\,\textrm{def}}{=} v$ and $\textrm{Out}((v,v'))  \stackrel{\!\,\!\,\textrm{def}}{=} v'$ for all
edges $(v,v')\in E$.  There is therefore an edge $(v,v')$ between two
configurations $v= \ell(\vec v)$ and $v'= \ell'(\vec v')$ if there
exists an action $\ell \xrightarrow{\,\vec u,} \ell'\in A$ such that
$\vec v'=\vec v+\vec u$.  Note that, quite importantly,
$\vec v+\vec u$ must be non-negative on every coordinate for this edge
to exist.  If no action can be applied, there is an edge to the
sink $\bot$, which ensures that $E$ is total: for all $v\in V$,
there exists an edge $(v,v')\in E$ for some $v'$, and thus there are
no deadlocks in the graph.

The configurations are naturally partitioned into those in
$V_\mathrm{Eve}  \stackrel{\!\,\!\,\textrm{def}}{=} \mathcal{L}_\mathrm{Eve}\times\mathbb{N}^ k$ controlled by Eve and those in
$V_\mathrm{Adam}  \stackrel{\!\,\!\,\textrm{def}}{=} \mathcal{L}_\mathrm{Adam}\times\mathbb{N}^ k$ controlled by Adam.  Regarding
the sink, the only edge starting from $\bot$ loops back
to it, and it does not matter who of Eve or Adam controls it.  This
gives rise to an infinite arena $\mathcal{A}_\mathbb{N}  \stackrel{\!\,\!\,\textrm{def}}{=}(G_\mathbb{N}, V_\mathrm{Eve}, V_\mathrm{Adam})$ called
the natural semantics of $\mathcal{V}$.

 Although we work in a turn-based setting with perfect
information, it is sometimes enlightening to consider the partial map
$\Delta{:}\,V\times A \mathrel{\ooalign{\hfil$\mapstochar\mkern5mu$\hfil\cr$\to$\cr}} E$ defined by
$\Delta( \ell(\vec v),a)  \stackrel{\!\,\!\,\textrm{def}}{=}( \ell(\vec v),a( \ell(\vec v)))$ if
$\ell(\vec v)\in \mathrm{dom}\, a$ and
$\Delta( \ell(\vec v),a)  \stackrel{\!\,\!\,\textrm{def}}{=}( \ell(\vec v), \bot)$ if
$\ell(\vec v)\not\in \mathrm{dom}\, A$.  Note that a sequence $\pi$ over $E$
that avoids the sink can also be described by an initial
configuration $\ell_0(\vec v_0)$ paired with a sequence
over $A$.

````{prf:example} natural semantics
:label: 11-ex:sem

  {numref}`11-fig:sem` illustrates the natural semantics of the system
  of {numref}`11-fig:mwg`; observe that all the configurations $\ell(0,n)$
  for $n\in\mathbb{N}$ lead to the sink.

````

```{figure} ./../FigAndAlgos/11-fig:sem.png
:name: 11-fig:sem
:align: center
The natural semantics of the
    vector system of {numref}`11-fig:mwg`: a circle (resp.\
    a square) at position $(i,j)$ of the grid denotes a configuration
    $\ell(i,j)$ (resp.\ $\ell'(i,j)$) controlled by Eve (resp. Adam).
```

 A vector system $\mathcal{V}=( \mathcal{L}, A, \mathcal{L}_\mathrm{Eve}, \mathcal{L}_\mathrm{Adam}, k)$, a
colouring $\mathfrak{c}{:}\,E\to C$, and an
objective $\Omega\subseteq C^\omega$ together define a vector game
$\mathcal{G}=(  \mathcal{A}_\mathbb{N}(\mathcal{V}), \mathfrak{c},\Omega)$.  Because $\mathcal{A}_\mathbb{N}(\mathcal{V})$ is an
infinite arena, we need to impose restrictions on our colourings
$\mathfrak{c}{:}\,E\to C$ and the qualitative
objectives $\Omega\subseteq C^\omega$; at the very least, they should
be recursive.

There are then two variants of the associated decision problem:

*  the given initial credit variant, where we are given $\mathcal{V}$,
  $\mathfrak{c}$, $\Omega$, a location $\ell_0\in \mathcal{L}$ and an initial credit
  $\vec v_0\in\mathbb{N}^ k$, and ask whether Eve wins $\mathcal{G}$ from the
  initial configuration $\ell_0(\vec v_0)$;
*  the existential initial credit variant, where we are given
  $\mathcal{V}$, $\mathfrak{c}$, $\Omega$, and a location $\ell_0\in \mathcal{L}$, and ask
  whether there exists an initial credit $\vec v_0\in\mathbb{N}^ k$ such
  that Eve wins $\mathcal{G}$ from the initial
  configuration $\ell_0(\vec v_0)$.

Let us instantiate the previous abstract definition of vector games.
We first consider two reachability-like
reachability
objectives, where $C  \stackrel{\!\,\!\,\textrm{def}}{=}\{\varepsilon, \textrm{Win}\}$ and
$\Omega  \stackrel{\!\,\!\,\textrm{def}}{=} \mathtt{Reach}$, namely configuration reachability and
coverability.  The difference between the two is that, in the
configuration reachability problem, a specific configuration
$\ell_f(\vec v_f)$ should be visited, whereas in the coverability
problem, Eve attempts to visit $\ell_f(\vec v')$ for some
vector $\vec v'$ componentwise larger or equal to
$\vec v_f$.

```{margin}
The name coverability comes from the the
  literature on Petri nets and vector addition systems with
  states, because Eve is attempting to **cover**
  $\ell_f(\vec v_f)$, i.e., to reach a configuration $\ell_f(\vec v')$
  with $\vec v'\geq\vec v_f$.
```

```{admonition} Problem (configuration reachability vector game with given initial credit)
:name: 11-pb:reach
**INPUT**:  A vector system
  $\mathcal{V}=( \mathcal{L}, A, \mathcal{L}_\mathrm{Eve}, \mathcal{L}_\mathrm{Adam}, k)$, an initial location
  $\ell_0\in \mathcal{L}$, an initial credit $\vec v_0\in\mathbb{N}^ k$, and a
  target configuration $\ell_f(\vec v_f)\in \mathcal{L}\times\mathbb{N}^ k$.

**QUESTION**: Does Eve have a strategy to reach $\ell(\vec v)$ from
  $\ell_0(\vec v_0)$?
  That is, does she win the configuration
  reachability game $(  \mathcal{A}_\mathbb{N}(\mathcal{V}), \mathfrak{c}, \mathtt{Reach})$ from
  $\ell_0(\vec v_0)$, where $\mathfrak{c}(e)=  \textrm{Win}$ if and only if
  $\textrm{In}(e)= \ell_f(\vec v_f)$?
```

```{admonition} Problem (coverability vector game with given initial credit)
:name: 11-pb:cov
**INPUT**:  A vector system
  $\mathcal{V}=( \mathcal{L}, A, \mathcal{L}_\mathrm{Eve}, \mathcal{L}_\mathrm{Adam}, k)$, an initial location
  $\ell_0\in \mathcal{L}$, an initial credit $\vec v_0\in\mathbb{N}^ k$, and a
  target configuration $\ell_f(\vec v_f)\in \mathcal{L}\times\mathbb{N}^ k$.

**QUESTION**: Does Eve have a strategy to reach $\ell(\vec v')$ for some
  $\vec v'\geq\vec v_f$ from $\ell_0(\vec v_0)$?
  That is, does she win
  the coverability game $(  \mathcal{A}_\mathbb{N}(\mathcal{V}), \mathfrak{c}, \mathtt{Reach})$ from
  $\ell_0(\vec v_0)$, where $\mathfrak{c}(e)=  \textrm{Win}$ if and only if
  $\textrm{In}(e)= \ell_f(\vec v')$ for some $\vec v'\geq\vec v_f$?
```

````{prf:example} Objectives
:label: 11-ex:cov

  Consider the target configuration $\ell(2,2)$ in
  {numref}`11-fig:mwg,11-fig:sem`.  Eve\'s winning region in the
  configuration reachability vector game is
  $W_\mathrm{Eve}=\{ \ell(n+1,n+1)\mid n\in\mathbb{N}\}\cup\{ \ell'(0,1)\}$, displayed on the left
  in {numref}`11-fig:cov`.  Eve has indeed an obvious winning strategy
  from any configuration $\ell(n,n)$ with $n\geq 2$, which is to use
  the action $\ell \xrightarrow{\,-1,-1,} \ell$ until she reaches $\ell(2,2)$.
  Furthermore, in $\ell'(0,1)$---due to the natural semantics---,
  Adam has no choice but to use the action $\ell' \xrightarrow{\,2,1,} \ell$:
  therefore $\ell'(0,1)$ and $\ell(1,1)$ are also winning for Eve.

```{figure} ./../FigAndAlgos/11-fig:cov.png
:name: 11-fig:cov
:align: center
The winning regions of Eve in the
    configuration reachability game (left) and the coverability game
    (right) on the graphs of {numref}`11-fig:mwg,11-fig:sem` with target
    configuration $\ell(2,2)$.  The winning vertices are in filled in
    green, while the losing ones are filled with white with a red
    border; the sink is always losing.
```

In the coverability vector game, Eve\'s winning region is
$W_\mathrm{Eve}=\{ \ell(m+2,n+2), \ell'(m+2,n+2), \ell'(0,n+1), \ell(1,n+2), \ell'(2m+2,1), \ell(2m+3,1)\mid
m,n\in\mathbb{N}\}$
displayed on the right in {numref}`11-fig:cov`.  Observe in particular
that Adam is forced to use the action $\ell' \xrightarrow{\,2,1,}\ell$ from
the configurations of the form $\ell'(0,n+1)$, which brings him to a
configuration $\ell(2,n+2)$ coloured $\textrm{Win}$ in the game, and thus the
configurations of the form $\ell(1,n+1)$ are also winning for Eve 
since she can play $\ell \xrightarrow{\,-1,0,} \ell'$.  Thus the configurations of
the form $\ell(2m+3,n+1)$ are also winning for Eve, as she can play
the action $\ell \xrightarrow{\,-1,0,} \ell'$ to a winning configuration
$\ell'(2m+2,n+1)$ where all the actions available to Adam go into
her winning region.

````

````{prf:remark} Location reachability
:label: 11-rk:cov2cov

  One can notice that coverability is equivalent to **location
  reachability**, where we are given a target location $\ell_f$ but no
  target vector, and want to know whether Eve have a strategy to
  reach $\ell_f(\vec v)$ for some $\vec v$.

  Indeed, in both configuration reachability and coverability, we
  can assume without loss of generality that $\ell_f\in \mathcal{L}_\mathrm{Eve}$ is
  controlled by Eve and that $\vec v_f=\vec 0$ is the zero
  vector. Here is a $\textrm{LOGSPACE}$ reduction to that case.  If
  $\ell_0(\vec v_0)= \ell_f(\vec v_f)$ in the case of configuration
  reachability, or $\ell_0= \ell_f$ and $\vec v_0\geq\vec v_f$ in the
  case of coverability, the problem is trivial.
  
  Otherwise, any winning play must use at least one action.  For
  each incoming action $a=( \ell \xrightarrow{\,\vec u,} \ell_f)$ of $\ell_f$,
  create a new location $\ell_a$ controlled by Eve and replace $a$ by
  $\ell \xrightarrow{\,\vec u,} \ell_a \xrightarrow{\,\vec 0,} \ell_f$, so that Eve gains the
  control right before any play reaches $\ell_f$.  Also add a new
  location $\smiley$ controlled by Eve with actions
  $\ell_a \xrightarrow{\,-\vec v_f,}\smiley$, and use $\smiley(\vec 0)$ as target
  configuration.

````

````{prf:remark} Coverability to reachability
:label: 11-rk:cov2reach

  There is a $\textrm{LOGSPACE}$ reduction from coverability to
  configuration reachability.  By {prf:ref}`11-rk:cov2cov`, we can assume
  without loss of generality that $\ell_f\in \mathcal{L}_\mathrm{Eve}$ is controlled
  by Eve and that $\vec v_f=\vec 0$ is the zero vector. It suffices
  therefore to add an action $\ell_f \xrightarrow{\,-\vec e_j,} \ell_f$ for
  all $1\leq j\leq k$.

````

Departing from reachability games, the
following is a very simple kind of safety
games where $C  \stackrel{\!\,\!\,\textrm{def}}{=}\{\varepsilon, \textrm{Lose}\}$ and $\Omega  \stackrel{\!\,\!\,\textrm{def}}{=} \mathtt{Safe}$;
{numref}`11-fig:nonterm` shows Eve\'s winning region in the case of the
graphs of {numref}`11-fig:mwg,11-fig:sem`.

```{admonition} Problem (non-termination vector game with given initial credit)
:name: 11-pb:nonterm
**INPUT**:  A vector system
  $\mathcal{V}=( \mathcal{L}, A, \mathcal{L}_\mathrm{Eve}, \mathcal{L}_\mathrm{Adam}, k)$, an initial location
  $\ell_0\in \mathcal{L}$, and an initial credit $\vec v_0\in\mathbb{N}^ k$.

**QUESTION**: Does Eve have a strategy to avoid the sink $\bot$ from
  $\ell_0(\vec v_0)$?
  That is, does she win the non-termination
  game $(  \mathcal{A}_\mathbb{N}(\mathcal{V}), \mathfrak{c}, \mathtt{Safe})$ from $\ell_0(\vec v_0)$, where
  $\mathfrak{c}(e)= \textrm{Lose}$ if and only if $\textrm{In}(e)= \bot$?
```

```{figure} ./../FigAndAlgos/11-fig:nonterm.png
:name: 11-fig:nonterm
:align: center
The winning region of Eve in the
    non-termination game on the graphs of {numref}`11-fig:mwg,11-fig:sem`.
```

Finally, one of the most general vector games are parity games, where $C  \stackrel{\!\,\!\,\textrm{def}}{=}\{1,\dots,d\}$ and
$\Omega  \stackrel{\!\,\!\,\textrm{def}}{=} \mathtt{Parity}$.  In order to define a colouring of the natural
semantics, we assume that we are provided with a **location
  colouring** $\mathrm{lcol}{:}\, \mathcal{L}\to\{1,\dots,d\}$.
```{admonition} Problem (parity vector game with given initial credit)
:name: 11-pb:parity
**INPUT**: A vector system
  $\mathcal{V}=( \mathcal{L}, A, \mathcal{L}_\mathrm{Eve}, \mathcal{L}_\mathrm{Adam}, k)$, an initial location
  $\ell_0\in \mathcal{L}$, an initial credit $\vec v_0\in\mathbb{N}^ k$, and a
  location colouring $\mathrm{lcol}{:}\, \mathcal{L}\to\{1,\dots,d\}$ for some $d>0$.

**QUESTION**: Does Eve have a strategy to simultaneously avoid the
  sink $\bot$ and fulfil the parity objective from $\ell_0(\vec
  v_0)$? That is, does she win the parity game
  $(  \mathcal{A}_\mathbb{N}(\mathcal{V}), \mathfrak{c}, \mathtt{Parity})$ from $\ell_0(\vec v_0)$, where
  $\mathfrak{c}(e)  \stackrel{\!\,\!\,\textrm{def}}{=} \mathrm{lcol}( \ell)$ if $\textrm{In}(e)= \ell(\vec v)$ for
  some $\vec v\in\mathbb{N}^ k$, and $\mathfrak{c}(e)  \stackrel{\!\,\!\,\textrm{def}}{=} 1$ if $\textrm{In}(e)= \bot$?
```

````{prf:remark} Non termination to parity
:label: 11-rk:nonterm2parity

  There is a $\textrm{LOGSPACE}$ reduction from non-termination to
  parity.
  Indeed, the two games coincide if we pick the constant location
  colouring defined by $\mathrm{lcol}( \ell)  \stackrel{\!\,\!\,\textrm{def}}{=} 2$ for all $\ell\in \mathcal{L}$ in
  the parity game.

````

````{prf:remark} Coverability to parity
:label: 11-rk:cov2parity

  There is a $\textrm{LOGSPACE}$ reduction from coverability to
  parity.  Indeed, by {prf:ref}`11-rk:cov2cov`, we can assume
  that $\ell_f\in \mathcal{L}_\mathrm{Eve}$ is controlled by Eve and that the target
  credit is $\vec v_f=\vec 0$ the zero vector.  It suffices
  therefore to add an action $\ell_f \xrightarrow{\,\vec 0,} \ell_f$ and to colour
  every location $\ell\neq \ell_f$ with $\mathrm{lcol}( \ell)  \stackrel{\!\,\!\,\textrm{def}}{=} 1$ and
  to set $\mathrm{lcol}( \ell_f)  \stackrel{\!\,\!\,\textrm{def}}{=} 2$.

````

The existential initial credit variants of
\crefrange{11-pb:reach}{11-pb:parity} are defined similarly, where
$\vec v_0$ is not given as part of the input, but existentially
quantified in the question.

(11-sec:undec)=
## Undecidability
The bad news is that, although \crefrange{11-pb:reach}{11-pb:parity}
are all decidable in the one-player case---see
the \cref[11-sec:references]{bibliographic notes} at the end of the
chapter---, they become undecidable in the two-player setting.

````{prf:theorem} Undecidability of vector games
:label: 11-th:undec

  Configuration reachability, coverability, non-termination, and
  parity vector games, both with given and
  with existential initial credit, are undecidable in any dimension
  $k\geq 2$.

````

````{admonition} Proof
:class: dropdown tip

  By {prf:ref}`11-rk:cov2reach` and {prf:ref}`11-rk:nonterm2parity`, it suffices to prove the
  undecidability of coverability and non-termination.  For this,
  we exhibit reductions from the halting problem of deterministic
  Minsky machines with at least two counters.

   Formally, a deterministic Minsky machine with $k$ counters
  $\mathcal{M}=( \mathcal{L}, A, k)$ is defined similarly to a vector addition
  system with states with additional zero test actions
  $a=( \ell \xrightarrow{\,i \stackrel{\!\,\!\,\textrm{?0,}}{=}} \ell')$.  The set of locations contains a
  distinguished halt location $\ell_\mathtt{halt}$, and for every
  $\ell\in \mathcal{L}$, exactly one of the following holds: either (i)
  $( \ell \xrightarrow{\,\vec e_i,} \ell')\in A$ for some $0<i\leq k$ and
  $\ell'\in \mathcal{L}$, or (ii) $( \ell \xrightarrow{\,i \stackrel{\!\,\!\,\textrm{?0,}}{=}} \ell')\in A$ and
  $( \ell \xrightarrow{\,-\vec e_i,} \ell'')\in A$ for some $0<i\leq k$ and
  $\ell', \ell''\in \mathcal{L}$, or (iii) $\ell= \ell_\mathtt{halt}$.  The
  semantics of $\mathcal{M}$ extends the natural semantics by
  handling zero tests actions $a=( \ell \xrightarrow{\,i \stackrel{\!\,\!\,\textrm{?0,}}{=}} \ell')$: we
  define the domain as $\mathrm{dom}\, a  \stackrel{\!\,\!\,\textrm{def}}{=}\{ \ell(\vec v)\mid \vec v(i)=0\}$
  and the image by $a( \ell(\vec v))  \stackrel{\!\,\!\,\textrm{def}}{=}  \ell(\vec v)$.  This
  semantics is deterministic, and from any starting vertex of $\mathcal{A}_\mathbb{N}(\mathcal{M})$,
  there is a unique play, which either eventually visits
  $\ell_\mathtt{halt}$ and then the sink in the next step, or keeps
  avoiding both $\ell_\mathtt{halt}$ and the sink
  indefinitely.

   The halting problem asks, given a deterministic Minsky machine
  and an initial location $\ell_0$, whether it halts, that is, whether
  $\ell_\mathtt{halt}(\vec v)$ is reachable for
  some $\vec v\in\mathbb{N}^ k$ starting from $\ell_0(\vec 0)$.  The
  halting problem is undecidable in any dimension
  $k\geq 2$ {cite}`Minsky:1967`.
  Thus the halting problem is akin to the coverability of
  $\ell_\mathtt{halt}(\vec 0)$ with given initial credit $\vec 0$,
  but on the one hand there is only one player and on the other hand
  the machine can perform zero tests.

```{figure} ./../FigAndAlgos/11-fig:undec.png
:name: 11-fig:undec
:align: center
Schema of the reduction in the proof of {prf:ref}`11-th:undec`.
```
  Here is now a reduction to
  [Problem](11-pb:cov).  Given an instance of the halting problem, i.e.,
  given a deterministic Minsky machine $\mathcal{M}=( \mathcal{L}, A, k)$ and an
  initial location $\ell_0$, we construct a vector system
  $\mathcal{V}  \stackrel{\!\,\!\,\textrm{def}}{=}( \mathcal{L}\uplus \mathcal{L}_{ \stackrel{\!\,\!\,\textrm{?0}}{=}}\uplus\{\frownie\}, A', \mathcal{L}, \mathcal{L}_{ \stackrel{\!\,\!\,\textrm{?0}}{=}}\uplus\{\frownie\}, k)$
  where all the original locations are controlled by Eve and
  $\mathcal{L}_{ \stackrel{\!\,\!\,\textrm{?0}}{=}}\uplus\{\frownie\}$ is a set of new locations
  controlled by Adam.  We use $\mathcal{L}_{ \stackrel{\!\,\!\,\textrm{?0}}{=}}$ as a set of
  locations defined by
  
$$

     \mathcal{L}_{ \stackrel{\!\,\!\,\textrm{?0}}{=}}&  \stackrel{\!\,\!\,\textrm{def}}{=}\{ \ell'_{i \stackrel{\!\,\!\,\textrm{?0}}{=}}\mid\exists \ell\in \mathcal{L}\mathbin.( \ell \xrightarrow{\,i \stackrel{\!\,\!\,\textrm{?0,}}{=}} \ell')\in A\}\intertext{and
                   define the set of actions by (see {numref}`11-fig:undec`)}
     A'&  \stackrel{\!\,\!\,\textrm{def}}{=}\{ \ell \xrightarrow{\,\vec
          e_i,} \ell'\mid( \ell \xrightarrow{\,\vec e_i,} \ell')\in A\}\cup\{ \ell \xrightarrow{\,-\vec e_i,} \ell''\mid( \ell \xrightarrow{\,-\vec e_i,} \ell'')\in A\}\\
    &\:\cup\:\{ \ell \xrightarrow{\,\vec
      0,} \ell'_{i \stackrel{\!\,\!\,\textrm{?0}}{=}},\;\;\: \ell'_{i \stackrel{\!\,\!\,\textrm{?0}}{=}}\!\! \xrightarrow{\,\vec 0,} \ell',\;\;\: \ell'_{i \stackrel{\!\,\!\,\textrm{?0}}{=}}\!\! \xrightarrow{\,-\vec e_i,}\frownie\mid( \ell \xrightarrow{\,i \stackrel{\!\,\!\,\textrm{?0,}}{=}} \ell')\in A\}\;.
  
$$

  We use $\ell_0(\vec 0)$ as initial configuration and
  $\ell_\mathtt{halt}(\vec 0)$ as target configuration for the
  constructed coverability instance.  Here is the crux of the
  argument why Eve has a winning strategy to cover
  $\ell_\mathtt{halt}(\vec 0)$ from $\ell_0(\vec 0)$ if and only if
  the Minsky machine halts.
  
  Consider any configuration $\ell(\vec v)$.  If
  $( \ell \xrightarrow{\,\vec e_i,} \ell')\in A$, Eve has no choice but to apply
  $\ell \xrightarrow{\,\vec e_i,} \ell'$ and go to the configuration
  $\ell'(\vec v+\vec e_i)$ also reached in one step in $\mathcal{M}$.  If
  $\{ \ell \xrightarrow{\,i \stackrel{\!\,\!\,\textrm{?0,}}{=}} \ell', \ell \xrightarrow{\,-\vec e_i,} \ell''\}\in A$ and
  $\vec v(i)=0$, due to the natural semantics, Eve cannot use the
  action $\ell \xrightarrow{\,-\vec e_i,} \ell''$, thus she must use
  $\ell \xrightarrow{\,\vec 0,} \ell'_{i \stackrel{\!\,\!\,\textrm{?0}}{=}}$.  Still due to the natural
  semantics, Adam cannot use
  $\ell'_{i \stackrel{\!\,\!\,\textrm{?0}}{=}}\!\! \xrightarrow{\,-\vec e_i,}\frownie$, thus he must use
  $\ell'_{i \stackrel{\!\,\!\,\textrm{?0}}{=}}\!\! \xrightarrow{\,\vec 0,} \ell'$.  Hence Eve regains the
  control in $\ell'(\vec v)$, which was also the configuration reached
  in one step in $\mathcal{M}$.  Finally, if
  $\{ \ell \xrightarrow{\,i \stackrel{\!\,\!\,\textrm{?0,}}{=}} \ell', \ell \xrightarrow{\,-\vec e_i,} \ell''\}\in A$ and
  $\vec v(i)>0$, Eve can choose: if she uses
  $\ell \xrightarrow{\,-\vec e_i,} \ell''$, she ends in the configuration
  $\ell''(\vec v-\vec e_i)$ also reached in one step in $\mathcal{M}$.  In
  fact, she should not use $\ell \xrightarrow{\,\vec 0,} \ell'_{i \stackrel{\!\,\!\,\textrm{?0}}{=}}$,
  because Adam would then have the opportunity to apply
  $\ell'_{i \stackrel{\!\,\!\,\textrm{?0}}{=}}\!\! \xrightarrow{\,-\vec e_i,}\frownie$ and to win, as
  $\frownie$ is a deadlock location and all the subsequent moves end
  in the sink.  Thus, if $\mathcal{M}$ halts, then Eve has a winning
  strategy that simply follows the unique play of $\mathcal{M}$, and
  conversely, if Eve wins, then necessarily she had to follow the
  play of $\mathcal{M}$ and thus the machine halts.

 Further note that, in a deterministic Minsky machine the
  halting problem is similarly akin to the **complement** of
  non-termination with given initial credit $\vec 0$.  This means
  that, in the vector system
  $\mathcal{V}=( \mathcal{L}\uplus \mathcal{L}_{ \stackrel{\!\,\!\,\textrm{?0}}{=}}\uplus\{\frownie\}, A', \mathcal{L}, \mathcal{L}_{ \stackrel{\!\,\!\,\textrm{?0}}{=}}\uplus\{\frownie\}, k)$
  defined earlier, Eve has a winning strategy to avoid the sink
  from $\ell_0(\vec 0)$ if and only if the given Minsky
  machine does
  not halt from $\ell_0(\vec 0)$, which shows the undecidability of
  [Problem](11-pb:nonterm).

 Finally, let us observe that both the existential and the
  universal initial credit variants of the halting problem are also
  undecidable.  Indeed, given an instance of the halting problem,
  i.e., given a deterministic Minsky machine $\mathcal{M}=( \mathcal{L}, A, k)$
  and an initial location $\ell_0$, we add $k$ new locations
  $\ell_k, \ell_{ k-1},\dots, \ell_1$ with respective actions
  $\ell_j \xrightarrow{\,-\vec e_j,} \ell_j$ and $\ell_j \xrightarrow{\,j \stackrel{\!\,\!\,\textrm{?0,}}{=}} \ell_{j-1}$
  for all $k\geq j>0$.  This modified machine first resets all its
  counters to zero before reaching $\ell_0(\vec 0)$ and then performs
  the same execution as the original machine.  Thus there exists an
  initial credit $\vec v$ such that the modified machine
  reaches $\ell_\mathtt{halt}$ from $\ell_k(\vec v)$ if and only if
  for all initial credits $\vec v$ the modified machine
  reaches $\ell_\mathtt{halt}$ from $\ell_k(\vec v)$, if and only if
  $\ell_\mathtt{halt}$ was reachable from $\ell_0(\vec 0)$ in the
  original machine.  The previous construction of a vector system
  applied to the modified machine then shows the undecidability of the
  existential initial credit variants of
  [Problem](11-pb:cov,11-pb:nonterm)

  .

````
