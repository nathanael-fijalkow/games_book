(5-sec:discounted)=
# Discounted payoff in MDPs

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
In this section, we consider MDPs with edges coloured by rational numbers 
and with the objective $\DiscountedPayoff$, defined in the same way as in 
\Cref{chap:payoffs}. We start the chapter by proving that using the play-based semantics for the discounted-payoff objective yields no loss of generality. 

````{prf:lemma} NEEDS TITLE AND LABEL 
\label{5-lem:disc-step-one}
In a discounted-payoff MDP, for each strategy $ \sigma $ and each vertex $ v $ it holds $ \playPay(v, \sigma) = \stepPay(v, \sigma) $.
 

\label{5-lem:disc-step-one}
In a discounted-payoff MDP, for each strategy $ \sigma $ and each vertex $ v $ it holds $ \playPay(v, \sigma) = \stepPay(v, \sigma) $.

````

````{admonition} Proof
:class: dropdown tip

We have 
\begin{align*} \playPay(v,\sigma) &= \expv^\sigma_v[(1-\lambda)\lim_{k \rightarrow \infty} \sum_{i=0}^{k-1}\lambda^i \colouring(\play_i) ] = (1-\lambda) \lim_{k \rightarrow \infty} \expv^\sigma_v[\sum_{i=0}^{k-1}\lambda^i \colouring(\play_i) ] 
\\
&= (1-\lambda)\cdot\lim_{k \rightarrow \infty} \sum_{i=0}^{k-1}\lambda^i\expv^\sigma_v[ \colouring(\play_i) ] = \stepPay(v, \sigma).
\end{align*}

%
Here, the last equality on the first line follows from the dominated convergence theorem~\cite[Theorem 1.6.9]{Ash&Doleans-Dade:2000} and the following equality comes from the linearity of expectation. (To apply the dom. convergence 
theorem, we use the fact that for each 
$k$ we have $\DiscountedPayoff^{k}(\play)\leq \maxc.
$)

````


## Optimal values and memoryless optimality

 In this sub-section we give a 
characterization of the value vector $\Value(\mdp)$ and prove that there always exists a 
memoryless deterministic strategy that is optimal in every vertex. Our 
exposition follows (in a condensed form) the one in {cite}`Puterman:2005`, the techniques 
being somewhat similar to the ones in the previous chapter.

%

%reachability value $\Value(v)$ of a given vertex as well as optimal 

%We start with a characterization of $\Value(v)$ in terms of a fixed point of a 

%this 

%$\Reach(\genColour)$, 

We define an operator $\discOP\colon 
\R^{\vertices}\rightarrow \R^{\vertices}$ as follows: each vector 
$\vec{x}$
is mapped to a vector 
$\vec{y}

= \discOP(\vec{x})$ such that:

$$

\vec{y}_v = \max_{a \in \actions} \sum_{u\in \vertices} \probTranFunc(u\mid 
v,a) 
\cdot\left((1-\lambda)\cdot\colouring(v,u) + \lambda\cdot \vec{x}_u \right).

%\max_{a \in \actions} \sum_{u\in\in \vertices} \probTranFunc(u\mid v,a) \cdot 

%\end{cases}

$$


````{prf:lemma} NEEDS TITLE 5-lem:fixpoint
:label: 5-lem:fixpoint

The operator $\discOP$ is a contraction mapping. Hence, $\discOP$ has a unique 
fixed point $\vec{x}^*$ in $\R^{\vertices}$, and $\vec{x}^* = 
\lim_{k\rightarrow \infty} \discOP^k(\vec{x})$, for any 
$\vec{x}\in\R^{\vertices}$.

````

````{admonition} Proof
:class: dropdown tip

The proof proceeds by a computation analogous to the one in the first half of 
the proof of {prf:ref}`4-thm:discounted`; we just need to reason about actions 
rather than edges (and of course, use the formula defining $\discOP$ instead of 
the one for games). The second part follows from the Banach fixed-point theorem.

````

We aim to prove that $\Value(\mdp)$ is the unique fixed point $\vec{x}^*$ of 
$\discOP$. We start with an auxiliary definition.

````{prf:definition} NEEDS TITLE 5-def:disc-safe-act
:label: 5-def:disc-safe-act

