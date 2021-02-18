(7-sec:discounted)=
# Concurrent discounted games


```{math}
\newcommand{\ValueOp}{\text{valOp}}
\newcommand{\dest}{\Delta}
\newcommand{\PTIME}{\textrm{PTIME}}
```

In this section we focus on concurrent discounted games. 
The key property of these games is that to a high degree, only the relative early part of the play matters.
We will first argue that the value iteration algorithm works and especially converges to the value of the game and then that there are stationary optimal strategies in concurrent discounted games.
While the value iteration algorithm also works for the games considered in the latter sections, we will not explicitly show it there, since the proofs become much more complex. The argument here however will allow us to show quite a few more statements in essence as corollaries of the theorem that value iteration works.

The value iteration algorithm is based on the concept of finite-horizon (or time limited) games. It is also sometimes referred to as dynamic programming.
Specifically, apart from the usual definition of a game, there is an additional integer $T$, denoting how many rounds are remaining initially, and a vector $v$, assigning a reward to each node if the game ends in that node with 0 rounds remaining. After round $T$ the reward is 0. 
I.e. for $T=0$, the outcome reward from node $x$ is $v_x$ in the first round and 0 in each later round.
Let $\text{valOp}T(v)$ be the vector that assigns to each node its value in the game with time-limit $T$ with vector $v$.

In general this formulation leads to a simple dynamic algorithm that computes $\text{valOp}T(v)$ inductively in $T$. 
We have that $\text{valOp}0(v)=v$ and given $\text{valOp}{T-1}(v)$ it is easy to compute $\text{valOp}T(v)$ because, if Eve selects row $i$ and Adam column $j$ in node $x$ in the first round, the outcome is 

$$
\sum_{v\in V}\text{valOp}{T-1}(v)\Deltax,i,j)(v)
$$

and thus $(\text{valOp}T(v))_x$ is the value of the matrix $M^{T,x,v}$, where entry $i,j$ is 

$$
\sum_{v\in V}\text{valOp}{T-1}(v)\Deltax,i,j)(v)
$$


It is common to start with the all-0 vector for $v$ when using the value iteration algorithm.

The following lemma shows many interesting properties of concurrent discounted games.





````{prf:lemma} NEEDS TITLE cor:long
:label: cor:long

Concurrent discounted games have the following properties:

*  The value iteration algorithm converges for any initial vector $v$
*  The value iteration algorithm has an unique fix-point, independent of the initial vector $v$.
*  There are optimal stationary strategies in concurrent discounted games and the unique fix-point of the value iteration algorithm is the value (thus, the games are determined)
*  The value of a concurrent discounted game can approximated in PPAD
*  There are $\epsilon$-optimal stationary strategies with patience below $\frac{m\log(\epsilon/2)}{\log(1-\gamma)\epsilon}$.

````

````{admonition} Proof
:class: dropdown tip

The first item comes from considering the vectors $v$ and $\text{valOp}1(v)$. We thus have that $\text{valOp}{T+1}(v)\in [\text{valOp}{T}(v)-(1-\gamma)^T,\text{valOp}{T}(v)+(1-\gamma)^T]$ for all $T$. The statement then comes from that $\sum_{i=1}^\infty (1-\gamma)^i$ is a converging sum.

The second item comes from considering two fix-points, $u,v$. I.e., $\text{valOp}1(v)=v$ and thus $\text{valOp}T(v)=v$ for all $T$. Similar for $u$.
But, $v=\text{valOp}T(v)\in [\text{valOp}T(u)-(1-\gamma)^T, \text{valOp}T(u)+(1-\gamma)^T]=[u-(1-\gamma)^T, u+(1-\gamma)^T]$. Since it is true for all $T$, we have that $u=v$.

\begin{claim}
 Consider some $T$ and the strategy for Eve that plays the first $T$ steps following an optimal strategy in the finite-horizon game of length $T$ with vector $v$, followed by playing arbitrarily. 
