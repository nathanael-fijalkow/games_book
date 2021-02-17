(9-sec:controllable_predecessor_operator)=
# Controllable-Predecessor Operator

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
We present the controllable-predecessor operator which, given sets of
states $X$ and $Y$, returns the set of states from which \Eve can
reach $X$ in one step, while avoiding states of $Y$ during \Eve's
delay. Intuitively, the states in $Y$ are the states from which \Adam
may force an action leading outside of $X$, which \Eve would better avoid.

Recall that $\vertices = \Locs \times \Realnn^\Clocks$.
The set of **safe time-predecessors** to reach $X \subseteq \vertices$ while
avoiding $Y \subseteq \vertices$

is defined as follows:

%  \begin{array}{ll}
\begin{multline*}
\predt(X,Y) = \{(\ell,\nu) \in \vertices \mid \exists d\geq
    0.\ (\ell,\nu+d) \in X \wedge{} \\
    \forall d' \in[0,d).\ (\ell,\nu+d') \not  \in Y\}.
\end{multline*}

%\]
In words, from any configuration of $\predt(X,Y)$,
the set $X$ can be reached by
delaying while never crossing any configuration of $Y$ on the way. 
For any $X \subseteq \vertices$, let us denote

$$
  \predc(X) = \{ (\ell,\nu) \in \vertices \mid \exists e \in \EE(\ell).\ 
\exists (\ell',\nu') \in X.\ (\ell,\nu) \xrightarrow{e} (\ell',\nu')\}.
$$

This is the set of immediate predecessors of $X$ by edges in $\EE$.
Symmetrically, we~define $\predu(X)$ using $\EA$ instead of $\EE$.
Our controllable-predecessor operator is then defined as 

%\NM{Replace $\predc(X)$ with $X\cup\predc(X)$? besoin dans une preuve, je crois. A verifier}


$$
  \pi(X) = \predt(X\cup \predc(X), \predu(\vertices \setminus X)).
$$



%  Reecrire avec jeux concurrents + ajouter remarque jeux a tours}

Intuitively, the states in $\pi(X)$ are those from which \Eve~can wait
until she
can take a controllable transition to~reach $X$, and so that

%inside $X$.
no transitions that \Adam could take while \Eve is waiting may lead
outside of $X$.

````{prf:lemma} NEEDS TITLE 9-lem:pimonotonic
:label: 9-lem:pimonotonic

  The operator $\pi$ is 
  order-preserving: if $X\subseteq Y$, then
  $\pi(X) \subseteq \pi(Y)$.  

````


````{prf:example} NEEDS TITLE AND LABEL 
Consider the timed game to the left of
{numref}`9-fig:contpred`. In~that game, \Eve can reach her target when
clock $x_2$ reaches value $3$ while $x_1$ is in $[1;4]$. However,
\Adam can take the game to a bad state when simultaneously
$x_1\in[1;2]$ and $x_2\leq 2$. The~diagram to the right of
{numref}`9-fig:contpred` shows the set of winning valuations for~\Eve:
it~is computed as $\predt(X,Y)$ where $X=\predc(\{W\}\times\Realnn)$
and $Y=\predu(\{\ell_0,\ell_1\}\times\Realnn)$.

```{figure} ./../FigAndAlgos/9-fig:contpred.png
:name: 9-fig:contpred
:align: center
Controllable predecessors
```
 

Consider the timed game to the left of
{numref}`9-fig:contpred`. In~that game, \Eve can reach her target when
clock $x_2$ reaches value $3$ while $x_1$ is in $[1;4]$. However,
\Adam can take the game to a bad state when simultaneously
$x_1\in[1;2]$ and $x_2\leq 2$. The~diagram to the right of
{numref}`9-fig:contpred` shows the set of winning valuations for~\Eve:
it~is computed as $\predt(X,Y)$ where $X=\predc(\{W\}\times\Realnn)$
and $Y=\predu(\{\ell_0,\ell_1\}\times\Realnn)$.

```{figure} ./../FigAndAlgos/9-fig:contpred.png
:name: 9-fig:contpred
:align: center
Controllable predecessors
```

````

%   Consider a timed arena $\calT$.

%   
%   and any configuration ${q \in \vertices}$, it~holds $q \in \pi(X)$ if, and only~if

% \end{lemma}


%   .... \NM{(re)definir $\textsf{Attr}_\TA(X)$? Mettre ref section 2.1 ?}


% for $\Eve$. It is the timed automata analogue to Theorem ....

%   \label{9-thm:fp}

%   a configuration $q$ is winning for $\Eve$ if, and only if

%   $q \in X$ and $X = \pi(X)$.

% \end{theorem}



````{admonition} Remark 
  When considering zero-sum objectives (which we do in this chapter),
a~turn-based arena can be built to decide whether \Eve has a winning
strategy (and~possibly construct~one).  Intuitively, the turn-based
arena is obtained by letting \Eve first pick a pair $(d,e)$ with $e
\in \EE$, and then letting \Adam either respect this choice (i.e.,
play a larger delay) or preempt \Eve's action by choosing $(d',e')$
with $d' \leq d$ and $e' \in \EA$.
\Eve has a winning strategy in this turn-based arena if, and only if she has one in the original game.
However, this does not apply to \Adam; if he has a winning strategy, this only means that \Eve
does not have a winning strategy in the original game.

Given $\calT = (\Locs, \Clocks,\EE,\EA, c)$, we define the arena $\TA
= (\vertices,\VE,\VA,E, c'')$ 
with objective $\Omega$, where $\VE = \Locs\times \Realnn^\Clocks$ and
$\VA=\Locs\times\Realnn^\Clocks\times(\Realnn \times \EE
\cup\{\bot\})$.  The~set of successors of configuration $(\ell,\nu)
\in \VE$ is the set $\{(\ell,\nu,a)\mid a \text{ available at
}(\ell,\nu)\}$.

%  \{ (\ell,\nu,(d,e)) \mid e \text{ valid at } \nu+d\},

From a configuration $((\ell,\nu),(d,e))\in\VA$, several cases may
occur:

*  if \Adam has no available action from $(\ell,\nu)$, or if he can
  only play actions $(d',e')$ with $d'>d$, then the only transition
  from $((\ell,\nu),(d,e))$ goes to $\step((\ell,\nu),(d,e))$;
*  Otherwise, for all actions $(d',e')$ for \Adam satisfying $d'\leq d$,
  there is a transition from $((\ell,\nu),(d,e))$
  to $\step((\ell,\nu),(d',e'))$.
  Moreover, if \Adam has an available action $(d',e')$ with $d'\geq d$,
  then there is also a transition
  from $((\ell,\nu),(d,e))$ to $\step((\ell,\nu),(d,e))$.

%   there is a transition from $((\ell,\nu),(d,e))$


%  \{\step((\ell,\nu),(d,e))\}

%  \{ (\step((\ell,\nu), (d',e')) \mid d' \leq d, e' \in \EA(\ell), e'+d' \models g_{e'}\}.

From a configuration $((\ell,\nu),\bot)$, there is a transition
to $\step((\ell,\nu),(d',e'))$ for each available action $(d',e')$
of~\Adam.
The coloring function is defined as $c''((\ell,\nu)) = c(\ell)$
and $c''((\ell,\nu),(d,e)) = c(\ell)$.

%and the above edges for each player. We do not need its precise definition



````

