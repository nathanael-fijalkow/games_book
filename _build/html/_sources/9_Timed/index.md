(9-chap:timed)=
# Timed Games

```{image} ./../Illustrations/9.jpg
:alt: illustration
:class: bg-primary mb-1
:width: 400px
:align: center
```

```{math}
```


Written by Nicolas Markey, Ocan Sankur



The ability to model real-time constraints is crucial when automata
and games are used for verification and synthesis. Timed
automata {cite}`AD94` are a model of choice for reasonning about
real-time systems: they~extend finite-state automata with a
finite number of **clocks**, which are real-valued variables all
growing at the same rate, used to measure and constrain the elapse of
time between various transitions in the automaton. Because these
clocks can take arbitrary non-negative values, the~set of
configurations of a timed automaton is infinite. Still, reachability
(and~many other problems) remain decidable in timed
automata. The~interested reader can find more background
in {cite}`AD94`, but we will try to keep our presentation self-contained.

In this chapter, we consider game models based on timed automata;
we~call them **timed games** throughout this chapter. In~timed
games, besides choosing which transitions should be played,
the~players also decide how much time will elapse before each
transition. The elapsed time is determined using clocks, and the edges have
guards which determine clock values for which the edge can be taken.




%which are essentially discrete systems in which time delays are

%  automata} {cite}`AD94`, which provides a convenient way of





````{prf:example} NEEDS TITLE 9-ex:intro
:label: 9-ex:intro

{numref}`9-fig:ta1` contains a timed game with clock $x$, where Eve's objective is to reach the vertex $G$.
We will define these arenas as concurrent arenas: dashed edges belong to Adam,
and plain edges to Eve. Both players can take any edge at any time as long as
the guard is satisfied. For instance, Eve's edge from $\ell_1$ to $\ell_2$ is only available if clock $x$ has value at most $1$, while Adam's edge from $\ell_1$ to $\ell_3$ is available if $x$ is less than $1$. 


```{figure} ./../FigAndAlgos/9-fig:ta1.png
:name: 9-fig:ta1
:align: center
Timed game $\TA_1$.
```

````

In the next section, we define timed games and their semantics formally.
Then we introduce some classical tools needed to reason
about the space of clock valuations, and finally present an efficient
algorithm for deciding the winner in timed games with reachability
objectives.