Let $\vec{x}\in \R^{\vertices}$. We say that an action $a$ is $\vec{x}$-safe in 
a vertex $v$ if
\begin{equation}
\label{5-eq:disc-safe-act}
a= \underset{a' \in \actions}{\arg\max} \sum_{u\in \vertices} 
\probTranFunc(u\mid 
v,a') 
\cdot\left((1-\lambda)\cdot\colouring(v,u) + \lambda\cdot \vec{x}_u \right).
\end{equation}

A strategy $\sigma$ is $\vec{x}$-safe, if for 
each play $ \play $ ending in a vertex $v$, all actions that are selected with a positive 
probability by $\sigma$ for $\play$ are $\vec{x}$-safe in $v$.

````


Given a strategy $\sigma$ we define $\valsigma$ to be the vector such that $\vec{x}_{v}^\sigma = 
\playPay(v,\sigma)$. For memoryless strategies, $\valsigma$ can be computed efficiently as follows:
Each memoryless strategy $\sigma$ defines a **linear** operator $\discOP_{\sigma}$ which maps each vector 
$\vec{x}\in \R^{\vertices}$ to a vector $\vec{y}=\discOP_{\sigma}(\vec{x})$ 
such that 
$$
\vec{y}_v = \sum_{a\in \actions} \sigma(a\mid v) \cdot 
\left(\sum_{u \in \vertices} 
\probTranFunc(u \mid v,a) \cdot( (1-\lambda)\cdot \colouring(u,v) + 
\lambda \cdot \vec{x}_u )\right).
$$
  

````{prf:lemma} NEEDS TITLE 5-lem:disc-val-sigma
:label: 5-lem:disc-val-sigma

Let $\sigma$ be a memoryless strategy using rational probabilities. Then the operator $\discOP_{\sigma}$ has a unique fixed point, which is equal to $\valsigma$ and which can be computed in polynomial time.

````

````{admonition} Proof
:class: dropdown tip

The operator $\discOP_{\sigma}$ can be seen as an instantiation of $\discOP$ in an MDP where there is no choice, since the action probabilities are chosen according to $\sigma$.  {prf:ref}`5-lem:fixpoint` shows that 
$\vec{x}^\sigma$ is a fixed-point of $\discOP^\sigma$. Since $\discOP_{\sigma}$ is again a contraction, it has a unique fixed point; and since it is linear, the fixed point can be computed in polynomial time, e.g. by Gaussian elimination (in its polynomial bit-complexity variant known as Bareiss algorithm {cite}`Bareiss:1968`).

````


%Note that for any $\vec{x}\in\R^{\vertices}$ and any $v\in \vertices$ there is 

We now prove that there is a memoryless strategy ensuring outcome given by the fixed point of $\discOP$. Hence, the fixed point gives a lower bound on the values of vertices.

````{prf:lemma} NEEDS TITLE 5-lem:disc-val-lower
:label: 5-lem:disc-val-lower

Let $\vec{x}^*$ be the unique fixed point of $\discOP$. 
Then there exists an MD strategy that is $\vec{x}^*$-safe. Moreover, for each $\vec{x}^*$-safe memoryless strategy it holds that  
$\playPay(v,\sigma) =\vec{x}_v^*$ for each $v\in \vertices$.

````

````{admonition} Proof
:class: dropdown tip

 Note that for each $\vec{x}\in \R^{\vertices}$ and each $v\in 
\vertices$ there always exists at least one action that is $\vec{x}$-safe in 
$v$. Hence, there is a memoryless deterministic strategy which 
in each $v$ chooses an arbitrary (but fixed) action that is $\vec{x}^*$-safe in 
$v$. 

Now let $ \sigma $ be an arbitrary $\vec{x}^*$-safe memoryless strategy.
By  {prf:ref}`5-lem:disc-val-sigma`, the vector $\valsigma$ is the unique fixed point of $\discOP^\sigma$.
 But since $\sigma$ 
is $\vec{x}^*$-safe, $\vec{x^*}$ is also a fixed point of $\discOP^\sigma$. 
Hence, $\vec{x}^* = \vec{x}^\sigma$.

````

It remains to prove that $\vec{x}^*$ gives, for each vertex, an upper 
bound on the expected discounted payoff achievable by any strategy from that 
vertex. We introduce some additional notation to be used in the proof of the 
next lemma, as well as in some later results: namely, we denote by 
$\dPayoffStep{k}(\play)$ the 
discounted 
payoff accumulated during the first $k$ steps of $\play$, i.e. the number 
$(1-\lambda)\sum_{i=0}^{k-1} \lambda^i
\, \colouring(\play_i)$. The following lemma can be proved by an easy induction.

````{prf:lemma} NEEDS TITLE 5-lem:disc-iterates
:label: 5-lem:disc-iterates

For each $k\geq 0$ and each vertex $v$ we have 

$$
\sup_{\sigma}\expv^{\sigma}_{v}[\dPayoffStep{k}] = 
(\discOP^k(\vec{0}))_v
$$
 
(here $\vec{0}$ is a $|\vertices|$-dimensional vector of zeroes).

````

The previous lemma is used to prove the required upper bound on $\Value(v)$.

````{prf:lemma} NEEDS TITLE 5-lem:disc-val-upper
:label: 5-lem:disc-val-upper

For each vertex $v$ it holds 
$\Value(v)\leq \vec{x}^*_v$, where $\vec{x}^*$ is the 
unique fixed point of $\discOP$.

````

````{admonition} Proof
:class: dropdown tip

%for each $k\geq 0$ and each vertex $v$ we have 

%(\discOP^k(\vec{0}))_v
$$
 

%
We have $\DiscountedPayoff(\play) = \lim_{k\rightarrow 
\infty}\dPayoffStep{k}(\play)$ (for each $\play$) and hence, by 
dominated 
convergence theorem we have $\expv^\sigma_v[\DiscountedPayoff] = 
\lim_{k\rightarrow 
\infty}\expv^\sigma_v[\dPayoffStep{k}]$. 

Hence,

\begin{align}
\Value(v) &= \sup_{\sigma}\expv^\sigma_v[\DiscountedPayoff] \nonumber\\

%\infty}\DiscountedPayoff^k]\nonumber \\
&= \sup_{\sigma}\lim_{k\rightarrow \infty}\expv^\sigma_v[\dPayoffStep{k}] 
\label{5-eq:disc-limit-transition}.

