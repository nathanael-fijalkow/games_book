(5-sec:end_components)=
# End components

```{math}

\newcommand{\expv}{\mathbb{E}} \newcommand{\discProbDist}{f} \newcommand{\sampleSpace}{S} \newcommand{\sigmaAlg}{\mathcal{F}} \newcommand{\probm}{\mathbb{P}} \newcommand{\rvar}{X} 

\newcommand{\actions}{A} \newcommand{\colouring}{c} \newcommand{\probTranFunc}{\Delta} \newcommand{\edges}{E} \newcommand{\colours}{C} \newcommand{\mdp}{\mathcal{M}} \newcommand{\vinit}{v_0} \newcommand{\cylProb}{p} \newcommand{\emptyPlay}{\epsilon} \newcommand{\objective}{\Omega} \newcommand{\genColour}{\textsc{c}} \newcommand{\quantObj}{f} \newcommand{\quantObjExt}{\bar{\quantObj}} \newcommand{\indicator}[1]{\mathbf{1}_{#1}} \newcommand{\eps}{\varepsilon} \newcommand{\maxc}{\max_{\colouring}} 
\newcommand{\winPos}{W_{>0}}
\newcommand{\winAS}{W_{=1}}
\newcommand{\cylinder}{\mathit{Cyl}}
\newcommand{\PrePos}{\text{Pre}_{>0}}
\newcommand{\PreAS}{\text{Pre}_{=1}}
\newcommand{\PreOPPos}{\mathcal{P}_{>0}}
\newcommand{\OPAS}{\mathcal{P}_{=1}}
\newcommand{\safeOP}{\mathit{Safe_{=1}}}
\newcommand{\closed}{\mathit{Cl}}

\newcommand{\reachOP}{\mathcal{V}}
\newcommand{\discOP}{\mathcal{D}}
\newcommand{\valsigma}{\vec{x}^{\sigma}}
\newcommand{\lp}{\mathcal{L}}
\newcommand{\lpdisc}{\lp_{\mathit{disc}}}
\newcommand{\lpreach}{\lp_{\mathit{reach}}}
\newcommand{\lpmp}{\lp_{\mathit{mp}}}
\newcommand{\lpsol}[1]{\bar{\vec{#1}}}
\newcommand{\lpsolg}[1]{\bar{#1}}
\newcommand{\lpmpdual}{\lpmp^{\mathit{dual}}}
\newcommand{\actevent}[3]{\actions^{#1}_{#2,#3}} 
\newcommand{\MeanPayoffSup}{\MeanPayoff^{\;+}}
\newcommand{\MeanPayoffInf}{\MeanPayoff^{\;-}}
\newcommand{\mcprob}{P}
\newcommand{\invdist}{\vec{z}}
\newcommand{\hittime}{T}
\newcommand{\playPay}{\textsf{p-Payoff}}
\newcommand{\stepPay}{\textsf{s-Payoff}}
\newcommand{\Pay}{\textsf{Payoff}}
\newcommand{\mec}{M}
\newcommand{\OPS}{\mathcal{S}_{=1}}
\newcommand{\smallmp}{\mathit{mp}}
\newcommand{\vgood}{v_{\mathit{good}}}
\newcommand{\vbad}{v_{\mathit{bad}}}
\newcommand{\finact}{fin}
\newcommand{\mecs}{\mathit{MEC}}
\newcommand{\slice}[2]{#1_{#2-}}
\newcommand{\ReachOp}{\mathcal{R}}
\newcommand{\dPayoffStep}[1]{\DiscountedPayoff^{\;(#1)}}
\newcommand{\solvset}{S}
\newcommand{\Eve}{\textrm{Eve}}
\newcommand{\Adam}{\textrm{Adam}}
\newcommand{\set}[1]{\left\{ #1 \right\}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Zinfty}{\Z \cup \set{\pm \infty}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\Rinfty}{\R \cup \set{\pm \infty}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\Qinfty}{\Q \cup \set{\pm \infty}}
\newcommand{\argmax}{\textrm{argmax}}
\newcommand{\argmin}{\textrm{argmin}}
\newcommand{\Op}{\mathbb{O}}
\newcommand{\Prob}{\mathbb{P}} \newcommand{\dist}{\mathcal{D}} \newcommand{\Dist}{\dist} \newcommand{\supp}{\textrm{supp}} 
\newcommand{\game}{\mathcal{G}} \renewcommand{\Game}{\game} \newcommand{\arena}{\mathcal{A}} \newcommand{\Arena}{\arena} 
\newcommand{\col}{\textsf{col}} \newcommand{\Col}{\col} 
\newcommand{\mEve}{\mathrm{Eve}}
\newcommand{\mAdam}{\mathrm{Adam}}
\newcommand{\mRandom}{\mathrm{Random}}
\newcommand{\vertices}{V} \newcommand{\VE}{V_\mEve} \newcommand{\VA}{V_\mAdam} \newcommand{\VR}{V_\mRandom} 
\newcommand{\ing}{\textrm{In}}
\newcommand{\Ing}{\ing}
\newcommand{\out}{\textrm{Out}}
\newcommand{\Out}{\out}
\newcommand{\dest}{\Delta} 
\newcommand{\WE}{W_\mEve} \newcommand{\WA}{W_\mAdam} 
\newcommand{\Paths}{\textrm{Paths}} \newcommand{\play}{\pi} \newcommand{\first}{\textrm{first}} \newcommand{\last}{\textrm{last}} 
\newcommand{\mem}{\mathcal{M}} \newcommand{\Mem}{\mem} 
\newcommand{\Pre}{\textrm{Pre}} \newcommand{\PreE}{\textrm{Pre}_\mEve} \newcommand{\PreA}{\textrm{Pre}_\mAdam} \newcommand{\Attr}{\textrm{Attr}} \newcommand{\AttrE}{\textrm{Attr}_\mEve} \newcommand{\AttrA}{\textrm{Attr}_\mAdam} \newcommand{\rank}{\textrm{rank}}
\renewcommand{\Win}{\textrm{Win}} 
\renewcommand{\Lose}{\textrm{Lose}} 
\newcommand{\Value}{\textrm{val}} 
\newcommand{\ValueE}{\textrm{val}_\mEve} 
\newcommand{\ValueA}{\textrm{val}_\mAdam}
\newcommand{\val}{\Value} 
\newcommand{\Automaton}{\mathbf{A}} 
\newcommand{\Safe}{\mathtt{Safe}}
\newcommand{\Reach}{\mathtt{Reach}} 
\newcommand{\Buchi}{\mathtt{Buchi}} 
\newcommand{\CoBuchi}{\mathtt{CoBuchi}} 
\newcommand{\Parity}{\mathtt{Parity}} 
\newcommand{\Muller}{\mathtt{Muller}} 
\newcommand{\Rabin}{\mathtt{Rabin}} 
\newcommand{\Streett}{\mathtt{Streett}} 
\newcommand{\MeanPayoff}{\mathtt{MeanPayoff}} 
\newcommand{\DiscountedPayoff}{\mathtt{DiscountedPayoff}}
\newcommand{\Energy}{\mathtt{Energy}}
\newcommand{\TotalPayoff}{\mathtt{TotalPayoff}}
\newcommand{\ShortestPath}{\mathtt{ShortestPath}}
\newcommand{\Sup}{\mathtt{Sup}}
\newcommand{\Inf}{\mathtt{Inf}}
\newcommand{\LimSup}{\mathtt{LimSup}}
\newcommand{\LimInf}{\mathtt{LimInf}}
\newcommand{\NL}{\textrm{NL}}
\newcommand{\PTIME}{\textrm{PTIME}}
\newcommand{\NP}{\textrm{NP}}
\newcommand{\coNP}{\textrm{coNP}}
\newcommand{\PSPACE}{\textrm{PSPACE}}
```
To solve mean-payoff optimization in general MDPs, as well as general optimization problems for $\omega$-regular objectives, we need to introduce a crucial notion of an **end component**.

