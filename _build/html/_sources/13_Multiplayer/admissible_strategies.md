(13-sec:admissible_strategies)=
# Admissible strategies

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

Nash equilibria and their variants seen so far describe stable situations
from which players have no incentive to deviate. This however is of limited use
in some situations. First, the stability relies on the fact that all players are informed
of the strategy profile to be played; that is, some central authority needs to publicly
announce the strategies for all players. Second, each equilibrium describes a single possible
situation. If there are several equilibria, it is not clear which one is to be chosen.

Rather than concentrating on particular equilibria, game theorists have studied
reasonings players may follow in order to exclude some strategies that are necessarily worse than others.
These worse strategies are called **dominated**.
By formalizing dominated and non-dominated strategies for a given player, one can then predict the behavior of rational players
since such a player would never use a dominated strategy but rather always pick the best one available.

In this section, we will formalize dominated strategies and show how these can be computed in games.
We then briefly show that this reasoning can be repeated, and present the iterated elimination of dominated strategies.

(definition-1)=
## Definition
The notion of **dominance** is used to compare strategies 
with respect to payoffs they yield against the rest of the players' strategies.
Consider the example of {prf:ref}`13-tab:normal-adm`.
Given a strategy of the second player, playing $B$ is always at least as good
as playing $A$ for the first player.
In fact, again $C$, $B$ yields a payoff of $4$ which is better than $3$, the payoff of $A$;
and against $D$, both yield $0$.
The strategy $B$ is said to dominate $A$. Intuitively, 
$B$ is either better or as good as $A$ **in all situations**, so 
playing $B$ is the rational choice for Player $1$.

Furthermore, by this analysis, Player $2$ knows that Player $1$ will player $B$.
Given this information, the best response of Player $1$ is to play $C$.
By **iterated elimination**, we established that

$(B, C)$ should be the only strategy profile to be played by players following this reasoning.

\begin{table}
  \caption{A normal form game solvable by iterated elimination.}
  \label{13-tab:normal-adm}
  \begin{center}
    \begin{tabular}[c]{|@{\hspace{1em}}l@{\hspace{1em}}|@{\hspace{1em}}c@{\hspace{1em}}c@{\hspace{1em}}|}
      \hline
      & A & B \\
      \hline
      C & 3, 3 & 4, 1\\
      D & 0 , 4 & 0, 0\\
      \hline
    \end{tabular}
  \end{center}
\end{table}

Let us formalize this notion.

````{prf:definition} NEEDS LABEL Dominance

