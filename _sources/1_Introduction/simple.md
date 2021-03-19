(1-sec:simple)=
# A first model of games

```{math}

\renewcommand{\Game}{\game}

```

The first model we define is the common denominator of most models studied in this book:

*  $2$-player,
*  zero sum,
*  turn based,
*  perfect information

game.

## Players

The term $2$-player means that there are two players, Eve and Adam.
Many, many different names have been used: Player $0$ and Player $1$, 
Player I and Player II as in descriptive complexity,
&Eacute;lo&iuml;se and Ab&eacute;lard, Circle and Square, corresponding to the graphical representation, 
Even and Odd, mostly for parity objectives, Player and Opponent, Pathfinder and Verifier in the context of automata,
Max and Min, which makes sense for quantitative objectives,
and this is only a very partial list of names they have been given.
In the names Eve and Adam, the first letters refer to $\exists$ and $\forall$ suggesting a duality between them.
We will make use of their gender to distinguish between them, so we speak of her or his strategy.

We speak of $1$-player games when there is only one player.
In the context of stochastic games, we refer to random as a third player, and more precisely as half a player.
Hence a $2\frac{1}{2}$-player game is a stochastic game with two players,
and a $1\frac{1}{2}$-player game is a stochastic game with one player.

The situation where there are more than two players is called multiplayer games.

## Graphs

A (directed) graph is given by a set $V$ of vertices and a set $E \subseteq V \times V$ of edges.
For an edge $e = (v,v')$ we write $In(e)$ for the incoming vertex $v$ and 
$Out(e)$ for the outgoing vertex $v'$:
we say that $e$ is an outgoing edge of $v$ and an incoming edge to $v'$.

A path $\pi = v_0 v_1 \cdots$ is a non empty finite or infinite sequence of consecutive vertices: 
for all $i$ we have $(v_i,v_{i+1}) \in E$.
We let $first(\pi)$ denote the first vertex occurring in $\pi$ and $last(\pi)$ the last one if $\pi$ is finite.
We say that $\pi$ starts from $first(\pi)$ and if $\pi$ is finite $\pi$ ends in $last(\pi)$.
We sometimes talk of a path and let the context determine whether it is finite or infinite.

We let $Paths(G) \subseteq V^+$ denote the set of finite paths in the graph $G$, sometimes omitting $G$ when clear from the context.
To restrict to paths starting from $v$ we write $Paths(G,v)$.
The set of infinite paths is $Paths_\omega(G) \subseteq V^\omega$, and $Paths_\omega(G,v)$ for those starting from $v$.

We use the standard terminology of graphs: 
for instance 
a vertex $v'$ is a successor of $v$ if $(v,v') \in E$,
and then $v$ is a predecessor of $v'$,
a vertex $v'$ is reachable from $v$ if there exists a path starting from $v$
and ending in $v'$,
the outdegree of a vertex is its number of outgoing edges,
the indegree is its number of incoming edges,
a simple path is a path with no repetitions of vertices,
a cycle is a path whose first and last vertex coincide,
it is a simple cycle if it does not strictly contain another cycle,
a self loop is an edge from a vertex to itself,
and a sink is a vertex with only a self loop as outgoing edge.

## Arenas

The arena is the place where the game is played, they have also been called game structures or game graphs.

In the turn based setting we define here, the set of vertices is divided into vertices controlled by each player.
Since we are for now interested in **$2$-player** games, 
we have $V =  V_\mathrm{Eve} \uplus  V_\mathrm{Adam}$, where $V_\mathrm{Eve}$ is the set of vertices controlled by Eve and $V_\mathrm{Adam}$ the set of vertices controlled by Adam.
We represent vertices in $V_\mathrm{Eve}$ by circles, and vertices in $V_\mathrm{Adam}$ by squares, and also say that $v \in  V_\mathrm{Eve}$
belongs to Eve, or that Eve owns or controls $v$, and similarly for Adam.
An arena is given by a graph and the sets $V_\mathrm{Eve}$ and $V_\mathrm{Adam}$.
In the context of games, vertices are often referred to as positions.

