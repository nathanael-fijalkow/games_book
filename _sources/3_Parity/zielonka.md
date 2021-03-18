(3-sec:zielonka)=
# A quasipolynomial time attractor decomposition algorithm

```{math}

\renewcommand{\H}{\mathcal{H}}

\renewcommand{\Game}{\game}

```

````{prf:theorem} Quasipolynomial McNaughton Zielonka algorithm
:label: 3-thm:quasipolynomial_mcnaughton_zielonka_algorithm

There exists a quasipolynomial time algorithm for solving parity games, and more specifically of complexity $n^{O(\log n)}$.

````

```{figure} ./../FigAndAlgos/3-algo:zielonka_even.png
:name: 3-algo:zielonka_even
:align: center
The recursive algorithm for computing the winning region of parity games.
```

We revisit the exponential recursive algorithm presented in Section {ref}`2-sec:parity`.
We refer to {numref}`3-algo:zielonka_even` for an equivalent presentation of this algorithm, 
where we make explicit all recursive calls involving the maximal priority $d$.
The benefit of doing this is to make the following observation:
during the $i$th recursive call for $d$, the algorithm removes from the game $\Game$ the subset 
$X_i =  \textrm{Attr}_\mathrm{Adam}^{\Game}(  W_\mathrm{Adam}(\Game_i) )$. 
Note that $X_i$ is a trap for Eve in $\Game$ and a subset of the winning region of Adam in $\Game$:
we say that $X_i$ is a dominion for Eve.
More generally, given a game $\Game$, a set $X$ of vertices is a dominion for Eve if
it is a trap for Adam and a subset of the winning region of Eve.

Let $i_{\infty}$ be the final value of $i$, the sets $X_0,\dots,X_{i_{\infty}-1}$ are disjoint.
The **key idea** is that this implies that at most one of them can have size more than half the total size.

To take advantage of this, we change the specification of the algorithm: 
the new algorithm takes as input a parity game and two parameters $s_{ \mathrm{Eve}}$ and $s_{ \mathrm{Adam}}$.
As before, they are two mutually recursive procedures, $\textsl{SolveE}$ and $\textsl{SolveA}$.
At an intuitive level, the objective of $\textsl{SolveE}(\Game,s_{ \mathrm{Eve}},s_{ \mathrm{Adam}})$ 
is to return a (non-empty whenever possible) dominion for Eve of size at most $s_{ \mathrm{Eve}}$.

We spell out the pseudocode of $\textsl{SolveE}$ in {numref}`3-algo:quasipoly_zielonka_even`, leaving out the perfectly symmetric $\textsl{SolveA}$.
The base cases are when there is only one priority, in which case Eve wins everywhere if the priority is even, and Adam wins everywhere if the priority is odd.

```{figure} ./../FigAndAlgos/3-algo:quasipoly_zielonka_even.png
:name: 3-algo:quasipoly_zielonka_even
:align: center
A recursive quasipolynomial algorithm for computing the winning regions of parity games -- the procedure $\textsl{SolveE}$.
```

We need three simple facts about traps.

````{prf:observation} Facts about traps
:label: 3-fact:traps

*  Let $S$ be a trap for Eve in the game $\Game$ and $X$ a set of vertices, 
then $S \setminus  \textrm{Attr}_\mathrm{Eve}(X)$ is a trapfor Eve in the subgame of $\Game$ induced by $V \setminus  \textrm{Attr}_\mathrm{Eve}(X)$.
*  Let $S$ be a trap for Eve in the game $\Game$ and $X$ a set of vertices such that $S \cap X = \emptyset$, 
then $S \subseteq V \setminus  \textrm{Attr}_\mathrm{Adam}(X)$ and $S$ is a trap for Eve in the subgame of $\Game$ induced by $V \setminus  \textrm{Attr}_\mathrm{Adam}(X)$.
*  Let $S$ be a trap for Eve in the game $\Game$ and $Z$ a trap for Eve in the subgame of $\Game$ induced by $S$,
then $Z$ is a trap for Eve in $\Game$.

````

The following lemma implies the correctness of the algorithm.

````{prf:lemma} Correctness of the quasipolynomial McNaughton Zielonka algorithm
:label: 3-lem:correctness_quasipoly_zielonka

