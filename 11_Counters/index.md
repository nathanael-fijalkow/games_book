(11-chap:counters)=
# Games with Counters

```{image} ./../Illustrations/11.jpg
:alt: illustration
:class: bg-primary mb-1
:width: 400px
:align: center
```

```{math}
\newcommand{\Eve}{\textrm{Eve}}
\newcommand{\Adam}{\textrm{Adam}}
```


Written by Sylvain Schmitz



%\input{sec-intro}

Just like timed games arise from timed systems and pushdown games
from pushdown systems, counter games arise from (multi-)counter
systems.  Those are finite-state systems further endowed with a
finite number of counters whose values range over the natural numbers,
and are widely used to model and reason about systems handling
discrete resources.  Such resources include for instance money on a
bank account, items on a factory line, molecules in chemical
reactions, organisms in biological ones, replicated processes in
distributed computing, etc.  As with timed or pushdown systems,
counter systems give rise to infinite graphs that can be turned into
infinite game arenas.

\AP One could populate a zoo with the many variants of counter systems,
depending on the available counter operations.  One of the best known
specimens in this zoo are Minsky machines {cite}`Minsky:1967`,
where the operations are incrementing a counter, decrementing it, or
testing whether its value is zero.  Minsky machines are a universal
model of computation: their reachability problem is undecidable,
already with only two counters.  From the algorithmic perspective we
promote in this book, this means that the counter games arising from
Minsky machines are not going to be very interesting, unless perhaps
if we restrict ourselves to a single counter.  A more promising
species in our zoo are **"vector addition systems with
  states"** {cite}`Greibach:1978,Hopcroft&Pansiot:1979`---or,
equivalently, Petri nets {cite}`Petri:1962`---, where the only
available operations are increments and decrements.  "Vector addition
systems with states" enjoy a decidable reachability
problem {cite}`Mayr:1981,Kosaraju:1982,Lambert:1992,Leroux:2011`, which
makes them a much better candidate for studying the associated games.

In this chapter, we focus on vector games, that is, on games defined
on arenas defined by vector addition systems with states with a
partition of states controlled by~\textrm{Eve} and~\textrm{Adam}  As we are going to
see in Section {ref}`11-sec:counters`, those games turn out to be undecidable
already for quite restricted objectives and just two counters.  We
then investigate two restricted classes of vector games.

1.  In Section {ref}`11-sec:dim1`, we consider **one-counter games**.  These can
  be reduced to the pushdown games of Chapter {ref}`10-chap:pushdown` and are
  therefore decidable.  Most of the section is thus devoted to proving
  sharp complexity lower bounds, already in the case of so-called
  **countdown games**.

2.  In Section {ref}`11-sec:avag`, we turn our attention to the main results of
  this chapter.  By suitably restricting both
  
  
  the systems, with an
  **asymmetry** condition that forbids \textrm{Adam} to manipulate the
  counters, and
  
  the objective, with a **monotonicity@monotonic objective**
    condition that ensures that \textrm{Eve}s winning region is "upwards
    closed"---meaning that larger counter values make it easier for
    her to win---,
  
  one obtains a class of decidable vector games where "finite
  memory" strategies are sufficient.
  
  *    This class is still rich enough to find many applications, and we
  zoom in on the connections with resource-conscious games like
  **energy** games and **bounding** games in
  Section {ref}`11-sec:resource`---a subject that will be taken further in
  Chapter {ref}`12-chap:multiobjective`.
  
  *  The computational complexity of asymmetric "monotonic@monotonic
  objective vector games" is now well-understood, and we devote
  Section {ref}`11-sec:complexity` to the topic; \cref{11-tbl:cmplx} at the end of
  the chapter summarises these results.
  


%\ifstandalone

%\tableofcontents













%\ifstandalone\addcontentsline{toc}{section}{Bibliographic Notes}\fi

