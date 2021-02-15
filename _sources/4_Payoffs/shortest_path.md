(4-sec:shortest_path)=
# Shortest path games

```{math}
\newcommand{\FC}{\mathrm{FC}\xspace} 
\newcommand{\Cycles}{\mathrm{Cycles}\xspace} 
\newcommand{\Mean}{\mathrm{Mean}\xspace} 
\newcommand{\FirstCycle}{\mathrm{FirstCycle}\xspace} 
\newcommand{\SuffixAllCycles}{\mathrm{SuffixAllCycles}\xspace} 
\newcommand{\FirstCycleReset}{\mathrm{FirstCycleReset}\xspace} 
\newcommand{\siblank}{\mathtt{-}}
\newcommand{\Lift}{\textrm{Lift}}
\newcommand{\Rbar}{\overline\R}
\newcommand{\downward}[1]{\mathop{\downarrow_{#1}}}
\newcommand{\gval}{\mathrm{gr}\text{-}\val}
\newcommand{\bigO}{O}\newcommand{\Eve}{\textrm{Eve}}
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
\newcommand{\coNP}{\textrm{coNP}}
\newcommand{\PSPACE}{\textrm{PSPACE}}
```
The quantitative objective $\Sup$ generalises the qualitative
objective $\Reach$ by stating numerical preferences on the target. 
Another quantitative extension of the reachability objective is to quantify the cost of a path towards the target.
We define the quantitative objective $\ShortestPath$ over the set of colours $C = \Z \cup \set{\Win}$ by

$$
\ShortestPath(\rho) =
  \begin{cases}
    - \infty & \text{if } \rho_k \neq \Win \text{ for all } k \\
    - \sum_{i = 0}^{k-1} \rho_i & \text{for $k$ the first index such that } \rho_k = \Win.
  \end{cases}
$$

Two remarks are in order.

*  Recall that in our definition of quantitative objectives Eve wants to maximise the outcome,
which is why we introduce $\ShortestPath$ with a minus sign:
we interpret the weights as costs and Eve is trying to reach the target with the smallest possible cost.
*  We use the same abusive terminology as for the shortest path graph problem: the cost of a path is the sum of the weights along it
(until the first occurence of $\Win$) and we are looking for a path of minimal cost, hence not necessarily the shortest in number of edges.

Solving shortest path games in full generality is not easy; we will come back to it at the end of this chapter using some results obtained along the way.
Let us first illustrate the difficulties, and then solve the special case where the weights are non-negative.
We fix a shortest path game $\Game$.
Recall that by definition:

$$
\val(v) = \sup_{\sigma} \inf_{\tau} \ShortestPath(\pi^v_{\sigma,\tau}).
$$

Hence for a vertex $v$ there are three possibilities: 

*  $val(v) = -\infty$, meaning that Eve cannot ensure to reach $\Win$ with a finite cost,
*  $\val(v) \in \Z$, meaning that Eve can ensure to reach $\Win$ with a finite cost,
*  $\val(v) = \infty$, meaning that Eve can ensure to reach $\Win$ with arbitrarily negative cost.

As we will see, detecting whether $\val(v) = -\infty$ is easy: this is equivalent to asking whether 
$v \notin \AttrE(\Win)$ as stated in  {prf:ref}`4-lem:detecting_minus_infinity`.
The second case where $\val(v) \in \Z$ will be an occasion to revisit the attractor computation from Section {ref}`2-sec:attractors`
in a quantitative setting.
Most of the difficulty lies in the third case, where 


```{prf:lemma} NEEDS TITLE 4-lem:detecting_minus_infinity
:label: 4-lem:detecting_minus_infinity
:nonumber:

Let $\Game$ a shortest path game and $v$ a vertex.
Then $\val(v) = -\infty$ if and only if $v \notin \AttrE(\Win)$.

```

```{admonition} Proof
:class: dropdown tip

\mynote{TO DO}

```


