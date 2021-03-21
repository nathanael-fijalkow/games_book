(5-sec:discounted)=
# Discounted payoff in MDPs

```{math}

```

In this section, we consider MDPs with edges coloured by rational numbers 
and with the objective $\mathtt{DiscountedPayoff}$, defined in the same way as in 
{prf:ref}`chap:payoffs`. We start the chapter by proving that using the play-based semantics for the discounted-payoff objective yields no loss of generality.

````{prf:lemma} Equivalence of the definitions for discounted payoffs
:label: 5-lem:disc-step-one

In a discounted-payoff MDP, for each strategy $ \sigma $ and each vertex $ v $ it holds $  \textsf{p-Payoff}(v, \sigma) =  \textsf{s-Payoff}(v, \sigma) $.

````

````{admonition} Proof
:class: dropdown tip

We have 

$$
  \textsf{p-Payoff}(v,\sigma) &=  \mathbb{E}^\sigma_v[(1-\lambda)\lim_{k \rightarrow \infty} \sum_{i=0}^{k-1}\lambda^i  c( \pi_i) ] = (1-\lambda) \lim_{k \rightarrow \infty}  \mathbb{E}^\sigma_v[\sum_{i=0}^{k-1}\lambda^i  c( \pi_i) ] 
\\
&= (1-\lambda)\cdot\lim_{k \rightarrow \infty} \sum_{i=0}^{k-1}\lambda^i \mathbb{E}^\sigma_v[  c( \pi_i) ] =  \textsf{s-Payoff}(v, \sigma).

$$

Here, the last equality on the first line follows from the dominated convergence theorem (Theorem 1.6.9 in {cite}`Ash&Doleans-Dade:2000`) and the following equality comes from the linearity of expectation. (To apply the dom. convergence 
theorem, we use the fact that for each 
$k$ we have $\mathtt{DiscountedPayoff}^{k}( \pi)\leq  \max_{ c}.
$)

````

## Optimal values and memoryless optimality

 In this subsection we give a 
characterization of the value vector $\textrm{val}( \mathcal{M})$ and prove that there always exists a 
memoryless deterministic strategy that is optimal in every vertex. Our 
exposition follows (in a condensed form) the one in {cite}`Puterman:2005`, the techniques 
being somewhat similar to the ones in the previous chapter.

We define an operator $\mathcal{D}\colon 
 \mathbb{R}^{ V}\rightarrow  \mathbb{R}^{ V}$ as follows: each vector $\vec{x}$ is mapped to a vector 
$\vec{y} =  \mathcal{D}(\vec{x})$ such that:

$$

\vec{y}_v = \max_{a \in  A} \sum_{u\in  V}  \Delta(u\mid 
v,a) 
\cdot\left((1-\lambda)\cdot c(v,u) + \lambda\cdot \vec{x}_u \right).

$$

````{prf:lemma} NEEDS TITLE 5-lem:fixpoint
:label: 5-lem:fixpoint

The operator $\mathcal{D}$ is a contraction mapping. Hence, $\mathcal{D}$ has a unique 
fixed point $\vec{x}^*$ in $\mathbb{R}^{ V}$, and $\vec{x}^* = 
\lim_{k\rightarrow \infty}  \mathcal{D}^k(\vec{x})$, for any 
$\vec{x}\in \mathbb{R}^{ V}$.

````

````{admonition} Proof
:class: dropdown tip

The proof proceeds by a computation analogous to the one in the first half of 
the proof of {prf:ref}`4-thm:discounted`; we just need to reason about actions 
rather than edges (and of course, use the formula defining $\mathcal{D}$ instead of 
the one for games). The second part follows from the Banach fixed point theorem.

````

We aim to prove that $\textrm{val}( \mathcal{M})$ is the unique fixed point $\vec{x}^*$ of 
$\mathcal{D}$. We start with an auxiliary definition.

````{prf:definition} NEEDS TITLE 5-def:disc-safe-act
:label: 5-def:disc-safe-act

Let $\vec{x}\in  \mathbb{R}^{ V}$. We say that an action $a$ is $\vec{x}$-safe in 
a vertex $v$ if

$$

