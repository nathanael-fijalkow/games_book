(1-sec:objectives)=
# Objectives

We present in this section the main objectives and their representations.
An objective may depend upon a set of parameters which are sometimes omitted when clear from the context.

Let us recall how we define classes of conditions: we first define an objective, for instance $\Safe \subseteq \set{\Win,\Lose}^\omega$.
For an arena and a colouring function $\col$ defined over this arena this induces the safety condition $\Safe[\col]$.
Given an arena and a condition $W$ over this arena we say that $W$ is **a** safety condition if 
there exists $\col$ such that $W = \Safe[\col]$.
The same terminology is used for all other objectives.

## Prefix dependent qualitative objectives: safety and reachability

The safety objective is the simplest qualitative objective:
the set of colours is $\set{\Win,\Lose}$, 
and safety requires that the colour $\Lose$ is never seen.
Formally:

$$

\Safe = \set{\rho \in \set{\Win,\Lose}^\omega : \forall i, \rho_i \neq \Lose}.

$$


In the example represented in  {ref}`Figure <1-fig:safety_game_example>`, 
a play is winning if if it never visits the vertex labelled $\Lose$.
Eve wins from the four vertices on the left and loses from all the others, which is represented by the two dotted areas.

```{figure} Fig/1-fig:safety_game_example.png
:name: 1-safety_game_example
:align: center
An example of a safety game. 
The vertex on the bottom right is labelled $\Lose$, all the others are implicitly labelled $\Win$;
the condition of Eve is to avoid the vertex labelled $\Lose$.
The two dotted areas represent the winning regions of each player.
```

The dual of the safety objective is the reachability objective: 
the set of colours is $\set{\Win,\Lose}$,
and reachability requires that the colour $\Win$ is seen at least once.
Formally:

$$

\Reach = \set{\rho \in \set{\Win,\Lose}^\omega : \exists i, \rho_i = \Win}.

$$


Safety and reachability conditions are dual:

$$

\Paths_\omega \setminus \Safe[\col] = \Reach[\overline{\col}] \quad ; \quad
\Paths_\omega \setminus \Reach[\col] = \Safe[\overline{\col}].

$$

where $\overline{\col}$ swaps $\Win$ and $\Lose$ in $\col$.
Consequently, if the condition for Eve is a safety condition, then the condition for Adam is a reachability condition, and conversely.

## Prefix independent qualitative objectives: B&uuml;chi, CoB&uuml;chi, and Parity

Safety and reachability objectives specify which colours occur or not, hence are prefix dependent.
We now introduce objectives specifying which colours occur infinitely many times, which will naturally be prefix independent.

The **B&uuml;chi** objective is over the set of colours $\set{1,2}$,
it requires that the colour $2$ is seen infinitely many times.
Formally:

$$

\Buchi = \set{\rho \in \set{1,2}^\omega : \forall j, \exists i \ge j, \rho_i = 2}.

$$