```{figure} ./../1-fig:optimal_strategies_shortest_path_game.png
:name: 1-fig:optimal_strategies_shortest_path_game
:align: center
An example of a shortest path game with negative weights Eve does not have an optimal strategy.
Indeed $\val(v_0) = \infty$ since for any $k$, Eve has a strategy ensuring that $\ShortestPath$ is $k$
by using $k$ times the self loop $-1$ before reaching $\Win$.
However, if she never reaches $\Win$ the outcome is $-\infty$.
```

## Shortest path games with non-negative weights

```{prf:theorem} NEEDS TITLE 4-thm:shortest path-positive
:label: 4-thm:shortest path-positive
:nonumber:

Shortest path games with non-negative weights are uniformly positionally determined for both players```{margin}
This positionality result does not extend to infinite games```.
There exists a value iteration algorithm for computing the value function of these games in polynomial time and space.
\mynote{More precisely}, 

```

We rely on the high-level presentation of value iteration algorithms given in Section {ref}`1-sec:value_iteration`.

```{prf:lemma} NEEDS TITLE 4-lem:optimal_strategies_shortest_path_games
:label: 4-lem:optimal_strategies_shortest_path_games
:nonumber:

Let $\Game$ be a shortest path game with non-negative weights, then there exists an optimal strategy $\sigma$ for Eve.

```


```{admonition} Proof
:class: dropdown tip

Thanks to the assumption that the weights are positive,
$\ShortestPath$ takes value in the non-positive integers, in particular is a set of integers bounded from above.
This implies that the supremum is indeed a maximum.

```

{numref}`1-fig:optimal_strategies_shortest_path_game` shows that the assumption that all weights are non-negative 
in  {prf:ref}`4-lem:optimal_strategies_shortest_path_games` is necessary.

We consider the complete lattice $Y = -\N \cup \set{-\infty}$ equipped with the natural order and the function $\delta : Y \times C \to Y$ defined by

$$
\delta(x, w) = 
\begin{cases}
0 & \text{ if } w = \Win \\
x - w & \text{ if } w \in \N.
\end{cases}
$$

We let $F_V$ be the lattice of functions $V \to Y$ equipped with the componentwise order induced by $Y$.
Note that $\delta$ is monotonic, it induces the monotonic operator $\Op : F_V \to F_V$ defined by:

