(11-sec:complexity)=
# The complexity of asymmetric monotone games

```{math}

\providecommand{\dom}{\mathrm{dom}\,}
\newcommand\pto{\mathrel{\ooalign{\hfil$\mapstochar\mkern5mu$\hfil\cr$\to$\cr}}}
\newcommand{\decpb}[3][]{\begin{problem}[#1]\\[-1.7em]\begin{description}     
    \item[input:] {#2}
    \item[question:] {#3}
    \end{description}
  \end{problem}}

\newcommand{\step}[1]{\xrightarrow{\,\raisebox{-1pt}[0pt][0pt]{\scriptsize\ensuremath
      {#1}}\,}}
\newcommand{\mstep}[1]{\xrightarrow{\,\raisebox{-1pt}[6pt][0pt]{\scriptsize\ensuremath
      {#1}}\,}}
\providecommand{\pop}{\mathrm{pop}}
\providecommand{\push}[1]{\mathrm{push}(#1)}
\providecommand{\mymoot}[1]{}
\renewcommand{\natural}{\arena_\+N}
\newcommand{\capp}[2][C]{\overline{\vec #2}^{#1}}
\let\oldcite\cite
\renewcommand{\cite}{\citep}
\providecommand{\citep}{\oldcite}
\providecommand{\citet}{\cite}
\providecommand{\citem}[2][1]{#1 {cite}`#2`}
\providecommand{\qedhere}{\ensuremath\Box}
\providecommand{\col}{\mathfrak c}
\providecommand{
}{}
\providecommand{
}{}
\providecommand{\ensuremath}{}
\providecommand{\raisebox}[1]{}
\providecommand{\scalebox}[1]{}

\renewcommand{\Game}{\game}

