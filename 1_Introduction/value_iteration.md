(1-sec:value_iteration)=
# Value iteration algorithms

```{math}

```

In this section and the next we discuss two families of fixed point algorithms for solving games.
The goal is to highlight the main ingredients for constructing algorithms in these two families.
If the descriptions below are too abstract it may be useful to see concrete instantiations: 
we refer to Chapter {ref}`4-chap:payoffs` for archetypical examples, and also to Chapter {ref}`3-chap:parity`.

## The value function

The key ingredient of a value iteration algorithm is a value function.
For a quantitative game $\mathcal{G}$ with condition $f = \Phi[ \mathfrak{c}]$ over the set of colours $C$, 
assuming that $\mathcal{G}$ is determined it admits a value function

$$
 \textrm{val}^{ \mathcal{G}} : V \to   \mathbb{R} \cup  \left\{ \pm \infty \right\},
$$

which is defined as

$$
 \textrm{val}^{ \mathcal{G}} = \sup_{\sigma}\ \inf_{\tau}\ f(\pi_{\sigma,\tau}^v) = \inf_{\tau}\ \sup_{\sigma}\ f(\pi_{\sigma,\tau}^v),
$$

where $\sigma$ ranges over strategies of Eve, $\tau$ over strategies of Adam, 
and $\pi_{\sigma,\tau}^v$ is the play consistent with $\sigma$ and $\tau$ from $v$.
In particular we write $\textrm{val}^{\sigma}$ for $\inf_{\tau}\ f(\pi_{\sigma,\tau}^v)$.

For a qualitative game $\mathcal{G}$ there is no notion of a value function so the first step in constructing a value iteration
algorithm is to define a meaningful notion of value function.
Let us assume that the condition is $\Omega[ \mathfrak{c}]$ over the set of colours $C$.
The first ingredient is a lattice $(Y,\le)$ together with a function $\textrm{val} : C^\omega \to Y$ for evaluating plays, taking the role of the quantitative condition $f$.
The value function is $\textrm{val}^{ \mathcal{G}} : V \to Y$ defined as

$$
 \textrm{val}^{ \mathcal{G}}(v) = \sup_{\sigma}\ \inf_{\tau}\   \textrm{val}(\pi_{\sigma,\tau}^v).
$$

As above we write $\textrm{val}^{\sigma}$ for $\inf_{\tau}\   \textrm{val}(\pi_{\sigma,\tau}^v)$.

The following principle implies that computing the value function in particular yields the winning regions.

````{prf:property} Characterisation of the winning regions
:label: 1-property:characterisation_winning_regions

For all vertices $v$ we have that Eve wins from $v$ if and only if $\textrm{val}^{ \mathcal{G}}(v) \neq \bot$, where $\bot$ is the least element in $Y$.

````

In the remainder of this section we assume the existence of a value function $\textrm{val}^{ \mathcal{G}} : V \to Y$ (note that choosing $Y =   \mathbb{R} \cup  \left\{ \pm \infty \right\}$ covers the quantitative case) and fix as a goal to either compute or approximate it.

## Fixed point

We let $F_V$ denote the set of functions $V \to Y$, it is a lattice when equipped with the componentwise (partial) order induced by $Y$:
we say that $\mu \le \mu'$ if for all vertices $v$ we have $\mu(v) \le \mu'(v)$.

The second ingredient is a function $\delta : Y \times C \to Y$ inducing an operator $\mathbb{O} : F_V \to F_V$ defined by and satisfying the following principle:

```{margin}
This form is for two player games, the operator has to be adapted to more complex settings such as stochastic or concurrent games.
```

$$
 \mathbb{O}(\mu)(v) = 
