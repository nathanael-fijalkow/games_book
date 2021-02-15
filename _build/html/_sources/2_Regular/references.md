(2-sec:references)=
# Bibliographic references

```{math}
\newcommand{\F}{\mathcal{F}} 
\newcommand{\LAR}{\mathrm{LAR}}
\newcommand{\Zielonka}{\mathrm{Zielonka}}
\newcommand{\depth}{\mathrm{depth}}
\newcommand{\support}{\mathrm{supp}}
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
\renewcommand{\Win}{\textrm{Win}} 
\renewcommand{\Lose}{\textrm{Lose}} 
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

The interest in reachability objectives goes beyond automata theory and logic.
The attractor computation presented in~Section {ref}`2-sec:attractors` is inspired by the backward induction principle due to Zermelo {cite}`Zermelo:1913`, 
which was used to show that well founded games (**i.e.** where all plays are finite) are determined.
The word attractor (together with traps and subgames) first appeared in Zielonka's work 
on Muller games {cite}`Zielonka:1998`, but without the algorithmic point of view.
A naive implementation of the attractor would have a quadractic time complexity.
It is difficult to give credit for the linear time algorithm since the problem being very natural it has appeared in several contexts,
for instance in database theory as an inference algorithm by Beeri and Bernstein {cite}`Beeri&Bernstein:1979`
or in the framework of computing least fixed points over transition systems by Arnold and Crubill&eacute; {cite}`Arnold&Crubille:1988`.


The other objectives studied in this chapter are called $\omega$-regular,
let us discuss their relevance in automata theory and logic.
An important application of automata theory is to make logic effective: by translating, sometimes called compiling,
a logical formula into an equivalent automaton, we can solve problems such as satisfiability or model-checking by reducing them
to analysing automata and in particular their underlying graph structures.
In this context, the reachability objective is used for automata over finite words: 
the classical definition is that a run is accepting if the last state is accepting.
Monadic second-order logic over finite words can be effectively translated into finite automata, 
marking the beginning of a close connection between logic and automata theory.

Considering logics over infinite structures led to the study of automata over infinite structures such as words and trees.
The first objective to be studied in this context was B&uuml;chi objective, introduced by B&uuml;chi {cite}`Buchi:1962`: 
a run is accepting if it visits infinitely many times an accepting state.
Unfortunately the class of languages of infinite words recognised by deterministic B&uuml;chi automata is not closed under projection (corresponding in logic to existential quantification), said differently non-deterministic B&uuml;chi automata are strictly more expressive than deterministic ones
hence not equivalent to monadic second-order logic over infinite words.
Muller {cite}`Muller:1963` introduced the Muller objectives and attempted to prove the closure under projection for deterministic Muller automata. Alas, the proof had a flaw.
The first correct proof of the result is due to McNaughton {cite}`McNaughton:1966`.

The correspondence between monadic second-order logic and Muller automata was extended from infinite words to infinite binary trees
by Rabin {cite}`Rabin:1969`, yielding the celebrated decidability of monadic second-order logic over infinite trees.
Rabin introduced and worked with Rabin objectives; his proof is arguably very complicated and a lot of subsequent works focussed on finding the right notions and tools for better understanding his approach.
Streett {cite}`Streett:1981` suggested to use the complement of Rabin objectives, now called Streett objectives, for translating temporal logics
to Streett automata.
As discussed in~Section {ref}`1-sec:references`, a key step was made by applying determinacy results for games
to complementation results for automata.
The parity objectives appeared in this context as a (and in fact, the) subclass of Muller objectives which is positionally determined for both players.
They have been defined (with some variants) independently by several authors: Wagner {cite}`Wagner:1979`,
Mostowski {cite}`Mostowski:1984` who called them Rabin chain, 
Emerson and Jutla {cite}`Emerson&Jutla:1991` who first used the name parity, 
and McNaughton {cite}`McNaughton:1993`.
The idea can be traced back to the difference hierarchy by Hausdorff {cite}`Hausdorff:1914`.
The proof of the positionality was obtained independently by Mostowski {cite}`Mostowski:1991`, 
Emerson and Jutla {cite}`Emerson&Jutla:1991`, and McNaughton {cite}`McNaughton:1993` (the latter proof is for finite games).
Later Walukiewicz {cite}`Walukiewicz:2002` gave another very elegant proof.


McNaughton {cite}`McNaughton:1993` introduced the idea of solving Muller games by induction on the colours,
leading to McNaughton algorithm as presented in~Section {ref}`2-sec:muller`.
To some extent, the algorithms for solving B&uuml;chi, CoB&uuml;chi, and parity games are all special cases of McNaughton algorithm.

Taking a step back in time, McNaughton already proposed the **Latest Appearance Record** (LAR) discussed in~Section {ref}`2-sec:zielonka` 
for solving Muller games in his flawed attempt to solve the synthesis problem {cite}`McNaughton:1965` (see~Section {ref}`1-sec:references`).
The LAR was later used by Gurevich and Harrington {cite}`Gurevich&Harrington:1982` as memory for winning strategies in Muller games.
Thomas {cite}`Thomas:1995` showed that the LAR can be used to reduce Muller games to parity games.

Zielonka {cite}`Zielonka:1998` greatly contributed to the study of Muller objectives and their subclasses
through his illuminating analysis of Zielonka trees.
One of the many contributions of Zielonka's landmark paper {cite}`Zielonka:1998` was to follow McNaughton's approach for 
constructing a recursive algorithm for solving parity games, and show that it implies their positionality.
We follow in~Section {ref}`2-sec:parity` Zielonka's presentation of the algorithm, which is sometimes called Zielonka algorithm but more accurately 
McNaughton Zielonka algorithm.

The characterisation result showing how Zielonka tree captures the exact memory requirements of Muller objectives is due to 
Dziembowski, Jurdzi&#324;ski, and Walukiewicz {cite}`Dziembowski&Jurdzinski&Walukiewicz:1997`.


The $\NP$-completeness stated in {prf:ref}`2-thm:Rabin_complexity` for solving Rabin games is due to Emerson and Jutla {cite}`Emerson&Jutla:1988`.
The study of the complexity of solving Muller games is due to Dawar and Hunter {cite}`Hunter&Dawar:2005`.
The $\PSPACE$-completeness results stated in {prf:ref}`2-thm:complexity_Muller,2-thm:Muller_games_DAG` only concern two representations for Muller objectives. There are several others, which are not equally succinct.
For all representations but one the $\PSPACE$-completeness result holds; the only exception is the explicit representation
where the condition is specified by listing all sets of vertices in $\F$.
Surprisingly, solving Muller games with the explicit representation is in $\P$ as shown by Horn {cite}`Horn:2008`.


Our proof of positionality for Rabin objectives for {prf:ref}`2-thm:Rabin_positional_determinacy` 
and its extension to submixing objectives {prf:ref}`2-thm:submixing_positional` 
is inspired by the fairly mixing property of Gimbert and Zielonka {cite}`Gimbert&Zielonka:2004`
and the concave property of Kopczy&#324;ski {cite}`Kopczynski:2006,Kopczynski:2008`.
Gimbert and Zielonka {cite}`Gimbert&Zielonka:2005` further refined the submixing property to give a characterisation of objectives which are positionally determined for both players over finite games (they work in the more general framework of preference relations, which includes both qualitative and quantitative objectives).


```{bibliography}
:style: unsrtalpha
:filter: cited and chap == "2"
```