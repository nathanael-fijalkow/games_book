(2-sec:parity)=
# An exponential time algorithm for parity games

Recall that the parity objective extends B&uuml;chi and coB&uuml;chi objectives:

$$

\Parity = \set{\rho \in [1,d]^\omega \mid \text{ the largest priority appearing infinitely often in } \rho \text{ is even}}.

$$



```{admonition} Theorem
:class: theorem
:name: 2-thm:parity

Parity objectives are uniformly positionally determined for both players\footnote{See \cref{2-rmk:finite_infinite} for the case of infinite games.}.
There exists an algorithm for computing the winning regions of parity games in exponential time,
and more precisely of complexity $O(m n^d)$.
The space complexity of $O(nd)$.

Furthermore, solving parity games is in $\NP \cap \coNP$.

```

To prove  {ref}`Theorem <2-thm:parity>` we first construct a recursive algorithm for computing the winning regions of parity games.
The algorithm is often called Zielonka's algorithm, or more accurately McNaughton Zielonka's algorithm.
We refer to the reference section {ref}`Section <2-sec:references>` for a discussion on this nomenclature.
We will see that the positionaly determinacy result for both players will be a consequence of the analysis of the algorithm.
The $\NP \cap \coNP$ complexity bounds will be discussed at the end of this section.

The following lemma induces (half of) the recursive algorithm.
Identifying a colour and its set of vertices we write $d$ for the set of vertices of priority $d$.

```{admonition} Lemma
:class: lemma
:name: 2-lem:zielonka_even

Let $\Game$ be a parity game with priorities in $[1,d]$, and $d$ even.
Let $\Game'$ be the subgame of $\Game$ induced by $V \setminus \AttrE(d)$.

*  If $\WA(\Game') = \emptyset$, then $\WE(\Game) = V$.
*  If $\WA(\Game') \neq \emptyset$, 
let $\Game''$ be the subgame of $\Game$ induced by $V \setminus \AttrA( \WA(\Game') )$,
then $\WE(\Game) = \WE(\Game'')$.

```

