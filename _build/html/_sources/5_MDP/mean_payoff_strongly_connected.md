(5-sec:mean_payoff_strongly_connected)=
# Mean-payoff optimality in strongly connected MDPs


```{math}
\newcommand{\expv}{\mathbb{E}}
\newcommand{\probm}{\mathbb{P}}
\newcommand{\actions}{A}
\newcommand{\colouring}{c}
\newcommand{\probTranFunc}{\Delta}
\newcommand{\mdp}{\mathcal{M}}
\newcommand{\reachOP}{\mathcal{V}}
\newcommand{\discOP}{\mathcal{D}}
\newcommand{\lpmp}{\lp_{\mathit{mp}}}
\newcommand{\lpmpdual}{\lpmp^{\mathit{dual}}}
\newcommand{\MeanPayoffSup}{\MeanPayoff^{\;+}}
\newcommand{\MeanPayoffInf}{\MeanPayoff^{\;-}}
\newcommand{\mcprob}{P}
\newcommand{\invdist}{\vec{z}}
\newcommand{\playPay}{\textsf{p-Payoff}}
\newcommand{\stepPay}{\textsf{s-Payoff}}
\newcommand{\solvset}{S}
\newcommand{\N}{\mathbb{N}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\vertices}{V}
\newcommand{\ing}{\textrm{In}}
\newcommand{\play}{\pi}
\newcommand{\MeanPayoff}{\mathtt{MeanPayoff}}
\newcommand{\DiscountedPayoff}{\mathtt{DiscountedPayoff}}
```

As shown in the previous section, the optimal solution of any of the programs $\lp_{\mathit{mp}}, $\lp_{\mathit{mp}}{\mathit{dual}} gives us an upper bound on the optimal value. In this sub-section we show that in strongly connected MDPs: a) a value of every vertex is the same; b) from a solution of $\lp_{\mathit{mp}} one can extract a memoryless deterministic strategy $\sigma$ whose expected mean-payoff is well defined (i.e., the preconditions of  {prf:ref}`5-lem:limit-defined` are satisfied)) and equal to the objective value of the solution. Moreover, if the solution in question is optimal, then $ \sigma $ is optimal for both $\textsf{p-Payoff}- and $\textsf{s-Payoff}-semantics.

````{prf:definition} NEEDS TITLE 5-def:scc-mdp
:label: 5-def:scc-mdp

An MDP is **strongly connected** if for each pair of vertices $u,v$ there exists a strategy which, when starting in $u$, reaches $v$ with a positive probability. 

````

