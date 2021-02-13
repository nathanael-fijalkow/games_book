(2-sec:muller)=
# Rabin, Streett, and Muller games

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
\renewcommand{\Win}{**Win**} 
\renewcommand{\Lose}{**Lose**} 
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
The prefix independent objectives we studied so far are B&uuml;chi, CoB&uuml;chi, and their joint extension the parity objectives.
The definition of the latter may seem a bit arbitrary; the study of Muller objectives will show how parity objectives naturally emerge as a well-behaved class of objectives.


Let us start with a very general class of infinitary objectives, where infinitary means that the objective only considers the set of colours appearing infinitely many times.
For a sequence $\rho$, we let $\Inf(\rho)$ denote the set of colours appearing infinitely many times in $\rho$.
The Muller objective is over the set of colours $C = [1,d]$ and is parametrised by some $\F \subseteq 2^C$, **i.e.** a family of subsets of $C$.
The objective is defined as follows:

$$
\Muller(\F) = \set{ \rho \in C^\omega : \Inf(\rho) \in \F }.
$$

Muller objectives include any objective specifying the set of colours appearing infinitely often.
There are different possible representations for a Muller objective, for instance using logical formulas or circuits.
We will here consider the most natural one which simply consists in listing the elements of $\F$.
Note that $\F$ can have size up to $2^{2^d}$, and each element of $\F$ (which is a subset of $C$)
requires up to $d$ bits to be identified, so the representation of $\F$ can be very large.

We note that the complement of a Muller objective is another Muller objective: 
$C^\omega \setminus \Muller(\F) = \Muller(2^C \setminus \F)$. 
In particular if Eve has a Muller objective then Adam also has a Muller objective.


To define subclasses of Muller objectives we make assumptions on $\F \subseteq 2^C$.
We say that $\F$ is closed under union if whenever $X,Y \in \F$ then $X \cup Y \in \F$.
Let us define Streett objectives as the subclass of Muller objectives given by $\F$ closed under union.
The following purely combinatorial lemma gives a nice characterisation of these objectives.

```{prf:lemma} needs title 2-lem:characterisation_Streett
:label: 2-lem:characterisation_Streett
:nonumber:

A collection $\F \subseteq 2^C$ is closed under union if and only if there exists a set of pairs $(R_i,G_i)_{i \in [1,d]}$
with $R_i,G_i \subseteq C$ such that $X \in \F$ is equivalent to for all $i \in [1,d]$, 
if $X \cap R_i \neq \emptyset$ then $X \cap G_i \neq \emptyset$.

```

We will see in  Section {ref}`2-sec:zielonka` a natural and optimised way to construct these pairs using the Zielonka tree.
In the meantime let us give a direct proof of this result.

```{admonition} Proof
:class: dropdown tip

Let $\F$ closed under union.
We note that for any $S \notin \F$, either no subsets of $S$ are in $\F$ or there exists a maximal subset $S'$ of $S$ in $\F$:
indeed it is the union of all subsets of $S$ in $\F$.
It directly follows that for a subset $X$ we have the following equivalence:
$X \in \F$ if and only if for any $S \notin \F$, if $X \subseteq S$ then $X \subseteq S'$.
This is rewritten equivalently as: if $X \cap (C \setminus S') \neq \emptyset$ then $X \cap (C \setminus S) \neq \emptyset$.
Hence a suitable set of pairs satisfying the required property is 
$\set{(C \setminus S', C \setminus S) : S \notin \F}$.

```

Thanks to this lemma we can give a direct alternative definition of Streett objectives.
There is a parameter $d$ controlling the number of pairs.
The set of colours is $C = \set{G_1,R_1,\dots,G_d,R_d}$ and

$$
\Streett = \set{ \rho \in C^\omega : \forall i \in [1,d],\ R_i \in \Inf(\rho) \implies G_i \in \Inf(\rho) }.
$$

It is customary to call $R_i$ the $i$\textsuperscript{th} request and $G_i$ the corresponding response;
with this terminology the Streett objective requires that every request made infinitely many times must be responded to infinitely many times.

The Rabin objectives are the complement of the Streett objectives: 

$$
\Rabin = \set{ \rho \in C^\omega : \exists i \in [1,d],\ R_i \in \Inf(\rho) \wedge G_i \notin \Inf(\rho) }.
$$



## McNaughton algorithm: an exponential time algorithm for Muller games

\input{mcnaughton}

## Positional determinacy for Rabin games

\input{positional_rabin}

## The complexity of solving Rabin games

\input{complexity_rabin}

## The complexity of solving Muller games
    
\input{complexity_muller}
