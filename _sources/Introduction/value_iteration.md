(1-sec:value_iteration)=
# Value iteration algorithms

```{math}
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
\newcommand{\argmax}{\text{argmax}}
\newcommand{\argmin}{\text{argmin}}
\newcommand{\Op}{\mathbb{O}}
\newcommand{\Prob}{\mathbb{P}} \newcommand{\dist}{\mathcal{D}} \newcommand{\Dist}{\dist} \newcommand{\supp}{\text{supp}} 
\newcommand{\game}{\mathcal{G}} \renewcommand{\Game}{\game} \newcommand{\arena}{\mathcal{A}} \newcommand{\Arena}{\arena} 
\newcommand{\col}{\textsf{col}} \newcommand{\Col}{\col} 
\newcommand{\mEve}{\mathrm{Eve}}
\newcommand{\mAdam}{\mathrm{Adam}}
\newcommand{\mRandom}{\mathrm{Random}}
\newcommand{\vertices}{V} \newcommand{\VE}{V_\mEve} \newcommand{\VA}{V_\mAdam} \newcommand{\VR}{V_\mRandom} 
\newcommand{\ing}{\text{In}}
\newcommand{\Ing}{\ing}
\newcommand{\out}{\text{Out}}
\newcommand{\Out}{\out}
\newcommand{\dest}{\Delta} 
\newcommand{\WE}{W_\mEve} \newcommand{\WA}{W_\mAdam} 
\newcommand{\Paths}{\text{Paths}} \newcommand{\play}{\pi} \newcommand{\first}{\text{first}} \newcommand{\last}{\text{last}} 
\newcommand{\mem}{\mathcal{M}} \newcommand{\Mem}{\mem} 
\newcommand{\Pre}{\text{Pre}} \newcommand{\PreE}{\text{Pre}_\mEve} \newcommand{\PreA}{\text{Pre}_\mAdam} \newcommand{\Attr}{\text{Attr}} \newcommand{\AttrE}{\text{Attr}_\mEve} \newcommand{\AttrA}{\text{Attr}_\mAdam} \newcommand{\rank}{\text{rank}}
\renewcommand{\Win}{\textsc{Win}} 
\renewcommand{\Lose}{\textsc{Lose}} 
\newcommand{\Value}{\text{val}} 
\newcommand{\ValueE}{\text{val}_\mEve} 
\newcommand{\ValueA}{\text{val}_\mAdam}
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
```
In this section and the next we discuss two families of fixed point algorithms for solving games.
The goal is to highlight the main ingredients for constructing algorithms in these two families.
If the descriptions below are too abstract it may be useful to see concrete instantiations: 
we refer to  Chapter {ref}`4-chap:payoffs` for archetypical examples, and also to  Chapter {ref}`3-chap:parity`.

## The value function

The key ingredient of a value iteration algorithm is a value function.
For a quantitative game $\Game$ with condition $f = \Phi[\col]$ over the set of colours $C$, 
assuming that $\Game$ is determined it admits a value function

$$
\Value^{\game} : V \to \Rinfty,
$$

which is defined as 

$$
\Value^{\game} = \sup_{\sigma}\ \inf_{\tau}\ f(\pi_{\sigma,\tau}^v) = \inf_{\tau}\ \sup_{\sigma}\ f(\pi_{\sigma,\tau}^v),
$$

where $\sigma$ ranges over strategies of Eve, $\tau$ over strategies of Adam, 
and $\pi_{\sigma,\tau}^v$ is the play consistent with $\sigma$ and $\tau$ from $v$.
In particular we write $\Value^{\sigma}$ for $\inf_{\tau}\ f(\pi_{\sigma,\tau}^v)$.

For a qualitative game $\Game$ there is no notion of a value function so the first step in constructing a value iteration
algorithm is to define a meaningful notion of value function.
Let us assume that the condition is $\Omega[\col]$ over the set of colours $C$.
The first ingredient is a lattice $(Y,\le)$ together with a function $\val : C^\omega \to Y$ for evaluating plays, taking the role of the quantitative condition $f$.
The value function is $\Value^{\game} : V \to Y$ defined as

