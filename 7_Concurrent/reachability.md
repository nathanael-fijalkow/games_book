(7-sec:reachability)=
# Concurrent reachability games

In this section we consider concurrent reachability games. 
Intuitively, unlike concurrent discounted games, these games cares only about the final part of the play.
This, while perhaps not clear directly from the definitions, makes the games somewhat harder. For instance, the value iteration algorithm requires double-exponential time.
Note that like for concurrent discounted games, if we force Eve to follow some strategy, the game reduces to a MDP and there exists optimal positional strategies.

We will not prove the following known lemma. We will however, show the weaker statement that the decision problem for the value can be done in PSPACE.

````{prf:lemma} NEEDS TITLE lemm:reach_determined
:label: lemm:reach_determined

Concurrent reachability games are determined. Also, finding the value of a concurrent reachability game can be done in TFNP[NP]

````

We will argue that there might not be optimal strategies for Eve in concurrent reachability games. 
The game we will use will later be a member of a family of games that requires high patience to play well.

The snowball game (or purgatory 1) is defined as follows:
There are 3 vertices, the goal vertex $\textrm{Win}$, $\bot$ (an absorbing vertex) and a vertex 1, which has a 2x2 matrix, such that $\Delta(x,r,c)$ is a dirac distribution over (1)
$\textrm{Win}$ for $r=c$, (2) $1$ for $r<c$ and (3) $\bot$ for $r>c$.
When we illustrate the game, we write view the goal vertex $\textrm{Win}$ as being an absorbing vertex with color 1.
There is an illustration of the snowball game in {numref}`7-fig:snowball`.

```{figure} ./../FigAndAlgos/7-fig:snowball.png
:name: 7-fig:snowball
:align: center
The snowball game or purgatory 1, in which no optimal strategy exists for Eve
```

For any $\epsilon>0$, consider the stationary strategy for Eve that plays the first action with probability $1-\epsilon$. 
If Adam plays the left column always, play will reach $\textrm{Win}$ with pr. $1-\epsilon$. If Adam plays the right column always, play reaches $\textrm{Win}$ with pr. 1. Hence, the strategy for Eve is $\epsilon$-optimal and the value of the vertex is 1.

On the other hand, if Adam plays the right column whenever Eve plays the first action with pr. 1, and otherwise plays the first action, 
then in the last round in the vertex there must be a positive pr. that play goes to vertex 0. Hence, Eve has no optimal strategy.

````{prf:lemma} NEEDS TITLE lemm:no_opt_reach
:label: lemm:no_opt_reach

Eve need not have an optimal strategy in a concurrent reachability game

````

The following lemma states some classical results for concurrent reachability games that we will not prove.

````{prf:lemma} NEEDS TITLE lemm:reach_class
:label: lemm:reach_class

*  For any $\epsilon>0$, there are always $\epsilon$-optimal stationary strategies for Eve and optimal stationary strategies for Adam. 
*  The value iteration algorithm converges to the optimal value and is defined exactly like for concurrent discounted games, except that $\gamma=0$ and the target vertex has value 1 in the first iteration
*  The values $v$ are the least fix-point (i.e., every other fix-point $v'$ is such that for all $i$ $v_i\leq v'$) of the value iteration operator $\text{valOp}$

````

(Note that the games are not symmetric, in that Eve tries to reach a node and Adam tries to stay away from it, and in particular, even though Eve need not have an optimal strategy in a concurrent reachability game, Adam always has one)

The decision problem for the existential first order theory over the reals is the following decision problem:
Given a function $F: \mathbb{R}^n\rightarrow \{\text{true},\text{false}\}$, is there an vector $v$ such that $F(v)$ is true?
The function $F$ must be an well-formed (i.e. connected with logical `and', `or' and `not') quantifier-free formula over polynomial inequalities.
E.g. $x^2y+z\geq 5\wedge \neg (xz\leq 3)$ would be such a function.

````{prf:lemma} NEEDS TITLE AND LABEL 
The decision problem for the existential theory over the reals is in PSPACE

The decision problem for the existential theory over the reals is in PSPACE

````

