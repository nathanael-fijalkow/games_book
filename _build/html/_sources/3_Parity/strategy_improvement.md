(3-sec:strategy_improvement)=
# An exponential time strategy improvement algorithm

```{math}

\renewcommand{\H}{\mathcal{H}}

\renewcommand{\Game}{\game}

```

````{prf:theorem} NEEDS TITLE 3-thm:strategy_improvement
:label: 3-thm:strategy_improvement

There exists a strategy improvement algorithm for solving parity games in exponential time.

````

We rely on the high-level presentation of strategy improvement algorithms given in Section {ref}`1-sec:strategy_improvement`.
In a nutshell: the algorithm constructs a sequence of strategies, the next one being an improvement over the current one,
until reaching an optimal strategy.

> **Adding the option of stopping the game.**

Let $\mathcal{G}$ a parity game with priorities in $[1,d]$.
Let us give Eve an extra move $\mathtt{-}$ that indicates that the game should stop and that she can play from any vertex of hers.
So a strategy for Eve is now a function $\sigma :  V_\mathrm{Eve} \rightarrow E \cup  \left\{  \mathtt{- \right\}}$ 
where $\sigma(v) =  \mathtt{-}$ indicates that Eve has chosen to stop the game, and $\sigma(v) \ne  \mathtt{-}$ should be interpreted as normal.
Adam is not allowed to stop the game, so strategies for Adam remain unchanged.
We say that a play ending with $\mathtt{-}$ is stopped.

For reasoning it will be useful to consider the parity graph $\Game[\sigma]$ obtained from $\Game$ by restricting the outgoing edges from $V_\mathrm{Eve}$
to those prescribed by $\sigma$. 
Recall that we say that a parity graph (without stopping option) satisfies parity from $v$ if all infinite paths from $v$ satisfy parity.
Then a strategy $\sigma$ is winning from $v$ if and only if the parity graph $\Game[\sigma]$ satisfies parity from $v$.

Since we added the option for Eve to stop the game we introduce a new terminology: 
we say that a strategy $\sigma$ respects parity if all infinite plays consistent with $\sigma$ satisfy parity,
equivalently all infinite paths in $\Game[\sigma]$ satisfy parity, not requiring anything of stopped plays.

We say that a cycle is even if the maximal priority along the cycle is even, and it is odd otherwise. 
Respecting parity is characterised using cycles:

````{prf:observation} NEEDS TITLE AND LABEL 
A strategy $\sigma$ respects parity if and only if all cycles in $\Game[\sigma]$ are even.

A strategy $\sigma$ respects parity if and only if all cycles in $\Game[\sigma]$ are even.

````

The algorithm will only manipulate strategies respecting parity.

> **Evaluating a strategy.**

The first question is: given a strategy $\sigma$, how to evaluate it (in order to later improve it)?
As explained in Section {ref}`1-sec:strategy_improvement` towards this goal we define a value function $\textrm{val}^{\sigma} : V \to Y$.

We let $\textrm{val}^{\sigma}(v) = \min_\tau   \textrm{val}( \pi_{\sigma,\tau}^v)$ where $\tau$ ranges over (general) strategies for Adam, so we first need to define the value of the play $\pi =  \pi_{\sigma,\tau}^v$.
If $\pi$ is stopped, then $\textrm{val}( \pi)$ is the tuple $(p_1, p_2, \dots, p_d)$ where $p_i$ is the number of times that priority $p$ appears on the play.
Otherwise $\textrm{val}( \pi)$ is $\top$ if $\pi$ satisfies parity, and $\bot$ if $\pi$ does not satisfy parity.
So the value of a play is either $\top$, $\bot$, or a multiset of priorities;
we let $Y$ denote the (infinite) set consisting of these elements.

We define a total order $\le$ on $Y$ making it a complete lattice.
First, $\top$ is the greatest element and $\bot$ the least element.
For $t = (a_1, a_2, \dots, a_d)$ and $t' = (b_1, b_2, \dots, b_d)$,
we have that $t < t'$ if and only if $p$ is the largest index such that $t_p \ne t'_p$ and 

