(5-sec:end_components)=
# End components


```{math}
\newcommand{\probm}{\mathbb{P}}
\newcommand{\probTranFunc}{\Delta}
\newcommand{\edges}{E}
\newcommand{\mdp}{\mathcal{M}}
\newcommand{\vinit}{v_0}
\newcommand{\winPos}{W_{>0}}
\newcommand{\winAS}{W_{=1}}
\newcommand{\OPAS}{\mathcal{P}_{=1}}
\newcommand{\mec}{M}
\newcommand{\mecs}{\mathit{MEC}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\vertices}{V}
\newcommand{\Ing}{\ing}
\newcommand{\play}{\pi}
\newcommand{\Safe}{\mathtt{Safe}}
\newcommand{\Reach}{\mathtt{Reach}}
\newcommand{\Inf}{\mathtt{Inf}}
\newcommand{\ing}{\textrm{In}}
```

To solve mean-payoff optimization in general MDPs, as well as general optimization problems for $\omega$-regular objectives, we need to introduce a crucial notion of an **end component**.

````{prf:definition} NEEDS TITLE AND LABEL 
\label{5-def:ec}
An **end component (EC)** of an MDP is any set $M of vertices having the following two properties:

 *  For each $u \in M there exists an action $ a $ that is **$ M-safe** in $ u $, i.e. satisfies that for all vertices  $v$ with $ \Deltav \mid u,a) > 0 $ it holds $ v \in M$.
 *  For each pair of distinct vertices $ u,v \in M there is a path from $ u $ to $ v $ visiting only the states from $M.

In other words, $ M$ is an EC of $ \mathcal{M}$ if and only if $ M$ is a closed set and the sub-MDP $ \mdp_M$ is strongly connected. 
 

\label{5-def:ec}
An **end component (EC)** of an MDP is any set $M of vertices having the following two properties:

 *  For each $u \in M there exists an action $ a $ that is **$ M-safe** in $ u $, i.e. satisfies that for all vertices  $v$ with $ \Deltav \mid u,a) > 0 $ it holds $ v \in M$.
 *  For each pair of distinct vertices $ u,v \in M there is a path from $ u $ to $ v $ visiting only the states from $M.

In other words, $ M$ is an EC of $ \mathcal{M}$ if and only if $ M$ is a closed set and the sub-MDP $ \mdp_M$ is strongly connected. 

````



From the player's point of view, the following property of ECs is important.

````{prf:lemma} NEEDS TITLE AND LABEL 
\label{5-lem:EC-sweep}
Let $M be an EC and $v \in M. Then there is an MD strategy $\sigma$ which, when starting in a vertex inside $M, never visits a vertex outside of $ M$ and at the same time ensures that with probability one, the vertex $v$ is visited infinitely often. Moreover, $\sigma$ can be computed in polynomial time.
 

\label{5-lem:EC-sweep}
Let $M be an EC and $v \in M. Then there is an MD strategy $\sigma$ which, when starting in a vertex inside $M, never visits a vertex outside of $ M$ and at the same time ensures that with probability one, the vertex $v$ is visited infinitely often. Moreover, $\sigma$ can be computed in polynomial time.

````

````{admonition} Proof
:class: dropdown tip

%For the finite-memory construction, note that for each vertex $v\in M there is an MD strategy in $ \mdp_M$ ensuring that $v$ is reached with probability 1 from any initial vertex in $ M$. Indeed, it holds that  $\mathcal{P}_{=1}v,M=M, so the result follows from  {prf:ref}`5-thm:as-char`. To construct the required strategy, we enumerate the vertices of $ M$ in some fixed order $ u_1, u_2, \dots u_\ell $ and employ a strategy which initially behaves as a winning strategy for almost-sure reachability of $ u_1 $, once $ u_1 $ is reached it starts to behave as a winning strategy for a.s. reaching $ u_2 $, etc.; this continues until $ u_\ell $ is reached, in which case we switch back to reaching $ u_1 $ and loop through this sequence of strategies forever. Clearly, memory of size $ \ell $ is sufficient for such looping. That all vertices of $ M$ are visited infinitely often follows by an easy induction.

