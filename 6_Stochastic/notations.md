(6-sec:notations)=
# Notations

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
```
Let us first define the arenas stochastic games will be played on:

````{prf:definition} NEEDS TITLE AND LABEL 
  A stochastic arena is a tuple $\arena = (\vertices,E,\delta)$ where
  
  *  $\vertices = \VA \sqcup \VE \sqcup \Randomvertices$ is a
    finite set of vertices, partitionned into vertices of Adam, Eve,
    and random vertices;
  *  $E \subseteq \vertices \times \vertices$ is the set of
    edges;
  *  $\delta : \Randomvertices \to \dist(\vertices)$ is the
    probabilistic transition function, which satisfies:
    $\forall v \in \Randomvertices$, $\delta(v)(w)>0$ iff
    $(v,w) \in E$.
  
 

  A stochastic arena is a tuple $\arena = (\vertices,E,\delta)$ where
  
  *  $\vertices = \VA \sqcup \VE \sqcup \Randomvertices$ is a
    finite set of vertices, partitionned into vertices of Adam, Eve,
    and random vertices;
  *  $E \subseteq \vertices \times \vertices$ is the set of
    edges;
  *  $\delta : \Randomvertices \to \dist(\vertices)$ is the
    probabilistic transition function, which satisfies:
    $\forall v \in \Randomvertices$, $\delta(v)(w)>0$ iff
    $(v,w) \in E$.
  

````


```{figure} ./../FigAndAlgos/6-fig:ex-stoch-arena.png
:name: 6-fig:ex-stoch-arena
:align: center
Example of a stochastic arena: circle nodes belong to Eve,
    square nodes to Adam, and diamond nodes are random.
```

Similarly to non-stochastic arenas, one can equip a stochastic arena
with a winning objectives to define a stochastic game.

````{prf:definition} NEEDS TITLE AND LABEL 
  A stochastic game is a tuple $\game = (\arena,\Omega)$ where
  
  *  $\arena$ is a stochastic arena;
  *  $\Omega \subseteq \vertices^\omega$ is the (qualitative)
    winning objective.
  
 

  A stochastic game is a tuple $\game = (\arena,\Omega)$ where
  
  *  $\arena$ is a stochastic arena;
  *  $\Omega \subseteq \vertices^\omega$ is the (qualitative)
    winning objective.
  

````

For $\Win \subseteq \vertices$, letting $\Omega = \Reach(\Win)$ gives
rise to a stochastic reachability game.
Of course, one may consider more general $\omega$-regular
properties. We write $\mathds{1}_\Omega$ for the characteristic
function of the winning objective $\Omega$.

In this game, Eve aims at maximizing the probability that a play
belongs to $\Omega$, while Adam has the opposite objective of
minimizing that probability. In that sense, we study quantitative
games, although the winning objective is qualitative.

A **strategy** for Eve is a function
$\sigma: V^* \VE \to \dist(\vertices)$ such that whenever
$\sigma(h v)(v') >0$ then $(v,v') \in E$. Similarly, one can define
strategies for Adam. When a strategy profile $(\sigma,\tau)$ is
fixed, and assuming the arena is clear from context, we write
$\probm_{\sigma,\tau}^v$ for the probability measure on infinite plays
when the initial vertex is $v$. In particular,
$\probm_{\sigma,\tau}^v(\mathds{1}_\Omega)$ is the outcome of the profile
$(\sigma,\tau)$.

% is evident.% $\sigma$: strategies of Eve; $\tau$: strategies of Adam

The **value for Eve** in $\game$ from $v$ is defined as
$\ValueE^\game(v) = \sup_{\sigma} \inf_{\tau}
\probm_{\sigma,\tau}^v(\mathds{1}_\Omega)$, whereas symmetrically the
**supremum value** is
$\ValueA^\game(v) = \inf_{\tau}\sup_{\sigma}
\probm_{\sigma,\tau}^v(\mathds{1}_\Omega)$. Clearly enough,
$\ValueE^\game(v) \leq \ValueA^\game(v)$.  When the converse
inequality holds, the game is **determined** and the **value**
of $v$ in $\game$ is denoted $\Value^\game(v)$. Moreover, if the value
is attained by positional strategies $\sigma$ and $\tau$, $\game$ is
said to be **positionally determined**. **Strong determinacy**
means that for every threshold $c$, either Eve has a strategy to
ensure that the probability that the play belongs to $\Omega$ is at
least $c$, or Adam has a strategy to ensure probability $< c$ to for
the set of plays satisfying $\Omega$.

Back to the example of Figure~\ref{6-fig:ex-stoch-arena}, assume that
Eve and Adam play the following pure positional strategies:
$\sigma(v_0) = v_1$, $\sigma(v_2) = v_3$, $\sigma(v_5) = v_5$ and
$\tau(v_6) = v_5$. Under such a strategy profile, starting in $v_0$,
the probability to reach $v_7$ is
$\probm_{\sigma,\tau}^{v_0}(\mathds{1}_{\Reach(\{v_7\})}) = \frac 2
3$. In fact, strategy $\sigma$ for Eve is optimal for the
reachability objective $\Reach(\{v_7\})$, and we will justify that
$\ValueE^\game(v_0) = \ValueA^\game(v_0) = \frac 2 3$.

