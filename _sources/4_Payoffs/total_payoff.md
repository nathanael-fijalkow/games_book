(4-sec:total_payoff)=
# Total payoff games

```{math}
\newcommand{\FC}{\mathrm{FC}\xspace} 
\newcommand{\Cycles}{\mathrm{Cycles}\xspace} 
\newcommand{\Mean}{\mathrm{Mean}\xspace} 
\newcommand{\FirstCycle}{\mathrm{FirstCycle}\xspace} 
\newcommand{\SuffixAllCycles}{\mathrm{SuffixAllCycles}\xspace} 
\newcommand{\FirstCycleReset}{\mathrm{FirstCycleReset}\xspace} 
\newcommand{\siblank}{\mathtt{-}}
\newcommand{\Lift}{\textrm{Lift}}
\newcommand{\Rbar}{\overline\R}
\newcommand{\downward}[1]{\mathop{\downarrow_{#1}}}
\newcommand{\gval}{\mathrm{gr}\text{-}\val}
\newcommand{\bigO}{O}\newcommand{\Eve}{\textrm{Eve}}
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
```
Yet another interesting quantitative objective---that is closely
related with shortest path objective---is the total payoff defined by

$$\TotalPayoff(\pi)=\limsup_{n} \sum_{i=0}^{n-1} c(\pi_i)$$

Contrary to the shortest path objective, total payoff games have no
reachability objective intertwined with the quantitative objective. In
particular, all plays will be infinite (if there are no deadlocks in
the arena, which we suppose without loss of generality) and their
payoff is the superior limit of the partial sums: we need this
superior limit since partial sums might not have a limit (consider for
instance the sequence of costs $1,-1,1,-1,1,\ldots$ whose partial sums
alternate between $1$ and $0$).

This objective is also closely related to the mean payoff, in the
sense that it refines the mean payoff objective. Indeed, notice that
the total payoff of a play is finite if and only if the mean payoff of
this play is null. Then, the total payoff enables a finer, two-stage
analysis of a game: first, compute the mean payoff of a given start
vertex $v$; then subtract this value from all edge weights and scale
the resulting weights if necessary to obtain integers (the resulting
game has now mean payoff 0 starting from $v$); finally, compute the
(finite) total payoff of the new game to quantify how the partial sums
are fluctuating around the mean payoff of the original game. For
instance, this allows one to distinguish situation
$1,-1,1,-1,1,\ldots$ where the total payoff is $1$ from a close
situation $-1,1,-1,1,\ldots$ with total payoff $0$: this could be seen
as a budget constraint that players must satisfy in order to be able
to survive the game. Total payoff is therefore also closely related to
**energy games** where Eve tries to optimise its energy consumption
(again computed with partial sums) while keeping at all time the
energy level above $0$. However, no trivial reduction exist to encode
total payoff games into energy games (that will be solved
in~\cref{chap:counters})

It should not be surprising that total payoff games are determined
but, contrary to shortest path games, positional strategies are now
sufficient for both players to play optimally in total payoff
games. Instead of giving yet another distinct proof, like for
mean payoff or discounted payoff games, we give a general recipe
defined by Gimbert and Zielonka {cite}`Gimbert&Zielonka:2004`. They define
sufficient conditions for a quantitative objective to fulfil the
positional determinacy.

```{prf:definition} NEEDS TITLE 4-def:fairly-mixing
:label: 4-def:fairly-mixing

  A payoff $\mathsf{P}\colon C^\omega\to \overline R$ is **fairly
    mixing** if:
  
  
1.  for all $x\in C^+$, $y_0,y_1\in C^\omega$, if
    $\mathsf{P}(y_0)\leq \mathsf{P}(y_1)$ then
    $\mathsf{P}(xy_0)\leq \mathsf{P}(xy_1)$;
  
2.  for all $x\in C^+$, $y\in C^\omega$,
    $\min(\mathsf{P}(x^\omega),\mathsf{P}(y)) \leq \mathsf{P}(xy)\leq
    \max(\mathsf{P}(x^\omega),\mathsf{P}(y))$;
  
3.  if $(x_i)_{i\in \N}$ is a sequence of non-empty words
    $x_i\in C^+$ such that $x_0x_1x_2\cdots$ contains only a finite
    number of colours, and $I\uplus J=\N$ is a partition of $\N$ into two
    infinite sets, then
    

$$\inf(\mathcal{P}_I\cup \mathcal{P}_J) \leq
      \mathsf{P}(x_0x_1x_2\cdots) \leq \sup(\mathcal{P}_I\cup
      \mathcal{P}_J)$$

 with
    $\mathcal P_I=\{\mathsf{P}(x_{i_0}x_{i_1}x_{i_2}\cdots)\mid i_k\in
    I\}$ and
    $\mathcal{P}_J=\{\mathsf{P}(x_{j_0}x_{j_1}x_{j_2}\cdots)\mid
    j_k\in J\}$.
  

```

It is not difficult to convince oneself that