The adjective **finite** means that the arena is finite, **i.e.** there are finitely many vertices (hence finitely many edges).
We oppose **deterministic** to **stochastic**: in the first definition we are giving here, 
there is no stochastic aspect in the game.
An important assumption, called **perfect information**, says that the players see everything about how the game
is played out, in particular they see the other player's moves.

```{figure} ./../FigAndAlgos/1-fig:arena_example.png
:name: 1-fig:arena_example
:align: center
An example of an arena. Circles are controlled by Eve and squares by Adam.
```
Our definition of an arena does not include the initial vertex. 

We assume that all vertices have an outgoing edge.
This is for technical convenience, as it implies that we do not need to explain what happens when a play cannot be prolonged.

## Playing

The interaction between the two players consists in moving a token on the vertices of the arena.
The token is initially on some vertex.
When the token is in some vertex $v$, the player who controls the vertex chooses an outgoing edge $e$ of $v$
and pushes the token along this edge to the next vertex $Out(e) = v'$.
The outcome of this interaction is the sequence of vertices traversed by the token: it is a path. 
In the context of games a path is also called a play and as for paths usually written $\pi$.
We note that plays can be finite (but non empty) or infinite.

## Strategies

The most important notion in this book is that of **strategies** (sometimes called policies).
A strategy for a player is a full description of his or her moves in all situations.
Formally, a strategy is a function mapping finite plays to edges:

$$
\sigma :  Paths \to E.
$$

We use $\sigma$ for strategies of Eve and $\tau$ for strategies of Adam so when considering a strategy $\sigma$ it is implicitly for Eve,
and similarly $\tau$ is implicitly a strategy for Adam.

We say that a play $\pi = v_0 v_1 \dots$ is consistent with a strategy $\sigma$ of Eve if
for all $i$ such that $v_i \in  V_\mathrm{Eve}$ we have $\sigma( \pi_{\le i}) = (v_i,v_{i+1})$.
The definition is easily adapted for strategies of Adam.

Once an initial vertex $v$ and two strategies $\sigma$ and $\tau$ have been fixed, 
there exists a unique infinite play starting from $v$ and consistent with both strategies written $\pi^{v}_{\sigma,\tau}$.
Note that the fact that it is infinite follows from our assumption that all vertices have an outgoing edge.

## Conditions

The last ingredient to wrap up the definitions is (winning) conditions, which is what Eve wants to achieve.
There are two types of conditions: the **qualitative**, or Boolean ones, and the **quantitative** ones.

A qualitative condition is $W \subseteq  Paths_\omega$: it separates winning from losing plays, in other words a play which belongs to $W$ is winning and otherwise it is losing. We also say that the play satisfies $W$.
In the zero sum context a play which is losing for Eve is winning for Adam, so Adam's condition is $Paths_\omega \setminus W$.

A quantitative condition is $f :  Paths_\omega \to   \mathbb{R} \cup  \left\{ \pm \infty \right\}$: it assigns a real value (or plus or minus infinity) to a play, which can be thought of as a payoff or a score.
In the zero sum context Eve wants to maximise while Adam wants to minimise the outcome.

Often we define $W$ as a subset of $V^\omega$ and $f$ as $f : V^\omega \to   \mathbb{R} \cup  \left\{ \pm \infty \right\}$,
since $Paths_\omega$ is included in $V^\omega$.

## Objectives

To reason about classes of games with the same conditions, we introduce the notions of objectives and colouring functions.
An objective and a colouring function together induce a condition.
The main point is that **objectives are independent of the arenas**, so we can speak of the class of conditions induced by a given objective,
and by extension a class of games induced by a given objective, for instance parity games.

We fix a set $C$ of colours. 
A qualitative objective is $\Omega \subseteq C^\omega$, and a quantitative objective is a function $\Phi : C^\omega \to   \mathbb{R} \cup  \left\{ \pm \infty \right\}$. 

