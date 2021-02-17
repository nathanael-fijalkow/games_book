(7-sec:notations)=
# Notations

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
\newcommand{\EXPSPACE}{\textrm{EXPSPACE}}
\newcommand{\EXP}{\textrm{EXP}}
\newcommand{\kEXP}{\textrm{kEXP}}
```
The definition of arena $\arena$ in this chapter is $\arena=(G,\dest)$, where $G=(V,E)$ is a graph and $\dest:V\times A\times A\rightarrow \Dist(E)$. In particular, we are not using the sets $\VA$ and $\VE$.
The games are played similarly to before and formally as follows: 
There is a token, initially on the initial vertex. 
Whenever the token is on some vertex $v$, 
Eve selects an action $r$ in $A$ and Adam selects an action $c$ in $A$. The edge $e=(v,c,w)$ is then drawn from the distribution $\dest(v,r,c)$ and the token is pushed from $v$ to $w$.
 In general, the game continues like that forever.

We will use the following simplifying assumptions in this chapter:

1.  We will assume that all colors are in $\{0,1\}$, except for the section on Matrix games where we additionally also allow $-1$ (to be able to easily illustrate the game rock-paper-scissors). This simplifies some expressions, but generally, the dependency on the number of colors is not too bad comparatively.

2.  To make illustrations easier, we assume that for any pair of edges $e,e'$ in $\dest(v,a,a')$ for any $v,a,a'$, we have that $c(e)=c(e')$, i.e. the color does not depend on which edge is picked from $\dest(v,a,a')$, but only $v,a,a'$. This assumption does not matter for the types of games considered.

We will overload the notation slightly for notational convenience, in that for any $v,a,a'$, we will write $c(v,a,a')$ for $c(e)$ where $e\in \dest(v,a,a')$ (note that the second assumption ensures that this is well-defined, i.e. there is only one such color).

A vertex $v$ is absorbing iff each player has only 1 action in $v$ and $\Delta(v,1,1)=v$.

To describe the complexity of good stationary strategies in concurrent games, we will use the notion of patience. Given a probability distribution $d\in \Dist$ the distribution has patience $p$ if $p=\min_{i\in \supp(d)} d(i)$ (i.e. the patience is the smallest, non-zero probability that an event may happen according to $d$).
In essence, if you have low enough patience you can typically guess the strategy and check whether it is a good strategy (when you fix a strategy, the game becomes a Markov decision process, which are relative easy to work with), the game can solved in $\NP\cup \coNP$. However, some times the patience is huge and writing down a good strategy, in binary, cannot be done in polynomial space (it is quite surprising in some sense that even with this property, finding the values in the games remain in $\PSPACE$).

We will illustrate a stochastic arena $\arena=(G,\dest)$ as follows:
For each non-absorbing vertex $v$, there is matrix.
 Entry $(i,j)$ of the matrix illustrating $v\in V$ describes what happens if, when the token is on $v$, Eve plays $i$ and Adam $j$. The entry contains a color $c$, which is $c(v,i,j)$, and 
there is an arrow from entry $(i,j)$ of $v$ to $w$ if there is an edge   
$e=(v,c,w)$ in $\dest(v,i,j)$. 
 The arrow corresponding to $e$ is denoted with the probability $\dest(v,i,j)(e)$. 
Especially, to simplify the illustrations we will do as follows: If $|\supp(\dest(v,i,j))|=1$, we do not include the probability (which is 1). Also, in that case, let $e=(v,c,w)=\dest(v,i,j)$ 
and 
if $v=w$, we omit the arrow and if $w$ is absorbing we write $c^*$ in entry $i,j$ of $v$, where $c$ is the color $c(w,1,1)$ (in this case, we omit the number $c(e)$ from the illustration, but in none of our illustrations does this number matter for what we try to illustrate). 
