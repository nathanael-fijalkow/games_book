(5-sec:optimal_reachability)=
# Optimal reachability

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
In this final section, we prove  {prf:ref}`5-thm:quant-reachability-main`. The proof bears many similarities to the methods for discounted MDPs, hence we only sketch the process and point out the key differences. Throughout the section we assume that **targets are sinks**, i.e. that a vertex coloured by $\Win$ has only a self loop as the single outgoing edge. Modifying an MDP to accommodate this does not influence reachability probabilities in any way.

Consider the reachability operator $\ReachOp\colon[0,1]^{\vertices}\rightarrow [0,1]^{\vertices}$ such that for $\vec{y} = \ReachOp(\vec{x})$ it holds


$$
\vec{y}_v = \begin{cases}

 \max_{a\in \actions} \sum_{u\in \vertices} \probTranFunc(u \mid v,a)\cdot x_u & \colouring(v) \neq \Win \\
 1 & \colouring(v) = \Win.
\end{cases} 
$$



```{prf:lemma} needs title 5-lem:quant-reach-operator-fixed-point
:label: 5-lem:quant-reach-operator-fixed-point
:nonumber:

For each initial vector $\vec{x}$, the limit $\lim_{k \rightarrow \infty}\ReachOp^k(\vec{x})$ exists. Moreover, if $\vec{x} \leq \ReachOp(\vec{x})$, then the limit is equal to the least fixed point of $\ReachOp$ that is greater than or equal to $\vec{x}$; if $\ReachOp(\vec{x})\leq \vec{x}$, then the limit is equal to the greatest fixed point of $\ReachOp$ that is less than or equal to $\vec{x}$.

```

```{admonition} Proof
:class: dropdown tip

The existence of the limit follows from the monotonicity of $\ReachOp$.
In addition, it can be easily checked that the set $[0,1]^{\vertices}$ is a directed complete partial order and that $\ReachOp$ is a Scott-continuous operator on this set. Hence, the result follows from the Kleene's theorem (see also Tarski-Kantorovich principle).

```

We denote by $\Reach^k(\Win)$ the set of all plays that reach $\Win$ within the first $k$ steps. Clearly, for each $\sigma$ and $\vinit$ we have $\lim_{k \rightarrow \infty} \probm^\sigma_{\vinit}(\Reach^k(\Win)) = \probm^\sigma_{\vinit}(\Reach(\Win))$.

```{prf:lemma} needs title 5-lem:quant-reach-step-operator
:label: 5-lem:quant-reach-step-operator
:nonumber:

For each $k\in \N$ and $v\in \vertices$, $\ReachOp^k(\vec{0})_v = \sup_{\sigma}\probm^\sigma_v(\Reach^k(\Win))$. In particular, the vector $\vec{x}^* = \lim_{k \rightarrow\infty} \ReachOp^k(\vec{0})$ is the least fixed point of $ \ReachOp $ and it is equal to the vector of reachability values. 

```

```{admonition} Proof
:class: dropdown tip

The first part can be proved by a straightforward induction, the second part follows by  {prf:ref}`5-lem:quant-reach-operator-fixed-point` and a simple limiting argument.

```



