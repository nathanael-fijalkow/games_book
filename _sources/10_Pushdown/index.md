(10-chap:pushdown)=
# Pushdown Games

```{image} ./../Illustrations/10.jpg
:alt: illustration
:class: bg-primary mb-1
:width: 400px
:align: center
```
```{math}
\def\AC#1{\textcolor{green!50!black}{\checkmark}\marginpar{\color{green!50!black}AC: #1}} 
\def\acchanged#1{{#1}}
\def\OS#1{\textcolor{red}{\checkmark}\marginpar{\color{red}OS: #1}} 

\renewcommand{\qed}{$\square$}
\newcommand{\pop}{\mathrm{pop}}
\newcommand{\push}[1]{\mathrm{push}(#1)}
\newcommand{\PDS}{\mathcal{P}}
\newcommand{\pdscol}[1]{\col(#1)}
\newcommand{\vect}[1]{\overrightarrow{#1}}
\newcommand{\ttrue}{t\! t}
\newcommand{\ffalse}{f\!\! f}
\newcommand {\Stepsg}[1]{\ensuremath{\mathit{Steps}_{#1}}}
\newcommand{\sh}{\mathrm{sh}}
\newcommand{\fgraph}{\widetilde{G}}
\newcommand{\farena}{\widetilde{\arena}}
\newcommand{\fgame}{\widetilde{\game}}
\newcommand{\fplay}{\widetilde{\play}}
\newcommand{\fsigma}{\widetilde{\sigma}}
\newcommand {\Rounds}[1]{\ensuremath{\mathit{Rounds}_{#1}}}
\newcommand{\kind}[2]{kind(#1,#2)}
\newcommand{\factcol}[2]{\mathrm{mcol}(#1,#2)}
\newcommand{\fac}[1]{kind^{#1}}
\newcommand{\pcol}[1]{\mathrm{mcol}^{#1}}
\newcommand{\hgraph}{\widehat{G}}
\newcommand{\harena}{\widehat{\arena}}
\newcommand{\hgame}{\widehat{\game}}
\newcommand{\hplay}{\widehat{\play}}
\newcommand{\hsigma}{\widehat{\sigma}}
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

Written by Arnaud Carayol, Olivier Serre



This chapter studies two-player games whose arena is defined by a pushdown system.

```{margin}
We use here the term pushdown system rather than pushdown automaton to stress the fact that we are not considering these devices as language acceptors but rather focus on the transitions systems they define.
```

 The vertices of the arena are the configurations of the pushdown system (i.e., pairs composed of a control state and a word representing the content of the stack) and the edges of the arena are defined by the pushdown system's transitions. For simplicity, both the ownership of a configuration and the objective will only depend on the control state of the configuration. Hence the partition of all the configurations between the two players will simply be given by a partition the control states. We will mainly consider the parity objective. Via a standard reduction\AC{Insert a reference to a previous chapter.}, parity pushdown game can be used to solve any pushdown game with an $\omega$-regular objectives (which in our setting is simply an $\omega$-regular set of infinite words over  the alphabet of control states). 

The main conceptual novelty of this chapter is that the arena is no longer finite. However as these games are described by a finite amount of information: the pushdown system, the ownership partition and the $\omega$-regular objective, they are amenable to algorithmic treatment. The first natural problem in this line is to decide the winner of the game from a given configuration. We will also consider the computation of **finite representations** for the winning regions and the winning strategies. 









%

%
## Lower Bound

%Here we show that even for reachability condition the problem is hard for exponential time. We give the proof of Walukiewicz that reduces from the acceptance problem for linear-space alternating Turing machine.

% Hardness for PSPACE when using a counter instead of a general stack (proof ?)

%
## Alternative Approaches

%Connection the full binary tree. Again regularity of the winning region plus the existence of regular positional strategies with Rabin's lemma. 

%

%

%

%

%\section{Beyond Parity Pushdown Games}

%
## Beyond Parity Condition

%Here we present the unboundedness winning condition (mention topological complexity?) and we argue how it can be decided in the same way as parity. Discuss also existing extensions where it is mixed with parity.

%
## Beyond Pushdown Games

%Here we introduce/discuss (depending space) higher-order pushdown automata. We mainly describe the results and also their implications (wrt logic, program verification). Just a discussion probably not the time.

%