\begin{cases}
\max  \left\{ \delta( \mu(v'),  \mathfrak{c \right\}(v)) : (v,v') \in E} & \text{ if } v \in  V_\mathrm{Eve}, \\
\min  \left\{ \delta( \mu(v'),  \mathfrak{c \right\}(v)) : (v,v') \in E} & \text{ if } v \in  V_\mathrm{Adam}.
\end{cases}
$$

````{prf:property} Fixed point
:label: 1-property:fixed_point

The function $\textrm{val}^{ \mathcal{G}}$ is a fixed point of the operator $\mathbb{O}$.

````

This fixed point principle is often tightly related to the fact the $\mathcal{G}$ is positionally determined for both players.
The fact that $\textrm{val}^{ \mathcal{G}} =  \mathbb{O}(  \textrm{val}^{ \mathcal{G}})$ means that from a vertex $v$, 
the value $\textrm{val}^{ \mathcal{G}}(v)$ can be computed locally, **i.e.** by considering the maximum or the minimum over all edges $(v,v')$ 
of a function $\delta$ of $\textrm{val}^{ \mathcal{G}}(v')$ and of $\mathfrak{c}(v)$.
The choice of minimum or maximum corresponds to the goal of the players: Eve wants to maximise the outcome and Adam to minimise it.

## Fixed point through contraction

Let us first consider the family of value iteration algorithms based on Banach's fixed point theorem as stated in {prf:ref}`1-thm:banach`
and let us fix as a goal to approximate $\textrm{val}^{ \mathcal{G}}$.
We equip $F_V$ with a norm $||\cdot||$.

````{prf:property} Fixed point through contraction
:label: 1-property:fixed_point_contraction

The operator $\mathbb{O}$ is contracting in the complete space $(F_V,||\cdot||)$ implying that $\textrm{val}^{ \mathcal{G}}$ is the unique fixed point of $\mathbb{O}$.

````

The algorithm is the following:
we choose some $\textrm{val}_0 : V \to Y$ and then compute the sequence $( \textrm{val}_k)_{k \in  \mathbb{N}}$ defined by $\textrm{val}_{k+1} =  \mathbb{O}( \textrm{val}_k)$
until we get the desired quality of approximation for $\textrm{val}^{ \mathcal{G}}$.
We have

$$
|| \textrm{val}_k -  \textrm{val}^{ \mathcal{G}}|| \le \frac{\lambda^k}{1 - \lambda} \cdot || \textrm{val}_1 -  \textrm{val}_0||,
$$

where $\lambda \in (0,1)$ is the contraction factor of $\mathbb{O}$.
Hence to get an $\varepsilon$-approximation of $\textrm{val}^{ \mathcal{G}}$ it is enough to perform 
$k = O \left( \frac{\log(\varepsilon)}{\log(\lambda)} \right)$ iterations.

## Fixed point through monotonicity

The second family of algorithms is based on Kleene's fixed point theorem as stated in {prf:ref}`1-thm:kleene`.

````{prf:property} Fixed point through monotonicity
:label: 1-property:fixed_point_monotonicity

The function $\delta$ is monotonic (meaning that if $y \le y'$ then for all colours $c$ we have $\delta(y,c) \le \delta(y',c)$)
and $\textrm{val}^{ \mathcal{G}}$ is the greatest fixed point of the monotonic operator $\mathbb{O}$.

````

````{prf:remark} NEEDS TITLE AND LABEL 
It is possible to define the value function as the **least** fixed point of $\mathbb{O}$, 
and this is equivalent up to some inversions in the lattice $(Y,\le)$ and the operator $\mathbb{O}$.
There are two reasons why we chose to define the value function as the **greatest** fixed point of $\mathbb{O}$.
The first is that this implies that the operator $\mathbb{O}$ is defined in the same way in both qualitative and quantitative cases (for the other definition, min and max would be swapped in the definition of $\mathbb{O}$ for qualitative games, which contradicts the intuition given above),
and the second is that with this convention losing from $v$ is equivalent to $\textrm{val}^{ \mathcal{G}}(v) = \bot$,
while in the other convention it is equivalent to $\textrm{val}^{ \mathcal{G}}(v) = \top$, where $\top$ is the greatest element in $Y$.

It is possible to define the value function as the **least** fixed point of $\mathbb{O}$, 
and this is equivalent up to some inversions in the lattice $(Y,\le)$ and the operator $\mathbb{O}$.
There are two reasons why we chose to define the value function as the **greatest** fixed point of $\mathbb{O}$.
The first is that this implies that the operator $\mathbb{O}$ is defined in the same way in both qualitative and quantitative cases (for the other definition, min and max would be swapped in the definition of $\mathbb{O}$ for qualitative games, which contradicts the intuition given above),
and the second is that with this convention losing from $v$ is equivalent to $\textrm{val}^{ \mathcal{G}}(v) = \bot$,
while in the other convention it is equivalent to $\textrm{val}^{ \mathcal{G}}(v) = \top$, where $\top$ is the greatest element in $Y$.

````

{prf:ref}`1-thm:kleene` states that $\textrm{val}^{ \mathcal{G}}$ is also the greatest post-fixed point.
Recall that a post-fixed point is $\mu$ such that $\mu \le  \mathbb{O}(\mu)$, which in this context we call a progress measure.
Expanding the definitions: for all vertices $v$, we have

$$
\begin{array}{llll}
\mu(v) & \le & \max  \left\{ \delta( \mu(v'),  \mathfrak{c \right\}(v)) : (v,v') \in E} & \text{ if } v \in  V_\mathrm{Eve}, \\
\mu(v) & \le & \min  \left\{ \delta( \mu(v'),  \mathfrak{c \right\}(v)) : (v,v') \in E} & \text{ if } v \in  V_\mathrm{Adam},
\end{array}
$$

which is equivalent to the more familiar definition of progress measures: for all vertices $v$, we have

$$
\begin{array}{llll}
\exists (v,v') \in E,\ & \mu(v) \le \delta( \mu(v'),  \mathfrak{c}(v)) & \text{ if } v \in  V_\mathrm{Eve}, \\
\forall (v,v') \in E,\ & \mu(v) \le \delta( \mu(v'),  \mathfrak{c}(v)) & \text{ if } v \in  V_\mathrm{Adam}.
\end{array}
$$

The characterisation principle can be equivalently stated as follows.

````{prf:property} Characterisation of the winning regions, equivalent formulation with progress measures
:label: 1-property:progress_measure

For all vertices $v$ we have Eve wins from $v$ if and only if there exists a progress measure $\mu$ such that $\mu(v) \neq \bot$.

````

The third information given by {prf:ref}`1-thm:kleene` is that $\textrm{val}^{ \mathcal{G}}$ is the limit of the sequence $( \mathbb{O}^k(\top))_{k \in  \mathbb{N}}$.

If $Y$ is a finite lattice then so is $F_V$, and the algorithm for computing $\textrm{val}^{ \mathcal{G}}$ is as follows:
we let $\textrm{val}_0$ defined by $\textrm{val}_0(v) = \top$ and then compute the sequence $( \textrm{val}_k)_{k \in  \mathbb{N}}$ defined by 
$\textrm{val}_{k+1} = \min( \mathbb{O}( \textrm{val}_k),  \textrm{val}_k)$.
There exists $k$ such that $\textrm{val}_{k+1} =  \textrm{val}_k$, at which point we have that $\textrm{val}_k =  \textrm{val}^{ \mathcal{G}}$,
from which we obtain the winning regions thanks to the characterisation principle.
A naive upper bound on $k$ is $|F_V| \le |Y|^n$, but usually a finer analysis of the algorithm yields better bounds on the number of iterations to reach the fixed point.

If $Y$ is not finite that the sequence $( \textrm{val}_k)_{k \in  \mathbb{N}}$ converges towards $\textrm{val}^{ \mathcal{G}}$ and further analysis is required to evaluate the convergence speed.

````{prf:remark} NEEDS TITLE AND LABEL 
It is sometimes useful to define instead of the operator $\mathbb{O}$ a set of operators $( \mathbb{O}_v)_{v \in V}$:

$$
 \mathbb{O}_v(\mu)(u) = 
\begin{cases}
\mu(v) & \text{ if } u \neq v, \\
\max  \left\{ \delta( \mu(v'),  \mathfrak{c \right\}(v)) : (v,v') \in E} & \text{ if } u = v \in  V_\mathrm{Eve}, \\
\min  \left\{ \delta( \mu(v'),  \mathfrak{c \right\}(v)) : (v,v') \in E} & \text{ if } u = v \in  V_\mathrm{Adam}.
\end{cases}
$$

The fixed points of $\mathbb{O}$ and of the set of operators $( \mathbb{O}_v)_{v \in V}$ are the same
and the ideas described above can be applied using {prf:ref}`1-thm:kleene_set_operators` instead of {prf:ref}`1-thm:kleene`.

It is sometimes useful to define instead of the operator $\mathbb{O}$ a set of operators $( \mathbb{O}_v)_{v \in V}$:

$$
 \mathbb{O}_v(\mu)(u) = 
\begin{cases}
\mu(v) & \text{ if } u \neq v, \\
\max  \left\{ \delta( \mu(v'),  \mathfrak{c \right\}(v)) : (v,v') \in E} & \text{ if } u = v \in  V_\mathrm{Eve}, \\
\min  \left\{ \delta( \mu(v'),  \mathfrak{c \right\}(v)) : (v,v') \in E} & \text{ if } u = v \in  V_\mathrm{Adam}.
\end{cases}
$$

The fixed points of $\mathbb{O}$ and of the set of operators $( \mathbb{O}_v)_{v \in V}$ are the same
and the ideas described above can be applied using {prf:ref}`1-thm:kleene_set_operators` instead of {prf:ref}`1-thm:kleene`.

````

