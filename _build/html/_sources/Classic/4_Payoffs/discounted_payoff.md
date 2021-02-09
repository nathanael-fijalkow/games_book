(4-sec:discounted_payoff)=
# Discounted payoff games

From a practical point of view, the modelling of a real-world
situation via mean payoff games requires that only the long-term
behaviour is important. Since mean payoff only depends on the limit of
the play, it cannot be used to model the beginning of the execution:
the mean payoff is said to be **prefix independent**. In economical
studies, there is a tendency to make the prefixes count more, since
they represent short-term implications of the actions taken, even if
long-term behaviours also matter. The common payoff used to model this
preference to prefixes is the discounted payoff that associates to a
play $\play$ the weight

$$\DiscountedPayoff_\lambda(\play) = (1-\lambda)\sum_{i=0}^{\infty} \lambda^i
  \, c(\play_i)$$

 where $\lambda$ is a parameter in the interval
$(0,1)$, ensuring the convergence of the infinite series (since
weights $c(\play_i)$ are bounded). The coefficient $1-\lambda$ before
the series is just to counterbalance the fact that if all weights in
the game are $1$, we would like the payoff to be 1 too, which then
holds since $\sum_{i=0}^\infty \lambda^i = \frac 1{1-\lambda}$. When
$\lambda$ tends to $0$, only the prefixes (and even the first weight)
matters. On the contrary, when $\lambda$ tends to $1$, the
discounted payoff looks more and more like the mean payoff. To grasp
an intuition why this holds, consider a play that results from
positional strategies in a mean payoff game. The weights encountered
during the play then ultimately follow a periodic sequence
$w_0,w_1,\ldots,w_{r-1},w_0,w_1,\ldots,w_{r-1},w_0,\ldots$ with
average-payoff $\frac 1 r\sum_{i=0}^{r-1}w_i$. Grouping the terms of
the series $(1-\lambda)\sum_{i=0}^{\infty} \lambda^i \, w_i$ by
batches of $r$ terms, we then obtain

$$(1-\lambda)\sum_{i=0}^{\infty} \lambda^{ri} \sum_{j=0}^{r-1}
  \lambda^jw_j=\frac{1-\lambda}{1-\lambda^r}\sum_{j=0}^{r-1}
  \lambda^jw_j= \frac
  1{1+\lambda+\cdots+\lambda^{r-1}}\sum_{j=0}^{r-1} \lambda^jw_j$$

that tends towards the average-payoff $\frac 1 r\sum_{j=0}^{r-1} w_j$
when $\lambda$ tends to $1$.

The weighted game of {ref}`Figure <4-fig:MP>` can also be equipped with a
discounted payoff. If $\lambda$ is close to $1$, for instance
$\lambda=0.9$, then optimal strategies are the same as for the
mean payoff objective: $\sigma^*(0)=1$, $\sigma^*(2)=3$,
$\tau^*(1)=2$, $\tau^*(3)=1$, and $\tau^*(4)=0$. In that case, the
discounted payoff of the unique lasso play
$(0,1)\big((1,2)(2,3)(3,1)\big)^\omega$ starting in $0$ and following
this profile of strategies is
$(1-\lambda)\left(4+
  \frac{2\lambda+4\lambda^2-\lambda^3}{1-\lambda^3}\right)$, which is
around $1.7$ when $\lambda=0.99$, while the mean payoff optimal value
of vertex 0 was $5/3\approx 1.67$. However, the situation completely
changes when $\lambda$ decreases. When $\lambda=0.5$ for instance,
Adam changes his decision in vertex $1$ and decides to go to vertex
$0$: this is because the cycle $(1,0)$ has now a discounted payoff
that becomes low enough, the first weight $0$ being much lower than
$2$ (if he decides to go to vertex $2$). For a really low value of
$\lambda$, for instance $\lambda=0.1$, the decisions again change
drastically for both players: now the optimal (positional) strategy
become $\sigma^*(0)=4$, $\sigma^*(2)=3$, $\tau^*(1)=0$, $\tau^*(3)=0$,
and $\tau^*(4)=0$, i.e.~Adam changed his decision in vertex $3$, and
Eve in vertex $0$. However, we note that for each value of $\lambda$
considered so far, positional optimal strategies are described. This
is no accident, as we will see in the remainder of the chapter.

We now study how to solve this class of games, and how it is used to
obtain a theoretically more efficient solution to mean payoff
games. Indeed, we will obtain a pseudopolynomial time complexity for
both objectives.

## Positional determinacy via a contraction mapping