%=\big(\sup_{k\geq 1} \reachOP^k(\vec{0})\big)_v = \big(\lim_{k\rightarrow 

\end{align}


It remains to prove that the RHS of~\eqref{5-eq:disc-limit-transition} is not 
greater than $\vec{x}^*= \lim_{k\rightarrow 
\infty}\discOP^k(\vec{0})=\lim_{k\rightarrow \infty} 
\sup_{\sigma}\expv^\sigma_v[\dPayoffStep{k}]$ (the last inequality follows 
by {prf:ref}`5-lem:disc-iterates`). It suffices to 
show that for each $\sigma'$ we have $\lim_{k\rightarrow 
\infty}\expv^{\sigma'}_v\dPayoffStep{k}] \leq \lim_{k\rightarrow 
\infty}\sup_{\sigma}\expv^\sigma_v[\dPayoffStep{k}]$. But this immediately 
follows from the fact that the inequality holds for each concrete $k$.

````

The following theorem summarizes the results.

````{prf:theorem} NEEDS TITLE 5-thm:disc-val-char-mem
:label: 5-thm:disc-val-char-mem

The vector of values $\Value(\mdp)$ in a discounted sum MDP $\mdp$ is the 
unique fixed point $\vec{x}^*$ of the operator $\discOP$. Moreover, there 
exists a 
memoryless deterministic strategy that is optimal in every vertex.

````

````{admonition} Proof
:class: dropdown tip

The characterization of $\Value(\mdp)$ follows directly from 
Lemmas~\ref{5-lem:disc-val-lower} and~\ref{5-lem:disc-val-upper}. The MD 
optimality follows from {prf:ref}`5-lem:disc-val-lower`.

````

In the rest of this section we discuss several algorithms for computing the 
values and optimal strategies in discounted-payoff MDPs.

## Value iteration

The value iteration algorithm works in the same way as in the case of 
discounted-payoff games: we simply iterate the operator $\discOP$ on the 
initial argument $\vec{0}$. We know that $\Value(\mdp)=\lim_{k\rightarrow 
\infty}\discOP^k(\vec{0})$, and hence, iterating $\discOP$ yields an 
approximation of $\Value(\mdp)$. The iteration might not reached the fixed 
point (i.e. $\Value(\mdp)$) in a finite number of steps, but we can provide 
simple bounds on the precision of the approximation.

````{prf:lemma} NEEDS TITLE 5-lem:disc-val-it-convergence
:label: 5-lem:disc-val-it-convergence

For each $k\in \N$, $||\Value(\mdp)-\discOP^k(\vec{0}) ||_{\infty} \leq 
\lambda^k \cdot \maxc$. (Recall that $\maxc=\max_{e\in 
\edges}|\colouring(e)|$).

````

````{admonition} Proof
:class: dropdown tip

This follows immediately from {prf:ref}`5-lem:disc-iterates` and from the fact that 
for each play $\play$, $\sum_{i=k}^{\infty}\lambda^i\cdot 
\colouring(\play_i)\leq \frac{1}{1-\lambda}\cdot\lambda^k \cdot \maxc$.

````

Similar analysis can be applied to strategies induced by the approximate 
vectors.

````{prf:lemma} NEEDS TITLE 5-lem:disc-val-it-eps-strategies
:label: 5-lem:disc-val-it-eps-strategies

Let $\eps>0$ be arbitrary and let 

$$
k(\eps)=\left\lceil\frac{\log_2\left(\frac{\eps(1-\lambda)}{4\maxc}\right)}{\log_2(\lambda)}
 \right\rceil .
$$
 Then, every 
$\discOP^{k(\eps)}(\vec{0})$-safe memoryless strategy is $\eps$-optimal in 
every vertex.

````

````{admonition} Proof
:class: dropdown tip

Let $\sigma$ be any $\discOP^{k(\eps)}(\vec{0})$-safe memoryless strategy and 
let $\discOP_{\sigma}$ be the corresponding operator. We have that
\begin{align}
||\Value(\mdp) - \valsigma ||_{\infty} &= ||\Value(\mdp) 
-\discOP^{k(\eps)}(\vec{0}) +\discOP^{k(\eps)}(\vec{0}) - \valsigma 
||_{\infty} \nonumber
\\
&\leq ||\Value(\mdp) -\discOP^{k(\eps)}(\vec{0}) 
||_{\infty} + || \discOP^{k(\eps)}(\vec{0}) - \valsigma
||_{\infty}. \label{5-eq:disc-val-it-bound}
\end{align}

The first term in~\eqref{5-eq:disc-val-it-bound} is $\leq \eps/2$ 
by the choice of $k(\eps)$ and {prf:ref}`5-lem:disc-val-it-convergence`. We prove 
that the second term 
in~\eqref{5-eq:disc-val-it-bound} is also bounded by $\eps/2$. Note that we 
have $\valsigma=\discOP_{\sigma}(\valsigma)$ (as was already proved 
in~ {prf:ref}`5-lem:disc-val-lower`) and $\discOP(\discOP^{k(\eps)}(\vec{0})) = 
\discOP_\sigma(\discOP^{k(\eps)}(\vec{0}))$ (since $\sigma$ is 
$\discOP^{k(\eps)}(\vec{0})$-safe). Using this we get
\begin{align*}
|| \discOP^{k(\eps)}(\vec{0}) - \valsigma
||_{\infty} & = || \discOP^{k(\eps)}(\vec{0}) -\discOP^{k(\eps)+1}(\vec{0}) + 
\discOP^{k(\eps)+1}(\vec{0}) - \valsigma
||_{\infty}\\
&\leq || \discOP^{k(\eps)}(\vec{0}) -\discOP^{k(\eps)+1}(\vec{0}) ||_{\infty} + 
||\discOP^{k(\eps)+1}(\vec{0}) - \valsigma
||_{\infty}
\\
&=|| \discOP^{k(\eps)}(\vec{0}) -\discOP^{k(\eps)+1}(\vec{0}) ||_{\infty} + 
||\discOP_\sigma(\discOP^{k(\eps)}(\vec{0})) - 
\discOP_\sigma(\valsigma)||_{\infty}\\

%|| \discOP^{k(\eps)}(\vec{0}) -\discOP^{k(\eps)+1}(\vec{0}) ||_{\infty} + 

%\discOP_\sigma(\valsigma)||_{\infty}\\
&\leq || \discOP^{k(\eps)}(\vec{0}) -\discOP^{k(\eps)+1}(\vec{0}) ||_{\infty} + 
\lambda\cdot||(\discOP^{k(\eps)}(\vec{0})) - 
\valsigma||_{\infty}
\end{align*}


Re-arranging yields $|| \discOP^{k(\eps)}(\vec{0}) - \valsigma
||_{\infty} \leq \frac{1}{1-\lambda}\cdot|| 
\discOP^{k(\eps)}(\vec{0}) - 
\discOP^{k(\eps)+1}
||_{\infty} $.
It follows from {prf:ref}`5-lem:disc-val-it-convergence`  that 
$||\discOP^{k(\eps)}(\vec{0}) -\discOP^{k(\eps)+1}(\vec{0}) ||_{\infty} 
\leq 2\cdot\lambda^{k(\eps)}\cdot \max|\colouring|\leq 
\frac{(1-\lambda)\eps}{2}$, the last 
inequality holding by the choice of $k(\eps)$. Plugging this into the 
formula above yields $|| \discOP^{k(\eps)}(\vec{0}) - \valsigma
||_{\infty} \leq\frac{\eps}{2}$, as required. 

````




%$\eps$-optimal strategy can be computed in time polynomial in the size of the 

Using a value-gap result 
(similar to the game case, but proved using a different technique), one can 
show that sufficiently precise iterates can be used to computate an **optimal** strategy. 
This is summarized in the following lemma due to {cite}`Tseng:1990`.

````{prf:lemma} NEEDS TITLE 5-lem:disc-vi-optimal-strategy
:label: 5-lem:disc-vi-optimal-strategy

Let $d$ be the least common multiple of denominators of the following numbers: $\lambda$, all   
transition probabilities, and all edge colourings in $\mdp$. Next, let $\eps^* = 
\frac{1}{d^{(3|\vertices|+3)}\cdot |\vertices|^{\frac{\vertices}{2}}}$.
Then, any $\discOP^{k(\eps^*)}(\vec{0})$-safe memoryless deterministic strategy 
is 
optimal in every 
vertex.

````

````{admonition} Proof
:class: dropdown tip

%By {prf:ref}`5-lem:disc-val-it-eps-strategies`, $\sigma$ is $\eps^*$-optimal. 

%optimal.
 Let $\sigma^*$ be any MD optimal strategy (it is guaranteed 
to exist by {prf:ref}`5-thm:disc-val-char-mem`). By the same theorem, we have that 
$\Value(\mdp)=\discOP^{\sigma}(\Value(\mdp))$. By the definition of 
$\discOP^{\sigma}$, we can write the above equation as $\Value(\mdp)= 
(1-\lambda)\cdot \vec{c}+\lambda \cdot P\cdot \Value(\mdp)$, where $\vec{c}$ is 
a vector whose each 
component 
is a 
sum of several terms, each term being a product of an edge colour and of a 
transition probability; and $P$ is a matrix containing 
transition 
probabilities. Multiplying the equation by $d^3$ yields $d^3\Value(\mdp)= 
d^3(1-\lambda)\cdot \vec{c}+d^3\lambda \cdot P\cdot \Value(\mdp)$. Since this equation has a unique fixed point (due to 
$\discOP^\sigma$ being a contraction), the matrix $A = d^3(I - \lambda P)$ (where $ I $ is the unit matrix) is 
regular, and moreover, composed of integers (ue to the choice of $ d $). By Cramer's rule, each entry of $\Value(\mdp)$ is equal to 
$\det(B)/\det(A)$, where $B$ is a matrix obtained by replacing some column of 
$A$ with $d^3(1-\lambda)\vec{c}$ (which is again an integer vector, due to the multiplication by $ d^3 $). Hence, each entry of $\Value(\mdp)$ is a rational number with denominator $\det(A)$. Hadamard's inequality {cite}`Garling:07` implies $|\det(A)|\leq d^{3|\vertices|}{|\vertices|}^{\frac{|\vertices|}{2}}$.

Now let $\sigma$ be any $\discOP^{k(\eps^*)}(\vec{0})$-safe MD strategy. By {prf:ref}`5-lem:disc-val-it-eps-strategies`, $\sigma$ is $\eps^*$-optimal. We prove that all actions used by $\sigma$ are $\vec{x}^*$-safe, which means that $\sigma$ is optimal by {prf:ref}`5-lem:disc-val-lower`. Assume that in some vertex $v$ the strategy $\sigma$ uses action $a$ that is not $\vec{x}^*$-safe. Denote $\vec{y}=\discOP_\sigma(\vec{x}^*)$. We have $ |\vec{y}_v - \vec{x}^*_v| > 0 $, since otherwise $a$ would be $\vec{x}^*$-safe. But then we can obtain a lower bound on the difference by investigating the bitsize of the numbers involved:
\begin{align*}
|\vec{y}_v - \vec{x}^*_v| &= \left|\frac{d^3}{d^3}\vec{y}_v - \frac{d^3}{d^3}\vec{x}^*_v\right|
\\
&=\frac{1}{d^3}\left|\sum_{u \in \vertices} 
\underbrace{d\cdot\probTranFunc(u \mid v,a)}_{\text{integer}} \cdot( \underbrace{d^2(1-\lambda)\cdot \colouring(u,v)}_{\text{integer}} + 
\underbrace{d^2\cdot\lambda \cdot \vec{x}^*_u ) - d^3\vec{x}^*}_{\text{int. multiples of $1/\det(A)$}}\right| \\
&\geq \frac{1}{d^3\cdot \det(A)}\geq \frac{1}{d^{(3|\vertices|+3)}\cdot{|\vertices|}^{\frac{|\vertices|}{2}}}.
\end{align*}



Now put $\vec{z}=\discOP_\sigma(\discOP^{k(\eps)}(\vec{0}))$. We have the following (using, on the first line, the fact that $|a+b| \geq |a|-|b|$):

%|\vec{z}_v - \vec{x}^*_v| &= |\sum_{u \in \vertices} 

%\lambda \cdot \discOP^{k(\eps)}(\vec{0})_u) - \vec{x}^*_v| && \\

