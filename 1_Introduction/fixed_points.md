(1-sec:fixed_points)=
# Generic fixed point algorithms


```{math}
\newcommand{\N}{\mathbb{N}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\Rinfty}{\R \cup \set{\pm \infty}}
\newcommand{\Op}{\mathbb{O}}
```

Let $X$ be a set and $\mathbb{O}: X \to X$ a function that we call an operator, we say that $x \in X$ is a fixed point of $\mathbb{O} if $\mathbb{O}x) = x$.
Fixed points will appear extensively in this book. 
We describe here two general approaches for computing them: Banach's and Kleene's fixed point theorems.

## Banach fixed point theorem

Let us consider a set $X$ equipped with some norm $||\cdot||$.
It is said complete if all Cauchy sequences converge.
The typical example of a complete space is $\mathbb{R}d$ for some $d \in \mathbb{N} equipped with the infinity norm $||x|| = \max_{i \in [1,d]} |x_i|$.

An operator $\mathbb{O}: X \to X$ is contracting if there exists $\lambda < 1$ such that for all $x,y \in X$ we have
$||\mathbb{O}x) - \mathbb{O}y)|| \le \lambda \cdot ||x - y||$.

````{prf:theorem} Banach fixed point theorem
:label: 1-thm:banach

Let $(X,||\cdot||)$ be a complete space and $\mathbb{O}: X \to X$ a contracting operator, then $\mathbb{O} has a unique fixed point $x_*$.
For any $x_0 \in X$, the sequence $(\mathbb{O}k(x_0))_{k \in \mathbb{N}$ converges towards $x_*$ and the rate of convergence is given by

$$
||\mathbb{O}k(x_0) - x_*|| \le \frac{\lambda^k}{1 - \lambda} \cdot ||\mathbb{O}x_0) - x_0||.
$$


````


%It is said complete if all Cauchy sequences converge.

%$d(\mathbb{O}x),\mathbb{O}y)) \le \lambda \cdot d(x,y)$.

%\begin{theorem}[Banach's fixed point theorem]

%Let $(X,d)$ be a complete metric space and $\mathbb{O}: X \to X$ a contracting operator, then $\mathbb{O} has a unique fixed point $x_*$.

%

$$

%$$



## Kleene fixed point theorem

Let us consider a lattice $(X,\le)$: the binary relation $\le$ is a partial order, and every pair of elements has a least upper bound and a greatest lower bound. It is a complete lattice if every set has a least upper bound and a greatest lower bound.
A lattice is finite if the set $X$ is finite.
Note that finite lattices are always complete.

We write $\bot$ for the least element in $X$ and $\top$ for the greatest element.
An operator $\mathbb{O}: X \to X$ is monotonic if for all $x,y \in X$ such that $x \le y$ we have $\mathbb{O}x) \le \mathbb{O}y)$,
inflationary if for all $x \in X$ we have $x \le \mathbb{O}x)$,
and preserves suprema if $\mathbb{O}\sup_n x_n) = \sup_n \mathbb{O}x_n)$ for all increasing sequences $(x_n)_{n \in \mathbb{N}$.
The twin notions are deflationary if $x \ge \mathbb{O}x)$ and preserves infima defined accordingly.

We say that $x$ is a pre-fixed point if $\mathbb{O}x) \le x$ and a post-fixed point if $\mathbb{O}x) \ge x$.

````{prf:theorem} Kleene fixed point theorem
:label: 1-thm:kleene

Let $(X,\le)$ be a complete lattice and $\mathbb{O}: X \to X$ a monotonic operator, then $\mathbb{O} has a least fixed point
which is also the least pre-fixed point.

Furthermore:

*  if $X$ is finite the sequence defined by $u_0 = \bot$ and $u_{k+1} = \max(u_k, \mathbb{O}u_k))$ is stationary and its limit is the least fixed point of $\mathbb{O}, and if $\mathbb{O} is inflationary the sequence is simply $(\mathbb{O}k(\bot))_{k \in \mathbb{N}$;
*  if $\mathbb{O} preserves suprema then the least fixed point of $\mathbb{O} is $\sup \set{ \mathbb{O}k(\bot) :  k \in \mathbb{N}$.

````

Under the same assumptions $\mathbb{O} has a greatest fixed point which is the greatest post-fixed point and can be computed in similar ways,
replacing inflationary by deflationary and preserves suprema by preserves infima.

%which is monotonic and inflationary if $\mathbb{O} is monotonic.

The typical example of a complete lattice and one that we will use often in this book is the powerset of a set equipped with the inclusion between subsets. The least element is the empty set, the greatest element the full set, and least and greatest upper bounds are given by union and intersection.
An example of an infinite complete lattice is $\mathbb{R}\cup \set{\pm \infty} equipped with the natural order.


We state a variant of  {prf:ref}`1-thm:kleene` for a set of operators $\Op_i : X \to X$ for $i \in I$.
Naturally we say that $x \in X$ is a fixed point of the set of operators $(\Op_i)_{i \in I}$ if for all $i \in I$ we have $\Op_i(x) = x$.

````{prf:theorem} Kleene fixed point theorem for a finite lattice and a set of operators
:label: 1-thm:kleene_set_operators

Let $(X,\le)$ be a finite lattice and $\Op_i : X \to X$ a set of monotonic operators for $i \in I$, then $(\Op_i)_{i \in I}$ has a least fixed point.
The non-deterministic algorithm given in {numref}`1-algo:fixed_point` computes the least fixed point of $(\Op_i)_{i \in I}$.

````

Under the same assumptions $(\Op_i)_{i \in I}$ has a greatest fixed point which is computed by the dual algorithm.

```{figure} ./../FigAndAlgos/1-algo:fixed_point.png
:name: 1-algo:fixed_point
:align: center
The generic non-deterministic least fixed point algorithm for a set of monotonic operators.
```