```

Unlike general vector games and configuration reachability
asymmetric ones, coverability, non-termination, and
parity asymmetric vector games are decidable.
We survey in this section the best known complexity bounds for every
case; see {prf:ref}`11-tbl:cmplx` at the end of the chapter for a summary.

(11-sec:up)=
## Upper Bounds
We begin with complexity upper bounds.  The main results are that
parity games with existential initial credit
can be solved in  \textrm{coNP}, but are in  \textrm{kEXP}[2] with "given initial
credit".  In both cases however, the complexity is pseudo-polynomial
if both the dimension $k$ and the number of priorities $d$ are
fixed, which is rather good news: one can hope that, in practice, both
the number of different resources (encoded by the counters) and the
complexity of the functional specification (encoded by the parity
condition) are tiny compared to the size of the system.

(11-sec:up-exist)=
### Existential Initial Credit

> **Counterless Strategies**

Consider a strategy $\tau$ of Adam in a vector game.  In all the
games we consider, uniform positional strategies suffice over the
infinite arena $\natural(\?V)=(V,E, V_\mathrm{Eve}, V_\mathrm{Adam})$: $\tau$ maps vertices
in $V$ to edges in $E$.  We call $\tau$ counterless if, for all
locations $\ell\in \?L_\mathrm{Adam}$ and all vectors
$\vec v,\vec v'\in\+N^ k$, $\tau( \ell(\vec v))=\tau( \ell(\vec v'))$.
A counterless strategy thus only considers the current location of
the play.

````{prf:lemma} Counterless strategies
:label: 11-lem:counterless

  Let $\?V=( \?L, A, \?L_\mathrm{Eve}, \?L_\mathrm{Adam}, k)$ be an "asymmetric
  vector system", $\ell_0\in \?L$ be a location, and
  $\mathrm{lcol}{:}\, \?L\to\{1,\dots,d\}$ be a location colouring.  If Adam 
  wins from $\ell_0(\vec v)$ for every initial credit $\vec v$ in the
  parity game played over $\?V$ with $\mathrm{lcol}$, then
  he has a single counterless strategy such that he wins from
  $\ell_0(\vec v)$ for every initial credit $\vec v$.

````

````{admonition} Proof
:class: dropdown tip

  Let $A_\mathrm{Adam}  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=}\{( \ell\step{\vec
    u} \ell')\in A\mid \ell\in \?L_\mathrm{Adam}\}$ be the set of actions
  controlled by Adam.  We assume without loss of generality that
  every location $\ell\in \?L_\mathrm{Adam}$ has either one or two outgoing
  actions, thus $| \?L_\mathrm{Adam}|\leq| A_\mathrm{Adam}|\leq
  2| \?L_\mathrm{Adam}|$.  We proceed by induction over $| A_\mathrm{Adam}|$.  For
  the base case, if $| A_\mathrm{Adam}|=| \?L_\mathrm{Adam}|$ then every location
  controlled by Adam has a single outgoing action, thus any
  strategy for Adam is trivially counterless.

  For the induction step, consider some location
  $\hat \ell\in \?L_\mathrm{Adam}$ with two outgoing actions
  $a_l  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=}\hat \ell\step{\vec 0} \ell_l$ and
  $a_r  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=}\hat \ell\step{\vec 0} \ell_r$.  Let $\?V_l$ and $\?V_r$ be
  the vector systems obtained from $\?V$ by removing
  respectively $a_r$ and $a_l$ from $A$, i.e., by using
  $A_l  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=} A\setminus\{a_r\}$ and
  $A_r  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=} A\setminus\{a_l\}$.  If $\textrm{Adam}$ wins the
  parity game from $\ell(\vec v)$ for every
  initial credit $\vec v$ in either $\?V_l$ or $\?V_r$, then by
  induction hypothesis he has a counterless winning strategy winning
  from $\ell(\vec v)$ for every initial credit $\vec v$, and the same
  strategy is winning in $\?V$ from $\ell(\vec v)$ for every initial
  credit $\vec v$.

  In order to conclude the proof, we show that, if Adam loses in
  $\?V_l$ from $\ell_0(\vec v_l)$ for some $\vec v_l\in\+N^ k$ and in
  $\?V_r$ from $\ell_0(\vec v_r)$ for some $\vec v_r\in\+N^ k$, then
  there exists $\vec v_0\in\+N^ k$ such that Eve wins from
  $\ell_0(\vec v_0)$ in $\?V$.  Let $\sigma_l$ and $\sigma_r$ denote
  Eve\'s winning strategies in the two games.  By a slight abuse of
  notations (justified by the fact that we are only interested in a
  few initial vertices), we see plays as sequences of actions and
  strategies as maps $A^\ast\to A$.\todoquestion{I hope this is not too messy}  Consider the set of
  plays consistent with $\sigma_r$ starting from $\ell_0(\vec v_r)$.
  If none of those plays visits $\hat \ell$, then $\textrm{Eve}$ wins in $\?V$
  from $\ell_0(\vec v_r)$ and we conclude.  Otherwise, there is some
  finite prefix $\hat\pi$ of a play that
  visits $\hat \ell(\hat{\vec v})$ for some vector
  $\hat{\vec v}=\vec v_r+ w(\hat\pi)$.  We let
  $\vec v_0  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=}\vec v_l+\hat{\vec v}$ and show that Eve wins from
  $\ell_0(\vec v_0)$.

  \begin{scope}    We define now a strategy $\sigma$ for $\textrm{Eve}$ over $\?V$ that
    switches between applying $\sigma_l$ and $\sigma_r$ each time
    $a_r$ is used and switches back each time $a_l$ is used.  More
    precisely, given a finite or infinite sequence $\pi$ of actions,
    we decompose $\pi$ as $\pi_1 a_1 \pi_2 a_2 \pi_3\cdots$ where each
    segment $\pi_j\in( A\setminus\{a_l,a_r\})^\ast$ does not use
    either $a_l$ nor $a_r$ and each $a_j\in\{a_l,a_r\}$.  The
    associated mode $m(j)\in\{l,r\}$ of a segment $\pi_j$
    is $m(1)  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=} l$ for the initial segment and otherwise
    $m(j)  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=} l$ if $e_{j-1}=a_l$ and $m(j)  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=} r$ otherwise.  The
    $l$-subsequence associated with $\pi$ is the sequence of segments
    $\pi(l)  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=}\pi_{l_1}a_{l_2-1}\pi_{l_2}a_{l_3-1}\pi_{l_3}\cdots$
    with mode $m(l_i)=l$, while the $r$-subsequence is the sequence
    $\pi(r)  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=}\hat\pi a_{r_1-1}\pi_{r_1}a_{r_2-1}\pi_{r_2}\cdots$
    with mode $m(r_i)=r$ prefixed by $\hat\pi$.  Then we let
    $\sigma(\pi)  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=}\sigma_{m}(\pi(m))$ where $m\in\{l,r\}$ is the
    mode of the last segment of $\pi$.

    Consider an infinite play $\pi$ consistent with $\sigma$ starting
    from $\ell_0(\vec v_0)$.  Since $\vec v_0\geq\vec v_l$ and
    $\vec v_0\geq \vec v_r+ w(\hat\pi)$, $\pi(l)$ and $\pi(r)$
    starting from $\ell_0(\vec v_0)$ are consistent with
    simulating---in the sense of {prf:ref}`11-lem:mono`---$\sigma_l$
    from $\ell_0(\vec v_l)$ and $\sigma_r$ from $\ell_0(\vec v_r)$.
    Let $\pi'$ be a finite prefix of $\pi$.  Then
    $w(\pi')= w(\pi'(l))+ w(\pi'(r))$ where $\pi'(l)$
    is a prefix of $\pi(l)$ and $\pi'(r)$ of $\pi(r)$, thus
    $w(\pi'(l))\leq\vec v_l$ and
    $w(\pi'(r))\leq\vec v_r+ w(\hat\pi)$, thus
    $w(\pi')\leq\vec v_0$: the play $\pi$ avoids the sink.
    Furthermore, the maximal priority seen infinitely often along
    $\pi(l)$ and $\pi(r)$ is even (note that one of $\pi(l)$
    and $\pi(r)$ might not be infinite), thus the maximal priority
    seen infinitely often along $\pi$ is also even.  This shows
    that $\sigma$ is winning for Eve from $\ell_0(\vec v_0)$.\todoquestion{Is
    that clear?}
  \end{scope}

````

We are going to exploit {prf:ref}`11-lem:counterless`
in {prf:ref}`11-th:exist-easy` in order to prove a  \textrm{coNP}\ upper bound for
asymmetric games with existential initial credit: it suffices in
order to decide those games to guess a counterless winning
strategy $\tau$ for Adam and check that it is indeed winning by
checking that Eve loses the one-player game arising from $\tau$.
This last step requires an algorithmic result of independent interest.

> **One-player Case**

Let $\?V=( \?L, A, k)$ be a vector addition system with states,
$\mathrm{lcol}{:}\, \?L\to\{1,\dots,d\}$ a location colouring, and
$\ell_0\in \?L$ an initial location.  Then Eve wins the
parity one-player game from $\ell_0(\vec v_0)$
for some initial credit $\vec v_0$ if and only if there exists some
location such that

*  $\ell$ is reachable from $\ell_0$ in the directed graph
  underlying $\?V$ and
*  there is a cycle $\pi\in A^\ast$ from $\ell$ to itself such
  that $w(\pi)\geq 0$ and the maximal priority occurring
  along $\pi$ is even.

Indeed, assume we can find such a location $\ell$.  Let
$\hat\pi\in A^\ast$ be a path from $\ell_0$ to $\ell$ and $\vec
v_0(i)  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=}\max\{\| w(\pi')\|\mid\pi'\text{ is a prefix of
}\hat\pi\pi\}$ for all $1\leq i\leq k$.  Then $\ell_0(\vec v_0)$ can
reach $\ell(\vec v_0+ w(\hat\pi))$ in the natural semantics
of $\?V$ by following $\hat\pi$, and then $\ell(\vec v_0+\vec
W(\hat\pi)+n w(\pi))\geq  \ell(\vec v_0+ w(\hat\pi))$ after
$n$ repetitions of the cycle $\pi$.  The infinite play arising from
this strategy has an even maximal priority.

Conversely, if Eve wins, then there is a winning play
$\pi\in A^\omega$ from $\ell_0(\vec v_0)$ for some $\vec v_0$.
Recall that $(V,{\leq})$ is a wqo, and we argue as in
{prf:ref}`11-lem:finmem` that there is indeed such a location $\ell$.

Therefore, solving one-player parity vector games boils down to
determining the existence of a cycle with non-negative effect and even
maximal priority.  We shall use linear programming techniques in order
to check the existence of such a cycle in polynomial
time {cite}`Kosaraju&Sullivan:1988`.

\begin{scope}
Let us start with a relaxed problem: we call a
multi-cycle a non-empty finite set of cycles $\Pi$ and let
$w(\Pi)  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=}\sum_{\pi\in\Pi} w(\pi)$ be its weight; we write
$t\in\Pi$ if $t\in\pi$ for some $\pi\in\Pi$.
Let $M\in 2^{ A}$ be a set of `mandatory' subsets of actions and
$F\subseteq A$ a set of `forbidden' actions.  Then we say that
$\Pi$ is non-negative if $w(\Pi)\geq\vec 0$, and that it is
suitable for $(M,F)$ if for all $A'\in M$ there exists
$t\in A'$ such that $t\in\Pi$, and if for all $t\in F$,
$t\not\in\Pi$.  We use the same terminology for a single cycle $\pi$.

````{prf:lemma} Linear programs for suitable non-negative multi-cycles
:label: 11-lem:zmulticycle

  Let $\?V$ be a vector addition system with states,
  $M\in 2^{ A}$, and $F\subseteq A$.  We can check in polynomial
  time whether $\?V$ contains a non-negative multi-cycle $\Pi$
  suitable for $(M,F)$.

````

````{admonition} Proof
:class: dropdown tip

  We reduce the problem to solving a linear program.  For a
  location $\ell$, let
  $\mathrm{in}( \ell)  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=}\{( \ell'\step{\vec u} \ell)\in A\mid
   \ell'\in \?L\}$
  and
  $\mathrm{out}( \ell)  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=}\{( \ell\step{\vec u} \ell')\in A\mid
   \ell'\in \?L\}$ be its sets of incoming and outgoing actions.  The
  linear program has a variable $x_a$ for each action $a\in A$,
  which represents the number of times the action $a$ occurs in
  the multi-cycle.  It consists of the following contraints:
  
$$

    \forall \ell&\in \?L,&\sum_{a\in\mathrm{in}( \ell)}x_a&=\sum_{a\in\mathrm{out}( \ell)}x_a\;,\tag{multi-cycle}\\
    \forall a&\in A,&x_a&\geq 0\;,\tag{non-negative uses}\\
    \forall i&\in\{1,\dots, k\},&\sum_{a\in A} x_a\cdot w(t)(i)&\geq
                                            0\;,\tag{non-negative weight}\\
    &&\sum_{a\in A}x_a&\geq 0\tag{non empty}\\
    \forall  A'&\in M,&\sum_{a\in A'}x_a&\geq 0\;,\tag{every subset
                                               in $M$ is used}\\
    \forall a&\in F,&x_a&= 0\;.\tag{no forbidden actions}
  
$$

  As solving a linear program is in polynomial time {cite}``\todoquestion{agree
  on a ref with Chapter {ref}`8-chap:signal`?}, the result follows.

````

Of course, what we are aiming for is finding a non-negative
**cycle** suitable for $(M,F)$ rather than a multi-cycle.
Let us define for this the relation $\ell\sim \ell'$ over $\?L$ if
$\ell= \ell'$ or if there exists a non-negative multi-cycle $\Pi$
suitable for $(M,F)$ such that $\ell$ and $\ell'$ belong to some
cycle $\pi\in\Pi$.
\begin{claim}\label{11-cl:sim} The relation $\sim$ is an equivalence
  relation.\end{claim}

````{admonition} Proof
:class: dropdown tip

  Symmetry and reflexivity are trivial, and if $\ell\sim \ell'$ and
  $\ell'\sim \ell''$ because $\ell$ and $\ell'$ appear in some cycle
  $\pi\in\Pi$ and $\ell'$ and $\ell''$ in some cycle $\pi'\in\Pi'$ for
  two non-negative multi-cycles $\Pi$ and $\Pi'$ suitable
  for $(M,F)$, then up to a circular shift $\pi$ and $\pi'$ can be
  assumed to start and end with $\ell'$, and then
  $(\Pi\setminus\{\pi\})\cup(\Pi'\setminus\{\pi'\})\cup\{\pi\pi'\}$ is
  also a non-negative multi-cycle suitable for $(M,F)$.

````

Thus $\sim$ defines a partition $\?L/{\sim}$ of $\?L$.
In order to find a non-negative cycle $\pi$ suitable for $(M,F)$,
we are going to compute the partition $\?L/{\sim}$ of $\?L$
according to $\sim$.  If we obtain a partition with a single
equivalence class, we are done: there exists such a cycle.  Otherwise,
such a cycle if it exists must be included in one of the subsystems
$(P, A\cap(P\times\+Z^ k\times P), k)$ induced by the equivalence
classes $P\in \?L/{\sim}$.  This yields {numref}`11-algo:zcycle`, which
assumes that we know how to compute the partition $\?L/{\sim}$.  Note
that the depth of the recursion in {numref}`11-algo:zcycle` is bounded
by $| \?L|$ and that recursive calls operate over disjoint subsets
of $\?L$, thus assuming that we can compute the partition in
polynomial time, then {numref}`11-algo:zcycle` also works in polynomial
time.

```{figure} ./../FigAndAlgos/11-algo:zcycle.png
:name: 11-algo:zcycle
:align: center
$\text{cycle}(\?V,M,F)$
```

It remains to see how to compute the partition $\?L/{\sim}$. Consider
for this the set of actions
$A'  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=}\{a\mid\exists\Pi\text{ a non-negative multi-cycle
  suitable for $(M,F)$ with $a\in\Pi$}\}$ and
$\?V'=( \?L', A', k)$ the subsystem induced by $A'$.
\begin{claim}
\label{11-cl:part}
  There exists a path from $\ell$ to $\ell'$ in $\?V'$
  if and only if $\ell\sim \ell'$.
\end{claim}

````{admonition} Proof
:class: dropdown tip

  If $\ell\sim \ell'$, then either $\ell= \ell'$ and there is an empty
  path, or there exist $\Pi$ and $\pi\in\Pi$ such that $\ell$
  and $\ell'$ belong to $\pi$ and $\Pi$ is a non-negative
  multi-cycle suitable for $(M,F)$, thus every action of $\pi$ is
  in $A'$ and there is a path in $\?V'$.  

  Conversely, if there is a path $\pi\in{ A'}^\ast$ from $\ell$
  to $\ell'$, then $\ell\sim \ell'$ by induction on $\pi$.  Indeed, if
  $|\pi|=0$ then $\ell= \ell'$.  For the induction step, $\pi=\pi' a$
  with $\pi'\in{ A'}^\ast$ a path from $\ell$ to $\ell''$ and
  $a=( \ell''\step{\vec u} \ell')\in A'$ for some $\vec u$.  By
  induction hypothesis, $\ell\sim \ell''$ and since $a\in A'$,
  $\ell''\sim \ell'$, thus $\ell\sim \ell'$ by transitivity shown
  in {prf:ref}`11-cl:sim`. 

````

By {prf:ref}`11-cl:part`, the equivalence classes of $\sim$ are the
strongly connected components of $\?V'$.  This yields the following
polynomial time algorithm for computing $\?L/{\sim}$.

```{figure} ./../FigAndAlgos/11-algo:part.png
:name: 11-algo:part
:align: center
$\text{partition}(\?V,M,F)$
```

Together, {prf:ref}`11-lem:zmulticycle`
and {numref}`11-algo:part,11-algo:zcycle` yield the following.

````{prf:lemma} Polynomial-time detection of suitable non-negative cycles
:label: 11-lem:zcycle

  Let $\?V$ be a vector addition system with states,
  $M\in 2^{ A}$, and $F\subseteq A$.  We can check in polynomial
  time whether $\?V$ contains a non-negative cycle $\pi$
  suitable for $(M,F)$.

````

Finally, we obtain the desired polynomial time upper bound for
parity in vector addition systems with states.

````{prf:theorem} Existential one-player parity vector games are in \P
:label: 11-thm:zcycle

  Whether Eve wins a one-player parity vector game with
  existential initial credit is in \P.

````

````{admonition} Proof
:class: dropdown tip

  Let $\?V=( \?L, A, k)$ be a vector addition system with states,
  $\mathrm{lcol}{:}\, \?L\to\{1,\dots,$ $d\}$ a location colouring, and
  $\ell_0\in \?L$ an initial location.  We start by trimming $\?V$ to
  only keep the locations reachable from $\ell_0$ in the underlying
  directed graph.  Then, for every even priority $p\in\{1,\dots,d\}$,
  we use {prf:ref}`11-lem:zcycle` to check for the existence of a
  non-negative cycle with maximal priority $p$: it suffices for this
  to set $M  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=}\{ \mathrm{lcol}^{-1}(p)\}$ and
  $F  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=} \mathrm{lcol}^{-1}(\{p+1,\dots,d\})$.

````

\end{scope}

> **Upper Bounds**

We are now equipped to prove our upper bounds.  We begin with a nearly
trivial case.  In a coverability asymmetric vector game with
existential initial credit, the counters play no role at all: Eve 
has a winning strategy for some initial credit in the vector game if
and only if she has one to reach the target location $\ell_f$ in the
finite game played over $\?L$ and edges $( \ell, \ell')$ whenever
$\ell\step{\vec u} \ell'\in A$ for some $\vec u$.  This entails that
coverability asymmetric vector games are quite easy to solve.

````{prf:theorem} Existential coverability asymmetric vector games are in \P
:label: 11-th:cov-exist-P

  Coverability asymmetric vector games with "existential initial
  credit" are \P-complete.

````

Regarding non-termination and parity, we
exploit {prf:ref}`11-lem:counterless` and {prf:ref}`11-thm:zcycle`.

````{prf:theorem} Existential parity asymmetric vector games are in  \textrm{coNP}
:label: 11-th:exist-easy

  Non-termination and parity asymmetric
  vector games with existential initial credit are in  \textrm{coNP}.

````

````{admonition} Proof
:class: dropdown tip

  By {prf:ref}`11-rk:nonterm2parity`, it suffices to prove the statement for
  parity games.  By {prf:ref}`11-lem:counterless`,
  if Adam wins the game, we can guess a counterless winning
  strategy $\tau$ telling which action to choose for every location.
  This strategy yields a one-player game, and by {prf:ref}`11-thm:zcycle`
  we can check in polynomial time that $\tau$ was indeed winning
  for Adam.

````

Finally, in fixed dimension and with a fixed number of priorities, we
can simply apply the results of Section {ref}`11-sec:bounding`.

````{prf:corollary} Existential fixed-dimensional parity asymmetric vector games are pseudo-polynomial
:label: 11-cor:exist-pseudop

  Parity asymmetric vector games with
  existential initial credit are in pseudo-polynomial time if the
  dimension and the number of priorities are fixed.

````

````{admonition} Proof
:class: dropdown tip

  Consider an asymmetric vector system
  $\?V=( \?L, A, \?L_\mathrm{Eve}, \?L_\mathrm{Adam}, k)$ and a location
  colouring $\mathrm{lcol}{:}\, \?L\to\{1,\dots,2d\}$.
  By {prf:ref}`11-lem:parity2bounding`, the parity vector game with
  existential initial credit over $\?V$ problem reduces to a
  bounding game with existential initial credit over a "vector
  system" $\?V'=( \?L', A', \?L'_\mathrm{Eve}, \?L'_\mathrm{Adam}, k+d)$ where
  $\?L'\in O(| \?L|)$ and $\| A'\|=\| A\|$.
  By {prf:ref}`11-th:bounding`, it suffices to consider the case of a
  non-termination game with existential initial credit played over
  the bounded semantics $\mathcal{A}_B(\?V')$ where $B$ is in
  $(| \?L'|\cdot\| A'\|)^{O( k+d)^3}$.  Such a game can be solved in
  linear time in the size of the bounded arena using attractor
  techniques, thus in $O(| \?L|\cdot B)^{ k+d}$, which is in
  $(| \?L|\cdot\| A\|)^{O( k+d)^4}$ in terms of the original instance.

````

(11-sec:up-given)=
### Given Initial Credit
\TODO{Section {ref}`11-sec:up-given`}

````{prf:theorem} Upper bounds for asymmetric vector games
:label: 11-th:avag-easy

  Coverability, non-termination, and parity
  asymmetric vector games with given initial credit are in
   \textrm{kEXP}[2].  If the dimension is fixed, they are in  \textrm{EXP}, and if the
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
following lower bound matching {prf:ref}`11-th:exist-easy`, already with a
unary encoding.

````{prf:theorem} Existential non-termination asymmetric vector games are  \textrm{coNP}-hard
:label: 11-th:exist-hard

  Non-termination, and parity
  asymmetric vector games with existential initial credit are
   \textrm{coNP}-hard.% in any dimension $k\geq 2$.

````

````{admonition} Proof
:class: dropdown tip

  By {prf:ref}`11-rk:nonterm2parity`, it suffices to show hardness for
  non-termination games.  We reduce from the \lang{3SAT} problem:
  given a formula $\varphi=\bigwedge_{1\leq i\leq m}C_i$ where each
  clause $C_i$ is a disjonction of the form
  $\ell_{i,1}\vee  \ell_{i,2}\vee  \ell_{i,3}$ of literals taken from
  $X=\{x_1,\neg x_1,x_2,$ $\neg x_2,\dots,x_k,\neg x_k\}$, we construct
  an asymmetric vector system $\?V$ where Eve wins the
  non-termination game with existential initial credit if and only
  if $\varphi$ is not satisfiable; since the game is determined, we
  actually show that Adam wins the game if and only if $\varphi$ is
  satisfiable.

  Our vector system has dimension $2k$, and for a literal
  $\ell\in X$, we define the vector
  
$$

    \vec u_\ell  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=}\begin{cases}
      \vec e_{2n-1}-\vec e_{2n}&\text{if }  \ell=x_n\;,\\
      \vec e_{2n}-\vec e_{2n-1}&\text{if }  \ell=\neg x_n\;.
    \end{cases}
  
$$

  We define $\?V  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=}( \?L, A, \?L_\mathrm{Eve}, \?L_\mathrm{Adam},2k)$ where
  
$$

     \?L_\mathrm{Eve}&  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=}\{\varphi\}\cup\{  \ell_{i,j}\mid 1\leq i\leq m,1\leq j\leq
                3\}\;,\\
     \?L_\mathrm{Adam}&  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=}\{C_i\mid 1\leq i\leq m\}\;,\\
     A&  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=}\{\varphi\step{\vec 0}C_i\mid 1\leq i\leq m\}\cup\{C_i\step{\vec 0}  \ell_{i,j},\;\;  \ell_{i,j}\xrightarrow{\vec u_{  \ell_{i,j}}}\varphi\mid 1\leq i\leq m,1\leq j\leq 3\}\;.
  
$$

  \begin{scope}
    We use $\varphi$ as our initial location.
            
    Let us call a map $v{:}\,X\to\{0,1\}$ a literal assignment; we
    call it conflicting if there exists $1\leq n\leq k$ such that
    $v(x_n)=v(\neg x_n)$.

    Assume that $\varphi$ is satisfiable.  Then there exists a
    non-conflicting literal assignment $v$ that satisfies all the
    clauses: for each $1\leq i\leq m$, there exists $1\leq j\leq 3$
    such that $v(  \ell_{i,j})=1$; this yields a counterless strategy
    for Adam, which selects $(C_i,  \ell_{i,j})$ for each
    $1\leq i\leq m$.  Consider any infinite play consistent with
    this strategy.  This play only visits literals $\ell$ where
    $v(  \ell)=1$.  There exists a literal $\ell\in X$ that is visited
    infinitely often along the play, say $\ell=x_n$.  Because $v$ is
    non-conflicting, $v(\neg x_n)=0$, thus the location $\neg x_n$
    is never visited.  Thus the play uses the action
    $\ell\step{\vec e_{2n-1}-\vec e_{2n}}\varphi$ infinitely often,
    and never uses any action with a positive effect on
    component $2n$.  Hence the play is losing from any initial credit.

    Conversely, assume that $\varphi$ is not satisfiable.  By
    contradiction, assume that Adam wins the game for all initial
    credits.  By {prf:ref}`11-lem:counterless`, he has a counterless winning
    strategy $\tau$ that selects a literal in every clause.  Consider
    a literal assignment that maps each one of the selected literals
    to $1$ and the remaining ones in a non-conflicting manner.  By
    definition, this literal assignment satisfies all the clauses,
    but because $\varphi$ is not satisfiable, it is conflicting:
    necessarily, there exist $1\leq n\leq k$ and $1\leq i,i'\leq m$,
    such that $\tau$ selects $x_n$ in $C_i$ and $\neg x_n$ in
    $C_{i'}$.  But this yields a winning strategy for Eve, which
    alternates in the initial location $\varphi$ between $C_{i}$
    and $C_{i'}$, and for which an initial credit
    $\vec e_{2n-1}+\vec e_{2n}$ suffices: a contradiction.
  \end{scope}

````

Note that {prf:ref}`11-th:exist-hard` does not apply to fixed dimensions
$k\geq 2$.  We know by {prf:ref}`11-cor:exist-pseudop` that those games can
be solved in pseudo-polynomial time if the number of priorities is
fixed, and by {prf:ref}`11-th:exist-easy` that they are in  \textrm{coNP}.

### Given Initial Credit

With given initial credit, we have a lower bound matching the
 \textrm{kEXP}[2] upper bound of {prf:ref}`11-th:avag-easy`, already with a unary
encoding.  The proof itself is an adaptation of the proof by
\citem[Lipton]{Lipton:1976} of  \textrm{EXPSPACE}-hardness of coverability in
the one-player case.

````{prf:theorem} Coverability and non-termination asymmetric vector games are { \textrm{kEXP}[2]-hard}
:label: 11-th:avag-hard

  Coverability, non-termination, and parity
  asymmetric vector games with given initial credit are
   \textrm{kEXP}[2]-hard.

````

````{admonition} Proof
:class: dropdown tip

  We reduce from the halting problem of an alternating Minsky
  machine $\?M=( \?L, A, \?L_\mathrm{Eve}, \?L_\mathrm{Adam}, k)$ with counters
  bounded by $B  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=} 2^{2^n}$ for $n  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{def}}}}{=}|\?M|$.  Such a machine is
  similar to an asymmetric vector system with increments
  $\ell\step{\vec e_i} \ell'$, decrements $\ell\step{-\vec e_i} \ell'$,
  and zero test actions $\ell\step{i\eqby?0} \ell'$, all
  restricted to locations $\ell\in \?L_\mathrm{Eve}$; the only actions
  available to Adam are actions $\ell\step{\vec 0} \ell'$.  The
  set of locations contains a distinguished `halt' location
  $\ell_\mathtt{halt}\in \?L$ with no outgoing action.  The
  machine comes with the promise that, along any play, the norm of
  all the visited configurations $\ell(\vec v)$ satisfies
  $\|\vec v\|<B$.  The halting problem asks, given an initial
  location $\ell_0\in \?L$, whether Eve has a winning strategy to
  visit $\ell_\mathtt{halt}(\vec v)$ for some $\vec v\in\+N^ k$ from
  the initial configuration $\ell_0(\vec 0)$.  This problem is
   \textrm{kEXP}[2]-complete if $k\geq 3$ by standard
  arguments {cite}`Fischer&Meyer&Rosenberg:1968`.

            by a quick refresher on Lipton's construction {cite}`Lipton:1976`;
    see also {cite}`Esparza:1996` for a nice exposition.  At the heart
    of the construction lies a collection of one-player gadgets
    implementing **level $j$** meta-increments
    $\ell\mstep{2^{2^j}\cdot\vec c} \ell'$ and **level $j$**
    meta-decrements $\ell\mstep{-2^{2^j}\cdot\vec c} \ell'$ for
    some unit vector $\vec c$ using $O(j)$ auxiliary counters and
    $\poly(j)$ actions, with precondition that the auxiliary counters
    are initially empty in $\ell$ and postrelation that they are empty
    again in $\ell'$.  The construction is by induction over $j$; let
    us first see a naive implementation for meta-increments.  For
    the base case $j=0$, this is just a standard action
    $\ell\step{2\vec c} \ell'$.  For the induction step $j+1$, we use
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
      meta-increment $\ell\mstep{2^{2^{j+1}}\cdot\vec c} \ell'$.
