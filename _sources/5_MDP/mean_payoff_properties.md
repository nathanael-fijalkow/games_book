(5-sec:mean_payoff_properties)=
# Mean-payoff in MDPs: General properties and linear programming


```{math}
\newcommand{\expv}{\mathbb{E}}
\newcommand{\probm}{\mathbb{P}}
\newcommand{\actions}{A}
\newcommand{\colouring}{c}
\newcommand{\probTranFunc}{\Delta}
\newcommand{\vinit}{v_0}
\newcommand{\maxc}{\max_{\colouring}}
\newcommand{\lpmp}{\lp_{\mathit{mp}}}
\newcommand{\lpmpdual}{\lpmp^{\mathit{dual}}}
\newcommand{\MeanPayoffInf}{\MeanPayoff^{\;-}}
\newcommand{\playPay}{\textsf{p-Payoff}}
\newcommand{\stepPay}{\textsf{s-Payoff}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\vertices}{V}
\newcommand{\ing}{\textrm{In}}
\newcommand{\play}{\pi}
\newcommand{\last}{\textrm{last}}
\newcommand{\MeanPayoff}{\mathtt{MeanPayoff}}
\newcommand{\MeanPayoffOld}{\MeanPayoff}
```

\newcommand{\mathtt{MeanPayoff}\mathtt{MeanPayoff}

We will use the $\liminf$ variant of mean-payoff:


$$
\mathtt{MeanPayoff}{\;-}\pi = \liminf_n \frac{1}{n} \sum_{i = 0}^{n-1} c(\play_i)
$$


In particular, the play-based expected mean-payoff achieved by $ \sigma $ from $ v $ is $ \textsf{p-Payoff}v, \sigma) = \expv_v^\sigma[\mathtt{MeanPayoff}{\;-} $, while for the step-based counterpart we have $ \textsf{s-Payoff}v, \sigma) = \liminf_{n \rightarrow \infty} \frac{1}{n} \sum_{i=0}^{n-1} \expv_v^\sigma[c\play_i)]$.

The use of $ \liminf $ is natural in the formal verification setting: taking the $\liminf$ rather than $ \limsup $ emphasizes the worst-case behaviour along a play. However, all the results in this section hold also for $\limsup$-based mean-payoff, though some proofs are more complex. See the bibliographic remarks for more details.

%In the probabilistic setting, there are two ways of defining the expected mean-payoff under a given strategy $ \sigma $. The first way follows the recipe laid out in the preliminaries to this chapter, i.e. viewing $ \mathtt{MeanPayoff}{\;-}$ as a random variable in the probability space induced by $ \sigma $. In such a case, the mean-payoff achieved by $ \sigma $ from vertex $ v $ is $ \expv_v^\sigma[\mathtt{MeanPayoff}$, i.e. we compute the expectation of mean-payoff over all runs. The second way does just the reverse, i.e. for each time step $i$ we compute the expected reward accumulated in that step and then compute the limit average of these one-step expectations. Formally, the mean-payoff of $ \sigma $ from $ v $ is, according to this semantics, defined as $ \liminf_{ n\rightarrow \infty }  \frac{1}{ n } \sum_{i=0}^{n-1} \expv_v^\sigma [c(\play_i)] $.

In general, $\textsf{s-Payoff}v,\sigma)$ can be different from $ \textsf{p-Payoff}v, \sigma) $. However, we have the following simple consequence of the dominated convergence theorem:

````{prf:lemma} NEEDS TITLE AND LABEL 
\label{5-lem:limit-defined}
Let $U$ be the set of all plays $\pi  for which $\lim_{n\rightarrow \infty} \frac{1}{n} \sum_{i=0}^{n-1}[c\play_i)]$ is undefined. If $v_0\sigma$ are such that $\mathbb{P}\sigma_{v_0(U) = 0$, then $\textsf{s-Payoff}v_0\sigma) = \textsf{p-Payoff}v_0 \sigma) $.
 

\label{5-lem:limit-defined}
Let $U$ be the set of all plays $\pi  for which $\lim_{n\rightarrow \infty} \frac{1}{n} \sum_{i=0}^{n-1}[c\play_i)]$ is undefined. If $v_0\sigma$ are such that $\mathbb{P}\sigma_{v_0(U) = 0$, then $\textsf{s-Payoff}v_0\sigma) = \textsf{p-Payoff}v_0 \sigma) $.