To see that this leads to a recursive algorithm, we note that $\Game'$ has priorities in $[1,d-1]$
and that if $\WA(\Game') \neq \emptyset$, then $\Game''$ has less vertices than $\Game$.



```{admonition} Proof
:class: dropdown tip

We prove the first item. 

Let $\sigma_d$ be an attractor strategy ensuring to reach $d$ from $\AttrE(d)$.
Consider a winning strategy for Eve from $V \setminus \AttrE(d)$ in $\Game'$, it induces a strategy $\sigma'$ in $\Game$.
We construct a strategy $\sigma$ in $\Game$ as the disjoint union of $\sigma_d$ on $\AttrE(d)$ and of $\sigma'$ on $V \setminus \AttrE(d)$.
Any play consistent with $\sigma$ either enters $\AttrE(d)$ infinitely many times, 
or eventually remains in $V \setminus \AttrE(d)$ and is eventually consistent with $\sigma'$.
In the first case it sees infinitely many times $d$, which is even and maximal, hence satisfies $\Parity$, 
and in the other case since $\sigma'$ is winning the play satisfies $\Parity$.
Thus $\sigma$ is winning from $V$.

We now look at the second item.

Let $\tau_a$ denote an attractor strategy from $\AttrA(\WA(\Game')) \setminus \WA(\Game')$.
Consider a winning strategy for Adam from $\WA(\Game')$ in $\Game'$, it induces a strategy $\tau'$ in $\Game$.
Since $V \setminus \AttrE(d)$ is a trap for Eve, this implies that $\tau'$ is a winning strategy in $\Game$.
Consider now a winning strategy in the game $\Game''$ from $\WA(\Game'')$, it induces a strategy $\tau''$ in $\Game$.
The set $V \setminus \AttrA( \WA(\Game') )$ may not be a trap for Eve, so we cannot conclude that $\tau''$ is a winning strategy in $\Game$,
and it indeed may not be.
We construct a strategy $\tau$ in $\Game$ as the (disjoint) union of the strategy $\tau_a$ on $\AttrA(\WA(\Game')) \setminus \WA(\Game')$,
the strategy $\tau'$ on $\WA(\Game')$ and the strategy $\tau''$ on $\WA(\Game'')$.
We argue that $\tau$ is winning from $\AttrA( \WA(\Game') ) \cup \WA(\Game'')$ in $\Game$.
Indeed, any play consistent with this strategy in $\Game$ either stays forever in $\WA(\Game'')$ hence is consistent with $\tau''$
or enters $\AttrA( \WA(\Game') )$, hence is eventually consistent with $\tau'$.
In both cases this implies that the play is winning.
Thus we have proved that $\AttrA( \WA(\Game') ) \cup \WA(\Game'') \subseteq \WA(\Game)$.

We now show that $\WE(\Game'') \subseteq \WE(\Game)$, which implies the converse inclusion.
Consider a winning strategy from $\WE(\Game'')$ in $\Game''$, it induces a strategy $\sigma$ in $\Game$.
Since $\Game''$ is a trap for Adam, any play consistent with $\sigma$ stays forever in $\WE(\Game'')$, 
implying that $\sigma$ is winning from $\WE(\Game'')$ in $\Game$.

```

To get the full algorithm we need the analogous lemma for the case where the maximal priority is odd.
We do not prove the following lemma as it is the exact dual of the previous lemma, and the proof is the same swapping the two players.

```{admonition} Lemma
:class: lemma
:name: 2-lem:zielonka_odd

Let $\Game$ be a parity game with priorities in $[1,d]$, and $d$ odd.
Let $\Game'$ be the subgame of $\Game$ induced by $V \setminus \AttrA(d)$.

*  If $\WE(\Game') = \emptyset$, then $\WA(\Game) = V$.
*  If $\WE(\Game') \neq \emptyset$, let $\Game''$ be the subgame of $\Game$ induced by $V \setminus \AttrE( \WE(\Game') )$,
then $\WA(\Game) = \WA(\Game'')$.

```

The algorithm is presented in pseudocode in  {ref}`Algorithm <2-algo:zielonka>`.

The proofs of  {ref}`Lemma <2-lem:zielonka_even>` and  {ref}`Lemma <2-lem:zielonka_odd>` also imply that parity games are positionally determined for both players.
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


We finish the proof of  {ref}`Theorem <2-thm:parity>` by sketching the argument that solving parity games is in $\NP \cap \coNP$.
The first observation is that computing the winning regions of the one player variants of parity games can be done in polynomial time
through a simple graph analysis that we do not detail here.
The $\NP$ and $\coNP$ algorithms are the following: guess a winning positional strategy,
and check whether it is winning by computing the winning regions of the one player game induced by the strategy.
Guessing a strategy for Eve is a witness that the answer is yes so it yields an $\NP$ algorithm,
and guessing a strategy for Adam yields a $\coNP$ algorithm.

{ref}`Chapter <3-chap:parity>` is devoted to the study of advanced algorithms for parity games.

\begin{algorithm}
 \KwData{A parity game $\Game$ with priorities in $[1,d]$}
 \SetKwFunction{FSolveEven}{SolveEven}
 \SetKwFunction{FSolveOdd}{SolveOdd}
 \SetKwProg{Fn}{Function}{:}{}
 \DontPrintSemicolon

\Fn{\FSolveEven{$\Game$}}{

Let $\Game'$ the subgame of $\Game$ induced by $V \setminus \AttrE(d)$

$X \leftarrow$ \FSolveOdd{$\Game'$}

\If{$X = \emptyset$}{\Return{$V$}}
\Else{
Let $\Game''$ the subgame of $\Game$ induced by $V \setminus \AttrA(X)$

\FSolveEven{$\Game''$}
}
}

\Fn{\FSolveOdd{$\Game$}}{
\If{$d = 1$}{\Return{$V$}}

Let $\Game'$ the subgame of $\Game$ induced by $V \setminus \AttrA(d)$

$X \leftarrow$ \FSolveEven{$\Game'$}

\If{$X = \emptyset$}{\Return{$V$}}
\Else{
Let $\Game''$ the subgame of $\Game$ induced by $V \setminus \AttrE(X)$

\FSolveOdd{$\Game''$}
}
}

\If{$d$ is even}{
\FSolveEven{$\Game$}
}
\Else{
\FSolveOdd{$\Game$}
}
\caption{A recursive algorithm for computing the winning regions of parity games.}
\label{2-algo:zielonka}
\end{algorithm}
