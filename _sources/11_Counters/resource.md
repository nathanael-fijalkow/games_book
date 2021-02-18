(11-sec:resource)=
# Resource-conscious games


```{math}
\newcommand{\eqdef}{\eqby{def}}
\newcommand{\Loc}{\?L}
\newcommand{\Act}{A}
\newcommand{\loc}{\ell}
\newcommand{\sink}{\bot}
\newcommand{\dd}{k}
\newcommand{\energy}{\arena_\+E}
\newcommand{\bounded}{\arena_B}
\newcommand{\lcol}{\mathrm{lcol}}
\newcommand{\vcol}{\mathrm{vcol}}
\newcommand{\Eve}{\textrm{Eve}}
\newcommand{\Adam}{\textrm{Adam}}
\newcommand{\game}{\mathcal{G}}
\newcommand{\col}{\textsf{col}}
\newcommand{\mEve}{\mathrm{Eve}}
\newcommand{\mAdam}{\mathrm{Adam}}
\newcommand{\VE}{V_\mEve}
\newcommand{\VA}{V_\mAdam}
\newcommand{\ing}{\textrm{In}}
\newcommand{\WE}{W_\mEve}
\newcommand{\Lose}{\textrm{Lose}}
\newcommand{\Safe}{\mathtt{Safe}}
```

Vector games are very well suited for reasoning about systems
manipulating discrete resources, modelled as counters.  However, in
the natural semantics, actions that would deplete some resource,
i.e., that would make some counter go negative, are simply inhibited.
In models of real-world systems monitoring resources like a gas
tank or a battery, a depleted resource would be considered as a system
failure.  In the energy games of Section {ref}`11-sec:energy`, those situations
are accordingly considered as winning for \textrm{Adam}  Moreover, if we are
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
allows \textrm{Adam} to win.  This is captured by an energy semantics
$\arena_\+E\?V)\eqby{def}V,E_\+E,V_\mEveV_\mathrm{Adam} associated with a "vector
system" $\?V$: we let as before
$V\eqby{def}\?Ltimes\+N^k\uplus\{\bot}$, but define instead
\begin{align*}
  E_\+E&\eqby{def}\{(\ell\vec v), \ell(\vec v+\vec u)\mid
         \ellstep{\vec u}\ell\inAtext{
      and }\vec v+\vec u\geq\vec 0\}\\
    &\:\cup\:\{(\ell\vec v),\bot\mid\forall\ellstep{\vec
      u}\ell\inAmathbin.\vec v+\vec u\not\geq\vec 0\}
    \cup\{(\bot\bot\}\;.
\end{align*}
In the energy semantics, moves that would result in a negative
component lead to the sink instead of being inhibited.

````{prf:example} Energy semantics
:label: 11-ex:nrg

  {numref}`11-fig:nrg` illustrates the energy semantics of the vector
  system depicted in {numref}`11-fig:mwg` on \cpageref{11-fig:mwg}.  Observe that,
  by contrast with the natural semantics of the same system depicted
  in {numref}`11-fig:sem`, all the configurations $\ell(0,n)$ controlled
  by \textrm{Adam} can now move to the sink.

````

```{figure} ./../FigAndAlgos/11-fig:nrg.png
:name: 11-fig:nrg
:align: center
The energy semantics of the
    vector system of {numref}`11-fig:mwg`: a circle (resp.\
    a square) at position $(i,j)$ of the grid denotes a configuration
    $\elli,j)$ (resp.\ $\ell(i,j)$) controlled by~\textrm{Eve} (resp.\
    \textrm{Adam}.
```

Given a colouring $\textsf{col}:}\,E\to C$ and an objective $\Omega$, we
call the resulting game $(\arena_\+E\?V),\textsf{col}\Omega)$ an energy
game.  In particular, we shall speak of "configuration
reachability, coverability, non-termination, and parity@parity
vector game energy games" when replacing $\natural(\?V)$ by
$\arena_\+E\?V)$ in \crefrange{11-pb:reach}{11-pb:parity}; the
existential initial credit variants are defined similarly.