The link between an arena and an objective is given by a colouring function $\textsf{col} : V \to C$ labelling vertices of the graph by colours.
We extend $\textsf{col}$ componentwise to induce $\textsf{col} :  Paths_\omega \to C^\omega$ mapping plays to sequences of colours:

$$
 \textsf{col}(v_0 v_1 \dots) =  \textsf{col}(v_0)\  \textsf{col}(v_1) \dots
$$

A qualitative objective $\Omega$ and a colouring function $\textsf{col}$ induce a qualitative condition $\Omega[ \textsf{col}]$ defined by:

$$
\Omega[ \textsf{col}] =  \left\{  \pi \in  Paths_\omega :  \textsf{col \right\}( \pi) \in \Omega}.
$$

When $\textsf{col}$ is clear from the context we sometimes say that a play $\pi$ satisfies $\Omega$ but the intended meaning is that 
$\pi$ satisfies $\Omega[ \textsf{col}]$, equivalently that $\textsf{col}( \pi) \in \Omega$.

Similarly, a quantitative objective $\Phi : C^\omega \to   \mathbb{R} \cup  \left\{ \pm \infty \right\}$ and a colouring function $\textsf{col}$ induce 
a quantitative condition $\Phi[ \textsf{col}] :  Paths_\omega \to   \mathbb{R} \cup  \left\{ \pm \infty \right\}$ defined by:

$$
\Phi[ \textsf{col}]( \pi) = \Phi( \textsf{col}( \pi)).
$$

````{prf:remark} NEEDS TITLE AND LABEL 
In our definition the colouring function labels vertices.
Another more general definition would label edges, and yet another relaxation would be to allow partial functions,
meaning that some vertices (or edges) are not labelled by a colour.
In most cases the variants are all (in some sense) equivalent; 
whenever we use a different definition we will make it explicit by referring for instance to edge colouring functions
or partial colouring functions.

In our definition the colouring function labels vertices.
Another more general definition would label edges, and yet another relaxation would be to allow partial functions,
meaning that some vertices (or edges) are not labelled by a colour.
In most cases the variants are all (in some sense) equivalent; 
whenever we use a different definition we will make it explicit by referring for instance to edge colouring functions
or partial colouring functions.

````

## Games

We can now give the following definitions.

````{prf:definition} NEEDS LABEL Games

*  A graph is a tuple $G = (V,E)$ where $V$ is a set of vertices
and $E$ is a set of edges.

*  An arena is a tuple $\mathcal{A} = (G, V_\mathrm{Eve}, V_\mathrm{Adam})$ where $G$ is a graph over the set of vertices $V$ and $V =  V_\mathrm{Eve} \uplus  V_\mathrm{Adam}$.

*  A colouring function is a function $\textsf{col} : V \to C$ where $C$ is a set of colours.

*  A qualitative condition is $W \subseteq  Paths_\omega$.

*  A qualitative objective is a subset $\Omega \subseteq C^\omega$.
A colouring function $\textsf{col}$ and a qualitative objective $\Omega$ induce 
a qualitative condition $\Omega[ \textsf{col}]$.

*  A qualitative game $\mathcal{G}$ is a tuple $( \mathcal{A},W)$ where $\mathcal{A}$ is an arena and $W$ a qualitative condition.

*  A quantitative condition is $f :  Paths_\omega \to   \mathbb{R} \cup  \left\{ \pm \infty \right\}$.

*  A quantitative objective $\Phi$ is a function $\Phi : C^\omega \to   \mathbb{R} \cup  \left\{ \pm \infty \right\}$.
A colouring function $\textsf{col}$ and a quantitative objective $\Phi$ induce 
a quantitative condition $\Phi[ \textsf{col}]$.

*  A quantitative game $\mathcal{G}$ is a tuple $( \mathcal{A},f)$ where $\mathcal{A}$ is an arena and $f$ a quantitative condition.

````

To be specific, the definition above is for $2$-player zero sum turn based perfect information games.
As a convention we use the condition to qualify games, so for instance parity games are games equipped with a parity condition.
This extends to graphs: we speak of a graph with condition $W$ for a graph equipped with a condition $W$,
and for instance a mean payoff graph if $W$ is a mean payoff condition.

