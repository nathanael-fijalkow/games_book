(11-sec:resource)=
# Resource-conscious games

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
Vector games are very well suited for reasoning about systems
manipulating discrete resources, modelled as counters.  However, in
the natural semantics, actions that would deplete some resource,
i.e., that would make some counter go negative, are simply inhibited.
In models of real-world systems monitoring resources like a gas
tank or a battery, a depleted resource would be considered as a system
failure.  In the energy games of Section {ref}`11-sec:energy`, those situations
are accordingly considered as winning for \Adam.  Moreover, if we are
modelling systems with a bounded capacity for storing resources, a
counter exceeding some bound might also be considered as a failure,
which will be considered with bounding games in Section {ref}`11-sec:bounding`.

These resource-conscious games can be seen as providing alternative
semantics for vector systems.  They will also be instrumental in
establishing complexity upper bounds for monotonic "asymmetric vector
games" later in Section {ref}`11-sec:complexity`, and are strongly related to
multidimensional mean-payoff games, as will be explained in
Section {ref}`12-sec:MPEG` of Chapter {ref}`12-chap:multiobjective`.

(11-sec:energy)=
## Energy Semantics

Energy games model systems where the depletion of a resource
allows \Adam\ to win.  This is captured by an energy semantics
$\energy(\?V)\eqdef(V,E_\+E,\VE,\VA)$ associated with a "vector
system" $\?V$: we let as before
$V\eqdef(\Loc\times\+N^\dd)\uplus\{\sink\}$, but define instead
\begin{align*}
  E_\+E&\eqdef \{(\loc(\vec v), \loc'(\vec v+\vec u)\mid
         \loc\step{\vec u}\loc'\in\Act\text{
      and }\vec v+\vec u\geq\vec 0\}\\
    &\:\cup\:\{(\loc(\vec v),\sink)\mid\forall\loc\step{\vec
      u}\loc'\in\Act\mathbin.\vec v+\vec u\not\geq\vec 0\}
    \cup\{(\sink,\sink)\}\;.
\end{align*}
In the energy semantics, moves that would result in a negative
component lead to the sink instead of being inhibited.

````{prf:example} Energy semantics
:label: 11-ex:nrg

  {numref}`11-fig:nrg` illustrates the energy semantics of the vector
  system depicted in {numref}`11-fig:mwg` on \cpageref{11-fig:mwg}.  Observe that,
  by contrast with the natural semantics of the same system depicted
  in {numref}`11-fig:sem`, all the configurations $\loc'(0,n)$ controlled
  by \Adam\ can now move to the sink.

````

```{figure} ./../FigAndAlgos/11-fig:nrg.png
:name: 11-fig:nrg
:align: center
The energy semantics of the
    vector system of {numref}`11-fig:mwg`: a circle (resp.\
    a square) at position $(i,j)$ of the grid denotes a configuration
    $\loc(i,j)$ (resp.\ $\loc'(i,j)$) controlled by~\Eve\ (resp.\
    \Adam).
```

Given a colouring $\col{:}\,E\to C$ and an objective $\Omega$, we
call the resulting game $(\energy(\?V),\col,\Omega)$ an energy
game.  In particular, we shall speak of "configuration
reachability, coverability, non-termination, and parity@parity
vector game energy games" when replacing $\natural(\?V)$ by
$\energy(\?V)$ in \crefrange{11-pb:reach}{11-pb:parity}; the
existential initial credit variants are defined similarly.

````{prf:example} Energy games
:label: 11-ex:cov-nrg

  Consider the target configuration $\loc(2,2)$ in
  {numref}`11-fig:mwg,11-fig:nrg`.  \Eve's winning region in the
  configuration reachability energy game is
  $\WE=\{\loc(n+2,n+2)\mid n\in\+N\}$, displayed on the left in
  {numref}`11-fig:cov-nrg`.  In the coverability energy game, \Eve's
  winning region is
  $\WE=\{\loc(m+2,n+2),\loc'(m+3,n+2)\mid m,n\in\+N\}$ displayed on
  the right in {numref}`11-fig:cov-nrg`.

````

```{figure} ./../FigAndAlgos/11-fig:cov-nrg.png
:name: 11-fig:cov-nrg
:align: center
The winning regions of \Eve\ in the
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
  coverability, non-termination, and parity@parity vector games,
  both with given and with existential initial credit.

````

````{admonition} Proof
:class: dropdown tip

  Let us first reduce asymmetric vector games to energy games.
  Given $\?V$, $\col$, and $\Omega$ where $\?V$ is asymmetric and
  $\Eve$ loses if the play ever visits the sink $\sink$, we see that
  $\Eve$ wins $(\natural(\?V),\col,\Omega)$ from some $v\in V$ if and
  only if she wins $(\energy(\?V),\col,\Omega)$ from $v$.  Of course,
  this might not be true if $\?V$ is not asymmetric, as seen for
  instance in  {prf:ref}`11-ex:cov,11-ex:cov-nrg`.
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

  \medskip Conversely, let us reduce energy games to "asymmetric
  vector games".  Consider
  $\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,\dd)$, a colouring $\col$
  defined from a vertex colouring $\vcol$ by
  $\col(e)\eqdef\vcol(\ing(e))$, and an objective $\Omega$, where
  $\vcol$ and $\Omega$ are such that $\Eve$ loses if the play ever
  visits the sink $\sink$ and such that, for all $\pi\in C^\ast$,
  $p\in C$, and $\pi'\in C^\omega$, $\pi p\pi'\in\Omega$ if and only
  if $\pi pp\pi'\in\Omega$ (we shall call $\Omega$
  **stutter-invariant**, and the objectives in the statement are
  indeed stutter-invariant).  We construct an "asymmetric vector
  system"
  $\?V'\eqdef(\Loc\uplus\Loc_\Act,\Act',\Loc_\mEve\uplus\Loc_\Act,\Loc_\mAdam,\dd)$
  where we add the following locations controlled by~\Eve:
    \begin{align*}
      \Loc_\Act&\eqdef\{\loc_a\mid a=(\loc\step{\vec
                 u}\loc')\in\Act\text{ and }\loc\in\Loc_\mAdam\}\;.
      \intertext{We also modify the set of actions:}
      \Act'&\eqdef\{\loc\step{\vec u}\loc'\mid \loc\step{\vec
             u}\loc'\in\Act\text{ and }\loc\in\Loc_\mEve\}\\
      &\:\cup\:\{\loc\step{\vec 0}\loc_a,\;\loc_a\step{\vec u}\loc'\mid a=(\loc\step{\vec u}\loc')\in\Act\text{ and }\loc\in\Loc_\mAdam\}\;.
    \end{align*}
    {numref}`11-fig:avg` presents the result of this reduction on the
    system of {numref}`11-fig:mwg`.  We define a vertex colouring
    $\vcol'$ of $\arena_\+N(\?V')$ with $\vcol'(v)\eqdef\vcol(v)$ for
    all $v\in \Loc\times\+N^\dd\uplus\{\sink\}$ and
    $\vcol'(\loc_a(\vec v))\eqdef\vcol(\loc(\vec v))$ if
    $a=(\loc\step{\vec u}\loc')\in\Act$.  Then, for all vertices
    $v\in V$, \Eve\ wins from $v$ in the energy game
    $(\energy(\?V),\col,\Omega)$ if and only if she wins from $v$ in
    the vector game $(\natural(\?V'),\col',\Omega)$.  The crux of
    the argument is that, in a configuration $\loc(\vec v)$ where
    $\loc\in\Loc_\mAdam$, if $a=(\loc\step{\vec u}\loc')\in\Act$ is an
    action with $\vec v+\vec u\not\geq\vec 0$, in the "energy
    semantics, \Adam\ can force the play into the sink" by
    playing $a$; the same occurs in $\?V'$ with the "natural
    semantics", as \Adam\ can now choose to play
    $\loc\step{\vec 0}\loc_a$ where \Eve\ has only
    $\loc_a\step{\vec u}\loc'$ at her disposal, which leads to the
    sink.\todoquestion{Is that clear?}
    
    
    
    
    
    
    
    

````

In turn, energy games with existential initial credit are related
to the multi-dimensional mean-payoff games of
Chapter {ref}`12-chap:multiobjective`.
% case of dimension~one in Subsection {ref}`11-subsec:mono-dim1`.



(11-sec:bounding)=
## Bounded Semantics

While \Adam\ wins immediately in an energy game if a resource gets
depleted, he also wins in a bounding game if a resource reaches a
certain bound $B$.  
This is
a **hard upper bound**, allowing to model systems where exceeding a
capacity results in failure, like a dam that overflows and floods the
area.  We define for a bound $B\in\+N$ the bounded semantics
$\bounded(\?V)=(V^B,E^B,\VE^B,\VA^B)$ of a vector system $\?V$ by
\begin{align*}
  V^B&\eqdef\{\loc(\vec v)\mid\loc\in\Loc\text{ and }\|\vec v\|<B\}\;,\\
  E^B&\eqdef \{(\loc(\vec v),\loc'(\vec v+\vec u))\mid\loc\step{\vec
       u}\loc'\in\Act,\vec v+\vec u\geq\vec 0,\text{ and }\|\vec
       v+\vec u\|<B\}\\
     &\:\cup\:\{(\loc(\vec v),\sink)\mid\forall\loc\step{\vec
               u}\loc'\in\Act\mathbin.\vec v+\vec u\not\geq\vec
               0\text{ or }\|\vec v+\vec u\|\geq B\}
     \cup\{(\sink,\sink)\}\;.
\end{align*}
As usual, $\VE^B\eqdef V^B\cap\Loc_\mEve\times\+N^\dd$ and
$\VA^B\eqdef V^B\cap\Loc_\mAdam\times\+N^\dd$.  Any edge from the
energy semantics that would bring to a configuration $\loc(\vec v)$
with $\vec v(i)\geq B$ for some $1\leq i\leq\dd$ leads instead to the
sink.  All the configurations in this arena have norm less than $B$,
thus $|V^B|=|\Loc| B^\dd+1$, and the qualitative games of
Chapter {ref}`2-chap:regular` are decidable over this arena.

Our focus here is on non-termination games played on the "bounded
semantics" where $B$ is not given as part of the input, but quantified
existentially.  As usual, the existential initial credit variant
of \cref{11-pb:bounding} is obtained by quantifying $\vec v_0$
existentially in the question.
\decpb[bounding game with given initial credit]
{\label{11-pb:bounding} A vector system
  $\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,\dd)$, an initial location
  $\loc_0\in\Loc$, and an initial credit $\vec v_0\in\+N^\dd$.}
  {Does there exist $B\in\+N$ such that \Eve\ has a strategy to avoid the
  sink $\sink$ from $\loc_0(\vec v_0)$ in the "bounded
  semantics"?  That is, does there exist $B\in\+N$ such that she wins
  the bounding game $(\bounded(\?V),\col,\Safe)$ from
  $\loc_0(\vec v_0)$, where $\col(e)\eqdef\Lose$ if and only if $\ing(e)=\sink$?}

````{prf:lemma} NEEDS TITLE 11-lem:parity2bounding
:label: 11-lem:parity2bounding

  There is a \logspace\ reduction from parity@parity vector games
  asymmetric vector games to bounding games, both with given
  and with existential initial credit.

````

````{admonition} Proof
:class: dropdown tip

  Given an asymmetric vector system
  $\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,\dd)$, a location colouring
  $\lcol{:}\,\Loc\to\{1,\dots,2d\}$, and an initial location
  $\loc_0\in\Loc$, we construct a vector system $\?V'$ of dimension
  $\dd'\eqdef\dd+d$ as described in {numref}`11-fig:bounding`, where the
  priorities in $\?V$ for $p\in\{1,\dots,d\}$ are indicated above the
  corresponding locations.
  
  
```{figure} ./../FigAndAlgos/11-fig:bounding.png
:name: 11-fig:bounding
:align: center
Schema of the reduction to
      bounding games in the proof of  {prf:ref}`11-lem:parity2bounding`.
```
  
  If \Eve\ wins the bounding game played over $\?V'$ from some
  configuration $\loc_0(\vec v_0)$, then she also wins the "parity
  vector game" played over $\?V$ from the configuration $\loc_0(\vec
  v'_0)$ where $\vec v'_0$ is the projection of $\vec v_0$
  to $\+N^\dd$.  Indeed, she can play essentially the same strategy:
  by  {prf:ref}`11-lem:mono` she can simply ignore the new decrement
  self loops, while the actions on the components in
  $\{\dd+1,\dots,\dd+d\}$ ensure that the maximal priority visited
  infinitely often is even---otherwise some decrement $-\vec
  e_{\dd+p}$ would be played infinitely often but the increment $\vec
  e_{\dd+p}$ only finitely often.\todoquestion{Should I provide more details?}
  

  \medskip
  Conversely, consider the parity@parity vector game game $\game$ played over
  $\natural(\?V)$ with the colouring defined by $\lcol$.  Then the
  Pareto limit of the game is finite, thus there exists a natural
  number
  \begin{equation}\label{11-eq:b0}
    B_0\eqdef 1+\max_{\loc_0(\vec v_0)\in\mathsf{Pareto}(\?G)}\|\vec
  v_0\|
  \end{equation} bounding the norms of the minimal winning configurations.
  For a vector $\vec v$ in $\+N^\dd$, let us write $\capp[B_0]v$ for
  the vector `capped' at $B$: for all $1\leq i\leq\dd$,
  $\capp[B_0]v(i)\eqdef\vec v(i)$ if $\vec v(i)<B_0$ and
  $\capp[B_0]v\eqdef B_0$ if $\vec v(i)\geq B_0$.

  
  
  
  
  
  
  
  

  Consider now some configuration $\loc_0(\vec
  v_0)\in\mathsf{Pareto}(\game)$.  As seen in  {prf:ref}`11-lem:finmem`,
  since $\loc_0(\vec v_0)\in\WE(\game)$, there is a finite
  self-covering tree witnessing the fact, and an associated winning
  strategy.  Let $H(\loc_0(\vec v_0))$ denote the height of this
  self-covering tree and observe that all the configurations in this
  tree have norm bounded by $\|\vec v_0\|+\|\Act\|\cdot H(\loc_0(\vec
  v_0))$.
  Let us define
  \begin{equation}\label{11-eq:b}
   B\eqdef B_0+(\|\Act\|+1)\cdot \max_{\loc_0(\vec
  v_0)\in\mathsf{Pareto}(\?G)}H(\loc_0(\vec v_0))\;.
  \end{equation}
  This is a bound on the norm of the configurations appearing on the
  (finitely many) self-covering trees spawned by the elements
  of $\mathsf{Pareto}(\game)$.  Note that $B\geq B_0+(\|\Act\|+1)$ since
  a self-covering tree has height at least~one.

  Consider the non-termination game
  $\game_B\eqdef(\bounded(\?V'),\col',\Safe)$ played over the
  bounded semantics defined by $B$, where $\col'(e)=\Lose$ if and
  only if $\ing(e)=\sink$.  Let $\vec b\eqdef\sum_{1\leq p\leq
  d}(B-1)\cdot\vec e_{\dd+p}$.
  {\renewcommand{\qedsymbol}{}
  \begin{claim}\label{11-cl:parity2bounding} If $\loc_0(\vec
    v)\in\WE(\game)$, then
    $\loc_0(\capp[B_0]{v}+\vec b)\in\WE(\game_B)$.
  \end{claim}}
  Indeed, by definition of the "Pareto
  limit" $\mathsf{Pareto}(\game)$, if $\loc_0(\vec v)\in\WE(\game)$,
  then there exists $\vec v_0\leq\vec v$ such that $\loc_0(\vec
  v_0)\in\mathsf{Pareto}(\game)$.  By definition of the bound $B_0$,
  $\|\vec v_0\|<B_0$, thus $\vec v_0\leq\capp[B_0]v$.  Consider the
  self-covering tree of height $H(\loc_0(\vec v_0))$ associated
  to $\loc_0(\vec v_0)$, and the strategy $\sigma'$ defined by the
  memory structure from the
  proof of  {prf:ref}`11-lem:finmem`.  This is a winning strategy for \Eve
  in $\game$ starting from $\loc_0(\vec v_0)$, and
  by  {prf:ref}`11-lem:mono`, it is also winning
  from $\loc_0(\capp[B_0]v)$.
    
  Here is how \Eve\ wins $\game_B$ from $\loc_0(\capp[B_0]v+\vec b)$.
  She essentially follows the strategy $\sigma'$, with two
  modifications.  First, whenever $\sigma'$ goes to a return node
  $\loc(\vec v)$ instead of a leaf $\loc(\vec v')$---thus $\vec
  v\leq\vec v'$---, the next time \Eve\ has the control, she uses the
  self loops to decrement the current configuration by $\vec v'-\vec
  v$.  This ensures that any play consistent with the modified
  strategy remains between zero and $B-1$ on the components
  in $\{1,\dots,\dd\}$.  (Note that if she never regains the control,
  the current vector never changes any more since $\?V$ is
  asymmetric.)

  Second, whenever a play in $\game$ visits a location with even
  parity $2p$ for some $p$ in $\{1,\dots,d\}$, \Eve\ has the opportunity
  to increase the coordinates in $\{\dd+1,\dots,\dd+p\}$ in $\game_B$.
  She does so and increments until all these components reach $B-1$.
  This ensures that any play consistent with the modified strategy
  remains between zero and $B-1$ on the components
  in $\{\dd+1,\dots,\dd+p\}$.  Indeed, $\sigma'$ guarantees that the
  longest sequence of moves before a play visits a location with
  maximal even priority is bounded by $H(\loc_0(\vec v_0))$, thus the
  decrements $-\vec e_{\dd+p}$ introduced in $\game_B$ by the
  locations from $\game$ with odd parity $2p-1$ will never force the
  play to go negative.\todoquestion{Is that clear enough?}

````

The bound $B$ defined in~\cref{11-eq:b} in the previous proof is not
constructive, and possibly much larger than really required.
Nevertheless, one can sometimes show that an explicit $B$ suffices in
a bounding game.
A simple example is provided by the coverability asymmetric
vector games with existential initial credit arising from
\cref{11-rk:cov2parity}, i.e., where the objective is to reach some
location $\loc_f$.  Indeed, it is rather straightforward that there
exists a suitable initial credit such that \Eve\ wins the game if and
only if she wins the finite reachability game played over the
underlying directed graph over $\Loc$ where we ignore the counters.
Thus, for an initial location $\loc_0$, $B_0=|\Loc|\cdot\|\Act\|+1$
bounds the norm of the necessary initial credit, while a simple path
may visit at most $|\Loc|$ locations, thus
$B=B_0+|\Loc|\cdot\|\Act\|$ suffices for \Eve\ to win the constructed
bounding game.

In the general case of bounding games with "existential initial
credit", an explicit bound can be established.  The proof goes
along very different lines and is too involved to fit in this chapter,
but we refer the reader
to {cite}`Jurdzinski&Lazic&Schmitz:2015,Colcombet&Jurdzinski&Lazic&Schmitz:2017`
for details.

````{prf:theorem} Bounds on bounding
:label: 11-th:bounding

  If \Eve\ wins a bounding game with existential initial credit
  defined by a "vector
  system" $\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,\dd)$, then an
  initial credit $\vec v_0$ with $\|\vec
  v_0\|=(4|\Loc|\cdot\|\Act\|)^{2(\dd+2)^3}$ and a bound
  $B=2(4|\Loc|\cdot\|\Act\|)^{2(\dd+2)^3}+1$ suffice for this.

````

\Cref{11-th:bounding} also yields a way of handling bounding games
with given initial credit.  
\TODO{Last missing bit regarding complexity upper bounds.}
  