%& = |\sum_{u \in \vertices} 

%\lambda \cdot (\discOP^{k(\eps)}(\vec{0})_u \underbrace{-\vec{x}^*_u)   +\discOP_\sigma(\vec{x}^*)}_{\parbox{2.5cm}{\scriptsize\text{introduce  $-\discOP_\sigma(\vec{x}^*)_v+\discOP_\sigma(\vec{x}^*)_v$}} }-\vec{x}^*_v | && \\

%\probTranFunc(u | v,a) \cdot( (1-\lambda)\cdot \colouring(u,v) + 

%&\geq \frac{1}{d^{3|\vertices|+3}\cdot |\vertices|^{|\vertices|}} - 

%\end{align*}
\begin{align*}
|\vec{z}_v - \vec{x}^*_v| &=
 |\vec{z}_v-\discOP_\sigma(\vec{x}^*)_v+\discOP_\sigma(\vec{x}^*)_v-\vec{x}^*_v | 
\geq |\discOP_\sigma(\vec{x}^*)_v-\vec{x}^*_v | - |\vec{z}_v-\discOP_\sigma(\vec{x}^*)_v |  \\
&\geq \frac{1}{d^{(3|\vertices|+3)}\cdot |\vertices|^{\frac{|\vertices|}{2}}} - |\discOP_\sigma(\discOP^{k(\eps)}(\vec{0}))_v-\discOP_\sigma(\vec{x}^*)_v |\quad (\text{as shown above})\\
&\geq \frac{1}{d^{(3|\vertices|+3)}\cdot |\vertices|^{\frac{|\vertices|}{2}}} - |\discOP_{\sigma}(\discOP^{k(\eps^*)}(\vec{0}) - \vec{x}^*)_v|  \quad (\text{since $\discOP_{\sigma}$ is linear})\\
&\geq \eps^* - \lambda\cdot||\discOP^{k(\eps^*)}(\vec{0}) - \vec{x}^* ||_{\infty}
> \eps^* - \frac{\eps^*}{2}  \quad (\text{ {prf:ref}`5-lem:disc-val-it-convergence`})\\&=\frac{\eps^*}{2}.

%

\end{align*}


In particular, it must hold that $\vec{z}_v< \vec{x}^*_v$. Otherwise we would have $\discOP^{k(\eps^*)+1}(\vec{0})_v \geq \discOP_{\sigma}(\discOP^{k(\eps^*)}(\vec{0}))_v \geq \vec{x^*}_v + \frac{\eps^*}{2} $, a contradiction with $\discOP^{k(\eps^*)+1}(\vec{0})$ being an $\frac{\eps^*}{4}$-ap\-prox\-imation of $\vec{x}^*$ (by  {prf:ref}`5-lem:disc-val-it-convergence` and the choice of $k(\eps^*)$).

At the same time, $|\discOP(\discOP^{k(\eps^*)}(\vec{0}))_v - \vec{x}^*|\leq \frac{\eps^*}{4}$, due to the choice of $k(\eps^*)$. Since $\vec{z}_v \leq \vec{x}_v^*$, we get $\vec{z}_v < \vec{x}_v^* - \frac{\eps}{2} \leq \discOP(\discOP^{k(\eps^*)}(\vec{0}))_v$, a contradiction with $\sigma$ being $\discOP^{k(\eps^*)}(\vec{0})$-safe. 

````



````{prf:corollary} NEEDS TITLE 5-cor:VI-optimal-strategy-comp
:label: 5-cor:VI-optimal-strategy-comp

An optimal MD strategy in discounted-payoff MDPs with a fixed discount factor can be computed in polynomial time. 

````

````{admonition} Proof
:class: dropdown tip

The number $1/\eps^*$, where $\eps^*$ is from  {prf:ref}`5-lem:disc-vi-optimal-strategy`, has bitsize polynomial in the size of the MDP when the discount factor is fixed. Hence, the number $k(\eps^*)$ defined as in  {prf:ref}`5-lem:disc-val-it-eps-strategies` has a polynomial magnitude, so it suffices to perform only polynomially many iterations. Since each iteration requires polynomially many arithmetic operations that involve only summation and multiplication by a constant, the result follows.

````


## Strategy improvement, linear programming, and (strongly) 
polynomial time

The strategy (or policy) improvement (also called strategy/policy iteration in the literature) for MDPs works similarly as for games, see {numref}`5-algo:disc-strategy-improvement`. In the algorithm, we use $\discOP_{a,v}(\vec{x})$ as a shortcut for $ \sum_{u \in \vertices}\probTranFunc(u\mid v,a)\left((1-\lambda)\cdot\colouring(v,u) + \lambda\cdot \vec{x}_u \right)$

%\item Let $\sigma_0$ be any MD strategy. Put $i=0$.

%\item For each vertex $v$, check if there is an **improving** action $a$, i.e. an action  such that $\sum_{u \in \vertices}\probTranFunc(u\mid v,a)\left((1-\lambda)\cdot\colouring(v,u) + \lambda\cdot \vec{x}_u \right) > \vec{x}^{\sigma_i}_v. $ If yes, then let $a_v$ be any action such that $a_v = \underset{a' \in \actions}{\arg\max} \sum_{u\in \vertices} 

%v,a') 

%\item If no state admitted an improving action, return $\sigma_{i}$ as the optimal strategy. Otherwise, let $\sigma_{i+1}$ be the strategy such that $\sigma_{i+1}(v)=a_v$ for each $v\in V$; then put $i:=i+1$ and go to (2.).

\begin{algorithm}
\KwData{A discounted-payoff MDP $ \mdp $}

%\SetKwProg{Fn}{Function}{:}{}

$i \leftarrow 0$\;
$ \sigma_i \leftarrow \text{arbitrary MD strategy} $\;
\Repeat{$ \sigma_{i} = \sigma_{i-1} $}{
compute $ \vec{x}^{\sigma_i} = \left(\expv^{\sigma_i}_v[\DiscountedPayoff]\right)_{v\in \vertices} $ \tcp*{Using  {prf:ref}`5-lem:disc-val-sigma`}
\ForEach{$ v \in \vertices $}{
$ \mathit{Improve}(v) \leftarrow \sigma_{i}(v) $\;
\ForEach{$ a \in \actions $}{
\lIf{$\discOP_{a,v}(\vec{x}^{\sigma_i}) >\discOP_{a,\mathit{Improve}(v)}(\vec{x}^{\sigma_i})$}{
$\mathit{Improve}(v) \leftarrow a$
}
}
$\sigma_{i+1}(v) \leftarrow \mathit{Improve}(v)$
}
$ i \leftarrow i+1 $
}
\Return{$ \sigma_i $}

%$Y \leftarrow \winPos(\mdp_X,\Reach(\genColour))$ \tcp*{Computed by {numref}`5-algo:reach-pos`}

%$Y' \leftarrow Y$\;

%}

%}

