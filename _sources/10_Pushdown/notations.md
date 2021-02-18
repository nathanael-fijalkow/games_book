(10-sec:notations)=
# Notations


```{math}
\newcommand{\pop}{\mathrm{pop}}
\newcommand{\PDS}{\mathcal{P}}
\newcommand{\sh}{\mathrm{sh}}
\newcommand{\Eve}{\textrm{Eve}}
\newcommand{\Adam}{\textrm{Adam}}
\newcommand{\game}{\mathcal{G}}
\newcommand{\arena}{\mathcal{A}}
\newcommand{\mEve}{\mathrm{Eve}}
\newcommand{\mAdam}{\mathrm{Adam}}
\newcommand{\VE}{V_\mEve}
\newcommand{\VA}{V_\mAdam}
\newcommand{\Reach}{\mathtt{Reach}}
\newcommand{\Buchi}{\mathtt{Buchi}}
```

A **pushdown system** is a tuple $\mathcal{P}= (Q,Q_{\mathrm{Eve}, Q_{\mathrm{Adam}, \Gamma,\Delta,C)$\AC{Do we add $\pdscol{}$ and $\bot$ to the tuple of a pushdown system ? I have no opinion.} 
where:
 
*  $Q$ is a finite set of control states with $Q = Q_{\mathrm{Eve} \uplus Q_{\mathrm{Adam}$ which is partionned between the two players \textrm{Eve}and \textrm{Adam} Moreover with each state $q$ is associated a colour $\pdscol{q} \acchanged{\in C}$;*  $\Gamma$ is the stack alphabet. There is a special bottom-of-stack symbol, denoted $\bot$, which does not belong to $\Gamma$; we let $\Gamma_\bot$ denote the alphabet $\Gamma \cup \set{\bot}$;
*  $\Delta:Q\times \Gamma_\bot\rightarrow 2^{Q\times\{\mathrm{pop}\push{\gamma}\mid \gamma\in\Gamma\}}$ is the transition relation. We additionally require that for all states $p,q\in Q$, $(q,\mathrm{pop}\notin\Delta(p,\bot)$, i.e., the bottom of stack symbol is never popped.

We call a pair $(p,s)\in Q \times \bot\Gamma^*$ a **configuration** of $\mathcal{P}: $p$ is the control state of the configuration while $s$ is its stack content. We let $\mathrm{sh}(p,s))=|s|-1$ denote the **stack height** of the  configuration $(p,s)$. \acchanged{Intuitively, if $(q,\push{\gamma'})$ belongs to $\Delta(p,\gamma)$, the pushdown system
in any configuration of the form $(p,s\gamma)$ can go to state $q$ after pushing the symbol $\gamma$ on top of the stack, leading to the configuration $(q,s\gamma\gamma')$. Similarly, if $(q,\mathrm{pop}$ belongs to $\Delta(p,\gamma)$, the pushdown system
in any configuration of the form $(p,s\gamma)$ can go to the configuration $(q,s)$ after **poping** the top symbol from the stack.}



A pushdown system induces an arena $\mathcal{A}= (G,V_\mEveV_\mathrm{Adam} called a **pushdown arena** where

*  the set of vertices is the set $V = Q \times \bot\Gamma^* $ of configurations of $\mathcal{P} with $V_\mathrm{Eve} Q_{\mathrm{Eve} \times \bot\Gamma^*$ 
and $V_\mathrm{Adam} Q_{\mathrm{Adam} \times \bot\Gamma^* $;
*  the set $E$ of edges induced by $\Delta$ is
\begin{equation*}
\begin{split}
E  = & \{((p,s\gamma),\pdscol{p},(q,s)) \mid (q,\mathrm{pop}\in\Delta(p,\gamma)\}\quad \cup \\ 
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

Consider the pushdown system $\mathcal{P}= (Q,Q_{\mathrm{Eve}, Q_{\mathrm{Adam}, \Gamma,\Delta)$ where:

*  $Q_{\mathrm{Eve}=\{q,r\}$ and $Q_{\mathrm{Adam}=\{p\}$; $\pdscol{p} = 1$, $\pdscol{q} = 2$ and $\pdscol{r} = 0$.
*  $\Gamma=\{\gamma\}$ is a singleton.
*  $\Delta(p,\bot) = \{(p,\push{\gamma})\}$, $\Delta(p,\gamma) = \{(p,\push{\gamma}),(q,\mathrm{pop}\}$, $\Delta(q,\bot) = \{(r,\push{\gamma})\}$, $\Delta(q,\gamma) = \{(q,\mathrm{pop}\}$ and $\Delta(r,\gamma) = \{(q,\mathrm{pop}\}$.

{numref}`10-fig:example-pushdown-game-1` depicts the part of the pushdown arena $\mathcal{A} induced by $\mathcal{P} when restricted to the vertices reachable from $(p,\bot)$.

Consider the reachability game $(\mathcal{A} \mathtt{Reach}\{0\}))$. Then, every vertex of the form $(q,\bot v)$ is winning for \textrm{Eve}and every vertex of the form $(p,\bot v)$ is winning for \textrm{Adam}as \textrm{Adam}can always choose to push a $\gamma$-symbol while remaining in state $p$ hence always avoiding the state $r$ (which is the only state with colour $0$). If instead we consider, the B&uuml;chi game $\mathtt{Buchi}\{0,2\})$, then \textrm{Eve}is winning form all vertices. The strategy for \textrm{Adam}consisting in always pushing a $\gamma$-symbol while remaining in state $p$ results in a play that infinitely often sees the colour $2$.

```{figure} ./../FigAndAlgos/10-fig:example-pushdown-game-1.png
:name: 10-fig:example-pushdown-game-1
:align: center
Pushdown arena from  {prf:ref}`10-ex:pushdown-game-1`
```

````


As a pushdown arena is in general infinite, the **winning region** for \textrm{Eve} i.e., the set of winning vertices for \textrm{Eve}may not admit a finite presentation. Similarly, for objectives for which finite-memory strategies exists, the question of whether such a strategy can be finitely presented (and computed) is raised. Hence, we will in general distinguish the following three algorithmic problems.

```{admonition} Problem

For pushdown games, solving the game means solving the following decision problem:

**INPUT**: A pushdown game $\mathcal{G} and an initial vertex $v_0$

**QUESTION**: Does Eve win $\mathcal{G} from $v_0$?

```

```{admonition} Problem

For pushdown games, computing the winning region means solving the following problem:

**INPUT**: A pushdown game $\mathcal{G}

**COMPUTE**: A finite presentation of the set $v$ of vertices from which  Eve wins $\mathcal{G}

\end{tabular}

```

In  {prf:ref}`10-thm:regularity-wr`, we will show that the winning region can be described by a finite-state automaton  for a large class of qualitative winning conditions.

```{admonition} Problem

For pushdown games, computing a winning strategy means solving the following problem:

**INPUT**: A pushdown game $\mathcal{G}

**COMPUTE**: A finite presentation of a strategy for \textrm{Eve}that is winning from any vertex in the winning region for Eve in $\mathcal{G}

```


We will show, for parity pushdown games, that the winning strategy can be described using either a finite-state automaton (see Section {ref}`10-sec:regular-strat`) or a pushdown automaton (see Section {ref}`10-sec:pushdown-strat`).