We often introduce notations implicitly: for instance when we introduce a qualitative game $\Game$ without specifying the arena and the condition, it is understood that the arena is $\mathcal{A}$ and the condition $W$.

We always implicitly take the point of view of Eve. 
Since we consider zero sum games we can easily reverse the point of view by considering the qualitative game 
$( \mathcal{A}, Paths_\omega \setminus W)$ and the qualitative game $( \mathcal{A},-f)$.
Indeed for the latter Adam wants to minimise $f$, which is equivalent to maximising $-f$.
The term zero sum comes from this: the total outcome for the two players is $f + (-f)$, meaning zero.

````{prf:remark} NEEDS TITLE AND LABEL 
Unless otherwise stated we assume that graphs are finite, meaning that there are finitely many vertices (hence finitely many edges).
We equivalently say that the arena or the game is finite.
Part {ref}`part:infinite` will study games over infinite graphs.

Unless otherwise stated we assume that graphs are finite, meaning that there are finitely many vertices (hence finitely many edges).
We equivalently say that the arena or the game is finite.
Part {ref}`part:infinite` will study games over infinite graphs.

````

## Winning in qualitative games

Now that we have the definitions of a game we can ask the main question: 
given a game $\mathcal{G}$ and a vertex $v$, who wins $\mathcal{G}$ from $v$?

Let $\mathcal{G}$ be a qualitative game and $v$ a vertex.
A strategy $\sigma$ for Eve is called winning from $v$ if every play starting from $v$ consistent with $\sigma$ is winning, 
**i.e.** satisfies $W$.
Another common terminology is that $\sigma$ ensures $W$.
In that case we say that Eve has a winning strategy from $v$ in $\mathcal{G}$, or equivalently that Eve wins $\mathcal{G}$ from $v$.
This vocabulary also applies to Adam: for instance 
a strategy $\tau$ for Adam is called winning from $v$ if every play starting from $v$ consistent with $\tau$ is losing, 
**i.e.** does not satisfy $W$.

We let $W_\mathrm{Eve}( \mathcal{G})$ denote the set of vertices $v$ such that Eve wins $\mathcal{G}$ from $v$,
it is called winning region, or sometimes winning set. 
A vertex in $W_\mathrm{Eve}( \mathcal{G})$ is said winning for Eve.
The analogous notation for Adam is $W_\mathrm{Adam}( \mathcal{G})$.

We say that a strategy is optimal if it is winning from all vertices in $W_\mathrm{Eve}( \mathcal{G})$.

````{prf:observation} Winning regions are disjoint
:label: 1-fact:winning_regions_disjoint

For all qualitative games $\mathcal{G}$ we have $W_\mathrm{Eve}( \mathcal{G}) \cap  W_\mathrm{Adam}( \mathcal{G}) = \emptyset$.

````

````{admonition} Proof
:class: dropdown tip

Assume for the sake of contradiction that both players have a winning strategy from $v$, then $\pi^{v}_{\sigma,\tau}$
would both satisfy $W$ and not satisfy $W$, a contradiction.

````

It is however not clear that for every vertex $v$, **some** player has a winning strategy from $v$,
which symbolically reads $W_\mathrm{Eve}( \mathcal{G}) \cup  W_\mathrm{Adam}( \mathcal{G}) = V$.
One might imagine that if Eve picks a strategy, then Adam can produce a counter strategy beating Eve's strategy, 
and vice versa, if Adam picks a strategy, then Eve can come up with a strategy winning against Adam's strategy.
A typical example would be rock-paper-scissors (note that this is a concurrent game, meaning the two players play simultanously,
hence it does not fit in the definitions given so far), where neither player has a winning strategy.

Whenever $W_\mathrm{Eve}( \mathcal{G}) \cup  W_\mathrm{Adam}( \mathcal{G}) = V$, we say that the game is determined.
Being determined can be understood as follows: the outcome can be determined before playing assuming both players play optimally since one of them can ensure to win whatever is the strategy of the opponent.

