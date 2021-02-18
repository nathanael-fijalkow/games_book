(4-sec:qualitative)=
# Refining qualitative objectives with quantities


```{math}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\play}{\pi}
\newcommand{\AttrE}{\textrm{Attr}_\mEve}
\newcommand{\Win}{\textrm{Win}}
\newcommand{\Lose}{\textrm{Lose}}
\newcommand{\Safe}{\mathtt{Safe}}
\newcommand{\Reach}{\mathtt{Reach}}
\newcommand{\Buchi}{\mathtt{Buchi}}
\newcommand{\CoBuchi}{\mathtt{CoBuchi}}
\newcommand{\MeanPayoff}{\mathtt{MeanPayoff}}
\newcommand{\DiscountedPayoff}{\mathtt{DiscountedPayoff}}
\newcommand{\Sup}{\mathtt{Sup}}
\newcommand{\Inf}{\mathtt{Inf}}
\newcommand{\LimSup}{\mathtt{LimSup}}
\newcommand{\LimInf}{\mathtt{LimInf}}
```

In this section we define quantitative objectives extending the qualitative objectives $\mathtt{Safe}, $\mathtt{Reach}, $\mathtt{Buchi}, and $\mathtt{CoBuchi}.

%visit infinitely often) $v_f^{(1)}$ if possible, or $v_f^{(2)}$

%of preferences with a parity condition by mapping $v_f^{(1)}$ to the

%etc. A more natural and versatile way to model this preference though

%this section.

The four quantitative objectives we will define in this section return as outcome some weight in the sequence (for instance, the maximum weight).
This is in contrast with the $\mathtt{MeanPayoff} and $\mathtt{DiscountedPayoff} objectives that we will study later,
which perform **arithmetic operations** on the sequence of weights.

A first way to compute a payoff from a sequence of weights $\rho \in \mathbb{Z}\omega$ is to consider the maximum weight in the sequence:

$$
\mathtt{Sup}\rho) = \sup_i \rho_i.
$$

This extends the qualitative objective $\mathtt{Reach}\textrm{Win}$ in the following sense: 
the objective $\mathtt{Reach}\textrm{Win}$ corresponds to the quantitative objective $\mathtt{Sup} using two weights: $0$ for $\textrm{Lose} and $1$ for $\textrm{Win}.
The outcome of a sequence is $1$ if and only if the sequence contains $\textrm{Win}.
It refines $\mathtt{Reach}\textrm{Win}$ by specifying (numerical) preferences.

The dual objective is to consider the smallest weight:

$$
\mathtt{Inf}\rho) = \inf_i \rho_i.
$$

The qualitative objective $\mathtt{Safe}\textrm{Win}$ corresponds to the quantitative objective $\mathtt{Inf}
using two weights: $0$ for $\textrm{Win} and $1$ for $\textrm{Lose}.
The outcome of a sequence is $0$ if and only if the sequence does not contain $\textrm{Lose}.

Similarly the following quantitative objectives refine $\mathtt{Buchi} and $\mathtt{CoBuchi}:

$$
  \mathtt{LimSup}\rho) = \limsup_i \rho_i,\qquad 
  \mathtt{LimInf}\rho) = \liminf_i \rho_i.
$$


%using weights $0$ and $1$, we have that the payoff of a play $\pi

%$\textrm{Win} (respectively, visits finitely often a losing colour $\textrm{Lose}).

The analyses and algorithms for solving games with $\mathtt{Reach}, $\mathtt{Safe}, $\mathtt{Buchi}, and $\mathtt{CoBuchi} objectives extend to these four quantitative objectives.

````{prf:theorem} NEEDS TITLE 4-thm:sup-inf-limsup-liminf
:label: 4-thm:sup-inf-limsup-liminf

Games with objectives $\mathtt{Sup} and $\mathtt{LimSup} are uniformly positionally determined for both players.
There exists an algorithm for computing the value function of both games in polynomial time and space.
More precisely, let $k$ be the number of different weights in the game,
the time complexity is $O(m)$ for objective $\mathtt{Sup} and $O(knm)$ for objective $\mathtt{LimSup},
and for both algorithms the space complexity is $O(m)$.

````


````{admonition} Proof
:class: dropdown tip

We sketch the algorithm for the objective $\mathtt{Sup}, the cae $\mathtt{LimSup} is similar.
Let $c_1 < \dots < c_k$ be the ordered enumeration of all weights in the game.
The set of vertices of value $c_k$ is $\textrm{Attr}_\mEvec_k)$, which can be computed in linear time.
We then construct the subgame $\Game'$ of $\Game$ induced by $V \setminus \textrm{Attr}_\mEvec_k)$,
and continue recursively: $\Game'$ has one less weight.

A naive complexity analysis yields a time complexity $O(km)$, but it is easily refined to $O(m)$ 
by revisiting the attractor computation and showing that each edge in the whole game is treated at most once
throughout the recursive attractor computations.
This complexity analysis does not extend to $\mathtt{LimSup} objectives, where the complexity is multiplied by $k$.

````