Then, the outcome is above $\text{valOp}T(v)- (1-\gamma)^T\max_{i} v_i$.
\end{claim}
\begin{proof}
For any strategy for Adam, the expected reward for the first $T$ rounds is at least the expected reward in the finite-horizon game. In each remaining round, the reward is at least $0$ in the real game, but $v_i$ in round $T$ for some $i$ followed by 0's in the finite-horizon game.
Since the outcome is $\text{valOp}T(v)$ in the finite-horizon game, the real outcome is then as described.

````

One can show a similar statement for Adam.
For any $\epsilon>0$ one can pick a big enough $T$ such that $(1-\gamma)^T\max_{i} v_i\leq \epsilon$.

Let $v^*$ be the unique fix-point of the value iteration algorithm. 
Thus, $v^*=\text{valOp}T(v^*)$ for all $T$. Pick some optimal strategies $\sigma_x,\tau_x$ in $M^{T,x,v^*}$ for each $x$. Let $\sigma^*,\tau^*$ be the strategies that play $\sigma_x,\tau_x$ whenever in node $x$ in each round.
The strategy $\sigma,\tau$ are optimal in $\text{valOp}T(v^*)$ for each $T$, because $v^*$ is a fix-point. 
But, for each $\epsilon>0$,  the strategy $\sigma$ ensures outcome at least $v-\epsilon$ and $\tau$ ensures outcome at most $v+\epsilon$ using the claim. Hence, the third item follows.

The fourth item follows from that the value iteration algorithm is a contraction.

For the fifth item, consider the strategy used in the claim. 
Let $T$ be $\log(\epsilon/2)/\log(1-\gamma)$, i.e. $T$ is such that 

$$
\gamma \sum_{i=T}^{\infty}(1-\gamma)^i=\epsilon/2
$$

or in words, $T$ is such that the total outcome of each step after the $T$-th step is at most $\epsilon/2$.
Intuitively, if we modify the strategy very little, then the change is unlikely to come up in the first $T$ steps. More precisely, we will modify our strategy so that the probability that change will matter is less than $\epsilon/2$. That implies that the outcome differs by at most $\epsilon$ from the value.
We will use this intuition together with the argument for the third item to give a bound on the patience of $\epsilon$-optimal strategies. Fix some optimal stationary strategy $\sigma$ for Eve and an arbitrary stationary strategy $\tau$ for Adam. Let $\sigma'$ be a stationary strategy obtained from $\sigma$ rounded greedily  so that each probability is a rational number with denominator 

$$
q=mT/\epsilon=\frac{m\log(\epsilon/2)}{\log(1-\gamma)\epsilon}.
$$

 We will argue that $\sigma'$ is $\epsilon$-optimal.

