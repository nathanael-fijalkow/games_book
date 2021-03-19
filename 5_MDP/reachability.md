(5-sec:reachability)=
# Positive and almost-sure reachability and safety in MDPs

```{math}

\renewcommand{\Game}{\game}

```

%We start our study of algorithmic problems for MDPs with the most basic

> **Positive reachability**

Analogously to classical games (cf. Chapter {ref}`2-chap:regular`), we define a one-step **positive 
probability** predecessor 
operator, $\text{Pre}_{>0}$,
as follows: for $U\subseteq  V$ we put

$$

 \text{Pre}_{>0}(U) &= \{v \in  V \mid \exists a \in  A, \exists u \in U: 
 \Delta(u\mid v,a)>0 \}.\\

$$

We also define an operator $\mathcal{P}_{>0}$ s.t. for each $X\subseteq V$ we have

$$

 \mathcal{P}_{>0}(X) = X\cup  \text{Pre}_{>0}(X).

$$

It is easy to see that $\mathcal{P}_{>0}$ is a classical 
reachability operator in the underlying graph of the MDP, i.e. denoting $X_0 = 
X$ and $X_i =  \mathcal{P}_{>0}(X_{i-1})$, we get that $X_i$ is exactly the set of 
vertices from which a vertex of $X$ is reachable via a finite play of length at 
most $i$. It follows that iterating $\mathcal{P}_{>0}$ on any initial set reaches a 
fixed point in at most $n-1$ steps, where $n=| V|$.

We have the following simple characterization of the positively winning set:

````{prf:theorem} Characterisation of the positively winning set
:label: 5-thm:positive-char

For each vertex $v$, the following conditions are equivalent:

1.  The vertex $v$ belongs to $W_{>0}( \mathcal{M}, \mathtt{Reach}( c))$.
2.  There 
exists a (possibly empty) finite play from $v$ to a vertex of colour $c$.
3.  The vertex $v$ 
belongs to the fixed point of the iteration $V_c, 
 \mathcal{P}_{>0}( V_c), \mathcal{P}_{>0}^2( V_c),\cdots$.

Moreover, there exists a memoryless deterministic strategy that is positively 
winning from each vertex in $W_{>0}( \mathcal{M}, \mathtt{Reach}( c))$.

````

````{admonition} Proof
:class: dropdown tip

$(1)\Rightarrow(2)$: We have that $\mathtt{Reach}( c) = \cup_{ \pi \in X} 
 \mathit{Cyl}(\pi)$, where $X$ is the set of all finite plays ending in a vertex of 
colour $c$ and $\mathit{Cyl}(\pi)$ is the basic cylinder determined by 
$\pi$. Since $X$ is a countable set, from the property (3.) of a probability 
measure it follows that $\mathbb{P}^\sigma_{ \mathcal{M},v}( \mathtt{Reach}( c))>0$ if and 
only if there exists $\pi\in X$ with 
$\mathbb{P}^\sigma_{ \mathcal{M},v}( \mathit{Cyl}( \pi))>0$. For the latter to hold, it must 
be that either $\pi= \epsilon$, in which case $C(v)= c$, or 
$\pi$ is a non-empty play initiated in $v$ and reaching a colour 
$c$, as required.

```{margin}
Arguments of this style are said to invoke a union bound. 
```

$(2)\Rightarrow(3)$:
This is straightforward.

$(3)\Rightarrow (1)$:
For a vertex $v$, let $\textrm{rank}(v)$ be the smallest $i$ such that $v \in 
 \mathcal{P}_{>0}^i( V_c)$ (if no such $i$ exists, then 
$\textrm{rank}(v)=\infty$). For each $v$ with a positive rank there exists an action 
$a_v$ and vertex $u_v$ such that $\Delta(u_v\mid v,a_v)>0$ and 
$\textrm{rank}(u_v)<  \textrm{rank}(v)$. Consider any MD strategy $  \sigma $ with the following property: 
in each vertex of 
$W_{>0}( \mathcal{M}, \mathtt{Reach}( c))\setminus  V_{ c}$, $ \sigma $ selects the 
action $a_v$ defined above with probability 1. A straightforward induction on the rank shows that such a $ \sigma $ is positively winning from each vertex of 
$W_{>0}( \mathcal{M}, \mathtt{Reach}( c))$. This also proves the last part 
of the lemma.

````

As for complexity, we can focus on the problem of determining whether a given 
vertex belongs to $W_{>0}( \mathcal{M}, \mathtt{Reach}( c))$.

````{prf:corollary} Complexity of deciding positive reachability
:label: 5-cor:pos-complexity