*  For all dominions $S$ for Eve, if $|S| \le s_{ \mathrm{Eve}}$, then $S \subseteq \textsl{SolveE}(\Game,s_{ \mathrm{Eve}},s_{ \mathrm{Adam}})$.
*  For all dominions $S$ for Adam, if $|S| \le s_{ \mathrm{Adam}}$, then $S \cap \textsl{SolveE}(\Game,s_{ \mathrm{Eve}},s_{ \mathrm{Adam}}) = \emptyset$.

````

Indeed, $W_\mathrm{Eve}(\Game)$ and $W_\mathrm{Adam}(\Game)$ are dominions for Eve and Adam in $\Game$, 
so  {prf:ref}`3-lem:correctness_quasipoly_zielonka` implies that $\textsl{SolveE}(\Game,n,n) =  W_\mathrm{Eve}(\Game)$.

````{admonition} Proof
:class: dropdown tip

The proof is by induction on the number of priorities: indeed all recursive calls to $\textsl{SolveA}$ are for games with one less priority.
It follows that by induction hypothesis the following two properties hold, for all $i$.

*  For all dominions $S$ in $\Game_i$ for Adam, if $|S| \le s_{ \mathrm{Adam}}$, 
then 

$$ S \subseteq \textsl{SolveA}(\Game_i,s_{ \mathrm{Eve}},s_{ \mathrm{Adam}}). $$

*  For all dominions $S$ in $\Game_i$ for Eve, if $|S| \le s_{ \mathrm{Eve}}$, 
then 

$$ S \cap \textsl{SolveA}(\Game_i,s_{ \mathrm{Eve}},s_{ \mathrm{Adam}}) = \emptyset. $$

Since there will be an induction inside this induction, we refer to the induction above as the external induction,
and the second one as the internal induction.

We write $i_{\infty}$ for the final value of $i$, **i.e.** such that 
$\textsl{SolveE}(\Game,s_{ \mathrm{Eve}},s_{ \mathrm{Adam}}) = V_{i_{\infty}}$.
Note that the first item reads $S \subseteq V_{i_{\infty}}$.

Let $S$ be a dominion for Eve in $\Game$ such that $|S| \le s_{ \mathrm{Eve}}$.
We show by internal induction on $i$ that 
$S \subseteq V_i$.

For $i = 0$ this is by definition.
We now assume that $S \subseteq V_i$.
Recall that $\Game_i$ is the subgame of $\H_i$ induced by $V_i \setminus  \textrm{Attr}_\mathrm{Eve}^{\H_i}(d)$.
It follows from the first item of \cref{3-fact:traps} that $S \setminus  \textrm{Attr}_\mathrm{Eve}^{\H_i}(d)$
is a dominion for Eve in $\Game_i$.
Since $S \setminus  \textrm{Attr}_\mathrm{Eve}^{\H_i}(d)$ has size at most $s_{ \mathrm{Eve}}$, 
the second item of the external induction hypothesis implies that 
$S \setminus  \textrm{Attr}_\mathrm{Eve}^{\Game_i}(d)$ has an empty intersection with $X_i = \textsl{SolveA}(\Game_i,s_{ \mathrm{Eve}},s_{ \mathrm{Adam}})$,
implying that $S \cap X_i = \emptyset$.
It follows from the second item of \cref{3-fact:traps} that $S \subseteq V_i \setminus  \textrm{Attr}_\mathrm{Adam}^{\H_i}(X_i) = V_{i+1}$.
This finishes the internal induction, and implies the first item.

We now prove the second item.

Let $S$ be a (non-empty) dominion for Adam in $\Game$ such that $|S| \le s_{ \mathrm{Adam}}$.
We write $S_i = S \cap V_i$.
Note that the second item reads $S_{i_{\infty}} = \emptyset$.

We first show by internal induction on $i$ that 
$S_i$ is a dominion for Adam in $\H_i$.
For $i = 0$ this is by definition.
We now assume that $S_i$ is a dominion for Adam in $\H_i$.
Recall that $\H_{i+1}$ is the subgame of $\H_i$ induced by $V_{i+1} = V_i \setminus  \textrm{Attr}_\mathrm{Adam}^{\H_i}(X_i)$.
It follows from the first item of \cref{3-fact:traps} applied to $S_i$ (swapping the roles of Eve and Adam) 
that $S_i \setminus  \textrm{Attr}_\mathrm{Adam}^{\H_i}(X_i) = S_{i+1}$ is a dominion for Adam in $\H_{i+1}$.
This finishes the internal induction.

