(5-sec:mean_payoff_strongly_connected)=
# Mean-payoff optimality in strongly connected MDPs

```{math}

```

As shown in the previous section, the optimal solution of any of the programs $\mathcal{L}_{\mathit{mp}}$, $\mathcal{L}_{\mathit{mp}}^{\mathit{dual}}$ gives us an upper bound on the optimal value. In this sub-section we show that in strongly connected MDPs: a) a value of every vertex is the same; b) from a solution of $\mathcal{L}_{\mathit{mp}}$ one can extract a memoryless deterministic strategy $\sigma$ whose expected mean-payoff is well defined (i.e., the preconditions of {prf:ref}`5-lem:limit-defined` are satisfied)) and equal to the objective value of the solution. Moreover, if the solution in question is optimal, then $ \sigma $ is optimal for both $\textsf{p-Payoff}$- and $\textsf{s-Payoff}$-semantics.

````{prf:definition} NEEDS TITLE 5-def:scc-mdp
:label: 5-def:scc-mdp

An MDP is **strongly connected** if for each pair of vertices $u,v$ there exists a strategy which, when starting in $u$, reaches $v$ with a positive probability. 

````

For the rest of this section we fix an optimal solution $\bar{\vec{x}}_{v,a}$ of $\mathcal{L}_{\mathit{mp}}$. We denote by $S$ the set of all vertices for which there exists action $a$ s.t. $\bar{\vec{x}}_{v,a}>0.$ From the shape of $\mathcal{L}_{\mathit{mp}}$ it follows that $S$ is non-empty and closed, and hence we can consider a sub-MDP $\mathcal{M}_{ S}$ induced by $S$. In $\mathcal{M}_{ S}$ we then define a memoryless randomized strategy $\sigma$ by putting 

$$

\sigma(a\mid v)=\frac{ \bar{\vec{x}}_{(v,a)}}{\sum_{b\in  A} \bar{\vec{x}}_{(v,b)}}.

$$

Fixing a strategy $\sigma$ yields a **Markov chain** $\mathcal{M}_S^{\sigma}$. Markov chain can be viewed as an MDP with a single action (and hence, with no non-determinism). $\mathcal{M}_{ S}^\sigma$ in particular can be viewed an MDP with the same vertices, edges, and colouring as $\mathcal{M}_S$, but with a single action (as non-determinism was already resolved by $\sigma$). The probability of transitioning from a vertex $u$ to a vertex $v$ in a Markov chain is denoted by $P_{u,v}$. In $\mathcal{M}_{ S}^{\sigma}$ we have $P_{u,v}=\sum_{a\in  A}  \Delta(v\mid u,a)\cdot\sigma(a\mid u)$, the right-hand side being computed in the original MDP $\mathcal{M}$. Both $\mathcal{M}_S$ and $\mathcal{M}_{ S}^{\sigma}$ have the same sets of plays and for each initial vertex, the probability measure induced by $\sigma$ in $\mathcal{M}$ equals the probability measure arising (under the unique policy) in $\mathcal{M}_{ S}^{\sigma}$. Hence, to prove anything about $\sigma$ it suffices to analyse $\mathcal{M}_{ S}^{\sigma}$.

> **A refresher on Markov chains.**

 We review some fundamental notions of Markov chain theory {cite}`Norris:1998`. A Markov chain that is strongly connected is called **irreducible**. The one-step transition probabilities in a Markov chain can be arranged into a square matrix $P$, which has one row and one column for each vertex. The cell in the row corresponding to a vertex $u$ and in the column corresponding to a vertex $v$ bears the value $P_{u,v}$ defined above. An easy induction shows that the matrix $P^k$ contains $k$-step transition probabilities. That is, the probability of being in $v$ after $k$ steps from vertex $u$ is equal to the $(u,v)$-cell of $P^k$, which we denote by $P^{(k)}_{u,v}$.

A vertex $u$ of a Markov chain is **recurrent** if, when starting from $u$, it is revisited infinitely often with probability $1$. On the other hand, if the probability that $u$ is re-visited only finitely often is one, then the vertex is **transient**. It is known (Theorem 1.5.3 in {cite}`Norris:1998`) that each vertex of a finite Markov chain is either recurrent or transient, and that these two properties can be equivalently characterized as follows: vertex $u$ is recurrent if and only if  $\sum_{k=0}^{\infty} P^{(k)}_{u,u}=\infty$, otherwise it is transient.

