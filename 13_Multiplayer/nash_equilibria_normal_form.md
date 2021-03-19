(13-sec:nash_equilibria_normal_form)=
# Nash Equilibria for games in normal form

```{math}

\def\payoff{f}

\def\Act{A}
\def\Agt{\mathcal{P}}
\def\move{\textsf{move}}
\def\Out{\textsf{Out}}
\def\Dev{\textsf{Dev}}
\def\maxinf{\text{\rm maxinf}}
\def\pes{\textsf{pes}}
\def\opt{\textsf{opt}}
\def\proj{\textsf{proj}}
\def\devg{\textsf{DevGame}}
\def\Coalition{\mathcal{C}}

\renewcommand{\Game}{\game}

```

The normal form games we consider differ from the matrix games of Chapter {ref}`7-chap:concurrent`, in that each player has their own payoff.
So for instance, when player 1 chooses column Hawk, and player 2 chooses
row Dove, the payoff for player 1 is $\payoff_{P_1}(\text{Hawk}, \text{Dove}) = 4$.

Let us call a vector of strategies specifying a strategy for each player a **strategy profile**. In normal-form games, each cell of the table $\Delta$ corresponds to a strategy profile.

````{prf:definition} NEEDS TITLE AND LABEL 
  A **Nash equilibrium** is a **stable** strategy profile in which
  strategy is a best response against the other strategies.

  A **Nash equilibrium** is a **stable** strategy profile in which
  strategy is a best response against the other strategies.

````

Thus a Nash equilibrium is a stable situation in the sense that
no player has an incentive in changing their strategy.
Nash proved that when
players are allowed to randomise among all their strategies, there always
exists a Nash equilibrium.

````{prf:theorem} NEEDS LABEL Existence of Nash equilibria

In every normal-form game with a finite number of
players, each having a finite number of pure strategies, there exists a
randomised Nash equilibrium.

````

Note that not all games contain pure Nash equilibria.
For example, in the rock-paper-scissors game, the best response to rock
is paper, to paper is scissors, and to scissors is rock, so none of these
pure strategies can be an equilibrium.

For finding a pure Nash equilibrium in a normal-form game, there is a simple
polynomial time algorithm.
For each strategy profile, we look for each player whether they have a better
response than their current strategy.
If no player has a better response, the strategy profile is a Nash equilibrium,
otherwise we move to the next one, and if none satisfies the condition then there is no equilibrium.

````{prf:example} NEEDS LABEL Medium Access Control

Consider a medium access control
problem, where several users share access to a wireless channel. A
communication over the channel is successful if there are no collisions,
that is, if a single user is transmitting their message only. During each
slot, each user chooses either to transmit or to idle. Intuitively, the
number of packets transmitted without collision decreases with
the number of users emitting in the same slot. Furthermore each attempt
at transmitting has a cost. An example payoff for two players,
is represented in Table {prf:ref}`ex:medium-access`.

\begin{table}
  \caption{A game of medium access.}
  \label{ex:medium-access}
  \begin{center}
    \begin{tabular}[c]{|@{\hspace{1em}}l@{\hspace{1em}}|@{\hspace{1em}}c@{\hspace{1em}}c@{\hspace{1em}}|}
      \hline
      & Emit & Wait\\
      \hline
      Emit & -1, -1 & 2, 0\\
      Wait & 0 , 2 & 0, 0\\
      \hline
    \end{tabular}
  \end{center}
\end{table}

````

We encourage the reader to find the Nash equilibria of the above game.

The game described above corresponds to a single slot of this system. In
a practical scenario, there would be a succession of slots and the payoff would be
the sum of payoffs over all slots. Normal-form games are thus not
sufficient to represent games with repetitions and to study the
evolution of the behaviours as the game evolves.

One possibilty to model repetition is to use
**games in extensive form** which are games played on finite trees.
However such games only model a fixed number of repetitions unlike
infinite or arbitrary duration games as studied in this book. We thus
study, in the rest of this chapter, algorithms for games played on
graphs.

(13-subsec:definitions)=
## Definitions

````{prf:definition} NEEDS TITLE AND LABEL 
  A multiplayer **arena** \(\mathcal{A}\) with $k$ players is a tuple
  
  \(\langle V, \Act,\Delta,(c_P)_{P\in \Agt} \rangle \), where:

  *      \(V\) is a finite set of vertices;
  *      \(\Agt = \{1,2,\ldots,k\}\) is the set of players;
  *      \(\Act\) is a finite set of actions, a tuple \((a_P)_{P \in \Agt}\)
    containing one action \(a_P\) for each player $A$ is called a
    **move**, thus \(\Act^k\) is the set of possible moves;
  *      \(\Delta : V \times \Act^k \to V\) is the transition function which
    associates to a pair of vertices and moves the resulting state;
  *      \((c_P)_{P \in \Agt}\) is a tuple of colouring functions
    with $c_P : V \rightarrow C$ for each $P \in \Agt$.

  A multiplayer **arena** \(\mathcal{A}\) with $k$ players is a tuple
  
  \(\langle V, \Act,\Delta,(c_P)_{P\in \Agt} \rangle \), where:

  *      \(V\) is a finite set of vertices;
  *      \(\Agt = \{1,2,\ldots,k\}\) is the set of players;
  *      \(\Act\) is a finite set of actions, a tuple \((a_P)_{P \in \Agt}\)
    containing one action \(a_P\) for each player $A$ is called a
    **move**, thus \(\Act^k\) is the set of possible moves;
  *      \(\Delta : V \times \Act^k \to V\) is the transition function which
    associates to a pair of vertices and moves the resulting state;
  *      \((c_P)_{P \in \Agt}\) is a tuple of colouring functions
    with $c_P : V \rightarrow C$ for each $P \in \Agt$.

````

````{prf:example} NEEDS TITLE AND LABEL 
A simple three-player concurrent game is represented in {numref}`13-fig:example1`.
Vertices are $v_0$, $v_1$, $v_2$, $v_3$ and $v_4$.

Players are named $P_1$, $P_2$, $P_3$.
The set of actions is $\Act = \{ a , b\}$.
The transition relation is given by the edges in the graph, for instance
$\Delta(s_0, (a, b, a))$ is $v_1$. In our figures, $\ast$ represents
an arbitrary action.
The colouring function is represented below vertices as tuples ranging over players.
For instance, a vertex labelled by $(1,1,0)$ assigns
the first two players the colour $1$, and the third player the colour $0$,
In particular, $c_{P_1}(v_2) = 1$, and $c_{P_3}(v_2)= 0$.

A simple three-player concurrent game is represented in {numref}`13-fig:example1`.
Vertices are $v_0$, $v_1$, $v_2$, $v_3$ and $v_4$.