```{prf:definition} needs title and label 
\label{5-def:ec}
An **end component (EC)** of an MDP is any set $\mec$ of vertices having the following two properties:

 *  For each $u \in \mec$ there exists an action $ a $ that is **$ \mec$-safe** in $ u $, i.e. satisfies that for all vertices  $v$ with $ \probTranFunc(v \mid u,a) > 0 $ it holds $ v \in \mec $.
 *  For each pair of distinct vertices $ u,v \in \mec$ there is a path from $ u $ to $ v $ visiting only the states from $\mec$.

In other words, $ \mec $ is an EC of $ \mdp $ if and only if $ \mec $ is a closed set and the sub-MDP $ \mdp_\mec $ is strongly connected. 
 
:label: 
\label{5-def:ec}
An **end component (EC)** of an MDP is any set $\mec$ of vertices having the following two properties:

 *  For each $u \in \mec$ there exists an action $ a $ that is **$ \mec$-safe** in $ u $, i.e. satisfies that for all vertices  $v$ with $ \probTranFunc(v \mid u,a) > 0 $ it holds $ v \in \mec $.
 *  For each pair of distinct vertices $ u,v \in \mec$ there is a path from $ u $ to $ v $ visiting only the states from $\mec$.

In other words, $ \mec $ is an EC of $ \mdp $ if and only if $ \mec $ is a closed set and the sub-MDP $ \mdp_\mec $ is strongly connected. 

:nonumber:

\label{5-def:ec}
An **end component (EC)** of an MDP is any set $\mec$ of vertices having the following two properties:

 *  For each $u \in \mec$ there exists an action $ a $ that is **$ \mec$-safe** in $ u $, i.e. satisfies that for all vertices  $v$ with $ \probTranFunc(v \mid u,a) > 0 $ it holds $ v \in \mec $.
 *  For each pair of distinct vertices $ u,v \in \mec$ there is a path from $ u $ to $ v $ visiting only the states from $\mec$.

In other words, $ \mec $ is an EC of $ \mdp $ if and only if $ \mec $ is a closed set and the sub-MDP $ \mdp_\mec $ is strongly connected. 

```


