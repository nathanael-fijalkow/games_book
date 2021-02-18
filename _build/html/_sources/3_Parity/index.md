(3-chap:parity)=
# Parity Games

```{image} ./../Illustrations/3.jpg
:alt: illustration
:class: bg-primary mb-1
:width: 400px
:align: center
```

```{math}
```


Written by John Fearnley, Nathana&euml;l Fijalkow



A possible taxonomy of algorithms for solving parity games distinguishes three families:

*  strategy improvement algorithms, which construct a sequence of improving strategies until reaching an optimal strategy. 
We will construct in Section {ref}`3-sec:strategy_improvement` an exponential time strategy improvement algorithm.

*  attractor decomposition algorithms, which decompose a game through a sequence of attractor computations. 
The first and archetypical example is McNaughton Zielonka algorithm defined in Section {ref}`2-sec:parity`. 
We will present in Section {ref}`3-sec:zielonka` a quasipolynomial time algorithm improving over this algorithm.

*  value iteration algorithms, which find an optimal strategy through the computation of a value function.
An equivalent point of view on this family of algorithms is the use of separating automata for reducing parity games to safety games.
We introduce the framework of separating automata in Section {ref}`3-sec:separation` and give a quasipolynomial time algorithm as an instanciation of it. 
We then construct value iteration algorithms through the notion of universal trees in Section {ref}`3-sec:value_iteration`,
and present a third quasipolynomial time algorithm in the form of a value iteration algorithm.

As a conclusion Section {ref}`3-sec:relationships` discusses the relationships between the different algorithms: in what sense are separating automata and value iteration algorithms equivalent through the notion of universal trees, and how does this family compare to the other two families of algorithms described above.

````{admonition} Remark 
We already proved in  {prf:ref}`2-thm:parity` that parity games are positionally determined for both players, so in this chapter when considering a strategy we implicitly assume that it is positional.

````


%
%



%
%



%
%



%
%



%
%



%
%