```
  
  Note that this level $(j+1)$ gadget contains two copies of the
  level $j$ meta-increment and two of the level $j$
  meta-decrement, hence this naive implementation has
  size $\mathsf{exp}(j)$.  In order to obtain a polynomial size, we would like
  to use a single **shared** level $j$ gadget for each $j$, instead
  of hard-wiring multiple copies.  The idea is to use a `dispatch
  mechanism,' using extra counters, to encode the choice of "unit
  vector" $\vec c$ and of return location $\ell'$.  Let us see how to
  do this in the case of the return location $\ell'$; the mechanism
  for the vector $\vec c$ is similar.  We enumerate the (finitely many)
  possible return locations $\ell_0,\dots, \ell_{m-1}$ of the gadget
  implementing $\ell\mstep{2^{2^{j+1}}\cdot\vec c} \ell'$.  We use two
  auxiliary counters with unit vectors $\vec r_j$
  and $\bar{\vec r}_j$ to encode the return location.  Assume $\ell'$
  is the $i$th possible return location, i.e., $\ell'= \ell_i$ in our
  enumeration: before entering the shared gadget implementation, we
  initialise $\vec r_j$ and $\bar{\vec r}_j$ by performing the action
  $\ell\step{i\cdot\vec r_j+(m-i)\cdot\bar{\vec r}_j}\cdots$.  Then,
  where we would simply go to $\ell'$ in {numref}`11-fig:meta-incr` at
  the end of the gadget, the shared gadget has a final action
  $\cdots\step{\vec 0} \ell_{\mathrm{return}_j}$ leading to a dispatch
  location for returns: for all $0\leq i<m$, we have an action
  $\ell_{\mathrm{return}_j}\step{-i\cdot\vec r_j-(m-i)\cdot\bar{\vec
      r}_j} \ell_i$
  that leads to the desired return location.\todoquestion{Is that
    clear enough?}

  \bigskip Let us return to the proof.  Consider an instance of the
  halting problem.  We first exhibit a reduction to coverability;
  by {prf:ref}`11-rk:cov2parity`, this will also entail the  \textrm{kEXP}[2]-hardness
  of parity asymmetric vector games.  We
  build an asymmetric vector system
  $\?V=( \?L', A', \?L'_\mathrm{Eve}, \?L_\mathrm{Adam}, k')$ with
  $k'=2 k+O(n)$.  Each of the counters $\mathtt{c}_i$ of $\?M$ is
  paired with a **complementary** counter $\bar{\mathtt{c}_i}$ such
  that their sum is $B$ throughout the simulation of $\?M$.  We
  denote by $\vec c_i$ and $\bar{\vec c}_i$ the corresponding "unit
  vectors for $1\leq i\leq k$.  The vector system" $\?V$ starts by
  initialising the counters $\bar{\mathtt{c}}_i$ to $B$ by a sequence
  of meta-increments
  $\ell'_{i-1}\mstep{2^{2^n}\cdot\bar{\vec c}_i} \ell'_i$ for
  $1\leq i\leq k$, before starting the simulation by an action
  $\ell'_k\step{\vec 0} \ell_0$.  The simulation of $\?M$ uses the
  actions depicted in {numref}`11-fig:lipton`.  Those maintain the
  invariant on the complement counters.  Regarding zero tests, Eve 
  yields the control to Adam, who has a choice between performing a
  meta-decrement that will fail if $\bar{\mathtt c}_i< 2^{2^n}$,
  which by the invariant is if and only if $\mathtt{c}_i>0$, or going
  to $\ell'$.