The rounding proceeds inductively as follows for each node $x$:
The numbers $p_i$ are the original probability and the numbers $p_i'$ are the new probabilities.
For each $i$, the number $p_i'$ is defined as follows: If $\sum_{j=1}^{i-1}(p_i-p_i')>0$, then round up (i.e. $p_i'$ is the smallest rational with denominator $q$ so that $p_i<p_i'$) and otherwise round down, except the last number $p_\ell'$, which is such that $\sum_{j=1}^{\ell}p_i'=1$.
Note that this ensures that $-1/q<\sum_{j=1}^{i-1}(p_i-p_i')<1/q$. It also ensures that $|p_i-p_i'|<1/q$ for all $i$ (including for $i=\ell$).

For all nodes $x$ and rounds $T'\leq T$ we will define some random variables.
Specifically, the random variables denote what happen in round $T'$ if in node $x$.
The random variable $X_{x,T'}$ (resp. $Y_{x,T'}$) denotes the action picked by Eve if Eve follows $\sigma$ (resp. $\sigma'$).
The random variable $Z_{x,T'}$ denotes the action picked by Adam.
For each action pair $(i,j)$  the random variable $W_{x,i,j,T'}$ denotes the node entered in round $T'+1$, if Eve picks $i$ and Adam $j$. 
(As a side note: Each of the random variables are distributed the same way independent of $T'$).
Each of these random variables are independent of each other, except that (as we will define later) the random variables $X_{x,T'}$ and $Y_{x,T'}$ for each $x,T'$ are very much not independent of each other.

We see that we can view the first $T$ steps of the play when Eve follows $\sigma$ by only considering the outcome of $X_{x,T'}$, $Z_{x,T'}$ and $W_{x,i,j,T'}$ for all $T'$ and $x$ (even stronger: We only need to consider one $x,i,j$ for each $T'$, because the token is on only one node at a time). Similarly, for $\sigma'$, but using $Y_{x,T'}$ instead of $X_{x,T'}$.
For this to work, note that each random variable should be independent, except that the random variables $X_{x,T'}$ and $Y_{x',T''}$ need not be independent of each other for any $x',T''$. This is precisely the property we had for them!
For each $x,T'$,  we will then use a coupling $C_{x,T'}=(X'_{x,T'},Y'_{x,T'})$, a distribution over $[m]^2$, such that $X'_{x,T}$ is distributed as $X_{x,T'}$ and $Y'_{x,T'}$ is distributed as $Y_{x,T'}$. We will use a classic result for distributions, called the Coupling Lemma.

To introduce the Coupling Lemma, first, we need the notion of total variation distance. Given two distributions, $\Delta$ and $\Delta'$ over a set $S$, the total variation distance $t$ between $\Delta$ and $\Delta'$ is 

$$
t(\Delta,\Delta')=\frac{1}{2}\sum_{x\in S} |\Delta(x)-\Delta'(x)|
$$

 

````{prf:lemma} NEEDS TITLE AND LABEL 
For any distributions $\Delta$ and $\Delta'$ over a set $S$, we have 

*  for all couplings $(X,Y)$ of $\Delta$ and $\Delta'$, that 

$$
t(\Delta,\Delta)\leq \Pr[X\neq Y]
$$

*  that there is a coupling $(X',Y')$ of $\Delta$ and $\Delta'$ satisfying that 

$$
t(\Delta,\Delta)= \Pr[X'\neq Y']
$$


 

For any distributions $\Delta$ and $\Delta'$ over a set $S$, we have 

*  for all couplings $(X,Y)$ of $\Delta$ and $\Delta'$, that 

$$
t(\Delta,\Delta)\leq \Pr[X\neq Y]
$$

*  that there is a coupling $(X',Y')$ of $\Delta$ and $\Delta'$ satisfying that 

$$
t(\Delta,\Delta)= \Pr[X'\neq Y']
$$



````

Because of our rounding, we have that $t(X'_{x,T'},Y'_{x,T'})<\frac{m}{2q}$. 
Using that with the coupling lemma (the second part to be precise), lets us find a coupling $C_{x,T'}=(X'_{x,T'},Y'_{x,T'})$ 
such that $\Pr[X'_{x,T'}\neq Y'_{x,T'}]<\frac{m}{2q}$.

Consider the plays $\play_1,\play_2$ for when Eve follows $\sigma$ or $\sigma'$ respectively.
We can view the first $T$ steps of these plays by considering $X'_{x,T'}$ instead of $X_{x,T'}$ and similar when Eve follows $\sigma'$.
We can therefore see that the first $T$ steps two plays are different with probability 
$=p<\frac{mT}{2q}=\epsilon/2$
 using union bounds. 
 

We therefore see that the value for the path $\play_1$ cannot differ from the value of $\play_2$ with more than $p\gamma\sum_{i=1}^T(1-\gamma)^i=p$. I.e. in the worst case, if $\play_1$ and $\play_2$ differs, the reward is 1 in each step for $\play_1$ but 0 in each step for $\play_2$.
Also, the rewards in the steps after step $T$ can also differ by at most $1$ and by our choice of $T$, we have that outcome contributed from these remaining steps are worth less than $\epsilon/2$ as well.
Hence, we see that $\sigma'$ obtains the same as $\sigma$ except for $\epsilon$ against any strategy $\tau$ and is thus $\epsilon$-optimal.









\end{proof}

There is a classic problem in geometry called the sum-of-square-roots problem. The problem is defined as follows:
Let $a,b_1,b_2,\dots,b_n$ be natural numbers. Is $\sum_{i=1}^n\sqrt{b_i}>a$? 

The problem comes up for decision problems about distances in Euclidean space. It is not known to be in P or NP for that matter, but is in the fourth level of the countering hierarchy, slightly inside PSPACE. The issue is in essence that it is not known how good an approximation of $\sqrt{b_i}$ is necessary to decide the strict inequality. 

We will use the sum-of-square-roots problem to give an informal hardness argument, in that finding the exact value of a concurrent game is in general harder than solving the sum-of-square-roots problem. 

Consider the following game $G$:
There are three vertices, $\{0,1,s\}$ where $0$ and $1$ are absorbing, with color 0 and 1 respectively.
The vertex $s$ is such that (1) $c(s,i,j)=0$, (2) $\Deltas,i,i)=1$ (for $i\in \{1,2\}$), (3) $\Deltas,2,1)=0$ and (4) $\Deltas,1,i)$ is the uniform distribution over $s$ and $0$. The game is illustrated in Figure \ref{7-fig:sqroot}.