For the rest of this section we fix an optimal solution $\lpsol{x}_{v,a}$ of $\lp_{\mathit{mp}}. We denote by $S the set of all vertices for which there exists action $a$ s.t. $\lpsol{x}_{v,a}>0.$ From the shape of $\lp_{\mathit{mp}} it follows that $S is non-empty and closed, and hence we can consider a sub-MDP $\mdp_{S$ induced by $S. In $\mdp_{S$ we then define a memoryless randomized strategy $\sigma$ by putting 
$$
\sigma(a\mid v)=\frac{\lpsol{x}_{(v,a)}}{\sum_{b\in A\lpsol{x}_{(v,b)}}.
$$

Fixing a strategy $\sigma$ yields a **Markov chain** $\mdp_S{\sigma}$. Markov chain can be viewed as an MDP with a single action (and hence, with no non-determinism). $\mdp_{S^\sigma$ in particular can be viewed an MDP with the same vertices, edges, and colouring as $\mdp_S, but with a single action (as non-determinism was already resolved by $\sigma$). The probability of transitioning from a vertex $u$ to a vertex $v$ in a Markov chain is denoted by $\mcprob_{u,v}$. In $\mdp_{S^{\sigma}$ we have $\mcprob_{u,v}=\sum_{a\in A \Deltav\mid u,a)\cdot\sigma(a\mid u)$, the right-hand side being computed in the original MDP $\mathcal{M}. Both $\mdp_S and $\mdp_{S^{\sigma}$ have the same sets of plays and for each initial vertex, the probability measure induced by $\sigma$ in $\mathcal{M} equals the probability measure arising (under the unique policy) in $\mdp_{S^{\sigma}$. Hence, to prove anything about $\sigma$ it suffices to analyse $\mdp_{S^{\sigma}$.

> **A refresher on Markov chains.**

 We review some fundamental notions of Markov chain theory {cite}`Norris:1998`. A Markov chain that is strongly connected is called **irreducible**. The one-step transition probabilities in a Markov chain can be arranged into a square matrix $P, which has one row and one column for each vertex. The cell in the row corresponding to a vertex $u$ and in the column corresponding to a vertex $v$ bears the value $\mcprob_{u,v}$ defined above. An easy induction shows that the matrix $Pk$ contains $k$-step transition probabilities. That is, the probability of being in $v$ after $k$ steps from vertex $u$ is equal to the $(u,v)$-cell of $Pk$, which we denote by $P{(k)}_{u,v}$.

A vertex $u$ of a Markov chain is **recurrent** if, when starting from $u$, it is revisited infinitely often with probability $1$. On the other hand, if the probability that $u$ is re-visited only finitely often is one, then the vertex is **transient**. It is known~\cite[Theorem 1.5.3]{Norris:1998} that each vertex of a finite Markov chain is either recurrent or transient, and that these two properties can be equivalently characterized as follows: vertex $u$ is recurrent if and only if  $\sum_{k=0}^{\infty}P{(k)}_{u,u}=\infty$, otherwise it is transient.

An **invariant distribution** in a Markov chain with a vertex set $V is a $|V$-dimensional non-negative row vector $\vec{z} which adds up to $1$ and satisfies $ \vec{z}cdot P= \vec{z}.

The following lemma holds for arbitrary finite Markov chains.

````{prf:lemma} NEEDS TITLE AND LABEL 
\label{5-lem:MC-inv-rec}
Let $\vec{z} be an invariant distribution and $v$ a vertex such that $\invdist_v > 0$. Then $v$ is recurrent.
 

\label{5-lem:MC-inv-rec}
Let $\vec{z} be an invariant distribution and $v$ a vertex such that $\invdist_v > 0$. Then $v$ is recurrent.

````

````{admonition} Proof
:class: dropdown tip

Let $n$ be the number of vertices in the chain and $p_{\min}$ the minimum non-zero entry of $P.
Assume, for the sake of contradiction, that $v$ is transient. We show that in such a case, for each vertex $u$ it holds $\lim_{k\rightarrow\infty} P{(k)}_{u,v} = 0$. For $u=v$ this is immediate, since the sum $\sum_{k=0}^{\infty}P{(k)}_{v,v}$ converges for  transient $v$. Otherwise, let $f_{u,v,i}$ be the probability that a play starting in $u$ visits $v$ for the **first time** in exactly $i$ steps. Then $P{(k)}_{u,v}=\sum_{i=0}^k f_{u,v,i}\cdot P{(k-i)}_{v,v}$. Now when starting in a vertex from which $v$ is reachable with a positive probability, at least one of the following events happens with probability $\geq p_{\min}^n$ in the first $n$ steps: either we reach a vertex from which $v$ is not reachable with positive probability, or we reach $v$. If neither of the events happens, we are, after $n$ steps, still in a vertex from which $v$ can be reached with a positive probability. In such a case, the argument can be inductively repeated (analogously to the proof of  {prf:ref}`5-thm:as-char`) to show that $f_{u,v,i}\leq (1-p_{\min}^n)^{\lfloor\frac{i}{n}\rfloor}\leq (1-p_{\min}^n)^{\frac{i-n}{n}}$.

Since $\sum_{k=0}^{\infty}P{(k)}_{v,v}$ converges, for each $\eps>0$ there exists $j_\eps$ such that $\sum_{i=j_{\eps}}^{\infty}P{(i)}_{v,v} < \frac{\eps}{2}$. Similarly, there exists $\ell_\eps$ such that 
$$
\sum_{i=\ell_{\eps}}^{\infty}{(1-p_{\min}^n)^{\frac{i-n}{n}}} = \frac{(1-p_{\min}^n)^{\frac{\ell_\eps}{n}}}{\left(1-(1-p_{\min}^n)^{\frac{1}{n}}\right)\cdot(1-p_{\min}^n)}< \frac{\eps}{2},
$$
 and hence $\sum_{i=\ell_{\eps}}^{\infty} f_{u,v,i}< \frac{\eps}{2}.$

Now we put $m_{\eps}=\max\{j_\eps,\ell_\eps\}$. For any $k\geq 2m_{\eps}$ we have $P{(k)}_{u,v}=\sum_{i=0}^k f_{u,v,i}\cdot P{(k-i)}_{v,v} \leq \sum_{i=m_{\eps}}^{k}f_{u,v,i} + \sum_{i=0}^{m_{\eps}}P{(k-i)}_{v,v}\leq\sum_{i=m_{\eps}}^{k}f_{u,v,i} + \sum_{i=m_{\eps}}^{k}P{(i)}_{v,v}<\eps$ (note that all the series involved are non-negative). This proves that $P{(k)}_{u,v}$ vanishes in the limit.

Finally, we derive the contradiction. Since $\vec{z} satisfies $\vec{z}cdot P= \vec{z}, we also have $\vec{z}cdot Pk = \vec{z} for all $k$. Hence, the $v$-component of $\vec{z}cdot Pk$ is equal to $\invdist_v>0$. But as shown above, the $v$-column of $Pk$ converges to the all-zero vector as $k\rightarrow \infty$, so also $(\vec{z}cdot Pk)_v$ vanishes in the limit, a contradiction.

````



> **Towards the optimality of $ \sigma $.**

 We now turn back to the chain $\mdp_{S^{\sigma}$, where the memoryless strategy $ \sigma $ is obtained from the optimal solution of $ \lp_{\mathit{mp}}$. In general, $ \mdp_{S^{\sigma} $ does not have to be irreducible. Hence, we use the following lemma and its corollary to extract an irreducible sub-chain, to which we can apply known results of Markov chain theory.

````{prf:lemma} NEEDS TITLE 5-lem:mc-rec
:label: 5-lem:mc-rec

Let $\bar{\vec{z}$ be a vector such that for each $v\in S it holds $\bar{\vec{z}_v=\sum_{a\in A \lpsol{x}_{v,a}$. Then $\bar{\vec{z}$ is an invariant distribution of $\mdp_{S^{\sigma}$. Consequently, all vertices of $\mdp_{S^{\sigma}$ are recurrent.

````

````{admonition} Proof
:class: dropdown tip

The first part follows directly from the fact that $\lpsol{x}_{v,a}$ is a feasible solution of $\lp_{\mathit{mp}}. The second part follows from {prf:ref}`5-lem:MC-inv-rec` and from the fact that $\bar\vec{z} is positive (by the definition of $S).

````


````{prf:corollary} NEEDS TITLE 5-cor:mp-scc-extraction
:label: 5-cor:mp-scc-extraction

The set $S can be partitioned into subsets $\solvset_1,\solvset_2,\dots,\solvset_m$ such that each $\solvset_i$ induces a strongly connected sub-chain of $\mdp_{S^{\sigma}$.

````

````{admonition} Proof
:class: dropdown tip

Let $v\inS be arbitrary and let $U_v\subseteq S be the set of all vertices reachable with positive probability from $v$ in $\mdp_{S^{\sigma}$. Then $v$ is reachable (in $\mdp_{S^{\sigma}$) with positive probability from each $u\in U_v$: otherwise, there would be a positive probability of never revisiting $v$, a contradiction with each vertex being recurrent in $\mdp_{S^{\sigma}$ ( {prf:ref}`5-lem:mc-rec`). Hence, $U_v$ induces a strongly connected sub-MDP (or sub-chain) of $\mdp_{S^{\sigma}$. It is easy to show that if $U_v \neq U_w$ for some $v\neq w $, then the two sets must be disjoint.

````

Hence, we can extract from $S a set $Q$ inducing a strongly-connected sub-chain of $\mdp_{S^{\sigma}$, which we denote $\mathcal{M}{\sigma}_{Q}$. The set $Q$ also induces a strongly connected sub-MDP of $\mathcal{M} denoted by $\mdp_Q$. The chain $\mathcal{M}{\sigma}_{Q}$ arises by fixing, in $\mdp_Q$, a strategy formed by a restriction of $\sigma$ to $Q$. We use the following powerful theorem to analyse $\mathcal{M}{\sigma}_{Q}$.

````{prf:theorem} Ergodic theorem; see Theorem~1.10.2 in {cite}`Norris:1998`
:label: 5-thm:ergodic
 In a strongly connected Markov chain (with a finite set of vertices $V) there exists a unique invariant distribution $\vec{z}. Moreover, for every vector $\vec{h}\in \mathbb{R}{V$ the following equation holds with probability 1:

$$
\lim_{n \rightarrow \infty} \frac{1}{n} \sum_{i=0}^{n-1}\vec{h}_{\textrm{In}\pi_i)} = \sum_{v\inV \invdist_v\cdot \vec{h}_v.
$$

(In particular, the limit is well-defined with probability 1).

````


We can use the Ergodic theorem to shows that the expected mean-payoff achieved by $\sigma$ in $\mdp_{Q}$ matches the optimal value of $ \lp_{\mathit{mp}}$, in a very strong sense: the probability of a play having a mean-payoff equal to this optimal value is 1 under $ \sigma $.

````{prf:theorem} NEEDS TITLE 5-cor:mp-scc-optimality
:label: 5-cor:mp-scc-optimality

Let $\sigma_Q$ be the restriction of $\sigma$ to $Q$. Then for every $v\in Q$ it holds that $\mathbb{P}{\sigma_Q}_{\mdp_Q,v}(\mathtt{MeanPayoff}{\;-}= r^*)=1$, where $r^*$ is the is the optimal value of $\lp_{\mathit{mp}}. 

````

````{admonition} Proof
:class: dropdown tip

Let $ \vec{w}\in\mathbb{R}{V\timesA $ be a vector sych that $\vec{w}_{(v,a)}=\lpsol{x}_{(v,a)}/\sum_{(q,a)\in Q\timesA \lpsol{x}_{(q,a)}$ for every $(v,a)\in Q\times A, and $\vec{w}_{(v,a)}=0$ for all other $(v,a)$. We claim that $ \vec{w} $ is also an optimal solution of $\lp_{\mathit{mp}}. 

To prove feasibility, note that setting $\vec{w}_{(v,a)}=0$ for each $v\in Vsetminus Q$ does not break the constraints~\eqref{5-eq:mdp-flow}. This is because $Q$ induces a strongly connected sub-chain of $\mdp_{S^{\sigma}$, and hence there are no $v\in V, $u\in Vsetminus Q$ such that $\lpsol{x}_{(u,a)}\cdot \Deltav\mid u,a)>0$. Next,~\eqref{5-eq:mdp-flow} is invariant w.r.t. multiplication of variables by a constant, so normalizing the remaining values preserves~\eqref{5-eq:mdp-flow} and ensures that~\eqref{5-eq:mdp-freq-1} holds. 

To prove optimality, assume that the objective value of $\vec{w}$ is smaller than $r^*$. Then we can mirror the construction from the previous paragraph and produce a feasible solution ${\hat{\vec{w}}_{(v,a)}}$ whose $(Q\timesA$-indexed components are zero and the rest are normalized components of $\lpsol{x}$. Then $r^*$ is a convex combination of the objective values of $\vec{w}$ and $\hat{\vec{w}}$, so $\hat{\vec{w}}$ must have a strictly larger value than $r^*$, a contradiction with the latter's optimality.

We now plug $ \vec{w} $ into the ergodic theorem as follows: As in {prf:ref}`5-lem:mc-rec`, it easy to prove that setting $\invdist_v=\sum_{a\inA\vec{w}_{(v,a)}$ yields an invariant distribution. Now put $\vec{h}_v=\sum_{a\inA\sigma(a\mid v)\cdot cv,a)$ ($ =  \sum_{w \in V \mcprob_{v,w}\cdot cv,w)$). From the Ergodic theorem we get that $\lim_{n \rightarrow \infty} \frac{1}{n} \sum_{i=0}^{n-1}\vec{h}_{\textrm{In}\pi_i)}$ almost-surely exists and equals 
\begin{align}
\sum_{v\in Q} \invdist_v\cdot \vec{h}_v &= \sum_{v\in V \left(\big(\sum_{d\inA\vec{w}_{(v,d)}\big)\cdot \big(\sum_{a\inA\sigma(a\mid v)\cdot cv,a) \big)\right) \nonumber\\
&= \sum_{v\in Q} \left(\Bigg( \frac{\sum_{d\inA\lpsol{x}_{(v,d)}}{\sum\limits_{\substack{q\in Q\\ b\in A} \lpsol{x}_{(q,b)}} \Bigg)\cdot \Bigg( \frac{\sum_{a\inA\lpsol{x}_{(v,a)}\cdotcv,a)}{\sum\limits_{d\in  A \lpsol{x}_{(v,d)}} \Bigg) \right) \nonumber\\
&= \frac{1}{\sum\limits_{\substack{q\in Q\\ b\in A} \lpsol{x}_{(q,b)}}\cdot\sum\limits_{\substack{v\in Q\\ a\inA} \lpsol{x}_{(v,a)}\cdot cv,a) = \sum\limits_{\substack{v\in Q\\ a\inA} \vec{w}_{(v,a)}\cdotcv,a) =r^*.\label{5-eq:ergodic-use}
\end{align}

It remains to take a step from the left-hand side of~\eqref{5-eq:ergodic-use} towards the mean payoff. To this end, we construct a new Markov chain $\mdp_Q'$ from $\mdp_Q$ by splitting every edge $(u,v)$ with a new dummy vertex $d_{u,v}$ (i.e., $d_{u,v}$ has one edge incoming from $u$ with probability $\mcprob_{u,v}$ and one edge outgoing to $v$ with probability $1$). In $\mdp_Q'$ we define a vector $\vec{h}'$ s.t. for each vertex $d_{u,v}$ the vector $ \vec{h}' $ has the $ d_{u,v} $-component equal to $cu,v)$, while the components corresponding to the original vertices are zero. It is easy to check that $\mdp_Q'$  is strongly connected and that it has an invariant distribution $\vec{z}$ defined by $\vec{z}_v=\invdist_v/2$ for $v$ in $Q$ and $\vec{z}_{d_{u,v}}=\frac{\invdist_u\cdot\mcprob_{u,v}}{2}$ for $(u,v)$ an edge of $\mdp_Q$.
Also, by easy induction, for each play $\pi of length $n$ in $\mdp_Q$ it holds $\frac{1}{n}\sum_{i=0}^{n-1}c\play_i) = \frac{1}{n}\sum_{i=0}^{2n-1}\vec{h}'_{\textrm{In}\play_i')}$, where $\pi$ is the unique play in $\mdp_Q'$ obtained from $\pi by splitting edges with appropriate dummy vertices. Hence, 
\begin{equation}
\label{5-eq:mc-opt-limit}
\lim_{n\rightarrow \infty}\frac{1}{n}\sum_{i=0}^{n-1}c\play_i) = 2\cdot \lim_{n\rightarrow \infty}\frac{1}{n}\sum_{i=0}^{n-1}\vec{h}'_{\textrm{In}\play_i')},\end{equation} provided that both limits exist. By the ergodic theorem  applied to $\mdp_Q'$, we have that the RHS  limit in~\eqref{5-eq:mc-opt-limit} is defined with probability 1 and equal to
\begin{align*}
\underbrace{\sum_{v\in Q} \vec{z}_v \cdot \vec{h}'_{v}}_{=0} + \sum_{u,v\in Q} \vec{z}_{d_{u,v}}\cdot \vec{h}'_{d_{u,v}} = \frac{1}{2}\sum_{u\in Q}\invdist_u\cdot\left( \sum_{v\in Q}\mcprob_{u,v}\cdot cu,v)\right)\\ =\frac{1}{2}\sum_{u\in Q} \invdist_u\cdot \vec{h}_u=\frac{r^*}{2},
\end{align*}

the last equality being shown above. Plugging this into~\eqref{5-eq:mc-opt-limit} yields that if a limit on the LHS (i.e., the mean payoff of a play) is well-defined with probability 1, then it is equal to $r^*$ also with probability 1. But if there was a set $L$ of positive probability in $\mdp_Q$ with $\lim_{n \rightarrow \infty}\frac{1}{n}\sum_{i=0}^{n-1}c\play_i)$ undefined for each $\piin L$, by splitting the plays in $L$ we would obtain a positive-probability set of plays in $\mdp_Q'$ in which $\lim_{n \rightarrow \infty}\frac{1}{n}\sum_{i=0}^{n-1}\vec{h}'_{\textrm{In}\play_i')}$ is also undefined, a contradiction with the ergodic theorem. 

%
%

%\mathbb{E}{\bar\sigma_W}_{\mdp_{W},v}[\lim_{n \rightarrow \infty} \frac{1}{n} \sum_{i=0}^{n-1}h(\textrm{In}\pi_i))] &= \lim_{n \rightarrow \infty} \frac{1}{n}\sum_{i=0}^{n-1}\mathbb{E}{\bar\sigma_W}_{\mdp_{W},v}[h(\textrm{In}\pi_i))]\\

%&= \lim_{n \rightarrow \infty} \frac{1}{n}\sum_{i=0}^{n-1}\mathbb{E}{\bar\sigma_W}_{\mdp_{W},v}[c\play_i) ] = \mathbb{E}{\bar\sigma_W}_{\mdp_{W},v}[ \lim_{n \rightarrow \infty} \frac{1}{n}\sum_{i=0}^{n-1} c\play_i)].

%

%The first equality follows from the dominated convergence theorem and from the fact that the limit-average of $h$ is a.s. defined. For the last equality, we need to show that also $\lim_{n \rightarrow \infty} \frac{1}{n}\sum_{i=0}^{n-1} c\play_i)$ is a.s. defined. To this end, we construct a new Markov chain $\mdp_W'$ from $\mdp_W$ by splitting every edge $(u,v)$ with a new dummy vertex $d_{u,v}$ (i.e., $d_{u,v}$ has one edge incoming from $u$ with probability $\mcprob_{u,v}$ and one edge outgoing to $v$ with probability $1$). In $\mdp_W'$ we define a function $h'$ mapping each $d_{u,v}$ to $cu,v)$, and each other vertex to $0$. It is straightforward to check that $\mdp_W'$ is strongly connected and that for each play $\pi of length $n$ in $\mdp_W$ it holds $\sum_{i=0}^{n-1}c\play_i) = \sum_{i=0}^{2n-1}h'(\textrm{In}\play_i'))$, where $\pi$ is the unique play in $\mdp_W'$ obtained from $\pi by splitting edges with dummy vertices. Hence, we have $ $

% Hence, if there was a set $L$ of positive probability in $\mdp_W$ with $\lim_{n \rightarrow \infty}\frac{1}{n}\sum_{i=0}^{n-1}c\play_i)$ undefined for each $\piin L$, by splitting the plays in $L$ we would obtain a positive-probability set of plays in $\mdp_W'$ in which $\lim_{n \rightarrow \infty}\frac{1}{n}\sum_{i=0}^{n-1}h'(\textrm{In}\play_i'))$ is also undefined, a contradiction with the ergodic theorem.

````

So far, we have constructed an optimal strategy $\sigma_Q$ but only on the part $Q$ of the original MDP $\mathcal{M}. To conclude the construction, we define a memoryless strategy $\sigma^*$ in $\mathcal{M} as follows: we fix a memoryless deterministic strategy $\sigma_{=1}$ that is winning, from each vertex of $\mathcal{M}$ for the objective of almost-sure reaching of $Q$ (such a strategy exists since $\mathcal{M} is strongly connected, see also  {prf:ref}`5-thm:as-char`. Then we put $\sigma^*(v)=\sigma_{=1}(v)$ if $v\not\in Q$ and $\sigma^*(v)=\sigma_Q(v)$ otherwise. Hence, starting in any vertex, $\sigma^*$ eventually reaches $Q$ with probability 1 and then it starts behaving as $\sigma_Q$. The optimality of such a strategy follows from the prefix independence of mean payoff, as argued in the next theorem.

````{prf:theorem} NEEDS TITLE 5-thm:mp-valcomp
:label: 5-thm:mp-valcomp
 For any sequence of numbers $c_0,c_1,\dots$ and any $k\in\mathbb{N} it holds $\liminf_{n\rightarrow \infty}\frac{1}{n}\sum_{i=0}^{n-1}c_i = \liminf_{m\rightarrow \infty}\frac{1}{m}\sum_{i=0}^{m-1}c_{k+i}$. As a consequence, 
for every vertex $v$ in $\mathcal{M} it holds $\mathbb{P}{\sigma_Q}_{\mdp_Q,v}(\mathtt{MeanPayoff}{\;-}r^*)=1,$ where $r^*$ is the optimal value of $\lp_{\mathit{mp}}. Hence, $\mathbb{E}{\sigma^*}_v[\mathtt{MeanPayoff}{\;-}= r^*$.

````

````{admonition} Proof
:class: dropdown tip

We have
\begin{align*}
\liminf_{n\rightarrow \infty}\frac{c_0 + \cdots c_{n-1}}{n} &= \liminf_{n\rightarrow \infty}\left(\underbrace{\frac{k}{n}}_{\mathrlap{\text{vanishes for } n\rightarrow \infty}}\cdot\frac{c_0 + \cdots + c_{k-1}}{k} + \underbrace{\frac{n-k}{n}}_{\mathrlap{\rightarrow 1 \text{ for } n\rightarrow \infty}}\cdot\frac{c_k+\cdot+c_{n-1}}{n-k} \right)\\
&=\liminf_{m\rightarrow\infty} \frac{c_k+\dots+c_{k+m-1}}{m}.
\end{align*} A similar argument holds for $\limsup.$

With probability 1, a play has an infinite suffix consisting of plays from $\mdp_Q^{\sigma}$, and thus also $\mathtt{MeanPayoff}{\;-} and $\mathtt{MeanPayoff}{\;+} determined by this suffix. By \Cref{5-cor:mp-scc-optimality}, these quantities are equal to $r^*$ with probability 1.

````



The following theorem summarizes the computational aspects.

````{prf:theorem} NEEDS TITLE 5-thm:mp-rand-opt-main
:label: 5-thm:mp-rand-opt-main

In a strongly connected mean-payoff MDP, one can compute, in polynomial time, a memoryless randomized strategy which is optimal from every vertex, as well as the (single) optimal value of every vertex.

````

````{admonition} Proof
:class: dropdown tip

We obtain, in polynomial time, an optimal solution of $\lp_{\mathit{mp}}, with the optimal objective value being the optimal value of every vertex ( {prf:ref}`5-thm:mp-valcomp`). We then use this optimal solution $\lpsol{x}$ to construct the strategy $\sigma$ and the  Markov chain $\mdp_{S^{\sigma}$. From this chain we extract a strongly connected subset of vertices $Q$ (in polynomial time, by a simple graph reachability analysis). With the subset in hand, we can construct strategies $\sigma_Q$ and $\sigma_{=1}$, all polynomial-time computations (see  {prf:ref}`5-thm:as-char`). These two strategies are then combined to produce the optimal strategy $\sigma^*$.

````


## Deterministic optimality in strongly connected MDPs

It remains to prove that we can actually compute a memoryless~**deterministic** strategy that is optimal in every vertex. Looking back at the construction that resulted in  {prf:ref}`5-thm:mp-rand-opt-main`, we see that the optimal strategy $\sigma^*$ might be randomized because the computed optimal solution $\lpsol{x}$ of $\lp_{\mathit{mp}} can contain two components $(v,a)$, $(v,b)$ with $a\neq b$ and both $\lpsol{x}_{(v,a)}$ and $\lpsol{x}_{(v,b)}$ being positive. To prove memoryless deterministic optimality, we will show that there is always an optimal solution which yields a deterministic strategy, and that such a solution can be obtained in polynomial time.

The previous section implicitly defined two mappings: First, a mapping $\Psi$, which maps every solution $ \vec{x} $ of $\lp_{\mathit{mp}} to a memoryless strategy in some sub-MDP of $\mathcal{M}, by putting $\Psi(\vec{x}) = \sigma$ where $\sigma(a\mid v) = \vec{x}_{(v,a)}/\sum_{b\in A\vec{x}_{(v,b)}$. Second, mapping $\Xi$, which maps each memoryless strategy $\sigma$ that induces a strongly connected Markov chain to a solution $\Xi(\sigma)$ of $\lp_{\mathit{mp}} such that $\Xi(\sigma)_{(v,a)}=\invdist_v\cdot \sigma(a\mid v)$, where $\vec{z} is the unique invariant distribution of the chain induced by $\sigma$.

````{prf:lemma} NEEDS TITLE 5-lem:sol-strat-correspondence
:label: 5-lem:sol-strat-correspondence

Let $X$ be the set containing exactly those solutions $\vec{x}$ of $\lp_{\mathit{mp}} for which the strategy  $\Psi(\vec{x})$ induces a strongly connected Markov chain. Then the mappings $\Psi$ and $\Xi$ are bijections between $X$ and the set of all memoryless strategies in some sub-MDP of $\mathcal{M} that induce a strongly connected Markov chain.

````

````{admonition} Proof
:class: dropdown tip

A straightforward computation shows that $\Xi\circ\Psi$ and $\Psi\circ\Xi$ are identity functions on the respective sets.

````


````{prf:definition} NEEDS TITLE AND LABEL 
\label{5-def:pure-lp}
A solution $\vec{x}$ of $\lp_{\mathit{mp}}is **pure** if for every vertex $v$ there is at most one action $a$ such that $\vec{x}_{(v,a)}>0$.
 

\label{5-def:pure-lp}
A solution $\vec{x}$ of $\lp_{\mathit{mp}}is **pure** if for every vertex $v$ there is at most one action $a$ such that $\vec{x}_{(v,a)}>0$.

````



The following lemma follows from the way in which strategies $\sigma$ and $\sigma^*$ were constructed in the previous sub-section.

````{prf:lemma} NEEDS TITLE AND LABEL 
\label{5-lem:pure-lpsol}
Let $\lpsol{x}$ be a pure optimal solution of $\lp_{\mathit{mp}} and denote $ S = \{v \in Vmid \exists a \text{ s.t. }\lpsol{x}_{(v,a)}>0\} $. Then the strategy $\sigma=\Psi(\lpsol{x})$ is an MD strategy in $\mdp_{S$. Hence, in such a case, the strategy $\sigma^*$ constructed from $ \sigma $ as in  {prf:ref}`5-thm:mp-rand-opt-main` is an optimal MD strategy in $\mathcal{M}.
 

\label{5-lem:pure-lpsol}
Let $\lpsol{x}$ be a pure optimal solution of $\lp_{\mathit{mp}} and denote $ S = \{v \in Vmid \exists a \text{ s.t. }\lpsol{x}_{(v,a)}>0\} $. Then the strategy $\sigma=\Psi(\lpsol{x})$ is an MD strategy in $\mdp_{S$. Hence, in such a case, the strategy $\sigma^*$ constructed from $ \sigma $ as in  {prf:ref}`5-thm:mp-rand-opt-main` is an optimal MD strategy in $\mathcal{M}.

````

It remains to show how to find a pure optimal solution of $\lp_{\mathit{mp}}. To this end we exploit some fundamental properties of linear programs.

A linear program is in the **standard** (or equational) form if its set of constraints can be expressed as $A\cdot \vec{x} = \vec{b}$, $\vec{x}\geq 0$, where $\vec{x}$ is a vector of variables, $\vec{b}$ is a non-negative vector, and $A$ is a matrix of an appropriate dimension. In this notation, all the vectors are column vectors, i.e. $A$ has one column per each variable. Note that $\lp_{\mathit{mp}} is a program in the standard form. A feasible solution $\vec{x}$ of such a program is **basic** if the columns of $A$ corresponding to variables whose value is positive in $\vec{x}$ form a linearly independent set of vectors. Since the maximal number of linearly independent columns equals the maximal number of linearly independent rows (a number called a **rank** of $A$), we know that each basic feasible solution has at most as many positive entries as there are rows of $A$. 

The next two lemmas prove some fundamental properties of basic feasible solutions.

````{prf:lemma} NEEDS TITLE 5-lem:basic-cond-unique
:label: 5-lem:basic-cond-unique

Assume that a linear program in a standard form has two basic feasible solutions $\vec{x},\vec{x}'$ such that both solutions have the same set of non-zero components, and the cardinality of this set equals the number of equality constraints in the program. Then $\vec{x}=\vec{x}'$.

````

````{admonition} Proof
:class: dropdown tip

Write $A\cdot \vec{x} = \vec{b}$ the equational constraints of the LP.
If $\vec{x}$ is a basic feasible solution, then it solves the equation $A_{N} \cdot \vec{x}_N = \vec{b}$, where $A_N$ ($  N$ stands for non-zero) is obtained from $A$ by removing all columns corresponding to zero components of $\vec{x}$, and   $\vec{x}_N$ is obtained from $\vec{x}$ by removing all zero components. 

Since $\vec{x}$ has as many non-zero components as there are rows of $A$, it follows that $A_N$ is a square matrix. Since $\vec{x}$ is a basic solution, $A_N$ is regular (its columns are linearly independent) and $\vec{x}=A_{N}^{-1}\cdot \vec{b}$ is uniquely determined by $A_N$. Repeating the same argument for $\vec{x}'$ yields $\vec{x}'=A_{N}^{-1}\cdot \vec{b}= \vec{x}$.

````


````{prf:lemma} NEEDS TITLE 5-lem:basic-sol
:label: 5-lem:basic-sol

If a linear program in a standard form has an optimal solution, then it has also a basic optimal solution. Moreover, a basic optimal solution can be found in polynomial time.

````

````{admonition} Proof
:class: dropdown tip
[Sketch]
The existence of a basic optimal solution is a well-known linear programming fact, e.g. the standard simplex algorithm works by traversing the set of basic feasible solutions until it finds an optimal one {cite}`Matousek:2007`. For computing an optimal basic solution, we can use one of the polynomial-time interior-point methods for linear programming, such as the path-following method {cite}`Karmarkar:1984,Gonzaga:1992`. While these methods work by traversing the interior of the polyhedron of feasible solutions, they converge, in polynomial time, to a point that is closer to the optimal basic solution than to all the other basic solutions. By a process called **purification,** such a point can be then converted to the closest basic solution, i.e. to the optimal one {cite}`Gonzaga:1992`.

````





%Now the linear program $\lp_{\mathit{mp}} has $|V+1$ constraints, so by the above argument its basic solutions have at most $|V+1$ non-zero entries. To obtain a deterministic strategy, we need to push this bound further.

````{prf:theorem} NEEDS TITLE 5-thm:lpmp-basic-dim
:label: 5-thm:lpmp-basic-dim

One can find, in polynomial time, an optimal deterministic strategy in a given strongly connected  mean-payoff MDP.

````

````{admonition} Proof
:class: dropdown tip

First, we use {prf:ref}`5-lem:basic-sol` to find a basic optimal solution $\lpsol{x}$ of $\lp_{\mathit{mp}}.
We check if it is pure. If yes, we are done. Otherwise,

%Assume that there is a basic feasible solution $\lpsol{x}$ of $\lp_{\mathit{mp}} that is not pure. Then 
there is $v\in V and two distinct actions $a,b$ such that $\lpsol{x}_{(v,a)}>0$ and $\lpsol{x}_{(v,b)}>0.$ Let $ S = \{v \in Vmid \exists a \text{ s.t. }\lpsol{x}_{(v,a)}>0\} $. By~\Cref{5-cor:mp-scc-extraction}, we can partition $S into several subsets, each of which induces a strongly connected sub-MDP of $\mathcal{M}. Let $Q$ be a class of this partition containing $v$. We have that the optimal mean-payoff value of every vertex in $\mdp_Q$ is the same as in $\mathcal{M}. This is because, 
as in the beginning of the proof of~\Cref{5-cor:mp-scc-optimality}, we can transform $\lpsol{x}$ into another optimal solution of the same value as $\lpsol{x}$ which has non-zero entries only for components indexed by $(q,a)$ with $q\in Q$. All these computations can be easily implemented in polynomial time. 

We argue that $Q$ is a strict subset of $V. Indeed, assume that $Q=V. Then $\lpsol{x}$ induces a randomized strategy $\sigma$ in $\mathcal{M}. Moreover, since $\lpsol{x}$ is a basic solution, it has at most $|V+1$ positive entries, and since it is non-pure, it must have exactly $n+1$ positive entries, i.e.  {prf:ref}`5-lem:basic-cond-unique` is applicable to $\lpsol{x}$, since $\lp_{\mathit{mp}} has exactly $|V+1$ constraints. Now we define a new strategy $\sigma'$ in $\mathcal{M} by slightly changing the behaviour in $v$. To this end, choose some $\eps>0$ and put $\sigma'(a\mid v)=\sigma(a\mid v)-\eps$ and $\sigma'(b\mid v)=\sigma(b\mid v)+\eps$; we choose $\eps$ small enough so that both quantities are still non-zero. The chain $\mathcal{M}{\sigma'}$ is still strongly connected. Now let $\vec{x}' = \Xi(\sigma')$. Then $\vec{x}'$ is a solution of $\lp_{\mathit{mp}} which is still basic, with a set of non-zero components being the same as in $\lpsol{x}$. At the same time, $\vec{x}'\neq \lpsol{x}$, since $\sigma\neq {\sigma'}$ and $\Xi$ is a bijection ( {prf:ref}`5-lem:sol-strat-correspondence`). But this is a contradiction with  {prf:ref}`5-lem:basic-cond-unique`.

Hence, $\mdp_Q$ is a strict sub-MDP of $\mathcal{M} in which the value of every vertex is the same as in the original MDP. We can perform a recursive call of the aforementioned computation on $\mdp_Q$ (compute basic optimal solution of $\lp_{\mathit{mp}}, check purity, possibly extract and recurse on a sub-MDP).
The depth of recursion is bounded by $|V$, so the running time is polynomial. Since each sub-MDP obtained during the recursion is non-empty, and the size of the MDPs decreases, the recursion must eventually terminate with a basic optimal solution (in some sub-MDP $\mathcal{M}$) that is pure. This yields a memoryless deterministic strategy in $\mathcal{M}$ whose value is equal to the optimal value in $\mathcal{M}$ Such a strategy can be extended to whole $\mathcal{M} by solving almost sure reachability to $ \mathcal{M} $, as described in the previous sub-section.

%As such,  In particular, $\tilde{x}$ has exactly $|W|+1$ positive entries (due to its non-purity), which is the number of constraints in $\lp_{\mathit{mp}}{W}$. Hence, {prf:ref}`5-lem:basic-unique` applies to $\tilde{x}$.

%Since the solution $\tilde{x}$ is not pure, it induces a randomized strategy $\tilde\sigma$ in $\mdp_W$ (a restriction of $\bar\sigma$ to $\mdp_W$). 

%Now we define a new strategy $\sigma$ in $\mdp_W$ by slightly changing the behaviour in $v$. To this end, choose some $\eps>0$ and put $\sigma(a\mid v)=\tilde\sigma(a\mid v)-\eps$ and $\sigma(a\mid v)=\tilde\sigma(a\mid v)+\eps$; we choose $\eps$ small enough so that both quantities are still non-zero. The chain $\mathcal{M}\sigma$ (whose transition matrix we denote $P) is still strongly connected. Now let $x = \Xi(\sigma)$. Then $x$ is a solution of $\lp_{\mathit{mp}} which is still basic, with a set of non-zero components being the same as in $\lpsol{x}$. At the same time, $x\neq \tilde{x}$, since $\sigma\neq \tilde{\sigma}$ and $\Xi$ is a bijection ( {prf:ref}`5-lem:sol-strat-correspondence`). But this is a contradiction, since there cannot be two basic feasible solutions with the same set of non-zero components. 

%   

````











%
````{prf:lemma} NEEDS TITLE AND LABEL 

%Each strategy $\sigma$ induces a solution $\lpsol{x}$ of $\lp_{\mathit{mp}} whose objective value is at least $\mathbb{E}\sigma_v[\mathtt{MeanPayoff}.$

%
````{admonition} Proof
:class: dropdown tip

%
````



%

%reachability values, we denote by $\mathtt{DiscountedPayoff}{k}(\pi$ the 

%payoff accumulated during the first $k$ steps of $\pi, i.e. the number 

%\, c\play_i)$. 

%lemma can be proved by an easy induction.

%\begin{lemma}

%For each $k\geq 0$ and each vertex $v$ it holds that 

%(\mathcal{D}k(\vec{0}))_v
$$
 

% 

%Each strategy $\sigma$ induces a solution $\lpsol{x}$ of $\lp_{\mathit{mp}} whose objective value is at least $\mathbb{E}\sigma_v[\mathtt{MeanPayoff}.$

%
````{admonition} Proof
:class: dropdown tip

%
````



%

%reachability values, we denote by $\mathtt{DiscountedPayoff}{k}(\pi$ the 

%payoff accumulated during the first $k$ steps of $\pi, i.e. the number 

%\, c\play_i)$. 

%lemma can be proved by an easy induction.

%\begin{lemma}

%For each $k\geq 0$ and each vertex $v$ it holds that 

%(\mathcal{D}k(\vec{0}))_v
$$
 

%
````

%
%
%Now $\mathtt{DiscountedPayoff}\pi = \lim_{k\rightarrow 

%dominated 

%\lim_{k\rightarrow 

%$k$ we have $\mathtt{DiscountedPayoff}{k}(\pi\leq \max_{e\in 

%$)

%Hence 

%\begin{align*}

%\sup_{\sigma}\mathbb{E}\sigma_v[\lim_{k\rightarrow \infty}\mathtt{DiscountedPayoff}k]\\

%\\

%=\big(\sup_{k\geq 1} \mathcal{V}k(\vec{0})\big)_v = \big(\lim_{k\rightarrow 

%\end{align*}



%Note that the last equality in the first line follows from (XXX - SET UP SOME 

%line 

%$\big(\mathcal{V}\vec{0})\big)_v,\big(\mathcal{V}2(\vec{0})\big)_v,\dots$ is 

%vector 

%

%\label{5-lem:reach-value-limit}

%\end{theorem}

%The previous theorem yields a simple algorithm for approximation of 

%consists of iterating $\mathcal{V} with initial seed $\vec{0}$, which yields 

%disadvantage of value iteration is that it might not converge to the true 

%the MDP in Figure~\ref{xxx}. However,...

%



%\end{theorem}









%(v_0,v_1)(v_1,v_2)\cdots(v_{k-1},v_k)$ we put

%\label{5-eq:cylinder-probs}

%\begin{cases}

%\prod_{i=1}^{k} \sum_{a \in A\sigma(a\mid )

%\end{equation}
