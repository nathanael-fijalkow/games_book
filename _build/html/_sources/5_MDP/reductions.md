(5-sec:reductions)=
# Reductions to optimal reachability

```{math}

\renewcommand{\Game}{\game}

```

The MEC decomposition can be used to reduce several optimization problems (including general mean-payoff optimization) to optimizing reachability probability. Recall that in the optimal reachability problem, we are given an MDP $\mathcal{M}$ (with coloured vertices) and a colour $Win \in C$. The task is to find a strategy $\sigma$ that maximizes $  \mathbb{P}^\sigma_{ v_0}( \mathtt{Reach}( Win))$, the probability of reaching a vertex coloured by $Win$. The main result on reachability MDPs, which we prove in Section {ref}`5-sec:general-reachability`, is as follows:

````{prf:theorem} Solving reachability MDPs
:label: 5-thm:quant-reachability-main

In reachability MDPs, the value of each vertex is rational and computable in polynomial time. Moreover, we can compute, in polynomial time, a memoryless deterministic strategy that is optimal in every vertex.

````

## From optimal B&uuml;chi to reachability

In B&uuml;chi MDPs, the vertices are assigned colours from the set $\{1,2\}$ and our aim is to find a strategy maximizing $  \mathbb{P}^\sigma_{ v_0}( \mathtt{Buchi})$, i.e. maximizing the probability that a vertex coloured by $2$ is visited infinitely often.
We say that a MEC $M$ of a B&uuml;chi MDP is **good** if it contains a vertex coloured by 2.

````{prf:theorem} Solving B&uuml;chi MDPs
:label: 5-thm:quant-buchi

In B&uuml;chi MDPs, the value of each vertex is rational and computable in polynomial time. Moreover, we can compute, in polynomial time, a memoryless deterministic strategy that is optimal in every vertex.

````

````{admonition} Proof
:class: dropdown tip

Let $\mathcal{M}_b$ be a B&uuml;chi MDP and let $\mathcal{M}_r$ be a reachability MDP obtained from $\mathcal{M}_b$ by repainting each vertex belonging to a good MEC with the colour $Win$. Note that $\mathcal{M}_r$ can be computed in polynomial time by performing the MEC decomposition of $\mathcal{M}_b$ ({numref}`5-algo:MEC-decomposition`) and checking goodness of each MEC.

We prove that the value of each vertex in $\mathcal{M}_b$ is equal to the value of the corresponding vertex in $\mathcal{M}_r$.

First, fix any $\sigma$ and $v_0$ (due to equality of underlying graphs, we can view these as a strategy/initial vertex both in $\mathcal{M}_b$ and $\mathcal{M}_r$). By {prf:ref}`5-lem:EC-inf`, the probability of visiting infinitely often a vertex outside of a MEC is 0. Hence, the probability of visiting infinitely often a vertex coloured by 2 (in $\mathcal{M}_b$) is the same as the probability of visiting infinitely often a vertex coloured by 2 which belongs to (a necessarily good) MEC, which is in turn bounded from above by the probability that $\sigma$ visits (in $\mathcal{M}_r$) a vertex coloured by $Win$.

Conversely, let $\sigma^*$ be the MD reachability-optimal strategy in $\mathcal{M}_r$ (which exists by {prf:ref}`5-thm:quant-reachability-main`). We construct a strategy $\sigma$ in $\mathcal{M}_b$ which achieves, in every vertex, the same B&uuml;chi-value as the reachability value achieved in that vertex by $\sigma^*$ in $\mathcal{M}_r$. Outside of any good MEC, $\sigma$ behaves exactly as $\sigma^*$. Inside a good MEC $M$, $\sigma$ behaves as the MD strategy from {prf:ref}`5-lem:EC-sweep`, ensuring that some fixed vertex in $M$ of colour $2$ is almost-surely visited infinitely often. Since $\sigma$ is stitched together from MD strategies on non-overlapping domains, it is memoryless deterministic and it ensures that once a good MEC is reached, the B&uuml;chi condition is satisfied almost-surely.

