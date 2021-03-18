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
\newcommand*\pretime{\ensuremath{\textrm{\sf Pre}_{\geq 0}}} 
\newcommand*\reset{\mathsf{Reset}}

\def\predc{\textrm{\sf Pred}_c}
\def\predt{\textrm{\sf Pred}_{\geq 0}} 
\def\predu{\textrm{\sf Pred}_u}

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

\renewcommand{\Game}{\game}

```

We present the controllable-predecessor operator which, given sets of
states $X$ and $Y$, returns the set of states from which  \textrm{Eve} can
reach $X$ in one step, while avoiding states of $Y$ during  \textrm{Eve}'s
delay. Intuitively, the states in $Y$ are the states from which  \textrm{Adam}
may force an action leading outside of $X$, which  \textrm{Eve} would better avoid.

Recall that $V = \Locs \times \Realnn^\Clocks$.
The set of **safe time-predecessors** to reach $X \subseteq  V$ while
avoiding $Y \subseteq  V$

is defined as follows:

\begin{multline*}
\predt(X,Y) = \{(\ell,\nu) \in  V \mid \exists d\geq
    0.\ (\ell,\nu+d) \in X \wedge{} \\
    \forall d' \in[0,d).\ (\ell,\nu+d') \not  \in Y\}.
\end{multline*}

In words, from any configuration of $\predt(X,Y)$,
the set $X$ can be reached by
delaying while never crossing any configuration of $Y$ on the way. 
For any $X \subseteq  V$, let us denote

$$
  \predc(X) = \{ (\ell,\nu) \in  V \mid \exists e \in \EE(\ell).\ 
\exists (\ell',\nu') \in X.\ (\ell,\nu) \xrightarrow{e} (\ell',\nu')\}.
$$

This is the set of immediate predecessors of $X$ by edges in $\EE$.
Symmetrically, we define $\predu(X)$ using $\EA$ instead of $\EE$.
Our controllable-predecessor operator is then defined as

$$
  \pi(X) = \predt(X\cup \predc(X), \predu( V \setminus X)).
$$

Intuitively, the states in $\pi(X)$ are those from which  \textrm{Eve} can wait
until she
can take a controllable transition to reach $X$, and so that

no transitions that  \textrm{Adam} could take while  \textrm{Eve} is waiting may lead
outside of $X$.

````{prf:lemma} NEEDS TITLE 9-lem:pimonotonic
:label: 9-lem:pimonotonic

  The operator $\pi$ is 
  order-preserving: if $X\subseteq Y$, then
  $\pi(X) \subseteq \pi(Y)$.  

````

````{prf:example} NEEDS TITLE AND LABEL 
Consider the timed game to the left of
{numref}`9-fig:contpred`. In that game,  \textrm{Eve} can reach her target when
clock $x_2$ reaches value $3$ while $x_1$ is in $[1;4]$. However,
 \textrm{Adam} can take the game to a bad state when simultaneously
$x_1\in[1;2]$ and $x_2\leq 2$. The diagram to the right of
{numref}`9-fig:contpred` shows the set of winning valuations for  \textrm{Eve}:
it is computed as $\predt(X,Y)$ where $X=\predc(\{W\}\times\Realnn)$
and $Y=\predu(\{\ell_0,\ell_1\}\times\Realnn)$.

```{figure} ./../FigAndAlgos/9-fig:contpred.png
:name: 9-fig:contpred
:align: center
Controllable predecessors
```

Consider the timed game to the left of
{numref}`9-fig:contpred`. In that game,  \textrm{Eve} can reach her target when
clock $x_2$ reaches value $3$ while $x_1$ is in $[1;4]$. However,
 \textrm{Adam} can take the game to a bad state when simultaneously
$x_1\in[1;2]$ and $x_2\leq 2$. The diagram to the right of
{numref}`9-fig:contpred` shows the set of winning valuations for  \textrm{Eve}:
it is computed as $\predt(X,Y)$ where $X=\predc(\{W\}\times\Realnn)$
and $Y=\predu(\{\ell_0,\ell_1\}\times\Realnn)$.

```{figure} ./../FigAndAlgos/9-fig:contpred.png
:name: 9-fig:contpred
:align: center
Controllable predecessors
```

````

````{admonition} Remark 
  When considering zero-sum objectives (which we do in this chapter),
a turn-based arena can be built to decide whether  \textrm{Eve} has a winning
strategy (and possibly construct one).  Intuitively, the turn-based
arena is obtained by letting  \textrm{Eve} first pick a pair $(d,e)$ with $e
\in \EE$, and then letting  \textrm{Adam} either respect this choice (i.e.,
play a larger delay) or preempt  \textrm{Eve}'s action by choosing $(d',e')$
with $d' \leq d$ and $e' \in \EA$.
 \textrm{Eve} has a winning strategy in this turn-based arena if, and only if she has one in the original game.
However, this does not apply to  \textrm{Adam}; if he has a winning strategy, this only means that  \textrm{Eve}
does not have a winning strategy in the original game.

Given $\calT = (\Locs, \Clocks,\EE,\EA, c)$, we define the arena $\TA
= ( V, V_\mathrm{Eve}, V_\mathrm{Adam},E, c'')$ 
with objective $\Omega$, where $V_\mathrm{Eve} = \Locs\times \Realnn^\Clocks$ and
$V_\mathrm{Adam}=\Locs\times\Realnn^\Clocks\times(\Realnn \times \EE
\cup\{\bot\})$.  The set of successors of configuration $(\ell,\nu)
\in  V_\mathrm{Eve}$ is the set $\{(\ell,\nu,a)\mid a \text{ available at
}(\ell,\nu)\}$.

From a configuration $((\ell,\nu),(d,e))\in V_\mathrm{Adam}$, several cases may
occur:

*  if  \textrm{Adam} has no available action from $(\ell,\nu)$, or if he can
  only play actions $(d',e')$ with $d'>d$, then the only transition
  from $((\ell,\nu),(d,e))$ goes to $\step((\ell,\nu),(d,e))$;
*  Otherwise, for all actions $(d',e')$ for  \textrm{Adam} satisfying $d'\leq d$,
  there is a transition from $((\ell,\nu),(d,e))$
  to $\step((\ell,\nu),(d',e'))$.
  Moreover, if  \textrm{Adam} has an available action $(d',e')$ with $d'\geq d$,
  then there is also a transition
  from $((\ell,\nu),(d,e))$ to $\step((\ell,\nu),(d,e))$.

From a configuration $((\ell,\nu),\bot)$, there is a transition
to $\step((\ell,\nu),(d',e'))$ for each available action $(d',e')$
of  \textrm{Adam}.
The coloring function is defined as $c''((\ell,\nu)) = c(\ell)$
and $c''((\ell,\nu),(d,e)) = c(\ell)$.

````

