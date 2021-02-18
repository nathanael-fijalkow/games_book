(9-sec:controllable_predecessor_operator)=
# Controllable-Predecessor Operator


```{math}
\newcommand{\Eve}{\textrm{Eve}}
\newcommand{\Adam}{\textrm{Adam}}
\newcommand{\vertices}{V}
\newcommand{\VE}{V_\mEve}
\newcommand{\VA}{V_\mAdam}
\newcommand{\mEve}{\mathrm{Eve}}
\newcommand{\mAdam}{\mathrm{Adam}}
```

We present the controllable-predecessor operator which, given sets of
states $X$ and $Y$, returns the set of states from which \textrm{Eve}can
reach $X$ in one step, while avoiding states of $Y$ during \textrm{Eve}s
delay. Intuitively, the states in $Y$ are the states from which \textrm{Adam}may force an action leading outside of $X$, which \textrm{Eve}would better avoid.

Recall that $V= \Locs \times \Realnn^\Clocks$.
The set of **safe time-predecessors** to reach $X \subseteq V while
avoiding $Y \subseteq V

is defined as follows:

%  \begin{array}{ll}
\begin{multline*}
\predt(X,Y) = \{(\ell,\nu) \in V\mid \exists d\geq
    0.\ (\ell,\nu+d) \in X \wedge{} \\
    \forall d' \in[0,d).\ (\ell,\nu+d') \not  \in Y\}.
\end{multline*}

%\]
In words, from any configuration of $\predt(X,Y)$,
the set $X$ can be reached by
delaying while never crossing any configuration of $Y$ on the way. 
For any $X \subseteq V, let us denote

$$
  \predc(X) = \{ (\ell,\nu) \in V\mid \exists e \in \EE(\ell).\ 
\exists (\ell',\nu') \in X.\ (\ell,\nu) \xrightarrow{e} (\ell',\nu')\}.
$$

This is the set of immediate predecessors of $X$ by edges in $\EE$.
Symmetrically, we~define $\predu(X)$ using $\EA$ instead of $\EE$.
Our controllable-predecessor operator is then defined as 

%\NM{Replace $\predc(X)$ with $X\cup\predc(X)$? besoin dans une preuve, je crois. A verifier}


$$
  \pi(X) = \predt(X\cup \predc(X), \predu(V\setminus X)).
$$



%  Reecrire avec jeux concurrents + ajouter remarque jeux a tours}

Intuitively, the states in $\pi(X)$ are those from which \textrm{Eve}can wait
until she
can take a controllable transition to~reach $X$, and so that

%inside $X$.
no transitions that \textrm{Adam}could take while \textrm{Eve}is waiting may lead
outside of $X$.

````{prf:lemma} NEEDS TITLE 9-lem:pimonotonic
:label: 9-lem:pimonotonic

  The operator $\pi$ is 
  order-preserving: if $X\subseteq Y$, then
  $\pi(X) \subseteq \pi(Y)$.  

````


````{prf:example} NEEDS TITLE AND LABEL 
Consider the timed game to the left of
{numref}`9-fig:contpred`. In~that game, \textrm{Eve}can reach her target when
clock $x_2$ reaches value $3$ while $x_1$ is in $[1;4]$. However,
\textrm{Adam}can take the game to a bad state when simultaneously
$x_1\in[1;2]$ and $x_2\leq 2$. The~diagram to the right of
{numref}`9-fig:contpred` shows the set of winning valuations for~\textrm{Eve}
it~is computed as $\predt(X,Y)$ where $X=\predc(\{W\}\times\Realnn)$
and $Y=\predu(\{\ell_0,\ell_1\}\times\Realnn)$.

```{figure} ./../FigAndAlgos/9-fig:contpred.png
:name: 9-fig:contpred
:align: center
Controllable predecessors
```
 