The construction of $\sigma$ in the aforementioned paragraph is effective: given the optimal strategy $\sigma^*$ for reachability, $\sigma$ can be constructed in polynomial time.

````

## From optimal parity to optimal reachability

In parity MDPs, the vertices are labelled by colours form the set $\{1,\dots,d\}$ (w.l.o.g. we stipulate that $d\leq | V|$) and the goal is to find a strategy maximizing $  \mathbb{P}^\sigma_{ v_0}( \mathtt{Parity}),$ i.e. maximizing the probability that the largest priority appearing infinitely often along a play is even.

````{prf:theorem} Solving parity MDPs
:label: 5-thm:parity-main

In Parity MDPs, the value of each vertex is rational and computable in polynomial time. Moreover, we can compute, in polynomial time, a memoryless deterministic strategy that is optimal in every vertex.

````

````{admonition} Proof
:class: dropdown tip

Let $\mathcal{M}_p$ be a parity MDP. We will proceed similarly to {prf:ref}`5-thm:quant-buchi`, constructing a reachability MDP $\mathcal{M}_r$ with the same underlying graph as $\mathcal{M}_p$.

To this end, let $\mathcal{M}_i$ be the largest sub-MDP of $\mathcal{M}_p$ containing only the vertices of priority $\leq i$. Formally, we set $V_i =  W_{=1}( \mathcal{M}_p, \mathtt{Safe}( c^{-1}(\{i+1,\ldots,d\})) )$ and define $\mathcal{M}_i$ to be the sub-MDP induced by $V_i$ (note that $\mathcal{M}_i$ might be empty). We say that a vertex of $\mathcal{M}_p$ is $i$-good if it is contained in some MEC $M$ of $\mathcal{M}_i$ such that the largest vertex priority inside $M$ is equal to $i$. We say that a vertex is even-good if it is $i$-good for some even $i$. We set up a reachability MDP $\mathcal{M}_r$ by taking $\mathcal{M}_p$ and re-colouring each its even-good vertex with colour $Win$. To do this, we need to compute, for each even priority $i$, the MDP $\mathcal{M}_i$ and its MEC-decomposition. This can be done in polynomial time ({numref}`5-algo:MEC-decomposition`). 

We again prove that the value of every vertex in $\mathcal{M}_p$ is equal to the value of the corresponding vertex in $\mathcal{M}_r$.

Let $\sigma$ and $v_0$ be arbitrary. By {prf:ref}`5-lem:EC-inf`, $\mathbb{P}^\sigma_{ \mathcal{M}_p, v_0}( \mathtt{Parity})$ is equal to the probability that $\mathtt{Inf}( \pi)$  is an EC in which the largest priority is even. But each such EC is also an EC of some $\mathcal{M}_i$ with even $i$, and thus is also contained in a MEC of a $\mathcal{M}_i$ in which the largest priority is $ i $. Hence, $\mathbb{P}^\sigma_{ \mathcal{M}_p, v_0}( \mathtt{Parity})\leq  \mathbb{P}^\sigma_{ \mathcal{M}_r, v_0}( \mathtt{Reach}( Win))$.

Conversely, let $\sigma^*$ be the MD reachability-optimal strategy in $\mathcal{M}_r$. We construct an MD strategy $\sigma$ in $\mathcal{M}_p$ as follows: in a vertex $v$ which is not even-good, $\sigma$ behaves as $\sigma^*$. For a vertex $v$ that is even-good, we identify the smallest even $i$ such that $v$ is $i$-good. 
This means that $v$ belongs to some MEC $M$ of $\mathcal{M}_i$ in which the largest priority is $i$. 
By {prf:ref}`5-lem:EC-sweep`, we can compute, in polynomial time, an MD strategy $\sigma_M$ which ensures that the largest-priority vertex in $( \mathcal{M}_i)_M$ is visited infinitely often, and we set $\sigma(v)$ to $\sigma_M(v)$. Note that given $\sigma^*$, the strategy $\sigma$ can be constructed in polynomial time. It remains to show that $\mathbb{P}^\sigma_{ \mathcal{M}_p, v_0}( \mathtt{Parity})\geq  \mathbb{P}^{\sigma^*}_{ \mathcal{M}_r, v_0}( \mathtt{Reach}( Win))$.

