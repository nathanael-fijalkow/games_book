(9-sec:notations)=
# Notations

```{math}

```

We fix a finite set $\mathcal{C}$ of clock variables to be used
in our timed games. Elements of $\mathbb{R}_{\geq 0}^ \mathcal{C}$, which assign a
value to each clock, are called **valuations**.

Clocks will be used to define **clock constraints**, which in turn
are used in timed automata to restrict the set of allowed behaviours:
edges are decorated with clock constraints defining conditions for
their availability.

An **atomic clock constraint** is a formula of the form $k \preceq
x \preceq' l$ or $k \preceq x - y \preceq' l$ where $x,y \in  \mathcal{C}$,
$k,l \in \mathbb{Z}\cup\{-\infty,\infty\}$ and
${\mathord\preceq,\mathord\preceq' \in
  \{\mathord<,\mathord\leq\}}$. A **clock constraint** is a
conjunction of atomic clock constraints.  A valuation $\nu\colon
 \mathcal{C}\to \mathbb{R}_{\geq 0}$ satisfies a clock constraint $g$, denoted $\nu \models g$,
if all atomic clock constraints are satisfied when each $x\in  \mathcal{C}$
is replaced with its value $\nu(x)$.  We write $\Phi_\mathcal{C}$ for the
set of clock constraints built on the clock set $\mathcal{C}$.

For a subset $R\subseteq  \mathcal{C}$ and a valuation $\nu$, we denote
with ${\nu[R \leftarrow 0]}$ the valuation defined by ${\nu[R
    \leftarrow 0](x) = 0}$ if $x \in R$ and ${\nu[R\leftarrow 0](x) =
  \nu(x)}$ otherwise. Given $d \in \mathbb{R}_{\geq 0}$ and a
valuation $\nu$, the valuation $\nu+d$ is defined by $(\nu+d)(x) =
\nu(x)+d$ for all $x\in  \mathcal{C}$. We extend these operations to sets
of valuations in the obvious way.

We now formally define **timed games**, which are finite
representations that define infinite-state, non-stochastic concurrent
games.

````{prf:definition} NEEDS TITLE AND LABEL 
  A **timed arena** $\mathcal{T}$ is a tuple $( \mathcal{L},
   \mathcal{C}, E_{ \textrm{Eve}}, E_{ \textrm{Adam}}, c)$, where $\mathcal{L}$ is a finite set of locations,
  $\mathcal{C}$ is a finite set of clocks, $E_{ \textrm{Eve}}, E_{ \textrm{Adam}} \subseteq  \mathcal{L} \times
  \Phi_\mathcal{C} \times 2^ \mathcal{C} \times \mathcal{L}$ are the sets of
  edges respectively controlled by Eve and  \textrm{Adam},

  and $c\colon  E_{ \textrm{Eve}}\cup E_{ \textrm{Adam}} \to C$ is the coloring function.

  A **timed game** is a pair $( \mathcal{T},\Omega)$ where
  $\Omega \subseteq C^\omega$ a qualitative objective.

  A **timed arena** $\mathcal{T}$ is a tuple $( \mathcal{L},
   \mathcal{C}, E_{ \textrm{Eve}}, E_{ \textrm{Adam}}, c)$, where $\mathcal{L}$ is a finite set of locations,
  $\mathcal{C}$ is a finite set of clocks, $E_{ \textrm{Eve}}, E_{ \textrm{Adam}} \subseteq  \mathcal{L} \times
  \Phi_\mathcal{C} \times 2^ \mathcal{C} \times \mathcal{L}$ are the sets of
  edges respectively controlled by Eve and  \textrm{Adam},

  and $c\colon  E_{ \textrm{Eve}}\cup E_{ \textrm{Adam}} \to C$ is the coloring function.

  A **timed game** is a pair $( \mathcal{T},\Omega)$ where
  $\Omega \subseteq C^\omega$ a qualitative objective.

````

A configuration of such a timed automaton is a pair $(\ell,\nu)$ where
$\ell\in \mathcal{L}$ and $\nu\colon  \mathcal{C}\to \mathbb{R}_{\geq 0}$.  The set of
configurations is the set of vertices of the infinite-state game
defined by $\mathcal{T}$.