Let \(S \subseteq \mathcal{S}^{\Agt}\) be a set of the form
\(S = S_1 \times S_2 \times \cdots \times S_n\) which we will call a
rectangular set. Let \(\sigma,\sigma' \in S_i\). Strategy \(\sigma\)
**very weakly dominates** strategy \(\sigma'\) with respect to \(S\),
written \(\sigma_i \ge_S \sigma'_i\), if from all vertices \(v_0\):

$$
  \forall \sigma_{-i} \in S_{-i}, \payoff_i(  Out(v_0,\sigma'_i,\sigma_{-i}))
  \ge
  \payoff_i(  Out(v_0, \sigma_i, \sigma_{-i})).
$$

Strategy \(\sigma_i\) **weakly dominates** strategy \(\sigma'_i\)
in \(S\), written \(\sigma >_S \sigma'\), if
\(\sigma \ge_S \sigma'\) and \(\neg(\sigma' \le_S \sigma)\).

A strategy that is
not weakly dominated in \(S\) is **admissible** in \(S\). The
subscripts on \(\ge_S\) and \(>_S\) are omitted when the sets of
strategies are clear from the context.

````

Algorithms rely on the notion of **optimistic** and
**pessimistic value** of a history. The pessimistic value is the
maximum payoff that a player can ensure in the worst case within the strategy set $S$.
The optimistic value is
the best the player can achieve with the help of other players, given the strategy set $S$.

````{prf:definition} NEEDS LABEL Values
 The **pessimistic value** of a strategy
\(\sigma_i\) for a history \(h\) with respect to a rectangular set of
strategies \(S\), is

*    \(\pes_i(S,h,\sigma_i) = \inf_{\sigma_{-i} \in S_{-i}} \payoff_{i}(h \cdot   Out( last(h), \sigma_i,\sigma_{-i})).\)

The **pessimistic value of a history** \(h\) for \(A_i\) with respect
to a rectangular set of strategies \(S\) is given by:

*    \(\pes_i(S,h) = \sup_{\sigma_i \in S_i} \pes_i(S,s,\sigma_i).\)

The **optimistic value** of a strategy \(\sigma_i\) for a history
\(h\) with respect to a rectangular set of strategies \(S\) is given by:

*    \(\opt_i(S,h,\sigma_i) = \sup_{\sigma_{-i} \in S_{-i}} \payoff_i (h_{\le |h|-2} \cdot   Out( last(h), \sigma_i,\sigma_{-i})).\)

The **optimistic value** of a history \(h\) for \(A_{i}\) with
respect to a rectangular set of strategies \(S\) is given by:

*    \(\opt_i(S,h) = \sup_{\sigma_i \in S_i} \payoff_{i}(\opt_i(S,h,\sigma_i))\)

````

We will first consider the case where $S$ is the set of all strategies,
and omit $S$ in the above notations.

(simple-safety-games)=
## Simple Safety games

\begin{figure}
\begin{center}  
\begin{tikzpicture}
\draw (0,0) node[draw, inner sep=2pt, circle] (I) {$v_0$};
\draw (I.-90) node[below] {};
\draw (4,1) node[draw, circle, inner sep=2pt] (C1) {$v_1$};
\draw (C1.-100) node[below] {};
\draw (4,-1) node[draw, circle, inner sep=2pt, circle] (C2) {$v_2$};

\draw (8, 1) node[draw, circle, inner sep=2pt] (S1) {$v_3$};
\draw (S1.-90) node[below] {$-1, -1, 0$};
\draw (8,-1) node[draw, circle, inner sep=2pt] (S2) {$v_4$};
\draw (S2.-90) node[below] {$-1, 0, -1$};
\draw[-latex'] (-1, 0) -- (I);
\draw[-latex'] (I) -- node[above]{$(*,a,*)$} (C1);
\draw[-latex'] (I) -- node[below]{$(*,b,*)$} (C2);
\draw[-latex'] (C1) --node[left]{$(a,*,*)$} (C2);
\draw[-latex'] (C1) -- node[above]{$(b,*,*)$} (S1);
\draw[-latex'] (C2) -- node[above]{$(*,*,a)$} (S2);
\draw[-latex', rounded corners] (C2) -- +(1,1) -- node[right]{$(*,*,b)$}(C1);
\end{tikzpicture}
\caption{Example of a three-player turn-based simple safety game.

Numbers below states describe the safety objective, for instance $-1, -1, 0$ is losing for player 1 and 2.
}
\label{13-fig:simple-safety}
\end{center}
\end{figure}

Simple safety games, are safety games in which there are no transitions
from losing vertices to non-losing ones. Restricting to this particular
class of game makes the problem simpler because the objective becomes
prefix independent.
Any safety game can be converted to an equivalent simple safety game
by encoding in the states which players have visited so far a losing
state. Note that this translation can be exponential in the number of
players.

For simple safety games, the pessimistic and optimistic values do not depend
on the full history but only on the last state: for all histories
\(\pes_i(h) = \pes_i( last(h))\) and \(\opt_i(h) = \opt_i( last(h))\).

Note that in safety games (and any qualitative games) values can be only
1 (for winning) and 0 (for losing) and since the pessimistic value is
always less than the optimistic one, the pair \((\pes_i, \opt_i)\) can
only take three values: \((0, 0)\), \((0, 1)\) and \((1, 1)\).

Intuitively, players should avoid decreasing this pair of values if they can.
In fact, the characterization of admissible strategies we give below will be based on this
simple observation.

````{prf:example} NEEDS TITLE AND LABEL 
  An example of a simple safety game is given in {numref}`13-fig:simple-safety`.
  In this game, player 1 controls $v_1$ where its optimistic
  value is $0$, as it is possible that the outcome will never reach
  $v_3$ or $v_4$.
  However $v_3$ has optimistic value $-1$ for player 1, as it is a losing
  state for player 1.
  Going from $v_1$ to $v_3$ is a bad choice for player 1, and
  it is indeed dominated by the strategy that would always choose to go
  to $v_2$.
  In state $v_3$, player 3 has pessimistic value $0$ since it can ensure not
  visiting $v_4$.
  The winning strategy for player 3 which is to always go to $v_1$ is also
  the only non-dominated strategy.
  For player 2, from state $v_0$, both choices lead to a state with values
  $(-1, 0)$ so no choice is particularly better and both strategies are
  non-dominated.

  An example of a simple safety game is given in {numref}`13-fig:simple-safety`.
  In this game, player 1 controls $v_1$ where its optimistic
  value is $0$, as it is possible that the outcome will never reach
  $v_3$ or $v_4$.
  However $v_3$ has optimistic value $-1$ for player 1, as it is a losing
  state for player 1.
  Going from $v_1$ to $v_3$ is a bad choice for player 1, and
  it is indeed dominated by the strategy that would always choose to go
  to $v_2$.
  In state $v_3$, player 3 has pessimistic value $0$ since it can ensure not
  visiting $v_4$.
  The winning strategy for player 3 which is to always go to $v_1$ is also
  the only non-dominated strategy.
  For player 2, from state $v_0$, both choices lead to a state with values
  $(-1, 0)$ so no choice is particularly better and both strategies are
  non-dominated.

````

````{prf:definition} NEEDS TITLE AND LABEL  Let \(D_i\) be the set of edges
\((v,v') \in E\) such that \(v \in V_i\) 

\(\pes_i(v) > \pes_i(v')\) or \(\opt_i(v) > \opt_i(v')\). These
are called **dominated edges**.
 
 Let \(D_i\) be the set of edges
\((v,v') \in E\) such that \(v \in V_i\) 

\(\pes_i(v) > \pes_i(v')\) or \(\opt_i(v) > \opt_i(v')\). These
are called **dominated edges**.

````

````{prf:theorem} Characterisation of Admissible Strategies
:label: 13-thm:adm

Admissible
strategies for player \(A_i\) are the strategies that never take actions
in \(D_i\).

````

````{admonition} Proof
:class: dropdown tip
 We show that if \(A_i\) plays an admissible strategy
\(\sigma_i\) then the value cannot decrease on a transition controled by
\(A_i\). Let \(\rho \in   Out(\sigma_i,\sigma_{-i})\), and \(k\) an index
such that \(\rho_k \in V_i\). Let \((v, v') = \sigma_i(\rho_{\le k})\):

*    If \(\pes_i(\rho_k)=1\), then \(\sigma_i\) has to be winning against
  all strategies \(\sigma_{-i}\) of \(A_{-i}\), otherwise it would be
  weakly dominated by such a strategy. Since there is no such strategy
  from a state with value \(\pes_i \leq 0\), we must have \(\pes_i(v')=1\).
*    If \(\opt_i(\rho_k) = 1\), then, by definition, there is a profile \(\sigma'\) such that
  \(\rho = \payoff(  Out(v, \sigma')) = 1\).
  Assume that $\opt_i(v')=0$. Then $\sigma_i$ is dominated by the strategy
  $\sigma_i''$ obtained from $\sigma_i$ by making it switch to $\sigma'$ at $v$.
  In fact, $\sigma_i$ is losing against all strategies of $-i$, while $\sigma_i''$
  is winning at least against $\sigma_{-i}'$.

*    If $\pes_i(v)=0$ or $\opt_i(s) = 0$, then the value cannot decrease further.

In the other direction, let \(\sigma_i,\sigma_i'\) be two strategies of
player \(A_i\) and assume \(\sigma_i' >_S \sigma_i\). We will prove
\(\sigma_i\) takes a transition in \(D_i\) at some point.

Let us fix some objects before developing the proof. There is a vertex
\(v\) and strategy profile \(\sigma_{-i} \in S_{-i}\) such that
\(\payoff(  Out(v,\sigma_i',\sigma_{-i}))=1 \wedge \payoff(  Out(v,\sigma_i,\sigma_{-i})=0\).
Let \(\rho =   Out(v,\sigma_i,\sigma_{-i})\) and
\(\rho' =   Out(v,\sigma_i',\sigma_{-i})\). Consider the first position
where these runs differ: write \(\rho = w \cdot s' \cdot s_2 \cdot w'\)
and \(\rho' = w \cdot s' \cdot s_1 \cdot w''\).

The following are simple facts that can be seen easily:

*    \(s' \in V_i\), because the strategy of the other players
  are identical in the two runs.
*    \(\opt_i(s_1) = 1\) because
  \(\payoff(  Out(v,\sigma_i',\sigma_{-i}))=1\)
*    \(\pes_i(s_2) = 0\) because
  \(\payoff(  Out(v,\sigma_i,\sigma_{-i}))=0\)

If \(\opt_i(s_2) = 0\) or \(\pes_i(s_1) = 1\) then
\(s' \rightarrow s_2 \in D_i\) so \(\sigma_i\) takes a transition of
\(D_i\). The remaining case to complete the proof is \(\opt_i(s_2) = 1\)
and \(\pes_i(s_1) = 0\).
Let us assume that $\sigma_i$ does not take any edges from $D_i$.
We will show that there is
a strategy for $-i$ against which $\sigma_i$ wins and $\sigma_i'$ loses,
which contradicts the hypothesis that $\sigma_i'$ weakly dominates $\sigma_i$.

We first construct a profile \(\sigma_{-i}^2 \in S_{-i}\) such that
\(\payoff(  Out(s_2,\sigma_i,\sigma_{-i}^2))=1\).

Strategy \(\sigma_{-i}^2\in S_{-i}\) never decreases
the optimistic value from \(1\) to \(0\) since the optimistic value is nonincreasing.
By assumption, \(\sigma_i\)
itself does not decrease the value of \(A_i\) because it does not take
transitions of \(D_i\). So the outcome of \((\sigma_i,\sigma_{-i}^2)\)
never reaches a state of optimistic value \(0\). Hence it never reaches
a state in \(Bad_i\) and therefore it is winning for \(A_i\).

Let us now consider a profile \(\sigma_{-i}^1 \in S_{-i}\) such that
\(\payoff(\sigma_i',\sigma_{-i}^1)=0\) from \(s_1\). Such a strategy exists
because
\(\pes_i(s_1) = 0\), so $\sigma_i'$ is not a winning strategy.
Then there exists a
strategy profile \(\sigma_{-i}^1\) such that \(\sigma_i'\) loses from
\(s_1\).

Now consider strategy profile \(\sigma_{-i}'\) that plays like
\(\sigma_{-i}\) if the play does not start with \(w\);
and otherwise switches to
\(\sigma_{-i}^1\) at history \(ws_1\) and to \(\sigma_{-i}^2\) at history \(ws_2\).
Formally, given a history \(h\), \(\sigma_{-i}'(h) =\)

*    \(\sigma_{-i}^1( h')\) if \(w \cdot s_1\) is a prefix of \(h\) and
  \(w \cdot s_1 \cdot h' = h\)
*    \(\sigma_{-i}^2( h')\) if \(w \cdot s_2\) is a prefix of \(h\) and
  \(w \cdot s_2 \cdot h' = h\)
*    \(\sigma_{-i}(h)\) otherwise

Clearly we have
\(\payoff_i(  Out_s(\sigma_i,\sigma_{-i}'))= 1 \wedge \payoff_i(  Out_s(\sigma_i',\sigma_{-i}')) = 0\),
which contradicts \(\sigma_i' \ge_S \sigma_i\).

````

(parity-games)=
## Parity games

The caracterization given for simple safety game is not enough for
parity objectives, as we will see in the following example.

\begin{figure}
  \begin{center}
    \begin{tikzpicture}
      \draw (0,0) node[draw, circle, inner sep=4pt] (I) {$v_0$};
      \draw (I.-90) node[below] {};
      \draw (4,0) node[draw, inner sep=4pt, circle] (C1) {$v_1$};
      \draw (C1.-100) node[below] {};
      \draw (8,0) node[draw, circle, inner sep=4pt] (C2) {$\Omega_1$};
      \draw (I.-90) node[below] {$1$};
      \draw (C1.-90) node[below] {$1$};
      \draw (C2.-90) node[below] {$2$};
      \draw[-latex'] (-1, 0) -- (I);
      \draw[-latex'] (I) -- node[above]{$(a,*)$} (C1);
      \draw[-latex'] (I) ..controls +(1,2) and +(-1,2)  .. node[above]{$(b,*)$}  (I);
      \draw[-latex'] (C1) -- node[above]{$(*,a)$}(C2);
      \draw[-latex'] (C1) .. controls +(-2, -2) ..  node[above]{$(*,b)$} (I);
      \draw[-latex', rounded corners] (C2)..controls +(1,2) and +(-1,2) .. node[above]{$(a,*)$}(C2);
    \end{tikzpicture}
    \caption{Parity game where the objective for player 1 is to visit
      $\Omega_1$ infinitely often. Player 1 controls square vertices and player 2
      round vertices.}
    \label{fig:adm-parity}
  \end{center}
\end{figure}

````{prf:example} NEEDS TITLE AND LABEL 
  Consider the example in figure {prf:ref}`fig:adm-parity`.
  In this example, although the strategy that always stays in $v_0$
  does not decrease the value of player 1, it is dominated because
  it has no chance of winning.
  By contrast the strategy that always go to $v_1$ has a chance of
  being helped by player 2 and actualy reaching $\Omega_1$ it therefore
  dominates the first strategy.

  Consider the example in figure {prf:ref}`fig:adm-parity`.
  In this example, although the strategy that always stays in $v_0$
  does not decrease the value of player 1, it is dominated because
  it has no chance of winning.
  By contrast the strategy that always go to $v_1$ has a chance of
  being helped by player 2 and actualy reaching $\Omega_1$ it therefore
  dominates the first strategy.

````

However the fact that an admissible strategy should not decrease its own
value still holds. Assuming strategy \(\sigma_i\) of player \(P_i\) does
not decrease its own value, we can classify its outcome in three
categories according to their ultimate values.

*    either ultimately \(\opt_i = 0\), in which case all strategies are
  losing, and thus any strategy is admissible
*    or ultimately \(\pes_i = 1\), in which case admissible strategies are
  exactly the winning ones
*    or ultimately \(\pes_i = 0\) and \(\opt_i = 1\). We will focus on this
case which is more involved.

From a state of value \(0\), an admissible strategy of \(P_i\) should
allow a winning play for \(P_i\) with the help of other players.

We write \(H_i\) for set of vertices \(v\) controlled by a player
\(P_j\ne P_i\) that have at least two successors of optimistic value
\(1\). Formally, the **help-states** $H_i$ of player \(P_i\) are defined
as:

$$
 \bigcup_{P_j\in \Agt \setminus\{i\}} \left\{ s \in V_j \mid \exists s',s'',\ s' \neq s'' \wedge\ s\rightarrow s' \land s \rightarrow s'' \wedge\ \opt_i(s') = 1 \wedge\ \opt_i(s'') = 1 \right\}.
$$

Intuitively, admissible strategies in the case satisfying \(\pes_i = 0\) and \(\opt_i = 1\)
are those that visit infinitely often help states. In fact, letting other players make choices
means that the player is allowing the possibility of them helping to achieve the objective.
More precisely, we have the following property whose proof is omitted.

````{prf:lemma} NEEDS TITLE AND LABEL 
Let \(v\in V\), \(P_i\in \Agt\) and \(\rho\) a play be
such that \(\exists^\infty k. \opt_{i}(\rho_k) = 1\). There exists
\(\sigma_i\) admissible such that \(\rho \in   Out(v, \sigma_i)\) if, and
only if, \(\payoff_i(\rho) = 1\) or
\(\exists^\infty k. \rho_k \in H_i\).

Let \(v\in V\), \(P_i\in \Agt\) and \(\rho\) a play be
such that \(\exists^\infty k. \opt_{i}(\rho_k) = 1\). There exists
\(\sigma_i\) admissible such that \(\rho \in   Out(v, \sigma_i)\) if, and
only if, \(\payoff_i(\rho) = 1\) or
\(\exists^\infty k. \rho_k \in H_i\).

````

(iterated-elimination)=
## Iterated elimination

Once each player is restricted to use admissible strategies, they can
further refine their choices knowing that other players will not be using dominated strategies.
We already saw this in the example of {prf:ref}`13-tab:normal-adm`.
In fact, once player $1$ has eliminated strategy $A$ (which is dominated by $B$),
player $2$ can use this information since its best response against the remaining strategies is $C$.
In more complex games, this reasoning can be repeated and take several steps before converging.
This repeated process is called **iterated elimination of dominated strategies**.

We now define this process formally.

````{prf:definition} NEEDS LABEL Iterated elimination

The **sequence of iterative elimination** is a sequence of rectangular strategy sets defined as follows.
$S^0 = (S_i^0)_{P_i \in \Agt}$ is the set of all strategies.
For $k \geq 0$, if we write $S^k = (S_i)_{P_i \in \Agt}$,
then $S^{k+1}_i$ is the set of strategies in $S^{k}_i$ that are not dominated in $S^k$.

````

Thus, the step $1$ of the sequence of iterative elimination corresponds
to admissible strategies defined above. Let us call them $1$-admissible.
In step 2, we again compute strategies that are dominated by only
considering $1$-admissible strategies for all players, and repeat.
Strategies that survive all step of elimination are said **iteratively admissible**.

````{prf:theorem} NEEDS TITLE AND LABEL 
  In parity games, the sequence of iterative elimination converges, and it reaches a non-empty fixpoint.

  In parity games, the sequence of iterative elimination converges, and it reaches a non-empty fixpoint.

````

We prove this result only for simple safety games since the case of parity conditions is too complex for the scope of this book.

Intuitively, given a game $G$, {prf:ref}`13-thm:adm` tells us that any strategy for player $P_i$ that avoids using edges $D_i$ is admissible. So if we remove all edges $\cup_{P_i \in \Agt} D_i$ from the
game to obtain a new game called $G_1$, then all strategies of $G_1$ (for all players) are admissible in $G$, and conversely.
We can then repeat this process to $G_1$: we construct $G_2$ by eliminating all dominated edges
in $G_1$, and get that admissible strategies in $G_1$ are exactly all strategies of $G_2$,
which correspond to $2$-admissible strategies, and so on.

Since the size of the games decrease at each step, this process necessarily stops.
It remains to show that the limit game $G_\infty$ contains strategies. We will show that
all vertices have at least one outgoing edge in $G_\infty$.
It suffices to show that the sets $D_i$ never contains all edges leaving a vertex.
Let us consider any game $G_j$.
For a vertex $v \in V_i$ with $\pes_i(v)=0$ and $\opt_i(v)=0$, none of the edges are dominated.
For a vertex $v \in V_i$ with $\pes_i(v)=1$ (and necessarily $\opt_i(v)=1$), there exists a winning strategy in $G_j$ so
there must be a successor $v'$ with $\pes_i(v')=1$ which is not dominated.
Last, for a vertex $v \in V_i$ with $\pes_i(v)=0$ and $\opt_i(v)=1$, there exists a winning play from $v$ so for some successor $v'$ we must have $\opt_i(v')=1$ which is an edge that is not dominated.