Consider an optimal stationary strategy in $G$ for Eve. Let $p$ be the probability with which she plays the first action. If Adam knows that Eve will follow this strategy, the game devolves into a MDP. We know from that for such there exists optimal positional strategies and thus Adam is either going to play the left or right column always. Clearly, $0<p<1$ because $p=0$ or 1 means that either playing the left or right column with probability 1 would ensure that no positive reward ever happens.


```{figure} ./../FigAndAlgos/7-fig:sqroot.png
:name: 7-fig:sqroot
:align: center
Concurrent discounted game with value $v_s=-2+\sqrt{4+2(1-\gamma)}$
```



Let $v_0=0,v_1=1,v_s$ be the values of the three vertices. If he plays the left column, the outcome is $p(1-\gamma)$.
If he plays the right column, the outcome is $p/2(1-\gamma)v_s+(1-p)(1-\gamma)$. Observe that the former is increasing in $p$ and the latter is decreasing (since clearly, $0<(1-\gamma)v_s<v_s$). Also, both are continues. Thus, the optimum is for $p(1-\gamma)$ to be equal to $p/2(1-\gamma)v_s+(1-p)(1-\gamma)$ and both equal to $v_s$.
We will first isolate $v_s$ in $v_s=p/2(1-\gamma)v_s+(1-p)(1-\gamma)$.
\begin{align*}
v_s&=p/2(1-\gamma)v_s+(1-p)(1-\gamma)\Rightarrow (1-p/2(1-\gamma))v_s=(1-p)(1-\gamma)\Rightarrow \\
v_s&=\frac{(1-p)(1-\gamma)}{1-p/2(1-\gamma)}\enspace .
\end{align*}

Note that $p,\gamma<1$ thus, $1-p/2(1-\gamma)\neq 0$.
We then have the equality 
\begin{align*}
\frac{(1-p)(1-\gamma)}{1-p/2(1-\gamma)}&=p(1-\gamma)\Rightarrow\\(1-p)(1-\gamma)&=p(1-\gamma)(1-p/2(1-\gamma))\Rightarrow\\
0&=\frac{1-\gamma}{2} p^2+2p-1\Rightarrow \\
p&=\frac{-2\pm\sqrt{4+2(1-\gamma)}}{1-\gamma} \enspace .
\end{align*}

