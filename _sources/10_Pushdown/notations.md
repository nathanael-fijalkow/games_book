(10-sec:notations)=
# Notations

```{math}
\def\AC#1{\textcolor{green!50!black}{\checkmark}\marginpar{\color{green!50!black}AC: #1}} 
\def\acchanged#1{{#1}}
\def\OS#1{\textcolor{red}{\checkmark}\marginpar{\color{red}OS: #1}} 

\renewcommand{\qed}{$\square$}
\newcommand{\pop}{\mathrm{pop}}
\newcommand{\push}[1]{\mathrm{push}(#1)}
\newcommand{\PDS}{\mathcal{P}}
\newcommand{\pdscol}[1]{\col(#1)}
\newcommand{\vect}[1]{\overrightarrow{#1}}
\newcommand{\ttrue}{t\! t}
\newcommand{\ffalse}{f\!\! f}
\newcommand {\Stepsg}[1]{\ensuremath{\mathit{Steps}_{#1}}}
\newcommand{\sh}{\mathrm{sh}}
\newcommand{\fgraph}{\widetilde{G}}
\newcommand{\farena}{\widetilde{\arena}}
\newcommand{\fgame}{\widetilde{\game}}
\newcommand{\fplay}{\widetilde{\play}}
\newcommand{\fsigma}{\widetilde{\sigma}}
\newcommand {\Rounds}[1]{\ensuremath{\mathit{Rounds}_{#1}}}
\newcommand{\kind}[2]{kind(#1,#2)}
\newcommand{\factcol}[2]{\mathrm{mcol}(#1,#2)}
\newcommand{\fac}[1]{kind^{#1}}
\newcommand{\pcol}[1]{\mathrm{mcol}^{#1}}
\newcommand{\hgraph}{\widehat{G}}
\newcommand{\harena}{\widehat{\arena}}
\newcommand{\hgame}{\widehat{\game}}
\newcommand{\hplay}{\widehat{\play}}
\newcommand{\hsigma}{\widehat{\sigma}}
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
A **pushdown system** is a tuple $\PDS = (Q,Q_{\mEve}, Q_{\mAdam}, \Gamma,\Delta,C)$\AC{Do we add $\pdscol{}$ and $\bot$ to the tuple of a pushdown system ? I have no opinion.} 
where:
 
*  $Q$ is a finite set of control states with $Q = Q_{\mEve} \uplus Q_{\mAdam}$ which is partionned between the two players \Eve and \Adam. Moreover with each state $q$ is associated a colour $\pdscol{q} \acchanged{\in C}$;*  $\Gamma$ is the stack alphabet. There is a special bottom-of-stack symbol, denoted $\bot$, which does not belong to $\Gamma$; we let $\Gamma_\bot$ denote the alphabet $\Gamma \cup \set{\bot}$;
*  $\Delta:Q\times \Gamma_\bot\rightarrow 2^{Q\times\{\pop,\push{\gamma}\mid \gamma\in\Gamma\}}$ is the transition relation. We additionally require that for all states $p,q\in Q$, $(q,\pop)\notin\Delta(p,\bot)$, i.e., the bottom of stack symbol is never popped.

We call a pair $(p,s)\in Q \times \bot\Gamma^*$ a **configuration** of $\PDS$: $p$ is the control state of the configuration while $s$ is its stack content. We let $\sh((p,s))=|s|-1$ denote the **stack height** of the  configuration $(p,s)$. \acchanged{Intuitively, if $(q,\push{\gamma'})$ belongs to $\Delta(p,\gamma)$, the pushdown system
in any configuration of the form $(p,s\gamma)$ can go to state $q$ after pushing the symbol $\gamma$ on top of the stack, leading to the configuration $(q,s\gamma\gamma')$. Similarly, if $(q,\pop)$ belongs to $\Delta(p,\gamma)$, the pushdown system
in any configuration of the form $(p,s\gamma)$ can go to the configuration $(q,s)$ after **poping** the top symbol from the stack.}



A pushdown system induces an arena $\arena = (G,\VE,\VA)$ called a **pushdown arena** where

*  the set of vertices is the set $V = Q \times \bot\Gamma^* $ of configurations of $\PDS$ with $\VE = Q_{\mEve} \times \bot\Gamma^*$ 
and $\VA = Q_{\mAdam} \times \bot\Gamma^* $;
*  the set $E$ of edges induced by $\Delta$ is
\begin{equation*}
\begin{split}
E  = & \{((p,s\gamma),\pdscol{p},(q,s)) \mid (q,\pop)\in\Delta(p,\gamma)\}\quad \cup \\ 
&  \{((p,s\gamma),\pdscol{p},(q,s\gamma\gamma')) \mid (q,\push{\gamma'})\in\Delta(p,\gamma)\}.
\end{split}
\end{equation*}



\acchanged{

````{admonition} Remark 
In this chapter, we deviate slightly from the general setting used in the book as we colour vertices and not edges. 
Because we only consider qualitative objectives, it is more convenient to consider the equivalent setting where we label vertices by colours rather than edges which is the usual convention in pushdown games.  
In the definition of a pushdown arena, the colour of an edge is uniquely determined by the colour of the control state of the source vertex. Therefore,  we also view in this chapter plays as sequences of vertices rather than sequences of edges.

````

}

Finally, a **pushdown game** is a game played on a pushdown arena. In this chapter we only consider qualitative objectives of the form $\Omega\subseteq C^\omega$ \acchanged{where $C$ is the set of colours. As in our definition, 
colours are associated to control states, the objective we consider only depend on the sequence of control states of the configurations visited along a play. By a slight abuse of notation, for a play $\pi \in V^*$, we let $\pi=(p_1,s_1)(p_2,s_2)\cdots \in \Omega$ denotes the fact that the sequences of colours $(\pdscol{p_i})_{i\geq 1}$ belongs to $\Omega$.} 



````{prf:example} NEEDS TITLE 10-ex:pushdown-game-1
:label: 10-ex:pushdown-game-1

Consider the pushdown system $\PDS = (Q,Q_{\mEve}, Q_{\mAdam}, \Gamma,\Delta)$ where:

*  $Q_{\mEve}=\{q,r\}$ and $Q_{\mAdam}=\{p\}$; $\pdscol{p} = 1$, $\pdscol{q} = 2$ and $\pdscol{r} = 0$.
*  $\Gamma=\{\gamma\}$ is a singleton.
*  $\Delta(p,\bot) = \{(p,\push{\gamma})\}$, $\Delta(p,\gamma) = \{(p,\push{\gamma}),(q,\pop)\}$, $\Delta(q,\bot) = \{(r,\push{\gamma})\}$, $\Delta(q,\gamma) = \{(q,\pop)\}$ and $\Delta(r,\gamma) = \{(q,\pop)\}$.

{numref}`10-fig:example-pushdown-game-1` depicts the part of the pushdown arena $\arena$ induced by $\PDS$ when restricted to the vertices reachable from $(p,\bot)$.

Consider the reachability game $(\arena, \Reach(\{0\}))$. Then, every vertex of the form $(q,\bot v)$ is winning for \Eve and every vertex of the form $(p,\bot v)$ is winning for \Adam as \Adam can always choose to push a $\gamma$-symbol while remaining in state $p$ hence always avoiding the state $r$ (which is the only state with colour $0$). If instead we consider, the B&uuml;chi game $\Buchi(\{0,2\})$, then \Eve is winning form all vertices. The strategy for \Adam consisting in always pushing a $\gamma$-symbol while remaining in state $p$ results in a play that infinitely often sees the colour $2$.

```{figure} ./../FigAndAlgos/10-fig:example-pushdown-game-1.png
:name: 10-fig:example-pushdown-game-1
:align: center
Pushdown arena from  {prf:ref}`10-ex:pushdown-game-1`
```

````


As a pushdown arena is in general infinite, the **winning region** for \Eve, i.e., the set of winning vertices for \Eve may not admit a finite presentation. Similarly, for objectives for which finite-memory strategies exists, the question of whether such a strategy can be finitely presented (and computed) is raised. Hence, we will in general distinguish the following three algorithmic problems.

```{admonition} Problem

For pushdown games, solving the game means solving the following decision problem:

**INPUT**: A pushdown game $\game$ and an initial vertex $v_0$

**QUESTION**: Does Eve win $\game$ from $v_0$?

```

```{admonition} Problem

For pushdown games, computing the winning region means solving the following problem:

\begin{tabular}{rl}
**INPUT:** & A pushdown game $\game$ \\
**OUTPUT:** & A finite presentation of the set $v$ of vertices from which  Eve wins $\game$
\end{tabular}

```

In  {prf:ref}`10-thm:regularity-wr`, we will show that the winning region can be described by a finite-state automaton  for a large class of qualitative winning conditions.

```{admonition} Problem

For pushdown games, computing a winning strategy means solving the following problem:

\begin{tabular}{rp{9.5cm}}
**INPUT:** & A pushdown game $\game$ \\
**OUTPUT:** & A finite presentation of a strategy for \Eve that is winning from any vertex in the winning region for Eve in $\game$
\end{tabular}

```


We will show, for parity pushdown games, that the winning strategy can be described using either a finite-state automaton (see Section {ref}`10-sec:regular-strat`) or a pushdown automaton (see Section {ref}`10-sec:pushdown-strat`).
