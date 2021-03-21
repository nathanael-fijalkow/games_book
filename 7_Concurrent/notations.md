(7-sec:notations)=
# Notations

```{math}

```

The definition of arena $\mathcal{A}$ in this chapter is $\mathcal{A}=(G, \Delta)$, where $G=(V,E)$ is a graph and $\Delta:V\times A\times A\rightarrow   \mathcal{D}(E)$. In particular, we are not using the sets $V_\mathrm{Adam}$ and $V_\mathrm{Eve}$.
The games are played similarly to before and formally as follows: 
There is a token, initially on the initial vertex. 
Whenever the token is on some vertex $v$, 
Eve selects an action $r$ in $A$ and Adam selects an action $c$ in $A$. The edge $e=(v,c,w)$ is then drawn from the distribution $\Delta(v,r,c)$ and the token is pushed from $v$ to $w$.
 In general, the game continues like that forever.

We will use the following simplifying assumptions in this chapter:

1.  We will assume that all colors are in $\{0,1\}$, except for the section on Matrix games where we additionally also allow $-1$ (to be able to easily illustrate the game rock-paper-scissors). This simplifies some expressions, but generally, the dependency on the number of colors is not too bad comparatively.
2.  To make illustrations easier, we assume that for any pair of edges $e,e'$ in $\Delta(v,a,a')$ for any $v,a,a'$, we have that $c(e)=c(e')$, i.e. the color does not depend on which edge is picked from $\Delta(v,a,a')$, but only $v,a,a'$. This assumption does not matter for the types of games considered.

We will overload the notation slightly for notational convenience, in that for any $v,a,a'$, we will write $c(v,a,a')$ for $c(e)$ where $e\in  \Delta(v,a,a')$ (note that the second assumption ensures that this is well-defined, i.e. there is only one such color).

A vertex $v$ is absorbing iff each player has only 1 action in $v$ and $\Delta(v,1,1)=v$.

To describe the complexity of good stationary strategies in concurrent games, we will use the notion of patience. Given a probability distribution $d\in   \mathcal{D}$ the distribution has patience $p$ if $p=\min_{i\in  \textrm{supp}(d)} d(i)$ (i.e. the patience is the smallest, non-zero probability that an event may happen according to $d$).
In essence, if you have low enough patience you can typically guess the strategy and check whether it is a good strategy (when you fix a strategy, the game becomes a Markov decision process, which are relative easy to work with), the game can solved in $\textrm{NP}\cup  \textrm{coNP}$. However, some times the patience is huge and writing down a good strategy, in binary, cannot be done in polynomial space (it is quite surprising in some sense that even with this property, finding the values in the games remain in $\textrm{PSPACE}$).

We will illustrate a stochastic arena $\mathcal{A}=(G, \Delta)$ as follows:
For each non-absorbing vertex $v$, there is matrix.
 Entry $(i,j)$ of the matrix illustrating $v\in V$ describes what happens if, when the token is on $v$, Eve plays $i$ and Adam $j$. The entry contains a color $c$, which is $c(v,i,j)$, and 
there is an arrow from entry $(i,j)$ of $v$ to $w$ if there is an edge   
$e=(v,c,w)$ in $\Delta(v,i,j)$. 
 The arrow corresponding to $e$ is denoted with the probability $\Delta(v,i,j)(e)$. 
Especially, to simplify the illustrations we will do as follows: If $| \textrm{supp}( \Delta(v,i,j))|=1$, we do not include the probability (which is 1). Also, in that case, let $e=(v,c,w)= \Delta(v,i,j)$ 
and 
if $v=w$, we omit the arrow and if $w$ is absorbing we write $c^*$ in entry $i,j$ of $v$, where $c$ is the color $c(w,1,1)$ (in this case, we omit the number $c(e)$ from the illustration, but in none of our illustrations does this number matter for what we try to illustrate). 