First, it is easier (than for mean payoff games) to prove that
discounted payoff games are positionally determined, by using a
description of the values as a fixed point of a contracting operator
$F\colon \R^V\to \R^V$ that maps every vector $\vec x=(x_v)_{v\in V}$
to a new vector $(y_v)_{v\in V}$ corresponding to the best that both
players can hope for in one transition if they are rewarded by vector
$\vec x$ afterwards: for all $v\in V$, we thus let
\begin{equation}y_v =
  \begin{cases}
    \max_{(v,v')\in E} [(1-\lambda) c(v,v') + \lambda x_{v'}] &
    \text{ if } v\in \VE\\
    \min_{(v,v')\in E} [(1-\lambda) c(v,v') + \lambda x_{v'}] &
    \text{ if } v\in \VA\\
  \end{cases}\label{4-eq:F-contraction}
\end{equation}

```{admonition} Theorem (\cite{Zwick&Paterson:1996})
:class: theorem
:name: 4-thm:discounted

  Discounted payoff games are positionally determined.

```

```{admonition} Proof
:class: dropdown tip

  We prove that $F$ is indeed a contracting operator.
  For all vectors $\vec x=(x_v)_{v\in V}$ and
  $\vec y = (y_v)_{v\in V}$, we have, by definition,
  $\|F(\vec x)-F(\vec y)\|_\infty = \max_{v\in V}|F(\vec x)_v-F(\vec
  y)_v|$. Let $v\in \VE$. Consider a vertex $v'$ such that
  $F(\vec x)_v = (1-\lambda) c(v,v') + \lambda x_{v'}$. Then,
  $F(\vec y)_v\geq (1-\lambda) c(v,v') + \lambda y_{v'}$ so that
  $F(\vec x)_v-F(\vec y)_v\leq \lambda(x_{v'}-y_{v'})$. By now
  considering $v''$ such that
  $F(\vec y)_v = (1-\lambda) c(v,v'') + \lambda y_{v''}$, we obtain
  also that $F(\vec x)_v-F(\vec y)_v\geq \lambda(x_{v''}-y_{v''})$. In
  the overall, we thus have
  $|F(\vec x)_v-F(\vec y)_v|\leq \lambda\|\vec x-\vec y\|_\infty$. The
  same reasoning also applies to a vertex $v$ of $\VA$. Therefore, we
  obtain
  $\|F(\vec x)-F(\vec y)\|_\infty\leq \lambda\|\vec x-\vec y\|_\infty$
  which means that $F$ is a contraction mapping (since $0<\lambda<1$).

  By Banach fixed-point theorem, $F$ admits a unique fixed-point
  vector $\vec{x^*}$, such that $F(\vec{x^*})=\vec {x^*}$. This
  fixed-point is moreover the limit of the sequence of vectors
  $(F^n(\vec 0))_{n\in \N}$ with $\vec 0$ being the null vector, by
  Kleene fixed-point theorem (since $F$ is continuous, by composition
  of continuous functions). Imagine that Eve plays a positional
  strategy dictated by the equality $F(\vec{x^*})=\vec {x^*}$,
  i.e.~when in vertex $v\in \VE$, she chooses to go to some vertex
  $v'$ such that $x^*_v = (1-\lambda) c(v,v') + \lambda
  x^*_{v'}$. Then, she guarantees, by an easy induction proof, a value
  at least $x^*_v$ when starting in vertex $v$ (for all $v\in V$). A
  symmetrical argument for Adam allows one to obtain that, for all
  $v\in V$, 

$$\ValueA(v)\leq x^*_v \leq \ValueE(v)\,.$$

 Since we
  always have $\ValueE(v)\leq \ValueA(v)$, we finally obtain that the
  game is determined, and that $x^*$ is equal to the optimal value
  vector. Moreover, the two above positional strategies for Eve and
  Adam are optimal.

```

As for mean payoff (or parity) games, the existence of positional
optimal (or winning) strategies for both players, and the ability to
solve in polynomial time the one-player version of these games, allows
us to obtain easily an $\NP\cap\coNP$ complexity to solve
discounted payoff games in the case of integer costs and a rational
discount factor. The use of the above contracting operator even
ensures that the Turing machines guessing and checking the optimal
strategies may indeed be designed as unambiguous (instead of just
non-deterministic). Calling $\UP$ the class of problems that can be
solved by an unambiguous Turing machine running in polynomial time,
and $\coUP$ the class of problems whose complement are in $\UP$, we
then obtain the theorem:

```{admonition} Theorem (\cite{Jurdzinski:1998})
:class: theorem
:name: 4-thm:disc-up

  Discounted payoff games with integer costs and rational discount
  factor $\lambda$ can be solved in $\UP\cap\coUP$.

```

```{admonition} Proof
:class: dropdown tip

  Using the previous result, we know that the value of a
  discounted payoff game is the **unique** solution of the fixed
  point equation $\vec x = F(\vec x)$, with $F$ a contraction
  mapping. Therefore, guessing vector $\vec x$ and checking it is
  indeed a fixed point of $F$ can be performed in an unambiguous
  Turing machine. To conclude, it only remains to show that this check
  can be done in polynomial time, in particular we must show that the
  values $\vec x$ are **short** in terms of their binary
  representation. The equality $\vec x = F(\vec x)$ induces optimal
  decisions in each vertex, thus leading to a profile of strategies
  for both players. We summarise this profile
  in:  *  a square Boolean matrix
  $Q\in \{0,1\}^{V\times V}$, whose entry $Q_{v,v'}$ is $1$ if
  $(v,v')$ is the chosen edge in $v$ by the profile, and $0$
  otherwise; *  a vector $\vec c\in \Z^{V}$, whose entry $c_v$ is
  the weight of the edge $(v,v')$ chosen in $v$ by the
  profile.   We can then write the fixed point equation
  as 

$$\vec x = (1-\lambda) \vec c + \lambda Q \vec x\,.$$

 Letting
  $\lambda = a/b$ the rational discount factor, the above equation
  rewrites into \begin{equation} A\vec x = (b-a)\vec
  c\label{4-eq:1} \end{equation} with $A= b I- a Q$ ($I$ being the
  identity matrix). Therefore, $A$ is a matrix that has at most two
  non-zero elements in each row: each of these non-zero elements can
  be written using at most $N=\max(\log_2 a,\log_2 b)$ bits (therefore
  polynomial in the representation of the game), and are therefore
  bounded in absolute value by $2^N$. By induction on the size of the
  matrix, we can then show that the determinant of $A$ is at most
  $4^{Nn}$. \cref{4-eq:1} then resolves, using Cramer's formula, by
  $x_v = \det (A_v) / \det (A)$, with $A_v$ the matrix obtained from $A$
  by replacing the $v$-th column with vector $(b-a)\vec c$. Therefore,
  all components of $\vec x$ can be written with only a polynomial of
  bits with respect to the size of the costs in the arena and $N$.

  The $\coUP$ membership follows, as in  {ref}`Theorem <4-thm:MP-NPcoNP>`, from a
  dual reasoning for Adam, using the above determinacy result for
  discounted payoff games. 

```

For the discounted payoff game of {ref}`Figure <4-fig:MP>`, the contracting
operator is:

$$F\left(
  \begin{array}{c}
    x_{v_0}\\x_{v_1}\\x_{v_2}\\x_{v_3}\\x_{v_4}
  \end{array}\right) =
  \left(
    \begin{array}{c}
      \max\big(4(1-\lambda)+\lambda x_{v_1}, (1-\lambda)5+\lambda x_{v_4}\big)\\
      \min\big(\lambda x_{v_0}, 2(1-\lambda)+\lambda x_{v_2}\big)\\
      \max\big((1-\lambda)+\lambda x_{v_2}, 4(1-\lambda)+\lambda x_{v_3}\big)\\
      \min\big(-2(1-\lambda)+\lambda x_{v_0}, -(1-\lambda)+\lambda x_{v_1}\big)\\
      \min\big(-2(1-\lambda)+\lambda x_{v_0}, 2(1-\lambda)+\lambda x_{v_4}\big)
    \end{array}
  \right)\,.$$


A careful analysis gives the fixed points for all values of
$\lambda\in (0,1)$, which in turn allows us to find the associated
positional optimal strategies $\sigma^*$ and $\tau^*$ on the various
intervals of values for $\lambda$, summarised in the following table:

$$
  \begin{array}{|c|c|c|c|c|}\hline
    \lambda & (0, \lambda_1]
    & (\lambda_1,\lambda_2] & (\lambda_2,\lambda_3]
    & (\lambda_3,1) \\\hline
    \sigma^*(v_0) & v_4 & v_4 &  v_1   & v_1  \\\hline
    \tau^*(v_1) & v_0 &  v_0 &   v_0 &   v_2  \\\hline
    \sigma^*(v_2) & v_3  & v_3   & v_3 &   v_3 \\\hline
    \tau^*(v_3) &v_0 &  v_1  & v_1 &   v_1  \\\hline
    \tau^*(v_4) & v_0 &  v_0  & v_0 &  v_0\\\hline
  \end{array}$$

where frontiers are at $\lambda_1 = 1-\sqrt 2/2 \approx 0.293$,
$\lambda_2 = 1/2$, and $\lambda_3 \approx 0.841$. For instance, on
interval $(0,\lambda_1]$, Adam gets discounted payoff
$\frac{5\lambda-2}{1+\lambda}$ when starting 
in vertex $v_3$, while switching his decision in interval
$(\lambda_1,\lambda_2]$ allows him to secure
$\frac{-2\lambda^3+6\lambda^2-1}{1+\lambda}$: this gives the
explanation for the value of $\lambda_1$ which allows one to equal the
two values. A similar reasoning provides the values of
$\lambda_2$ and $\lambda_3$.

## Strategy improvement algorithm

We apply the strategy improvement paradigm already used for
mean payoff games. However, in the context of discounted payoff games,
this algorithm will directly run on the game itself to compute optimal
values and an optimal strategy for Eve (instead of only deciding if
Eve can guarantee a positive mean payoff).

The principle is identical though: it relies on an amelioration of a
strategy based on a local switching policy. Starting from an arbitrary
positional strategy of Eve, we apply local improvements by switching
some decisions to obtain a strictly better positional strategy. Since
there are only a finite (but exponential) number of positional
strategies, this strategy improvement algorithm will terminate (with
at most exponential time worst-case complexity). Moreover, it is
correct, as we will see, meaning that the local optimum we find when
no more switching is applicable is indeed a global optimum for Eve,
meaning that we have computed a (positional) optimal strategy for her.

To describe the switching policy used to solve discounted payoff
games, consider a strategy $\sigma$ of Eve, and let $\Value^\sigma(v)$
be the best possible value Adam can get against $\sigma$, when the
play starts from vertex $v$:

$$\Value^\sigma(v) = \inf_\tau
  \DiscountedPayoff_\lambda(v,\sigma,\tau).$$

 Two strategies $\sigma$
and $\sigma'$ are compared with respect to the vectors
$\vec x=\Value^\sigma$ and $\vec{x'}=\Value^{\sigma'}$: we denote by
$\vec x\leq \vec{x'}$ the fact that $x_v\leq x'_v$ for all vertices
$v\in V$. Computing the vector $\Value^\sigma$ amounts to solving a
one-player discounted payoff game where Eve's vertices are now
constrained to follow $\sigma$, and thus can be replaced by Adam's
vertices. By {ref}`Theorem <4-thm:discounted>`, the solution of such a
one-player game is still the unique fixed point of the contraction
mapping $F_\sigma$ defined for all $\vec x\in \R^V$ and $v\in V$ by

$$F_\sigma(\vec x)_v = \min_{(v,v')\in E}[(1-\lambda)c(v,v')+\lambda x_{v'}].$$



```{admonition} Proposition
:class: proposition
:name: 4-lem:one-player-DP

  We can compute in polynomial time the optimal value of a one-player
  discounted payoff game, by finding the unique fixed point
  $\vec{x^*}$ of the previous contraction mapping $F_\sigma$.

```

```{admonition} Proof
:class: dropdown tip

  We first show that if a vector $\vec x$ satisfies
  $\vec x\leq F_\sigma(\vec x)$, then $\vec x\leq \vec{x^*}$. Indeed,
  consider any positional strategy $\tau$ of the unique player Adam,
  and a vertex $v\in V$. Then,
  $x_v\leq F_\sigma(\vec x)_v\leq (1-\lambda)c(v,v')+\lambda x_{v'}$ with
  $(v,v')=\tau(v)$. We let $\play$ be the play starting in $v$, following
  $\tau$, and denote by $v=v_0,v_1,\ldots$ the sequence of vertices
  visited by $\play$. By induction,
  $x_v \leq (1-\lambda)\sum_{i=0}^{n-1}\lambda^i c(\play_i) +
  \lambda^nx_{v_n}$. Letting $n$ go to $+\infty$, we get that
  $x_v\leq \DiscountedPayoff_\lambda(\play)$. Since this holds for all
  strategies of Adam, and $\vec{x^*}$ is the optimal value vector of the
  game by {ref}`Theorem <4-thm:discounted>`, we obtain $x_v\leq x^*_v$.

  Therefore, it follows that $x^*$ is the unique solution of the
  linear program
  

$$
    \begin{cases}
      \max\sum_{v\in V}x_v \\
      \text{under the constraints }\quad x_v\leq
      (1-\lambda)c(v,v')+\lambda x_{v'}\qquad \forall (v,v')\in E
    \end{cases}$$

  Such a linear program can be solved in polynomial time. 

```

On top of computing the value $\Value^\sigma$ of a strategy $\sigma$
of Eve, we also compute the best response of Adam, that is the best
(positional) strategy $\tau$ he must play to achieve the lowest payoff
possible for Eve.

For the discounted payoff game of {ref}`Figure <4-fig:MP>` with $\lambda=0.5$,
if we start from Eve's strategy $\sigma(0)=4$ and $\sigma(2)=2$, the
simplified contraction mapping in the one-player remaining game is
given by:

$$F_\sigma\left(
  \begin{array}{c}
    x_0\\x_1\\x_2\\x_3\\x_4
  \end{array}\right) =
  \left(
    \begin{array}{c}
      (1-\lambda)5+\lambda x_4\\
      \min\big(\lambda x_0, 2(1-\lambda)+\lambda x_2\big)\\
      (1-\lambda)+\lambda x_2\\
      \min\big(-2(1-\lambda)+\lambda x_0, -(1-\lambda)+\lambda x_1\big)\\
      \min\big(-2(1-\lambda)+\lambda x_0, 2(1-\lambda)+\lambda x_4\big)
    \end{array}
  \right)\,.$$

 We compute the best response of Adam by solving the
linear program:

$$\begin{cases}
    \max x_0+x_1+x_2+x_3+x_4 \\
    \text{under the constraints } & x_0=(1-\lambda)5+\lambda
    x_4 \\
    & x_1\leq \lambda x_0 \\
    & x_1\leq 2(1-\lambda)+\lambda x_2\\
    & x_2 = (1-\lambda)+\lambda x_2 \qquad (\text{thus } x_2=1) \\
    & x_3\leq -2(1-\lambda)+\lambda x_0\\
    & x_3 \leq -(1-\lambda)+\lambda x_1 \\
    & x_4\leq -2(1-\lambda)+\lambda x_0\\
    & x_4\leq 2(1-\lambda)+\lambda x_4
  \end{cases}$$

 Feeding this linear program to a solver gives back the
solution $\vec x=(8/3,4/3,1,1/6,\allowbreak 1/3)$, which is associated
with the best response of Adam defined as $\tau(1)=0$, $\tau(3)=1$,
and $\tau(4)=0$. We can check if this vector $\vec x$ is a fixed point
of $F$ (and not only $F_\sigma$): we indeed have
$F(\vec x)_0=\max\big(4(1-\lambda)+\lambda x_1, (1-\lambda)5+\lambda
x_4\big)= \max(8/3,8/3)= 8/3$, but
$F(\vec x)_2=\max\big((1-\lambda)+\lambda x_2, 4(1-\lambda)+\lambda
x_3\big) = \max(1,25/12)=25/12\neq 1$. This suggests modifying
strategy $\sigma$ to a new strategy $\sigma'$ with $\sigma'(0)=4$ and
$\sigma'(2)=3$. The new vector of values found by solving the new
linear program is $\vec{x'}=(8/3,4/3,25/12,1/6,1/3)$, that is the
(unique) fixed point of $F$. Notice in particular that
$\vec{x}\leq \vec{x'}$ with a strict inequality on the component of
vertex $2$.

\medskip

We now come back to the general case by describing more precisely the
algorithm in {ref}`Algorithm <4-algo:DP-strategy-improvement>`, and prove its
correctness.  For a particular strategy $\sigma$ for Eve, once
$\Value^\sigma$ computed, we can check whether
$F(\Value^\sigma)=\Value^\sigma$ (with $F$ the more general operator
defined in \eqref{4-eq:F-contraction}). If it is the case, then we
know that the optimal value vector of the game is indeed
$\Value^\sigma$: thus, $\sigma$ is a positional optimal strategy for
Eve, and the best response of Adam is a positional optimal strategy
for him. In case $F(\Value^\sigma)\neq\Value^\sigma$, we consider for
every vertex $v\in \VE$, the decision $v'$ such that
$F(\Value^\sigma)_v=(1-\lambda)c(v,v')+\lambda \Value^\sigma(v')$. We
gather all these decisions in a new strategy $\sigma'$ for Eve (only
modifying $\sigma$ over vertices for which it allows for a strictly
better value, to ensure the termination of the algorithm).

\begin{algorithm}
 \KwData{A discounted payoff game $\game$ with discount factor
 $\lambda\in(0,1)$, and $F$ the contracting operator defined
 in~\eqref{4-eq:F-contraction}}
  
 $\sigma \leftarrow$ arbitrary positional strategy for Eve ;

 $\Value^\sigma \leftarrow $ fixed-point of $F_\sigma$  \tcp*{by {ref}`Lemma <4-lem:one-player-DP>`}

 \While{$F(\Value^\sigma) \neq \Value^\sigma$}
 {   
 \For{$v\in \VE$}
 {
   \If{$F(\Value^\sigma)_v \neq \Value^\sigma(v)$}{
     $v' \leftarrow $ a vertex such that $F(\Value^\sigma)_v =
     (1-\lambda)c(v,v')+\lambda \Value^\sigma(v')$ ;
     
     $\sigma(v) \leftarrow v'$
     }
}

  $\Value^\sigma \leftarrow $ fixed-point of $F_\sigma$   \tcp*{by {ref}`Lemma <4-lem:one-player-DP>`}

}

\Return{$(\Value^\sigma,\sigma)$}
\caption{The strategy improvement algorithm for discounted payoff games.}
\label{4-algo:DP-strategy-improvement}
\end{algorithm}

```{admonition} Theorem
:class: theorem
:name: 4-thm:DP-strategy-improvement-correctness

  Strategy improvement algorithm computes the value of the game, as
  well as a positional optimal strategy for Eve, in exponential time. 

```

```{admonition} Proof
:class: dropdown tip

  When the algorithm returns a strategy $\sigma$, it fulfils
  $F(\Value^\sigma)\neq \Value^\sigma$, and thus,
  by {ref}`Theorem <4-thm:disc-up>`, $\Value^\sigma$ is the value of the game,
  and $\sigma$ an optimal strategy of Eve.

  We thus only have to prove the termination of the algorithm, as well
  as its complexity. Consider the positional strategy $\sigma$ in the
  beginning of an iteration such that
  $F(\Value^\sigma)\neq \Value^\sigma$, as well as the strategy
  $\sigma'$ updated at the end of the same iteration. We see why
  $\Value^\sigma\leq \Value^{\sigma'}$, with a strict inequality for
  at least one of the coefficients. If it is correct, then it shows
  that the **while** loop terminates after a finite number of
  iterations, since there are only a finite number of positional
  strategies and that we cannot visit twice the same one.  More
  precisely, the algorithm has an exponential worst-case complexity,
  since it may have to go through all (or at least a large fraction
  of) the positional strategies.

  We thus prove that $\Value^\sigma\leq \Value^{\sigma'}$. Consider
  for that the two best responses of Adam, $\tau$ and $\tau'$
  respectively. As in the proof of {ref}`Theorem <4-thm:disc-up>`, letting $Q$,
  $\vec c$, $Q'$, and $\vec {c'}$ the respective matrices and cost
  vectors described by the profiles of strategies $(\sigma,\tau)$ and
  $(\sigma',\tau')$, we have
  

$$\Value^\sigma = (1-\lambda) \vec c + \lambda Q \Value^\sigma \qquad
    \text{ and } \qquad \Value^{\sigma'} = (1-\lambda) \vec {c'} +
    \lambda Q' \Value^{\sigma'}\,.$$

  Therefore, by adding and subtracting $\lambda Q'
  \Value^\sigma$ we obtain:
  

$$\Value^{\sigma'}-\Value^\sigma=\lambda Q'
    (\Value^{\sigma'}-\Value^{\sigma}) + \underbrace{\lambda
      (Q'-Q)\Value^\sigma + (1-\lambda)(\vec{c'}-\vec c)}_{=\vec
      \delta}\,.$$

 Since $Q'$ is a positive matrix with coefficients in
  $\{0,1\}$, the series $\sum_i \lambda^iQ'^i$ converges, which shows
  that $I-\lambda Q'$ is invertible of inverse
  $\sum_{i=0}^\infty \lambda^i Q'^i$. In particular, the inverse
  $(I-\lambda Q')^{-1}$ has only non negative coefficients, and its
  diagonal coefficients are positive. Therefore, to show that
  $\Value^{\sigma'}-\Value^\sigma=(I-\lambda Q')^{-1} \vec\delta$ is
  non-negative with at least one positive coefficient, it suffices to
  show that $\vec\delta$ is non-negative with at least one positive
  coefficient. Consider thus $v\in V$:
  
  *  If $v\in \VE$, we have
    $\delta_v=\lambda(\Value^{\sigma}(v'_1)-\Value^\sigma(v_1)) +
    (1-\lambda)(c(v,v'_1)-c(v,v_1))$, with
    $\sigma(v)=(v,v_1)$ and $\sigma'(v)=(v,v'_1)$. If $v_1=v'_1$, then
    $\delta_v=0$. Otherwise, since $\sigma'$ is obtained by switching
    the decisions according to $F$, we have $\delta_v>0$: notice that
    there exists at least one such vertex $v$, since otherwise,
    $\sigma'=\sigma$ and the algorithm has already terminated.
  *  If $v\in \VA$, we have the same formula for $\delta_v$ with
    $\tau(v)=(v,v_1)$ and $\tau'(v)=(v,v'_1)$. Once again, $\delta_v=0$
    if $v_1=v'_1$. Otherwise, since $\tau$ is the best response of Adam
    to the strategy $\sigma$ of Eve, $\tau$ is at least as good as
    $\tau'$, which means that $\delta_v\geq 0$ too.
  

```

We now study another algorithm to compute the values with a possibly
better worst-case complexity, trading an exponential (with respect to
the number of vertices) complexity (but polynomial with respect to the
binary encoding of $\lambda$ and the weights of the arena), for a
pseudopolynomial time complexity (polynomial with respect to the
number of vertices and the binary encoding of the weights of the
arena, but exponential with respect to the binary encoding of
$\lambda$).

## Value iteration algorithm

Another way to make use of the contraction mapping $F$
of~\eqref{4-eq:F-contraction} is to compute the sequence
$\big(F^n(\vec 0)\big)_{n\in \N}$ that converges towards the value
vector. However, the sequence is not stationary in general, and thus,
to obtain an exact value we find a index $K$ for which $F^K(\vec 0)$
is close to $\Value$, as well as a rounding procedure to get the exact
value $\Value$ from its approximation $F^K(\vec 0)$. It is mainly
based on the following technical lemma stating that $\Value(v)$ is a
rational number with a denominator that we can bound, in a similar
manner as for~\cref{4-cor:rational-MP} in the mean payoff setting:

```{admonition} Lemma
:class: lemma
:name: 4-lem:rational-discounted

  If the arena has integer costs and $\lambda=\frac a b\in (0,1)$,
  then for all vertices $v\in V$, $D\times \Value(v)\in \Z$, with
  $D= b^{n-1}\prod_{j=1}^{n}(b^j-a^j)$.

```

```{admonition} Proof
:class: dropdown tip

  By picking any two optimal positional strategies for Eve and Adam
  (by {ref}`Theorem <4-thm:discounted>`), we obtain a play $\pi$ starting in
  vertex $v\in V$ that has a discounted payoff
  $\DiscountedPayoff(\pi) = \Value(v)$. Since both strategies are
  positional, the play $\pi$ is a lasso: thus, the sequence of costs
  encountered through the play is of the form
  $w_0,w_1,\ldots,w_{k-1},(w_{k},\ldots,w_\ell)^\omega$, with
  $0\leq k\leq\ell< n$ and $w_i\in \Z$. We can thus compute the
  optimal value exactly:
  \begin{align*}
    \Value(v) &= (1-\lambda) \left[\sum_{i=0}^{k-1} \lambda^i w_i +
               \lambda^{k}\sum_{m=0}^\infty
               \lambda^{(\ell-k+1)m}\sum_{i=0}^{\ell-k}
               \lambda^iw_{k+i}\right]\\
             &= \frac{b-a}b \left[\sum_{i=0}^{k-1} \frac{b^{k-1-i}a^i w_i}{b^{k-1}} +
               \frac{\lambda^{k}}{1-\lambda^{\ell-k+1}}\sum_{i=0}^{\ell-k}
               \frac{b^{\ell-k-i}a^iw_{k+i}}{b^{\ell-k}}\right]\\
             &= \frac {N_1}{b^{k}} + 
               \frac{a^{k}b^{\ell-k+1}}{b^{k+1}(b^{\ell-k+1}-a^{\ell-k+1})}
               \frac{N_2}{b^{\ell-k}} \qquad \text{(with $N_1,N_2\in \Z$)}\\
             &= \frac{N_3}{b^{k}(b^{\ell-k+1}-a^{\ell-k+1})} \qquad \text{(with
               $N_3\in \Z$)}\\
             &= \frac{N}{b^{n-1}\prod_{j=1}^{n}(b^j-a^j)} \qquad \text{(with
               $N\in \Z$)} 
  \end{align*}
  which proves that $\Value(v)\times D = N\in \Z$.

```

Therefore, $\Value(v)$ is a rational number with a denominator bounded
by $D$. In particular, if we have an approximation $\eta$ of
$\Value(v)$ such that $|\Value(v)-\eta|<\frac 1 {2D}$, we get that
$\Value(v) = \frac{\lfloor D\eta+1/2\rfloor}D$. Using the fact that
operator $F$ is contracting, we can find an index $K$ after which this
rounding leads to the correct optimal value vector. In the following,
we let again $W = \max_{(v,c,v')\in E} |c|$ the maximal weight on edges of the arena, in
absolute values.

```{admonition} Lemma
:class: lemma
:name: 4-lem:number-steps-VI-discounted

  Let $K\in \N$ at most
  $\frac{1}{-\log_2\lambda} \left(\frac{n(n+3)}{2}\log_2b +
    \log_2 W+2\right)$. Then,
  $\|F^K(\vec 0)-\Value\|_\infty < \frac 1 {2D}$.

```

```{admonition} Proof
:class: dropdown tip

  First, we bound $D$ by $b^{n+\frac{n(n+1)}2}$, so that
  $\frac{n(n+3)}{2}\log_2b\geq \log_2D$. Therefore
  $K\geq \frac{1}{-\log_2\lambda} (\log_2D + \log_2 W+\log_24) =
  \log_{1/\lambda}(4DW)$. This implies that
  $\lambda^KW\leq \frac{1}{4D}< \frac 1 {2D}$. But $F$ is
  $\lambda$-contracting, so that
  $\|F^K(\vec 0)-\Value\|_\infty\leq
  \lambda^K\|\Value\|_\infty$. Since $\Value(v)$ is the discounted sum
  of weights all bounded in absolute value by $W$, we also know that
  $\|\Value\|_\infty\leq W$ which allows us to conclude.

```

Therefore, the value iteration algoritm consists at iterating the
contracting mapping $F$ for a certain number $K$ of steps which is
polynomial with respect to the arena, each of the steps being
performed in time $O(m)$, and then finish the computation by a
rounding procedure (see {ref}`Algorithm <4-algo:DP-value-iteration>`). In the
overall, it thus has complexity $O(K m)$.

\begin{algorithm}
 \KwData{A discounted payoff game $\game$ with discount factor
 $\lambda= a/b\in(0,1)$, and $F$ the contracting operator defined
 in~\eqref{4-eq:F-contraction}}
  
 $\vec x \leftarrow \vec 0$ ;

 $K \leftarrow \left\lceil \frac{1}{-\log_2\lambda} \left(\frac{n(n+3)}{2}\log_2b +
     \log_2 W+2\right) \right\rceil$ ;

 \For{$i = 1$ to $K$}
 {
   $\vec x \leftarrow F(\vec x)$
 }

 \Return{$\vec x$}
\caption{The value iteration algorithm for discounted payoff games.}
\label{4-algo:DP-value-iteration}
\end{algorithm}

```{admonition} Theorem
:class: theorem
:name: 4-thm:DP-value-iteration

  Value iteration algorithm computes in pseudopolynomial time the
  value vector of a given discounted payoff game with only rational
  weights and a rational discount factor $\lambda\in (0,1)$. 

```

```{admonition} Proof
:class: dropdown tip

  The correctness of the algorithm follows
  from {ref}`Lemma <4-lem:number-steps-VI-discounted>`.  This algorithm runs
  in pseudopolynomial time (and not polynomial-time) because of the
  dependence in the discount factor $\lambda$. Indeed, consider that
  $\lambda = 1-\frac 1 b$, with $b\in \N\setminus \{0\}$. Then, we may
  store $\lambda$ with $\log_2 b$ bits, yet
  $\frac 1{-\log_2\lambda} \sim_{b\to \infty} b\ln 2$ is exponential
  in $\log_2b$.

```


Once the optimal values are known, finding some positional optimal
strategies for both players still requires to work, as we have already
seen in {ref}`Section <1-sec:memory>`:

```{admonition} Theorem
:class: theorem
:name: 4-thm:DP-strategies

  In a discounted payoff game with integer costs and rational discount
  factor $\lambda = a/b$, optimal strategies for both players can be
  found in
  $\bigO\big((n^3b\log_2b + \log_2W)\allowbreak
  \log(m/n) m\big)$ time.

```


## Polynomial reduction from mean payoff games to
  discounted payoff games
\label{4-sec:mean_payoff-values}

Building upon the pseudopolynomial time algorithm for
discounted payoff, we now describe a classical encoding of mean payoff
games into discounted payoff games to obtain another algorithm with
pseudopolynomial time complexity for mean payoff games. Compared to
the algorithms studied before that were computing the values of a
mean payoff game by a binary search, this other algorithm (indeed the
oldest one) is more direct even if it does not obtain a better
complexity.

Recall that~\cref{4-cor:rational-MP} states that, in an arena where
costs are integers, the mean payoff value $\Value(v)$ is a rational
number with denominator in $\{1,\ldots,n\}$. The minimal distance
between two rational numbers $\frac \alpha k$ and $\frac{\alpha'}{k'}$
with $k,k'\in \{1,\ldots,n\}$ is
$\frac 1{n-1}-\frac 1{n}=\frac{1}{n(n-1)}$. Thus, a
$\frac{1}{2n(n-1)}$ approximation $\beta$ of $\Value(v)$ is enough
to apply a rounding procedure finding the only rational
$\frac \alpha k$ with $k\in \{1,\ldots,n\}$ in interval
$[\beta-\frac{1}{2n(n-1)}, \beta+\frac{1}{2n(n-1)}]$. By
interpreting the mean payoff game as a discounted payoff game with a
nicely chosen $\lambda$, we are able to find such a good
approximation:

```{admonition} Theorem (\cite{Zwick&Paterson:1996})
:class: theorem
:name: 4-thm:MP-Zwick-Paterson

  Let $\arena$ be an arena with integer costs. Let
  $\lambda\in(0,1)$. We let $\Value(v)$ be the value of vertex $v$ in
  the mean payoff game on $\arena$, and $\Value_\lambda(v)$ be the
  value of vertex $v$ in the discounted payoff game on $\arena$, with
  $\lambda$ as discount factor. Then
  $\|\Value-\Value_\lambda\|_\infty\leq 2n(1-\lambda)W$.

```

```{admonition} Proof
:class: dropdown tip

  Let $v\in V$. We prove the inequality
  $\Value_\lambda(v)-\Value(v)\geq -2n(1-\lambda)W$ by reasoning on
  Eve's strategies: a similar reasoning on Adam's strategies allows
  one to obtain the other inequality
  $\Value_\lambda(v)-\Value(v)\leq 2n(1-\lambda)W$.

  By {ref}`Theorem <4-thm:mean_payoff_positional>`, we may select positional optimal
  strategies for Eve and Adam in the mean payoff game, denoted by
  $\sigma^*$ and $\tau^*$ respectively. As we have already seen, the play
  $\play$ starting in $v$ following $\sigma^*$ and $\tau^*$ is then a
  lasso, with a sequence of costs encountered of the form
  $w_0,w_1,\ldots,w_{k-1},(w_k,\ldots,w_\ell)^\omega$ with
  $0\leq k\leq \ell<n$. Then,
  $\Value(v)=\frac 1 {\ell-k+1}\sum_{i=k}^\ell w_i$. By choosing the
  same strategy $\sigma$ for Eve in the discounted payoff game, we
  know that Eve's value is at least
  $\DiscountedPayoff_\lambda(\play)$: therefore, by the determinacy
  result of {ref}`Theorem <4-thm:discounted>`,
  $\Value_\lambda(v)\geq \DiscountedPayoff_\lambda(\play)$. We now
  compute precisely $\DiscountedPayoff_\lambda(\play)$:
  \begin{align*}
    \DiscountedPayoff_\lambda(\play)
    &=
      (1-\lambda)\sum_{i=0}^{k-1}\lambda^i
      \underbrace{w_i}_{\makebox[0pt][c]{\scriptsize$\geq -W$}}
      +
      (1-\lambda)\lambda^k\sum_{m=0}^\infty
      \lambda^{(\ell-k+1)m} \sum_{i=0}^{\ell-k}\lambda^iw_{k+i}\\
    & \geq -(1-\lambda^k)W +
      \frac{(1-\lambda) \lambda^k}{1-\lambda^{\ell-k+1}}
      \sum_{i=0}^{\ell-k}\lambda^iw_{k+i} \tag*{\eqref{4-eq:1}}
  \end{align*}
  By shifting all weights by $W$, we can rewrite the remaining
  sum as:
  

$$\sum_{i=0}^{\ell-k}\lambda^iw_{k+i} =
    \sum_{i=0}^{\ell-k}\lambda^i(w_{k+i}+W) -
    W\sum_{i=0}^{\ell-k}\lambda^i$$

  By using the fact that $w_{k+i}+W$ is non-negative and
  $\lambda^i\geq \lambda^{\ell-k}$, we obtain
  \begin{align*}
    \sum_{i=0}^{\ell-k}\lambda^iw_{k+i}
    &\geq \lambda^{\ell-k}
      \sum_{i=0}^{\ell-k}(w_{k+i}+W) -W
      \frac{1-\lambda^{\ell-k+1}}{1-\lambda} \\
    &= \lambda^{\ell-k}
      \sum_{i=0}^{\ell-k}w_{k+i} + (\ell-k+1)\lambda^{\ell-k}W
      -W \frac{1-\lambda^{\ell-k+1}}{1-\lambda}
  \end{align*}
  Therefore, since $\Value(v)=\frac 1 {\ell-k+1}\sum_{i=k}^\ell w_i$,
  we obtain
  

$$\sum_{i=0}^{\ell-k}\lambda^iw_{k+i}\geq
    \lambda^{\ell-k}(\ell-k+1)(\Value(v)+W)-
    W\frac{1-\lambda^{\ell-k+1}}{1-\lambda} \,.$$

  Simplifying~\cref{4-eq:1} gives:
  

$$\DiscountedPayoff_\lambda(\play)
    \geq -W+ \frac{(1-\lambda)(\ell-k+1)}{1-\lambda^{\ell-k+1}}
    \lambda^\ell (\Value(v) + W)$$

 Since
  $\frac {1-\lambda^{\ell-k+1}}{1-\lambda} =
  \sum_{i=0}^{\ell-k}\lambda^i < \ell-k+1$, and $\Value(v) + W\geq 0$
  (the mean payoff is an average of costs of the arena, so it is in
  the interval $[-W,W]$), we have
  

$$\DiscountedPayoff_\lambda(\play)
    \geq -W + \lambda^\ell (\Value(v) + W)$$

 Finally, notice that
  $\ell\leq n$, so that
  $\lambda^\ell\geq \lambda^{n}>(1-n(1-\lambda))$, using the fact
  that
  $\frac{1-\lambda^{n}}{1-\lambda} = \sum_{i=0}^{n-1}\lambda^i <
  n$. Therefore,
  \begin{align*}
    \DiscountedPayoff_\lambda(\play)
    &\geq -W + (1-n(1-\lambda)) (\Value(v) + W)\\
    &= -n(1-\lambda)(W+\Value(v)) + \Value(v)\\
    &\geq -2n(1-\lambda)W + \Value(v)
  \end{align*}
  by using again $\Value(v)\leq W$. We obtain
  

$$\Value_\lambda(v)-\Value(v)\geq -2n(1-\lambda)W$$

  as wanted, which allows us to conclude. 

```

Therefore, by picking $\lambda = 1-\frac 1{4n^2(n-1)W}$, we may
obtain a good enough approximation of the mean payoff optimal value,
by solving the associated discounted payoff game. From a complexity
point of view, this value iteration algorithm runs in polynomial time
with respect to the arena, but exponential with respect to the
representation of $\lambda$: here, it is therefore polynomial in
$4n^2(n-1)W$ which leads to a pseudopolynomial complexity to solve
mean payoff games. More precisely,

```{admonition} Theorem
:class: theorem
:name: 4-thm:MP-direct-value-iteration

  The direct value iteration algorithm computes the values of a
  mean payoff game in complexity $O(mn^3W)$.

```

As for discounted payoff game, a binary search also
permits to obtain optimal positional strategies for both players in
$\bigO\big(n^4m\log(m/n)W\big)$ time.

Notice that the previous encoding implies a better theoretical
complexity for mean payoff and parity games, that what we obtained
before:

```{admonition} Corollary
:class: corollary
:name: 4-col:UP

  Deciding the winner (with respect to a threshold) for mean payoff
  games, and deciding the winner for parity games, can be done in
  $\UP\cap\coUP$.

```

```{admonition} Proof
:class: dropdown tip

  The previous polynomial-time reduction from mean payoff to
  discounted payoff games allows to lift the $\UP\cap\coUP$ complexity
  of {ref}`Theorem <4-thm:disc-up>`. Moreover, the polynomial-time reduction
  of {ref}`Theorem <4-thm:parity2MP>` allows one to obtain the same complexity for
  parity games. 

```