````


In particular, for any finite-memory strategy $ \sigma $, the two values coincide, since applying such a strategy turns an MDP into a finite Markov chain where the existence of the limit can be inferred using decomposition into strongly connected components and applying the Ergodic theorem.
We will show that in our case of finite-state MDPs, the two approaches coincide not only at the levels of finite-memory strategies, but also as optimality criteria: that is, no matter which of the two semantics we use, the optimal values are the same and a strategy that is optimal w.r.t. one of the semantics is also optimal for the other one. We caution the reader that such a result does not automatically transfer to more complex settings, such as infinite-state MDPs or multi-objective optimization. 





%An MDP is **strongly connected** if for each pair of vertices $u,v$ there exists a finite play from $u$ to $v$. 



To simplify the subsequent notation, we define the **expected one-step** reward of a vertex-action pair $(v,a)$ to be the number $\sum_{w\in V \Deltaw\mid v,a)\cdot cv,w)$. Overloading the notation, we denote this quantity by $cv,a)$.

In mean-payoff  MDPs, a crucial role is played by the linear program $\lp_{\mathit{mp}} pictured in {numref}`5-fig:mp-lin`.


\begin{figure}[h]
\begin{alignat}{2}
\text{{maximize}} \quad &\sum_{v\in V a \in A x_{(v,a)} \cdot cv,a),\quad \textrm{ 
subject to }\nonumber \\
  \sum_{\substack{u\inV\ a \in A} x_{(u,a)}\cdot \Deltav\mid u,a) &= \sum_{a \in A x_{v,a}
&\quad&\text{for all $v\in V}\label{5-eq:mdp-flow} \\
 \sum_{v\inVa\in A x_{v,a}&=1 &&\label{5-eq:mdp-freq-1} \\
 x_{v,a} &\geq 0  &&\text{for all $v\in Va\in A} \label{5-eq:mdp-freq-nonnegp}

\end{alignat}
\caption{The linear program $\lp_{\mathit{mp}} with variables $x_{(v,a)}$ for  $v\in Va\in A.}
\label{5-fig:mp-lin}
\end{figure}

There is a correspondence between feasible solutions of $\lp_{\mathit{mp}} and the strategies in the corresponding MDP. Intuitively, in a solution corresponding to a strategy $\sigma$, the value of a variable $x_{v,a}$ describes the expected frequency with which $\sigma$ visits $v$ and plays $a$ upon such a visit. These frequencies must obey the **flow constraints**~\eqref{5-eq:mdp-flow} and must represent a probability distribution, which is ensured by~\eqref{5-eq:mdp-freq-1} and~\eqref{5-eq:mdp-freq-nonnegp}. The objective function then represents the expected mean payoff. Of high importance is also the linear program which is **dual** to $\lp_{\mathit{mp}}. This dual program, denoted $\lp_{\mathit{mp}}{\mathit{dual}}, is pictured in Figure~\ref{5-fig:mp-dual}. (For a refresher on linear programming and duality, see, e.g. {cite}`Matousek:2007`).

\begin{figure}[h]
\begin{alignat}{2}
&\text{{minimize} }\quad g \quad \textrm{ 
subject to }\nonumber \\
&g -cv,a) + \sum_{u\inV\Deltau\mid v,a)\cdot y_u \geq y_v 
\quad\text{for all $(v,a)\in Vtimes A}\label{5-eq:mp-lpdual}

%x_{v,a} &\geq 0  &&\text{for all $v\in Va\in A}

\end{alignat}
\caption{The linear program $\lp_{\mathit{mp}}{\mathit{dual}} with variables $g$ and $y_v$ for each  $v\in V.}
\label{5-fig:mp-dual}
\end{figure}

````{admonition} Remark [Nomenclature]
A feasible solution of $ \lp_{\mathit{mp}}$ is a vector $\vec{x} \in \mathbb{R}{Vtimes A $ s.t. setting $ x_{(v,a)}=\vec{x}_{(v,a)} $ for all $ (v,a) $ satisfies the constraints in $ \lp_{\mathit{mp}}$. A feasible solution of $ \lp_{\mathit{mp}}{\mathit{dual}} $ is a tuple $ (g,\vec{y}) $, where $ g\in\mathbb{R}$ (using the same notation for the number and the variable should not cause  confusion here) and $ \vec{y}\in \mathbb{R}{V$ s.t. setting the corresponding variables to numbers prescribed by $ g $ and $ \vec{y} $ satisfies the constraints.

````

The variable $g$ in $\lp_{\mathit{mp}}{\mathit{dual}} is often called **gain** while the vector of $y$-variables is called **bias.** This is because it provides information on how much does the payoff (under some strategy) accumulated up to a certain step deviate from the estimate provided by the mean-payoff value of that strategy. This is illustrated in the following lemma, which forms the first step of our analysis. 

````{prf:lemma} NEEDS TITLE 5-lem:dual-bound-step
:label: 5-lem:dual-bound-step

Let $({g}, \vec{y})$ be a feasible solution of $\lp_{\mathit{mp}}{\mathit{dual}} and let $Y^{(i)}$, where $i\geq 0$, be a random variable such that $Y^{(i)}(\pi= \vec{y}_{\textrm{In}\pi_i)}.$ Then for each strategy $\sigma$, each vertex $v_0, and each $n\geq 0$ it holds $\mathbb{E}\sigma_{v_0[\sum_{i=0}^{n-1}c\play_i)]\leq n\cdot {g}- \vec{y}_{v_0 +\mathbb{E}\sigma_{v_0 [Y^{(n)}]$.

````

````{admonition} Proof
:class: dropdown tip

By induction on $n$. For $n=0$, both sides are equal to 0. Now assume that the inequality holds for some $n\geq 0$. By the induction hypothesis
\begin{align}
\mathbb{E}\sigma_{v_0[\sum_{i=0}^{n}c\play_i)] &= \mathbb{E}\sigma_{v_0[\sum_{i=0}^{n-1}c\play_i)] + \mathbb{E}\sigma_{v_0[c\play_n)] \leq n{g}- \vec{y}_{v_0 +\mathbb{E}\sigma_{v_0 [Y^{(n)}] + \mathbb{E}\sigma_{v_0[c\play_n)] \label{5-eq:mpdual-1}
\end{align}

\begingroup
\allowdisplaybreaks

We now obtain a bound for the third term on the RHS of~\eqref{5-eq:mpdual-1}. In the following, we denote by $\Pi_n$ the set of all plays of length $n$. Then we have
\begin{align*}
\mathbb{E}\sigma_v [Y^{(n)}]&= \sum_{v\inV  \vec{y}_v\cdot\mathbb{P}\sigma_{v_0(\textrm{In}\pi_n)=v)
=\sum_{v\inV  \vec{y}_v\cdot \bigg(\sum_{\substack{\pi\in \Pi_n\\ \textrm{last}\pi)=v}}\mathbb{P}\sigma_{v_0(\pi) \bigg) \\
&=\sum_{v\inV  \vec{y}_v\cdot \bigg(\sum_{\substack{\pi\in \Pi_n\\ \textrm{last}\pi)=v}}\mathbb{P}\sigma_{v_0(\pi)\cdot\big(\underbrace{\sum_{a\inA\sigma(a\mid \pi)}_{=1} \big)\bigg) \\
&= \sum_{\substack{v\inV\ a \in A}  \vec{y}_v\cdot \bigg(\sum_{\substack{\pi\in \Pi_n\\ \textrm{last}\pi)=v}}\mathbb{P}\sigma_{v_0(\pi)\cdot\sigma(a\mid \pi)\bigg)\\
\text{(by~\eqref{5-eq:mp-lpdual})}\hspace{3mm}
&{\leq}\sum_{\substack{v\inV\ a\in A} \bigg( {g} -cv,a) + \sum_{u\inV\Deltau\mid v,a)\cdot  \vec{y}_u\bigg)\cdot\bigg(\sum_{\substack{\pi\in \Pi_n\\ \textrm{last}\pi)=v}}\mathbb{P}\sigma_{v_0(\pi)\cdot\sigma(a\mid \pi)\bigg)\\
&= {g}\cdot\underbrace{\sum_{\substack{v\inV\ a\in A}\sum_{\substack{\pi\in \Pi_n\\ \textrm{last}\pi)=v}}\mathbb{P}\sigma_{v_0(\pi)\cdot\sigma(a\mid \pi)}_{=1}\\&\quad-\underbrace{\sum_{\substack{v\inV\ a\in A}\sum_{\substack{\pi\in \Pi_n\\ \textrm{last}\pi)=v}}\mathbb{P}\sigma_{v_0(\pi)\cdot\sigma(a\mid \pi)\cdotcv,a)}_{=\mathbb{E}\sigma_{v_0[c\play_n)]}\\
&\quad +\underbrace{\sum_{\substack{v,u\in V\ a \in A}\sum_{\substack{\pi\in \Pi_n\\ \textrm{last}\pi)=v}} \mathbb{P}\sigma_{v_0(\pi)\cdot\sigma(a\mid \pi)\cdot \Deltau\mid v,a)\cdot  \vec{y}_u}_{=\mathbb{E}\sigma_{v_0[Y^{(n+1)}]}.
\end{align*}
\endgroup

Plugging this into~\eqref{5-eq:mpdual-1} yields the desired $\mathbb{E}\sigma_{v_0[\sum_{i=0}^{n}c\play_i)] \leq (n+1) {g}- \vec{y}_{v_0 + \mathbb{E}\sigma_{v_0[Y^{(n+1)}]$. 

````


````{prf:corollary} NEEDS TITLE 5-cor:mp-value-bound
:label: 5-cor:mp-value-bound

Let $g$ be the objective value of some feasible solution of $\lp_{\mathit{mp}}{\mathit{dual}}. Then for every strategy $\sigma$ and every vertex $v_0 it holds $\textsf{p-Payoff}v_0\sigma) \leq \textsf{s-Payoff}v_0\sigma) \leq g$.

````

````{admonition} Proof
:class: dropdown tip

Let $ ({g}, \vec{y})$ be any feasible solution of $\lp_{\mathit{mp}}{\mathit{dual}}.
By  {prf:ref}`5-lem:dual-bound-step` we have, for every $n\geq 0$, that $\mathbb{E}\sigma_{v_0[\frac{1}{n}\sum_{i=0}^{n-1}c\play_i)]\leq g - \frac{ \vec{y}_{v_0}{n}+ \frac{1}{n}\mathbb{E}\sigma_{v_0 [Y^{(n)}]$. Since $ \vec{y}_{v_0$ is a constant and $|\mathbb{E}\sigma_{v_0 [Y^{(n)}]|$ is bounded by the constant $ \max_{v\in V|\vec{y}_v|$ that is independent of $n$, the last two terms on the RHS vanish as $n$ goes to $\infty$. Hence, also $\textsf{s-Payoff}v_0\sigma) = \liminf_{n\rightarrow \infty} \mathbb{E}\sigma_{v_0[\frac{1}{n}\sum_{i=0}^{n-1}c\play_i)] \leq g$. It remains to show that we have $\textsf{p-Payoff}v_0\sigma) \leq \textsf{s-Payoff}v_0\sigma)$, but this immediately follows from the Fatou's lemma~\cite[Theorem 1.6.8]{Ash&Doleans-Dade:2000}.

````


````{prf:corollary} NEEDS TITLE 5-cor:lpmp-optimal-exists
:label: 5-cor:lpmp-optimal-exists

Both the linear programs $\lp_{\mathit{mp}} and $\lp_{\mathit{mp}}{\mathit{dual}} have a feasible solution. Hence, both have an optimal solution and the optimal values of the objective functions in these programs are equal.

````

````{admonition} Proof
:class: dropdown tip

One can easily construct a feasible solution for $\lp_{\mathit{mp}}{\mathit{dual}} by setting all the $y$-variables to $0$ and $g$ to $\max_{c. By the duality theorem for linear programming, to show that also $\lp_{\mathit{mp}} has feasible solution it suffices to show that the objective function of $\lp_{\mathit{mp}}{\mathit{dual}} is bounded from below. But this follows from \Cref{5-cor:mp-value-bound}, since there is at least one strategy $\sigma$ giving us the lower bound (in particular, the objective function is bounded from below by $-\max_{c). The second part follows immediately by linear programming duality.

````