*  either $p$ is even and $t_p < t'_p$,
*  or $p$ is odd and $t_p > t'_p$.

Then $\le$ is the reflexive closure of $<$: we have $t \le t'$ if $t < t'$ or $t = t'$.

These conditions specify which priorities Eve likes to see along a play.
Given a choice, Eve would prefer to see even priorities and to avoid odd priorities, but these preferences are hierarchical: 
assuming that $d$ is even, Eve would like to see as many edges of priority $d$ as possible. 
If two plays see $d$ the same number of times, Eve prefers the play that visits the fewest vertices of
priority $d-1$, and if two plays see $d$ and $d-1$ the same number of times,
then Eve would like to maximise the number of times that $d-2$ is visited, and so on recursively.

> **The value function as a fixed point.**

We define $\delta : Y \times [1,d] \to Y$ by

$$
\delta(t,p) = 
\begin{cases}
(a_1, a_2, \dots, a_p + 1, a_{p+1}, \dots, a_d) & \text{ if } t = (a_1, a_2, \dots, a_d), \\
\top & \text{ if } t = \top, \\
\bot & \text{ if } t = \bot.
\end{cases}
$$

We note that $\delta$ is monotonic: for all $p \in [1,d]$,
if $t \le t'$ then $\delta(t,p) \le \delta(t',p)$. 
We extend $\delta$ to $\delta : Y \times [1,d]^* \to Y$.

We let $F^\sigma_V$ denote the set of functions $\mu : V \to Y$ such that $\mu(v) = \emptyset$ if $\sigma(v) =  \mathtt{-}$,
it is a lattice when equipped with the componentwise (partial) order induced by $Y$:
we say that $\mu \le \mu'$ if for all vertices $v$ we have $\mu(v) \le \mu'(v)$.
We then define an operator $\mathbb{O} : F^\sigma_V \to F^\sigma_V$ by

$$
 \mathbb{O}(\mu)(v) = 
