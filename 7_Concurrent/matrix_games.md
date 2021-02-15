(7-sec:matrix_games)=
# Matrix games

```{math}
\newcommand{\ValueOp}{\text{valOp}}
\newcommand{\rk}{\text{rk}}
\newcommand{\crgLim}{\text{crgLim1}}
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
```
A matrix game is a game defined from a $(R\times C)$-matrix $M$  of numbers for some $R,C$.
The game is played as follows: Eve picks a row $r$ and Adam picks a column $c$ simulations like in rock-paper-scissors. Adam then pays Eve $M[r,c]$, i.e. the content of the entry defined by being in row $r$ and column $c$.
A strategy in such a game for Eve (resp. Adam) consists of a distribution over the rows (resp. columns). 
There is an illustration of rock-paper-scissors as a matrix game in Figure~\ref{fig:rps}.


```{figure} ./../fig:rps.png
:name: fig:rps
:align: center
Rock-paper-scissors. The color is 1 if Eve wins, 0 if they draw and -1 if Adam wins. Also, the actions are ordered as in the name of the game
```

The following theorem lists some known results for matrix games:

```{prf:theorem} NEEDS TITLE lem:mat
:label: lem:mat

Each $(m\times n)$-matrix game $M$ is determined and there exists optimal strategies for each player. 

*  The value and an optimal strategy for each player can be found in polynomial time and the problem is equivalent to linear programming.

*  Let $c>0$ be some constant. Consider the matrix $cM$ where each entry of $M$ has been multiplied by $c$. Then, the value of $cM$ is $cv$.
*  Let $c$ be some constant. Consider the matrix $M+c$ where each entry of $M$ is $c$ larger (additively). Then, the value of $M+c$ is $v+c$.
*  The value of matrix games are monotone in the entries.

```

We will omit the proof of the existence of values, optimal strategies and the first bullet.
The second bullet can be viewed as changing currency and clearly, this does not affect the optimal strategy.
The third bullet can be viewed as getting a reward before playing the game, and again, clearly this does not affect how to play it.
The last bullet can be seen from that each pair of strategies must give a higher reward if the entries of the matrix is higher.
This is especially true if you consider the optimal strategy for Eve in $M$ together with an arbitrary strategy for Adam, which then shows that the value is higher.

Given a matrix $M$, we will by $\Value[M]$ denote the value of the matrix game $M$. 

Perhaps interestingly, an illustration of a matrix $M$ can be viewed as a game arena $\arena$ (for concurrent games) with only one non-absorbing vertex. In each type of games considered in this section (apart from concurrent reachability games, where no game can be illustrated as a matrix with non-star entries different from 0), the value of the game with that arena matches $\Value[M]$ and the optimal strategies for each player is to play an optimal strategy from $M$ in each round. One can also consider a game arena $\arena^*$ with an illustration similar to $M$, but where there is a star in each entry (and $c(v,i,j)=0$ for the unique non-absorbing state $v$ and any pair of actions $i,j$).
Again, the value is $\Value[M]$ (except for the case of discounted objectives, where the value is $(1-\delta)\Value[M]$) and the optimal strategies for each player is again to play an optimal strategy from $M$. 

One could easily be lead to believe that in games (called repeated games with absorbing states) that can be illustrated as a single matrix $M$ with some entries stared and others not, the value would be similar to $\Value[M]$ and the optimal strategy would again be to play the optimal strategy from $M$. 
However, this is very much not true and indeed, many of the games in this chapter, illustrating how complex concurrent games can be, are repeated games with absorbing states! In particular repeated games with absorbing states may (1)~have irrational values and probabilities in optimal strategies (with any objective), (2)~have no optimal strategies (for reachability and mean-payoff objectives) and (3)~have no $\epsilon$-optimal finite-memory or $\epsilon$-optimal Markov strategies (for mean-payoff objectives)!