%For the MR construction, take a strategy which in each vertex $ u\in M$ uniformly randomizes between all actions that are $ M-safe in $ u $. Applying such a strategy yields a strongly connected Markov chain. Using similar arguments as in the previous paragraph, we can show that in such a chain the probability of reaching $ v $ from $ u $ is 1, for any pair of vertices $ u,v $. The rest again follows by an easy induction. 

From  {prf:ref}`5-thm:as-char` we know that we can compute, in polynomial time, an MD strategy $\sigma$ in the sub-MDP $ \mdp_M$ ensuring that $v$ is reached with probability 1 from any initial vertex in $ M$. Indeed, this is because $M= W_{>0}\mdp_M,\mathtt{Reach}v))$, due to the second condition in the definition of a MEC. Since $M is closed, this strategy never leaves $M. Whenever, the strategy leaves $v$, it guarantees that we return to $v$ with probability 1. Hence, for each $k$, the probability of event $V_k$ --- visiting $v$ at least $k$ times --- is $1$. Since $V_{k+1}\subseteq V_k$, it follows that also the probability of $\bigcap_{i=1}^\infty V_i$ is equal to $1$, which is what we aimed to prove.

````

The main reason for introducing ECs is that they are crucial for understanding the limiting behaviour of MDPs.

````{prf:definition} NEEDS TITLE 5-def:inf
:label: 5-def:inf

We denote by $\mathtt{Inf}\pi$ the set of vertices that appear infinitely often along a play $ \pi$.

````


````{prf:lemma} NEEDS TITLE 5-lem:EC-inf
:label: 5-lem:EC-inf

