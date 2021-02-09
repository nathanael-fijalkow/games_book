(2-sec:buchi)=
# A quadratic time algorithm for B&uuml;chi games

Recall that the objective $\Buchi$ requires that the colour $\Win$ appears infinitely many times
and $\CoBuchi$ requires that the colour $\Lose$ appears finitely many times.

```{admonition} Theorem
:class: theorem
:name: 2-thm:Buchi

B&uuml;chi objectives are uniformly positionally determined for both players\footnote{See \cref{2-rmk:finite_infinite} for the case of infinite games.}.
There exists an algorithm for computing the winning regions of B&uuml;chi games in quadratic time, more precisely $O(mn)$,
and linear space, more precisely $O(m)$.

```

The first sentence implies that CoB&uuml;chi games are also uniformly positionally determined.
We present two different yet very similar algorithms. 

## A first algorithm

The following lemma implies  {ref}`Theorem <2-thm:Buchi>`.

```{admonition} Lemma
:class: lemma
:name: 2-lem:Buchi_second

Let $\Game$ be a B&uuml;chi game.

*  If $\AttrE(\Win) = V$, then $\WE(\Game) = V$.
*  If $\AttrE(\Win) \neq V$, 
let $\Game'$ be the subgame of $\Game$ induced by $V \setminus \AttrA( V \setminus \AttrE(\Win) )$,
then $\WE(\Game) = \WE(\Game')$.

```


```{admonition} Proof
:class: dropdown tip

We prove the first item. 

Let $\sigma_a$ be an attractor strategy ensuring to reach $\Win$ from $\AttrE(\Win)$, and $\sigma_p$ any (positional) strategy from $\Win$.
We construct the strategy $\sigma$ as the disjoint union of $\sigma_a$ and $\sigma_p$:

$$

\sigma(v) = 
\begin{cases}
\sigma_a(v) & \text{ if } v \in \AttrE(\Win) \setminus \Win, \\
\sigma_p(v) & \text{ if } v \in \Win.
\end{cases}

$$

Note that $\sigma$ is positional.
We argue that $\sigma$ ensures $\Buchi[\Win]$.
Indeed a play consistent with $\sigma$ can be divided into infinitely many finite plays,
each of them consistent with $\sigma_a$ until reaching $\Win$,
then one step consistent with $\sigma_p$.
Thus $\sigma$ is winning from $V$.

We now look at the second item.

We first prove that $\AttrA(V \setminus \AttrE(\Win)) \subseteq \WA(\Game)$.
Let $\tau_a$ denote an attractor strategy ensuring to reach $V \setminus \AttrE(\Win)$ from $\AttrA(V \setminus \AttrE(\Win))$,
and $\tau_c$ a counter-attractor strategy ensuring to stay in $V \setminus \AttrE(\Win)$ hence in never to reach $\Win$.
We construct the strategy $\tau$ as the disjoint union of $\tau_a$ and $\tau_c$:

$$

\tau(v) = 
\begin{cases}
\tau_a(v) & \text{ if } v \in \AttrA(V \setminus \AttrE(\Win)) \setminus (V \setminus \AttrE(\Win)), \\
\tau_c(v) & \text{ if } v \in V \setminus \AttrE(\Win).
\end{cases}

$$

Note that $\tau$ is positional.
Any play consistent with $\tau$ is first consistent with $\tau_a$ until reaching $V \setminus \AttrE(\Win)$ and 
then is consistent with $\tau_c$ and stays there forever.
In this second phase it in particular does not visit $\Win$, 
implying that the play visits $\Win$ finitely many times, so it is winning.
Thus we have proved that $\AttrA(V \setminus \AttrE(\Win)) \subseteq \WA(\Game)$,
implying $\WE(\Game) \subseteq V \setminus \AttrA(V \setminus \AttrE(\Win))$.

We now show that $\WE(\Game') \subseteq \WE(\Game)$, which implies the converse inclusion.
Consider a winning strategy from $\WE(\Game')$ in $\Game'$, it induces a strategy $\sigma$ in $\Game$.
Since $\Game'$ is a trap for Adam, any play consistent with $\sigma$ stays forever in $\WE(\Game')$, 
implying that $\sigma$ is winning from $\WE(\Game')$ in $\Game$.

```

The algorithm is presented in pseudocode in  {ref}`Algorithm <2-algo:Buchi_first>`.
For the complexity analysis, the algorithm performs at most $n$ recursive calls
and each of them involves two attractor computations, implying the time complexity $O(mn)$.

\begin{algorithm}
 \KwData{A B&uuml;chi game.}
 \SetKwFunction{FSolve}{Solve}
 \SetKwProg{Fn}{Function}{:}{}
 \DontPrintSemicolon