```{prf:proposition} NEEDS TITLE 4-prop:objectives-fairly
:label: 4-prop:objectives-fairly

  Quantitative objectives $\Inf$, $\Sup$, $\LimInf$, $\LimSup$,
  $\Parity$ (mapping $1$ to sequences whose the greatest colour seen
  infinitely often is even), $\MeanPayoff$,
  $\DiscountedPayoff_\lambda$, $\TotalPayoff$ are fairly mixing
  payoffs.

```

Then, a rather technical proof by induction on the number of vertices
in the arena allows one to get the following strong result:
{cite}`Gimbert&Zielonka:2004`

```{prf:theorem} NEEDS TITLE 4-thm:fairly-mixing
:label: 4-thm:fairly-mixing

  If $\mathsf P$ is a fairly mixing payoff function, then all finite
  games $(\arena,\mathsf P)$ are positionally determined.

```


```{prf:corollary} NEEDS TITLE 4-cor:TP-determinacy
:label: 4-cor:TP-determinacy

  Total payoff games are positionally determined.

```

In particular, it gives $\NP\cap\coNP$ complexity to solve
total payoff games, since one-player total payoff games can be solved
in polynomial time using Floyd-Warshall algorithm to compute all-pairs
shortest path in a weighted graph. Obtaining a deterministic algorithm
is nonetheless not as immediate as before, using the operator
$F\colon \R^V\to \R^V$ mapping every vector $\vec x=(x_v)_{v\in V}$
towards the new vector $(y_v)_{v\in V}$, defined, for all $v\in V$,
by:

$$y_v =
  \begin{cases}
    \max_{(v,v')\in E} [c(v,v') + x_{v'}] &
    \text{ if } v\in \VE\\
    \min_{(v,v')\in E} [c(v,v') + x_{v'}] & \text{ if } v\in \VA
  \end{cases}$$


Indeed, this operator may have several fixed points, and even more
problematic is the fact that the value of the game may be different
from the greatest and lowest fixed points, forbidding to find the
correct fixed point easily. Consider for example the total payoff game
of {numref}`4-fig:totalpayoff`. Operator $F$ is then
$F(x_0,x_1,x_2) = \big(\max(x_1-1,x_2-2),x_0+1,x_0+2\big)$. Its fixed
points are all vectors $(a,a+1,a+2)$ with $a\in \overline R$: in
particular, its greatest fixed point is $(+\infty, +\infty, +\infty)$
and its lowest fixed point is $(-\infty, -\infty, -\infty)$. However,
the optimal value vector is $(0,1,2)$.

Instead, to compute the value, a computation based on two nested fixed
points exists, relying upon the encoding of a total payoff game into a
pseudopolynomial size shortest path game---still with the same
costs---resulting in a pseudopolynomial time algorithm.
{cite}`Brihaye&Geeraerts&HaddadA&Monmege:2017`

```{prf:theorem} NEEDS TITLE 4-thm:TP-optimal-strategies
:label: 4-thm:TP-optimal-strategies

  We can compute the optimal values of total payoff games, as well as
  positional optimal strategies for both players, with a
  pseudopolynomial time complexity.

```

```{admonition} Proof
:class: dropdown tip
[Sketch of proof]
  Let $\arena$ be the arena of the total payoff game. Consider an
  arena $\arena^k$ consisting of $k$ modified copies of $\arena$ as
  well as a fresh target vertex $v_f$: in the $j$-th copy of $\arena$
  (with $1\leq j\leq k$), every time an edge is taken, Adam has the
  opportunity (encoded via a copy of each vertex, owned by Adam) to
  exit the $j$-th copy when he wants, then giving the token to Eve
  that has the choice between continuing the game in the $(j-1)$-th
  copy (unless $j=1$) or stopping the game by jumping into the target
  $v_f$. In the first copy of the game, Eve has no choice but to allow
  Adam to stop whenever he decides. However, when $k$ increases, the
  fact that Eve can delay the stopping of the game for a great number
  of times precludes Adam to cheat by asking to stop while obtaining a
  too low value. We can prove, by a careful analysis, that the
  shortest path game played on arena $\arena^K$ with
  $K= n\big((2n-1)W +1\big)$ has a value equal to the
  total payoff game on arena $\arena$.

  By using the previous value iteration techniques, we obtain a
  pseudopolynomial time algorithm to compute the optimal values in
  the total payoff game. Instead of building the entire arena
  $\arena^k$, we can benefit from the multiple copies of the same
  sub-arena to emulate the construction with an operator $H$ mapping
  the values of each vertex in the $k$-th copy, to the values of each
  vertex in the $k+1$-th copy (operator $H$ does not depend on
  $k$). Because Eve (the maximiser player) is the one that is
  responsible for allowing to exit the game or not, the actual value
  of the $k$-th copy is obtained by $H^k(\bot)$, with $\bot$ the
  vector with all components being $-\infty$. The computation of $H$,
  that is a shortest path game whose output values depend on a given
  vector, depends on another fixed-point computation, as described
  before. This way, we improve the spacial complexity, without
  deteriorating the time complexity.

```



```{figure} ./../4-fig:totalpayoff.png
:name: 4-fig:totalpayoff
:align: center
A total payoff game
```

