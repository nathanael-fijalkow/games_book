(1-sec:9_fixed_points)=
# Generic fixed point algorithms

Let $X$ be a set and $\Op : X \to X$ a function that we call an operator, we say that $x \in X$ is a fixed point of $\Op$ if $\Op(x) = x$.
Fixed points will appear extensively in this book. 
We describe here two general approaches for computing them: Banach's and Kleene's fixed point theorems.

### Banach's fixed point theorem

Let us consider a set $X$ equipped with some norm $||\cdot||$.
It is said complete if all Cauchy sequences converge.
The typical example of a complete space is $\R^d$ for some $d \in \N$ equipped with the infinity norm $||x|| = \max_{i \in [1,d]} |x_i|$.

An operator $\Op : X \to X$ is contracting if there exists $\lambda < 1$ such that for all $x,y \in X$ we have
$||\Op(x) - \Op(y)|| \le \lambda \cdot ||x - y||$.

```{admonition} Theorem (Banach's fixed point theorem)
:class: theorem
:name: 1-thm:banach

Let $(X,||\cdot||)$ be a complete space and $\Op : X \to X$ a contracting operator, then $\Op$ has a unique fixed point $x_*$.
For any $x_0 \in X$, the sequence $(\Op^k(x_0))_{k \in \N}$ converges towards $x_*$ and the rate of convergence is given by

$$

||\Op^k(x_0) - x_*|| \le \frac{\lambda^k}{1 - \lambda} \cdot ||\Op(x_0) - x_0||.

$$


```



### Kleene's fixed point theorem

Let us consider a lattice $(X,\le)$: the binary relation $\le$ is a partial order, and every pair of elements has a least upper bound and a greatest lower bound. It is a complete lattice if every set has a least upper bound and a greatest lower bound.
A lattice is finite if the set $X$ is finite.
Note that finite lattices are always complete.

We write $\bot$ for the least element in $X$ and $\top$ for the greatest element.
An operator $\Op : X \to X$ is monotonic if for all $x,y \in X$ such that $x \le y$ we have $\Op(x) \le \Op(y)$,
inflationary if for all $x \in X$ we have $x \le \Op(x)$,
and preserves suprema if $\Op(\sup_n x_n) = \sup_n \Op(x_n)$ for all increasing sequences $(x_n)_{n \in \N}$.
The twin notions are deflationary if $x \ge \Op(x)$ and preserves infima defined accordingly.

We say that $x$ is a pre-fixed point if $\Op(x) \le x$ and a post-fixed point if $\Op(x) \ge x$.

```{admonition} Theorem (Kleene's fixed point theorem)
:class: theorem
:name: 1-thm:kleene

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


We state a variant of  {ref}`Theorem <1-thm:kleene>` for a set of operators $\Op_i : X \to X$ for $i \in I$.
Naturally we say that $x \in X$ is a fixed point of the set of operators $(\Op_i)_{i \in I}$ if for all $i \in I$ we have $\Op_i(x) = x$.

```{admonition} Theorem (Kleene's fixed point theorem for a finite lattice and a set of operators)
:class: theorem
:name: 1-thm:kleene_set_operators

Let $(X,\le)$ be a finite lattice and $\Op_i : X \to X$ a set of monotonic operators for $i \in I$, then $(\Op_i)_{i \in I}$ has a least fixed point.
The non-deterministic algorithm given in  {ref}`Algorithm <1-algo:fixed_point>` computes the least fixed point of $(\Op_i)_{i \in I}$.

```

Under the same assumptions $(\Op_i)_{i \in I}$ has a greatest fixed point which is computed by the dual algorithm.

\begin{algorithm}
 \KwData{$(X,\le)$ a finite lattice and $\Op_i : X \to X$ a set of monotonic operators for $i \in I$}

$x \leftarrow \bot$ 

\Repeat{$x$ is a fixed point of $(\Op_i)_{i \in I}$}{
Choose $i \in I$ such that $\neg (\Op_i(x) \le x)$

$x \leftarrow \max(x, \Op_i(x))$ 
}

\Return{$x$}
\caption{The generic non-deterministic least fixed point algorithm for a set of monotonic operators.}
\label{1-algo:fixed_point}
\end{algorithm}

