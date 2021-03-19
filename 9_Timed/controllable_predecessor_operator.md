(9-sec:controllable_predecessor_operator)=
# Controllable-Predecessor Operator

```{math}

\renewcommand{\Game}{\game}

```

We present the controllable-predecessor operator which, given sets of
states $X$ and $Y$, returns the set of states from which Eve can
reach $X$ in one step, while avoiding states of $Y$ during Eve's
delay. Intuitively, the states in $Y$ are the states from which Adam
may force an action leading outside of $X$, which Eve would better avoid.

Recall that $V =  \mathcal{L} \times  \mathbb{R}_{\geq 0}^ \mathcal{C}$.
The set of **safe time-predecessors** to reach $X \subseteq  V$ while
avoiding $Y \subseteq  V$

is defined as follows:

\begin{multline*}
 \mathsf{Pred}_{\geq 0}(X,Y) = \{(\ell,\nu) \in  V \mid \exists d\geq
    0.\ (\ell,\nu+d) \in X \wedge{} \\
    \forall d' \in[0,d).\ (\ell,\nu+d') \not  \in Y\}.
\end{multline*}

In words, from any configuration of $\mathsf{Pred}_{\geq 0}(X,Y)$,
the set $X$ can be reached by
delaying while never crossing any configuration of $Y$ on the way. 
For any $X \subseteq  V$, let us denote

$$
   \mathsf{Pred}_c(X) = \{ (\ell,\nu) \in  V \mid \exists e \in  E_{ \textrm{Eve}}(\ell).\ 
\exists (\ell',\nu') \in X.\ (\ell,\nu) \xrightarrow{e} (\ell',\nu')\}.
$$

This is the set of immediate predecessors of $X$ by edges in $E_{ \textrm{Eve}}$.
Symmetrically, we define $\mathsf{Pred}_u(X)$ using $E_{ \textrm{Adam}}$ instead of $E_{ \textrm{Eve}}$.
Our controllable-predecessor operator is then defined as

$$
  \pi(X) =  \mathsf{Pred}_{\geq 0}(X\cup  \mathsf{Pred}_c(X),  \mathsf{Pred}_u( V \setminus X)).
$$

Intuitively, the states in $\pi(X)$ are those from which Eve can wait
until she
can take a controllable transition to reach $X$, and so that

no transitions that Adam could take while Eve is waiting may lead
outside of $X$.

````{prf:lemma} NEEDS TITLE 9-lem:pimonotonic
:label: 9-lem:pimonotonic

  The operator $\pi$ is 
  order-preserving: if $X\subseteq Y$, then
  $\pi(X) \subseteq \pi(Y)$.  

````

````{prf:example} Example for the controllable predecessor operator
:label: 9-ex:controllable_predecessor_operator

Consider the timed game to the left of
{numref}`9-fig:contpred`. In that game, Eve can reach her target when
clock $x_2$ reaches value $3$ while $x_1$ is in $[1;4]$. However,
Adam can take the game to a bad state when simultaneously
$x_1\in[1;2]$ and $x_2\leq 2$. The diagram to the right of
{numref}`9-fig:contpred` shows the set of winning valuations for Eve:
it is computed as $\mathsf{Pred}_{\geq 0}(X,Y)$ where $X= \mathsf{Pred}_c(\{W\}\times \mathbb{R}_{\geq 0})$
and $Y= \mathsf{Pred}_u(\{\ell_0,\ell_1\}\times \mathbb{R}_{\geq 0})$.

```{figure} ./../FigAndAlgos/9-fig:contpred.png
:name: 9-fig:contpred
:align: center
Controllable predecessors
```

````

````{prf:remark} Reduction for zero-sum objectives
:label: 9-rmk:reduction_zero_sum

When considering zero-sum objectives (which we do in this chapter),
a turn-based arena can be built to decide whether Eve has a winning
strategy (and possibly construct one).  Intuitively, the turn-based
arena is obtained by letting Eve first pick a pair $(d,e)$ with $e
\in  E_{ \textrm{Eve}}$, and then letting Adam either respect this choice (i.e.,
play a larger delay) or preempt Eve's action by choosing $(d',e')$
with $d' \leq d$ and $e' \in  E_{ \textrm{Adam}}$.
Eve has a winning strategy in this turn-based arena if, and only if she has one in the original game.
However, this does not apply to Adam; if he has a winning strategy, this only means that Eve
does not have a winning strategy in the original game.

Given $\mathcal{T} = ( \mathcal{L},  \mathcal{C}, E_{ \textrm{Eve}}, E_{ \textrm{Adam}}, c)$, we define the arena $\mathcal{A}
= ( V, V_\mathrm{Eve}, V_\mathrm{Adam},E, c'')$ 
with objective $\Omega$, where $V_\mathrm{Eve} =  \mathcal{L}\times  \mathbb{R}_{\geq 0}^ \mathcal{C}$ and
$V_\mathrm{Adam}= \mathcal{L}\times \mathbb{R}_{\geq 0}^ \mathcal{C}\times( \mathbb{R}_{\geq 0} \times  E_{ \textrm{Eve}}
\cup\{\bot\})$.  The set of successors of configuration $(\ell,\nu)
\in  V_\mathrm{Eve}$ is the set $\{(\ell,\nu,a)\mid a \text{ available at
}(\ell,\nu)\}$.

From a configuration $((\ell,\nu),(d,e))\in V_\mathrm{Adam}$, several cases may
occur:

*  if Adam has no available action from $(\ell,\nu)$, or if he can
  only play actions $(d',e')$ with $d'>d$, then the only transition
  from $((\ell,\nu),(d,e))$ goes to $\mathsf{step}((\ell,\nu),(d,e))$;
*  Otherwise, for all actions $(d',e')$ for Adam satisfying $d'\leq d$,
  there is a transition from $((\ell,\nu),(d,e))$
  to $\mathsf{step}((\ell,\nu),(d',e'))$.
  Moreover, if Adam has an available action $(d',e')$ with $d'\geq d$,
  then there is also a transition
  from $((\ell,\nu),(d,e))$ to $\mathsf{step}((\ell,\nu),(d,e))$.

From a configuration $((\ell,\nu),\bot)$, there is a transition
to $\mathsf{step}((\ell,\nu),(d',e'))$ for each available action $(d',e')$
of Adam.
The coloring function is defined as $c''((\ell,\nu)) = c(\ell)$
and $c''((\ell,\nu),(d,e)) = c(\ell)$.

````

