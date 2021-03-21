(5-sec:optimal_reachability)=
# Optimal reachability

```{math}

```

In this final section, we prove {prf:ref}`5-thm:quant-reachability-main`. The proof bears many similarities to the methods for discounted MDPs, hence we only sketch the process and point out the key differences. Throughout the section we assume that **targets are sinks**, i.e. that a vertex coloured by $\textrm{Win}$ has only a self loop as the single outgoing edge. Modifying an MDP to accommodate this does not influence reachability probabilities in any way.

Consider the reachability operator $\mathcal{R}\colon[0,1]^{ V}\rightarrow [0,1]^{ V}$ such that for $\vec{y} =  \mathcal{R}(\vec{x})$ it holds

$$
\vec{y}_v = \begin{cases}

 \max_{a\in  A} \sum_{u\in  V}  \Delta(u \mid v,a)\cdot x_u &  c(v) \neq  \textrm{Win} \\
 1 &  c(v) =  \textrm{Win}.
\end{cases} 
$$

````{prf:lemma} NEEDS TITLE 5-lem:quant-reach-operator-fixed-point
:label: 5-lem:quant-reach-operator-fixed-point

For each initial vector $\vec{x}$, the limit $\lim_{k \rightarrow \infty} \mathcal{R}^k(\vec{x})$ exists. Moreover, if $\vec{x} \leq  \mathcal{R}(\vec{x})$, then the limit is equal to the least fixed point of $\mathcal{R}$ that is greater than or equal to $\vec{x}$; if $\mathcal{R}(\vec{x})\leq \vec{x}$, then the limit is equal to the greatest fixed point of $\mathcal{R}$ that is less than or equal to $\vec{x}$.

````

````{admonition} Proof
:class: dropdown tip

The existence of the limit follows from the monotonicity of $\mathcal{R}$.
In addition, it can be easily checked that the set $[0,1]^{ V}$ is a directed complete partial order and that $\mathcal{R}$ is a Scott-continuous operator on this set. Hence, the result follows from the Kleene's theorem (see also Tarski-Kantorovich principle).

````

We denote by $\mathtt{Reach}^k( \textrm{Win})$ the set of all plays that reach $\textrm{Win}$ within the first $k$ steps. Clearly, for each $\sigma$ and $v_0$ we have $\lim_{k \rightarrow \infty}  \mathbb{P}^\sigma_{ v_0}( \mathtt{Reach}^k( \textrm{Win})) =  \mathbb{P}^\sigma_{ v_0}( \mathtt{Reach}( \textrm{Win}))$.

````{prf:lemma} NEEDS TITLE 5-lem:quant-reach-step-operator
:label: 5-lem:quant-reach-step-operator

For each $k\in  \mathbb{N}$ and $v\in  V$, $\mathcal{R}^k(\vec{0})_v = \sup_{\sigma} \mathbb{P}^\sigma_v( \mathtt{Reach}^k( \textrm{Win}))$. In particular, the vector $\vec{x}^* = \lim_{k \rightarrow\infty}  \mathcal{R}^k(\vec{0})$ is the least fixed point of $  \mathcal{R} $ and it is equal to the vector of reachability values. 

````

````{admonition} Proof
:class: dropdown tip

The first part can be proved by a straightforward induction, the second part follows by {prf:ref}`5-lem:quant-reach-operator-fixed-point` and a simple limiting argument.

````