We see that $\frac{-2-\sqrt{4+2(1-\gamma)}}{1-\gamma}<0$. Thus, $p=\frac{-2+\sqrt{4+2(1-\gamma)}}{1-\gamma}$.
Also, 

$$v_s=-2+\sqrt{4+2(1-\gamma)}\enspace .$$

 
It is straight-forward to modify the construction to get any square-root desired for a fixed $\gamma$. 


By making such a construction for each number $\sqrt{b_i}$, we can make another vertex $s^*$ that has the value of $(1-\gamma)\frac{\sum_{i=1}^n\sqrt{b_i}}{n}$ with a single action for each player and that goes to a uniformly random vertex. 
Observe that decreasing each reward by $x$, reduces the value of each vertex by $x$. Reduce each reward by $\frac{an}{1-\gamma}$.
We can then decide the sum-of-square-roots problem by deciding whether the value of $s^*$ is strictly above $0$. 

We get the following lemma.

````{prf:lemma} NEEDS TITLE AND LABEL 
The (exact) decision problem for the value is sum-of-square-root hard for concurrent discounted games
 

The (exact) decision problem for the value is sum-of-square-root hard for concurrent discounted games

````

We will use this game  $G$ as an example to illustrate how to make the $\Delta-function deterministic for concurrent games while having the same value and a similar optimal strategy.


```{figure} ./../FigAndAlgos/7-fig:sqroot2.png
:name: 7-fig:sqroot2
:align: center
Alternate concurrent discounted game with value $v_s=-2+\sqrt{4+2(1-\gamma)}$
```

Consider the following game $G'$:
There are three vertices, $\{0,1,s\}$ where $0$ and $1$ are absorbing, with color 0 and 1 respectively.
The vertex $s$ is such that (1)
$c(s,i,j)=0$ for all $i,j$, (2) $\Deltas,i,j)=s$ for $i+1=j$ (i.e. for $(i,j)\in \{(1,2),(2,3)\}$), (3) $\Deltas,i,j)=0$ for $i+j=4$ (i.e. the other diagonal, $(i,j)\in \{(3,1),(2,2),(1,3)\}$) and (4) $\Deltas,i,j)=1$ otherwise (i.e. for $(i,j)\in \{(1,1),(2,1),(3,2),(3,3)\}$).
 The game is illustrated in Figure \ref{7-fig:sqroot2}.
 
We will argue that the value of $G'$ is equal to that of $G$.
 We clearly have that the value of $s$ is in $(0,1)$.
Consider a stationary strategy $\sigma$ for Eve
such that $\sigma(1)\neq \sigma(2)$. Let $p_i=\sigma(i)$ for $i\in \{1,2,3\}$. 
Let $\sigma'$ be such that $\sigma'(3)=p_3$ and otherwise, $\sigma'(i)=\frac{p_1+p_2}{2}$ for $i\in\{1,2\}$. Let $p_i'=\sigma'(i)$ for $i\in \{1,2,3\}$.
\begin{claim}
The strategy $\sigma'$ is at least as good as $\sigma$
\end{claim}

````{admonition} Proof
:class: dropdown tip

If Adam plays 1, then the expected outcome is 
$p_1+p_2=p'_1+p'_2$ no matter if Eve plays $\sigma$ or $\sigma'$. 
If he plays $i$ for $i\in\{2,3\}$, the expected outcome is $
\frac{p_{4-i}}{1-p_{i-1}}$ if Eve plays $\sigma$ and otherwise, if she plays $\sigma'$, the expected outcome is   
$\frac{p'_1}{1-p'_2}=\frac{p'_2}{1-p'_1}$. 
Note that $\frac{p'_1}{1-p'_2}>\min_{i\in\{2,3\}\frac{p_{4-i}}{1-p_{i-1}}}$ and thus, $\sigma'$ is at least as good a strategy as $\sigma$.

````