````{prf:theorem} Borel determinacy
:label: 1-thm:borel_determinacy

Qualitative games with Borel conditions are determined.

````

The definition of Borel sets goes beyond the scope of this book. 
Suffice to say that all conditions studied in this book are (very simple) examples of Borel sets,
implying that our qualitative games are all determined 
(as long as we consider perfect infomation and turn based games, the situation will change with more general models of games).

## Computational problems for qualitative games

We identify three computational problems.
The first is that of solving a game, which is the simplest one and since it induces a decision problem, allows us 
to make complexity theoretic statements.

```{admonition} Problem

For qualitative games, solving the game means solving the following decision problem:

**INPUT**: A qualitative game $\mathcal{G}$ and a vertex $v$

**QUESTION**: Does Eve win $\mathcal{G}$ from $v$?

```

The second problem extends the previous one: most algorithms solve games for all vertices at once instead of only for the given initial vertex.
This is called computing the winning regions.

```{admonition} Problem

For qualitative games, computing the winning regions means solving the following computational task:

**INPUT**: A qualitative game $\mathcal{G}$

**COMPUTE**: $W_\mathrm{Eve}( \mathcal{G})$ and $W_\mathrm{Adam}( \mathcal{G})$

```

The third problem is constructing a winning strategy.

```{admonition} Problem

For qualitative games, constructing a winning strategy means solving the following computational task:

**INPUT**: A qualitative game $\mathcal{G}$ and a vertex $v$

**COMPUTE**: A winning strategy for Eve from $v$

```

We did not specify how the winning regions or the winning strategies are represented, this will depend on the types of games we consider.

## Values in quantitative games

Let $\mathcal{G}$ be a quantitative game and $v$ a vertex.
Given $x \in  \mathbb{R}$ called a threshold, we say that a strategy $\sigma$ for Eve ensures $x$ from $v$ 
if every play $\pi$ starting from $v$ consistent with $\sigma$ has value at least $x$ under $f$,
**i.e.** $f( \pi) \ge x$.
In that case we say that Eve has a strategy ensuring $x$ in $\mathcal{G}$ from $v$.

Note that by doing so we are actually considering a qualitative game in disguise, 
where the qualitative condition is the set of plays having value at least $x$ under $f$.
Formally, a quantitative condition $f$ and a threshold $x$ induce a qualitative condition

$$
f_{\ge x} =  \left\{  \pi \in  Paths_\omega \mid f( \pi) \ge x \right\}.
$$

Analogously, we say that a strategy $\tau$ for Adam ensures $x$ from $v$ 
if every play $\pi$ starting from $v$ consistent with $\tau$ has value at most $x$ under $f$,
**i.e.** $f( \pi) \le x$.

We let $val_\mathrm{Eve}^{ \mathcal{G}}(v)$ denote the quantity

$$
\sup_{\sigma} \inf_{\tau} f( \pi_{\sigma,\tau}^{v}),
$$

where $\sigma$ ranges over all strategies of Eve and $\tau$ over all strategies of Adam.
We also write $val_\mathrm{Eve}^{\sigma}(v) = \inf_{\tau} f( \pi_{\sigma,\tau}^{v})$
so that $val_\mathrm{Eve}^{ \mathcal{G}}(v) = \sup_{\sigma}  val_\mathrm{Eve}^\sigma(v)$.
This is called the value of Eve in the game $\mathcal{G}$ from $v$,
and represents the best outcome that she can ensure against any strategy of Adam.
Note that $val_\mathrm{Eve}^{ \mathcal{G}}(v)$ is either a real number, $\infty$, or $-\infty$.

A strategy $\sigma$ such that $val_\mathrm{Eve}^\sigma(v) =  val_\mathrm{Eve}^{ \mathcal{G}}(v)$ is called optimal from $v$,
and it is simply optimal if the equality holds for all vertices.
Equivalently, $\sigma$ is optimal from $v$ if for every play $\pi$ consistent with $\sigma$ starting from $v$ 
we have $f( \pi) \ge  val_\mathrm{Eve}^{ \mathcal{G}}(v)$.