\begin{cases}
\min  \left\{ \delta( \mu(v'),  \textsf{col \right\}(v)) : (v,v') \in E} & \text{if } \sigma(v) \neq  \mathtt{-} \\
\emptyset & \text{if } \sigma(v) =  \mathtt{-}.
\end{cases}
$$

Since $\delta$ is monotonic so is $\mathbb{O}$.

````{prf:observation} NEEDS TITLE AND LABEL 
The function $\textrm{val}^\sigma$ is a fixed point of $\mathbb{O}$ in $F^\sigma_V$.

The function $\textrm{val}^\sigma$ is a fixed point of $\mathbb{O}$ in $F^\sigma_V$.

````

Unfortunately, $\textrm{val}^{\sigma}$ is not in general the greatest fixed point of $\mathbb{O}$ in $F^\sigma_V$;
let us analyse this in more details.
Let $\mu$ a fixed point of $\mathbb{O}$ in $F^\sigma_V$, there are two cases. 
For a vertex $v$ such that there exists a stopped play $\pi$ starting from $v$, we have $\mu(v) \le   \textrm{val}(\pi)$, and more generally
$\mu(v) \le \inf_{\pi}   \textrm{val}(\pi)$ where $\pi$ ranges over all stopped plays starting from $v$.
The problem is for a vertex $v$ such that no plays starting from $v$ are stopped: 
we can have either $\mu(v) = \top$ or $\mu(v) = \bot$, irrespective of whether the play satisfies parity or not.
From this discussion we obtain the following result.

````{prf:lemma} NEEDS TITLE 3-lem:greatest_fixed_point
:label: 3-lem:greatest_fixed_point

If $\sigma$ respects parity, then $\textrm{val}^{\sigma}$ is the greatest fixed point of $\mathbb{O}$ in $F^\sigma_V$.

````

> **Improving a strategy.**

We reach the last item in the construction of the algorithm: the notion of switchable edges.
Let $\sigma$ a strategy. We say that an edge $e = (v,v')$ is switchable if

$$
\delta(  \textrm{val}^{\sigma}(v'), \textsf{col}(v)) > \delta(  \textrm{val}^{\sigma}(u), \textsf{col}(v)) \text{ where } \sigma(v) = (v,u).
$$

Intuitively: according to $\textrm{val}^{\sigma}$, playing $e$ is better than playing $\sigma(v)$.

Given a strategy $\sigma$ and an edge $e = (v,v')$ we use $\sigma[v \to e]$ to denote the strategy playing $e$ from $v$ 
and follow $\sigma$ from all other vertices.
Let us write $\sigma \le \sigma'$ if for all vertices $v$ we have $\textrm{val}^{\sigma}(v) \le   \textrm{val}^{\sigma'}(v)$,
and $\sigma < \sigma'$ if additionally $\neg (\sigma' \le \sigma)$.

> **The algorithm.**

The algorithm starts with a specified initial strategy, which is the strategy
$\sigma_0$ where $\sigma_0(v) =  \mathtt{-}$ for all vertices $v \in  V_\mathrm{Eve}$. 
It may not hold that $\sigma_0$ respects parity since $\mathcal{G}$ may contain odd cycles fully controlled by Adam.
This can be checked in linear time and the attractor to the corresponding vertices removed from the game.
After this preprocessing $\sigma_0$ indeed respects parity.

The pseudocode of the algorithm is given in {numref}`3-algo:strategy_improvement`.

```{figure} ./../FigAndAlgos/3-algo:strategy_improvement.png
:name: 3-algo:strategy_improvement
:align: center
The strategy improvement algorithm for parity games.
```

> **Proof of correctness.**

We start by stating a very simple property of $\delta$, which is key in the arguments below.

````{prf:observation} NEEDS TITLE AND LABEL 
Let $t \in Y$ and $p_1,\dots,p_k \in [1,d]$ such that $t$ and $\delta(t,p_1 \dots p_k)$ are neither $\top$ nor $\bot$.
Then $t \le \delta(t,p_1 \dots p_k)$ if and only if $\max  \left\{ p_1,\dots,p_k \right\}$ is even.

Let $t \in Y$ and $p_1,\dots,p_k \in [1,d]$ such that $t$ and $\delta(t,p_1 \dots p_k)$ are neither $\top$ nor $\bot$.
Then $t \le \delta(t,p_1 \dots p_k)$ if and only if $\max  \left\{ p_1,\dots,p_k \right\}$ is even.

````

The following lemma states the two important properties of $(Y,\le)$ and $\delta$.

````{prf:lemma} NEEDS TITLE 3-lem:key_property
:label: 3-lem:key_property

Let $G$ a parity graph (with no stopping option).

*  If there exists $\mu : V \to Y$ such that for all vertices $v$ we have $\mu(v) \neq \top,\bot$
and for all edges $(v,u) \in E$ we have $\mu(v) \le \delta(\mu(u), \textsf{col}(v))$,
then $G$ satisfies parity.
*  If there exists $\mu : V \to Y$ such that for all vertices $v$ we have $\mu(v) \neq \top,\bot$
and for all edges $(v,u) \in E$ we have $\mu(v) \ge \delta(\mu(u), \textsf{col}(v))$,
then $G$ satisfies the complement of parity.

````

````{admonition} Proof
:class: dropdown tip

We prove the first property, the second is proved in exactly the same way.
Thanks to the characterisation using cycles it is enough to show that all cycles in $G$ are even.
Let us consider a cycle in $G$:

$$
\pi = (v_0,v_1) (v_1,v_2) \cdots (v_{k-1},v_0).
$$

For all $i \in [0,k-1]$ we have $\mu(v_i) \le \delta(\mu(v_{i+1 \mod k}), \textsf{col}(v_i))$.
By monotonicity of $\delta$ this implies $\mu(v_1) \le \delta(\mu(v_1), \textsf{col}(v_{k-1}) \cdots  \textsf{col}(v_0))$.
Thanks to  {prf:ref}`3-lem:key_property` this implies that the maximum priority in $\left\{  \textsf{col \right\}(v_0),\dots, \textsf{col}(v_{k-1})}$ is even.

````

Let $\sigma$ a strategy respecting parity. 
A progress measure for $\Game[\sigma]$ is a post-fixed point of $\mathbb{O}$ in $F^\sigma_V$:
it is a function $\mu : V \to Y$ such that $\mu(v) = \emptyset$ if $\sigma(v) =  \mathtt{-}$ and $\mu \le  \mathbb{O}(\mu)$,
which means that $\mu(v) \le \min  \left\{  \delta(\mu(v'), \textsf{col \right\}(v)) : (v,v') \in E}$.

We now rely on  {prf:ref}`3-lem:greatest_fixed_point` and  {prf:ref}`3-lem:key_property` to prove the two principles: progress and optimality.

````{prf:lemma} NEEDS LABEL Progress

Let $\sigma$ a strategy respecting parity and $e = (v,v')$ a switchable edge.
We let $\sigma'$ denote $\sigma[v \to e]$.
Then $\sigma'$ respects parity and $\sigma < \sigma'$.

````

````{admonition} Proof
:class: dropdown tip

We first argue that $\sigma'$ respects parity.
The fact that $e = (v,v')$ is switchable reads

$$
\delta(  \textrm{val}^\sigma(v'), \textsf{col}(v)) > \delta(  \textrm{val}^\sigma(u), \textsf{col}(v)),
$$

and by definition of $\textrm{val}^\sigma$ we have $\textrm{val}^\sigma(v) = \delta(  \textrm{val}^\sigma(u), \textsf{col}(v))$,
which implies $\textrm{val}^\sigma(v) < \delta(  \textrm{val}^\sigma(v'), \textsf{col}(v))$, and in particular $\textrm{val}^\sigma(v) \neq \top$.

Let us consider the parity graph $\Game[\sigma']$ and note that for all edges $e' = (s,t)$ 
we have $\textrm{val}^\sigma(s) \le \delta(  \textrm{val}^\sigma(t), \textsf{col}(s))$:
indeed either $e'$ is an edge in $\Game[\sigma]$ and this is by definition of $\textrm{val}^\sigma$,
or $e' = e$ and the inequality was proved just above.

Since $\sigma$ respects parity $\textrm{val}^\sigma$ does not take the value $\bot$.
But we cannot apply (the first item of)  {prf:ref}`3-lem:key_property` yet because $\textrm{val}^\sigma$ may have value $\top$.
However by definition of $\textrm{val}^\sigma$ for all vertices $s$ such that $\textrm{val}^\sigma(s) = \top$ all paths from $s$ satisfy parity,
so it is enough to consider the parity graph obtained from $\Game[\sigma']$ by removing all such vertices.
The first item of  {prf:ref}`3-lem:key_property` implies that it satisfies parity, hence $\Game[\sigma']$ as well.

At this point we know that $\sigma'$ respects parity, which thanks to  {prf:ref}`3-lem:greatest_fixed_point`
implies that $\textrm{val}^{\sigma'}$ is the greatest fixed point of $\mathbb{O}$ in $F^{\sigma'}_V$.

We now argue that $\textrm{val}^\sigma$ is a progress measure for $\mathcal{G}[\sigma']$.
For all vertices but $v$ this is clear because the outgoing edges are the same in $\mathcal{G}[\sigma]$ and in $\mathcal{G}[\sigma']$.
For $v$ as argued above we have $\textrm{val}^\sigma(v) < \delta(  \textrm{val}^\sigma(v'), \textsf{col}(v))$.
It follows that $\textrm{val}^\sigma$ is indeed a progress measure for $\mathcal{G}[\sigma']$.
Since $\textrm{val}^{\sigma'}$ is the greatest fixed point of $\mathbb{O}$ in $F^{\sigma'}_V$, this implies that 
$\textrm{val}^{\sigma} \le   \textrm{val}^{\sigma'}$.

We now show that $\textrm{val}^{\sigma} <   \textrm{val}^{\sigma'}$. 
Using $\textrm{val}^{\sigma}(v') \le   \textrm{val}^{\sigma'}(v')$ and the monotonicity of $\delta$ we obtain that
$\delta(  \textrm{val}^\sigma(v'), \textsf{col}(v)) \le \delta(  \textrm{val}^{\sigma'}(v'), \textsf{col}(v))$.
By definition of $\textrm{val}^{\sigma'}$ we have $\textrm{val}^{\sigma'}(v) = \delta(  \textrm{val}^{\sigma'}(v'), \textsf{col}(v))$
and together with $\textrm{val}^\sigma(v) < \delta(  \textrm{val}^\sigma(v'), \textsf{col}(v))$ this implies that
$\textrm{val}^\sigma(v) <   \textrm{val}^{\sigma'}(v)$.

````

````{prf:lemma} NEEDS LABEL Optimality

Let $\sigma$ a strategy respecting parity that has no switchable edges, then 
$\sigma$ is winning from all vertices of $W_\mathrm{Eve}(\Game)$.

````

````{admonition} Proof
:class: dropdown tip

The fact that $\sigma$ respects parity means that it is a winning strategy
from all vertices $v$ such that $\textrm{val}^\sigma(v) = \top$.
It also implies that for all vertices $v$ we have $\textrm{val}^{\sigma}(v) \neq \bot$.
We now prove that Adam has a winning strategy from all vertices $v$ such that $\textrm{val}^{\sigma}(v) \neq \top$.
We construct a strategy of Adam by

$$
\forall v \in  V_\mathrm{Adam},\ \tau(v) =  \textrm{argmin}  \left\{  \delta(  \textrm{val}^{\sigma \right\}(u), \textsf{col}(v)) : (v,u) \in E }.
$$

We argue that $\tau$ ensures the complement of parity from all vertices $v$ such that $\textrm{val}^{\sigma}(v) \neq \top$.
Let us consider $\Game[\tau]$ the parity graph obtained from $\Game$ by restricting the outgoing edges from $V_\mathrm{Adam}$
to those prescribed by $\tau$.
We argue that for all edges $(v,,v')$ in $\mathcal{G}[\tau]$, we have 
$\textrm{val}^{\sigma}(v) \ge \delta(  \textrm{val}^{\sigma}(v'), \textsf{col}(v))$.
Once this is proved we conclude using the second item of  {prf:ref}`3-lem:key_property` implying that $\Game[\tau]$ satisfies the complement of parity.

The first case is when $v \in  V_\mathrm{Eve}$. 
Let $\sigma(v) = (v,u)$.
Since the edge $e = (v,v')$ is not switchable we have 
$\delta(  \textrm{val}^{\sigma}(v'), \textsf{col}(v)) \le \delta(  \textrm{val}^{\sigma}(u), \textsf{col}(v))$.
By definition of $\textrm{val}^\sigma$ we have $\textrm{val}^\sigma(v) = \delta(  \textrm{val}^{\sigma}(u), \textsf{col}(v))$,
implying the desired inequality.

The second case is when $v \in  V_\mathrm{Adam}$, it holds by definition of $\tau$.

````

> **Complexity analysis.**

The computation of $\textrm{val}^\sigma$ for a strategy $\sigma$ can be seen to be a shortest path problem where distances are measured using the operator $\le$. 
Thus, any algorithm for the shortest path problem can be applied, such as the Bellman-Ford algorithm.
In particular computing $\textrm{val}^\sigma$ can be done in polynomial time, and even more efficiently through a refined analysis.

An aspect of the algorithm we did not develop is choosing the switchable edge.
It is possible to switch not only one edge but a set of switchable edges at each iteration, making this question worse: 
which subset of the switchable edges should be chosen?
Many possible rules for choosing this set have been studied, as for instance the **greedy all-switches** rule. 

The next question is the number of iterations, meaning the length of the sequence
$\sigma_0,\sigma_1,\dots$. It is at most exponential since it is bounded by the number of strategies (which is bounded aggressively by $m^n$).
There are lower bounds showing that the sequence can be of exponential length, which apply to different rules for choosing switchable edges.
Hence the overall complexity is exponential; we do not elaborate further here. 

