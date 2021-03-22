(6-sec:notations)=
# Notations

Let us first define the arenas stochastic games will be played on:

````{prf:definition} Stochastic arenas
:label: 6-def:stochastic_arenas

A stochastic arena is a tuple $\mathcal{A} = ( V,E,\delta)$ where

*  $V =  V_\mathrm{Adam} \sqcup  V_\mathrm{Eve} \sqcup   V_{\text{Rand}}$ is a
finite set of vertices, partitionned into vertices of Adam, Eve,
and random vertices;
*  $E \subseteq  V \times  V$ is the set of
edges;
*  $\delta :   V_{\text{Rand}} \to  \mathcal{D}( V)$ is the
probabilistic transition function, which satisfies:
$\forall v \in   V_{\text{Rand}}$, $\delta(v)(w)>0$ iff
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

````{prf:definition} Stochastic games
:label: 6-def:stochastic_games

A stochastic game is a tuple $\mathcal{G} = ( \mathcal{A},\Omega)$ where

*  $\mathcal{A}$ is a stochastic arena;
*  $\Omega \subseteq  V^\omega$ is the (qualitative)
winning objective.

````

For $\textrm{Win} \subseteq  V$, letting $\Omega =  \mathtt{Reach}( \textrm{Win})$ gives
rise to a stochastic reachability game.
Of course, one may consider more general $\omega$-regular
properties. We write $\mathds{1}_\Omega$ for the characteristic
function of the winning objective $\Omega$.

In this game, Eve aims at maximizing the probability that a play
belongs to $\Omega$, while Adam has the opposite objective of
minimizing that probability. In that sense, we study quantitative
games, although the winning objective is qualitative.

A **strategy** for Eve is a function
$\sigma: V^*  V_\mathrm{Eve} \to  \mathcal{D}( V)$ such that whenever
$\sigma(h v)(v') >0$ then $(v,v') \in E$. Similarly, one can define
strategies for Adam. When a strategy profile $(\sigma,\tau)$ is
fixed, and assuming the arena is clear from context, we write
$\mathbb{P}_{\sigma,\tau}^v$ for the probability measure on infinite plays
when the initial vertex is $v$. In particular,
$\mathbb{P}_{\sigma,\tau}^v(\mathds{1}_\Omega)$ is the outcome of the profile
$(\sigma,\tau)$.

The **value for Eve** in $\mathcal{G}$ from $v$ is defined as
$\textrm{val}_\mathrm{Eve}^ \mathcal{G}(v) = \sup_{\sigma} \inf_{\tau}
 \mathbb{P}_{\sigma,\tau}^v(\mathds{1}_\Omega)$, whereas symmetrically the
**supremum value** is
$\textrm{val}_\mathrm{Adam}^ \mathcal{G}(v) = \inf_{\tau}\sup_{\sigma}
 \mathbb{P}_{\sigma,\tau}^v(\mathds{1}_\Omega)$. Clearly enough,
$\textrm{val}_\mathrm{Eve}^ \mathcal{G}(v) \leq  \textrm{val}_\mathrm{Adam}^ \mathcal{G}(v)$.  When the converse
inequality holds, the game is **determined** and the **value**
of $v$ in $\mathcal{G}$ is denoted $\textrm{val}^ \mathcal{G}(v)$. Moreover, if the value
is attained by positional strategies $\sigma$ and $\tau$, $\mathcal{G}$ is
said to be **positionally determined**. **Strong determinacy**
means that for every threshold $c$, either Eve has a strategy to
ensure that the probability that the play belongs to $\Omega$ is at
least $c$, or Adam has a strategy to ensure probability $< c$ to for
the set of plays satisfying $\Omega$.

Back to the example of Figure {numref}`6-fig:ex-stoch-arena`, assume that
Eve and Adam play the following pure positional strategies:
$\sigma(v_0) = v_1$, $\sigma(v_2) = v_3$, $\sigma(v_5) = v_5$ and
$\tau(v_6) = v_5$. Under such a strategy profile, starting in $v_0$,
the probability to reach $v_7$ is
$\mathbb{P}_{\sigma,\tau}^{v_0}(\mathds{1}_{ \mathtt{Reach}(\{v_7\})}) = \frac 2
3$. In fact, strategy $\sigma$ for Eve is optimal for the
reachability objective $\mathtt{Reach}(\{v_7\})$, and we will justify that
$\textrm{val}_\mathrm{Eve}^ \mathcal{G}(v_0) =  \textrm{val}_\mathrm{Adam}^ \mathcal{G}(v_0) = \frac 2 3$.