The problem of deciding whether a given vertex of a given MDP belongs to 
$W_{>0}( \mathcal{M}, \mathtt{Reach}( c))$ is  \textrm{NL}-complete. Moreover, the set $W_{>0}( \mathcal{M}, \mathtt{Reach}( c))$ can be computed in linear time.

````

````{admonition} Proof
:class: dropdown tip

{prf:ref}`5-thm:positive-char` 
gives a blueprint for a logspace reduction from this problem to the 
**s-t-connectivity** problem for directed graphs, and vice versa. The latter 
problem is well known to be  \textrm{NL}-complete {cite}`Savitch:1970`. Moreover, the set of states from which a target colour is reachable can be computed by a simple graph search (e.g. by BFS), hence in linear time.

````

> **Almost-sure reachability and safety**

 While the reachability and safety objectives are seemingly dual, in MDPs there is an intimate connection between them.

Let's start with almost-sure reachability. Consider the  **almost-sure predecessor operator $\text{Pre}_{=1}$**, s.t. for each $U \subseteq  V$ we have 

$$

 \text{Pre}_{=1}(U) = \{v \in  V \mid \exists a \in  A, \forall t \in 
 V:  \Delta(t\mid v,a)>0 \Rightarrow t \in U \}.

$$

One might be tempted to mimic the positive reachability case and perform the iteration $ X \leftarrow X \cup  \text{Pre}_{=1}(X) $ on the set $  V_{ c} $ until a fixed point is reached.
But this 
is not correct: consider an MDP with two vertices, $u,v$, the latter one being coloured by $\textrm{Win}$. We have only one action $a$: in $v$, the action self loops on $v$, while in $u$ playing the action either switches moves us to $v$ or leaves us in $u$, both options having probability $\frac{1}{2}$. The probability that we **never** reach $v$ from $u$ is 
equal to $\lim_{n\rightarrow \infty} \left(\frac{1}{2}\right)^n = 0$, and hence 
$W_{=1}( \mathcal{M}, \mathtt{Reach}( \textrm{Win}))=\{u,v\}$. However, $\{v\}\cup \text{Pre}_{=1}(\{v\})=\{v\}$, so 
$v$ is not included into the outcome of the iteration. Note that there indeed exists an infinite play which **can** be generated by the strategy and 
which 
never visits $v$, but the probability of generating such a play is $0$. 

Instead, we make a detour via safety. Consider the one-step **almost-sure safety** operator $\mathit{Safe_{=1}}$ acting on sets of vertices:

$$

 \mathit{Safe_{=1}}(X)= X \cap  \text{Pre}_{=1}(X).

$$

This operator gives rise to a notion of a closed set, which is important for the study of safety objectives in MDPs.

````{prf:definition} Closed set in an MDP
:label: 5-def:closed_set_MDP

A set $X$ of vertices is closed if $  \mathit{Safe_{=1}}(X)=X$. A sub-MDP of an MDP $  \mathcal{M} $ defined by a closed subset $X$ of $  \mathcal{M} $'s states is the MDP $\mathcal{M}_X = (X, E_X, \Delta_X, c_X)$ defined as follows:

*  $E_X$ is obtained from $E$ by removing edges incident to a vertex from $V\setminus X$;
*  $\Delta_X$ is obtained from $\Delta\subseteq  V\times A\times \mathcal{D}( E)$ by removing all triples $(v,a,f)$ where either $v\not \in X$ or where the support of $f$ is not contained in $X$;
*  $c_X$ is a restriction of $c$ to $X$.

We denote by $\mathit{Cl}( \mathcal{M})$ the set of all closed sets in $\mathcal{M}.$

````

Intuitively, a set is closed if Eve has a strategy ensuring that she stays in the set forever.

Now consider the iteration of $ X,  \mathit{Safe_{=1}}(X), \mathit{Safe_{=1}}^2(X),\ldots $ of the safety operator. Clearly $\mathit{Safe_{=1}}(X)\subseteq X$. Hence, the iteration reaches a fixed point in at most $| V|$ steps. We get the following:

````{prf:lemma} Inclusion of the least fixed of the safety operator
:label: 5-lem:safety-iteration

The fixed point of iterating $  \mathit{Safe_{=1}} $ on some initial set $ X $ of $  \mathcal{M} $'s vertices is the largest (w.r.t. inclusion) closed set contained in $ X $. In particular, a vertex of $ X $ which does not belong to the fixpoint cannot belong to  $W_{=1}( \mathcal{M}, \mathtt{Safe}( V \setminus X))$.

````

````{admonition} Proof
:class: dropdown tip

