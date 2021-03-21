(11-sec:resource)=
# Resource-conscious games

```{math}

\newcommand{\capp}[2][C]{\overline{\vec #2}^{#1}}

```

Vector games are very well suited for reasoning about systems
manipulating discrete resources, modelled as counters.  However, in
the natural semantics, actions that would deplete some resource,
i.e., that would make some counter go negative, are simply inhibited.
In models of real-world systems monitoring resources like a gas
tank or a battery, a depleted resource would be considered as a system
failure.  In the energy games of Section {ref}`11-sec:energy`, those situations
are accordingly considered as winning for Adam.  Moreover, if we are
modelling systems with a bounded capacity for storing resources, a
counter exceeding some bound might also be considered as a failure,
which will be considered with bounding games in Section {ref}`11-sec:bounding`.

These resource-conscious games can be seen as providing alternative
semantics for vector systems.  They will also be instrumental in
establishing complexity upper bounds for monotonic asymmetric vector
games later in Section {ref}`11-sec:complexity`, and are strongly related to
multidimensional mean-payoff games, as will be explained in
Section {ref}`12-sec:MPEG` of Chapter {ref}`12-chap:multiobjective`.

(11-sec:energy)=
## Energy Semantics

Energy games model systems where the depletion of a resource
allows Adam to win.  This is captured by an energy semantics
$\mathcal{A}_\mathbb{E}(\mathcal{V})  \stackrel{\!\,\!\,\textrm{def}}{=}(V,E_\mathbb{E}, V_\mathrm{Eve}, V_\mathrm{Adam})$ associated with a vector
system $\mathcal{V}$: we let as before
$V  \stackrel{\!\,\!\,\textrm{def}}{=}( \mathcal{L}\times\mathbb{N}^ k)\uplus\{ \bot\}$, but define instead

