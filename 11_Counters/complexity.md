(11-sec:complexity)=
# The complexity of asymmetric monotone games

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
Unlike general vector games and configuration reachability
asymmetric ones, coverability, non-termination, and
parity@parity vector game asymmetric vector games are decidable.
We survey in this section the best known complexity bounds for every
case; see \cref{11-tbl:cmplx} at the end of the chapter for a summary.

(11-sec:up)=
## Upper Bounds
We begin with complexity upper bounds.  The main results are that
parity@parity vector game games with existential initial credit
can be solved in \coNP, but are in \kEXP[2] with "given initial
credit".  In both cases however, the complexity is pseudo-polynomial
if both the dimension $\dd$ and the number of priorities $d$ are
fixed, which is rather good news: one can hope that, in practice, both
the number of different resources (encoded by the counters) and the
complexity of the functional specification (encoded by the parity
condition) are tiny compared to the size of the system.


(11-sec:up-exist)=
### Existential Initial Credit

> **Counterless Strategies**

Consider a strategy $\tau$ of \Adam\ in a vector game.  In all the
games we consider, uniform positional strategies suffice over the
infinite arena $\natural(\?V)=(V,E,\VE,\VA)$: $\tau$ maps vertices
in $V$ to edges in $E$.  We call $\tau$ counterless if, for all
locations $\loc\in\Loc_\mAdam$ and all vectors
$\vec v,\vec v'\in\+N^\dd$, $\tau(\loc(\vec v))=\tau(\loc(\vec v'))$.
A counterless strategy thus only considers the current location of
the play.

````{prf:lemma} Counterless strategies
:label: 11-lem:counterless

  Let $\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,\dd)$ be an "asymmetric
  vector system", $\loc_0\in\Loc$ be a location, and
  $\lcol{:}\,\Loc\to\{1,\dots,d\}$ be a location colouring.  If \Adam
  wins from $\loc_0(\vec v)$ for every initial credit $\vec v$ in the
  parity@parity vector game game played over $\?V$ with $\lcol$, then
  he has a single counterless strategy such that he wins from
  $\loc_0(\vec v)$ for every initial credit $\vec v$.

````