By the construction of $\sigma$, once we reach a vertex which is $i$-good for some even $i$, all the following vertices will be $j$-good for some even $j\leq i$. From this and from {prf:ref}`5-lem:EC-inf` it follows that $\mathbb{P}^{\sigma^*}_{ \mathcal{M}_r, v_0}( \mathtt{Reach}( Win))$ is equal to the probability that $\sigma$ produces a play $\pi$ with the following property: $\exists i \text{ even}$ such that all but finitely many vertices on $\pi$ are $i$-good but are not $j$-good for any even $j<i$. This can be in turn rephrased as the probability that $\mathtt{Inf}( \pi)$ is an EC whose all vertices are $i$-good for some even $i$ but none of them is $j$-good for an even $j<i$; we call such an EC **$i$-definite**. But within such an EC, $\sigma$ forever behaves as $\sigma_M$ for some MEC $\mathcal{M}$ of $\mathcal{M}_i$ in which the maximal priority is $i$. Hence, once an $i$-definite EC is reached, the strategy almost-surely ensures that priority $i$ is visited infinitely often and ensures that no larger priority is ever visited. It follows that  $\mathbb{P}^{\sigma^*}_{ \mathcal{M}_r, v_0}( \mathtt{Reach}( Win)) =  \mathbb{P}^{\sigma}_{ \mathcal{M}_p, v_0}(\inf( \pi) \text{ is $i$-definite for even }i ) =  \mathbb{P}^{\sigma}_{ \mathcal{M}_p, v_0}( \mathtt{Parity}).$

````

## From general mean-payoff to optimal reachability

We already know how to solve strongly connected mean-payoff MDPs. We now combine this result with MEC decomposition to reduce the general (not strongly connected) mean-payoff optimization to MDP reachability.

We start with a strengthening of {prf:ref}`5-thm:mp-valcomp`.

````{prf:lemma} NEEDS TITLE 5-lem:MEC-mp-strict-bound
:label: 5-lem:MEC-mp-strict-bound

Let $\mathcal{M}$ be a strongly connected mean-payoff MDP and $r^*$ the value of each of its vertices. Then, for each $\sigma$ and $v_0$ we have $\mathbb{P}^\sigma_{ v_0}(  \mathtt{MeanPayoff}^{\;-} > r^*) = 0 $.

````

````{admonition} Proof
:class: dropdown tip

