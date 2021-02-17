(9-sec:notations)=
# Notations

```{math}
\usepackage{amsmath}
  
\newcommand*\Realnn{\mathbb{R}_{\geq 0}}
\newcommand*\Clocks{\mathcal{C}}
\newcommand*\TA{\ensuremath{\mathcal{A}}}
\newcommand*\Locs{\mathcal{L}}
\newcommand*\Clocksz{\mathcal{C}_0}
\newcommand*\calQ{\mathcal{Q}}
\newcommand*\state{\mathsf{state}}
\newcommand*\trans{\mathsf{trans}}
\newcommand*\post{\mathsf{post}}
\newcommand*\step{\mathsf{step}}
\newcommand*\postta{\ensuremath{\textrm{\sf Post}}}
\newcommand*\preta{\ensuremath{\textrm{\sf Pre}}}
\newcommand*\unreset{\ensuremath{\textrm{\sf Unreset}}}
\newcommand*\posttime{\ensuremath{\textrm{\sf Post}_{\geq 0}}}
\newcommand*\pretime{\ensuremath{\textrm{\sf Pre}_{\geq 0}}} \newcommand*\reset{\mathsf{Reset}}
\newcommand{\sem}[1]{\ensuremath{#1}}
\newcommand{\size}[1]{\ensuremath{|#1|}}

\def\predc{\textrm{\sf Pred}_c}
\def\predt{\textrm{\sf Pred}_{\geq 0}} \def\predu{\textrm{\sf Pred}_u}
\def\calP{\mathcal P}
\def\calC{\mathcal C}
\def\calT{\mathcal T}
\def\Dep{\textsf{Dep}}
\def\Wait{\textsf{Wait}}
\def\Passed{\textsf{Passed}}
\def\Act{\textsf{Act}}
\def\EA{E_{\Adam}}
\def\EE{E_{\Eve}}

\newcommand\zone[1]{\ensuremath{\left\llbracket#1\right\rrbracket}}
\def\NM#1{\textcolor{green!50!black}{\checkmark}\marginpar{\color{green!50!black}NM: #1}} 
\long\def\NMlong#1{\medskip\par{\color{green!50!black}NM: #1}\medskip\par}
\def\OS#1{\textcolor{blue!50!black}{\checkmark}\marginpar{\color{blue!50!black}OS: #1}} 
\long\def\OSlong#1{\medskip\par{\color{blue!50!black}OS: #1}\medskip\par}

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
We~fix a finite set $\Clocks$ of clock variables to be used
in our timed games. Elements of $\Realnn^\Clocks$, which assign a
value to each clock, are called **valuations**.

Clocks will be used to define **clock constraints**, which in turn
are used in timed automata to restrict the set of allowed behaviours:
edges are decorated with clock constraints defining conditions for
their availability.%under which this edge $e$ is available.An~**atomic clock constraint** is a formula of the form $k \preceq
x \preceq' l$ or $k \preceq x - y \preceq' l$ where $x,y \in \Clocks$,
$k,l \in \mathbb{Z}\cup\{-\infty,\infty\}$ and
${\mathord\preceq,\mathord\preceq' \in
  \{\mathord<,\mathord\leq\}}$. A~**clock constraint** is a
conjunction of atomic clock constraints.  A~valuation $\nu\colon
\Clocks\to\Realnn$ satisfies a clock constraint $g$, denoted $\nu \models g$,
if~all atomic clock constraints are satisfied when each $x\in \Clocks$
is replaced with its value $\nu(x)$.  We~write $\Phi_\Clocks$ for the
set of clock constraints built on the clock set $\Clocks$.


For a subset $R\subseteq \Clocks$ and a valuation $\nu$, we~denote
with ${\nu[R \leftarrow 0]}$ the valuation defined by ${\nu[R
    \leftarrow 0](x) = 0}$ if $x \in R$ and ${\nu[R\leftarrow 0](x) =
  \nu(x)}$ otherwise. Given $d \in \mathbb{R}_{\geq 0}$ and a
valuation $\nu$, the~valuation $\nu+d$ is defined by $(\nu+d)(x) =
\nu(x)+d$ for all $x\in \Clocks$. We~extend these operations to sets
of valuations in the obvious~way.
%graph just like regular arenas, but they additionally contain clock%defined as a~pair $(\ell,\nu)$ of a **location** $\ell$ and a%The configurations will become the vertices of the game % Hence, the game is played in an arena whose vertices are %a state of the underlying finite automaton, and $\nu$ a clock valuation.
%\OS{j'ai d\'efini vertex comme une paire $(\ell,\nu)$ pour faire commes les jeux finis.%Hence, the precise state of the arena is determined by the%thus call the vertices $\ell$ of the underlying finite graph%will be called **vertices**.

We now formally define **timed games**, which are finite
representations that define infinite-state, non-stochastic concurrent
games. 

````{prf:definition} NEEDS TITLE AND LABEL 
  A~**timed arena** $\calT$ is a tuple $(\Locs,
  \Clocks,\EE,\EA, c)$, where $\Locs$ is a finite set of locations,
  $\Clocks$~is a finite set of clocks, $\EE,\EA \subseteq \Locs \times
  \Phi_\Clocks \times 2^\Clocks \times \mathcal{L}$ are the sets of
  edges respectively controlled by \Eve and~\Adam,%  respectively, 
  and $c\colon \EE\cup\EA \to C$ is the coloring function.%the chapter also allows attaching them to states later.}
  A~**timed game** is a pair $(\calT,\Omega)$ where
  $\Omega \subseteq C^\omega$ a qualitative objective.
 

  A~**timed arena** $\calT$ is a tuple $(\Locs,
  \Clocks,\EE,\EA, c)$, where $\Locs$ is a finite set of locations,
  $\Clocks$~is a finite set of clocks, $\EE,\EA \subseteq \Locs \times
  \Phi_\Clocks \times 2^\Clocks \times \mathcal{L}$ are the sets of
  edges respectively controlled by \Eve and~\Adam,%  respectively, 
  and $c\colon \EE\cup\EA \to C$ is the coloring function.%the chapter also allows attaching them to states later.}
  A~**timed game** is a pair $(\calT,\Omega)$ where
  $\Omega \subseteq C^\omega$ a qualitative objective.

````

A~configuration of such a timed automaton is a pair $(\ell,\nu)$ where
$\ell\in\Locs$ and $\nu\colon \Clocks\to\Realnn$.  The~set of
configurations is the set of vertices of the infinite-state game
defined by $\calT$.%$c'((\ell,\nu)) = c(\ell)$.

The~actions of both players are pairs $(d,e)$ where $d\in\Realnn$ is a
delay they want to wait before playing their controlled
action $e$. Action $(d,e)$ is available for~\Eve (resp.~\Adam) in
configuration $(\ell,\nu)$ if $e\in\EE(\ell)$ (resp. $e\in\EA(\ell)$)
and, writing $e=(\ell,g,R,\ell')$, if additionally $\nu+d\models g$;
in~other terms, the~clock constraint (called~**guard**~hereafter)
on $e$ must hold true under the clock valuation reached after elapsing
$d$ time units. We~add an extra dummy action $\bot$ for the case where
some player has no available action (this~action is only available if
no other actions~are).

Once both players have selected an action available from
configuration $(\ell,\nu)$, the action $(d,e)$ with smallest delay is
performed (by breaking ties in favor of Adam), leading to configuration $(\ell',(\nu+d)[R\leftarrow 0])$:
this corresponds to letting $d$ time units elapse, thereby reaching
configuration $(\ell,\nu+d)$, and to following edge $e$ (which by
construction is available from $(\ell,\nu+d)$).  We~define
$\step((\ell,\nu),(d,e))$ for the configuration
$(\ell',(\nu+d)[R\leftarrow 0])$ reached from $(\ell,\nu)$ by applying
action $(d,e)$.


This definition captures the concurrent nature of the interaction
between a controller~(\Eve) and its environment~(\Adam) in a real-time
system, since none of the players knows in advance how long the
opponent will want to wait before performing her transition.
The~semantics of a timed arena $(\Locs, \Clocks,\EE,\EA)$ can then
formally be defined in terms of a concurrent arena (following the
definition of \cref{sec-concurrent-def}).  The~underlying
graph $(V,E)$ is such that $V=\Locs\times \Realnn^{\Clocks}$, and $E=
V\times C\times V$; the~set of actions of~\Eve is $\Realnn\times\EE$, and that
of~\Adam is $\Realnn\times\EA$; finally, the transition function,
which is not stochastic in our case, maps any
configuration $(\ell,\nu)$ and pair of actions $(d_\Eve,e_\Eve)$ and
$(d_\Adam,e_\Adam)$ to the edge $((\ell,\nu),\gamma,
\step((\ell,\nu),(d,e)))$, where $(d,e)=(d_\Eve,e_\Eve)$ and $\gamma=c(e_\mEve)$
if
$d_\Eve<d_\Adam$,  and $(d,a)=(d_\Adam,e_\Adam)$ and $\gamma=c(e_\mAdam)$ otherwise.%infinite-state concurrent game in the natural way:

A~path in a timed arena $\calT$ then is a path in its
associated infinite-state concurrent arena. The~qualitative
objective $\Omega$ can then be evaluated along runs of a timed arena in
the natural way.
%\NM{definition written to stick to that of \cref{chap:concurrent}.Contrary to~\cref{chap:concurrent}, in this chapter we~only consider
deterministic strategies% in timed games have never been studied.

```{margin}
Adding randomization over the
  infinite sets of actions is beyond the scope of this chapter.