An **invariant distribution** in a Markov chain with a vertex set $V$ is a $| V|$-dimensional non-negative row vector $\vec{z}$ which adds up to $1$ and satisfies $  \vec{z}\cdot  P =  \vec{z}$.

The following lemma holds for arbitrary finite Markov chains.

````{prf:lemma} NEEDS TITLE 5-lem:MC-inv-rec
:label: 5-lem:MC-inv-rec

Let $\vec{z}$ be an invariant distribution and $v$ a vertex such that $\vec{z}_v > 0$. Then $v$ is recurrent.

````

````{admonition} Proof
:class: dropdown tip

Let $n$ be the number of vertices in the chain and $p_{\min}$ the minimum non-zero entry of $P$.
Assume, for the sake of contradiction, that $v$ is transient. We show that in such a case, for each vertex $u$ it holds $\lim_{k\rightarrow\infty}  P^{(k)}_{u,v} = 0$. For $u=v$ this is immediate, since the sum $\sum_{k=0}^{\infty} P^{(k)}_{v,v}$ converges for  transient $v$. Otherwise, let $f_{u,v,i}$ be the probability that a play starting in $u$ visits $v$ for the **first time** in exactly $i$ steps. Then $P^{(k)}_{u,v}=\sum_{i=0}^k f_{u,v,i}\cdot  P^{(k-i)}_{v,v}$. Now when starting in a vertex from which $v$ is reachable with a positive probability, at least one of the following events happens with probability $\geq p_{\min}^n$ in the first $n$ steps: either we reach a vertex from which $v$ is not reachable with positive probability, or we reach $v$. If neither of the events happens, we are, after $n$ steps, still in a vertex from which $v$ can be reached with a positive probability. In such a case, the argument can be inductively repeated (analogously to the proof of {prf:ref}`5-thm:as-char`) to show that $f_{u,v,i}\leq (1-p_{\min}^n)^{\lfloor\frac{i}{n}\rfloor}\leq (1-p_{\min}^n)^{\frac{i-n}{n}}$.

Since $\sum_{k=0}^{\infty} P^{(k)}_{v,v}$ converges, for each $\varepsilon>0$ there exists $j_\varepsilon$ such that $\sum_{i=j_{ \varepsilon}}^{\infty} P^{(i)}_{v,v} < \frac{ \varepsilon}{2}$. Similarly, there exists $\ell_\varepsilon$ such that 

$$

\sum_{i=\ell_{ \varepsilon}}^{\infty}{(1-p_{\min}^n)^{\frac{i-n}{n}}} = \frac{(1-p_{\min}^n)^{\frac{\ell_\varepsilon}{n}}}{\left(1-(1-p_{\min}^n)^{\frac{1}{n}}\right)\cdot(1-p_{\min}^n)}< \frac{ \varepsilon}{2},

$$

 and hence $\sum_{i=\ell_{ \varepsilon}}^{\infty} f_{u,v,i}< \frac{ \varepsilon}{2}.$

Now we put $m_{ \varepsilon}=\max\{j_\varepsilon,\ell_\varepsilon\}$. For any $k\geq 2m_{ \varepsilon}$ we have $P^{(k)}_{u,v}=\sum_{i=0}^k f_{u,v,i}\cdot  P^{(k-i)}_{v,v} \leq \sum_{i=m_{ \varepsilon}}^{k}f_{u,v,i} + \sum_{i=0}^{m_{ \varepsilon}} P^{(k-i)}_{v,v}\leq\sum_{i=m_{ \varepsilon}}^{k}f_{u,v,i} + \sum_{i=m_{ \varepsilon}}^{k} P^{(i)}_{v,v}< \varepsilon$ (note that all the series involved are non-negative). This proves that $P^{(k)}_{u,v}$ vanishes in the limit.

Finally, we derive the contradiction. Since $\vec{z}$ satisfies $\vec{z}\cdot  P =  \vec{z}$, we also have $\vec{z}\cdot  P^k =  \vec{z}$ for all $k$. Hence, the $v$-component of $\vec{z}\cdot  P^k$ is equal to $\vec{z}_v>0$. But as shown above, the $v$-column of $P^k$ converges to the all-zero vector as $k\rightarrow \infty$, so also $( \vec{z}\cdot  P^k)_v$ vanishes in the limit, a contradiction.

````

> **Towards the optimality of $ \sigma $.**

 We now turn back to the chain $\mathcal{M}_{ S}^{\sigma}$, where the memoryless strategy $ \sigma $ is obtained from the optimal solution of $   \mathcal{L}_{\mathit{mp}} $. In general, $  \mathcal{M}_{ S}^{\sigma} $ does not have to be irreducible. Hence, we use the following lemma and its corollary to extract an irreducible sub-chain, to which we can apply known results of Markov chain theory.