A similar argument shows that for any strategy $\tau$ for Adam the similar strategy $\tau'$ where $\tau'(1)=\tau(1)$ and $\tau'(i)=\frac{\tau(2)+\tau(3)}{2}$ for $i\in\{2,3\}$ is at least as good as $\tau$.
Consider that the players follows such stationary strategies $\sigma'$ and $\tau'$.
Let $\sigma$ be 

$$\sigma(i)=\begin{cases} \sigma'(1)+\sigma'(2)&\text{if }i=1\\
\sigma'(3)&\text{if }i=2\enspace .\end{cases}$$

Similarly, let 
 $\tau$ be 

$$\tau(i)=\begin{cases} \tau'(1)&\text{if }i=1\\
\tau'(2)+\tau'(3)&\text{if }i=2\enspace .\end{cases}$$

But playing $\sigma$ and $\tau$ in $G$ gives the same outcome as playing $\sigma'$ and $\tau'$ in $G'$ as can be seen as follows: In either game, with probability

$$
\sigma'(1)\tau'(2)+\sigma'(2)\tau'(3)=\frac{\sigma(1)\tau(2)}{2}$$

 we play again with a reward of 0, with probability 

$$\sigma'(1)\tau'(3)+\sigma'(2)\tau'(2)+\sigma'(3)\tau'(1)=
\frac{\sigma(1)\tau(2)}{2}
+\sigma(2)\tau(1)
$$

we get absorbed in 0 after a reward of 0 and with probability 

$$
(\sigma'(1)+\sigma'(2))\tau'(1)+(\tau'(2)+\tau'(3))\sigma'(3)
$$

 we get absorbed in 1 after a reward of 0.
But this is in particular the case if the players play optimally and thus, the value is the same in the two games.


Before, in Corollary \ref{cor:long}, we argued that the patience of $\epsilon$-optimal stationary strategies was $q=\frac{m\log(\epsilon/2)}{\log(1-\gamma)\epsilon}$.
Giving a similar exponential bound for the optimal stationary strategies is harder than solving the sum-of-square-roots problem, as we will argue next.
Assume that we had an exponential bound for optimal stationary strategies.

```{figure} ./../FigAndAlgos/7-fig:exact-hard.png
:name: 7-fig:exact-hard
:align: center
Concurrent discounted game that implies that if there is an exponential lower bound on patience, then the sum-of-square-roots problem is in P
```

Consider an arbitrary yes-instance of the sum-of-square-roots problem, giving a vertex $s^*$. Reduce each reward by $a$ and in the new game let $s^*_a$ be the vertex corresponding to $s^*$. 
We will now create a game that uses the previous game as a sub-game.
The game has 1 additional vertex $s'$, which is a 2x2-matrix, such that $c(s',i,j)=0$ and $\Deltas,1,1)=1$ and $\Deltas,2,2)=s^*$ and $\Deltas,i,j)=0$ for $i\neq j$.
There is an illustration in Figure~\ref{7-fig:exact-hard}, using the vertex $s^*$ as above. 
Using an argument like above, we see that the probability $p$ to play the top action in the vertex $s'$ is such that $p(1-\gamma)=(1-p)(1-\gamma)x$, where $x$ is the value of $s^*$. Thus, $x=\frac{p}{1-p}$. If $p$ only needs to be exponential small, then $x$ is exponentially small as well. This is true for any yes-instance of the sum-of-square-roots problem and thus, we only need polynomially many digits to decide the problem. We can find polynomially many digits of $\sqrt{b_i}$ for each $i$ in polynomial time. We get the following lemma.

````{prf:lemma} NEEDS TITLE AND LABEL 
Giving an exponential lower-bound on patience for optimal stationary strategies in concurrent discounted games implies that the sum-of-square-roots problem is in $\textrm{PTIME}
 

Giving an exponential lower-bound on patience for optimal stationary strategies in concurrent discounted games implies that the sum-of-square-roots problem is in $\textrm{PTIME}

````

