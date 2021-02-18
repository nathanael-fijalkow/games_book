(5-sec:reachability)=
# Positive and almost-sure reachability and safety in MDPs

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

%objective: reachability. 

% computing optimal reachability values and strategies can be reduced to optimizing 

% opposed to the game case, where reachability games can be solved in polynomial 

% Hence, in this section 

% reachability problems. 
 
% see, actually \P-complete), they can be efficiently solved by specific 



> **Positive reachability**

  
Analogously to classical games (cf. Chapter {ref}`2-chap:regular`), we define a one-step **positive 
probability** predecessor 
operator, $\PrePos$,
as follows: for $U\subseteq \vertices$ we put

\begin{align*}
\PrePos(U) &= \{v \in \vertices \mid \exists a \in \actions, \exists u \in U: 
\probTranFunc(u\mid v,a)>0 \}.\\

%\vertices: \probTranFunc(t\mid v,a)>0 \Rightarrow t \in U \}.
\end{align*}

%\PrePos(Y)$ if $X\subseteq Y$, while $\PreAS$ is **antitone,** i.e.  


We also define an operator $\PreOPPos$ s.t. for each $X\subseteq\vertices$ we have

$$
\PreOPPos(X) = X\cup \PrePos(X).
$$

It is easy to see that $\PreOPPos$ is a classical 
reachability operator in the underlying graph of the MDP, i.e. denoting $X_0 = 
X$ and $X_i = \PreOPPos(X_{i-1})$, we get that $X_i$ is exactly the set of 
vertices from which a vertex of $X$ is reachable via a finite play of length at 
most $i$. It follows that iterating $\PreOPPos$ on any initial set reaches a 
fixed point in at most $n-1$ steps, where $n=|\vertices|$.

We have the following simple characterization of the positively winning set:

````{prf:theorem} Characterisation of the positively winning set
:label: 5-thm:positive-char

For each vertex $v$, the following conditions are equivalent:

1.  The vertex $v$ belongs to $\winPos(\mdp,\Reach(\genColour))$.

2.  There 
exists a (possibly empty) finite play from $v$ to a vertex of colour $\genColour$.

3.  The vertex $v$ 
belongs to the fixed point of the iteration $\vertices_\genColour, 
\PreOPPos(\vertices_\genColour),\PreOPPos^2(\vertices_\genColour),\cdots$.

Moreover, there exists a memoryless deterministic strategy that is positively 
winning from each vertex in $\winPos(\mdp,\Reach(\genColour))$.

````

````{admonition} Proof
:class: dropdown tip

$(1)\Rightarrow(2)$: We have that $\Reach(\genColour) = \cup_{\play \in X} 
\cylinder(\pi)$, where $X$ is the set of all finite plays ending in a vertex of 
colour $\genColour$ and $\cylinder(\pi)$ is the basic cylinder determined by 
$\pi$. Since $X$ is a countable set, from the property (3.) of a probability 
measure it follows that $\probm^\sigma_{\mdp,v}(\Reach(\genColour))>0$ if and 
only if there exists $\play\in X$ with 
$\probm^\sigma_{\mdp,v}(\cylinder(\play))>0$. For the latter to hold, it must 
be that either $\play=\emptyPlay$, in which case $\colours(v)=\genColour$, or 
$\play$ is a non-empty play initiated in $v$ and reaching a colour 
$\genColour$, as required.

```{margin}
Arguments of this style are said to invoke a union bound. 
```



$(2)\Rightarrow(3)$:
This is straightforward.

$(3)\Rightarrow (1)$:
For a vertex $v$, let $\rank(v)$ be the smallest $i$ such that $v \in 
\PreOPPos^i(\vertices_\genColour)$ (if no such $i$ exists, then 
$\rank(v)=\infty$). For each $v$ with a positive rank there exists an action 
$a_v$ and vertex $u_v$ such that $\probTranFunc(u_v\mid v,a_v)>0$ and 
$\rank(u_v)< \rank(v)$. Consider any MD strategy $  \sigma $ with the following property: 
in each vertex of 
$\winPos(\mdp,\Reach(\genColour))\setminus \vertices_{\genColour}$, $ \sigma $ selects the 
action $a_v$ defined above with probability 1. A straightforward induction on the rank shows that such a $ \sigma $ is positively winning from each vertex of 
$\winPos(\mdp,\Reach(\genColour))$. This also proves the last part 
of the lemma.

