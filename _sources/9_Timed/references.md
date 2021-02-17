(9-sec:references)=
# Bibliographic references

```{math}
\usepackage{amsmath}
  
\newcommand*\Realnn{\mathbb{R}_{\geq 0}}
\newcommand*\Clocks{\mathcal{C}}
\newcommand*\TA{\ensuremath{\mathcal{A}}}
\newcommand*\Locs{\mathcal{L}}
\newcommand*\Clocksz{\mathcal{C}_0}
\newcommand*\calQ{\mathcal{Q}}
\newcommand*\state{\mathsf{state}}
\newcommand*\trans{\mathsf{trans}}
\newcommand*\post{\mathsf{post}}
\newcommand*\step{\mathsf{step}}
\newcommand*\postta{\ensuremath{\textrm{\sf Post}}}
\newcommand*\preta{\ensuremath{\textrm{\sf Pre}}}
\newcommand*\unreset{\ensuremath{\textrm{\sf Unreset}}}
\newcommand*\posttime{\ensuremath{\textrm{\sf Post}_{\geq 0}}}
\newcommand*\pretime{\ensuremath{\textrm{\sf Pre}_{\geq 0}}} \newcommand*\reset{\mathsf{Reset}}
\newcommand{\sem}[1]{\ensuremath{#1}}
\newcommand{\size}[1]{\ensuremath{|#1|}}

\def\predc{\textrm{\sf Pred}_c}
\def\predt{\textrm{\sf Pred}_{\geq 0}} \def\predu{\textrm{\sf Pred}_u}
\def\calP{\mathcal P}
\def\calC{\mathcal C}
\def\calT{\mathcal T}
\def\Dep{\textsf{Dep}}
\def\Wait{\textsf{Wait}}
\def\Passed{\textsf{Passed}}
\def\Act{\textsf{Act}}
\def\EA{E_{\Adam}}
\def\EE{E_{\Eve}}

\newcommand\zone[1]{\ensuremath{\left\llbracket#1\right\rrbracket}}
\def\NM#1{\textcolor{green!50!black}{\checkmark}\marginpar{\color{green!50!black}NM: #1}} 
\long\def\NMlong#1{\medskip\par{\color{green!50!black}NM: #1}\medskip\par}
\def\OS#1{\textcolor{blue!50!black}{\checkmark}\marginpar{\color{blue!50!black}OS: #1}} 
\long\def\OSlong#1{\medskip\par{\color{blue!50!black}OS: #1}\medskip\par}

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
Timed games were first introduced by Asarin, Maler, Pnueli and Sifakis {cite}`MPS95,AMPS98`, in a
slightly different form.  Our presentation is based on the algorithms
proposed by Liu and Smolka {cite}`LS98`, and extended to timed games by
Cassez, David, Fleury, Larsen and Lime {cite}`CDFLL05`;
its~main advantage is that it runs **on-the-fly**, building (part
of) the arena while exploring it, and terminating as soon as a winning
strategy is found.  A~first on-the-fly algorithm was proposed by Tripakis and Altisen
in {cite}`TA99`, but it was not fully on-the-fly as it would run on a
quotient graph of the timed arena, which involves an expensive
preprocessing step.

Timed games---and already timed automata---may exhibit unrealistic
behaviours, such as finite-duration executions containing infinitely
many transitions (often referred to as **Zeno** behaviours).
In~our semantics, \Adam may always prevent \Eve from playing her move
by choosing a shorter delay than hers, even if it means selecting a convergent
sequence of delays. {numref}`9-fig:exzeno` displays a simple example of
such a situation: in~that game, \Adam~may prevent \Eve from reaching her
winning state $q_1$ by always selecting a delay shorter than the delay
proposed by~\Eve.

```{figure} ./../FigAndAlgos/9-fig:exzeno.png
:name: 9-fig:exzeno
:align: center
A timed game where \Adam may prevent \Eve from reaching $q_1$
```

An alternative semantics of timed games was proposed by de~Alfaro,
Faella, Henzinger, Majumdar, and Stoelinga {cite}`AFHMS03` to
circumvent this problem: it~consists in **blaming** at each round
the player playing the shortest delay, and declaring any player losing
(even~if she reaches her goal) in case the infinite sequence of delays
converges and that player received infinitely many blames.  For~such a
semantics, \Eve~has a winning strategy in the game
of {numref}`9-fig:exzeno`, which consists in proposing a converging
sequence of delays, until her action is applied; such a strategy
requires infinite memory, but strategies with randomized delays can
circumvent this {cite}`CHP08`. Other~approaches to avoid
arbitrary-precision strategies have been explored
in {cite}`BMS15,BFM15,LLTW14,ORS14`.

% circumvent this problem: it~consists in **blaming** at each round

% (even~if she reaches her goal) in case the infinite sequence of delays

% semantics, \Eve~has a winning strategy in the game

% avoid strategies that require arbitrary

Timed games have been extended with weights, in order to model other
quantities besides time (e.g. energy consumption). This is somewhat
similar to the finite-state games extended with payoffs
of~\cref{chap:payoffs}; in~the timed setting however, besides evolving
along transitions in the game, the payoff is also modified when timed
elapses, and the change is proportional to the time spent. As~proven
in {cite}`BBR05,BBM06`, optimal reachability (a.k.a. the shortest-path
problem) is undecidable in that setting, but arbitrary-precise
approximation of the optimal cost can be computed {cite}`BJM15`.

Timed games with partial observability have been investigated
in {cite}`BDMP03`: in~that setting, \Eve only has partial observation
of the state and clock valuation of the arena; she~also owns a finite
set of clocks she can use to measure other delays. Whether \Eve has a
winning strategy in such a setting has been proved decidable if the
set of clocks and their precision are fixed; it~is undecidable if they
are not fixed.

A~different setting was developed in {cite}`CDLLR07`, with
**stuttering-invariant strategies**, which are triggered by
observation changes. The~on-the-fly algorithm presented in this
chapter can be adapted to that setting {cite}`CDLLR07`. 

The~algorithm we presented in this chapter is implemented in the tool
Uppaal TiGa {cite}`BCD+07`. Uppaal~TiGa has been applied on various
cases {cite}`CJLRR09,Sor14`, and combined with
reinforcement-learning techniques to efficiently synthesise, optimise
and evaluate strategies for stochastic timed games {cite}`DJLMT15`.

Another approach, relying on
abstraction-refinement techniques, was proposed in {cite}`EMP10`;
it~merges locations so as to obtain simpler games, while weakening one
player and strengthening her opponent. Solving the smaller games
provides approximations on the winning set, which are used to refine
the abstractions and accelerate their analyses. This~approach is
implemented in the tool Synthia {cite}`PEM11`.



```{bibliography}
:style: unsrtalpha
:filter: cited and chap == "9"
```