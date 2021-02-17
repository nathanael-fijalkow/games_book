(1-sec:computation)=
# Computational models

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

## The Random Access Machine model of computation

For complexity statements we consider the classical Turing model of computation.
However for algorithmic results the Turing model is a bit painful and unnatural hence it is customary to use the Random Access Machine (RAM) model instead.
Intuitively this corresponds to using a standard imperative programming language on a usual computer which can create, access, and update variables.
There are variants of the RAM model; to be specific the one we use and describe here is called word RAM.
The main reason to use the RAM model is to make our life easier by hiding some small computational costs which are inessential for our purposes.


The memory is arranged in machine words whose size is a parameter $w$ to be fixed depending on the problem.
A machine word is a register which stores some information as a binary word of length $w$.
The first key assumption of the RAM model is that **memory can be accessed in constant time**.
In other words, machine words are registers with a unique address and can be accessed either directly or indirectly.
A concrete implication is that checking whether an element belongs to a set is a single operation (if each element of the set can be stored in a single machine word).


We consider an (often implicit) set of basic operations operating on a constant number of machine words; 
addition, multiplication, subtraction, division, and comparison of integers are typical examples.
The second key assumption is the unit cost model, it says that the time complexity (also called cost) of basic operations is constant.
This convention implies that we can manipulate counters for small numbers with no additional complexity, this will be useful in many situations.

We note that this is unrealistic as it means that for instance we can compute the number $2^{2^n}$ by repeatedly squaring $2$: the complexity is $O(n)$ but this number uses $O(2^n)$ bits hence cannot be generated in polynomial time using a Turing machine.
We will not make use of such weaknesses in our algorithms.


The size of an input is the number of machine words required to store it.
The most common choice for the machine word size is $w = \log(s)$ where $s$ is the size of the input as we want to at least be able to store an integer $x$ of order $s$ in one machine word.
However in situations in which there are numerical inputs, it is reasonable to assume that each input number fits into one machine word,
leading to a potentially larger $w$.
Note that an algorithm in the word RAM model with machine word size $w$ is allowed to use numbers that are larger than $2^w$, but such numbers should be split among several machine words.


The time complexity is the number of steps performed by the machine, as a function of the input size, 
and the space complexity is the maximal number of machine words used throughout the computation.

## Games representations in the RAM model
The important parameters for algorithms on games are $n$ the number of vertices and $m$ the number of edges.
Note that our assumption that every vertex has an outgoing edge implies that $n \le m$.

The machine word size is always at least $w = \log(m)$, so that both a vertex and an edge can be stored in one machine word.
A graph is given by the list of vertices and the list of edges, which implies that its size is $O(n + m) = O(m)$.
An algorithm can go through all vertices, all edges, or all successors or predecessors of a given vertex, 
with no additional cost for the space complexity.

An arena additionally specifies for each vertex which player controls the vertex, which is a boolean value also stored in one machine word.
The representation of conditions and colouring functions is different for each and is discussed when introducing them.

## Polynomial versus strongly polynomial time algorithms

Let us consider a computational problem in which the input consists of a sequence of $N$ integers plus a number $n$ of other input bits.
We write $L$ for the total number of bits needed to encode the input integer numbers. 
We say that an algorithm runs in strongly polynomial time if: 

*  the number of arithmetic operations is bounded by a polynomial in the number of integers $N$ in the input instance; and
*  the space used by the algorithm is bounded by a polynomial in the size $L + n$ of the input.

An equivalent definition using the unit cost word RAM model is that the algorithm uses machine word size $w = L + \log(n)$
and runs in polynomial time.

## Linear programming

We give here only the very essential definitions and results related to linear programming,
and refer to {cite}`Bertsimas&Tsitsiklis:1997` for a reference book on the topic.

A linear program (in canonical form) uses a set of real variables organised in a vector $x$ and is defined by

$$
\begin{array}{l}
\text{maximise } c^T x \text{ subject to } \\
A x \le b \text{ and } x \ge 0,
\end{array}
$$

where $c$ and $b$ are rational vectors (with $c^T$ the transpose of $c$) and $A$ is a rational matrix. 
More explicitly: 

$$
\begin{array}{l}
\text{maximise } \sum_{j = 1}^n c_j x_j \text{ subject to } \\
\forall i \in [1,m],\ \sum_{j = 1}^n A_{i,j} x_j \le b_i \\
\forall j \in [1,n],\ x_j \ge 0.
\end{array}
$$

Solving a linear program is finding an optimal assignment $x^*$ of the variables.

````{prf:theorem} Linear programming
:label: 1-thm:linear_programming

There exists a polynomial time algorithm for solving linear programs.

````

We define here linear programs with a maximising objective. 
The same problem with minimising $c^T x$ can be easily shown to be equivalent.

The statement above says that there exists a weakly polynomial time algorithm; whether there exists a strongly polynomial algorithm for linear programming is a long standing open question.

