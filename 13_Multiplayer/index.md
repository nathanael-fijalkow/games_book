(13-chap:multiplayer)=
# Multiplayer Games

```{image} ./../Illustrations/13.jpg
:alt: illustration
:class: bg-primary mb-1
:width: 400px
:align: center
```
```{math}
\def\payoff{\ensuremath{f}}
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
\def\Coalition{\ensuremath{\mathcal{C}}}
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

Written by Romain Brenguier, Ocan Sankur



In two player games seen so far, players had objectives that are
opposite to each other's, so we were able to define them giving only
Eve's objective. Adam was seen as a purely adversarial player. Such games
are called **zero-sum** games since, in a quantitative setting, the
sum of the payoffs of the two players would sum up to zero in any
outcome. However, the objectives of the players are not entirely
conflicting in all games.
In particular, in multiplayer games, that is,
games with more than two players, the binary view of zero-sum games
does not make sense;%games with more than two players, cannot be zero-sum by definition;
but there are also interesting examples of non-zero sum games with only two
players (we will see one below). In this setting, winning strategies are
no longer suitable to describe rational behaviors since the opponents
should no longer be seen as purely adversarial. In fact, when the
objectives of the players are not opposite, some cooperation becomes
possible. Then, rather than assuming that opponents are purely
adversarial, it is interesting to study the possible outcomes when they
are simply **rational**, that is, follow the best strategy for their
own objectives. The notion of equilibria we will study in this chapter
aims at describing such rational behaviors.

If one is expecting for sure some specific strategies to be played by the
opponents, then the most rational response is to choose the
**best response**, that is, the strategy that is optimal for the
player against the given strategies of the other players. Thus, if we
assign strategies to players, and if the players are all aware of the
strategies of the other players, then each player will be willing to
change their strategy if theirs does not turn out to be a best response.
Such a situation is seen as unstable and is undesirable in many
applications of game theory. **Nash equilibrium** is defined simply
as a stable situation in such a setting: a strategy profile in which the
strategy of each player is a best response to the rest of the
strategies. Thus, no player has any incentive to change their strategy.

We will see the formal definition of a Nash equilibrium in the next
section. Let us first consider the following example.

The following Hawk-Dove game was first presented by the biologists Smith
and Price, and shown in Table~\ref{13-tab:hawk-dove}.
Here, two animals are fighting for ressources and can choose to
either act as a hawk or as a dove.
If both player choose hawk they will have to fight for resources, and
thus only get payoff 0. If only one chooses hawk, they get a high payoff of
4, because they get all the valuable resources for themselves, while the dove
gets 1: they get plenty of resources but gets hunted. When they both choose
dove, they both get a payoff of 3: they have to share resources but do not get
hunted.

When a player chooses hawk then the best payoff for the opponent is
obtained by choosing dove, so as to avoid fighting for resources.
So, dove is the best response to hawk. Reciprocally, the best response to
dove is to play hawk. There are two equilibria: (Hawk, Dove) and
(Dove, Hawk), where no player has an interest in changing their
strategy. Note that the highest payoff a player can ensure
(against all adversary strategies) is only $1$.%\todo{What does winning strategy mean??}
Nash showed the existence of such equilibria in any normal-form game
,
which may require randomized strategies.

```{margin}
normal-form games are also called matrix games, and some
specific form was defined in \Cref{chap:concurrent}.
```

 This result
revolutionized the field of economics, where it is used to analyze
competitions between firms or government economic policies for example.
Game theory and the concept of Nash equilibrium are now applied to
diverse fields: in finance to analyse the evolution of market prices, in
biology to understand the evolution of some species, in political
sciences to explain public choices made by parties.

\begin{table}
  \caption{The Hawk-Dove game. Each column corresponds to a strategy of
    \(P_1\) and each line to a strategy of \(P_2\).}
  \label{13-tab:hawk-dove}
  \begin{center}
    \begin{tabular}[c]{|@{~}l@{~}|@{~}c@{~} @{~}c@{~}|}
      \hline
      & Hawk & Dove \\
      \hline
      Hawk & 0 , 0 & 1 , 4 \\
      Dove & 4 , 1 & 3 , 3 \\
      \hline
    \end{tabular}
  \end{center}
\end{table}

\medskip
In this chapter, we will first study the computation of Nash
equilibria in multiplayer concurrent games with $\omega$-regularobjectives. The algorithms we present here differ from those that were
given for normal-form games since ours are infinite-duration with
omega-regular objectives. We will then present extensions of this notion
such as secure and
robust equilibria. The second result we develop is
the notion of admissibility: this is a different approach to the study
of rational behaviours and consist in eliminating for each player
irrational choices of strategies.






