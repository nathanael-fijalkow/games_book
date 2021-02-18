(5-sec:reachability)=
# Positive and almost-sure reachability and safety in MDPs


```{math}
\newcommand{\probm}{\mathbb{P}}
\newcommand{\actions}{A}
\newcommand{\colouring}{c}
\newcommand{\probTranFunc}{\Delta}
\newcommand{\edges}{E}
\newcommand{\colours}{C}
\newcommand{\mdp}{\mathcal{M}}
\newcommand{\emptyPlay}{\epsilon}
\newcommand{\genColour}{\textsc{c}}
\newcommand{\winPos}{W_{>0}}
\newcommand{\winAS}{W_{=1}}
\newcommand{\cylinder}{\mathit{Cyl}}
\newcommand{\PrePos}{\text{Pre}_{>0}}
\newcommand{\PreAS}{\text{Pre}_{=1}}
\newcommand{\PreOPPos}{\mathcal{P}_{>0}}
\newcommand{\OPAS}{\mathcal{P}_{=1}}
\newcommand{\safeOP}{\mathit{Safe_{=1}}}
\newcommand{\closed}{\mathit{Cl}}
\newcommand{\dist}{\mathcal{D}}
\newcommand{\vertices}{V}
\newcommand{\play}{\pi}
\newcommand{\last}{\textrm{last}}
\newcommand{\rank}{\textrm{rank}}
\newcommand{\Win}{\textrm{Win}}
\newcommand{\Safe}{\mathtt{Safe}}
\newcommand{\Reach}{\mathtt{Reach}}
\newcommand{\NL}{\textrm{NL}}
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
operator, $\text{Pre}_{>0},
as follows: for $U\subseteq V we put

\begin{align*}
\text{Pre}_{>0}U) &= \{v \in V\mid \exists a \in A \exists u \in U: 
\Deltau\mid v,a)>0 \}.\\

%V \Deltat\mid v,a)>0 \Rightarrow t \in U \}.
\end{align*}

%\text{Pre}_{>0}Y)$ if $X\subseteq Y$, while $\text{Pre}_{=1} is **antitone,** i.e.  


We also define an operator $\mathcal{P}_{>0} s.t. for each $X\subseteqV we have

$$
\mathcal{P}_{>0}X) = X\cup \text{Pre}_{>0}X).
$$

It is easy to see that $\mathcal{P}_{>0} is a classical 
reachability operator in the underlying graph of the MDP, i.e. denoting $X_0 = 
X$ and $X_i = \mathcal{P}_{>0}X_{i-1})$, we get that $X_i$ is exactly the set of 
vertices from which a vertex of $X$ is reachable via a finite play of length at 
most $i$. It follows that iterating $\mathcal{P}_{>0} on any initial set reaches a 
fixed point in at most $n-1$ steps, where $n=|V$.

We have the following simple characterization of the positively winning set:

````{prf:theorem} Characterisation of the positively winning set
:label: 5-thm:positive-char

For each vertex $v$, the following conditions are equivalent:

1.  The vertex $v$ belongs to $W_{>0}\mathcal{M}\mathtt{Reach}\textsc{c})$.

2.  There 
exists a (possibly empty) finite play from $v$ to a vertex of colour $\textsc{c}.

3.  The vertex $v$ 
belongs to the fixed point of the iteration $\vertices_\textsc{c} 
\mathcal{P}_{>0}\vertices_\textsc{c},\mathcal{P}_{>0}2(\vertices_\textsc{c},\cdots$.

Moreover, there exists a memoryless deterministic strategy that is positively 
winning from each vertex in $W_{>0}\mathcal{M}\mathtt{Reach}\textsc{c})$.

````

````{admonition} Proof
:class: dropdown tip

$(1)\Rightarrow(2)$: We have that $\mathtt{Reach}\textsc{c} = \cup_{\pi\in X} 
\mathit{Cyl}\pi)$, where $X$ is the set of all finite plays ending in a vertex of 
colour $\textsc{c} and $\mathit{Cyl}\pi)$ is the basic cylinder determined by 
$\pi$. Since $X$ is a countable set, from the property (3.) of a probability 
measure it follows that $\mathbb{P}\sigma_{\mathcal{M}v}(\mathtt{Reach}\textsc{c})>0$ if and 
only if there exists $\piin X$ with 
$\mathbb{P}\sigma_{\mathcal{M}v}(\mathit{Cyl}\pi)>0$. For the latter to hold, it must 
be that either $\pi\epsilon, in which case $Cv)=\textsc{c}, or 
$\pi is a non-empty play initiated in $v$ and reaching a colour 
$\textsc{c}, as required.

```{margin}
Arguments of this style are said to invoke a union bound. 
```



$(2)\Rightarrow(3)$:
This is straightforward.

$(3)\Rightarrow (1)$:
For a vertex $v$, let $\textrm{rank}v)$ be the smallest $i$ such that $v \in 
\mathcal{P}_{>0}i(\vertices_\textsc{c}$ (if no such $i$ exists, then 
$\textrm{rank}v)=\infty$). For each $v$ with a positive rank there exists an action 
$a_v$ and vertex $u_v$ such that $\Deltau_v\mid v,a_v)>0$ and 
$\textrm{rank}u_v)< \textrm{rank}v)$. Consider any MD strategy $  \sigma $ with the following property: 
in each vertex of 
$W_{>0}\mathcal{M}\mathtt{Reach}\textsc{c})\setminus \vertices_{\textsc{c}$, $ \sigma $ selects the 
action $a_v$ defined above with probability 1. A straightforward induction on the rank shows that such a $ \sigma $ is positively winning from each vertex of 
$W_{>0}\mathcal{M}\mathtt{Reach}\textsc{c})$. This also proves the last part 
of the lemma.

````


%\KwData{An MDP $ \mathcal{M}$}

%\SetKwProg{Fn}{Function}{:}{}

%$W \leftarrow \vertices_\textsc{c} \;

%$W' \leftarrow W$\;

%}

%

%\Return{$W$}

%\label{5-algo:reach-pos}



As for complexity, we can focus on the problem of determining whether a given 
vertex belongs to $W_{>0}\mathcal{M}\mathtt{Reach}\textsc{c})$. 

````{prf:corollary} Complexity of deciding positive reachability
:label: 5-cor:pos-complexity

The problem of deciding whether a given vertex of a given MDP belongs to 
$W_{>0}\mathcal{M}\mathtt{Reach}\textsc{c})$ is \textrm{NL}complete. Moreover, the set $W_{>0}\mathcal{M}\mathtt{Reach}\textsc{c})$ can be computed in linear time.

````

````{admonition} Proof
:class: dropdown tip

 {prf:ref}`5-thm:positive-char` 
gives a blueprint for a logspace reduction from this problem to the 
**s-t-connectivity** problem for directed graphs, and vice versa. The latter 
problem is well known to be \textrm{NL}complete {cite}`Savitch:1970`. Moreover, the set of states from which a target colour is reachable can be computed by a simple graph search (e.g. by BFS), hence in linear time.

````

%be straightforward, via the certificate definition of FNL. Read the paper 



%Memoryless deterministic strategies are sufficient for positive reachability 

%MD 

%$W_{>0}\mathcal{M}\mathtt{Reach}\textsc{c})$, can be both computed in polynomial time.



> **Almost-sure reachability and safety**

 While the reachability and safety objectives are seemingly dual, in MDPs there is an intimate connection between them.

%

Let's start with almost-sure reachability. Consider the  **almost-sure predecessor operator $\text{Pre}_{=1}**, s.t. for each $U \subseteq V we have 
$$
\text{Pre}_{=1}U) = \{v \in V\mid \exists a \in A \forall t \in 
V \Deltat\mid v,a)>0 \Rightarrow t \in U \}.
$$

%winning 

%\cup \text{Pre}_{=1}X)$, starting with the initial argument $\vertices_\textsc{c}. 

One might be tempted to mimic the positive reachability case and perform the iteration $ X \leftarrow X \cup \text{Pre}_{=1}X) $ on the set $ \vertices_{\textsc{c} $ until a fixed point is reached.
But this 
is not correct: consider an MDP with two vertices, $u,v$, the latter one being coloured by $\textrm{Win}. We have only one action $a$: in $v$, the action self loops on $v$, while in $u$ playing the action either switches moves us to $v$ or leaves us in $u$, both options having probability $\frac{1}{2}$. The probability that we **never** reach $v$ from $u$ is 
equal to $\lim_{n\rightarrow \infty} \left(\frac{1}{2}\right)^n = 0$, and hence 
$W_{=1}\mathcal{M}\mathtt{Reach}\textrm{Win})=\{u,v\}$. However, $\{v\}\cup\text{Pre}_{=1}\{v\})=\{v\}$, so 
$v$ is not included into the outcome of the iteration. Note that there indeed exists an infinite play which **can** be generated by the strategy and 
which 
never visits $v$, but the probability of generating such a play is $0$. 

Instead, we make a detour via safety. Consider the one-step **almost-sure safety** operator $\mathit{Safe_{=1}} acting on sets of vertices:

\begin{align*}
\mathit{Safe_{=1}}X)= X \cap \text{Pre}_{=1}X).
\end{align*}

This operator gives rise to a notion of a closed set, which is important for the study of safety objectives in MDPs.



````{prf:definition} Closed set in an MDP
:label: 5-def:closed_set_MDP

A set $X$ of vertices is closed if $ \mathit{Safe_{=1}}X)=X$. A sub-MDP of an MDP $ \mathcal{M}$ defined by a closed subset $X$ of $ \mathcal{M}$'s states is the MDP $\mdp_X = (X,\edges_X,\probTranFunc_X,\colouring_X)$ defined as follows:

*  $\edges_X$ is obtained from $E by removing edges incident to a vertex from $Vsetminus X$;
*  $\probTranFunc_X$ is obtained from $\Deltasubseteq VtimesAtimes\mathcal{D}E$ by removing all triples $(v,a,f)$ where either $v\not \in X$ or where the support of $f$ is not contained in $X$;
*  $\colouring_X$ is a restriction of $c to $X$.

We denote by $\mathit{Cl}\mathcal{M}$ the set of all closed sets in $\mathcal{M}$

````

Intuitively, a set is closed if Eve has a strategy ensuring that she stays in the set forever.


Now consider the iteration of $ X, \mathit{Safe_{=1}}X),\mathit{Safe_{=1}}2(X),\ldots $ of the safety operator. Clearly $\mathit{Safe_{=1}}X)\subseteq X$. Hence, the iteration reaches a fixed point in at most $|V$ steps. We get the following:

````{prf:lemma} Inclusion of the least fixed of the safety operator
:label: 5-lem:safety-iteration

The fixed point of iterating $ \mathit{Safe_{=1}}$ on some initial set $ X $ of $ \mathcal{M}$'s vertices is the largest (w.r.t. inclusion) closed set contained in $ X $. In particular, a vertex of $ X $ which does not belong to the fixpoint cannot belong to  $W_{=1}\mathcal{M}\mathtt{Safe}V\setminus X))$.

````

````{admonition} Proof
:class: dropdown tip

A straightforward induction on the number of iteration shows that if a vertex $ v $ is removed in an $ i $-th iteration, then no matter what strategy Eve uses, she has to reach $ Vsetminus X $ in at most $ i $ steps with a positive probability. The lemma follows.

````



%

%
%Now getting the almost-sure winning set for reachability entails repeated computation of positive winning sets on smaller and smaller sub-MDPs of $\mathcal{M}.



%To get the almost-surely winning set, we define the operator $\mathcal{P}_{=1}c,\cdot)\colon \mathit{Cl}\mathcal{M} \rightarrow \mathit{Cl}\mathcal{M}$, parametrized by a colour $\textsc{c}, whose computation is shown in {numref}`5-algo:reach-opas`. Note that the algorithm terminates 



%\item We set $Y=W_{>0}\mdp_X,\mathtt{Reach}\textsc{c})$.

%
%
%
%
%
%\end{itemize}



```{figure} ./../FigAndAlgos/5-algo:safety.png
:name: 5-algo:safety
:align: center
An algorithm computing $W_{=1}\mathcal{M}\mathtt{Safe}\textsc{c})$
```


````{prf:theorem} Complexity of the almost-sure safety winning set
:label: 5-thm:safety-main

{numref}`5-algo:safety` computes the set $W_{=1}\mathcal{M}\mathtt{Safe}\textsc{c})$ in strongly polynomial time. Moreover, there exists a memoryless deterministic strategy, computable in polynomial time, that is almost-surely winning from every vertex of $W_{=1}\mathcal{M}\mathtt{Safe}\textsc{c})$.

````

````{admonition} Proof
:class: dropdown tip

The correctness follows immediately from  {prf:ref}`5-lem:safety-iteration`. The algorithm makes at most linearly many iterations, each of which has at most linear complexity. Hence, the complexity is at most quadratic. The strong polynomiality is testified by the fact that the algorithm only tests whether a 
probability of a given transition is positive or not, for which the exact 
values of positive probabilities are irrelevant. Clearly the output of the algorithm is a closed set, and hence for each $ v\in  W_{=1}\mathcal{M}\mathtt{Safe}\textsc{c})$ there is an action $ a_v $ such that all edges in the support of $ \Deltav,a_v)  $ lead back to $ W_{=1}\mathcal{M}\mathtt{Safe}\textsc{c}) $. Any MD strategy which in each $ v\in  W_{=1}\mathcal{M}\mathtt{Safe}\textsc{c}) $ chooses $ a_v $ with probability 1 is a.s. winning inside $ W_{=1}\mathcal{M}\mathtt{Safe}\textsc{c}) $, which proves the last part of the lemma.

````





```{figure} ./../FigAndAlgos/5-algo:reach-as.png
:name: 5-algo:reach-as
:align: center
An algorithm computing $W_{=1}\mathcal{M}\mathtt{Reach}\textsc{c})$
```

With a.s. safety solved, we go back to a.s. reachability, which is solved via {numref}`5-algo:reach-as`. Note that in the first iteration, the algorithm computes the set 
$W_{=1}\mathcal{M}\mathtt{Safe}Z))$ where $ Z =  W_{>0}\mathcal{M}\mathtt{Reach}\textsc{c})$. We might be tempted to think that this set already equals $ W_{=1}\mathcal{M}\mathtt{Reach}\textsc{c}) $, but this is not the case. To see this, consider an MDP with three states $ u,v,t $ and two actions $ a,b $ such that $ t $ is coloured by $ \textrm{Win}$, both actions self loop in $ v $ and $ t $, and $ \Deltat \mid u,a) = \Deltav \mid u,a) = \frac{1}{2} $ while $ \Deltau \mid u,b) = 1 $. Then $ W_{=1}\mathcal{M}\mathtt{Reach}\textrm{Win}) = \{t\} $ while at the same time $ W_{=1}\mathcal{M}\mathtt{Safe} W_{>0}\mathcal{M}\mathtt{Reach}\textrm{Win}))) = \{u,t\}$. However, iterating the computation works, as shown in the following theorem.

````{prf:theorem} Algorithm for the almost-sure reachability winning set
:label: 5-thm:as-char

{numref}`5-algo:reach-as` computes $W_{=1}\mathcal{M}\mathtt{Reach}\textsc{c})$ in strongly polynomial time. Moreover, there is an MD strategy, computable in strongly polynomial time, that is almost-surely winning from every vertex of $W_{=1}\mathcal{M}\mathtt{Reach}\textsc{c})$.

````

````{admonition} Proof
:class: dropdown tip

Since the set $ W $ can only decrease in each iteration, the algorithm terminates.
We prove that upon termination, $W$ equals $W_{=1}\mathcal{M}\mathtt{Reach}\textsc{c})$.

We start with the $ \subseteq $ direction. We have $W \subseteq W_{>0}\mdp_W,\mathtt{Reach}\textsc{c})$. By  {prf:ref}`5-thm:positive-char` there exists an MD strategy $\sigma$ in $\mdp_W$ which is positively winning from each vertex of $W$. We show that the same strategy is also almost-surely winning from each vertex of $W$ in $\mdp_W$ and thus also from each vertex of $W$ in $\mathcal{M}, which also proves the second part of the theorem. 

Let $v$ be any vertex of $W$ and denote $|W|$ by $\ell$. Since $\sigma$ is memoryless, it guarantees that a vertex of $\vertices_{\textsc{c}$ is reached with a positive probability in at most $\ell$ steps (see also the construction of $ \sigma $ in the proof of  {prf:ref}`5-thm:positive-char`), and since it is also deterministic, it guarantees that the probability $p$ of reaching $\vertices_{\textsc{c}$ in at most $\ell$ steps is at least $p_{\min}^{\ell}$, where  $p_{\min}$ is the smallest non-zero edge probability in $\mdp_W$. Now imagine that $\ell$ steps have elapsed and we have not yet reached $\vertices_{\textsc{c}$. This happens with a probability at most $(1-p_{\min}^\ell)$. However, even after these $\ell$ steps we are still in $W$, since $ \sigma  $ is a strategy in $ \mdp_w $. Hence, the probability that we do not reach $\vertices_\textsc{c} within the first $2\ell$ steps is bounded by $(1-p_{\min}^\ell)^{2}$. To realize why this is the case, note that any finite play $\pi of length $2\ell$ can be split into two halves, $\pi,\pi'$ of length $\ell$, and then $\mathbb{P}{\sigma}_{v}(\mathit{Cyl}\pi)=\mathbb{P}{\sigma}_{v}(\mathit{Cyl}\pi))\cdot\mathbb{P}{\sigma}_{\textrm{last}\pi)}(\mathit{Cyl}\pi'))$ (here we use the fact that $\sigma$ is memoryless). Using this and some arithmetic, one can show that, denoting $\mathit{Avoid}_i$ the set of all plays that avoid the vertices of $\vertices_{\textsc{c}$ in steps $\ell\cdot(i-1)$ to $\ell\cdot(i)-1$, it holds 
$$
\mathbb{P}{\sigma}_{v}(\mathit{Avoid}_1\cap \mathit{Avoid}_2) \leq \mathbb{P}{\sigma}_{v}(\mathit{Avoid}_1)\cdot \max_{u\in W\setminus \vertices_{\textsc{c}}\mathbb{P}{\sigma}_{u}(\mathit{Avoid}_1)\leq (1-p_{\min}^\ell)^{2}.
$$



One can then continue by induction to show that $\mathbb{P}{\sigma}_{v}(\bigcap_{i=1}^j \mathit{Avoid}_i)\leq (1-p_{\min}^\ell)^{j},$ and hence

$$
\mathbb{P}\sigma_{v}(\mathtt{Reach}\textsc{c})= 1-\mathbb{P}{\sigma}_{v}(\bigcap_{i=1}^\infty \mathit{Avoid}_i) \leq 1-\lim_{j\rightarrow \infty}(1-p_{\min}^\ell)^{j}= 1-0=1.
$$

Now we prove the $ \supseteq $ direction. Denote $X=W_{=1}\mathcal{M}\mathtt{Reach}\textsc{c})$. We prove that $ W \supseteq X $ is an invariant of the iteration. Initially this is clear. Now assume that this holds before an iteration takes place. It is easy to check that $X$ is closed, so $\mdp_{X}$ is well-defined. We prove that $ X \subseteq W_{=1}\mdp_W,\mathtt{Safe}W\setminus Z)) $, where $ Z $ is defined during the iteration. A strategy in $\mathcal{M} that reaches $\vertices_{\textsc{c}$ with probability 1 must never visit a vertex from $Vsetminus X$ with a positive probability. Hence, each such strategy can be viewed also as a strategy in $\mdp_{X}$. It follows that  $X=W_{=1}\mdp_X,\mathtt{Reach}\textsc{c}) = W_{>0}\mdp_{X},\mathtt{Reach}\textsc{c}) \subseteq W_{>0}\mdp_{W},\mathtt{Reach}\textsc{c}) = Z$, the middle inclusion following from induction hypothesis. Now by  {prf:ref}`5-lem:safety-iteration` and  {prf:ref}`5-thm:safety-main`, the set $ W_{=1}\mdp_W,\mathtt{Safe}W\setminus Z)) $ is the largest closed set contained in $ Z $. But $ X $ is also closed, and ashown above, it is contained in $ Z $. Hence,  $ X \subseteq W_{=1}\mdp_W,\mathtt{Safe}W \setminus Z)) $.

The complexity follows form \Cref{5-cor:pos-complexity} and  {prf:ref}`5-thm:safety-main`; and also from the fact that the main loop must terminate in $ \leq |V $ steps. The strong polynomiality again follows from the algorithm being oblivious to precise probabilities.

````


%\begin{claim}

%If there is an MD strategy positively winning for $ \mathtt{Reach}\textsc{c} $ in every vertex of the MDP, then the same strategy a.s. winning for $ \mathtt{Reach}\textsc{c} $ from every vertex.



We also have a complementary hardness result. 

%following:

````{prf:theorem} Complexity of the almost-sure reachability winning set
:label: 5-thm:as-complexity

The problem of determining whether a given vertex of a given MDP belongs to 
$W_{=1}\mathcal{M}\mathtt{Reach}\textsc{c})$ is \P-complete.

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
$W_{=1}\mdp_{\mathcal{C}},\mathtt{Reach}\mathit{true}))$.

````

> **Positive safety**

 We conclude this section by a discussion of positive safety. 



````{prf:theorem} Algorithm for the positive safety winning set
:label: 5-thm:pos-safety-main

Let $ \mdp_{\bar\textsc{c} $ be an MDP obtained from $ \mathcal{M}$ by changing all $ \textsc{c}$-coloured vertices to sinks (i.e. all actions in these vertices just self loop on the vertex). Then
$ W_{>0}\mathcal{M}\mathtt{Safe}\textsc{c}) = W_{>0}\mdp_{\bar\textsc{c},\mathtt{Reach}W_{=1}\mdp_{\bar\textsc{c},\mathtt{Safe}\textsc{c})) ) $. In particular, the set $ W_{>0}\mathcal{M}\mathtt{Safe}\textsc{c}) $ can be computed in a strongly polynomial time and there exists a memoryless deterministic strategy, computable in strongly polynomial time, that is positively winning from every vertex of $W_{>0}\mathcal{M}\mathtt{Safe}\textsc{c})$.

````

````{admonition} Proof
:class: dropdown tip

Clearly $ W_{>0}\mathcal{M}\mathtt{Safe}\textsc{c}) = W_{>0}\mdp_{\bar{\textsc{c}},\mathtt{Safe}\textsc{c}) $ and $ W_{=1}\mathcal{M}\mathtt{Safe}\textsc{c}) = W_{=1}\mdp_{\bar{\textsc{c}},\mathtt{Safe}\textsc{c}) $; and moreover the corresponding winning strategies easily transfer between the two MDPs (for a safety objective, the behaviour after visiting a $ \textsc{c}$-coloured state is inconsequential).
Hence, putting $ Z = W_{=1}\mdp_{\bar{\textsc{c}},\mathtt{Safe}\textsc{c}) $, it is sufficient to show that  $ W_{>0}\mdp_{\bar{\textsc{c}},\mathtt{Safe}\textsc{c}) =W_{>0}\mdp_{\bar\textsc{c},\mathtt{Reach}Z))  $  

The $ \supseteq $  inclusion is clear as well as the construction of the witnessing MD strategy (in the vertices of that are outside of $ Z $, we behave as the positively winning MD strategy for reaching $ Z $, while inside $ Z $ we behave as the a.s. winning strategy for $ \mathtt{Safe}\textsc{c} $). 

For the other inclusion, let $ X = V\setminus W_{>0}\mdp_{\bar{\textsc{c}},\mathtt{Reach}Z)) $. We prove that $ X\subseteq V\setminus W_{>0}\mdp_{\bar{\textsc{c}},\mathtt{Safe}\textsc{c}) $. Assign ranks to vertices inductively as follows: each vertex coloured by $ \textsc{c}$ gets rank $ 0 $. Now if ranks $ \leq i $ have been already assigned, then a vertex  $ v $ is assigned rank $i+1  $ if it  does  not already have a lower rank but for all actions $ a\inA$ there exists a vertex $ u $ of rank $ \leq i $ s.t. $ \Deltau \mid v,a) >0$. Then each vertex in $ X $ is assigned a finite rank: indeed, the set of vertices without a rank is closed and does not contain $ \textsc{c}$-coloured vertices, hence it is contained in $ Z $. 
Now fix any strategy $ \sigma $ starting in a vertex $v \in X $. By definition of $ X $, $ \sigma $ never reaches $ Z $ and hence never visits an unranked state. At the same time, whenever $ \sigma $ is in a ranked state, there is, by definition of ranks, a probability at least $p_{\min}  $ (the minimal edge probability in $ \mathcal{M}$) of transitioning to a lower-ranked state in the next step. Hence, in every moment, the probability of $ \sigma $ reaching a $ \textsc{c}$-coloured state within the next $ |V $ steps is at least $ p_{\min}^{|V} $. By a straightforward adaptation of the second part of the proof of  {prf:ref}`5-thm:as-char`, $ \sigma $ eventually visits $ \vertices_{\textsc{c} $ with probability 1. Since $ \sigma $ was arbitrary, this shows that $ v\not \inW_{>0}\mdp_{\bar{\textsc{c}},\mathtt{Safe}\textsc{c}).  $

The complexity follows from the results on positive reachability and a.s. safety.

````


%studied in this chapter, and in particular, the almost-sure reachability 

%values in mean-payoff MDPs, for which we give a polynomial-time algorithm 

%establishing {prf:ref}`5-thm:as-complexity`. However, the algorithm we presented in 

%polynomial time}. 

%probability of a given transition is positive or not, for which the exact 

%

%\label{5-thm:qual-reach-sp}

%$W_{=1}\mathcal{M}\mathtt{Reach}\textsc{c})$, as well as the corresponding winning 

%\end{theorem}
