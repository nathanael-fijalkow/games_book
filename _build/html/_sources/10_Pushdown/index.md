(10-chap:pushdown)=
# Pushdown Games

```{image} ./../Illustrations/10.jpg
:alt: illustration
:class: bg-primary mb-1
:width: 400px
:align: center
```

```{math}

\def\AC#1{\textcolor{green!50!black}{\checkmark}\marginpar{\color{green!50!black}AC: #1}} 

\def\acchanged#1{{#1}}
\def\OS#1{\textcolor{red}{\checkmark}\marginpar{\color{red}OS: #1}}

\renewcommand{\qed}{$\square$}

\newcommand {\Stepsg}[1]{\ensuremath{\mathit{Steps}_{#1}}}

\newcommand {\Rounds}[1]{\ensuremath{\mathit{Rounds}_{#1}}}

\renewcommand{\Game}{\game}

```


Written by Arnaud Carayol, Olivier Serre



This chapter studies two-player games whose arena is defined by a pushdown system.

```{margin}
We use here the term pushdown system rather than pushdown automaton to stress the fact that we are not considering these devices as language acceptors but rather focus on the transitions systems they define.
```

 The vertices of the arena are the configurations of the pushdown system (i.e., pairs composed of a control state and a word representing the content of the stack) and the edges of the arena are defined by the pushdown system's transitions. For simplicity, both the ownership of a configuration and the objective will only depend on the control state of the configuration. Hence the partition of all the configurations between the two players will simply be given by a partition the control states. We will mainly consider the parity objective. Via a standard reduction\AC{Insert a reference to a previous chapter.}, parity pushdown game can be used to solve any pushdown game with an $\omega$-regular objectives (which in our setting is simply an $\omega$-regular set of infinite words over  the alphabet of control states). 

The main conceptual novelty of this chapter is that the arena is no longer finite. However as these games are described by a finite amount of information: the pushdown system, the ownership partition and the $\omega$-regular objective, they are amenable to algorithmic treatment. The first natural problem in this line is to decide the winner of the game from a given configuration. We will also consider the computation of **finite representations** for the winning regions and the winning strategies.