A straightforward induction on the number of iteration shows that if a vertex $ v $ is removed in an $ i $-th iteration, then no matter what strategy Eve uses, she has to reach $  V\setminus X $ in at most $ i $ steps with a positive probability. The lemma follows.

````

```{figure} ./../FigAndAlgos/5-algo:safety.png
:name: 5-algo:safety
:align: center
An algorithm computing $W_{=1}( \mathcal{M}, \mathtt{Safe}( c))$
```

````{prf:theorem} Complexity of the almost-sure safety winning set
:label: 5-thm:safety-main

{numref}`5-algo:safety` computes the set $W_{=1}( \mathcal{M}, \mathtt{Safe}( c))$ in strongly polynomial time. Moreover, there exists a memoryless deterministic strategy, computable in polynomial time, that is almost-surely winning from every vertex of $W_{=1}( \mathcal{M}, \mathtt{Safe}( c))$.

````

````{admonition} Proof
:class: dropdown tip

The correctness follows immediately from {prf:ref}`5-lem:safety-iteration`. The algorithm makes at most linearly many iterations, each of which has at most linear complexity. Hence, the complexity is at most quadratic. The strong polynomiality is testified by the fact that the algorithm only tests whether a 
probability of a given transition is positive or not, for which the exact 
values of positive probabilities are irrelevant. Clearly the output of the algorithm is a closed set, and hence for each $ v\in   W_{=1}( \mathcal{M}, \mathtt{Safe}( c))$ there is an action $ a_v $ such that all edges in the support of $  \Delta(v,a_v)  $ lead back to $  W_{=1}( \mathcal{M}, \mathtt{Safe}( c)) $. Any MD strategy which in each $ v\in   W_{=1}( \mathcal{M}, \mathtt{Safe}( c)) $ chooses $ a_v $ with probability 1 is a.s. winning inside $  W_{=1}( \mathcal{M}, \mathtt{Safe}( c)) $, which proves the last part of the lemma.

````

```{figure} ./../FigAndAlgos/5-algo:reach-as.png
:name: 5-algo:reach-as
:align: center
An algorithm computing $W_{=1}( \mathcal{M}, \mathtt{Reach}( c))$
```

With a.s. safety solved, we go back to a.s. reachability, which is solved via {numref}`5-algo:reach-as`. Note that in the first iteration, the algorithm computes the set 
$W_{=1}( \mathcal{M}, \mathtt{Safe}(Z))$ where $ Z =   W_{>0}( \mathcal{M}, \mathtt{Reach}( c))$. We might be tempted to think that this set already equals $  W_{=1}( \mathcal{M}, \mathtt{Reach}( c)) $, but this is not the case. To see this, consider an MDP with three states $ u,v,t $ and two actions $ a,b $ such that $ t $ is coloured by $  \textrm{Win} $, both actions self loop in $ v $ and $ t $, and $  \Delta(t \mid u,a) =  \Delta(v \mid u,a) = \frac{1}{2} $ while $  \Delta(u \mid u,b) = 1 $. Then $  W_{=1}( \mathcal{M}, \mathtt{Reach}( \textrm{Win})) = \{t\} $ while at the same time $  W_{=1}( \mathcal{M}, \mathtt{Safe}(  W_{>0}( \mathcal{M}, \mathtt{Reach}( \textrm{Win})))) = \{u,t\}$. However, iterating the computation works, as shown in the following theorem.

````{prf:theorem} Algorithm for the almost-sure reachability winning set
:label: 5-thm:as-char

{numref}`5-algo:reach-as` computes $W_{=1}( \mathcal{M}, \mathtt{Reach}( c))$ in strongly polynomial time. Moreover, there is an MD strategy, computable in strongly polynomial time, that is almost-surely winning from every vertex of $W_{=1}( \mathcal{M}, \mathtt{Reach}( c))$.

````

````{admonition} Proof
:class: dropdown tip

Since the set $ W $ can only decrease in each iteration, the algorithm terminates.
We prove that upon termination, $W$ equals $W_{=1}( \mathcal{M}, \mathtt{Reach}( c))$.

We start with the $ \subseteq $ direction. We have $W \subseteq  W_{>0}( \mathcal{M}_W, \mathtt{Reach}( c))$. By {prf:ref}`5-thm:positive-char` there exists an MD strategy $\sigma$ in $\mathcal{M}_W$ which is positively winning from each vertex of $W$. We show that the same strategy is also almost-surely winning from each vertex of $W$ in $\mathcal{M}_W$ and thus also from each vertex of $W$ in $\mathcal{M}$, which also proves the second part of the theorem. 

