(9-chap:timed)=
# Timed Games

```{image} ./../Illustrations/9.jpg
:alt: illustration
:class: bg-primary mb-1
:width: 400px
:align: center
```

```{math}

\usepackage{amsmath}
  
\newcommand*\Realnn{\mathbb{R}_{\geq 0}}
\newcommand*\Clocks{\mathcal{C}}
\newcommand*\TA{\ensuremath{\mathcal{A}}}
\newcommand*\Locs{\mathcal{L}}
\newcommand*\Clocksz{\mathcal{C}_0}
\newcommand*\calQ{\mathcal{Q}}
\newcommand*\state{\mathsf{state}}
\newcommand*\trans{\mathsf{trans}}
\newcommand*\post{\mathsf{post}}
\newcommand*\step{\mathsf{step}}

\newcommand*\postta{\ensuremath{\textrm{\sf Post}}}
\newcommand*\preta{\ensuremath{\textrm{\sf Pre}}}
\newcommand*\unreset{\ensuremath{\textrm{\sf Unreset}}}
\newcommand*\posttime{\ensuremath{\textrm{\sf Post}_{\geq 0}}}
\newcommand*\pretime{\ensuremath{\textrm{\sf Pre}_{\geq 0}}} 
\newcommand*\reset{\mathsf{Reset}}

\def\predc{\textrm{\sf Pred}_c}
\def\predt{\textrm{\sf Pred}_{\geq 0}} 
\def\predu{\textrm{\sf Pred}_u}

\def\calP{\mathcal P}
\def\calC{\mathcal C}
\def\calT{\mathcal T}
\def\Dep{\textsf{Dep}}
\def\Wait{\textsf{Wait}}
\def\Passed{\textsf{Passed}}
\def\Act{\textsf{Act}}

\def\EA{E_{\Adam}}
\def\EE{E_{\Eve}}

\newcommand\zone[1]{\ensuremath{\left\llbracket#1\right\rrbracket}}

\def\NM#1{\textcolor{green!50!black}{\checkmark}\marginpar{\color{green!50!black}NM: #1}} 
\long\def\NMlong#1{\medskip\par{\color{green!50!black}NM: #1}\medskip\par}
\def\OS#1{\textcolor{blue!50!black}{\checkmark}\marginpar{\color{blue!50!black}OS: #1}} 
\long\def\OSlong#1{\medskip\par{\color{blue!50!black}OS: #1}\medskip\par}

\renewcommand{\Game}{\game}

```


Written by Nicolas Markey, Ocan Sankur



The ability to model real-time constraints is crucial when automata
and games are used for verification and synthesis. Timed
automata {cite}`AD94` are a model of choice for reasonning about
real-time systems: they extend finite-state automata with a
finite number of **clocks**, which are real-valued variables all
growing at the same rate, used to measure and constrain the elapse of
time between various transitions in the automaton. Because these
clocks can take arbitrary non-negative values, the set of
configurations of a timed automaton is infinite. Still, reachability
(and many other problems) remain decidable in timed
automata. The interested reader can find more background
in {cite}`AD94`, but we will try to keep our presentation self-contained.

In this chapter, we consider game models based on timed automata;
we call them **timed games** throughout this chapter. In timed
games, besides choosing which transitions should be played,
the players also decide how much time will elapse before each
transition. The elapsed time is determined using clocks, and the edges have
guards which determine clock values for which the edge can be taken.

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