$$

  E_\mathbb{E}&  \stackrel{\!\,\!\,\textrm{def}}{=} \{( \ell(\vec v),  \ell'(\vec v+\vec u)\mid
          \ell \xrightarrow{\,\vec u,} \ell'\in A\text{
      and }\vec v+\vec u\geq\vec 0\}\\
    &\:\cup\:\{( \ell(\vec v), \bot)\mid\forall \ell \xrightarrow{\,\vec
      u,} \ell'\in A\mathbin.\vec v+\vec u\not\geq\vec 0\}
    \cup\{( \bot, \bot)\}\;.

$$

In the energy semantics, moves that would result in a negative
component lead to the sink instead of being inhibited.

````{prf:example} Energy semantics
:label: 11-ex:nrg

  {numref}`11-fig:nrg` illustrates the energy semantics of the vector
  system depicted in {numref}`11-fig:mwg` on \cpageref{11-fig:mwg}.  Observe that,
  by contrast with the natural semantics of the same system depicted
  in {numref}`11-fig:sem`, all the configurations $\ell'(0,n)$ controlled
  by Adam can now move to the sink.

````

```{figure} ./../FigAndAlgos/11-fig:nrg.png
:name: 11-fig:nrg
:align: center
The energy semantics of the
    vector system of {numref}`11-fig:mwg`: a circle (resp.\
    a square) at position $(i,j)$ of the grid denotes a configuration
    $\ell(i,j)$ (resp.\ $\ell'(i,j)$) controlled by Eve (resp. Adam).
```

Given a colouring $\mathfrak{c}{:}\,E\to C$ and an objective $\Omega$, we
call the resulting game $(  \mathcal{A}_\mathbb{E}(\mathcal{V}), \mathfrak{c},\Omega)$ an energy
game.  In particular, we shall speak of configuration
reachability, coverability, non-termination, and parity energy games when replacing $\mathcal{A}_\mathbb{N}(\mathcal{V})$ by
$\mathcal{A}_\mathbb{E}(\mathcal{V})$ in \crefrange{11-pb:reach}{11-pb:parity}; the
existential initial credit variants are defined similarly.

````{prf:example} Energy games
:label: 11-ex:cov-nrg

  Consider the target configuration $\ell(2,2)$ in
  {numref}`11-fig:mwg,11-fig:nrg`.  Eve\'s winning region in the
  configuration reachability energy game is
  $W_\mathrm{Eve}=\{ \ell(n+2,n+2)\mid n\in\mathbb{N}\}$, displayed on the left in
  {numref}`11-fig:cov-nrg`.  In the coverability energy game, Eve\'s
  winning region is
  $W_\mathrm{Eve}=\{ \ell(m+2,n+2), \ell'(m+3,n+2)\mid m,n\in\mathbb{N}\}$ displayed on
  the right in {numref}`11-fig:cov-nrg`.

````

```{figure} ./../FigAndAlgos/11-fig:cov-nrg.png
:name: 11-fig:cov-nrg
:align: center
The winning regions of Eve in the
    configuration reachability energy game (left) and the
    coverability energy game
    (right) on the graphs of {numref}`11-fig:mwg,11-fig:nrg` with target
    configuration $\ell(2,2)$.  The winning vertices are in filled in
    green, while the losing ones are filled with white with a red
    border; the sink is always losing.
```

The reader might have noticed that the natural semantics of the
asymmetric system of {numref}`11-fig:avg` and the energy semantics of
the system of {numref}`11-fig:mwg` are essentially the same.  This
correspondence is quite general.

````{prf:lemma} Energy vs.\ asymmetric vector games
:label: 11-lem:nrg

  Energy games and asymmetric vector games are
  \logspace-equivalent for configuration reachability,
  coverability, non-termination, and parity,
  both with given and with existential initial credit.

````

````{admonition} Proof
:class: dropdown tip

  Let us first reduce asymmetric vector games to energy games.
  Given $\mathcal{V}$, $\mathfrak{c}$, and $\Omega$ where $\mathcal{V}$ is asymmetric and
  $\textrm{Eve}$ loses if the play ever visits the sink $\bot$, we see that
  $\textrm{Eve}$ wins $(  \mathcal{A}_\mathbb{N}(\mathcal{V}), \mathfrak{c},\Omega)$ from some $v\in V$ if and
  only if she wins $(  \mathcal{A}_\mathbb{E}(\mathcal{V}), \mathfrak{c},\Omega)$ from $v$.  Of course,
  this might not be true if $\mathcal{V}$ is not asymmetric, as seen for
  instance in {prf:ref}`11-ex:cov` and {prf:ref}`11-ex:cov-nrg`.

 Conversely, let us reduce energy games to asymmetric
  vector games.  Consider
  $\mathcal{V}=( \mathcal{L}, A, \mathcal{L}_\mathrm{Eve}, \mathcal{L}_\mathrm{Adam}, k)$, a colouring $\mathfrak{c}$
  defined from a vertex colouring $\mathrm{vcol}$ by
  $\mathfrak{c}(e)  \stackrel{\!\,\!\,\textrm{def}}{=} \mathrm{vcol}( \textrm{In}(e))$, and an objective $\Omega$, where
  $\mathrm{vcol}$ and $\Omega$ are such that $\textrm{Eve}$ loses if the play ever
  visits the sink $\bot$ and such that, for all $\pi\in C^\ast$,
  $p\in C$, and $\pi'\in C^\omega$, $\pi p\pi'\in\Omega$ if and only
  if $\pi pp\pi'\in\Omega$ (we shall call $\Omega$
  **stutter-invariant**, and the objectives in the statement are
  indeed stutter-invariant).  We construct an asymmetric vector
  system
  $\mathcal{V}'  \stackrel{\!\,\!\,\textrm{def}}{=}( \mathcal{L}\uplus \mathcal{L}_A, A', \mathcal{L}_\mathrm{Eve}\uplus \mathcal{L}_A, \mathcal{L}_\mathrm{Adam}, k)$
  where we add the following locations controlled by Eve:
    
