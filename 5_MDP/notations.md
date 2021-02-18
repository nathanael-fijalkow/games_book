(5-sec:notations)=
# Notations

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
\newcommand{\UP}{\textrm{UP}}
\newcommand{\coNP}{\textrm{coNP}}
\newcommand{\coUP}{\textrm{coUP}}
\newcommand{\PSPACE}{\textrm{PSPACE}}
\newcommand{\EXPSPACE}{\textrm{EXPSPACE}}
\newcommand{\EXP}{\textrm{EXP}}
\newcommand{\kEXP}{\textrm{kEXP}}
```
We write vectors in boldface: $ \vec{x}, \vec{y}, $ etc. For a vector $ \vec{x} $ indexed by a set $ I $ (i.e. $ \vec{x}\in \mathbb{R}^I $) we denote by $ \vec{x}_i $ the value of the component whose index is  $i\in I  $. 

A (discrete) probability distribution over a finite or countably infinite set $A$ is a function $\discProbDist A \colon \rightarrow [0,1]$ such that $\sum_{a\in A}\discProbDist(a)=1$. The support of such a distribution $\discProbDist$ is the set of all $a\in A$ with $\discProbDist(a)>0$. A distribution $f$ is called Dirac if its support has size 1.

We denote by $\dist(A)$ the set of all probability distributions over $A$.

We also deal with probabilities over uncountable sets of events. This is accomplished via the standard notion of a **probability space.**

````{prf:definition} Probability space
:label: 5-def:probspace

A probability space is a triple
$(\sampleSpace,\sigmaAlg,\probm)$ where

*  $\sampleSpace$ is a non-empty set of **events** (so called
**sample space**). 

*  $\sigmaAlg$ is a sigma-algebra over $\sampleSpace$,
i.e. a collection of subsets of $\sampleSpace$ that contains the empty set
$\emptyset$ and that is closed under complementation and countable unions. The members of $\sigmaAlg$ are called $\sigmaAlg$-measurable 
sets.

*  $\probm$ is a probability measure on $\sigmaAlg$, i.e. a function
$\probm\colon \sigmaAlg\rightarrow[0,1]$ such that:

*  $\probm(\emptyset)=0$;

*  for all $A\in \sigmaAlg$ it holds $\probm(\sampleSpace \setminus
A)=1-\probm(A)$; and

*  for all countable sequences of pairwise disjoint sets $A_1,A_2,\dots \in \sigmaAlg$ (i.e., $A_i \cap A_j = \emptyset$ for all $i\neq j$)
we have $\sum_{i=1}^{\infty}\probm(A_i)=\probm(\bigcup_{i=1}^{\infty} A_i)$.


````


A random variable in the probability space $(\sampleSpace,\sigmaAlg,\probm)$ is an $\sigmaAlg$-measurable function $\rvar\colon \Omega \rightarrow \R \cup
\{-\infty,\infty\}$, i.e.,
a function such that for every $a\in \R \cup \{ -\infty,\infty\}$ the set
$\{\omega\in \Omega\mid \rvar(\omega)\leq a\}$ belongs to $\mathcal{F}$. We denote by $\expv[\rvar]$ the expected value of a random variable $\rvar$~(see Chapter 5 in {cite}`Bil:1995` for a formal definition).

We first give a syntactic notion of an MDP which is an analogue of the notion of an arena for games.

````{prf:definition} MDP
:label: 5-def:MDP

A Markov decision process is a tuple $(\vertices,\edges,\probTranFunc,\colouring)$. The meaning of $\vertices$, $\edges$, and $\colouring$ is the same as for games, i.e. $\vertices$ is a finite set of vertices, $\edges\subseteq \vertices\times\vertices$ is a set of edges and $\colouring\colon \edges \rightarrow \colours$ a mapping of edges to a set of colours. However, the meaning of $\probTranFunc$ is now different: $\probTranFunc$ is a partial probabilistic transition function of type $\probTranFunc\colon \vertices \times \actions \rightarrow \dist(\edges)$, such that the support of $\probTranFunc(v,a)$ only contains edges outgoing from $v$.

 We usually write $\probTranFunc(v'\mid v,a)$ as a shorthand for $\probTranFunc(v,a)((v,v'))$, i.e. the probability of transitioning from $v$ to $v'$ under action $a$.

````


We also stipulate that for each edge $(v_1,v_2)$ there exists an action $a\in \actions$ such that $\probTranFunc(v_2\mid v_1,a)>0$. Edges not satisfying this can be always removed without changing the semantics of the MDP, which is defined below. We denote by $ p_{\min} $ the smallest non-zero edge probability in a given MDP, i.e. $ p_{\min} = \min\{x>0 \mid \exists u,v \in \vertices, a \in \actions \text{ s.t. } x = \probTranFunc(v\mid u,a)\}. $

We denote by $\edges_\genColour$ the set of edges coloured by $\genColour$. Also, for MDPs where $\colours$ is some set of numbers, we use $\maxc$ to denote the number $\max_{e\in 
\edges}|\colouring(e)|$.
In the setting of MDPs it is technically convenient to encode regular objectives (Reachability, B&uuml;chi,\dots) by colours on **vertices** as opposed to edges. Hence, when discussing these objectives, we assume that the colouring function $\colouring$ has the type $\vertices \rightarrow \colours$.



%TODO: REMARK ABOUT POSSIBLE REPRESENTATION WITH STOCHASTIC VERTICES

> **Plays and strategies in MDPs**



%however, one new important notion, the one of cylinder sets. A basic 

%having $\play$ as a prefix.

 The way in which a play is generated in an MDP is similar to games, but now encompasses a certain degree of randomness. There is a single player, say Eve, who controls all the vertices. Eve's interaction with the world described by an MDP is probabilistic. One reason is the stochasticity of the transition function, the other is the fact that in MDP settings, it is usually permitted for Eve to use randomised strategies. Formally, a randomised strategy is a function $\sigma : E^* \to \dist(A)$, which to each finite play assigns a probability distribution over actions. 

 We typically shorten $\sigma(\play)(a)$ to $\sigma(a\mid \play)$.
 
 
In this section, we will refer to randomised strategies simply as strategies. The strategies known from the game setting will be called  deterministic strategies. Formally, a deterministic strategy can be viewed as a special type of a randomised strategy which always selects a Dirac distribution over the edges. We shorten memoryless randomised/deterministic to MR and MD, respectively.

Now a play in an MDP is produced as follows: in each step, when the finite play produced so far (i.e. the history of the game token's movement) is $\play$, Eve chooses an action $a$ randomly according to the distribution $\sigma(\play)$. Then, an edge outgoing from $\last(\play)$ is chosen randomly according to $\probTranFunc(\last(\play),a)$ and the token is pushed along the selected edge. As shown below, this intuitive process can be formalized by constructing a special probability space whose sample space consists of infinite plays in the MDP. 



> **Formal semantics of MDPs**


Formally, to each MDP $\mdp$, each (Eve's) strategy $\sigma$ in $\mdp$, and 
each initial vertex $\vinit$ we assign a probability space 
$(\sampleSpace_{\mdp},\sigmaAlg_{\mdp},\probm^{\sigma}_{\mdp,\vinit})$. To 
explain the individual components, we need the notion of a cylinder set. A 
basic cylinder determined by a finite play $\play$ is the set of 
all infinite plays in $\mdp$ having $\play$ as a prefix. Now the above 
probability space consists of the following components:

*  $\sampleSpace_{\mdp}$ is the set of all infinite plays in $\mdp$;
*  $\sigmaAlg_{\mdp}$ is the **Borel** sigma-algebra over 
$\Omega_{\mdp}$; this is the smallest sigma-algebra containing all the 
basic cylinder sets determined by finite plays in $\mdp$. The sets in 
$\sigmaAlg_{\mdp}$ are called events. Note that the smallest sigma-algebra of the desired property is guaranteed to exist, since an intersection of an arbitrary number of sigma-algebras is again a sigma algebra.
*  $\probm^{\sigma}_{\mdp,\vinit}$ is the unique probability measure 
arising from the **cylinder construction** detailed below. We use 
$\expv^{\sigma}_{\mdp,\vinit}$ to denote the expectation operator 
associated to the measure $\probm^{\sigma}_{\mdp,\vinit}$.




Since the sample space $\sampleSpace_{\mdp}$ is uncountable, we construct the 
probability measure by first specifying a probability of certain simple sets of 
runs and then using an appropriate **measure-extension** theorem to extend 
the probability measure, in a unique way, to all sets in $\sigmaAlg_{\mdp}$.
The standard cylinder construction  
proceeds as follows: for each finite play $\play$ we define the probability 
$\cylProb(\play)$ such that

*  for an empty play $\emptyPlay$ we put $\cylProb(\emptyPlay)=1$;
*  for a non-empty play $\play=\play_0\cdots \play_{k}$ initiated in 
$\vinit$ we put 

$$\cylProb(\play) = \cylProb(\play_{< k})\cdot \Big(\sum_{a \in \actions} 
\sigma(a\mid \play_{< k})\cdot \probTranFunc(\last(\play)\mid 
\last(\play_{< k}),a) 
\Big), $$

where we use the convention that $\last(\play_{< 0})=\vinit$;
*  for all other $\play$ we have $\cylProb(\play)=0$.

Now using an appropriate measure-extension theorem
(such as Hahn-Kol\-mo\-go\-rov theorem~\cite[Corollary 2.5.4 and Proposition  2.5.7]{Rosenthal:2006}, or Carath\'eodory theorem~\cite[Theorem 1.3.10]{Ash&Doleans-Dade:2000}) one can show that there is a 
unique probability 
measure $\probm^{\sigma}_{\mdp,\vinit} $ on $\sigmaAlg_{\mdp}$ such that for 
every cylinder set $\cylinder(\play)$ determined by some finite play $\play$ we have $\probm_{\vinit}^\sigma(\cylinder(\play))=\cylProb(\play)$. (Abusing the notation, we write $\probm^{\sigma}_{\mdp,\vinit}(\play)$ for the probability of this cylinder set). There 
are some intermediate steps to be performed before an extension theorem 
can be applied, and we omit these due to space constraints. Full details on the 
cylinder construction can be found, e.g. in {cite}`Ash&Doleans-Dade:2000,Novotny:2015`.

While the construction of the probability measure 
$\probm^{\sigma}_{\mdp,\vinit}$ might seem a bit esoteric, in the context of 
MDP verification we do not usually need to be concerned with all the delicacies 
behind the associated probability space. The sets of plays that we work with 
typically arise from the basic cylinder sets by means of countable unions, 
intersections, and simple combinations thereof; such sets by definition belong 
to the 
sigma-algebra $\sigmaAlg_{\mdp}$, and their probabilities can be inferred using 
basic probabilistic reasoning. Nevertheless, one should keep in mind that all the 
probabilistic argumentation rests on solid formal grounds. 

%practice the formal understanding of probability theory might find the 

%chapters with stochastic models) introduces some set of plays or a random 

%$\sigmaAlg_{\mdp}$, why is the random variable $\sigmaAlg_{\mdp}$-measurable, 

%objects.

In the standard MDP literature {cite}`Puterman:2005`, the plays are often defined as alternating sequence of vertices and actions. Here we stick to the edge-based definition inherited from deterministic games. Still, we would sometimes like to speak about quantities such as probability that action $a$ is taken in step $i$. To this end, we introduce, for each strategy $\sigma$, each action $a$,  and each $i\geq 0$,  a random variable $\actevent{\sigma}{a}{i}$ such that $\actevent{\sigma}{a}{i}(\play)=\sigma(\play_{< i})(a)$. It is easy to check that  $\expv^\sigma_v[\actevent{\sigma}{a}{i}]$ is the probability that action $a$ is played in step $i$ when using strategy $\sigma$.

> **Objectives in MDPs**


Similarly to plays, the notions of both qualitative and quantitative objectives 
are inherited from the non-stochastic world of games. However, since plays in 
MDPs are generated stochastically, even for a fixed strategy $\sigma$ there is 
typically no single infinite play that would constitute the outcome of 
$\sigma$. A concrete $\sigma$ might yield different outcomes, depending on the 
results of random events during the interaction with the MDP. Hence, we need a 
more general way of evaluating strategies in MDPs. 

In the game setting, a qualitative objective was given as a set $\objective
\subseteq \colours^{\omega}$. In the MDP setting, we require that such 
$\objective$ is measurable in the sense that the set $\colouring^{-1}(\objective) = \{\play \in \sampleSpace_{\mdp} \mdp \colouring(\play) \in \objective \}$ belongs to $\sigmaAlg_{\mdp}$. We can then talk about a 
probability that the produced play falls satisfies $\objective$. For instance, for a 
colour $\genColour$ the objective $ \Reach(\genColour) $ is indeed measurable, since $ \colouring^{-1}(\objective) $ can be written as a countable union of all basic cylinders that are determined by finite plays ending in a vertex coloured by $ \genColour $. Indeed, all the qualitative objectives studied in previous chapters can be shown measurable in a similar way, and we encourage the reader to prove this as an exercise.
Hence, the expression 
$\probm^{\sigma}_{\mdp,\vinit}(\Reach(\genColour))$ 
denotes the probability that a vertex of colour $\genColour$ is reached when 
using 
strategy $\sigma$ from vertex $\vinit$. 
In line with previous conventions, we 
stipulate that Eve aims to maximize this probability. 

The situation is more complex for quantitative objectives. As shown in the previous chapter, 
when working with quantitative objectives, the set of colours $\colours$ is typically the set of real numbers (or a subset thereof), and the quantitative objective is given by an aggregating function $\quantObj\colon \colours^\omega \rightarrow \R$, which can be extended into a function $\quantObjExt\colon \edges^\omega \rightarrow \R $ by putting $ \quantObjExt(\play) = \quantObj( \colouring(\play_0)\colouring(\play_1)\cdots) $.

%objective in the game setting was given by a function 

In the MDP setting, we 
require that $\quantObjExt$ is $\sigmaAlg_{\mdp}$-measurable, which 
means that for each $x\in \R$ the set $\{\pi\in \edges^\omega\mid 
\quantObj(\colouring(\play_0)\colouring(\play_1)\cdots) \leq x\}$ belongs to 
$\sigmaAlg_{\mdp}$ (again this holds for all the objectives studied 
in the previous chapters). Then there are two ways in which we can define the expected payoff achieved by strategy $ \sigma $ from a vertex $ v $.
First, we can treat 
$\quantObjExt$ as a random variable 
in the probability space 
$(\sampleSpace_{\mdp},\sigmaAlg_{\mdp},\probm^{\sigma}_{\mdp,v})$. Then the play-based payoff of $\sigma$ from $ v $, which we denote by $ \playPay_\quantObj(v,\sigma) $, is the expected value of this random variable, i.e. $ \playPay_\quantObj(v,\sigma) = \expv_{v}^\sigma [\quantObjExt] $. That is, we compute the expected payoff over all plays. This approach subsumes also qualitative objectives: For such an objective $\objective$ we can consider an indicator random 
variable $\indicator{\objective}$, such that $\indicator{\objective}(\play)=1$ 
of 
$\play\in\Omega$ and $\indicator{\objective}(\play)=0$ otherwise. Then 
$\probm^{\sigma}_{\mdp,v}(\objective) = 
\expv^{\sigma}_{\mdp,v}[\indicator{\objective}] = \playPay_{\indicator{\objective}}(v,\sigma)$.



The second approach to quantitative objectives in MDPs, common e.g. in the operations research literature, is step-based: for each time step $i$ we compute the expected one-step reward (i.e. colour) encountered in that step and then  aggregate  these one-step expectations. Formally, the step-based payoff of $ \sigma $ from $ v $ is $ \stepPay_f(v,\sigma) = \quantObj(\expv_{v}^\sigma[\colouring(\play_0)] \expv_{v}^\sigma[\colouring(\play_1)]\cdots] ) $, where for each $ i $ we treat the expression $ \colouring(\play_i) $ as a random variable returning the colour (i.e. a number) which labels the $ i $-th edge of the randomly produced play (recall here that we index edges from $ 0 $). 

Depending on the concrete quantitative objective and on the shape of $\sigma$, the path- and step-based payoffs from a given vertex might or might not be equal. Nevertheless, in this chapter we study only objectives for which these two semantics yield the **same optimization criteria:** no matter which of the two semantics we use, the optimal values will be the same and strategy that is optimal w.r.t. one of the semantics is also optimal for the other one. Hence, we will fix the play-based approach as the default one, writing just $ \Pay_f(v,\sigma)$ instead of $ \playPay_f(v,\sigma) $. We will prove the equivalence with step-based payoff where necessary. Also, we will drop the subscript $ f $ when the payoff function is known from the context.

%qualitative objectives arising from quantitative ones. In such a case we could 

%variable $\quantObj$ surpasses a given threshold $t\in \R$, i.e. maximizing the 


%conveniently described in terms of optimizing the expected value. For a 

%variable $\indicator{\objective}$, such that $\indicator{\objective}(\play)=1$ 

%$\play\in\Omega$ and $\indicator{\objective}(\play)=0$ otherwise. Then 

%\expv^{\sigma}_{\mdp,\vinit}[\indicator{\objective}]$. Hence, we can think of 

> **Optimal strategies and decision problems**


Let us fix an MDP $\mdp$ and an objective given by a random variable 
$\quantObj$. The value of a vertex $v\in\vertices$ is the number 
$\Value(v)=\sup_{\sigma} \Pay_f(v,\sigma)$. We let $\Value(\mdp)$ denote the $|\vertices|$-dimensional vector whose component 
indexed by $v$ equals $\Value(v)$.

We say that a strategy $\sigma$ is $\eps$-optimal in $v$, for some $\eps\geq 0$, if $\Pay_f(v,\sigma) \geq \Value(v) - \eps$. A $0$-optimal strategy is simply called optimal. 

For qualitative objectives, there are additional modes of objective satisfaction. Given such an objective $\objective$, we say that a strategy $\sigma$ is almost-surely winning from $v$ if $\expv^{\sigma}_{\mdp,v}[\indicator{\objective}]=1$, i.e. if the run produced by $\sigma$ falls into $\objective$ with probability $1$. We also say that $\sigma$ is positively winning from $ v $ if $\expv^{\sigma}_{\mdp,v}[\indicator{\objective}]>0$. For strategies that are winning in the non-stochastic game sense, i.e. that **cannot** produce a run not belonging to $\objective$, are usually called surely winning to distinguish them from the above concepts. We denote by $\winPos(\mdp,\objective)$ and $\winAS(\mdp,\objective)$ the sets of all vertices of $\mdp$ from which there exists a positively or almost-surely winning strategy for the objective $\objective$, respectively.


The problems pertaining to the existence of almost-surely or positively winning strategy are often called **qualitative problems** in the MDP literature, while the notion **quantitative problems** covers the general notion of optimizing the expectation of some random variable. We do not use such a nomenclature here so as to avoid confusion with qualitative vs. quantitative objectives as defined in Chapter {ref}`1-chap:introduction`. Instead, we will refer directly to, e.g. almost-sure reachability while using the term optimal reachability to refer to the expectation-maximization problem.

%

%An algorithm which takes MDPs as inputs is said to run in **strongly polynomial time** if the number of arithmetic 

%of vertices, edges, and actions (but independent of the bit size of the 

%\end{definition}


%