We will now, given a number $c$, encode the problem whether the value in a concurrent reachability game is  $<c$, starting from some vertex $x$.
The idea is that we can describe a fix-point of the value iteration operator, i.e.
we can describe that $v_i= \textrm{val}[M^i(v)]_i$. Since we know that the values are the least fix-point, we can then just add the condition that $v_x<c$. 
We can describe the value of a matrix game by guessing a strategy for each player, $\sigma$ for Eve and $\tau$ for Adam, and then checking that these strategies are optimal by showing that the outcome obtained by following Eve's strategy is equal to what is obtained by following Adam's.
I.e. we check that for Eve's strategy, the least outcome obtained when Adam plays any given column is $v_i$ and similar for Adam.
We describe that as $v_i=\min_{a\in [m]} (\sigma M^i_{*,a}(v))$ and $v_i=\max_{a\in [m]} (\tau M^i_{a,*}(v))$, where $M^i_{*,j}(v)$ is the $j$-th column of $M^i(v)$ and $M^i_{j,*}(v)$ is the $j$-th row for all $j$. 
We can express that $x=\min(a_1,a_2,\dots,a_n)$ for any number $n$ and any polynomials $a_1,a_2,a_n$, in the first order theory of the reals by stating that 

$$
x\leq a_1\wedge x\leq a_2\wedge \dots \wedge x\leq a_n \wedge (x=a_1\vee x=a_2\vee \dots \vee x=a_n) \enspace .$$

Similarly, one can also describe that $x=\max(a_1,a_2,\dots,a_n)$ for any number $n$ and any polynomials $a_1,a_2,a_n$.

We can similarly make a statement that $v_x\leq c$. Using that PSPACE is equal to co-PSPACE, we also get that we can find if $v_x\geq c$ and $v_x>c$ and therefore also $v_x=c$ and $v_x\neq c$, all in PSPACE.

````{prf:lemma} NEEDS TITLE AND LABEL 
Decision problems for the values in a concurrent reachability game is in PSPACE

Decision problems for the values in a concurrent reachability game is in PSPACE

````

The set of vertices that have value 0 can be found in polynomial time. This is because, the set of vertices that have value 0 in the time limited game of length $n$ has also value 0 in all other time limited games. That this is so is easy to see by considering that Eve plays an $\epsilon$-optimal strategy for $v>\epsilon$, where $v$ is the value of the vertex with the lowest value. The game then devolves to a MDP for Adam, and the statement is true for such.

````{prf:lemma} NEEDS TITLE lemm:find_0_reach
:label: lemm:find_0_reach

The set of vertices of value 0 in a concurrent reachability game can be found in polynomial time

````

Next, we will also argue that we can find the set of vertices $S_1$ that have value 1 in polynomial time as well.
For notational convenience, for stationary strategies $\sigma,\tau$ we will, for a set $x$ and a set of vertices $S$ use 

$$
F^{\sigma,\tau}(x,S):=\sum_{r\in A_1}\sum_{c\in A_2}\sum_{x'\in S}\sigma(x)(r)\tau(x)(c)\delta(x,r,c)(x')\enspace ,$$

 i.e. the probability when the players follows $\sigma,\tau$ to go from $x$ directly to a vertex in $S$.

For a set $S$, containing $\textrm{Win}$ and a non-empty subset $S'\subseteq(S\setminus \{ \textrm{Win}\})$ and a vertex $x\in S'$, let the {\em subset property} be the following:
For each $\epsilon>0$, there is a strategy $\sigma$ for Eve, such that for any strategy $\tau$ for Adam, $F^{\sigma,\tau}(x,S\setminus S')\cdot \epsilon >F^{\sigma,\tau}(x,V\setminus S)$.

For a set $S$, containing $\textrm{Win}$, let the {\em value-1-property} be that the subset property is satisfied for each $S'\subseteq(S\setminus \{ \textrm{Win}\})$ (with some $x\in S'$).
For a set $S$ satisfying the value-1-property, we will define some subsets.
Let $S^0$ be the set consisting of $\textrm{Win}$.
Let $S^i$, for each $i\geq 1$ be the set of vertices such that for each $x\in S^i$,
the vertex $x$ satisfies the subset property for $S'$ and $S=\bigcup_{j=0}^{i-1}S^j$.
Let $\ell$ be the largest number such that $S^\ell$ is non-empty (note that $S^i$, for $i>\ell$ must then be empty).

We will be using the following lemma.

````{prf:lemma} NEEDS TITLE AND LABEL 
The set of vertices $S_1$ of value 1 satisfies the value-1-property

The set of vertices $S_1$ of value 1 satisfies the value-1-property

````

````{admonition} Proof
:class: dropdown tip

