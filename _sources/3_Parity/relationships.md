(3-sec:relationships)=
# Comparing the three families of algorithms

```{math}

```

At the beginning of the chapter we described three families of algorithms: 
strategy improvement, attractor decomposition, and value iterations.

Let us first clarify the relationship between the separation framework discussed in Section {ref}`3-sec:separation`
and the value iteration paradigm presented in Section {ref}`3-sec:value_iteration`.
Both are families of algorithms: 

*  An $(n,d)$-separating automaton $\mathbf{A}$ induces an algorithm for solving parity games in time 
$O(m \cdot | \mathbf{A}|)$ where $| \mathbf{A}|$ is the size of $\mathbf{A}$, meaning the number of states.
*  An $(n,d/2)$-universal tree $T$ induces a value iteration algorithm for solving parity games in time 
proportional to $|T|$ where $|T|$ is the size of $T$, meaning the number of leaves (the exact complexity depends on the cost of computing $\delta$ in $T$, which is typically small).

These two families are in a strong sense equivalent:

````{prf:theorem} NEEDS TITLE AND LABEL 

*  An $(n,d)$-separating automaton induces an $(n,d/2)$-universal tree of the same size;
*  An $(n,d/2)$-universal tree induces an $(n,d)$-separating automaton of the same size.

*  An $(n,d)$-separating automaton induces an $(n,d/2)$-universal tree of the same size;
*  An $(n,d/2)$-universal tree induces an $(n,d)$-separating automaton of the same size.

````

We do not prove this theorem here but note that it can be stated more generally for any positionally determined objective,
replacing universal trees by the notion of universal graphs.

The main advantage of the value iteration presentation is the space complexity, which for a good choice of the universal tree
can be made very small (quasilinear).

In terms of complexity, the strategy improvement has exponential complexity, while both attractor decompositions and value iterations algorithms have quasipolynomial complexity.
Let us make a finer comparison: the complexity of the attractor decomposition algorithm is a polynomial multiplied by the (non polynomial) term

$$
\binom{\lceil \log(n) \rceil + d - 1}{\lceil \log(n) \rceil},
$$

while for the value iteration algorithm the complexity is a polynomial multiplied by the (also non polynomial) term

$$
\binom{\lceil \log(n) \rceil + d/2 - 1}{\lceil \log(n) \rceil}.
$$

The key difference is that the former performs an induction using all priorities, while the latter considers only odd priorities hence the dependence in $d/2$.
Although our presentation of the attractor decomposition algorithm does not make it explicit, 
this class of algorithms is also related to the notion of universal trees; 
however an algorithm is induced not by one $(n,d/2)$-universal tree, but by two: one for each player,
which are then interleaved to organise the recursive calls of the algorithm.

Since both value iteration and attractor decomposition algorithms are connected to the combinatorial notion of universal trees,
the next question is whether the construction given in Section {ref}`3-sec:value_iteration` is optimal.
The answer is unfortunately yes, there exists a lower bound on the size of universal trees which matches this construction up to polynomial factors.

The last question we discuss here is whether there exists a quasipolynomial strategy improvement algorithm.
In particular a natural attempt would be to use universal trees for this endeavour.
Unfortunately, this fails: {prf:ref}`3-lem:key_property` explains that for the particular choice of the lattice $Y$,
functions $\mu : V \to Y$ can be used both to certify that a graph satisfies parity or that it satisfies the complement of parity.
Both implications are used in the correctness proof of the algorithm.
This symmetric feature is lost with universal trees, which only satisfy one of the two implications, stated in {prf:ref}`3-lem:progress_measure`.
