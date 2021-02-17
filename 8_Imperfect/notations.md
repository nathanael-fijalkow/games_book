(8-sec:notations)=
# Notations

```{math}
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
We consider **stochastic games with signals**, that are a standard tool in game theory to model imperfect information in stochastic games {cite}`sorinafirst,dinahnicolas1,renault2`.
When playing a stochastic game with signals, players cannot observe
the actual state of the game, nor the actions played by themselves or
their opponent: the only source of information of a player are private
signals they receive throughout the play.  Stochastic games with
signals subsume standard stochastic games {cite}`shapley`, repeated
games with incomplete information {cite}`aumann`, games with imperfect
monitoring {cite}`dinahnicolas1`, concurrent games {cite}`dAH00` and
deterministic games with imperfect information on one
side {cite}`reif,chdr07`.
%\newcommand{\SA}{S_{\mAdam}}
Like in previous chapters, $V$, $C$ and $A$  
denote respectively the sets
of vertices, colors and actions.

````{prf:definition} NEEDS TITLE AND LABEL 
An imperfect information arena $\arena$ is a tuple $(S,\Delta)$ where 

*  $S$ is the set of **signals**
*  $\Delta : V \times A \times A \to \dist(V \times S \times S \times C)$
 maps the current vertex and a pair of actions to a probability distribution
 over vertices, pairs of signals and colors.

 

An imperfect information arena $\arena$ is a tuple $(S,\Delta)$ where 

*  $S$ is the set of **signals**
*  $\Delta : V \times A \times A \to \dist(V \times S \times S \times C)$
 maps the current vertex and a pair of actions to a probability distribution
 over vertices, pairs of signals and colors.

````

\newcommand{\NN}{\mathbb{N}}
\newcommand{\RR}{\mathbb{R}}

Initially, the game is in a state $v_0 \in V$ chosen according to a probability distribution
$\ini\in\dist(V)$ known by both players; the initial state is
$v_0$ with probability $\ini(v_0)$.  At each step $n\in\NN$, both players
simultaneously choose some actions $a,b \in A$
 They respectively receive signals
$s,t \in S$ ,
 and the game moves to a
new state $v_{n+1}$.  This happens with probability
$\Delta(v_{n},a,b)(v_{n+1},c,d)$.
{This fixed probability is known by both players,
as well as the whole description of the game.}

A **play** is a sequence $(v_0,a_0,b_0,s_0,t_0,c_0),(v_1,a_1,b_1,s_1,t_1,c_1),(v_2\ldots$
such that for every $n$, the probability $\Delta(v_{n},a_n,b_n)(v_{n+1},s_n,t_n,c_n)$
is positive.

A sequence of signals for a player
is **realisable** for Eve if it appears in a play,
we denote $R_E \subseteq S^*$ the set of these sequence.
Similarly for Adam.

> **An example.**

The simplified poker can be 
modelled as a stochastic game with signals.
Actions of players are **public signals**
sent to both players.
Also their the payoff of Eve is publicly announced,
when non-zero. 
Upon choosing whether to call or fold,
Adam cannot distinguish between states
$\spadesuit${\tt Raised} and $\blacksquare${\tt Raised},
in both cases he received the sequence of signals $\circ,{\tt raise}$.
A graphical representation is provided on
Figure~\ref{9-fig:poker}.
%$\circ$ to both players, the signals are not represented.
\newcommand{\pay}{ {\tt pay}}


```{figure} ./../FigAndAlgos/9-fig:poker.png
:name: 9-fig:poker
:align: center
The simplified poker game.
```

The game is played with  $4$ cards $\{\spadesuit,\heartsuit,\clubsuit,\diamondsuit\}$.
We exploit the symmetry of payoffs with respect to $\{\heartsuit,\clubsuit,\diamondsuit\}$ and identify these three colours 
as a single one, denoted $\blacksquare$, received initially by Eve with probability $\frac{3}{4}$.
The set of vertices
is an initial vertex ${\tt Start}$,
a terminal vertex ${\tt End}$
plus the four states

$$
\{\spadesuit,\blacksquare\} \times 
 \{{\tt Play,Raised}\}\enspace.
 $$

The set of colors are possible payoffs $C=\{0,-1,+1,-3,+3\}$.

The set of actions $A$ 
is the union of 
actions of Eve 
$A_E=\{{\tt \cdot, check,raise}\}$
and actions of Adam
$A_A=\{{\tt \cdot, call, fold}\}$.

The set of signals is $\{\circ , \spadesuit, \blacksquare\}$ plus
$\{{\tt check},{\tt raise},{\tt call},{\tt fold}\}\times \{0,-1,+1,-3,+3\}$.

The rules of the game,
are defined by the set of **legal** transitions.
Let $c \in \{\spadesuit,\blacksquare\}$.
The following transitions are legal.
\begin{align*}
&~\Delta({\tt Start},{\tt \cdot},{\tt \cdot})((c,{\tt Play}),c,\circ,0)=
\begin{cases}
\frac{1}{4}& \text{ if } c= \spadesuit\\
\frac{3}{4}& \text{ if } c= \blacksquare\enspace.
\end{cases}\\
&~\Delta((c,{\tt Play}),{\tt check},{\tt \cdot})({\tt End},{\tt check}_x,{\tt check}_x,x)=1
\text{ where } x=
\begin{cases}
+1 & \text{ if } c=\spadesuit\\
-1& \text{ if } c=\blacksquare.
\end{cases}
\\
&~\Delta((c,{\tt Play}),{\tt raise},{\tt \cdot})((c,{\tt Raised}),{\tt raise_0},{\tt raise_0},0)=1\\
&~\Delta((c,{\tt Raised}),{\tt \cdot},{\tt call})({\tt End},{\tt call}_x,{\tt call}_x,x)=1 
\text{ where } x=
\begin{cases}
+3 & \text{ if } c=\spadesuit\\
-3 & \text{ if } c=\blacksquare.
\end{cases}
\\
&~\Delta((c,{\tt Raised}),{\tt \cdot},{\tt fold})({\tt End},{\tt fold_1},{\tt fold_1},+1)=1\\
&~\text{state ${\tt End}$ is absorbing with payoff $0$.}
\end{align*}



To simplify the notations,
we assumed in the general case
that players share the same set of actions and signals.
As a consequence, other transitions than the legal ones
are possible. 
One can use a threat to guarantee that Eve plays
${\tt check}$ and ${\tt raise}$ after receiving her card,
by setting a heavy loss of $-10$ if she plays another action instead.
Same thing to enforce that Adam plays ${\tt call}$ or ${\tt fold}$
after receiving the signal ${\tt raise}$.
When targetting applications,
legal moves should be explicitely
specified, typically using an automaton
to compute the set of legal actions
depending on the sequence of signals.


> **Strategies: behavioral, mixed and general.**


Intuitively, players make their decisions based upon the sequence of
signals they receive, which is formalised with strategies. 
There are several natural classes of strategies to play games with signals, as discussed in {cite}`horn_remember` and~\cite[Section 4]{BGGjacm}.

A behavioural strategy of Eve associates
with every realisable sequence of signals a probability distribution
over actions:  

$$
\sigma: R_E \to \dist(A)\enspace.
$$

When Eve plays $\sigma$, after having received a sequence of signals
$s_0,\ldots,s_n$ she chooses action $a$ with probability
$\sigma(s_0,\ldots,s_n)(a)$. 
Strategies of Adam are the same, except they are defined on $R_A$.

Remark that in general a player may not observe which actions he actually played,
for example $S$ might be a singleton 
in which case the players only knows the number of steps so far.

A game has **observable actions** if there exists a mapping
 $\Act:S \to A$ 
 such that

$$
\Delta(v,a,b)(w,s,t)>0 
\implies
(a=\Act(s) \land b=\Act(t))\enspace. 
$$


In~\cite[Lemma 4.6 and 4.7]{BGGjacm} it was shown that without loss of generality,
one can consider games where actions are observable and players 
play behavioural strategies. The discussion is technical and beyond the scope of this book.
