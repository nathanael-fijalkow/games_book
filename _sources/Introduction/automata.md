(1-sec:automata)=
# Automata

```{math}
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
\newcommand{\argmax}{\text{argmax}}
\newcommand{\argmin}{\text{argmin}}
\newcommand{\Op}{\mathbb{O}}
\newcommand{\Prob}{\mathbb{P}} \newcommand{\dist}{\mathcal{D}} \newcommand{\Dist}{\dist} \newcommand{\supp}{\text{supp}} 
\newcommand{\game}{\mathcal{G}} \renewcommand{\Game}{\game} \newcommand{\arena}{\mathcal{A}} \newcommand{\Arena}{\arena} 
\newcommand{\col}{\textsf{col}} \newcommand{\Col}{\col} 
\newcommand{\mEve}{\mathrm{Eve}}
\newcommand{\mAdam}{\mathrm{Adam}}
\newcommand{\mRandom}{\mathrm{Random}}
\newcommand{\vertices}{V} \newcommand{\VE}{V_\mEve} \newcommand{\VA}{V_\mAdam} \newcommand{\VR}{V_\mRandom} 
\newcommand{\ing}{\text{In}}
\newcommand{\Ing}{\ing}
\newcommand{\out}{\text{Out}}
\newcommand{\Out}{\out}
\newcommand{\dest}{\Delta} 
\newcommand{\WE}{W_\mEve} \newcommand{\WA}{W_\mAdam} 
\newcommand{\Paths}{\text{Paths}} \newcommand{\play}{\pi} \newcommand{\first}{\text{first}} \newcommand{\last}{\text{last}} 
\newcommand{\mem}{\mathcal{M}} \newcommand{\Mem}{\mem} 
\newcommand{\Pre}{\text{Pre}} \newcommand{\PreE}{\text{Pre}_\mEve} \newcommand{\PreA}{\text{Pre}_\mAdam} \newcommand{\Attr}{\text{Attr}} \newcommand{\AttrE}{\text{Attr}_\mEve} \newcommand{\AttrA}{\text{Attr}_\mAdam} \newcommand{\rank}{\text{rank}}
\renewcommand{\Win}{\textsc{Win}} 
\renewcommand{\Lose}{\textsc{Lose}} 
\newcommand{\Value}{\text{val}} 
\newcommand{\ValueE}{\text{val}_\mEve} 
\newcommand{\ValueA}{\text{val}_\mAdam}
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
```
The study of games is deeply intertwined with automata over infinite words and trees.
We will not elaborate much on that aspect in this book, but in a few places we will use automata.
We define here (non-deterministic) automata over infinite words, and refer to {cite}`Thomas:1997`
for a survey on automata theory over infinite objects (words and trees) and logic.

```{prf:definition} Automata
Let $\Sigma$ be an alphabet.
An automaton over the alphabet $\Sigma$ is a tuple $\Automaton = (Q,q_0,\Delta,A)$ where:

*  $Q$ is a finite set of states,

*  $q_0 \in Q$ is the initial state,

*  $\Delta \subseteq Q \times \Sigma \times Q$ is the transition relation,

*  $A \subseteq \Delta^\omega$ is the acceptance condition.

```

We assume that automata are complete: from any state $q$ and letter $a$,
there exists a transition $(q,a,q') \in \Delta$. 
This mirrors the convention for games that every vertex has an outgoing edge.

There is one difference at the syntactic level between games and automata: 
in games the condition is defined over sequences of vertices, 
while in automata the acceptance condition is defined over sequences of transitions (which contain more information than states).
In other words for automata we use transition based acceptance conditions instead of state based acceptance conditions.
This more succinct definition of automata naturally composes with games in the same way as the state based acceptance definition does,
see Section {ref}`1-sec:reductions`, and sometimes yields smaller automata, see Section {ref}`2-sec:zielonka`


For a (finite or infinite) word $w = w_0 w_1 \dots$, a run $\rho = (q_0,w_0,q_1)(q_1,w_1,q_2) \dots$ over $w$ is a sequence of consecutive transitions starting from the initial state $q_0$.
An infinite run is accepting if it belongs to $A$, in which case we also say that it satisfies $A$.
A word $w$ is accepted if there exists an accepting run over $w$. 
We let $L(\Automaton)$ denote the set of accepted words and call it the language defined by $\Automaton$,
or sometimes recognised by $\Automaton$.


An automaton is deterministic if for all states $q \in Q$ and letter $a \in \Sigma$, there exists at most one transition $(q,a,q') \in \Delta$.
In that case the transition relation becomes a transition function $\delta : Q \times \Sigma \to Q$.
The key property of deterministic automata is that for every word there exists exactly one run over it.


We use the same approach as for games for defining classes of automata with the same conditions:
an objective $\Omega \subseteq C^\omega$ and a colouring function $\col : \Delta \to C$ 
induce an acceptance condition $\Omega[\col] \subseteq \Delta^\omega$.
For deterministic automata the colouring function becomes $\col : Q \times \Sigma \to C$.
As for games the objective qualifies the automaton, so we speak of a parity automaton if it uses a parity objective.

```{prf:theorem} (needs title)

Non-deterministic B&uuml;chi, CoB&uuml;chi, parity, and deterministic parity automata define the same class of languages called $\omega$-regular languages.

```

