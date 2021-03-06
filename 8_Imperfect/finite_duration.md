(8-sec:finite_duration)=
# Finite duration

We start with some results on the very interesting class of game
with finite duration.

A game has **finite duration**
if there is a set of absorbing vertices $L$, called **leaves**,
such that every play eventually reaches $L$.
In other words, the directed graph $(V,E)$ induced by all pairs $(v,w)$
such that 
$\exists a,b\in A, s,t \in S, \Delta(v,a,b)(w,s,t) > 0$
is acyclic, except for self loops on leaves.

Moreover, $C$ is the set of real numbers,
colours are called **payoffs**.
At the moment the play $\pi$ reaches a leaf $\ell\in L$
for the first time,
the game is essentially over:
Eve receives the sum of payoffs seen to far,
denoted ${\tt pay}(\pi)$ and all future payoffs are $0$.
Such plays are called **terminal plays**.

Once a terminal play occurs, the game is over.
For this reason, in this section we restrict realisable sequences of signals
to the ones occurring in terminal plays and their prefixes.
This guarantees finiteness of $R_E$ and $R_A$ since

$$
R_E \cup R_A \subseteq S^{\leq n}\enspace.
$$

An initial distribution $\delta_0$ and two strategies $\sigma$ and $\tau$ of Eve and Adam naturally induce a probability distribution $\mathbb{P}_{ \delta_0}^{\sigma,\tau}$
on the set of terminal plays starting in one of the vertices $v_0,  \delta_0(v_0)>0$.
Players have opposite interests:
Eve seeks to maximize her expected payoff

$$
\mathbb{E}_{ \delta_0}^{\sigma,\tau}= \sum_{\text{ terminal plays }\pi} 
\mathbb{P}_{ \delta_0}^{\sigma,\tau}(\pi) \cdot {  {\tt pay}}(\pi)\enspace,
$$

while Adam wants to minimize it.

(8-subsec:value)=
## Existence and computability of the value

Next theorem gathers several folklore results.

````{prf:theorem} Finite duration games
:label: 8-thm:finiteimperfecthaveval

A game with finite duration and imperfect information has a value:
for every initial distribution $\delta_0$,

$$
\sup_\sigma \inf_\tau \mathbb{E}_{ \delta_0}^{\sigma,\tau}
 = 
 \inf_\tau \sup_\sigma \mathbb{E}_{ \delta_0}^{\sigma,\tau}\enspace.
$$

This value is denoted $\textrm{val}( \delta_0)$
and is computable .

```{margin}
provided payoffs are presented in a way
compatible with linear solvers, typically 
rational values.
```

Both players have optimal strategies.

````

> **Reduction to normal form.**

The main ingredient for proving this theorem is a transformation
of the game into a matrix game called its **normal form**.

The intuition is that a player,
instead of choosing progressively her actions
as she receives new signals,
may choose once for all at the beginning of the game
how to react to every possible sequence of signals
she might receive in the future.

Fix an initial distribution $\delta_0$.
In the normal form version the game,
Eve  picks 
a **deterministic** strategy
$\sigma : R_E \to A$
while simultaneously
Adam picks
$\tau : R_A \to A$.
Then the game is over
and Eve receives payoff
$\mathbb{E}_{ \delta_0}^{\sigma,\tau}$.
There are finitely many such deterministic strategies,
thus the normal form game is a **matrix game**.
See Section {ref}`7-sec:matrix_games` for more details
about matrix games.

> **An example.**

In the simplified poker example,
the reduction is as follows.

We rely on the formal description of the game at the end of {prf:ref}`subsec:formalimp`
and perform two simplifications.
First, we only consider strategies playing moves according to the rules,
other strategies are strategically useless.

Deterministic strategies of Eve are
mappings $\sigma : \{\spadesuit,\blacksquare\}
\to\{ {\tt check},{\tt raise}\}$.
Adam has only two deterministic strategies:
after the sequence $\circ {\tt Raised}$,
he should choose between
actions ${\tt call}$ and ${\tt fold}$.

