(4-sec:notations)=
# Notations

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
In this chapter all objectives we consider use the set of colours $C = \Z$ the set of integers 
(or $C = \Z \cup \set{\Win}$ for the shortest path objective), 
so a colour is called a weight interpreted as a payoff for Eve.
We will study different quantitative objectives corresponding to different ways of aggregating the weights.
Recall that in a quantitative objective Eve aims at maximising the outcome, while Adam
tries to minimise it.
We let $\ValueE^\game(v)$ and $\ValueA^\game(v)$ be the values for Eve and Adam in the game $\game$: 
this is the best each player can unilaterally guarantee from the vertex $v$, no matter which strategy the other player uses.
All the quantitative objectives we will study in this chapter are Borel, hence determined thanks to \cref{1-cor:borel_determinacy}: 
$\ValueE^\game(v) = \ValueA^\game(v)$ for all vertices $v$. 
We thus let $\Value^\game(v)$ denote this value (and $\Value(v)$ if $\Game$ is clear from the context).

For complexity statements we use the unit cost RAM model as defined in Section {ref}`1-sec:computation`.
For each objective we introduce we will discuss what is the relevant machine word size, both we can already make some preliminary remarks.
Let us consider a game $\Game$ with an objective using the set of colours $C = \Z$
and let $W$ denote the largest weight appearing in $\Game$ in absolute value.
Choosing the machine word size $w = \log(m) + \log(W)$ implies that an edge together with its weight can be stored in one machine word and that we can perform arithmetic operations on weights, hence for most objectives we will use the machine word size $w = \log(m) + \log(W)$.
The only exception will be the discounted payoff objectives, which additionally have a discount factor $\lambda \in (0,1)$
that needs to be given in the input.
