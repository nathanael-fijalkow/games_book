(8-sec:infinite_duration)=
# Infinite duration


```{math}
\newcommand{\rand}{{\tt rand}}
\newcommand{\Isafe}{{\tt ISafe}}
\newcommand{\LL}{\mathcal{L}}
\newcommand{\LLE}{\LL_{\text{Eve},=1}}
\newcommand{\LLA}{\LL_{\text{Adam},>0}}
\newcommand{\can}{\textsf{max}}
\newcommand{\targets}{TT}
\newcommand{\bh}{\setminus}
\newcommand{\signauxdeux}{T}
\newcommand{\actionsun}{A}
\newcommand{\Act}{\text{Act}}
\newcommand{\ini}{\delta_0}
\newcommand{\win}{{\tt Win}}
\newcommand{\winreach}{{\tt Reach}}
\newcommand{\winsafe}{{\tt Safety}}
\newcommand{\winbuchi}{{\tt Buchi}}
\newcommand{\wincobuchi}{{\tt CoBuchi}}
\newcommand{\states}{V}
\newcommand{\ar}{\arena}
\newcommand{\belun}{\mathcal{B}_{\text{Eve}}}
\newcommand{\beldeux}{\mathcal{B}_{\text{Adam}}}
\newcommand{\deuxbelun}{\mathcal{B}^{(2)}_{Eve}}
\newcommand{\tp}{\Delta}
\newcommand{\N}{\mathbb{N}}
\newcommand{\dist}{\mathcal{D}}
\newcommand{\supp}{\textrm{supp}}
\newcommand{\arena}{\mathcal{A}}
\newcommand{\play}{\pi}
\newcommand{\Reach}{\mathtt{Reach}}
\newcommand{\PTIME}{\textrm{PTIME}}
```

Games with infinite duration and imperfect information
are a natural model for applications such as synthesis 
of controllers of embedded systems.
This is illustrated by the example of the network controller.
Whereas in the previous section games of finite-duration
were equipped with real-valued payoffs, 
here we focus on B&uuml;chi conditions.


## Playing games with infinite duration and imperfect information

Notations used for games of finite duration are kept.
On top of that we need to define how probabilities are measured
and the winning conditions.

> **Measuring probabilities.**