```{figure} ./../FigAndAlgos/11-fig:lipton.png
:name: 11-fig:lipton
:align: center
Schema of the reduction to
      coverability in the proof of {prf:ref}`11-th:avag-hard`.
```
  
  It is hopefully clear that Eve wins the coverability game played
  on $\?V$ starting from $\ell'_0(\vec 0)$ and with target
  configuration $\ell_\mathtt{halt}(\vec 0)$ if and only if the
  alternating Minsky machine halts.

 Regarding non-termination games, we use essentially the
  same reduction.  First observe that, if Eve can ensure reaching
  $\ell_\mathtt{halt}$ in the alternating Minsky machine, then she
  can do so after at most $| \?L|B^ k$ steps.  We therefore use a
  `time budget': this is an additional component in $\?V$ with
  associated unit vector $\vec t$.  This component is initialised to
  $| \?L|B^ k=| \?L|2^{ k 2^n}$ before the simulation, and decreases
  by one at every step; see {numref}`11-fig:lipton-nonterm`.  We also add
  a self loop $\ell_\mathtt{halt}\step{\vec 0} \ell_\mathtt{halt}$.
  Then the only way to avoid the sink and thus to win the
  non-termination game is to reach $\ell_\mathtt{halt}$.
  
```{figure} ./../FigAndAlgos/11-fig:lipton-nonterm.png
:name: 11-fig:lipton-nonterm
:align: center
Schema of the reduction to
      non-termination in the proof of {prf:ref}`11-th:avag-hard`.