````{admonition} Proof
:class: dropdown tip

  Let $\Act_\mAdam\eqdef\{(\loc\step{\vec
    u}\loc')\in\Act\mid\loc\in\Loc_\mAdam\}$ be the set of actions
  controlled by \Adam.  We assume without loss of generality that
  every location $\loc\in\Loc_\mAdam$ has either one or two outgoing
  actions, thus $|\Loc_\mAdam|\leq|\Act_\mAdam|\leq
  2|\Loc_\mAdam|$.  We proceed by induction over $|\Act_\mAdam|$.  For
  the base case, if $|\Act_\mAdam|=|\Loc_\mAdam|$ then every location
  controlled by \Adam\ has a single outgoing action, thus any
  strategy for \Adam\ is trivially counterless.

  For the induction step, consider some location
  $\hat\loc\in\Loc_\mAdam$ with two outgoing actions
  $a_l\eqdef\hat\loc\step{\vec 0}\loc_l$ and
  $a_r\eqdef\hat\loc\step{\vec 0}\loc_r$.  Let $\?V_l$ and $\?V_r$ be
  the vector systems obtained from $\?V$ by removing
  respectively $a_r$ and $a_l$ from $\Act$, i.e., by using
  $\Act_l\eqdef\Act\setminus\{a_r\}$ and
  $\Act_r\eqdef\Act\setminus\{a_l\}$.  If $\Adam$ wins the
  parity@parity vector game game from $\loc(\vec v)$ for every
  initial credit $\vec v$ in either $\?V_l$ or $\?V_r$, then by
  induction hypothesis he has a counterless winning strategy winning
  from $\loc(\vec v)$ for every initial credit $\vec v$, and the same
  strategy is winning in $\?V$ from $\loc(\vec v)$ for every initial
  credit $\vec v$.

  In order to conclude the proof, we show that, if \Adam\ loses in
  $\?V_l$ from $\loc_0(\vec v_l)$ for some $\vec v_l\in\+N^\dd$ and in
  $\?V_r$ from $\loc_0(\vec v_r)$ for some $\vec v_r\in\+N^\dd$, then
  there exists $\vec v_0\in\+N^\dd$ such that \Eve\ wins from
  $\loc_0(\vec v_0)$ in $\?V$.  Let $\sigma_l$ and $\sigma_r$ denote
  \Eve's winning strategies in the two games.  By a slight abuse of
  notations (justified by the fact that we are only interested in a
  few initial vertices), we see plays as sequences of actions and
  strategies as maps $\Act^\ast\to\Act$.\todoquestion{I hope this is not too messy}  Consider the set of
  plays consistent with $\sigma_r$ starting from $\loc_0(\vec v_r)$.
  If none of those plays visits $\hat\loc$, then $\Eve$ wins in $\?V$
  from $\loc_0(\vec v_r)$ and we conclude.  Otherwise, there is some
  finite prefix $\hat\pi$ of a play that
  visits $\hat\loc(\hat{\vec v})$ for some vector
  $\hat{\vec v}=\vec v_r+\weight(\hat\pi)$.  We let
  $\vec v_0\eqdef\vec v_l+\hat{\vec v}$ and show that \Eve\ wins from
  $\loc_0(\vec v_0)$.

  \begin{scope}    We define now a strategy $\sigma$ for $\Eve$ over $\?V$ that
    switches between applying $\sigma_l$ and $\sigma_r$ each time
    $a_r$ is used and switches back each time $a_l$ is used.  More
    precisely, given a finite or infinite sequence $\pi$ of actions,
    we decompose $\pi$ as $\pi_1 a_1 \pi_2 a_2 \pi_3\cdots$ where each
    segment $\pi_j\in(\Act\setminus\{a_l,a_r\})^\ast$ does not use
    either $a_l$ nor $a_r$ and each $a_j\in\{a_l,a_r\}$.  The
    associated mode $m(j)\in\{l,r\}$ of a segment $\pi_j$
    is $m(1)\eqdef l$ for the initial segment and otherwise
    $m(j)\eqdef l$ if $e_{j-1}=a_l$ and $m(j)\eqdef r$ otherwise.  The
    $l$-subsequence associated with $\pi$ is the sequence of segments
    $\pi(l)\eqdef\pi_{l_1}a_{l_2-1}\pi_{l_2}a_{l_3-1}\pi_{l_3}\cdots$
    with mode $m(l_i)=l$, while the $r$-subsequence is the sequence
    $\pi(r)\eqdef\hat\pi a_{r_1-1}\pi_{r_1}a_{r_2-1}\pi_{r_2}\cdots$
    with mode $m(r_i)=r$ prefixed by $\hat\pi$.  Then we let
    $\sigma(\pi)\eqdef\sigma_{m}(\pi(m))$ where $m\in\{l,r\}$ is the
    mode of the last segment of $\pi$.

    Consider an infinite play $\pi$ consistent with $\sigma$ starting
    from $\loc_0(\vec v_0)$.  Since $\vec v_0\geq\vec v_l$ and
    $\vec v_0\geq \vec v_r+\weight(\hat\pi)$, $\pi(l)$ and $\pi(r)$
    starting from $\loc_0(\vec v_0)$ are consistent with
    simulating---in the sense of  {prf:ref}`11-lem:mono`---$\sigma_l$
    from $\loc_0(\vec v_l)$ and $\sigma_r$ from $\loc_0(\vec v_r)$.
    Let $\pi'$ be a finite prefix of $\pi$.  Then
    $\weight(\pi')=\weight(\pi'(l))+\weight(\pi'(r))$ where $\pi'(l)$
    is a prefix of $\pi(l)$ and $\pi'(r)$ of $\pi(r)$, thus
    $\weight(\pi'(l))\leq\vec v_l$ and
    $\weight(\pi'(r))\leq\vec v_r+\weight(\hat\pi)$, thus
    $\weight(\pi')\leq\vec v_0$: the play $\pi$ avoids the sink.
    Furthermore, the maximal priority seen infinitely often along
    $\pi(l)$ and $\pi(r)$ is even (note that one of $\pi(l)$
    and $\pi(r)$ might not be infinite), thus the maximal priority
    seen infinitely often along $\pi$ is also even.  This shows
    that $\sigma$ is winning for \Eve\ from $\loc_0(\vec v_0)$.\todoquestion{Is
    that clear?}
  \end{scope}

````

We are going to exploit  {prf:ref}`11-lem:counterless`
in \cref{11-th:exist-easy} in order to prove a~\coNP\ upper bound for
asymmetric games with existential initial credit: it suffices in
order to decide those games to guess a counterless winning
strategy $\tau$ for \Adam\ and check that it is indeed winning by
checking that \Eve\ loses the one-player game arising from $\tau$.
This last step requires an algorithmic result of independent interest.

> **One-player Case**

Let $\?V=(\Loc,\Act,\dd)$ be a vector addition system with states,
$\lcol{:}\,\Loc\to\{1,\dots,d\}$ a location colouring, and
$\loc_0\in\Loc$ an initial location.  Then \Eve\ wins the
parity@parity vector game one-player game from $\loc_0(\vec v_0)$
for some initial credit $\vec v_0$ if and only if there exists some
location such that

*  $\loc$ is reachable from $\loc_0$ in the directed graph
  underlying $\?V$ and
*  there is a cycle $\pi\in\Act^\ast$ from $\loc$ to itself such
  that $\weight(\pi)\geq 0$ and the maximal priority occurring
  along $\pi$ is even.

Indeed, assume we can find such a location $\loc$.  Let
$\hat\pi\in\Act^\ast$ be a path from $\loc_0$ to $\loc$ and $\vec
v_0(i)\eqdef\max\{\|\weight(\pi')\|\mid\pi'\text{ is a prefix of
}\hat\pi\pi\}$ for all $1\leq i\leq\dd$.  Then $\loc_0(\vec v_0)$ can
reach $\loc(\vec v_0+\weight(\hat\pi))$ in the natural semantics
of $\?V$ by following $\hat\pi$, and then $\loc(\vec v_0+\vec
W(\hat\pi)+n\weight(\pi))\geq \loc(\vec v_0+\weight(\hat\pi))$ after
$n$~repetitions of the cycle $\pi$.  The infinite play arising from
this strategy has an even maximal priority.

Conversely, if \Eve\ wins, then there is a winning play
$\pi\in\Act^\omega$ from $\loc_0(\vec v_0)$ for some $\vec v_0$.
Recall that $(V,{\leq})$ is a wqo, and we argue as in
 {prf:ref}`11-lem:finmem` that there is indeed such a location $\loc$.

\medskip
Therefore, solving one-player parity vector games boils down to
determining the existence of a cycle with non-negative effect and even
maximal priority.  We shall use linear programming techniques in order
to check the existence of such a cycle in polynomial
time {cite}`Kosaraju&Sullivan:1988`.

\medskip
\begin{scope}
Let us start with a relaxed problem: we call a
multi-cycle a non-empty finite set of cycles $\Pi$ and let
$\weight(\Pi)\eqdef\sum_{\pi\in\Pi}\weight(\pi)$ be its weight; we write
$t\in\Pi$ if $t\in\pi$ for some $\pi\in\Pi$.
Let $M\in 2^{\Act}$ be a set of `mandatory' subsets of actions and
$F\subseteq\Act$ a set of `forbidden' actions.  Then we say that
$\Pi$ is non-negative if $\weight(\Pi)\geq\vec 0$, and that it is
suitable for $(M,F)$ if for all $\Act'\in M$ there exists
$t\in\Act'$ such that $t\in\Pi$, and if for all $t\in F$,
$t\not\in\Pi$.  We use the same terminology for a single cycle $\pi$.

````{prf:lemma} Linear programs for suitable non-negative multi-cycles
:label: 11-lem:zmulticycle

  Let $\?V$ be a vector addition system with states,
  $M\in 2^{\Act}$, and $F\subseteq\Act$.  We can check in polynomial
  time whether $\?V$ contains a non-negative multi-cycle $\Pi$
  suitable for $(M,F)$.

````

````{admonition} Proof
:class: dropdown tip

  We reduce the problem to solving a linear program.  For a
  location $\loc$, let
  $\mathrm{in}(\loc)\eqdef\{(\loc'\step{\vec u}\loc)\in\Act\mid
  \loc'\in\Loc\}$
  and
  $\mathrm{out}(\loc)\eqdef\{(\loc\step{\vec u}\loc')\in\Act\mid
  \loc'\in\Loc\}$ be its sets of incoming and outgoing actions.  The
  linear program has a variable $x_a$ for each action $a\in\Act$,
  which represents the number of times the action $a$ occurs in
  the multi-cycle.  It consists of the following contraints:
  \begin{align*}
    \forall\loc&\in\Loc,&\sum_{a\in\mathrm{in}(\loc)}x_a&=\sum_{a\in\mathrm{out}(\loc)}x_a\;,\tag{multi-cycle}\\
    \forall a&\in\Act,&x_a&\geq 0\;,\tag{non-negative uses}\\
    \forall i&\in\{1,\dots,\dd\},&\sum_{a\in\Act} x_a\cdot\weight(t)(i)&\geq
                                            0\;,\tag{non-negative weight}\\
    &&\sum_{a\in\Act}x_a&\geq 0\tag{non empty}\\
    \forall \Act'&\in M,&\sum_{a\in\Act'}x_a&\geq 0\;,\tag{every subset
                                               in $M$ is used}\\
    \forall a&\in F,&x_a&= 0\;.\tag{no forbidden actions}
  \end{align*}
  As solving a linear program is in polynomial time {cite}``\todoquestion{agree
  on a ref with Chapter {ref}`8-chap:signal`?}, the result follows.

````

Of course, what we are aiming for is finding a non-negative
**cycle** suitable for $(M,F)$ rather than a multi-cycle.
Let us define for this the relation $\loc\sim\loc'$ over $\Loc$ if
$\loc=\loc'$ or if there exists a non-negative multi-cycle $\Pi$
suitable for $(M,F)$ such that $\loc$ and $\loc'$ belong to some
cycle $\pi\in\Pi$.
\begin{claim}\label{11-cl:sim} The relation $\sim$ is an equivalence
  relation.\end{claim}

````{admonition} Proof
:class: dropdown tip

  Symmetry and reflexivity are trivial, and if $\loc\sim\loc'$ and
  $\loc'\sim\loc''$ because $\loc$ and $\loc'$ appear in some cycle
  $\pi\in\Pi$ and $\loc'$ and $\loc''$ in some cycle $\pi'\in\Pi'$ for
  two non-negative multi-cycles $\Pi$ and $\Pi'$ suitable
  for $(M,F)$, then up to a circular shift $\pi$ and $\pi'$ can be
  assumed to start and end with $\loc'$, and then
  $(\Pi\setminus\{\pi\})\cup(\Pi'\setminus\{\pi'\})\cup\{\pi\pi'\}$ is
  also a non-negative multi-cycle suitable for $(M,F)$.

````

Thus $\sim$ defines a partition $\Loc/{\sim}$ of $\Loc$.
In order to find a non-negative cycle $\pi$ suitable for $(M,F)$,
we are going to compute the partition $\Loc/{\sim}$ of $\Loc$
according to $\sim$.  If we obtain a partition with a single
equivalence class, we are done: there exists such a cycle.  Otherwise,
such a cycle if it exists must be included in one of the subsystems
$(P,\Act\cap(P\times\+Z^\dd\times P),\dd)$ induced by the equivalence
classes $P\in\Loc/{\sim}$.  This yields {numref}`11-algo:zcycle`, which
assumes that we know how to compute the partition $\Loc/{\sim}$.  Note
that the depth of the recursion in {numref}`11-algo:zcycle` is bounded
by $|\Loc|$ and that recursive calls operate over disjoint subsets
of $\Loc$, thus assuming that we can compute the partition in
polynomial time, then {numref}`11-algo:zcycle` also works in polynomial
time.

```{figure} ./../FigAndAlgos/11-algo:zcycle.png
:name: 11-algo:zcycle
:align: center
$\text{cycle}(\?V,M,F)$
```

It remains to see how to compute the partition $\Loc/{\sim}$. Consider
for this the set of actions
$\Act'\eqdef\{a\mid\exists\Pi\text{ a non-negative multi-cycle
  suitable for $(M,F)$ with $a\in\Pi$}\}$ and
$\?V'=(\Loc',\Act',\dd)$ the subsystem induced by $\Act'$.
\begin{claim}
\label{11-cl:part}
  There exists a path from $\loc$ to $\loc'$ in $\?V'$
  if and only if $\loc\sim\loc'$.
\end{claim}

````{admonition} Proof
:class: dropdown tip

  If $\loc\sim\loc'$, then either $\loc=\loc'$ and there is an empty
  path, or there exist $\Pi$ and $\pi\in\Pi$ such that $\loc$
  and $\loc'$ belong to $\pi$ and $\Pi$ is a non-negative
  multi-cycle suitable for $(M,F)$, thus every action of $\pi$ is
  in $\Act'$ and there is a path in $\?V'$.  

  Conversely, if there is a path $\pi\in{\Act'}^\ast$ from $\loc$
  to $\loc'$, then $\loc\sim\loc'$ by induction on $\pi$.  Indeed, if
  $|\pi|=0$ then $\loc=\loc'$.  For the induction step, $\pi=\pi' a$
  with $\pi'\in{\Act'}^\ast$ a path from $\loc$ to $\loc''$ and
  $a=(\loc''\step{\vec u}\loc')\in\Act'$ for some $\vec u$.  By
  induction hypothesis, $\loc\sim\loc''$ and since $a\in\Act'$,
  $\loc''\sim\loc'$, thus $\loc\sim\loc'$ by transitivity shown
  in~\cref{11-cl:sim}. 

````

By \cref{11-cl:part}, the equivalence classes of $\sim$ are the
strongly connected components of $\?V'$.  This yields the following
polynomial time algorithm for computing $\Loc/{\sim}$.

```{figure} ./../FigAndAlgos/11-algo:part.png
:name: 11-algo:part
:align: center
$\text{partition}(\?V,M,F)$
```

Together,  {prf:ref}`11-lem:zmulticycle`
and {numref}`11-algo:part,11-algo:zcycle` yield the following.

````{prf:lemma} Polynomial-time detection of suitable non-negative cycles
:label: 11-lem:zcycle

  Let $\?V$ be a vector addition system with states,
  $M\in 2^{\Act}$, and $F\subseteq\Act$.  We can check in polynomial
  time whether $\?V$ contains a non-negative cycle $\pi$
  suitable for $(M,F)$.

````

Finally, we obtain the desired polynomial time upper bound for
parity@parity vector games in vector addition systems with states.

````{prf:theorem} Existential one-player parity vector games are in~\P
:label: 11-thm:zcycle

  Whether \Eve\ wins a one-player parity vector game with
  existential initial credit is in~\P.

````

````{admonition} Proof
:class: dropdown tip

  Let $\?V=(\Loc,\Act,\dd)$ be a vector addition system with states,
  $\lcol{:}\,\Loc\to\{1,\dots,$ $d\}$ a location colouring, and
  $\loc_0\in\Loc$ an initial location.  We start by trimming $\?V$ to
  only keep the locations reachable from $\loc_0$ in the underlying
  directed graph.  Then, for every even priority $p\in\{1,\dots,d\}$,
  we use  {prf:ref}`11-lem:zcycle` to check for the existence of a
  non-negative cycle with maximal priority $p$: it suffices for this
  to set $M\eqdef\{\lcol^{-1}(p)\}$ and
  $F\eqdef\lcol^{-1}(\{p+1,\dots,d\})$.

````

\end{scope}

> **Upper Bounds**

We are now equipped to prove our upper bounds.  We begin with a nearly
trivial case.  In a coverability asymmetric vector game with
existential initial credit, the counters play no role at all: \Eve
has a winning strategy for some initial credit in the vector game if
and only if she has one to reach the target location $\loc_f$ in the
finite game played over $\Loc$ and edges $(\loc,\loc')$ whenever
$\loc\step{\vec u}\loc'\in\Act$ for some $\vec u$.  This entails that
coverability asymmetric vector games are quite easy to solve.

````{prf:theorem} Existential coverability asymmetric vector games are in~\P
:label: 11-th:cov-exist-P

  Coverability asymmetric vector games with "existential initial
  credit" are \P-complete.

````

Regarding non-termination and parity@parity vector game, we
exploit  {prf:ref}`11-lem:counterless,11-thm:zcycle`.

````{prf:theorem} Existential parity asymmetric vector games are in~\coNP
:label: 11-th:exist-easy

  Non-termination and parity@parity vector game asymmetric
  vector games with existential initial credit are in~\coNP.

````

````{admonition} Proof
:class: dropdown tip

  By \cref{11-rk:nonterm2parity}, it suffices to prove the statement for
  parity@parity vector games games.  By  {prf:ref}`11-lem:counterless`,
  if \Adam\ wins the game, we can guess a counterless winning
  strategy $\tau$ telling which action to choose for every location.
  This strategy yields a one-player game, and by  {prf:ref}`11-thm:zcycle`
  we can check in polynomial time that $\tau$ was indeed winning
  for~\Adam.

````

Finally, in fixed dimension and with a fixed number of priorities, we
can simply apply the results of Section {ref}`11-sec:bounding`.

````{prf:corollary} Existential fixed-dimensional parity asymmetric vector games are pseudo-polynomial
:label: 11-cor:exist-pseudop

  Parity@parity vector game asymmetric vector games with
  existential initial credit are in pseudo-polynomial time if the
  dimension and the number of priorities are fixed.

````

````{admonition} Proof
:class: dropdown tip

  Consider an asymmetric vector system
  $\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,\dd)$ and a location
  colouring $\lcol{:}\,\Loc\to\{1,\dots,2d\}$.
  By  {prf:ref}`11-lem:parity2bounding`, the parity vector game with
  existential initial credit over $\?V$ problem reduces to a
  bounding game with existential initial credit over a "vector
  system" $\?V'=(\Loc',\Act',\Loc'_\mEve,\Loc'_\mAdam,\dd+d)$ where
  $\Loc'\in O(|\Loc|)$ and $\|\Act'\|=\|\Act\|$.
  By \cref{11-th:bounding}, it suffices to consider the case of a
  non-termination game with existential initial credit played over
  the bounded semantics $\bounded(\?V')$ where $B$ is in
  $(|\Loc'|\cdot\|\Act'\|)^{O(\dd+d)^3}$.  Such a game can be solved in
  linear time in the size of the bounded arena using attractor
  techniques, thus in $O(|\Loc|\cdot B)^{\dd+d}$, which is in
  $(|\Loc|\cdot\|\Act\|)^{O(\dd+d)^4}$ in terms of the original instance.

````


(11-sec:up-given)=
### Given Initial Credit
\TODO{Section {ref}`11-sec:up-given`}

````{prf:theorem} Upper bounds for asymmetric vector games
:label: 11-th:avag-easy

  Coverability, non-termination, and parity@parity vector game
  asymmetric vector games with given initial credit are in
  \kEXP[2].  If the dimension is fixed, they are in \EXP, and if the
  number of priorities is also fixed, they are in pseudo-polynomial
  time.

````



(11-sec:low)=
## Lower Bounds
Let us turn our attention to complexity lower bounds for monotonic
asymmetric vector games.  It turns out that most of the upper bounds
shown in Section {ref}`11-sec:up` are tight.

### Existential Initial Credit

In the existential initial credit variant of our games, we have the
following lower bound matching \cref{11-th:exist-easy}, already with a
unary encoding.

````{prf:theorem} Existential non-termination asymmetric vector games are \coNP-hard
:label: 11-th:exist-hard

  Non-termination, and parity@parity vector game
  asymmetric vector games with existential initial credit are
  \coNP-hard.

````

````{admonition} Proof
:class: dropdown tip

  By \cref{11-rk:nonterm2parity}, it suffices to show hardness for
  non-termination games.  We reduce from the \lang{3SAT} problem:
  given a formula $\varphi=\bigwedge_{1\leq i\leq m}C_i$ where each
  clause $C_i$ is a disjonction of the form
  $\litt_{i,1}\vee\litt_{i,2}\vee\litt_{i,3}$ of literals taken from
  $X=\{x_1,\neg x_1,x_2,$ $\neg x_2,\dots,x_k,\neg x_k\}$, we construct
  an asymmetric vector system $\?V$ where \Eve\ wins the
  non-termination game with existential initial credit if and only
  if $\varphi$ is not satisfiable; since the game is determined, we
  actually show that \Adam\ wins the game if and only if $\varphi$ is
  satisfiable.

  Our vector system has dimension $2k$, and for a literal
  $\litt\in X$, we define the vector
  \begin{equation*}
    \vec u_\litt\eqdef\begin{cases}
      \vec e_{2n-1}-\vec e_{2n}&\text{if }\litt=x_n\;,\\
      \vec e_{2n}-\vec e_{2n-1}&\text{if }\litt=\neg x_n\;.
    \end{cases}
  \end{equation*}
  We define $\?V\eqdef(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,2k)$ where
  \begin{align*}
    \Loc_\mEve&\eqdef\{\varphi\}\cup\{\litt_{i,j}\mid 1\leq i\leq m,1\leq j\leq
                3\}\;,\\
    \Loc_\mAdam&\eqdef\{C_i\mid 1\leq i\leq m\}\;,\\
    \Act&\eqdef\{\varphi\step{\vec 0}C_i\mid 1\leq i\leq m\}\cup\{C_i\step{\vec 0}\litt_{i,j},\;\;\litt_{i,j}\xrightarrow{\vec u_{\litt_{i,j}}}\varphi\mid 1\leq i\leq m,1\leq j\leq 3\}\;.
  \end{align*}
  \begin{scope}
    We use $\varphi$ as our initial location.
            
    Let us call a map $v{:}\,X\to\{0,1\}$ a literal assignment; we
    call it conflicting if there exists $1\leq n\leq k$ such that
    $v(x_n)=v(\neg x_n)$.

    Assume that $\varphi$ is satisfiable.  Then there exists a
    non-conflicting literal assignment $v$ that satisfies all the
    clauses: for each $1\leq i\leq m$, there exists $1\leq j\leq 3$
    such that $v(\litt_{i,j})=1$; this yields a counterless strategy
    for \Adam, which selects $(C_i,\litt_{i,j})$ for each
    $1\leq i\leq m$.  Consider any infinite play consistent with
    this strategy.  This play only visits literals $\litt$ where
    $v(\litt)=1$.  There exists a literal $\litt\in X$ that is visited
    infinitely often along the play, say $\litt=x_n$.  Because $v$ is
    non-conflicting, $v(\neg x_n)=0$, thus the location $\neg x_n$
    is never visited.  Thus the play uses the action
    $\litt\step{\vec e_{2n-1}-\vec e_{2n}}\varphi$ infinitely often,
    and never uses any action with a positive effect on
    component $2n$.  Hence the play is losing from any initial credit.

    Conversely, assume that $\varphi$ is not satisfiable.  By
    contradiction, assume that \Adam\ wins the game for all initial
    credits.  By  {prf:ref}`11-lem:counterless`, he has a counterless winning
    strategy $\tau$ that selects a literal in every clause.  Consider
    a literal assignment that maps each one of the selected literals
    to $1$ and the remaining ones in a non-conflicting manner.  By
    definition, this literal assignment satisfies all the clauses,
    but because $\varphi$ is not satisfiable, it is conflicting:
    necessarily, there exist $1\leq n\leq k$ and $1\leq i,i'\leq m$,
    such that $\tau$ selects $x_n$ in $C_i$ and $\neg x_n$ in
    $C_{i'}$.  But this yields a winning strategy for \Eve, which
    alternates in the initial location $\varphi$ between $C_{i}$
    and $C_{i'}$, and for which an initial credit
    $\vec e_{2n-1}+\vec e_{2n}$ suffices: a contradiction.
  \end{scope}
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

````

Note that \cref{11-th:exist-hard} does not apply to fixed dimensions
$\dd\geq 2$.  We know by \cref{11-cor:exist-pseudop} that those games can
be solved in pseudo-polynomial time if the number of priorities is
fixed, and by \cref{11-th:exist-easy} that they are in \coNP.

### Given Initial Credit

With given initial credit, we have a lower bound matching the
\kEXP[2] upper bound of \cref{11-th:avag-easy}, already with a unary
encoding.  The proof itself is an adaptation of the proof by
\citem[Lipton]{Lipton:1976} of \EXPSPACE-hardness of coverability in
the one-player case.

````{prf:theorem} Coverability and non-termination asymmetric vector games are {\kEXP[2]-hard}
:label: 11-th:avag-hard

  Coverability, non-termination, and parity@parity vector game
  asymmetric vector games with given initial credit are
  \kEXP[2]-hard.

````

````{admonition} Proof
:class: dropdown tip

  We reduce from the halting problem of an alternating Minsky
  machine $\?M=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,\dd)$ with counters
  bounded by $B\eqdef 2^{2^n}$ for $n\eqdef|\?M|$.  Such a machine is
  similar to an asymmetric vector system with increments
  $\loc\step{\vec e_i}\loc'$, decrements $\loc\step{-\vec e_i}\loc'$,
  and zero test actions $\loc\step{i\eqby?0}\loc'$, all
  restricted to locations $\loc\in\Loc_\mEve$; the only actions
  available to \Adam\ are actions $\loc\step{\vec 0}\loc'$.  The
  set of locations contains a distinguished `halt' location
  $\loc_\mathtt{halt}\in\Loc$ with no outgoing action.  The
  machine comes with the promise that, along any play, the norm of
  all the visited configurations $\loc(\vec v)$ satisfies
  $\|\vec v\|<B$.  The halting problem asks, given an initial
  location $\loc_0\in\Loc$, whether \Eve\ has a winning strategy to
  visit $\loc_\mathtt{halt}(\vec v)$ for some $\vec v\in\+N^\dd$ from
  the initial configuration $\loc_0(\vec 0)$.  This problem is
  \kEXP[2]-complete if $\dd\geq 3$ by standard
  arguments {cite}`Fischer&Meyer&Rosenberg:1968`.

  
            by a quick refresher on Lipton's construction {cite}`Lipton:1976`;
    see also {cite}`Esparza:1996` for a nice exposition.  At the heart
    of the construction lies a collection of one-player gadgets
    implementing **level $j$** meta-increments
    $\loc\mstep{2^{2^j}\cdot\vec c}\loc'$ and **level $j$**
    meta-decrements $\loc\mstep{-2^{2^j}\cdot\vec c}\loc'$ for
    some unit vector $\vec c$ using $O(j)$ auxiliary counters and
    $\poly(j)$ actions, with precondition that the auxiliary counters
    are initially empty in $\loc$ and postrelation that they are empty
    again in $\loc'$.  The construction is by induction over $j$; let
    us first see a naive implementation for meta-increments.  For
    the base case $j=0$, this is just a standard action
    $\loc\step{2\vec c}\loc'$.  For the induction step $j+1$, we use
    the gadget of {numref}`11-fig:meta-incr` below, where
    $\vec x_{j},\bar{\vec x}_{j},\vec z_{j},\bar{\vec z}_{j}$ are
    distinct fresh unit vectors: the gadget performs two nested
    loops, each of $2^{2^j}$ iterations, thus iterates the unit
    increment of $\vec c$ a total of $\big(2^{2^j}\big)^2=2^{2^{j+1}}$
    times.  A meta-decrement is obtained similarly.

    
```{figure} ./../FigAndAlgos/11-fig:meta-incr.png
:name: 11-fig:meta-incr
:align: center
A naive implementation of the
      meta-increment $\loc\mstep{2^{2^{j+1}}\cdot\vec c}\loc'$.
```
  
  Note that this level $(j+1)$ gadget contains two copies of the
  level $j$ meta-increment and two of the level $j$
  meta-decrement, hence this naive implementation has
  size $\mathsf{exp}(j)$.  In order to obtain a polynomial size, we would like
  to use a single **shared** level $j$ gadget for each $j$, instead
  of hard-wiring multiple copies.  The idea is to use a `dispatch
  mechanism,' using extra counters, to encode the choice of "unit
  vector" $\vec c$ and of return location $\loc'$.  Let us see how to
  do this in the case of the return location $\loc'$; the mechanism
  for the vector $\vec c$ is similar.  We enumerate the (finitely many)
  possible return locations $\loc_0,\dots,\loc_{m-1}$ of the gadget
  implementing $\loc\mstep{2^{2^{j+1}}\cdot\vec c}\loc'$.  We use two
  auxiliary counters with unit vectors $\vec r_j$
  and $\bar{\vec r}_j$ to encode the return location.  Assume $\loc'$
  is the $i$th possible return location, i.e., $\loc'=\loc_i$ in our
  enumeration: before entering the shared gadget implementation, we
  initialise $\vec r_j$ and $\bar{\vec r}_j$ by performing the action
  $\loc\step{i\cdot\vec r_j+(m-i)\cdot\bar{\vec r}_j}\cdots$.  Then,
  where we would simply go to $\loc'$ in {numref}`11-fig:meta-incr` at
  the end of the gadget, the shared gadget has a final action
  $\cdots\step{\vec 0}\loc_{\mathrm{return}_j}$ leading to a dispatch
  location for returns: for all $0\leq i<m$, we have an action
  $\loc_{\mathrm{return}_j}\step{-i\cdot\vec r_j-(m-i)\cdot\bar{\vec
      r}_j}\loc_i$
  that leads to the desired return location.\todoquestion{Is that
    clear enough?}
  

  \bigskip Let us return to the proof.  Consider an instance of the
  halting problem.  We first exhibit a reduction to coverability;
  by \cref{11-rk:cov2parity}, this will also entail the \kEXP[2]-hardness
  of parity@parity vector game asymmetric vector games.  We
  build an asymmetric vector system
  $\?V=(\Loc',\Act',\Loc'_\mEve,\Loc_\mAdam,\dd')$ with
  $\dd'=2\dd+O(n)$.  Each of the counters $\mathtt{c}_i$ of $\?M$ is
  paired with a **complementary** counter $\bar{\mathtt{c}_i}$ such
  that their sum is $B$ throughout the simulation of $\?M$.  We
  denote by $\vec c_i$ and $\bar{\vec c}_i$ the corresponding "unit
  vectors for $1\leq i\leq\dd$.  The vector system" $\?V$ starts by
  initialising the counters $\bar{\mathtt{c}}_i$ to $B$ by a sequence
  of meta-increments
  $\loc'_{i-1}\mstep{2^{2^n}\cdot\bar{\vec c}_i}\loc'_i$ for
  $1\leq i\leq\dd$, before starting the simulation by an action
  $\loc'_\dd\step{\vec 0}\loc_0$.  The simulation of $\?M$ uses the
  actions depicted in {numref}`11-fig:lipton`.  Those maintain the
  invariant on the complement counters.  Regarding zero tests, \Eve
  yields the control to \Adam, who has a choice between performing a
  meta-decrement that will fail if $\bar{\mathtt c}_i< 2^{2^n}$,
  which by the invariant is if and only if $\mathtt{c}_i>0$, or going
  to $\loc'$.

  
```{figure} ./../FigAndAlgos/11-fig:lipton.png
:name: 11-fig:lipton
:align: center
Schema of the reduction to
      coverability in the proof of \cref{11-th:avag-hard}.
```
  
  It is hopefully clear that \Eve\ wins the coverability game played
  on $\?V$ starting from $\loc'_0(\vec 0)$ and with target
  configuration $\loc_\mathtt{halt}(\vec 0)$ if and only if the
  alternating Minsky machine halts.

  \medskip Regarding non-termination games, we use essentially the
  same reduction.  First observe that, if \Eve\ can ensure reaching
  $\loc_\mathtt{halt}$ in the alternating Minsky machine, then she
  can do so after at most $|\Loc|B^\dd$ steps.  We therefore use a
  `time budget': this is an additional component in $\?V$ with
  associated unit vector $\vec t$.  This component is initialised to
  $|\Loc|B^\dd=|\Loc|2^{\dd 2^n}$ before the simulation, and decreases
  by~one at every step; see {numref}`11-fig:lipton-nonterm`.  We also add
  a self loop $\loc_\mathtt{halt}\step{\vec 0}\loc_\mathtt{halt}$.
  Then the only way to avoid the sink and thus to win the
  non-termination game is to reach $\loc_\mathtt{halt}$.
  
```{figure} ./../FigAndAlgos/11-fig:lipton-nonterm.png
:name: 11-fig:lipton-nonterm
:align: center
Schema of the reduction to
      non-termination in the proof of \cref{11-th:avag-hard}.
```

  We still need to extend our initialisation phase.  It suffices for
  this to implement a gadget for $\dd$-meta-increments
  $\loc\mstep{2^{\dd 2^j}\cdot\vec c}\loc'$ and $\dd$-meta-decrements
  $\loc\mstep{-2^{\dd 2^j}\cdot\vec c}\loc'$; this is the same argument as
  in Lipton's construction, with a base case $\loc\mstep{2^\dd}\loc'$
  for $j=0$.  Then we initialise our time budget through $|\Loc|$
  successive $\dd$-meta-increments
  $\loc\mstep{2^{\dd 2^n}\cdot\vec t}\loc'$.
  

````

The proof of \cref{11-th:avag-hard} relies crucially on the fact that the
dimension is not fixed: although $\dd\geq 3$ suffices in the
alternating Minsky machine, we need $O(|\?M|)$ additional counters
to carry out the reduction.  A separate argument is thus needed in
order to match the \EXP\ upper bound of \cref{11-th:avag-easy} in fixed
dimension.

````{prf:theorem} Fixed-dimensional coverability and non-termination asymmetric vector games are \EXP-hard
:label: 11-th:avag-two

  Coverability, non-termination, and parity@parity vector game
  asymmetric vector games with given initial credit are
  \EXP-hard in dimension $\dd\geq 2$.

````

````{admonition} Proof
:class: dropdown tip

  We exhibit a reduction from countdown games with "given initial
  credit", which are \EXP-complete by \cref{11-th:countdown-given}.
  Consider an instance of a configuration reachability countdown
  game: a countdown system
  $\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,1)$ with initial
  configuration $\loc_0(n_0)$ and target
  configuration $\smiley(0)$---as seen in the proof
  of \cref{11-th:countdown-given}, we can indeed assume that the target
  credit is zero; we will also assume that \Eve\ controls $\smiley$ and
  that the only action available in $\smiley$ is
  $\smiley\step{-1}\smiley$.  We construct an asymmetric "vector
  system" $\?V'$ of dimension~2 such that \Eve\ can ensure
  reaching $\smiley(0,n_0)$ from $\loc_0(n_0,0)$ in $\?V'$ if and only
  if she could ensure reaching $\smiley(0)$ from $\loc_0(n_0)$
  in $\?V$.  The translation is depicted in {numref}`11-fig:dim2`.
  
  
```{figure} ./../FigAndAlgos/11-fig:dim2.png
:name: 11-fig:dim2
:align: center
Schema of the reduction in the proof
    of \cref{11-th:avag-two}.
```
    
  The idea behind this translation is that a configuration $\loc(c)$
  of $\?V$ is simulated by a configuration $\loc(c,n_0-c)$ in $\?V'$.
  The crucial point is how to handle \Adam's moves.  In a
  configuration $\loc(c,n_0-c)$ with $\loc\in\Loc_\mAdam$, according
  to the natural semantics of $\?V$, \Adam\ should be able to
  simulate an action $\loc\step{-n}\loc'$ if and only if $c\geq n$.
  Observe that otherwise if $c<n$ and thus $n_0-c>n_0-n$, \Eve\ can
  play to reach $\smiley$ and win immediately.  An exception to the
  above is if $n$ is minimal among the decrements in $\loc$, because
  according to the natural semantics of $\?V$, if $c<n$ there should
  be an edge to the sink, and this is handled in the second line
  of {numref}`11-fig:dim2`.

  Then \Eve\ can reach $\smiley(0,n_0)$ if and only if she can cover
  $\smiley(0,n_0)$, if and only if she can avoid the sink thanks to
  the self loop $\smiley\step{0,0}\smiley$.  This
  shows the \EXP-hardness of coverability and non-termination
  asymmetric vector games in dimension~two; the hardness of
  parity@parity vector game follows
  from \cref{11-rk:cov2parity,11-rk:nonterm2parity}.

````

  

(11-sec:mono-dim1)=
## Dimension One

\TODO{contents of Section {ref}`11-sec:mono-dim1` depend on what goes into Chapter {ref}`12-chap:multiobjective`}