Consider the timed game to the left of
{numref}`9-fig:contpred`. In~that game, \textrm{Eve}can reach her target when
clock $x_2$ reaches value $3$ while $x_1$ is in $[1;4]$. However,
\textrm{Adam}can take the game to a bad state when simultaneously
$x_1\in[1;2]$ and $x_2\leq 2$. The~diagram to the right of
{numref}`9-fig:contpred` shows the set of winning valuations for~\textrm{Eve}
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
%   and any configuration ${q \in V$, it~holds $q \in \pi(X)$ if, and only~if

% \end{lemma}


%   .... \NM{(re)definir $\textsf{Attr}_\TA(X)$? Mettre ref section 2.1 ?}


% for $\textrm{Eve}. It is the timed automata analogue to Theorem ....

%   \label{9-thm:fp}

%   a configuration $q$ is winning for $\textrm{Eve} if, and only if

%   $q \in X$ and $X = \pi(X)$.

% \end{theorem}



````{admonition} Remark 
  When considering zero-sum objectives (which we do in this chapter),
a~turn-based arena can be built to decide whether \textrm{Eve}has a winning
strategy (and~possibly construct~one).  Intuitively, the turn-based
arena is obtained by letting \textrm{Eve}first pick a pair $(d,e)$ with $e
\in \EE$, and then letting \textrm{Adam}either respect this choice (i.e.,
play a larger delay) or preempt \textrm{Eve}s action by choosing $(d',e')$
with $d' \leq d$ and $e' \in \EA$.
\textrm{Eve}has a winning strategy in this turn-based arena if, and only if she has one in the original game.
However, this does not apply to \textrm{Adam} if he has a winning strategy, this only means that \textrm{Eve}does not have a winning strategy in the original game.

Given $\calT = (\Locs, \Clocks,\EE,\EA, c)$, we define the arena $\TA
= (VV_\mEveV_\mAdamE, c'')$ 
with objective $\Omega$, where $V_\mathrm{Eve} \Locs\times \Realnn^\Clocks$ and
$V_\mathrm{Adam}Locs\times\Realnn^\Clocks\times(\Realnn \times \EE
\cup\{\bot\})$.  The~set of successors of configuration $(\ell,\nu)
\in V_\mathrm{Eve}is the set $\{(\ell,\nu,a)\mid a \text{ available at
}(\ell,\nu)\}$.

%  \{ (\ell,\nu,(d,e)) \mid e \text{ valid at } \nu+d\},

From a configuration $((\ell,\nu),(d,e))\inV_\mathrm{Adam} several cases may
occur:

*  if \textrm{Adam}has no available action from $(\ell,\nu)$, or if he can
  only play actions $(d',e')$ with $d'>d$, then the only transition
  from $((\ell,\nu),(d,e))$ goes to $\step((\ell,\nu),(d,e))$;
*  Otherwise, for all actions $(d',e')$ for \textrm{Adam}satisfying $d'\leq d$,
  there is a transition from $((\ell,\nu),(d,e))$
  to $\step((\ell,\nu),(d',e'))$.
  Moreover, if \textrm{Adam}has an available action $(d',e')$ with $d'\geq d$,
  then there is also a transition
  from $((\ell,\nu),(d,e))$ to $\step((\ell,\nu),(d,e))$.

%   there is a transition from $((\ell,\nu),(d,e))$


%  \{\step((\ell,\nu),(d,e))\}

%  \{ (\step((\ell,\nu), (d',e')) \mid d' \leq d, e' \in \EA(\ell), e'+d' \models g_{e'}\}.

From a configuration $((\ell,\nu),\bot)$, there is a transition
to $\step((\ell,\nu),(d',e'))$ for each available action $(d',e')$
of~\textrm{Adam}
The coloring function is defined as $c''((\ell,\nu)) = c(\ell)$
and $c''((\ell,\nu),(d,e)) = c(\ell)$.

%and the above edges for each player. We do not need its precise definition



````