\noindent
From the player's point of view, the following property of ECs is important.

```{prf:lemma} needs title and label 
\label{5-lem:EC-sweep}
Let $\mec$ be an EC and $v \in \mec$. Then there is an MD strategy $\sigma$ which, when starting in a vertex inside $\mec$, never visits a vertex outside of $ \mec $ and at the same time ensures that with probability one, the vertex $v$ is visited infinitely often. Moreover, $\sigma$ can be computed in polynomial time.
 
:label: 
\label{5-lem:EC-sweep}
Let $\mec$ be an EC and $v \in \mec$. Then there is an MD strategy $\sigma$ which, when starting in a vertex inside $\mec$, never visits a vertex outside of $ \mec $ and at the same time ensures that with probability one, the vertex $v$ is visited infinitely often. Moreover, $\sigma$ can be computed in polynomial time.

:nonumber:

\label{5-lem:EC-sweep}
Let $\mec$ be an EC and $v \in \mec$. Then there is an MD strategy $\sigma$ which, when starting in a vertex inside $\mec$, never visits a vertex outside of $ \mec $ and at the same time ensures that with probability one, the vertex $v$ is visited infinitely often. Moreover, $\sigma$ can be computed in polynomial time.

```

```{admonition} Proof
:class: dropdown tip

From  {prf:ref}`5-thm:as-char` we know that we can compute, in polynomial time, an MD strategy $\sigma$ in the sub-MDP $ \mdp_\mec $ ensuring that $v$ is reached with probability 1 from any initial vertex in $ \mec $. Indeed, this is because $\mec = \winPos(\mdp_M,\Reach(v))$, due to the second condition in the definition of a MEC. Since $\mec$ is closed, this strategy never leaves $\mec$. Whenever, the strategy leaves $v$, it guarantees that we return to $v$ with probability 1. Hence, for each $k$, the probability of event $V_k$ --- visiting $v$ at least $k$ times --- is $1$. Since $V_{k+1}\subseteq V_k$, it follows that also the probability of $\bigcap_{i=1}^\infty V_i$ is equal to $1$, which is what we aimed to prove.

```

