(11-sec:counters)=
# Vector games


```{math}
\newcommand{\eqdef}{\eqby{def}}
\newcommand{\Loc}{\?L}
\newcommand{\Act}{A}
\newcommand{\weight}{w}
\newcommand{\loc}{\ell}
\newcommand{\sink}{\bot}
\newcommand{\dd}{k}
\newcommand{\lcol}{\mathrm{lcol}}
\newcommand{\Eve}{\textrm{Eve}}
\newcommand{\Adam}{\textrm{Adam}}
\newcommand{\game}{\mathcal{G}}
\newcommand{\col}{\textsf{col}}
\newcommand{\mEve}{\mathrm{Eve}}
\newcommand{\mAdam}{\mathrm{Adam}}
\newcommand{\VE}{V_\mEve}
\newcommand{\VA}{V_\mAdam}
\newcommand{\ing}{\textrm{In}}
\newcommand{\out}{\textrm{Out}}
\newcommand{\dest}{\Delta}
\newcommand{\WE}{W_\mEve}
\newcommand{\Win}{\textrm{Win}}
\newcommand{\Lose}{\textrm{Lose}}
\newcommand{\Safe}{\mathtt{Safe}}
\newcommand{\Reach}{\mathtt{Reach}}
\newcommand{\Parity}{\mathtt{Parity}}
```

\AP A vector system is a finite directed graph with a partition of
the vertices and weighted edges.  Formally, it is a tuple
$\?V=(\?LA\Loc_\mathrm{Eve}\Loc_\mathrm{Adam}k$ where $kin\+N$ is a
dimension, $\?L is a finite set of locations partitioned into the
locations controlled by \textrm{Eve} and \textrm{Adam} i.e.,
$\?L\Loc_\mathrm{Eve}uplus \Loc_\mathrm{Adam}, and
$Asubseteq \?Ltimes\+Z^ktimes\?L is a finite set of
weighted actions.  We write $\ellstep{\vec u}\ell$
rather than $(\ell\vec u,\ell)$ for actions in $A.  A
vector addition system with states is a vector system where
$\Loc_\mathrm{Adam}\emptyset$, i.e., it corresponds to the one-player case.

````{prf:example} vector system
:label: 11-ex:mwg

  {numref}`11-fig:mwg` presents a vector system of
  dimension two with locations $\{\ell\ell\}$ where $\ell is
  controlled by \textrm{Eve} and $\ell$ by \textrm{Adam}
  

````

```{figure} ./../FigAndAlgos/11-fig:mwg.png
:name: 11-fig:mwg
:align: center
A vector system.
```

The intuition behind a vector system is that it
maintains $k counters $\mathtt{c}_1,\dots,\mathtt{c}_k assigned
to integer values.  An action $\ellstep{\vec u}\ell\inA then
updates each counter by adding the corresponding entry of $\vec u$,
that is for all $1\leq j\leqk, the action performs the update
$\mathtt{c}_j := \mathtt{c}_j+\vec u(j)$.

\medskip \AP Before we proceed any further, let us fix some notations
for vectors in $\+Z^k.  We write `$\vec 0$' for the zero vector
with $\vec 0(j)\eqby{def}0$ for all $1\leq j\leqk.  For all
$1\leq j\leqk, we write `$\vec e_j$' for the unit vector with
$\vec e_j(j)\eqby{def}1$ and $\vec e_{j}(j')\eqby{def}0$ for all $j'\neq j$.
Addition and comparison are defined componentwise, so that for
instance $\vec u\leq\vec u'$ if and only if for all $1\leq j\leqk,
$\vec u(j)\leq\vec u'(j)$.  We write
$w\ellstep{\vec u}\ell)\eqby{def}vec u$ for the weight of an
action and $w\pi)\eqby{def}sum_{1\leq j\leq |\pi|}w\pi_j)$
for the cumulative weight of a finite sequence of actions
$\pi\inA\ast$.  For a vector $\vec u\in\+Z^k, we use its
infinity norm $\|\vec u\|\eqby{def}max_{1\leq j\leqk|\vec u(j)|$,
hence $\|\vec 0\|=0$ and $\|\vec e_j\|=\|-\vec e_j\|=1$, and we let
$\|\ellstep{\vec u}\ell\|\eqby{def}|w\ellstep{\vec
  u}\ell)\|=\|\vec u\|$
