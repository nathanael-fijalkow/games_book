(6-sec:algos)=
# Algorithms

```{math}
\newcommand{\adist}{\ensuremath{f}}
\newcommand{\probm}{\mathbb{P}}
\newcommand{\lfp}{**lfp**}
\newcommand{\vwin}{\ensuremath{v_{\textsc{win}}}}
\newcommand{\vlose}{\ensuremath{v_{\textsc{lose}}}}
\newcommand{\Adamvertices}{\VA}
\newcommand{\Evevertices}{\VE}
\newcommand{\Randomvertices}{\vertices_{\text{Rand}}}
\newcommand{\perm}{\pi}
\newcommand{\DetAtt}{\ensuremath{**DetAtt**}}

\newcommand{\weight}{\mathbf{w}} \newcommand{\nats}{\mathbb{N}}\newcommand{\Eve}{\textrm{Eve}}
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
\newcommand{\EXPSPACE}{\textrm{EXPSPACE}}
\newcommand{\EXP}{\textrm{EXP}}
\newcommand{\kEXP}{\textrm{kEXP}}
`%\item Reduction to stopping games (Condon92)%  algorithm?%  possibilities, like the one ``converge-from-below in Condon93, or%\item mathematical programming: algo taken from Condon93?%\end{itemize}
We have shown that stochastic reachability games are central to the (quantitative) analysis of stochastic games. 
We have indeed reduced the quantitative analysis of all kinds of stochastic games to stochastic reachability games. We will now present algorithms for stochastic reachability games.

## Value iteration