We showed that $S_i$ is a dominion for Adam in $\H_i$ for each $i$.
To apply the external inductive hypothesis, we need to exhibit dominions for Adam in $\Game_i$ for each $i$.
We consider $\H'_i$ the subgame of $\H_i$ induced by $S_i$.
Let $Z_i =  W_\mathrm{Adam}^{\H'_i}( \mathtt{Parity} \cup  \mathtt{Reach}(d))$: 
in words, $Z_i$ is the subset of vertices of $S_i$ from where Adam can ensure that the parity objective is not satisfied
and never to see priority $d$.
We prove two properties:

*  If $Z_i = \emptyset$, then $S_i = \emptyset$.

The fact that $Z_i$ is empty implies that Eve has a strategy $\sigma$ in $\Game_i$ which from $S_i$ ensures $\mathtt{Parity}$ or to see priority $d$.
Since $S_i$ is a dominion for Adam in $\H_i$, there exists a strategy $\tau$ for Adam which from $S_i$ ensures the complement of $\mathtt{Parity}$
and to stay in $S_i$. 
Playing $\sigma$ against $\tau$ yields a contradiction, since $\sigma$ ensures $\mathtt{Parity}$ if the play remains in $S_i$.

*  $Z_i$ is a dominion for Adam in $\Game_i$.

That $Z_i$ is a subset of the winning region of Adam in $\Game_i$ is clear.
To see that $Z_i$ is a trap for Eve in $\Game_i$, we first note that since $S_i$ is a trap for Eve in $\H_i$
and $Z_i$ is a trap for Eve in $\H'_i$, the subgame of $\H_i$ induced by $S_i$, 
then $Z_i$ is a trap in $\H_i$ by the third item of \cref{3-fact:traps}.
Now, since $Z_i$ has an empty intersection with $d$, by the second item of \cref{3-fact:traps} 
this implies that $Z_i$ is a trap for Eve in the subgame of $\H_i$ induced by $V_i \setminus  \textrm{Attr}_\mathrm{Eve}^{\H_i}(d)$,
which is exactly $\Game_i$.

We are now fully equipped to prove that $S_{i_{\infty}} = \emptyset$.
Let $i_{\ell}$ be the value of $i$ for which the algorithm performs a recursive call for a large dominion.
Since the sequence $(S_i)_i$ is non-increasing, if $S_i$ is empty for some $i$, then $S_{i_{\infty}}$ as well.

The first while loop was exited for $i = i_{\ell}$, implying that

$$
\textsl{SolveA}(\Game_{i_{\ell}},s_{ \mathrm{Eve}},\lfloor s_{ \mathrm{Adam}} / 2 \rfloor) = \emptyset.
$$

We apply the external inductive hypothesis to the dominion $Z_{i_{\ell}}$ for Adam in $\Game_{i_{\ell}}$
for the parameter $\lfloor s_{ \mathrm{Adam}} / 2 \rfloor$: if $|Z_{i_{\ell}}| \le \lfloor s_{ \mathrm{Adam}} / 2 \rfloor$, then
$Z_{i_{\ell}} \subseteq \textsl{SolveA}(\Game_{i_{\ell}},s_{ \mathrm{Eve}},\lfloor s_{ \mathrm{Adam}} / 2 \rfloor)$,
implying that $Z_{i_{\ell}}$ is empty, which by the first property above implies that $S_{i_{\ell}}$ is empty,
thus $S_{i_{\infty}}$ as well, proving the second item of  {prf:ref}`3-lem:correctness_quasipoly_zielonka`.
Excluding this case, we then analyse the situation where 
$|Z_{i_{\ell}}| > \lfloor s_{ \mathrm{Adam}} / 2 \rfloor$. 

We apply again the external inductive hypothesis to $Z_{i_\ell}$, but this time 
for the parameter $s_{ \mathrm{Adam}}$: 
if $|Z_{i_\ell}| \le s_{ \mathrm{Adam}}$, then $Z_{i_\ell} \subseteq X_{i_\ell}$.
Since $Z_{i_\ell} \subseteq S_{i_\ell} \subseteq S$ and $|S| \le s_{ \mathrm{Adam}}$, the premise is satisfied,
so $Z_{i_\ell} \subseteq X_{i_\ell}$.
Since $Z_{i_\ell}$ is non-empty, so is $X_{i_\ell}$: the search for a large dominion was successful, and in particular
$i$ is incremented at this stage, implying that $i_\ell < i_\infty$.

Consider $S_{i_\ell + 1} = S_{i_\ell} \setminus  \textrm{Attr}_\mathrm{Adam}^{\H_{i_\ell}}(X_{i_\ell})$.
In particular $S_{i_\ell + 1} \subseteq S_{i_\ell} \setminus X_{i_\ell} \subseteq S_{i_\ell} \setminus Z_{i_\ell}$, so

$$
|S_{i_\ell + 1}| \le |S_{i_\ell}| - |Z_{i_\ell}| \le \lfloor s_{ \mathrm{Adam}} / 2 \rfloor.
$$

The second while loop was exited for $i = i_{\infty}$, implying that

$$
\textsl{SolveA}(\Game_{i_{\infty}},s_{ \mathrm{Eve}},\lfloor s_{ \mathrm{Adam}} / 2 \rfloor) = \emptyset.
$$

We apply the external inductive hypothesis to the dominion $Z_{i_{\infty}}$ for Adam in $\Game_{i_{\infty}}$
for the parameter $\lfloor s_{ \mathrm{Adam}} / 2 \rfloor$: if $|Z_{i_{\infty}}| \le \lfloor s_{ \mathrm{Adam}} / 2 \rfloor$, then
$Z_{i_{\infty}} \subseteq \textsl{SolveA}(\Game_{i_{\infty}},s_{ \mathrm{Eve}},\lfloor s_{ \mathrm{Adam}} / 2 \rfloor)$.
The premise holds because $|S_{i_\ell + 1}| \le \lfloor s_{ \mathrm{Adam}} / 2 \rfloor$, the sequence $(S_i)_i$ is non-increasing, 
$i_\ell < i_\infty$, and $Z_{i_{\infty}} \subseteq S_{i_\infty}$.
Hence $Z_{i_\infty}$ is empty. Thanks to the first property above for $Z_i$, this implies that $S_{i_\infty}$ is empty.
This finishes the proof of the second item of  {prf:ref}`3-lem:correctness_quasipoly_zielonka`.

````

We obtain an algorithm for computing the winning regions of parity games using $\textsl{SolveE}(\Game,n,n)$,
where $\Game$ is a parity game with $n$ vertices.

We now perform a complexity analysis.
Let us write $f(m,n,d,s_{ \mathrm{Eve}},s_{ \mathrm{Adam}})$ for the complexity of the algorithm over parity games with $m$ edges, $n$ vertices, $d$ priorities,
and parameters $s_{ \mathrm{Eve}}$ and $s_{ \mathrm{Adam}}$.
We have $f(m,n,1,s_{ \mathrm{Eve}},s_{ \mathrm{Adam}}) = O(n)$ and $f(m,0,d,s_{ \mathrm{Eve}},s_{ \mathrm{Adam}}) = f(m,n,d,0,s_{ \mathrm{Adam}}) = f(m,n,d,s_{ \mathrm{Eve}},0) = O(1)$, 
with the general induction

$$
\begin{array}{lll}
f(m,n,d,s_{ \mathrm{Eve}},s_{ \mathrm{Adam}}) & \le & n \cdot f(m,n,d-1,s_{ \mathrm{Eve}},\lfloor s_{ \mathrm{Adam}} / 2 \rfloor) \\
  & & +\ f(m,n,d-1,s_{ \mathrm{Eve}},s_{ \mathrm{Adam}}) \\
  & & +\ O(nm).
\end{array}
$$

The term $n \cdot f(m,n,d-1,s_{ \mathrm{Eve}},\lfloor s_{ \mathrm{Adam}} / 2 \rfloor)$ corresponds to the recursive calls for small dominions, 
the term $f(m,n,d-1,s_{ \mathrm{Eve}},s_{ \mathrm{Adam}})$ to the recursive call for a large dominion,
and $O(nm)$ for the computation of the attractors.
We obtain

$$
f(m,n,d,n,n) \le m \cdot n^{1 + 2 \lfloor \log n \rfloor} \cdot \binom{d + 2 \lfloor \log n \rfloor}{2 \lfloor \log n \rfloor}.
$$

which implies a quasipolynomial upper bound of $n^{O(\log n)}$.