Players are named $P_1$, $P_2$, $P_3$.
The set of actions is $\Act = \{ a , b\}$.
The transition relation is given by the edges in the graph, for instance
$\Delta(s_0, (a, b, a))$ is $v_1$. In our figures, $\ast$ represents
an arbitrary action.
The colouring function is represented below vertices as tuples ranging over players.
For instance, a vertex labelled by $(1,1,0)$ assigns
the first two players the colour $1$, and the third player the colour $0$,
In particular, $c_{P_1}(v_2) = 1$, and $c_{P_3}(v_2)= 0$.

````

```{figure} ./../FigAndAlgos/13-fig:example1.png
:name: 13-fig:example1
:align: center
Example of a three-player concurrent arena. The symbol $\ast$ on edges can be replaced by either $a$ or $b$.
```

A **history** of the multiplayer arena

\({\mathcal A}\) is a finite sequence of states and moves ending with a
state, i.e. a word in \((V \cdot \Act^\Agt)^* \cdot V\). Note that unlike
for two player games we include actions in the history, because knowing
the source and target vertices does not mean you know which player chose
which actions.

For a history $\pi$, we write \(\pi_i\) the $i$-th vertex of $\pi$, starting from $0$, and

\(\move_i(\pi)\) its $i$-th move, thus
\(\pi = \pi_0 \cdot \move_0(\pi \cdot \pi_1 \cdots \move_{n-1}(\pi)\cdot \pi_n\), and
with this notation $\move_i(\pi)_P$ is the $i$-th action of player $P$ in $h$.
The length $|\pi|$ of such a history is $n + 1$. We write
$\textrm{last}(\pi)$ the last vertex of h, i.e. \(\pi_{|\pi|-1}\).
A play \(\rho\) is an
infinite sequence of vertices and moves, i.e. an element of
\((V \cdot \Act^{\Agt})^\omega\).

````{prf:definition} NEEDS LABEL Strategy and coalition

  A strategy is a function which associates an action to each history.
  We often write $\sigma_A$ for a strategy of player $P$.
  A coalition $\Coalition$ is a set of players in $\Agt$, and we write
  
  $-\Coalition$ for the remaining players, that is $-\Coalition = Agt \setminus \Coalition$.
  Let \(\Coalition\) be a coalition, a strategy \(\sigma_\Coalition\) for \(\Coalition\) is a function
  which associates a strategy \(\sigma_P\) to each player \(P\in \Coalition\).
  Given a strategy $\sigma_\Coalition$, when it is clear from the context, we simply
  write \(\sigma_P\) for \(\sigma_\Coalition(P)\).

````

````{prf:definition} NEEDS LABEL Outcomes

  A history \(\pi\) is compatible
  with the strategy \(\sigma_\Coalition\) for coalition $\Coalition$ if, for all \(k < |\pi| - 1\) and all
  \(P \in \Coalition\), \((\move_k(\pi))_P = \sigma_P(\pi{\le k})\), and
  \(\Delta(\pi_k, \move_k(\pi)) = \pi_{k+1}\). A play \(\rho\) is compatible with
  the strategy \(\sigma_\Coalition\) if all its prefixes are. We write
  
  \(  \textrm{Out}_{\mathcal{A}}(v_0, \sigma_\Coalition)\) for the set of plays in \(\mathcal{A}\) that
  are compatible with strategy \(\sigma_\Coalition\) and have initial vertex
  \(v_0\). Let \(  \textrm{Out}_{\mathcal{A}}(\sigma_\Coalition)\) denote the union
  of \(  \textrm{Out}_{\mathcal{A}}(v_0, \sigma_\Coalition)\) for all $v_0$,
  and \(  \textrm{Out}_{\mathcal{A}}(v_0)\) the union of all \(  \textrm{Out}_{\mathcal{A}}(v_0, \sigma_\Coalition)\).
  The subscript $\mathcal{A}$ can be omitted if it is clear from the context.
  These paths are called **outcomes** of \(\sigma_\Coalition\) from
  \(v_0\).

````

Note that
when the coalition \(\Coalition\) is composed of all the players
the outcome from a given state is unique.

````{prf:example} NEEDS TITLE AND LABEL 
  Consider in the example of {numref}`13-fig:example1`, the following
  strategies:
  
  *  $P_1$ always plays $a$, i.e. $\sigma_{P_1}(\pi) = a$ for all histories $\pi$;
  *  $P_2$ plays $a$ in $v_0$ if it is the first state and then always plays $b$, i.e. $\sigma_{P_2}(v_0) = a$ and $\sigma_{P_2}(\pi) = b$ for all $\pi \ne v_0$;
  *  $P_3$ always plays $b$, i.e. $\sigma_{P_3}(\pi) = b$.
  
  The outcome from $v_0$ in that case is
  
$$

      \textrm{Out}(v_0, \sigma_{\{P_1, P_2, P_3\}})   = &   v_0 \cdot (a, a, b) \cdot v_2 \cdot (a, b, b)
                                                \cdot v_4 \cdot (a, b, b) \cdot\\
                                              & \left(v_0 \cdot (a, b, b)
                                                \cdot v_1 \cdot (a, b, b)
                                                \cdot v_3 \cdot (a, b, b)\right)^\omega
  
$$

  Consider in the example of {numref}`13-fig:example1`, the following
  strategies:
  
  *  $P_1$ always plays $a$, i.e. $\sigma_{P_1}(\pi) = a$ for all histories $\pi$;
  *  $P_2$ plays $a$ in $v_0$ if it is the first state and then always plays $b$, i.e. $\sigma_{P_2}(v_0) = a$ and $\sigma_{P_2}(\pi) = b$ for all $\pi \ne v_0$;
  *  $P_3$ always plays $b$, i.e. $\sigma_{P_3}(\pi) = b$.
  
  The outcome from $v_0$ in that case is
  
$$

      \textrm{Out}(v_0, \sigma_{\{P_1, P_2, P_3\}})   = &   v_0 \cdot (a, a, b) \cdot v_2 \cdot (a, b, b)
                                                \cdot v_4 \cdot (a, b, b) \cdot\\
                                              & \left(v_0 \cdot (a, b, b)
                                                \cdot v_1 \cdot (a, b, b)
                                                \cdot v_3 \cdot (a, b, b)\right)^\omega
  
$$

````

````{prf:definition} NEEDS LABEL Multiplayer game

  A **payoff** function associates a real number to each outcome.
  We will be mostly be interested in solving games with qualitative
  objectives, that is payoffs that take values $0$ and $1$.

  A **multiplayer game** \((\mathcal{A}, (\payoff_P)_{P \in \Agt})\) is given by a multiplayer arena $\mathcal{A}$, an initial
  vertex $v_0$ and payoff function $\payoff_P$ for each player $P$.
  When $\payoff_P$ is qualitative we simply write $\Omega_P$
  for the corresponding objective.

````

(13-subsec:algorithm-for-finding-nash-equilibria)=
## The Nash equilibrium problem

In this section we will present an algorithm to compute
Nash equilibria in
multiplayer games.
The problem we are interested in is to decide the existence of a Nash
equilibrium in which the objectives of a given set of players are
satisfied.

```{admonition} Problem

**INPUT**: 
\parbox[t]{0.75\textwidth}{Multiplayer game $(\mathcal{A}, (\payoff_P)_{P \in \Agt})$, payoff
  bounds $(b_P)_{P\in\ \Agt}$, and initial vertex $v_0$}

**QUESTION**: 
  \parbox[t]{0.75\textwidth}{is there
a Nash equilibrium $\sigma_{\Agt}$ such that for all
$P \in \Agt, \payoff_P(  \textrm{Out}({v_0,\sigma_{\Agt}})) \ge b_P$?}

```
\todo{OS: I don't know how to fix this alignment issue}

The algorithm is based on a reduction to zero-sum two-players games,
which allows us to use algorithms presented in the previous chapters of
this book. More precisely, we present the **deviator game**, which is
a transformation of a concurrent multiplayer game into a turn-based
zero-sum game, such that there are strong links between equilibria in
the former and winning strategies in the latter. The proofs of
this section are independent of the type of objectives we consider.

(13-subsection:deviators)=
## Deviators

A central notion we use is that of **deviators**. These are the
players who have played different moves from those prescribed in a given
profile, thus causing a deviation from the expected outcome. Formally, a
deviator from move
\(a_{\Agt}\) to \(a'_{\Agt}\) is a player
\(D \in \Agt\) such that \(a_D \ne a'_D\) . We denote the set of
deviators by 

$$
        \Dev(a_{\Agt} , a'_{\Agt} ) = \{D \in \Agt \mid a_D \ne a'_D \}.
$$

 We extend the definition to pairs of histories and strategies by
taking the union of deviator sets of each step along the history.
Formally,

$$
\Dev(\pi, \sigma_{\Agt}) = \bigcup_{0\le i < |h|}  \Dev(\move_i(\pi), \sigma_{\Agt}(\pi_{\le i})).
$$

For an infinite play \(\rho\), we define

\(\Dev(\rho, \sigma_{\Agt} ) = \bigcup_{i \in \mathbb{N}} \Dev(\move_i(\rho), \sigma_{\Agt}(\rho_{\le i} ))\).
Intuitively, having chosen a strategy profile \(\sigma_{\Agt}\) and
observed a play \(\rho\), deviators represent the players that must have
changed their strategies from \(\sigma_{\Agt}\) in order to generate
\(\rho\).

````{prf:lemma} NEEDS TITLE 13-lem:deviator
:label: 13-lem:deviator

Given a play \(\rho\), strategy profile $\sigma_\Agt$, a coalition \(\Coalition\)
contains \(\Dev(\rho)\), if and only if, there exists a strategy
\(\sigma'_\Coalition\) such that \(  \textrm{Out}(\rho_1, \sigma_{-\Coalition}, \sigma'_\Coalition) = \rho\).

````

````{admonition} Proof
:class: dropdown tip

Assume that coalition \(\Coalition\) contains
\(\Dev(\rho, \sigma_{\Agt})\). We define the strategy \(\sigma_\Coalition\) to be
such that for all \(i\in \mathbb{N}\),
\(\sigma_\Coalition(\rho_{\le i} ) = (\move_i(\rho))_\Coalition\). By hypothesis, we have,
for all indices \(i\),
\(\Dev(\move_i(\rho), \sigma_{\Agt}(\rho_{\leq i})) \subseteq \Coalition\), so for
all players \(A\not\in \Coalition\),
\(\sigma_A(\rho_{\le i}) = (\move_i(\rho))_A\). Then
\(\Delta(\rho_i, \sigma'_\Coalition(\rho_{\le i}), \sigma_{-\Coalition}(\rho_{\le i})) = \rho_{i+1}\).
Hence \(\rho\) is the outcome of the profile
\((\sigma_{-\Coalition}, \sigma'_\Coalition)\).

For the other direction, let \(\sigma_{\Agt}\) be a strategy profile,
\(\sigma'_\Coalition\) a strategy for coalition \(\Coalition\), and
\(\rho \in Out_G(\rho_0 , \sigma_{-\Coalition}, \sigma'_\Coalition)\). We have for all
indices \(i\) that
\(\move_i(\rho) = (\sigma_{-\Coalition}(\rho_{\le i}), \sigma'_\Coalition(\rho_{\le i}))\).
Therefore for all players \(A \not\in \Coalition\),
\((\move_i(\rho))_A = \sigma_A(\rho_{\le i})\). Then
\(\Dev(\move_i(\rho), \sigma_{\Agt}(\rho_{\le i})) \subseteq \Coalition\). Hence
\(\Dev(\rho, \sigma_{\Agt}) \subseteq \Coalition\).

````

````{prf:example} NEEDS TITLE AND LABEL 
  In the example of {numref}`13-fig:example1`, we consider again the strategies,
  such that for all histories $\pi$, $\sigma_{P_1}(\pi) = a$,
  $\sigma_{P_2}(v_0) = a$ and if $\pi \ne v_0$, $\sigma_{P_2}(\pi) = b$,
  and $\sigma_{P_3}(\pi) = b$.
  Then $\Dev(v_0 \cdot (a, a, b) \cdot v_2 \cdot (a, a, b) \cdot v_1 \cdot
  (a, b, a) \cdot v_2, \sigma_{\Agt})$ is the union of:
  
  *  $\Dev(\sigma_{\Agt}(v_0), (a, a, b)) = \Dev((a, a, b), (a, a, b)) = \varnothing$
  *  $\Dev(\sigma_{\Agt}(v_0 \cdot (a, a, b) \cdot v_2), (a, a, b)) =
    \Dev( (a, b, b), (a, a, b)) = \{P_2\}$
  *  $\Dev(\sigma_{\Agt}(v_0 \cdot (a, a, b) \cdot v_2 \cdot (a, a, b) \cdot v_1), (a, b, a)) =
    \Dev( (a, b, b), (a, b, a)) = \{P_3\}$.
  
  We obtain
  $\Dev(v_0 \cdot (a, a, b) \cdot v_2 \cdot (a, a, b) \cdot v_1 \cdot
  (a, b, a) \cdot v_2, \sigma_{\Agt}) = \{ P_2, P_3\}$.
  This means that both $P_2$ and $P_3$ need to change their strategies
  from $\sigma_{\Agt}$ to obtain the given history.

  In the example of {numref}`13-fig:example1`, we consider again the strategies,
  such that for all histories $\pi$, $\sigma_{P_1}(\pi) = a$,
  $\sigma_{P_2}(v_0) = a$ and if $\pi \ne v_0$, $\sigma_{P_2}(\pi) = b$,
  and $\sigma_{P_3}(\pi) = b$.
  Then $\Dev(v_0 \cdot (a, a, b) \cdot v_2 \cdot (a, a, b) \cdot v_1 \cdot
  (a, b, a) \cdot v_2, \sigma_{\Agt})$ is the union of:
  
  *  $\Dev(\sigma_{\Agt}(v_0), (a, a, b)) = \Dev((a, a, b), (a, a, b)) = \varnothing$
  *  $\Dev(\sigma_{\Agt}(v_0 \cdot (a, a, b) \cdot v_2), (a, a, b)) =
    \Dev( (a, b, b), (a, a, b)) = \{P_2\}$
  *  $\Dev(\sigma_{\Agt}(v_0 \cdot (a, a, b) \cdot v_2 \cdot (a, a, b) \cdot v_1), (a, b, a)) =
    \Dev( (a, b, b), (a, b, a)) = \{P_3\}$.
  
  We obtain
  $\Dev(v_0 \cdot (a, a, b) \cdot v_2 \cdot (a, a, b) \cdot v_1 \cdot
  (a, b, a) \cdot v_2, \sigma_{\Agt}) = \{ P_2, P_3\}$.
  This means that both $P_2$ and $P_3$ need to change their strategies
  from $\sigma_{\Agt}$ to obtain the given history.

````

Note that Nash equilibria are defined only with respect to deviations by
single players, that is, we require all players to achieve worse or equal
payoffs than the prescribed profile when they single-handedly change
strategies. Thus, only the outcomes with singleton deviator sets
will be of interest for us in the next section where we present the algorithm.

(deviator-game)=
## Deviator Game
We now present an algorithm to reduce multiplayer games to two-player games
using the notion of deviators we just defined.

Given a **game**
\(\mathcal{G} = (\mathcal{A}, (\payoff_A)_{A \in \Agt})\),

we define the deviator game, denoted \(\devg(\mathcal{G})\).

Intuitively, in this game, Eve needs to play
according to an equilibrium, while Adam tries to find a profitable
deviation for any player. The vertices are \(V' = V \times 2^{\Agt}\),
where the second component, a subset of \(\Agt\), records the deviators
of the current history.

At each step, Eve chooses an action profile, and Adam chooses the move
that will apply. Adam can either respect Eve's choice, or pick a
different action profile in which case the deviators will be added to
the second component of the vertex. The game begins in
\((v_0 , \varnothing)\) and then proceeds as follows: from a vertex
\((v, D)\), Eve chooses an action profile \(a_{\Agt}\), and Adam chooses
a possibly different one \(a'_{\Agt}\). The next vertex is
\((\Delta(v, a'_{\Agt} ), D \cup \Dev(a_{\Agt} , a'_{\Agt} ))\).

````{prf:example} NEEDS TITLE AND LABEL 
  An example of a partial construction of the deviator game for the
  example of {numref}`13-fig:example1`, is given in {numref}`13-fig:ex-dev`.
  We cannot represent the full construction here, as there are 40 vertices.

  An example of a partial construction of the deviator game for the
  example of {numref}`13-fig:example1`, is given in {numref}`13-fig:ex-dev`.
  We cannot represent the full construction here, as there are 40 vertices.

````

```{figure} ./../FigAndAlgos/13-fig:ex-dev.png
:name: 13-fig:ex-dev
:align: center
Example a deviator game construction.
```

We define projections \(\proj_{V}\) and \(\proj_{\Dev}\) from \(V'\) to

\(V\) and from \(V'\) to \(2^{\Agt}\) respectively, as well as
\(\proj_{\Act}\) from \(Act^{\Agt} \times Act^{\Agt}\) to \(Act^{\Agt}\) which
maps to the second component of the product, that is, Adam's action.

For a history or play \(\rho\), define \(\pi_{  \textrm{Out}}(\rho)\) as the play
\(\rho'\) for which, \(\rho'_i = \proj_V(\rho_i)\) and
\(\move_i(\rho') = \proj_{\Act}(\move_i(\rho))\) for all $i$. This is thus the play
induced by Adam's actions.
Let us also denote $\Dev(\rho) = \proj_{\Dev}( \textrm{last}(\rho))$.

We can associate a strategy of Eve to each strategy profile
\(\sigma_{\Agt}\) such that she chooses the moves prescribed by
\(\sigma_{\Agt}\) at each history of \(\devg(\mathcal{G})\). Formally, we write
\(\kappa(\sigma_{\Agt})\) for the strategy defined by
\(\kappa(\sigma_{\Agt})(\pi) = \sigma_{\Agt}(\proj_{  \textrm{Out}}(\pi))\) for all histories $\pi$.

The following lemma states the correctness of the construction of the
deviator game \(\devg(\mathcal{G})\), in the sense that it records the set of
deviators in the strategy profile suggested by Adam with respect to the
strategy profile suggested by Eve.

````{prf:lemma} NEEDS TITLE 13-prop:correctness-deviator-game
:label: 13-prop:correctness-deviator-game

  Let $\mathcal{G}$ be a multiplayer game, $v$ a vertex, \(\sigma_{\Agt}\) a
  strategy profile, and \(\sigma_{\exists} = \kappa(\sigma_{\Agt})\) the
  associated strategy in the deviator game.

  1.      If \(\rho \in   \textrm{Out}_{\devg(\mathcal{G})}((v,\emptyset),\sigma_\exists)\), then
    \(\Dev(\proj_{  \textrm{Out}}(\rho), \sigma_{\Agt} ) = \Dev(\rho)\).
  2.      If \(\rho \in   \textrm{Out}_G(v)\) and for all index \(i\),
    \(\rho'_i = (\rho_i , \Dev(\rho_{\le i} , \sigma_{\Agt}))\) and
    \(\move_i(\rho') = (\sigma_{\Agt} (\rho_{\le i} ), \move_i(\rho))\), then
    \(\rho' \in   \textrm{Out}_{\devg(\mathcal{G})}((v,\emptyset), \sigma_\exists)\).

````

````{admonition} Proof
:class: dropdown tip

  We prove that for all $i$,
  \(\Dev(\proj_{  \textrm{Out}}(\rho_{\le i} , \sigma_{\Agt}) = \proj_{\Dev} (\rho_{\le i} )\),
which implies the property. The property holds for i = 0, since
initially both sets are empty. Assume now that it holds for \(i \ge 0\).
Then:

$$

  \Dev(\proj_{  \textrm{Out}}(\rho_{\le i+1}) , \sigma_{\Agt} ) = & \Dev(\proj_{  \textrm{Out}}(\rho_{\le i}), \sigma_{\Agt} ) \cup \Dev(\sigma_{\Agt} (\proj_{  \textrm{Out}}(\rho_{\le i})), \proj_{\Act} (\move_{i+1} (\rho))) \\
  & \text{(by definition of deviators)}\\
  =& \Dev (\rho_{\le i} ) \cup \Dev(\sigma_{\Agt} (\proj_{  \textrm{Out}} (\rho_{\le i}), \proj_{\Act} (\move_{i+1} (\rho))) \\
  & \text{(by induction hypothesis)} \\
  = & \Dev (\rho_{\le i} ) \cup \Dev(\sigma_\exists (\rho_{\le i} ), \proj_{\Act} (\move_{i+1}(\rho))) \\
  & \text{(by definition of \(\sigma_\exists\) )}\\
  = & \Dev (\rho_{\le i} ) \cup \Dev(\move_{i+1}(\rho)) \\
  & \text{(by assumption \(\rho \in   \textrm{Out}_{\devg(\mathcal{G})} ((v,\emptyset), \sigma_\exists)\))}\\
  = & \Dev(\rho_{\le i+1} ) \\
  & \text{(by construction of \(\devg(\mathcal{G})\))} \\

$$

Which concludes the induction.

We now prove the second part. The property is shown by induction. It
holds for \(v_0\). Assume it is true up to index \(i>0\), then

$$

\Delta'(\rho'_i , \sigma_\exists(\rho'_{\le i}), \move_i(\rho)) = &
\Delta'((\rho_i , \Dev(\rho_{\le i} , \sigma_{\Agt})), \sigma_{\exists} (\rho'_{\le i} ), \move_i(\rho))\\
&  \text{(by definition of \(\rho'\))} \\
= & \Delta(\rho_i , \move_i(\rho)), \Dev(\rho_{\le i}, \sigma_{\Agt}) \cup \Dev(\sigma_{\exists}(\rho'_{\le i}), \rho_{i+1} )) \\
&  \text{(by construction of \(\Delta'\) )}\\
= & (\rho_{i+1} , \Dev(\rho_{\le i}, \sigma_{\Agt} ) \cup \Dev(\sigma_{\exists}(\rho'_{\le i}), \rho_{i+1} )) \\
& \text{(since \(\rho\) is an outcome of the game)} \\
= & (\rho_{i+1} , \Dev(\rho_{\le i} , \sigma_{\Agt} ) \cup \Dev(\sigma_{\Agt} (\rho_{\le i}), \rho_{i+1} )) \\
& \text{(by construction of \(\sigma_\exists\))} \\
= & (\rho_{i+1} , \Dev(\rho_{\le i+1} , \sigma_{\Agt} ))\\
& \text{(by definition of deviators)} \\
= & \rho'_{i+1}. \\

$$

````

The objective of Eve in the deviator game is defined so that winning
strategies correspond to equilibria of the original game. First, as an
intermediary step, given coalition \(\Coalition\), player \(P\) and
bound \(b\), we will construct an objective stating that we can ensure
that the payoff of $P$ will not exceed $b$ even if players in $\Coalition$ change
their strategies.
Consider the following objective in \(\devg(\mathcal{G})\):

$$
  \Omega(\Coalition, P, b) = \{\rho \in   \textrm{Out}_{\devg(\mathcal{G})} \mid \Dev(\rho) \subseteq \Coalition \Rightarrow \payoff_P(\proj_{  \textrm{Out}}(\rho)) \le b\}.
$$

Intuitively, this says that if only players
in $\Coalition$ deviated from the strategy suggested by Eve, then the payoff
of $P$ is smaller than $b$.
We now show that a strategy ensuring bound \(b\) for the payoff of
$P$ against coalition \(\Coalition\) corresponds to a winning strategy for
\(\Omega(\Coalition, P, b)\) in the deviator game.

````{prf:lemma} NEEDS TITLE 13-lem:omegaCAg
:label: 13-lem:omegaCAg

  Let \(\Coalition \subseteq \Agt\) be a coalition,
  \(\sigma_{\Agt}\) be a strategy profile, \(b \in \mathbb{R}\) a bound,
  and \(P\) a player. For all strategies \(\sigma'_\Coalition\), vertex $v_0$,
  and coalition \Coalition, \(\payoff_P(  \textrm{Out}_{\devg(\mathcal{G})}(v_0, \sigma_{-\Coalition}, \sigma'_\Coalition)) \le b\) if, and
  only if, \(\kappa(\sigma_{\Agt})\) is winning in \(\devg(\mathcal{G})\) for objective
  \(\Omega(\Coalition, P, b)\).

````

````{admonition} Proof
:class: dropdown tip
 Let \(\rho\) be an outcome of
  \(\sigma_\exists=\kappa(\sigma_{\Agt}) \in \devg(\mathcal{G})\). By Lemma
  {prf:ref}`13-prop:correctness-deviator-game`, we have that
  \(\Dev(\rho) = \Dev(\proj_V(\rho),\sigma_{\Agt})\). By Lemma
  {prf:ref}`13-lem:deviator`, \(\proj_V(\rho)\) is the outcome of
  \((\sigma_{-\Dev(\rho)},\sigma'_{\Dev(\rho)})\) for some
  \(\sigma'_{\Dev(\rho)}\). If \(\Dev(\rho) \subseteq \Coalition\), then
  \(\payoff_P(\proj_V(\rho)) = \payoff_P(\sigma_{-\Coalition},\sigma_{\Coalition\setminus \Dev(\rho)}, \sigma'_{\Dev(\rho)}) = \payoff_P(\sigma_{-\Coalition},\sigma''_{\Coalition})\)
  where \(\sigma''_P = \sigma'_P\) if \(P \in \Dev(\rho)\) and \(\sigma_P\)
  otherwise. By hypothesis, this payoff is smaller than or equal to \(b\).
  This holds for
  all outcomes \(\rho\) of \(\sigma_\exists\), thus \(\sigma_\exists\) is
  a winning strategy for \(\Omega(\Coalition,P,b)\).

  For the other direction, assume \(\sigma_\exists = \kappa(\sigma_{\Agt})\)
  is a winning strategy in \(\devg(\mathcal{G})\) for \(\Omega(\Coalition,P,b)\). Let
  \(\sigma'_\Coalition\) be a strategy for \(\Coalition\) and \(\rho\) the outcome of
  \((\sigma'_{\Coalition},\sigma_{-{\Coalition}})\). By
  Lem. {prf:ref}`13-lem:deviator`,
  \(\Dev(\rho,\sigma_{\Agt}) \subseteq \Coalition\). By
  Lem. {prf:ref}`13-prop:correctness-deviator-game`,
  \(\rho'= (\rho_j, \Dev(\rho_{\le j},\sigma_{\Agt}))_{j\in \mathbb{N}}\) is
  an outcome of \(\sigma_\exists\). We have that
  \(\Dev(\rho') = \Dev(\rho,\sigma_{\Agt}) \subseteq \Coalition\). Since
  \(\sigma_\exists\) is winning, \(\rho\) is such that
  \(\payoff_P(\proj_V(\rho)) \le b\). Since
  \(\payoff_{P}(\proj_V(\rho')) = \payoff_{P}(\rho)\),
  this shows that for all strategies \(\sigma'_\Coalition\),
  \(\payoff_P(\sigma_{-\Coalition},\sigma'_\Coalition) \le b\).

````

Now, Eve can show that there is a Nash equilibrium in a given game
by proving that whenever there is a single deviator,
the deviating player does not gain more than without the deviation,
while she does not have to prove anything on plays involving several
deviators.

````{prf:theorem} NEEDS TITLE 13-thm:dev-nash
:label: 13-thm:dev-nash

  Let \(\mathcal{G} = (\mathcal{A}, (\payoff_P)_{P \in \Agt})\) be a game, \(\sigma_{\Agt}\) a strategy
  profile in \(\mathcal{G}\), vertex $v_0$, and \(F = (\payoff_P(  \textrm{Out}_{\mathcal{A}}(v_0,\sigma_{\Agt})))_{P\in \Agt}\)
  the payoff
  profile of \(\sigma_{\Agt}\) from $v_0$. The strategy profile \(\sigma_{\Agt}\) is a
  Nash equilibrium if, and only if, strategy \(\kappa(\sigma_{\Agt})\) is
  winning in \(\devg(\mathcal{A})\) for the objective \(N(F)\) defined by:

$$N(F) = \{\rho \mid |\Dev(\rho)| \ne 1\}
    \cup \bigcup_{P\in \Agt} \{\rho \mid \Dev(\rho) = \{P\}
    \land \payoff_P(\proj_{  \textrm{Out}}(\rho)) \le F_P\}.$$

````

````{admonition} Proof
:class: dropdown tip
 By {prf:ref}`13-lem:omegaCAg`, \(\sigma_{\Agt}\) is a Nash
  equilibrium if, and only if, for each player \(P\),

  \(\kappa(\sigma_{\Agt})\) is winning for
  
  \(\Omega(\{P\}, P, F_P)\).
  So it is enough to show that for each player \(P\),
  \(\kappa(\sigma_{\Agt})\) is winning for
  \(\Omega(\{P\},P, F_P)\) if,
  
  and only if, \(\kappa(\sigma_{\Agt})\) is winning for \(N(F)\).

  **Implication** Let \(\rho\) be an outcome of
  \(\kappa(\sigma_{\Agt})\).

*    If \(|\Dev(\rho)| \ne 1\), then \(\rho\) is in \(N(F)\) by
  definition.
*    If \(|\Dev(\rho)| = 1\), then for \(\{P\} = \Dev(\rho)\),
  \(\payoff_P(\proj_{  \textrm{Out}}(\rho)) \leq F_P\) because
  \(\kappa(\sigma_{\Agt})\) is winning for
  \(\Omega(\Dev(\rho), P, F_P)\). Therefore \(\rho\) is
  in \(N(F)\).

This holds for all outcomes \(\rho\) of \(\kappa(\sigma_{\Agt})\) and shows
that \(\kappa(\sigma_{\Agt})\) is winning for \(N(F)\).

**Reverse implication** 
Assume that
\(\kappa(\sigma_{\Agt})\) is winning for \(N(F)\). We now show that
\(\kappa(\sigma_{\Agt})\) is winning for
\(\Omega(\{P\},P, F_P)\) for each player \(P\). Let
\(\rho\) be an outcome of \(\kappa(\sigma_{\Agt})\), we have
\(\rho \in N(F)\). We show that \(\rho\) belongs to
\(\Omega(\{P\}, P, F_P)\):

*    If \(\Dev(\rho) = \varnothing\) then \(\rho =   \textrm{Out}(v_0, \sigma_{\Agt})\) and
  \(\payoff_P(\rho) = F_P\), so \(\rho\) is in
  \(\Omega(\{P\},P, F_P)\)
*    If \(\Dev(\rho) \not\subseteq \{ P \}\), then
  \(\rho \in \Omega(\Coalition,P,F_P)\) by definition.
*    Otherwise \(\Dev(\rho) = \{P\}\). Since \(\rho \in N(F)\),
  \(\payoff_P(\rho) \le F_P\). Hence
  \(\rho \in \Omega(\Coalition,P,F_P)\).

This holds for all outcomes \(\rho\) of \(\kappa(\sigma_{\Agt})\) and shows
it is winning for \(\Omega(\{P\},P,F_P)\) for each
player \(P\in \Agt\), which shows that \(\sigma_{\Agt}\) is a Nash
equilibrium.

````

(13-subsec:algorithm-for-parity-objectives)=
### Algorithm for Parity Objectives
We now focus on the case of Parity objectives.
Recall that
Each player $P$ has
a colouring function $c_P : V \rightarrow \mathbb{N}$, inducing the parity objective $\Omega_A$.

Thus the payoff $\payoff_Ps$ assigns 1 to paths belonging to $\Omega_A$ and 0
to the others.

We now give an algorithm for the Nash equilibrium problem with parity
objectives. Given a payoff for each player \((F_P)_{P\in \Agt} \),
we can deduce from the previous theorem an algorithm that
constructs a Nash equilibrium if there exists one. We construct the
deviator game and note that we can reduce the number of vertices as
follows: since  \(\Dev(\rho_{\le k})\) is nondecreasing,
we know that  \textrm{Eve} wins whenever this set has at least two elements.
In the construction, states with at least two deviators can be replaced by a
sink vertex that is winning for  \textrm{Eve}. This means that the constructed
game has at most \(n \times (|\Agt| + 1) + 1\) states.

The objective can be expressed as a Parity condition in the following
way:

*    for each vertex \(v' = (v, \{ P \})\), \(c'(v') = c_P(v) + 1\) if
  \(F_P = 0\) and \(2 \cdot \max_v c_P(v) \) otherwise;
*    for each vertex \(v' = (v, D)\) with \(|D| \ne 1\), \(c'(v') = 2 \cdot \max_v c_P(v)\)
  i.e. it is winning for Eve.

Notice that the colouring function $c'$ inverts the parity
in the case where there is a single deviator who is losing in the
prescribed strategy profile (that is, $F_P=0$). In fact,
when $F_P=1$, the player cannot obtain more since they are already winning
so the colour is set to $2\cdot \max_v c_P(v) $ which is winning for  \textrm{Eve}.

````{prf:lemma} NEEDS TITLE AND LABEL 
  We have \(\maxinf(c'(\rho_i)) \in 2 \mathbb{N}\) if, and
  only if, \(\rho\in N(F)\),
  where $N(F)$ is as defined in {prf:ref}`13-thm:dev-nash`.

  We have \(\maxinf(c'(\rho_i)) \in 2 \mathbb{N}\) if, and
  only if, \(\rho\in N(F)\),
  where $N(F)$ is as defined in {prf:ref}`13-thm:dev-nash`.

````

````{admonition} Proof
:class: dropdown tip
 For the implication, we will prove the contrapositive.
Let \(\rho\) be a play not in \(N(F)\), then since the deviators can only
increase along a play, we have that \(\Dev(\rho) = \{ P \}\) for some
player \(P\) and \(\payoff_P(\rho) > F_P\). This means
\(F_P = 0\) and \(\maxinf(c_P(\rho_i)) \in 2 \mathbb{N}\). By
definition of \(c'\) this implies that
\(\maxinf(c'(\rho_i)) \in 2 \mathbb{N} + 1\) which proves the
implication.

For the other implication, let \(\rho\) be such that
\(\maxinf(c'(\rho_i)) \in 2 \mathbb{N} + 1\). By definition of
\(c'\) this means \(\rho\) contains infinitely many states of the form
\((v, \{P\})\) with \(F_P = 0\). Since the deviators only increase
along the run, there is a player \(P\) such that \(\rho\) stays in the
component \(V \times \{P\}\) after some index \(k\). Then for \(i\geq k\),
\(c'(\rho_i) = c_P(\rho_i)+1\), hence
\(\maxinf(c'(\rho_i)) = \maxinf(c_P(\rho_i)) + 1\).
Therefore \(\maxinf(c_P(\rho_i)) \in 2 \mathbb{N}\), which means
\(\payoff_P(\rho) = 1 > F_P\). By definition of \(N(F)\),
\(\rho\not\in N(F)\).

````

Given that the size of the game is polynomial and that parity games can
be decided in quasipolynomial time (see {prf:ref}`3-corollary:quasipoly`), the preceeding lemma
implies the following theorem.

````{prf:theorem} NEEDS TITLE AND LABEL 
For parity games, there is a quasipolynomial algorithm to decide whether there is a Nash
equilibrium with a given payoff.

For parity games, there is a quasipolynomial algorithm to decide whether there is a Nash
equilibrium with a given payoff.

````

(13-subsection:extensions-of-nash-equilibria)=
## Extensions of Nash Equilibria

(13-subsection:subgame-perfect-equilibria)=
### Subgame Perfect Equilibria

Nash equilibria present the disadvantage that once a player has deviated,
the others will try to punish him, forgetting everything about their own
objectives.
If we were to observe the game after this point of
deviation, it would not look like the players are playing rationally and
in fact it would not correspond to a Nash equilibrium. The concept of
**subgame perfect equilibria** refines the concept of Nash
equilibrium by imposing that at each step of the history, the strategy
behaves like Nash equilibrium if we were to start the game now. Formally,
let us write \(\sigma_P \circ h\) the strategy which maps all histories
\(h'\) to \(\sigma_P(h \cdot h')\), that is the strategy that behave
like \(\sigma_P\) after \(h\). Then \((\sigma_P)_{P\in \Agt}\) is a
**subgame perfect equilibrium** if for all histories \(h\),
\((\sigma_P \circ h)_{P \in \Agt}\) is a Nash equilibrium.

Imposing such a strong restriction is justified by the fact that subgame
perfect Nash equilibria exist for a large class of games. In particular
subgame perfect equilibria always exist in turn-based games with
reachability objectives.

````{prf:example} NEEDS TITLE AND LABEL 
  Consider the example of {numref}`13-fig:ex-subgame`.
  There is a Nash equilibria whose outcome goes through states
  $v_0 \rightarrow v_1 \rightarrow \Omega_1$.
  In this equilibrium, Player $1$ should play $b$ in $v_2$,
  so that the best response of Player $2$ is to play $a$ at $v_0$.
  Intuitively, player $1$ is threatening player $2$, to make them
  both lose from $v_2$, but this threat is not credible,
  and the profile is not a subgame perfect equilibrium.
  In fact, once $v_2$ is reached it is better for Player $1$
  to play $a$ so it is unlikely that the player will execute the said threat.
  The only subgame perfect equilibrium of this game ends in 
  the vertex satisfying both
  $\Omega_1$ and $\Omega_2$.

  Consider the example of {numref}`13-fig:ex-subgame`.
  There is a Nash equilibria whose outcome goes through states
  $v_0 \rightarrow v_1 \rightarrow \Omega_1$.
  In this equilibrium, Player $1$ should play $b$ in $v_2$,
  so that the best response of Player $2$ is to play $a$ at $v_0$.
  Intuitively, player $1$ is threatening player $2$, to make them
  both lose from $v_2$, but this threat is not credible,
  and the profile is not a subgame perfect equilibrium.
  In fact, once $v_2$ is reached it is better for Player $1$
  to play $a$ so it is unlikely that the player will execute the said threat.
  The only subgame perfect equilibrium of this game ends in 
  the vertex satisfying both
  $\Omega_1$ and $\Omega_2$.

````

```{figure} ./../FigAndAlgos/13-fig:ex-subgame.png
:name: 13-fig:ex-subgame
:align: center
Two-player game with reachability objectives. The goal of
  player 1 is to reach a state labeled with $\Omega_1$ and that of
  player 2 is to reach a state labeled with $\Omega_2$. 
```

(13-subsec:robust-equilibria)=
### Robust equilibria
The notion of robust equilibria refines Nash equilibria in two ways:

*    a robust equilibrium is **resilient**, i.e. when a small coalition
  change its strategy, none of the players of the coalition improves their
  payoff;
*    it is **immune**, i.e. when a small coalition changes its strategy,
  it does not decrease the payoffs of the non-deviating players.

The size of small coalitions is determined by parameter \(k\) for
resilience and \(t\) for immunity. When a strategy is both
\(k\)-resilient and \(t\)-immune, it is called a \((k,t)\)-robust
equilibrium.

The motivation behind this concept is to address these two weaknesses of
Nash equilibra:

*    There is no guarantee on payoffs when two (or more) players deviate together.
  Such a situation can occur in networks if the same person controls several devices
  (a laptop and a phone for instance) and can then coordinate their
  behaviours. In this case, the devices would be considered as different
  players and Nash equilibria can offer no guarantee.
*    When a deviation occurs, the strategies of the equilibrium can punish
  the deviating user without any regard for the payoffs of the others. This
  can result in a situation where, because of a faulty device, nobody
  can use the protocol anymore.

By comparison, finding resilient equilibria with \(k>1\), 
ensures that clients have no interest in forming coalitions (up
to size \(k\)), and finding immune equilibria with \(t>0\)
ensures that other clients will not suffer from some players (up to
\(t\)) behaving differently from what was expected.

The deviator construction can be reused for finding such equilibria. We
only need to adapt the objectives. Given a game \(G=(\mathcal{A}, (\payoff_P)_{P \in \Agt})\), a
strategy profile \(\sigma_{\Agt}\), and parameters \(k\), \(t\), we have

*    The strategy profile \(\sigma_{\Agt}\) is \(k\)-resilient if, and only
  if, strategy \(\kappa(\sigma_{\Agt})\) is winning in \(\devg(\mathcal{A})\) for the
  **resilience objective** \(\mathcal{R}(k,F)\) where
  \(F = (\payoff_P(  \textrm{Out}_{\mathcal{A}}(v_0, \sigma_{\Agt})))_{P \in \Agt}\) is the payoff profile of
  \(\sigma_{\Agt}\) and \(\mathcal{R}(k,F)\) is defined by:

$$
    \begin{array}{ll}
      \mathcal{R}(k,F) = & \{ \rho \in   \textrm{Out}_{\devg(\mathcal{A})}\mid   |\Dev(\rho)| > k \} \\
                          &\cup
                            \{ \rho  \in   \textrm{Out}_{\devg(\mathcal{A})} \mid   |\Dev(\rho)| = k \land \forall P \in \Dev(\rho).\ \payoff_{P}(\proj_{  \textrm{Out}}(\rho)) \le F_P\} \\
                          & \cup \{ \rho  \in   \textrm{Out}_{\devg(\mathcal{A})}\mid   |\Dev(\rho)| < k \land \forall P \in \Agt.\ \payoff_{P}(\proj_{  \textrm{Out}}(\rho)) \le F_P\}.
    \end{array}
  $$

*    The strategy profile \(\sigma_{\Agt}\) is \(t\)-immune if, and only if,
  strategy \(\kappa(\sigma_{\Agt})\) is winning for the **immunity
  objective** \(\mathcal{I}(t,F)\) where
  \(F = (\payoff(  \textrm{Out}_{\mathcal{A}}(v_0, \sigma_{\Agt})))_{P \in \Agt}\) is the payoff profile of
  \(\sigma_{\Agt}\) and \(\mathcal{I}(t,F)\) is defined by:

$$
    \begin{array}{ll}
    \mathcal{I}(t,F) = & \{ \rho  \in   \textrm{Out}_{\devg(\mathcal{A})} \mid |\Dev(\rho)| > t \}  \\
      & \cup \{ \rho  \in   \textrm{Out}_{\devg(\mathcal{A})} \mid   \forall P \in \Agt \setminus \Dev(\rho).\  F_P \le \payoff_{P}(\proj_{  \textrm{Out}}(\rho)) \}.
    \end{array}
  $$

*    The strategy profile \(\sigma_{\Agt}\) is a \((k,t)\)-robust profile in
  \(G\) if, and only if, \(\kappa(\sigma_{\Agt})\) is winning for the
  **robustness objective**

$$
        \mathcal{R}(k,t,F)= \mathcal{R}(k,F) \cap \mathcal{I}(t,F),
        $$

 where
        \(F = (\payoff_P(  \textrm{Out}_{\mathcal{A}}(v_0, \sigma_{\Agt})))_{P \in \Agt}\) is the payoff profile of
        \(\sigma_{\Agt}\).

We omit the proof and encourage the reader to do it by themselves.

(13-subsec:extension-to-games-with-hidden-actions)=
### Extension to games with hidden actions
In most practical cases, players only have a partial view of the
state of the system; so they may not be able, for instance, to
detect a deviating player immediately.
Studying equilibria in general imperfect information as in {prf:ref}`chap:signal` 
would be well adapted in such situations.
Unfortunately, these games are too powerful in general since
the existence of Nash equilibria is undecidable in this case.

Nevertheless, the problem is decidable for a restricted form of imperfect
information where the players observe the visited states
but do not see the played actions; thus the actions are **hidden**.

We will thus consider strategies defined as functions from \(V^*\) to \(Act\),
which represents the fact that players' decision can only depend on observed
sequence of states but not on other players' actions.

In this case, deviators cannot be defined as obviously as before, as it may
not always be possible to identify one unique deviator responsible for a
deviation. The construction will thus maintain a set of **suspects**, those players that might have been
responsible for the observed deviation.
Formally, suspects for an edge \((v, v')\) with respect to a move
\((a_P)_{P\in \Agt}\) are players \(P\) such that there is \(a'_P\) and
\(\Delta(a'_P, a_{-P}) = (v, v')\). Rather than computing the
union of deviators along a history, we now consider the intersection of
suspects. That is, if at vertex $v$, the suspect set is $S$, and the strategy profile is $\sigma_\Agt$,
and if the next vertex is $v'$, then
the suspect set becomes $S \cap \{ P \in \Agt \mid \exists a'_P, \Delta(a'_P, a_{-P}) = (v, v')\}$.

The **suspect game** can be defined just like the deviator game by replacing the deviators component
by the suspects component.
The objective for Eve is that no suspect player improves their payoff. In fact, in
case of deviation, we know that the deviator belongs to the set of suspects although
we cannot know which one has deviated for sure so Eve must ensure this for all suspects.

````{prf:example} NEEDS TITLE AND LABEL 
  Consider the example of {numref}`13-fig:hidden`.
  If actions were visible there would be an equilibrium ending in the
  state labeled with $\Omega_3$: player 3 simply has to punish the player
  who would deviate from this path.
  But if we now consider hidden actions, in case of a deviation, player 3
  would observe that the play went arrives in $v_1$ instead of $v_2$
  and both Player 1 and Player 2 are suspects.
  Since Player 3 cannot punish both players at the same time, there is no
  Nash equilibrium ending satisfying $\Omega_3$.

  Consider the example of {numref}`13-fig:hidden`.
  If actions were visible there would be an equilibrium ending in the
  state labeled with $\Omega_3$: player 3 simply has to punish the player
  who would deviate from this path.
  But if we now consider hidden actions, in case of a deviation, player 3
  would observe that the play went arrives in $v_1$ instead of $v_2$
  and both Player 1 and Player 2 are suspects.
  Since Player 3 cannot punish both players at the same time, there is no
  Nash equilibrium ending satisfying $\Omega_3$.

````

```{figure} ./../FigAndAlgos/13-fig:hidden.png
:name: 13-fig:hidden
:align: center
Three-player game with hidden actions. The goal of
  player $i$ is to reach a state labeled with $\Omega_i$.
```
