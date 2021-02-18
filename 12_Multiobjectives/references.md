(12-sec:references)=
# Bibliographic references

```{math}

\newcommand{\expv}{\mathbf{E}} \newcommand{\markovProcess}{\ensuremath{{\mathcal{P}} }}
\newcommand{\stratStoch}{\ensuremath{\tau^{\text{stoch}} }}
\newcommand{\BWC}{\text{BWC}}
\newcommand{\ecsSet}{\ensuremath{\mathcal{E}} }
\newcommand{\edgesNonZero}{\ensuremath{E_{\delta}} }
\newcommand{\ec}{\ensuremath{U} }
\newcommand{\playerOne}{\text{Eve} }
\newcommand{\playerTwo}{\text{Adam} }
\newcommand{\winningECs}{\ensuremath{\mathcal{W}} }
\newcommand{\losingECs}{\ensuremath{\mathcal{L}} }
\newcommand{\edges}{\ensuremath{E} }
\newcommand{\maxWinningECs}{\ensuremath{\mathcal{U}_{\textsc{w}}} }
\newcommand{\infVisited}[1]{\ensuremath{{\sf Inf}(#1)} }
\newcommand{\negligibleStates}{\ensuremath{V_{{\sf neg}}} }
\newcommand{\stratWC}{\ensuremath{\sigma^{\text{wc}}} }
\newcommand{\stratExp}{\ensuremath{\sigma^{\text{e}}} }
\newcommand{\stratComb}{\ensuremath{\sigma^{\text{cmb}}} }
\newcommand{\stratSecure}{\ensuremath{\sigma^{\text{sec}}} }
\newcommand{\stratWNS}{\ensuremath{\sigma^{\text{wns}}} }
\newcommand{\stratGlobal}{\ensuremath{\sigma^{\text{glb}}} }
\newcommand{\stepsWC}{\ensuremath{L} }
\newcommand{\stepsExp}{\ensuremath{K} }
\newcommand{\stepsGlobal}{\ensuremath{N} }
\newcommand{\cmbSum}{\ensuremath{\mathsf{Sum}} }
\newcommand{\typeA}{\ensuremath{**(a)**} }
\newcommand{\typeB}{\ensuremath{**(b)**} }
\newcommand{\thresholdWC}{\ensuremath{\alpha} }
\newcommand{\thresholdExp}{\ensuremath{\beta} }
\newcommand{\state}{\ensuremath{v} }
\newcommand{\gameNonZero}{\ensuremath{\arena_{\delta}} }
\newcommand{\reduc}{\ensuremath{\downharpoonright} }
\newcommand{\probm}{\mathbb{P}} 
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
As discussed in the introduction, the literature on multiobjective models is too vast to provide a full account here. We therefore focus on some directions particularly relevant to our focus.

> **Multidimension games.**

 Energy games and their related work were discussed in~\cref{chap:counters}. Our presentation of mean-payoff games is inspired by Velner et al. {cite}`Velner&al:2015`. Brenguier and Raskin studied the Pareto curves of these games in {cite}`Brenguier&Raskin:2015`. While we considered **conjunctions** of mean-payoff objectives, Velner proved that Boolean combinations lead to undecidability {cite}`Velner:2015`.

The undecidability of total-payoff games was first established in {cite}`Chatterjee&al:2015` via reduction from the halting problem for two-counter machines: we provided here a new, simpler proof based on robot games {cite}`Niskanen&Potapov&Reichert:2016`. This undecidability result, along with the complexity barriers of mean-payoff and total-payoff games, motivated the introduction of (multidimension) **window objectives**: conservative variants of mean-payoff and total-payoff objectives that benefit from increased tractability and permit to reason about time bounds {cite}`Chatterjee&al:2015`. Window variants of parity objectives have been studied in {cite}`Bruyere&Hautem&Randour:2016`.

> **Combinations of different objectives.**

 We focused on multidimension games obtained by conjunction of **identical** objectives. Conjunctions of **heterogeneous** objectives have been studied in a variety of contexts including mean-payoff parity games {cite}`Chatterjee&Henzinger&Jurdzinski:2005,Daviaud&Jurdzinski&Lazic:2018`, energy parity games {cite}`Chatterjee&Doyen:2012,Chatterjee&Randour&Raskin:2014`, average-energy games with energy constraints {cite}`Bouyer&al:2018,Bouyer&al:2017`, simple quantitative objectives {cite}`Bruyere&Hautem&Raskin:2016`. Le Roux, Pauly and Randour studied general conditions under which finite-memory strategies suffice to play optimally, even in a broad multi-objective setting {cite}`LeRoux&Pauly&Randour:2018`.

> **Beyond worst-case synthesis.**

 Our presentation is mostly based on {cite}`Bruyere&al:2017`, where all technical details can be found. As noted in {cite}`Bruyere&al:2017`, allowing large inequalities in the BWC problem may require infinite-memory strategies. The case of infinite-memory strategies was studied in {cite}`Clemente&Raskin:2015` along with multidimension BWC mean-payoff problems. BWC problems were studied for other objectives, such as shortest path {cite}`Bruyere&al:2017` or parity {cite}`Berthon&Randour&Raskin:2017`; and on other related models (e.g., {cite}`Brazdil&Kucera&Novotny:2016,Almagor&Kupferman&Velner:2016`). BWC principles have been implemented in the tool \textsc{Uppaal} {cite}`David&al:2014`.

Comparisons with other rich behavioural models can be found in {cite}`Randour&Raskin&Sankur:2015,Brenguier&al:2016`.

```{bibliography}
:style: unsrtalpha
:filter: cited and chap == "12"
```