````


%\KwData{An MDP $ \mdp $}

%\SetKwProg{Fn}{Function}{:}{}

%$W \leftarrow \vertices_\genColour$ \;

%$W' \leftarrow W$\;

%}

%

%\Return{$W$}

%\label{5-algo:reach-pos}



As for complexity, we can focus on the problem of determining whether a given 
vertex belongs to $\winPos(\mdp,\Reach(\genColour))$. 

````{prf:corollary} Complexity of deciding positive reachability
:label: 5-cor:pos-complexity

The problem of deciding whether a given vertex of a given MDP belongs to 
$\winPos(\mdp,\Reach(\genColour))$ is \NL-complete. Moreover, the set $\winPos(\mdp,\Reach(\genColour))$ can be computed in linear time.

````

````{admonition} Proof
:class: dropdown tip

 {prf:ref}`5-thm:positive-char` 
gives a blueprint for a logspace reduction from this problem to the 
**s-t-connectivity** problem for directed graphs, and vice versa. The latter 
problem is well known to be \NL-complete {cite}`Savitch:1970`. Moreover, the set of states from which a target colour is reachable can be computed by a simple graph search (e.g. by BFS), hence in linear time.

````

%be straightforward, via the certificate definition of FNL. Read the paper 



%Memoryless deterministic strategies are sufficient for positive reachability 

%MD 

%$\winPos(\mdp,\Reach(\genColour))$, can be both computed in polynomial time.



> **Almost-sure reachability and safety**

 While the reachability and safety objectives are seemingly dual, in MDPs there is an intimate connection between them.

%

Let's start with almost-sure reachability. Consider the  **almost-sure predecessor operator $\PreAS$**, s.t. for each $U \subseteq \vertices$ we have 
$$
\PreAS(U) = \{v \in \vertices \mid \exists a \in \actions, \forall t \in 
\vertices: \probTranFunc(t\mid v,a)>0 \Rightarrow t \in U \}.
$$

%winning 

%\cup \PreAS(X)$, starting with the initial argument $\vertices_\genColour$. 

One might be tempted to mimic the positive reachability case and perform the iteration $ X \leftarrow X \cup \PreAS(X) $ on the set $ \vertices_{\genColour} $ until a fixed point is reached.
But this 
is not correct: consider an MDP with two vertices, $u,v$, the latter one being coloured by $\Win$. We have only one action $a$: in $v$, the action self loops on $v$, while in $u$ playing the action either switches moves us to $v$ or leaves us in $u$, both options having probability $\frac{1}{2}$. The probability that we **never** reach $v$ from $u$ is 
equal to $\lim_{n\rightarrow \infty} \left(\frac{1}{2}\right)^n = 0$, and hence 
$\winAS(\mdp,\Reach(\Win))=\{u,v\}$. However, $\{v\}\cup\PreAS(\{v\})=\{v\}$, so 
$v$ is not included into the outcome of the iteration. Note that there indeed exists an infinite play which **can** be generated by the strategy and 
which 
never visits $v$, but the probability of generating such a play is $0$. 

Instead, we make a detour via safety. Consider the one-step **almost-sure safety** operator $\safeOP$ acting on sets of vertices:

\begin{align*}
\safeOP(X)= X \cap \PreAS(X).
\end{align*}

This operator gives rise to a notion of a closed set, which is important for the study of safety objectives in MDPs.



````{prf:definition} Closed set in an MDP
:label: 5-def:closed_set_MDP

A set $X$ of vertices is closed if $ \safeOP(X)=X$. A sub-MDP of an MDP $ \mdp $ defined by a closed subset $X$ of $ \mdp $'s states is the MDP $\mdp_X = (X,\edges_X,\probTranFunc_X,\colouring_X)$ defined as follows:

*  $\edges_X$ is obtained from $\edges$ by removing edges incident to a vertex from $\vertices\setminus X$;
*  $\probTranFunc_X$ is obtained from $\probTranFunc\subseteq \vertices\times\actions\times\dist(\edges)$ by removing all triples $(v,a,f)$ where either $v\not \in X$ or where the support of $f$ is not contained in $X$;
*  $\colouring_X$ is a restriction of $\colouring$ to $X$.

