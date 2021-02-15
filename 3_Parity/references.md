(3-sec:references)=
# Bibliographic references

```{math}
\renewcommand{\H}{\mathcal{H}} 
\newcommand{\Lift}{\textrm{Lift}} 
\newcommand{\F}{\mathcal{F}} 
\newcommand{\sinit}{\sigma_{\textnormal{init}}}
\newcommand{\siblank}{\mathtt{-}}
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
```
We refer to Section {ref}`2-sec:references` for the role of parity objectives and how they emerged in automata theory as a subclass of Muller objectives.
Another related motivation comes from the works of Emerson, Jutla, and Sistla {cite}`Emerson&Jutla&Sistla:1993`,
who showed that solving parity games is linear-time equivalent to the model-checking problem for modal $\mu$-calculus.
This logical formalism is an established tool in program verification, and a common denominator to a wide range of modal, temporal and fixpoint logics used in various fields.


Let us discuss the progress obtained over the years for each of the three families of algorithms.


**Value iteration algorithms and separating automata**.
The heart of value iteration algorithms is the value function, which in the context of parity games and related developments for automata
have been studied under the name progress measures or signatures.
They appear naturally in the context of fixed point computations so it is hard to determine who first introduced them.
Streett and Emerson {cite}`Streett&Emerson:1984,Streett&Emerson:1989` defined signatures for the study of the modal $\mu$-calculus,
and Stirling and Walker {cite}`Stirling&Walker:1989` later developped the notion.
Both the proofs of Emerson and Jutla {cite}`Emerson&Jutla:1991` and of Walukiewicz {cite}`Walukiewicz:1996` use signatures to show the positionality of parity games over infinite games.

Jurdzi&#324;ski {cite}`Jurdzinski:2000` used this notion to give the first value iteration algorithm for parity games, 
with running time $O(m n^{d/2})$.
The algorithm is called small progress measures and is an instance of the class of value iteration algorithms we construct 
in Section {ref}`3-sec:value_iteration` by considering the universal tree of size $n^h$.
Bernet, Janin, and Walukiewicz {cite}`Bernet&Janin&Walukiewicz:2002` investigated reductions from parity games to safety games
through the notion of permissive strategies, and constructed a separating automaton

```{margin}
We note that the general framework of separating automata came later, introduced by Boja{\'n```

czyk and Czerwi&#324;ski {cite}`Bojanczyk&Czerwinski:2018`.} corresponding to the universal tree of size $n^h$.

The new era for parity games started in 2017 when Calude, Jain, Khoussainov, Li, and Stephan {cite}`Calude&Jain&al:2017` constructed a quasipolynomial time algorithm. 
Our presentation follows the technical developments of the subsequent paper by Fearnley, Jain, Schewe, Stephan, and Wojtczak {cite}`Fearnley&Jain&al:2017` which recasts the algorithm as a value iteration algorithm.
Boja&#324;czyk and Czerwi&#324;ski {cite}`Bojanczyk&Czerwinski:2018` introduce the separation framework to better understand the original algorithm.

Soon after two other quasipolynomial time algorithms emerged.
Jurdzi&#324;ski and Lazi{\'c} {cite}`Jurdzinski&Lazic:2017` showed that the small progress measure algorithm can be adapted to a succinct progress measure algorithm, matching (and slightly improving) the quasipolynomial time complexity.
The presentation using universal tree that we follow in Section {ref}`3-sec:value_iteration` and an almost matching lower bound on their sizes is due to Fijalkow {cite}`Fijalkow:2018`.
The connection between separating automata and universal trees was shown by Czerwi&#324;ski, Daviaud, Fijalkow, Jurdzi&#324;ski, Lazi{\'c}, and Parys {cite}`Czerwinski&Daviaud&al:2018`. 

The third quasipolynomial time algorithm is due to Lehtinen {cite}`Lehtinen:2018`.
The original algorithm has a slightly worse complexity ($n^{O(\log(n))}$ instead of $n^{O(\log(d))}$),
but Parys {cite}`Parys:2020` later improved the construction to (essentially) match the complexity of the previous two algorithms.
Although not explicitly, the algorithm constructs an automaton with similar properties as a separating automaton,
but the automaton is non-deterministic.
Colcombet and Fijalkow {cite}`Colcombet&Fijalkow:2019` revisited the link between separating automata and universal trees
and proposed the notion of good for small games automata, capturing the automaton defined by Lehtinen's algorithm.
The equivalence result between separating automata, good for small games automata, and universal graphs, holds for any positionally determined objective, giving a strong theoretical foundation for the family of value iteration algorithms.


**Attractor decomposition algorithms**.
The McNaughton Zielonka's algorithm has complexity $O(m n^d)$.
Parys {cite}`Parys:2019` constructed the fourth quasipolynomial time algorithm as an improved take over McNaughton Zielonka's algorithm.
As for Lehtinen's algorithm, the original algorithm has a slightly worse complexity ($n^{O(\log(n))}$ instead of $n^{O(\log(d))}$).
Lehtinen, Schewe, and Wojtczak {cite}`Lehtinen&Schewe&Wojtczak:2019` later improved the construction.
As discussed in Section {ref}`3-sec:relationships` the complexity of this algorithm is quasipolynomial and of the form $n^{O(\log(d))}$,
but a bit worse than the three previous algorithms since the algorithm is symmetric and has a recursion depth of $d$,
while the value iteration algorithms only consider odd priorities hence replace $d$ by $d/2$.

Jurdzi&#324;ski and Morvan {cite}`Jurdzinksi&Morvan:2020` constructed a generic McNaughton Zielonka's algorithm parameterised by the choice of two universal trees, one for each player.
\mynote{CONTINUE}



**Strategy improvement algorithms**.
As we will see in Chapter {ref}`4-chap:payoff`, parity games can be reduced to mean payoff games,
so any algorithm for solving mean payoff games can be used for solving parity games.
In particular, the existing strategy improvement algorithm for mean payoff games can be run on parity games. 
V{\"o}ge and Jurdzin&#324;ski {cite}`Voge&Jurdzinski:2000` introduced the first discrete strategy improvement for parity games,
running in exponential time.
For some time there was some hope that the strategy improvement algorithm, for some well chosen policy on switching edges,
solves parity games in polynomial time.
Friedmann {cite}`Friedmann:2011` cast some serious doubts by constructing numerous exponential lower bounds applying to different variants of the algorithm.
Fearnley {cite}`Fearnley:2017` investigated efficient implementations of the algorithm, focussing on the cost of computing and updating the value function for a given strategy.
Our proof of correctness is original. \mynote{SAY MORE?}

The complexity was reduced to subexponential with randomised algorithms 
by Jurdzin&#324;ski, Paterson, and Zwick {cite}`Jurdzinski&Paterson&Zwick:2008`.
A natural question is whether there exists a quasipolynomial strategy improvement algorithm; 
as discussed in Section {ref}`3-sec:relationships` the notion of universal trees cannot be used to achieve this,
and the question remains to this day open.


```{bibliography}
:style: unsrtalpha
:filter: cited and chap == "3"
```