(11-sec:dim1)=
# Games in dimension one

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
\providecommand{\medskip}{}
\providecommand{\ensuremath}{}
\providecommand{\raisebox}[1]{}
\providecommand{\scalebox}[1]{}

\renewcommand{\Game}{\game}

```

 {prf:ref}`11-th:undec` leaves open whether vector games might be
decidable in dimension one.  They are indeed decidable, and more
generally we learned in Chapter {ref}`10-chap:pushdown` that "one-counter
games"---with the additional ability to test the counter for
zero---were decidable and in fact  PSPACE-complete.  This might seem
to settle the case of vector games in dimension one, except that the
one-counter games of Chapter {ref}`10-chap:pushdown` only allow integer
weights in $\{-1,1\}$, whereas we allow arbitrary updates in $\+Z$
with a binary encoding.  Hence the  PSPACE\ upper bound of
Chapter {ref}`10-chap:pushdown` becomes an  EXPSPACE\ one for succinct
one-counter games.

````{prf:corollary} One-dimensional vector games are in  EXPSPACE
:label: 11-cor:dim1

  Configuration reachability, coverability, non-termination, and
  parity@parity vector game vector games, both with given and with "existential
  initial credit", are in  EXPSPACE\ in dimension one.

````

````{admonition} Proof
:class: dropdown tip
\\
  \TODO{proof of {prf:ref}`11-cor:dim1` depends on how Section {ref}`10-sec:one-counter` is written}

````

The goal of this section is therefore to establish that this
 EXPSPACE\ upper bound is tight (in most cases), by proving a matching
lower bound in Section {ref}`11-sec:one-counter`.  But first, we will study a
class of one-dimensional vector games of independent interest in
Section {ref}`11-sec:countdown`: countdown games.

(11-sec:countdown)=
## Countdown Games

 A one-dimensional vector system
$\?V=( \?L, A, \?L_\mathrm{Eve}, \?L_\mathrm{Adam},1)$ is called a countdown
system if $A\subseteq \?L\times\+Z_{<0}\times \?L$, that is, if
for all $( \ell\step z \ell')\in A$, $z<0$.  We consider the games
defined by countdown systems, both with given and with
existential initial credit, and call the resulting games countdown
games.

````{prf:theorem} Countdown games are  EXP-complete
:label: 11-th:countdown-given

  Configuration reachability and coverability countdown games
  with given initial credit are  EXP-complete.

````

````{admonition} Proof
:class: dropdown tip

  For the upper bound, consider an instance, i.e., a "countdown
  system" $\?V=( \?L, A, \?L_\mathrm{Eve}, \?L_\mathrm{Adam},1)$, an initial
  location $\ell_0\in \?L$, an initial credit $n_0\in\+N$, and a
  target configuration $\ell_f(n_f)\in \?L\times\+N$.  Because every
  action decreases strictly the counter value, the reachable part
  of the natural semantics of $\?V$ starting from $\ell_0(n_0)$ is
  finite and of size at most $1+| \?L|\cdot (n_0+1)$, and because $n_0$
  is encoded in binary, this is at most exponential in the size of the
  instance.  As seen in Chapter {ref}`2-chap:regular`, such a reachability
  game can be solved in time polynomial in the size of the finite
  graph, thus in  EXP\ overall.

  \medskip For the lower bound, we start by considering a game played
  over an exponential-time Turing machine, before showing how to
  implement this game as a countdown game.  Let us consider for this
  an arbitrary Turing machine $\?M$ working in deterministic
  exponential time $2^{p(n)}$ for some fixed polynomial $p$ and an
  input word $w=a_1\cdots a_n$ of length $n$, which we assume to be
  positive.  Let $m  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{def}}}{=} 2^{p(n)}\geq n$.  The computation of $\?M$
  on $w$ is a sequence of configurations $C_1,C_2,\dots,C_t$ of
  length $t\leq m$.  Each configuration $C_i$ is of the form
  $\triangleright \gamma_{i,1}\cdots\gamma_{i,m} \triangleleft$ where $\triangleright$ and
  $\triangleleft$ are endmarkers and the symbols $\gamma_{i,j}$ are either
  taken from the finite tape alphabet $\Gamma$ (which includes a blank
  symbol $\Box$) or a pair $(q,a)$ of a state from $Q$ and a tape
  symbol $a$.  We assume that the set of states $Q$ contains a single
  accepting state $q_\mathrm{final}$.  The entire computation can be
  arranged over a $t\times m$ grid where each line corresponds to a
  configuration $C_i$, as shown in {numref}`11-fig:exp`.

```{figure} ./../FigAndAlgos/11-fig:exp.png
:name: 11-fig:exp
:align: center
The computation of $\?M$ on
  input $w=a_1\cdots a_n$.  This particular picture assumes $\?M$
  starts by rewriting $a_1$ into $a'_1$ and moving to the right in a
  state $q_1$, and empties its tape before accepting its input by going
  to state $q_\mathrm{final}$.
