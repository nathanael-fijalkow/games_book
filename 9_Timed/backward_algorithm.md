(9-sec:backward_algorithm)=
# Backward Algorithm

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
\newcommand*\pretime{\ensuremath{\textrm{\sf Pre}_{\geq 0}}} \newcommand*\reset{\mathsf{Reset}}
\newcommand{\sem}[1]{\ensuremath{#1}}
\newcommand{\size}[1]{\ensuremath{|#1|}}

\def\predc{\textrm{\sf Pred}_c}
\def\predt{\textrm{\sf Pred}_{\geq 0}} \def\predu{\textrm{\sf Pred}_u}
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
Given the DBM data structure we presented,
a backward fixpoint algorithm follows for computing the winning configurations in a timed game:

````{prf:theorem} NEEDS TITLE AND LABEL 
   \label{9-thm:timed-control}
   For any timed game $\TA$ and target set $G \subseteq \VE$, 
   the~limit $\lim_{k \rightarrow \infty} \pi^k(G)$ exists, and is reached 
   in a finite number of steps. This limit is precisely the set of states from
   which the controller has a winning strategy for reaching $G$.
 

   \label{9-thm:timed-control}
   For any timed game $\TA$ and target set $G \subseteq \VE$, 
   the~limit $\lim_{k \rightarrow \infty} \pi^k(G)$ exists, and is reached 
   in a finite number of steps. This limit is precisely the set of states from
   which the controller has a winning strategy for reaching $G$.

````


````{admonition} Proof
:class: dropdown tip
[Sketch]

  We~briefly explain why the fixpoint computation terminates and refer
  to {cite}`AMPS98,CDFLL05` for more details.  The~proof relies on the notion of
  **regions**. Intuitively, regions are minimal zones, not
  containing any other zone. More precisely, writing $K$ for the maximal
  (absolute) integer constant appearing in the timed game, the~set of regions is
  the set of zones associated with
  DBMs $(\mathord\prec_{i,j},M_{i,j})$ such that
  
  
  *  $M_{i,j}\in [-K; K]\cup\{-\infty;+\infty\}$ for all $i$ and $j$;
  *  for all $i\not=j$,
     \begin{itemize}
    *  either $M_{i,j}=-M_{j,i}$ and
      $\mathord\prec_{i,j}=\mathord\prec_{j,i}=\mathord\leq$,
     *  or $|M_{i,j}+M_{j,i}|=1$ and 
      $\mathord\prec_{i,j}=\mathord\prec_{j,i}=\mathord<$,
    *  or $(\prec_{i,j},M_{i,j})=(<,+\infty)$ and $(\prec_{j,i},M_{j,i})=(<,-K)$.
     
  
  
  \end{itemize}
  The set of regions form a finite partition of $\Realnn^{\Clocks}$.
  The~main argument for the proof is that the
  image by $\pi$ of any finite union of regions is a finite union of
  regions. Since $\pi$ is non-decreasing, the~sequence $\pi^k(G)$
  converges after finitely many steps.

  The~fact that $\pi^k(G)$ may
  only contain winning configurations follows from our construction,
  and can be proved easily by induction on $k$.
  One can also show that for all configurations outside of $\pi^k(G)$,
  there is no strategy that is winning within $k$ steps. This follows since
  the definition of $\pi(\cdot)$ gives the actions to be played by \Adam to
  prevent \Eve from winning.
  Note that this does not necessarily yield a winning strategy for \Adam,
  since the game is not determined.

````


%Hence, this operator allows us to express the states that can be controlled

%operator exists and can be computed. 

%See also Tripakis et al. before 2005.