The normal form is

$$
\begin{array}{c|c|c}
&  {\tt call} &{\tt fold}\\
\hline
\spadesuit\to {\tt check},  \blacksquare\to {\tt check}
& -0.5 & -0.5\\
\hline
\spadesuit\to {\tt raise},  \blacksquare\to {\tt check}
& 0 & -0.5\\
\hline
\spadesuit\to {\tt raise},  \blacksquare\to {\tt raise}
& -1.5 & +1\\
\hline
\spadesuit\to {\tt check},  \blacksquare\to {\tt raise}
& -2 & +1\\
\end{array}
$$

The first line corresponds to Eve never raising,
thus her odds are +1 euro at $25\
and -1 at $75\
$-0.5$.
The third line corresponds to Eve always raising.
If Adam calls then her odds are +3 at $25\
and -3 at $75\
If Adam folds, she gets payoff +1.

Remark that the rows where Eve checks with $\spadesuit$
are dominated by the corresponding row where Eve does not.
Thus checking with $\spadesuit$ (slow playing) has no strategic interest,
and  by elimination of weakly dominated strategies,
the normal form game is equivalent to:

$$
\begin{array}{c|c|c}
&  {\tt call} &{\tt fold}\\
\hline
\spadesuit\to {\tt raise},  \blacksquare\to {\tt check}
& 0 & -0.5\\
\hline
\spadesuit\to {\tt raise},  \blacksquare\to {\tt raise}
& -1.5 & 1\\
\end{array}
$$

The value of this game is $-\frac{1}{4}$.
Eve has a unique optimal strategy which consists in playing the top row with probability
$\frac{5}{6}$.
In other words, she should bluff with probability $\frac{1}{6}$ when she receives $\blacksquare$.
Adam has a unique optimal strategy which consists in calling or folding
with equal probability $\frac{1}{2}$\enspace.

> **Proof of {prf:ref}`8-thm:finiteimperfecthaveval`.**

The example illustrates
the correspondance between behavioural strategies in the finite-duration game on one side
and mixed strategies in the normal form game on the other.
In the general case, the correspondance can be stated as follows.

````{prf:lemma} NEEDS TITLE 8-lem:impinffinite
:label: 8-lem:impinffinite

Denote $\text{Strat}$ the set of behavioural strategies,
$\text{Strat}_d$ the subset of deterministic strategies
and $\mathcal{D}( \text{Strat}_d)$ the set of strategies in the normal form game.

1.  There is a mapping 
$
\Phi :  \text{Strat} \to  \mathcal{D}( \text{Strat}_d)
$

which preserves payoffs:

$$
\forall \sigma,\tau \in  \text{Strat},
\mathbb{E}_{ \delta_0}^{\sigma,\tau}
=
\sum_{\sigma',\tau' \in  \text{Strat}_d}\Phi(\sigma)(\sigma')\cdot\Phi(\tau)(\tau') 
\cdot\mathbb{E}_{ \delta_0}^{\sigma',\tau'}\enspace.
$$

2.  Since actions are observable,
there is a mapping 
$
\Phi' :  \mathcal{D}( \text{Strat}_d) \to  \text{Strat} 
$

which preserves payoffs:

$$
\forall \Sigma,T \in  \mathcal{D}( \text{Strat}),
\sum_{\sigma',\tau' \in  \text{Strat}_d}\Sigma(\sigma') T(\tau')
\mathbb{E}_{ \delta_0}^{\sigma',\tau'}
=
\mathbb{E}_{ \delta_0}^{\Phi'(\sigma),\Phi'(\tau)}
\enspace.
$$

3.  $\Phi'\circ \Phi$ is the identity.

````

We assumed earlier that each player can observe
its own actions. This hypothesis is necessary for ii) and iii)
to hold in general.

````{admonition} Proof
:class: dropdown tip