Similarly to {prf:ref}`5-def:disc-safe-act` we say that an action $a$ is $\vec{x}$-safe in $v$ if it holds that $a= \underset{a' \in  A}{\arg\max} \sum_{u\in  V} 
 \Delta(u\mid v,a') \cdot\vec{x}_u.$ Recall that a strategy $\sigma$ is $\vec{x}$-safe if all actions selected in a vertex with non-zero probability are $\vec{x}$-safe in that vertex.

````{prf:lemma} NEEDS TITLE 5-lem:quant-reach-value-distribution
:label: 5-lem:quant-reach-value-distribution

Let $ \vec{x}^* $ be as in {prf:ref}`5-lem:quant-reach-step-operator`. 
Next, let $Z^{(n)}$ be a random variable which for a given time step $n$ looks at the current vertex $v$ after $n$ steps and returns the value $\vec{x}^*_v$. Then for every $\vec{x}^*$-safe strategy $\sigma$ it holds $\mathbb{E}^\sigma_{ v_0}[Z^{(n)}] = \vec{x}^*_{ v_0}$. Moreover, it holds $\mathbb{E}^\sigma_{ v_0}[Z^{(n)}\cdot  \mathbf{1}_{ c{(  \textrm{Out}{( \pi_{n})})}= \textrm{Win}}] =  \mathbb{P}^\sigma_{ v_0}( \mathtt{Reach}^n( \textrm{Win})).$

````

````{admonition} Proof
:class: dropdown tip

By an easy induction on $n$, using the fact that target states are  sinks.

````

Now an analogue of {prf:ref}`5-lem:disc-val-lower` does not hold for reachability: a strategy playing only $\vec{x}^*$-safe actions might not be optimal (indeed, it might not reach $\textrm{Win}$ at all). Instead, we proceed as follows: Let $\mathcal{M}^*$ be an MDP in which we `disable', in each state $v$, all actions that are not $\vec{x}^*$-safe in $v$. This can be formally done by adding a new non-target sink vertex $ \mathit{sink} $, an edge from each original vertex to $ \mathit{sink} $, and stipulating that each action $a$ that is disabled in a vertex $ v $ chooses, when played in $ v $ in $  \mathcal{M}^*$, the edge leading to $ \mathit{sink} $ with probability 1.

````{prf:lemma} NEEDS TITLE 5-lem:quant-reach-pruning-unsafe
:label: 5-lem:quant-reach-pruning-unsafe

The vectors of reachability values $  \textrm{val}( \mathcal{M})$ and $\textrm{val}( \mathcal{M}^*) $ are equal.
In particular, $  W_{>0}( \mathcal{M}, \mathtt{Reach}( \textrm{Win})) =  W_{>0}( \mathcal{M}^*, \mathtt{Reach}( \textrm{Win})).$

````

````{admonition} Proof
:class: dropdown tip

Let $\vec{x}^*$ again denote the vector of optimal values in $\mathcal{M}$. If all actions in $  \mathcal{M} $ are $\vec{x}^*$-safes, then the lemma clearly holds. Otherwise there is some $\delta\in(0,1)$ such that for each action $a$ that is not $\vec{x}^*$-safe in some vertex $ v $ it holds $\sum_{u\in  V}  \Delta(u\mid v,a) \cdot\vec{x}_u \leq \vec{x}^*_v - \delta$.

Let $\epsilon \in(0,\delta)$ be arbitrary and fix an $\epsilon$-optimal strategy $\sigma$ in $\mathcal{M}$. We will show that there is a $(2 \varepsilon/\delta)$-optimal  strategy $\sigma'$ which only uses $\vec{x}^*$-safe actions. Since $\varepsilon$ can be chosen arbitrarily close to $0$, this shows that $\vec{x}^*$-safe strategies can get arbitrarily close to the value, hence $\textrm{val}( \mathcal{M}^*)= \textrm{val}( \mathcal{M})$.

The strategy $\sigma'$ initially mimics $\sigma$ up to the first point in time when an action that is not $\vec{x}^*$-safe in the current vertex is to be selected. At this point $\sigma'$ switches to behave as any $\vec{x}^*$-safe strategy. To analyse the value achieved by $\sigma'$, we need to bound the probability of the event $\mathit{NonSafe}$ that the switch occurs. By the same reasoning as in {prf:ref}`5-lem:quant-reach-value-distribution`, we can show that for all $n$ it holds $\mathbb{P}^\sigma_{ v_0}( \mathtt{Reach}^n( \textrm{Win})) \leq  \mathbb{E}^\sigma_{ v_0}[Z^{(n)}] \leq  \vec{x}^*_{ v_0}- \delta\cdot \mathbb{P}_{ v_0}^\sigma(\mathit{NonSafe^{(n)}})$, where $\mathit{NonSafe^{(n)}}$ is the probability that a switch occurs in the first $n$ steps. By taking $n$ to the limit we get $\mathbb{P}^\sigma_{ v_0}( \mathtt{Reach}( \textrm{Win})) \leq \vec{x}^*_{ v_0}- \delta\cdot \mathbb{P}_{ v_0}^\sigma(\mathit{NonSafe})$. At the same time $\vec{x}^*_{ v_0}- \varepsilon\leq   \mathbb{P}^\sigma_{ v_0}( \mathtt{Reach}( \textrm{Win}))$. Combining these two inequalities yields $\mathbb{P}_{ v_0}^\sigma(\mathit{NonSafe}) \leq  \frac{ \varepsilon}{\delta}.$ Now clearly $\mathbb{P}_{ v_0}^{\sigma'}( \mathtt{Reach}( \textrm{Win})) \geq \vec{x}^*_{ v_0} -  \varepsilon -  \mathbb{P}_{ v_0}^{\sigma}(\mathit{NonSafe}) \geq \vec{x}^*_{ v_0} -  \varepsilon -  \varepsilon/\delta \geq \vec{x}^*_{ v_0} -2 \varepsilon/\delta$.

````

````{prf:lemma} NEEDS TITLE 5-lem:quant-reach-strat-contsruction
:label: 5-lem:quant-reach-strat-contsruction

Given the vector $\vec{x}^*$ of optimal reachability values, we can compute, in polynomial time, the optimal MD reachability strategy in $\mathcal{M}$.

````

````{admonition} Proof
:class: dropdown tip

Given $\vec{x}^*$, we construct the MDP $\mathcal{M}^*$ and compute the winning strategy $\sigma$ for positive reachability in $\mathcal{M}^*$. We already know that $\sigma$ can be taken memoryless and computed in polynomial time ({prf:ref}`5-thm:positive-char`). We claim that $\sigma$ is an optimal reachability strategy in $\mathcal{M}$. By {prf:ref}`5-lem:quant-reach-pruning-unsafe` it suffices to show that $\sigma$ is optimal in $\mathcal{M}^*$. Let $W$ be the winning region for positive reachability in $\mathcal{M}^*$. Since $\sigma$ is memoryless, with probability $1$ we reach either $\textrm{Win}$ or a vertex of value $0$ (from which we cannot return to $W$ anymore); in other words, for almost all plays $\pi$ we have that $\mathbf{1}_{  \textrm{Out}( \pi_n)\in W}$ eventually equals $\mathbf{1}_{ c(  \textrm{Out}( \pi_n)) =  \textrm{Win}}$. Hence, using {prf:ref}`5-lem:quant-reach-value-distribution` we get $\vec{x}^*_{ v_0} = \lim_{n\rightarrow\infty} \mathbb{E}^\sigma_{ v_0}[Z^{(n)}] =  \mathbb{E}^\sigma_{ v_0}[\lim_{n\rightarrow\infty} Z^{(n)}] =  \mathbb{E}^\sigma_{ v_0}[\lim_{n\rightarrow\infty} Z^{(n)}\cdot \mathbf{1}_{  \textrm{Out}( \pi_n)\in W}] =  \mathbb{E}^\sigma_{ v_0}[\lim_{n\rightarrow\infty} Z^{(n)}\cdot  \mathbf{1}_{ c(  \textrm{Out}( \pi_{n})) =  \textrm{Win} } ] =  \mathbb{P}_{ v_0}^\sigma( \mathtt{Reach}( \textrm{Win}))$. Here, the third equality holds since $ \vec{x}^*_v $ is zero for $ v\not\in W $, while the  swapping of expectations and limits can be performed due to the dominated convergence theorem.

````

To finish the proof of {prf:ref}`5-thm:quant-reachability-main`, it remains to prove that the vector of optimal values $\vec{x}^*$ can be computed in polynomial time. We again employ linear programming.

```{figure} ./../FigAndAlgos/5-fig:reach-lp.png
:name: 5-fig:reach-lp
:align: center
The linear program $\mathcal{L}_{\mathit{reach}}$ with variables $x_v$, $v\in  V$.
```

````{prf:lemma} NEEDS TITLE 5-lem:quant-reach-lp
:label: 5-lem:quant-reach-lp

The linear program $\mathcal{L}_{\mathit{reach}}$ in {numref}`5-fig:reach-lp` has a unique optimal solution 
$\bar{\vec{x}}$ such that $\bar{\vec{x}} = \vec{x}^*$.

````

````{admonition} Proof
:class: dropdown tip

Clearly $\vec{x}^*$ is a feasible solution of $\mathcal{L}_{\mathit{reach}}$. Similarly to {prf:ref}`5-lem:disc-lp` we prove that each feasible solution $\vec{x}$ of $\mathcal{L}_{\mathit{reach}}$ satisfies $\vec{x}\geq \vec{x}^*$. We can proceed analogously  to {prf:ref}`5-lem:disc-lp`, just replacing the operator $\mathcal{D}$ with $\mathcal{R}$. The proof can be mimicked up to the point where we get that $\lim_{k\rightarrow \infty}  \mathcal{R}^k (\vec{x}) \leq \vec{x}$ (the limit exists by {prf:ref}`5-lem:quant-reach-operator-fixed-point`). Since $\mathcal{R}(\vec{x})\leq \vec{x}$ for each feasible solution $\vec{x}$, from {prf:ref}`5-lem:quant-reach-operator-fixed-point` we get that the limit is a fixed point of $\mathcal{R}$, and in hence it is greater or equal to the least fixed point of $\mathcal{R}$, i.e. $\vec{x}^*$ ({prf:ref}`5-lem:quant-reach-step-operator`). Hence, also $\vec{x} \geq \lim_{k\rightarrow \infty}  \mathcal{R}^k (\vec{x}_0)\geq \vec{x}^*$. 

````

{prf:ref}`5-lem:quant-reach-strat-construction` and {prf:ref}`5-lem:quant-reach-lp` give us {prf:ref}`5-thm:quant-reachability-main`.
