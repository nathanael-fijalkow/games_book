(8-chap:signal)=
# Games with Signals

```{image} ./../Illustrations/8.jpg
:alt: illustration
:class: bg-primary mb-1
:width: 400px
:align: center
```
```{math}
\newcommand{\pay}{ {\tt pay}}
\newcommand{\probimp}[3]{\mathbb{P}^{#1}_{#2}\left({#3}\right)}
\newcommand{\rand}{{\tt rand}}
\newcommand{\Isafe}{{\tt ISafe}}
\newcommand{\LL}{\mathcal{L}}
\newcommand{\KK}{\mathcal{K}}
\newcommand{\LLE}{\LL_{\text{Eve},=1}}
\newcommand{\LLA}{\LL_{\text{Adam},>0}}
\newcommand{\can}{\textsf{max}}
\newcommand{\targets}{TT}
\newcommand{\bh}{\setminus}
\newcommand{\signauxdeux}{T}
\newcommand{\actionsun}{A}
\newcommand{\Strat}{\text{Strat}}
\newcommand{\Act}{\text{Act}}
\newcommand{\ini}{\delta_0}
\newcommand{\win}{{\tt Win}}
\newcommand{\winreach}{{\tt Reach}}
\newcommand{\winsafe}{{\tt Safety}}
\newcommand{\winbuchi}{{\tt Buchi}}
\newcommand{\wincobuchi}{{\tt CoBuchi}}
\newcommand{\states}{V}
\newcommand{\ar}{\arena}
\newcommand{\action}{a}
\newcommand{\belun}{\mathcal{B}_{\text{Eve}}}
\newcommand{\beldeux}{\mathcal{B}_{\text{Adam}}}
\newcommand{\deuxbelun}{\mathcal{B}^{(2)}_{Eve}}
\newcommand{\tp}{\Delta}
\newcommand{\parties}[1]{\ensuremath{\mathcal{P}(#1)}}
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

Written by Hugo Gimbert



> **Imperfect information.**

This chapter presents a few results about zero-sum games with imperfect information.
Those games are a generalization of concurrent games in order to take into account the possibility that players might be imperfectly informed about the current state of the game
and the actions taken by their opponent, or even their own action. We will also discuss situations where players may forget what they used to know.

Before providing formal definitions of games with imperfect information,
we give three examples.

> **Simple poker.**


%Chris Ferguson, Bright Trading, Westwood, California Thomas S. Ferguson, University of California, Los Angeles
Our first example is a finite duration game which is a simplified version of poker,
inspired by Borel and von Neumann simplified poker {cite}`ferguson`.
This game is played with  $4$ cards $\{\spadesuit,\heartsuit,\clubsuit,\diamondsuit\}$.

*  The goal of Eve and Adam is to win
the content of a pot in which, initially, they both put $1$ euro.
*  Eve receives a private random card, unknown by Adam.
*  Eve decides whether to check or raise.
If she checks then she wins the pot iff her card is $\spadesuit$.
*  If Eve raises then Adam has two options: fold
or call. If Adam folds then Eve receives the pot.
If Adam raises then both player add two euros in the pot
and Eve wins the pot iff her card is $\spadesuit$.

A natural strategy for Eve is to raise when she has a spade and otherwise
check. Playing so, she reveals her card to Adam,
and we will see that the optimal behaviour for her
consists in bluffing from time to time,
i.e. raise although her card is not a spade.

> **The distracted logician.**

Our second example is another finite duration game.
A logician is driving home. For that he should go through two crossings,
and turn left at the first one and right at the second one.
This logician is very much absorbed in his thoughts,
trying to prove that $P\neq NP$,
and is thus pretty distracted: upon taking a decision, he cannot  tell
whether he already saw a crossing or not.

This simple example is useful to discuss the observability of actions
and make a distinction between
mixed strategies and behavioral strategy.
 
> **Network controller.**

The following example is inspired from collision regulation
in ethernet protocols: the controller of a network card
has to share an ethernet layer with
another network card, controller by another controller,
possibly malicious.

When sending a data packet,
the controller selects a delay in microseconds between $1$ and $512$
and transmits this delay to the network card.
The other controller does the same.
The network cards try to send their data packet at the chosen dates.
Choosing the same date results in a data collision, and the process is repeated until
there is no collision, at that time the data can be sent.

The chosen delay has to be kept hidden from the opponent.
This way, it can be chosen randomly,
which ensures that the data will eventually be sent with probability $1$,
whatever does the opponent.
  
> **Guess my set.**

Our third example is an infinite duration game,
parametrized by some integer $n$.
The play is
divided into three phases.

*  In the first phase, Eve secretly chooses a subset
$X \subsetneq \{1, \ldots,2n\}$ of size $n$
among the $\binom{2n}{n}$ possibilities.
*  In the second phase, Eve discloses to Adam
$\frac{1}{2}\binom{2n}{n}$ pairwise distinct sets of size
$n$ which are all different from $X$. 
*  In the third phase, Adam aims at guessing $X$ by trying up to
$\frac{1}{2} \binom{2n}{n}$ sets of size $n$. 
If Adam succeeds in guessing $X$,
the game restarts from the beginning. Otherwise, 
Eve wins.

Clearly Adam has a strategy to prevent forever
Eve to win: try up one by one all those sets
that were not disclosed by Eve.
This strategy uses a lot of memory:
Adam has to remember the whole sequence of $\frac{1}{2} \binom{2n}{n}$
 sets disclosed by Eve.
We will see that a variant of this game can be represented 
in a compact way, using a number of states polynomial in $n$.
As a consequence, playing optimally a game with imperfect-information and infinite duration
might require a memory of size doubly-exponential in the size of the game.