There may not exist optimal strategies which is why we introduce the following notion.
For $\varepsilon > 0$, a strategy $\sigma$ such that $val_\mathrm{Eve}^\sigma(v) \ge  val_\mathrm{Eve}^{ \mathcal{G}}(v) - \varepsilon$
is called $\varepsilon$-optimal.
If $val_\mathrm{Eve}^{ \mathcal{G}}(v)$ is finite there exist $\varepsilon$-optimal strategies for any $\varepsilon > 0$.

Symmetrically, we let $val_\mathrm{Adam}^{ \mathcal{G}}(v)$ denote

$$
\inf_{\tau} \sup_{\sigma} f( \pi_{\sigma,\tau}^{v}).
$$

````{prf:observation} Comparison of values for Eve and Adam
:label: 1-fact:comparaison_values_eve_adam

For all quantitative games $\mathcal{G}$ and vertex $v$ we have $val_\mathrm{Eve}^{ \mathcal{G}}(v) \le  val_\mathrm{Adam}^{ \mathcal{G}}(v)$.

````

````{admonition} Proof
:class: dropdown tip

For any function $F : X \times Y \to   \mathbb{R} \cup  \left\{ \pm \infty \right\}$, we have

$$
\sup_{x \in X} \inf_{y \in Y} F(x,y) \le \inf_{y \in Y} \sup_{x \in X} F(x,y).
$$

````

If this inequality is an equality, we say that the game $\mathcal{G}$ is **determined** in $v$,
and let $val^{ \mathcal{G}}(v)$ denote the value in the game $\mathcal{G}$ from $v$
and $val^\sigma(v)$ for $\inf_{\tau} f( \pi_{\sigma,\tau}^{v})$.
Similarly as for the qualitative case, being determined can be understood as follows: the outcome can be determined before playing assuming both players play optimally, and in that case the outcome is the value.

We say that a quantitative objective $f : C^\omega \to   \mathbb{R} \cup  \left\{ \pm \infty \right\}$ is Borel if for all $x \in  \mathbb{R}$,
the qualitative objective $f_{\ge x} \subseteq C^\omega$ is a Borel set.

````{prf:corollary} Borel determinacy for quantitative games
:label: 1-cor:borel_determinacy

Quantitative games with Borel conditions are determined, meaning that
for all quantitative games $\mathcal{G}$ we have $val_\mathrm{Eve}^{ \mathcal{G}} =  val_\mathrm{Adam}^{ \mathcal{G}}$.

````

````{admonition} Proof
:class: dropdown tip

If $val_\mathrm{Eve}^{ \mathcal{G}}(v) = \infty$ then thanks to the inequality above $val_\mathrm{Adam}^{ \mathcal{G}}(v) = \infty$ and the equality holds.
Assume $val_\mathrm{Eve}^{ \mathcal{G}}(v) = -\infty$ and let $r$ be a real number.
(The argument is actually the same as for the finite case but for the sake of clarity we treat them independently.)
We consider $f_{\ge r}$.
By definition, this a qualitative Borel condition, so {prf:ref}`1-thm:borel_determinacy` implies that it is determined.
Since Eve cannot have a winning strategy for $f_{\ge r}$, as this would contradict the definition of $val_\mathrm{Eve}^{ \mathcal{G}}(v)$,
this implies that Adam has a winning strategy for $f_{\ge r}$, 
meaning a strategy $\tau$ such that every play $\pi$ starting from $v$ consistent with $\tau$ satisfy $f( \pi) < r$.
In other words, $val_\mathrm{Adam}^{\tau}(v) = \sup_{\sigma} f( \pi_{\sigma,\tau}^{v}) \le r$, which implies that $val_\mathrm{Adam}^{ \mathcal{G}}(v) \le r$.
Since this is true for any real number $r$, this implies $val_\mathrm{Adam}^{ \mathcal{G}}(v) = -\infty$.