````{prf:lemma} NEEDS TITLE 5-lem:mc-rec
:label: 5-lem:mc-rec

Let $\bar{ \vec{z}}$ be a vector such that for each $v\in  S$ it holds $\bar{ \vec{z}}_v=\sum_{a\in  A}  \bar{\vec{x}}_{v,a}$. Then $\bar{ \vec{z}}$ is an invariant distribution of $\mathcal{M}_{ S}^{\sigma}$. Consequently, all vertices of $\mathcal{M}_{ S}^{\sigma}$ are recurrent.

````

````{admonition} Proof
:class: dropdown tip

The first part follows directly from the fact that $\bar{\vec{x}}_{v,a}$ is a feasible solution of $\mathcal{L}_{\mathit{mp}}$. The second part follows from {prf:ref}`5-lem:MC-inv-rec` and from the fact that $\bar \vec{z}$ is positive (by the definition of $S$).

````

````{prf:corollary} NEEDS TITLE 5-cor:mp-scc-extraction
:label: 5-cor:mp-scc-extraction

The set $S$ can be partitioned into subsets $S_1, S_2,\dots, S_m$ such that each $S_i$ induces a strongly connected sub-chain of $\mathcal{M}_{ S}^{\sigma}$.

````

````{admonition} Proof
:class: dropdown tip