The proof is by contradiction. Thus, there is an $S$ (not containing $\textrm{Win}$) such that $S_1$ and $S$ does not satisfy the subset property for any $x\in S$. I.e. for some constant $\epsilon>0$,
$F^{\sigma,\tau}(x,S_1\setminus S)\epsilon \leq F^{\sigma,\tau}(x,V\setminus S_1)$ for any strategy $\sigma$ for Eve and some strategy $\tau_{\sigma}$ for Adam and for every $x\in S$.
But then, all vertices in $S$ have value $\leq (1-\epsilon)+\epsilon V_{\max}$ where $v_{\max}<1$ is the largest value of a vertex in $V\setminus S_1$.
This is because to get to $\textrm{Win}$ from $S$, it must leave $S$ and in that step, the probability to go to a vertex in  $V\setminus S_1$ (from which one cannot obtain more than $v_{\max}$) is at least the constant $\epsilon$.  

````

We will argue that this is a precise characterization of $S_1$ next.

````{prf:lemma} NEEDS TITLE AND LABEL 
Consider a set $S'$ satisfying the value-1-property.
Then each vertex of $S'$ has value 1.\label{lem:sufficent_for_value1}

Consider a set $S'$ satisfying the value-1-property.
Then each vertex of $S'$ has value 1.\label{lem:sufficent_for_value1}

````

````{admonition} Proof
:class: dropdown tip

We will for all $i$ and any $\epsilon>0$ construct a strategy $\sigma_{i,\epsilon}$ for Eve that starting from a vertex in $\bigcup_{j=i}^n S^j$ will eventually get to $S^{i-1}$ with probability at least $1-\epsilon$ (especially, the strategy $\sigma_{1,\epsilon}$ is $\epsilon$-optimal). We will do it using backwards induction in $i$ and thus start from $i=\ell$.