Assume that the statement is not true. Then there exist $\sigma, v_0$ as well as numbers $\epsilon,\delta>0 $ and $n_0 \in  \mathbb{N}$ s.t. the probability of the following set of plays $X_{\epsilon,n_0}$ is at least $\delta$: a play $\pi$ belongs to $X_{\epsilon,n_0}$ if for every $n\geq n_0$ it holds $\frac{1}{n}\sum_{i=0}^{n-1} c( \pi_i) \geq x^* +  \varepsilon$. We construct a new strategy $\sigma'$, which proceeds in a series of episodes. Every episode starts in $v_0$, and for the first $n_0$ steps of the, episode $\sigma'$ mimics $\sigma$. After that, it checks, in every step $n$, whether the payoff accumulated since the start of the episode is at least $n\cdot(r^* +  \varepsilon)$. If this holds, we mimic $\sigma$ for one more step. If the inequality is violated, we immediately restart, i.e. return to $v_0$ (can be performed with probability $1$ due to the MDP being strongly connected) and once in $v_0$, start a new episode which mimics $\sigma$ from the beginning. By our assumption, the probability of not performing a reset in a given episode is at least $\delta>0$. Hence, with probability $1$ we witness only finitely many resets, after which we produce a play whose suffix has mean-payoff at least $r^* + e$. By prefix independence of mean-payoff ({prf:ref}`5-thm:mp-valcomp`), $\mathbb{E}^{\sigma'}_{ v_0} [  \mathtt{MeanPayoff}^{\;-}] \geq r^* +  \varepsilon,$ a contradiction.

````

We will need to strengthen the previous lemma so that it applies not only to strongly connected MDPs, but also to MECs in some larger MDPs. The strengthening is performed in the following two lemmas. The first lemma says that once we exit a MEC, with some positive probability we will never return.

````{prf:lemma} NEEDS TITLE 5-lem:MEC-noreturn
:label: 5-lem:MEC-noreturn

Let $  M $ be a MEC of an MDP $  \mathcal{M} $ and let $ v\in  M $, $ a\in  A $ be such that $ a $ **is not** $  M $-safe in $ v $. Then there exists $ t $ s.t. $  \Delta(t\mid v,a)>0 $ and  $ t \not \in  W_{=1}( \mathcal{M}, \mathtt{Reach}( M)) $.

````

````{admonition} Proof
:class: dropdown tip

Assume that $ a $ is not $  M $-safe in $ v $ and that all $ t $'s with $  \Delta(t\mid v,a)>0 $ belong to $  W_{=1}( \mathcal{M}, \mathtt{Reach}( M)) $. Fix the MD strategy $  \sigma $ which is almost-surely winning for reaching $  M $ from each vertex of $  W_{=1}( \mathcal{M}, \mathtt{Reach}( M)) $ ({prf:ref}`5-thm:as-char`). For each $ t $ s.t.  $  \Delta(t\mid v,a)>0 $, let $  M_t $ denote the set of vertices which can be (with a positive probability) visited under $ \sigma $. Put $  M' =  M \cup (\bigcup_{t\in  V, \Delta(t\mid v,a)>0} M_t )$. Then $  M' $ is closed, since $  M $ is closed and since for every $ u $ in some $  M_t $ there exists an action (the one selected by $ \sigma $ for $ u $) under which we surely stay in $  M_t $. Moreover, the $  M'$-induced sub-MDP is strongly connected: each $ t $ with $  \Delta(t\mid v,a)>0 $ is reachable from within $  M $ (through $ v $) and thus each vertex in some $M_t $ is reachable from $  M $. In turn, from each vertex in some $  M_t $ (where $  \Delta(t\mid v,a)>0 $) we can reach $  M $ without leaving $  M_t $, due to the definition of $ \sigma $. Hence, $  M' $ is a MEC which strictly contains $  M $, a contradiction with the maximality of $  M. $

````

Given a play $\pi$ and strategy $\sigma$, we define a **slice** of $\sigma$ as a strategy $\sigma_{ \pi-}$ such that for each $\pi'$ starting in $last( \pi)$ it holds $\sigma_{ \pi-}( \pi') = \sigma( \pi \pi')$, while on other plays $\sigma_{ \pi-}$ just mimics $\sigma$.

````{prf:lemma} NEEDS TITLE 5-lem:MEC-stable
:label: 5-lem:MEC-stable

Let $M$ be a MEC of $\mathcal{M}$ and $r^*$ the mean-payoff value of every vertex in the strongly connected sub-MDP induced by $M$. Then the set $E$ of all plays that have $\mathtt{Inf}( \pi)\subseteq M$ and at the same time mean payoff greater than $r$ has probability zero under any strategy $\sigma$.

````

````{admonition} Proof
:class: dropdown tip

 Assume, for contradiction, that there is a strategy $\sigma$ and $\delta > 0$ such that the probability of $E$ under $ \sigma  $ is at least $\delta$. Note that we do not immediately have a contradiction with {prf:ref}`5-lem:MEC-mp-strict-bound`, since $\sigma$ might leave $M$ (and then return back). 
 
 We say that a play $  \pi $ **cheats** in step $ i $ if it is inside $  M $ in $ i $-th step and outside of $  M $ in the next step (which can only be caused by an $  M $-unsafe action being played). From {prf:ref}`5-lem:MEC-noreturn` we have that there is $ p>0 $ s.t. upon every exit from $  M $ we return with probability at most $ (1-p) $. Hence, the probability that a play cheats infinitely often is $ 0 $. It follows that there is $ k\in  \mathbb{N} $ s.t. $  \mathbb{P}_{ v_0}^\sigma( \pi \text{ cheats after $\geq k $ steps}) \leq (\delta\cdot p_{\min})/4 $, where $ p_{\min} $ is the smallest non-zero edge probability in $  \mathcal{M} $. 
 
 Whenever we are in some $ v\in  M $ and play an action that is not $  M $-safe in $ v $, this results into a cheat with  probability at least $ p_{\min} $. Thus, the total probability that this happens after at least $ k $ steps, i.e. the quantity 
$$

q= \sum_{i \geq k}\;\sum_{v\in  M}\;\sum_{a \text{ not $  M $-safe in v}} \mathbb{E}^\sigma_{ v_0}[ \actevent{\sigma}{a}{i}\cdot \mathbf{1}_{  Out( \pi_i)= v} ] , 
$$ (5-eq:mec-cheat)

 is bounded by $  \mathbb{P}_{ v_0}^\sigma( \pi \text{ cheats after more than $ k $ steps})/p_{\min} \leq \delta/4$.
 
 Let's go back to $ E $ now. On each play in $ E $ there is a step $ i $ from which on the play stays in $  M $ forever: we say that the play is $ i $-definite and we denote by $E_k$ the set of all $ i $-definite plays in $ E $. By union bound, there is $ \ell \in  \mathbb{N}, \ell \geq k $ s.t. $  \mathbb{P}_{ v_0}^\sigma(E_\ell)  \geq \delta/2$. 
 
 We define a new strategy $ \sigma' $ as follows: on each play prefix, $ \sigma' $ by default mimics $ \sigma $, except for the case when at least $ \ell $ steps have elapsed, the current vertex $ v $ is in $  M $, and $ \sigma $ prescribes to play, with positive probability, an action which is not $  M $ safe in $ v $. In such a case, $ \sigma $ is overridden and we play any action that is $  M $-safe in $ v $ instead (after which we return to simulating $ \sigma $, until the override kicks in again). The probability that such an override happens is bounded by the quantity $ q $ from {eq}`5-eq:mec-cheat`, and hence by $ \delta/4 $. Since  $  \mathbb{P}_{ v_0}^\sigma(E_\ell)  \geq \delta/2$, at least half the measure of $ E_{\ell} $ stays untouched by the overrides; hence  $  \mathbb{P}_{ v_0}^{\sigma'}(E_\ell)\geq \delta/4 $.
 
 We are ready to apply the final argument. There are only finitely many plays of length $ \ell $. Hence, by union bound, there is a play $  \pi $ of length $ \ell $ such that $\mathbb{P}_{ v_0}^{\sigma'}(E_\ell \cap  \mathit{Cyl}( \pi))>0$. Consider the strategy  $\sigma'_{ \pi-}$. 
 Starting in $  last( \pi) $, we have that $\sigma'_{ \pi-}$ never leaves $  M $, due to the overrides in $ \sigma' $. Hence, $\sigma'_{ \pi-}$ can be seen as a strategy in the strongly connected MDP $  \mathcal{M}_M $. Now consider the set $ E'=\{ \pi'\mid  \pi'\exists \pi''\in E \text{ s.t. }  \pi''= \pi \pi'\} $. Then $  \mathbb{P}_{ last( \pi)}^{ \sigma'_{ \pi-}}(E') =  \mathbb{P}_{ v_0}^{\sigma'}(E_\ell \cap  \mathit{Cyl}( \pi))>0 $; but due to the prefix independence of mean payoff, all plays in $ E' $ have payoff $ > r^* $, a contradiction with {prf:ref}`5-lem:MEC-mp-strict-bound`.

````

````{prf:theorem} NEEDS TITLE 5-thm:general-mp-main
:label: 5-thm:general-mp-main

In mean-payoff MDPs, the value of each vertex is rational and computable in polynomial time. Moreover, we can compute, in polynomial time, a memoryless deterministic strategy that is optimal in every vertex.

````

````{admonition} Proof
:class: dropdown tip

First, note that we can w.l.o.g. restrict to MDPs in which each edge is coloured by a number between $0$ and $ 1 $. To see this, let $\mathcal{M}$ be an MDP and $a,b$ any two numbers, with $a$ non-negative. We can construct an MDP $\mathcal{M}'$ by re-colouring each edge $(u,v)$ of $\mathcal{M}$ with colour $a\cdot  c(u,v)+b$, where $c$ is the original colouring in $\mathcal{M}$. It is then easy to see that for each strategy $\sigma$ it holds $\mathbb{E}_{ \mathcal{M}, v_0}^\sigma[  \mathtt{MeanPayoff}^{\;-}]=( \mathbb{E}_{ \mathcal{M}', v_0}^\sigma[  \mathtt{MeanPayoff}^{\;-}]/a)-b$, so a strategy optimizing the mean payoff in $\mathcal{M}'$ is also optimal in $\mathcal{M}$. Hence, we always can re-scale the colouring into the unit interval while preserving the optimization criterion.

So now let $\mathcal{M}_\mathit{mp}$ be a mean-payoff MDP with edge-colouring $c$. We construct, in polynomial time, a new reachability MDP $\mathcal{M}_r$ as follows: first, we compute the MEC decomposition of $\mathcal{M}_\mathit{mp}$ ({numref}`5-algo:MEC-decomposition`). Let $M_1,\dots, M_k$ be all the resulting MECs. For each MEC $M_i$ we compute the optimal mean-payoff value $r_i^*$ in the sub-MDP induced by $M_i$ (which is shared by all vertices of this sub-MDP, by {prf:ref}`5-thm:mp-valcomp`), along with the corresponding memoryless deterministic optimal strategy. We already know how to do this in polynomial time ({prf:ref}`5-thm:mp-rand-opt-main` and {prf:ref}`5-thm:lpmp-basic-dim`). Now we add new vertices $v_{\mathit{good}}$, $v_{\mathit{bad}}$, both with self loops, and edges incoming to these vertices from each vertex that belongs to some MEC of $\mathcal{M}_\mathit{mp}$. The vertex $v_{\mathit{good}}$ is the only vertex coloured by $Win$ in $\mathcal{M}_r$. Finally, we add a new action $fin$ which behaves as follows: For each vertex $v$ belonging to a MEC $M_i$ we set $\Delta( v_{\mathit{good}}\mid v, fin) = r^*_i$ and $\Delta( v_{\mathit{bad}}\mid v, fin) = 1-r^*_i $. In a non-MEC vertex $ v $, we put $  \Delta(v, fin) =  \Delta(v,a) $ for some $ a\in  A $, $ a\neq  fin $, so that no new behaviour is introduced in these vertices.

We show that for any original vertex (i.e. all vertices but $v_{\mathit{good}}, v_{\mathit{bad}}$) the optimal values in both MDPs are the same and the optimal strategies are easily transferable from one MDP to the other.

First, let $\sigma$ be an $\varepsilon$-optimal strategy in $\mathcal{M}_\mathit{mp}$. 

We have $\mathbb{E}^\sigma_{ v_0}[  \mathtt{MeanPayoff}^{\;-}] = \sum_{i=1}^k \mathbb{E}^\sigma_{ v_0}[  \mathtt{MeanPayoff}^{\;-}\cdot  \mathbf{1}_{ \mathtt{Inf}\subseteq M_i}] \leq \sum_{i=1}^k  \mathbb{E}^\sigma_{ v_0}[r_i^*\cdot  \mathbf{1}_{ \mathtt{Inf}= M_i}] = \sum_{i=1}^k r_i^* \cdot  \mathbb{P}_{ v_0}^\sigma( \mathtt{Inf}= M_i) $; here the first equation follows from {prf:ref}`5-lem:EC-inf` and the subsequent inequality from {prf:ref}`5-lem:MEC-stable`. Moreover, for each $i$ there is a number $n_0^i$ such that the probability of all plays that stay inside $M_i$ in all the steps from $n_0^i$ to infinity is at least $\mathbb{P}_{ v_0}^\sigma( \mathtt{Inf}\subseteq M_i) - \frac{ \varepsilon}{k} $. Let $n_0 = \max_{1\leq i \leq k} n^i_0$.

We construct a reachability strategy $\sigma_r$ which mimics $\sigma$ for the first $n_0$ steps. After $n_0$ steps it performs a switch: if the current vertex is in some $M_i$ we immediately play the action $fin$, otherwise we start to behave arbitrarily. We have $\mathbb{P}_{ v_0}^{\sigma_r}( \mathtt{Reach}( Win)) \geq \sum_{i=1}^{k} r_i^* \cdot  \mathbb{P}_{ v_0}^{\sigma_r}( last( \pi_{\leq n_0}) \in  M_i ) \geq \sum_{i=1}^k r_i^* \cdot  \mathbb{P}_{ v_0}^\sigma( \mathtt{Inf}\subseteq M_i) -  \varepsilon \geq  \mathbb{E}^\sigma_{ v_0}[  \mathtt{MeanPayoff}^{\;-}] - \varepsilon$, the last equality shown in the previous paragraph. Since $\sigma$ is $\varepsilon$-optimal for mean-payoff, $\mathbb{P}_{ v_0}^{\sigma_r}( \mathtt{Reach}( Win))$ is at most $2 \varepsilon$ away from the mean-payoff value of $ v $. Since $\varepsilon>0$ was chosen arbitrarily, we get that the reachability value in $\mathcal{M}_{r}$ is at least as large as the mean-payoff value in $\mathcal{M}_{ \mathit{mp}}$.

Conversely, let $\sigma^*$ be the optimal MD strategy in $\mathcal{M}_r$. We say that $\sigma^*$ ends in a vertex $v$ if $\sigma^*(v)= fin$. We can assume that if $\sigma^*$ ends in some $v \in  M_i$ then it ends in all vertices of $M_i$. This is because whenever $\sigma^*$ ends in some vertex $v \in  M_i$, the reachability value of $v$ must be equal to $r^*_i$, otherwise playing $fin$ would not be optimal here. But the optimal reachability value in every vertex of a given MEC is the same (due to {prf:ref}`5-lem:EC-sweep`), so if playing $fin$ is optimal in some vertex of $M_i$, it is optimal in all such vertices. Now we can define an MD strategy $\sigma_{ \mathit{mp}}$ in $\mathcal{M}_\mathit{mp}$ to initially mimic $\sigma^*$, and upon encountering any MEC $M_i$ in which $\sigma^*$ ends, immediately switch to the MD strategy that is optimal in the mean-payoff sub-MDP $\mathcal{M}_i$. We have $\mathbb{E}^{\sigma_{ \mathit{mp}}}_{ v_0}[  \mathtt{MeanPayoff}^{\;-}]  =  \sum_{i=1}^{k}  \mathbb{P}^{\sigma^*}_{ v_0}(\text{end in } M_i)\cdot r^*_i =  \mathbb{P}^{\sigma^*}_{ v_0} ( \mathtt{Reach}( Win)). $ Since $\sigma^*$ as well as the optimal strategies in all $M_i$ can be computed in polynomial time ( {prf:ref}`5-thm:quant-reachability-main` and {prf:ref}`5-thm:lpmp-basic-dim`), we get the result.

````