$$
\Value^{\game}(v) = \sup_{\sigma}\ \inf_{\tau}\ \val(\pi_{\sigma,\tau}^v).
$$

As above we write $\Value^{\sigma}$ for $\inf_{\tau}\ \val(\pi_{\sigma,\tau}^v)$.

The following principle implies that computing the value function in particular yields the winning regions.

```{prf:property} Characterisation of the winning regions
For all vertices $v$ we have that Eve wins from $v$ if and only if $\Value^{\game}(v) \neq \bot$, where $\bot$ is the least element in $Y$.

```

In the remainder of this section we assume the existence of a value function $\Value^{\game} : V \to Y$ (note that choosing $Y = \Rinfty$ covers the quantitative case) and fix as a goal to either compute or approximate it.

## Fixed point

We let $F_V$ denote the set of functions $V \to Y$, it is a lattice when equipped with the componentwise (partial) order induced by $Y$:
we say that $\mu \le \mu'$ if for all vertices $v$ we have $\mu(v) \le \mu'(v)$.

The second ingredient is a function $\delta : Y \times C \to Y$ inducing an operator $\Op : F_V \to F_V$ defined by (This form is for two player games, the operator has to be adapted to more complex settings such as stochastic or concurrent games) and satisfying the following principle:

$$
\Op(\mu)(v) = 
\begin{cases}
\max \set{\delta( \mu(v'), \col(v)) : (v,v') \in E} & \text{ if } v \in \VE, \\
\min \set{\delta( \mu(v'), \col(v)) : (v,v') \in E} & \text{ if } v \in \VA.
\end{cases}
$$



```{prf:property} Fixed point
The function $\val^{\game}$ is a fixed point of the operator $\Op$.

```

This fixed point principle is often tightly related to the fact the $\Game$ is positionally determined for both players.
The fact that $\val^{\game} = \Op(\val^{\game})$ means that from a vertex $v$, 
the value $\val^{\game}(v)$ can be computed locally, **i.e.** by considering the maximum or the minimum over all edges $(v,v')$ 
of a function $\delta$ of $\val^{\game}(v')$ and of $\col(v)$.
The choice of minimum or maximum corresponds to the goal of the players: Eve wants to maximise the outcome and Adam to minimise it.

## Fixed point through contraction

Let us first consider the family of value iteration algorithms based on Banach's fixed point theorem as stated in  {prf:ref}`1-thm:banach`
and let us fix as a goal to approximate $\Value^{\game}$.
We equip $F_V$ with a norm $||\cdot||$.

```{prf:property} Fixed point through contraction
The operator $\Op$ is contracting in the complete space $(F_V,||\cdot||)$ implying that $\Value^{\game}$ is the unique fixed point of $\Op$.

```

The algorithm is the following:
we choose some $\Value_0 : V \to Y$ and then compute the sequence $(\Value_k)_{k \in \N}$ defined by $\Value_{k+1} = \Op(\Value_k)$
until we get the desired quality of approximation for $\Value^{\game}$.
We have

$$
||\Value_k - \Value^{\game}|| \le \frac{\lambda^k}{1 - \lambda} \cdot ||\Value_1 - \Value_0||,
$$

where $\lambda \in (0,1)$ is the contraction factor of $\Op$.
Hence to get an $\varepsilon$-approximation of $\Value^{\game}$ it is enough to perform 
$k = O \left( \frac{\log(\varepsilon)}{\log(\lambda)} \right)$ iterations.

## Fixed point through monotonicity

The second family of algorithms is based on Kleene's fixed point theorem as stated in  {prf:ref}`1-thm:kleene`.

```{prf:property} Fixed point through monotonicity
The function $\delta$ is monotonic (meaning that if $y \le y'$ then for all colours $c$ we have $\delta(y,c) \le \delta(y',c)$)
and $\val^{\game}$ is the greatest fixed point of the monotonic operator $\Op$.

```


```{prf:remark} (needs title)

It is possible to define the value function as the **least** fixed point of $\Op$, 
and this is equivalent up to some inversions in the lattice $(Y,\le)$ and the operator $\Op$.
There are two reasons why we chose to define the value function as the **greatest** fixed point of $\Op$.
The first is that this implies that the operator $\Op$ is defined in the same way in both qualitative and quantitative cases (for the other definition, min and max would be swapped in the definition of $\Op$ for qualitative games, which contradicts the intuition given above),
and the second is that with this convention losing from $v$ is equivalent to $\Value^{\game}(v) = \bot$,
while in the other convention it is equivalent to $\Value^{\game}(v) = \top$, where $\top$ is the greatest element in $Y$.

```

 {prf:ref}`1-thm:kleene` states that $\Value^{\game}$ is also the greatest post-fixed point.
Recall that a post-fixed point is $\mu$ such that $\mu \le \Op(\mu)$, which in this context we call a progress measure.
Expanding the definitions: for all vertices $v$, we have

$$
\begin{array}{llll}
\mu(v) & \le & \max \set{\delta( \mu(v'), \col(v)) : (v,v') \in E} & \text{ if } v \in \VE, \\
\mu(v) & \le & \min \set{\delta( \mu(v'), \col(v)) : (v,v') \in E} & \text{ if } v \in \VA,
\end{array}
$$

which is equivalent to the more familiar definition of progress measures: for all vertices $v$, we have

$$
\begin{array}{llll}
\exists (v,v') \in E,\ & \mu(v) \le \delta( \mu(v'), \col(v)) & \text{ if } v \in \VE, \\
\forall (v,v') \in E,\ & \mu(v) \le \delta( \mu(v'), \col(v)) & \text{ if } v \in \VA.
\end{array}
$$

The characterisation principle can be equivalently stated as follows.

```{prf:property} Characterisation of the winning regions -- equivalent formulation with progress measures
For all vertices $v$ we have Eve wins from $v$ if and only if there exists a progress measure $\mu$ such that $\mu(v) \neq \bot$.

```

The third information given by  {prf:ref}`1-thm:kleene` is that $\Value^{\game}$ is the limit of the sequence $(\Op^k(\top))_{k \in \N}$.

If $Y$ is a finite lattice then so is $F_V$, and the algorithm for computing $\Value^{\game}$ is as follows:
we let $\Value_0$ defined by $\Value_0(v) = \top$ and then compute the sequence $(\Value_k)_{k \in \N}$ defined by 
$\Value_{k+1} = \min(\Op(\Value_k), \Value_k)$.
There exists $k$ such that $\Value_{k+1} = \Value_k$, at which point we have that $\Value_k = \Value^{\game}$,
from which we obtain the winning regions thanks to the characterisation principle.
A naive upper bound on $k$ is $|F_V| \le |Y|^n$, but usually a finer analysis of the algorithm yields better bounds on the number of iterations to reach the fixed point.

If $Y$ is not finite that the sequence $(\Value_k)_{k \in \N}$ converges towards $\Value^{\game}$ and further analysis is required to evaluate the convergence speed.

```{prf:remark} (needs title)

It is sometimes useful to define instead of the operator $\Op$ a set of operators $(\Op_v)_{v \in V}$:

$$
\Op_v(\mu)(u) = 
\begin{cases}
\mu(v) & \text{ if } u \neq v, \\
\max \set{\delta( \mu(v'), \col(v)) : (v,v') \in E} & \text{ if } u = v \in \VE, \\
\min \set{\delta( \mu(v'), \col(v)) : (v,v') \in E} & \text{ if } u = v \in \VA.
\end{cases}
$$

The fixed points of $\Op$ and of the set of operators $(\Op_v)_{v \in V}$ are the same
and the ideas described above can be applied using  {prf:ref}`1-thm:kleene_set_operators` instead of  {prf:ref}`1-thm:kleene`.

```