Similarly to  {prf:ref}`5-def:disc-safe-act` we say that an action $a$ is $\vec{x}$-safe in $v$ if it holds that $a= \underset{a' \in \actions}{\arg\max} \sum_{u\in \vertices} 
\probTranFunc(u\mid v,a') \cdot\vec{x}_u.$ Recall that a strategy $\sigma$ is $\vec{x}$-safe if all actions selected in a vertex with non-zero probability are $\vec{x}$-safe in that vertex. 

```{prf:lemma} needs title 5-lem:quant-reach-value-distribution
:label: 5-lem:quant-reach-value-distribution
:nonumber:

Let $ \vec{x}^* $ be as in  {prf:ref}`5-lem:quant-reach-step-operator`. 
Next, let $Z^{(n)}$ be a random variable which for a given time step $n$ looks at the current vertex $v$ after $n$ steps and returns the value $\vec{x}^*_v$. Then for every $\vec{x}^*$-safe strategy $\sigma$ it holds $\expv^\sigma_{\vinit}[Z^{(n)}] = \vec{x}^*_{\vinit}$. Moreover, it holds $\expv^\sigma_{\vinit}[Z^{(n)}\cdot \indicator{\colouring{(\Out{(\play_{n})})}=\Win}] = \probm^\sigma_{\vinit}(\Reach^n(\Win)).$

```

```{admonition} Proof
:class: dropdown tip

By an easy induction on $n$, using the fact that target states are  sinks.

```



Now an analogue of  {prf:ref}`5-lem:disc-val-lower` does not hold for reachability: a strategy playing only $\vec{x}^*$-safe actions might not be optimal (indeed, it might not reach $\Win$ at all). Instead, we proceed as follows: Let $\mdp^*$ be an MDP in which we disable, in each state $v$, all actions that are not $\vec{x}^*$-safe in $v$. This can be formally done by adding a new non-target sink vertex $ \mathit{sink} $, an edge from each original vertex to $ \mathit{sink} $, and stipulating that each action $a$ that is disabled in a vertex $ v $ chooses, when played in $ v $ in $ \mdp^*$, the edge leading to $ \mathit{sink} $ with probability 1. 

```{prf:lemma} needs title 5-lem:quant-reach-pruning-unsafe
:label: 5-lem:quant-reach-pruning-unsafe
:nonumber:

The vectors of reachability values $ \Value(\mdp)$ and $\Value(\mdp^*) $ are equal.
In particular, $ \winPos(\mdp,\Reach(\Win)) = \winPos(\mdp^*,\Reach(\Win)).$

```

```{admonition} Proof
:class: dropdown tip

Let $\vec{x}^*$ again denote the vector of optimal values in $\mdp$. If all actions in $ \mdp $ are $\vec{x}^*$-safes, then the lemma clearly holds. Otherwise there is some $\delta\in(0,1)$ such that for each action $a$ that is not $\vec{x}^*$-safe in some vertex $ v $ it holds $\sum_{u\in \vertices} \probTranFunc(u\mid v,a) \cdot\vec{x}_u \leq \vec{x}^*_v - \delta$.

Let $\epsilon \in(0,\delta)$ be arbitrary and fix an $\epsilon$-optimal strategy $\sigma$ in $\mdp$. We will show that there is a $(2\eps/\delta)$-optimal  strategy $\sigma'$ which only uses $\vec{x}^*$-safe actions. Since $\eps$ can be chosen arbitrarily close to $0$, this shows that $\vec{x}^*$-safe strategies can get arbitrarily close to the value, hence $\Value(\mdp^*)=\Value(\mdp)$.

The strategy $\sigma'$ initially mimics $\sigma$ up to the first point in time when an action that is not $\vec{x}^*$-safe in the current vertex is to be selected. At this point $\sigma'$ switches to behave as any $\vec{x}^*$-safe strategy. To analyse the value achieved by $\sigma'$, we need to bound the probability of the event $\mathit{NonSafe}$ that the switch occurs. By the same reasoning as in  {prf:ref}`5-lem:quant-reach-value-distribution`, we can show that for all $n$ it holds $\probm^\sigma_{\vinit}(\Reach^n(\Win)) \leq \expv^\sigma_{\vinit}[Z^{(n)}] \leq  \vec{x}^*_{\vinit}- \delta\cdot\probm_{\vinit}^\sigma(\mathit{NonSafe^{(n)}})$, where $\mathit{NonSafe^{(n)}}$ is the probability that a switch occurs in the first $n$ steps. By taking $n$ to the limit we get $\probm^\sigma_{\vinit}(\Reach(\Win)) \leq \vec{x}^*_{\vinit}- \delta\cdot\probm_{\vinit}^\sigma(\mathit{NonSafe})$. At the same time $\vec{x}^*_{\vinit}-\eps\leq  \probm^\sigma_{\vinit}(\Reach(\Win))$. Combining these two inequalities yields $\probm_{\vinit}^\sigma(\mathit{NonSafe}) \leq  \frac{\eps}{\delta}.$ Now clearly $\probm_{\vinit}^{\sigma'}(\Reach(\Win)) \geq \vec{x}^*_{\vinit} - \eps - \probm_{\vinit}^{\sigma}(\mathit{NonSafe}) \geq \vec{x}^*_{\vinit} - \eps - \eps/\delta \geq \vec{x}^*_{\vinit} -2\eps/\delta$.

```


```{prf:lemma} needs title 5-lem:quant-reach-strat-contsruction
:label: 5-lem:quant-reach-strat-contsruction
:nonumber:

Given the vector $\vec{x}^*$ of optimal reachability values, we can compute, in polynomial time, the optimal MD reachability strategy in $\mdp$.

```

```{admonition} Proof
:class: dropdown tip

Given $\vec{x}^*$, we construct the MDP $\mdp^*$ and compute the winning strategy $\sigma$ for positive reachability in $\mdp^*$. We already know that $\sigma$ can be taken memoryless and computed in polynomial time ( {prf:ref}`5-thm:positive-char`). We claim that $\sigma$ is an optimal reachability strategy in $\mdp$. By  {prf:ref}`5-lem:quant-reach-pruning-unsafe` it suffices to show that $\sigma$ is optimal in $\mdp^*$. Let $W$ be the winning region for positive reachability in $\mdp^*$. Since $\sigma$ is memoryless, with probability $1$ we reach either $\Win$ or a vertex of value $0$ (from which we cannot return to $W$ anymore); in other words, for almost all plays $\play$ we have that $\indicator{\Out(\play_n)\in W}$ eventually equals $\indicator{\colouring(\Out(\play_n)) = \Win}$. Hence, using  {prf:ref}`5-lem:quant-reach-value-distribution` we get $\vec{x}^*_{\vinit} = \lim_{n\rightarrow\infty}\expv^\sigma_{\vinit}[Z^{(n)}] = \expv^\sigma_{\vinit}[\lim_{n\rightarrow\infty} Z^{(n)}] = \expv^\sigma_{\vinit}[\lim_{n\rightarrow\infty} Z^{(n)}\cdot\indicator{\Out(\play_n)\in W}] = \expv^\sigma_{\vinit}[\lim_{n\rightarrow\infty} Z^{(n)}\cdot \indicator{\colouring(\Out(\play_{n})) = \Win } ] = \probm_{\vinit}^\sigma(\Reach(\Win))$. Here, the third equality holds since $ \vec{x}^*_v $ is zero for $ v\not\in W $, while the  swapping of expectations and limits can be performed due to the dominated convergence theorem.

```

To finish the proof of  {prf:ref}`5-thm:quant-reachability-main`, it remains to prove that the vector of optimal values $\vec{x}^*$ can be computed in polynomial time. We again employ linear programming. 

\begin{figure}[h]
\begin{align*}
&\text{minimize} \sum_{v\in \vertices} x_v, \text{ subject to }&\\
x_v &=1 &\text{if $\colouring({v}) = \Win$}\\
x_v &=0 &\text{if $v \not \in \winPos(\mdp,\Reach(\Win))$  } \\
x_v &\geq \sum_{u\in \vertices} \probTranFunc(u\mid v,a)\cdot x_u&\text{for all other $v\in \vertices$ and $a\in \actions$.}\end{align*}
\caption{The linear program $\lpreach$ with variables $x_v$, $v\in \vertices$.}
\label{5-fig:reach-lp}
\end{figure}

```{prf:lemma} needs title and label 
\label{5-lem:quant-reach-lp}
The linear program $\lpreach$ in  {numref}`5-fig:reach-lp` has a unique optimal solution 
$\bar{\vec{x}}$ such that $\bar{\vec{x}} = \vec{x}^*$.
 
:label: 
\label{5-lem:quant-reach-lp}
The linear program $\lpreach$ in  {numref}`5-fig:reach-lp` has a unique optimal solution 
$\bar{\vec{x}}$ such that $\bar{\vec{x}} = \vec{x}^*$.

:nonumber:

\label{5-lem:quant-reach-lp}
The linear program $\lpreach$ in  {numref}`5-fig:reach-lp` has a unique optimal solution 
$\bar{\vec{x}}$ such that $\bar{\vec{x}} = \vec{x}^*$.

```

```{admonition} Proof
:class: dropdown tip

Clearly $\vec{x}^*$ is a feasible solution of $\lpreach$. Similarly to  {prf:ref}`5-lem:disc-lp` we prove that each feasible solution $\vec{x}$ of $\lpreach$ satisfies $\vec{x}\geq \vec{x}^*$. We can proceed analogously  to  {prf:ref}`5-lem:disc-lp`, just replacing the operator $\discOP$ with $\ReachOp$. The proof can be mimicked up to the point where we get that $\lim_{k\rightarrow \infty} \ReachOp^k (\vec{x}) \leq \vec{x}$ (the limit exists by  {prf:ref}`5-lem:quant-reach-operator-fixed-point`). Since $\ReachOp(\vec{x})\leq \vec{x}$ for each feasible solution $\vec{x}$, from  {prf:ref}`5-lem:quant-reach-operator-fixed-point` we get that the limit is a fixed point of $\ReachOp$, and in hence it is greater or equal to the least fixed point of $\ReachOp$, i.e. $\vec{x}^*$ ( {prf:ref}`5-lem:quant-reach-step-operator`). Hence, also $\vec{x} \geq \lim_{k\rightarrow \infty} \ReachOp^k (\vec{x}_0)\geq \vec{x}^*$. 

```

\noindent
Lemmas \ref{5-lem:quant-reach-strat-contsruction} and \ref{5-lem:quant-reach-lp} give us  {prf:ref}`5-thm:quant-reachability-main`.