We denote by $\closed(\mdp)$ the set of all closed sets in $\mdp.$

````

Intuitively, a set is closed if Eve has a strategy ensuring that she stays in the set forever.


Now consider the iteration of $ X, \safeOP(X),\safeOP^2(X),\ldots $ of the safety operator. Clearly $\safeOP(X)\subseteq X$. Hence, the iteration reaches a fixed point in at most $|\vertices|$ steps. We get the following:

````{prf:lemma} Inclusion of the least fixed of the safety operator
:label: 5-lem:safety-iteration

The fixed point of iterating $ \safeOP $ on some initial set $ X $ of $ \mdp $'s vertices is the largest (w.r.t. inclusion) closed set contained in $ X $. In particular, a vertex of $ X $ which does not belong to the fixpoint cannot belong to  $\winAS(\mdp,\Safe(\vertices \setminus X))$.

````

````{admonition} Proof
:class: dropdown tip

A straightforward induction on the number of iteration shows that if a vertex $ v $ is removed in an $ i $-th iteration, then no matter what strategy Eve uses, she has to reach $ \vertices\setminus X $ in at most $ i $ steps with a positive probability. The lemma follows.

````



%

%
%Now getting the almost-sure winning set for reachability entails repeated computation of positive winning sets on smaller and smaller sub-MDPs of $\mdp$.



%To get the almost-surely winning set, we define the operator $\OPAS(c,\cdot)\colon \closed(\mdp) \rightarrow \closed(\mdp)$, parametrized by a colour $\genColour$, whose computation is shown in {numref}`5-algo:reach-opas`. Note that the algorithm terminates 



%\item We set $Y=\winPos(\mdp_X,\Reach(\genColour))$.

%
%
%
%
%
%\end{itemize}



```{figure} ./../FigAndAlgos/5-algo:safety.png
:name: 5-algo:safety
:align: center
An algorithm computing $\winAS(\mdp,\Safe(\genColour))$
```


````{prf:theorem} Complexity of the almost-sure safety winning set
:label: 5-thm:safety-main

{numref}`5-algo:safety` computes the set $\winAS(\mdp,\Safe(\genColour))$ in strongly polynomial time. Moreover, there exists a memoryless deterministic strategy, computable in polynomial time, that is almost-surely winning from every vertex of $\winAS(\mdp,\Safe(\genColour))$.

````

````{admonition} Proof
:class: dropdown tip

The correctness follows immediately from  {prf:ref}`5-lem:safety-iteration`. The algorithm makes at most linearly many iterations, each of which has at most linear complexity. Hence, the complexity is at most quadratic. The strong polynomiality is testified by the fact that the algorithm only tests whether a 
probability of a given transition is positive or not, for which the exact 
values of positive probabilities are irrelevant. Clearly the output of the algorithm is a closed set, and hence for each $ v\in  \winAS(\mdp,\Safe(\genColour))$ there is an action $ a_v $ such that all edges in the support of $ \probTranFunc(v,a_v)  $ lead back to $ \winAS(\mdp,\Safe(\genColour)) $. Any MD strategy which in each $ v\in  \winAS(\mdp,\Safe(\genColour)) $ chooses $ a_v $ with probability 1 is a.s. winning inside $ \winAS(\mdp,\Safe(\genColour)) $, which proves the last part of the lemma.

````





```{figure} ./../FigAndAlgos/5-algo:reach-as.png
:name: 5-algo:reach-as
:align: center
An algorithm computing $\winAS(\mdp,\Reach(\genColour))$
```

With a.s. safety solved, we go back to a.s. reachability, which is solved via {numref}`5-algo:reach-as`. Note that in the first iteration, the algorithm computes the set 
$\winAS(\mdp,\Safe(Z))$ where $ Z =  \winPos(\mdp,\Reach(\genColour))$. We might be tempted to think that this set already equals $ \winAS(\mdp,\Reach(\genColour)) $, but this is not the case. To see this, consider an MDP with three states $ u,v,t $ and two actions $ a,b $ such that $ t $ is coloured by $ \Win $, both actions self loop in $ v $ and $ t $, and $ \probTranFunc(t \mid u,a) = \probTranFunc(v \mid u,a) = \frac{1}{2} $ while $ \probTranFunc(u \mid u,b) = 1 $. Then $ \winAS(\mdp,\Reach(\Win)) = \{t\} $ while at the same time $ \winAS(\mdp,\Safe( \winPos(\mdp,\Reach(\Win)))) = \{u,t\}$. However, iterating the computation works, as shown in the following theorem.