```

}.%On enleve le footnote? Ou bien on dit ca a ete peu etudie avec la ref.}%the end of this chapter.}.
  As~a result, timed games are not
determined, as illustrated in the following example.

```{figure} ./../FigAndAlgos/9-fig:ta2.png
:name: 9-fig:ta2
:align: center
Timed arena $\TA_2$. Solid arrow is Eve's, dashed one is Adam's.
```



````{prf:example} NEEDS LABEL Timed Games are not Determined
  In the timed arena $\TA_2$ defined in {numref}`9-fig:ta2`, from configuration $(\ell_0,\vec{0})$, \Eve does not have a winning strategy to reach location $\ell_1$, but \Adam does not have a winning strategy either to avoid $\ell_1$.
  In fact, available moves for both players consist in $(d,(\ell_0,\ell_1))$ with $0< d<1$ for \Eve, and $(d',(\ell_0,\ell_2))$ with $0< d' < 1$ for~\Adam.
  Thus, for any particular delay $0<d<1$ chosen by~\Eve, \Adam has a possible delay $d<d'<1$ which leads to $\ell_2$, which is losing for~\Eve.
  This shows that \Eve does not have a winning strategy.
  The argument is however symmetric, and \Adam also does not have a winning strategy to avoid $\ell_1$.
  Timed games are thus non determined.

````



%Although the infinite-state concurrent games we defined above

%V$ with $q_1 = (\ell_0,\vec{0})$ and %there exists $e_i \in E$ and $d\geq 0$ with $q_{i+1} = \step(q_i,(d,e_i))$.%$V_{\Eve}$ with no possible successor.%as a function $f\colon V^* \rightarrow \Realnn \times \EE$%is a valid move at $q_k$.
%strategy $f$} is defined as the set of maximal runs $\rho$ such that%  \item $\rho_1 = (\ell_0,\vec{0})$,%\end{enumerate}%Given a target%define $\Omega(T)$ as the set of maximal runs that visit $T$ at least once.

````{prf:example} NEEDS LABEL Winning strategy on running example
Let us consider again the example of {numref}`9-fig:ta1` and see whether Eve
has a winning strategy from the initial configuration.
At the initial configuration $\ell_1,x=0$, \Eve needs to make a move towards $\ell_2$
while $x\leq 1$ since whenever $x>1$, \Adam can move to $\ell_5$ which guarantees \Eve's lost.
Assume the game proceeds to $\ell_2$ with any value $x\leq 1$. Here, \Eve can try to wait
until $x\geq 2$ and go to $G$. However, if $x<1$, then \Adam can move to $\ell_3$.
From this location, \Eve can guarantee to come back to $\ell_2$ with $x=1$, and then move to $G$ and win the game.
Assume now that from $\ell_1$, the game proceeds to $\ell_3$ with $x=0$ due to~\Adam's move.
Again, \Eve can wait for 1 time unit, and go back to $\ell_2$ with $x=1$, and win the game.Hence, \Eve has a winning strategy from $\ell_1$ for all $x\leq 1$, and from $\ell_2$
for all values of $x$.

````


In this chapter, the main problem we are interested in is determining
whether \Eve has a strategy for her reachability objective.
Let $\vec{0}$ denote the clock valuation assigning $0$ to all clocks.

\begin{problem}
  Given a timed arena $\calT$, initial location $\ell_0$, and a
  reachability objective $\Reach(\Win)$,
  decide whether \Eve has a
  winning strategy in $(\calT,\Reach(\Win))$ from
  configuration $(\ell_0,\vec{0})$.
\end{problem}

The difficulty of this problem is that the concurrent
game $((V,E),\Delta,\Omega)$ has an infinite state-space, and players
have infinitely many actions.  We~thus start by studying a data
structure to represent sets of states and operations to compute
successors and predecessors on these sets.  We then give two
algorithms to solve the above problem.  We~also show how such a
strategy for \Eve can be computed and finitely represented.