The choice of an initial distribution
$\delta_0in\mathcal{D}V)$ 
and two strategies
$\sigma:  R_E \to \mathcal{D}A)$
and $\tau:  R_A \to \mathcal{D}A)$
for Eve and Adam
defines a Markov chain on the set of all finite plays.
This in turn defines a probability measure
$\mathbb{P}_{\delta_0^{\sigma,\tau}$ on the Borel-measurable
subsets of $\Delta^\omega$.
The random variables $V_n,A_n,B_n,S_{n}$ and $T_{n}$ denote
respectively the $n$-th state, action of Eve, action of Adam, 
signal received by Eve and Adam,
and we denote $\pi_n$ the finite play 
$\pi_n = V_0,A_0,B_0,S_0,T_0,V_1,\ldots,S_{n},T_{n},V_{n+1}$.

%

%*  
%*  
%*  
%
The probability measure $\mathbb{P}_{\delta_0^{\sigma,\tau}$ is the only
probability measure over $\Delta^\omega$ such that
for every $v\in V$, 
$\mathbb{P}^{\sigma,\tau}_{\delta_0(V_0 = v) = \delta_0v)$
and for every $n\in\mathbb{N},
\begin{multline*}

\mathbb{P}^{\sigma,\tau}_{\delta_0(V_{n+1}, S_{n}, T_{n} \mid \pi_n) \\
= \sigma(S_0\cdots S_{n-1})(A_{n}) \cdot \tau(T_0\cdots T_{n-1})(B_n) \cdot \Delta(V_n,A_n,B_n)(V_{n+1},S_{n},T_{n})\enspace,
\end{multline*}
where we use standard notations for conditional probability measures.

> **Winning conditions.**


The set of colours is $C=\{0,1\}$.
The reachability, safety, B&uuml;chi and coB&uuml;chi condition
 condition are defined as follows:
 \begin{align*}
 &{\tt Reach}\{\exists n\in\mathbb{N} C_n  = 1\}\\
&{\tt Safety}\{\forall n\in\mathbb{N} C_n = 0\}\\
&{\tt Buchi}\{\forall m \in \mathbb{N} \exists n \geq m, C_n=1\}\\
&{\tt CoBuchi}= \{\exists m \in \mathbb{N} \forall n \geq m, C_n = 0\}\enspace.
\end{align*}

When the winning condition is ${\tt Win},
Eve and Adam use strategies
$\sigma$ and $\tau$ and the initial distribution is $\delta_0,
then Eve wins the game with probability:

$$
\mathbb{P}^{\sigma,\tau}_{\delta_0({\tt Win}\enspace.
$$

Eve wants to maximise this probability, while Adam wants
to minimise it.  

%almost-surely winning strategy.



## The value problem.

The value problem is computationally intractable
for games with infinite duration and imperfect information.
This holds even for the very simple case
of blind one-player games with reachability conditions.
Those are games where the set of
signals is a singleton and actions of Adam have no influence
on the transition probabilities. These games can be seen
as probabilistic automata, hence the undecidability result of Paz applies.

````{prf:theorem} NEEDS TITLE AND LABEL {cite}`Paz`
Whether Eve has a strategy to win with probability $\geq \frac{1}{2}$
is undecidable, even in blind one-player games.
 
{cite}`Paz`
Whether Eve has a strategy to win with probability $\geq \frac{1}{2}$
is undecidable, even in blind one-player games.

````

Actually, the value might not even exist.

````{prf:proposition} NEEDS TITLE AND LABEL  {cite}`repgames`
There is a game with infinite duration imperfect information and B&uuml;chi condition
in which 

$$
\sup_\sigma \inf_\tau \mathbb{P}^{\sigma,\tau}_{\delta_0({\tt Buchi}
=
\frac{1}{2}
<
1
=
\inf_\tau \sup_\sigma  \mathbb{P}^{\sigma,\tau}_{\delta_0({\tt Buchi}\enspace.
$$

 
 {cite}`repgames`
There is a game with infinite duration imperfect information and B&uuml;chi condition
in which 

$$
\sup_\sigma \inf_\tau \mathbb{P}^{\sigma,\tau}_{\delta_0({\tt Buchi}
=
\frac{1}{2}
<
1
=
\inf_\tau \sup_\sigma  \mathbb{P}^{\sigma,\tau}_{\delta_0({\tt Buchi}\enspace.
$$


````

The value however exists for games with reachability condition {cite}`repgames`.

Although the value problem is not decidable,
there are
some other interesting  decision problems to consider.

## Winning with probability $1$ or $>0$


> **Winning almost-surely or positively.**

  A strategy $\sigma$ for Eve is **almost-surely winning**
  from an initial distribution $\delta_0 if
\begin{equation*}\label{eq:as}
  \forall \tau,
  \mathbb{P}^{\sigma,\tau}_{\delta_0({\tt Win}=1\enspace.
\end{equation*}
When such an almost-surely strategy $\sigma$ exists, the initial distribution $\delta_0
is said to be almost-surely winning (for Eve).

A less enjoyable situation for Eve is when she only has a
positively winning strategy.
  A strategy $\sigma$ for Eve is **positively winning** from
  an initial distribution $\delta_0 if
\begin{equation*}
  \forall \tau,
  \mathbb{P}^{\sigma,\tau}_{\delta_0({\tt Win}>0\enspace.
\end{equation*}
When such a strategy $\sigma$ exists, the initial distribution $\delta$
is said to be positively winning (for Eve).
Symmetrically, a
strategy $\tau$ for Adam is positively winning if it guarantees
$\forall \sigma, \mathbb{P}^{\sigma,\tau}_{\delta_0({\tt Win}<1$.

The worst situation for Eve is when her opponent has an
almost-surely winning strategy $\tau$, which thus ensures $\mathbb{P}^{\sigma,\tau}_{\delta_0({\tt Win}=0$
whatever strategy $\sigma$ is chosen by Eve. 

> **Qualitative determinacy.**



````{prf:theorem} Qualitative determinacy
:label: 8-thm:qualitative_determinacy

Stochastic games with signals and reachability, safety and B&uuml;chi
winning conditions are qualitatively determined:
either Eve wins almost-surely winning
or Adam wins positively.
Formally, in those games,

$$
\left(\forall \tau, \exists \sigma,\mathbb{P}^{\sigma,\tau}_{\delta_0({\tt Win}=1\right)
\implies
\left(\exists \sigma,\forall \tau ,\mathbb{P}^{\sigma,\tau}_{\delta_0({\tt Win}=1\right)\enspace.
$$


````

The proof of this result is given in the next section.

Since reachability and safety games are dual, a consequence of {prf:ref}`8-thm:qualitative_determinacy`, is that in a reachability game, every initial
distribution is either almost-surely winning for Eve,
almost-surely winning for Adam, or positively
winning for both players.
When a safety condition is satisfied almost-surely for a fixed profile of strategies,
it trivially implies that the safety condition is
satisfied by all consistent plays,
thus for safety games winning **surely** is the same than winning almost-surely.


By contrast, co-B&uuml;chi games are **not** qualitatively determined:

````{prf:lemma} NEEDS TITLE AND LABEL 
There is a co-B&uuml;chi game in which neither Eve has an almost-surely winning strategy
nor Adam has a positively winning strategy.
 

There is a co-B&uuml;chi game in which neither Eve has an almost-surely winning strategy
nor Adam has a positively winning strategy.

````

````{admonition} Proof
:class: dropdown tip

In this game, Eve observes
everything, Adam is blind (he only observes his own actions),
and Eve's objective is to visit only finitely many times the ${\large \frownie}$-state. The initial state is $\large{\frownie}$. The set of actions is $\{a,b,c,d\}$.
All transitions are deterministic.

\begin{figure}[h]
\begin{center}

\end{center}
\caption{Co-B&uuml;chi games are not qualitatively determined.}
\label{chap9fig4}
\end{figure} 

On one hand, no strategy $\Sigma$
is almost-surely winning for Eve
for her co-B&uuml;chi objective.
{
Since both players can observe their actions,
it is enough to prove that no behavioral
strategy
$\sigma\in C^*\to \Delta(I)$ of Eve is almost-surely winning.
Fix strategy $\sigma$ and assume towards contradiction that $\sigma$ is almost-surely winning. 
We define a strategy $\tau$
such that
$\probimp{\sigma,\tau}{\frownie}{ {\tt Buchi} > 0$.
Strategy $\tau$ starts by playing only $c$.
The probability to be in state $\frownie$ at step $n$ is
$x^{0}_n = \probimp{\sigma,c^\omega}{\frownie}{V_n=\frownie}$ and since $\sigma$ is almost-surely winning then $x^{0}_n \to_n 0$ thus there exists  $n_0$ such that 
$x^{0}_{n_0}\leq \frac{1}{2}$.
Then $\tau$ plays $d$ at step $n_0$.
Assuming the state was $2$ when $d$ was played, 
the probability to be in state $\frownie$ at step $n\geq n_0$ is
$x^{1}_n = \probimp{\sigma,c^{n_0}dc^\omega}{\frownie}{V_{n}=\frownie\mid V_{n_0}=\frownie}$
and since $\sigma$ is almost-surely winning there exists $n_1$ such that
$x^{1}_{n_1}\leq  \frac{1}{4}$.
Then $\tau$ plays $d$ at step $n_1$.
By induction we keep defining $\tau$ this way so that
$\tau=c^{n_0-1}d c^{n_1 - n_0 - 1}dc^{n_2 - n_1 - 1}d \cdots $.
and for every $k\in \mathbb{N},
$\probimp{\sigma,\tau}{\frownie}{
V_{n_{k+1}}=\frownie
\text{ and }
V_{n_{k+1}-1}=2
\mid 
V_{n_{k}}=\frownie
} \geq 1 - \frac{1}{2^{k+1}}$.
Thus finally
$\probimp{\sigma,\tau}{\frownie}{{\tt Buchi} \geq
\Pi_{k} (1 - \frac{1}{2^{k+1}})>0$ which contradicts the hypothesis.

}

On the other hand, Adam does not have a positively winning
strategy either.
{
Intuitively, Adam cannot win positively because as time passes, either the play reaches state $1$ or the chances that Adam plays action $d$ drop to $0$. When these chances are small, 
Eve can play action $c$ and she bets no more $d$ will be played and the play will stay safe in state $2$. If Eve loses her bet
then again she waits until the chances to see another $d$ are small and then plays action $c$. Eve may lose a couple of bets but almost-surely she eventually is right and the ${\tt CoBuchi} condition is almost-surely fulfilled.

%since both players can observe their actions,

%strategy

%The strategy $\tau$ being fixed,

%Eve such that 

%The only state where Eve's action matters

%After a play $p=V_0i_0j_0\cdots V_n$ ending up in state $\frownie$

%

$$

%\geq \frac{1}{2}\enspace,

%is satisfied in this case action $b$ is played.

%According to L\'evy law, 

%converges $\mathbb{P}^{\sigma,\tau}_{\frownie}$-almost-surely to the indicator function $1_{E_0}$ of the event $E_0$. 

%If $E_0$ does not hold then $\probimp{\sigma,\tau}{\frownie}{ E_0\mid P_{ n}}$ converges to $0$ thus eventually the trigger condition is not satisfied anymore hence Eve eventually plays no more $b$'s, only  $a$'s. But $E_0$ 

%thus the play reaches state $1$.

Finally neither Eve wins almost-surely nor Adam wins positively.
}

````


> **Decidability**



````{prf:theorem} NEEDS TITLE th:main
:label: th:main

Deciding whether the initial distribution of a B&uuml;chi games,
is almost-surely winning for Eve is
2\EXPTIME-complete.
For safety games, the same problem is \EXPTIME-complete.

````

Concerning winning positively a {\em safety or co-B&uuml;chi game}, one
can use {prf:ref}`8-thm:qualitative_determinacy` and the determinacy property: Adam
has a positively winning strategy in the above game if and only if
Eve has no almost-surely winning strategy. Therefore, deciding
when Adam has a positively winning strategy can also be done, with
the same complexity.


````{prf:theorem} NEEDS TITLE th:main2
:label: th:main2

For reachability and B&uuml;chi games where either Eve is perfectly informed about the state
or Adam is
better informed than Eve, deciding whether the initial distribution is
almost-surely winning for Eve is
\EXPTIME-complete.
In safety games
Eve is perfectly
informed {about the state}, the decision problem is in \textrm{PTIME}

````


%stochastic B&uuml;chi games with signals do not have a

%everything, Adam is blind (he only observes his own actions),

%

%\begin{center}

%\begin{gpicture}(30,13)(0,5)

%\gasset{Nframe=y,Nfill=n,Nw=3,Nh=3,ExtNL=n,Nmr=2}

%\node(L)(0,10){$1$}

%\node[Nframe=n,Nw=3,Nh=3](1)(15,10){$\Huge{\frownie}$}

%\drawedge[curvedepth=2](2,1){$* d$}

%\drawedge(1,L){$* d$}

%\drawloop[loopdiam=3](2){$* c$}

%\end{gpicture}

%\caption{Co-B&uuml;chi games are not qualitatively determined.}

%\end{figure} 

%

%is almost-surely winning for Eve

%{

%since both players can observe their actions,

%strategy

%Fix strategy $\sigma$ and assume towards contradiction that $\sigma$ is almost-surely winning. 

%such that

%Strategy $\tau$ starts by playing only $c$.

%$x^{0}_n = \probimp{\sigma,c^\omega}{\frownie}{V_n=\frownie}$ and since $\sigma$ is almost-surely winning then $x^{0}_n \to_n 0$ thus there exists  $n_0$ such that 

%Then $\tau$ plays $d$ at step $n_0$.

%the probability to be in state $\frownie$ at step $n\geq n_0$ is

%and since $\sigma$ is almost-surely winning there exists $n_1$ such that

%Then $\tau$ plays $d$ at step $n_1$.

%$\tau=c^{n_0-1}d c^{n_1 - n_0 - 1}dc^{n_2 - n_1 - 1}d \cdots $.

%$\probimp{\sigma,\tau}{\frownie}{

%\text{ and }

%\mid 

%} \geq 1 - \frac{1}{2^{k+1}}$.

%$\probimp{\sigma,\tau}{\frownie}{{\tt Buchi} \geq

%

%

%strategy either.

%Intuitively, Adam cannot win positively because as time passes, either the play reaches state $1$ or the chances that Adam plays action $d$ drop to $0$. When these chances are small, 

%then again she waits until the chances to see another $d$ are small and then plays action $c$. Eve may lose a couple of bets but almost-surely she eventually is right and the ${\tt CoBuchi} condition is fulfilled.

%since both players can observe their actions,

%strategy

%The strategy $\tau$ being fixed,

%Eve such that 

%The only state where Eve's action matters

%After a play $p=V_0i_0j_0\cdots V_n$ ending up in state $\frownie$

%\[

%\geq \frac{1}{2}\enspace,

%is satisfied in this case action $b$ is played.

%According to L\'evy law, 

%converges $\mathbb{P}^{\sigma,\tau}_{\frownie}$-almost-surely to the indicator function $1_{E_0}$ of the event $E_0$. 

%If $E_0$ does not hold then $\probimp{\sigma,\tau}{\frownie}{ E_0\mid P_{ n}}$ converges to $0$ thus eventually the trigger condition is not satisfied anymore hence Eve eventually plays no more $b$'s, only  $a$'s. But $E_0$ 

%thus the play reaches state $1$.

%


## Qualitative determinacy: proof of {prf:ref}`8-thm:qualitative_determinacy`

> **Beliefs.**

The
**belief** of a player
is the set of possible states of the game, according
to the signals received by the player. 

````{prf:definition} NEEDS LABEL Belief

{Let $\mathcal{A} be an arena with observable actions.}
  From an initial set of states $L\subseteqV, the belief of
  Eve after having received signal $s$ is:
  \begin{multline*}
\mathcal{B}_{\text{Eve}}L,s) =
 \{ v\inV\mid \exists l\in L, t\in S \text{ such that } \Deltal,s,t)(v,\text{Act}s),\text{Act}t))>0\}\enspace.  
  \end{multline*}

Remark that in this definition we use the fact that actions of Eve are observable,
thus when he receives a signal $s\in C$ Eve can deduce he played action
$\action_1(c)\in I$.
The belief of Eve after having received a sequence of signals $s_1,\ldots,s_n$ is defined inductively by:
\[
\mathcal{B}_{\text{Eve}}L,s_1,s_2,\ldots,s_n)
 = \mathcal{B}_{\text{Eve}}\mathcal{B}_{\text{Eve}}L,s_1,\ldots,s_{n-1}),s_n).\enspace
$$

Beliefs of Adam are defined similarly.
{
Given an initial distribution $\delta$,
we denote
$\mathcal{B}_{\text{Eve}}n$ the random variable defined by}
\begin{align*}
&{\mathcal{B}_{\text{Eve}}{0} = \textrm{supp}\delta)}\\
&{\mathcal{B}_{\text{Eve}}{n+1} =\mathcal{B}_{\text{Eve}}\textrm{supp}\delta),C_1,\ldots,C_{n+1})
= \mathcal{B}_{\text{Eve}}\mathcal{B}_{\text{Eve}}n,C_{n+1})
\enspace.}
\end{align*}

````



We will also rely on the notion of **belief of belief**, called
here **2-belief**, which, roughly speaking, represents for one
player the set of possible beliefs for his (or her) adversary,
as well as the possible current state.

````{prf:definition} NEEDS LABEL 2-Belief

{Let $\mathcal{A}be an arena with observable actions.}
  From an initial set ${\mathcal{L}} \subseteq V  \times \parties{V$ of pairs composed of a state and a belief
  for Adam, the 2-belief of Eve after having received signal $c$ is the subset of 
$V  \times \parties{V$ defined by:


$$
  \mathcal{B}^{(2)}_{Eve}{\mathcal{L}},s) = \{ (v,\mathcal{B}_{\text{Adam}}L,t)) \mid
\exists  (\ell,L) \in {\mathcal{L}},  t\in S,
  \Deltav,s,t)(\ell,\text{Act}s),\text{Act}t))
  >0\} \enspace.
  $$



From an initial set ${\mathcal{L}} \subseteq V\times \parties{V$ of pairs composed of a state and a belief
for Adam, the 2-belief of Eve after having  received a sequence of
signals $s_1,\ldots,s_n$ is defined inductively by:

$$
\mathcal{B}^{(2)}_{Eve}{\mathcal{L}},s_1,s_2,\ldots,s_n) =
\mathcal{B}^{(2)}_{Eve}left(\mathcal{B}^{(2)}_{Eve}left({\mathcal{L}},s_1,\ldots,s_{n-1}\right),s_n\right)\enspace.
$$


````

There are natural definitions of $3$-beliefs (beliefs on beliefs on beliefs)
and even $k$-beliefs however for our purpose, $2$-beliefs are enough,
in the following sense:
in B&uuml;chi games the positively winning sets of Adam
can be characterised by fix-point equations on sets of $2$-beliefs,
and some positively winning strategies of Adam with finite-memory
can be implemented using $2$-beliefs.

> **Supports positively winning supports.**


Note that whether an initial distribution $\delta_0 is almost-surely or
positively winning depends only on its support, because
$\mathbb{P}^{\sigma,\tau}_{\delta_0({\tt Win}
=\sum_{v\in V}\delta_0v)\cdot\mathbb{P}^{\sigma,\tau}_{\delta_0({\tt Win}\mid V_0= v)$.
As a consequence, we will say that a support
$L\subseteq V$ is almost-surely or positively winning for a
player if there exists a distribution with support $L$ which has the
same property.

In the sequel, we will denote $\LL_{\text{Eve},=1} the set of supports almost-surely winning for Eve
and  $\LL_{\text{Adam},>0} those positively winning for Adam.

Then the qualitative determinacy theorem is a corollary of the following lemma.

````{prf:lemma} NEEDS TITLE AND LABEL 
In every B&uuml;chi game, every non-empty support
which does not belong to $\LL_{\text{Adam},>0} belongs to $\LL_{\text{Eve},=1}.
 

In every B&uuml;chi game, every non-empty support
which does not belong to $\LL_{\text{Adam},>0} belongs to $\LL_{\text{Eve},=1}.

````

The proof of this lemma relies on the definition of a strategy
called the maximal strategy.
We prove that this strategy is almost-surely winning from any initial
distribution which is not positively winning for Adam. 

````{prf:definition} Maximal strategy
:label: 8-def:maximalstrategy

For every non-empty support $L\subseteq V$ we define
 the set  of {$L$-safe} actions for Eve as

$$
{\tt ISafe}L) = \left\{ a \in A \mid  \forall s \in S, (\text{Act}s)=a) \implies (\mathcal{B}_{\text{Eve}}L,s)\not\in\LL_{\text{Adam},>0}  )\right\}\enspace,
$$

in other words these are the actions which Eve can play without taking the risk
that her belief is positively winning for Adam.

The **maximal strategy** is the strategy of Eve
which plays the uniform distribution
on ${\tt ISafe}\mathcal{B}_{\text{Eve}}$
when it is not empty and plays the uniform distribution on $A$ otherwise.
It is denoted $\sigma_{\textsf{max}$.

````

To play her maximal strategy at step $n$,
Eve only needs to keep track of her belief $\mathcal{B}_{\text{Eve}}n$,
thus $\sigma_{\textsf{max}$ can be implemented by Eve 
using a finite-memory device which keeps track of the current belief.
Such a strategy is said to be **belief-based**.
We will use several times  the following technical lemma about belief-based strategies.

````{prf:lemma} NEEDS TITLE lem:borelcantelli
:label: lem:borelcantelli

{Fix a B&uuml;chi game.}
Let $\mathcal{L}\subseteq \parties{V}$ 
and $\sigma$ a strategy for player $1$.
Assume that
$\sigma$ is a belief
strategy,
$\mathcal{L} is downward-closed
(i.e. $L\in\mathcal{L}\land L' \subseteq L \implies L'\in \mathcal{L})
and for every $L\in\mathcal{L}setminus \{\emptyset\}$ and every strategy $\tau$,
\begin{align}
\label{eq:pos}
& \probimp{\sigma,\tau}{\delta_L}{\mathtt{Reach} > 0\enspace,\\
 \label{eq:belstab}
&\probimp{\sigma,\tau}{\delta_L}{\forall n\in\mathbb{N}\mathcal{B}_{\text{Eve}}n\in \mathcal{L} = 1\enspace.
\end{align}
Then $\sigma$ is almost-surely winning for the B&uuml;chi game from any support 
$L\in \mathcal{L}setminus \{\emptyset\}$. 

````

````{admonition} Proof
:class: dropdown tip

{
Since $\mathcal{L} is downward-closed then $\forall L\in \mathcal{L}\forall l\in L, \{l\}\in\mathcal{L}
thus~\eqref{eq:pos} implies 
\be
\forall L\in \mathcal{L}\forall l\in L,
 \probimp{\sigma,\tau}{\delta_L}{\mathtt{Reach}mid V_0=l} > 0\enspace.
 \label{eq:pos2}
\end{equation}
}
{
Once $\sigma$ is fixed then the game is a one-player game with state space $V\times 2^V$ and imperfect information and~\eqref{eq:pos2} implies that in this one-player game,
\be
\label{eq:sigmamproperty}
\forall L\in \mathcal{L}\forall l\in L, \forall \tau,
 \probimp{\tau}{\delta_L}{\mathtt{Reach}\mid V_0=l} > \varepsilon\enspace,
 \ee
where $N=|K|\cdot 2^{|K|}$
and $\varepsilon = p_{\min}^{|K|\cdot 2^{|K|}}$
and $p_{\min}$ is the minimal non-zero transition probability.
Moreover~\eqref{eq:belstab} implies that
in this one-player game the second component of the state space is always in $\mathcal{L}, whatever strategy $\tau$ is played by player $2$.
Remind the definition
 \begin{align*}
 {\tt Reach}\{\exists n\in\mathbb{N} C_n  = 1\}\enspace.
\end{align*}
As a consequence, in this one-player game
for every $m\in\mathbb{N},
and every behavioral strategy $\tau$ and every 
%and $d_1\cdots d_m\in D^*$ and 
$l\in V$,
\be
\label{eq:sigmamproperty2}
\probimp{\tau}{\delta_L}
{ \exists m \leq n \leq m+ N, C_n = 1 \mid
K_m = l
}
\geq \varepsilon,
\ee
whenever $\probimp{\tau}{\delta_L}{V_m=l} > 0$.
}
We use the Borel-Cantelli Lemma to conclude the proof.
According to~\eqref{eq:sigmamproperty2},
for every $\tau$, $L\in\overline{\mathcal{L}$, 
$m\in \mathbb{N},
\be
\probimp{\tau}{\delta_L}
{ \exists n, mN \leq n < (m+ 1)N, C_n=1
\mid V_{mN}
}
\geq \varepsilon,
\ee
which implies for every behavioral strategy $\tau$ and $k,m\in\mathbb{N},

$$
\probimp{\tau}{\delta_L}
{\forall n,  \left((m\cdot N) \leq n < ((m+k) \cdot N) \implies  C_n \neq 1 \right)}\leq  \left(1 - \varepsilon\right)^k\enspace.
$$

Since $\sum_k \left(1 - \varepsilon\right)^k$ is finite,
we can apply Borel-Cantelli Lemma for the events 
$(\{\forall n, m\cdot N \leq n < (m+k) \cdot N \implies  C_n\neq 1\})_k$
and we get
$\nonumber
\probimp{\tau}{\delta_L}{\forall n, m\cdot N \leq n  \implies  C_n\neq 1}=0
$
thus
\be\label{eq:assss}\nonumber
\probimp{\tau}{\delta_L}{{\tt Buchi}=1\enspace.
\ee

As a consequence $\sigma$ is almost-surely winning for the 
B&uuml;chi game.

````


An important feature of the maximal strategy is the following.

````{prf:lemma} NEEDS TITLE AND LABEL 
In a B&uuml;chi game
with observable actions,
let $\delta\in\Delta(K)$ be an initial distribution which is not positively 
winning for Adam,
i.e. $\textrm{supp}\delta)\not\in\LL_{\text{Adam},>0}.
Then for every strategy $\tau$ of Adam
\begin{equation}
\label{eq:LLstable}
\mathbb{P}^{\sigma_\textsf{max}\tau}_{\delta}(\forall n \in \mathbb{N} \mathcal{B}_{\text{Eve}}n \not\in\LL_{\text{Adam},>0})=1\enspace.
\end{equation}
 

In a B&uuml;chi game
with observable actions,
let $\delta\in\Delta(K)$ be an initial distribution which is not positively 
winning for Adam,
i.e. $\textrm{supp}\delta)\not\in\LL_{\text{Adam},>0}.
Then for every strategy $\tau$ of Adam
\begin{equation}
\label{eq:LLstable}
\mathbb{P}^{\sigma_\textsf{max}\tau}_{\delta}(\forall n \in \mathbb{N} \mathcal{B}_{\text{Eve}}n \not\in\LL_{\text{Adam},>0})=1\enspace.
\end{equation}

````

````{admonition} Proof
:class: dropdown tip

We only provide a sketch of proof.
The proof is an induction based on the fact that for every non-empty subset $L\subseteq V$,

$$
(L\not \in \LL_{\text{Adam},>0} \implies ({\tt ISafe}L)\neq \emptyset)\enspace.
$$

Assume a contrario that ${\tt ISafe}L) = \emptyset$ for some $L\not \in \LL_{\text{Adam},>0}.
Then for every action $a\in A$ there exists a signal $s_a\in S$
such that $\mathcal{B}_{\text{Eve}}L,s_a)\neq \emptyset$ and $\mathcal{B}_{\text{Eve}}L,s_a) \in \LL_{\text{Adam},>0}.
Since $\mathcal{B}_{\text{Eve}}L,s_a)\neq \emptyset$, the definition of the belief operator implies:

$$
\exists v_a\in L, w_a\in V,  t_a \in T, \text{ such that }  \Deltaw_a,s_a,t_a)(v_a,\text{Act}s),\text{Act}t_a)) > 0\enspace.
$$


But then Adam can win positively from $L$ with the following strategy.
At the first round, Adam plays randomly any action in $A$.
At the next round, Adam picks up randomly a belief in  $\LL_{\text{Adam},>0} and 
plays forever the corresponding positively winning strategy.
Remark that this strategy of Adam is not described as a behavioural strategy
but rather as a finite-memory strategy. Since actions are observable,
such a finite-memory strategy can be turned into a behavioural one,
see~\cite[Lemma 4.6 and 4.7]{BGGjacm}.

Why is Adam strategy positively winning from $L$?
Whatever action $a\in A$ is played by Eve,
with positive probability she will receive signal $s_a$,
because Adam might play the action $\text{Act}t_a)$.
Since $\mathcal{B}_{\text{Eve}}L,s_a) \in \LL_{\text{Adam},>0} then there Adam might with positive probability
play a strategy positively winning when the initial belief
of Eve is $\mathcal{B}_{\text{Eve}}L,s_a)$. Thus whatever action Eve chooses,
she might lose with positive probability.

````

\medskip 

The notion of maximal strategy being defined,
we can complete the proof of {prf:ref}`8-thm:qualitative_determinacy`.
For that, we show that
$\sigma_{\textsf{max}$
is almost-surely
winning from every support not in $\LL_{\text{Adam},>0}.


Reachability and safety conditions can be easily encoded as B&uuml;chi conditions,
thus it is enough to consider  B&uuml;chi games.


The first step is to prove that for every $L\in\LL_{\text{Eve},=1},
for every strategy $\tau$ of Adam,
\be\label{eq:LLpasM}

\probimp{\sigma_{\textsf{max},\tau}{\delta_L}{{\tt Safety} < 1 \enspace.
\ee
We prove~\eqref{eq:LLpasM} by contradiction.
Assume~\eqref{eq:LLpasM} does not hold for some $L\in \LL_{\text{Eve},=1}

and strategy $\tau$:
\be\label{eq:winsafe}
\probimp{\sigma_{\textsf{max},\tau}{\delta_L}{{\tt Safety}} = 1\enspace.
\ee
Under this assumption we use $\tau$ to build a strategy positively winning from $L$,
which will contradict the hypothesis 
$L\in\LL_{\text{Adam},>0}.
Although $\tau$ is surely winning from $L$ against the particular strategy $\sigma_{\textsf{max}$,
there is no reason for $\tau$ to be positively winning from $L$
against all other strategies of player $1$.
{
However we can rely on $\tau$
in order to define another strategy 
$\tau'$ for Adam positively winning from $L$.
The strategy $\tau'$ is a strategy
which gives positive probability to play $\tau$
all along the play,
as well as any strategy in the family
of strategies
$(\tau_{n,B})_{n\in\mathbb{N}B\in \LL_{\text{Adam},>0}$ defined as follows.
For every $B\in\LL_{\text{Adam},>0} we choose a strategy $\tau_B$ positively winning from $B$.
Then
$\tau_{n,B}$ is the strategy which plays 
the uniform distribution on $A$ for the first $n$ steps then forgets past signals and switches definitively to $\tau_B$. 

A possible way to implement the  strategy $\tau'$
is as follows.
At the beginning of the play
player $2$ tosses a fair coin. If the result is head then he plays $\tau$. Otherwise he keeps 
tossing coins and as long as the coin toss is head, player $2$ plays randomly an action in $J$ .
The day the coin toss is tail, he picks up randomly some $B\in\LL_{\text{Adam},>0} and starts playing $\tau_B$.
}
Remark that this strategy of Adam is not described as a behavioural strategy
but, since actions are observable,
such a finite-memory strategy can be turned into a behavioural one,
see~\cite[Lemma 4.6 and 4.7]{BGGjacm}.

%the strategy

%beginning of the play and:

%  \item plays like $\tau$ forever if the result of this initial coin toss is head,

%$\tau'$ plays the uniform distribution over $J$. If the result of one of the coin tosses is head,

%and a strategy $\tau_B$ positively winning from $B$, 


Now that $\tau'$ is defined, we prove it is positively winning from $L$.
Let $E$ be the event 
{player $1$ plays only actions that are safe with respect to her belief, i.e.}

$$
E = \{ \forall n\in \mathbb{N} A_n \in \Isafe_\mathcal{L}\mathcal{B}_{\text{Eve}}n)\}\enspace.
$$

Then for every behavioral strategy $\sigma$:

  * [\textbullet]
Either $\probimp{\sigma,\tau'}{\delta_L}{E}=1$. In this case 

$$
\probimp{\sigma,\tau'}{\delta_L}{{\tt Safety}> 0\enspace,
$$

because for every {finite play $\piv_0a_0b_0s_1t_1v_1\cdots v_n$,}

$$
\left(\probimp{\sigma,\tau'}{\delta_L}{\pi > 0\right)
\implies
\left(\probimp{\sigma_{\textsf{max},\tau'}{\delta_L}{\pi > 0\right)
\implies
{\tt Safety}enspace,
$$

where the first implication holds because, by definition of $\sigma_{\textsf{max}$ and $E$,
for every $s_1\cdots s_n\in CS^*, \textrm{supp}\sigma(s_1\cdots s_n))\subseteq \textrm{supp}\sigma_{\textsf{max}(s_1\cdots s_n))$

while the second implication is from~\eqref{eq:winsafe}.
Thus $\probimp{\sigma,\tau}{\delta_L}{{\tt Safety}= 1$ and we get
$\probimp{\sigma,\tau'}{\delta_L}{{\tt Safety} > 0$ by definition of
$\tau'$.
* [\textbullet]
Or $\probimp{\sigma,\tau'}{\delta_L}{E}<1$.
Then by definition of $E$ there exists $n\in\mathbb{N}

such that 

$$
\probimp{\sigma,\tau'}{\delta_L}{A_n  \not\in
\Isafe_\mathcal{L}\mathcal{B}_{\text{Eve}}n)}>0\enspace.
$$

{
By definition of $\Isafe_\mathcal{L} it implies
$\probimp{\sigma,\tau'}{\delta_L}{\mathcal{B}_{\text{Eve}}{n+1}  \in \mathcal{L}>0$,
thus there exists $B\in \mathcal{L} such that
$\probimp{\sigma,\tau'}{\delta_L}{\mathcal{B}_{\text{Eve}}{n+1} =B}>0$.
By definition of $\tau'$ we get
$\probimp{\sigma,\tau_{n+1,B}}{\delta_L}{\mathcal{B}_{\text{Eve}}{n+1} =B}>0$,
because whatever finite play $v_0,\ldots, v_{n+1}$ leads with positive probability to
the event $\{\mathcal{B}_{\text{Eve}}{n+1} =B\}$,
the same finite play can occur with 
$\tau_{n+1,B}$ since $\tau_{n+1,B}$ plays every possible action for the $n+1$ first steps.
Since $\tau_{n+1,B}$ coincides with $\tau_{\tt rand} for the first $n+1$ steps then
by definition of beliefs,
$\probimp{\sigma,\tau_{n+1,B}}{\delta_L}{\mathcal{B}_{\text{Eve}}{n+1} =B}>0$
and $B\subseteq \{ k\in K\mid \probimp{\sigma,\tau_{n+1,B}}{\delta_L}{K_{n+1}=k\mid \mathcal{B}_{\text{Eve}}{n+1} =B}>0\}$.

%$\probimp{\sigma,\tau_{n+1,B}}{\delta_L}{\mathcal{B}_{\text{Eve}}{n+1} =B\mid K_0 = k_0}>0$

Using the definition of $\tau_B$ we get 
$\probimp{\sigma,\tau_{n+1,B}}{\delta_L}{{\tt CoBuchi}>0$.
}
As a consequence by definition of $\tau'$
we get  $ \probimp{\sigma,\tau'}{\delta_L}{{\tt CoBuchi}
>0 $.
  
In both cases, for every $\sigma$,
$\probimp{\sigma,\tau'}{\delta_L}{{\tt CoBuchi}} >0 $
thus $\tau'$ is positively winning from $L$.
This contradicts the
hypothesis $L\in \LL_{\text{Eve},=1}. As a consequence we get~\eqref{eq:LLpasM} by contradiction.

\medskip

Using~\eqref{eq:LLpasM}, we apply {prf:ref}`8-lem:borelcantelli` to the collection 
$\overline{\LL_{\text{Adam},>0}$ and the strategy $\sigma_{\textsf{max}$.
The collection $\overline{\LL_{\text{Adam},>0}$ is downward-closed because $\LL_{\text{Adam},>0} is upward-closed: if a support is positively winning for Adam then any greater support is positively winning as well, using the same positively winning strategy.

Thus $\sigma_{\textsf{max}$ is almost-surely winning for the B&uuml;chi game from every support in $\overline{\LL_{\text{Adam},>0}$ i.e. every support which is not positively winning for Adam, hence the game is qualitatively determined.

(8-subsec:proof)=
## Decidability: proof of {prf:ref}`8-thm:main` and {prf:ref}`8-thm:main2`

### A na\"ive algorithm

As a corollary of the proof of qualitative determinacy
( {prf:ref}`8-thm:qualitative_determinacy`), we get a maximal strategy $\sigma_\textsf{max}
for player $1$ (see {prf:ref}`8-def:maximalstrategy`) to win
almost-surely B&uuml;chi games.

````{prf:corollary} NEEDS TITLE 8-cor:asmem
:label: 8-cor:asmem

  If player $1$ has an almost-surely winning strategy in a B&uuml;chi
  game {with observable actions} then the maximal strategy $\sigma_{\textsf{max}$ is almost-surely
  winning.

````

A simple algorithm to decide for which player a game is winning can be derived from~\cref{8-cor:asmem}: this simple algorithm enumerates all possible belief strategies

and test each one of them to see if it is almost-surely winning. The test reduces to checking positive winning in one-player co-B&uuml;chi games and can be done in exponential time.

As there is a doubly exponential number of {belief} strategies, this can be done in time doubly exponential. 
This algorithm also appears in {cite}`GS-icalp09`.
This settles the upper bound for {prf:ref}`8-thm:main`. 

The lower bounds are established in {prf:ref}`8-thm:hard`, proving that this enumeration algorithm is
  optimal for worst case complexity.  While optimal in the worst case,
  this algorithm is {likely to be unefficient in practice}.  For instance, if player
  $1$ has no almost-surely winning strategy, then this algorithm will
  enumerate every single of the doubly exponential many {possible belief}
  strategies.  Instead, we provide fix-point algorithms which do not
  enumerate every possible strategy in {prf:ref}`8-thm:qdec1` for
  reachability games and {prf:ref}`8-thm:qdec2` for B&uuml;chi games.
  Although they should perform better on games with particular
  structures, these fix-point algorithms still have a worst-case
  2-\EXPTIME\ complexity.


### A fix-point algorithm for reachability games

We turn now to the {\color{black} (fix-points)} algorithms which compute the set of supports that
are almost-surely or positively winning for various objectives.

% \setcounter{theo:qdec1}{\value{theorem}}

````{prf:theorem} Deciding positive winning in reachability games
:label: theo:qdec1
 
In a reachability game each initial distribution $\delta$ is either positively winning for player $1$ or surely winning for player $2$, and this depends only on $\textrm{supp}\delta)\subseteq V.

%of $\parties{V$.

%has a strategy with finite memory $\parties{V$.
  The corresponding partition of $\parties{V$ is computable in
  time $\mathcal{O}\left(|G| \cdot 2^{|V}\right)$, where $|G| $ denotes
  the size of the description of the game,
  as the largest fix-point of a monotonic operator
$\Phi:\parties{\parties{V}}\to \parties{\parties{V}}$
computable in time linear in $|G| $.
  
  
  

````

We denote $TT the set of vertices whose colour is $1$.

````{admonition} Proof
:class: dropdown tip


Let $\LL_\infty\subseteq \parties{VbhTT$
be the greatest fix-point of the monotonic operator
$\Phi:\parties{\parties{VbhTT}\to \parties{\parties{VbhTT}$ defined by:
\be
\label{eq:defphi}
\Phi(\mathcal{L}=\{L\in \mathcal{L}\mid
\exists j_L\in J, \forall d\inT (\action_2(d)=j_L)\implies (\mathcal{B}_{\text{Adam}}L,d)\in \mathcal{L}\cup \{\emptyset)\}\}\enspace,
\ee
in other words $\Phi(\mathcal{L}$ is the set of supports
such that player $2$ has an action which
ensure his next belief will be in $\mathcal{L},
whatever signal $d$ he might receive.

Let $\sigma_{{\tt rand}$ be the strategy for player $1$ that plays randomly any action.

We are going to prove that:

1.  every support in $\LL_\infty$ is surely winning for player $2$,

2.  and $\sigma_{{\tt rand}$ is positively winning from any support $L\subseteqV which is not in $\LL_\infty$.

We start with proving the first item.
To win surely from any support $L\in\LL_\infty$, player $2$ uses the following
belief strategy $\tau_B$: when the current belief of player $2$ is $L\in\LL_\infty$ then player $2$
plays an action $j_L$ defined as in~\eqref{eq:defphi}.
By definition of $\Phi$ and since $\LL_\infty$ is a fix-point of $\Phi$,
there always exists such an action.

%and update operator $\mathcal{B}_{\text{Adam}}.
When playing with the belief strategy $\tau_B$,
starting from a support in $\LL_\infty$,
the beliefs of player $2$ stay in $\LL_\infty$
and never intersect $TT because $\LL_\infty\subseteq \parties{VbhTT$.
{According to property~\eqref{eq:beln_lemma} of beliefs ( {prf:ref}`8-lem:beliefs`)},
this guarantees the play never visits $TT,
whatever strategy is used by player $1$.

We now prove the second item.

%that plays randomly any action.
Let
$\LL_0=\parties{VbhTT\supseteq
\LL_1=\Phi(\LL_0)\supseteq \LL_2=\Phi(\LL_1)\ldots$ and $\LL_\infty$
be the limit of this sequence, the greatest fix-point of $\Phi$.
  We
prove that for any support $L\in\parties{V$, if
$L\not\in\LL_\infty$ then: \be\label{eq:postoprove} \text{$\sigma_{{\tt rand}$ is
  positively winning for player $1$ from $L$}\enspace.  \end{equation}If $L\capTT\not=\emptyset$,~\eqref{eq:postoprove} is obvious.  To deal with
the case where {$L\cap TT=\emptyset$}, we define for every
$n\in\mathbb{N}, $\KK_n = \parties{VbhTT \setminus\LL_n$, and we
prove by induction on $n\in\mathbb{N} that for every $L\in\KK_n$, for every
initial distribution $\delta_L$ with support $L$, for every {behavioral} strategy
$\tau$, \be\label{eq:topo} \probimp{\sigma_{{\tt rand},\tau}{\delta_L}{\exists m, 2\leq
  m\leq n+1, V_m\inTT}>0 \enspace.  \end{equation}For
$n=0$,~\eqref{eq:topo} is obvious because $\KK_0=\emptyset$.  Suppose
that for some $n\in\mathbb{N}, \eqref{eq:topo} holds for every $L'\in\KK_n$,
and let $L\in\KK_{n+1}\setminus\KK_n$.
Then by definition of $\KK_{n+1}$, \be\label{eq:LLLn}
L\in\LL_{n}\setminusPhi(\LL_n)\enspace.  \end{equation}Let $\delta_L$ be an initial
distribution with support $L$ and $\tau$ any behavioral strategy for player $2$.
Let $J_0\subseteq J$ be the support of $\tau(\delta_L)$ and $j_L\in J_0$.  According
to~\eqref{eq:LLLn}, by definition of $\Phi$, there exists a signal
$d\in D$ such that $\action_2(d)=j_L$ and
 $\mathcal{B}_{\text{Adam}}L,d)\not \in \LL_n$ and $\mathcal{B}_{\text{Adam}}L,d)\neq \emptyset$.
{According to  property~\eqref{eq:belief_compute} of beliefs ( {prf:ref}`8-lem:beliefs`),} 
 $\forall k \in \mathcal{B}_{\text{Adam}}L,d),\probimp{\sigma_{{\tt rand},\tau}{\delta_L}{V_2 =k\land D_1=d}  > 0$.
   If
$\mathcal{B}_{\text{Adam}}L,d)\capTT\not= \emptyset$ then according to
the definition of beliefs,
$\probimp{\sigma_{{\tt rand},\tau}{\delta_L}{V_2\inTT>0$.  Otherwise
$\mathcal{B}_{\text{Adam}}L,d)\in\parties{VbhTT\setminusLL_n=\KK_n$ hence
distribution $\delta_{d}:k\to \probimp{\sigma_{{\tt rand},\tau}{\delta_L}{V_2 =k\mid D_1=d}$
has its support in $\KK_n$. By inductive hypothesis, for every
behavioral strategy $\tau'$,

$$\probimp{\sigma_{{\tt rand},\tau'}{\delta_{d}}{\exists m\in\mathbb{N} 2\leq
  m\leq n+1, V_m\inTT>0$$

hence using the shifting lemma and the
definition of $\delta_{d}$,

$$
\probimp{\sigma_{{\tt rand},\tau}{\delta}{\exists m\in\mathbb{N}
  3\leq m\leq n+2, V_m\inTT>0\enspace,$$

which completes the proof of the inductive
step.
{
Hence~\eqref{eq:topo} holds for every behavioral strategy 
$\tau$. Thus, according to {prf:ref}`8-lem:actioneq3`,~\eqref{eq:topo}
holds as well for every general strategy $\tau$.
}

To compute

the partition of supports between those positively winning for player $1$
and those surely winning for player $2$,

it is enough to compute

the largest fix-point of $\Phi$.
Since $\Phi$ is monotonic, and each application of the operator
can be computed in time linear in the size of the game ($|G|$)
and the number of supports ($2^{|V}$)
the overall computation can be achieved in time $|G| \cdot 2^{|V}$.
To compute the strategy $\tau_B$, it is enough to compute
for each $L\in\LL_\infty$ one action $j_L$ such that
$(\action_2(d)=j_L)\implies (\mathcal{B}_{\text{Adam}}L,d)\in\LL_\infty)$.

````

As a byproduct of the proof one obtains the following bounds on time
and probabilities before reaching a target state, when player $1$ uses
the uniform memoryless strategy $\sigma_{{\tt rand}$.  From an initial
distribution positively winning for the reachability objective, for
every strategy $\tau$, \be\label{eq:bounds}
\probimp{\sigma_{{\tt rand},\tau}{\delta}{\exists n\leq 2^{\mid V    \mid}, C_n = 1}\geq \left(
  \frac{1}{p_{\min}\midAmid}\right)^{2^{\lvertVlvert}}\enspace,
\end{equation}
where $p_{\min}$ is the smallest non-zero transition probability.


### A fix-point algorithm for B&uuml;chi games

To decide whether player $1$ wins almost-surely a B&uuml;chi game,
we provide an algorithm which runs in doubly-exponential time.
It uses the algorithm for reachability games as a sub-procedure.


````{prf:theorem} NEEDS LABEL Deciding almost-sure winning in B&uuml;chi games

  \label{theo:qdec2} In a B&uuml;chi game each initial distribution
  $\delta$ is either almost-surely winning for player $1$ or
  positively winning for player $2$, and this depends only on
  $\textrm{supp}\delta)\subseteq V.

%of $\parties{V$.

%has a strategy with finite memory $\parties{V$.
The corresponding partition of $\parties{V$ is computable in
time $\mathcal{O}\left(2^{2^{|G|}}\right)$, where $|G|$ denotes the size of the description of the game,
as a projection of the greatest
fix-point $\LL_\infty$
of a monotonic operator

$$\Psi:
\parties{\parties{V\timesV
\to
\parties{\parties{V\timesV
\enspace.
$$

The operator $\Psi$ is computable using as a nested fix-point the operator $\Phi$ of {prf:ref}`8-thm:qdec1`.
 The almost-surely winning belief strategy of player $1$ and the positively winning $2$-belief strategy of player $2$  can be extracted 
from $\LL_\infty$.

````


%$\parties{\parties{V\timesV$ to remember the possible

% The finite memory $\parties{\parties{V\timesV$ of the

% remember what are the possible pairs of current state and pessimistic

\smallskip

%
````{admonition} Proof
:class: dropdown tip
[Sketch of proof]
We sketch the main ideas of the proof of {prf:ref}`8-thm:qdec2`.

%
````{prf:definition} NEEDS LABEL Uniform positive reachability

%$\tau$ of player $2$,

%\forall l\in L, \probimp{\sigma,\tau}{\delta_L}{\exists n,K_n\inTTmid K_0=l}>0\enspace.

%
````

%player $1$ should win positively the reachability game whatever initial state has been selected by the initial distribution.

First, suppose that from **every** initial support, player $1$ can
win positively the  reachability game.
{Then she can do so using a belief strategy and according to {prf:ref}`8-lem:borelcantelli`,}
this strategy guarantees
almost-surely the B&uuml;chi condition.

In general though player $1$ is not in such an easy situation and
there exists a support $L$ which is **not** positively winning
for her for the reachability objective.
Then by qualitative determinacy, player $2$ has a strategy to achieve surely her safety objective
from $L$, which is **a fortiori**
surely winning for her co-B&uuml;chi objective as well.

We prove that in case player $2$ can **force with positive
  probability the belief of player $1$** to be $L$ eventually from another
support $L'$, then player $2$
{ has a general strategy to win positively from $L'$}.
This is not completely obvious because in general player $2$ cannot
know exactly **when** the belief of player $1$ is $L$ (he can only
compute the 2-Belief, letting him know all the possible beliefs player
1 can have).  However player $2$ can make blind guesses,
and be right with $>0$ probability.
For winning positively from $L'$, player $2$ plays
totally randomly until he guesses randomly that the belief of player
$1$ is $L$, at that moment he switches to a strategy surely winning
from $L$.  Such a strategy is far from being optimal, because player
$2$ plays randomly and in most cases he makes a wrong guess about the
belief of player $1$.  However 
there is a non zero probability for his guess to be right.

%right moment the belief of player $1$.

Hence, player $1$ should surely avoid her belief to be $L$
or $L'$ if she wants to win almost-surely.
However, doing so player $1$ may prevent the play from
reaching target states, which may create another positively winning
support for player $2$, and so on. This is the basis of our fix-point algorithm.

Using these ideas, we prove that the set
$\LL_\infty\subseteq \parties{V$ of supports almost-surely
winning for player $1$ for the B&uuml;chi objective is the largest set of
initial supports from which:
\begin{multline}
\label{eq-dag}
\tag{$\dag$}
\textrm{player $1$ has a strategy
  which win positively the reachability game}\\
\textrm{and also ensures at the same time
  her belief to stay in } \LL_\infty .
\end{multline}

Property \eqref{eq-dag} can be reformulated as a reachability
condition in a new game whose states are states of the original game
augmented with beliefs of player $1$, kept hidden to player $2$.

The fix-point characterisation suggests the following algorithm for
computing the set of supports positively winning for player $2$:
$\parties{V\setminusLL_\infty$ is the limit of the sequence
$\emptyset=\LL_0'\subsetneq \LL_0'\cup \LL_1''\subsetneq\LL_0'\cup
\LL_1'\subsetneq \LL_0'\cup \LL_1'\cup \LL_2''\subsetneq\ldots
\subsetneq \LL_0'\cup \cdots \cup \mathcal{L}_m
=\parties{V\setminusLL_\infty$, where

*  from supports in $\mathcal{L}'_{i+1}$ player $2$ can surely guarantee the safety objective,
under the hypothesis that player $1$ 
{guarantees for sure} her beliefs to stay outside $\mathcal{L}_i$,
*  from supports in $\mathcal{L}_{i+1}$ player $2$ can ensure with positive probability the belief of player $1$ to be in $\mathcal{L}'_{i+1}$ eventually,
under the same hypothesis.

The overall strategy of player $2$ positively winning for the co-B&uuml;chi objective

consists in playing randomly for some time until he decides to pick
up randomly a belief $L$ of player $1$ in some $\mathcal{L}'_i$,
bets that the current belief of player $1$ is $L$ and that player $1$
guarantees for sure
her future beliefs 
will stay outside $\mathcal{L}_i$.
He forgets
the signals he has received up to that moment and switches
definitively to a strategy which guarantees the first item.  With positive
probability, player $2$ 
guesses correctly the belief of player $1$ at the right moment, and
future beliefs of player $1$ will stay in $\mathcal{L}_i$, in which case the
co-B&uuml;chi condition holds and player $2$ wins.

{In order to ensure the first item, player $2$ makes use of the hypothesis
about player $1$ beliefs staying outside $\LL_i'$. For that player $2$ needs to keep track of all the possible beliefs of player $1$, hence the doubly-exponential memory.
The reason is player $2$ can infer
from this data structure some information about the possible actions played by player $1$: in case
for every possible belief of player $1$ an action $i\in I$ creates a risk to reach $\mathcal{L}_i$
then player $2$ knows for sure this action is not played by player $1$.
This in turn helps player $2$ to know which are the possible states of the game.
Finally, when player $2$ estimates the state of the game using his $2$-beliefs,
this gives a potentially more accurate estimation of the possible states than simply computing his $1$-beliefs.}

{The positively winning $2$-belief strategy of player $2$ has a particular structure.
All memory updates are deterministic except for one: from
the initial memory state $\emptyset$,
whatever signal is received there is non-zero chance that the memory state stays $\emptyset$ but it may as well 
be updated to several other memory states.}

%
````

\smallskip