````{prf:definition} NEEDS TITLE AND LABEL 
  A stochastic arena $\arena = (\vertices,E,\delta)$ is said to be
  **simple** if
  
  *  $V$ contains two sink vertices $v_{\Eve}$ and $v_{\Adam}$;
  *  every non-sink vertex
    $v \in \vertices \setminus \{v_{\Eve},v_{\Adam}\}$ has two
    successors;
  *  every random vertex $v \in \Randomvertices$ is an
    **average vertex**, that is, for every vertex
    $v'\in \vertices$, $(v,v') \in E$ implies
    $\delta(v,v')=\frac{1}{2}$.
  
 

  A stochastic arena $\arena = (\vertices,E,\delta)$ is said to be
  **simple** if
  
  *  $V$ contains two sink vertices $v_{\Eve}$ and $v_{\Adam}$;
  *  every non-sink vertex
    $v \in \vertices \setminus \{v_{\Eve},v_{\Adam}\}$ has two
    successors;
  *  every random vertex $v \in \Randomvertices$ is an
    **average vertex**, that is, for every vertex
    $v'\in \vertices$, $(v,v') \in E$ implies
    $\delta(v,v')=\frac{1}{2}$.
  

````

With a simple stochastic arena is naturally associated the
reachability objective $\Reach(\{v_{\Eve}\})$. The resulting game is
called a **simple stochastic game**.

````{prf:proposition} NEEDS TITLE AND LABEL 
  There exists a polynomial time transformation from stochastic games
  to simple stochastic games, which preserves the values.
 

  There exists a polynomial time transformation from stochastic games
  to simple stochastic games, which preserves the values.

````

More precisely,

````{admonition} Proof
:class: dropdown tip

  Let $\arena = (\vertices,E,\delta)$ be an arbitrary stochastic
  arena. First of all, all vertices in $\Win$ are merged into a single
  sink vertex $v_\Eve$.

  Assume $v \in \Randomvertices$ is a random vertex with $k$ outgoing
  edges, with probabilities $p_1, \cdots, p_k$, leading respectively
  to $v_1,\cdots,v_k$. We first introduce intermediary vertices in
  order to build a binary tree, whose leaves are $v_1 \cdots v_k$,
  root is $v$, and probabilities are set at each level of the tree in
  order to recover $p_1, \cdots p_k$ on the respective branches. This
  introduces $O(\log(k))$ fresh vertices, and is illustrated on an
  example on {numref}`6-fig:gen2binary`.

  
```{figure} ./../FigAndAlgos/6-fig:gen2binary.png
:name: 6-fig:gen2binary
:align: center
From general random vertices to binary ones.
```

  It remains to explain how to simulate a discrete probability
  distribution from say vertex $v$ to vertices $v_1$ and $v_2$ with
  probabilities $\frac{p}{q}$, resp.  $\frac{q-p}{q}$, using average
  vertices only.  We let $t \in\nats$ be such that
  $2^{t-1} \leq q < 2^{t}$. Using the binary encodings of $p$ resp.
  $q-p$ as $a_1 \cdots a_t$ resp. $b_1 \cdots b_t$ (with most
  significant bit first) we build the following gadget. The input
  vertex is $v$ and for every $2 \leq i \leq t+1$, it has two exit
  edges with accumulated probabilities $2^{-i}$. Now, if $a_i=1$
  (resp.  $b_1 =1$), one vertex with probability $2^{-(i+1)}$ is $v_1$
  (resp. $v_2$). The pending edges are redirected to $v$ itself. The
  transformation is depicted in {numref}`6-fig:simul`, assuming
  $p=11\equiv_{b} 1011$ and $q=14$ (so that
  $p-q = 3 \equiv_{b} 0011$).  For simplicity some vertices are
  represented several times to avoid intricate transitions. One can
  check that this gadget indeed simulates probabilities $\frac p q$ to
  $v_1$ and $\frac {q-p} q$ to $v_2$.

  
```{figure} ./../FigAndAlgos/6-fig:simul.png
:name: 6-fig:simul
:align: center
From binary random vertices to average ones.
```

  
  For vertices owned by either of the two players, only the first step
  of the above transformation is needed (injection of a binary tree).

  The overall transformation yields a simple stochastic game with
  $O(n(\log(n)+k))$ additional vertices, where $k$ is the maximum
  number of bits required to represent probabilities in
  $\game$. Moreover, for vertices in $\vertices'$ that were originally
  in $\vertices$, the value is preserved.

````



````{prf:definition} NEEDS TITLE AND LABEL 
  A simple stochastic game is **stopping** if for every vertex
  $v \in \vertices$ and under every \nat{pure positional} strategy profile
  $(\sigma,\tau)$, $\probm_{\sigma,\tau}^v(\Reach(\{v_\Eve,v_\Adam\})) >0$.
 

  A simple stochastic game is **stopping** if for every vertex
  $v \in \vertices$ and under every \nat{pure positional} strategy profile
  $(\sigma,\tau)$, $\probm_{\sigma,\tau}^v(\Reach(\{v_\Eve,v_\Adam\})) >0$.

````



````{prf:theorem} Reduction to stopping games
:label: 6-thm:reduction_stopping_games

For every simple stochastic game, one can build a  stopping  one, such that the value is $> \frac{1}{2}$ is the original game iff it is $>\frac{1}{2}$ in the stopping game. 

````

Caution: the transformation from general SSG to stopping
SSG does not preserve the value! more precisely, one can approximate
up to an arbitrary precision the value in an SSG by the value in a
stopping one by decreasing the fixed termination probability at each step.

````{prf:proposition} Fixed point characterisation for stopping simple stochastic games
:label: 6-prop:fixed_point_characterisation_stopping_ssg

Let $\game$ be a stopping simple stochastic game. Then, the operator $\mathfrak{F}$ has a unique fixpoint.

````

The first proof of determinacy of those games already gave a first
value iteration algorithm. This was first due to Shapley under the
hypothesis of stopping games.

## Strategy enumeration and strategy improvement algorithms

%  arguments basiques (et pas de martingales)}%\pat{\fbox{Pat} ce qui me reste \`a faire au 22 novembre : la%  la fin; des intuitions sur les vertex qui sont profitables ou pas

We have seen in Section {ref}`6-sec:determinacy` that stochastic
reachability games are positionally determined: there are optimal
 pure positional strategies for both players. We present here a
strategy improvement algorithm to compute the values at each vertex of
the game, and strategies achieving these values.

The algorithm focuses on the role of random vertices in the game, and
is based on the fact that amongst two random vertices, one of them is
likely to be better for \Eve, while the other will be better for \Adam
(or they are equally good). We will start proving a strategy
enumeration algorithm, where, given a permutation of the set of random
vertices, one computes adequate strategies for \Eve and \Adam; under
some assumptions on the permutation (liveness and self-consistency),
those strategies will be provably optimal. We will show that there
will be some live and self-consistent permutation, implying the
correctness and completeness of the algorithm. Based on this approach,
we will design a strategy improvement algorithm.

We start with the strategy enumeration algorithm
(Subsection {ref}`6-subsec:first` to Subsection {ref}`6-subsec:last`), and will
conclude with the strategy improvement algorithm
(Subsection {ref}`6-subsec:algo-strat-improv`).

%   qui suit}% \item we show that each player has an optimal memoryless strategy% \item we discuss complexity issues%   (prefix independent) $\omega$-regular winning objectives.

(6-subsubsec:first)=
### Computing almost-sure winning or almost-sure losing states

The algorithms we will present assume that games are
**normalized**, that is, there is a unique vertex denoted $\vwin$
(resp. $\vlose$) with value $1$ (resp. $0$).  This is without loss of
generality since:

*  vertices with value $1$ (resp. $0$) can be computed in
  polynomial time;
*  all vertices with value $1$ (resp. $0$) can be replaced by a
  single sink vertex $\vwin$ (resp. $\vlose$);
*  the target reachability state is set to $\vwin$.

The only point that we will discuss is the first item above. General
transformations assigning a non-stochastic parity game to each
stochastic parity game, which allow to compute almost-sure winning
states, have been developed. \pat{it would be nice to cite
  here {cite}`CJH-csl03`} However, we focus on the simpler reachability
games that we are focusing on, and we briefly describe the
construction here, inspired by {cite}`paulin-nathalie`:

*  For computing vertices with value $1$: replace a random vertex
  $v$ with an \Adam vertex $v_A$ and an \Eve vertex $v_E$. Any edge
  going to $v$ in the original game will go to $v_A$; there will be an
  edge $v_A \to v_E$ with priority $1$; if $v \to v'$ in the original
  game, then $v_A \to v'$ with priority $2$ in the new game, and $v_E
  \to v'$ with priority $1$ in the new game. We add a selfloop over
  $\Win$ with priority $2$. Then, a vertex is almost-sure winning
  (that is, has value $1$) in the original game if and only if it is
  winning in the constructed non-stochastic parity game.
*  For computing vertices with value $0$: give each random vertex
  $v$ to \Adam. Then, a vertex has value $0$ in the original game if
  and only if it is losing in the constructed non-stochastic parity
  game.

%   which transforms a stochastic parity games into a non-stochastic%   case of reachability/safety games, an ad-hoc algorithm \`a la%   $v_A$ and an \Eve vertex $v_E$. Any edge going to $v$ will go to%   $v_A \xrightarrow{2} v'$ and $v_E \xrightarrow{1} v'$. Selfloop over
From now on, we assume that the game $\game$ is normalized.
% unique vertex $\vwin$ (resp. $\vlose$) with value $1$ (resp. $0$),

### Permutation of random vertices

Assume that from vertex $v$ belonging to \Eve, one can choose between
two random vertices $v_1$ and $v_2$ such that the value of $v_1$ is
larger than the value of $v_2$, then obviously \Eve should choose to
go to $v_1$. The idea will then be for \Eve to target random vertices
with the largest possible values. We formalize this idea below

%   random vertices cannot be good for \Eve and \Adam}

We write $\Randomvertices = \{v_1,\ldots,v_k\}$. % $\vwin$
The idea will be to order random vertices in such a way that the
higher is a random vertice (in the order), the better it is for \Eve;
and conversely, the smaller is a random vertice (in the order), the
worse it is for \Adam. We fix a permutation
$\perm: \Randomvertices \to \Randomvertices$, and abusively write
$\perm_i = \perm^{-1}(v_i)$, the $i$-th element in the order defined
by $\perm$.

We define the deterministic attractor operator $\DetAtt$ as
follows. If $X \subseteq \vertices$, we define inductively the
sequence $(X_i)_{i \ge 0}$ by:

$$
\left\{
\begin{array}{rcl}
  X_0 & =& X \\
  X_{i+1} &=& X_i \cup \{v \in \Evevertices \mid \exists w \in X_i\
  \text{s.t.}\ (v,w) \in E\} \\
   && \phantom{X_i} \cup \{v \in \Adamvertices \mid \forall w \in X_i,\ 
  (v,w) \in E\ \text{implies}\ v \in X_i\}
\end{array}
\right.
$$

The deterministic attractor of $X$ is then given by:

$$
\DetAtt(X) = \lim_{i \to +\infty} X_i = \bigcup_{i =0}^{+\infty} X_i
$$

Note that since $\vertices$ is finite, the sequence $(X_i)_{i \ge 0}$
stabilizes and the above union is actually finite.  \pat{refer to the
  relevant previous chapter, there certainly is one.}

Let $\perm$ be a permutation. We define the $\perm$-regions as
deterministic attractors to the random vertices (taken in the correct
order) as follows:

$$
\left\{
\begin{array}{l}
  W_\perm^{k+1}  = \{\vwin\} \\
  W_\perm^i =
  \DetAtt(\{\perm_i,\ldots,\perm_k,\vwin\}) \setminus \bigcup_{j=i+1}^{k+1}
  W_\perm^j\quad \forall 1 \le i \le k \\ 
  W_\perm^0 = V \setminus \bigcup_{j=1}^{k+1} W_\perm^j = \{\vlose\}
\end{array}
\right.
$$

The last equality (for $W_\perm^0$) holds since (i) from vertices in
$W_\perm^0$ \Adam can enforce avoiding $\Randomvertices \cup
\{\vwin\}$ (by determinacy of non-stochastic reachability games
\pat{ref to a previous chapter?}), yielding only losing outcomes, and
(ii) $\vlose$ is the unique vertex with value $0$ (by
assumption). Later, we will write $W_\perm^{\ge j}$ for
$\bigcup_{i=j}^{k+1} W_\perm^i$.

Given $\perm$ a permutation, we define strategies $\sigma_\perm$ (for
\Eve) and $\tau_\perm$ (for \Adam) such that on $W_\perm^i$:

*  $\sigma_\perm$ is a pure and positional attractor strategy to
  $\{\perm_i,\ldots,\perm_k,\vwin\}$;
*  $\tau_\perm$ is a pure and positional trapping strategy avoiding
  $\{\perm_{i+1},\ldots,\perm_k,\vwin\}$.

Those two strategies obviously exist: $\sigma_\perm$ exists by
definition of the deterministic attractor, while $\tau_\perm$ exists
by determinacy of reachability games (if a vertex is not winning for
\Eve for a reachability objective, then it is winning for \Adam for
the corresponding safety objective).

We can then define for every $v \in \vertices$:

$$
\begin{array}{rcl}
\val_\perm(v) &=& \probm_{\sigma_\perm,\tau_\perm}^v(\Reach(\Win))
\end{array}
$$

which can be easily computed using systems of linear
equations.

The rest of this section is devoted to a proof of the following
result, which uses only basic arguments:

````{prf:theorem} NEEDS TITLE AND LABEL 
  \label{6-thm:corr-strat-improv}
  There is a permutation $\perm$ such that $\sigma_\perm$ is optimal
  for \Eve and $\tau_\perm$ is optimal for \Adam. Given a permutation
  $\perm$, we can check in polynomial time whether $\sigma_\perm$ and
  $\tau_\perm$ are optimal.
 

  \label{6-thm:corr-strat-improv}
  There is a permutation $\perm$ such that $\sigma_\perm$ is optimal
  for \Eve and $\tau_\perm$ is optimal for \Adam. Given a permutation
  $\perm$, we can check in polynomial time whether $\sigma_\perm$ and
  $\tau_\perm$ are optimal.

````

We will explain in Subsection {ref}`6-subsec:algo-strat-improv` how this
theorem can be turned into a strategy improvement algorithm for
computing values and optimal strategies in stochastic reachability
games.


### Live and self-consistent permutations


We say that a permutation $\perm$ is **self-consistent** whenever:

$$
\val_\perm(\perm_1) \le \val_\perm(\perm_2) \le \ldots \le \val_\perm(\perm_k)
$$

That is, the order given by $\perm$ coincides with the preference of
\Eve.

We say $\perm$ is **live** whenever for every $1 \le i \le k$:

$$
\delta(\perm_i)\big(W_\perm^{\ge i+1}\big)>0
$$

That is, there is a direct move from $\perm_i$ to one of the vertices
in larger attractors. In particular, with positive probability, one
goes closer to $\vwin$ and hence eventually reach $\vwin$.

\medskip We will show that $\perm$-strategies associated with a live
and self-consistent permutation $\perm$ are optimal for both players.
And that such a permutation always exists. We start with the
correctness, and will turn to the existence later.


### Correctness of live and self-consistent permutations

% any further assumption on $\perm$.%   \label{stoch:lemma1}%   \item $\val_\perm(\vlose) = 0$ and $\val_\perm(\vwin) = 1$;%     $\val_\perm(v) = \val_\perm(\perm_i)$;%     \val_\perm(\sigma_\perm(v))$;%     \val_\perm(\tau_\perm(v))$;%       \text{s.t.}\ (v,w) \in E} \delta(v)(w) \cdot \val_\perm(w)$.% \end{lemma}
%   The first item is obvious.
  %   vertex, the strategy profile $(\sigma_\perm,\tau_\perm)$ generates a%   from $v$ when applying $(\sigma_\perm,\tau_\perm)$. By definition of%   $\tau_\perm$ (trapping strategy avoiding%   be $\perm_i$. According values follow, proving the second item.
%   attractor strategy), $\sigma_\perm(v) \in W_\perm^i \cup%   W_\perm^{\ge i+1}$, $\sigma_\perm(v) \notin%   W_\perm^i \cup \{\perm_i\} = W_\perm^i$, and we get that%   (third item).
%   trapping strategy), $\tau_\perm(v) \notin%   W_\perm^i$, we nevertheless have that $\tau_\perm(v) \in W_\perm^i%   W_\perm^i \cup \{\perm_i\} = W_\perm^i$. Hence $\val_\perm(v) =% \end{proof}


We first give some properties always satisfied by strategies
$\sigma_\perm$ and $\tau_\perm$ without any condition on $\perm$, and
refine these properties to show that $\sigma_\perm$ and $\tau_\perm$
are (local) best responses to each others, when the permutation is
self-consistent.

````{prf:lemma} NEEDS TITLE AND LABEL 
  \label{stoch:lemma2}
  We write (\ddag) for the assumption that $\perm$ is self-consistent.
  
  
1.  $\val_\perm(\vlose) = 0$ and $\val_\perm(\vwin) = 1$;
  
2.  for every $1 \le i \le k$, for every $v \in W_\perm^i$,
    $\val_\perm(v) = \val_\perm(\perm_i)$;
  
3.  For every $v \in \Evevertices$,
    

$$
    \val_\perm(v) = \val_\perm(\sigma_\perm(v)) \stackrel{(\ddag)}{=}
    \max_{w\ \text{s.t.}\ (v,w) \in E} \val_\perm(w)
    $$

  
4.  For every $v \in \Adamvertices$,
    

$$
    \val_\perm(v) = \val_\perm(\tau_\perm(v)) \stackrel{(\ddag)}{=}
    \min_{w\ \text{s.t.}\ (v,w) \in E} \val_\perm(w)
    $$

       
5.  For every $v \in \Randomvertices$, $\val_\perm(v) = \sum_{w\
      \text{s.t.}\ (v,w) \in E} \delta(v)(w) \cdot \val_\perm(w)$.
  
 

  \label{stoch:lemma2}
  We write (\ddag) for the assumption that $\perm$ is self-consistent.
  
  
1.  $\val_\perm(\vlose) = 0$ and $\val_\perm(\vwin) = 1$;
  
2.  for every $1 \le i \le k$, for every $v \in W_\perm^i$,
    $\val_\perm(v) = \val_\perm(\perm_i)$;
  
3.  For every $v \in \Evevertices$,
    

$$
    \val_\perm(v) = \val_\perm(\sigma_\perm(v)) \stackrel{(\ddag)}{=}
    \max_{w\ \text{s.t.}\ (v,w) \in E} \val_\perm(w)
    $$

  
4.  For every $v \in \Adamvertices$,
    

$$
    \val_\perm(v) = \val_\perm(\tau_\perm(v)) \stackrel{(\ddag)}{=}
    \min_{w\ \text{s.t.}\ (v,w) \in E} \val_\perm(w)
    $$

       
5.  For every $v \in \Randomvertices$, $\val_\perm(v) = \sum_{w\
      \text{s.t.}\ (v,w) \in E} \delta(v)(w) \cdot \val_\perm(w)$.
  

````


````{admonition} Proof
:class: dropdown tip


  The first item is obvious.
  
  For every $v \in W_\perm^i$, up to the first visit to a random
  vertex, the strategy profile $(\sigma_\perm,\tau_\perm)$ generates a
  unique path. So we can speak of the first random vertex encountered
  from $v$ when applying $(\sigma_\perm,\tau_\perm)$. By definition of
  $\sigma_\perm$ (attractor to $\{\perm_i,\ldots,\perm_k,\vwin\}$) and
  $\tau_\perm$ (trapping strategy avoiding
  $\{\perm_{i+1},\ldots,\perm_k,\vwin\}$), this random vertex can only
  be $\perm_i$. According values follow, proving the second item.

  Assume $v \in \Evevertices \cap W_\perm^i$.  By definition of
  $\sigma_\perm$ (being an attractor strategy), $\sigma_\perm(v) \in
  W_\perm^i \cup \{\perm_i,\ldots,\perm_k,\vwin\}$. Dually, since $v
  \notin W_\perm^{\ge i+1}$, $\sigma_\perm(v) \notin
  \{\perm_{i+1},\ldots,\perm_k,\vwin\}$. Hence, $\sigma_\perm(v) \in
  W_\perm^i \cup \{\perm_i\} = W_\perm^i$, and we get that
  $\val_\perm(v) = \val_\perm(\perm_i) = \val_\perm(\sigma_\perm(v))$.
  Assume (towards a contradiction) that there is $w \in \vertices$
  such that $(v,w) \in E$ and $\val_\perm(w)>\val_\perm(v)$.  Since
  $\val_\perm(w) > \val_\perm(v) = \val_\perm(\perm_i)$, by
  self-consistence, it is the case that $w \in W_\perm^j$ with $j > i$
  (with $\val_\perm(w) = \val_\perm(\perm_j)$). But then, we can
  deduce that $v \in \DetAtt(w) \subseteq
  \DetAtt(\{\perm_j,\ldots,\perm_k,\vwin\})$, which is not the case,
  since $v \notin W_\perm^{\ge i+1} \supseteq W_\perm^j$. There is
  therefore a contradiction, and we can conclude that $\val_\perm(v) =
  \max_{w\ \text{s.t.}\ (v,w) \in E} \val_\perm(w)$.

  Assume $v \in \Adamvertices \cap W_\perm^i$. By definition of
  $\sigma_\perm$ (being a trapping strategy), $\tau_\perm(v) \notin
  \{\perm_{i+1},\ldots,\perm_k,\vwin\}$. However since $v \in
  W_\perm^i$, we nevertheless have that $\tau_\perm(v) \in W_\perm^i
  \cup \{\perm_i,\ldots,\perm_k,\vwin\}$, hence $\tau_\perm(v) \in
  W_\perm^i \cup \{\perm_i\} = W_\perm^i$. Hence $\val_\perm(v) =
  \val_\perm(\perm_i) = \val_\perm(\tau_\perm(v))$.  Assume (towards a
  contradiction) that there is $w \in \vertices$ such that $(v,w) \in
  E$ and $\val_\perm(w)<\val_\perm(v)$. As in the previous item, by
  self-consistence, $w \in W_\perm^j$ with $j<i$. But, $v$ can only be
  in a deterministic attractor if all its successors already are. This
  contradicts the fact that $w \in W_\perm^j$, hence $w \notin
  W_\perm^{\ge j+1} \supseteq W_\perm^i$. Hence, we conclude that
  $\val_\perm(v) = \min_{w\ \text{s.t.}\ (v,w) \in E} \val_\perm(w)$.

  The fifth item is straightforward hence omitted.  \qed

````

As a consequence of {prf:ref}`6-lem:lemma2`, we get that $\val_\perm$
is a fixpoint of Bellman's equations, hence it is larger than (or
equal to) the least fixpoint of Bellman's equations, that is $\val^*$:%  utilis\'e la notation $\val^*$ avant}

````{prf:corollary} NEEDS TITLE AND LABEL 
  Assume $\perm$ is self-consistent.  Then for every $v \in
  \vertices$, $\val^*(v) \le \val_\perm(v)$.
 

  Assume $\perm$ is self-consistent.  Then for every $v \in
  \vertices$, $\val^*(v) \le \val_\perm(v)$.

````

The converse inequality is not true for general or self-consistent
permutations, but will require the liveness property. One of the main
advantages of a live permutation $\perm$ is that it induces a
stopping MDP when \Eve plays according to $\sigma_\perm$: \Adam
will not be able to prevent the game converging to $\vlose$ and $\vwin$.

````{prf:lemma} NEEDS TITLE AND LABEL 
  \label{stoch:lemma:stopping}
  Let $\perm$ be a live permutation. Then, for every \Adam's strategy
  $\tau$, for every vertex $v$:
  

$$
  \probm^v_{\sigma_\perm,\tau} (\Reach(\{\vlose,\vwin\})) = 1
  $$

 

  \label{stoch:lemma:stopping}
  Let $\perm$ be a live permutation. Then, for every \Adam's strategy
  $\tau$, for every vertex $v$:
  

$$
  \probm^v_{\sigma_\perm,\tau} (\Reach(\{\vlose,\vwin\})) = 1
  $$


````


````{admonition} Proof
:class: dropdown tip

  We make use of the progress property induced by a live permutation.
  Let
  

$$
  \alpha = \min_{1 \le i \le k} \delta(\perm_i) \big(W_\perm^{\ge
    i+1}\big)
  $$

  By definition of a live permutation, $\alpha>0$.

  We write $V_i$ for the random variable representing the $i$-th state
  of a run.
   By definition of $\alpha$, for every $v \in \vertices$, for every $1
  \le i \le k$ and for every $l \ge 0$,
  

$$
  \probm^v_{\sigma_\perm,\tau}\Big(V_{l+1} \in W_\perm^{\ge i+1} \mid
  V_l = \perm_i\Big) \ge \alpha
  $$

  Also, for every $1 \le i \le k$, for every $v \in \vertices$, for
  every $l \ge 0$,
  

$$
  \probm^v_{\sigma_\perm,\tau}\Big(\exists h < |W_\perm^i|\
  \text{s.t.}\ V_{l+h} \in \{\perm_i,\ldots,\perm_k,\vwin\} \mid V_l
  \in W_\perm^i\Big)=1
  $$

  since $\sigma_\perm$ plays according to attractor strategies in
  according subsets of vertices.

  Hence we deduce that for every $v \in \vertices$, for every $l \ge
  0$,
  

$$
  \probm^v_{\sigma_\perm,\tau}\Big(V_{l+|\vertices|}=\vwin \mid V_l
  \ne \vlose\Big) \ge \alpha^k
  $$

  which we can rewrite as:
  

$$
  \probm^v_{\sigma_\perm,\tau}\Big(\forall 0 \le l \le l' \le
  l+|\vertices|,\ V_{l'} \ne \vwin \mid V_l \ne \vlose\Big) \le
  (1-\alpha^k)
  $$

  Iterating, we get that for every $i$, for every $v \in \vertices$,
  

$$
  \probm^v_{\sigma_\perm,\tau}\Big(\forall l \le i \cdot |\vertices|,\
  V_{l} \ne \vwin \mid V_0 \ne \vlose\Big) \le (1-\alpha^k)^i
  $$

  We  deduce that for every $v \in \vertices$,
  

$$
  \probm^v_{\sigma_\perm,\tau}(\forall l \ge 0,\ V_l \ne \vwin \mid
  V_0 \ne \vlose) = 0
  $$

  We conclude with
  

$$
  \probm^v_{\sigma_\perm,\tau}(\exists l \ge 0,\ V_l = \vwin \mid V_0
  \ne \vlose) = 1
  $$

  hence with the statement.

````


````{prf:lemma} NEEDS TITLE AND LABEL 
  Let $\perm$ be a live and self-consistent permutation.  Then for
  every $v \in \vertices$,  $\val_\perm(v) \le \val^*(v)$.%   $\sigma_\perm$ is optimal for \Eve and $\sigma_\perm$ is optimal for 

  Let $\perm$ be a live and self-consistent permutation.  Then for
  every $v \in \vertices$,  $\val_\perm(v) \le \val^*(v)$.%   $\sigma_\perm$ is optimal for \Eve and $\sigma_\perm$ is optimal for
````


````{admonition} Proof
:class: dropdown tip

  Fix a pure positional \Adam's strategy $\tau$. The tuple
  $(\probm_{\sigma_\perm,\tau}^v(\Reach(\Win)))_{v \in \vertices}$ is
  a
    solution to the following equations:
  

$$
  \left\{\begin{array}{ll} x_v =
      x_{\tau(v)} & \text{if}\ v \in \Adamvertices \\
      x_v = x_{\sigma_\perm(v)} & \text{if}\ v \in \Evevertices \\
      x_v = \sum_{w\ \text{s.t.}\ (v,w) \in E} \delta(v)(w) \cdot
      x_w  & \text{if}\ v \in \Randomvertices \\
      x_{\vwin} = 1 \\
      x_{\vlose} = 0
    \end{array}\right.
  $$

  In particular, it is a solution to the following inequations:
                 

$$
  \left\{\begin{array}{ll} 
      x_v \ge \min_{w\ \text{s.t.}\ (v,w) \in E}
      x_w & \text{if}\ v \in \Adamvertices \\
      x_v = x_{\sigma_\perm(v)}  & \text{if}\ v \in \Evevertices \\
      x_v = \sum_{w\ \text{s.t.}\ (v,w) \in E} \delta(v)(w) \cdot x_w
      & \text{if}\ v \in \Randomvertices \\
      x_{\vwin} = 1 \\
      x_{\vlose} = 0
    \end{array}\right.
  $$

  Since the MDP (when $\sigma_\perm$ has been fixed) is stopping (see {prf:ref}`6-lem:stopping`), there is no proper end-component
  (except $\{\vwin\}$ and $\{\vlose\}$), and the above system of
  inequations has a unique minimal solution, which is the unique
  solution of the same system with $=$ instead of $\ge$.

  On the other hand {prf:ref}`6-lem:lemma2` tells us that
  $(\val_\perm(v))_{v \in\vertices}$ can only be that unique
  solution. Hence, for every $v \in \vertices$:
  

$$
  \val_\perm(v) \le \probm_{\sigma_\perm,\tau}^v(\Reach(\Win))
  $$

  %   \item For every memoryless and pure \Eve's strategy $\sigma$,%     is the smallest solution to the following equations:%     \left\{\begin{array}{ll} x_v =%         x_v = x_{\tau_\perm(v)} & \text{if}\ v \in \Adamvertices \\%         x_w \\%         x_{\vlose} = 0%     \]%     

$$%           E}%         x_v = x_{\tau_\perm(v)} & \text{if}\ v \in \Adamvertices \\%         x_w \\%         x_{\vlose} = 0%     $$

%   solution. \pat{c'est bien ok ?}
%   $(\val_\perm(v))_{v \in\vertices}$ can only be that maximal%   

$$%   \probm_{\sigma,\tau_\perm}^v(\Reach(\Win))%   This shows that $\sigma_\perm$ plays optimally against $\tau_\perm$.
  Since this holds for every pure positional strategy $\tau$ of \Adam,
  we conclude that for every $v \in \vertices$,
  $\val_\perm(v) \le \val^*(v)$. \qed
       
````


````{prf:corollary} NEEDS TITLE AND LABEL 
  \label{stoch:coro}
  Let $\perm$ be a live and self-consistent permutation. Then, for
  every $v \in \vertices$, $\val^*(v) = \val_\perm(v)$.  
 

  \label{stoch:coro}
  Let $\perm$ be a live and self-consistent permutation. Then, for
  every $v \in \vertices$, $\val^*(v) = \val_\perm(v)$.  

````


### Existence of a live and self-consistent permutation


````{prf:lemma} NEEDS TITLE AND LABEL 
  \label{stoch:lemma:croissant}
  Let $\perm$ be a live permutation such that
  \[
  \val^*(\perm_1) \le \val^*(\perm_2) \le \ldots \le \val^*(\perm_k)
  $$

  Then, $\perm$ is self-consistent.
 

  \label{stoch:lemma:croissant}
  Let $\perm$ be a live permutation such that
  \[
  \val^*(\perm_1) \le \val^*(\perm_2) \le \ldots \le \val^*(\perm_k)
  $$

  Then, $\perm$ is self-consistent.

````


````{admonition} Proof
:class: dropdown tip

  We will show that for every vertex $v \in \vertices$, $\val^*(v) =
  \val_\perm(v)$. This will ne enough for proving the expected result.

  We first show a counterpart to {prf:ref}`6-lem:lemma2` for
  $\val^*$:
  
````{prf:lemma} NEEDS TITLE AND LABEL 
    Same hypotheses as {prf:ref}`6-lem:croissant`. Then:
    
    
1.  $\val^*(\vlose) = 0$ and $\val^*(\vwin) = 1$;
    
2.  for every $1 \le i \le k$, for every $v \in W_\perm^i$,
      $\val^*(v) = \val^*(\perm_i)$.
    
   

    Same hypotheses as {prf:ref}`6-lem:croissant`. Then:
    
    
1.  $\val^*(\vlose) = 0$ and $\val^*(\vwin) = 1$;
    
2.  for every $1 \le i \le k$, for every $v \in W_\perm^i$,
      $\val^*(v) = \val^*(\perm_i)$.
    
  
````

  \begin{proof}
    Notice that item 1 is obvious. 
            
    We then focus on item 2.  Assume $v \in W_\perm^i$, and define
    strategy $\sigma^*$ from $v$ as $\sigma_\perm$ (attractor strategy
    to $\{\perm_i,\ldots,\perm_k,\vwin\}$) until $\vwin$ or a random
    vertex $\pi_j$ ($j \ge i$) is reached; in the latter case, switch
    to an optimal strategy out of $\pi_j$. We obviously get that for
    every strategy $\tau$ for \Adam,
    $\probm_{\sigma^*,\tau}^v(\Reach(\{\vwin\})) \ge \min_{i \le j \le
      k}\val^*(\perm_j) = \val^*(\perm_i)$. Hence $\val^*(v) \ge
    \val^*(\perm_i)$.
    
    Conversely define strategy $\tau^*$ from $v$ as $\tau_\perm$
    (trapping strategy out of $\{\perm_{i+1},\ldots,\perm_k,\vwin\}$)
    until $\vlose$ or a random vertex $\pi_j$ ($j \le i$) is reached;
    in the latter case, switch to an optimal strategy out of
    $\pi_j$. Note that it can a priori be the case that we never hit
    $\vlose$ or a random vertex, but this is good to \Adam. However we
    can conclude that for every strategy $\sigma$ for \Eve,
    $\probm_{\sigma,\tau^*}^v(\Reach(\{\vwin\})) \le \max_{1 \le j \le
      i}\val^*(\perm_j) = \val^*(\perm_i)$. Hence
    $\val^*(v) \le \val^*(\perm_i)$.

             This allows to conclude item 2, hence the lemma.
  
````

  Both $\val^*$ and $\val_\perm$ satisfy the system of equations:
  

$$
  \left\{\begin{array}{ll} 
      x_v = x_{\perm_i} & \text{if}\ v \in W_\perm^i \\ 
                x_v = \sum_{w\ \text{s.t.}\ (v,w) \in E} \delta(v)(w) \cdot x_w
      & \text{if}\ v \in \Randomvertices \\
      x_{\vwin} = 1 \\
      x_{\vlose} = 0
    \end{array}\right.
  $$

  We can rewrite this system into:
  

$$
  \left\{\begin{array}{ll} 
      x_v = x_{\perm_i} & \text{if}\ v \in W_\perm^i \\ 
                x_{\perm_i} = \sum_{j=0}^{k+1} \delta(\perm_i)(W_\perm^j) \cdot x_{\perm_j}
      & \\
      x_{\vwin} = 1 \\
      x_{\vlose} = 0
    \end{array}\right.
  $$

  Since $\perm$ is live this system has a unique solution!  Hence
  $\val^* = \val_\perm$, and $\perm$ is self-consistent.
\end{proof}

It remains to show that there always exist  a live permutation
satisfying the hypothesis of {prf:ref}`6-lem:croissant`.

To do so, we show the following structural property of the game, which
will help building an appropriate live permutation.

````{prf:lemma} NEEDS TITLE AND LABEL 
  \label{stoch:lemma:structure}
  Let $\{\vwin\} \subseteq X \subseteq V$ be a subset of vertices, and
  $Y = V \setminus \DetAtt(X)$. Then either $Y = \{\vlose\}$, or there
  is a random vertex $v \in Y$ such that $\val^*(v) = \max\{\val^*(w)
  \mid w \in Y\}$ and $\delta(v)\Big(\DetAtt(X)\Big)>0$.
 

  \label{stoch:lemma:structure}
  Let $\{\vwin\} \subseteq X \subseteq V$ be a subset of vertices, and
  $Y = V \setminus \DetAtt(X)$. Then either $Y = \{\vlose\}$, or there
  is a random vertex $v \in Y$ such that $\val^*(v) = \max\{\val^*(w)
  \mid w \in Y\}$ and $\delta(v)\Big(\DetAtt(X)\Big)>0$.

````


````{admonition} Proof
:class: dropdown tip

    Let $Z = \textsf{Argmax}_Y (\val^*)$. We assume that there is no
  random vertex $v \in Z \cap \Randomvertices$ such that
  $\delta(v)\Big(\DetAtt(X)\Big)>0$. We will show that $Z =
  \{\vlose\}$, which will imply $Y = \{\vlose\}$. To do so, we show
  that if $v \in Z$, then $\val^*(v) = 0$.  We fix $v \in Z$, and we
  assume towards a contradiction that $\val^*(v)>0$.

  Let $\tau$ be a pure positional \Adam's strategy on $Y$ avoiding
  $\DetAtt(X)$: by definition, $\tau(Y) \subseteq Y$. Also, one can
  argue that $\tau(Z) \subseteq Z$. Indeed otherwise there is $v' \in
  Z$ such that $\tau(v') \in Y \setminus Z$. Thus, $\val^*(\tau(v')) <
  \val^*(v')$, which is not possible since $\val^*(v') = \min_{w\
    \text{s.t.}\ (v',w) \in E} \val^*(w)$ (Bellman's equations). Also
  by Bellman's equations, if $v' \in \Randomvertices \cap Z$, for
  every $w'$ such that $\delta(v')(w')>0$, $\val^*(w') =
  \val^*(v')$. By assumption, it cannot be the case that $w' \in
  \DetAtt(X)$, hence $w' \in Z$.  Let $v' \in Z \cap \Evevertices$. If
  there is $w' \notin Z$ such that $(v',w') \in E$, then it must be
  the case that $w' \in Y \setminus Z$: indeed, it cannot be the case
  that $w' \in \DetAtt(X)$, otherwise $v'$ would also be in
  $\DetAtt(X)$.

  We now define strategy $\tau'$ which plays from $v$ as $\tau$ until
  $Z$ is left, and then $\tau'$ plays an optimal strategy for \Adam.
  Let $\sigma$ be a strategy for \Eve. Under the profile
  $(\sigma,\tau')$ from $v$, either we stay forever in $Z$, or we
  leave at some \Eve's vertex $v'$ towards a vertex $w'$ with
  $\val^*(w') < \val^*(v') = \val^*(v)$ (recall the discussion
  above). We can then write:
  \begin{eqnarray*}
    \probm_{\sigma,\tau'}(\Reach(\{\vwin\})) &=&
    \probm_{\sigma,\tau'}(\Reach(\{\vwin\}) \mid \text{stays in}\  Z\
    \text{forever}) \cdot  \probm_{\sigma,\tau'}(\text{stays in}\  Z\
    \text{forever}) \\ 
    && + \sum_{(v',w') \in (Z \times (Y \setminus Z) \cap E)} 
    \probm_{\sigma,\tau'}(\Reach(\{\vwin\}) \mid
    \text{leave via}\  (v',w')) \cdot
    \probm_{\sigma,\tau'}(\text{leave via}\  (v',w')) \\
    & = & 0 \cdot \probm_{\sigma,\tau'}(\text{stays in}\  Z\
    \text{forever}) + \sum_{(v',w') \in (Z \times (Y \setminus Z) \cap
      E)}  \val^*(w') \cdot
    \probm_{\sigma,\tau'}(\text{leave via}\  (v',w')) \\
    & \le & \beta
  \end{eqnarray*}
  where $\beta = \max \{\val^*(w) \mid w \in Y \setminus Z\} <
  \val^*(v)$.  Hence, we get $\val^*(v) \le \beta < \val^*(v)$. This
  is a contradiction.

````


````{prf:lemma} NEEDS TITLE AND LABEL 
  \label{stoch:lemma-existence}
  There is a live and self-consistent permutation.
 

  \label{stoch:lemma-existence}
  There is a live and self-consistent permutation.

````


````{admonition} Proof
:class: dropdown tip

  We will define a permutation $\perm$ inductively, by repeatedly
  using {prf:ref}`6-lem:structure`.  For every $i =k, \ldots
  ,1$ we define $\perm_i$ by applying
  Lemma {prf:ref}`6-lem:structure` to $X =
  \{\perm_{i+1},\ldots,\perm_k,\vwin\}$.

  By construction,
  
  *  $\val^*(\perm_i) = \max \{\val^*(v) \mid v \in V \setminus
    \DetAtt(\{\perm_{i+1},\ldots,\perm_k,\vwin\})\}$;
  *      $\delta(\perm_i)\Big(\DetAtt(\{\perm_{i+1},\ldots,\perm_k,\vwin\})\Big)
    >0$
  
  Hence, $\perm$ is live, and the hypothesis of {prf:ref}`6-lem:croissant` is satisfied. Hence $\perm$ is
  self-consistent. This concludes the proof.

````


### Complexity analysis

To obtain the polynomial-time complexity claimed in {prf:ref}`6-thm:corr-strat-improv`, we realize that once a
permutation $\perm$ is fixed, computing the sets $W_\pi^i$ can be done
in polynomial time (those are simple attractors), and corresponding
strategies $\sigma_\perm$ and $\tau_\perm$ can be simultaneously
computed as well. Now, computing $\val_\perm$ reduces to computing the
probability to reach $\vwin$ in the induced Markov chain, which is
known to be possible in polynomial time. Note that we could improve
the complexity by reducing the Markov chain to a Markov chain where
the only vertices are $\Randomvertices \cup \{\vlose,\vwin\}$, but
this would only marginally impact the overall complexity.

(6-subsubsec:last)=
### Strategy enumeration algorithm

Thanks to {prf:ref}`6-thm:corr-strat-improv`, we get an algorithm
to compute values and optimal strategies for both players in a
stochastic reachability game: enumerate permutations of random
vertices, and for each of them, check whether it is live and
self-consistent; stop when one is found.However, as such, this requires to enumerate all permutations of
random vertices, and there are $|\Randomvertices|!$ of them. Hence the
overall complexity of finding the values and the optimal strategies is
exponential.



(6-subsubsec:algo-strat-improv)=
### Strategy improvement algorithm
%  dig\'erer... j'esp\`ere qu'il n'y a pas d'erreur}

We will describe a strategy improvement algorithm, which may avoid
enumerating all permutations. Note that there is nevertheless no
guarantee that the overall complexity will be betther than the
strategy enumeration algorithm.

The algorithm consists in the following steps:

*  Initialization step: Compute a live permutation $\perm$
*  Improvement step: Given a live permutation $\perm$, compute a
  live and self-consistent permutation in $\game[\sigma_\perm]$, the
  restriction of game $\game$ where $\Eve$ always plays according to
  $\sigma_\perm$.
Below, since we will speak of games $\game$, $\game[\sigma_\perm]$ and
even $\game[\sigma_{\perm'}]$, when speaking about the value of the
game, we will specify the game in which we consider the value. For
instance, $\val^*_{\game[\sigma_\perm]}$ denotes the value vector of the game
$\game[\sigma_\perm]$, and $\val_{\game,\perm}$ denotes the former
$\val_\perm$.

We will argue (though not with full details) that the following
properties are satisfied by the algorithm:

1.  An initial live permutation can be computed in polynomial time.

2.  For every live permutation $\perm$, one can compute in
  polynomial time a live and self-consistent permutation $\perm'$ in
  $\game[\sigma_\perm]$.

3.  The above-mentioned permutation $\perm'$ is live in $\game$ as
  well.

4.  The improvement step really implements some improvement:
  
  *  $\val^*_{\game[\sigma_\perm]} \le
    \val^*_{\game[\sigma_{\perm'}]}$, and
  *  $\val^*_{\game[\sigma_\perm]} =
    \val^*_{\game[\sigma_{\perm'}]}$ implies that $\perm'$ is
    self-consistent.
  

The first property is based on the construction of {prf:ref}`6-lem:existence`.

For the second property, we know as a consequence of {prf:ref}`6-thm:corr-strat-improv` that there exists a live and
self-consistent permutation $\perm'$ in $\game[\sigma_{\perm}]$,
provided we prove that $\game[\sigma_{\perm}]$ is normalized (this was
a general assumption of the approach, mentioned in Subsection {ref}`6-subsec:first`). This is actually the case since
every proper vertex $v$ can be proven to have a value strictly within
$0$ and $1$ in $\game[\sigma_{\perm}]$ (it is indeed smaller in
$\game[\sigma_{\perm}]$ than in $\game$ since $\game[\sigma_{\perm}]$
offers less options to \Eve, and it cannot be $0$, using a proof
similar to that of {prf:ref}`6-lem:stopping`).% nevertheless assumes the underlying game be normalized. So it is just% argue that every vertex $v \ne \vwin,\vlose$ is such that its value in% value in game $\game[\sigma_\perm]$ is bounded from above by the value% $1$ in $\game[\sigma_\perm]$; using a proof similar to the proof of% $\vlose$ can have value $0$. 
Now, since $\game[\sigma_\perm]$ turns out to be a Markov decision
process, values of all random vertices can be computed in polynomial
time using linear programming; then we can apply a construction
similar to that of {prf:ref}`6-lem:existence` to get a live and
self-consistent permutation $\perm'$ in $\game[\sigma_\perm]$. This
yields a polynomial time algorithm to compute $\perm'$.

For the third property, we realize that% permutation $\perm'$ in $\game[\sigma_\perm]$ is live in $\game$:
$\perm'$-regions in $\game[\sigma_\perm]$ are included in
$\perm'$-regions in $\game$, which immediately implies the result.

The last property is harder to argue; it expresses the fact that the
new permutation $\perm'$ improves over $\perm$. % the proof, but not full details.

````{admonition} Proof
:class: dropdown tip
  Since $\perm'$ is live and self-consistent in $\game[\sigma_\perm]$,
  by~\cref{6-cor:}, extending the previous notations, we
  get that
  $\val^*_{\game[\sigma_\perm]} =
  \val_{\game[\sigma_\perm],\perm'}$. Now, since $\perm'$ is
  self-consistent in $\game[\sigma_\perm]$, we deduce that
  

$$
    \val^*_{\game[\sigma_\perm]}(\perm'_1) \le
    \val^*_{\game[\sigma_\perm]}(\perm'_2) \le \dots \le
    \val^*_{\game[\sigma_\perm]}(\perm'_k)
  $$


  We consider the following family of strategies for \Eve in $\game$:
  for every $n$, $\sigma^{(n)}$ is the strategy where \Eve plays
  according to $\sigma_{\perm'}$ up to its $n$-th visit to a random
  vertex, and then switches to $\sigma_\perm$. 

````
 
We can then prove:   
````{prf:lemma} Converge of the sequence of values
:label: 6-lem:convergence_sequence_values

The sequence $(\val_{\game,\sigma^{(n)}})_n$ is non-decreasing.

````

  
````{admonition} Proof
:class: dropdown tip

    We do the proof by induction on $n$.  We focus on $n=0$, and prove
    below that $\val_{\game,\sigma^{(1)}} \ge
    \val_{\game,\sigma^{(0)}}$. First notice that $\sigma^{(0)} =
    \sigma_\perm$.

    First, notice that $v \in W_{\game,\perm'}^i$ for some $i$, and $v
    \in W_{\game[\sigma_\perm],\perm'}^j$ for some $j$. This
    $game[\perm]$ restricts actions of \Eve, we immediately get $i \ge
    j$. Hence, applying the line of inequalities at the beginning of
    the proof of the larger lemma,
    $\val^*_{\game[\sigma_\perm]}(\perm'_j) \le
    \val^*_{\game[\sigma_\perm]}(\perm'_i)$.

    If \Eve plays with $\sigma^{(1)}$, the definition of
    $\sigma_{\perm'}$ ensures that the first random vertex (or
    terminal vertex) which is visited when starting in $v$ belongs to
    $\{\perm'_i,\perm'_{i+1},\dots,\perm'_k,\vwin\}$, so since from
    that vertex, $\sigma^{(1)}$ plays according to $\sigma_\perm$, we
    get:
    

$$
    \val_{\game,\sigma^{(1)}}(v) \ge \min
    \{\val^*_{\game[\sigma_\perm]}(\perm'_i),
    \val^*_{\game[\sigma_\perm]}(\perm'_{i+1}),\dots,
    \val^*_{\game[\sigma_\perm]}(\perm'_k),1\} \ge
    \val^*_{\game[\sigma_\perm]}(\perm'_i)
    $$

    since $\val^*_{\game[\sigma_\perm]} = \val_{\game,\sigma_\perm}$.

    Now, when playing $\sigma_\perm = \sigma^{(0)}$ from $v$, 

    Thanks to  {prf:ref}`6-lem:lemma2`, since $v \in
    W_{\game[\sigma_\perm],\perm'}^j$,
    $\val_{\game[\sigma_\perm],\perm'}(v) =
    \val_{\game[\sigma_\perm],\perm'}(\perm'_j)$ and hence (as argued
    in the proof of the larger lemma,
    $\val_{\game[\sigma_\perm],\perm'} =
    \val^*_{\game[\sigma_\perm]}$), $\val^*_{\game[\sigma_\perm]}(v) =
    \val^*_{\game[\sigma_\perm]}(\perm'_j)$. We conclude that:
    

$$
    \val_{\sigma_\perm}(v) = \val^*_{\game[\sigma_\perm]}(v) \le
    \val^*_{\game[\sigma_\perm]}(\perm'_j) \le
    \val^*_{\game[\sigma_\perm]}(\perm'_i) \le
    \val_{\game,\sigma^{(1)}}(v)
    $$

    which concludes the initial case for the induction.

    \smallskip The inductive step is then rather straightforward: the
    two strategies $\sigma^{(n+2)}$ and $\sigma^{(n+1)}$ coincide
    until a first random vertex is encounted, and then the first one
    switches to $\sigma^{(n+1)}$ while the other switches to
    $\sigma^{(n)}$. Hence, using the induction hypothesis that
    $\sigma^{(n+1)}$ is better for \Eve than $\sigma^{(n)}$, we can
    conclude.
  
````

  Let $\tau$ be an \Adam's strategy. Since $\perm'$ has been shown to
  be live in $\game$, applying  {prf:ref}`6-lem:stopping`, we
  get that: $\probm^v_{\sigma_{\perm'},\tau} (\Reach(\{\vwin\})) =
  \probm^v_{\sigma_{\perm'},\tau} (\neg\Reach(\{\vlose\}))$. This last
  probability value coincides with $\lim_{n \to +\infty}
  \probm^v_{\sigma_{\perm'},\tau} (\neg\Reach_{\le n}(\{\vlose\}))$,
  the probability to not reach $\vlose$ for the first $n$ visits to a
  random vertex; for these $n$ first visits, $\sigma_{\perm'}$
  coincides with $\sigma^{(n)}$, hence
  $\probm^v_{\sigma_{\perm'},\tau} (\Reach(\{\vwin\})) \ge \lim_{n\to
    +\infty} \probm^v_{\sigma^{(n)},\tau} (\Reach(\{\vwin\}))$. By
  definition of value in a game, this last term is larger than or
  equal to $\lim_{n \to+\infty}\val_{\game,\sigma^{(n)}}$, hence
  $\lim_{n \to+\infty}\val_{\game,\sigma^{(n)}} \le
  \val_{\game,\perm'}$.

  We conclude that:
  

$$
  \val^*_{\game[\sigma_\perm]} = \val_{\game,\sigma^{(0)}} \le
  \val_{\game,\sigma^{(1)}} \le \val_{\game,\sigma^{(2)}} \le \dots\le
  \lim_{n \to +\infty} \val_{\game,\sigma^{(n)}} \le
  \val^*_{\game[\sigma_{\perm'}]}
  $$


  \medskip Assume now that $\val^*_{\game[\sigma_\perm]} =
  \val^*_{\game[\sigma_{\perm'}]}$. Then applying the first line of
  inequalities above, we get:
  

$$
  \val^*_{\game[\sigma_{\perm'}]}(\perm'_1) \le
  \val^*_{\game[\sigma_{\perm'}]}(\perm'_2) \le \dots \le
  \val^*_{\game[\sigma_{\perm'}]}(\perm'_k)
  $$

  Now, the strategy $\tau_{\perm'}$ is precisely the optimal strategy
  against $\sigma_{\perm'}$ \pat{Not so sure of the argument, it is
    not argued that way in GH09}, hence for every vertex $v$:
  

$$
  \val^*_{\game[\sigma_{\perm'}]}(v) = \inf_\tau
  \probm^v_{\sigma_{\perm'},\tau} (\Reach(\{\vwin\})) =
  \probm^v_{\sigma_{\perm'},\tau_{\perm'}} (\Reach(\{\vwin\})) =
  \val_{\game,\perm'}
  $$

  We deduce that
  

$$
  \val_{\game,\perm'}(\perm'_1) \le \val_{\game,\perm'}(\perm'_2) \le
  \dots \le \val_{\game,\perm'}(\perm'_k)
  $$

  which is precisely the definition of a self-consistent permutation
  in $\game$, so we are done.
  \end{proof}

This last property ensures both termination of the algorithm: indeed,
it is ensured by the finiteness of the number of permutations, and by
the improvement characterization above. Note that it may be the case
that in the worst-case, all permutations will be enumerated. No lower
nor upper bound is known no far.



## Mathematical programming

From Condon'93 resolution of stochastic games (assuming they are
stopping, and with 2 successors only, and proba all 1/2) to quadratic
programming.