\caption{An algorithm computing an optimal MD strategy in a discounted MDP}
\label{5-algo:disc-strategy-improvement}
\end{algorithm}

````{prf:theorem} NEEDS TITLE 5-thm:disc-strat-it
:label: 5-thm:disc-strat-it

The strategy improvement algorithm for discounted MDPs terminates in a finite (and at most exponential) number of steps and returns an optimal MD strategy.

````

````{admonition} Proof
:class: dropdown tip

First we need to show that whenever $\sigma_{i+1}\neq \sigma_i$, then  $\vec{x}^{\sigma_{i+1}} \geq \vec{x}^{\sigma_i}$ and $\vec{x}^{\sigma_{i+1}} \neq \vec{x}^{\sigma_i}$ (we write this by $\vec{x}^{\sigma_{i+1}} \succ\vec{x}^{\sigma_i}$). So fix some $ i $ s.t. an improvement is performed in the $ i $-th iteration of the repeat-loop. We have $\discOP_{\sigma_{i+1}}(\vec{x}^{\sigma_i})\succ\discOP_{\sigma_{i}}(\vec{x}^{\sigma_i})= \vec{x}^{\sigma_i}$, i.e. $\discOP_{\sigma_{i+1}}(\vec{x}^{\sigma_i})-\vec{x}^{\sigma_i} \succ 0$. Let $P$, $\vec{c}$ be the matrix and vector such that the equation $\vec{x}=\discOP_{\sigma_{i+1}}(\vec{x})$ can be written as $\vec{x}= (1-\lambda)\cdot \vec{c}+\lambda \cdot P\cdot\vec{x}$. Since the equation $\vec{x}=\discOP_{\sigma_{i+1}}(\vec{x})$ has a unique fixed point (as $ \discOP_{\sigma_{i+1}} $ is a contraction), the matrix $ I-\lambda P $ is invertible. Then $\discOP_{\sigma_{i+1}}(\vec{x}^{\sigma_i})-\vec{x}^{\sigma_i} \succ 0$ can be written as  $(1-\lambda)\vec{c} + (\lambda P - I)\vec{x}^{\sigma_i} \succ 0 $, or equivalently $\vec{x}^{\sigma_i}\prec (1-\lambda)\vec{c}\cdot(I-\lambda P)^{-1}.$ But the RHS of this inequality is equal to the fixed point of $\discOP_{\sigma_{i+1}}$, i.e. to $\vec{x}^{\sigma_{i+1}} .$