Let us now assume that $x =  val_\mathrm{Eve}^{ \mathcal{G}}(v)$ is finite and let $\varepsilon > 0$.
We consider $f_{\ge x + \varepsilon}$.
By definition, this a qualitative Borel condition, so {prf:ref}`1-thm:borel_determinacy` implies that it is determined.
Since Eve cannot have a winning strategy for $f_{\ge x + \varepsilon}$, as this would contradict the definition of $val_\mathrm{Eve}^{ \mathcal{G}}(v)$,
this implies that Adam has a winning strategy for $f_{\ge x + \varepsilon}$, 
meaning a strategy $\tau$ such that every play $\pi$ starting from $v$ consistent with $\tau$ satisfy $f( \pi) < x + \varepsilon$.
In other words, $val_\mathrm{Adam}^{\tau}(v) = \sup_{\sigma} f( \pi_{\sigma,\tau}^{v}) \le x + \varepsilon$, which implies that $val_\mathrm{Adam}^{ \mathcal{G}}(v) \le x + \varepsilon$.
Since this is true for any $\varepsilon > 0$, this implies $val_\mathrm{Adam}^{ \mathcal{G}}(v) \le  val_\mathrm{Eve}^{ \mathcal{G}}(v)$.
As we have seen the converse inequality holds, implying the equality.

````

Note that this determinacy result does not imply the existence of optimal strategies.

## Computational problems for quantitative games

As for qualitative games, we identify different computational problems.
The first is solving the game.
```{admonition} Problem

For quantitative games, solving the game means solving the following decision problem:

**INPUT**: A quantitative game $\mathcal{G}$, a vertex $v$, and a threshold $x \in   \mathbb{Q} \cup  \left\{ \pm \infty \right\}$

**QUESTION**: Does Eve have a strategy ensuring $x$ from $v$?

```

A very close problem is the value problem.
```{admonition} Problem

For quantitative games, solving the value problem means solving the following decision problem:

**INPUT**: A quantitative game $\mathcal{G}$, a vertex $v$, and a threshold $x \in   \mathbb{Q} \cup  \left\{ \pm \infty \right\}$

**QUESTION**: Is it true that $val^{ \mathcal{G}}(v) \ge x$?

```

The two problems of solving a game and the value problem are not quite equivalent: 
they become equivalent if we assume the existence of optimal strategies.

The value problem is directly related to computing the value.
```{admonition} Problem

For quantitative games, computing the value means solving the following computational task:

**INPUT**: A quantitative game $\mathcal{G}$ and a vertex $v$

**COMPUTE**: $val^{ \mathcal{G}}(v)$

```

What computing the value means may become unclear if the value is not a rational number, making its representation complicated.
Especially in this case, it may be enough to approximate the value, which is indeed what the value problem gives us: 
by repeatingly applying an algorithm solving the value problem one can approximate the value to any given precision,
using a binary search.

````{prf:lemma} Binary search for computing the value
:label: 1-lem:binary_search_computing_value

If there exists an algorithm $A$ for solving the value problem of a class of games, 
then there exists an algorithm for approximating the value of games in this class within precision $\varepsilon$ 
using $\log(\frac{1}{\varepsilon})$ calls to the algorithm $A$.

````

The following problem is global, in the same way as computing the winning regions.
```{admonition} Problem

For quantitative games, computing the value function means solving the following computational task:

**INPUT**: A quantitative game $\mathcal{G}$

**COMPUTE**: The value function $val^{ \mathcal{G}} : V \to   \mathbb{R} \cup  \left\{ \pm \infty \right\}$

```

Finally, we are sometimes interested in constructing optimal strategies provided they exist.
```{admonition} Problem

For quantitative games, constructing an optimal strategy means solving the following computational task:

**INPUT**: A quantitative game $\mathcal{G}$ and a vertex $v$

**COMPUTE**: An optimal strategy from $v$

```
A close variant is to construct $\varepsilon$-optimal strategies, usually with $\varepsilon$ given as input.

## Prefix independent objectives

A qualitative objective $\Omega$ is:

