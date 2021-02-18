(6-sec:algos)=
# Algorithms


```{math}
\newcommand{\probm}{\mathbb{P}}
\newcommand{\vwin}{\ensuremath{v_{\textsc{win}}}}
\newcommand{\vlose}{\ensuremath{v_{\textsc{lose}}}}
\newcommand{\Adamvertices}{\VA}
\newcommand{\Evevertices}{\VE}
\newcommand{\Randomvertices}{\vertices_{\text{Rand}}}
\newcommand{\perm}{\pi}
\newcommand{\DetAtt}{\ensuremath{**DetAtt**}}
\newcommand{\nats}{\mathbb{N}}\newcommand{\Eve}{\textrm{Eve}}
\newcommand{\Adam}{\textrm{Adam}}
\newcommand{\game}{\mathcal{G}}
\newcommand{\arena}{\mathcal{A}}
\newcommand{\vertices}{V}
\newcommand{\VE}{V_\mEve}
\newcommand{\VA}{V_\mAdam}
\newcommand{\Win}{\textrm{Win}}
\newcommand{\val}{\Value}
\newcommand{\Reach}{\mathtt{Reach}}
\newcommand{\mEve}{\mathrm{Eve}}
\newcommand{\mAdam}{\mathrm{Adam}}
\newcommand{\Value}{\textrm{val}}
```


%\item Reduction to stopping games (Condon92)

%  algorithm?

%  possibilities, like the one converge-from-below in Condon93, or

%\item mathematical programming: algo taken from Condon93?

%\end{itemize}

We have shown that stochastic reachability games are central to the (quantitative) analysis of stochastic games. 
We have indeed reduced the quantitative analysis of all kinds of stochastic games to stochastic reachability games. We will now present algorithms for stochastic reachability games.

## Value iteration


````{prf:definition} NEEDS TITLE AND LABEL 
  A stochastic arena $\mathcal{A}= (VE,\delta)$ is said to be
  **simple** if
  
  *  $V$ contains two sink vertices $v_{\Eve}$ and $v_{\textrm{Adam}$;
  *  every non-sink vertex
    $v \in V\setminus \{v_{\Eve},v_{\textrm{Adam}\}$ has two
    successors;
  *  every random vertex $v \in \vertices_{\text{Rand}} is an
    **average vertex**, that is, for every vertex
    $v'\in V, $(v,v') \in E$ implies
    $\delta(v,v')=\frac{1}{2}$.
  
 

  A stochastic arena $\mathcal{A}= (VE,\delta)$ is said to be
  **simple** if
  
  *  $V$ contains two sink vertices $v_{\Eve}$ and $v_{\textrm{Adam}$;
  *  every non-sink vertex
    $v \in V\setminus \{v_{\Eve},v_{\textrm{Adam}\}$ has two
    successors;
  *  every random vertex $v \in \vertices_{\text{Rand}} is an
    **average vertex**, that is, for every vertex
    $v'\in V, $(v,v') \in E$ implies
    $\delta(v,v')=\frac{1}{2}$.
  

````

With a simple stochastic arena is naturally associated the
reachability objective $\mathtt{Reach}\{v_{\Eve}\})$. The resulting game is
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

  Let $\mathcal{A}= (VE,\delta)$ be an arbitrary stochastic
  arena. First of all, all vertices in $\textrm{Win} are merged into a single
  sink vertex $v_\Eve$.

  Assume $v \in \vertices_{\text{Rand}} is a random vertex with $k$ outgoing
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
  vertices only.  We let $t \in\mathbb{N}}\newcommand{\Eve}{\textrm{Eve} be such that
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
  $\mathcal{G}. Moreover, for vertices in $V$ that were originally
  in $V, the value is preserved.

````



````{prf:definition} NEEDS TITLE AND LABEL 
  A simple stochastic game is **stopping** if for every vertex
  $v \in V and under every \nat{pure positional} strategy profile
  $(\sigma,\tau)$, $\probm_{\sigma,\tau}^v(\mathtt{Reach}\{v_\Eve,v_\textrm{Adam}})) >0$.
 

  A simple stochastic game is **stopping** if for every vertex
  $v \in V and under every \nat{pure positional} strategy profile
  $(\sigma,\tau)$, $\probm_{\sigma,\tau}^v(\mathtt{Reach}\{v_\Eve,v_\textrm{Adam}})) >0$.

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

Let $\mathcal{G} be a stopping simple stochastic game. Then, the operator $\mathfrak{F}$ has a unique fixpoint.

````

The first proof of determinacy of those games already gave a first
value iteration algorithm. This was first due to Shapley under the
hypothesis of stopping games.




## Strategy enumeration and strategy improvement algorithms


%  arguments basiques (et pas de martingales)}