Now there are only finitely (exponentially) many MD strategies and since$\vec{x}^{\sigma_{i+1}} \succ\vec{x}^{\sigma_i}$, we have that no strategy is considered twice. Hence, the algorithm eventually terminates. Upon termination, there is no improving action, so the algorithm has found a strategy $\sigma$ whose value vector $\valsigma$ is the fixed point of $\discOP$. Such a strategy is optimal by  {prf:ref}`5-thm:disc-val-char-mem`. 

````


While each of the steps (1.)--(4.) can be performed in polynomial time, the 
worst-case number of iterations is exponential {cite}`Hollanders&Delvenne&Jungers:2012`. However, the 
algorithm has nice properties in the case when the discount factor is fixed, as we'll see below. It is also intimately connected to the linear programming approach.

We can indeed aim to directly solve 
the equation $\vec{x} = \discOP(\vec{x})$, thus obtaining the fixed point of 
$\discOP$, by using a suitable LP. While the operator $\discOP$ is not 
in itself linear, solving the equation can be encoded into a linear  program. 
The main idea can be described as follows: given some numbers $y,z$, the 
solution $\bar{x}$ to the equation $x=\max\{y,z\}$ is exactly the smallest 
solution to the set of inequalities $x\geq y$, $x\geq z$. Hence, to solve the 
equation  $\vec{x} = \discOP(\vec{x})$, we set up the following linear program 
$\lpdisc$:

