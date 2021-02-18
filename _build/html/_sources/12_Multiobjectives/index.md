(12-chap:multiobjective)=
# Games with multiple objectives

```{image} ./../Illustrations/12.jpg
:alt: illustration
:class: bg-primary mb-1
:width: 400px
:align: center
```
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


Written by Mickael Randour



Up to this chapter, we have mostly been interested in finding strategies that achieve a **single** objective or optimise a **single** payoff function. Our goal here is to discuss what happens when one goes further and wants to build strategies that (i) ensure **several objectives**, or (ii) provide **richer guarantees** than the simple worst-case or expectation ones used respectively in zero-sum games and MDPs. 

Consider case (i). Such requirements arise naturally in applications: for instance, one may want to define a trade-off between the performance of a system and its energy consumption. A model of choice for this is the natural **multidimension** extension of the games of Chapter {ref}`4-chap:payoffs`, where we consider weight vectors on edges and combinations of objectives.

In case (ii), we base our study on stochastic models such as MDPs (Chapter {ref}`5-chap:mdp`). We will notably present how to devise controllers that provide strong guarantees in a worst-case scenario while behaving efficiently on average (based on a stochastic model of its environment built through statistical observations); effectively reconciling the rational antagonistic behaviour of Adam, used in games, with the stochastic interpretation of uncontrollable interaction at the core of MDPs.

Stepping into the multiobjective world is like entering a jungle: the sights are amazing but the wildlife is overwhelming. Providing an exhaustive account of existing multiobjective models and the latest developments in their study is a task doomed to fail: simply consider the combinatorial explosion of all the possible combinations based on the already non-exhaustive set of games studied in the previous chapters. Hence, our goal here is to guide the reader through his first steps in the jungle, highlighting the specific dangers and challenges of the multiobjective landscape, and displaying some techniques to deal with them. To that end, we focus on models studied in Chapter {ref}`2-chap:regular`, Chapter {ref}`4-chap:payoffs`, Chapter {ref}`5-chap:mdp` and Chapter {ref}`11-chap:counters`, and multiobjective settings that extend them. We favour simple, natural classes of problems, that already suffice to grasp the cornerstones of multiobjective reasoning. 

> **Chapter outline**

 In Section {ref}`12-sec:multiple_dimensions`, we illustrate the additional complexity of multiobjective games and how relations between different classes of games that hold in the single objective case often break as soon as we consider combinations of objectives. 

The next two sections are devoted to the **simplest form** of multiobjective games: games with **conjunctions** of classical objectives. In Section {ref}`12-sec:mean_payoff_energy`, we present the classical case of multidimension mean-payoff and energy games, which preserve relatively nice properties with regard to their single-objective counterparts. In Section {ref}`12-sec:total_payoff_shortest_path`, we discuss the opposite situation of total-payoff and shortest path games: their nice single-objective behaviour vanishes here.

In the last two sections, we explore a different meaning of **multiobjective** through so-called rich behavioural models. Our quest here is to find strategies that provide several types of guarantees, of different nature, for the same quantitative objective. In Section {ref}`12-sec:beyond_worst_case`, we address the problem of **beyond worst-case synthesis**, which combines the rational antagonistic interpretation of two-player zero-sum games with the stochastic nature of MDPs. We will study the mean-payoff setting and see how to construct strategies that ensure a strict worst-case constraint while providing the highest expected value possible.
In Section {ref}`12-sec:percentile`, we briefly present **percentile queries**, which extend **probability threshold problems** in MDPs to their multidimension counterparts. \todo{Check what I do exactly.} Interestingly, **randomized strategies** become needed in this context, whereas up to Section {ref}`12-sec:percentile`, we only consider deterministic strategies as they suffice.

We close the chapter with the usual bibliographic discussion and pointers towards some of the many recent advances in multiobjective reasoning.