````{prf:theorem} Algorithm for the almost-sure reachability winning set
:label: 5-thm:as-char

{numref}`5-algo:reach-as` computes $\winAS(\mdp,\Reach(\genColour))$ in strongly polynomial time. Moreover, there is an MD strategy, computable in strongly polynomial time, that is almost-surely winning from every vertex of $\winAS(\mdp,\Reach(\genColour))$.

````

````{admonition} Proof
:class: dropdown tip

Since the set $ W $ can only decrease in each iteration, the algorithm terminates.
We prove that upon termination, $W$ equals $\winAS(\mdp,\Reach(\genColour))$.

We start with the $ \subseteq $ direction. We have $W \subseteq \winPos(\mdp_W,\Reach(\genColour))$. By  {prf:ref}`5-thm:positive-char` there exists an MD strategy $\sigma$ in $\mdp_W$ which is positively winning from each vertex of $W$. We show that the same strategy is also almost-surely winning from each vertex of $W$ in $\mdp_W$ and thus also from each vertex of $W$ in $\mdp$, which also proves the second part of the theorem. 

Let $v$ be any vertex of $W$ and denote $|W|$ by $\ell$. Since $\sigma$ is memoryless, it guarantees that a vertex of $\vertices_{\genColour}$ is reached with a positive probability in at most $\ell$ steps (see also the construction of $ \sigma $ in the proof of  {prf:ref}`5-thm:positive-char`), and since it is also deterministic, it guarantees that the probability $p$ of reaching $\vertices_{\genColour}$ in at most $\ell$ steps is at least $p_{\min}^{\ell}$, where  $p_{\min}$ is the smallest non-zero edge probability in $\mdp_W$. Now imagine that $\ell$ steps have elapsed and we have not yet reached $\vertices_{\genColour}$. This happens with a probability at most $(1-p_{\min}^\ell)$. However, even after these $\ell$ steps we are still in $W$, since $ \sigma  $ is a strategy in $ \mdp_w $. Hence, the probability that we do not reach $\vertices_\genColour$ within the first $2\ell$ steps is bounded by $(1-p_{\min}^\ell)^{2}$. To realize why this is the case, note that any finite play $\play$ of length $2\ell$ can be split into two halves, $\play',\play''$ of length $\ell$, and then $\probm^{\sigma}_{v}(\cylinder(\play))=\probm^{\sigma}_{v}(\cylinder(\play'))\cdot\probm^{\sigma}_{\last(\play')}(\cylinder(\play''))$ (here we use the fact that $\sigma$ is memoryless). Using this and some arithmetic, one can show that, denoting $\mathit{Avoid}_i$ the set of all plays that avoid the vertices of $\vertices_{\genColour}$ in steps $\ell\cdot(i-1)$ to $\ell\cdot(i)-1$, it holds 
$$
\probm^{\sigma}_{v}(\mathit{Avoid}_1\cap \mathit{Avoid}_2) \leq \probm^{\sigma}_{v}(\mathit{Avoid}_1)\cdot \max_{u\in W\setminus \vertices_{\genColour}}\probm^{\sigma}_{u}(\mathit{Avoid}_1)\leq (1-p_{\min}^\ell)^{2}.
$$



One can then continue by induction to show that $\probm^{\sigma}_{v}(\bigcap_{i=1}^j \mathit{Avoid}_i)\leq (1-p_{\min}^\ell)^{j},$ and hence

$$
\probm^\sigma_{v}(\Reach(\genColour))= 1-\probm^{\sigma}_{v}(\bigcap_{i=1}^\infty \mathit{Avoid}_i) \leq 1-\lim_{j\rightarrow \infty}(1-p_{\min}^\ell)^{j}= 1-0=1.
$$

Now we prove the $ \supseteq $ direction. Denote $X=\winAS(\mdp,\Reach(\genColour))$. We prove that $ W \supseteq X $ is an invariant of the iteration. Initially this is clear. Now assume that this holds before an iteration takes place. It is easy to check that $X$ is closed, so $\mdp_{X}$ is well-defined. We prove that $ X \subseteq \winAS(\mdp_W,\Safe(W\setminus Z)) $, where $ Z $ is defined during the iteration. A strategy in $\mdp$ that reaches $\vertices_{\genColour}$ with probability 1 must never visit a vertex from $\vertices\setminus X$ with a positive probability. Hence, each such strategy can be viewed also as a strategy in $\mdp_{X}$. It follows that  $X=\winAS(\mdp_X,\Reach(\genColour)) = \winPos(\mdp_{X},\Reach(\genColour)) \subseteq \winPos(\mdp_{W},\Reach(\genColour)) = Z$, the middle inclusion following from induction hypothesis. Now by  {prf:ref}`5-lem:safety-iteration` and  {prf:ref}`5-thm:safety-main`, the set $ \winAS(\mdp_W,\Safe(W\setminus Z)) $ is the largest closed set contained in $ Z $. But $ X $ is also closed, and ashown above, it is contained in $ Z $. Hence,  $ X \subseteq \winAS(\mdp_W,\Safe(W \setminus Z)) $.

The complexity follows form \Cref{5-cor:pos-complexity} and  {prf:ref}`5-thm:safety-main`; and also from the fact that the main loop must terminate in $ \leq |\vertices| $ steps. The strong polynomiality again follows from the algorithm being oblivious to precise probabilities.

````


%\begin{claim}

%If there is an MD strategy positively winning for $ \Reach(\genColour) $ in every vertex of the MDP, then the same strategy a.s. winning for $ \Reach(\genColour) $ from every vertex.



We also have a complementary hardness result. 

%following:

````{prf:theorem} Complexity of the almost-sure reachability winning set
:label: 5-thm:as-complexity

The problem of determining whether a given vertex of a given MDP belongs to 
$\winAS(\mdp,\Reach(\genColour))$ is \P-complete.

````

````{admonition} Proof
:class: dropdown tip

We procced by a reduction 
from the **circuit value problem (CVP)**.
An instance of **CVP** is a directed acyclic graph $\mathcal{C}$, 
representing a boolean circuit: each internal node represents either an OR gate 
or an AND gate, while each leaf node is labelled by **true** or 
**false**. Each internal node is guaranteed to have exactly two children. 
Each node of $\mathcal{C}$ evaluates to a unique truth value: the value of a 
leaf is given by its label and the value of an internal node $v$ is given by 
applying the logical operator corresponding to the node to the truth values of 
the two children of $v$, the evaluation proceeding in a backward topological order. The task is to decide whether a given node $w$ of 
$\mathcal{C}$ evaluates to **true**. **CVP** was shown to be 
\P-hard (under logspace reductions) in {cite}`Ladner:1975`. 
In {cite}`Chatterjee&Doyen&Henzinger:2010`, the following logspace reduction 
from CVP to 
almost-sure reachability in MDPs is presented: given a boolean circuit 
$\mathcal{C}$, construct an MDP $\mdp_{\mathcal{C}}$ whose vertices correspond 
to the gates 
of $\mathcal{C}$. There are two actions, call them $\mathit{left}$ and $\mathit{right}$. In each vertex corresponding to an OR gate $g$, the 
$\mathit{left}$ action transitions with probability 1 to the vertex 
representing the left child of $g$, and similarly for the action 
$\mathit{right}$ 
and the right child. In a vertex corresponding to an AND gate $g$, both actions behave the same: the transition into each of the two children 
of $g$ with probability $\frac{1}{2}$. Vertices corresponding to leafs have self loop as the only outgoing edges, and 
moreover, they are coloured with the respective labels in $\mathcal{C}$. It is 
easy to check that a gate of $\mathcal{C}$ evaluates to $\mathit{true}$ if and 
only if the corresponding vertex belongs to 
$\winAS(\mdp_{\mathcal{C}},\Reach(\mathit{true}))$.

````

> **Positive safety**

 We conclude this section by a discussion of positive safety. 



````{prf:theorem} Algorithm for the positive safety winning set
:label: 5-thm:pos-safety-main

Let $ \mdp_{\bar\genColour} $ be an MDP obtained from $ \mdp $ by changing all $ \genColour $-coloured vertices to sinks (i.e. all actions in these vertices just self loop on the vertex). Then
$ \winPos(\mdp,\Safe(\genColour)) = \winPos(\mdp_{\bar\genColour},\Reach(\winAS(\mdp_{\bar\genColour},\Safe(\genColour))) ) $. In particular, the set $ \winPos(\mdp,\Safe(\genColour)) $ can be computed in a strongly polynomial time and there exists a memoryless deterministic strategy, computable in strongly polynomial time, that is positively winning from every vertex of $\winPos(\mdp,\Safe(\genColour))$.

````

````{admonition} Proof
:class: dropdown tip

Clearly $ \winPos(\mdp,\Safe(\genColour)) = \winPos(\mdp_{\bar{\genColour}},\Safe(\genColour)) $ and $ \winAS(\mdp,\Safe(\genColour)) = \winAS(\mdp_{\bar{\genColour}},\Safe(\genColour)) $; and moreover the corresponding winning strategies easily transfer between the two MDPs (for a safety objective, the behaviour after visiting a $ \genColour $-coloured state is inconsequential).
Hence, putting $ Z = \winAS(\mdp_{\bar{\genColour}},\Safe(\genColour)) $, it is sufficient to show that  $ \winPos(\mdp_{\bar{\genColour}},\Safe(\genColour)) =\winPos(\mdp_{\bar\genColour},\Reach(Z))  $  

The $ \supseteq $  inclusion is clear as well as the construction of the witnessing MD strategy (in the vertices of that are outside of $ Z $, we behave as the positively winning MD strategy for reaching $ Z $, while inside $ Z $ we behave as the a.s. winning strategy for $ \Safe(\genColour) $). 

For the other inclusion, let $ X = \vertices \setminus \winPos(\mdp_{\bar{\genColour}},\Reach(Z)) $. We prove that $ X\subseteq \vertices \setminus \winPos(\mdp_{\bar{\genColour}},\Safe(\genColour)) $. Assign ranks to vertices inductively as follows: each vertex coloured by $ \genColour $ gets rank $ 0 $. Now if ranks $ \leq i $ have been already assigned, then a vertex  $ v $ is assigned rank $i+1  $ if it  does  not already have a lower rank but for all actions $ a\in\actions $ there exists a vertex $ u $ of rank $ \leq i $ s.t. $ \probTranFunc(u \mid v,a) >0$. Then each vertex in $ X $ is assigned a finite rank: indeed, the set of vertices without a rank is closed and does not contain $ \genColour $-coloured vertices, hence it is contained in $ Z $. 
Now fix any strategy $ \sigma $ starting in a vertex $v \in X $. By definition of $ X $, $ \sigma $ never reaches $ Z $ and hence never visits an unranked state. At the same time, whenever $ \sigma $ is in a ranked state, there is, by definition of ranks, a probability at least $p_{\min}  $ (the minimal edge probability in $ \mdp $) of transitioning to a lower-ranked state in the next step. Hence, in every moment, the probability of $ \sigma $ reaching a $ \genColour $-coloured state within the next $ |\vertices| $ steps is at least $ p_{\min}^{|\vertices|} $. By a straightforward adaptation of the second part of the proof of  {prf:ref}`5-thm:as-char`, $ \sigma $ eventually visits $ \vertices_{\genColour} $ with probability 1. Since $ \sigma $ was arbitrary, this shows that $ v\not \in\winPos(\mdp_{\bar{\genColour}},\Safe(\genColour)).  $

The complexity follows from the results on positive reachability and a.s. safety.

````


%studied in this chapter, and in particular, the almost-sure reachability 

%values in mean-payoff MDPs, for which we give a polynomial-time algorithm 

%establishing {prf:ref}`5-thm:as-complexity`. However, the algorithm we presented in 

%polynomial time}. 

%probability of a given transition is positive or not, for which the exact 

%

%\label{5-thm:qual-reach-sp}

%$\winAS(\mdp,\Reach(\genColour))$, as well as the corresponding winning 

%\end{theorem}