The dual of the B&uuml;chi objective is the **CoB{\"uchi**} objective: 
the set of colours is $\set{2,3}$, it requires that the colour $3$ is seen finitely many times.
Formally:

$$

\CoBuchi = \set{\rho \in \set{2,3}^\omega : \exists j, \forall i \ge j, \rho_i \neq 3}.

$$


B&uuml;chi and CoB&uuml;chi conditions are dual:

$$

\Paths_\omega \setminus \Buchi[\col] = \CoBuchi[\col + 1] \quad ; \quad
\Paths_\omega \setminus \CoBuchi[\col] = \Buchi[\col - 1].

$$

where $\col + 1$ adds one to $\col$ (since $\col$ maps vertices to $\set{1,2}$, $\col + 1$ maps vertices to $\set{2,3}$),
and similarly for $\col - 1$.
Consequently, if the condition for Eve is a B&uuml;chi condition, then the condition for Adam is a CoB&uuml;chi condition, and conversely.


We now define the parity objectives.
Let $[i,j]$ be an interval with $i,j \in \N$ used as a parameter defining the range of priorities.
The parity objective with parameters $i,j$ uses the set of colours $[i,j]$, which are referred to as priorities, and is defined by

$$

\Parity([i,j]) = \set{\rho \in [i,j]^\omega \left| \begin{array}{c} \text{ the largest priority appearing} \\ \text{infinitely many times in } \rho \text{ is even}\end{array} \right.}.

$$

We made the dependence in $[i,j]$ explicit by writing $\Parity([i,j])$, but we will most of the time write $\Parity$
and assume that the range of priorities is $[1,d]$, so $d$ is the number of priorities.
There are two possible conventions for defining parity objectives: considering the largest priority appearing infinitely many times, or the smallest one. They are strictly equivalent (through the transformation $x \mapsto 2d - x$) but depending on the situation one can be technically more convenient than the other.

We illustrate the definition on two examples.

$$

1\ 2\ 4\ 7\ 5\ 7\ 5\ 3\ 6\ 3\ 6\ 3\ 6\ 3\ 6\ \cdots \in \Parity,

$$

because the two priorities which appear infinitely often are $3$ and $6$, and the largest one is $6$, which is even.

$$

2\ 2\ 2\ 4\ 1\ 7\ 5\ 3\ 3\ 3\ 3\ 3\ 3\ 3\ 3\ \cdots \notin \Parity,

$$

because the only priority which appears infinitely often is $3$ and it is odd.

Two remarks are in order.
First, B&uuml;chi and CoB&uuml;chi objectives are parity objectives for the set of colours $[1,2]$ and $[2,3]$, respectively.
Second, the parity conditions are self dual: 

$$

\Paths_\omega \setminus \Parity([i,j])[\col] = \Parity([i+1,j+1])[\col + 1],

$$

where $\col + 1$ adds one to $\col$.
Hence if the condition for Eve is a parity condition, then the condition for Adam is also a parity condition.

{ref}`Figure <1-fig:parity_game_example>` presents an example of a parity game. 
The priority of a vertex is given by its label.

```{figure} Fig/1-fig:parity_game_example.png
:name: 1-parity_game_example
:align: center
An example of a parity game.
The two dotted areas represent the winning regions of each player.
```

## Conventions

Given an objective $\Omega \subseteq C^\omega$ we use a colouring function $\col : V \to C$ to induce the condition $\Omega[\col]$.
We extend this notation to sets of vertices and colours as follows.

*  A set of vertices $F \subseteq V$ induces the colouring function $\col_F$ defined by 
$\col_F(v) = \Win$ if $v \in F$ and $\col_F(v) = \Lose$ otherwise.
For $F \subseteq V$ we define $\Safe[F]$ as $\Safe[\col_F]$: it requires that no vertex from $F$ is ever visited.
*  A colour $c \in C$ induces the set of vertices $\col^{-1}(c)$ labelled by $c$.
The condition $\Safe[c]$ requires that the colour $c$ is never visited.

We apply this convention to safety, B&uuml;chi, and CoB&uuml;chi conditions: for $F \subseteq V$,

$$

\begin{array}{ccccc}
\Reach[F] & = & \Reach[\col_F] & = & \set{\play \in \Paths_\omega : \exists i, \Ing(\play_i) \in F}, \\
\Buchi[F] & = & \Buchi[\col_F] & = & \set{\play \in \Paths_\omega : \forall j, \exists i \ge j, \Ing(\play_i) \in F}, \\
\CoBuchi[F] & = & \CoBuchi[\col_F] & = & \set{\play \in \Paths_\omega : \exists j, \forall i \ge j, \Ing(\play_i) \notin F},
\end{array}

$$

 
similarly extended to colours.

## Representations for qualitative objectives

For reachability, safety, B&uuml;chi, and CoB&uuml;chi conditions we need one bit per vertex to specify whether it is winning or losing,
hence the machine word size $w = \log(m)$ implies that one machine word can store either an edge or a vertex together with this one bit of information.

The situation changes for parity conditions, where each vertex has a priority in $[1,d]$ hence requiring $\log(d)$ bits.
We then choose the machine word size $w = \log(m) + \log(d)$ in such a way that one machine word can store
either an edge or a vertex together with its priority.

## Quantitative objectives

In this introduction chapter we only define two quantitative objectives: mean payoff and discounted payoff.
More objectives will be defined and studied in {ref}`Chapter <4-chap:payoffs>`, and later in {ref}`Chapter <12-chap:multiobjective>`.

Mean payoff and discounted payoff use the set of colours $C = \Z$ the set of integers.
A colour is called a weight, interpreted as a payoff for Eve.

The mean payoff quantitative objective comes in two different flavours: using the supremum limit

$$

\MeanPayoff^+(\rho) = \limsup_k \frac{1}{k} \sum_{i = 0}^{k-1} \rho_i.

$$

or the infimum limit

$$

\MeanPayoff^-(\rho) = \liminf_k \frac{1}{k} \sum_{i = 0}^{k-1} \rho_i.

$$

As we shall see, in most settings the two objectives will be equivalent.
For this reason, we often use $\MeanPayoff$ to denote $\MeanPayoff^-$.

{ref}`Figure <1-fig:mp_game_example>` presents an example of a mean payoff game. 
The weight of a vertex is given by its label.
In this example the dotted areas represent the winning regions for the threshold is $0$, 
**i.e.** the induced qualitative objective $\MeanPayoff_{\ge 0} = \set{\rho \in C^\omega : \MeanPayoff(\rho) \ge 0}$.

```{figure} Fig/1-fig:mp_game_example.png
:name: 1-mp_game_example
:align: center
An example of a mean payoff game. 
The dotted areas represent the winning regions for the qualitative objective $\MeanPayoff_{\ge 0}$.
```


The discounted payoff quantitative objective is parameterised by a discount factor $\lambda \in (0,1)$.
It is defined by:

$$

\DiscountedPayoff_\lambda(\rho) = \lim_k \sum_{i = 0}^{k-1} \lambda^i \rho_i.

$$

Expanding the definition: $\DiscountedPayoff_\lambda(\rho) = \rho_0 + \lambda \rho_1 + \lambda^2 \rho_2 + \dots$.
Intuitively, the importance of the weights decrease over time: the weight $\rho_i$ is multiplied by $\lambda^i$ which goes to $0$ as $i$ goes to infinity.
The discount factor ensures that the limit exists for sequences with bounded weights,
which is holds for all plays since a (finite) game contains finitely many different weights.

### Representations for quantitative objectives

Let us consider a game $\Game$ with either a mean payoff or a discountedd payoff condition.
Let $W$ denote the largest weight appearing in $\Game$ in absolute value.

Choosing the machine word size $w = \log(m) + \log(W)$ implies that either an edge 
or a vertex together with its weight can be stored in one machine word and that we can perform arithmetic operations on weights.
For mean payoff games this means that the input size is $O(m)$.

For discounted payoff games we additionally need to represent the discount factor $\lambda$, 
which we assume is a rational number $\lambda = \frac{a}{b}$.
Since we want to perform arithmetic operations on $\lambda$ it is convenient to store it on one machine word,
hence the choice for the machine word size $w = \log(m) + \log(W) + \log(b)$.