\begin{figure}[h]
\begin{align*}
&\text{{minimize} $\sum_{v\in \vertices} x_v$, \textrm{ 
subject to }}&\\
&x_v \geq \sum_{u\in \vertices} \probTranFunc(u\mid 
v,a)\cdot\left((1-\lambda)\cdot \colouring(v,u) + \lambda\cdot x_u \right)
&
\text{for all $v\in \vertices$ and $a\in \actions$.}
% z_q & \geq 0 & \text{ for all } q\in Q
\end{align*}
\caption{The linear program $\lpdisc$ with variables $x_v$, $v\in \vertices$.}
\label{5-fig:disc-lp}
\end{figure}

````{prf:lemma} NEEDS TITLE 5-lem:disc-lp
:label: 5-lem:disc-lp

The linear program $\lpdisc$ has a unique optimal solution 
$\bar{\vec{x}}$ that satisfies $\bar{\vec{x}} = \Value(\mdp)$.

````

````{admonition} Proof
:class: dropdown tip

Let $\vec{x}^* = \Value(\mdp)$ be the unique fixed point of $\discOP$. Clearly 
setting $x_v = \vec{x}^*_v$ yields a feasible solution of $\lpdisc$. 
We show 
that $\vec{x}^*$ is actually an optimal solution, by proving that for each 
feasible solution $\vec{x}$ it holds $\vec{x} \geq \vec{x}^*$. (This also 
shows 
the uniqueness, since it says that an optimal solution is the infimum of the 
set of 
all feasible solutions.) First, note that for any feasible solution $\vec{x}$ 
it holds $\discOP(\vec{x})\leq \vec{x}$, by the construction of $\lpdisc$. 
Next, if $\vec{x}$ is a feasible solution, then $\discOP(\vec{x})$ is also a 
feasible solution; otherwise, there would be some $v$ and $a\in \actions$ 
such that 
\begin{align*}\discOP(\vec{x})_v &< \sum_{u\in \vertices} \probTranFunc(u\mid 
v,a)\cdot\left((1-\lambda)\cdot \colouring(v,u) + \lambda\cdot 
\discOP(\vec{x})_u \right) \\ &\leq \sum_{u\in \vertices} \probTranFunc(u\mid 
v,a)\cdot\left((1-\lambda)\cdot \colouring(v,u) + \lambda\cdot \vec{x}_u 
\right) \leq \discOP(\vec{x})_v.
\end{align*}
Here, the first inequality on the second line follows from 
$\discOP(\vec{x})\leq \vec{x}$, while the second inequality follows from the 
definition of $\discOP$. But $\discOP(\vec{x})_v < \discOP(\vec{x})_v$ is an 
obvious contradiction. So $\discOP(\vec{x})$ is indeed a feasible solution and 
by applying the argument above, we get $\discOP^2(\vec{x}) \leq 
\discOP(\vec{x})$. By a simple induction, $\discOP^{i+1}(\vec{x})\leq 
\discOP^{i}(\vec{x})\leq \vec{x}$ for each $i\geq 0.$ Hence, also $\vec{x}^* = 
\lim_{i\rightarrow \infty} \discOP^i(\vec{x}) \leq \vec{x}$ (the first equality 
comes from  {prf:ref}`5-lem:fixpoint`).

