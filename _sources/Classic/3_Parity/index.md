(3-sec:index)=
# Parity

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



A possible taxonomy of algorithms for solving parity games distinguishes three families:

*  strategy improvement algorithms, which construct a sequence of improving strategies until reaching an optimal strategy. 
We will construct in  Section {ref}`3-sec:strategy_improvement` an exponential time strategy improvement algorithm.

*  attractor decomposition algorithms, which decompose a game through a sequence of attractor computations. 
The first and archetypical example is McNaughton Zielonka algorithm defined in  Section {ref}`2-sec:parity`. 
We will present in  Section {ref}`3-sec:quasipolynomial_zielonka` a quasipolynomial time algorithm improving over this algorithm.

*  value iteration algorithms, which find an optimal strategy through the computation of a value function.
An equivalent point of view on this family of algorithms is the use of separating automata for reducing parity games to safety games.
We introduce the framework of separating automata in  Section {ref}`3-sec:separation` and give a quasipolynomial time algorithm as an instanciation of it. 
We then construct value iteration algorithms through the notion of universal trees in  Section {ref}`3-sec:value_iteration`,
and present a third quasipolynomial time algorithm in the form of a value iteration algorithm.

As a conclusion  Section {ref}`3-sec:relationships` discusses the relationships between the different algorithms: in what sense are separating automata and value iteration algorithms equivalent through the notion of universal trees, and how does this family compare to the other two families of algorithms described above.

```{prf:remark} (needs title)

We already proved in  {prf:ref}`2-thm:parity` that parity games are positionally determined for both players, so in this chapter when considering a strategy we implicitly assume that it is positional.

```















