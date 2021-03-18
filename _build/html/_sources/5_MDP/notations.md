(5-sec:notations)=
# Notations

```{math}

\renewcommand{\Game}{\game}

```

We write vectors in boldface: $ \vec{x}, \vec{y}, $ etc. For a vector $ \vec{x} $ indexed by a set $ I $ (i.e. $ \vec{x}\in \mathbb{R}^I $) we denote by $ \vec{x}_i $ the value of the component whose index is  $i\in I  $. 

A (discrete) probability distribution over a finite or countably infinite set $A$ is a function $f \colon A \rightarrow [0,1]$ such that $\sum_{a\in A} f(a)=1$. The support of such a distribution $f$ is the set of all $a\in A$ with $f(a)>0$. A distribution $f$ is called Dirac if its support has size 1.

We denote by $\mathcal{D}(A)$ the set of all probability distributions over $A$.

We also deal with probabilities over uncountable sets of events. This is accomplished via the standard notion of a **probability space.**

````{prf:definition} Probability space
:label: 5-def:probspace

A probability space is a triple
$( S, \mathcal{F}, \mathbb{P})$ where

*  $S$ is a non-empty set of **events** (so called
**sample space**). 

*  $\mathcal{F}$ is a sigma-algebra over $S$,
i.e. a collection of subsets of $S$ that contains the empty set
$\emptyset$ and that is closed under complementation and countable unions. The members of $\mathcal{F}$ are called $\mathcal{F}$-measurable 
sets.

*  $\mathbb{P}$ is a probability measure on $\mathcal{F}$, i.e. a function
$\mathbb{P}\colon  \mathcal{F}\rightarrow[0,1]$ such that:

    1.  $\mathbb{P}(\emptyset)=0$;

    2.  for all $A\in  \mathcal{F}$ it holds $\mathbb{P}( S \setminus
A)=1- \mathbb{P}(A)$; and

    3.  for all countable sequences of pairwise disjoint sets $A_1,A_2,\dots \in  \mathcal{F}$ (i.e., $A_i \cap A_j = \emptyset$ for all $i\neq j$)
we have $\sum_{i=1}^{\infty} \mathbb{P}(A_i)= \mathbb{P}(\bigcup_{i=1}^{\infty} A_i)$.

````

A random variable in the probability space $( S, \mathcal{F}, \mathbb{P})$ is an $\mathcal{F}$-measurable function $X\colon \Omega \rightarrow  \mathbb{R} \cup
\{-\infty,\infty\}$, i.e.,
a function such that for every $a\in  \mathbb{R} \cup \{ -\infty,\infty\}$ the set
$\{\omega\in \Omega\mid  X(\omega)\leq a\}$ belongs to $\mathcal{F}$. We denote by $\mathbb{E}[ X]$ the expected value of a random variable $X$ (see Chapter 5 in {cite}`Billingsley:1995` for a formal definition).

We first give a syntactic notion of an MDP which is an analogue of the notion of an arena for games.

````{prf:definition} MDP
:label: 5-def:MDP

A Markov decision process is a tuple $( V, E, \Delta, c)$. The meaning of $V$, $E$, and $c$ is the same as for games, i.e. $V$ is a finite set of vertices, $E\subseteq  V\times V$ is a set of edges and $c\colon  E \rightarrow  C$ a mapping of edges to a set of colours. However, the meaning of $\Delta$ is now different: $\Delta$ is a partial probabilistic transition function of type $\Delta\colon  V \times  A \rightarrow  \mathcal{D}( E)$, such that the support of $\Delta(v,a)$ only contains edges outgoing from $v$.

 We usually write $\Delta(v'\mid v,a)$ as a shorthand for $\Delta(v,a)((v,v'))$, i.e. the probability of transitioning from $v$ to $v'$ under action $a$.

````

We also stipulate that for each edge $(v_1,v_2)$ there exists an action $a\in  A$ such that $\Delta(v_2\mid v_1,a)>0$. Edges not satisfying this can be always removed without changing the semantics of the MDP, which is defined below. We denote by $ p_{\min} $ the smallest non-zero edge probability in a given MDP, i.e. $ p_{\min} = \min\{x>0 \mid \exists u,v \in  V, a \in  A \text{ s.t. } x =  \Delta(v\mid u,a)\}. $

We denote by $E_c$ the set of edges coloured by $c$. Also, for MDPs where $C$ is some set of numbers, we use $\max_{ c}$ to denote the number $\max_{e\in 
 E}| c(e)|$.
In the setting of MDPs it is technically convenient to encode regular objectives (Reachability, B&uuml;chi,\dots) by colours on **vertices** as opposed to edges. Hence, when discussing these objectives, we assume that the colouring function $c$ has the type $V \rightarrow  C$.