```

  We now set up a two-player game where  Eve\ wants to prove that the
  input $w$ is accepted.  Let
  $\Gamma'  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{def}}}{=} \{ \triangleright, \triangleleft\}\cup\Gamma\cup(Q\times\Gamma)$. Rather
  than exhibiting the full computation from {numref}`11-fig:exp`, the
  game will be played over positions $(i,j,\gamma_{i,j})$ where
  $0<i\leq m$, $0\leq j\leq m+1$, and $\gamma_{i,j}\in\Gamma'$.   Eve\ 
  wants to show that, in the computation of $\?M$ over $w$ as depicted
  in {numref}`11-fig:exp`, the $j$th cell of the $i$th
  configuration $C_i$ contains $\gamma_{i,j}$.  In order to
  substantiate this claim, observe that the content of any cell
  $\gamma_{i,j}$ in the grid is determined by the actions of $\?M$
  and the contents of (up to) three cells in the previous
  configuration.  Thus, if $i>1$ and $0<j<m+1$,  Eve\ provides a triple
  $(\gamma_{i-1,j-1},\gamma_{i-1,j},\gamma_{i-1,j+1})$ of symbols
  in $\Gamma'$ that yield $\gamma_{i,j}$ according to the actions
  of $\?M$, which we denote by
  $\gamma_{i-1,j-1},\gamma_{i-1,j},\gamma_{i-1,j+1}\vdash\gamma_{i,j}$,
  and  Adam\ chooses $j'\in\{j-1,j,j+1\}$ and returns the control
  to  Eve\ in position $(i-1,j',\gamma_{i-1,j'})$.  Regarding the
  boundary cases where $i=0$ or $j=0$ or $j=m+1$,  Eve\ wins
  immediately if $j=0$ and $\gamma={ \triangleright}$, or if $j=m+1$ and
  $\gamma={ \triangleleft}$, or if $i=0$ and $0<j\leq n$ and $\gamma=a_j$, or if
  $i=0$ and $n<j\leq m$ and $\gamma={ \Box}$, and otherwise  Adam\ wins
  immediately.  The game starts in a position
  $(t,j,(q_\mathrm{final},a))$ for some $0<t\leq m$, $0< j\leq m$,
  and $a\in\Gamma$ of  Eve's choosing.  It should be clear that  Eve\ 
  has a winning strategy in this game if and only if $w$ is accepted
  by $\?M$.

  We now implement the previous game as a coverability game over a
  countdown system $\?V  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{def}}}{=}( \?L, A, \?L_\mathrm{Eve}, \?L_\mathrm{Adam},1)$.
  The idea is that the pair $(i,j)$ will be encoded as
  $(i-1)\cdot(m+2)+j+2$ in the counter value, while the
  symbol $\gamma_{i,j}$ will be encoded in the location.  For
  instance, the endmarker $\triangleright$ at position $(1,0)$ will be
  represented by configuration $\ell_{ \triangleright}(2)$, the first input
  $(q_0,a_1)$ at position $(1,1)$ by $\ell_{(q_0,a_1)}(3)$, and the
  endmarker $\triangleleft$ at position $(m,m+1)$ by
  $\ell_{ \triangleleft}(m\cdot(m+2)+1)$. The game starts from the initial
  configuration $\ell_0(n_0)$ where $n_0  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{def}}}{=} m\cdot(m+2)+1$ and the
  target location is $\smiley$.

  We define for this the sets of locations
  
$$

     \?L_\mathrm{Eve}&  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{def}}}{=}\{ \ell_0,\smiley,\frownie\}
               \cup\{ \ell_\gamma\mid\gamma\in\Gamma'\}\;,\\
     \?L_\mathrm{Adam}&  \stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{def}}}{=}\{ \ell_{(\gamma_1,\gamma_2,\gamma_3)}\mid\gamma_1,\gamma_2,\gamma_3\in\Gamma'\}
               \cup\{ \ell_{=j}\mid 0<j\leq n\}
               \cup\{ \ell_{1\leq?\leq m-n+1}\}\;.
  
$$

  The intention behind the locations $\ell_{=j}\in \?L_\mathrm{Adam}$ is
  that  Eve\ can reach $\smiley$ from a configuration $\ell_{=j}(c)$ if
  and only if $c=j$; we accordingly define $A$ with the following
  actions, where $\frownie$ is a deadlock location:
  
$$

     \ell_{=j}&\step{-j-1}\frownie\;,& \ell_{=j}&\step{-j}\smiley\;.
  \intertext{Similarly,  Eve\ should be able to reach $\smiley$ from
  $\ell_{1\leq?\leq m-n+1}(c)$ if and only if $1\leq c\leq m-n+1$,
  which is implemented by the actions}
     \ell_{1\leq?\leq m-n+1}&\step{-m+n-2}\frownie\;,&
     \ell_{1\leq?\leq m-n+1}&\step{-1}\smiley\;,&
    \smiley&\step{-1}\smiley\;.
  
$$

  Note this last action also ensures that  Eve\ can reach the
  location $\smiley$ if and only if she can reach the configuration
  $\smiley(0)$, thus the game can equivalently be seen as a
  configuration reachability game.

  Regarding initialisation,  Eve\ can choose her initial position,
  which we implement by the actions
  
$$

     \ell_0 &\step{-1}  \ell_0 &  \ell_0 &\step{-1} \ell_{(q_\mathrm{final},a)}&&\text{for $a\in\Gamma$}\;.
    \intertext{Outside the boundary cases, the game is implemented by
    the following actions:}
     \ell_\gamma&\step{-m} \ell_{(\gamma_1,\gamma_2,\gamma_3)}&&&&\text{for
  $\gamma_1,\gamma_2,\gamma_3\vdash\gamma$}\;,\\  \ell_{(\gamma_1,\gamma_2,\gamma_3)}&\step{-k} \ell_{\gamma_k}&&&&\text{for
  $k\in\{1,2,3\}$}\;.
  \intertext{We handle the endmarker positions via the following
  actions, where  Eve\ proceeds along the left edge
  of {numref}`11-fig:exp` until she reaches the initial left endmarker:}
    \ell_\triangleright&\step{-m-2} \ell_\triangleright\;,&  \ell_\triangleright&\step{-1} \ell_{=1}\;,&  \ell_\triangleleft&\step{-m-1} \ell_\triangleright\;.
  \intertext{For the positions inside the input word $w=a_1\cdots
  a_n$, we use the actions}
   \ell_{(q_0,a_1)}&\step{-2} \ell_{=1}\;,& \ell_{a_j}&\step{-2} \ell_{=j}&&\text{for
  $1<j\leq n$}\;.
  \intertext{Finally, for the blank symbols of $C_1$, which should be
  associated with a counter value $c$ such that $n+3\leq c\leq m+3$, we use the
  action}
   \ell_\Box&\step{-n-2} \ell_{1\leq?\leq m-n+1}\;.&&&&&\qedhere\hspace*{-1.5em}
  
$$

````

````{prf:theorem} Existential countdown games are  EXPSPACE-complete
:label: 11-th:countdown-exist

  Configuration reachability and coverability countdown games
  with existential initial credit are  EXPSPACE-complete.

````

````{admonition} Proof
:class: dropdown tip

   For the upper bound, consider an instance, i.e., a "countdown
   system" $\?V=( \?L, A, \?L_\mathrm{Eve}, \?L_\mathrm{Adam},1)$, an initial
   location $\ell_0$, and a target configuration $\ell_f\in \?L$.  We
   reduce this to an instance of configuration reachability with
   given initial credit in a one-dimensional vector system by
   adding a new location $\ell'_0$ controlled by  Eve\ with actions
   $\ell'_0\step{1} \ell'_0$ and $\ell'_0\step 0 \ell_0$, and asking
   whether  Eve\ has a winning strategy starting from $\ell'_0(0)$ in
   the new system.  By {prf:ref}`11-cor:dim1`, this "configuration
   reachability" game can be solved in  EXPSPACE.

   \medskip For the lower bound, we reduce from the acceptance problem
   of a deterministic Turing machine working in exponential space.
   The reduction is the same as in the proof
   of {prf:ref}`11-th:countdown-given`, except that now the length $t$ of the
   computation is not bounded a priori, but this is compensated by the
   fact that we are playing the existential initial credit version
   of the countdown game.  \qedhere%%   Indeed,  Eve\ wins the countdown game

````

\medskip
Originally, countdown games were introduced with a slightly
different objective, which corresponds to the following decision
problem.

\decpb[zero reachability with given initial credit]
  {A countdown system $\?V=( \?L,T, \?L_\mathrm{Eve}, \?L_\mathrm{Adam},1)$, an
  initial location $\ell_0\in \?L$, and an initial credit
  $n_0\in\+N$.}
  {Does  Eve\ have a strategy to reach a configuration $\ell(0)$ for
  some $\ell\in \?L$?\\That is, does she win the zero
  reachability\index{zero reachability|see{countdown game}}
  game $(\?A_\+N(\?V), \textsf{col}, \mathtt{Reach})$ from $\ell_0(n_0)$, where
  $\textsf{col}(e)= Win$ if and only if $In(e)= \ell(0)$ for some $\ell\in \?L$?}

````{prf:theorem} Countdown to zero games are  EXP-complete
:label: 11-th:countdown-zero

  Zero reachability countdown games with given initial credit
  are  EXP-complete.

````

````{admonition} Proof
:class: dropdown tip

  The upper bound of {prf:ref}`11-th:countdown-given` applies in the same
  way.  Regarding the lower bound, we modify the lower bound
  construction of {prf:ref}`11-th:countdown-given` in the following way: we
  use $\ell_0(2\cdot n_0+1)$ as initial configuration, multiply all
  the action weights in $A$ by two, and add a new
  location $\ell_\mathrm{zero}$ with an action
  $\smiley\step{-1} \ell_\mathrm{zero}$.  Because all the counter
  values in the new game are odd unless we reach $\ell_\mathrm{zero}$,
  the only way for  Eve\ to bring the counter to zero in this new game
  is to first reach $\smiley(1)$, which occurs if and only if she
  could reach $\smiley(0)$ in the original game.

````

(11-sec:one-counter)=
## Vector Games in Dimension One

Countdown games are frequently employed to prove complexity lower
bounds.  Here, we use them to show that the  EXPSPACE\ upper bounds
from {prf:ref}`11-cor:dim1` are tight in most cases.

````{prf:theorem} The complexity of vector games in dimension one
:label: 11-th:dim1

  Configuration reachability, coverability, and "parity@parity
  vector game vector games, both with given and with existential
  initial credit", are  EXPSPACE-complete in dimension one;
  non-termination vector games in dimension one are  EXP-hard with
  given initial credit and  EXPSPACE-complete with "existential
  initial credit".

````

````{admonition} Proof
:class: dropdown tip

  By {prf:ref}`11-th:countdown-exist`, configuration reachability and
  coverability vector games with existential initial credit
  are  EXPSPACE-hard in dimension one.
  Furthermore, {prf:ref}`11-rk:cov2parity` allows to deduce that
  parity@parity vector game is also  EXPSPACE-hard.  Finally, we can
  argue as in the upper bound proof of {prf:ref}`11-th:countdown-exist` that
  all these games are also hard with given initial credit: we add a
  new initial location $\ell'_0$ controlled by  Eve\ with actions
  $\ell'_0\step 1 \ell'_0$ and $\ell'_0\step 0 \ell_0$ and play the game
  starting from $\ell'_0(0)$.

  Regarding non-termination, we can add a self loop $\smiley\step
  0\smiley$ to the construction
  of {prf:ref}`11-th:countdown-given` and {prf:ref}`11-th:countdown-exist`: then the only way
  to build an infinite play that avoids the sink is to reach the
  target location $\smiley$.  This shows that the games are  EXP-hard
  with given initial credit and  EXPSPACE-hard with "existential
  initial credit.  Note that the trick of reducing existential" to
  given initial credit with an initial incrementing loop $\ell'_0\step
  1 \ell'_0$ does not work, because  Eve\ would have a trivial winning
  strategy that consists in just playing this loop forever.

````