The main reason for introducing ECs is that they are crucial for understanding the limiting behaviour of MDPs.

```{prf:definition} needs title 5-def:inf
:label: 5-def:inf
:nonumber:

We denote by $\Inf(\play)$ the set of vertices that appear infinitely often along a play $ \play $.

```


```{prf:lemma} needs title 5-lem:EC-inf
:label: 5-lem:EC-inf
:nonumber:

For any $ \vinit $ and $ \sigma $ it holds $ \probm^\sigma_{\vinit} ( \{\play \mid \Inf(\play) \text{ is an EC }  \}) = 1 $. 

```

```{admonition} Proof
:class: dropdown tip

Assume the converse. Then in some MDP there is a set of vertices $ X $ which is not an EC but satisfies $ \probm^\sigma_{\vinit}(\Inf = X ) > 0 $. Since $ X $ is not an EC, there is a vertex $ v \in X $ in which any (even randomized) choice of action results in leaving $ X $ with probability at least $  p_{\min} > 0$ (recall that $ p_{\min} $ is the smallest non-zero edge probability in the MDP).

Let $ \mathit{Stay}_k $ be the set of plays in $\{\Inf = X \}$ which, from step $ k $ on, never visit a vertex outside of $ X $. Since $ \{\Inf = X \}  = \bigcup_{i=1}^{\infty} \mathit{Stay}_i$, by union bound we get $ \probm^\sigma_{\vinit}(\mathit{Stay}_{k_0})>0 $ for some  $ k_0\in \N $. Let $ \mathit{Vis}_j $ denote the set of all plays in $ \mathit{Stay}_{k_0} $ that visit $ v $ at least $ j $ times **after** the step $ k_0 $. Since $  \mathit{Stay}_{k_0} \subseteq \{\Inf = X\}$, we have $  \mathit{Stay}_{k_0} \cap \mathit{Vis}_j = \mathit{Stay}_{k_0} $ for each $ j $. But an easy induction shows that  $ \probm_{\vinit}^\sigma (\mathit{Stay}_{k_0} \cap \mathit{Vis}_{j+1} ) \leq \probm_{\vinit}^\sigma(\{\Ing(\play_{k_0}) \in X \})\cdot p_{\min}^j$, since every visit to $ v $ brings a  risk at least $p_{\min}$ of falling out of $ X $. The latter number converges to zero, so $ \probm_{\vinit}^\sigma (\mathit{Stay}_{k_0}) = \lim_{j\rightarrow \infty}\probm_{\vinit}^\sigma (\mathit{Stay}_{k_0}) = \lim_{j\rightarrow \infty}\probm_{\vinit}^\sigma (\mathit{Stay}_{k_0} \cap\mathit{Vis}_{j+1}) =  0$, a contradiction.

```

In general, there can be exponentially many end components in an MDP (e.g. for a complete underlying graph and one action per edge, each subset of vertices is an EC). However, we can usually restrict to analysing **maximal** ECs.