The actions of both players are pairs $(d,e)$ where $d\in \mathbb{R}_{\geq 0}$ is a
delay they want to wait before playing their controlled
action $e$. Action $(d,e)$ is available for Eve (resp. Adam) in
configuration $(\ell,\nu)$ if $e\in E_{ \textrm{Eve}}(\ell)$ (resp. $e\in E_{ \textrm{Adam}}(\ell)$)
and, writing $e=(\ell,g,R,\ell')$, if additionally $\nu+d\models g$;
in other terms, the clock constraint (called **guard** hereafter)
on $e$ must hold true under the clock valuation reached after elapsing
$d$ time units. We add an extra dummy action $\bot$ for the case where
some player has no available action (this action is only available if
no other actions are).

Once both players have selected an action available from
configuration $(\ell,\nu)$, the action $(d,e)$ with smallest delay is
performed (by breaking ties in favor of Adam), leading to configuration $(\ell',(\nu+d)[R\leftarrow 0])$:
this corresponds to letting $d$ time units elapse, thereby reaching
configuration $(\ell,\nu+d)$, and to following edge $e$ (which by
construction is available from $(\ell,\nu+d)$).  We define
$\mathsf{step}((\ell,\nu),(d,e))$ for the configuration
$(\ell',(\nu+d)[R\leftarrow 0])$ reached from $(\ell,\nu)$ by applying
action $(d,e)$.

This definition captures the concurrent nature of the interaction
between a controller (Eve) and its environment (Adam) in a real-time
system, since none of the players knows in advance how long the
opponent will want to wait before performing her transition.
The semantics of a timed arena $( \mathcal{L},  \mathcal{C}, E_{ \textrm{Eve}}, E_{ \textrm{Adam}})$ can then
formally be defined in terms of a concurrent arena (following the
definition of Section {ref}`8-sec:notations`).  The underlying
graph $(V,E)$ is such that $V= \mathcal{L}\times  \mathbb{R}_{\geq 0}^{ \mathcal{C}}$, and $E=
V\times C\times V$; the set of actions of Eve is $\mathbb{R}_{\geq 0}\times E_{ \textrm{Eve}}$, and that
of Adam is $\mathbb{R}_{\geq 0}\times E_{ \textrm{Adam}}$; finally, the transition function,
which is not stochastic in our case, maps any
configuration $(\ell,\nu)$ and pair of actions $(d_\textrm{Eve},e_\textrm{Eve})$ and
$(d_\textrm{Adam},e_\textrm{Adam})$ to the edge $((\ell,\nu),\gamma,
 \mathsf{step}((\ell,\nu),(d,e)))$, where $(d,e)=(d_\textrm{Eve},e_\textrm{Eve})$ and $\gamma=c(e_\mathrm{Eve})$
if
$d_\textrm{Eve}<d_\textrm{Adam}$,  and $(d,a)=(d_\textrm{Adam},e_\textrm{Adam})$ and $\gamma=c(e_\mathrm{Adam})$ otherwise.

A path in a timed arena $\mathcal{T}$ then is a path in its
associated infinite-state concurrent arena. The qualitative
objective $\Omega$ can then be evaluated along runs of a timed arena in
the natural way.

Contrary to Chapter {ref}`7-chap:concurrent`, in this chapter we only consider deterministic strategies

```{margin}
Adding randomization over the infinite sets of actions is beyond the scope of this chapter.
```

  As a result, timed games are not
determined, as illustrated in the following example.

```{figure} ./../FigAndAlgos/9-fig:ta2.png
:name: 9-fig:ta2
:align: center
Timed arena $\mathcal{A}_2$. Solid arrow is Eve's, dashed one is Adam's.
```

````{prf:example} NEEDS LABEL Timed Games are not Determined

  In the timed arena $\mathcal{A}_2$ defined in {numref}`9-fig:ta2`, from configuration $(\ell_0,\vec{0})$, Eve does not have a winning strategy to reach location $\ell_1$, but Adam does not have a winning strategy either to avoid $\ell_1$.
  In fact, available moves for both players consist in $(d,(\ell_0,\ell_1))$ with $0< d<1$ for Eve, and $(d',(\ell_0,\ell_2))$ with $0< d' < 1$ for  \textrm{Adam}.
  Thus, for any particular delay $0<d<1$ chosen by  \textrm{Eve}, Adam has a possible delay $d<d'<1$ which leads to $\ell_2$, which is losing for  \textrm{Eve}.
  This shows that Eve does not have a winning strategy.
  The argument is however symmetric, and Adam also does not have a winning strategy to avoid $\ell_1$.
  Timed games are thus non determined.

````

````{prf:example} NEEDS LABEL Winning strategy on running example

Let us consider again the example of {numref}`9-fig:ta1` and see whether Eve
has a winning strategy from the initial configuration.
At the initial configuration $\ell_1,x=0$, Eve needs to make a move towards $\ell_2$
while $x\leq 1$ since whenever $x>1$, Adam can move to $\ell_5$ which guarantees Eve's lost.
Assume the game proceeds to $\ell_2$ with any value $x\leq 1$. Here, Eve can try to wait
until $x\geq 2$ and go to $G$. However, if $x<1$, then Adam can move to $\ell_3$.
From this location, Eve can guarantee to come back to $\ell_2$ with $x=1$, and then move to $G$ and win the game.
Assume now that from $\ell_1$, the game proceeds to $\ell_3$ with $x=0$ due to Adam's move.
Again, Eve can wait for 1 time unit, and go back to $\ell_2$ with $x=1$, and win the game.

Hence, Eve has a winning strategy from $\ell_1$ for all $x\leq 1$, and from $\ell_2$
for all values of $x$.

````

In this chapter, the main problem we are interested in is determining
whether Eve has a strategy for her reachability objective.
Let $\vec{0}$ denote the clock valuation assigning $0$ to all clocks.

\decpb{Solving a timed reachability game}{A timed arena $\mathcal{T}$, initial location $\ell_0$, and a reachability objective $\mathtt{Reach}( \textrm{Win})$}{Does Eve has a winning strategy in $( \mathcal{T}, \mathtt{Reach}( \textrm{Win}))$ from configuration $(\ell_0,\vec{0})$.}

The difficulty of this problem is that the concurrent
game $((V,E),\Delta,\Omega)$ has an infinite state-space, and players
have infinitely many actions.  We thus start by studying a data
structure to represent sets of states and operations to compute
successors and predecessors on these sets.  We then give two
algorithms to solve the above problem.  We also show how such a
strategy for Eve can be computed and finitely represented.