$$
\Op(f)(v) = 
\begin{cases}
\max \set{\delta( f(v'), w) : (v,w,v') \in E} & \text{ if } v \in \VE, \\
\min \set{\delta( f(v'), w) : (v,w,v') \in E} & \text{ if } v \in \VA.
\end{cases}
$$

Thanks to  {prf:ref}`1-thm:kleene`, the operator $\Op$ has a greatest fixed point which is also the greatest post-fixed point of $\Op$.
The latter are functions $f \in F_V$ such that $f \le \Op(f)$ and called progress measures.

```{prf:lemma} NEEDS TITLE AND LABEL 
Let $\Game$ be a shortest path game with non-negative weights, then $\val$ is the greatest fixed point of $\Op$.
 
:label: 
Let $\Game$ be a shortest path game with non-negative weights, then $\val$ is the greatest fixed point of $\Op$.

:nonumber:

Let $\Game$ be a shortest path game with non-negative weights, then $\val$ is the greatest fixed point of $\Op$.

```


```{admonition} Proof
:class: dropdown tip

We show the following two properties:

*  $\val$ is a progress measure;
*  for every progress measure $f$ we have $f \le \val$.

Since the greatest fixed point of $\Op$ is also the greatest progress measure, this implies the result.

We show the first item.
Thanks to  {prf:ref}`4-lem:optimal_strategies_shortest_path_games` there exists $\sigma$ an optimal strategy for Eve.
Consider a vertex $v$.
If $v \in \VE$ we need to show that 

$$
\val(v) \le \max \set{\delta(\val(v'), w) : (v,w,v') \in E},
$$

and if $v \in \VA$ that 

$$
\val(v) \le \min \set{\delta(\val(v'), w) : (v,w,v') \in E}.
$$

Let $(v,w,v') \in E$ a move consistent with $\sigma$: if $v \in \VE$ then 
$\sigma(v) = (v,w,v')$, if $v \in \VA$ this is any outgoing edge of $v$,
we show that $\val(v) \le \delta(\val(v'), w)$ which implies both inequalities.

If $\val(v) = -\infty$ then the inequality holds, so we can assume that $\val(v) \neq -\infty$.

We distinguish two cases.
If $w = \Win$ then $\delta(\val(v'), \Win) = 0$ so the inequality holds.
Otherwise $w \in \N$. 
Let us assume towards contradiction that $\val(v) > \delta(\val(v'), w) = \val(v') - w$.
Let $\sigma' = \sigma_{\mid (v,w,v')}$ the strategy induced by $\sigma$ after playing $(v,w,v')$.
Let $\play'$ a play consistent with $\sigma'$ from $v'$.
The play $\play = (v,w,v') \play'$ is consistent with $\sigma$ from $v$ and since $\sigma$ is optimal 
this implies that $\ShortestPath(\play) \ge \val(v)$.
Hence every play consistent with $\sigma'$ from $v'$ ensure $\val(v) + w$, which is strictly greater than $\val(v')$
contradicting the definition of $\val(v')$.
Thus the inequality $\val(v) \le \delta(\val(v'), w)$ holds.


We now show the second item.
Let $f$ be a progress measure, we define a positional strategy $\sigma$
by $\sigma(v) = (v,w,v')$ such that $f(v) \le \delta(f(v'), w)$, and show that $f \le \val$.
We consider a vertex $v$ and show that for every play $\play$ consistent with $\sigma$ from $v$ we have 
$f(v) \le \ShortestPath(\play)$. 
This is easily shown for finite plays by induction on the length and then for infinite plays by taking the limit.
This implies that $f(v) \le \val^\sigma(v) = \inf_\tau \ShortestPath(\play^v_{\sigma,\tau})$,
and then $f(v) \le \sup_{\sigma} \val^\sigma(v) = \val(v)$.

```

Thanks to  {prf:ref}`1-thm:kleene` $\val$ can be computed by a greatest fixed point algorithm.
To obtain the announced complexity we carefully define the data structure.

The pseudocode is given in {numref}`4-algo:value_iteration_shortest_path_non_negative`.

```{figure} ./../4-algo:value_iteration_shortest_path_non_negative.png
:name: 4-algo:value_iteration_shortest_path_non_negative
:align: center
The value iteration algorithm for shortest path games with non-negative weights.
```

```{admonition} Proof
:class: dropdown tip

  We follow a similar approach as in Dijkstra's algorithm, keeping an
  estimation $\ell(v)\in\R$ of the shortest paths towards the target
  $\Win$ from vertices $v$ in a set $S$, still to be considered; these
  estimations are refined greedily along the computation. We
  initialise $S$ to $V$, and all values $\ell(v)$ to $+\infty$, except
  for vertices just after an edge of the target $\Win$ that we put at
  $0$. For vertices $u$ of Eve, we need more information and thus keep
  track of a mapping from successors of $u$ towards the value
  $\ell(u,v)\in\R$ of the current shortest path from $u$ to $\Win$,
  going through the edge $(u,v)$. We have that $\ell(u)$ is the
  maximal value of $\ell(u,v)$ for all successor vertices $v$: in
  particular, as long as one of the successors $v$ still has value
  $\ell(v)=+\infty$, the value $\ell(u)$ remains $+\infty$.

  The algorithm consists in iteratively picking a minimal element $v$
  of $S$, with respect to $\ell(v)$, remove it from $S$, and update
  $\ell(u)$ for all vertices $u$ such that $(u,v)\in E$:
  
  *  if $u\in \VA$, $\ell(u)$ is updated to $c(u,v)+\ell(v)$
    whenever the latter value is smaller than $\ell(u)$;
  *  if $u\in \VE$, $\ell(u,v)$ is updated to $c(u,v)+\ell(v)$, and
    the value of $\ell(u)$ is updated accordingly.
  

  This continues until there are no more vertices in $S$ after which
  we return the values $\ell(u)$ that we can prove to be the actual
  values $\Value(u)$ of each vertex $u$. Let us denote by $S_i$ and
  $\ell_i(u)$ the values of $S$ and $\ell(u)$ in iteration $i$. We
  prove the following invariants:
  
  
1.  for all iterations $i$, $\ell_i(u)$ is equal to the value
    $\Value_{\game_i}(u)$ in the shortest path game $\game_i$ obtained
    from $i$ by replacing the cost $c(v,w)$ of each edge with
    $+\infty$ if both endpoints $v$ and $w$ are still in $S_i$;
  
2.  moreover,
    $\min\{\ell_i(v)\mid v\in S_i\}\geq \max\{\Value_{\game}(v)\mid
    v\notin S_i\}$ which generalises the greedy property crucial to
    the correctness of Dijkstra's algorithm.
  
  Since the cost of each edge in $\game_i$ only decreases along the
  various iterations, it is also the case for the values
  $\Value_{\game_i}(u)$. More precisely, the invariant shows that
  $\ell_i(u)=\Value_{\game_i}(u)$ for all $u\in S_i$, and
  $\ell_i(u)=\Value_{\game}(u)$ for all $u\notin S_i$. The proofs are
  very similar to the usual proofs and can be found in great details
  in {cite}`Khachiyan&al:2008`.

  From a complexity point of view, there is no doubt that the various
  computations can be performed in polynomial time. A careful
  analysis, using (minimum) Fibonacci heaps, as in Dijkstra's
  algorithm, allows one to obtain an overall complexity
  $\bigO(m+n\log(n))$. 

```


## Detection of $-\infty$ vertices with mean payoff games
However, contrary to the previous payoffs, the **positional**
determinacy result no longer holds as shows the example
in {numref}`4-fig:memory`. In this game, there are two positional
strategies for Adam: $\tau_1(v_1)=(v_1,v_0)$ and
$\tau_2(v_1)=(v_1,v_2)$. Strategy $\tau_1$ does not guarantee Adam to
reach the target, since Eve can play the cycle $(v_1,v_0)$ forever and
obtain payoff $+\infty$. Strategy $\tau_2$ guarantees payoff
$0$. However, Adam can play smarter by scaring Eve. Imagine that Adam
plays once to $v_0$, and then switches to $v_2$: he then guarantees a
value $-1$. Doing so one more time, he can guarantee value $-2$. And
so on, until he decides to do it $50$ times, showing to Eve that he is
able to get $-50$. Then, the optimal decision for Eve is to go
directly to the target. Therefore, Adam needs memory to play optimally
in this example: his optimal strategy is to go to $v_0$ the first 50
times the play visits $v_1$, and switch to $v_2$ after the 50th
time. However Eve still has a positional optimal strategy that
consists in always going to $v_2$. This is always the case as we
discuss later. Notice that the possible absence of optimal positional
strategies for Adam makes non-trivial an upper bound of the form
$\NP\cap\coNP$ in the complexity of solving shortest path games.

```{figure} ./../4-fig:memory.png
:name: 4-fig:memory
:align: center
A shortest path game, with $v_2$ being the target vertex,
    where Adam needs memory to play optimally
```

Apart from the complication on the memory requirement for Adam to play
optimally, one other technical difficulty arises from the presence of
vertices with optimal value $-\infty$: this is the case when Adam may
reach a target of $\Win$ while controlling a negative cycle along the
way. As previously announced, this is closely related with mean payoff
games: {cite}`Brihaye&Geeraerts&HaddadA&Monmege:2017`

```{prf:theorem} NEEDS TITLE 4-thm:-infty-MP
:label: 4-thm:-infty-MP
:nonumber:

  Let $\arena$ be an arena.
  
  *  If the game $\game=(\arena,\ShortestPath(\Win))$ has no
    vertices $v$ of value $\Value^\game(v)=+\infty$, and the only
    outgoing edges of vertices in $\Win$ are self loops of weight $0$,
    then for all vertices $v$, $\Value^\game(v)=-\infty$ if and only
    if $\Value^{\game'}(v)<0$ if $\game'=(\arena,\MeanPayoff)$ is the
    associated mean payoff game on the same arena.
  *  Reciprocally, if $\game=(\arena,\MeanPayoff)$, we can build in
    polynomial time a game $\game'=(\arena',\ShortestPath(\Win))$ such
    that $\Value^\game(v)<0$ if and only if
    $\Value^{\game'}(v) =-\infty$.
  

```

```{admonition} Proof
:class: dropdown tip

  For the first item, if $\Value^{\game'}(v)<0$, there exists a
  profile of optimal positional strategies $(\sigma^*,\tau^*)$: the
  outcome starting in $v$ and following this profile ends up in a loop
  with total cost $<0$. For every $M>0$, we can construct a strategy
  $\tau^M$ for Adam that ensures in $\game$ a payoff at most $-M$,
  which then proves that $\Value^\game(v)=-\infty$: strategy $\tau^M$
  is obtained by playing strategy $\tau^*$ until the accumulated cost
  is less than $-M-nW$, with $W=\max_{(v,c,v')\in E} |c|$, after
  which he switches to an attractor strategy towards $\Win$ (which
  exists from every vertex of the game, since no vertices have value
  $+\infty$). Since the attractor strategy reaches the target in at
  most $n$ steps, the value of $\tau^M$ from $v$ is at most $-M$.

  Reciprocally, if $\Value^\game(v)=-\infty$, for $M=nW$,
  consider a strategy $\tau^M$ of Adam guaranteeing a payoff less than
  $-M$. Consider, towards a contradiction, a positional strategy
  $\sigma$ of Eve that secures a non-negative mean payoff. The play of
  $\game$ following the profile $(\sigma,\tau^M)$ necessarily leads to
  $\Win$, while visiting at least one negative cycle, around a given
  vertex $v'$. If $v'\in \VE$, Eve is not the one choosing to exit the
  cycle (since she is following a positional strategy), so Adam can
  modify its strategy to stay forever in the negative cycle, which
  contradicts the fact that $\sigma$ secures a non-negative
  mean payoff. If $v'\in \VA$, Adam can also choose to stay forever in
  the negative cycle by modifying his strategy. Therefore, Eve cannot
  have a positional strategy securing a non-negative mean payoff: by
  positional determinacy of mean payoff games
  ( {prf:ref}`4-thm:mean_payoff_positional`), Eve cannot have any strategy securing
  a non-negative mean payoff.

  \medskip For the second item, without loss of generality, suppose
  that $\arena$ is a bipartite arena,
  i.e. $E\subseteq \VA\times \VE\cup\VE\times \VA$. The new arena
  $\arena'$ is obtained by adding a fresh target $v_t$ with edges
  $(v,v_t)$ for all $v\in \VA$, as well as an edge $(v_t,v_t)$, all of
  cost 0. Consider the game $\game'=(\arena',\ShortestPath(\Win))$
  with $\Win = \{v_t\}$. By construction and using the bipartite
  hypothesis, Adam always has a strategy to reach $\Win$, so that no
  vertices $v$ have a value $\Value^{\game'}(v)=+\infty$. By letting
  $\game''=(\arena',\MeanPayoff)$, the previous item shows that
  $\Value^{\game'}(v)=-\infty$ if and only if
  $\Value^{\game''}(v)<0$. To conclude, it only remains to show that
  $\Value^{\game}(v)<0$ if and only if $\Value^{\game''}(v)<0$. By
  mapping positional strategies from $\game$ to $\game''$, we easily
  obtain $\Value^{\game''}(v)\leq \Value^\game(v)$, so the direct
  implication holds. For the converse, if $\Value^{\game''}(v)<0$, the
  target $v_t$ cannot be visited by a profile of positional optimal
  strategies (otherwise the mean payoff would be 0): projecting the
  play from $\game''$ on $\game$ therefore shows that
  $\Value^{\game}(v)\leq \Value^{\game''}(v) <0$. 

```


## A pseudopolynomial time value iteration algorithm
As shown above, we can detect vertices of value $+\infty$ and
$-\infty$ if needed. We now explain how to compute the exact optimal
value of other vertices, by a value iteration algorithm. Similarly to
the case of mean payoff or discounted games, the algorithm consists in
an iterative search of a fixed point of the operator
$F\colon \R^V\to \R^V$ mapping every vector $\vec x=(x_v)_{v\in V}$ to
the new vector $(y_v)_{v\in V}$, defined, for all $v\in V$, by:

$$y_v =
  \begin{cases}
    0 & \text{ if } v\in \Win\\
    \max_{(v,v')\in E} [c(v,v') + x_{v'}] &
    \text{ if } v\in \VE\setminus \Win\\
    \min_{(v,v')\in E} [c(v,v') + x_{v'}] & \text{ if } v\in
    \VA\setminus \Win
  \end{cases}$$


Notice the similarity with respect to the $\Lift$ operator used in the
value iteration algorithm for mean payoff
({numref}`4-algo:value_iteration_MP`): the following arguments are thus
very resembling to the ones already presented in the case of
mean payoff. Here, we obtain a more precise information though, since
it directly gives us the values for the shortest path objective
towards a fixed target.

In the presence of vertices of value $-\infty$, the iterative fixed
point computation would not terminate. However, thanks to the
following lemma (where we again let $W=\max_{(v,c,v')\in E} |c|$), we
know that finite values are bounded below, so that an intermediate
step of speed-up can detect the vertices of value $-\infty$.

```{prf:lemma} NEEDS TITLE 4-lem:-infty
:label: 4-lem:-infty
:nonumber:

  In a shortest path game $\game$, all vertices $v$ with a value
  $\Value(v)<-(n-1) W$ have value $\Value(v)=-\infty$.

```

```{admonition} Proof
:class: dropdown tip

  Consider a strategy $\tau$ of Adam securing a value $<-(n-1) W$
  from a given vertex $v$. We show that in the mean payoff game
  $\game'$ described in {prf:ref}`4-thm:-infty-MP`, vertex $v$ has value
  $<0$, which allows us to conclude. Let $\sigma$ be a positional
  strategy of Eve. By hypothesis, the play $\pi$ starting in $v$ and
  following the profile $(\sigma,\tau)$ has a payoff
  $\ShortestPath(\pi)<-(n-1) W$: therefore, it contains a negative
  cycle. As before, Adam can therefore modify its strategy so that he
  sticks to the choices he does in the first cycle he visits: this new
  strategy is indeed independent of $\sigma$, so that the according
  strategy indeed secures a negative mean payoff.

```

Thus, we let $G\colon\overline\R^V\to\overline\R^V$ mapping each
vertex $\vec x = (x_v)_{v\in V}$ to the mapping $(y_v)_{v\in V}$
defined by $y_v = x_v$ if $x_v\geq -(n-1)W$ and $y_v=-\infty$
otherwise. We consider then the sequence
$(\vec x^n = (GF)^n(\top))_{n\in \N}$, with $\top$ the vector having
all components equal to $+\infty$. Since it generalises the attractor
computation, after $n$ steps, vertices with a value
$\Value(v)<+\infty$ have been discovered: they are the only ones such
that $x^{n}_v < +\infty$. Moreover, these vertices satisfy
$x^{n}_v\leq n W$ since a given path towards the target has been
discovered along the first $n$ iterations. Since the mapping $GF$ is
monotonous, the sequence $(\vec x^n)_{n\in \N}$ is
non-increasing. Since it can only take values in the finite set
$\{-\infty\}\cup \{-(n-1) W+1, -(n-1) W+2,\ldots,nW\}
\cup\{+\infty\}$, it is stabilising: there exists a step $N$ such that
$\vec x^N=\vec x^{N+1}$. Notice that an a priori bound on $N$ is
$(2n-1)W n + n$. A careful analysis allows one to show that
$\vec x^N=\Value^\game$: the main argument is the fact that the
stabilisation of the sequence at index $N$ allows one to show by
induction that $N$ steps suffice for Adam to guarantee that he has
reached a target vertex while getting the optimal value.

{cite}`Brihaye&Geeraerts&HaddadA&Monmege:2017`

```{prf:theorem} NEEDS TITLE 4-thm:SP-pseudopoly-algo
:label: 4-thm:SP-pseudopoly-algo
:nonumber:

  We can compute in pseudopolynomial time the values of a
  shortest path game. 

```