\Fn{\FSolve{$\Game$}}{
$X \leftarrow \AttrE(\Win)$

\If{$X = V$}{
\Return{$V$}
}
\Else{
Let $\Game'$ the subgame of $\Game$ induced by $V \setminus \AttrA(X)$

\Return{$\FSolve{$\Game'$}$}
}
}
\caption{The first quadratic time algorithm for solving B{\"uchi} games.}
\label{2-algo:Buchi_first}
\end{algorithm}

## A second algorithm

The following lemma induces a different algorithm, it also implies  {ref}`Theorem <2-thm:Buchi>`.

```{admonition} Lemma
:class: lemma
:name: 2-lem:Buchi

Let $\game$ a B&uuml;chi game.
Then $\WE(\game)$ is the greatest fixed point of the monotonic operator 

$$

Y \mapsto \AttrE \left( \Win \cap \PreE(Y) \right).

$$


```


```{admonition} Proof
:class: dropdown tip

Thanks to  {ref}`Theorem <1-thm:kleene>` the fixed point computation is realised by setting $Y_0 = V$
and $Y_{k+1} = Y_k \cap \AttrE \left(\Win \cap \PreE(Y_k) \right)$.
This constructs a non-increasing sequence $(Y_k)_{k \in \N}$ of subsets of $V$
satisfying the property:
\begin{center}
If $Y_k = Y_{k+1}$, then $Y_{k+1} = Y_{k+2}$.
\end{center}
It follows that the sequence stabilises after at most $n-1$ steps, i.e. $Y_{n-1} = Y_n$.
We let $Y$ denote the fixed point, and note that $Y = \AttrE(\Win \cap \PreE(Y))$.

We first show that $Y \subseteq \WE(\game)$. 
Let $\sigma_a$ be an attractor strategy ensuring to reach $\Win \cap \PreE(Y)$ from $Y$.
We also define a positional strategy $\sigma_p$:
for $v \in \VE$, if $v \in \PreE(Y)$ there exists $(v,v') \in E$ such that $v' \in Y$, let us define $\sigma_p(v) = (v,v')$.

We define a positional strategy $\sigma$ as follows:

$$

\sigma(v) = 
\begin{cases}
\sigma_a(v) & \text{if } v \in \AttrE(\Win \cap \PreE(Y)) \setminus (\Win \cap \PreE(Y)), \\
\sigma_p(v)& \text{if } v \in \Win \cap \PreE(Y).
\end{cases}

$$

We argue that $\sigma$ ensures $\Buchi[\Win]$ from $Y$. 
Indeed a play consistent with $\sigma$ can be divided into infinitely many finite plays,
each of them consistent with $\sigma_a$ until reaching $\Win \cap \PreE(Y)$,
then one step consistent with $\sigma_p$ and leading to $Y$.


We now show that $\WE(\game) \subseteq Y$.
For this we show $V \setminus Y \subseteq \WA(\game)$.
For $v \in V \setminus Y$, the rank of $v$ is the smallest $k \in \N$ such that $v \in V \setminus Y_k$.
Equivalently, $v \in Y_{k-1} \setminus Y_k$.
Note that no vertices have rank $0$.

Let $k \in \N$. 
Let $\tau_{a,k}$ be a counter-attractor strategy ensuring from $V \setminus \AttrE(\Win \cap \PreE(Y_k))$
to stay in $V \setminus \AttrE(\Win \cap \PreE(Y_k))$ so in particular never to reach $\Win \cap \PreE(Y_k)$.
We also define a positional strategy $\tau_{p,k}$:
for $v \in \VA$ of rank $k+1$, if $v \in \Win \setminus \PreE(Y_k)$ there exists $(v,v') \in E$ such that $v' \in V \setminus Y_k$
implying that the rank of $v'$ is at most $k$, let us define $\tau_{p,k}(v) = (v,v')$.

We construct the strategy $\tau$ as the disjoint union of all $\tau_{a,k}$ and $\tau_{p,k}$:

$$

\tau(v) = 
\begin{cases}
\tau_{a,k}(v) & \text{if } v \in (Y_k \setminus Y_{k+1}) \setminus \Win, \\
\tau_{p,k}(v) & \text{if } v \in \Win \cap (Y_k \setminus Y_{k+1}).
\end{cases}

$$

We argue that $\tau$ ensures $\CoBuchi[\Win]$. 
Consider a play consistent with $\tau$ starting from a vertex $v$ of rank $k+1$.
First, as long as the play is consistent with $\tau_{a,k}$, it remains in $V \setminus \AttrE(\Win \cap \PreE(Y_k))$
and the rank does not increase.
We distinguish two cases.
If the play never reaches $\Win$, then it satisfies $\CoBuchi[\Win]$.
Otherwise it reaches $\Win$, and then the next step is consistent with $\tau_{p,k}$ 
so the next vertex has rank at most $k$.
Thus along any play consistent with $\tau$, the rank never increases and each time a vertex in $\Win$ is reached the rank decreases,
implying that it satisfies $\CoBuchi[\Win]$.

```

{ref}`Lemma <2-lem:Buchi>` directly transfers to  {ref}`Algorithm <2-algo:Buchi_second>`.

\begin{algorithm}
 \KwData{A B&uuml;chi game.}

$Y_0 \leftarrow V$ 

$k \leftarrow 0$ 
     
\Repeat{$Y_{k+1} = Y_k$}{
$Y_{k+1} \leftarrow Y_k \cap \AttrE \left( \Win \cap \PreE(Y_k) \right)$ 

$k \leftarrow k + 1$
}

\Return{$Y_k$}
\caption{The second quadratic time algorithm for solving B{\"uchi} games.}
\label{2-algo:Buchi_second}
\end{algorithm}

```{admonition} Remark
:class: remark

Both algorithms have the same complexity but they are not equivalent: the number of recursive calls of the first algorithm
may be strictly smaller than the number of iterations of the repeat loop in the second algorithm.
Both can be extended into (different) algorithms for parity games and beyond; in this chapter we will work with the first algorithm.

```