We start with i).
Intuitively,
all random choices of actions performed by
a behavioural strategy $\sigma$ of Eve can be done at the beginning of the play.
Playing $\sigma$ 
is equivalent to playing each deterministic strategy $\sigma'$ 
with probability

$$
\Phi(\sigma)(\sigma') = 
\Pi_{u \in R_E} \sigma(u)(\sigma'(u))\enspace.
$$

We prove ii).
Let $\Sigma\in \mathcal{D}( \text{Strat})$. The definition of the behavioural strategy
$\sigma=\Phi'(\Sigma)$ is as follows.
Let $s_0\ldots s_k$ be a finite sequence of signals.
Since actions are observable, this defines unambigously
the sequence of corresponding actions $a_0\ldots a_k$
where $a_i =  \text{Act}(s_i)$.

We set $\sigma(s_0\ldots s_k)(a)$ to be the probability that a 
deterministic strategy
chosen with $\Sigma$ chooses action $a$ after signals
$s_0\ldots s_k$, conditioned on the fact that it has already
chosen action $a_0\ldots a_k$:

$$
\sigma(s_0\ldots s_k)(a) 
=
\Sigma\left(\sigma'(s_0\ldots s_k)=a \mid \forall 0\leq i \leq k,
 \sigma'(s_0\ldots s_{i-1})= \text{Act}(s_i)\right)\enspace,
$$

where the vertical pipe denotes a conditional probability.

````

We proceed with the proof of {prf:ref}`8-thm:finiteimperfecthaveval`.

According to {prf:ref}`8-lem:mat`,
the normal form has a value and optimal strategies
for each player. 
Denote $\textrm{val}_N$ the value
and $\Sigma^\sharp$ and $T^\sharp$ the optimal strategies.
Let $\sigma^\sharp=\Phi'(\Sigma^\sharp)$.
Then $\sigma^\sharp$ ensures a payoff
of at least $\textrm{val}_N$ in the imperfect information game,
because for every strategy $\tau$,

$$
\mathbb{E}_{ \delta_0}^{\sigma^\sharp,\tau}
=
\mathbb{E}_{ \delta_0}^{\Phi'(\Sigma^\sharp),\Phi'(\Phi(\tau))}
=
\sum_{\sigma',\tau' \in  \text{Strat}_d}\Sigma^\sharp(\sigma') \Phi(\tau)(\tau')
\mathbb{E}_{ \delta_0}^{\sigma',\tau'}
\geq   \textrm{val}_N\enspace,
$$

where the first equalities are applications of {prf:ref}`8-lem:impinffinite`
and the inequality is by optimality of $\Sigma^\sharp$.
Symmetrically, 
$\tau^\sharp=\Phi'(T^\sharp)$ guarantees 
$\forall \sigma,\mathbb{E}_{ \delta_0}^{\sigma,\tau^\sharp}\leq  \textrm{val}_N$. 
Thus the value of the game with finite duration
is $\textrm{val}_N$ and $\sigma^\sharp$
and $\tau^\sharp$ are optimal.\qed

(8-subsec:reduction_linear_programming)=
## The Koller-Meggido-von Stengel reduction to linear programming

The reduction of a finite-duration game with imperfect information
to its normal form proves that the value exists and
is computable.
However the corresponding algorithm is computationally
very expensive, it requires solving
a linear program of size roughly doubly-exponential in the size 
of the original game, since the normal form is a matrix
index by $A^{R_E} \times A^{R_A}$ and the set of signal sequences
might contain all sequences of $S$ of length $\leq n$.

Koller, Meggido and von Stengel did provide a
more efficient direct reduction to linear programming.
Strategies of Eve in the normal form game live
in $\mathbb{R}^{A^{R_E}}$
while her strategies in the game with imperfect information
live in a space
with exponentially fewer dimensions, namely
$\mathbb{R}^{R_E\times A}$.
The direct reduction avoids this dimensional blowup.

````{prf:theorem} NEEDS TITLE AND LABEL 
The value of a game with imperfect information
can be computed by a linear program with
$|R_E| + |R_A|$ variables.

The value of a game with imperfect information
can be computed by a linear program with
$|R_E| + |R_A|$ variables.

````

As a consequence, in the particular case where the game graph is a tree
then $|R_E|\leq n$ and $|R_A|\leq n$
and the value can be computed in polynomial time,
like stated in {cite}`stengel`.

````{admonition} Proof
:class: dropdown tip

The construction of the linear program relies on three key ideas.

First, representing a behavioral strategy $\sigma:R_E \to  \mathcal{D}(A)$
 of Eve as a **plan** $\pi:R_E  \to [0,1]$
 recursively defined by $\pi(\epsilon) = 1$
 and for every $s_0\cdots s_n \in R_E, s\in S$,
 
$$

& \pi(s_0\cdots s_n\cdot s) = \pi(s_0\cdots s_n) \cdot
 \sigma(s_0\cdots s_n)( \text{Act}(s))\enspace.
 
$$

Remind that actions are observable and $\text{Act}(s)$
denotes the action that Eve has just played
before receiving signal $s$.
In the linear program, plans are represented by variables 
$\left(p_r\right)_{r \in R_E}$. 
Valuations corresponding to plans can be characterized by 
the following equalities.
First, $p_\epsilon = 1$.
Second, for every 
$s_0\ldots s_{n-1}s,s_0\ldots s_{n-1}s' \in R_E$,

$$

( \text{Act}(s)= \text{Act}(s')) \implies \left(p_{s_0\ldots s_{n-1}s}= p_{s_0\ldots s_{n-1}s'}\right)\enspace.

$$

We denote $p_{s_0\ldots s_{n-1}a}$ the common value of
all $p_{s_0\ldots s_{n-1}s}$ with $a= \text{Act}(s)$.
The third equality is 
$p_{s_0\ldots s_{n-1}}=\sum_{a\in A} p_{s_0\ldots s_{n-1}a}$ \enspace.

 The second key idea is to introduce variables evaluating the contribution of a 
 (realisable) sequence
 of signals of Adam to the total expected payoff Eve.
 These contributions are represented by variables $(v_r)_{r \in R_A}$.

 The third key idea is to aggregate the product of transition
 probabilities along a play.
For every play $(v_0,a_0,b_0,s_0,t_0,c_0),\ldots,(v_k,a_k,b_k,s_k,t_k,c_k)$
 we denote $\mathbb{E}(\pi)$ the product of all transition
probabilities of $\pi$ and $r_{E}(\pi)$ the sequence of signals of Eve in this play:

$$

&\mathbb{E}(\pi) =  \delta_0(v_0)\cdot \Delta(v_0,a_0,b_0,s_0,t_0,c_0)
  \cdots \Delta(v_k,a_k,b_k,s_k,t_k,c_k)\\
 & r_{E}(\pi) = s_0,s_1,\ldots,s_k\enspace.

$$

We show that the following linear program with variables
  $(p_r)_{r \in R_E}$, $(v_r)_{r\in R_A}$
  has an optimal solution which equals to $\textrm{val}( \delta_0)$.
 For every sequences of signals $r \in R_A$
 we denote $T_A(r)$ the (possibly empty)
 set of terminal plays whose sequence of signals for Adam is $r$.

$$

&\text{Maximise $v_{\epsilon}$ subject to}
\notag\\
\notag\\
\notag&\text{$\left(p_r\right)_{r \in R_E}$ is a plan of Eve}
\notag\\
\notag\\
\notag\forall r \in R_A,
\forall a \in A,&
\\

&
\label{eq:implp2}
v_{r} \leq \sum\limits_{\substack{rs \in R_A\\s \in S,  \text{Act}(s)=a}}
v_{rs} + \sum\limits_{\pi \in T(r)} \mathbb{E}(\pi) \cdot   {\tt pay}(\pi) \cdot 
p_{r_E(\pi)}

$$

For our purpose,
it is enough to establish 
that the optimal solution of the LP
is

$$
  \textrm{val}( \delta_0) = \sup_\sigma \min\limits_{\tau\text{ deterministic}} \mathbb{E}_{ \delta_0}^{\sigma,\tau}\enspace.
$$

The reason is that in a matrix game,
for every fixed strategy of Eve,
Adam can minimize the payoff by playing a single action
with probability $1$.
Thus, according to the reduction to normal form seen in the previous chapter,
for every strategy $\sigma$ of Eve,
there is a **deterministic** strategy $\tau$ of Adam
which minimizes $\mathbb{E}_{ \delta_0}^{\sigma,\tau}$.

We show first that for every feasible solution 
$(p_r)_{r \in R_E}$, $(v_r)_{r\in R_A}$ of the linear program,
the strategy $\sigma$ corresponding to the plan $(p_r)_{r \in R_E}$
guarantees that for every **deterministic** strategy $\tau$,
$\mathbb{E}_{ \delta_0}^{\sigma,\tau} \geq v_\epsilon$.
Since $\tau$ is deterministic
then $\mathbb{E}_{ \delta_0}^{\sigma,\tau}$
is the sum of all $\mathbb{E}(\pi) \cdot   {\tt pay}(\pi) \cdot 
p_{r_E(\pi)}$ over plays $\pi$ played according to $\tau$
thus a trivial induction shows $\mathbb{E}_{ \delta_0}^{\sigma,\tau}\geq v_\epsilon$.

We show now that to every strategy $\sigma$ of Eve,
and to every deterministic optimal answer $\tau$ of Adam, 
corresponds a feasible solution of the program
such that $v_\epsilon = \mathbb{E}_{ \delta_0}^{\sigma,\tau}$.
Let  $(p_r)_{r \in R_E}$ the plan corresponding to $\sigma$.
For every $r\in R_A$ define $v_r$ be the expected payoff of Eve
in an auxiliary game where she plays $\sigma$
and Adam plays $\tau$ and the payoff of Eve is turned to $0$
whenever Adam signals sequence does not start with $r$.
We show that the linear constraint {eq}`8-eq:implp2` holds for every $r\in R_A$
 and action $a$.
Since $\tau$ is deterministic then {eq}`8-eq:implp2` is an equality
whenever $a=\tau(r)$.
And since $\tau$ is an optimal answer to $\sigma$,
it is locally optimal in the sense where playing an action
different from $\tau(r)$ after $r$ cannot be profitable to Adam,
hence {eq}`8-eq:implp2` holds.
Finally, $(p_r)_{r \in R_E}$, $(v_r)_{r\in R_A}$ is a feasible solution.

````

> **An example.**

The following linear program computes the value
of the simplified poker example.
DEAL WITH LINEAR PROGRAMS!

> **Nose scratch variant.**

Assume now that Eve does not have the perfect poker face:
whenever she has $\spadesuit$ she scratches
her nose with probability $\frac{1}{2}$ whereas
in general it happens only with probability $\frac{1}{6}$.
Only Adam is aware of this sign,
which he receives
as a private signal $s$ (scratch) or $n$ (no scratch).

Compared to the perfect poker face situation,
 the situation is slightly better for Adam:
 the value drops from $-\frac{1}{4}$
to $(-\frac{1}{4} -\frac{1}{10})$.
The optimal bluff frequency of Eve decreases
 from $\frac{1}{6}$ to $\frac{1}{10}$.
Computation details follow.

DEAL WITH LINEAR PROGRAMS!

The optimum is reached when $8y-10=8-12y$
i.e. when $p_{\blacksquare,{\tt c} }=\frac{9}{10}$
and is equal to $-\frac{7}{20}=-\frac{1}{4}-\frac{1}{10}$ .