a= \underset{a' \in  A}{\arg\max} \sum_{u\in  V} 
 \Delta(u\mid 
v,a') 
\cdot\left((1-\lambda)\cdot c(v,u) + \lambda\cdot \vec{x}_u \right).
$$ (5-eq:disc-safe-act)

A strategy $\sigma$ is $\vec{x}$-safe, if for 
each play $  \pi $ ending in a vertex $v$, all actions that are selected with a positive 
probability by $\sigma$ for $\pi$ are $\vec{x}$-safe in $v$.

````

Given a strategy $\sigma$ we define $\vec{x}^{\sigma}$ to be the vector such that $\vec{x}_{v}^\sigma = 
 \textsf{p-Payoff}(v,\sigma)$. For memoryless strategies, $\vec{x}^{\sigma}$ can be computed efficiently as follows:
Each memoryless strategy $\sigma$ defines a **linear** operator $\mathcal{D}_{\sigma}$ which maps each vector 
$\vec{x}\in  \mathbb{R}^{ V}$ to a vector $\vec{y}= \mathcal{D}_{\sigma}(\vec{x})$ 
such that 

$$

\vec{y}_v = \sum_{a\in  A} \sigma(a\mid v) \cdot 
\left(\sum_{u \in  V} 
 \Delta(u \mid v,a) \cdot( (1-\lambda)\cdot  c(u,v) + 
\lambda \cdot \vec{x}_u )\right).

$$

````{prf:lemma} NEEDS TITLE 5-lem:disc-val-sigma
:label: 5-lem:disc-val-sigma

Let $\sigma$ be a memoryless strategy using rational probabilities. Then the operator $\mathcal{D}_{\sigma}$ has a unique fixed point, which is equal to $\vec{x}^{\sigma}$ and which can be computed in polynomial time.

````

````{admonition} Proof
:class: dropdown tip

The operator $\mathcal{D}_{\sigma}$ can be seen as an instantiation of $\mathcal{D}$ in an MDP where there is no choice, since the action probabilities are chosen according to $\sigma$. {prf:ref}`5-lem:fixpoint` shows that 
$\vec{x}^\sigma$ is a fixed-point of $\mathcal{D}^\sigma$. Since $\mathcal{D}_{\sigma}$ is again a contraction, it has a unique fixed point; and since it is linear, the fixed point can be computed in polynomial time, e.g. by Gaussian elimination (in its polynomial bit-complexity variant known as Bareiss algorithm {cite}`Bareiss:1968`).

````

We now prove that there is a memoryless strategy ensuring outcome given by the fixed point of $\mathcal{D}$. Hence, the fixed point gives a lower bound on the values of vertices.

````{prf:lemma} NEEDS TITLE 5-lem:disc-val-lower
:label: 5-lem:disc-val-lower

Let $\vec{x}^*$ be the unique fixed point of $\mathcal{D}$. 
Then there exists an MD strategy that is $\vec{x}^*$-safe. Moreover, for each $\vec{x}^*$-safe memoryless strategy it holds that  
$\textsf{p-Payoff}(v,\sigma) =\vec{x}_v^*$ for each $v\in  V$.

````

````{admonition} Proof
:class: dropdown tip

 Note that for each $\vec{x}\in  \mathbb{R}^{ V}$ and each $v\in 
 V$ there always exists at least one action that is $\vec{x}$-safe in 
$v$. Hence, there is a memoryless deterministic strategy which 
in each $v$ chooses an arbitrary (but fixed) action that is $\vec{x}^*$-safe in 
$v$. 

Now let $ \sigma $ be an arbitrary $\vec{x}^*$-safe memoryless strategy.
By {prf:ref}`5-lem:disc-val-sigma`, the vector $\vec{x}^{\sigma}$ is the unique fixed point of $\mathcal{D}^\sigma$.
 But since $\sigma$ 
is $\vec{x}^*$-safe, $\vec{x^*}$ is also a fixed point of $\mathcal{D}^\sigma$. 
Hence, $\vec{x}^* = \vec{x}^\sigma$.

````

It remains to prove that $\vec{x}^*$ gives, for each vertex, an upper 
bound on the expected discounted payoff achievable by any strategy from that 
vertex. We introduce some additional notation to be used in the proof of the 
next lemma, as well as in some later results: namely, we denote by 
$\mathtt{DiscountedPayoff}^{\;(k)}( \pi)$ the 
discounted 
payoff accumulated during the first $k$ steps of $\pi$, i.e. the number 
$(1-\lambda)\sum_{i=0}^{k-1} \lambda^i
\,  c( \pi_i)$. The following lemma can be proved by an easy induction.

````{prf:lemma} NEEDS TITLE 5-lem:disc-iterates
:label: 5-lem:disc-iterates

For each $k\geq 0$ and each vertex $v$ we have

$$

\sup_{\sigma} \mathbb{E}^{\sigma}_{v}[  \mathtt{DiscountedPayoff}^{\;(k)}] = 
( \mathcal{D}^k(\vec{0}))_v

$$

(here $\vec{0}$ is a $| V|$-dimensional vector of zeroes).

````

The previous lemma is used to prove the required upper bound on $\textrm{val}(v)$.

````{prf:lemma} NEEDS TITLE 5-lem:disc-val-upper
:label: 5-lem:disc-val-upper

For each vertex $v$ it holds 
$\textrm{val}(v)\leq \vec{x}^*_v$, where $\vec{x}^*$ is the 
unique fixed point of $\mathcal{D}$.

````

````{admonition} Proof
:class: dropdown tip

We have $\mathtt{DiscountedPayoff}( \pi) = \lim_{k\rightarrow 
\infty}  \mathtt{DiscountedPayoff}^{\;(k)}( \pi)$ (for each $\pi$) and hence, by 
dominated 
convergence theorem we have $\mathbb{E}^\sigma_v[ \mathtt{DiscountedPayoff}] = 
\lim_{k\rightarrow 
\infty} \mathbb{E}^\sigma_v[  \mathtt{DiscountedPayoff}^{\;(k)}]$. 

Hence,

$$

 \textrm{val}(v) &= \sup_{\sigma} \mathbb{E}^\sigma_v[ \mathtt{DiscountedPayoff}] \nonumber\\
&= \sup_{\sigma}\lim_{k\rightarrow \infty} \mathbb{E}^\sigma_v[  \mathtt{DiscountedPayoff}^{\;(k)}]

$$ (5-eq:disc-safe-act)

It remains to prove that the RHS of {eq}`5-eq:disc-limit-transition` is not 
greater than $\vec{x}^*= \lim_{k\rightarrow 
\infty} \mathcal{D}^k(\vec{0})=\lim_{k\rightarrow \infty} 
\sup_{\sigma} \mathbb{E}^\sigma_v[  \mathtt{DiscountedPayoff}^{\;(k)}]$ (the last inequality follows 
by {prf:ref}`5-lem:disc-iterates`). It suffices to 
show that for each $\sigma'$ we have $\lim_{k\rightarrow 
\infty} \mathbb{E}^{\sigma'}_v  \mathtt{DiscountedPayoff}^{\;(k)}] \leq \lim_{k\rightarrow 
\infty}\sup_{\sigma} \mathbb{E}^\sigma_v[  \mathtt{DiscountedPayoff}^{\;(k)}]$. But this immediately 
follows from the fact that the inequality holds for each concrete $k$.

````

The following theorem summarizes the results.

````{prf:theorem} NEEDS TITLE 5-thm:disc-val-char-mem
:label: 5-thm:disc-val-char-mem

The vector of values $\textrm{val}( \mathcal{M})$ in a discounted sum MDP $\mathcal{M}$ is the 
unique fixed point $\vec{x}^*$ of the operator $\mathcal{D}$. Moreover, there 
exists a 
memoryless deterministic strategy that is optimal in every vertex.

````

````{admonition} Proof
:class: dropdown tip

The characterization of $\textrm{val}( \mathcal{M})$ follows directly from 
Lemmas {prf:ref}`5-lem:disc-val-lower` and {prf:ref}`5-lem:disc-val-upper`. The MD 
optimality follows from {prf:ref}`5-lem:disc-val-lower`.

````

In the rest of this section we discuss several algorithms for computing the 
values and optimal strategies in discounted-payoff MDPs.

## Value iteration

The value iteration algorithm works in the same way as in the case of 
discounted-payoff games: we simply iterate the operator $\mathcal{D}$ on the 
initial argument $\vec{0}$. We know that $\textrm{val}( \mathcal{M})=\lim_{k\rightarrow 
\infty} \mathcal{D}^k(\vec{0})$, and hence, iterating $\mathcal{D}$ yields an 
approximation of $\textrm{val}( \mathcal{M})$. The iteration might not reached the fixed 
point (i.e. $\textrm{val}( \mathcal{M})$) in a finite number of steps, but we can provide 
simple bounds on the precision of the approximation.

````{prf:lemma} NEEDS TITLE 5-lem:disc-val-it-convergence
:label: 5-lem:disc-val-it-convergence

For each $k\in  \mathbb{N}$, $|| \textrm{val}( \mathcal{M})- \mathcal{D}^k(\vec{0}) ||_{\infty} \leq 
\lambda^k \cdot  \max_{ c}$. (Recall that $\max_{ c}=\max_{e\in 
 E}| c(e)|$).

````

````{admonition} Proof
:class: dropdown tip

This follows immediately from {prf:ref}`5-lem:disc-iterates` and from the fact that 
for each play $\pi$, $\sum_{i=k}^{\infty}\lambda^i\cdot 
 c( \pi_i)\leq \frac{1}{1-\lambda}\cdot\lambda^k \cdot  \max_{ c}$.

````

Similar analysis can be applied to strategies induced by the approximate 
vectors.

````{prf:lemma} NEEDS TITLE 5-lem:disc-val-it-eps-strategies
:label: 5-lem:disc-val-it-eps-strategies

Let $\varepsilon>0$ be arbitrary and let

$$

k( \varepsilon)=\left\lceil\frac{\log_2\left(\frac{ \varepsilon(1-\lambda)}{4 \max_{ c}}\right)}{\log_2(\lambda)}
 \right\rceil .

$$

 Then, every 
$\mathcal{D}^{k( \varepsilon)}(\vec{0})$-safe memoryless strategy is $\varepsilon$-optimal in 
every vertex.

````

````{admonition} Proof
:class: dropdown tip

Let $\sigma$ be any $\mathcal{D}^{k( \varepsilon)}(\vec{0})$-safe memoryless strategy and 
let $\mathcal{D}_{\sigma}$ be the corresponding operator. We have that

$$

|| \textrm{val}( \mathcal{M}) -  \vec{x}^{\sigma} ||_{\infty} &= || \textrm{val}( \mathcal{M}) 
- \mathcal{D}^{k( \varepsilon)}(\vec{0}) + \mathcal{D}^{k( \varepsilon)}(\vec{0}) -  \vec{x}^{\sigma} 
||_{\infty} \nonumber
\\
&\leq || \textrm{val}( \mathcal{M}) - \mathcal{D}^{k( \varepsilon)}(\vec{0}) 
||_{\infty} + ||  \mathcal{D}^{k( \varepsilon)}(\vec{0}) -  \vec{x}^{\sigma}
||_{\infty}. 

$$ (5-eq:disc-safe-act)

The first term in {eq}`5-eq:disc-val-it-bound` is $\leq  \varepsilon/2$ 
by the choice of $k( \varepsilon)$ and {prf:ref}`5-lem:disc-val-it-convergence`. We prove 
that the second term 
in {eq}`5-eq:disc-val-it-bound` is also bounded by $\varepsilon/2$. Note that we 
have $\vec{x}^{\sigma}= \mathcal{D}_{\sigma}( \vec{x}^{\sigma})$ (as was already proved 
in  {prf:ref}`5-lem:disc-val-lower`) and $\mathcal{D}( \mathcal{D}^{k( \varepsilon)}(\vec{0})) = 
 \mathcal{D}_\sigma( \mathcal{D}^{k( \varepsilon)}(\vec{0}))$ (since $\sigma$ is 
$\mathcal{D}^{k( \varepsilon)}(\vec{0})$-safe). Using this we get

$$

||  \mathcal{D}^{k( \varepsilon)}(\vec{0}) -  \vec{x}^{\sigma}
||_{\infty} & = ||  \mathcal{D}^{k( \varepsilon)}(\vec{0}) - \mathcal{D}^{k( \varepsilon)+1}(\vec{0}) + 
 \mathcal{D}^{k( \varepsilon)+1}(\vec{0}) -  \vec{x}^{\sigma}
||_{\infty}\\
&\leq ||  \mathcal{D}^{k( \varepsilon)}(\vec{0}) - \mathcal{D}^{k( \varepsilon)+1}(\vec{0}) ||_{\infty} + 
|| \mathcal{D}^{k( \varepsilon)+1}(\vec{0}) -  \vec{x}^{\sigma}
||_{\infty}
\\
&=||  \mathcal{D}^{k( \varepsilon)}(\vec{0}) - \mathcal{D}^{k( \varepsilon)+1}(\vec{0}) ||_{\infty} + 
|| \mathcal{D}_\sigma( \mathcal{D}^{k( \varepsilon)}(\vec{0})) - 
 \mathcal{D}_\sigma( \vec{x}^{\sigma})||_{\infty}\\

&\leq ||  \mathcal{D}^{k( \varepsilon)}(\vec{0}) - \mathcal{D}^{k( \varepsilon)+1}(\vec{0}) ||_{\infty} + 
\lambda\cdot||( \mathcal{D}^{k( \varepsilon)}(\vec{0})) - 
 \vec{x}^{\sigma}||_{\infty}

$$

Re-arranging yields $||  \mathcal{D}^{k( \varepsilon)}(\vec{0}) -  \vec{x}^{\sigma}
||_{\infty} \leq \frac{1}{1-\lambda}\cdot|| 
 \mathcal{D}^{k( \varepsilon)}(\vec{0}) - 
 \mathcal{D}^{k( \varepsilon)+1}
||_{\infty} $.
It follows from {prf:ref}`5-lem:disc-val-it-convergence`  that 
$|| \mathcal{D}^{k( \varepsilon)}(\vec{0}) - \mathcal{D}^{k( \varepsilon)+1}(\vec{0}) ||_{\infty} 
\leq 2\cdot\lambda^{k( \varepsilon)}\cdot \max| c|\leq 
\frac{(1-\lambda) \varepsilon}{2}$, the last 
inequality holding by the choice of $k( \varepsilon)$. Plugging this into the 
formula above yields $||  \mathcal{D}^{k( \varepsilon)}(\vec{0}) -  \vec{x}^{\sigma}
||_{\infty} \leq\frac{ \varepsilon}{2}$, as required.

````

Using a value-gap result 
(similar to the game case, but proved using a different technique), one can 
show that sufficiently precise iterates can be used to computate an **optimal** strategy. 
This is summarized in the following lemma due to {cite}`Tseng:1990`.

````{prf:lemma} NEEDS TITLE 5-lem:disc-vi-optimal-strategy
:label: 5-lem:disc-vi-optimal-strategy

Let $d$ be the least common multiple of denominators of the following numbers: $\lambda$, all   
transition probabilities, and all edge colourings in $\mathcal{M}$. Next, let $\varepsilon^* = 
\frac{1}{d^{(3| V|+3)}\cdot | V|^{\frac{ V}{2}}}$.
Then, any $\mathcal{D}^{k( \varepsilon^*)}(\vec{0})$-safe memoryless deterministic strategy 
is 
optimal in every 
vertex.

````

````{admonition} Proof
:class: dropdown tip

 Let $\sigma^*$ be any MD optimal strategy (it is guaranteed 
to exist by {prf:ref}`5-thm:disc-val-char-mem`). By the same theorem, we have that 
$\textrm{val}( \mathcal{M})= \mathcal{D}^{\sigma}( \textrm{val}( \mathcal{M}))$. By the definition of 
$\mathcal{D}^{\sigma}$, we can write the above equation as $\textrm{val}( \mathcal{M})= 
(1-\lambda)\cdot \vec{c}+\lambda \cdot P\cdot  \textrm{val}( \mathcal{M})$, where $\vec{c}$ is 
a vector whose each 
component 
is a 
sum of several terms, each term being a product of an edge colour and of a 
transition probability; and $P$ is a matrix containing 
transition 
probabilities. Multiplying the equation by $d^3$ yields $d^3 \textrm{val}( \mathcal{M})= 
d^3(1-\lambda)\cdot \vec{c}+d^3\lambda \cdot P\cdot  \textrm{val}( \mathcal{M})$. Since this equation has a unique fixed point (due to 
$\mathcal{D}^\sigma$ being a contraction), the matrix $A = d^3(I - \lambda P)$ (where $ I $ is the unit matrix) is 
regular, and moreover, composed of integers (ue to the choice of $ d $). By Cramer's rule, each entry of $\textrm{val}( \mathcal{M})$ is equal to 
$\det(B)/\det(A)$, where $B$ is a matrix obtained by replacing some column of 
$A$ with $d^3(1-\lambda)\vec{c}$ (which is again an integer vector, due to the multiplication by $ d^3 $). Hence, each entry of $\textrm{val}( \mathcal{M})$ is a rational number with denominator $\det(A)$. Hadamard's inequality {cite}`Garling:07` implies $|\det(A)|\leq d^{3| V|}{| V|}^{\frac{| V|}{2}}$.

Now let $\sigma$ be any $\mathcal{D}^{k( \varepsilon^*)}(\vec{0})$-safe MD strategy. By {prf:ref}`5-lem:disc-val-it-eps-strategies`, $\sigma$ is $\varepsilon^*$-optimal. We prove that all actions used by $\sigma$ are $\vec{x}^*$-safe, which means that $\sigma$ is optimal by {prf:ref}`5-lem:disc-val-lower`. Assume that in some vertex $v$ the strategy $\sigma$ uses action $a$ that is not $\vec{x}^*$-safe. Denote $\vec{y}= \mathcal{D}_\sigma(\vec{x}^*)$. We have $ |\vec{y}_v - \vec{x}^*_v| > 0 $, since otherwise $a$ would be $\vec{x}^*$-safe. But then we can obtain a lower bound on the difference by investigating the bitsize of the numbers involved:

$$

|\vec{y}_v - \vec{x}^*_v| &= \left|\frac{d^3}{d^3}\vec{y}_v - \frac{d^3}{d^3}\vec{x}^*_v\right|
\\
&=\frac{1}{d^3}\left|\sum_{u \in  V} 
\underbrace{d\cdot \Delta(u \mid v,a)}_{\text{integer}} \cdot( \underbrace{d^2(1-\lambda)\cdot  c(u,v)}_{\text{integer}} + 
\underbrace{d^2\cdot\lambda \cdot \vec{x}^*_u ) - d^3\vec{x}^*}_{\text{int. multiples of $1/\det(A)$}}\right| \\
&\geq \frac{1}{d^3\cdot \det(A)}\geq \frac{1}{d^{(3| V|+3)}\cdot{| V|}^{\frac{| V|}{2}}}.

$$

Now put $\vec{z}= \mathcal{D}_\sigma( \mathcal{D}^{k( \varepsilon)}(\vec{0}))$. We have the following (using, on the first line, the fact that $|a+b| \geq |a|-|b|$):

$$

|\vec{z}_v - \vec{x}^*_v| &=
 |\vec{z}_v- \mathcal{D}_\sigma(\vec{x}^*)_v+ \mathcal{D}_\sigma(\vec{x}^*)_v-\vec{x}^*_v | 
\geq | \mathcal{D}_\sigma(\vec{x}^*)_v-\vec{x}^*_v | - |\vec{z}_v- \mathcal{D}_\sigma(\vec{x}^*)_v |  \\
&\geq \frac{1}{d^{(3| V|+3)}\cdot | V|^{\frac{| V|}{2}}} - | \mathcal{D}_\sigma( \mathcal{D}^{k( \varepsilon)}(\vec{0}))_v- \mathcal{D}_\sigma(\vec{x}^*)_v |\quad (\text{as shown above})\\
&\geq \frac{1}{d^{(3| V|+3)}\cdot | V|^{\frac{| V|}{2}}} - | \mathcal{D}_{\sigma}( \mathcal{D}^{k( \varepsilon^*)}(\vec{0}) - \vec{x}^*)_v|  \quad (\text{since $\mathcal{D}_{\sigma}$ is linear})\\
&\geq  \varepsilon^* - \lambda\cdot|| \mathcal{D}^{k( \varepsilon^*)}(\vec{0}) - \vec{x}^* ||_{\infty}
>  \varepsilon^* - \frac{ \varepsilon^*}{2}  \quad (\text{{prf:ref}`5-lem:disc-val-it-convergence`})\\&=\frac{ \varepsilon^*}{2}.

$$

In particular, it must hold that $\vec{z}_v< \vec{x}^*_v$. Otherwise we would have $\mathcal{D}^{k( \varepsilon^*)+1}(\vec{0})_v \geq  \mathcal{D}_{\sigma}( \mathcal{D}^{k( \varepsilon^*)}(\vec{0}))_v \geq \vec{x^*}_v + \frac{ \varepsilon^*}{2} $, a contradiction with $\mathcal{D}^{k( \varepsilon^*)+1}(\vec{0})$ being an $\frac{ \varepsilon^*}{4}$-ap\-prox\-imation of $\vec{x}^*$ (by {prf:ref}`5-lem:disc-val-it-convergence` and the choice of $k( \varepsilon^*)$).

At the same time, $| \mathcal{D}( \mathcal{D}^{k( \varepsilon^*)}(\vec{0}))_v - \vec{x}^*|\leq \frac{ \varepsilon^*}{4}$, due to the choice of $k( \varepsilon^*)$. Since $\vec{z}_v \leq \vec{x}_v^*$, we get $\vec{z}_v < \vec{x}_v^* - \frac{ \varepsilon}{2} \leq  \mathcal{D}( \mathcal{D}^{k( \varepsilon^*)}(\vec{0}))_v$, a contradiction with $\sigma$ being $\mathcal{D}^{k( \varepsilon^*)}(\vec{0})$-safe. 

````

````{prf:corollary} NEEDS TITLE 5-cor:VI-optimal-strategy-comp
:label: 5-cor:VI-optimal-strategy-comp

An optimal MD strategy in discounted-payoff MDPs with a fixed discount factor can be computed in polynomial time. 

````

````{admonition} Proof
:class: dropdown tip

The number $1/ \varepsilon^*$, where $\varepsilon^*$ is from {prf:ref}`5-lem:disc-vi-optimal-strategy`, has bitsize polynomial in the size of the MDP when the discount factor is fixed. Hence, the number $k( \varepsilon^*)$ defined as in {prf:ref}`5-lem:disc-val-it-eps-strategies` has a polynomial magnitude, so it suffices to perform only polynomially many iterations. Since each iteration requires polynomially many arithmetic operations that involve only summation and multiplication by a constant, the result follows.

````

## Strategy improvement, linear programming, and (strongly) polynomial time

The strategy (or policy) improvement (also called strategy/policy iteration in the literature) for MDPs works similarly as for games, see {numref}`5-algo:disc-strategy-improvement`. In the algorithm, we use $\mathcal{D}_{a,v}(\vec{x})$ as a shortcut for $ \sum_{u \in  V} \Delta(u\mid v,a)\left((1-\lambda)\cdot c(v,u) + \lambda\cdot \vec{x}_u \right)$

```{figure} ./../FigAndAlgos/5-algo:disc-strategy-improvement.png
:name: 5-algo:disc-strategy-improvement
:align: center
An algorithm computing an optimal MD strategy in a discounted MDP
```

````{prf:theorem} NEEDS TITLE 5-thm:disc-strat-it
:label: 5-thm:disc-strat-it

The strategy improvement algorithm for discounted MDPs terminates in a finite (and at most exponential) number of steps and returns an optimal MD strategy.

````

````{admonition} Proof
:class: dropdown tip

First we need to show that whenever $\sigma_{i+1}\neq \sigma_i$, then  $\vec{x}^{\sigma_{i+1}} \geq \vec{x}^{\sigma_i}$ and $\vec{x}^{\sigma_{i+1}} \neq \vec{x}^{\sigma_i}$ (we write this by $\vec{x}^{\sigma_{i+1}} \succ\vec{x}^{\sigma_i}$). So fix some $ i $ s.t. an improvement is performed in the $ i $-th iteration of the repeat-loop. We have $\mathcal{D}_{\sigma_{i+1}}(\vec{x}^{\sigma_i})\succ \mathcal{D}_{\sigma_{i}}(\vec{x}^{\sigma_i})= \vec{x}^{\sigma_i}$, i.e. $\mathcal{D}_{\sigma_{i+1}}(\vec{x}^{\sigma_i})-\vec{x}^{\sigma_i} \succ 0$. Let $P$, $\vec{c}$ be the matrix and vector such that the equation $\vec{x}= \mathcal{D}_{\sigma_{i+1}}(\vec{x})$ can be written as $\vec{x}= (1-\lambda)\cdot \vec{c}+\lambda \cdot P\cdot\vec{x}$. Since the equation $\vec{x}= \mathcal{D}_{\sigma_{i+1}}(\vec{x})$ has a unique fixed point (as $  \mathcal{D}_{\sigma_{i+1}} $ is a contraction), the matrix $ I-\lambda P $ is invertible. Then $\mathcal{D}_{\sigma_{i+1}}(\vec{x}^{\sigma_i})-\vec{x}^{\sigma_i} \succ 0$ can be written as  $(1-\lambda)\vec{c} + (\lambda P - I)\vec{x}^{\sigma_i} \succ 0 $, or equivalently $\vec{x}^{\sigma_i}\prec (1-\lambda)\vec{c}\cdot(I-\lambda P)^{-1}.$ But the RHS of this inequality is equal to the fixed point of $\mathcal{D}_{\sigma_{i+1}}$, i.e. to $\vec{x}^{\sigma_{i+1}} .$

Now there are only finitely (exponentially) many MD strategies and since$\vec{x}^{\sigma_{i+1}} \succ\vec{x}^{\sigma_i}$, we have that no strategy is considered twice. Hence, the algorithm eventually terminates. Upon termination, there is no improving action, so the algorithm has found a strategy $\sigma$ whose value vector $\vec{x}^{\sigma}$ is the fixed point of $\mathcal{D}$. Such a strategy is optimal by {prf:ref}`5-thm:disc-val-char-mem`. 

````

While each of the steps (1.)--(4.) can be performed in polynomial time, the 
worst-case number of iterations is exponential {cite}`Hollanders&Delvenne&Jungers:2012`. However, the 
algorithm has nice properties in the case when the discount factor is fixed, as we'll see below. It is also intimately connected to the linear programming approach.

We can indeed aim to directly solve 
the equation $\vec{x} =  \mathcal{D}(\vec{x})$, thus obtaining the fixed point of 
$\mathcal{D}$, by using a suitable LP. While the operator $\mathcal{D}$ is not 
in itself linear, solving the equation can be encoded into a linear  program. 
The main idea can be described as follows: given some numbers $y,z$, the 
solution $\bar{x}$ to the equation $x=\max\{y,z\}$ is exactly the smallest 
solution to the set of inequalities $x\geq y$, $x\geq z$. Hence, to solve the 
equation  $\vec{x} =  \mathcal{D}(\vec{x})$, we set up the following linear program 
$\mathcal{L}_{\mathit{disc}}$:

```{figure} ./../FigAndAlgos/5-fig:disc-lp.png
:name: 5-fig:disc-lp
:align: center
The linear program $\mathcal{L}_{\mathit{disc}}$ with variables $x_v$, $v\in  V$.
```

````{prf:lemma} NEEDS TITLE 5-lem:disc-lp
:label: 5-lem:disc-lp

The linear program $\mathcal{L}_{\mathit{disc}}$ has a unique optimal solution 
$\bar{\vec{x}}$ that satisfies $\bar{\vec{x}} =  \textrm{val}( \mathcal{M})$.

````

````{admonition} Proof
:class: dropdown tip

Let $\vec{x}^* =  \textrm{val}( \mathcal{M})$ be the unique fixed point of $\mathcal{D}$. Clearly 
setting $x_v = \vec{x}^*_v$ yields a feasible solution of $\mathcal{L}_{\mathit{disc}}$. 
We show 
that $\vec{x}^*$ is actually an optimal solution, by proving that for each 
feasible solution $\vec{x}$ it holds $\vec{x} \geq \vec{x}^*$. (This also 
shows 
the uniqueness, since it says that an optimal solution is the infimum of the 
set of 
all feasible solutions.) First, note that for any feasible solution $\vec{x}$ 
it holds $\mathcal{D}(\vec{x})\leq \vec{x}$, by the construction of $\mathcal{L}_{\mathit{disc}}$. 
Next, if $\vec{x}$ is a feasible solution, then $\mathcal{D}(\vec{x})$ is also a 
feasible solution; otherwise, there would be some $v$ and $a\in  A$ 
such that 

$$
 \mathcal{D}(\vec{x})_v &< \sum_{u\in  V}  \Delta(u\mid 
v,a)\cdot\left((1-\lambda)\cdot  c(v,u) + \lambda\cdot 
 \mathcal{D}(\vec{x})_u \right) \\ &\leq \sum_{u\in  V}  \Delta(u\mid 
v,a)\cdot\left((1-\lambda)\cdot  c(v,u) + \lambda\cdot \vec{x}_u 
\right) \leq  \mathcal{D}(\vec{x})_v.

$$

Here, the first inequality on the second line follows from 
$\mathcal{D}(\vec{x})\leq \vec{x}$, while the second inequality follows from the 
definition of $\mathcal{D}$. But $\mathcal{D}(\vec{x})_v <  \mathcal{D}(\vec{x})_v$ is an 
obvious contradiction. So $\mathcal{D}(\vec{x})$ is indeed a feasible solution and 
by applying the argument above, we get $\mathcal{D}^2(\vec{x}) \leq 
 \mathcal{D}(\vec{x})$. By a simple induction, $\mathcal{D}^{i+1}(\vec{x})\leq 
 \mathcal{D}^{i}(\vec{x})\leq \vec{x}$ for each $i\geq 0.$ Hence, also $\vec{x}^* = 
\lim_{i\rightarrow \infty}  \mathcal{D}^i(\vec{x}) \leq \vec{x}$ (the first equality 
comes from {prf:ref}`5-lem:fixpoint`).

````

It is known that linear programming can be solved in polynomial time by 
interior-point techniques {cite}`Khachiyan:1979,Karmarkar:1984`. Hence, we get the following.

````{prf:theorem} NEEDS TITLE 5-thm:disc-polytime-lp
:label: 5-thm:disc-polytime-lp

The following holds for discounted-payoff MDPs:

1.  The value of each vertex as well as an MD optimal 
strategy can be computed in polynomial time. 
2.  The problem whether the value of a given vertex $v$ is at least a given constant 
(say 1) is \P-complete (under logspace reductions). The hardness result holds 
even for a fixed discount factor.

````

````{admonition} Proof
:class: dropdown tip
(1.)
The first part comes directly from {prf:ref}`5-lem:disc-lp`. Once the optimal value 
vector $\textrm{val}( \mathcal{M})$ is computed, we can choose any $\textrm{val}( \mathcal{M})$-safe MD 
strategy as the optimal one 
({prf:ref}`5-lem:disc-val-lower`).

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
in the reachability MDP. If the reachability MDP $\mathcal{M}$ does not have the 
``uniform 
path length'' property, we modify it by producing $| V|$ copies of 
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
algorithm of Dantzig solves $\mathcal{L}_{\mathit{disc}}$ in a strongly 
polynomial time in MDPs with a fixed discount factor. Formally, Ye proved that 
the number of iterations taken by the simplex method is bounded by 
$\frac{| V|^2\cdot (| A|-1)}{1-\lambda}\cdot 
\log(\frac{| V|^2}{1-\lambda})$, with each iteration requiring  
$\mathcal{O}(| V|^2\cdot | A|)$ arithmetic operations. This has 
also an impact on the strategy improvement method: it can be shown that strategy 
improvement in discounted MDPs is really just a `re-implementation' of the 
simplex algorithm using a different syntax. Hence, the strongly polynomial 
complexity bound for a fixed discount factor holds there as well.

````{prf:theorem} NEEDS TITLE AND LABEL 
For MDPs with a fixed discount factor, the value of each vertex as well as an 
optimal MD strategy can be computed in a strongly polynomial time.

For MDPs with a fixed discount factor, the value of each vertex as well as an 
optimal MD strategy can be computed in a strongly polynomial time.

````