and $\|A|\eqby{def}max_{a\inA\|wa)\|$.  Unless stated
otherwise, we assume that all our vectors are represented in binary,
hence $\|A|$ may be exponential in the size of $\?V$.

## Arenas and Games

\AP A vector system gives rise to an infinite graph
$G_\+N\eqby{def}V,E)$ over the set of vertices
$V\eqby{def}\?Ltimes\+N^k\uplus\{\bot}$.  The vertices of the
graph are either **configurations** $\ell\vec v)$ consisting of a
location $\ellin \?L and a vector of non-negative integers
$\vec v\in\+N^k---such a vector represents a valuation of the
counters $\mathtt{c}_1,\dots,\mathtt c_k---, or the
sink $\bot.

\AP Consider an action in $a=(\ellstep{\vec u}\ell)$ in $A: we
see it as a partial function
$a{:}\,\?Ltimes\+N^k,\pto \?Ltimes\+N^k with domain
$\dom a\eqby{def}{\ell\vec v)\mid \vec v+\vec u\geq\vec 0\}$ and image
$a(\ell\vec v))\eqby{def}\ell(\vec v+\vec u)$; let also
$\domAeqby{def}bigcup_{a\inA\dom a$.  This allows us to define
the set $E$ of edges as a set of pairs
\begin{align*}
  E&\eqby{def}{(\ell\vec v),a(\ell\vec v)))\mid a\inAtext{ and
     }\ell\vec v)\in\dom a\}\\%\ell(\vec v+\vec u))\mid
                               
  &\:\cup\:\{(\ell\vec v),\bot\mid\ell\vec v)\not\in\domA}\cup\{(\bot\bot\}\;,
\end{align*}
where $\textrm{In}(v,v'))\eqby{def}v$ and $\textrm{Out}(v,v'))\eqby{def}v'$ for all
edges $(v,v')\in E$.  There is therefore an edge $(v,v')$ between two
configurations $v=\ell\vec v)$ and $v'=\ell(\vec v')$ if there
exists an action $\ellstep{\vec u}\ell\inA such that
$\vec v'=\vec v+\vec u$.  Note that, quite importantly,
$\vec v+\vec u$ must be non-negative on every coordinate for this edge
to exist.  If no action can be applied, there is an edge to the
sink $\bot, which ensures that $E$ is total: for all $v\in V$,
there exists an edge $(v,v')\in E$ for some $v'$, and thus there are
no `deadlocks' in the graph.

The configurations are naturally partitioned into those in
$V_\mEveeqby{def}Loc_\mathrm{Eve}times\+N^k controlled by~\textrm{Eve} and those in
$V_\mAdameqby{def}Loc_\mathrm{Adam}times\+N^k controlled by~\textrm{Adam}  Regarding
the sink, the only edge starting from $\bot loops back
to it, and it does not matter who of \textrm{Eve} or \textrm{Adam} controls it.  This
gives rise to an infinite arena $\arena_\+N\eqby{def}G_\+N,V_\mEveV_\mathrm{Adam} called
the natural semantics of $\?V$.

\medskip Although we work in a turn-based setting with perfect
information, it is sometimes enlightening to consider the partial map
$\Delta:}\,V\times A\pto E$ defined by
$\Delta\ell\vec v),a)\eqby{def}\ell\vec v),a(\ell\vec v)))$ if
$\ell\vec v)\in\dom a$ and
$\Delta\ell\vec v),a)\eqby{def}\ell\vec v),\bot$ if
$\ell\vec v)\not\in\domA.  Note that a sequence $\pi$ over $E$
that avoids the sink can also be described by an initial
configuration $\loc_0(\vec v_0)$ paired with a sequence
over $A.
% will rather use a vertex colouring $\textsf{col}:}\,V\to C$ and allow it to


````{prf:example} NEEDS LABEL natural semantics
{11-ex:sem}
  {numref}`11-fig:sem` illustrates the natural semantics of the system
  of {numref}`11-fig:mwg`; observe that all the configurations $\ell0,n)$
  for $n\in\+N$ lead to the sink.

````


```{figure} ./../FigAndAlgos/11-fig:sem.png
:name: 11-fig:sem
:align: center
The natural semantics of the
    vector system of {numref}`11-fig:mwg`: a circle (resp.\
    a square) at position $(i,j)$ of the grid denotes a configuration
    $\elli,j)$ (resp.\ $\ell(i,j)$) controlled by~\textrm{Eve} (resp.\
    \textrm{Adam}.
```

%   semantics would use instead $\?Ltimes\+Z^k as set of vertices,

%   $\{(\ell\vec v),\ell(\vec v+\vec u))\mid \ellstep{\vec

%   as set of edges.  This eschews the need of a sink vertex since there

% \end{remark}

\AP A vector system $\?V=(\?LA\Loc_\mathrm{Eve}\Loc_\mathrm{Adam}k$, a
colouring $\textsf{col}:}\,E\to C$, and an
objective $\Omega\subseteq C^\omega$ together define a vector game
$\mathcal{G}(\natural(\?V),\textsf{col}\Omega)$.  Because $\natural(\?V)$ is an
infinite arena, we need to impose restrictions on our colourings
$\textsf{col}:}\,E\to C$ and the "qualitative
objectives" $\Omega\subseteq C^\omega$; at the very least, they should
be recursive.

There are then two variants of the associated decision problem:

* \AP the given initial credit variant, where we are given $\?V$,
  $\textsf{col}, $\Omega$, a location $\loc_0\in\?L and an initial credit
  $\vec v_0\in\+N^k, and ask whether \textrm{Eve} wins $\mathcal{G} from the
  initial configuration $\loc_0(\vec v_0)$;
* \AP the existential initial credit variant, where we are given
  $\?V$, $\textsf{col}, $\Omega$, and a location $\loc_0\in\?L, and ask
  whether there exists an initial credit $\vec v_0\in\+N^k such
  that \textrm{Eve} wins $\mathcal{G} from the initial
  configuration $\loc_0(\vec v_0)$.


Let us instantiate the previous abstract definition of vector games.
We first consider two `reachability-like'
\index{reachability!**see also** vector game\protect\mymoot|mymoot}
objectives, where $C\eqby{def}{\varepsilon,\textrm{Win}}$ and
$\Omega\eqby{def}Reach$, namely configuration reachability and
coverability.  The difference between the two is that, in the
configuration reachability problem, a specific configuration
$\loc_f(\vec v_f)$ should be visited, whereas in the coverability
problem, \textrm{Eve} attempts to visit $\loc_f(\vec v')$ for some
vector $\vec v'$ componentwise larger or equal to
$\vec v_f$.

\decpb[configuration reachability vector game with given initial credit]
{\label{11-pb:

```{margin}
The name `coverability' comes from the the
  literature on Petri nets and "vector addition systems with
  states", because \textrm{Eve} is attempting to **cover**
  $\loc_f(\vec v_f)$, i.e., to reach a configuration $\loc_f(\vec v')$
  with $\vec v'\geq\vec v_f$.
```

reach} A vector system
  $\?V=(\?LA\Loc_\mathrm{Eve}\Loc_\mathrm{Adam}k$, an initial location
  $\loc_0\in\?L, an initial credit $\vec v_0\in\+N^k, and a
  target configuration $\loc_f(\vec v_f)\in\?Ltimes\+N^k.}
{Does \textrm{Eve} have a strategy to reach $\ell\vec v)$ from
  $\loc_0(\vec v_0)$?\\That is, does she win the configuration
  reachability game $(\natural(\?V),\textsf{col}\mathtt{Reach}$ from
  $\loc_0(\vec v_0)$, where $\textsf{col}e)= \textrm{Win} if and only if
  $\textrm{In}e)=\loc_f(\vec v_f)$?}

\decpb[coverability vector game with given initial credit]
{\label{11-pb:cov} A vector system
  $\?V=(\?LA\Loc_\mathrm{Eve}\Loc_\mathrm{Adam}k$, an initial location
  $\loc_0\in\?L, an initial credit $\vec v_0\in\+N^k, and a
  target configuration $\loc_f(\vec v_f)\in\?Ltimes\+N^k.}
{Does \textrm{Eve} have a strategy to reach $\ell\vec v')$ for some
  $\vec v'\geq\vec v_f$ from $\loc_0(\vec v_0)$?\\That is, does she win
  the coverability game $(\natural(\?V),\textsf{col}\mathtt{Reach}$ from
  $\loc_0(\vec v_0)$, where $\textsf{col}e)= \textrm{Win} if and only if
  $\textrm{In}e)=\loc_f(\vec v')$ for some $\vec v'\geq\vec v_f$?}

````{prf:example} Objectives
:label: 11-ex:cov

  Consider the target configuration $\ell2,2)$ in
  {numref}`11-fig:mwg,11-fig:sem`.  \textrm{Eve}s winning region in the
  configuration reachability vector game is
  $W_\mathrm{Eve}{\elln+1,n+1)\mid n\in\+N\}\cup\{\ell(0,1)\}$, displayed on the left
  in {numref}`11-fig:cov`.  \textrm{Eve} has indeed an obvious winning strategy
  from any configuration $\elln,n)$ with $n\geq 2$, which is to use
  the action $\ellstep{-1,-1}\ell until she reaches $\ell2,2)$.
  Furthermore, in $\ell(0,1)$---due to the natural semantics---,
  \textrm{Adam} has no choice but to use the action $\ell\step{2,1}\ell:
  therefore $\ell(0,1)$ and $\ell1,1)$ are also winning for \textrm{Eve}

```{figure} ./../FigAndAlgos/11-fig:cov.png
:name: 11-fig:cov
:align: center
The winning regions of \textrm{Eve} in the
    configuration reachability game (left) and the coverability game
    (right) on the graphs of {numref}`11-fig:mwg,11-fig:sem` with target
    configuration $\ell(2,2)$.  The winning vertices are in filled in
    green, while the losing ones are filled with white with a red
    border; the sink is always losing.
```

In the coverability vector game, \textrm{Eve}s winning region is
$W_\mathrm{Eve}{\ellm+2,n+2),\ell(m+2,n+2),\ell(0,n+1),\ell1,n+2),\ell(2m+2,1),\ell2m+3,1)\mid
m,n\in\+N\}$
displayed on the right in {numref}`11-fig:cov`.  Observe in particular
that \textrm{Adam} is forced to use the action $\ell'\step{2,1}\ell$ from
the configurations of the form $\ell(0,n+1)$, which brings him to a
configuration $\ell(2,n+2)$ coloured $\textrm{Win} in the game, and thus the
configurations of the form $\ell1,n+1)$ are also winning for \textrm{Eve}since she can play $\ellstep{-1,0}\ell$.  Thus the configurations of
the form $\ell2m+3,n+1)$ are also winning for \textrm{Eve} as she can play
the action $\ellstep{-1,0}\ell$ to a winning configuration
$\ell(2m+2,n+1)$ where all the actions available to \textrm{Adam} go into
her winning region.

````


````{admonition} Remark [Location reachability]
\label{11-rk:cov2cov}
  In both configuration reachability and coverability, we can
  assume without loss of generality that $\loc_f\in\Loc_\mathrm{Eve} is
  controlled by \textrm{Eve} and that $\vec v_f=\vec 0$ is the zero vector.
  Thus coverability is equivalent to **location reachability**.
  
  There is indeed a \logspace\ reduction to that case.  If
  $\loc_0(\vec v_0)=\loc_f(\vec v_f)$ in the case of "configuration
  reachability", or $\loc_0=\loc_f$ and $\vec v_0\geq\vec v_f$ in the
  case of coverability, the problem is trivial.
  
  Otherwise, any winning play must use at least one action.  For
  each incoming action $a=(\ellstep{\vec u}\loc_f)$ of $\loc_f$,
  create a new location $\loc_a$ controlled by \textrm{Eve} and replace $a$ by
  $\ellstep{\vec u}\loc_a\step{\vec 0}\loc_f$, so that \textrm{Eve} gains the
  control right before any play reaches $\loc_f$.  Also add a new
  location $\smiley$ controlled by \textrm{Eve} with actions
  $\loc_a\step{-\vec v_f}\smiley$, and use $\smiley(\vec 0)$ as target
  configuration.

````


````{admonition} Remark [Coverability to reachability]
\label{11-rk:cov2reach}
  There is a \logspace\ reduction from coverability to
  configuration reachability.  By \cref{11-rk:cov2cov}, we can assume
  without loss of generality that $\loc_f\in\Loc_\mathrm{Eve} is controlled
  by \textrm{Eve} and that $\vec v_f=\vec 0$ is the zero vector. It suffices
  therefore to add an action $\loc_f\step{-\vec e_j}\loc_f$ for
  all $1\leq j\leqk.

````

Departing from reachability games, the
following is a very simple kind of safety
games where $C\eqby{def}{\varepsilon,\textrm{Lose}}$ and $\Omega\eqby{def}Safe$;
{numref}`11-fig:nonterm` shows \textrm{Eve}s winning region in the case of the
graphs of {numref}`11-fig:mwg,11-fig:sem`.
\decpb[non-termination vector game with given initial credit]
{\label{11-pb:nonterm} A vector system
  $\?V=(\?LA\Loc_\mathrm{Eve}\Loc_\mathrm{Adam}k$, an initial location
  $\loc_0\in\?L, and an initial credit $\vec v_0\in\+N^k.}
{Does \textrm{Eve} have a strategy to avoid the sink $\bot from
  $\loc_0(\vec v_0)$?\\That is, does she win the non-termination
  game $(\natural(\?V),\textsf{col}\mathtt{Safe}$ from $\loc_0(\vec v_0)$, where
  $\textsf{col}e)=\textrm{Lose} if and only if $\textrm{In}e)=\bot?} 

  
```{figure} ./../FigAndAlgos/11-fig:nonterm.png
:name: 11-fig:nonterm
:align: center
The winning region of \textrm{Eve} in the
    non-termination game on the graphs of {numref}`11-fig:mwg,11-fig:sem`.
```

%   Consider the non-termination game on the graphs of

%   {numref}`11-fig:nonterm`

Finally, one of the most general vector games are "parity@parity
vector game" games, where $C\eqby{def}{1,\dots,d\}$ and
$\Omega\eqby{def}Parity$.  In order to define a colouring of the "natural
semantics", we assume that we are provided with a **location
  colouring** $\mathrm{lcol}:}\,\?Lto\{1,\dots,d\}$.
\decpb[parity vector game with given initial credit]
{\label{11-pb:parity}A vector system
  $\?V=(\?LA\Loc_\mathrm{Eve}\Loc_\mathrm{Adam}k$, an initial location
  $\loc_0\in\?L, an initial credit $\vec v_0\in\+N^k, and a
  location colouring $\mathrm{lcol}:}\,\?Lto\{1,\dots,d\}$ for some $d>0$.}
  {Does \textrm{Eve} have a strategy to simultaneously avoid the
  sink $\bot and fulfil the \index{parity!**see also** vector
  game\protect\mymoot|mymoot}parity objective from $\loc_0(\vec
  v_0)$?\\That is, does she win the parity@parity vector game game
  $(\natural(\?V),\textsf{col}\mathtt{Parity}$ from $\loc_0(\vec v_0)$, where
  $\textsf{col}e)\eqby{def}lcol(\ell$ if $\textrm{In}e)=\ell\vec v)$ for
  some $\vec v\in\+N^k, and $\textsf{col}e)\eqby{def}1$ if $\textrm{In}e)=\bot?}

````{admonition} Remark [Non termination to parity]
\label{11-rk:nonterm2parity}
  There is a \logspace\ reduction from non-termination to
  parity@parity vector game.
  Indeed, the two games coincide if we pick the constant location
  colouring defined by $\mathrm{lcol}\ell\eqby{def}2$ for all $\ellin\?L in
  the parity game.

````

````{admonition} Remark [Coverability to parity]
\label{11-rk:cov2parity}
  There is a \logspace\ reduction from coverability to
  parity@parity vector game.  Indeed, by \cref{11-rk:cov2cov}, we can assume
  that $\loc_f\in\Loc_\mathrm{Eve} is controlled by \textrm{Eve} and that the target
  credit is $\vec v_f=\vec 0$ the zero vector.  It suffices
  therefore to add an action $\loc_f\step{\vec 0}\loc_f$ and to colour
  every location $\ellneq\loc_f$ with $\mathrm{lcol}\ell\eqby{def}1$ and
  to set $\mathrm{lcol}\loc_f)\eqby{def}2$.

````

The existential initial credit variants of
\crefrange{11-pb:reach}{11-pb:parity} are defined similarly, where
$\vec v_0$ is not given as part of the input, but existentially
quantified in the question.

(11-sec:undec)=
## Undecidability
The bad news is that, although \crefrange{11-pb:reach}{11-pb:parity}
are all decidable in the one-player case---see
the \hyperref[11-sec:references]{bibliographic notes} at the end of the
chapter---, they become undecidable in the two-player setting.

````{prf:theorem} Undecidability of vector games
:label: 11-th:undec

  Configuration reachability, coverability, non-termination, and
  parity@parity vector game vector games, both with given and
  with existential initial credit, are undecidable in any dimension
  $kgeq 2$.

````

````{admonition} Proof
:class: dropdown tip

  By \cref{11-rk:cov2reach,11-rk:nonterm2parity}, it suffices to prove the
  undecidability of coverability and non-termination.  For this,
  we exhibit reductions from the halting problem of "deterministic
  Minsky machines" with at least two counters.

  \AP Formally, a deterministic Minsky machine with $k~counters
  $\?M=(\?LAk$ is defined similarly to a "vector addition
  system with states" with additional zero test actions
  $a=(\ellstep{i\eqby?0}\ell)$.  The set of locations contains a
  distinguished `halt' location $\loc_\mathtt{halt}$, and for every
  $\ellin\?L, exactly one of the following holds: either (i)
  $(\ellstep{\vec e_i}\ell)\inA for some $0<i\leqk and
  $\ell\in\?L, or (ii) $(\ellstep{i\eqby?0}\ell)\inA and
  $(\ellstep{-\vec e_i}\ell')\inA for some $0<i\leqk and
  $\ell,\ell'\in\?L, or (iii) $\ell\loc_\mathtt{halt}$.  The
  semantics of $\?M$ extends the natural semantics by
  handling zero tests actions $a=(\ellstep{i\eqby?0}\ell)$: we
  define the domain as $\dom a\eqby{def}{\ell\vec v)\mid \vec v(i)=0\}$
  and the image by $a(\ell\vec v))\eqby{def}\ell\vec v)$.  This
  semantics is deterministic, and from any starting vertex of $\natural(\?M)$,
  there is a unique play, which either eventually visits
  $\loc_\mathtt{halt}$ and then the sink in the next step, or keeps
  avoiding both $\loc_\mathtt{halt}$ and the sink
  indefinitely. 
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

  \AP The halting problem asks, given a deterministic Minsky machine
  and an initial location $\loc_0$, whether it halts, that is, whether
  $\loc_\mathtt{halt}(\vec v)$ is reachable for
  some $\vec v\in\+N^k starting from $\loc_0(\vec 0)$.  The
  halting problem is undecidable in any dimension
  $kgeq 2$ {cite}`Minsky:1967`.
  Thus the halting problem is akin to the coverability of
  $\loc_\mathtt{halt}(\vec 0)$ with given initial credit $\vec 0$,
  but on the one hand there is only one player and on the other hand
  the machine can perform zero tests.

  
```{figure} ./../FigAndAlgos/11-fig:undec.png
:name: 11-fig:undec
:align: center
Schema of the reduction in the proof of \cref{11-th:undec}.
```
  Here is now a reduction to
  \cref{11-pb:cov}.  Given an instance of the halting problem, i.e.,
  given a deterministic Minsky machine $\?M=(\?LAk$ and an
  initial location $\loc_0$, we construct a vector system
  $\?V\eqby{def}\?Luplus\Loc_{\eqby?0}\uplus\{\frownie\},A,\?L\Loc_{\eqby?0}\uplus\{\frownie\},k$
  where all the original locations are controlled by~\textrm{Eve} and
  $\Loc_{\eqby?0}\uplus\{\frownie\}$ is a set of new locations
  controlled by~\textrm{Adam}  We use $\Loc_{\eqby?0}$ as a set of
  locations defined by
  \begin{align*}
    \Loc_{\eqby?0}&\eqby{def}{\ell_{i\eqby?0}\mid\exists\ellin\?Lmathbin.(\ellstep{i\eqby?0}\ell)\inA}\intertext{and
                   define the set of actions by (see {numref}`11-fig:undec`)}
    A&\eqby{def}{\ellstep{\vec
          e_i}\ell\mid(\ellstep{\vec e_i}\ell)\inA}\cup\{\ellstep{-\vec e_i}\ell'\mid(\ellstep{-\vec e_i}\ell')\inA}\\
    &\:\cup\:\{\ellstep{\vec
      0}\ell_{i\eqby?0},\;\;\:\ell_{i\eqby?0}\!\!\step{\vec 0}\ell,\;\;\:\ell_{i\eqby?0}\!\!\step{-\vec e_i}\frownie\mid(\ellstep{i\eqby?0}\ell)\inA}\;.
  \end{align*}
  We use $\loc_0(\vec 0)$ as initial configuration and
  $\loc_\mathtt{halt}(\vec 0)$ as target configuration for the
  constructed coverability instance.  Here is the crux of the
  argument why \textrm{Eve} has a winning strategy to cover
  $\loc_\mathtt{halt}(\vec 0)$ from $\loc_0(\vec 0)$ if and only if
  the Minsky machine@deterministic Minsky machine halts.
  
  Consider any configuration $\ell\vec v)$.  If
  $(\ellstep{\vec e_i}\ell)\inA, \textrm{Eve} has no choice but to apply
  $\ellstep{\vec e_i}\ell$ and go to the configuration
  $\ell(\vec v+\vec e_i)$ also reached in one step in $\?M$.  If
  $\{\ellstep{i\eqby?0}\ell,\ellstep{-\vec e_i}\ell'\}\inA and
  $\vec v(i)=0$, due to the natural semantics, \textrm{Eve} cannot use the
  action $\ellstep{-\vec e_i}\ell'$, thus she must use
  $\ellstep{\vec 0}\ell_{i\eqby?0}$.  Still due to the "natural
  semantics", \textrm{Adam} cannot use
  $\ell_{i\eqby?0}\!\!\step{-\vec e_i}\frownie$, thus he must use
  $\ell_{i\eqby?0}\!\!\step{\vec 0}\ell$.  Hence \textrm{Eve} regains the
  control in $\ell(\vec v)$, which was also the configuration reached
  in one step in $\?M$.  Finally, if
  $\{\ellstep{i\eqby?0}\ell,\ellstep{-\vec e_i}\ell'\}\inA and
  $\vec v(i)>0$, \textrm{Eve} can choose: if she uses
  $\ellstep{-\vec e_i}\ell'$, she ends in the configuration
  $\ell'(\vec v-\vec e_i)$ also reached in one step in $\?M$.  In
  fact, she should not use $\ellstep{\vec 0}\ell_{i\eqby?0}$,
  because \textrm{Adam} would then have the opportunity to apply
  $\ell_{i\eqby?0}\!\!\step{-\vec e_i}\frownie$ and to win, as
  $\frownie$ is a deadlock location and all the subsequent moves end
  in the sink.  Thus, if $\?M$ halts, then \textrm{Eve} has a winning
  strategy that simply follows the unique play of $\?M$, and
  conversely, if \textrm{Eve} wins, then necessarily she had to follow the
  play of $\?M$ and thus the machine halts.
    
  \medskip Further note that, in a deterministic Minsky machine the
  halting problem is similarly akin to the **complement** of
  non-termination with given initial credit $\vec 0$.  This means
  that, in the vector system
  $\?V=(\?Luplus\Loc_{\eqby?0}\uplus\{\frownie\},A,\?L\Loc_{\eqby?0}\uplus\{\frownie\},k$
  defined earlier, \textrm{Eve} has a winning strategy to avoid the sink
  from $\loc_0(\vec 0)$ if and only if the given "Minsky
  machine@deterministic Minsky machine" does
  not halt from $\loc_0(\vec 0)$, which shows the undecidability of
  \cref{11-pb:nonterm}.

  \medskip Finally, let us observe that both the existential and the
  universal initial credit variants of the halting problem are also
  undecidable.  Indeed, given an instance of the halting problem,
  i.e., given a deterministic Minsky machine $\?M=(\?LAk$
  and an initial location $\loc_0$, we add $k~new locations
  $\loc_k\loc_{k1},\dots,\loc_1$ with respective actions
  $\loc_j\step{-\vec e_j}\loc_j$ and $\loc_j\step{j\eqby?0}\loc_{j-1}$
  for all $kgeq j>0$.  This modified machine first resets all its
  counters to zero before reaching $\loc_0(\vec 0)$ and then performs
  the same execution as the original machine.  Thus there exists an
  initial credit $\vec v$ such that the modified machine
  reaches $\loc_\mathtt{halt}$ from $\loc_k\vec v)$ if and only if
  for all initial credits $\vec v$ the modified machine
  reaches $\loc_\mathtt{halt}$ from $\loc_k\vec v)$, if and only if
  $\loc_\mathtt{halt}$ was reachable from $\loc_0(\vec 0)$ in the
  original machine.  The previous construction of a vector system
  applied to the modified machine then shows the undecidability of the
  existential initial credit variants of
  \cref{11-pb:cov,11-pb:nonterm}
  
  
  
  
  .

````