> **Plays and strategies in MDPs**

 The way in which a play is generated in an MDP is similar to games, but now encompasses a certain degree of randomness. There is a single player, say Eve, who controls all the vertices. Eve's interaction with the world described by an MDP is probabilistic. One reason is the stochasticity of the transition function, the other is the fact that in MDP settings, it is usually permitted for Eve to use randomised strategies. Formally, a randomised strategy is a function $\sigma : E^* \to  \mathcal{D}(A)$, which to each finite play assigns a probability distribution over actions. 

 We typically shorten $\sigma( \pi)(a)$ to $\sigma(a\mid  \pi)$.

In this section, we will refer to randomised strategies simply as strategies. The strategies known from the game setting will be called  deterministic strategies. Formally, a deterministic strategy can be viewed as a special type of a randomised strategy which always selects a Dirac distribution over the edges. We shorten memoryless randomised/deterministic to MR and MD, respectively.

Now a play in an MDP is produced as follows: in each step, when the finite play produced so far (i.e. the history of the game token's movement) is $\pi$, Eve chooses an action $a$ randomly according to the distribution $\sigma( \pi)$. Then, an edge outgoing from $\textrm{last}( \pi)$ is chosen randomly according to $\Delta( \textrm{last}( \pi),a)$ and the token is pushed along the selected edge. As shown below, this intuitive process can be formalized by constructing a special probability space whose sample space consists of infinite plays in the MDP.

> **Formal semantics of MDPs**

Formally, to each MDP $\mathcal{M}$, each (Eve's) strategy $\sigma$ in $\mathcal{M}$, and 
each initial vertex $v_0$ we assign a probability space 
$( S_{ \mathcal{M}}, \mathcal{F}_{ \mathcal{M}}, \mathbb{P}^{\sigma}_{ \mathcal{M}, v_0})$. To 
explain the individual components, we need the notion of a cylinder set. A 
basic cylinder determined by a finite play $\pi$ is the set of 
all infinite plays in $\mathcal{M}$ having $\pi$ as a prefix. Now the above 
probability space consists of the following components:

*  $S_{ \mathcal{M}}$ is the set of all infinite plays in $\mathcal{M}$;
*  $\mathcal{F}_{ \mathcal{M}}$ is the **Borel** sigma-algebra over 
$\Omega_{ \mathcal{M}}$; this is the smallest sigma-algebra containing all the 
basic cylinder sets determined by finite plays in $\mathcal{M}$. The sets in 
$\mathcal{F}_{ \mathcal{M}}$ are called events. Note that the smallest sigma-algebra of the desired property is guaranteed to exist, since an intersection of an arbitrary number of sigma-algebras is again a sigma algebra.
*  $\mathbb{P}^{\sigma}_{ \mathcal{M}, v_0}$ is the unique probability measure 
arising from the **cylinder construction** detailed below. We use 
$\mathbb{E}^{\sigma}_{ \mathcal{M}, v_0}$ to denote the expectation operator 
associated to the measure $\mathbb{P}^{\sigma}_{ \mathcal{M}, v_0}$.

Since the sample space $S_{ \mathcal{M}}$ is uncountable, we construct the 
probability measure by first specifying a probability of certain simple sets of 
runs and then using an appropriate **measure-extension** theorem to extend 
the probability measure, in a unique way, to all sets in $\mathcal{F}_{ \mathcal{M}}$.
The standard cylinder construction  
proceeds as follows: for each finite play $\pi$ we define the probability 
$p( \pi)$ such that

*  for an empty play $\epsilon$ we put $p( \epsilon)=1$;
*  for a non-empty play $\pi= \pi_0\cdots  \pi_{k}$ initiated in 
$v_0$ we put

$$p( \pi) =  p( \pi_{< k})\cdot \Big(\sum_{a \in  A} 
\sigma(a\mid  \pi_{< k})\cdot  \Delta( \textrm{last}( \pi)\mid 
 \textrm{last}( \pi_{< k}),a) 
\Big), $$

where we use the convention that $\textrm{last}( \pi_{< 0})= v_0$;
*  for all other $\pi$ we have $p( \pi)=0$.

Now using an appropriate measure-extension theorem
(such as Hahn-Kol\-mo\-go\-rov theorem Corollary 2.5.4 and Proposition  2.5.7 in {cite}`Rosenthal:2006`, or Carath\'eodory theorem Theorem 1.3.10 in {cite}`Ash&Doleans-Dade:2000`) one can show that there is a 
unique probability 
measure $\mathbb{P}^{\sigma}_{ \mathcal{M}, v_0} $ on $\mathcal{F}_{ \mathcal{M}}$ such that for 
every cylinder set $\mathit{Cyl}( \pi)$ determined by some finite play $\pi$ we have $\mathbb{P}_{ v_0}^\sigma( \mathit{Cyl}( \pi))= p( \pi)$. (Abusing the notation, we write $\mathbb{P}^{\sigma}_{ \mathcal{M}, v_0}( \pi)$ for the probability of this cylinder set). There 
are some intermediate steps to be performed before an extension theorem 
can be applied, and we omit these due to space constraints. Full details on the 
cylinder construction can be found, e.g. in {cite}`Ash&Doleans-Dade:2000,Novotny:2015`.

While the construction of the probability measure 
$\mathbb{P}^{\sigma}_{ \mathcal{M}, v_0}$ might seem a bit esoteric, in the context of 
MDP verification we do not usually need to be concerned with all the delicacies 
behind the associated probability space. The sets of plays that we work with 
typically arise from the basic cylinder sets by means of countable unions, 
intersections, and simple combinations thereof; such sets by definition belong 
to the 
sigma-algebra $\mathcal{F}_{ \mathcal{M}}$, and their probabilities can be inferred using 
basic probabilistic reasoning. Nevertheless, one should keep in mind that all the 
probabilistic argumentation rests on solid formal grounds.

In the standard MDP literature {cite}`Puterman:2005`, the plays are often defined as alternating sequence of vertices and actions. Here we stick to the edge-based definition inherited from deterministic games. Still, we would sometimes like to speak about quantities such as probability that action $a$ is taken in step $i$. To this end, we introduce, for each strategy $\sigma$, each action $a$,  and each $i\geq 0$,  a random variable $\actevent{\sigma}{a}{i}$ such that $\actevent{\sigma}{a}{i}( \pi)=\sigma( \pi_{< i})(a)$. It is easy to check that  $\mathbb{E}^\sigma_v[\actevent{\sigma}{a}{i}]$ is the probability that action $a$ is played in step $i$ when using strategy $\sigma$.

> **Objectives in MDPs**

Similarly to plays, the notions of both qualitative and quantitative objectives 
are inherited from the non-stochastic world of games. However, since plays in 
MDPs are generated stochastically, even for a fixed strategy $\sigma$ there is 
typically no single infinite play that would constitute the outcome of 
$\sigma$. A concrete $\sigma$ might yield different outcomes, depending on the 
results of random events during the interaction with the MDP. Hence, we need a 
more general way of evaluating strategies in MDPs. 

In the game setting, a qualitative objective was given as a set $\Omega
\subseteq  C^{\omega}$. In the MDP setting, we require that such 
$\Omega$ is measurable in the sense that the set $c^{-1}( \Omega) = \{ \pi \in  S_{ \mathcal{M}}  \mathcal{M}  c( \pi) \in  \Omega \}$ belongs to $\mathcal{F}_{ \mathcal{M}}$. We can then talk about a 
probability that the produced play falls satisfies $\Omega$. For instance, for a 
colour $c$ the objective $  \mathtt{Reach}( c) $ is indeed measurable, since $  c^{-1}( \Omega) $ can be written as a countable union of all basic cylinders that are determined by finite plays ending in a vertex coloured by $  c $. Indeed, all the qualitative objectives studied in previous chapters can be shown measurable in a similar way, and we encourage the reader to prove this as an exercise.
Hence, the expression 
$\mathbb{P}^{\sigma}_{ \mathcal{M}, v_0}( \mathtt{Reach}( c))$ 
denotes the probability that a vertex of colour $c$ is reached when 
using 
strategy $\sigma$ from vertex $v_0$. 
In line with previous conventions, we 
stipulate that Eve aims to maximize this probability. 

The situation is more complex for quantitative objectives. As shown in the previous chapter, 
when working with quantitative objectives, the set of colours $C$ is typically the set of real numbers (or a subset thereof), and the quantitative objective is given by an aggregating function $f\colon  C^\omega \rightarrow  \mathbb{R}$, which can be extended into a function $\bar{ f}\colon  E^\omega \rightarrow  \mathbb{R} $ by putting $  \bar{ f}( \pi) =  f(  c( \pi_0) c( \pi_1)\cdots) $.

In the MDP setting, we 
require that $\bar{ f}$ is $\mathcal{F}_{ \mathcal{M}}$-measurable, which 
means that for each $x\in  \mathbb{R}$ the set $\{\pi\in  E^\omega\mid 
 f( c( \pi_0) c( \pi_1)\cdots) \leq x\}$ belongs to 
$\mathcal{F}_{ \mathcal{M}}$ (again this holds for all the objectives studied 
in the previous chapters). Then there are two ways in which we can define the expected payoff achieved by strategy $ \sigma $ from a vertex $ v $.
First, we can treat 
$\bar{ f}$ as a random variable 
in the probability space 
$( S_{ \mathcal{M}}, \mathcal{F}_{ \mathcal{M}}, \mathbb{P}^{\sigma}_{ \mathcal{M},v})$. Then the play-based payoff of $\sigma$ from $ v $, which we denote by $  \textsf{p-Payoff}_f(v,\sigma) $, is the expected value of this random variable, i.e. $  \textsf{p-Payoff}_f(v,\sigma) =  \mathbb{E}_{v}^\sigma [ \bar{ f}] $. That is, we compute the expected payoff over all plays. This approach subsumes also qualitative objectives: For such an objective $\Omega$ we can consider an indicator random 
variable $\mathbf{1}_{ \Omega}$, such that $\mathbf{1}_{ \Omega}( \pi)=1$ 
of 
$\pi\in\Omega$ and $\mathbf{1}_{ \Omega}( \pi)=0$ otherwise. Then 
$\mathbb{P}^{\sigma}_{ \mathcal{M},v}( \Omega) = 
 \mathbb{E}^{\sigma}_{ \mathcal{M},v}[ \mathbf{1}_{ \Omega}] =  \textsf{p-Payoff}_{ \mathbf{1}_{ \Omega}}(v,\sigma)$.

The second approach to quantitative objectives in MDPs, common e.g. in the operations research literature, is step-based: for each time step $i$ we compute the expected one-step reward (i.e. colour) encountered in that step and then  aggregate  these one-step expectations. Formally, the step-based payoff of $ \sigma $ from $ v $ is $  \textsf{s-Payoff}_f(v,\sigma) =  f( \mathbb{E}_{v}^\sigma[ c( \pi_0)]  \mathbb{E}_{v}^\sigma[ c( \pi_1)]\cdots] ) $, where for each $ i $ we treat the expression $  c( \pi_i) $ as a random variable returning the colour (i.e. a number) which labels the $ i $-th edge of the randomly produced play (recall here that we index edges from $ 0 $).

Depending on the concrete quantitative objective and on the shape of $\sigma$, the path- and step-based payoffs from a given vertex might or might not be equal. Nevertheless, in this chapter we study only objectives for which these two semantics yield the **same optimization criteria:** no matter which of the two semantics we use, the optimal values will be the same and strategy that is optimal w.r.t. one of the semantics is also optimal for the other one. Hence, we will fix the play-based approach as the default one, writing just $  \textsf{Payoff}_f(v,\sigma)$ instead of $  \textsf{p-Payoff}_f(v,\sigma) $. We will prove the equivalence with step-based payoff where necessary. Also, we will drop the subscript $ f $ when the payoff function is known from the context.

> **Optimal strategies and decision problems**

Let us fix an MDP $\mathcal{M}$ and an objective given by a random variable 
$f$. The value of a vertex $v\in V$ is the number 
$\textrm{val}(v)=\sup_{\sigma}  \textsf{Payoff}_f(v,\sigma)$. We let $\textrm{val}( \mathcal{M})$ denote the $| V|$-dimensional vector whose component 
indexed by $v$ equals $\textrm{val}(v)$.

We say that a strategy $\sigma$ is $\varepsilon$-optimal in $v$, for some $\varepsilon\geq 0$, if $\textsf{Payoff}_f(v,\sigma) \geq  \textrm{val}(v) -  \varepsilon$. A $0$-optimal strategy is simply called optimal. 

For qualitative objectives, there are additional modes of objective satisfaction. Given such an objective $\Omega$, we say that a strategy $\sigma$ is almost-surely winning from $v$ if $\mathbb{E}^{\sigma}_{ \mathcal{M},v}[ \mathbf{1}_{ \Omega}]=1$, i.e. if the run produced by $\sigma$ falls into $\Omega$ with probability $1$. We also say that $\sigma$ is positively winning from $ v $ if $\mathbb{E}^{\sigma}_{ \mathcal{M},v}[ \mathbf{1}_{ \Omega}]>0$. For strategies that are winning in the non-stochastic game sense, i.e. that **cannot** produce a run not belonging to $\Omega$, are usually called surely winning to distinguish them from the above concepts. We denote by $W_{>0}( \mathcal{M}, \Omega)$ and $W_{=1}( \mathcal{M}, \Omega)$ the sets of all vertices of $\mathcal{M}$ from which there exists a positively or almost-surely winning strategy for the objective $\Omega$, respectively.

The problems pertaining to the existence of almost-surely or positively winning strategy are often called **qualitative problems** in the MDP literature, while the notion **quantitative problems** covers the general notion of optimizing the expectation of some random variable. We do not use such a nomenclature here so as to avoid confusion with qualitative vs. quantitative objectives as defined in Chapter {ref}`1-chap:introduction`. Instead, we will refer directly to, e.g. almost-sure reachability while using the term optimal reachability to refer to the expectation-maximization problem.