$$

       \mathcal{L}_A&  \stackrel{\!\,\!\,\textrm{def}}{=}\{ \ell_a\mid a=( \ell \xrightarrow{\,\vec
                 u,} \ell')\in A\text{ and } \ell\in \mathcal{L}_\mathrm{Adam}\}\;.
      \intertext{We also modify the set of actions:}
       A'&  \stackrel{\!\,\!\,\textrm{def}}{=}\{ \ell \xrightarrow{\,\vec u,} \ell'\mid  \ell \xrightarrow{\,\vec
             u,} \ell'\in A\text{ and } \ell\in \mathcal{L}_\mathrm{Eve}\}\\
      &\:\cup\:\{ \ell \xrightarrow{\,\vec 0,} \ell_a,\; \ell_a \xrightarrow{\,\vec u,} \ell'\mid a=( \ell \xrightarrow{\,\vec u,} \ell')\in A\text{ and } \ell\in \mathcal{L}_\mathrm{Adam}\}\;.
    
$$

    {numref}`11-fig:avg` presents the result of this reduction on the
    system of {numref}`11-fig:mwg`.  We define a vertex colouring
    $\mathrm{vcol}'$ of $\mathcal{A}_\mathbb{N}(\mathcal{V}')$ with $\mathrm{vcol}'(v)  \stackrel{\!\,\!\,\textrm{def}}{=} \mathrm{vcol}(v)$ for
    all $v\in  \mathcal{L}\times\mathbb{N}^ k\uplus\{ \bot\}$ and
    $\mathrm{vcol}'( \ell_a(\vec v))  \stackrel{\!\,\!\,\textrm{def}}{=} \mathrm{vcol}( \ell(\vec v))$ if
    $a=( \ell \xrightarrow{\,\vec u,} \ell')\in A$.  Then, for all vertices
    $v\in V$, Eve wins from $v$ in the energy game
    $(  \mathcal{A}_\mathbb{E}(\mathcal{V}), \mathfrak{c},\Omega)$ if and only if she wins from $v$ in
    the vector game $(  \mathcal{A}_\mathbb{N}(\mathcal{V}'), \mathfrak{c}',\Omega)$.  The crux of
    the argument is that, in a configuration $\ell(\vec v)$ where
    $\ell\in \mathcal{L}_\mathrm{Adam}$, if $a=( \ell \xrightarrow{\,\vec u,} \ell')\in A$ is an
    action with $\vec v+\vec u\not\geq\vec 0$, in the energy
    semantics, Adam can force the play into the sink by
    playing $a$; the same occurs in $\mathcal{V}'$ with the natural
    semantics, as Adam can now choose to play
    $\ell \xrightarrow{\,\vec 0,} \ell_a$ where Eve has only
    $\ell_a \xrightarrow{\,\vec u,} \ell'$ at her disposal, which leads to the
    sink.\todoquestion{Is that clear?}

````

In turn, energy games with existential initial credit are related
to the multi-dimensional mean-payoff games of
Chapter {ref}`12-chap:multiobjective`.

(11-sec:bounding)=
## Bounded Semantics

While Adam wins immediately in an energy game if a resource gets
depleted, he also wins in a bounding game if a resource reaches a
certain bound $B$.  
This is
a **hard upper bound**, allowing to model systems where exceeding a
capacity results in failure, like a dam that overflows and floods the
area.  We define for a bound $B\in\mathbb{N}$ the bounded semantics
$\mathcal{A}_B(\mathcal{V})=(V^B,E^B, V_\mathrm{Eve}^B, V_\mathrm{Adam}^B)$ of a vector system $\mathcal{V}$ by

$$

  V^B&  \stackrel{\!\,\!\,\textrm{def}}{=}\{ \ell(\vec v)\mid \ell\in \mathcal{L}\text{ and }\|\vec v\|<B\}\;,\\
  E^B&  \stackrel{\!\,\!\,\textrm{def}}{=} \{( \ell(\vec v), \ell'(\vec v+\vec u))\mid \ell \xrightarrow{\,\vec
       u,} \ell'\in A,\vec v+\vec u\geq\vec 0,\text{ and }\|\vec
       v+\vec u\|<B\}\\
     &\:\cup\:\{( \ell(\vec v), \bot)\mid\forall \ell \xrightarrow{\,\vec
               u,} \ell'\in A\mathbin.\vec v+\vec u\not\geq\vec
               0\text{ or }\|\vec v+\vec u\|\geq B\}
     \cup\{( \bot, \bot)\}\;.

$$

As usual, $V_\mathrm{Eve}^B  \stackrel{\!\,\!\,\textrm{def}}{=} V^B\cap \mathcal{L}_\mathrm{Eve}\times\mathbb{N}^ k$ and
$V_\mathrm{Adam}^B  \stackrel{\!\,\!\,\textrm{def}}{=} V^B\cap \mathcal{L}_\mathrm{Adam}\times\mathbb{N}^ k$.  Any edge from the
energy semantics that would bring to a configuration $\ell(\vec v)$
with $\vec v(i)\geq B$ for some $1\leq i\leq k$ leads instead to the
sink.  All the configurations in this arena have norm less than $B$,
thus $|V^B|=| \mathcal{L}| B^ k+1$, and the qualitative games of
Chapter {ref}`2-chap:regular` are decidable over this arena.

Our focus here is on non-termination games played on the bounded
semantics where $B$ is not given as part of the input, but quantified
existentially.  As usual, the existential initial credit variant
of [Problem](11-pb:bounding) is obtained by quantifying $\vec v_0$
existentially in the question.
```{admonition} Problem (bounding game with given initial credit)
:name: 11-pb:bounding
**INPUT**:  A vector system
  $\mathcal{V}=( \mathcal{L}, A, \mathcal{L}_\mathrm{Eve}, \mathcal{L}_\mathrm{Adam}, k)$, an initial location
  $\ell_0\in \mathcal{L}$, and an initial credit $\vec v_0\in\mathbb{N}^ k$.

**QUESTION**: Does there exist $B\in\mathbb{N}$ such that Eve has a strategy to avoid the
  sink $\bot$ from $\ell_0(\vec v_0)$ in the bounded
  semantics?  That is, does there exist $B\in\mathbb{N}$ such that she wins
  the bounding game $(  \mathcal{A}_B(\mathcal{V}), \mathfrak{c}, \mathtt{Safe})$ from
  $\ell_0(\vec v_0)$, where $\mathfrak{c}(e)  \stackrel{\!\,\!\,\textrm{def}}{=} \textrm{Lose}$ if and only if $\textrm{In}(e)= \bot$?
```

````{prf:lemma} NEEDS TITLE 11-lem:parity2bounding
:label: 11-lem:parity2bounding

  There is a \logspace\ reduction from parity
  asymmetric vector games to bounding games, both with given
  and with existential initial credit.

````

````{admonition} Proof
:class: dropdown tip

  Given an asymmetric vector system
  $\mathcal{V}=( \mathcal{L}, A, \mathcal{L}_\mathrm{Eve}, \mathcal{L}_\mathrm{Adam}, k)$, a location colouring
  $\mathrm{lcol}{:}\, \mathcal{L}\to\{1,\dots,2d\}$, and an initial location
  $\ell_0\in \mathcal{L}$, we construct a vector system $\mathcal{V}'$ of dimension
  $k'  \stackrel{\!\,\!\,\textrm{def}}{=} k+d$ as described in {numref}`11-fig:bounding`, where the
  priorities in $\mathcal{V}$ for $p\in\{1,\dots,d\}$ are indicated above the
  corresponding locations.

```{figure} ./../FigAndAlgos/11-fig:bounding.png
:name: 11-fig:bounding
:align: center
Schema of the reduction to
      bounding games in the proof of {prf:ref}`11-lem:parity2bounding`.
```
  
  If Eve wins the bounding game played over $\mathcal{V}'$ from some
  configuration $\ell_0(\vec v_0)$, then she also wins the parity
  vector game played over $\mathcal{V}$ from the configuration $\ell_0(\vec
  v'_0)$ where $\vec v'_0$ is the projection of $\vec v_0$
  to $\mathbb{N}^ k$.  Indeed, she can play essentially the same strategy:
  by {prf:ref}`11-lem:mono` she can simply ignore the new decrement
  self loops, while the actions on the components in
  $\{ k+1,\dots, k+d\}$ ensure that the maximal priority visited
  infinitely often is even---otherwise some decrement $-\vec
  e_{ k+p}$ would be played infinitely often but the increment $\vec
  e_{ k+p}$ only finitely often.\todoquestion{Should I provide more details?}

  Conversely, consider the parity game $\mathcal{G}$ played over
  $\mathcal{A}_\mathbb{N}(\mathcal{V})$ with the colouring defined by $\mathrm{lcol}$.  Then the
  Pareto limit of the game is finite, thus there exists a natural
  number
  
$$

    B_0  \stackrel{\!\,\!\,\textrm{def}}{=} 1+\max_{ \ell_0(\vec v_0)\in\mathsf{Pareto}(\mathcal{G})}\|\vec
  v_0\|
  
$$ (11-eq:b0)
 bounding the norms of the minimal winning configurations.
  For a vector $\vec v$ in $\mathbb{N}^ k$, let us write $\capp[B_0]v$ for
  the vector capped at $B$: for all $1\leq i\leq k$,
  $\capp[B_0]v(i)  \stackrel{\!\,\!\,\textrm{def}}{=}\vec v(i)$ if $\vec v(i)<B_0$ and
  $\capp[B_0]v  \stackrel{\!\,\!\,\textrm{def}}{=} B_0$ if $\vec v(i)\geq B_0$.

  Consider now some configuration $\ell_0(\vec
  v_0)\in\mathsf{Pareto}( \mathcal{G})$.  As seen in {prf:ref}`11-lem:finmem`,
  since $\ell_0(\vec v_0)\in W_\mathrm{Eve}( \mathcal{G})$, there is a finite
  self-covering tree witnessing the fact, and an associated winning
  strategy.  Let $H( \ell_0(\vec v_0))$ denote the height of this
  self-covering tree and observe that all the configurations in this
  tree have norm bounded by $\|\vec v_0\|+\| A\|\cdot H( \ell_0(\vec
  v_0))$.
  Let us define
  
$$

   B  \stackrel{\!\,\!\,\textrm{def}}{=} B_0+(\| A\|+1)\cdot \max_{ \ell_0(\vec
  v_0)\in\mathsf{Pareto}(\mathcal{G})}H( \ell_0(\vec v_0))\;.
  
$$ (11-eq:b)

  This is a bound on the norm of the configurations appearing on the
  (finitely many) self-covering trees spawned by the elements
  of $\mathsf{Pareto}( \mathcal{G})$.  Note that $B\geq B_0+(\| A\|+1)$ since
  a self-covering tree has height at least one.

  Consider the non-termination game
  $\mathcal{G}_B  \stackrel{\!\,\!\,\textrm{def}}{=}(  \mathcal{A}_B(\mathcal{V}'), \mathfrak{c}', \mathtt{Safe})$ played over the
  bounded semantics defined by $B$, where $\mathfrak{c}'(e)= \textrm{Lose}$ if and
  only if $\textrm{In}(e)= \bot$.  Let $\vec b  \stackrel{\!\,\!\,\textrm{def}}{=}\sum_{1\leq p\leq
  d}(B-1)\cdot\vec e_{ k+p}$.
  {\renewcommand{ }{}
  \begin{claim}\label{11-cl:parity2bounding} If $\ell_0(\vec
    v)\in W_\mathrm{Eve}( \mathcal{G})$, then
    $\ell_0(\capp[B_0]{v}+\vec b)\in W_\mathrm{Eve}( \mathcal{G}_B)$.
  \end{claim}}
  Indeed, by definition of the Pareto
  limit $\mathsf{Pareto}( \mathcal{G})$, if $\ell_0(\vec v)\in W_\mathrm{Eve}( \mathcal{G})$,
  then there exists $\vec v_0\leq\vec v$ such that $\ell_0(\vec
  v_0)\in\mathsf{Pareto}( \mathcal{G})$.  By definition of the bound $B_0$,
  $\|\vec v_0\|<B_0$, thus $\vec v_0\leq\capp[B_0]v$.  Consider the
  self-covering tree of height $H( \ell_0(\vec v_0))$ associated
  to $\ell_0(\vec v_0)$, and the strategy $\sigma'$ defined by the
  memory structure from the
  proof of {prf:ref}`11-lem:finmem`.  This is a winning strategy for Eve 
  in $\mathcal{G}$ starting from $\ell_0(\vec v_0)$, and
  by {prf:ref}`11-lem:mono`, it is also winning
  from $\ell_0(\capp[B_0]v)$.
    
  Here is how Eve wins $\mathcal{G}_B$ from $\ell_0(\capp[B_0]v+\vec b)$.
  She essentially follows the strategy $\sigma'$, with two
  modifications.  First, whenever $\sigma'$ goes to a return node
  $\ell(\vec v)$ instead of a leaf $\ell(\vec v')$---thus $\vec
  v\leq\vec v'$---, the next time Eve has the control, she uses the
  self loops to decrement the current configuration by $\vec v'-\vec
  v$.  This ensures that any play consistent with the modified
  strategy remains between zero and $B-1$ on the components
  in $\{1,\dots, k\}$.  (Note that if she never regains the control,
  the current vector never changes any more since $\mathcal{V}$ is
  asymmetric.)

  Second, whenever a play in $\mathcal{G}$ visits a location with even
  parity $2p$ for some $p$ in $\{1,\dots,d\}$, Eve has the opportunity
  to increase the coordinates in $\{ k+1,\dots, k+p\}$ in $\mathcal{G}_B$.
  She does so and increments until all these components reach $B-1$.
  This ensures that any play consistent with the modified strategy
  remains between zero and $B-1$ on the components
  in $\{ k+1,\dots, k+p\}$.  Indeed, $\sigma'$ guarantees that the
  longest sequence of moves before a play visits a location with
  maximal even priority is bounded by $H( \ell_0(\vec v_0))$, thus the
  decrements $-\vec e_{ k+p}$ introduced in $\mathcal{G}_B$ by the
  locations from $\mathcal{G}$ with odd parity $2p-1$ will never force the
  play to go negative.\todoquestion{Is that clear enough?}

````

The bound $B$ defined in {eq}`11-eq:b` in the previous proof is not
constructive, and possibly much larger than really required.
Nevertheless, one can sometimes show that an explicit $B$ suffices in
a bounding game.
A simple example is provided by the coverability asymmetric
vector games with existential initial credit arising from
{prf:ref}`11-rk:cov2parity`, i.e., where the objective is to reach some
location $\ell_f$.  Indeed, it is rather straightforward that there
exists a suitable initial credit such that Eve wins the game if and
only if she wins the finite reachability game played over the
underlying directed graph over $\mathcal{L}$ where we ignore the counters.
Thus, for an initial location $\ell_0$, $B_0=| \mathcal{L}|\cdot\| A\|+1$
bounds the norm of the necessary initial credit, while a simple path
may visit at most $| \mathcal{L}|$ locations, thus
$B=B_0+| \mathcal{L}|\cdot\| A\|$ suffices for Eve to win the constructed
bounding game.

In the general case of bounding games with existential initial
credit, an explicit bound can be established.  The proof goes
along very different lines and is too involved to fit in this chapter,
but we refer the reader
to {cite}`Jurdzinski&Lazic&Schmitz:2015,Colcombet&Jurdzinski&Lazic&Schmitz:2017`
for details.

````{prf:theorem} Bounds on bounding
:label: 11-th:bounding

  If Eve wins a bounding game with existential initial credit
  defined by a vector
  system $\mathcal{V}=( \mathcal{L}, A, \mathcal{L}_\mathrm{Eve}, \mathcal{L}_\mathrm{Adam}, k)$, then an
  initial credit $\vec v_0$ with $\|\vec
  v_0\|=(4| \mathcal{L}|\cdot\| A\|)^{2( k+2)^3}$ and a bound
  $B=2(4| \mathcal{L}|\cdot\| A\|)^{2( k+2)^3}+1$ suffice for this.

````

{prf:ref}`11-th:bounding` also yields a way of handling bounding games
with given initial credit.  
\TODO{Last missing bit regarding complexity upper bounds.}