Let $v$ be any vertex of $W$ and denote $|W|$ by $\ell$. Since $\sigma$ is memoryless, it guarantees that a vertex of $V_{ c}$ is reached with a positive probability in at most $\ell$ steps (see also the construction of $ \sigma $ in the proof of {prf:ref}`5-thm:positive-char`), and since it is also deterministic, it guarantees that the probability $p$ of reaching $V_{ c}$ in at most $\ell$ steps is at least $p_{\min}^{\ell}$, where  $p_{\min}$ is the smallest non-zero edge probability in $\mathcal{M}_W$. Now imagine that $\ell$ steps have elapsed and we have not yet reached $V_{ c}$. This happens with a probability at most $(1-p_{\min}^\ell)$. However, even after these $\ell$ steps we are still in $W$, since $ \sigma  $ is a strategy in $  \mathcal{M}_w $. Hence, the probability that we do not reach $V_c$ within the first $2\ell$ steps is bounded by $(1-p_{\min}^\ell)^{2}$. To realize why this is the case, note that any finite play $\pi$ of length $2\ell$ can be split into two halves, $\pi', \pi''$ of length $\ell$, and then $\mathbb{P}^{\sigma}_{v}( \mathit{Cyl}( \pi))= \mathbb{P}^{\sigma}_{v}( \mathit{Cyl}( \pi'))\cdot \mathbb{P}^{\sigma}_{ \textrm{last}( \pi')}( \mathit{Cyl}( \pi''))$ (here we use the fact that $\sigma$ is memoryless). Using this and some arithmetic, one can show that, denoting $\mathit{Avoid}_i$ the set of all plays that avoid the vertices of $V_{ c}$ in steps $\ell\cdot(i-1)$ to $\ell\cdot(i)-1$, it holds 

$$

 \mathbb{P}^{\sigma}_{v}(\mathit{Avoid}_1\cap \mathit{Avoid}_2) \leq  \mathbb{P}^{\sigma}_{v}(\mathit{Avoid}_1)\cdot \max_{u\in W\setminus  V_{ c}} \mathbb{P}^{\sigma}_{u}(\mathit{Avoid}_1)\leq (1-p_{\min}^\ell)^{2}.

$$

One can then continue by induction to show that $\mathbb{P}^{\sigma}_{v}(\bigcap_{i=1}^j \mathit{Avoid}_i)\leq (1-p_{\min}^\ell)^{j},$ and hence

$$

 \mathbb{P}^\sigma_{v}( \mathtt{Reach}( c))= 1- \mathbb{P}^{\sigma}_{v}(\bigcap_{i=1}^\infty \mathit{Avoid}_i) \leq 1-\lim_{j\rightarrow \infty}(1-p_{\min}^\ell)^{j}= 1-0=1.

$$

Now we prove the $ \supseteq $ direction. Denote $X= W_{=1}( \mathcal{M}, \mathtt{Reach}( c))$. We prove that $ W \supseteq X $ is an invariant of the iteration. Initially this is clear. Now assume that this holds before an iteration takes place. It is easy to check that $X$ is closed, so $\mathcal{M}_{X}$ is well-defined. We prove that $ X \subseteq  W_{=1}( \mathcal{M}_W, \mathtt{Safe}(W\setminus Z)) $, where $ Z $ is defined during the iteration. A strategy in $\mathcal{M}$ that reaches $V_{ c}$ with probability 1 must never visit a vertex from $V\setminus X$ with a positive probability. Hence, each such strategy can be viewed also as a strategy in $\mathcal{M}_{X}$. It follows that  $X= W_{=1}( \mathcal{M}_X, \mathtt{Reach}( c)) =  W_{>0}( \mathcal{M}_{X}, \mathtt{Reach}( c)) \subseteq  W_{>0}( \mathcal{M}_{W}, \mathtt{Reach}( c)) = Z$, the middle inclusion following from induction hypothesis. Now by {prf:ref}`5-lem:safety-iteration` and {prf:ref}`5-thm:safety-main`, the set $  W_{=1}( \mathcal{M}_W, \mathtt{Safe}(W\setminus Z)) $ is the largest closed set contained in $ Z $. But $ X $ is also closed, and ashown above, it is contained in $ Z $. Hence,  $ X \subseteq  W_{=1}( \mathcal{M}_W, \mathtt{Safe}(W \setminus Z)) $.

The complexity follows form {prf:ref}`5-cor:pos-complexity` and {prf:ref}`5-thm:safety-main`; and also from the fact that the main loop must terminate in $ \leq | V| $ steps. The strong polynomiality again follows from the algorithm being oblivious to precise probabilities.

````

We also have a complementary hardness result.

````{prf:theorem} Complexity of the almost-sure reachability winning set
:label: 5-thm:as-complexity

The problem of determining whether a given vertex of a given MDP belongs to 
$W_{=1}( \mathcal{M}, \mathtt{Reach}( c))$ is  \textrm{PTIME}-complete.

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
$\mathcal{C}$, construct an MDP $\mathcal{M}_{\mathcal{C}}$ whose vertices correspond 
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
$W_{=1}( \mathcal{M}_{\mathcal{C}}, \mathtt{Reach}(\mathit{true}))$.

````

> **Positive safety**

 We conclude this section by a discussion of positive safety.

````{prf:theorem} Algorithm for the positive safety winning set
:label: 5-thm:pos-safety-main

Let $  \mathcal{M}_{\bar c} $ be an MDP obtained from $  \mathcal{M} $ by changing all $  c $-coloured vertices to sinks (i.e. all actions in these vertices just self loop on the vertex). Then
$  W_{>0}( \mathcal{M}, \mathtt{Safe}( c)) =  W_{>0}( \mathcal{M}_{\bar c}, \mathtt{Reach}( W_{=1}( \mathcal{M}_{\bar c}, \mathtt{Safe}( c))) ) $. In particular, the set $  W_{>0}( \mathcal{M}, \mathtt{Safe}( c)) $ can be computed in a strongly polynomial time and there exists a memoryless deterministic strategy, computable in strongly polynomial time, that is positively winning from every vertex of $W_{>0}( \mathcal{M}, \mathtt{Safe}( c))$.

````

````{admonition} Proof
:class: dropdown tip

Clearly $  W_{>0}( \mathcal{M}, \mathtt{Safe}( c)) =  W_{>0}( \mathcal{M}_{\bar{ c}}, \mathtt{Safe}( c)) $ and $  W_{=1}( \mathcal{M}, \mathtt{Safe}( c)) =  W_{=1}( \mathcal{M}_{\bar{ c}}, \mathtt{Safe}( c)) $; and moreover the corresponding winning strategies easily transfer between the two MDPs (for a safety objective, the behaviour after visiting a $  c $-coloured state is inconsequential).
Hence, putting $ Z =  W_{=1}( \mathcal{M}_{\bar{ c}}, \mathtt{Safe}( c)) $, it is sufficient to show that  $  W_{>0}( \mathcal{M}_{\bar{ c}}, \mathtt{Safe}( c)) = W_{>0}( \mathcal{M}_{\bar c}, \mathtt{Reach}(Z))  $  

The $ \supseteq $  inclusion is clear as well as the construction of the witnessing MD strategy (in the vertices of that are outside of $ Z $, we behave as the positively winning MD strategy for reaching $ Z $, while inside $ Z $ we behave as the a.s. winning strategy for $  \mathtt{Safe}( c) $). 

For the other inclusion, let $ X =  V \setminus  W_{>0}( \mathcal{M}_{\bar{ c}}, \mathtt{Reach}(Z)) $. We prove that $ X\subseteq  V \setminus  W_{>0}( \mathcal{M}_{\bar{ c}}, \mathtt{Safe}( c)) $. Assign ranks to vertices inductively as follows: each vertex coloured by $  c $ gets rank $ 0 $. Now if ranks $ \leq i $ have been already assigned, then a vertex  $ v $ is assigned rank $i+1  $ if it  does  not already have a lower rank but for all actions $ a\in A $ there exists a vertex $ u $ of rank $ \leq i $ s.t. $  \Delta(u \mid v,a) >0$. Then each vertex in $ X $ is assigned a finite rank: indeed, the set of vertices without a rank is closed and does not contain $  c $-coloured vertices, hence it is contained in $ Z $. 
Now fix any strategy $ \sigma $ starting in a vertex $v \in X $. By definition of $ X $, $ \sigma $ never reaches $ Z $ and hence never visits an unranked state. At the same time, whenever $ \sigma $ is in a ranked state, there is, by definition of ranks, a probability at least $p_{\min}  $ (the minimal edge probability in $  \mathcal{M} $) of transitioning to a lower-ranked state in the next step. Hence, in every moment, the probability of $ \sigma $ reaching a $  c $-coloured state within the next $ | V| $ steps is at least $ p_{\min}^{| V|} $. By a straightforward adaptation of the second part of the proof of {prf:ref}`5-thm:as-char`, $ \sigma $ eventually visits $  V_{ c} $ with probability 1. Since $ \sigma $ was arbitrary, this shows that $ v\not \in W_{>0}( \mathcal{M}_{\bar{ c}}, \mathtt{Safe}( c)).  $

The complexity follows from the results on positive reachability and a.s. safety.

````

