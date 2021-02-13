(4-sec:qualitative)=
# Refining qualitative objectives with quantities

```{math}
\newcommand{\Eve}{\textrm{Eve}}
\newcommand{\Adam}{\textrm{Adam}}
\newcommand{\set}[1]{\left\{ #1 \right\}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Zinfty}{\Z \cup \set{\pm \infty}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\Rinfty}{\R \cup \set{\pm \infty}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\Qinfty}{\Q \cup \set{\pm \infty}}
\newcommand{\argmax}{\text{argmax}}
\newcommand{\argmin}{\text{argmin}}
\newcommand{\Op}{\mathbb{O}}
\newcommand{\Prob}{\mathbb{P}} \newcommand{\dist}{\mathcal{D}} \newcommand{\Dist}{\dist} \newcommand{\supp}{\text{supp}} 
\newcommand{\game}{\mathcal{G}} \renewcommand{\Game}{\game} \newcommand{\arena}{\mathcal{A}} \newcommand{\Arena}{\arena} 
\newcommand{\col}{\textsf{col}} \newcommand{\Col}{\col} 
\newcommand{\mEve}{\mathrm{Eve}}
\newcommand{\mAdam}{\mathrm{Adam}}
\newcommand{\mRandom}{\mathrm{Random}}
\newcommand{\vertices}{V} \newcommand{\VE}{V_\mEve} \newcommand{\VA}{V_\mAdam} \newcommand{\VR}{V_\mRandom} 
\newcommand{\ing}{\text{In}}
\newcommand{\Ing}{\ing}
\newcommand{\out}{\text{Out}}
\newcommand{\Out}{\out}
\newcommand{\dest}{\Delta} 
\newcommand{\WE}{W_\mEve} \newcommand{\WA}{W_\mAdam} 
\newcommand{\Paths}{\text{Paths}} \newcommand{\play}{\pi} \newcommand{\first}{\text{first}} \newcommand{\last}{\text{last}} 
\newcommand{\mem}{\mathcal{M}} \newcommand{\Mem}{\mem} 
\newcommand{\Pre}{\text{Pre}} \newcommand{\PreE}{\text{Pre}_\mEve} \newcommand{\PreA}{\text{Pre}_\mAdam} \newcommand{\Attr}{\text{Attr}} \newcommand{\AttrE}{\text{Attr}_\mEve} \newcommand{\AttrA}{\text{Attr}_\mAdam} \newcommand{\rank}{\text{rank}}
\renewcommand{\Win}{\textsc{Win}} 
\renewcommand{\Lose}{\textsc{Lose}} 
\newcommand{\Value}{\text{val}} 
\newcommand{\ValueE}{\text{val}_\mEve} 
\newcommand{\ValueA}{\text{val}_\mAdam}
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
```
In this section we define quantitative objectives extending the qualitative objectives $\Safe$, $\Reach$, $\Buchi$, and $\CoBuchi$.

The four quantitative objectives we will define in this section return as outcome some weight in the sequence (for instance, the maximum weight).
This is in contrast with the $\MeanPayoff$ and $\DiscountedPayoff$ objectives that we will study later,
which perform **arithmetic operations** on the sequence of weights.

A first way to compute a payoff from a sequence of weights $\rho \in \Z^\omega$ is to consider the maximum weight in the sequence:

$$
\Sup(\rho) = \sup_i \rho_i.
$$

This extends the qualitative objective $\Reach[\Win]$ in the following sense: 
the objective $\Reach[\Win]$ corresponds to the quantitative objective $\Sup$ using two weights: $0$ for $\Lose$ and $1$ for $\Win$.
The outcome of a sequence is $1$ if and only if the sequence contains $\Win$.
It refines $\Reach[\Win]$ by specifying (numerical) preferences.

The dual objective is to consider the smallest weight:

$$
\Inf(\rho) = \inf_i \rho_i.
$$

The qualitative objective $\Safe[\Win]$ corresponds to the quantitative objective $\Inf$
using two weights: $0$ for $\Win$ and $1$ for $\Lose$.
The outcome of a sequence is $0$ if and only if the sequence does not contain $\Lose$.

Similarly the following quantitative objectives refine $\Buchi$ and $\CoBuchi$:

$$
  \LimSup(\rho) = \limsup_i \rho_i,\qquad 
  \LimInf(\rho) = \liminf_i \rho_i.
$$


The analyses and algorithms for solving games with $\Reach$, $\Safe$, $\Buchi$, and $\CoBuchi$ objectives extend to these four quantitative objectives.

```{prf:theorem} (needs title)
:label: 4-thm:sup-inf-limsup-liminf

Games with objectives $\Sup$ and $\LimSup$ are uniformly positionally determined for both players.
There exists an algorithm for computing the value function of both games in polynomial time and space.
More precisely, let $k$ be the number of different weights in the game,
the time complexity is $O(m)$ for objective $\Sup$ and $O(knm)$ for objective $\LimSup$,
and for both algorithms the space complexity is $O(m)$.

```


```{admonition} Proof
:class: dropdown tip

We sketch the algorithm for the objective $\Sup$, the cae $\LimSup$ is similar.
Let $c_1 < \dots < c_k$ be the ordered enumeration of all weights in the game.
The set of vertices of value $c_k$ is $\AttrE(c_k)$, which can be computed in linear time.
We then construct the subgame $\Game'$ of $\Game$ induced by $V \setminus \AttrE(c_k)$,
and continue recursively: $\Game'$ has one less weight.

A naive complexity analysis yields a time complexity $O(km)$, but it is easily refined to $O(m)$ 
by revisiting the attractor computation and showing that each edge in the whole game is treated at most once
throughout the recursive attractor computations.
This complexity analysis does not extend to $\LimSup$ objectives, where the complexity is multiplied by $k$.

```

