(2-sec:parity)=
# Parity games

```{math}

\renewcommand{\Game}{\game}

```

Recall that the parity objective extends B&uuml;chi and coB&uuml;chi objectives:

$$
 \mathtt{Parity} =  \left\{ \rho \in [1,d]^\omega \mid \text{ the largest priority appearing infinitely often in  \right\} \rho \text{ is even}}.
$$

````{prf:theorem} Positional determinacy and complexity of parity games
:label: 2-thm:parity

Parity objectives are uniformly positionally determined for both players.

```{margin}
See {prf:ref}`2-rmk:finite_infinite` for the case of infinite games.
```

There exists an algorithm for computing the winning regions of parity games in exponential time,
and more precisely of complexity $O(m n^d)$.
The space complexity of $O(nd)$.

Furthermore, solving parity games is in $NP \cap  coNP$.

````

To prove {prf:ref}`2-thm:parity` we first construct a recursive algorithm for computing the winning regions of parity games.
The algorithm is often called Zielonka's algorithm, or more accurately McNaughton Zielonka's algorithm.
We refer to the reference section Section {ref}`2-sec:references` for a discussion on this nomenclature.
We will see that the positionaly determinacy result for both players will be a consequence of the analysis of the algorithm.
The $NP \cap  coNP$ complexity bounds will be discussed at the end of this section.

The following lemma induces (half of) the recursive algorithm.
Identifying a colour and its set of vertices we write $d$ for the set of vertices of priority $d$.

````{prf:lemma} Fixed point characterisation of the winning regions for parity games
:label: 2-lem:zielonka_even

Let $\Game$ be a parity game with priorities in $[1,d]$, and $d$ even.
Let $\Game'$ be the subgame of $\Game$ induced by $V \setminus  Attr_\mathrm{Eve}(d)$.

