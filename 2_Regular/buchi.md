(2-sec:buchi)=
# B&uuml;chi games

Recall that the objective $\mathtt{Buchi}$ requires that the colour $\textrm{Win}$ appears infinitely many times
and $\mathtt{CoBuchi}$ requires that the colour $\textrm{Lose}$ appears finitely many times.

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

Let $\mathcal{G}$ be a B&uuml;chi game.

*  If $\textrm{Attr}_\mathrm{Eve}( \textrm{Win}) = V$, then $W_\mathrm{Eve}(  \mathcal{G}) = V$.
*  If $\textrm{Attr}_\mathrm{Eve}( \textrm{Win}) \neq V$, 
let $\mathcal{G}'$ be the subgame of $\mathcal{G}$ induced by $V \setminus  \textrm{Attr}_\mathrm{Adam}( V \setminus  \textrm{Attr}_\mathrm{Eve}( \textrm{Win}) )$,
then $W_\mathrm{Eve}(  \mathcal{G}) =  W_\mathrm{Eve}(  \mathcal{G}')$.

````

````{admonition} Proof
:class: dropdown tip

We prove the first item. 

Let $\sigma_a$ be an attractor strategy ensuring to reach $\textrm{Win}$ from $\textrm{Attr}_\mathrm{Eve}( \textrm{Win})$, and $\sigma_p$ any (positional) strategy from $\textrm{Win}$.
We construct the strategy $\sigma$ as the disjoint union of $\sigma_a$ and $\sigma_p$:

$$
\sigma(v) = 
\begin{cases}
\sigma_a(v) & \text{ if } v \in  \textrm{Attr}_\mathrm{Eve}( \textrm{Win}) \setminus  \textrm{Win}, \\
\sigma_p(v) & \text{ if } v \in  \textrm{Win}.
\end{cases}
$$

Note that $\sigma$ is positional.
We argue that $\sigma$ ensures $\mathtt{Buchi}[ \textrm{Win}]$.
Indeed a play consistent with $\sigma$ can be divided into infinitely many finite plays,
each of them consistent with $\sigma_a$ until reaching $\textrm{Win}$,
then one step consistent with $\sigma_p$.
Thus $\sigma$ is winning from $V$.

We now look at the second item.

We first prove that $\textrm{Attr}_\mathrm{Adam}(V \setminus  \textrm{Attr}_\mathrm{Eve}( \textrm{Win})) \subseteq  W_\mathrm{Adam}(  \mathcal{G})$.
Let $\tau_a$ denote an attractor strategy ensuring to reach $V \setminus  \textrm{Attr}_\mathrm{Eve}( \textrm{Win})$ from $\textrm{Attr}_\mathrm{Adam}(V \setminus  \textrm{Attr}_\mathrm{Eve}( \textrm{Win}))$,
and $\tau_c$ a counter-attractor strategy ensuring to stay in $V \setminus  \textrm{Attr}_\mathrm{Eve}( \textrm{Win})$ hence in never to reach $\textrm{Win}$.
We construct the strategy $\tau$ as the disjoint union of $\tau_a$ and $\tau_c$:

$$
\tau(v) = 
\begin{cases}
\tau_a(v) & \text{ if } v \in  \textrm{Attr}_\mathrm{Adam}(V \setminus  \textrm{Attr}_\mathrm{Eve}( \textrm{Win})) \setminus (V \setminus  \textrm{Attr}_\mathrm{Eve}( \textrm{Win})), \\
\tau_c(v) & \text{ if } v \in V \setminus  \textrm{Attr}_\mathrm{Eve}( \textrm{Win}).
\end{cases}
$$

Note that $\tau$ is positional.
Any play consistent with $\tau$ is first consistent with $\tau_a$ until reaching $V \setminus  \textrm{Attr}_\mathrm{Eve}( \textrm{Win})$ and 
then is consistent with $\tau_c$ and stays there forever.
In this second phase it in particular does not visit $\textrm{Win}$, 
implying that the play visits $\textrm{Win}$ finitely many times, so it is winning.
Thus we have proved that $\textrm{Attr}_\mathrm{Adam}(V \setminus  \textrm{Attr}_\mathrm{Eve}( \textrm{Win})) \subseteq  W_\mathrm{Adam}(  \mathcal{G})$,
implying $W_\mathrm{Eve}(  \mathcal{G}) \subseteq V \setminus  \textrm{Attr}_\mathrm{Adam}(V \setminus  \textrm{Attr}_\mathrm{Eve}( \textrm{Win}))$.

We now show that $W_\mathrm{Eve}(  \mathcal{G}') \subseteq  W_\mathrm{Eve}(  \mathcal{G})$, which implies the converse inclusion.
Consider a winning strategy from $W_\mathrm{Eve}(  \mathcal{G}')$ in $\mathcal{G}'$, it induces a strategy $\sigma$ in $\mathcal{G}$.
Since $\mathcal{G}'$ is a trap for Adam, any play consistent with $\sigma$ stays forever in $W_\mathrm{Eve}(  \mathcal{G}')$, 
implying that $\sigma$ is winning from $W_\mathrm{Eve}(  \mathcal{G}')$ in $\mathcal{G}$.

````

The algorithm is presented in pseudocode in {numref}`2-algo:Buchi_first`.
For the complexity analysis, the algorithm performs at most $n$ recursive calls
and each of them involves two attractor computations, implying the time complexity $O(mn)$.

```{figure} ./../FigAndAlgos/2-algo:Buchi_first.png
:name: 2-algo:Buchi_first
:align: center
The first quadratic time algorithm for solving B{\uchi} games.
```

## A second algorithm

The following lemma induces a different algorithm, it also implies {prf:ref}`2-thm:Buchi`.

````{prf:lemma} Second fixed point characterisation of the winning region for Buchi games
:label: 2-lem:Buchi

Let $\mathcal{G}$ a B&uuml;chi game.
Then $W_\mathrm{Eve}( \mathcal{G})$ is the greatest fixed point of the monotonic operator

$$
Y \mapsto  \textrm{Attr}_\mathrm{Eve} \left(  \textrm{Win} \cap  \textrm{Pre}_\mathrm{Eve}(Y) \right).
$$

````

````{admonition} Proof
:class: dropdown tip

Thanks to {prf:ref}`1-thm:kleene` the fixed point computation is realised by setting $Y_0 = V$
and $Y_{k+1} = Y_k \cap  \textrm{Attr}_\mathrm{Eve} \left( \textrm{Win} \cap  \textrm{Pre}_\mathrm{Eve}(Y_k) \right)$.
This constructs a non-increasing sequence $(Y_k)_{k \in  \mathbb{N}}$ of subsets of $V$
satisfying the property:
\begin{center}
If $Y_k = Y_{k+1}$, then $Y_{k+1} = Y_{k+2}$.
\end{center}
It follows that the sequence stabilises after at most $n-1$ steps, i.e. $Y_{n-1} = Y_n$.
We let $Y$ denote the fixed point, and note that $Y =  \textrm{Attr}_\mathrm{Eve}( \textrm{Win} \cap  \textrm{Pre}_\mathrm{Eve}(Y))$.

We first show that $Y \subseteq  W_\mathrm{Eve}( \mathcal{G})$. 
Let $\sigma_a$ be an attractor strategy ensuring to reach $\textrm{Win} \cap  \textrm{Pre}_\mathrm{Eve}(Y)$ from $Y$.
We also define a positional strategy $\sigma_p$:
for $v \in  V_\mathrm{Eve}$, if $v \in  \textrm{Pre}_\mathrm{Eve}(Y)$ there exists $(v,v') \in E$ such that $v' \in Y$, let us define $\sigma_p(v) = (v,v')$.

We define a positional strategy $\sigma$ as follows:

$$
\sigma(v) = 
\begin{cases}
\sigma_a(v) & \text{if } v \in  \textrm{Attr}_\mathrm{Eve}( \textrm{Win} \cap  \textrm{Pre}_\mathrm{Eve}(Y)) \setminus ( \textrm{Win} \cap  \textrm{Pre}_\mathrm{Eve}(Y)), \\
\sigma_p(v)& \text{if } v \in  \textrm{Win} \cap  \textrm{Pre}_\mathrm{Eve}(Y).
\end{cases}
$$

We argue that $\sigma$ ensures $\mathtt{Buchi}[ \textrm{Win}]$ from $Y$. 
Indeed a play consistent with $\sigma$ can be divided into infinitely many finite plays,
each of them consistent with $\sigma_a$ until reaching $\textrm{Win} \cap  \textrm{Pre}_\mathrm{Eve}(Y)$,
then one step consistent with $\sigma_p$ and leading to $Y$.

We now show that $W_\mathrm{Eve}( \mathcal{G}) \subseteq Y$.
For this we show $V \setminus Y \subseteq  W_\mathrm{Adam}( \mathcal{G})$.
For $v \in V \setminus Y$, the rank of $v$ is the smallest $k \in  \mathbb{N}$ such that $v \in V \setminus Y_k$.
Equivalently, $v \in Y_{k-1} \setminus Y_k$.
Note that no vertices have rank $0$.

Let $k \in  \mathbb{N}$. 
Let $\tau_{a,k}$ be a counter-attractor strategy ensuring from $V \setminus  \textrm{Attr}_\mathrm{Eve}( \textrm{Win} \cap  \textrm{Pre}_\mathrm{Eve}(Y_k))$
to stay in $V \setminus  \textrm{Attr}_\mathrm{Eve}( \textrm{Win} \cap  \textrm{Pre}_\mathrm{Eve}(Y_k))$ so in particular never to reach $\textrm{Win} \cap  \textrm{Pre}_\mathrm{Eve}(Y_k)$.
We also define a positional strategy $\tau_{p,k}$:
for $v \in  V_\mathrm{Adam}$ of rank $k+1$, if $v \in  \textrm{Win} \setminus  \textrm{Pre}_\mathrm{Eve}(Y_k)$ there exists $(v,v') \in E$ such that $v' \in V \setminus Y_k$
implying that the rank of $v'$ is at most $k$, let us define $\tau_{p,k}(v) = (v,v')$.

We construct the strategy $\tau$ as the disjoint union of all $\tau_{a,k}$ and $\tau_{p,k}$:

$$
\tau(v) = 
\begin{cases}
\tau_{a,k}(v) & \text{if } v \in (Y_k \setminus Y_{k+1}) \setminus  \textrm{Win}, \\
\tau_{p,k}(v) & \text{if } v \in  \textrm{Win} \cap (Y_k \setminus Y_{k+1}).
\end{cases}
$$

We argue that $\tau$ ensures $\mathtt{CoBuchi}[ \textrm{Win}]$. 
Consider a play consistent with $\tau$ starting from a vertex $v$ of rank $k+1$.
First, as long as the play is consistent with $\tau_{a,k}$, it remains in $V \setminus  \textrm{Attr}_\mathrm{Eve}( \textrm{Win} \cap  \textrm{Pre}_\mathrm{Eve}(Y_k))$
and the rank does not increase.
We distinguish two cases.
If the play never reaches $\textrm{Win}$, then it satisfies $\mathtt{CoBuchi}[ \textrm{Win}]$.
Otherwise it reaches $\textrm{Win}$, and then the next step is consistent with $\tau_{p,k}$ 
so the next vertex has rank at most $k$.
Thus along any play consistent with $\tau$, the rank never increases and each time a vertex in $\textrm{Win}$ is reached the rank decreases,
implying that it satisfies $\mathtt{CoBuchi}[ \textrm{Win}]$.

````

{prf:ref}`2-lem:Buchi` directly transfers to {numref}`2-algo:Buchi_second`.

```{figure} ./../FigAndAlgos/2-algo:Buchi_second.png
:name: 2-algo:Buchi_second
:align: center
The second quadratic time algorithm for solving B{\uchi} games.
```

````{prf:remark} NEEDS TITLE AND LABEL 
Both algorithms have the same complexity but they are not equivalent: the number of recursive calls of the first algorithm
may be strictly smaller than the number of iterations of the repeat loop in the second algorithm.
Both can be extended into (different) algorithms for parity games and beyond; in this chapter we will work with the first algorithm.

Both algorithms have the same complexity but they are not equivalent: the number of recursive calls of the first algorithm
may be strictly smaller than the number of iterations of the repeat loop in the second algorithm.
Both can be extended into (different) algorithms for parity games and beyond; in this chapter we will work with the first algorithm.

````
