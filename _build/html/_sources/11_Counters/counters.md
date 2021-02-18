(11-sec:counters)=
# Vector games

```{math}
\newcommand{\?}{\mathcal}
\newcommand{\+}{\mathbb}
\newcommand{\tup}[1]{\langle #1\rangle}
\newcommand{\eqby}[1]{\stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{#1}}}}{=}}
\newcommand{\eqdef}{\eqby{def}}
\newcommand{\Loc}{\?L}
\newcommand{\Act}{A}
\providecommand{\dom}{\mathrm{dom}\,}
\newcommand\pto{\mathrel{\ooalign{\hfil$\mapstochar\mkern5mu$\hfil\cr$\to$\cr}}}
\newcommand{\weight}{w}
\newcommand{\loc}{\ell}
\newcommand{\sink}{\bot}
\newcommand{\dd}{k}
\newcommand{\CounterReach}{\textsf{CounterReach}\xspace}
\newcommand{\Cover}{\textsf{Cover}\xspace}
\newcommand{\NonTerm}{\textsf{NonTerm}\xspace}
\newcommand{\decpb}[3][]{\begin{problem}[#1]\\[-1.7em]\begin{description}     
    \item[\textsc{input:}] {#2}
    \item[\textsc{question:}] {#3}
    \end{description}
  \end{problem}}
\newcommand{\step}[1]{\xrightarrow{\,\raisebox{-1pt}[0pt][0pt]{\scriptsize\ensuremath
      {#1}}\,}}
\newcommand{\mstep}[1]{\xrightarrow{\,\raisebox{-1pt}[6pt][0pt]{\scriptsize\ensuremath
      {#1}}\,}}
\newcommand{\inst}[1]{\mathrel{\mathtt{#1}}}
\providecommand{\pop}{\mathrm{pop}}
\providecommand{\push}[1]{\mathrm{push}(#1)}
\providecommand{\mymoot}[1]{}
\newcommand{\blank}{\Box}
\newcommand{\emkl}{\triangleright}
\newcommand{\emkr}{\triangleleft}
\renewcommand{\natural}{\arena_\+N}
\newcommand{\energy}{\arena_\+E}
\newcommand{\bounded}{\arena_B}
\newcommand{\capped}{\arena_C}
\newcommand{\capp}[2][C]{\overline{\vec #2}^{#1}}
\let\oldcite\cite
\renewcommand{\cite}{\citep}
\providecommand{\citep}{\oldcite}
\providecommand{\citet}{\cite}
\providecommand{\citem}[2][1]{#1 {cite}`#2`}
\providecommand{\qedhere}{\ensuremath\Box}
\providecommand{\col}{\mathfrak c}
\newcommand{\lcol}{\mathrm{lcol}}
\newcommand{\vcol}{\mathrm{vcol}}
\newcommand{\litt}{\loc}
\newcommand{\Effect}{\Delta}
\providecommand{\AP}{}
\providecommand{\medskip}{}
\providecommand{\ensuremath}{}
\providecommand{\raisebox}[1]{}
\providecommand{\scalebox}[1]{}
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
\AP A vector system is a finite directed graph with a partition of
the vertices and weighted edges.  Formally, it is a tuple
$\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,\dd)$ where $\dd\in\+N$ is a
dimension, $\Loc$ is a finite set of locations partitioned into the
locations controlled by \Eve\ and \Adam, i.e.,
$\Loc=\Loc_\mEve\uplus \Loc_\mAdam$, and
$\Act\subseteq \Loc\times\+Z^\dd\times\Loc$ is a finite set of
weighted actions.  We write $\loc\step{\vec u}\loc'$
rather than $(\loc,\vec u,\loc')$ for actions in $\Act$.  A
vector addition system with states is a vector system where
$\Loc_\mAdam=\emptyset$, i.e., it corresponds to the one-player case.

````{prf:example} vector system
:label: 11-ex:mwg

  {numref}`11-fig:mwg` presents a vector system of
  dimension two with locations $\{\loc,\loc'\}$ where $\loc$ is
  controlled by \Eve\ and $\loc'$ by \Adam.
  

````

```{figure} ./../FigAndAlgos/11-fig:mwg.png
:name: 11-fig:mwg
:align: center
A vector system.
```

The intuition behind a vector system is that it
maintains $\dd$ counters $\mathtt{c}_1,\dots,\mathtt{c}_\dd$ assigned
to integer values.  An action $\loc\step{\vec u}\loc'\in\Act$ then
updates each counter by adding the corresponding entry of $\vec u$,
that is for all $1\leq j\leq\dd$, the action performs the update
$\mathtt{c}_j := \mathtt{c}_j+\vec u(j)$.

\medskip \AP Before we proceed any further, let us fix some notations
for vectors in $\+Z^\dd$.  We write `$\vec 0$' for the zero vector
with $\vec 0(j)\eqdef 0$ for all $1\leq j\leq\dd$.  For all
$1\leq j\leq\dd$, we write `$\vec e_j$' for the unit vector with
$\vec e_j(j)\eqdef 1$ and $\vec e_{j}(j')\eqdef 0$ for all $j'\neq j$.
Addition and comparison are defined componentwise, so that for
instance $\vec u\leq\vec u'$ if and only if for all $1\leq j\leq\dd$,
$\vec u(j)\leq\vec u'(j)$.  We write
$\weight(\loc\step{\vec u}\loc')\eqdef\vec u$ for the weight of an
action and $\weight(\pi)\eqdef\sum_{1\leq j\leq |\pi|}\weight(\pi_j)$
for the cumulative weight of a finite sequence of actions
$\pi\in\Act^\ast$.  For a vector $\vec u\in\+Z^\dd$, we use its
infinity norm $\|\vec u\|\eqdef\max_{1\leq j\leq\dd}|\vec u(j)|$,
hence $\|\vec 0\|=0$ and $\|\vec e_j\|=\|-\vec e_j\|=1$, and we let
$\|\loc\step{\vec u}\loc'\|\eqdef\|\weight(\loc\step{\vec
  u}\loc')\|=\|\vec u\|$
and $\|\Act\|\eqdef\max_{a\in\Act}\|\weight(a)\|$.  Unless stated
otherwise, we assume that all our vectors are represented in binary,
hence $\|\Act\|$ may be exponential in the size of $\?V$.

## Arenas and Games

\AP A vector system gives rise to an infinite graph
$G_\+N\eqdef(V,E)$ over the set of vertices
$V\eqdef(\Loc\times\+N^\dd)\uplus\{\sink\}$.  The vertices of the
graph are either **configurations** $\loc(\vec v)$ consisting of a
location $\loc\in \Loc$ and a vector of non-negative integers
$\vec v\in\+N^\dd$---such a vector represents a valuation of the
counters $\mathtt{c}_1,\dots,\mathtt c_\dd$---, or the
sink $\sink$.

\AP Consider an action in $a=(\loc\step{\vec u}\loc')$ in $\Act$: we
see it as a partial function
$a{:}\,\Loc\times\+N^\dd\,\pto \Loc\times\+N^\dd$ with domain
$\dom a\eqdef\{\loc(\vec v)\mid \vec v+\vec u\geq\vec 0\}$ and image
$a(\loc(\vec v))\eqdef \loc'(\vec v+\vec u)$; let also
$\dom\Act\eqdef\bigcup_{a\in\Act}\dom a$.  This allows us to define
the set $E$ of edges as a set of pairs
\begin{align*}
  E&\eqdef\{(\loc(\vec v),a(\loc(\vec v)))\mid a\in\Act\text{ and
     }\loc(\vec v)\in\dom a\}\\%\loc'(\vec v+\vec u))\mid
                               
  &\:\cup\:\{(\loc(\vec v),\sink)\mid\loc(\vec v)\not\in\dom\Act\}\cup\{(\sink,\sink)\}\;,
\end{align*}
where $\ing((v,v'))\eqdef v$ and $\out((v,v'))\eqdef v'$ for all
edges $(v,v')\in E$.  There is therefore an edge $(v,v')$ between two
configurations $v=\loc(\vec v)$ and $v'=\loc'(\vec v')$ if there
exists an action $\loc\step{\vec u}\loc'\in\Act$ such that
$\vec v'=\vec v+\vec u$.  Note that, quite importantly,
$\vec v+\vec u$ must be non-negative on every coordinate for this edge
to exist.  If no action can be applied, there is an edge to the
sink $\sink$, which ensures that $E$ is total: for all $v\in V$,
there exists an edge $(v,v')\in E$ for some $v'$, and thus there are
no `deadlocks' in the graph.

The configurations are naturally partitioned into those in
$\VE\eqdef\Loc_\mEve\times\+N^\dd$ controlled by~\Eve\ and those in
$\VA\eqdef\Loc_\mAdam\times\+N^\dd$ controlled by~\Adam.  Regarding
the sink, the only edge starting from $\sink$ loops back
to it, and it does not matter who of \Eve\ or \Adam\ controls it.  This
gives rise to an infinite arena $\arena_\+N\eqdef(G_\+N,\VE,\VA)$ called
the natural semantics of $\?V$.

\medskip Although we work in a turn-based setting with perfect
information, it is sometimes enlightening to consider the partial map
$\dest{:}\,V\times A\pto E$ defined by
$\dest(\loc(\vec v),a)\eqdef(\loc(\vec v),a(\loc(\vec v)))$ if
$\loc(\vec v)\in\dom a$ and
$\dest(\loc(\vec v),a)\eqdef(\loc(\vec v),\sink)$ if
$\loc(\vec v)\not\in\dom\Act$.  Note that a sequence $\pi$ over $E$
that avoids the sink can also be described by an initial
configuration $\loc_0(\vec v_0)$ paired with a sequence
over $\Act$.
% will rather use a vertex colouring $\col{:}\,V\to C$ and allow it to


````{prf:example} NEEDS LABEL natural semantics
{11-ex:sem}
  {numref}`11-fig:sem` illustrates the natural semantics of the system
  of {numref}`11-fig:mwg`; observe that all the configurations $\loc(0,n)$
  for $n\in\+N$ lead to the sink.

````


```{figure} ./../FigAndAlgos/11-fig:sem.png
:name: 11-fig:sem
:align: center
The natural semantics of the
    vector system of {numref}`11-fig:mwg`: a circle (resp.\
    a square) at position $(i,j)$ of the grid denotes a configuration
    $\loc(i,j)$ (resp.\ $\loc'(i,j)$) controlled by~\Eve\ (resp.\
    \Adam).
```

%   semantics would use instead $\Loc\times\+Z^\dd$ as set of vertices,

%   $\{(\loc(\vec v),\loc'(\vec v+\vec u))\mid \loc\step{\vec

%   as set of edges.  This eschews the need of a sink vertex since there

% \end{remark}

\AP A vector system $\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,\dd)$, a
colouring $\col{:}\,E\to C$, and an
objective $\Omega\subseteq C^\omega$ together define a vector game
$\game=(\natural(\?V),\col,\Omega)$.  Because $\natural(\?V)$ is an
infinite arena, we need to impose restrictions on our colourings
$\col{:}\,E\to C$ and the "qualitative
objectives" $\Omega\subseteq C^\omega$; at the very least, they should
be recursive.

There are then two variants of the associated decision problem:

* \AP the given initial credit variant, where we are given $\?V$,
  $\col$, $\Omega$, a location $\loc_0\in\Loc$ and an initial credit
  $\vec v_0\in\+N^\dd$, and ask whether \Eve\ wins $\game$ from the
  initial configuration $\loc_0(\vec v_0)$;
* \AP the existential initial credit variant, where we are given
  $\?V$, $\col$, $\Omega$, and a location $\loc_0\in\Loc$, and ask
  whether there exists an initial credit $\vec v_0\in\+N^\dd$ such
  that \Eve\ wins $\game$ from the initial
  configuration $\loc_0(\vec v_0)$.


Let us instantiate the previous abstract definition of vector games.
We first consider two `reachability-like'
\index{reachability!**see also** vector game\protect\mymoot|mymoot}
objectives, where $C\eqdef\{\varepsilon,\Win\}$ and
$\Omega\eqdef\Reach$, namely configuration reachability and
coverability.  The difference between the two is that, in the
configuration reachability problem, a specific configuration
$\loc_f(\vec v_f)$ should be visited, whereas in the coverability
problem, \Eve\ attempts to visit $\loc_f(\vec v')$ for some
vector $\vec v'$ componentwise larger or equal to
$\vec v_f$.

\decpb[configuration reachability vector game with given initial credit]
{\label{11-pb:

```{margin}
The name `coverability' comes from the the
  literature on Petri nets and "vector addition systems with
  states", because \Eve\ is attempting to **cover**
  $\loc_f(\vec v_f)$, i.e., to reach a configuration $\loc_f(\vec v')$
  with $\vec v'\geq\vec v_f$.
```

reach} A vector system
  $\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,\dd)$, an initial location
  $\loc_0\in\Loc$, an initial credit $\vec v_0\in\+N^\dd$, and a
  target configuration $\loc_f(\vec v_f)\in\Loc\times\+N^\dd$.}
{Does \Eve\ have a strategy to reach $\loc(\vec v)$ from
  $\loc_0(\vec v_0)$?\\That is, does she win the configuration
  reachability game $(\natural(\?V),\col,\Reach)$ from
  $\loc_0(\vec v_0)$, where $\col(e)= \Win$ if and only if
  $\ing(e)=\loc_f(\vec v_f)$?}

\decpb[coverability vector game with given initial credit]
{\label{11-pb:cov} A vector system
  $\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,\dd)$, an initial location
  $\loc_0\in\Loc$, an initial credit $\vec v_0\in\+N^\dd$, and a
  target configuration $\loc_f(\vec v_f)\in\Loc\times\+N^\dd$.}
{Does \Eve\ have a strategy to reach $\loc(\vec v')$ for some
  $\vec v'\geq\vec v_f$ from $\loc_0(\vec v_0)$?\\That is, does she win
  the coverability game $(\natural(\?V),\col,\Reach)$ from
  $\loc_0(\vec v_0)$, where $\col(e)= \Win$ if and only if
  $\ing(e)=\loc_f(\vec v')$ for some $\vec v'\geq\vec v_f$?}

````{prf:example} Objectives
:label: 11-ex:cov

  Consider the target configuration $\loc(2,2)$ in
  {numref}`11-fig:mwg,11-fig:sem`.  \Eve's winning region in the
  configuration reachability vector game is
  $\WE=\{\loc(n+1,n+1)\mid n\in\+N\}\cup\{\loc'(0,1)\}$, displayed on the left
  in {numref}`11-fig:cov`.  \Eve\ has indeed an obvious winning strategy
  from any configuration $\loc(n,n)$ with $n\geq 2$, which is to use
  the action $\loc\step{-1,-1}\loc$ until she reaches $\loc(2,2)$.
  Furthermore, in $\loc'(0,1)$---due to the natural semantics---,
  \Adam\ has no choice but to use the action $\loc'\step{2,1}\loc$:
  therefore $\loc'(0,1)$ and $\loc(1,1)$ are also winning for \Eve.

```{figure} ./../FigAndAlgos/11-fig:cov.png
:name: 11-fig:cov
:align: center
The winning regions of \Eve\ in the
    configuration reachability game (left) and the coverability game
    (right) on the graphs of {numref}`11-fig:mwg,11-fig:sem` with target
    configuration $\ell(2,2)$.  The winning vertices are in filled in
    green, while the losing ones are filled with white with a red
    border; the sink is always losing.
```

In the coverability vector game, \Eve's winning region is
$\WE=\{\loc(m+2,n+2),\loc'(m+2,n+2),\loc'(0,n+1),\loc(1,n+2),\loc'(2m+2,1),\loc(2m+3,1)\mid
m,n\in\+N\}$
displayed on the right in {numref}`11-fig:cov`.  Observe in particular
that \Adam\ is forced to use the action $\ell'\step{2,1}\ell$ from
the configurations of the form $\loc'(0,n+1)$, which brings him to a
configuration $\ell(2,n+2)$ coloured $\Win$ in the game, and thus the
configurations of the form $\loc(1,n+1)$ are also winning for \Eve
since she can play $\loc\step{-1,0}\loc'$.  Thus the configurations of
the form $\loc(2m+3,n+1)$ are also winning for \Eve, as she can play
the action $\loc\step{-1,0}\loc'$ to a winning configuration
$\loc'(2m+2,n+1)$ where all the actions available to \Adam\ go into
her winning region.

````


````{admonition} Remark [Location reachability]
\label{11-rk:cov2cov}
  In both configuration reachability and coverability, we can
  assume without loss of generality that $\loc_f\in\Loc_\mEve$ is
  controlled by \Eve\ and that $\vec v_f=\vec 0$ is the zero vector.
  Thus coverability is equivalent to **location reachability**.
  
  There is indeed a \logspace\ reduction to that case.  If
  $\loc_0(\vec v_0)=\loc_f(\vec v_f)$ in the case of "configuration
  reachability", or $\loc_0=\loc_f$ and $\vec v_0\geq\vec v_f$ in the
  case of coverability, the problem is trivial.
  
  Otherwise, any winning play must use at least one action.  For
  each incoming action $a=(\loc\step{\vec u}\loc_f)$ of $\loc_f$,
  create a new location $\loc_a$ controlled by \Eve\ and replace $a$ by
  $\loc\step{\vec u}\loc_a\step{\vec 0}\loc_f$, so that \Eve\ gains the
  control right before any play reaches $\loc_f$.  Also add a new
  location $\smiley$ controlled by \Eve\ with actions
  $\loc_a\step{-\vec v_f}\smiley$, and use $\smiley(\vec 0)$ as target
  configuration.

````


````{admonition} Remark [Coverability to reachability]
\label{11-rk:cov2reach}
  There is a \logspace\ reduction from coverability to
  configuration reachability.  By \cref{11-rk:cov2cov}, we can assume
  without loss of generality that $\loc_f\in\Loc_\mEve$ is controlled
  by \Eve\ and that $\vec v_f=\vec 0$ is the zero vector. It suffices
  therefore to add an action $\loc_f\step{-\vec e_j}\loc_f$ for
  all $1\leq j\leq\dd$.

````

Departing from reachability games, the
following is a very simple kind of safety
games where $C\eqdef\{\varepsilon,\Lose\}$ and $\Omega\eqdef\Safe$;
{numref}`11-fig:nonterm` shows \Eve's winning region in the case of the
graphs of {numref}`11-fig:mwg,11-fig:sem`.
\decpb[non-termination vector game with given initial credit]
{\label{11-pb:nonterm} A vector system
  $\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,\dd)$, an initial location
  $\loc_0\in\Loc$, and an initial credit $\vec v_0\in\+N^\dd$.}
{Does \Eve\ have a strategy to avoid the sink $\sink$ from
  $\loc_0(\vec v_0)$?\\That is, does she win the non-termination
  game $(\natural(\?V),\col,\Safe)$ from $\loc_0(\vec v_0)$, where
  $\col(e)=\Lose$ if and only if $\ing(e)=\sink$?} 

  
```{figure} ./../FigAndAlgos/11-fig:nonterm.png
:name: 11-fig:nonterm
:align: center
The winning region of \Eve\ in the
    non-termination game on the graphs of {numref}`11-fig:mwg,11-fig:sem`.
```

%   Consider the non-termination game on the graphs of

%   {numref}`11-fig:nonterm`

Finally, one of the most general vector games are "parity@parity
vector game" games, where $C\eqdef\{1,\dots,d\}$ and
$\Omega\eqdef\Parity$.  In order to define a colouring of the "natural
semantics", we assume that we are provided with a **location
  colouring** $\lcol{:}\,\Loc\to\{1,\dots,d\}$.
\decpb[parity vector game with given initial credit]
{\label{11-pb:parity}A vector system
  $\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,\dd)$, an initial location
  $\loc_0\in\Loc$, an initial credit $\vec v_0\in\+N^\dd$, and a
  location colouring $\lcol{:}\,\Loc\to\{1,\dots,d\}$ for some $d>0$.}
  {Does \Eve\ have a strategy to simultaneously avoid the
  sink $\sink$ and fulfil the \index{parity!**see also** vector
  game\protect\mymoot|mymoot}parity objective from $\loc_0(\vec
  v_0)$?\\That is, does she win the parity@parity vector game game
  $(\natural(\?V),\col,\Parity)$ from $\loc_0(\vec v_0)$, where
  $\col(e)\eqdef\lcol(\loc)$ if $\ing(e)=\loc(\vec v)$ for
  some $\vec v\in\+N^\dd$, and $\col(e)\eqdef 1$ if $\ing(e)=\sink$?}

````{admonition} Remark [Non termination to parity]
\label{11-rk:nonterm2parity}
  There is a \logspace\ reduction from non-termination to
  parity@parity vector game.
  Indeed, the two games coincide if we pick the constant location
  colouring defined by $\lcol(\loc)\eqdef 2$ for all $\loc\in\Loc$ in
  the parity game.

````

````{admonition} Remark [Coverability to parity]
\label{11-rk:cov2parity}
  There is a \logspace\ reduction from coverability to
  parity@parity vector game.  Indeed, by \cref{11-rk:cov2cov}, we can assume
  that $\loc_f\in\Loc_\mEve$ is controlled by \Eve\ and that the target
  credit is $\vec v_f=\vec 0$ the zero vector.  It suffices
  therefore to add an action $\loc_f\step{\vec 0}\loc_f$ and to colour
  every location $\loc\neq\loc_f$ with $\lcol(\loc)\eqdef 1$ and
  to set $\lcol(\loc_f)\eqdef 2$.

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
  $\dd\geq 2$.

````

````{admonition} Proof
:class: dropdown tip

  By \cref{11-rk:cov2reach,11-rk:nonterm2parity}, it suffices to prove the
  undecidability of coverability and non-termination.  For this,
  we exhibit reductions from the halting problem of "deterministic
  Minsky machines" with at least two counters.

  \AP Formally, a deterministic Minsky machine with $\dd$~counters
  $\?M=(\Loc,\Act,\dd)$ is defined similarly to a "vector addition
  system with states" with additional zero test actions
  $a=(\loc\step{i\eqby?0}\loc')$.  The set of locations contains a
  distinguished `halt' location $\loc_\mathtt{halt}$, and for every
  $\loc\in\Loc$, exactly one of the following holds: either (i)
  $(\loc\step{\vec e_i}\loc')\in\Act$ for some $0<i\leq\dd$ and
  $\loc'\in\Loc$, or (ii) $(\loc\step{i\eqby?0}\loc')\in\Act$ and
  $(\loc\step{-\vec e_i}\loc'')\in\Act$ for some $0<i\leq\dd$ and
  $\loc',\loc''\in\Loc$, or (iii) $\loc=\loc_\mathtt{halt}$.  The
  semantics of $\?M$ extends the natural semantics by
  handling zero tests actions $a=(\loc\step{i\eqby?0}\loc')$: we
  define the domain as $\dom a\eqdef\{\loc(\vec v)\mid \vec v(i)=0\}$
  and the image by $a(\loc(\vec v))\eqdef \loc(\vec v)$.  This
  semantics is deterministic, and from any starting vertex of $\natural(\?M)$,
  there is a unique play, which either eventually visits
  $\loc_\mathtt{halt}$ and then the sink in the next step, or keeps
  avoiding both $\loc_\mathtt{halt}$ and the sink
  indefinitely. 
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

  \AP The halting problem asks, given a deterministic Minsky machine
  and an initial location $\loc_0$, whether it halts, that is, whether
  $\loc_\mathtt{halt}(\vec v)$ is reachable for
  some $\vec v\in\+N^\dd$ starting from $\loc_0(\vec 0)$.  The
  halting problem is undecidable in any dimension
  $\dd\geq 2$ {cite}`Minsky:1967`.
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
  given a deterministic Minsky machine $\?M=(\Loc,\Act,\dd)$ and an
  initial location $\loc_0$, we construct a vector system
  $\?V\eqdef(\Loc\uplus\Loc_{\eqby?0}\uplus\{\frownie\},\Act',\Loc,\Loc_{\eqby?0}\uplus\{\frownie\},\dd)$
  where all the original locations are controlled by~\Eve\ and
  $\Loc_{\eqby?0}\uplus\{\frownie\}$ is a set of new locations
  controlled by~\Adam.  We use $\Loc_{\eqby?0}$ as a set of
  locations defined by
  \begin{align*}
    \Loc_{\eqby?0}&\eqdef\{\loc'_{i\eqby?0}\mid\exists\loc\in\Loc\mathbin.(\loc\step{i\eqby?0}\loc')\in\Act\}\intertext{and
                   define the set of actions by (see {numref}`11-fig:undec`)}
    \Act'&\eqdef\{\loc\step{\vec
          e_i}\loc'\mid(\loc\step{\vec e_i}\loc')\in\Act\}\cup\{\loc\step{-\vec e_i}\loc''\mid(\loc\step{-\vec e_i}\loc'')\in\Act\}\\
    &\:\cup\:\{\loc\step{\vec
      0}\loc'_{i\eqby?0},\;\;\:\loc'_{i\eqby?0}\!\!\step{\vec 0}\loc',\;\;\:\loc'_{i\eqby?0}\!\!\step{-\vec e_i}\frownie\mid(\loc\step{i\eqby?0}\loc')\in\Act\}\;.
  \end{align*}
  We use $\loc_0(\vec 0)$ as initial configuration and
  $\loc_\mathtt{halt}(\vec 0)$ as target configuration for the
  constructed coverability instance.  Here is the crux of the
  argument why \Eve\ has a winning strategy to cover
  $\loc_\mathtt{halt}(\vec 0)$ from $\loc_0(\vec 0)$ if and only if
  the Minsky machine@deterministic Minsky machine halts.
  
  Consider any configuration $\loc(\vec v)$.  If
  $(\loc\step{\vec e_i}\loc')\in\Act$, \Eve\ has no choice but to apply
  $\loc\step{\vec e_i}\loc'$ and go to the configuration
  $\loc'(\vec v+\vec e_i)$ also reached in one step in $\?M$.  If
  $\{\loc\step{i\eqby?0}\loc',\loc\step{-\vec e_i}\loc''\}\in\Act$ and
  $\vec v(i)=0$, due to the natural semantics, \Eve\ cannot use the
  action $\loc\step{-\vec e_i}\loc''$, thus she must use
  $\loc\step{\vec 0}\loc'_{i\eqby?0}$.  Still due to the "natural
  semantics", \Adam\ cannot use
  $\loc'_{i\eqby?0}\!\!\step{-\vec e_i}\frownie$, thus he must use
  $\loc'_{i\eqby?0}\!\!\step{\vec 0}\loc'$.  Hence \Eve\ regains the
  control in $\loc'(\vec v)$, which was also the configuration reached
  in one step in $\?M$.  Finally, if
  $\{\loc\step{i\eqby?0}\loc',\loc\step{-\vec e_i}\loc''\}\in\Act$ and
  $\vec v(i)>0$, \Eve\ can choose: if she uses
  $\loc\step{-\vec e_i}\loc''$, she ends in the configuration
  $\loc''(\vec v-\vec e_i)$ also reached in one step in $\?M$.  In
  fact, she should not use $\loc\step{\vec 0}\loc'_{i\eqby?0}$,
  because \Adam\ would then have the opportunity to apply
  $\loc'_{i\eqby?0}\!\!\step{-\vec e_i}\frownie$ and to win, as
  $\frownie$ is a deadlock location and all the subsequent moves end
  in the sink.  Thus, if $\?M$ halts, then \Eve\ has a winning
  strategy that simply follows the unique play of $\?M$, and
  conversely, if \Eve\ wins, then necessarily she had to follow the
  play of $\?M$ and thus the machine halts.
    
  \medskip Further note that, in a deterministic Minsky machine the
  halting problem is similarly akin to the **complement** of
  non-termination with given initial credit $\vec 0$.  This means
  that, in the vector system
  $\?V=(\Loc\uplus\Loc_{\eqby?0}\uplus\{\frownie\},\Act',\Loc,\Loc_{\eqby?0}\uplus\{\frownie\},\dd)$
  defined earlier, \Eve\ has a winning strategy to avoid the sink
  from $\loc_0(\vec 0)$ if and only if the given "Minsky
  machine@deterministic Minsky machine" does
  not halt from $\loc_0(\vec 0)$, which shows the undecidability of
  \cref{11-pb:nonterm}.

  \medskip Finally, let us observe that both the existential and the
  universal initial credit variants of the halting problem are also
  undecidable.  Indeed, given an instance of the halting problem,
  i.e., given a deterministic Minsky machine $\?M=(\Loc,\Act,\dd)$
  and an initial location $\loc_0$, we add $\dd$~new locations
  $\loc_\dd,\loc_{\dd-1},\dots,\loc_1$ with respective actions
  $\loc_j\step{-\vec e_j}\loc_j$ and $\loc_j\step{j\eqby?0}\loc_{j-1}$
  for all $\dd\geq j>0$.  This modified machine first resets all its
  counters to zero before reaching $\loc_0(\vec 0)$ and then performs
  the same execution as the original machine.  Thus there exists an
  initial credit $\vec v$ such that the modified machine
  reaches $\loc_\mathtt{halt}$ from $\loc_\dd(\vec v)$ if and only if
  for all initial credits $\vec v$ the modified machine
  reaches $\loc_\mathtt{halt}$ from $\loc_\dd(\vec v)$, if and only if
  $\loc_\mathtt{halt}$ was reachable from $\loc_0(\vec 0)$ in the
  original machine.  The previous construction of a vector system
  applied to the modified machine then shows the undecidability of the
  existential initial credit variants of
  \cref{11-pb:cov,11-pb:nonterm}
  
  
  
  
  .

````


