(2-sec:buchi)=
# B&uuml;chi games

```{math}

\renewcommand{\Game}{\game}

```

Recall that the objective $\mathtt{Buchi}$ requires that the colour $Win$ appears infinitely many times
and $\mathtt{CoBuchi}$ requires that the colour $Lose$ appears finitely many times.

````{prf:theorem} Positional determinacy and complexity of Buchi games
:label: 2-thm:Buchi

B&uuml;chi objectives are uniformly positionally determined for both players.

```{margin}
See {prf:ref}`2-rmk:finite_infinite` for the case of infinite games.
```

There exists an algorithm for computing the winning regions of B&uuml;chi games in quadratic time, more precisely $O(mn)$,
and linear space, more precisely $O(m)$.

````

The first sentence implies that CoB&uuml;chi games are also uniformly positionally determined.
We present two different yet very similar algorithms.

## A first algorithm

The following lemma implies {prf:ref}`2-thm:Buchi`.

````{prf:lemma} Fixed point characterisation of the winning region for Buchi games
:label: 2-lem:Buchi_second

Let $\Game$ be a B&uuml;chi game.

*  If $Attr_\mathrm{Eve}( Win) = V$, then $W_\mathrm{Eve}(\Game) = V$.
*  If $Attr_\mathrm{Eve}( Win) \neq V$, 
let $\Game'$ be the subgame of $\Game$ induced by $V \setminus  Attr_\mathrm{Adam}( V \setminus  Attr_\mathrm{Eve}( Win) )$,
then $W_\mathrm{Eve}(\Game) =  W_\mathrm{Eve}(\Game')$.

````

````{admonition} Proof
:class: dropdown tip

We prove the first item. 

Let $\sigma_a$ be an attractor strategy ensuring to reach $Win$ from $Attr_\mathrm{Eve}( Win)$, and $\sigma_p$ any (positional) strategy from $Win$.
We construct the strategy $\sigma$ as the disjoint union of $\sigma_a$ and $\sigma_p$:

$$
\sigma(v) = 
\begin{cases}
\sigma_a(v) & \text{ if } v \in  Attr_\mathrm{Eve}( Win) \setminus  Win, \\
\sigma_p(v) & \text{ if } v \in  Win.
\end{cases}
$$

Note that $\sigma$ is positional.
We argue that $\sigma$ ensures $\mathtt{Buchi}[ Win]$.
Indeed a play consistent with $\sigma$ can be divided into infinitely many finite plays,
each of them consistent with $\sigma_a$ until reaching $Win$,
then one step consistent with $\sigma_p$.
Thus $\sigma$ is winning from $V$.

We now look at the second item.

We first prove that $Attr_\mathrm{Adam}(V \setminus  Attr_\mathrm{Eve}( Win)) \subseteq  W_\mathrm{Adam}(\Game)$.
Let $\tau_a$ denote an attractor strategy ensuring to reach $V \setminus  Attr_\mathrm{Eve}( Win)$ from $Attr_\mathrm{Adam}(V \setminus  Attr_\mathrm{Eve}( Win))$,
and $\tau_c$ a counter-attractor strategy ensuring to stay in $V \setminus  Attr_\mathrm{Eve}( Win)$ hence in never to reach $Win$.
We construct the strategy $\tau$ as the disjoint union of $\tau_a$ and $\tau_c$:

$$
\tau(v) = 
\begin{cases}
\tau_a(v) & \text{ if } v \in  Attr_\mathrm{Adam}(V \setminus  Attr_\mathrm{Eve}( Win)) \setminus (V \setminus  Attr_\mathrm{Eve}( Win)), \\
\tau_c(v) & \text{ if } v \in V \setminus  Attr_\mathrm{Eve}( Win).
\end{cases}
$$

Note that $\tau$ is positional.
Any play consistent with $\tau$ is first consistent with $\tau_a$ until reaching $V \setminus  Attr_\mathrm{Eve}( Win)$ and 
then is consistent with $\tau_c$ and stays there forever.
In this second phase it in particular does not visit $Win$, 
implying that the play visits $Win$ finitely many times, so it is winning.
Thus we have proved that $Attr_\mathrm{Adam}(V \setminus  Attr_\mathrm{Eve}( Win)) \subseteq  W_\mathrm{Adam}(\Game)$,
implying $W_\mathrm{Eve}(\Game) \subseteq V \setminus  Attr_\mathrm{Adam}(V \setminus  Attr_\mathrm{Eve}( Win))$.

We now show that $W_\mathrm{Eve}(\Game') \subseteq  W_\mathrm{Eve}(\Game)$, which implies the converse inclusion.
Consider a winning strategy from $W_\mathrm{Eve}(\Game')$ in $\Game'$, it induces a strategy $\sigma$ in $\Game$.
Since $\Game'$ is a trap for Adam, any play consistent with $\sigma$ stays forever in $W_\mathrm{Eve}(\Game')$, 
implying that $\sigma$ is winning from $W_\mathrm{Eve}(\Game')$ in $\Game$.

````

The algorithm is presented in pseudocode in {numref}`2-algo:Buchi_first`.
For the complexity analysis, the algorithm performs at most $n$ recursive calls
and each of them involves two attractor computations, implying the time complexity $O(mn)$.

```{figure} ./../FigAndAlgos/2-algo:Buchi_first.png
:name: 2-algo:Buchi_first
:align: center
The first quadratic time algorithm for solving B{\"uchi} games.
```

## A second algorithm

The following lemma induces a different algorithm, it also implies {prf:ref}`2-thm:Buchi`.

````{prf:lemma} Second fixed point characterisation of the winning region for Buchi games
:label: 2-lem:Buchi

Let $\mathcal{G}$ a B&uuml;chi game.
Then $W_\mathrm{Eve}( \mathcal{G})$ is the greatest fixed point of the monotonic operator

$$
Y \mapsto  Attr_\mathrm{Eve} \left(  Win \cap  Pre_\mathrm{Eve}(Y) \right).
$$

````

````{admonition} Proof
:class: dropdown tip

Thanks to {prf:ref}`1-thm:kleene` the fixed point computation is realised by setting $Y_0 = V$
and $Y_{k+1} = Y_k \cap  Attr_\mathrm{Eve} \left( Win \cap  Pre_\mathrm{Eve}(Y_k) \right)$.
This constructs a non-increasing sequence $(Y_k)_{k \in  \mathbb{N}}$ of subsets of $V$
satisfying the property:
\begin{center}
If $Y_k = Y_{k+1}$, then $Y_{k+1} = Y_{k+2}$.
\end{center}
It follows that the sequence stabilises after at most $n-1$ steps, i.e. $Y_{n-1} = Y_n$.
We let $Y$ denote the fixed point, and note that $Y =  Attr_\mathrm{Eve}( Win \cap  Pre_\mathrm{Eve}(Y))$.

We first show that $Y \subseteq  W_\mathrm{Eve}( \mathcal{G})$. 
Let $\sigma_a$ be an attractor strategy ensuring to reach $Win \cap  Pre_\mathrm{Eve}(Y)$ from $Y$.
We also define a positional strategy $\sigma_p$:
for $v \in  V_\mathrm{Eve}$, if $v \in  Pre_\mathrm{Eve}(Y)$ there exists $(v,v') \in E$ such that $v' \in Y$, let us define $\sigma_p(v) = (v,v')$.

We define a positional strategy $\sigma$ as follows:

$$
\sigma(v) = 
\begin{cases}
\sigma_a(v) & \text{if } v \in  Attr_\mathrm{Eve}( Win \cap  Pre_\mathrm{Eve}(Y)) \setminus ( Win \cap  Pre_\mathrm{Eve}(Y)), \\
\sigma_p(v)& \text{if } v \in  Win \cap  Pre_\mathrm{Eve}(Y).
\end{cases}
$$

We argue that $\sigma$ ensures $\mathtt{Buchi}[ Win]$ from $Y$. 
Indeed a play consistent with $\sigma$ can be divided into infinitely many finite plays,
each of them consistent with $\sigma_a$ until reaching $Win \cap  Pre_\mathrm{Eve}(Y)$,
then one step consistent with $\sigma_p$ and leading to $Y$.

We now show that $W_\mathrm{Eve}( \mathcal{G}) \subseteq Y$.
For this we show $V \setminus Y \subseteq  W_\mathrm{Adam}( \mathcal{G})$.
For $v \in V \setminus Y$, the rank of $v$ is the smallest $k \in  \mathbb{N}$ such that $v \in V \setminus Y_k$.
Equivalently, $v \in Y_{k-1} \setminus Y_k$.
Note that no vertices have rank $0$.

Let $k \in  \mathbb{N}$. 
Let $\tau_{a,k}$ be a counter-attractor strategy ensuring from $V \setminus  Attr_\mathrm{Eve}( Win \cap  Pre_\mathrm{Eve}(Y_k))$
to stay in $V \setminus  Attr_\mathrm{Eve}( Win \cap  Pre_\mathrm{Eve}(Y_k))$ so in particular never to reach $Win \cap  Pre_\mathrm{Eve}(Y_k)$.
We also define a positional strategy $\tau_{p,k}$:
for $v \in  V_\mathrm{Adam}$ of rank $k+1$, if $v \in  Win \setminus  Pre_\mathrm{Eve}(Y_k)$ there exists $(v,v') \in E$ such that $v' \in V \setminus Y_k$
implying that the rank of $v'$ is at most $k$, let us define $\tau_{p,k}(v) = (v,v')$.

We construct the strategy $\tau$ as the disjoint union of all $\tau_{a,k}$ and $\tau_{p,k}$:

$$
\tau(v) = 
\begin{cases}
\tau_{a,k}(v) & \text{if } v \in (Y_k \setminus Y_{k+1}) \setminus  Win, \\
\tau_{p,k}(v) & \text{if } v \in  Win \cap (Y_k \setminus Y_{k+1}).
\end{cases}
$$

We argue that $\tau$ ensures $\mathtt{CoBuchi}[ Win]$. 
Consider a play consistent with $\tau$ starting from a vertex $v$ of rank $k+1$.
First, as long as the play is consistent with $\tau_{a,k}$, it remains in $V \setminus  Attr_\mathrm{Eve}( Win \cap  Pre_\mathrm{Eve}(Y_k))$
and the rank does not increase.
We distinguish two cases.
If the play never reaches $Win$, then it satisfies $\mathtt{CoBuchi}[ Win]$.
Otherwise it reaches $Win$, and then the next step is consistent with $\tau_{p,k}$ 
so the next vertex has rank at most $k$.
Thus along any play consistent with $\tau$, the rank never increases and each time a vertex in $Win$ is reached the rank decreases,
implying that it satisfies $\mathtt{CoBuchi}[ Win]$.

````

{prf:ref}`2-lem:Buchi` directly transfers to {numref}`2-algo:Buchi_second`.

```{figure} ./../FigAndAlgos/2-algo:Buchi_second.png
:name: 2-algo:Buchi_second
:align: center
The second quadratic time algorithm for solving B{\"uchi} games.
```

````{prf:remark} NEEDS TITLE AND LABEL 
Both algorithms have the same complexity but they are not equivalent: the number of recursive calls of the first algorithm
may be strictly smaller than the number of iterations of the repeat loop in the second algorithm.
Both can be extended into (different) algorithms for parity games and beyond; in this chapter we will work with the first algorithm.

Both algorithms have the same complexity but they are not equivalent: the number of recursive calls of the first algorithm
may be strictly smaller than the number of iterations of the repeat loop in the second algorithm.
Both can be extended into (different) algorithms for parity games and beyond; in this chapter we will work with the first algorithm.

````