*  If $W_\mathrm{Adam}(\Game') = \emptyset$, then $W_\mathrm{Eve}(\Game) = V$.
*  If $W_\mathrm{Adam}(\Game') \neq \emptyset$, 
let $\Game''$ be the subgame of $\Game$ induced by $V \setminus  Attr_\mathrm{Adam}(  W_\mathrm{Adam}(\Game') )$,
then $W_\mathrm{Eve}(\Game) =  W_\mathrm{Eve}(\Game'')$.

````

To see that this leads to a recursive algorithm, we note that $\Game'$ has priorities in $[1,d-1]$
and that if $W_\mathrm{Adam}(\Game') \neq \emptyset$, then $\Game''$ has less vertices than $\Game$.

````{admonition} Proof
:class: dropdown tip

We prove the first item. 

Let $\sigma_d$ be an attractor strategy ensuring to reach $d$ from $Attr_\mathrm{Eve}(d)$.
Consider a winning strategy for Eve from $V \setminus  Attr_\mathrm{Eve}(d)$ in $\Game'$, it induces a strategy $\sigma'$ in $\Game$.
We construct a strategy $\sigma$ in $\Game$ as the disjoint union of $\sigma_d$ on $Attr_\mathrm{Eve}(d)$ and of $\sigma'$ on $V \setminus  Attr_\mathrm{Eve}(d)$.
Any play consistent with $\sigma$ either enters $Attr_\mathrm{Eve}(d)$ infinitely many times, 
or eventually remains in $V \setminus  Attr_\mathrm{Eve}(d)$ and is eventually consistent with $\sigma'$.
In the first case it sees infinitely many times $d$, which is even and maximal, hence satisfies $\mathtt{Parity}$, 
and in the other case since $\sigma'$ is winning the play satisfies $\mathtt{Parity}$.
Thus $\sigma$ is winning from $V$.

We now look at the second item.

Let $\tau_a$ denote an attractor strategy 
from $Attr_\mathrm{Adam}( W_\mathrm{Adam}(\Game')) \setminus  W_\mathrm{Adam}(\Game')$.
Consider a winning strategy for Adam from $W_\mathrm{Adam}(\Game')$ in $\Game'$, it induces a strategy $\tau'$ in $\Game$.
Since $V \setminus  Attr_\mathrm{Eve}(d)$ is a trap for Eve, this implies that $\tau'$ is a winning strategy in $\Game$.
Consider now a winning strategy in the game $\Game''$ from $W_\mathrm{Adam}(\Game'')$, it induces a strategy $\tau''$ in $\Game$.
The set $V \setminus  Attr_\mathrm{Adam}(  W_\mathrm{Adam}(\Game') )$ may not be a trap for Eve, so we cannot conclude that $\tau''$ is a winning strategy in $\Game$,
and it indeed may not be.
We construct a strategy $\tau$ in $\Game$ as the (disjoint) union of the strategy $\tau_a$ on $Attr_\mathrm{Adam}( W_\mathrm{Adam}(\Game')) \setminus  W_\mathrm{Adam}(\Game')$,
the strategy $\tau'$ on $W_\mathrm{Adam}(\Game')$ and the strategy $\tau''$ on $W_\mathrm{Adam}(\Game'')$.
We argue that $\tau$ is winning from $Attr_\mathrm{Adam}(  W_\mathrm{Adam}(\Game') ) \cup  W_\mathrm{Adam}(\Game'')$ in $\Game$.
Indeed, any play consistent with this strategy in $\Game$ either stays forever in $W_\mathrm{Adam}(\Game'')$ hence is consistent with $\tau''$
or enters $Attr_\mathrm{Adam}(  W_\mathrm{Adam}(\Game') )$, hence is eventually consistent with $\tau'$.
In both cases this implies that the play is winning.
Thus we have proved that $Attr_\mathrm{Adam}(  W_\mathrm{Adam}(\Game') ) \cup  W_\mathrm{Adam}(\Game'') \subseteq  W_\mathrm{Adam}(\Game)$.

We now show that $W_\mathrm{Eve}(\Game'') \subseteq  W_\mathrm{Eve}(\Game)$, which implies the converse inclusion.
Consider a winning strategy from $W_\mathrm{Eve}(\Game'')$ in $\Game''$, it induces a strategy $\sigma$ in $\Game$.
Since $\Game''$ is a trap for Adam, any play consistent with $\sigma$ stays forever in $W_\mathrm{Eve}(\Game'')$, 
implying that $\sigma$ is winning from $W_\mathrm{Eve}(\Game'')$ in $\Game$.

````

To get the full algorithm we need the analogous lemma for the case where the maximal priority is odd.
We do not prove the following lemma as it is the exact dual of the previous lemma, and the proof is the same swapping the two players.

````{prf:lemma} Dual fixed point characterisation of the winning regions for parity games
:label: 2-lem:zielonka_odd

Let $\Game$ be a parity game with priorities in $[1,d]$, and $d$ odd.
Let $\Game'$ be the subgame of $\Game$ induced by $V \setminus  Attr_\mathrm{Adam}(d)$.

*  If $W_\mathrm{Eve}(\Game') = \emptyset$, then $W_\mathrm{Adam}(\Game) = V$.
*  If $W_\mathrm{Eve}(\Game') \neq \emptyset$, let $\Game''$ be the subgame of $\Game$ induced by $V \setminus  Attr_\mathrm{Eve}(  W_\mathrm{Eve}(\Game') )$,
then $W_\mathrm{Adam}(\Game) =  W_\mathrm{Adam}(\Game'')$.

````

The algorithm is presented in pseudocode in {numref}`2-algo:zielonka`.

The proofs of {prf:ref}`2-lem:zielonka_even` and {prf:ref}`2-lem:zielonka_odd` also imply that parity games are positionally determined for both players.
Indeed, winning strategies are defined as disjoint unions of strategies constructed inductively.

We now perform a complexity analysis.
We write $f(n,d)$ for the number of recursive calls performed by the algorithm on parity games with $n$ vertices and priorities in $[1,d]$.
We have $f(n,1) = 0 = f(0,d) = 0$, with the general induction:

$$
f(n,d) \le f(n,d-1) + f(n-1,d) + 2.
$$

The term $f(n,d-1)$ corresponds to the recursive call to $\Game'$, 
the term $f(n-1,d)$ to the recursive call to $\Game''$.
We obtain $f(n,d) \le n \cdot f(n,d-1) + 2n$,
so $f(n,d) \le 2(n + n^2 + \dots + n^{d-1}) = O(n^d)$.
In each recursive call we perform two attractor computations so the number of operations
in one recursive call is $O(m)$.
Thus the overall time complexity is $O(m n^d)$.

We finish the proof of {prf:ref}`2-thm:parity` by sketching the argument that solving parity games is in $NP \cap  coNP$.
The first observation is that computing the winning regions of the one player variants of parity games can be done in polynomial time
through a simple graph analysis that we do not detail here.
The $NP$ and $coNP$ algorithms are the following: guess a winning positional strategy,
and check whether it is winning by computing the winning regions of the one player game induced by the strategy.
Guessing a strategy for Eve is a witness that the answer is yes so it yields an $NP$ algorithm,
and guessing a strategy for Adam yields a $coNP$ algorithm.

Chapter {ref}`3-chap:parity` is devoted to the study of advanced algorithms for parity games.

```{figure} ./../FigAndAlgos/2-algo:zielonka.png
:name: 2-algo:zielonka
:align: center
A recursive algorithm for computing the winning regions of parity games.
```
