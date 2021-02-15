(5-sec:mean_payoff_properties)=
# Mean-payoff in MDPs: General properties and linear programming

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
\newcommand{\coNP}{\textrm{coNP}}
\newcommand{\PSPACE}{\textrm{PSPACE}}
```
\newcommand{\MeanPayoffOld}{\MeanPayoff}

We will use the $\liminf$ variant of mean-payoff:


$$
\MeanPayoffInf(\play) = \liminf_n \frac{1}{n} \sum_{i = 0}^{n-1} c(\play_i)
$$


In particular, the play-based expected mean-payoff achieved by $ \sigma $ from $ v $ is $ \playPay(v, \sigma) = \expv_v^\sigma[\MeanPayoffInf] $, while for the step-based counterpart we have $ \stepPay(v, \sigma) = \liminf_{n \rightarrow \infty} \frac{1}{n} \sum_{i=0}^{n-1} \expv_v^\sigma[\colouring(\play_i)]$.

The use of $ \liminf $ is natural in the formal verification setting: taking the $\liminf$ rather than $ \limsup $ emphasizes the worst-case behaviour along a play. However, all the results in this section hold also for $\limsup$-based mean-payoff, though some proofs are more complex. See the bibliographic remarks for more details.

In general, $\stepPay(v,\sigma)$ can be different from $ \playPay(v, \sigma) $. However, we have the following simple consequence of the dominated convergence theorem:

```{prf:lemma} NEEDS TITLE AND LABEL 
\label{5-lem:limit-defined}
Let $U$ be the set of all plays $\play$  for which $\lim_{n\rightarrow \infty} \frac{1}{n} \sum_{i=0}^{n-1}[\colouring(\play_i)]$ is undefined. If $\vinit,\sigma$ are such that $\probm^\sigma_{\vinit}(U) = 0$, then $\stepPay(\vinit,\sigma) = \playPay(\vinit, \sigma) $.
 
:label: 
\label{5-lem:limit-defined}
Let $U$ be the set of all plays $\play$  for which $\lim_{n\rightarrow \infty} \frac{1}{n} \sum_{i=0}^{n-1}[\colouring(\play_i)]$ is undefined. If $\vinit,\sigma$ are such that $\probm^\sigma_{\vinit}(U) = 0$, then $\stepPay(\vinit,\sigma) = \playPay(\vinit, \sigma) $.

:nonumber:

\label{5-lem:limit-defined}
Let $U$ be the set of all plays $\play$  for which $\lim_{n\rightarrow \infty} \frac{1}{n} \sum_{i=0}^{n-1}[\colouring(\play_i)]$ is undefined. If $\vinit,\sigma$ are such that $\probm^\sigma_{\vinit}(U) = 0$, then $\stepPay(\vinit,\sigma) = \playPay(\vinit, \sigma) $.

```


In particular, for any finite-memory strategy $ \sigma $, the two values coincide, since applying such a strategy turns an MDP into a finite Markov chain where the existence of the limit can be inferred using decomposition into strongly connected components and applying the Ergodic theorem.
We will show that in our case of finite-state MDPs, the two approaches coincide not only at the levels of finite-memory strategies, but also as optimality criteria: that is, no matter which of the two semantics we use, the optimal values are the same and a strategy that is optimal w.r.t. one of the semantics is also optimal for the other one. We caution the reader that such a result does not automatically transfer to more complex settings, such as infinite-state MDPs or multi-objective optimization. 




To simplify the subsequent notation, we define the **expected one-step** reward of a vertex-action pair $(v,a)$ to be the number $\sum_{w\in \vertices} \probTranFunc(w\mid v,a)\cdot \colouring(v,w)$. Overloading the notation, we denote this quantity by $\colouring(v,a)$.

In mean-payoff  MDPs, a crucial role is played by the linear program $\lpmp$ pictured in {numref}`5-fig:mp-lin`.

\begin{figure}[h]
\begin{alignat}{2}
\text{{maximize}} \quad &\sum_{v\in \vertices, a \in \actions} x_{(v,a)} \cdot \colouring(v,a),\quad \textrm{ 
subject to }\nonumber \\
  \sum_{\substack{u\in\vertices\\ a \in \actions}} x_{(u,a)}\cdot \probTranFunc(v\mid u,a) &= \sum_{a \in \actions} x_{v,a}
&\quad&\text{for all $v\in \vertices$}\label{5-eq:mdp-flow} \\
 \sum_{v\in\vertices,a\in \actions} x_{v,a}&=1 &&\label{5-eq:mdp-freq-1} \\
 x_{v,a} &\geq 0  &&\text{for all $v\in \vertices,a\in \actions$} \label{5-eq:mdp-freq-nonnegp}
\end{alignat}
\caption{The linear program $\lpmp$ with variables $x_{(v,a)}$ for  $v\in \vertices,a\in \actions$.}
\label{5-fig:mp-lin}
\end{figure}

There is a correspondence between feasible solutions of $\lpmp$ and the strategies in the corresponding MDP. Intuitively, in a solution corresponding to a strategy $\sigma$, the value of a variable $x_{v,a}$ describes the expected frequency with which $\sigma$ visits $v$ and plays $a$ upon such a visit. These frequencies must obey the **flow constraints**~\eqref{5-eq:mdp-flow} and must represent a probability distribution, which is ensured by~\eqref{5-eq:mdp-freq-1} and~\eqref{5-eq:mdp-freq-nonnegp}. The objective function then represents the expected mean payoff. Of high importance is also the linear program which is **dual** to $\lpmp$. This dual program, denoted $\lpmpdual$, is pictured in Figure~\ref{5-fig:mp-dual}. (For a refresher on linear programming and duality, see, e.g. {cite}`Matousek:2007`).

\begin{figure}[h]
\begin{alignat}{2}
&\text{{minimize} }\quad g \quad \textrm{ 
subject to }\nonumber \\
&g -\colouring(v,a) + \sum_{u\in\vertices}\probTranFunc(u\mid v,a)\cdot y_u \geq y_v 
\quad\text{for all $(v,a)\in \vertices\times \actions$}\label{5-eq:mp-lpdual}
\end{alignat}
\caption{The linear program $\lpmpdual$ with variables $g$ and $y_v$ for each  $v\in \vertices$.}
\label{5-fig:mp-dual}
\end{figure}

```{admonition} Remark [Nomenclature]
A feasible solution of $ \lpmp $ is a vector $\vec{x} \in \R^{\vertices\times \actions} $ s.t. setting $ x_{(v,a)}=\vec{x}_{(v,a)} $ for all $ (v,a) $ satisfies the constraints in $ \lpmp $. A feasible solution of $ \lpmpdual  $ is a tuple $ (g,\vec{y}) $, where $ g\in\R $ (using the same notation for the number and the variable should not cause  confusion here) and $ \vec{y}\in \R^{\vertices}$ s.t. setting the corresponding variables to numbers prescribed by $ g $ and $ \vec{y} $ satisfies the constraints.