%\pat{\fbox{Pat} ce qui me reste \`a faire au 22 novembre : la

%  la fin; des intuitions sur les vertex qui sont profitables ou pas


We have seen in Section {ref}`6-sec:determinacy` that stochastic
reachability games are positionally determined: there are optimal
 pure positional strategies for both players. We present here a
strategy improvement algorithm to compute the values at each vertex of
the game, and strategies achieving these values.

The algorithm focuses on the role of random vertices in the game, and
is based on the fact that amongst two random vertices, one of them is
likely to be better for \Eve, while the other will be better for \textrm{Adam}(or they are equally good). We will start proving a strategy
enumeration algorithm, where, given a permutation of the set of random
vertices, one computes adequate strategies for \Eve and \textrm{Adam} under
some assumptions on the permutation (liveness and self-consistency),
those strategies will be provably optimal. We will show that there
will be some live and self-consistent permutation, implying the
correctness and completeness of the algorithm. Based on this approach,
we will design a strategy improvement algorithm.

We start with the strategy enumeration algorithm
(Subsection {ref}`6-subsec:first` to Subsection {ref}`6-subsec:last`), and will
conclude with the strategy improvement algorithm
(Subsection {ref}`6-subsec:algo-strat-improv`).


%   qui suit}

% \item we show that each player has an optimal memoryless strategy

% \item we discuss complexity issues

%   (prefix independent) $\omega$-regular winning objectives.


(6-subsubsec:first)=
### Computing almost-sure winning or almost-sure losing states

The algorithms we will present assume that games are
**normalized**, that is, there is a unique vertex denoted $\ensuremath{v_{\textsc{win}}}
(resp. $\ensuremath{v_{\textsc{lose}}}) with value $1$ (resp. $0$).  This is without loss of
generality since:

*  vertices with value $1$ (resp. $0$) can be computed in
  polynomial time;
*  all vertices with value $1$ (resp. $0$) can be replaced by a
  single sink vertex $\ensuremath{v_{\textsc{win}}} (resp. $\ensuremath{v_{\textsc{lose}}});
*  the target reachability state is set to $\ensuremath{v_{\textsc{win}}}.

The only point that we will discuss is the first item above. General
transformations assigning a non-stochastic parity game to each
stochastic parity game, which allow to compute almost-sure winning
states, have been developed. \pat{it would be nice to cite
  here {cite}`CJH-csl03`} However, we focus on the simpler reachability
games that we are focusing on, and we briefly describe the
construction here, inspired by {cite}`paulin-nathalie`:

*  For computing vertices with value $1$: replace a random vertex
  $v$ with an \textrm{Adam}vertex $v_A$ and an \Eve vertex $v_E$. Any edge
  going to $v$ in the original game will go to $v_A$; there will be an
  edge $v_A \to v_E$ with priority $1$; if $v \to v'$ in the original
  game, then $v_A \to v'$ with priority $2$ in the new game, and $v_E
  \to v'$ with priority $1$ in the new game. We add a selfloop over
  $\textrm{Win} with priority $2$. Then, a vertex is almost-sure winning
  (that is, has value $1$) in the original game if and only if it is
  winning in the constructed non-stochastic parity game.
*  For computing vertices with value $0$: give each random vertex
  $v$ to \textrm{Adam} Then, a vertex has value $0$ in the original game if
  and only if it is losing in the constructed non-stochastic parity
  game.



%   which transforms a stochastic parity games into a non-stochastic

%   case of reachability/safety games, an ad-hoc algorithm \`a la


%   $v_A$ and an \Eve vertex $v_E$. Any edge going to $v$ will go to

%   $v_A \xrightarrow{2} v'$ and $v_E \xrightarrow{1} v'$. Selfloop over



From now on, we assume that the game $\mathcal{G} is normalized.

% unique vertex $\ensuremath{v_{\textsc{win}}} (resp. $\ensuremath{v_{\textsc{lose}}}) with value $1$ (resp. $0$),


### Permutation of random vertices

Assume that from vertex $v$ belonging to \Eve, one can choose between
two random vertices $v_1$ and $v_2$ such that the value of $v_1$ is
larger than the value of $v_2$, then obviously \Eve should choose to
go to $v_1$. The idea will then be for \Eve to target random vertices
with the largest possible values. We formalize this idea below


%   random vertices cannot be good for \Eve and \textrm{Adam}

We write $\vertices_{\text{Rand}}= \{v_1,\ldots,v_k\}$. 

% $\ensuremath{v_{\textsc{win}}}
The idea will be to order random vertices in such a way that the
higher is a random vertice (in the order), the better it is for \Eve;
and conversely, the smaller is a random vertice (in the order), the
worse it is for \textrm{Adam} We fix a permutation
$\pi \vertices_{\text{Rand}}\to \vertices_{\text{Rand}}, and abusively write
$\perm_i = \pi{-1}(v_i)$, the $i$-th element in the order defined
by $\pi.

We define the deterministic attractor operator $\ensuremath{**DetAtt**} as
follows. If $X \subseteq V, we define inductively the
sequence $(X_i)_{i \ge 0}$ by:

$$
\left\{
\begin{array}{rcl}
  X_0 & =& X \\
  X_{i+1} &=& X_i \cup \{v \in V_\mEvemid \exists w \in X_i\
  \text{s.t.}\ (v,w) \in E\} \\
   && \phantom{X_i} \cup \{v \in V_\mAdammid \forall w \in X_i,\ 
  (v,w) \in E\ \text{implies}\ v \in X_i\}
\end{array}
\right.
$$

The deterministic attractor of $X$ is then given by:

$$
\ensuremath{**DetAtt**}X) = \lim_{i \to +\infty} X_i = \bigcup_{i =0}^{+\infty} X_i
$$

Note that since $V is finite, the sequence $(X_i)_{i \ge 0}$
stabilizes and the above union is actually finite.  \pat{refer to the
  relevant previous chapter, there certainly is one.}

Let $\pi be a permutation. We define the $\pi-regions as
deterministic attractors to the random vertices (taken in the correct
order) as follows:

$$
\left\{
\begin{array}{l}
  W_\pi{k+1}  = \{\ensuremath{v_{\textsc{win}}}} \\
  W_\pii =
  \ensuremath{**DetAtt**}\{\perm_i,\ldots,\perm_k,\ensuremath{v_{\textsc{win}}}}) \setminus \bigcup_{j=i+1}^{k+1}
  W_\pij\quad \forall 1 \le i \le k \\ 
  W_\pi0 = V \setminus \bigcup_{j=1}^{k+1} W_\pij = \{\ensuremath{v_{\textsc{lose}}}}
\end{array}
\right.
$$

The last equality (for $W_\pi0$) holds since (i) from vertices in
$W_\pi0$ \textrm{Adam}can enforce avoiding $\vertices_{\text{Rand}}\cup
\{\ensuremath{v_{\textsc{win}}}}$ (by determinacy of non-stochastic reachability games
\pat{ref to a previous chapter?}), yielding only losing outcomes, and
(ii) $\ensuremath{v_{\textsc{lose}}} is the unique vertex with value $0$ (by
assumption). Later, we will write $W_\pi{\ge j}$ for
$\bigcup_{i=j}^{k+1} W_\pii$.

Given $\pi a permutation, we define strategies $\sigma_\pi (for
\Eve) and $\tau_\pi (for \textrm{Adam} such that on $W_\pii$:

*  $\sigma_\pi is a pure and positional attractor strategy to
  $\{\perm_i,\ldots,\perm_k,\ensuremath{v_{\textsc{win}}}}$;
*  $\tau_\pi is a pure and positional trapping strategy avoiding
  $\{\perm_{i+1},\ldots,\perm_k,\ensuremath{v_{\textsc{win}}}}$.

Those two strategies obviously exist: $\sigma_\pi exists by
definition of the deterministic attractor, while $\tau_\pi exists
by determinacy of reachability games (if a vertex is not winning for
\Eve for a reachability objective, then it is winning for \textrm{Adam}for
the corresponding safety objective).

We can then define for every $v \in V:

$$
\begin{array}{rcl}
\val_\piv) &=& \probm_{\sigma_\pi\tau_\pi^v(\mathtt{Reach}\textrm{Win})
\end{array}
$$

which can be easily computed using systems of linear
equations. 

The rest of this section is devoted to a proof of the following
result, which uses only basic arguments:

````{prf:theorem} NEEDS TITLE AND LABEL 
  \label{6-thm:corr-strat-improv}
  There is a permutation $\pi such that $\sigma_\pi is optimal
  for \Eve and $\tau_\pi is optimal for \textrm{Adam} Given a permutation
  $\pi, we can check in polynomial time whether $\sigma_\pi and
  $\tau_\pi are optimal.
 

  \label{6-thm:corr-strat-improv}
  There is a permutation $\pi such that $\sigma_\pi is optimal
  for \Eve and $\tau_\pi is optimal for \textrm{Adam} Given a permutation
  $\pi, we can check in polynomial time whether $\sigma_\pi and
  $\tau_\pi are optimal.

````

We will explain in Subsection {ref}`6-subsec:algo-strat-improv` how this
theorem can be turned into a strategy improvement algorithm for
computing values and optimal strategies in stochastic reachability
games.



### Live and self-consistent permutations


We say that a permutation $\pi is **self-consistent** whenever:

$$
\val_\pi\perm_1) \le \val_\pi\perm_2) \le \ldots \le \val_\pi\perm_k)
$$

That is, the order given by $\pi coincides with the preference of
\Eve.

We say $\pi is **live** whenever for every $1 \le i \le k$:

$$
\delta(\perm_i)\big(W_\pi{\ge i+1}\big)>0
$$

That is, there is a direct move from $\perm_i$ to one of the vertices
in larger attractors. In particular, with positive probability, one
goes closer to $\ensuremath{v_{\textsc{win}}} and hence eventually reach $\ensuremath{v_{\textsc{win}}}.

\medskip We will show that $\pi-strategies associated with a live
and self-consistent permutation $\pi are optimal for both players.
And that such a permutation always exists. We start with the
correctness, and will turn to the existence later.


### Correctness of live and self-consistent permutations


% any further assumption on $\pi.

%   \label{stoch:lemma1}

%   \item $\val_\pi\ensuremath{v_{\textsc{lose}}} = 0$ and $\val_\pi\ensuremath{v_{\textsc{win}}} = 1$;

%     $\val_\piv) = \val_\pi\perm_i)$;

%     \val_\pi\sigma_\piv))$;

%     \val_\pi\tau_\piv))$;

%       \text{s.t.}\ (v,w) \in E} \delta(v)(w) \cdot \val_\piw)$.

% \end{lemma}

%   The first item is obvious.
  

%   vertex, the strategy profile $(\sigma_\pi\tau_\pi$ generates a

%   from $v$ when applying $(\sigma_\pi\tau_\pi$. By definition of

%   $\tau_\pi (trapping strategy avoiding

%   be $\perm_i$. According values follow, proving the second item.

%   attractor strategy), $\sigma_\piv) \in W_\pii \cup

%   W_\pi{\ge i+1}$, $\sigma_\piv) \notin

%   W_\pii \cup \{\perm_i\} = W_\pii$, and we get that

%   (third item).

%   trapping strategy), $\tau_\piv) \notin

%   W_\pii$, we nevertheless have that $\tau_\piv) \in W_\pii

%   W_\pii \cup \{\perm_i\} = W_\pii$. Hence $\val_\piv) =


% \end{proof}


We first give some properties always satisfied by strategies
$\sigma_\pi and $\tau_\pi without any condition on $\pi, and
refine these properties to show that $\sigma_\pi and $\tau_\pi
are (local) best responses to each others, when the permutation is
self-consistent.

````{prf:lemma} NEEDS TITLE AND LABEL 
  \label{stoch:lemma2}
  We write (\ddag) for the assumption that $\pi is self-consistent.
  
  
1.  $\val_\pi\ensuremath{v_{\textsc{lose}}} = 0$ and $\val_\pi\ensuremath{v_{\textsc{win}}} = 1$;
  
2.  for every $1 \le i \le k$, for every $v \in W_\pii$,
    $\val_\piv) = \val_\pi\perm_i)$;
  
3.  For every $v \in V_\mathrm{Eve}    

$$
    \val_\piv) = \val_\pi\sigma_\piv)) \stackrel{(\ddag)}{=}
    \max_{w\ \text{s.t.}\ (v,w) \in E} \val_\piw)
    $$

  
4.  For every $v \in V_\mathrm{Adam}    

$$
    \val_\piv) = \val_\pi\tau_\piv)) \stackrel{(\ddag)}{=}
    \min_{w\ \text{s.t.}\ (v,w) \in E} \val_\piw)
    $$

  
  
  
  
  
  
5.  For every $v \in \vertices_{\text{Rand}}, $\val_\piv) = \sum_{w\
      \text{s.t.}\ (v,w) \in E} \delta(v)(w) \cdot \val_\piw)$.
  
 

  \label{stoch:lemma2}
  We write (\ddag) for the assumption that $\pi is self-consistent.
  
  
1.  $\val_\pi\ensuremath{v_{\textsc{lose}}} = 0$ and $\val_\pi\ensuremath{v_{\textsc{win}}} = 1$;
  
2.  for every $1 \le i \le k$, for every $v \in W_\pii$,
    $\val_\piv) = \val_\pi\perm_i)$;
  
3.  For every $v \in V_\mathrm{Eve}    

$$
    \val_\piv) = \val_\pi\sigma_\piv)) \stackrel{(\ddag)}{=}
    \max_{w\ \text{s.t.}\ (v,w) \in E} \val_\piw)
    $$

  
4.  For every $v \in V_\mathrm{Adam}    

$$
    \val_\piv) = \val_\pi\tau_\piv)) \stackrel{(\ddag)}{=}
    \min_{w\ \text{s.t.}\ (v,w) \in E} \val_\piw)
    $$

  
  
  
  
  
  
5.  For every $v \in \vertices_{\text{Rand}}, $\val_\piv) = \sum_{w\
      \text{s.t.}\ (v,w) \in E} \delta(v)(w) \cdot \val_\piw)$.
  

````


````{admonition} Proof
:class: dropdown tip


  The first item is obvious.
  
  For every $v \in W_\pii$, up to the first visit to a random
  vertex, the strategy profile $(\sigma_\pi\tau_\pi$ generates a
  unique path. So we can speak of the first random vertex encountered
  from $v$ when applying $(\sigma_\pi\tau_\pi$. By definition of
  $\sigma_\pi (attractor to $\{\perm_i,\ldots,\perm_k,\ensuremath{v_{\textsc{win}}}}$) and
  $\tau_\pi (trapping strategy avoiding
  $\{\perm_{i+1},\ldots,\perm_k,\ensuremath{v_{\textsc{win}}}}$), this random vertex can only
  be $\perm_i$. According values follow, proving the second item.

  Assume $v \in V_\mEvecap W_\pii$.  By definition of
  $\sigma_\pi (being an attractor strategy), $\sigma_\piv) \in
  W_\pii \cup \{\perm_i,\ldots,\perm_k,\ensuremath{v_{\textsc{win}}}}$. Dually, since $v
  \notin W_\pi{\ge i+1}$, $\sigma_\piv) \notin
  \{\perm_{i+1},\ldots,\perm_k,\ensuremath{v_{\textsc{win}}}}$. Hence, $\sigma_\piv) \in
  W_\pii \cup \{\perm_i\} = W_\pii$, and we get that
  $\val_\piv) = \val_\pi\perm_i) = \val_\pi\sigma_\piv))$.
  Assume (towards a contradiction) that there is $w \in V
  such that $(v,w) \in E$ and $\val_\piw)>\val_\piv)$.  Since
  $\val_\piw) > \val_\piv) = \val_\pi\perm_i)$, by
  self-consistence, it is the case that $w \in W_\pij$ with $j > i$
  (with $\val_\piw) = \val_\pi\perm_j)$). But then, we can
  deduce that $v \in \ensuremath{**DetAtt**}w) \subseteq
  \ensuremath{**DetAtt**}\{\perm_j,\ldots,\perm_k,\ensuremath{v_{\textsc{win}}}})$, which is not the case,
  since $v \notin W_\pi{\ge i+1} \supseteq W_\pij$. There is
  therefore a contradiction, and we can conclude that $\val_\piv) =
  \max_{w\ \text{s.t.}\ (v,w) \in E} \val_\piw)$.

  Assume $v \in V_\mAdamcap W_\pii$. By definition of
  $\sigma_\pi (being a trapping strategy), $\tau_\piv) \notin
  \{\perm_{i+1},\ldots,\perm_k,\ensuremath{v_{\textsc{win}}}}$. However since $v \in
  W_\pii$, we nevertheless have that $\tau_\piv) \in W_\pii
  \cup \{\perm_i,\ldots,\perm_k,\ensuremath{v_{\textsc{win}}}}$, hence $\tau_\piv) \in
  W_\pii \cup \{\perm_i\} = W_\pii$. Hence $\val_\piv) =
  \val_\pi\perm_i) = \val_\pi\tau_\piv))$.  Assume (towards a
  contradiction) that there is $w \in V such that $(v,w) \in
  E$ and $\val_\piw)<\val_\piv)$. As in the previous item, by
  self-consistence, $w \in W_\pij$ with $j<i$. But, $v$ can only be
  in a deterministic attractor if all its successors already are. This
  contradicts the fact that $w \in W_\pij$, hence $w \notin
  W_\pi{\ge j+1} \supseteq W_\pii$. Hence, we conclude that
  $\val_\piv) = \min_{w\ \text{s.t.}\ (v,w) \in E} \val_\piw)$.

  The fifth item is straightforward hence omitted.  \qed

````


As a consequence of {prf:ref}`6-lem:lemma2`, we get that $\val_\pi
is a fixpoint of Bellman's equations, hence it is larger than (or
equal to) the least fixpoint of Bellman's equations, that is $\textrm{val}$:

%  utilis\'e la notation $\textrm{val}$ avant}

````{prf:corollary} NEEDS TITLE AND LABEL 
  Assume $\pi is self-consistent.  Then for every $v \in
  V, $\textrm{val}(v) \le \val_\piv)$.
 

  Assume $\pi is self-consistent.  Then for every $v \in
  V, $\textrm{val}(v) \le \val_\piv)$.

````

The converse inequality is not true for general or self-consistent
permutations, but will require the liveness property. One of the main
advantages of a live permutation $\pi is that it induces a
stopping MDP when \Eve plays according to $\sigma_\pi: \textrm{Adam}will not be able to prevent the game converging to $\ensuremath{v_{\textsc{lose}}} and $\ensuremath{v_{\textsc{win}}}.

````{prf:lemma} NEEDS TITLE AND LABEL 
  \label{stoch:lemma:stopping}
  Let $\pi be a live permutation. Then, for every \textrm{Adam}s strategy
  $\tau$, for every vertex $v$:
  

$$
  \mathbb{P}v_{\sigma_\pi\tau} (\mathtt{Reach}\{\ensuremath{v_{\textsc{lose}}}\ensuremath{v_{\textsc{win}}}})) = 1
  $$

 

  \label{stoch:lemma:stopping}
  Let $\pi be a live permutation. Then, for every \textrm{Adam}s strategy
  $\tau$, for every vertex $v$:
  

$$
  \mathbb{P}v_{\sigma_\pi\tau} (\mathtt{Reach}\{\ensuremath{v_{\textsc{lose}}}\ensuremath{v_{\textsc{win}}}})) = 1
  $$


````


````{admonition} Proof
:class: dropdown tip

  We make use of the progress property induced by a live permutation.
  Let
  

$$
  \alpha = \min_{1 \le i \le k} \delta(\perm_i) \big(W_\pi{\ge
    i+1}\big)
  $$

  By definition of a live permutation, $\alpha>0$.

  We write $V_i$ for the random variable representing the $i$-th state
  of a run.
  
  By definition of $\alpha$, for every $v \in V, for every $1
  \le i \le k$ and for every $l \ge 0$,
  

$$
  \mathbb{P}v_{\sigma_\pi\tau}\Big(V_{l+1} \in W_\pi{\ge i+1} \mid
  V_l = \perm_i\Big) \ge \alpha
  $$

  Also, for every $1 \le i \le k$, for every $v \in V, for
  every $l \ge 0$,
  

$$
  \mathbb{P}v_{\sigma_\pi\tau}\Big(\exists h < |W_\pii|\
  \text{s.t.}\ V_{l+h} \in \{\perm_i,\ldots,\perm_k,\ensuremath{v_{\textsc{win}}}} \mid V_l
  \in W_\pii\Big)=1
  $$

  since $\sigma_\pi plays according to attractor strategies in
  according subsets of vertices.

  Hence we deduce that for every $v \in V, for every $l \ge
  0$,
  

$$
  \mathbb{P}v_{\sigma_\pi\tau}\Big(V_{l+|V}=\ensuremath{v_{\textsc{win}}}\mid V_l
  \ne \ensuremath{v_{\textsc{lose}}}Big) \ge \alpha^k
  $$

  which we can rewrite as:
  

$$
  \mathbb{P}v_{\sigma_\pi\tau}\Big(\forall 0 \le l \le l' \le
  l+|V,\ V_{l'} \ne \ensuremath{v_{\textsc{win}}}\mid V_l \ne \ensuremath{v_{\textsc{lose}}}Big) \le
  (1-\alpha^k)
  $$

  Iterating, we get that for every $i$, for every $v \in V,
  

$$
  \mathbb{P}v_{\sigma_\pi\tau}\Big(\forall l \le i \cdot |V,\
  V_{l} \ne \ensuremath{v_{\textsc{win}}}\mid V_0 \ne \ensuremath{v_{\textsc{lose}}}Big) \le (1-\alpha^k)^i
  $$

  We  deduce that for every $v \in V,
  

$$
  \mathbb{P}v_{\sigma_\pi\tau}(\forall l \ge 0,\ V_l \ne \ensuremath{v_{\textsc{win}}}\mid
  V_0 \ne \ensuremath{v_{\textsc{lose}}} = 0
  $$

  We conclude with
  

$$
  \mathbb{P}v_{\sigma_\pi\tau}(\exists l \ge 0,\ V_l = \ensuremath{v_{\textsc{win}}}\mid V_0
  \ne \ensuremath{v_{\textsc{lose}}} = 1
  $$

  hence with the statement.

````



````{prf:lemma} NEEDS TITLE AND LABEL 
  Let $\pi be a live and self-consistent permutation.  Then for
  every $v \in V,  $\val_\piv) \le \textrm{val}(v)$.

%   $\sigma_\pi is optimal for \Eve and $\sigma_\pi is optimal for

 

  Let $\pi be a live and self-consistent permutation.  Then for
  every $v \in V,  $\val_\piv) \le \textrm{val}(v)$.

%   $\sigma_\pi is optimal for \Eve and $\sigma_\pi is optimal for

````


````{admonition} Proof
:class: dropdown tip

  Fix a pure positional \textrm{Adam}s strategy $\tau$. The tuple
  $(\probm_{\sigma_\pi\tau}^v(\mathtt{Reach}\textrm{Win}))_{v \in V$ is
  a
  
  
  solution to the following equations:
  

$$
  \left\{\begin{array}{ll} x_v =
      x_{\tau(v)} & \text{if}\ v \in V_\mathrm{Adam}
      x_v = x_{\sigma_\piv)} & \text{if}\ v \in V_\mathrm{Eve}
      x_v = \sum_{w\ \text{s.t.}\ (v,w) \in E} \delta(v)(w) \cdot
      x_w  & \text{if}\ v \in \vertices_{\text{Rand}}\\
      x_{\ensuremath{v_{\textsc{win}}} = 1 \\
      x_{\ensuremath{v_{\textsc{lose}}} = 0
    \end{array}\right.
  $$

  In particular, it is a solution to the following inequations:
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

$$
  \left\{\begin{array}{ll} 
      x_v \ge \min_{w\ \text{s.t.}\ (v,w) \in E}
      x_w & \text{if}\ v \in V_\mathrm{Adam}
      x_v = x_{\sigma_\piv)}  & \text{if}\ v \in V_\mathrm{Eve}
      x_v = \sum_{w\ \text{s.t.}\ (v,w) \in E} \delta(v)(w) \cdot x_w
      & \text{if}\ v \in \vertices_{\text{Rand}}\\
      x_{\ensuremath{v_{\textsc{win}}} = 1 \\
      x_{\ensuremath{v_{\textsc{lose}}} = 0
    \end{array}\right.
  $$

  Since the MDP (when $\sigma_\pi has been fixed) is stopping (see {prf:ref}`6-lem:stopping`), there is no proper end-component
  (except $\{\ensuremath{v_{\textsc{win}}}}$ and $\{\ensuremath{v_{\textsc{lose}}}}$), and the above system of
  inequations has a unique minimal solution, which is the unique
  solution of the same system with $=$ instead of $\ge$.

  On the other hand {prf:ref}`6-lem:lemma2` tells us that
  $(\val_\piv))_{v \inV$ can only be that unique
  solution. Hence, for every $v \in V:
  

$$
  \val_\piv) \le \probm_{\sigma_\pi\tau}^v(\mathtt{Reach}\textrm{Win})
  $$

  
  
%   \item For every memoryless and pure \Eve's strategy $\sigma$,

%     is the smallest solution to the following equations:

%     \left\{\begin{array}{ll} x_v =

%         x_v = x_{\tau_\piv)} & \text{if}\ v \in V_\mathrm{Adam}

%         x_w \\

%         x_{\ensuremath{v_{\textsc{lose}}} = 0

%     \]

%     

$$

%           E}

%         x_v = x_{\tau_\piv)} & \text{if}\ v \in V_\mathrm{Adam}

%         x_w \\

%         x_{\ensuremath{v_{\textsc{lose}}} = 0

%     $$


%   solution. \pat{c'est bien ok ?}

%   $(\val_\piv))_{v \inV$ can only be that maximal

%   

$$

%   \probm_{\sigma,\tau_\pi^v(\mathtt{Reach}\textrm{Win})

%   This shows that $\sigma_\pi plays optimally against $\tau_\pi.

  Since this holds for every pure positional strategy $\tau$ of \textrm{Adam}
  we conclude that for every $v \in V,
  $\val_\piv) \le \textrm{val}(v)$. \qed
  
  
  
  
  
  
  

````


````{prf:corollary} NEEDS TITLE AND LABEL 
  \label{stoch:coro}
  Let $\pi be a live and self-consistent permutation. Then, for
  every $v \in V, $\textrm{val}(v) = \val_\piv)$.  
 

  \label{stoch:coro}
  Let $\pi be a live and self-consistent permutation. Then, for
  every $v \in V, $\textrm{val}(v) = \val_\piv)$.  

````


### Existence of a live and self-consistent permutation


````{prf:lemma} NEEDS TITLE AND LABEL 
  \label{stoch:lemma:croissant}
  Let $\pi be a live permutation such that
  \[
  \textrm{val}(\perm_1) \le \textrm{val}(\perm_2) \le \ldots \le \textrm{val}(\perm_k)
  $$

  Then, $\pi is self-consistent.
 

  \label{stoch:lemma:croissant}
  Let $\pi be a live permutation such that
  \[
  \textrm{val}(\perm_1) \le \textrm{val}(\perm_2) \le \ldots \le \textrm{val}(\perm_k)
  $$

  Then, $\pi is self-consistent.

````


````{admonition} Proof
:class: dropdown tip

  We will show that for every vertex $v \in V, $\textrm{val}(v) =
  \val_\piv)$. This will ne enough for proving the expected result.

  We first show a counterpart to {prf:ref}`6-lem:lemma2` for
  $\textrm{val}$:
  
````{prf:lemma} NEEDS TITLE AND LABEL 
    Same hypotheses as {prf:ref}`6-lem:croissant`. Then:
    
    
1.  $\textrm{val}(\ensuremath{v_{\textsc{lose}}} = 0$ and $\textrm{val}(\ensuremath{v_{\textsc{win}}} = 1$;
    
2.  for every $1 \le i \le k$, for every $v \in W_\pii$,
      $\textrm{val}(v) = \textrm{val}(\perm_i)$.
    
   

    Same hypotheses as {prf:ref}`6-lem:croissant`. Then:
    
    
1.  $\textrm{val}(\ensuremath{v_{\textsc{lose}}} = 0$ and $\textrm{val}(\ensuremath{v_{\textsc{win}}} = 1$;
    
2.  for every $1 \le i \le k$, for every $v \in W_\pii$,
      $\textrm{val}(v) = \textrm{val}(\perm_i)$.
    
  
````

  \begin{proof}
    Notice that item 1 is obvious. 
    
    
    
    

    We then focus on item 2.  Assume $v \in W_\pii$, and define
    strategy $\sigma^*$ from $v$ as $\sigma_\pi (attractor strategy
    to $\{\perm_i,\ldots,\perm_k,\ensuremath{v_{\textsc{win}}}}$) until $\ensuremath{v_{\textsc{win}}} or a random
    vertex $\pi_j$ ($j \ge i$) is reached; in the latter case, switch
    to an optimal strategy out of $\pi_j$. We obviously get that for
    every strategy $\tau$ for \textrm{Adam}
    $\probm_{\sigma^*,\tau}^v(\mathtt{Reach}\{\ensuremath{v_{\textsc{win}}}})) \ge \min_{i \le j \le
      k}\textrm{val}(\perm_j) = \textrm{val}(\perm_i)$. Hence $\textrm{val}(v) \ge
    \textrm{val}(\perm_i)$.
    
    Conversely define strategy $\tau^*$ from $v$ as $\tau_\pi
    (trapping strategy out of $\{\perm_{i+1},\ldots,\perm_k,\ensuremath{v_{\textsc{win}}}}$)
    until $\ensuremath{v_{\textsc{lose}}} or a random vertex $\pi_j$ ($j \le i$) is reached;
    in the latter case, switch to an optimal strategy out of
    $\pi_j$. Note that it can a priori be the case that we never hit
    $\ensuremath{v_{\textsc{lose}}} or a random vertex, but this is good to \textrm{Adam} However we
    can conclude that for every strategy $\sigma$ for \Eve,
    $\probm_{\sigma,\tau^*}^v(\mathtt{Reach}\{\ensuremath{v_{\textsc{win}}}})) \le \max_{1 \le j \le
      i}\textrm{val}(\perm_j) = \textrm{val}(\perm_i)$. Hence
    $\textrm{val}(v) \le \textrm{val}(\perm_i)$.

    
    
    
    This allows to conclude item 2, hence the lemma.
  
````

  Both $\textrm{val}$ and $\val_\pi satisfy the system of equations:
  

$$
  \left\{\begin{array}{ll} 
      x_v = x_{\perm_i} & \text{if}\ v \in W_\pii \\ 
      
      
      x_v = \sum_{w\ \text{s.t.}\ (v,w) \in E} \delta(v)(w) \cdot x_w
      & \text{if}\ v \in \vertices_{\text{Rand}}\\
      x_{\ensuremath{v_{\textsc{win}}} = 1 \\
      x_{\ensuremath{v_{\textsc{lose}}} = 0
    \end{array}\right.
  $$

  We can rewrite this system into:
  

$$
  \left\{\begin{array}{ll} 
      x_v = x_{\perm_i} & \text{if}\ v \in W_\pii \\ 
      
      
      x_{\perm_i} = \sum_{j=0}^{k+1} \delta(\perm_i)(W_\pij) \cdot x_{\perm_j}
      & \\
      x_{\ensuremath{v_{\textsc{win}}} = 1 \\
      x_{\ensuremath{v_{\textsc{lose}}} = 0
    \end{array}\right.
  $$

  Since $\pi is live this system has a unique solution!  Hence
  $\textrm{val} = \val_\pi, and $\pi is self-consistent.
\end{proof}

It remains to show that there always exist  a live permutation
satisfying the hypothesis of {prf:ref}`6-lem:croissant`.

To do so, we show the following structural property of the game, which
will help building an appropriate live permutation.

````{prf:lemma} NEEDS TITLE AND LABEL 
  \label{stoch:lemma:structure}
  Let $\{\ensuremath{v_{\textsc{win}}}} \subseteq X \subseteq V$ be a subset of vertices, and
  $Y = V \setminus \ensuremath{**DetAtt**}X)$. Then either $Y = \{\ensuremath{v_{\textsc{lose}}}}$, or there
  is a random vertex $v \in Y$ such that $\textrm{val}(v) = \max\{\textrm{val}(w)
  \mid w \in Y\}$ and $\delta(v)\Big(\ensuremath{**DetAtt**}X)\Big)>0$.
 

  \label{stoch:lemma:structure}
  Let $\{\ensuremath{v_{\textsc{win}}}} \subseteq X \subseteq V$ be a subset of vertices, and
  $Y = V \setminus \ensuremath{**DetAtt**}X)$. Then either $Y = \{\ensuremath{v_{\textsc{lose}}}}$, or there
  is a random vertex $v \in Y$ such that $\textrm{val}(v) = \max\{\textrm{val}(w)
  \mid w \in Y\}$ and $\delta(v)\Big(\ensuremath{**DetAtt**}X)\Big)>0$.

````


````{admonition} Proof
:class: dropdown tip

  
  
  Let $Z = \textsf{Argmax}_Y (\textrm{val})$. We assume that there is no
  random vertex $v \in Z \cap \vertices_{\text{Rand}} such that
  $\delta(v)\Big(\ensuremath{**DetAtt**}X)\Big)>0$. We will show that $Z =
  \{\ensuremath{v_{\textsc{lose}}}}$, which will imply $Y = \{\ensuremath{v_{\textsc{lose}}}}$. To do so, we show
  that if $v \in Z$, then $\textrm{val}(v) = 0$.  We fix $v \in Z$, and we
  assume towards a contradiction that $\textrm{val}(v)>0$.

  Let $\tau$ be a pure positional \textrm{Adam}s strategy on $Y$ avoiding
  $\ensuremath{**DetAtt**}X)$: by definition, $\tau(Y) \subseteq Y$. Also, one can
  argue that $\tau(Z) \subseteq Z$. Indeed otherwise there is $v' \in
  Z$ such that $\tau(v') \in Y \setminus Z$. Thus, $\textrm{val}(\tau(v')) <
  \textrm{val}(v')$, which is not possible since $\textrm{val}(v') = \min_{w\
    \text{s.t.}\ (v',w) \in E} \textrm{val}(w)$ (Bellman's equations). Also
  by Bellman's equations, if $v' \in \vertices_{\text{Rand}}\cap Z$, for
  every $w'$ such that $\delta(v')(w')>0$, $\textrm{val}(w') =
  \textrm{val}(v')$. By assumption, it cannot be the case that $w' \in
  \ensuremath{**DetAtt**}X)$, hence $w' \in Z$.  Let $v' \in Z \cap V_\mathrm{Eve}If
  there is $w' \notin Z$ such that $(v',w') \in E$, then it must be
  the case that $w' \in Y \setminus Z$: indeed, it cannot be the case
  that $w' \in \ensuremath{**DetAtt**}X)$, otherwise $v'$ would also be in
  $\ensuremath{**DetAtt**}X)$.

  We now define strategy $\tau'$ which plays from $v$ as $\tau$ until
  $Z$ is left, and then $\tau'$ plays an optimal strategy for \textrm{Adam}
  Let $\sigma$ be a strategy for \Eve. Under the profile
  $(\sigma,\tau')$ from $v$, either we stay forever in $Z$, or we
  leave at some \Eve's vertex $v'$ towards a vertex $w'$ with
  $\textrm{val}(w') < \textrm{val}(v') = \textrm{val}(v)$ (recall the discussion
  above). We can then write:
  \begin{eqnarray*}
    \probm_{\sigma,\tau'}(\mathtt{Reach}\{\ensuremath{v_{\textsc{win}}}})) &=&
    \probm_{\sigma,\tau'}(\mathtt{Reach}\{\ensuremath{v_{\textsc{win}}}}) \mid \text{stays in}\  Z\
    \text{forever}) \cdot  \probm_{\sigma,\tau'}(\text{stays in}\  Z\
    \text{forever}) \\ 
    && + \sum_{(v',w') \in (Z \times (Y \setminus Z) \cap E)} 
    \probm_{\sigma,\tau'}(\mathtt{Reach}\{\ensuremath{v_{\textsc{win}}}}) \mid
    \text{leave via}\  (v',w')) \cdot
    \probm_{\sigma,\tau'}(\text{leave via}\  (v',w')) \\
    & = & 0 \cdot \probm_{\sigma,\tau'}(\text{stays in}\  Z\
    \text{forever}) + \sum_{(v',w') \in (Z \times (Y \setminus Z) \cap
      E)}  \textrm{val}(w') \cdot
    \probm_{\sigma,\tau'}(\text{leave via}\  (v',w')) \\
    & \le & \beta
  \end{eqnarray*}
  where $\beta = \max \{\textrm{val}(w) \mid w \in Y \setminus Z\} <
  \textrm{val}(v)$.  Hence, we get $\textrm{val}(v) \le \beta < \textrm{val}(v)$. This
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

  We will define a permutation $\pi inductively, by repeatedly
  using {prf:ref}`6-lem:structure`.  For every $i =k, \ldots
  ,1$ we define $\perm_i$ by applying
  Lemma {prf:ref}`6-lem:structure` to $X =
  \{\perm_{i+1},\ldots,\perm_k,\ensuremath{v_{\textsc{win}}}}$.

  By construction,
  
  *  $\textrm{val}(\perm_i) = \max \{\textrm{val}(v) \mid v \in V \setminus
    \ensuremath{**DetAtt**}\{\perm_{i+1},\ldots,\perm_k,\ensuremath{v_{\textsc{win}}}})\}$;
  *      $\delta(\perm_i)\Big(\ensuremath{**DetAtt**}\{\perm_{i+1},\ldots,\perm_k,\ensuremath{v_{\textsc{win}}}})\Big)
    >0$
  
  Hence, $\pi is live, and the hypothesis of {prf:ref}`6-lem:croissant` is satisfied. Hence $\pi is
  self-consistent. This concludes the proof.

````


### Complexity analysis

To obtain the polynomial-time complexity claimed in {prf:ref}`6-thm:corr-strat-improv`, we realize that once a
permutation $\pi is fixed, computing the sets $W_\pi^i$ can be done
in polynomial time (those are simple attractors), and corresponding
strategies $\sigma_\pi and $\tau_\pi can be simultaneously
computed as well. Now, computing $\val_\pi reduces to computing the
probability to reach $\ensuremath{v_{\textsc{win}}} in the induced Markov chain, which is
known to be possible in polynomial time. Note that we could improve
the complexity by reducing the Markov chain to a Markov chain where
the only vertices are $\vertices_{\text{Rand}}\cup \{\ensuremath{v_{\textsc{lose}}}\ensuremath{v_{\textsc{win}}}}$, but
this would only marginally impact the overall complexity.

(6-subsubsec:last)=
### Strategy enumeration algorithm

Thanks to {prf:ref}`6-thm:corr-strat-improv`, we get an algorithm
to compute values and optimal strategies for both players in a
stochastic reachability game: enumerate permutations of random
vertices, and for each of them, check whether it is live and
self-consistent; stop when one is found.

However, as such, this requires to enumerate all permutations of
random vertices, and there are $|\vertices_{\text{Rand}}!$ of them. Hence the
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

*  Initialization step: Compute a live permutation $\pi
*  Improvement step: Given a live permutation $\pi, compute a
  live and self-consistent permutation in $\mathcal{G}\sigma_\pi$, the
  restriction of game $\mathcal{G} where $\Eve$ always plays according to
  $\sigma_\pi.

Below, since we will speak of games $\mathcal{G}, $\mathcal{G}\sigma_\pi$ and
even $\mathcal{G}\sigma_{\pi}]$, when speaking about the value of the
game, we will specify the game in which we consider the value. For
instance, $\textrm{val}_{\mathcal{G}\sigma_\pi}$ denotes the value vector of the game
$\mathcal{G}\sigma_\pi$, and $\val_{\mathcal{G}\pi$ denotes the former
$\val_\pi.

We will argue (though not with full details) that the following
properties are satisfied by the algorithm:

1.  An initial live permutation can be computed in polynomial time.

2.  For every live permutation $\pi, one can compute in
  polynomial time a live and self-consistent permutation $\pi$ in
  $\mathcal{G}\sigma_\pi$.

3.  The above-mentioned permutation $\pi$ is live in $\mathcal{G} as
  well.

4.  The improvement step really implements some improvement:
  
  *  $\textrm{val}_{\mathcal{G}\sigma_\pi} \le
    \textrm{val}_{\mathcal{G}\sigma_{\pi}]}$, and
  *  $\textrm{val}_{\mathcal{G}\sigma_\pi} =
    \textrm{val}_{\mathcal{G}\sigma_{\pi}]}$ implies that $\pi$ is
    self-consistent.
  

The first property is based on the construction of {prf:ref}`6-lem:existence`.

For the second property, we know as a consequence of {prf:ref}`6-thm:corr-strat-improv` that there exists a live and
self-consistent permutation $\pi$ in $\mathcal{G}\sigma_{\pi]$,
provided we prove that $\mathcal{G}\sigma_{\pi]$ is normalized (this was
a general assumption of the approach, mentioned in Subsection {ref}`6-subsec:first`). This is actually the case since
every proper vertex $v$ can be proven to have a value strictly within
$0$ and $1$ in $\mathcal{G}\sigma_{\pi]$ (it is indeed smaller in
$\mathcal{G}\sigma_{\pi]$ than in $\mathcal{G} since $\mathcal{G}\sigma_{\pi]$
offers less options to \Eve, and it cannot be $0$, using a proof
similar to that of {prf:ref}`6-lem:stopping`).

% nevertheless assumes the underlying game be normalized. So it is just

% argue that every vertex $v \ne \ensuremath{v_{\textsc{win}}}\ensuremath{v_{\textsc{lose}}} is such that its value in

% value in game $\mathcal{G}\sigma_\pi$ is bounded from above by the value

% $1$ in $\mathcal{G}\sigma_\pi$; using a proof similar to the proof of

% $\ensuremath{v_{\textsc{lose}}} can have value $0$. 
Now, since $\mathcal{G}\sigma_\pi$ turns out to be a Markov decision
process, values of all random vertices can be computed in polynomial
time using linear programming; then we can apply a construction
similar to that of {prf:ref}`6-lem:existence` to get a live and
self-consistent permutation $\pi$ in $\mathcal{G}\sigma_\pi$. This
yields a polynomial time algorithm to compute $\pi$.

For the third property, we realize that

% permutation $\pi$ in $\mathcal{G}\sigma_\pi$ is live in $\mathcal{G}:
$\pi$-regions in $\mathcal{G}\sigma_\pi$ are included in
$\pi$-regions in $\mathcal{G}, which immediately implies the result.

The last property is harder to argue; it expresses the fact that the
new permutation $\pi$ improves over $\pi.  
% the proof, but not full details.

````{admonition} Proof
:class: dropdown tip

  Since $\pi$ is live and self-consistent in $\mathcal{G}\sigma_\pi$,
  by~\cref{6-cor:}, extending the previous notations, we
  get that
  $\textrm{val}_{\mathcal{G}\sigma_\pi} =
  \val_{\mathcal{G}\sigma_\pi,\pi}$. Now, since $\pi$ is
  self-consistent in $\mathcal{G}\sigma_\pi$, we deduce that
  

$$
    \textrm{val}_{\mathcal{G}\sigma_\pi}(\pi_1) \le
    \textrm{val}_{\mathcal{G}\sigma_\pi}(\pi_2) \le \dots \le
    \textrm{val}_{\mathcal{G}\sigma_\pi}(\pi_k)
  $$


  We consider the following family of strategies for \Eve in $\mathcal{G}:
  for every $n$, $\sigma^{(n)}$ is the strategy where \Eve plays
  according to $\sigma_{\pi}$ up to its $n$-th visit to a random
  vertex, and then switches to $\sigma_\pi. 

````
 
We can then prove:

  
  
  

````{prf:lemma} Converge of the sequence of values
:label: 6-lem:convergence_sequence_values

The sequence $(\val_{\mathcal{G}\sigma^{(n)}})_n$ is non-decreasing.

````

  
````{admonition} Proof
:class: dropdown tip

    We do the proof by induction on $n$.  We focus on $n=0$, and prove
    below that $\val_{\mathcal{G}\sigma^{(1)}} \ge
    \val_{\mathcal{G}\sigma^{(0)}}$. First notice that $\sigma^{(0)} =
    \sigma_\pi.

    First, notice that $v \in W_{\mathcal{G}\pi}^i$ for some $i$, and $v
    \in W_{\mathcal{G}\sigma_\pi,\pi}^j$ for some $j$. This
    $game[\pi$ restricts actions of \Eve, we immediately get $i \ge
    j$. Hence, applying the line of inequalities at the beginning of
    the proof of the larger lemma,
    $\textrm{val}_{\mathcal{G}\sigma_\pi}(\pi_j) \le
    \textrm{val}_{\mathcal{G}\sigma_\pi}(\pi_i)$.

    If \Eve plays with $\sigma^{(1)}$, the definition of
    $\sigma_{\pi}$ ensures that the first random vertex (or
    terminal vertex) which is visited when starting in $v$ belongs to
    $\{\pi_i,\pi_{i+1},\dots,\pi_k,\ensuremath{v_{\textsc{win}}}}$, so since from
    that vertex, $\sigma^{(1)}$ plays according to $\sigma_\pi, we
    get:
    

$$
    \val_{\mathcal{G}\sigma^{(1)}}(v) \ge \min
    \{\textrm{val}_{\mathcal{G}\sigma_\pi}(\pi_i),
    \textrm{val}_{\mathcal{G}\sigma_\pi}(\pi_{i+1}),\dots,
    \textrm{val}_{\mathcal{G}\sigma_\pi}(\pi_k),1\} \ge
    \textrm{val}_{\mathcal{G}\sigma_\pi}(\pi_i)
    $$

    since $\textrm{val}_{\mathcal{G}\sigma_\pi} = \val_{\mathcal{G}\sigma_\pi$.

    Now, when playing $\sigma_\pi= \sigma^{(0)}$ from $v$, 

    Thanks to  {prf:ref}`6-lem:lemma2`, since $v \in
    W_{\mathcal{G}\sigma_\pi,\pi}^j$,
    $\val_{\mathcal{G}\sigma_\pi,\pi}(v) =
    \val_{\mathcal{G}\sigma_\pi,\pi}(\pi_j)$ and hence (as argued
    in the proof of the larger lemma,
    $\val_{\mathcal{G}\sigma_\pi,\pi} =
    \textrm{val}_{\mathcal{G}\sigma_\pi}$), $\textrm{val}_{\mathcal{G}\sigma_\pi}(v) =
    \textrm{val}_{\mathcal{G}\sigma_\pi}(\pi_j)$. We conclude that:
    

$$
    \val_{\sigma_\pi(v) = \textrm{val}_{\mathcal{G}\sigma_\pi}(v) \le
    \textrm{val}_{\mathcal{G}\sigma_\pi}(\pi_j) \le
    \textrm{val}_{\mathcal{G}\sigma_\pi}(\pi_i) \le
    \val_{\mathcal{G}\sigma^{(1)}}(v)
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

  Let $\tau$ be an \textrm{Adam}s strategy. Since $\pi$ has been shown to
  be live in $\mathcal{G}, applying  {prf:ref}`6-lem:stopping`, we
  get that: $\mathbb{P}v_{\sigma_{\pi},\tau} (\mathtt{Reach}\{\ensuremath{v_{\textsc{win}}}})) =
  \mathbb{P}v_{\sigma_{\pi},\tau} (\neg\mathtt{Reach}\{\ensuremath{v_{\textsc{lose}}}}))$. This last
  probability value coincides with $\lim_{n \to +\infty}
  \mathbb{P}v_{\sigma_{\pi},\tau} (\neg\Reach_{\le n}(\{\ensuremath{v_{\textsc{lose}}}}))$,
  the probability to not reach $\ensuremath{v_{\textsc{lose}}} for the first $n$ visits to a
  random vertex; for these $n$ first visits, $\sigma_{\pi}$
  coincides with $\sigma^{(n)}$, hence
  $\mathbb{P}v_{\sigma_{\pi},\tau} (\mathtt{Reach}\{\ensuremath{v_{\textsc{win}}}})) \ge \lim_{n\to
    +\infty} \mathbb{P}v_{\sigma^{(n)},\tau} (\mathtt{Reach}\{\ensuremath{v_{\textsc{win}}}}))$. By
  definition of value in a game, this last term is larger than or
  equal to $\lim_{n \to+\infty}\val_{\mathcal{G}\sigma^{(n)}}$, hence
  $\lim_{n \to+\infty}\val_{\mathcal{G}\sigma^{(n)}} \le
  \val_{\mathcal{G}\pi}$.

  We conclude that:
  

$$
  \textrm{val}_{\mathcal{G}\sigma_\pi} = \val_{\mathcal{G}\sigma^{(0)}} \le
  \val_{\mathcal{G}\sigma^{(1)}} \le \val_{\mathcal{G}\sigma^{(2)}} \le \dots\le
  \lim_{n \to +\infty} \val_{\mathcal{G}\sigma^{(n)}} \le
  \textrm{val}_{\mathcal{G}\sigma_{\pi}]}
  $$


  \medskip Assume now that $\textrm{val}_{\mathcal{G}\sigma_\pi} =
  \textrm{val}_{\mathcal{G}\sigma_{\pi}]}$. Then applying the first line of
  inequalities above, we get:
  

$$
  \textrm{val}_{\mathcal{G}\sigma_{\pi}]}(\pi_1) \le
  \textrm{val}_{\mathcal{G}\sigma_{\pi}]}(\pi_2) \le \dots \le
  \textrm{val}_{\mathcal{G}\sigma_{\pi}]}(\pi_k)
  $$

  Now, the strategy $\tau_{\pi}$ is precisely the optimal strategy
  against $\sigma_{\pi}$ \pat{Not so sure of the argument, it is
    not argued that way in GH09}, hence for every vertex $v$:
  

$$
  \textrm{val}_{\mathcal{G}\sigma_{\pi}]}(v) = \inf_\tau
  \mathbb{P}v_{\sigma_{\pi},\tau} (\mathtt{Reach}\{\ensuremath{v_{\textsc{win}}}})) =
  \mathbb{P}v_{\sigma_{\pi},\tau_{\pi}} (\mathtt{Reach}\{\ensuremath{v_{\textsc{win}}}})) =
  \val_{\mathcal{G}\pi}
  $$

  We deduce that
  

$$
  \val_{\mathcal{G}\pi}(\pi_1) \le \val_{\mathcal{G}\pi}(\pi_2) \le
  \dots \le \val_{\mathcal{G}\pi}(\pi_k)
  $$

  which is precisely the definition of a self-consistent permutation
  in $\mathcal{G}, so we are done.
  
  
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