````{prf:example} Energy games
:label: 11-ex:cov-nrg

  Consider the target configuration $\ell2,2)$ in
  {numref}`11-fig:mwg,11-fig:nrg`.  \textrm{Eve}s winning region in the
  configuration reachability energy game is
  $W_\mathrm{Eve}{\elln+2,n+2)\mid n\in\+N\}$, displayed on the left in
  {numref}`11-fig:cov-nrg`.  In the coverability energy game, \textrm{Eve}s
  winning region is
  $W_\mathrm{Eve}{\ellm+2,n+2),\ell(m+3,n+2)\mid m,n\in\+N\}$ displayed on
  the right in {numref}`11-fig:cov-nrg`.

````

```{figure} ./../FigAndAlgos/11-fig:cov-nrg.png
:name: 11-fig:cov-nrg
:align: center
The winning regions of \textrm{Eve} in the
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
  Given $\?V$, $\textsf{col}, and $\Omega$ where $\?V$ is asymmetric and
  $\textrm{Eve} loses if the play ever visits the sink $\bot, we see that
  $\textrm{Eve} wins $(\natural(\?V),\textsf{col}\Omega)$ from some $v\in V$ if and
  only if she wins $(\arena_\+E\?V),\textsf{col}\Omega)$ from $v$.  Of course,
  this might not be true if $\?V$ is not asymmetric, as seen for
  instance in  {prf:ref}`11-ex:cov,11-ex:cov-nrg`.
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

  \medskip Conversely, let us reduce energy games to "asymmetric
  vector games".  Consider
  $\?V=(\?LA\Loc_\mathrm{Eve}\Loc_\mathrm{Adam}k$, a colouring $\textsf{col}
  defined from a vertex colouring $\mathrm{vcol} by
  $\textsf{col}e)\eqby{def}vcol(\textrm{In}e))$, and an objective $\Omega$, where
  $\mathrm{vcol} and $\Omega$ are such that $\textrm{Eve} loses if the play ever
  visits the sink $\bot and such that, for all $\pi\in C^\ast$,
  $p\in C$, and $\pi'\in C^\omega$, $\pi p\pi'\in\Omega$ if and only
  if $\pi pp\pi'\in\Omega$ (we shall call $\Omega$
  **stutter-invariant**, and the objectives in the statement are
  indeed stutter-invariant).  We construct an "asymmetric vector
  system"
  $\?V'\eqby{def}\?Luplus\Loc_AA,\Loc_\mathrm{Eve}uplus\Loc_A\Loc_\mathrm{Adam}k$
  where we add the following locations controlled by~\textrm{Eve}
    \begin{align*}
      \Loc_A\eqby{def}{\loc_a\mid a=(\ellstep{\vec
                 u}\ell)\inAtext{ and }\ellin\Loc_\mathrm{Adam}}\;.
      \intertext{We also modify the set of actions:}
      A&\eqby{def}{\ellstep{\vec u}\ell\mid \ellstep{\vec
             u}\ell\inAtext{ and }\ellin\Loc_\mathrm{Eve}}\\
      &\:\cup\:\{\ellstep{\vec 0}\loc_a,\;\loc_a\step{\vec u}\ell\mid a=(\ellstep{\vec u}\ell)\inAtext{ and }\ellin\Loc_\mathrm{Adam}}\;.
    \end{align*}
    {numref}`11-fig:avg` presents the result of this reduction on the
    system of {numref}`11-fig:mwg`.  We define a vertex colouring
    $\mathrm{vcol}$ of $\arena_\+N(\?V')$ with $\mathrm{vcol}(v)\eqby{def}vcol(v)$ for
    all $v\in \?Ltimes\+N^kuplus\{\bot}$ and
    $\mathrm{vcol}(\loc_a(\vec v))\eqby{def}vcol(\ell\vec v))$ if
    $a=(\ellstep{\vec u}\ell)\inA.  Then, for all vertices
    $v\in V$, \textrm{Eve} wins from $v$ in the energy game
    $(\arena_\+E\?V),\textsf{col}\Omega)$ if and only if she wins from $v$ in
    the vector game $(\natural(\?V'),\textsf{col},\Omega)$.  The crux of
    the argument is that, in a configuration $\ell\vec v)$ where
    $\ellin\Loc_\mathrm{Adam}, if $a=(\ellstep{\vec u}\ell)\inA is an
    action with $\vec v+\vec u\not\geq\vec 0$, in the "energy
    semantics, \textrm{Adam} can force the play into the sink" by
    playing $a$; the same occurs in $\?V'$ with the "natural
    semantics", as \textrm{Adam} can now choose to play
    $\ellstep{\vec 0}\loc_a$ where \textrm{Eve} has only
    $\loc_a\step{\vec u}\ell$ at her disposal, which leads to the
    sink.\todoquestion{Is that clear?}
    
    
    
    
    
    
    
    

````

In turn, energy games with existential initial credit are related
to the multi-dimensional mean-payoff games of
Chapter {ref}`12-chap:multiobjective`.
% case of dimension~one in Subsection {ref}`11-subsec:mono-dim1`.



(11-sec:bounding)=
## Bounded Semantics

While \textrm{Adam} wins immediately in an energy game if a resource gets
depleted, he also wins in a bounding game if a resource reaches a
certain bound $B$.  
This is
a **hard upper bound**, allowing to model systems where exceeding a
capacity results in failure, like a dam that overflows and floods the
area.  We define for a bound $B\in\+N$ the bounded semantics
$\arena_B\?V)=(V^B,E^B,V_\mEveB,V_\mAdamB)$ of a vector system $\?V$ by
\begin{align*}
  V^B&\eqby{def}{\ell\vec v)\mid\ellin\?Ltext{ and }\|\vec v\|<B\}\;,\\
  E^B&\eqby{def}\{(\ell\vec v),\ell(\vec v+\vec u))\mid\ellstep{\vec
       u}\ell\inA\vec v+\vec u\geq\vec 0,\text{ and }\|\vec
       v+\vec u\|<B\}\\
     &\:\cup\:\{(\ell\vec v),\bot\mid\forall\ellstep{\vec
               u}\ell\inAmathbin.\vec v+\vec u\not\geq\vec
               0\text{ or }\|\vec v+\vec u\|\geq B\}
     \cup\{(\bot\bot\}\;.
\end{align*}
As usual, $V_\mEveB\eqby{def}V^B\cap\Loc_\mathrm{Eve}times\+N^k and
$V_\mAdamB\eqby{def}V^B\cap\Loc_\mathrm{Adam}times\+N^k.  Any edge from the
energy semantics that would bring to a configuration $\ell\vec v)$
with $\vec v(i)\geq B$ for some $1\leq i\leqk leads instead to the
sink.  All the configurations in this arena have norm less than $B$,
thus $|V^B|=|\?L B^k1$, and the qualitative games of
Chapter {ref}`2-chap:regular` are decidable over this arena.

Our focus here is on non-termination games played on the "bounded
semantics" where $B$ is not given as part of the input, but quantified
existentially.  As usual, the existential initial credit variant
of \cref{11-pb:bounding} is obtained by quantifying $\vec v_0$
existentially in the question.
\decpb[bounding game with given initial credit]
{\label{11-pb:bounding} A vector system
  $\?V=(\?LA\Loc_\mathrm{Eve}\Loc_\mathrm{Adam}k$, an initial location
  $\loc_0\in\?L, and an initial credit $\vec v_0\in\+N^k.}
  {Does there exist $B\in\+N$ such that \textrm{Eve} has a strategy to avoid the
  sink $\bot from $\loc_0(\vec v_0)$ in the "bounded
  semantics"?  That is, does there exist $B\in\+N$ such that she wins
  the bounding game $(\arena_B\?V),\textsf{col}\mathtt{Safe}$ from
  $\loc_0(\vec v_0)$, where $\textsf{col}e)\eqby{def}Lose$ if and only if $\textrm{In}e)=\bot?}

````{prf:lemma} NEEDS TITLE 11-lem:parity2bounding
:label: 11-lem:parity2bounding

  There is a \logspace\ reduction from parity@parity vector games
  asymmetric vector games to bounding games, both with given
  and with existential initial credit.

````

````{admonition} Proof
:class: dropdown tip

  Given an asymmetric vector system
  $\?V=(\?LA\Loc_\mathrm{Eve}\Loc_\mathrm{Adam}k$, a location colouring
  $\mathrm{lcol}:}\,\?Lto\{1,\dots,2d\}$, and an initial location
  $\loc_0\in\?L, we construct a vector system $\?V'$ of dimension
  $k\eqby{def}dd+d$ as described in {numref}`11-fig:bounding`, where the
  priorities in $\?V$ for $p\in\{1,\dots,d\}$ are indicated above the
  corresponding locations.
  
  
```{figure} ./../FigAndAlgos/11-fig:bounding.png
:name: 11-fig:bounding
:align: center
Schema of the reduction to
      bounding games in the proof of  {prf:ref}`11-lem:parity2bounding`.