```

  We still need to extend our initialisation phase.  It suffices for
  this to implement a gadget for $k$-meta-increments
  $\ell\mstep{2^{ k 2^j}\cdot\vec c} \ell'$ and $k$-meta-decrements
  $\ell\mstep{-2^{ k 2^j}\cdot\vec c} \ell'$; this is the same argument as
  in Lipton's construction, with a base case $\ell\mstep{2^ k} \ell'$
  for $j=0$.  Then we initialise our time budget through $| \?L|$
  successive $k$-meta-increments
  $\ell\mstep{2^{ k 2^n}\cdot\vec t} \ell'$.

````

The proof of {prf:ref}`11-th:avag-hard` relies crucially on the fact that the
dimension is not fixed: although $k\geq 3$ suffices in the
alternating Minsky machine, we need $O(|\?M|)$ additional counters
to carry out the reduction.  A separate argument is thus needed in
order to match the  \textrm{EXP}\ upper bound of {prf:ref}`11-th:avag-easy` in fixed
dimension.

````{prf:theorem} Fixed-dimensional coverability and non-termination asymmetric vector games are  \textrm{EXP}-hard
:label: 11-th:avag-two

  Coverability, non-termination, and parity
  asymmetric vector games with given initial credit are
   \textrm{EXP}-hard in dimension $k\geq 2$.

````

````{admonition} Proof
:class: dropdown tip

  We exhibit a reduction from countdown games with "given initial
  credit", which are  \textrm{EXP}-complete by {prf:ref}`11-th:countdown-given`.
  Consider an instance of a configuration reachability countdown
  game: a countdown system
  $\?V=( \?L, A, \?L_\mathrm{Eve}, \?L_\mathrm{Adam},1)$ with initial
  configuration $\ell_0(n_0)$ and target
  configuration $\smiley(0)$---as seen in the proof
  of {prf:ref}`11-th:countdown-given`, we can indeed assume that the target
  credit is zero; we will also assume that Eve controls $\smiley$ and
  that the only action available in $\smiley$ is
  $\smiley\step{-1}\smiley$.  We construct an asymmetric "vector
  system" $\?V'$ of dimension 2 such that Eve can ensure
  reaching $\smiley(0,n_0)$ from $\ell_0(n_0,0)$ in $\?V'$ if and only
  if she could ensure reaching $\smiley(0)$ from $\ell_0(n_0)$
  in $\?V$.  The translation is depicted in {numref}`11-fig:dim2`.

```{figure} ./../FigAndAlgos/11-fig:dim2.png
:name: 11-fig:dim2
:align: center
Schema of the reduction in the proof
    of {prf:ref}`11-th:avag-two`.