For any $ v_0$ and $ \sigma $ it holds $ \mathbb{P}\sigma_{v_0 ( \{\pi\mid \mathtt{Inf}\pi \text{ is an EC }  \}) = 1 $. 

````

````{admonition} Proof
:class: dropdown tip

Assume the converse. Then in some MDP there is a set of vertices $ X $ which is not an EC but satisfies $ \mathbb{P}\sigma_{v_0(\mathtt{Inf}= X ) > 0 $. Since $ X $ is not an EC, there is a vertex $ v \in X $ in which any (even randomized) choice of action results in leaving $ X $ with probability at least $  p_{\min} > 0$ (recall that $ p_{\min} $ is the smallest non-zero edge probability in the MDP).

Let $ \mathit{Stay}_k $ be the set of plays in $\{\mathtt{Inf}= X \}$ which, from step $ k $ on, never visit a vertex outside of $ X $. Since $ \{\mathtt{Inf}= X \}  = \bigcup_{i=1}^{\infty} \mathit{Stay}_i$, by union bound we get $ \mathbb{P}\sigma_{v_0(\mathit{Stay}_{k_0})>0 $ for some  $ k_0\in \mathbb{N}$. Let $ \mathit{Vis}_j $ denote the set of all plays in $ \mathit{Stay}_{k_0} $ that visit $ v $ at least $ j $ times **after** the step $ k_0 $. Since $  \mathit{Stay}_{k_0} \subseteq \{\mathtt{Inf}= X\}$, we have $  \mathit{Stay}_{k_0} \cap \mathit{Vis}_j = \mathit{Stay}_{k_0} $ for each $ j $. But an easy induction shows that  $ \probm_{v_0^\sigma (\mathit{Stay}_{k_0} \cap \mathit{Vis}_{j+1} ) \leq \probm_{v_0^\sigma(\{\textrm{In}play_{k_0}) \in X \})\cdot p_{\min}^j$, since every visit to $ v $ brings a  risk at least $p_{\min}$ of falling out of $ X $. The latter number converges to zero, so $ \probm_{v_0^\sigma (\mathit{Stay}_{k_0}) = \lim_{j\rightarrow \infty}\probm_{v_0^\sigma (\mathit{Stay}_{k_0}) = \lim_{j\rightarrow \infty}\probm_{v_0^\sigma (\mathit{Stay}_{k_0} \cap\mathit{Vis}_{j+1}) =  0$, a contradiction.

````

In general, there can be exponentially many end components in an MDP (e.g. for a complete underlying graph and one action per edge, each subset of vertices is an EC). However, we can usually restrict to analysing **maximal** ECs.

````{prf:definition} NEEDS TITLE AND LABEL 
\label{5-def:mec}
An end component $ M$ is a **maximal end component (MEC)** if no other end-component $ M $ is a superset of $ M$. We denote by $\mathit{MEC}\mathcal{M}$ the set of all MECs of $\mathcal{M}$
 

\label{5-def:mec}
An end component $ M$ is a **maximal end component (MEC)** if no other end-component $ M $ is a superset of $ M$. We denote by $\mathit{MEC}\mathcal{M}$ the set of all MECs of $\mathcal{M}$

````
 

If two ECs have a non-empty intersection, then their union is again an EC. Hence, every EC is contained in exactly one MEC, and the total number of MECs is bounded by $ |V $, since two distinct MECs must be disjoint. Moreover, the decomposition of an MDP into MECs can be computed in polynomial time.

\begin{algorithm}
\KwData{An MDP $ \mathcal{M}$}
\SetKwFunction{FTreat}{Treat}
\SetKwProg{Fn}{Function}{:}{}

$**List** \leftarrow \emptyset$ \tcp*{List of found MECs}

$ G \leftarrow (VE $ \tcp*{The underlying graph of $ \mathcal{M}$} 

\While{$G$ is non-empty}{
Decompose $ G $ into strongly connected components;

$ R \leftarrow \emptyset $ \tcp*{The list of vertices to remove.}
\ForEach{bottom SCC $ B $ of $ G $}{
$ B $ is a MEC of $ \mathcal{M}$, add it to $ **List** $;\\
$ R \leftarrow R \cup (V\setminus W_{=1}\mathcal{M}\mathtt{Safe}Vsetminus B)))$ \tcp*{Schedule removal of vertices from which $B$ cannot be avoided in $\mathcal{M}.}
} 
remove vertices in $R$ from $G$ along with adjacent edges
}


\Return{$**List**$}
\caption{Algorithm for MEC decomposition of an MDP.}
\label{5-algo:MEC-decomposition}
\end{algorithm}

````{prf:theorem} NEEDS TITLE 5-thm:MEC-decomposition-complexity
:label: 5-thm:MEC-decomposition-complexity

The set of all MECs in a given MDP can be computed in polynomial time.

````

````{admonition} Proof
:class: dropdown tip

There are several known algorithms, a simple one is pictured in {numref}`5-algo:MEC-decomposition`. Each iteration goes as follows: we first take the underlying directed graph of the MDP and find its strongly connected components using some of the well-known polynomial algorithms {cite}`Cormen&Leiserson&Rivest&Stein:2009`. We identify the bottom SCCs, i.e. those from which there is no outgoing edge in the graph. It is easy to see that each such SCC must form a MEC of $\mathcal{M}, and conversely, each MDP has at least one MEC that is also a bottom SCC of its underlying graph. Moreover, for each such bottom SCC $B $ we compute the **random attractor** of $B$, i.e. the set of vertices of $\mathcal{M} from which $B$ cannot be avoided under any strategy. To this end, we compute, in polynomial time, the almost-surely winning set $ W_{=1}\mathcal{M}\mathtt{Safe}V\setminus B)) $ which is the largest largest (w.r.t. set inclusion) subset of $V from which the player can ensure to stay in $V\setminus B$ forever (i.e. the complement of the random attractor of $B$). The computation can be done in polynomial time by  {prf:ref}`5-thm:safety-main`). No vertex of the random attractor of $B$ can belong to a MEC different from $ B $: such a MEC would be disjoint from $ B $ bu the player could not force avoiding $ B $ from within this MEC, a contradiction with MEC being a closed set. Hence, all MECs of $\mathcal{M} which are not a bottom SCC of $G$ are subsets of $W_{=1}\mathcal{M}\mathtt{Safe}V\setminus B)) \subseteq V\setminus R$, so we can remove all vertices in $R$ from the graph and continue to the next iteration (note that removing vertices in $R$ from $\mathcal{M} again yields a MDP, since the complement of $R$ is an intersection of closed sets, and thus again a closed set). The main loop performs at most $|V$ iterations, which yields the polynomial complexity.

````

