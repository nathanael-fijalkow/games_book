(5-sec:references)=
# Bibliographic references

```{math}

\newcommand{\expv}{\mathbb{E}} \newcommand{\discProbDist}{f} \newcommand{\sampleSpace}{S} \newcommand{\sigmaAlg}{\mathcal{F}} \newcommand{\probm}{\mathbb{P}} \newcommand{\rvar}{X} 

\newcommand{\actions}{A} \newcommand{\colouring}{c} \newcommand{\probTranFunc}{\Delta} \newcommand{\edges}{E} \newcommand{\colours}{C} \newcommand{\mdp}{\mathcal{M}} \newcommand{\vinit}{v_0} \newcommand{\cylProb}{p} \newcommand{\emptyPlay}{\epsilon} \newcommand{\objective}{\Omega} \newcommand{\genColour}{\textsc{c}} \newcommand{\quantObj}{f} \newcommand{\quantObjExt}{\bar{\quantObj}} \newcommand{\indicator}[1]{\mathbf{1}_{#1}} \newcommand{\eps}{\varepsilon} \newcommand{\maxc}{\max_{\colouring}} 
\newcommand{\winPos}{W_{>0}}
\newcommand{\winAS}{W_{=1}}
\newcommand{\cylinder}{\mathit{Cyl}}
\newcommand{\PrePos}{\text{Pre}_{>0}}
\newcommand{\PreAS}{\text{Pre}_{=1}}
\newcommand{\PreOPPos}{\mathcal{P}_{>0}}
\newcommand{\OPAS}{\mathcal{P}_{=1}}
\newcommand{\safeOP}{\mathit{Safe_{=1}}}
\newcommand{\closed}{\mathit{Cl}}

\newcommand{\reachOP}{\mathcal{V}}
\newcommand{\discOP}{\mathcal{D}}
\newcommand{\valsigma}{\vec{x}^{\sigma}}
\newcommand{\lp}{\mathcal{L}}
\newcommand{\lpdisc}{\lp_{\mathit{disc}}}
\newcommand{\lpreach}{\lp_{\mathit{reach}}}
\newcommand{\lpmp}{\lp_{\mathit{mp}}}
\newcommand{\lpsol}[1]{\bar{\vec{#1}}}
\newcommand{\lpsolg}[1]{\bar{#1}}
\newcommand{\lpmpdual}{\lpmp^{\mathit{dual}}}
\newcommand{\actevent}[3]{\actions^{#1}_{#2,#3}} 
\newcommand{\MeanPayoffSup}{\MeanPayoff^{\;+}}
\newcommand{\MeanPayoffInf}{\MeanPayoff^{\;-}}
\newcommand{\mcprob}{P}
\newcommand{\invdist}{\vec{z}}
\newcommand{\hittime}{T}
\newcommand{\playPay}{\textsf{p-Payoff}}
\newcommand{\stepPay}{\textsf{s-Payoff}}
\newcommand{\Pay}{\textsf{Payoff}}
\newcommand{\mec}{M}
\newcommand{\OPS}{\mathcal{S}_{=1}}
\newcommand{\smallmp}{\mathit{mp}}
\newcommand{\vgood}{v_{\mathit{good}}}
\newcommand{\vbad}{v_{\mathit{bad}}}
\newcommand{\finact}{fin}
\newcommand{\mecs}{\mathit{MEC}}
\newcommand{\slice}[2]{#1_{#2-}}
\newcommand{\ReachOp}{\mathcal{R}}
\newcommand{\dPayoffStep}[1]{\DiscountedPayoff^{\;(#1)}}
\newcommand{\solvset}{S}
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
\newcommand{\coNP}{\textrm{coNP}}
\newcommand{\PSPACE}{\textrm{PSPACE}}
```
There is a broad field of study related to Markov decision processes, with a history going as far as  1950's {cite}`Bellman:1957`. It is beyond the scope of this chapter to provide a comprehensive overview of the related literature. Nonetheless, in this section we provide pointers to the most significant works connected to our techniques as well as to works that can serve as a starting point for a further study.

One of the most widely used references for MDP-related research is the textbook by Puterman {cite}`Puterman:2005`. The textbook views MDPs from an operations research point-of-view, focusing on finite-horizon, discounted, total-reward, and average reward (an alternative name for mean-payoff) objectives. Regular objectives fall outside of the book's focus, though reachability can be viewed as a special case of the positive bounded total reward objectives studied in the book. An in-depth study of the textbook will impart to its reader the knowledge of many useful techniques for MDP analysis, though a reader who is a newcomer to MDPs might feel somewhat intimidated by its sheer volume and generality. In this chapter, we follow Puterman's exposition mainly in the discounted payoff, albeit in a rather condensed form. 

For mean-payoff MDPs, {cite}`Puterman:2005` follows similar blueprint as in the discounted case: first characterizing the optimal values via a suitable optimality equation and then deriving the value iteration, strategy improvement, and linear programming methods from this characterization. We use the linear programming as our foundational stone, focusing on the relationship between strategies and feasible solutions of the program. We note that value and strategy iteration for mean-payoff MDPs come with super-polynomial lower bounds, see, e.g. {cite}`Fearnley:2010,Fearnley:2010b`, or {cite}`Puterman:2005`, where it is shown that strategy improvement converges at least as fast as value iteration.

Also, {cite}`Puterman:2005` makes the initial analysis of mean-payoff MDPs in the context of **unichain** MDPs, and then extends to arbitrary MDPs, with strongly connected MDPs treated as a special case of the latter. While unichain is an important theoretical concept, in the context of formal methods and automata it is preferable to work with strongly connected MDPs. We also note that all the results in the mean-payoff sections hold also for $\MeanPayoffSup$. Almost all of the proofs are the same, with an important exception of \Cref{5-cor:mp-value-bound}, where Fatou's lemma cannot be used to prove that $\playPay(\vinit,\sigma) \leq \stepPay(\vinit,\sigma)$. Instead, we could use **martingale techniques** here. Martingales are an important concept in probability theory {cite}`Williams:1991`, with applications e.g. in analysis of infinite-state MDPs and stochastic games {cite}`Brazdil&Brozek&Etessami&Kucera:2011`. We can use martingales to strengthen  {prf:ref}`5-lem:dual-bound-step` by showing that the probability  of $\sum_{i=0}^{n-1}\colouring(\play_i) \geq \sqrt{n}\cdot \expv^\sigma_{\vinit}[\sum_{i=0}^{n-1}\colouring(\play_i)]$ converges (with an exponential rate of decay) to $0$ as $n\rightarrow \infty$, which allows us to prove the required bound for $\limsup$.

 The notion of a (M)EC as well as many techniques we use in the EC section are due to de Alfaro, whose thesis {cite}`dA:1997` details the evolution of the concept and its relation to similar notions. The algorithm for MEC decomposition is taken from {cite}`Chatterjee&Henzinger:2011`, where more advanced algorithms as well as use of MECs in parity MDPs are discussed.

For an overview of literature related to verification of temporal properties in MDPs, we refer the reader to the monograph {cite}`Baier&Katoen:2008`.

MDPs are also used as a prime model in reinforcement learning (RL), one of the classical yet rapidly evolving sub-fields of AI. For RL-centric view of MDPs, we point the reader towards the textbooks {cite}`Sutton&Barto:2018,Bertsekas:2017`.


```{bibliography}
:style: unsrtalpha
:filter: cited and chap == "5"
```