Note that the base case for $i=\ell$ follows directly from the condition.
We now for any $\epsilon>0$ will find a strategy $\sigma_{i,\epsilon}$, given that we have a strategy $\sigma_{i+1,\epsilon'}$ for any $\epsilon'>0$.
The idea is that the subset property gives a strategy $\sigma$ such that for all $\tau$, $F^{\sigma,\tau}(x,S'\setminus S)\epsilon/2 >F^{\sigma,\tau}(x,V\setminus S')$, for $S=\bigcup_{j=i}^{n} S^j$.
Note that in expectation, following this strategy, we go to some other vertex in $S$ with at least some fixed probability $p$ (that could be quite close to 1).
Hence, in expectation, we need to be in such a vertex $1/(1-p)$ times before entering either $S'\setminus S$ or $V\setminus S'$.
We therefore follow the strategy $\sigma_{i+1,\epsilon'}$ in $\bigcup_{j=i+1}^n S^j$, where $\epsilon'=\frac{\epsilon}{2(1-p)}$.
The inductive construction then follows by applying union bound over the $1/(1-p)$ times we are in $S^i$.

````

Note that the lemmas together shows that $S_1$ is the largest set satisfying value-1-property.

Our algorithm,  \text{crgLim1}, for finding $S_1$ is then as follows:
Assign to each vertex $x$ a rank $\text{rk}_x$, a value in $0,1,\dots,n,\bot$, starting with $\text{rk}_x=0$.
Let $\overline{S}^i$ be the set of vertices of rank $i$.
Let $\overline{S}_1=V\setminus S^{\bot}$.
We increment (where a rank is less than another if it is a smaller number. Also, all other ranks are below $\bot$) the rank of a non-goal vertex $x\in \overline{S}^i$, whenever it does not satisfy the subset property for $S=\overline{S}_1$ and $S'=\bigcup_{j=i}^n \overline{S}^j$.
Note that no vertex can satisfy the subset property for rank 0, since $S'$ is all vertices.
Whenever a stable configuration is reached, output $\overline{S}_1$.

````{prf:lemma} NEEDS TITLE AND LABEL 
The output of the  \text{crgLim1}\ algorithm is correct

The output of the  \text{crgLim1}\ algorithm is correct

````

````{admonition} Proof
:class: dropdown tip

The idea is that we want $S^i=\overline{S}^i$ at termination.
Note that the subset property is harder to satisfy for a vertex $x$ if we remove vertices from $S$ or from $(S\setminus S')$.
Thus, if at some time we have that $x$ does not satisfy the subset property for $S=\overline{S}_1$ and $S'=\bigcup_{j=i}^n \overline{S}^j$, then it does not do so for $S$ being any subset of $\overline{S}_1$ or $(S\setminus S')$ being any subset of $\bigcup_{j=0}^{i-1} \overline{S}^j$.
However, initially $S_1\supseteq\overline{S}_1$ (being all vertices) and $\bigcup_{j=i}^n S^j\supseteq \bigcup_{j=0}^{i-1} \overline{S}^j$ for all $i$. But we must have that $S_1\supseteq\overline{S}_1$ and $\bigcup_{j=i}^n S^j\supseteq \bigcup_{j=0}^{i-1} \overline{S}^j$ for all $i$, at all latter points as well, since in the last iteration it was satisfied, for all $i$ and all $x\in S^i$, we have that the subset property is satisfied for $S=\overline{S}_1$ and $S'=\bigcup_{j=i}^n \overline{S}^j$, because we have that $S\supseteq S_1$ and $(S\setminus S')=\bigcup_{j=1}^{i-1} \overline{S}^j\supseteq \bigcup_{j=1}^{i-1} S^j$.
On the other hand, eventually no vertex gets it rank incremented (since there are a finite number of ranks and vertices) and the algorithm terminates with a set $\overline{S}_1\supseteq S_1$ satisfying the value-1-property. Since $S_1$ is the largest such set, we have that $\overline{S}_1=S_1$.

````

We will now consider the running time of the algorithm.
We will consider that we can decide whether a pair of sets $S$ and $S'$ satisfies the subset property for a vertex $x$ can be solved in $O(k)$ time.
Let $S_x$ be the set of vertices that can be visited in a play immediately after $x$. Observe that $|S_x|$ is a lower bound on the number of arrows from matrix $x$ in our illustration of the game.
Consider a vertex $x$ and a rank $i$, and we want to find an upper bound on the computation we do on $x$ while it has rank $i$.
Clearly, we only need to consider incrementing the rank of $x$ whenever a vertex in $S_x$ has changed its value and only if it is changed to either $i$ (from $i-1$) or to $\bot$ (from $n$), because otherwise, the sets $S$ and $S'$ have not changed. 
Thus, we only do at most $2|S_x|+1$ checks whether $x$ satisfies the subset property.
There are $n+1$ ranks, so in total for $x$, we use at most $(n+1)(2|S_x|+1)$ checks.
Hence, in total over all $x$, we do $O(n\sum_{x} |S_x|)$ checks.

````{prf:lemma} NEEDS TITLE AND LABEL 
The run time of the  \text{crgLim1}\ algorithm is $O(nk\sum_{x} |S_x|)$ times

The run time of the  \text{crgLim1}\ algorithm is $O(nk\sum_{x} |S_x|)$ times 

````

We will then finally consider how to check whether $x$ satisfies the subset property for a pair of sets $S$ and $S'$.
We will do so by constructing a strategy $\sigma=\sigma(\epsilon)$ for Eve satisfying the property for any fixed $\epsilon>0$.
We will construct the strategy  $\sigma$ from some sequence of pairs of sets (of rows and columns) $(R_1,C_1),(R_2,C_2),\dots,(R_{\ell},C_{\ell})$. We will let $C_i^*=\bigcup_{j=1}^i C_j$ and similar for $R^*_i$.
For convenience, we also define $C_0^*$ as the empty set of columns.
We will define $R_i$ from $C_{i-1}^*$ as each row $r\not\in R_{i-1}^*$ such that, for all $c\not\in C^*_{i-1}$, we have that $F^{r,c}(x,V\setminus S)=0$.
We will define $C_i\not\in C_{i=1}^*$ from $R_i$ as each column $c$ such that there is a $r\in R_i$ such that 
$F^{r,c}(x,S\setminus S')>0$.
The set $R^{*}_{\ell}$ is the first set such that $R^*_{\ell+1}$ is empty (clearly, by construction all sets $R_i,C_i$ for $i>\ell$ would also be empty).

````{prf:lemma} NEEDS TITLE AND LABEL 
There is a strategy $\sigma(\epsilon)$ for all $\epsilon>0$ iff $C_{\ell}^*$ is the set of all columns

There is a strategy $\sigma(\epsilon)$ for all $\epsilon>0$ iff $C_{\ell}^*$ is the set of all columns

````

````{admonition} Proof
:class: dropdown tip

We will first argue that if $C_{\ell}^{*}$ is not all columns $C$, then the strategy $\tau$ that plays uniformly over $C'=(C\setminus C_{\ell}^*)$ shows that no strategy $\sigma(\epsilon)$ exists for small enough $\epsilon>0$. This is because any row $r$ such that $F^{r,c}(x,S\setminus S')>0$ for some $c\in C'$ is also such that $F^{r,c'}(x,V\setminus S)>0$ for some column $c'\in C'$. This is because otherwise $r$ would be in $R^i$ for some $i$ and then $c$ would be in $C_{\ell}^*$. Hence, the probability $F^{r,c'}(x,V\setminus S)$ cannot be more than a constant factor smaller than $F^{r,c}(x,S\setminus S')$.