```
    
  The idea behind this translation is that a configuration $\ell(c)$
  of $\?V$ is simulated by a configuration $\ell(c,n_0-c)$ in $\?V'$.
  The crucial point is how to handle Adam\'s moves.  In a
  configuration $\ell(c,n_0-c)$ with $\ell\in \?L_\mathrm{Adam}$, according
  to the natural semantics of $\?V$, Adam should be able to
  simulate an action $\ell\step{-n} \ell'$ if and only if $c\geq n$.
  Observe that otherwise if $c<n$ and thus $n_0-c>n_0-n$, Eve can
  play to reach $\smiley$ and win immediately.  An exception to the
  above is if $n$ is minimal among the decrements in $\ell$, because
  according to the natural semantics of $\?V$, if $c<n$ there should
  be an edge to the sink, and this is handled in the second line
  of {numref}`11-fig:dim2`.

  Then Eve can reach $\smiley(0,n_0)$ if and only if she can cover
  $\smiley(0,n_0)$, if and only if she can avoid the sink thanks to
  the self loop $\smiley\step{0,0}\smiley$.  This
  shows the  \textrm{EXP}-hardness of coverability and non-termination
  asymmetric vector games in dimension two; the hardness of
  parity follows
  from {prf:ref}`11-rk:cov2parity` and {prf:ref}`11-rk:nonterm2parity`.

````

(11-sec:mono-dim1)=
## Dimension One

\TODO{contents of Section {ref}`11-sec:mono-dim1` depend on what goes into Chapter {ref}`12-chap:multiobjective`}