```

The variable $g$ in $\lpmpdual$ is often called **gain** while the vector of $y$-variables is called **bias.** This is because it provides information on how much does the payoff (under some strategy) accumulated up to a certain step deviate from the estimate provided by the mean-payoff value of that strategy. This is illustrated in the following lemma, which forms the first step of our analysis. 

```{prf:lemma} NEEDS TITLE 5-lem:dual-bound-step
:label: 5-lem:dual-bound-step
:nonumber:

Let $({g}, \vec{y})$ be a feasible solution of $\lpmpdual$ and let $Y^{(i)}$, where $i\geq 0$, be a random variable such that $Y^{(i)}(\play)= \vec{y}_{\ing(\pi_i)}.$ Then for each strategy $\sigma$, each vertex $\vinit$, and each $n\geq 0$ it holds $\expv^\sigma_{\vinit}[\sum_{i=0}^{n-1}\colouring(\play_i)]\leq n\cdot {g}- \vec{y}_{\vinit} +\expv^\sigma_{\vinit} [Y^{(n)}]$.

```

```{admonition} Proof
:class: dropdown tip

By induction on $n$. For $n=0$, both sides are equal to 0. Now assume that the inequality holds for some $n\geq 0$. By the induction hypothesis
\begin{align}
\expv^\sigma_{\vinit}[\sum_{i=0}^{n}\colouring(\play_i)] &= \expv^\sigma_{\vinit}[\sum_{i=0}^{n-1}\colouring(\play_i)] + \expv^\sigma_{\vinit}[\colouring(\play_n)] \leq n{g}- \vec{y}_{\vinit} +\expv^\sigma_{\vinit} [Y^{(n)}] + \expv^\sigma_{\vinit}[\colouring(\play_n)] \label{5-eq:mpdual-1}
\end{align}

\begingroup
\allowdisplaybreaks