```
  
  If \textrm{Eve} wins the bounding game played over $\?V'$ from some
  configuration $\loc_0(\vec v_0)$, then she also wins the "parity
  vector game" played over $\?V$ from the configuration $\loc_0(\vec
  v'_0)$ where $\vec v'_0$ is the projection of $\vec v_0$
  to $\+N^k.  Indeed, she can play essentially the same strategy:
  by  {prf:ref}`11-lem:mono` she can simply ignore the new decrement
  self loops, while the actions on the components in
  $\{k1,\dots,kd\}$ ensure that the maximal priority visited
  infinitely often is even---otherwise some decrement $-\vec
  e_{kp}$ would be played infinitely often but the increment $\vec
  e_{kp}$ only finitely often.\todoquestion{Should I provide more details?}
  

  \medskip
  Conversely, consider the parity@parity vector game game $\mathcal{G} played over
  $\natural(\?V)$ with the colouring defined by $\mathrm{lcol}.  Then the
  Pareto limit of the game is finite, thus there exists a natural
  number
  \begin{equation}\label{11-eq:b0}
    B_0\eqby{def}1+\max_{\loc_0(\vec v_0)\in\mathsf{Pareto}(\?G)}\|\vec
  v_0\|
  \end{equation} bounding the norms of the minimal winning configurations.
  For a vector $\vec v$ in $\+N^k, let us write $\capp[B_0]v$ for
  the vector `capped' at $B$: for all $1\leq i\leqk,
  $\capp[B_0]v(i)\eqby{def}vec v(i)$ if $\vec v(i)<B_0$ and
  $\capp[B_0]v\eqby{def}B_0$ if $\vec v(i)\geq B_0$.

  
  
  
  
  
  
  
  

  Consider now some configuration $\loc_0(\vec
  v_0)\in\mathsf{Pareto}(\mathcal{G}$.  As seen in  {prf:ref}`11-lem:finmem`,
  since $\loc_0(\vec v_0)\inW_\mathrm{Eve}mathcal{G}$, there is a finite
  self-covering tree witnessing the fact, and an associated winning
  strategy.  Let $H(\loc_0(\vec v_0))$ denote the height of this
  self-covering tree and observe that all the configurations in this
  tree have norm bounded by $\|\vec v_0\|+\|A|\cdot H(\loc_0(\vec
  v_0))$.
  Let us define
  \begin{equation}\label{11-eq:b}
   B\eqby{def}B_0+(\|A|+1)\cdot \max_{\loc_0(\vec
  v_0)\in\mathsf{Pareto}(\?G)}H(\loc_0(\vec v_0))\;.
  \end{equation}
  This is a bound on the norm of the configurations appearing on the
  (finitely many) self-covering trees spawned by the elements
  of $\mathsf{Pareto}(\mathcal{G}$.  Note that $B\geq B_0+(\|A|+1)$ since
  a self-covering tree has height at least~one.

  Consider the non-termination game
  $\game_B\eqby{def}\arena_B\?V'),\textsf{col},\mathtt{Safe}$ played over the
  bounded semantics defined by $B$, where $\textsf{col}(e)=\textrm{Lose} if and
  only if $\textrm{In}e)=\bot.  Let $\vec b\eqby{def}sum_{1\leq p\leq
  d}(B-1)\cdot\vec e_{kp}$.
  {\renewcommand{\qedsymbol}{}
  \begin{claim}\label{11-cl:parity2bounding} If $\loc_0(\vec
    v)\inW_\mathrm{Eve}mathcal{G}$, then
    $\loc_0(\capp[B_0]{v}+\vec b)\inW_\mathrm{Eve}game_B)$.
  \end{claim}}
  Indeed, by definition of the "Pareto
  limit" $\mathsf{Pareto}(\mathcal{G}$, if $\loc_0(\vec v)\inW_\mathrm{Eve}mathcal{G}$,
  then there exists $\vec v_0\leq\vec v$ such that $\loc_0(\vec
  v_0)\in\mathsf{Pareto}(\mathcal{G}$.  By definition of the bound $B_0$,
  $\|\vec v_0\|<B_0$, thus $\vec v_0\leq\capp[B_0]v$.  Consider the
  self-covering tree of height $H(\loc_0(\vec v_0))$ associated
  to $\loc_0(\vec v_0)$, and the strategy $\sigma'$ defined by the
  memory structure from the
  proof of  {prf:ref}`11-lem:finmem`.  This is a winning strategy for \textrm{Eve}  in $\mathcal{G} starting from $\loc_0(\vec v_0)$, and
  by  {prf:ref}`11-lem:mono`, it is also winning
  from $\loc_0(\capp[B_0]v)$.
    
  Here is how \textrm{Eve} wins $\game_B$ from $\loc_0(\capp[B_0]v+\vec b)$.
  She essentially follows the strategy $\sigma'$, with two
  modifications.  First, whenever $\sigma'$ goes to a return node
  $\ell\vec v)$ instead of a leaf $\ell\vec v')$---thus $\vec
  v\leq\vec v'$---, the next time \textrm{Eve} has the control, she uses the
  self loops to decrement the current configuration by $\vec v'-\vec
  v$.  This ensures that any play consistent with the modified
  strategy remains between zero and $B-1$ on the components
  in $\{1,\dots,k}$.  (Note that if she never regains the control,
  the current vector never changes any more since $\?V$ is
  asymmetric.)

  Second, whenever a play in $\mathcal{G} visits a location with even
  parity $2p$ for some $p$ in $\{1,\dots,d\}$, \textrm{Eve} has the opportunity
  to increase the coordinates in $\{k1,\dots,kp\}$ in $\game_B$.
  She does so and increments until all these components reach $B-1$.
  This ensures that any play consistent with the modified strategy
  remains between zero and $B-1$ on the components
  in $\{k1,\dots,kp\}$.  Indeed, $\sigma'$ guarantees that the
  longest sequence of moves before a play visits a location with
  maximal even priority is bounded by $H(\loc_0(\vec v_0))$, thus the
  decrements $-\vec e_{kp}$ introduced in $\game_B$ by the
  locations from $\mathcal{G} with odd parity $2p-1$ will never force the
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
exists a suitable initial credit such that \textrm{Eve} wins the game if and
only if she wins the finite reachability game played over the
underlying directed graph over $\?L where we ignore the counters.
Thus, for an initial location $\loc_0$, $B_0=|\?L\cdot\|A|+1$
bounds the norm of the necessary initial credit, while a simple path
may visit at most $|\?L$ locations, thus
$B=B_0+|\?L\cdot\|A|$ suffices for \textrm{Eve} to win the constructed
bounding game.

In the general case of bounding games with "existential initial
credit", an explicit bound can be established.  The proof goes
along very different lines and is too involved to fit in this chapter,
but we refer the reader
to {cite}`Jurdzinski&Lazic&Schmitz:2015,Colcombet&Jurdzinski&Lazic&Schmitz:2017`
for details.

````{prf:theorem} Bounds on bounding
:label: 11-th:bounding

  If \textrm{Eve} wins a bounding game with existential initial credit
  defined by a "vector
  system" $\?V=(\?LA\Loc_\mathrm{Eve}\Loc_\mathrm{Adam}k$, then an
  initial credit $\vec v_0$ with $\|\vec
  v_0\|=(4|\?L\cdot\|A|)^{2(k2)^3}$ and a bound
  $B=2(4|\?L\cdot\|A|)^{2(k2)^3}+1$ suffice for this.

````

\Cref{11-th:bounding} also yields a way of handling bounding games
with given initial credit.  
\TODO{Last missing bit regarding complexity upper bounds.}
  