````

It is known that linear programming can be solved in polynomial time by 
interior-point techniques {cite}`Kha:1979,Karmarkar:1984`. Hence, we get the following.

````{prf:theorem} NEEDS TITLE 5-thm:disc-polytime-lp
:label: 5-thm:disc-polytime-lp

The following holds for discounted-payoff MDPs:

1.  The value of each vertex as well as an MD optimal 
strategy can be computed in polynomial time. 

2.  The problem whether the value of a given vertex $v$ is at least a given constant 
(say~1) is \P-complete (under logspace reductions). The hardness result holds 
even for a fixed discount factor.

````

````{admonition} Proof
:class: dropdown tip
(1.)
The first part comes directly from {prf:ref}`5-lem:disc-lp`. Once the optimal value 
vector $\Value(\mdp)$ is computed, we can choose any $\Value(\mdp)$-safe MD 
strategy as the optimal one 
( {prf:ref}`5-lem:disc-val-lower`).

(2.) Let $\lambda$ be the fixed discount factor. We show the lower 
bound, by extending the reduction 
from the CVP problem used for almost-sure reachability. First, we 
transform the input circuit into an MDP in the same way as in the reachability 
case, and we let $v$ be the vertex corresponding to a gate we wish to evaluate. 
Assume, for a while, that each path from $v$ to a target state has the same 
length $\ell$. Then we simply assign reward 
$\frac{1}{(1-\lambda)\cdot\lambda^{\ell -1}}$ to each edge 
entering a target state, and $0$ to all other edges. It is easy to check that 
the value of $v$ in the resulting discounted MDP is equal to the value of $v$ 
in the reachability MDP. If the reachability MDP $\mdp$ does not have the 
``uniform 
path length'' property, we modify it by producing $|\vertices|$ copies of 
itself so that each new vertex carries, apart from the original name, an index 
from $\{1,\dots,n\}$. The transition function in the new MDP mimics the 
original one, but from vertices with index $j<n$ we transition to the 
appropriate vertices of index $j+1$. The target vertices in the new MDP are 
those vertices of index $n$ that correspond to a target vertex of the 
original MDP (this does not break down the reduction, as target vertices in the original vertices can be assumed to have no outgoing edges other than self loops). This new MDP has the desired property and can be produced in a 
logarithmic space.

````

The previous theorem shows that discounted-payoff MDPs can be solved in 
polynomial time even if the discount factor is not fixed (i.e., it is taken as 
a part of the input). This is an important difference from the 2-player 
setting. However, the proof, resting on polynomial-time solvability of linear 
programming, leaves opened a question whether the discounted-payoff 
MDPs be solved in strongly polynomial time.  An answer was provided by Ye {cite}`Ye:2011`: already the classic simplex 
algorithm of Dantzig solves $\lpdisc$ in a strongly 
polynomial time in MDPs with a fixed discount factor. Formally, Ye proved that 
the number of iterations taken by the simplex method is bounded by 
$\frac{|\vertices|^2\cdot (|\actions|-1)}{1-\lambda}\cdot 
\log(\frac{|\vertices|^2}{1-\lambda})$, with each iteration requiring  
$\mathcal{O}(|\vertices|^2\cdot |\actions|)$ arithmetic operations. This has 
also an impact on the strategy improvement method: it can be shown that strategy 
improvement in discounted MDPs is really just a re-implementation of the 
simplex algorithm using a different syntax. Hence, the strongly polynomial 
complexity bound for a fixed discount factor holds there as well.

````{prf:theorem} NEEDS TITLE AND LABEL 
For MDPs with a fixed discount factor, the value of each vertex as well as an 
optimal MD strategy can be computed in a strongly polynomial time.
 

For MDPs with a fixed discount factor, the value of each vertex as well as an 
optimal MD strategy can be computed in a strongly polynomial time.

````