Otherwise, if $C_{\ell}^*=C$, then let $\sigma(\epsilon)$ be the strategy that picks an $i$ from the distribution $\mathcal{D}$ and then plays an action in $R^i$ uniformly at random. The distribution $\mathcal{D}$ is such that for all $j\in \{1,\dots,\ell-1\}$ we have $\Pr^{ \mathcal{D}}[i=j]\epsilon\delta_{\min}/m=\Pr^{ \mathcal{D}}[i>j]$. 

To argue that $\sigma=\sigma(\epsilon)$ satisfies the subset property for $x,S,S'$
consider each column $c$. We have that $c\in C^j$ for some $j$. 
Let $p$ be the pr. with which a row in $R^j$ is played by $\sigma$ and thus, $F^{\sigma,c}(x,S\setminus S')\geq p\delta_{\min}>0$.
Any row $r$ such that $F^{r,c}(x,V\setminus S)>0$ must be outside $R^*_j$ by construction (and if such a row exists $j<\ell$). 
We play such rows with pr. $\leq \Pr^{ \mathcal{D}}[i>j]$ and thus $\Pr^{ \mathcal{D}}[i>j]\geq F^{\sigma,c}(x,V\setminus S)$.
We have that $pm>\Pr^{ \mathcal{D}}[i=j]$ (strict because $j<\ell$) and thus, 

$$
F^{\sigma,c}(x,S\setminus S')\epsilon\geq p\delta_{\min}\epsilon>\delta_{\min}\epsilon/m\Pr^{ \mathcal{D}}\nolimits[i=j]\geq 
\Pr^{ \mathcal{D}}\nolimits[i>j]\geq F^{\sigma,c}(x,V\setminus S) \enspace .$$

This completes the proof of the lemma.
````

Our algorithm for checking if a vertex $x$ satisfies the subset property for sets $S,S'$ is as follows:
We will construct the sequence of sets $(R_1,C_1),(R_2,C_2),\dots,(R_{\ell},C_{\ell})$.
To do so we will use a datastructure.
The datastructure has the following properties:
Initially, for each column $c$, we will make a list $L_c$ of the rows $r$ such that $F^{r,c}(x,V\setminus S)>0$.
We will also have a counter for each row $r$ that initially contains how many such columns there are.
Finally for each row $r$, there is a list $L_r$ of columns such that $F^{r,c}(x,S\setminus S')>0$.

The algorithm then uses the datastructure as follows:
Let $i\leftarrow 1$.
Add all the rows with the counter at 0 to $R^i$. 
If $R^i$ is the empty set, return whether $C_{i-1}^*$ is all columns.
For each row $r$ in $R^i$ go through $c\in L_r$ and subtract 1 from the counter of each row in $L_c$. If a counter reach 0, add it to $R^{i+1}$.
Increment $i$.
Go to line 3.

The total time is $O(\sum_{r,c}| \textrm{supp}( \Delta(x,r,c))|)$ for the algorithm.

````{prf:lemma} NEEDS TITLE AND LABEL 
We can check whether a vertex $x$ satisfies the subset property for sets $S$ and $S'$ in time 

$$O(\sum_{r,c}| \textrm{supp}( \Delta(x,r,c))|)$$

We can check whether a vertex $x$ satisfies the subset property for sets $S$ and $S'$ in time 

$$O(\sum_{r,c}| \textrm{supp}( \Delta(x,r,c))|)$$

````

We therefore get that 
````{prf:lemma} NEEDS TITLE lem:val1
:label: lem:val1
\label{lemm:find_1_reach}
We can find the set of vertices of value 1 in time $O(n\sum_{x} |S_x|\sum_{r,c}| \textrm{supp}( \Delta(x,r,c))|)$

````

Next, we will give a lower bound for patience, i.e. that in some games, the patience for every $\epsilon$-optimal stationary strategy must be high. 
For a number $k$, let purgatory $k$ be the following game:
There are $2+k$ vertices, $\textrm{Win}$ (which is vertex 0), one vertex $\bot$ which is absorbing and each other vertex $i\in \{1,\dots, k\}$ has a 2x2 matrix, such that $\Delta(x,r,c)$ is a dirac distribution over (1)
$i-1$ for $r=c$, (2) $k$ for $r<c$ and (3) $\bot$ for $r>c$.
There is an illustration of Purgatory $4$ in Figure {numref}`7-fig:purgatory`.

```{figure} ./../FigAndAlgos/7-fig:purgatory.png
:name: 7-fig:purgatory
:align: center
Purgatory $4$. For clarity, the colors are omitted, except that $0^*$ corresponds to an edge to an absorbing vertex different from $\textrm{Win}$ and $1^*$ corresponds to an edge to $\textrm{Win}$
```

It is easy to see that all vertices but $\bot$ is in $S_1$, using the value 1 property.

````{prf:lemma} NEEDS TITLE lem:purgatory
:label: lem:purgatory

For any $0<\epsilon<1/2$ and any $k\geq 1$, there is a unique strategy for Eve with least patience which is $\epsilon$-optimal in purgatory $k$. That strategy has patience $\epsilon^{-2^{k-1}}$

````

````{admonition} Proof
:class: dropdown tip

We will find the best strategy with patience $1/p$ for any number $0<p<1/2$.
It is clear that the best strategy with patience $1/p$ is to play the strategy that maximizes the pr. of eventually reaching $i$ from vertex $j$ for all $j>i$ while having patience $1/p$.
Let $x_k=1-p$ and let $x_i=1-\sqrt{1-x_{i+1}}$. We will argue that $x_i$ is the probability of eventually reaching vertex $i-1$ from vertex $k$ for all $i\in \{1,\dots,k\}$ and that there is a unique best strategy with patience $1/p$.

The unique best strategy in vertex $k$ is to play the top action with pr. $1-p$ and the bottom action with pr. $p$. This ensures that the pr. $x_k$ of reaching $k-1$ from $k$ is $1-p$ if Adam plays the left column.

Consider now vertex $i\in \{1,\dots,k-1\}$.
For the purpose of finding good strategies in $i$, we can view vertex $i$, when Eve plays her best strategy in $j>i$ and Adam plays a best response, as a smaller reachability game with 3 vertices, i.e. $i-1$ (as $\textrm{Win}$), $\bot$ and $i$, where $\Delta(i,r,c)$ is (1) a dirac distribution over $i-1$ for $r=c$, (2) a dirac distribution over $\bot$ for $r>c$ and (3) a distribution that goes to $\bot$ with pr. $1-x_{i-1}$ and to $i$ with the remaining pr. for $r<c$. See Figure {numref}`7-fig:1purgatory`

Let $p_i$ be the probability with which a strategy $\sigma$ plays the top row in vertex $i$.
We can then consider the game as a MDP, since we have fixed a stationary strategy for one of the players.
It is clear that the pr. to reach $i-1$ from $i$ if Adam plays the right column is strictly increasing in $p_i$ and the pr. to reach $i-1$ from $i$ if Adam plays the left column is strictly decreasing in $p_i$. We will consider the strategy such that the pr. of reaching $i-1$ is equal no matter which column Adam plays (by the previous statement, this strategy must then be optimal).
Observe that the pr. of reaching $i-1$ if Adam always plays the left column is $p_i$ (which is then also the pr. to reach $i-1$ from $i$) and if he always plays the right column it is  $p_i x_i p_i+(1-p_i)$ (using that the pr. of reaching $i-1$ from $i$ is $p_i$).
Thus, we have that

$$
p_i=p_i x_i p_i+(1-p_i)\Rightarrow 0=p_i^2/2 x_i-p_i+1/2 \Rightarrow p_i=\frac{1\pm \sqrt{1-x_i}}{x_i}\enspace .$$

 We see that $\frac{1+ \sqrt{1-x_i}}{x_i}>1$ and thus the solution is $p_i=\frac{1- \sqrt{1-x_i}}{x_i}$ or that $(x_{i-1}=)x_ip_i=1- \sqrt{1-x_i}$.

Consider now that the strategy is exactly $\epsilon$-optimal, implying that $x_1=1-\epsilon$. 
We will argue that $p=\epsilon^{2^{k-1}}$.
We will do so by arguing  using induction in $i$ that $x_i=1-\epsilon^{2^{k-1}}$, since $x_k=1-p$ (this also shows that the strategy is indeed using patience $1/p$ since the probabilities in the other vertices, which are $p_i=\frac{x_{i-1}}{x_i}$, are strictly above $1/p$).
We have already noted that  $x_1=1-\epsilon=1-\epsilon^{2^0}$.
We will next argue that $x_i=1-\epsilon^{2^{k-1}}$, for $i\geq 2$ using that $x_{i-1}=1-\epsilon^{2^{k-2}}$.
We have that 

$$
1-\epsilon^{2^{k-2}}=x_{i-1}=1-\sqrt{1-x_{i}}\Rightarrow \sqrt{1-x_{i}}= \epsilon^{2^{k-2}}\Rightarrow
1-\epsilon^{2^{k-1}}=x_i\enspace .
$$

This completes the proof of the lemma.

````

Concurrent reachability games are not symmetric in the players. E.g. Adam always have an optimal strategy but Eve might not. We will next argue that Adam still requires double exponential patience to play well.

Consider the following game called purgatory duel $k$ which can be viewed as a symmetric version of purgatory $k$.
There are $3+2k$ vertices, $\textrm{Win}$ (which is vertex 0), one vertex $\bot$ which is absorbing (and is also vertex $0'$), and the start vertex $s$ and each other vertex $\{1,\dots, k,1',\dots,k'\}$ has a 2x2 matrix. Each vertex $x\in \{1,\dots, k\}$ is such that $\Delta(x,r,c)$ is a dirac distribution over (1) $x-1$ for $r=c$, (2) $s$ for $r<c$ and (3) $\bot$ for $r>c$.
 Each vertex $x'\in \{1',\dots, k'\}$ is such that $\Delta(x',r,c)$ is a dirac distribution over (1) $x-1'$ for $r=c$, (2) $s$ for $r<c$ and (3) $\textrm{Win}$ for $r>c$. The start vertex is 1x1 matrix and is such that $\Delta(s,r,c)$ is a uniform distribution over $k$ and $k'$.
There is a illustration of Purgatory Duel $2$ in Figure {numref}`7-fig:purgatoryduel`.

```{figure} ./../FigAndAlgos/7-fig:purgatoryduel.png
:name: 7-fig:purgatoryduel
:align: center
Purgatory duel $2$. For clarity, the colors are omitted, except that $0^*$ corresponds to an edge to an absorbing vertex different from $\textrm{Win}$ and $1^*$ corresponds to an edge to $\textrm{Win}$
```

We will say that a strategy $\sigma$ for Eve mirrors a strategy $\tau$ for Adam, if $\sigma(i)=\tau(i')$ and $\sigma(i')=\tau(i)$ for all $i$.
Similarly, $\tau$ mirrors $\sigma$.

````{prf:lemma} NEEDS TITLE AND LABEL 
The value of vertex $s$ is $1/2$. Also, for any $\epsilon>0$, any $(1/2-\epsilon)$-optimal strategy $\tau$ for Adam does not follow a dirac distribution in $i'$ for any $i'\in\{1',\dots,k'\}$. Finally, every $\epsilon$-optimal strategy is a mirror of an $\epsilon$-optimal strategy

The value of vertex $s$ is $1/2$. Also, for any $\epsilon>0$, any $(1/2-\epsilon)$-optimal strategy $\tau$ for Adam does not follow a dirac distribution in $i'$ for any $i'\in\{1',\dots,k'\}$. Finally, every $\epsilon$-optimal strategy is a mirror of an $\epsilon$-optimal strategy

````

````{admonition} Proof
:class: dropdown tip

First, the value of vertex $s$ is at most $1/2$. This is because Adam can mirror any strategy $\sigma$ for Eve. This ensures that any play reaching $\textrm{Win}$ is mirrored by an equally likely play reaching $\bot$. Thus, then the players follows these strategies, the pr. to reach $\textrm{Win}$ is equal to the pr. to reach $\bot$ (there might also be some positive pr. to not reach neither, but Adam also wins those plays). 

Fix $\epsilon>0$ and consider a strategy $\tau$ for Eve that plays a dirac distribution in $i'\in\{1',\dots,k'\}$. Then $\tau$ is not $(1/2-\epsilon)$-optimal. We can see that as follows: Let $\sigma$ be the strategy for Eve that plays $r=1$ when in $j'\in \{(i+1)',\dots,k'\}$ and the action which is not equal to $\tau(i')$ when in $i'$. This ensures that the play will always reach either $\textrm{Win}$ or $s$ from $k'$. But then  Eve can play an $(\epsilon/2)$-optimal strategy for purgatory $k$ in $\{1,\dots,k\}$, ensuring that $\textrm{Win}$ is reached with pr. at least $1-\epsilon/2$. But then $\tau$ is not $(1/2-\epsilon)$-optimal.

Consider that Adam is following a strategy $\tau$ that is not playing a dirac distribution in $i'\in\{1',\dots,k'\}$ and Eve is playing an arbitrary strategy $\sigma$. Then, eventually play reaches $\textrm{Win}$ or $\bot$ with pr. 1,  because in every $k+1$ steps, either $s$ is visited or either $\textrm{Win}$ or $\bot$ is reached, and after $s$ has been visited, $k'$ is next half the time and from $k'$ $\bot$ is reached with positive pr.

Consider an $\epsilon$-optimal strategy $\tau$ for Adam, for $\epsilon<1/2$. 
Then, let Eve's mirror strategy to $\tau$ be $\sigma_{\tau}$. Now, either $\textrm{Win}$ or $\bot$ is reached and because the strategies mirrors each other, the pr. to reach $\textrm{Win}$ is equal to that of reaching $\bot$. Thus, we see that the value is at most $1/2$, implying that it is exactly $1/2$.

It also follows that the strategies that are $\epsilon$-optimal mirrors each other.

````

We will now argue that Eve's (and thus Adam's) $\frac{1}{4}$-optimal strategies requires high patience.

To do so we will use the following lemma, showing that you can sometimes modify a concurrent game (or any of its special cases) and get a game with less value. While the proof is explicitly for concurrent reachability games, the proof is basically identical for concurrent discounted and mean-payoff games.
In a game $G$, for a vertex $v$ and a duration $T$, let $v^T_G$ be the value of the time-limited game with duration $T$.

````{prf:lemma} NEEDS TITLE lem:change_succ
:label: lem:change_succ

Consider a concurrent reachability game $G$ and a pair of vertices $u,v$, such that for all $T$, we have that $u^T_G\geq v^T_G$. Consider a vertex $w$ such that for a pair of actions, $(r,c)$ we have that $v\in  \textrm{supp}( \Delta(w,r,c))$. Consider an alternate game $G'$ equal to $G$, except that some of the probability mass is moved from $v$ to $u$ when playing $(r,c)$ in $w$, i.e. $0< \Delta(G,w,r,c)(v)- \Delta(G',w,r,c)(v)= \Delta(G',w,r,c)(u)- \Delta(G,w,r,c)(u)$.
Then for all vertices $z$ we have that $z^T_G\leq z^T_{G'}$

````

````{admonition} Proof
:class: dropdown tip

The proof is by induction in $T$.
The proof is trivial for $T=0$, because $z^T_G=0= z^T_{G'}$ for all non-goal vertices (and the goal vertex $\textrm{Win}$ has value 1).
For $T\geq 1$, we have that $z^{T-1}_G\leq z^{T-1}_{G'}$.
But, matrix games are monotone in their entries, so it follows directly that for $z\neq w$ we have that $z^{T}_G\leq z^{T}_{G'}$.
Consider the matrix for $w^T_G$ compared to $w^T_{G'}$. All entries but the one for $(r,c)$ are smaller directly by induction. We also have that $v^T_{G}\leq u^T_{G}\leq u^T_{G'}$, the first inequality by definition and the second by induction. We thus see that all entries in $w^T_{G}$ are smaller than in $w^T_{G'}$.
The lemma follows.

````

We are now ready to find the patience in concurrent reachability games.

````{prf:lemma} NEEDS TITLE AND LABEL 
Any $(1/4)$-optimal strategy, for either player, in purgatory duel $k$ has patience at least $(3/4)^{-2^{k-1}}$ for each $k$

Any $(1/4)$-optimal strategy, for either player, in purgatory duel $k$ has patience at least $(3/4)^{-2^{k-1}}$ for each $k$

````

````{admonition} Proof
:class: dropdown tip

We will show that the lemma is true for Eve's strategies and that it is true for Adam's follows from Lemma {prf:ref}`lem:change_succ`.
Consider an $(1/4)$-optimal strategy $\sigma$ for Eve. Fixing this strategy for Eve, we get a MDP for Adam. Clearly, in this MDP $G'$, we have that $0=\bot^T_{G'}\leq s^T_{G'}$ for all $T$. We can thus apply Lemma {prf:ref}`lem:change_succ` to changing $\Delta(1',1,1)$ from $\bot$ to $s$. In the resulting game $G''$, 
we still have that $0=\bot^T_{G''}\leq s^T_{G''}$ and thus, we can change $\Delta(1',2,2)$ from $\bot$ to $s$.
Let the next game be $G^*$.
Thus, for any $i'\in \{1',\dots,k'\}$, the plays from $i'$ to $\bot$ in $G^*$ all goes through $s$. Note that Adam can ensure that the play reaches $s$ from $i'$ and thus, when he plays optimally, do so.
Thus, whenever $s$ is entered and Adam plays optimally, $k$ is enter eventually with pr. 1.
For the purpose of the value, we can thus disregard $s$ and vertices in $\{1',\dots,k'\}$ and just view each edge going to $s$ as going to $k$ instead.
But the resulting game is purgatory $k$ (in which Eve has fixed his strategy) and Eve is playing a strategy that gives value at least $1/4$, which requires  at least $(3/4)^{-2^{k-1}}$ patience, by Lemma {prf:ref}`lem:purgatory`.

````