```{prf:definition} needs title and label 
\label{5-def:mec}
An end component $ \mec $ is a **maximal end component (MEC)** if no other end-component $ \mec' $ is a superset of $ \mec $. We denote by $\mecs(\mdp)$ the set of all MECs of $\mdp.$
 
:label: 
\label{5-def:mec}
An end component $ \mec $ is a **maximal end component (MEC)** if no other end-component $ \mec' $ is a superset of $ \mec $. We denote by $\mecs(\mdp)$ the set of all MECs of $\mdp.$

:nonumber:

\label{5-def:mec}
An end component $ \mec $ is a **maximal end component (MEC)** if no other end-component $ \mec' $ is a superset of $ \mec $. We denote by $\mecs(\mdp)$ the set of all MECs of $\mdp.$

```
 

If two ECs have a non-empty intersection, then their union is again an EC. Hence, every EC is contained in exactly one MEC, and the total number of MECs is bounded by $ |\vertices| $, since two distinct MECs must be disjoint. Moreover, the decomposition of an MDP into MECs can be computed in polynomial time.

\begin{algorithm}
\KwData{An MDP $ \mdp $}
\SetKwFunction{FTreat}{Treat}
\SetKwProg{Fn}{Function}{:}{}

$**List** \leftarrow \emptyset$ \tcp*{List of found MECs}

$ G \leftarrow (\vertices,\edges) $ \tcp*{The underlying graph of $ \mdp $} 

\While{$G$ is non-empty}{
Decompose $ G $ into strongly connected components;

$ R \leftarrow \emptyset $ \tcp*{The list of vertices to remove.}
\ForEach{bottom SCC $ B $ of $ G $}{
$ B $ is a MEC of $ \mdp $, add it to $ **List** $;\\
$ R \leftarrow R \cup (\vertices \setminus \winAS(\mdp,\Safe(\vertices\setminus B)))$ \tcp*{Schedule removal of vertices from which $B$ cannot be avoided in $\mdp$.}
} remove vertices in $R$ from $G$ along with adjacent edges
}


\Return{$**List**$}
\caption{Algorithm for MEC decomposition of an MDP.}
\label{5-algo:MEC-decomposition}
\end{algorithm}

```{prf:theorem} needs title 5-thm:MEC-decomposition-complexity
:label: 5-thm:MEC-decomposition-complexity
:nonumber:

The set of all MECs in a given MDP can be computed in polynomial time.

```

```{admonition} Proof
:class: dropdown tip

There are several known algorithms, a simple one is pictured in  {numref}`5-algo:MEC-decomposition`. Each iteration goes as follows: we first take the underlying directed graph of the MDP and find its strongly connected components using some of the well-known polynomial algorithms {cite}`Cormen&Leiserson&Rivest&Stein:2009`. We identify the bottom SCCs, i.e. those from which there is no outgoing edge in the graph. It is easy to see that each such SCC must form a MEC of $\mdp$, and conversely, each MDP has at least one MEC that is also a bottom SCC of its underlying graph. Moreover, for each such bottom SCC $B $ we compute the **random attractor** of $B$, i.e. the set of vertices of $\mdp$ from which $B$ cannot be avoided under any strategy. To this end, we compute, in polynomial time, the almost-surely winning set $ \winAS(\mdp,\Safe(\vertices \setminus B)) $ which is the largest largest (w.r.t. set inclusion) subset of $\vertices$ from which the player can ensure to stay in $\vertices \setminus B$ forever (i.e. the complement of the random attractor of $B$). The computation can be done in polynomial time by  {prf:ref}`5-thm:safety-main`). No vertex of the random attractor of $B$ can belong to a MEC different from $ B $: such a MEC would be disjoint from $ B $ bu the player could not force avoiding $ B $ from within this MEC, a contradiction with MEC being a closed set. Hence, all MECs of $\mdp$ which are not a bottom SCC of $G$ are subsets of $\winAS(\mdp,\Safe(\vertices \setminus B)) \subseteq \vertices \setminus R$, so we can remove all vertices in $R$ from the graph and continue to the next iteration (note that removing vertices in $R$ from $\mdp$ again yields a MDP, since the complement of $R$ is an intersection of closed sets, and thus again a closed set). The main loop performs at most $|\vertices|$ iterations, which yields the polynomial complexity.

```