*  closed under adding prefixes if for every finite sequence $\rho$ and for every infinite sequence $\rho'$,
if $\rho' \in \Omega$ then $\rho \rho' \in \Omega$;
*  closed under removing prefixes if for every finite sequence $\rho$ and for every infinite sequence $\rho'$,
if $\rho \rho' \in \Omega$ then $\rho' \in \Omega$;
*  prefix independent if it is closed under both adding and removing prefixes;
in other words whether a sequence satisfies $\Omega$ does not depend upon finite prefixes.

Let $\pi$ be a finite play consistent with $\sigma$, we write $\sigma_{\mid  \pi}$ for the strategy defined by

$$
\sigma_{\mid  \pi}( \pi') = \sigma( \pi  \pi').
$$

````{prf:observation} Winning for prefix independent objectives
:label: 1-fact:winning_prefix_independent_qualitative

Let $\Game$ be a qualitative game with objective $\Omega$ closed under removing prefixes,
$\sigma$ a winning strategy from $v$,
and $\pi$ a finite play consistent with $\sigma$ starting from $v$.
Then $\sigma_{\mid  \pi}$ is winning from $v' =  last( \pi)$.

````

````{admonition} Proof
:class: dropdown tip

Let $\pi'$ be an infinite play consistent with $\sigma_{\mid  \pi}$ from $v'$,
then $\pi  \pi'$ is an infinite play consistent with $\sigma$ starting from $v$, 
implying that it is winning, and since $\Omega$ is closed under removing prefixes
the play $\pi'$ is winning. Thus $\sigma_{\mid  \pi}$ is winning from $v'$.

````

````{prf:corollary} Reachable vertices of a winning strategy for prefix independent objectives
:label: 1-cor:reachable_vertices_prefix_independent

Let $\Game$ be a qualitative game with objective $\Omega$ closed under removing prefixes and $\sigma$ a winning strategy from $v$.
Then all vertices reachable from $v$ by a play consistent with $\sigma$ are winning.

````

In other words, when playing a winning strategy the play does not leave the winning region.

Similarly, a quantitative objective $\Phi$ is:

*  monotonic under adding prefixes if for every finite sequence $\rho$ and for every infinite sequence $\rho'$
we have $\Phi(\rho') \le \Phi(\rho \rho')$;
*  monotonic under removing prefixes if for every finite sequence $\rho$ and for every infinite sequence $\rho'$
we have $\Phi(\rho') \ge \Phi(\rho \rho')$;
*  prefix independent if it is monotonic under both adding and removing prefixes.

The fact above extends to quantitative objectives with the same proof.

````{prf:observation} Winning for prefix independent objectives, quantitative case
:label: 1-fact:winning_prefix_independent_quantitative

Let $\Game$ be a quantitative game with objective $\Phi$ monotonic under removing prefixes,
$\sigma$ a strategy ensuring $x$ from $v$, and $\pi$ a finite play consistent with $\sigma$ starting from $v$.
Then $\sigma_{\mid  \pi}$ ensures $x$ from $v' =  last( \pi)$.

````

````{admonition} Proof
:class: dropdown tip

Let $\pi'$ be an infinite play consistent with $\sigma_{\mid  \pi}$ from $v'$,
then $\pi  \pi'$ is an infinite play consistent with $\sigma$ starting from $v$, 
implying that $\Phi( \pi  \pi') \ge x$, and since $\Phi$ is monotonic under removing prefixes
this implies that $\Phi( \pi') \ge x$. Thus $\sigma_{\mid  \pi}$ ensures $x$ from $v'$.

````

````{prf:corollary} Comparison of values along a play
:label: 1-cor:comparison_values_along_play

Let $\Game$ be a quantitative game with objective $\Phi$ monotonic under removing prefixes and $\sigma$ an optimal strategy from $v$.
Then for all vertices $v'$ reachable from $v$ by a play consistent with $\sigma$ we have $val^{ \mathcal{G}}(v) \le   val^{ \mathcal{G}}(v')$.

````

In other words, when playing an optimal strategy the value is non-decreasing along the play.
