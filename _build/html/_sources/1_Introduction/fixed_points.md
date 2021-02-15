(1-sec:fixed_points)=
# Generic fixed point algorithms

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
```
Let $X$ be a set and $\Op : X \to X$ a function that we call an operator, we say that $x \in X$ is a fixed point of $\Op$ if $\Op(x) = x$.
Fixed points will appear extensively in this book. 
We describe here two general approaches for computing them: Banach's and Kleene's fixed point theorems.

## Banach fixed point theorem
Let us consider a set $X$ equipped with some norm $||\cdot||$.
It is said complete if all Cauchy sequences converge.
The typical example of a complete space is $\R^d$ for some $d \in \N$ equipped with the infinity norm $||x|| = \max_{i \in [1,d]} |x_i|$.

An operator $\Op : X \to X$ is contracting if there exists $\lambda < 1$ such that for all $x,y \in X$ we have
$||\Op(x) - \Op(y)|| \le \lambda \cdot ||x - y||$.

```{prf:theorem} Banach fixed point theorem
:label: 1-thm:banach

Let $(X,||\cdot||)$ be a complete space and $\Op : X \to X$ a contracting operator, then $\Op$ has a unique fixed point $x_*$.
For any $x_0 \in X$, the sequence $(\Op^k(x_0))_{k \in \N}$ converges towards $x_*$ and the rate of convergence is given by

$$
||\Op^k(x_0) - x_*|| \le \frac{\lambda^k}{1 - \lambda} \cdot ||\Op(x_0) - x_0||.
$$


```



## Kleene fixed point theorem
Let us consider a lattice $(X,\le)$: the binary relation $\le$ is a partial order, and every pair of elements has a least upper bound and a greatest lower bound. It is a complete lattice if every set has a least upper bound and a greatest lower bound.
A lattice is finite if the set $X$ is finite.
Note that finite lattices are always complete.

We write $\bot$ for the least element in $X$ and $\top$ for the greatest element.
An operator $\Op : X \to X$ is monotonic if for all $x,y \in X$ such that $x \le y$ we have $\Op(x) \le \Op(y)$,
inflationary if for all $x \in X$ we have $x \le \Op(x)$,
and preserves suprema if $\Op(\sup_n x_n) = \sup_n \Op(x_n)$ for all increasing sequences $(x_n)_{n \in \N}$.
The twin notions are deflationary if $x \ge \Op(x)$ and preserves infima defined accordingly.

We say that $x$ is a pre-fixed point if $\Op(x) \le x$ and a post-fixed point if $\Op(x) \ge x$.

```{prf:theorem} Kleene fixed point theorem
:label: 1-thm:kleene

Let $(X,\le)$ be a complete lattice and $\Op : X \to X$ a monotonic operator, then $\Op$ has a least fixed point
which is also the least pre-fixed point.

Furthermore:

*  if $X$ is finite the sequence defined by $u_0 = \bot$ and $u_{k+1} = \max(u_k, \Op(u_k))$ is stationary and its limit is the least fixed point of $\Op$, and if $\Op$ is inflationary the sequence is simply $(\Op^k(\bot))_{k \in \N}$;
*  if $\Op$ preserves suprema then the least fixed point of $\Op$ is $\sup \set{ \Op^k(\bot) :  k \in \N}$.

```

Under the same assumptions $\Op$ has a greatest fixed point which is the greatest post-fixed point and can be computed in similar ways,
replacing inflationary by deflationary and preserves suprema by preserves infima.

The typical example of a complete lattice and one that we will use often in this book is the powerset of a set equipped with the inclusion between subsets. The least element is the empty set, the greatest element the full set, and least and greatest upper bounds are given by union and intersection.
An example of an infinite complete lattice is $\Rinfty$ equipped with the natural order.


We state a variant of  {prf:ref}`1-thm:kleene` for a set of operators $\Op_i : X \to X$ for $i \in I$.
Naturally we say that $x \in X$ is a fixed point of the set of operators $(\Op_i)_{i \in I}$ if for all $i \in I$ we have $\Op_i(x) = x$.

```{prf:theorem} Kleene fixed point theorem for a finite lattice and a set of operators
:label: 1-thm:kleene_set_operators

Let $(X,\le)$ be a finite lattice and $\Op_i : X \to X$ a set of monotonic operators for $i \in I$, then $(\Op_i)_{i \in I}$ has a least fixed point.
The non-deterministic algorithm given in {numref}`1-algo:fixed_point` computes the least fixed point of $(\Op_i)_{i \in I}$.

```

Under the same assumptions $(\Op_i)_{i \in I}$ has a greatest fixed point which is computed by the dual algorithm.

```{figure} ./../1-algo:fixed_point.png
:name: 1-algo:fixed_point
:align: center
The generic non-deterministic least fixed point algorithm for a set of monotonic operators.
```

