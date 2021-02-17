(11-sec:dim1)=
# Games in dimension one

```{math}
\newcommand{\?}{\mathcal}
\newcommand{\+}{\mathbb}
\newcommand{\tup}[1]{\langle #1\rangle}
\newcommand{\eqby}[1]{\stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{#1}}}}{=}}
\newcommand{\eqdef}{\eqby{def}}
\newcommand{\Loc}{\?L}
\newcommand{\Act}{A}
\providecommand{\dom}[1]{\mathrm{dom}\,#1}
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
\AP \Cref{11-th-undec} leaves open whether vector games might be
decidable in dimension one.  They are indeed decidable, and more
generally we learned in Chapter {ref}`10-chap:pushdown` that "one-counter
games"---with the additional ability to test the counter for
zero---were decidable and in fact \PSPACE-complete.  This might seem
to settle the case of vector games in dimension one, except that the
one-counter games of Chapter {ref}`10-chap:pushdown` only allow integer
weights in $\{-1,1\}$, whereas we allow arbitrary updates in $\+Z$
with a binary encoding.  Hence the \PSPACE\ upper bound of
\cref{chap:pushdown} becomes an~\EXPSPACE\ one for succinct
one-counter games.

````{prf:corollary} NEEDS TITLE 11-cor-dim1
:label: 11-cor-dim1

  Configuration reachability, coverability, non-termination, and
  parity@parity vector game vector games, both with given and with "existential
  initial credit", are in \EXPSPACE\ in dimension one.

````

````{admonition} Proof
:class: dropdown tip
\\
  \TODO{proof of \cref{11-cor-dim1} depends on how Section {ref}`11-sec:one-counter` is written}

````

The goal of this section is therefore to establish that this
\EXPSPACE\ upper bound is tight (in most cases), by proving a matching
lower bound in \cref{11-one-counter}.  But first, we will study a
class of one-dimensional vector games of independent interest in
\cref{11-countdown}: countdown games.

(11-countdown)=
## Countdown Games

\AP A one-dimensional vector system
$\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,1)$ is called a countdown
system if $\Act\subseteq\Loc\times\+Z_{<0}\times\Loc$, that is, if
for all $(\loc\step z\loc')\in\Act$, $z<0$.  We consider the games
defined by countdown systems, both with given and with
existential initial credit, and call the resulting games countdown
games.

````{prf:theorem} NEEDS TITLE 11-countdown-given
:label: 11-countdown-given

  Configuration reachability and coverability countdown games
  with given initial credit are \EXP-complete.

````

````{admonition} Proof
:class: dropdown tip

  For the upper bound, consider an instance, i.e., a "countdown
  system" $\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,1)$, an initial
  location $\loc_0\in\Loc$, an initial credit $n_0\in\+N$, and a
  target configuration $\loc_f(n_f)\in\Loc\times\+N$.  Because every
  action decreases strictly the counter value, the reachable part
  of the natural semantics of $\?V$ starting from $\loc_0(n_0)$ is
  finite and of size at most $1+|\Loc|\cdot (n_0+1)$, and because $n_0$
  is encoded in binary, this is at most exponential in the size of the
  instance.  As seen in \cref{chap:regular}, such a reachability
  game can be solved in time polynomial in the size of the finite
  graph, thus in \EXP\ overall.

  \medskip For the lower bound, we start by considering a game played
  over an exponential-time Turing machine, before showing how to
  implement this game as a countdown game.  Let us consider for this
  an arbitrary Turing machine $\?M$ working in deterministic
  exponential time $2^{p(n)}$ for some fixed polynomial $p$ and an
  input word $w=a_1\cdots a_n$ of length $n$, which we assume to be
  positive.  Let $m\eqdef 2^{p(n)}\geq n$.  The computation of $\?M$
  on $w$ is a sequence of configurations $C_1,C_2,\dots,C_t$ of
  length $t\leq m$.  Each configuration $C_i$ is of the form
  $\emkl \gamma_{i,1}\cdots\gamma_{i,m}\emkr$ where $\emkl$ and
  $\emkr$ are endmarkers and the symbols $\gamma_{i,j}$ are either
  taken from the finite tape alphabet $\Gamma$ (which includes a blank
  symbol $\blank$) or a pair $(q,a)$ of a state from $Q$ and a tape
  symbol $a$.  We assume that the set of states $Q$ contains a single
  accepting state $q_\mathrm{final}$.  The entire computation can be
  arranged over a $t\times m$ grid as shown in \cref{11-fig-exp}.

  \begin{figure}[htbp]
    \centering
    \hspace*{-.5ex}\begin{tikzpicture}[on grid,every node/.style={anchor=base}]
      \draw[step=1,lightgray!50,dotted] (-.5,-0.8) grid (10.5,-5.2);
                \node[anchor=east] at (-.5,-5) {$C_1$};
      \node[anchor=east] at (-.5,-4) {$C_2$};
      \node[anchor=east] at (-.5,-3.4) {$\vdots $};
      \node[anchor=east] at (-.5,-3) {$C_{i-1}$};
      \node[anchor=east] at (-.5,-2) {$C_i$};
      \node[anchor=east] at (-.5,-1.4) {$\vdots $};
      \node[anchor=east] at (-.5,-1) {$C_t$};
           \draw[color=white](4,-.5) -- (4,-5.2) (8,-.5) -- (8,-5.2);
      \node[lightgray] at (0,-.5) {$0$};
      \node[lightgray] at (1,-.5) {$1$};
      \node[lightgray] at (2,-.5) {$2$};
      \node[lightgray] at (3,-.5) {$3$};
      \node[lightgray] at (4,-.5) {$\cdots$};
      \node[lightgray] at (5,-.5) {$j-1$};
      \node[lightgray] at (6,-.5) {$j$};
      \node[lightgray] at (7,-.5) {$j+1$};
      \node[lightgray] at (8,-.5) {$\cdots$};
      \node[lightgray] at (9,-.5) {$m$};
      \node[lightgray] at (10,-.5) {$m+1$};
           \node at (0,-1.1) {$\emkl$};
      \node at (0,-2.1) {$\emkl$};
      \node at (0,-3.1) {$\emkl$};
      \node at (0,-4.1) {$\emkl$};
      \node at (0,-5.1) {$\emkl$};
      \node at (10,-1.1) {$\emkr$};
      \node at (10,-2.1) {$\emkr$};
      \node at (10,-3.1) {$\emkr$};
      \node at (10,-4.1) {$\emkr$};
      \node at (10,-5.1) {$\emkr$};
           \node at (1,-5.1) {$q_0,a_1$};
      \node at (2,-5.1) {$a_2$};
      \node at (3,-5.1) {$a_3$};
      \node at (4,-5.1) {$\cdots$};
      \node at (5,-5.1) {$\blank$};
      \node at (6,-5.1) {$\blank$};
      \node at (7,-5.1) {$\blank$};
      \node at (8,-5.1) {$\cdots$};
      \node at (9,-5.1) {$\blank$};
           \node at (1,-4.1) {$a'_1$};
      \node at (2,-4.1) {$q_1,a_2$};
      \node at (3,-4.1) {$a_3$};
      \node at (4,-4.1) {$\cdots$};
      \node at (5,-4.1) {$\blank$};
      \node at (6,-4.1) {$\blank$};
      \node at (7,-4.1) {$\blank$};
      \node at (8,-4.1) {$\cdots$};
      \node at (9,-4.1) {$\blank$};
           \node at (5,-3.7) {$\vdots$};
      \node at (6,-3.7) {$\vdots$};
      \node at (7,-3.7) {$\vdots$};
      \node at (4,-3.1) {$\cdots$};
      \node at (5,-3.1) {$\gamma_{i-1,j-1}$};
      \node at (6,-3.1) {$\gamma_{i-1,j}$};
      \node at (7,-3.1) {$\gamma_{i-1,j+1}$};
      \node at (8,-3.1) {$\cdots$};
           \node at (5,-2.1) {$\cdots$};
      \node at (6,-2.1) {$\gamma_{i,j}$};
      \node at (7,-2.1) {$\cdots$};
      \node at (6,-1.7) {$\vdots$};
           \node at (1,-1.1) {$q_\mathrm{final},\blank$};
      \node at (2,-1.1) {$\blank$};
      \node at (3,-1.1) {$\blank$};
      \node at (4,-1.1) {$\cdots$};
      \node at (5,-1.1) {$\blank$};
      \node at (6,-1.1) {$\blank$};
      \node at (7,-1.1) {$\blank$};
      \node at (8,-1.1) {$\cdots$};
      \node at (9,-1.1) {$\blank$};      
      \end{tikzpicture}
    \caption{\label{11-fig-exp}The computation of $\?M$ on
  input $w=a_1\cdots a_n$.  This particular picture assumes $\?M$
  starts by rewriting $a_1$ into $a'_1$ and moving to the right in a
  state $q_1$, and empties its tape before accepting its input by going
  to state $q_\mathrm{final}$.}
  \end{figure}

  We now set up a two-player game where \Eve wants to prove that the
  input $w$ is accepted.  Let
  $\Gamma'\eqdef \{\emkl,\emkr\}\cup\Gamma\cup(Q\times\Gamma)$. Rather
  than exhibiting the full computation from \cref{11-fig-exp}, the
  game will be played over positions $(i,j,\gamma_{i,j})$ where
  $0<i\leq m$, $0\leq j\leq m+1$, and $\gamma_{i,j}\in\Gamma'$.  \Eve
  wants to show that, in the computation of $\?M$ over $w$ as depicted
  in \cref{11-fig-exp}, the $j$th cell of the $i$th
  configuration $C_i$ contains $\gamma_{i,j}$.  In order to
  substantiate this claim, observe that the content of any cell
  $\gamma_{i,j}$ in the grid is determined by the actions of $\?M$
  and the contents of (up to) three cells in the previous
  configuration.  Thus, if $i>1$ and $0<j<m+1$, \Eve provides a triple
  $(\gamma_{i-1,j-1},\gamma_{i-1,j},\gamma_{i-1,j+1})$ of symbols
  in $\Gamma'$ that yield $\gamma_{i,j}$ according to the actions
  of $\?M$, which we denote by
  $\gamma_{i-1,j-1},\gamma_{i-1,j},\gamma_{i-1,j+1}\vdash\gamma_{i,j}$,
  and \Adam chooses $j'\in\{j-1,j,j+1\}$ and returns the control
  to \Eve in position $(i-1,j',\gamma_{i-1,j'})$.  Regarding the
  boundary cases where $i=0$ or $j=0$ or $j=m+1$, \Eve wins
  immediately if $j=0$ and $\gamma={\emkl}$, or if $j=m+1$ and
  $\gamma={\emkr}$, or if $i=0$ and $0<j\leq n$ and $\gamma=a_j$, or if
  $i=0$ and $n<j\leq m$ and $\gamma={\blank}$, and otherwise \Adam wins
  immediately.  The game starts in a position
  $(t,j,(q_\mathrm{final},a))$ for some $0<t\leq m$, $0< j\leq m$,
  and $a\in\Gamma$ of \Eve's choosing.  It should be clear that \Eve
  has a winning strategy in this game if and only if $w$ is accepted
  by $\?M$.

  We now implement the previous game as a coverability game over a
  countdown system $\?V\eqdef(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,1)$.
  The idea is that the pair $(i,j)$ will be encoded as
  $(i-1)\cdot(m+2)+j+2$ in the counter value, while the
  symbol $\gamma_{i,j}$ will be encoded in the location.  For
  instance, the endmarker $\emkl$ at position $(1,0)$ will be
  represented by configuration $\loc_{\emkl}(2)$, the first input
  $(q_0,a_1)$ at position $(1,1)$ by $\loc_{(q_0,a_1)}(3)$, and the
  endmarker $\emkr$ at position $(m,m+1)$ by
  $\loc_{\emkr}(m\cdot(m+2)+1)$. The game starts from the initial
  configuration $\loc_0(n_0)$ where $n_0\eqdef m\cdot(m+2)+1$ and the
  target location is $\smiley$.

  We define for this the sets of locations
  \begin{align*}
    \Loc_\mEve&\eqdef\{\loc_0,\smiley,\frownie\}
               \cup\{\loc_\gamma\mid\gamma\in\Gamma'\}\;,\\
    \Loc_\mAdam&\eqdef\{\loc_{(\gamma_1,\gamma_2,\gamma_3)}\mid\gamma_1,\gamma_2,\gamma_3\in\Gamma'\}
               \cup\{\loc_{=j}\mid 0<j\leq n\}
               \cup\{\loc_{1\leq?\leq m-n+1}\}\;.
  \end{align*}
  The intention behind the locations $\loc_{=j}\in\Loc_\mAdam$ is
  that \Eve can reach $\smiley$ from a configuration $\loc_{=j}(c)$ if
  and only if $c=j$; we accordingly define $\Act$ with the following
  actions, where $\frownie$ is a deadlock location:
  \begin{align*}
    \loc_{=j}&\step{-j-1}\frownie\;,&\loc_{=j}&\step{-j}\smiley\;.
  \intertext{Similarly, \Eve should be able to reach $\smiley$ from
  $\loc_{1\leq?\leq m-n+1}(c)$ if and only if $1\leq c\leq m-n+1$,
  which is implemented by the actions}
    \loc_{1\leq?\leq m-n+1}&\step{-m+n-2}\frownie\;,&
    \loc_{1\leq?\leq m-n+1}&\step{-1}\smiley\;,&
    \smiley&\step{-1}\smiley\;.
  \end{align*}
  Note this last action also ensures that \Eve can reach the
  location $\smiley$ if and only if she can reach the configuration
  $\smiley(0)$, thus the game can equivalently be seen as a
  configuration reachability game.

  Regarding initialisation, \Eve can choose her initial position,
  which we implement by the actions
  \begin{align*}
    \loc_0 &\step{-1} \loc_0 & \loc_0 &\step{-1}\loc_{(q_\mathrm{final},a)}&&\text{for $a\in\Gamma$}\;.
    \intertext{Outside the boundary cases, the game is implemented by
    the following actions:}
    \loc_\gamma&\step{-m}\loc_{(\gamma_1,\gamma_2,\gamma_3)}&&&&\text{for
  $\gamma_1,\gamma_2,\gamma_3\vdash\gamma$}\;,\\ \loc_{(\gamma_1,\gamma_2,\gamma_3)}&\step{-k}\loc_{\gamma_k}&&&&\text{for
  $k\in\{1,2,3\}$}\;.
  \intertext{We handle the endmarker positions via the following
  actions, where \Eve proceeds along the left edge
  of \cref{11-fig-exp} until she reaches the initial left endmarker:}
   \loc_\emkl&\step{-m-2}\loc_\emkl\;,& \loc_\emkl&\step{-1}\loc_{=1}\;,& \loc_\emkr&\step{-m-1}\loc_\emkl\;.
  \intertext{For the positions inside the input word $w=a_1\cdots
  a_n$, we use the actions}
  \loc_{(q_0,a_1)}&\step{-2}\loc_{=1}\;,&\loc_{a_j}&\step{-2}\loc_{=j}&&\text{for
  $1<j\leq n$}\;.
  \intertext{Finally, for the blank symbols of $C_1$, which should be
  associated with a counter value $c$ such that $n+3\leq c\leq m+3$, we use the
  action}
  \loc_\blank&\step{-n-2}\loc_{1\leq?\leq m-n+1}\;.&&&&&\qedhere\hspace*{-1.5em}
  \end{align*}

````



````{prf:theorem} NEEDS TITLE 11-countdown-exist
:label: 11-countdown-exist

  Configuration reachability and coverability countdown games
  with existential initial credit are \EXPSPACE-complete.

````

````{admonition} Proof
:class: dropdown tip

   For the upper bound, consider an instance, i.e., a "countdown
   system" $\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,1)$, an initial
   location $\loc_0$, and a target configuration $\loc_f\in\Loc$.  We
   reduce this to an instance of configuration reachability with
   given initial credit in a one-dimensional vector system by
   adding a new location $\loc'_0$ controlled by~\Eve with actions
   $\loc'_0\step{1}\loc'_0$ and $\loc'_0\step 0\loc_0$, and asking
   whether \Eve has a winning strategy starting from $\loc'_0(0)$ in
   the new system.  By \cref{11-cor-dim1}, this "configuration
   reachability" game can be solved in \EXPSPACE.

   \medskip For the lower bound, we reduce from the acceptance problem
   of a deterministic Turing machine working in exponential space.
   The reduction is the same as in the proof
   of \cref{11-countdown-given}, except that now the length $t$ of the
   computation is not bounded a priori, but this is compensated by the
   fact that we are playing the existential initial credit version
   of the countdown game.  \qedher        
````

\medskip
Originally, countdown games were introduced with a slightly
different objective, which corresponds to the following decision
problem.
\AP\decpb[zero reachability with given initial credit]
  {A countdown system $\?V=(\Loc,T,\Loc_\mEve,\Loc_\mAdam,1)$, an
  initial location $\loc_0\in\Loc$, and an initial credit
  $n_0\in\+N$.}
  {Does \Eve have a strategy to reach a configuration $\loc(0)$ for
  some $\loc\in\Loc$?\\That is, does she win the zero
  reachability\index{zero reachability|see{countdown game}}
  game $(\?A_\+N(\?V),\col,\Reach)$ from $\loc_0(n_0)$, where
  $\col(e)=\Win$ if and only if $\ing(e)=\loc(0)$ for some $\loc\in\Loc$?}

````{prf:theorem} NEEDS TITLE 11-countdown-zero
:label: 11-countdown-zero

  Zero reachability countdown games with given initial credit
  are \EXP-complete.

````

````{admonition} Proof
:class: dropdown tip

  The upper bound of \cref{11-countdown-given} applies in the same
  way.  Regarding the lower bound, we modify the lower bound
  construction of \cref{11-countdown-given} in the following way: we
  use $\loc_0(2\cdot n_0+1)$ as initial configuration, multiply all
  the action weights in $\Act$ by two, and add a new
  location $\loc_\mathrm{zero}$ with an action
  $\smiley\step{-1}\loc_\mathrm{zero}$.  Because all the counter
  values in the new game are odd unless we reach $\loc_\mathrm{zero}$,
  the only way for \Eve to bring the counter to zero in this new game
  is to first reach $\smiley(1)$, which occurs if and only if she
  could reach $\smiley(0)$ in the original game.

````


(11-one-counter)=
## Vector Games in Dimension One

Countdown games are frequently employed to prove complexity lower
bounds.  Here, we use them to show that the \EXPSPACE\ upper bounds
from \cref{11-cor-dim1} are tight in most cases.

````{prf:theorem} NEEDS TITLE 11-th-dim1
:label: 11-th-dim1

  Configuration reachability, coverability, and "parity@parity
  vector game vector games, both with given and with existential
  initial credit", are \EXPSPACE-complete in dimension one;
  non-termination vector games in dimension one are \EXP-hard with
  given initial credit and \EXPSPACE-complete with "existential
  initial credit".

````

````{admonition} Proof
:class: dropdown tip

  By \cref{11-countdown-exist}, configuration reachability and
  coverability vector games with existential initial credit
  are \EXPSPACE-hard in dimension one.
  Furthermore, \cref{11-cov2parity} allows to deduce that
  parity@parity vector game is also \EXPSPACE-hard.  Finally, we can
  argue as in the upper bound proof of \cref{11-countdown-exist} that
  all these games are also hard with given initial credit: we add a
  new initial location $\loc'_0$ controlled by \Eve with actions
  $\loc'_0\step 1\loc'_0$ and $\loc'_0\step 0\loc_0$ and play the game
  starting from $\loc'_0(0)$.

  Regarding non-termination, we can add a self loop $\smiley\step
  0\smiley$ to the construction
  of \cref{11-countdown-given,12-countdown-exist}: then the only way
  to build an infinite play that avoids the sink is to reach the
  target location $\smiley$.  This shows that the games are \EXP-hard
  with given initial credit and \EXPSPACE-hard with "existential
  initial credit.  Note that the trick of reducing existential" to
  given initial credit with an initial incrementing loop $\loc'_0\step
  1\loc'_0$ does not work, because \Eve would have a trivial winning
  strategy that consists in just playing this loop forever.

````