We now obtain a bound for the third term on the RHS of~\eqref{5-eq:mpdual-1}. In the following, we denote by $\Pi_n$ the set of all plays of length $n$. Then we have
\begin{align*}
\expv^\sigma_v [Y^{(n)}]&= \sum_{v\in\vertices}  \vec{y}_v\cdot\probm^\sigma_{\vinit}(\ing(\pi_n)=v)
=\sum_{v\in\vertices}  \vec{y}_v\cdot \bigg(\sum_{\substack{\play'\in \Pi_n\\ \last(\play')=v}}\probm^\sigma_{\vinit}(\play') \bigg) \\
&=\sum_{v\in\vertices}  \vec{y}_v\cdot \bigg(\sum_{\substack{\play'\in \Pi_n\\ \last(\play')=v}}\probm^\sigma_{\vinit}(\play')\cdot\big(\underbrace{\sum_{a\in\actions}\sigma(a\mid \play')}_{=1} \big)\bigg) \\
&= \sum_{\substack{v\in\vertices\\ a \in \actions}}  \vec{y}_v\cdot \bigg(\sum_{\substack{\play'\in \Pi_n\\ \last(\play')=v}}\probm^\sigma_{\vinit}(\play')\cdot\sigma(a\mid \play')\bigg)\\
\text{(by~\eqref{5-eq:mp-lpdual})}\hspace{3mm}
&{\leq}\sum_{\substack{v\in\vertices\\ a\in \actions}} \bigg( {g} -\colouring(v,a) + \sum_{u\in\vertices}\probTranFunc(u\mid v,a)\cdot  \vec{y}_u\bigg)\cdot\bigg(\sum_{\substack{\play'\in \Pi_n\\ \last(\play')=v}}\probm^\sigma_{\vinit}(\play')\cdot\sigma(a\mid \play')\bigg)\\
&= {g}\cdot\underbrace{\sum_{\substack{v\in\vertices\\ a\in \actions}}\sum_{\substack{\play'\in \Pi_n\\ \last(\play')=v}}\probm^\sigma_{\vinit}(\play')\cdot\sigma(a\mid \play')}_{=1}\\&\quad-\underbrace{\sum_{\substack{v\in\vertices\\ a\in \actions}}\sum_{\substack{\play'\in \Pi_n\\ \last(\play')=v}}\probm^\sigma_{\vinit}(\play')\cdot\sigma(a\mid \play')\cdot\colouring(v,a)}_{=\expv^\sigma_{\vinit}[\colouring(\play_n)]}\\
&\quad +\underbrace{\sum_{\substack{v,u\in \vertices\\ a \in \actions}}\sum_{\substack{\play'\in \Pi_n\\ \last(\play')=v}} \probm^\sigma_{\vinit}(\play')\cdot\sigma(a\mid \play')\cdot \probTranFunc(u\mid v,a)\cdot  \vec{y}_u}_{=\expv^\sigma_{\vinit}[Y^{(n+1)}]}.
\end{align*}
\endgroup

Plugging this into~\eqref{5-eq:mpdual-1} yields the desired $\expv^\sigma_{\vinit}[\sum_{i=0}^{n}\colouring(\play_i)] \leq (n+1) {g}- \vec{y}_{\vinit} + \expv^\sigma_{\vinit}[Y^{(n+1)}]$. 

```


```{prf:corollary} NEEDS TITLE 5-cor:mp-value-bound
:label: 5-cor:mp-value-bound
:nonumber:

Let $g$ be the objective value of some feasible solution of $\lpmpdual$. Then for every strategy $\sigma$ and every vertex $\vinit$ it holds $\playPay(\vinit,\sigma) \leq \stepPay(\vinit,\sigma) \leq g$.

```

```{admonition} Proof
:class: dropdown tip

Let $ ({g}, \vec{y})$ be any feasible solution of $\lpmpdual$.
By  {prf:ref}`5-lem:dual-bound-step` we have, for every $n\geq 0$, that $\expv^\sigma_{\vinit}[\frac{1}{n}\sum_{i=0}^{n-1}\colouring(\play_i)]\leq g - \frac{ \vec{y}_{\vinit}}{n}+ \frac{1}{n}\expv^\sigma_{\vinit} [Y^{(n)}]$. Since $ \vec{y}_{\vinit}$ is a constant and $|\expv^\sigma_{\vinit} [Y^{(n)}]|$ is bounded by the constant $ \max_{v\in \vertices}|\vec{y}_v|$ that is independent of $n$, the last two terms on the RHS vanish as $n$ goes to $\infty$. Hence, also $\stepPay(\vinit,\sigma) = \liminf_{n\rightarrow \infty} \expv^\sigma_{\vinit}[\frac{1}{n}\sum_{i=0}^{n-1}\colouring(\play_i)] \leq g$. It remains to show that we have $\playPay(\vinit,\sigma) \leq \stepPay(\vinit,\sigma)$, but this immediately follows from the Fatou's lemma~\cite[Theorem 1.6.8]{Ash&Doleans-Dade:2000}.

```


```{prf:corollary} NEEDS TITLE 5-cor:lpmp-optimal-exists
:label: 5-cor:lpmp-optimal-exists
:nonumber:

Both the linear programs $\lpmp$ and $\lpmpdual$ have a feasible solution. Hence, both have an optimal solution and the optimal values of the objective functions in these programs are equal.

```

```{admonition} Proof
:class: dropdown tip

One can easily construct a feasible solution for $\lpmpdual$ by setting all the $y$-variables to $0$ and $g$ to $\maxc$. By the duality theorem for linear programming, to show that also $\lpmp$ has feasible solution it suffices to show that the objective function of $\lpmpdual$ is bounded from below. But this follows from \Cref{5-cor:mp-value-bound}, since there is at least one strategy $\sigma$ giving us the lower bound (in particular, the objective function is bounded from below by $-\maxc$). The second part follows immediately by linear programming duality.

```



