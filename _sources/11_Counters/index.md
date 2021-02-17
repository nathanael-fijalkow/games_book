(11-chap:counters)=
# Games with Counters

```{image} ./../Illustrations/11.jpg
:alt: illustration
:class: bg-primary mb-1
:width: 400px
:align: center
```
```{math}
\newcommand{\?}{\mathcal}
\newcommand{\+}{\mathbb}
\newcommand{\tup}[1]{\langle #1\rangle}
\newcommand{\eqby}[1]{\stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{#1}}}}{=}}
\newcommand{\eqdef}{\eqby{def}}
\newcommand{\Loc}{\?L}
\newcommand{\Act}{A}
\providecommand{\dom}[1]{\mathrm{dom}\,#1}
\newcommand\pto{\mathrel{\ooalign{\hfil$\mapstochar\mkern5mu$\hfil\cr$\to$\cr}}}
\newcommand{\weight}{w}
\newcommand{\loc}{\ell}
\newcommand{\sink}{\bot}
\newcommand{\dd}{k}
\newcommand{\CounterReach}{\textsf{CounterReach}\xspace}
\newcommand{\Cover}{\textsf{Cover}\xspace}
\newcommand{\NonTerm}{\textsf{NonTerm}\xspace}
\newcommand{\decpb}[3][]{\begin{problem}[#1]\\[-1.7em]\begin{description}     
    \item[\textsc{input:}] {#2}
    \item[\textsc{question:}] {#3}
    \end{description}
  \end{problem}}
\newcommand{\step}[1]{\xrightarrow{\,\raisebox{-1pt}[0pt][0pt]{\scriptsize\ensuremath
      {#1}}\,}}
\newcommand{\mstep}[1]{\xrightarrow{\,\raisebox{-1pt}[6pt][0pt]{\scriptsize\ensuremath
      {#1}}\,}}
\newcommand{\inst}[1]{\mathrel{\mathtt{#1}}}
\providecommand{\pop}{\mathrm{pop}}
\providecommand{\push}[1]{\mathrm{push}(#1)}
\providecommand{\mymoot}[1]{}
\newcommand{\blank}{\Box}
\newcommand{\emkl}{\triangleright}
\newcommand{\emkr}{\triangleleft}
\renewcommand{\natural}{\arena_\+N}
\newcommand{\energy}{\arena_\+E}
\newcommand{\bounded}{\arena_B}
\newcommand{\capped}{\arena_C}
\newcommand{\capp}[2][C]{\overline{\vec #2}^{#1}}
\let\oldcite\cite
\renewcommand{\cite}{\citep}
\providecommand{\citep}{\oldcite}
\providecommand{\citet}{\cite}
\providecommand{\citem}[2][1]{#1 {cite}`#2`}
\providecommand{\qedhere}{\ensuremath\Box}
\providecommand{\col}{\mathfrak c}
\newcommand{\lcol}{\mathrm{lcol}}
\newcommand{\vcol}{\mathrm{vcol}}
\newcommand{\litt}{\loc}
\newcommand{\Effect}{\Delta}

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
model of computation; their reachability problem is undecidable,
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
partition of states controlled by~\Eve and~\Adam.  As we are going to
see in \cref{11-counters}, those games turn out to be undecidable
already for quite restricted objectives and just two counters.  We
then investigate two restricted classes of vector games.

1.  In \cref{11-dim1}, we consider **one-counter games**.  These can
  be reduced to the pushdown games of \cref{chap:pushdown} and are
  therefore decidable.  Most of the section is thus devoted to proving
  sharp complexity lower bounds, already in the case of so-called
  **countdown games**.

2.  In \cref{11-avag}, we turn our attention to the main results of
  this chapter.  By suitably restricting both
  
  
  **asymmetry** condition that forbids \Adam to manipulate the
  counters, and
  
    condition that ensures that \Eve's winning region is "upwards
    closed"---meaning that larger counter values make it easier for
    her to win---,
  
  one obtains a class of decidable vector games where "finite
  memory" strategies are sufficient.
  
  *    This class is still rich enough to find many applications, and we
  zoom in on the connections with resource-conscious games like
  **energy** games and **bounding** games in
  \cref{11-resource}---a subject that will be taken further in
  \cref{chap:multiobjective}.
  
  *    The computational complexity of asymmetric "monotonic@monotonic
  objective vector games" is now well-understood, and we devote
  \cref{11-complexity} to the topic; \cref{11-tbl-cmplx} at the end of
  the chapter summarises these results.
  


%\ifstandalone

%\tableofcontents













%\ifstandalone\addcontentsline{toc}{section}{Bibliographic Notes}\fi