Let $v\in S$ be arbitrary and let $U_v\subseteq  S$ be the set of all vertices reachable with positive probability from $v$ in $\mathcal{M}_{ S}^{\sigma}$. Then $v$ is reachable (in $\mathcal{M}_{ S}^{\sigma}$) with positive probability from each $u\in U_v$: otherwise, there would be a positive probability of never revisiting $v$, a contradiction with each vertex being recurrent in $\mathcal{M}_{ S}^{\sigma}$ ({prf:ref}`5-lem:mc-rec`). Hence, $U_v$ induces a strongly connected `sub-MDP' (or sub-chain) of $\mathcal{M}_{ S}^{\sigma}$. It is easy to show that if $U_v \neq U_w$ for some $v\neq w $, then the two sets must be disjoint.

````

Hence, we can extract from $S$ a set $Q$ inducing a strongly-connected sub-chain of $\mathcal{M}_{ S}^{\sigma}$, which we denote $\mathcal{M}^{\sigma}_{Q}$. The set $Q$ also induces a strongly connected sub-MDP of $\mathcal{M}$ denoted by $\mathcal{M}_Q$. The chain $\mathcal{M}^{\sigma}_{Q}$ arises by fixing, in $\mathcal{M}_Q$, a strategy formed by a restriction of $\sigma$ to $Q$. We use the following powerful theorem to analyse $\mathcal{M}^{\sigma}_{Q}$.

````{prf:theorem} Ergodic theorem; see Theorem 1.10.2 in {cite}`Norris:1998`
:label: 5-thm:ergodic
 In a strongly connected Markov chain (with a finite set of vertices $V$) there exists a unique invariant distribution $\vec{z}$. Moreover, for every vector $\vec{h}\in  \mathbb{R}^{ V}$ the following equation holds with probability 1:

$$
\lim_{n \rightarrow \infty} \frac{1}{n} \sum_{i=0}^{n-1}\vec{h}_{ \textrm{In}(\pi_i)} = \sum_{v\in V}  \vec{z}_v\cdot \vec{h}_v.
$$

(In particular, the limit is well-defined with probability 1).

````

We can use the Ergodic theorem to shows that the expected mean-payoff achieved by $\sigma$ in $\mathcal{M}_{Q}$ matches the optimal value of $   \mathcal{L}_{\mathit{mp}} $, in a very strong sense: the probability of a play having a mean-payoff equal to this optimal value is 1 under $ \sigma $.

````{prf:theorem} NEEDS TITLE 5-cor:mp-scc-optimality
:label: 5-cor:mp-scc-optimality

Let $\sigma_Q$ be the restriction of $\sigma$ to $Q$. Then for every $v\in Q$ it holds that $\mathbb{P}^{\sigma_Q}_{ \mathcal{M}_Q,v}(  \mathtt{MeanPayoff}^{\;-} = r^*)=1$, where $r^*$ is the is the optimal value of $\mathcal{L}_{\mathit{mp}}$.

````

````{admonition} Proof
:class: dropdown tip

Let $ \vec{w}\in \mathbb{R}^{ V \times A} $ be a vector sych that $\vec{w}_{(v,a)}= \bar{\vec{x}}_{(v,a)}/\sum_{(q,a)\in Q\times A}  \bar{\vec{x}}_{(q,a)}$ for every $(v,a)\in Q\times  A$, and $\vec{w}_{(v,a)}=0$ for all other $(v,a)$. We claim that $ \vec{w} $ is also an optimal solution of $\mathcal{L}_{\mathit{mp}}$. 

To prove feasibility, note that setting $\vec{w}_{(v,a)}=0$ for each $v\in  V\setminus Q$ does not break the constraints {eq}`5-eq:mdp-flow`. This is because $Q$ induces a strongly connected sub-chain of $\mathcal{M}_{ S}^{\sigma}$, and hence there are no $v\in  V$, $u\in  V\setminus Q$ such that $\bar{\vec{x}}_{(u,a)}\cdot  \Delta(v\mid u,a)>0$. Next, {eq}`5-eq:mdp-flow` is invariant w.r.t. multiplication of variables by a constant, so normalizing the remaining values preserves {eq}`5-eq:mdp-flow` and ensures that {eq}`5-eq:mdp-freq-1` holds. 

To prove optimality, assume that the objective value of $\vec{w}$ is smaller than $r^*$. Then we can mirror the construction from the previous paragraph and produce a feasible solution ${\hat{\vec{w}}_{(v,a)}}$ whose $(Q\times A)$-indexed components are zero and the rest are normalized components of $\bar{\vec{x}}$. Then $r^*$ is a convex combination of the objective values of $\vec{w}$ and $\hat{\vec{w}}$, so $\hat{\vec{w}}$ must have a strictly larger value than $r^*$, a contradiction with the latter's optimality.

We now plug $ \vec{w} $ into the ergodic theorem as follows: As in {prf:ref}`5-lem:mc-rec`, it easy to prove that setting $\vec{z}_v=\sum_{a\in A}\vec{w}_{(v,a)}$ yields an invariant distribution. Now put $\vec{h}_v=\sum_{a\in A}\sigma(a\mid v)\cdot  c(v,a)$ ($ =  \sum_{w \in  V}  P_{v,w}\cdot  c(v,w)$). From the Ergodic theorem we get that $\lim_{n \rightarrow \infty} \frac{1}{n} \sum_{i=0}^{n-1}\vec{h}_{ \textrm{In}(\pi_i)}$ almost-surely exists and equals 

$$

\sum_{v\in Q}  \vec{z}_v\cdot \vec{h}_v &= \sum_{v\in  V} \left(\big(\sum_{d\in A}\vec{w}_{(v,d)}\big)\cdot \big(\sum_{a\in A}\sigma(a\mid v)\cdot  c(v,a) \big)\right) \nonumber\\
&= \sum_{v\in Q} \left(\Bigg( \frac{\sum_{d\in A} \bar{\vec{x}}_{(v,d)}}{\sum\limits_{\substack{q\in Q\\ b\in  A}}  \bar{\vec{x}}_{(q,b)}} \Bigg)\cdot \Bigg( \frac{\sum_{a\in A} \bar{\vec{x}}_{(v,a)}\cdot c(v,a)}{\sum\limits_{d\in   A}  \bar{\vec{x}}_{(v,d)}} \Bigg) \right) \nonumber\\
&= \frac{1}{\sum\limits_{\substack{q\in Q\\ b\in  A}}  \bar{\vec{x}}_{(q,b)}}\cdot\sum\limits_{\substack{v\in Q\\ a\in A}}  \bar{\vec{x}}_{(v,a)}\cdot  c(v,a) = \sum\limits_{\substack{v\in Q\\ a\in A}} \vec{w}_{(v,a)}\cdot c(v,a) =r^*.

$$ (5-eq:mc-opt-limit)

It remains to take a step from the left-hand side of {eq}`5-eq:ergodic-use` towards the mean payoff. To this end, we construct a new Markov chain $\mathcal{M}_Q'$ from $\mathcal{M}_Q$ by `splitting' every edge $(u,v)$ with a new dummy vertex $d_{u,v}$ (i.e., $d_{u,v}$ has one edge incoming from $u$ with probability $P_{u,v}$ and one edge outgoing to $v$ with probability $1$). In $\mathcal{M}_Q'$ we define a vector $\vec{h}'$ s.t. for each vertex $d_{u,v}$ the vector $ \vec{h}' $ has the $ d_{u,v} $-component equal to $c(u,v)$, while the components corresponding to the original vertices are zero. It is easy to check that $\mathcal{M}_Q'$  is strongly connected and that it has an invariant distribution $\vec{z}'$ defined by $\vec{z}'_v= \vec{z}_v/2$ for $v$ in $Q$ and $\vec{z}'_{d_{u,v}}=\frac{ \vec{z}_u\cdot P_{u,v}}{2}$ for $(u,v)$ an edge of $\mathcal{M}_Q$.
Also, by easy induction, for each play $\pi$ of length $n$ in $\mathcal{M}_Q$ it holds $\frac{1}{n}\sum_{i=0}^{n-1} c( \pi_i) = \frac{1}{n}\sum_{i=0}^{2n-1}\vec{h}'_{ \textrm{In}( \pi_i')}$, where $\pi'$ is the unique play in $\mathcal{M}_Q'$ obtained from $\pi$ by splitting edges with appropriate dummy vertices. Hence, 

