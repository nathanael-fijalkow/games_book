(10-chap:pushdown)=
# Pushdown Games

```{image} ./../Illustrations/10.jpg
:alt: illustration
:class: bg-primary mb-1
:width: 400px
:align: center
```

```{math}
```


Written by Arnaud Carayol, Olivier Serre



This chapter studies two-player games whose arena is defined by a pushdown system.

```{margin}
We use here the term pushdown system rather than pushdown automaton to stress the fact that we are not considering these devices as language acceptors but rather focus on the transitions systems they define.
```

 The vertices of the arena are the configurations of the pushdown system (i.e., pairs composed of a control state and a word representing the content of the stack) and the edges of the arena are defined by the pushdown system's transitions. For simplicity, both the ownership of a configuration and the objective will only depend on the control state of the configuration. Hence the partition of all the configurations between the two players will simply be given by a partition the control states. We will mainly consider the parity objective. Via a standard reduction\AC{Insert a reference to a previous chapter.}, parity pushdown game can be used to solve any pushdown game with an $\omega$-regular objectives (which in our setting is simply an $\omega$-regular set of infinite words over  the alphabet of control states). 

The main conceptual novelty of this chapter is that the arena is no longer finite. However as these games are described by a finite amount of information: the pushdown system, the ownership partition and the $\omega$-regular objective, they are amenable to algorithmic treatment. The first natural problem in this line is to decide the winner of the game from a given configuration. We will also consider the computation of **finite representations** for the winning regions and the winning strategies. 









%

%
## Lower Bound

%Here we show that even for reachability condition the problem is hard for exponential time. We give the proof of Walukiewicz that reduces from the acceptance problem for linear-space alternating Turing machine.

% Hardness for PSPACE when using a counter instead of a general stack (proof ?)

%
## Alternative Approaches

%Connection the full binary tree. Again regularity of the winning region plus the existence of regular positional strategies with Rabin's lemma. 

%

%

%

%

%\section{Beyond Parity Pushdown Games}

%
## Beyond Parity Condition

%Here we present the unboundedness winning condition (mention topological complexity?) and we argue how it can be decided in the same way as parity. Discuss also existing extensions where it is mixed with parity.

%
## Beyond Pushdown Games

%Here we introduce/discuss (depending space) higher-order pushdown automata. We mainly describe the results and also their implications (wrt logic, program verification). Just a discussion probably not the time.

%

