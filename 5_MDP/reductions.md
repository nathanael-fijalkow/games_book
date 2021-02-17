(5-sec:reductions)=
# Reductions to optimal reachability

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
\newcommand{\Win}{\textrm{Win}} 
\newcommand{\Lose}{\textrm{Lose}} 
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
\newcommand{\UP}{\textrm{UP}}
\newcommand{\coNP}{\textrm{coNP}}
\newcommand{\coUP}{\textrm{coUP}}
\newcommand{\PSPACE}{\textrm{PSPACE}}
\newcommand{\EXPSPACE}{\textrm{EXPSPACE}}
\newcommand{\EXP}{\textrm{EXP}}
\newcommand{\kEXP}{\textrm{kEXP}}
```
The MEC decomposition can be used to reduce several optimization problems (including general mean-payoff optimization) to optimizing reachability probability. Recall that in the optimal reachability problem, we are given an MDP $\mdp$ (with coloured vertices) and a colour $\Win \in\colours$. The task is to find a strategy $\sigma$ that maximizes $ \probm^\sigma_{\vinit}(\Reach(\Win))$, the probability of reaching a vertex coloured by $\Win$. The main result on reachability MDPs, which we prove in Section {ref}`5-sec:general-reachability`, is as follows:

````{prf:theorem} NEEDS TITLE 5-thm:quant-reachability-main
:label: 5-thm:quant-reachability-main

In reachability MDPs, the value of each vertex is rational and computable in polynomial time. Moreover, we can compute, in polynomial time, a memoryless deterministic strategy that is optimal in every vertex.

````


## From optimal B&uuml;chi to reachability


In B&uuml;chi MDPs, the vertices are assigned colours from the set $\{1,2\}$ and our aim is to find a strategy maximizing $ \probm^\sigma_{\vinit}(\Buchi)$, i.e. maximizing the probability that a vertex coloured by $2$ is visited infinitely often.
We say that a MEC $\mec$ of a B&uuml;chi MDP is **good** if it contains a vertex coloured by 2.

````{prf:theorem} NEEDS TITLE 5-thm:quant-buchi
:label: 5-thm:quant-buchi

In B&uuml;chi MDPs, the value of each vertex is rational and computable in polynomial time. Moreover, we can compute, in polynomial time, a memoryless deterministic strategy that is optimal in every vertex.

````

````{admonition} Proof
:class: dropdown tip

Let $\mdp_b$ be a B&uuml;chi MDP and let $\mdp_r$ be a reachability MDP obtained from $\mdp_b$ by repainting each vertex belonging to a good MEC with the colour $\Win$. Note that $\mdp_r$ can be computed in polynomial time by performing the MEC decomposition of $\mdp_b$ ({numref}`5-algo:MEC-decomposition`) and checking goodness of each MEC.

We prove that the value of each vertex in $\mdp_b$ is equal to the value of the corresponding vertex in $\mdp_r$.

First, fix any $\sigma$ and $\vinit$ (due to equality of underlying graphs, we can view these as a strategy/initial vertex both in $\mdp_b$ and $\mdp_r$). By  {prf:ref}`5-lem:EC-inf`, the probability of visiting infinitely often a vertex outside of a MEC is 0. Hence, the probability of visiting infinitely often a vertex coloured by 2 (in $\mdp_b$) is the same as the probability of visiting infinitely often a vertex coloured by 2 which belongs to (a necessarily good) MEC, which is in turn bounded from above by the probability that $\sigma$ visits (in $\mdp_r$) a vertex coloured by $\Win$.

Conversely, let $\sigma^*$ be the MD reachability-optimal strategy in $\mdp_r$ (which exists by {prf:ref}`5-thm:quant-reachability-main`). We construct a strategy $\sigma$ in $\mdp_b$ which achieves, in every vertex, the same B&uuml;chi-value as the reachability value achieved in that vertex by $\sigma^*$ in $\mdp_r$. Outside of any good MEC, $\sigma$ behaves exactly as $\sigma^*$. Inside a good MEC $\mec$, $\sigma$ behaves as the MD strategy from  {prf:ref}`5-lem:EC-sweep`, ensuring that some fixed vertex in $\mec$ of colour $2$ is almost-surely visited infinitely often. Since $\sigma$ is stitched together from MD strategies on non-overlapping domains, it is memoryless deterministic and it ensures that once a good MEC is reached, the B&uuml;chi condition is satisfied almost-surely.

The construction of $\sigma$ in the aforementioned paragraph is effective: given the optimal strategy $\sigma^*$ for reachability, $\sigma$ can be constructed in polynomial time.

````


## From optimal parity to optimal reachability

In parity MDPs, the vertices are labelled by colours form the set $\{1,\dots,d\}$ (w.l.o.g. we stipulate that $d\leq |\vertices|$) and the goal is to find a strategy maximizing $ \probm^\sigma_{\vinit}(\Parity),$ i.e. maximizing the probability that the largest priority appearing infinitely often along a play is even.

````{prf:theorem} NEEDS TITLE AND LABEL 
\label{5-thm:parity-main}
In Parity MDPs, the value of each vertex is rational and computable in polynomial time. Moreover, we can compute, in polynomial time, a memoryless deterministic strategy that is optimal in every vertex.
 

\label{5-thm:parity-main}
In Parity MDPs, the value of each vertex is rational and computable in polynomial time. Moreover, we can compute, in polynomial time, a memoryless deterministic strategy that is optimal in every vertex.

````

````{admonition} Proof
:class: dropdown tip

Let $\mdp_p$ be a parity MDP. We will proceed similarly to  {prf:ref}`5-thm:quant-buchi`, constructing a reachability MDP $\mdp_r$ with the same underlying graph as $\mdp_p$.

To this end, let $\mdp_i$ be the largest sub-MDP of $\mdp_p$ containing only the vertices of priority $\leq i$. Formally, we set $\vertices_i = \winAS(\mdp_p,\Safe(\colouring^{-1}(\{i+1,\ldots,d\})) )$ and define $\mdp_i$ to be the sub-MDP induced by $\vertices_i$ (note that $\mdp_i$ might be empty). We say that a vertex of $\mdp_p$ is $i$-good if it is contained in some MEC $\mec$ of $\mdp_i$ such that the largest vertex priority inside $\mec$ is equal to $i$. We say that a vertex is even-good if it is $i$-good for some even $i$. We set up a reachability MDP $\mdp_r$ by taking $\mdp_p$ and re-colouring each its even-good vertex with colour $\Win$. To do this, we need to compute, for each even priority $i$, the MDP $\mdp_i$ and its MEC-decomposition. This can be done in polynomial time ({numref}`5-algo:MEC-decomposition`). 

We again prove that the value of every vertex in $\mdp_p$ is equal to the value of the corresponding vertex in $\mdp_r$.

Let $\sigma$ and $\vinit$ be arbitrary. By {prf:ref}`5-lem:EC-inf`, $\probm^\sigma_{\mdp_p,\vinit}(\Parity)$ is equal to the probability that $\Inf(\play)$  is an EC in which the largest priority is even. But each such EC is also an EC of some $\mdp_i$ with even $i$, and thus is also contained in a MEC of a $\mdp_i$ in which the largest priority is $ i $. Hence, $\probm^\sigma_{\mdp_p,\vinit}(\Parity)\leq \probm^\sigma_{\mdp_r,\vinit}(\Reach(\Win))$.

Conversely, let $\sigma^*$ be the MD reachability-optimal strategy in $\mdp_r$. We construct an MD strategy $\sigma$ in $\mdp_p$ as follows: in a vertex $v$ which is not even-good, $\sigma$ behaves as $\sigma^*$. For a vertex $v$ that is even-good, we identify the smallest even $i$ such that $v$ is $i$-good. 
This means that $v$ belongs to some MEC $\mec$ of $\mdp_i$ in which the largest priority is $i$. 
By  {prf:ref}`5-lem:EC-sweep`, we can compute, in polynomial time, an MD strategy $\sigma_M$ which ensures that the largest-priority vertex in $(\mdp_i)_\mec$ is visited infinitely often, and we set $\sigma(v)$ to $\sigma_M(v)$. Note that given $\sigma^*$, the strategy $\sigma$ can be constructed in polynomial time. It remains to show that $\probm^\sigma_{\mdp_p,\vinit}(\Parity)\geq \probm^{\sigma^*}_{\mdp_r,\vinit}(\Reach(\Win))$.

By the construction of $\sigma$, once we reach a vertex which is $i$-good for some even $i$, all the following vertices will be $j$-good for some even $j\leq i$. From this and from  {prf:ref}`5-lem:EC-inf` it follows that $\probm^{\sigma^*}_{\mdp_r,\vinit}(\Reach(\Win))$ is equal to the probability that $\sigma$ produces a play $\play$ with the following property: $\exists i \text{ even}$ such that all but finitely many vertices on $\play$ are $i$-good but are not $j$-good for any even $j<i$. This can be in turn rephrased as the probability that $\Inf(\play)$ is an EC whose all vertices are $i$-good for some even $i$ but none of them is $j$-good for an even $j<i$; we call such an EC **$i$-definite**. But within such an EC, $\sigma$ forever behaves as $\sigma_M$ for some MEC $\mdp$ of $\mdp_i$ in which the maximal priority is $i$. Hence, once an $i$-definite EC is reached, the strategy almost-surely ensures that priority $i$ is visited infinitely often and ensures that no larger priority is ever visited. It follows that  $\probm^{\sigma^*}_{\mdp_r,\vinit}(\Reach(\Win)) = \probm^{\sigma}_{\mdp_p,\vinit}(\inf(\play) \text{ is $i$-definite for even }i ) = \probm^{\sigma}_{\mdp_p,\vinit}(\Parity).$

````


## From general mean-payoff to optimal reachability

We already know how to solve strongly connected mean-payoff MDPs. We now combine this result with MEC decomposition to reduce the general (not strongly connected) mean-payoff optimization to MDP reachability.

We start with a strengthening of  {prf:ref}`5-thm:mp-valcomp`.

````{prf:lemma} NEEDS TITLE 5-lem:MEC-mp-strict-bound
:label: 5-lem:MEC-mp-strict-bound

Let $\mdp$ be a strongly connected mean-payoff MDP and $r^*$ the value of each of its vertices. Then, for each $\sigma$ and $\vinit$ we have $\probm^\sigma_{\vinit}(\MeanPayoffInf > r^*) = 0 $.

````

````{admonition} Proof
:class: dropdown tip

Assume that the statement is not true. Then there exist $\sigma,\vinit$ as well as numbers $\epsilon,\delta>0 $ and $n_0 \in \N$ s.t. the probability of the following set of plays $X_{\epsilon,n_0}$ is at least $\delta$: a play $\play$ belongs to $X_{\epsilon,n_0}$ if for every $n\geq n_0$ it holds $\frac{1}{n}\sum_{i=0}^{n-1}\colouring(\play_i) \geq x^* + \eps$. We construct a new strategy $\sigma'$, which proceeds in a series of episodes. Every episode starts in $\vinit$, and for the first $n_0$ steps of the, episode $\sigma'$ mimics $\sigma$. After that, it checks, in every step $n$, whether the payoff accumulated since the start of the episode is at least $n\cdot(r^* + \eps)$. If this holds, we mimic $\sigma$ for one more step. If the inequality is violated, we immediately restart, i.e. return to $\vinit$ (can be performed with probability $1$ due to the MDP being strongly connected) and once in $\vinit$, start a new episode which mimics $\sigma$ from the beginning. By our assumption, the probability of not performing a reset in a given episode is at least $\delta>0$. Hence, with probability $1$ we witness only finitely many resets, after which we produce a play whose suffix has mean-payoff at least $r^* + e$. By prefix independence of mean-payoff ( {prf:ref}`5-thm:mp-valcomp`), $\expv^{\sigma'}_{\vinit} [\MeanPayoffInf] \geq r^* + \eps,$ a contradiction.

````

We will need to strengthen the previous lemma so that it applies not only to strongly connected MDPs, but also to MECs in some larger MDPs. The strengthening is performed in the following two lemmas. The first lemma says that once we exit a MEC, with some positive probability we will never return.

````{prf:lemma} NEEDS TITLE 5-lem:MEC-noreturn
:label: 5-lem:MEC-noreturn

Let $ \mec $ be a MEC of an MDP $ \mdp $ and let $ v\in \mec $, $ a\in \actions $ be such that $ a $ **is not** $ \mec $-safe in $ v $. Then there exists $ t $ s.t. $ \probTranFunc(t\mid v,a)>0 $ and  $ t \not \in \winAS(\mdp,\Reach(\mec)) $.

````

````{admonition} Proof
:class: dropdown tip

Assume that $ a $ is not $ \mec $-safe in $ v $ and that all $ t $'s with $ \probTranFunc(t\mid v,a)>0 $ belong to $ \winAS(\mdp,\Reach(\mec)) $. Fix the MD strategy $  \sigma $ which is almost-surely winning for reaching $ \mec $ from each vertex of $ \winAS(\mdp,\Reach(\mec)) $ ( {prf:ref}`5-thm:as-char`). For each $ t $ s.t.  $ \probTranFunc(t\mid v,a)>0 $, let $ \mec_t $ denote the set of vertices which can be (with a positive probability) visited under $ \sigma $. Put $ \mec' = \mec \cup (\bigcup_{t\in \vertices,\probTranFunc(t\mid v,a)>0}\mec_t )$. Then $ \mec' $ is closed, since $ \mec $ is closed and since for every $ u $ in some $ \mec_t $ there exists an action (the one selected by $ \sigma $ for $ u $) under which we surely stay in $ \mec_t $. Moreover, the $ \mec'$-induced sub-MDP is strongly connected: each $ t $ with $ \probTranFunc(t\mid v,a)>0 $ is reachable from within $ \mec $ (through $ v $) and thus each vertex in some $\mec_t $ is reachable from $ \mec $. In turn, from each vertex in some $ \mec_t $ (where $ \probTranFunc(t\mid v,a)>0 $) we can reach $ \mec $ without leaving $ \mec_t $, due to the definition of $ \sigma $. Hence, $ \mec' $ is a MEC which strictly contains $ \mec $, a contradiction with the maximality of $ \mec. $

````
 

Given a play $\play$ and strategy $\sigma$, we define a **slice** of $\sigma$ as a strategy $\slice{\sigma}{\play}$ such that for each $\play'$ starting in $\last(\play)$ it holds $\slice{\sigma}{\play}(\play') = \sigma(\play\play')$, while on other plays $\slice{\sigma}{\play}$ just mimics $\sigma$.
%\label{5-lem:MEC-stable}%\end{lemma}%Assume, for contradiction, that there is $\delta > 0$ such that the probability of $E$ is at least $\delta$. Note that we do not immediately have a contradiction with \Cref{xxx}, since $\sigma$ might leave $\mec$. However, there must be $i\geq 0$ such that the probability of leaving $\mec$ after more than $i$ steps is at most $\frac{\delta}{2}$ (otherwise we would leave $\mec$ a.s.). Consider a strategy $\sigma_i$ which mimics $\sigma$, but whenever it is in $v$ after more than $i$ steps, an instruction to play an $\mec$-unsafe action is overriden by some $\mec$-safe action. Since the probability of encountering the override is at most $\frac{\delta}{2}$, the probability of $E$ under $\sigma_i$ is still at least $\frac{\delta}{2}$. But then there is a play prefix $\play_{\leq k}$ such that the probability of $E$ under SLICE (which never leaves $\mec$) from $\last(\play_{\leq k})$ is still positive, a contradiction with \Cref{xxx}.
````{prf:lemma} NEEDS TITLE AND LABEL 
\label{5-lem:MEC-stable}%For every $\eps>0$ there is a stable $\eps$-optimal strategy $\sigma'$. Moreover, 
Let $\mec$ be a MEC of $\mdp$ and $r^*$ the mean-payoff value of every vertex in the strongly connected sub-MDP induced by $\mec$. Then the set $E$ of all plays that have $\Inf(\play)\subseteq\mec$ and at the same time mean payoff greater than $r$ has probability zero under any strategy $\sigma$.
%Let $\mdp$ be a mean-payoff MDP.  

\label{5-lem:MEC-stable}%For every $\eps>0$ there is a stable $\eps$-optimal strategy $\sigma'$. Moreover, 
Let $\mec$ be a MEC of $\mdp$ and $r^*$ the mean-payoff value of every vertex in the strongly connected sub-MDP induced by $\mec$. Then the set $E$ of all plays that have $\Inf(\play)\subseteq\mec$ and at the same time mean payoff greater than $r$ has probability zero under any strategy $\sigma$.
%Let $\mdp$ be a mean-payoff MDP. 
````

````{admonition} Proof
:class: dropdown tip
%We show how to incrementally (by induction on index $i$) construct a $\frac{\eps\cdot i}{\ell}$-optimal strategy such that for each $1 \leq i \leq \ell$, the MECs $\mec_j$ with $j\leq i$ are stable in the sense that $\probm^\sigma_{\vinit}(\Inf(\play) \subseteq \mec) > 0$ implies that $\mec$ is never left.%The base and induction cases are proved analogously, so fix $1\leq i \leq \ell$ and let $\mec = \mec_i$. Let $p$ be the infimum, over all $\frac{\eps}{\ell}$-optimal strategies, of probabilities that $\Inf =\mec$. Fix $\frac{\eps}{\ell}$-optimal strategy $\sigma$ such that $\probm_{\vinit}^\sigma(\Inf(\play)=\mec)\leq p + p_{\min}$, where $p_{\min}$ is the minimal nonzero probability in $\mdp$. Auppose that $\mec = \mec_i$ is unstable under $\sigma$. We will modify $\sigma$ to make $\mec$ stable.  To simplify notation, we will assume in the rest of the proof that $\vinit$ is in $\mec$. If this is not the case, we would need to perform a surgery on $\sigma$, modifying its behaviour after entering $\mec$. %To simplify notation, we can assume that $\vinit$ is in $\mec$, otherwise we would take $\vinit$ to be any vertex of $\mec$ 
 Assume, for contradiction, that there is a strategy $\sigma$ and $\delta > 0$ such that the probability of $E$ under $ \sigma  $ is at least $\delta$. Note that we do not immediately have a contradiction with  {prf:ref}`5-lem:MEC-mp-strict-bound`, since $\sigma$ might leave $\mec$ (and then return back). 
 
 We say that a play $ \play $ **cheats** in step $ i $ if it is inside $ \mec $ in $ i $-th step and outside of $ \mec $ in the next step (which can only be caused by an $ \mec $-unsafe action being played). From  {prf:ref}`5-lem:MEC-noreturn` we have that there is $ p>0 $ s.t. upon every exit from $ \mec $ we return with probability at most $ (1-p) $. Hence, the probability that a play cheats infinitely often is $ 0 $. It follows that there is $ k\in \N $ s.t. $ \probm_{\vinit}^\sigma(\play \text{ cheats after $\geq k $ steps}) \leq (\delta\cdot p_{\min})/4 $, where $ p_{\min} $ is the smallest non-zero edge probability in $ \mdp $. 
 
 Whenever we are in some $ v\in \mec $ and play an action that is not $ \mec $-safe in $ v $, this results into a cheat with  probability at least $ p_{\min} $. Thus, the total probability that this happens after at least $ k $ steps, i.e. the quantity \begin{equation}\label{5-eq:mec-cheat}q= \sum_{i \geq k}\;\sum_{v\in \mec}\;\sum_{a \text{ not $ \mec $-safe in v}}\expv^\sigma_{\vinit}[ \actevent{\sigma}{a}{i}\cdot\indicator{ \out(\play_i)= v} ] , \end{equation}
 is bounded by $ \probm_{\vinit}^\sigma(\play \text{ cheats after more than $ k $ steps})/p_{\min} \leq \delta/4$.
 
 Let's go back to $ E $ now. On each play in $ E $ there is a step $ i $ from which on the play stays in $ \mec $ forever: we say that the play is $ i $-definite and we denote by $E_k$ the set of all $ i $-definite plays in $ E $. By union bound, there is $ \ell \in \N, \ell \geq k $ s.t. $ \probm_{\vinit}^\sigma(E_\ell)  \geq \delta/2$. 
 
 We define a new strategy $ \sigma' $ as follows: on each play prefix, $ \sigma' $ by default mimics $ \sigma $, except for the case when at least $ \ell $ steps have elapsed, the current vertex $ v $ is in $ \mec $, and $ \sigma $ prescribes to play, with positive probability, an action which is not $ \mec $ safe in $ v $. In such a case, $ \sigma $ is overridden and we play any action that is $ \mec $-safe in $ v $ instead (after which we return to simulating $ \sigma $, until the override kicks in again). The probability that such an override happens is bounded by the quantity $ q $ from~\eqref{5-eq:mec-cheat}, and hence by $ \delta/4 $. Since  $ \probm_{\vinit}^\sigma(E_\ell)  \geq \delta/2$, at least half the measure of $ E_{\ell} $ stays untouched by the overrides; hence  $ \probm_{\vinit}^{\sigma'}(E_\ell)\geq \delta/4 $.
 
 We are ready to apply the final argument. There are only finitely many plays of length $ \ell $. Hence, by union bound, there is a play $ \play $ of length $ \ell $ such that $\probm_{\vinit}^{\sigma'}(E_\ell \cap \cylinder(\play))>0$. Consider the strategy  $\slice{\sigma'}{\play}$. 
 Starting in $ \last(\play) $, we have that $\slice{\sigma'}{\play}$ never leaves $ \mec $, due to the overrides in $ \sigma' $. Hence, $\slice{\sigma'}{\play}$ can be seen as a strategy in the strongly connected MDP $ \mdp_\mec $. Now consider the set $ E'=\{\play'\mid \play'\exists\play''\in E \text{ s.t. } \play''=\play\play'\} $. Then $ \probm_{\last(\play)}^{\slice{\sigma'}{\play}}(E') = \probm_{\vinit}^{\sigma'}(E_\ell \cap \cylinder(\play))>0 $; but due to the prefix independence of mean payoff, all plays in $ E' $ have payoff $ > r^* $, a contradiction with  {prf:ref}`5-lem:MEC-mp-strict-bound`.% Instead, note that .% Consider a strategy $\sigma_\ell$ which mimics $\sigma$, but whenever it is in $v$ after more than $\ell$ steps, any instruction to play an $\mec$-unsafe action is overridden by some $\mec$-safe action. This override does not affect any prefixed of plays%  Since the probability of encountering the override is at most $\frac{\delta}{2}$, the probability of $E$ under $\sigma_i$ is still at least $\frac{\delta}{2}$. But then there is a play prefix $\play_{\leq k}$ such that the probability of $E$ under $\sigma_{\play_{\leq _k}}$ (which never leaves $\mec$) from $\last(\play_{\leq k})$ is still positive, a contradiction with  {prf:ref}`5-lem:MEC-mp-strict-bound`.%%
````


````{prf:theorem} NEEDS TITLE 5-thm:general-mp-main
:label: 5-thm:general-mp-main

In mean-payoff MDPs, the value of each vertex is rational and computable in polynomial time. Moreover, we can compute, in polynomial time, a memoryless deterministic strategy that is optimal in every vertex.

````

````{admonition} Proof
:class: dropdown tip

First, note that we can w.l.o.g. restrict to MDPs in which each edge is coloured by a number between $0$ and $ 1 $. To see this, let $\mdp$ be an MDP and $a,b$ any two numbers, with $a$ non-negative. We can construct an MDP $\mdp'$ by re-colouring each edge $(u,v)$ of $\mdp$ with colour $a\cdot \colouring(u,v)+b$, where $\colouring$ is the original colouring in $\mdp$. It is then easy to see that for each strategy $\sigma$ it holds $\expv_{\mdp,\vinit}^\sigma[\MeanPayoffInf]=(\expv_{\mdp',\vinit}^\sigma[\MeanPayoffInf]/a)-b$, so a strategy optimizing the mean payoff in $\mdp'$ is also optimal in $\mdp$. Hence, we always can re-scale the colouring into the unit interval while preserving the optimization criterion.

So now let $\mdp_\smallmp$ be a mean-payoff MDP with edge-colouring $\colouring$. We construct, in polynomial time, a new reachability MDP $\mdp_r$ as follows: first, we compute the MEC decomposition of $\mdp_\smallmp$ ({numref}`5-algo:MEC-decomposition`). Let $\mec_1,\dots,\mec_k$ be all the resulting MECs. For each MEC $\mec_i$ we compute the optimal mean-payoff value $r_i^*$ in the sub-MDP induced by $\mec_i$ (which is shared by all vertices of this sub-MDP, by  {prf:ref}`5-thm:mp-valcomp`), along with the corresponding memoryless deterministic optimal strategy. We already know how to do this in polynomial time ( {prf:ref}`5-thm:mp-rand-opt-main,5-thm:lpmp-basic-dim`). Now we add new vertices $\vgood$, $\vbad$, both with self loops, and edges incoming to these vertices from each vertex that belongs to some MEC of $\mdp_\smallmp$. The vertex $\vgood$ is the only vertex coloured by $\Win$ in $\mdp_r$. Finally, we add a new action $\finact$ which behaves as follows: For each vertex $v$ belonging to a MEC $\mec_i$ we set $\probTranFunc(\vgood\mid v,\finact) = r^*_i$ and $\probTranFunc(\vbad\mid v,\finact) = 1-r^*_i $. In a non-MEC vertex $ v $, we put $ \probTranFunc(v,\finact) = \probTranFunc(v,a) $ for some $ a\in \actions $, $ a\neq \finact $, so that no new behaviour is introduced in these vertices.

We show that for any original vertex (i.e. all vertices but $\vgood,\vbad$) the optimal values in both MDPs are the same and the optimal strategies are easily transferable from one MDP to the other.

First, let $\sigma$ be an $\eps$-optimal strategy in $\mdp_\smallmp$. We have $\expv^\sigma_{\vinit}[\MeanPayoffInf] = \sum_{i=1}^k\expv^\sigma_{\vinit}[\MeanPayoffInf\cdot \indicator{\Inf\subseteq\mec_i}] \leq \sum_{i=1}^k \expv^\sigma_{\vinit}[r_i^*\cdot \indicator{\Inf=\mec_i}] = \sum_{i=1}^k r_i^* \cdot \probm_{\vinit}^\sigma(\Inf=\mec_i) $; here the first equation follows from  {prf:ref}`5-lem:EC-inf` and the subsequent inequality from  {prf:ref}`5-lem:MEC-stable`. Moreover, for each $i$ there is a number $n_0^i$ such that the probability of all plays that stay inside $\mec_i$ in all the steps from $n_0^i$ to infinity is at least $\probm_{\vinit}^\sigma(\Inf\subseteq\mec_i) - \frac{\eps}{k} $. Let $n_0 = \max_{1\leq i \leq k} n^i_0$.

We construct a reachability strategy $\sigma_r$ which mimics $\sigma$ for the first $n_0$ steps. After $n_0$ steps it performs a switch: if the current vertex is in some $\mec_i$ we immediately play the action $\finact$, otherwise we start to behave arbitrarily. We have $\probm_{\vinit}^{\sigma_r}(\Reach(\Win)) \geq \sum_{i=1}^{k} r_i^* \cdot \probm_{\vinit}^{\sigma_r}(\last(\play_{\leq n_0}) \in \mec_i ) \geq \sum_{i=1}^k r_i^* \cdot \probm_{\vinit}^\sigma(\Inf\subseteq\mec_i) - \eps \geq \expv^\sigma_{\vinit}[\MeanPayoffInf] -\eps$, the last equality shown in the previous paragraph. Since $\sigma$ is $\eps$-optimal for mean-payoff, $\probm_{\vinit}^{\sigma_r}(\Reach(\Win))$ is at most $2\eps$ away from the mean-payoff value of $ v $. Since $\eps>0$ was chosen arbitrarily, we get that the reachability value in $\mdp_{r}$ is at least as large as the mean-payoff value in $\mdp_{\smallmp}$.

Conversely, let $\sigma^*$ be the optimal MD strategy in $\mdp_r$. We say that $\sigma^*$ ends in a vertex $v$ if $\sigma^*(v)=\finact$. We can assume that if $\sigma^*$ ends in some $v \in \mec_i$ then it ends in all vertices of $\mec_i$. This is because whenever $\sigma^*$ ends in some vertex $v \in \mec_i$, the reachability value of $v$ must be equal to $r^*_i$, otherwise playing $\finact$ would not be optimal here. But the optimal reachability value in every vertex of a given MEC is the same (due to  {prf:ref}`5-lem:EC-sweep`), so if playing $\finact$ is optimal in some vertex of $\mec_i$, it is optimal in all such vertices. Now we can define an MD strategy $\sigma_{\smallmp}$ in $\mdp_\smallmp$ to initially mimic $\sigma^*$, and upon encountering any MEC $\mec_i$ in which $\sigma^*$ ends, immediately switch to the MD strategy that is optimal in the mean-payoff sub-MDP $\mdp_i$. We have $\expv^{\sigma_{\smallmp}}_{\vinit}[\MeanPayoffInf]  =  \sum_{i=1}^{k} \probm^{\sigma^*}_{\vinit}(\text{end in }\mec_i)\cdot r^*_i = \probm^{\sigma^*}_{\vinit} (\Reach(\Win)). $ Since $\sigma^*$ as well as the optimal strategies in all $\mec_i$ can be computed in polynomial time ( {prf:ref}`5-thm:quant-reachability-main,5-thm:lpmp-basic-dim`), we get the result.
````