$$

\lim_{n\rightarrow \infty}\frac{1}{n}\sum_{i=0}^{n-1} c( \pi_i) = 2\cdot \lim_{n\rightarrow \infty}\frac{1}{n}\sum_{i=0}^{n-1}\vec{h}'_{ \textrm{In}( \pi_i')},
$$ (5-eq:mc-opt-limit)
 provided that both limits exist. By the ergodic theorem  applied to $\mathcal{M}_Q'$, we have that the RHS  limit in {eq}`5-eq:mc-opt-limit` is defined with probability 1 and equal to

$$

\underbrace{\sum_{v\in Q}  \vec{z}'_v \cdot \vec{h}'_{v}}_{=0} + \sum_{u,v\in Q}  \vec{z}'_{d_{u,v}}\cdot \vec{h}'_{d_{u,v}} = \frac{1}{2}\sum_{u\in Q} \vec{z}_u\cdot\left( \sum_{v\in Q} P_{u,v}\cdot  c(u,v)\right)\\ =\frac{1}{2}\sum_{u\in Q}  \vec{z}_u\cdot \vec{h}_u=\frac{r^*}{2},

$$

the last equality being shown above. Plugging this into {eq}`5-eq:mc-opt-limit` yields that if a limit on the LHS (i.e., the mean payoff of a play) is well-defined with probability 1, then it is equal to $r^*$ also with probability 1. But if there was a set $L$ of positive probability in $\mathcal{M}_Q$ with $\lim_{n \rightarrow \infty}\frac{1}{n}\sum_{i=0}^{n-1} c( \pi_i)$ undefined for each $\pi\in L$, by splitting the plays in $L$ we would obtain a positive-probability set of plays in $\mathcal{M}_Q'$ in which $\lim_{n \rightarrow \infty}\frac{1}{n}\sum_{i=0}^{n-1}\vec{h}'_{ \textrm{In}( \pi_i')}$ is also undefined, a contradiction with the ergodic theorem.

````

So far, we have constructed an optimal strategy $\sigma_Q$ but only on the part $Q$ of the original MDP $\mathcal{M}$. To conclude the construction, we define a memoryless strategy $\sigma^*$ in $\mathcal{M}$ as follows: we fix a memoryless deterministic strategy $\sigma_{=1}$ that is winning, from each vertex of $\mathcal{M},$ for the objective of almost-sure reaching of $Q$ (such a strategy exists since $\mathcal{M}$ is strongly connected, see also {prf:ref}`5-thm:as-char`. Then we put $\sigma^*(v)=\sigma_{=1}(v)$ if $v\not\in Q$ and $\sigma^*(v)=\sigma_Q(v)$ otherwise. Hence, starting in any vertex, $\sigma^*$ eventually reaches $Q$ with probability 1 and then it starts behaving as $\sigma_Q$. The optimality of such a strategy follows from the prefix independence of mean payoff, as argued in the next theorem.

````{prf:theorem} NEEDS TITLE 5-thm:mp-valcomp
:label: 5-thm:mp-valcomp
 For any sequence of numbers $c_0,c_1,\dots$ and any $k\in \mathbb{N}$ it holds $\liminf_{n\rightarrow \infty}\frac{1}{n}\sum_{i=0}^{n-1}c_i = \liminf_{m\rightarrow \infty}\frac{1}{m}\sum_{i=0}^{m-1}c_{k+i}$. As a consequence, 
for every vertex $v$ in $\mathcal{M}$ it holds $\mathbb{P}^{\sigma_Q}_{ \mathcal{M}_Q,v}(  \mathtt{MeanPayoff}^{\;-}=r^*)=1,$ where $r^*$ is the optimal value of $\mathcal{L}_{\mathit{mp}}$. Hence, $\mathbb{E}^{\sigma^*}_v[  \mathtt{MeanPayoff}^{\;-}]= r^*$.

````

````{admonition} Proof
:class: dropdown tip

We have

$$

\liminf_{n\rightarrow \infty}\frac{c_0 + \cdots c_{n-1}}{n} &= \liminf_{n\rightarrow \infty}\left(\underbrace{\frac{k}{n}}_{\mathrlap{\text{vanishes for } n\rightarrow \infty}}\cdot\frac{c_0 + \cdots + c_{k-1}}{k} + \underbrace{\frac{n-k}{n}}_{\mathrlap{\rightarrow 1 \text{ for } n\rightarrow \infty}}\cdot\frac{c_k+\cdot+c_{n-1}}{n-k} \right)\\
&=\liminf_{m\rightarrow\infty} \frac{c_k+\dots+c_{k+m-1}}{m}.

$$
 A similar argument holds for $\limsup.$

With probability 1, a play has an infinite suffix consisting of plays from $\mathcal{M}_Q^{\sigma}$, and thus also $\mathtt{MeanPayoff}^{\;-}$ and $\mathtt{MeanPayoff}^{\;+}$ determined by this suffix. By {prf:ref}`5-cor:mp-scc-optimality`, these quantities are equal to $r^*$ with probability 1.

````

The following theorem summarizes the computational aspects.

````{prf:theorem} NEEDS TITLE 5-thm:mp-rand-opt-main
:label: 5-thm:mp-rand-opt-main

In a strongly connected mean-payoff MDP, one can compute, in polynomial time, a memoryless randomized strategy which is optimal from every vertex, as well as the (single) optimal value of every vertex.

````

````{admonition} Proof
:class: dropdown tip

We obtain, in polynomial time, an optimal solution of $\mathcal{L}_{\mathit{mp}}$, with the optimal objective value being the optimal value of every vertex ({prf:ref}`5-thm:mp-valcomp`). We then use this optimal solution $\bar{\vec{x}}$ to construct the strategy $\sigma$ and the  Markov chain $\mathcal{M}_{ S}^{\sigma}$. From this chain we extract a strongly connected subset of vertices $Q$ (in polynomial time, by a simple graph reachability analysis). With the subset in hand, we can construct strategies $\sigma_Q$ and $\sigma_{=1}$, all polynomial-time computations (see {prf:ref}`5-thm:as-char`). These two strategies are then combined to produce the optimal strategy $\sigma^*$.

````

## Deterministic optimality in strongly connected MDPs

It remains to prove that we can actually compute a memoryless **deterministic** strategy that is optimal in every vertex. Looking back at the construction that resulted in {prf:ref}`5-thm:mp-rand-opt-main`, we see that the optimal strategy $\sigma^*$ might be randomized because the computed optimal solution $\bar{\vec{x}}$ of $\mathcal{L}_{\mathit{mp}}$ can contain two components $(v,a)$, $(v,b)$ with $a\neq b$ and both $\bar{\vec{x}}_{(v,a)}$ and $\bar{\vec{x}}_{(v,b)}$ being positive. To prove memoryless deterministic optimality, we will show that there is always an optimal solution which yields a deterministic strategy, and that such a solution can be obtained in polynomial time.

The previous section implicitly defined two mappings: First, a mapping $\Psi$, which maps every solution $ \vec{x} $ of $\mathcal{L}_{\mathit{mp}}$ to a memoryless strategy in some sub-MDP of $\mathcal{M}$, by putting $\Psi(\vec{x}) = \sigma$ where $\sigma(a\mid v) = \vec{x}_{(v,a)}/\sum_{b\in  A}\vec{x}_{(v,b)}$. Second, mapping $\Xi$, which maps each memoryless strategy $\sigma$ that induces a strongly connected Markov chain to a solution $\Xi(\sigma)$ of $\mathcal{L}_{\mathit{mp}}$ such that $\Xi(\sigma)_{(v,a)}= \vec{z}_v\cdot \sigma(a\mid v)$, where $\vec{z}$ is the unique invariant distribution of the chain induced by $\sigma$.

````{prf:lemma} NEEDS TITLE 5-lem:sol-strat-correspondence
:label: 5-lem:sol-strat-correspondence

Let $X$ be the set containing exactly those solutions $\vec{x}$ of $\mathcal{L}_{\mathit{mp}}$ for which the strategy  $\Psi(\vec{x})$ induces a strongly connected Markov chain. Then the mappings $\Psi$ and $\Xi$ are bijections between $X$ and the set of all memoryless strategies in some sub-MDP of $\mathcal{M}$ that induce a strongly connected Markov chain.

````

````{admonition} Proof
:class: dropdown tip

A straightforward computation shows that $\Xi\circ\Psi$ and $\Psi\circ\Xi$ are identity functions on the respective sets.

````

````{prf:definition} NEEDS TITLE 5-def:pure-lp
:label: 5-def:pure-lp

A solution $\vec{x}$ of $\mathcal{L}_{\mathit{mp}}$is **pure** if for every vertex $v$ there is at most one action $a$ such that $\vec{x}_{(v,a)}>0$.

````

The following lemma follows from the way in which strategies $\sigma$ and $\sigma^*$ were constructed in the previous sub-section.

````{prf:lemma} NEEDS TITLE 5-lem:pure-lpsol
:label: 5-lem:pure-lpsol

Let $\bar{\vec{x}}$ be a pure optimal solution of $\mathcal{L}_{\mathit{mp}}$ and denote $ S = \{v \in  V\mid \exists a \text{ s.t. } \bar{\vec{x}}_{(v,a)}>0\} $. Then the strategy $\sigma=\Psi( \bar{\vec{x}})$ is an MD strategy in $\mathcal{M}_{ S}$. Hence, in such a case, the strategy $\sigma^*$ constructed from $ \sigma $ as in {prf:ref}`5-thm:mp-rand-opt-main` is an optimal MD strategy in $\mathcal{M}$.

````

It remains to show how to find a pure optimal solution of $\mathcal{L}_{\mathit{mp}}$. To this end we exploit some fundamental properties of linear programs.

A linear program is in the **standard** (or equational) form if its set of constraints can be expressed as $A\cdot \vec{x} = \vec{b}$, $\vec{x}\geq 0$, where $\vec{x}$ is a vector of variables, $\vec{b}$ is a non-negative vector, and $A$ is a matrix of an appropriate dimension. In this notation, all the vectors are column vectors, i.e. $A$ has one column per each variable. Note that $\mathcal{L}_{\mathit{mp}}$ is a program in the standard form. A feasible solution $\vec{x}$ of such a program is **basic** if the columns of $A$ corresponding to variables whose value is positive in $\vec{x}$ form a linearly independent set of vectors. Since the maximal number of linearly independent columns equals the maximal number of linearly independent rows (a number called a **rank** of $A$), we know that each basic feasible solution has at most as many positive entries as there are rows of $A$. 

The next two lemmas prove some fundamental properties of basic feasible solutions.

````{prf:lemma} NEEDS TITLE 5-lem:basic-cond-unique
:label: 5-lem:basic-cond-unique

Assume that a linear program in a standard form has two basic feasible solutions $\vec{x},\vec{x}'$ such that both solutions have the same set of non-zero components, and the cardinality of this set equals the number of equality constraints in the program. Then $\vec{x}=\vec{x}'$.

````

````{admonition} Proof
:class: dropdown tip

Write $A\cdot \vec{x} = \vec{b}$ the equational constraints of the LP.
If $\vec{x}$ is a basic feasible solution, then it solves the equation $A_{N} \cdot \vec{x}_N = \vec{b}$, where $A_N$ ($  N$ stands for `non-zero') is obtained from $A$ by removing all columns corresponding to zero components of $\vec{x}$, and   $\vec{x}_N$ is obtained from $\vec{x}$ by removing all zero components. 

Since $\vec{x}$ has as many non-zero components as there are rows of $A$, it follows that $A_N$ is a square matrix. Since $\vec{x}$ is a basic solution, $A_N$ is regular (its columns are linearly independent) and $\vec{x}=A_{N}^{-1}\cdot \vec{b}$ is uniquely determined by $A_N$. Repeating the same argument for $\vec{x}'$ yields $\vec{x}'=A_{N}^{-1}\cdot \vec{b}= \vec{x}$.

````

````{prf:lemma} NEEDS TITLE 5-lem:basic-sol
:label: 5-lem:basic-sol

If a linear program in a standard form has an optimal solution, then it has also a basic optimal solution. Moreover, a basic optimal solution can be found in polynomial time.

````

````{admonition} Proof
:class: dropdown tip

The existence of a basic optimal solution is a well-known linear programming fact, e.g. the standard simplex algorithm works by traversing the set of basic feasible solutions until it finds an optimal one {cite}`Matousek:2007`. For computing an optimal basic solution, we can use one of the polynomial-time interior-point methods for linear programming, such as the path-following method {cite}`Karmarkar:1984,Gonzaga:1992`. While these methods work by traversing the interior of the polyhedron of feasible solutions, they converge, in polynomial time, to a point that is closer to the optimal basic solution than to all the other basic solutions. By a process called **purification,** such a point can be then converted to the closest basic solution, i.e. to the optimal one {cite}`Gonzaga:1992`.

````

````{prf:theorem} NEEDS TITLE 5-thm:lpmp-basic-dim
:label: 5-thm:lpmp-basic-dim

One can find, in polynomial time, an optimal deterministic strategy in a given strongly connected  mean-payoff MDP.

````

````{admonition} Proof
:class: dropdown tip

First, we use {prf:ref}`5-lem:basic-sol` to find a basic optimal solution $\bar{\vec{x}}$ of $\mathcal{L}_{\mathit{mp}}$.
We check if it is pure. If yes, we are done. Otherwise,

there is $v\in  V$ and two distinct actions $a,b$ such that $\bar{\vec{x}}_{(v,a)}>0$ and $\bar{\vec{x}}_{(v,b)}>0.$ Let $ S = \{v \in  V\mid \exists a \text{ s.t. } \bar{\vec{x}}_{(v,a)}>0\} $. By {prf:ref}`5-cor:mp-scc-extraction`, we can partition $S$ into several subsets, each of which induces a strongly connected sub-MDP of $\mathcal{M}$. Let $Q$ be a class of this partition containing $v$. We have that the optimal mean-payoff value of every vertex in $\mathcal{M}_Q$ is the same as in $\mathcal{M}$. This is because, 
as in the beginning of the proof of {prf:ref}`5-cor:mp-scc-optimality`, we can transform $\bar{\vec{x}}$ into another optimal solution of the same value as $\bar{\vec{x}}$ which has non-zero entries only for components indexed by $(q,a)$ with $q\in Q$. All these computations can be easily implemented in polynomial time.

We argue that $Q$ is a strict subset of $V$. Indeed, assume that $Q= V$. Then $\bar{\vec{x}}$ induces a randomized strategy $\sigma$ in $\mathcal{M}$. Moreover, since $\bar{\vec{x}}$ is a basic solution, it has at most $| V|+1$ positive entries, and since it is non-pure, it must have exactly $n+1$ positive entries, i.e. {prf:ref}`5-lem:basic-cond-unique` is applicable to $\bar{\vec{x}}$, since $\mathcal{L}_{\mathit{mp}}$ has exactly $| V|+1$ constraints. Now we define a new strategy $\sigma'$ in $\mathcal{M}$ by slightly changing the behaviour in $v$. To this end, choose some $\varepsilon>0$ and put $\sigma'(a\mid v)=\sigma(a\mid v)- \varepsilon$ and $\sigma'(b\mid v)=\sigma(b\mid v)+ \varepsilon$; we choose $\varepsilon$ small enough so that both quantities are still non-zero. The chain $\mathcal{M}^{\sigma'}$ is still strongly connected. Now let $\vec{x}' = \Xi(\sigma')$. Then $\vec{x}'$ is a solution of $\mathcal{L}_{\mathit{mp}}$ which is still basic, with a set of non-zero components being the same as in $\bar{\vec{x}}$. At the same time, $\vec{x}'\neq  \bar{\vec{x}}$, since $\sigma\neq {\sigma'}$ and $\Xi$ is a bijection ({prf:ref}`5-lem:sol-strat-correspondence`). But this is a contradiction with {prf:ref}`5-lem:basic-cond-unique`.

Hence, $\mathcal{M}_Q$ is a strict sub-MDP of $\mathcal{M}$ in which the value of every vertex is the same as in the original MDP. We can perform a recursive call of the aforementioned computation on $\mathcal{M}_Q$ (compute basic optimal solution of $\mathcal{L}_{\mathit{mp}}$, check purity, possibly extract and recurse on a sub-MDP).
The depth of recursion is bounded by $| V|$, so the running time is polynomial. Since each sub-MDP obtained during the recursion is non-empty, and the size of the MDPs decreases, the recursion must eventually terminate with a basic optimal solution (in some sub-MDP $\mathcal{M}'$) that is pure. This yields a memoryless deterministic strategy in $\mathcal{M}'$ whose value is equal to the optimal value in $\mathcal{M}.$ Such a strategy can be extended to whole $\mathcal{M}$ by solving almost sure reachability to $  \mathcal{M}' $, as described in the previous sub-section.

````

