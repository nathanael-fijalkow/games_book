(11-sec:counters)=
# Vector games

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
\AP A vector system is a finite directed graph with a partition of
the vertices and weighted edges.  Formally, it is a tuple
$\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,\dd)$ where $\dd\in\+N$ is a
dimension, $\Loc$ is a finite set of locations partitioned into the
locations controlled by \Eve and \Adam, i.e.,
$\Loc=\Loc_\mEve\uplus \Loc_\mAdam$, and
$\Act\subseteq \Loc\times\+Z^\dd\times\Loc$ is a finite set of
weighted actions.  We write $\loc\step{\vec u}\loc'$
rather than $(\loc,\vec u,\loc')$ for actions in $\Act$.  A
vector addition system with states is a vector system where
$\Loc_\mAdam=\emptyset$, i.e., it corresponds to the one-player case.

````{prf:example} NEEDS TITLE 11-ex-mwg
:label: 11-ex-mwg

  \Cref{11-fig-mwg} presents a vector system of
  dimension two with locations $\{\loc,\loc'\}$ where $\loc$ is
  controlled by \Eve and $\loc'$ by \Ada   .

````

\begin{figure}[htbp]
  \centering
  \begin{tikzpicture}[auto,on grid,node distance=2.5cm]
    \node[s-eve](0){$\loc$};
    \node[s-adam,right=of 0](1){$\loc'$};
    \path[arrow,every node/.style={font=\footnotesize,inner sep=1}]
    (0) edge[loop left] node {$-1,-1$} ()
    (0) edge[bend right=10] node {$-1,0$} (1)
    (1) edge[bend left=30] node {$-1,0$} (0)
    (1) edge[bend right=30,swap] node {$2,1$} (0);
  \end{tikzpicture}
  \caption{\label{11-fig-mwg} A vector system.}
\end{figure}

The intuition behind a vector system is that it
maintains $\dd$ counters $\mathtt{c}_1,\dots,\mathtt{c}_\dd$ assigned
to integer values.  An action $\loc\step{\vec u}\loc'\in\Act$ then
updates each counter by adding the corresponding entry of $\vec u$,
that is for all $1\leq j\leq\dd$, the action performs the update
$\mathtt{c}_j := \mathtt{c}_j+\vec u(j)$.

\medskip \AP Before we proceed any further, let us fix some notations
for vectors in $\+Z^\dd$.  We write `$\vec 0$' for the zero vector
with $\vec 0(j)\eqdef 0$ for all $1\leq j\leq\dd$.  For all
$1\leq j\leq\dd$, we write `$\vec e_j$' for the unit vector with
$\vec e_j(j)\eqdef 1$ and $\vec e_{j}(j')\eqdef 0$ for all $j'\neq j$.
Addition and comparison are defined componentwise, so that for
instance $\vec u\leq\vec u'$ if and only if for all $1\leq j\leq\dd$,
$\vec u(j)\leq\vec u'(j)$.  We write
$\weight(\loc\step{\vec u}\loc')\eqdef\vec u$ for the weight of an
action and $\weight(\pi)\eqdef\sum_{1\leq j\leq |\pi|}\weight(\pi_j)$
for the cumulative weight of a finite sequence of actions
$\pi\in\Act^\ast$.  For a vector $\vec u\in\+Z^\dd$, we use its
infinity norm $\|\vec u\|\eqdef\max_{1\leq j\leq\dd}|\vec u(j)|$,
hence $\|\vec 0\|=0$ and $\|\vec e_j\|=\|-\vec e_j\|=1$, and we let
$\|\loc\step{\vec u}\loc'\|\eqdef\|\weight(\loc\step{\vec
  u}\loc')\|=\|\vec u\|$
and $\|\Act\|\eqdef\max_{a\in\Act}\|\weight(a)\|$.  Unless stated
otherwise, we assume that all our vectors are represented in binary,
hence $\|\Act\|$ may be exponential in the size of $\?V$.

## Arenas and Games
\AP A vector system gives rise to an infinite graph
$G_\+N\eqdef(V,E)$ over the set of vertices
$V\eqdef(\Loc\times\+N^\dd)\uplus\{\sink\}$.  The vertices of the
graph are either **configurations** $\loc(\vec v)$ consisting of a
location $\loc\in \Loc$ and a vector of non-negative integers
$\vec v\in\+N^\dd$---such a vector represents a valuation of the
counters $\mathtt{c}_1,\dots,\mathtt c_\dd$---, or the
sink $\sink$.

\AP Consider an action in $a=(\loc\step{\vec u}\loc')$ in $\Act$: we
see it as a partial function
$a{:}\,\Loc\times\+N^\dd\,\pto \Loc\times\+N^\dd$ with domain
$\dom a\eqdef\{\loc(\vec v)\mid \vec v+\vec u\geq\vec 0\}$ and image
$a(\loc(\vec v))\eqdef \loc'(\vec v+\vec u)$; let also
$\dom\Act\eqdef\bigcup_{a\in\Act}\dom a$.  This allows us to define
the set $E$ of edges as a set of pairs
\begin{align*}
  E&\eqdef\{(\loc(\vec v),a(\loc(\vec v)))\mid a\in\Act\text{ and
     }\loc(\vec v)\in\dom a\}\\%\loc'(\vec v+\vec u))\mid
                                &\:\cup\:\{(\loc(\vec v),\sink)\mid\loc(\vec v)\not\in\dom\Act\}\cup\{(\sink,\sink)\}\;,
\end{align*}
where $\ing((v,v'))\eqdef v$ and $\out((v,v'))\eqdef v'$ for all
edges $(v,v')\in E$.  There is therefore an edge $(v,v')$ between two
configurations $v=\loc(\vec v)$ and $v'=\loc'(\vec v')$ if there
exists an action $\loc\step{\vec u}\loc'\in\Act$ such that
$\vec v'=\vec v+\vec u$.  Note that, quite importantly,
$\vec v+\vec u$ must be non-negative on every coordinate for this edge
to exist.  If no action can be applied, there is an edge to the
sink $\sink$, which ensures that $E$ is total: for all $v\in V$,
there exists an edge $(v,v')\in E$ for some $v'$, and thus there are
no `deadlocks' in the graph.

The configurations are naturally partitioned into those in
$\VE\eqdef\Loc_\mEve\times\+N^\dd$ controlled by~\Eve and those in
$\VA\eqdef\Loc_\mAdam\times\+N^\dd$ controlled by~\Adam.  Regarding
the sink, the only edge starting from $\sink$ loops back
to it, and it does not matter who of \Eve or \Adam controls it.  This
gives rise to an infinite arena $\arena_\+N\eqdef(G_\+N,\VE,\VA)$ called
the natural semantics of $\?V$.

\medskip Although we work in a turn-based setting with perfect
information, it is sometimes enlightening to consider the partial map
$\dest{:}\,V\times A\pto E$ defined by
$\dest(\loc(\vec v),a)\eqdef(\loc(\vec v),a(\loc(\vec v)))$ if
$\loc(\vec v)\in\dom a$ and
$\dest(\loc(\vec v),a)\eqdef(\loc(\vec v),\sink)$ if
$\loc(\vec v)\not\in\dom\Act$.  Note that a sequence $\pi$ over $E$
that avoids the sink can also be described by an initial
configuration $\loc_0(\vec v_0)$ paired with a sequence
over $\Act$% will rather use a vertex colouring $\col{:}\,V\to C$ and allow it to

````{prf:example} NEEDS TITLE 11-ex-sem
:label: 11-ex-sem

  \Cref{11-fig-sem} illustrates the natural semantics of the system
  of~\cref{11-fig-mwg}; observe that all the configurations $\loc(0,n)$
  for $n\in\+N$ lead to the sink.

````

\begin{figure}[htbp]
  \centering\scalebox{.77}{
  \begin{tikzpicture}[auto,on grid,node distance=2.5cm]
    \draw[step=1,lightgray!50,dotted] (-5.7,0) grid (5.7,3.8);
    \node at (0,3.9) (sink) {\boldmath$\sink$};
    \draw[step=1,lightgray!50] (1,0) grid (5.5,3.5);
    \draw[step=1,lightgray!50] (-1,0) grid (-5.5,3.5);
    \draw[color=white](0,-.3) -- (0,3.8);
    \node at (0,0)[lightgray,font=\scriptsize,fill=white] {0};
    \node at (0,1)[lightgray,font=\scriptsize,fill=white] {1};
    \node at (0,2)[lightgray,font=\scriptsize,fill=white] {2};
    \node at (0,3)[lightgray,font=\scriptsize,fill=white] {3};
    \node at (1,3.9)[lightgray,font=\scriptsize,fill=white] {0};
    \node at (2,3.9)[lightgray,font=\scriptsize,fill=white] {1};
    \node at (3,3.9)[lightgray,font=\scriptsize,fill=white] {2};
    \node at (4,3.9)[lightgray,font=\scriptsize,fill=white] {3};
    \node at (5,3.9)[lightgray,font=\scriptsize,fill=white] {4};
    \node at (-1,3.9)[lightgray,font=\scriptsize,fill=white] {0};
    \node at (-2,3.9)[lightgray,font=\scriptsize,fill=white] {1};
    \node at (-3,3.9)[lightgray,font=\scriptsize,fill=white] {2};
    \node at (-4,3.9)[lightgray,font=\scriptsize,fill=white] {3};
    \node at (-5,3.9)[lightgray,font=\scriptsize,fill=white] {4};
    \node at (1,0)[s-eve-small] (e00) {};
    \node at (1,1)[s-adam-small](a01){};
    \node at (1,2)[s-eve-small] (e02){};
    \node at (1,3)[s-adam-small](a03){};
    \node at (2,0)[s-adam-small](a10){};
    \node at (2,1)[s-eve-small] (e11){};
    \node at (2,2)[s-adam-small](a12){};
    \node at (2,3)[s-eve-small] (e13){};
    \node at (3,0)[s-eve-small] (e20){};
    \node at (3,1)[s-adam-small](a21){};
    \node at (3,2)[s-eve-small] (e22){};
    \node at (3,3)[s-adam-small](a23){};
    \node at (4,0)[s-adam-small](a30){};
    \node at (4,1)[s-eve-small] (e31){};
    \node at (4,2)[s-adam-small](a32){};
    \node at (4,3)[s-eve-small] (e33){};
    \node at (5,0)[s-eve-small] (e40){};
    \node at (5,1)[s-adam-small](a41){};
    \node at (5,2)[s-eve-small] (e42){};
    \node at (5,3)[s-adam-small](a43){};
    \node at (-1,0)[s-adam-small](a00){};
    \node at (-1,1)[s-eve-small] (e01){};
    \node at (-1,2)[s-adam-small](a02){};
    \node at (-1,3)[s-eve-small] (e03){};
    \node at (-2,0)[s-eve-small] (e10){};
    \node at (-2,1)[s-adam-small](a11){};
    \node at (-2,2)[s-eve-small] (e12){};
    \node at (-2,3)[s-adam-small](a13){};
    \node at (-3,0)[s-adam-small](a20){};
    \node at (-3,1)[s-eve-small] (e21){};
    \node at (-3,2)[s-adam-small](a22){};
    \node at (-3,3)[s-eve-small] (e23){};
    \node at (-4,0)[s-eve-small] (e30){};
    \node at (-4,1)[s-adam-small](a31){};
    \node at (-4,2)[s-eve-small] (e32){};
    \node at (-4,3)[s-adam-small](a33){};
    \node at (-5,0)[s-adam-small](a40){};
    \node at (-5,1)[s-eve-small] (e41){};
    \node at (-5,2)[s-adam-small](a42){};
    \node at (-5,3)[s-eve-small] (e43){};
    \path[arrow]    (e11) edge (e00)
    (e22) edge (e11)
    (e31) edge (e20)
    (e32) edge (e21)
    (e21) edge (e10)
    (e12) edge (e01)
    (e23) edge (e12)
    (e33) edge (e22)
    (e13) edge (e02)
    (e43) edge (e32)
    (e42) edge (e31)
    (e41) edge (e30);
    \path[arrow]    (e11) edge (a01)
    (e20) edge (a10)
    (e22) edge (a12)
    (e31) edge (a21)
    (e32) edge (a22)
    (e21) edge (a11)
    (e12) edge (a02)
    (e30) edge (a20)
    (e10) edge (a00)
    (e13) edge (a03)
    (e23) edge (a13)
    (e33) edge (a23)
    (e43) edge (a33)
    (e42) edge (a32)
    (e41) edge (a31)
    (e40) edge (a30);
    \path[arrow]    (a11) edge (e01)
    (a20) edge (e10)
    (a22) edge (e12)
    (a31) edge (e21)
    (a32) edge (e22)
    (a21) edge (e11)
    (a12) edge (e02)
    (a30) edge (e20)
    (a10) edge (e00)
    (a33) edge (e23)
    (a23) edge (e13)
    (a13) edge (e03)
    (a43) edge (e33)
    (a42) edge (e32)
    (a41) edge (e31)
    (a40) edge (e30);
    \path[arrow]    (a01) edge (e22)
    (a10) edge (e31)
    (a11) edge (e32)
    (a00) edge (e21)
    (a02) edge (e23)
    (a12) edge (e33)
    (a22) edge (e43)
    (a21) edge (e42)
    (a20) edge (e41);
    \path[arrow]    (-5.5,3.5) edge (e43)
    (5.5,2.5) edge (e42)
    (2.5,3.5) edge (e13)
    (5.5,0.5) edge (e40)
    (-5.5,1.5) edge (e41)
    (-3.5,3.5) edge (e23)
    (-1.5,3.5) edge (e03)
    (4.5,3.5) edge (e33)
    (5.5,0) edge (e40)
    (5.5,2) edge (e42)
    (-5.5,1) edge (e41)
    (-5.5,3) edge (e43);
    \path[dotted]
    (-5.7,3.7) edge (-5.5,3.5)
    (5.7,2.7) edge (5.5,2.5)
    (2.7,3.7) edge (2.5,3.5)
    (5.7,0.7) edge (5.5,0.5)
    (-3.7,3.7) edge (-3.5,3.5)
    (-1.7,3.7) edge (-1.5,3.5)
    (4.7,3.7) edge (4.5,3.5)
    (-5.7,1.7) edge (-5.5,1.5)
    (5.75,0) edge (5.5,0)
    (5.75,2) edge (5.5,2)
    (-5.75,1) edge (-5.5,1)
    (-5.75,3) edge (-5.5,3);
    \path[arrow]
    (5.5,1) edge (a41)
    (-5.5,2) edge (a42)
    (-5.5,0) edge (a40)
    (5.5,3) edge (a43);
    \path[dotted]
    (5.75,1) edge (5.5,1)
    (-5.75,2) edge (-5.5,2)
    (-5.75,0) edge (-5.5,0)
    (5.75,3) edge (5.5,3);
    \path[-]
    (a30) edge (5.5,.75)
    (a32) edge (5.5,2.75)
    (a31) edge (-5.5,1.75)
    (a23) edge (4,3.5)
    (a03) edge (2,3.5)
    (a13) edge (-3,3.5)
    (a33) edge (-5,3.5)
    (a43) edge (5.5,3.25)
    (a41) edge (5.5,1.25)
    (a40) edge (-5.5,0.25)
    (a42) edge (-5.5,2.25);
    \path[dotted]
    (5.5,.75) edge (5.8,.9)
    (5.5,2.75) edge (5.8,2.9)
    (-5.5,1.75) edge (-5.8,1.9)
    (4,3.5) edge (4.4,3.7)
    (2,3.5) edge (2.4,3.7)
    (-3,3.5) edge (-3.4,3.7)
    (-5,3.5) edge (-5.4,3.7)
    (5.5,3.25) edge (5.8,3.4)
    (5.5,1.25) edge (5.8,1.4)
    (-5.5,.25) edge (-5.8,0.4)
    (-5.5,2.25) edge (-5.8,2.4);
    \path[arrow]
    (sink) edge[loop left] ()
    (e00) edge[bend left=8] (sink)
    (e01) edge[bend right=8] (sink)
    (e02) edge[bend left=8] (sink)
    (e03) edge[bend right=8] (sink);
  \end{tikzpicture}}
  \caption{\label{11-fig-sem} The natural semantics of the
    vector system of \cref{11-fig-mwg}: a circle (resp.\
    a square) at position $(i,j)$ of the grid denotes a configuration
    $\loc(i,j)$ (resp.\ $\loc'(i,j)$) controlled by~\Eve (resp.\
    \Adam).}
\end{figure}
%   semantics would use instead $\Loc\times\+Z^\dd$ as set of vertices,%   $\{(\loc(\vec v),\loc'(\vec v+\vec u))\mid \loc\step{\vec%   as set of edges.  This eschews the need of a sink vertex since there% \end{remark}
\AP A vector system $\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,\dd)$, a
colouring $\col{:}\,E\to C$, and an
objective $\Omega\subseteq C^\omega$ together define a vector game
$\game=(\natural(\?V),\col,\Omega)$.  Because $\natural(\?V)$ is an
infinite arena, we need to impose restrictions on our colourings
$\col{:}\,E\to C$ and the "qualitative
objectives" $\Omega\subseteq C^\omega$; at the very least, they should
be recursive.

There are then two variants of the associated decision problem:

* \AP the given initial credit variant, where we are given $\?V$,
  $\col$, $\Omega$, a location $\loc_0\in\Loc$ and an initial credit
  $\vec v_0\in\+N^\dd$, and ask whether \Eve wins $\game$ from the
  initial configuration $\loc_0(\vec v_0)$;
* \AP the existential initial credit variant, where we are given
  $\?V$, $\col$, $\Omega$, and a location $\loc_0\in\Loc$, and ask
  whether there exists an initial credit $\vec v_0\in\+N^\dd$ such
  that \Eve wins $\game$ from the initial
  configuration $\loc_0(\vec v_0)$.

Let us instantiate the previous abstract definition of vector games.
We first consider two `reachability-like'
\index{reachability!**see also** vector game\protect\mymoot|mymoot}
objectives, where $C\eqdef\{\varepsilon,\Win\}$ and
$\Omega\eqdef\Reach$, namely configuration reachability and
coverability.  The difference between the two is that, in the
configuration reachability problem, a specific configuration
$\loc_f(\vec v_f)$ should be visited, whereas in the coverability
problem, \Eve attempts to visit $\loc_f(\vec v')$ for some
vector $\vec v'$ componentwise larger or equal to
$\vec v_f$.

\decpb[configuration reachability vector game with given initial credit{\label{11-pb-reach} A vector system
  $\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,\dd)$, an initial location
  $\loc_0\in\Loc$, an initial credit $\vec v_0\in\+N^\dd$, and a
  target configuration $\loc_f(\vec v_f)\in\Loc\times\+N^\dd$.

```{margin}
The name `coverability' comes from the the
  literature on Petri nets and "vector addition systems with
  states", because \Eve is attempting to **cover**
  $\loc_f(\vec v_f)$, i.e., to reach a configuration $\loc_f(\vec v')$
  with $\vec v'\geq\vec v_f$.
```

{Does \Eve have a strategy to reach $\loc(\vec v)$ from
  $\loc_0(\vec v_0)$?\\That is, does she win the configuration
  reachability game $(\natural(\?V),\col,\Reach)$ from
  $\loc_0(\vec v_0)$, where $\col(e)= \Win$ if and only if
  $\ing(e)=\loc_f(\vec v_f)$?}

\decpb[coverability vector game with given initial credit{\label{11-pb-cov} A vector system
  $\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,\dd)$, an initial location
  $\loc_0\in\Loc$, an initial credit $\vec v_0\in\+N^\dd$, and a
  target configuration $\loc_f(\vec v_f)\in\Loc\times\+N^\dd$.{Does \Eve have a strategy to reach $\loc(\vec v')$ for some
  $\vec v'\geq\vec v_f$ from $\loc_0(\vec v_0)$?\\That is, does she win
  the coverability game $(\natural(\?V),\col,\Reach)$ from
  $\loc_0(\vec v_0)$, where $\col(e)= \Win$ if and only if
  $\ing(e)=\loc_f(\vec v')$ for some $\vec v'\geq\vec v_f$?}

````{prf:example} NEEDS TITLE 11-ex-cov
:label: 11-ex-cov

  Consider the target configuration $\loc(2,2)$ in
  \cref{11-fig-mwg,12-fig-sem}.  \Eve's winning region in the
  configuration reachability vector game is
  $\WE=\{\loc(n+1,n+1)\mid n\in\+N\}\cup\{\loc'(0,1)\}$, displayed on the left
  in \cref{11-fig-cov}.  \Eve has indeed an obvious winning strategy
  from any configuration $\loc(n,n)$ with $n\geq 2$, which is to use
  the action $\loc\step{-1,-1}\loc$ until she reaches $\loc(2,2)$.
  Furthermore, in $\loc'(0,1)$---due to the natural semantics---,
  \Adam has no choice but to use the action $\loc'\step{2,1}\loc$:
  therefore $\loc'(0,1)$ and $\loc(1,1)$ are also winning for \Eve.
\begin{figure}[htbp]
  \centering\scalebox{.48}{
  \begin{tikzpicture}[auto,on grid,node distance=2.5cm]
    \draw[step=1,lightgray!50,dotted] (-5.7,0) grid (5.7,3.8);
    \draw[color=white](0,-.3) -- (0,3.8);
    \node at (0,3.9) (sink) {\color{red!70!black}\boldmath$\sink$};
    \draw[step=1,lightgray!50] (1,0) grid (5.5,3.5);
    \draw[step=1,lightgray!50] (-1,0) grid (-5.5,3.5);
    \node at (0,0)[lightgray,font=\scriptsize,fill=white] {0};
    \node at (0,1)[lightgray,font=\scriptsize,fill=white] {1};
    \node at (0,2)[lightgray,font=\scriptsize,fill=white] {2};
    \node at (0,3)[lightgray,font=\scriptsize,fill=white] {3};
    \node at (1,3.9)[lightgray,font=\scriptsize,fill=white] {0};
    \node at (2,3.9)[lightgray,font=\scriptsize,fill=white] {1};
    \node at (3,3.9)[lightgray,font=\scriptsize,fill=white] {2};
    \node at (4,3.9)[lightgray,font=\scriptsize,fill=white] {3};
    \node at (5,3.9)[lightgray,font=\scriptsize,fill=white] {4};
    \node at (-1,3.9)[lightgray,font=\scriptsize,fill=white] {0};
    \node at (-2,3.9)[lightgray,font=\scriptsize,fill=white] {1};
    \node at (-3,3.9)[lightgray,font=\scriptsize,fill=white] {2};
    \node at (-4,3.9)[lightgray,font=\scriptsize,fill=white] {3};
    \node at (-5,3.9)[lightgray,font=\scriptsize,fill=white] {4};
    \node at (1,0)[s-eve-small,lose] (e00) {};
    \node at (1,1)[s-adam-small,win](a01){};
    \node at (1,2)[s-eve-small,lose] (e02){};
    \node at (1,3)[s-adam-small,lose](a03){};
    \node at (2,0)[s-adam-small,lose](a10){};
    \node at (2,1)[s-eve-small,win] (e11){};
    \node at (2,2)[s-adam-small,lose](a12){};
    \node at (2,3)[s-eve-small,lose] (e13){};
    \node at (3,0)[s-eve-small,lose] (e20){};
    \node at (3,1)[s-adam-small,lose](a21){};
    \node at (3,2)[s-eve-small,win] (e22){};
    \node at (3,3)[s-adam-small,lose](a23){};
    \node at (4,0)[s-adam-small,lose](a30){};
    \node at (4,1)[s-eve-small,lose] (e31){};
    \node at (4,2)[s-adam-small,lose](a32){};
    \node at (4,3)[s-eve-small,win] (e33){};
    \node at (5,0)[s-eve-small,lose] (e40){};
    \node at (5,1)[s-adam-small,lose](a41){};
    \node at (5,2)[s-eve-small,lose] (e42){};
    \node at (5,3)[s-adam-small,lose](a43){};
    \node at (-1,0)[s-adam-small,lose](a00){};
    \node at (-1,1)[s-eve-small,lose] (e01){};
    \node at (-1,2)[s-adam-small,lose](a02){};
    \node at (-1,3)[s-eve-small,lose] (e03){};
    \node at (-2,0)[s-eve-small,lose] (e10){};
    \node at (-2,1)[s-adam-small,lose](a11){};
    \node at (-2,2)[s-eve-small,lose] (e12){};
    \node at (-2,3)[s-adam-small,lose](a13){};
    \node at (-3,0)[s-adam-small,lose](a20){};
    \node at (-3,1)[s-eve-small,lose] (e21){};
    \node at (-3,2)[s-adam-small,lose](a22){};
    \node at (-3,3)[s-eve-small,lose] (e23){};
    \node at (-4,0)[s-eve-small,lose] (e30){};
    \node at (-4,1)[s-adam-small,lose](a31){};
    \node at (-4,2)[s-eve-small,lose] (e32){};
    \node at (-4,3)[s-adam-small,lose](a33){};
    \node at (-5,0)[s-adam-small,lose](a40){};
    \node at (-5,1)[s-eve-small,lose] (e41){};
    \node at (-5,2)[s-adam-small,lose](a42){};
    \node at (-5,3)[s-eve-small,lose] (e43){};
    \path[arrow]    (e11) edge (e00)
    (e22) edge (e11)
    (e31) edge (e20)
    (e32) edge (e21)
    (e21) edge (e10)
    (e12) edge (e01)
    (e23) edge (e12)
    (e33) edge (e22)
    (e13) edge (e02)
    (e43) edge (e32)
    (e42) edge (e31)
    (e41) edge (e30);
    \path[arrow]    (e11) edge (a01)
    (e20) edge (a10)
    (e22) edge (a12)
    (e31) edge (a21)
    (e32) edge (a22)
    (e21) edge (a11)
    (e12) edge (a02)
    (e30) edge (a20)
    (e10) edge (a00)
    (e13) edge (a03)
    (e23) edge (a13)
    (e33) edge (a23)
    (e43) edge (a33)
    (e42) edge (a32)
    (e41) edge (a31)
    (e40) edge (a30);
    \path[arrow]    (a11) edge (e01)
    (a20) edge (e10)
    (a22) edge (e12)
    (a31) edge (e21)
    (a32) edge (e22)
    (a21) edge (e11)
    (a12) edge (e02)
    (a30) edge (e20)
    (a10) edge (e00)
    (a33) edge (e23)
    (a23) edge (e13)
    (a13) edge (e03)
    (a43) edge (e33)
    (a42) edge (e32)
    (a41) edge (e31)
    (a40) edge (e30);
    \path[arrow]    (a01) edge (e22)
    (a10) edge (e31)
    (a11) edge (e32)
    (a00) edge (e21)
    (a02) edge (e23)
    (a12) edge (e33)
    (a22) edge (e43)
    (a21) edge (e42)
    (a20) edge (e41);
    \path[arrow]    (-5.5,3.5) edge (e43)
    (5.5,2.5) edge (e42)
    (2.5,3.5) edge (e13)
    (5.5,0.5) edge (e40)
    (-5.5,1.5) edge (e41)
    (-3.5,3.5) edge (e23)
    (-1.5,3.5) edge (e03)
    (4.5,3.5) edge (e33)
    (5.5,0) edge (e40)
    (5.5,2) edge (e42)
    (-5.5,1) edge (e41)
    (-5.5,3) edge (e43);
    \path[dotted]
    (-5.7,3.7) edge (-5.5,3.5)
    (5.7,2.7) edge (5.5,2.5)
    (2.7,3.7) edge (2.5,3.5)
    (5.7,0.7) edge (5.5,0.5)
    (-3.7,3.7) edge (-3.5,3.5)
    (-1.7,3.7) edge (-1.5,3.5)
    (4.7,3.7) edge (4.5,3.5)
    (-5.7,1.7) edge (-5.5,1.5)
    (5.75,0) edge (5.5,0)
    (5.75,2) edge (5.5,2)
    (-5.75,1) edge (-5.5,1)
    (-5.75,3) edge (-5.5,3);
    \path[arrow]
    (5.5,1) edge (a41)
    (-5.5,2) edge (a42)
    (-5.5,0) edge (a40)
    (5.5,3) edge (a43);
    \path[dotted]
    (5.75,1) edge (5.5,1)
    (-5.75,2) edge (-5.5,2)
    (-5.75,0) edge (-5.5,0)
    (5.75,3) edge (5.5,3);
    \path[-]
    (a30) edge (5.5,.75)
    (a32) edge (5.5,2.75)
    (a31) edge (-5.5,1.75)
    (a23) edge (4,3.5)
    (a03) edge (2,3.5)
    (a13) edge (-3,3.5)
    (a33) edge (-5,3.5)
    (a43) edge (5.5,3.25)
    (a41) edge (5.5,1.25)
    (a40) edge (-5.5,0.25)
    (a42) edge (-5.5,2.25);
    \path[dotted]
    (5.5,.75) edge (5.8,.9)
    (5.5,2.75) edge (5.8,2.9)
    (-5.5,1.75) edge (-5.8,1.9)
    (4,3.5) edge (4.4,3.7)
    (2,3.5) edge (2.4,3.7)
    (-3,3.5) edge (-3.4,3.7)
    (-5,3.5) edge (-5.4,3.7)
    (5.5,3.25) edge (5.8,3.4)
    (5.5,1.25) edge (5.8,1.4)
    (-5.5,.25) edge (-5.8,0.4)
    (-5.5,2.25) edge (-5.8,2.4);
    \path[arrow]
    (sink) edge[loop left] ()
    (e00) edge[bend left=8] (sink)
    (e01) edge[bend right=8] (sink)
    (e02) edge[bend left=8] (sink)
    (e03) edge[bend right=8] (sink);
  \end{tikzpicture}}\quad~~\scalebox{.48}{
  \begin{tikzpicture}[auto,on grid,node distance=2.5cm]
    \draw[step=1,lightgray!50,dotted] (-5.7,0) grid (5.7,3.8);
    \draw[color=white](0,-.3) -- (0,3.8);
    \node at (0,3.9) (sink) {\color{red!70!black}\boldmath$\sink$};
    \draw[step=1,lightgray!50] (1,0) grid (5.5,3.5);
    \draw[step=1,lightgray!50] (-1,0) grid (-5.5,3.5);
    \node at (0,0)[lightgray,font=\scriptsize,fill=white] {0};
    \node at (0,1)[lightgray,font=\scriptsize,fill=white] {1};
    \node at (0,2)[lightgray,font=\scriptsize,fill=white] {2};
    \node at (0,3)[lightgray,font=\scriptsize,fill=white] {3};
    \node at (1,3.9)[lightgray,font=\scriptsize,fill=white] {0};
    \node at (2,3.9)[lightgray,font=\scriptsize,fill=white] {1};
    \node at (3,3.9)[lightgray,font=\scriptsize,fill=white] {2};
    \node at (4,3.9)[lightgray,font=\scriptsize,fill=white] {3};
    \node at (5,3.9)[lightgray,font=\scriptsize,fill=white] {4};
    \node at (-1,3.9)[lightgray,font=\scriptsize,fill=white] {0};
    \node at (-2,3.9)[lightgray,font=\scriptsize,fill=white] {1};
    \node at (-3,3.9)[lightgray,font=\scriptsize,fill=white] {2};
    \node at (-4,3.9)[lightgray,font=\scriptsize,fill=white] {3};
    \node at (-5,3.9)[lightgray,font=\scriptsize,fill=white] {4};
    \node at (1,0)[s-eve-small,lose] (e00) {};
    \node at (1,1)[s-adam-small,win](a01){};
    \node at (1,2)[s-eve-small,lose] (e02){};
    \node at (1,3)[s-adam-small,win](a03){};
    \node at (2,0)[s-adam-small,lose](a10){};
    \node at (2,1)[s-eve-small,win] (e11){};
    \node at (2,2)[s-adam-small,lose](a12){};
    \node at (2,3)[s-eve-small,win] (e13){};
    \node at (3,0)[s-eve-small,lose] (e20){};
    \node at (3,1)[s-adam-small,win](a21){};
    \node at (3,2)[s-eve-small,win] (e22){};
    \node at (3,3)[s-adam-small,win](a23){};
    \node at (4,0)[s-adam-small,lose](a30){};
    \node at (4,1)[s-eve-small,win] (e31){};
    \node at (4,2)[s-adam-small,win](a32){};
    \node at (4,3)[s-eve-small,win] (e33){};
    \node at (5,0)[s-eve-small,lose] (e40){};
    \node at (5,1)[s-adam-small,win](a41){};
    \node at (5,2)[s-eve-small,win] (e42){};
    \node at (5,3)[s-adam-small,win](a43){};
    \node at (-1,0)[s-adam-small,lose](a00){};
    \node at (-1,1)[s-eve-small,lose] (e01){};
    \node at (-1,2)[s-adam-small,win](a02){};
    \node at (-1,3)[s-eve-small,lose] (e03){};
    \node at (-2,0)[s-eve-small,lose] (e10){};
    \node at (-2,1)[s-adam-small,lose](a11){};
    \node at (-2,2)[s-eve-small,win] (e12){};
    \node at (-2,3)[s-adam-small,lose](a13){};
    \node at (-3,0)[s-adam-small,lose](a20){};
    \node at (-3,1)[s-eve-small,lose] (e21){};
    \node at (-3,2)[s-adam-small,win](a22){};
    \node at (-3,3)[s-eve-small,win] (e23){};
    \node at (-4,0)[s-eve-small,lose] (e30){};
    \node at (-4,1)[s-adam-small,lose](a31){};
    \node at (-4,2)[s-eve-small,win] (e32){};
    \node at (-4,3)[s-adam-small,win](a33){};
    \node at (-5,0)[s-adam-small,lose](a40){};
    \node at (-5,1)[s-eve-small,lose] (e41){};
    \node at (-5,2)[s-adam-small,win](a42){};
    \node at (-5,3)[s-eve-small,win] (e43){};
    \path[arrow]    (e11) edge (e00)
    (e22) edge (e11)
    (e31) edge (e20)
    (e32) edge (e21)
    (e21) edge (e10)
    (e12) edge (e01)
    (e23) edge (e12)
    (e33) edge (e22)
    (e13) edge (e02)
    (e43) edge (e32)
    (e42) edge (e31)
    (e41) edge (e30);
    \path[arrow]    (e11) edge (a01)
    (e20) edge (a10)
    (e22) edge (a12)
    (e31) edge (a21)
    (e32) edge (a22)
    (e21) edge (a11)
    (e12) edge (a02)
    (e30) edge (a20)
    (e10) edge (a00)
    (e13) edge (a03)
    (e23) edge (a13)
    (e33) edge (a23)
    (e43) edge (a33)
    (e42) edge (a32)
    (e41) edge (a31)
    (e40) edge (a30);
    \path[arrow]    (a11) edge (e01)
    (a20) edge (e10)
    (a22) edge (e12)
    (a31) edge (e21)
    (a32) edge (e22)
    (a21) edge (e11)
    (a12) edge (e02)
    (a30) edge (e20)
    (a10) edge (e00)
    (a33) edge (e23)
    (a23) edge (e13)
    (a13) edge (e03)
    (a43) edge (e33)
    (a42) edge (e32)
    (a41) edge (e31)
    (a40) edge (e30);
    \path[arrow]    (a01) edge (e22)
    (a10) edge (e31)
    (a11) edge (e32)
    (a00) edge (e21)
    (a02) edge (e23)
    (a12) edge (e33)
    (a22) edge (e43)
    (a21) edge (e42)
    (a20) edge (e41);
    \path[arrow]    (-5.5,3.5) edge (e43)
    (5.5,2.5) edge (e42)
    (2.5,3.5) edge (e13)
    (5.5,0.5) edge (e40)
    (-5.5,1.5) edge (e41)
    (-3.5,3.5) edge (e23)
    (-1.5,3.5) edge (e03)
    (4.5,3.5) edge (e33)
    (5.5,0) edge (e40)
    (5.5,2) edge (e42)
    (-5.5,1) edge (e41)
    (-5.5,3) edge (e43);
    \path[dotted]
    (-5.7,3.7) edge (-5.5,3.5)
    (5.7,2.7) edge (5.5,2.5)
    (2.7,3.7) edge (2.5,3.5)
    (5.7,0.7) edge (5.5,0.5)
    (-3.7,3.7) edge (-3.5,3.5)
    (-1.7,3.7) edge (-1.5,3.5)
    (4.7,3.7) edge (4.5,3.5)
    (-5.7,1.7) edge (-5.5,1.5)
    (5.75,0) edge (5.5,0)
    (5.75,2) edge (5.5,2)
    (-5.75,1) edge (-5.5,1)
    (-5.75,3) edge (-5.5,3);
    \path[arrow]
    (5.5,1) edge (a41)
    (-5.5,2) edge (a42)
    (-5.5,0) edge (a40)
    (5.5,3) edge (a43);
    \path[dotted]
    (5.75,1) edge (5.5,1)
    (-5.75,2) edge (-5.5,2)
    (-5.75,0) edge (-5.5,0)
    (5.75,3) edge (5.5,3);
    \path[-]
    (a30) edge (5.5,.75)
    (a32) edge (5.5,2.75)
    (a31) edge (-5.5,1.75)
    (a23) edge (4,3.5)
    (a03) edge (2,3.5)
    (a13) edge (-3,3.5)
    (a33) edge (-5,3.5)
    (a43) edge (5.5,3.25)
    (a41) edge (5.5,1.25)
    (a40) edge (-5.5,0.25)
    (a42) edge (-5.5,2.25);
    \path[dotted]
    (5.5,.75) edge (5.8,.9)
    (5.5,2.75) edge (5.8,2.9)
    (-5.5,1.75) edge (-5.8,1.9)
    (4,3.5) edge (4.4,3.7)
    (2,3.5) edge (2.4,3.7)
    (-3,3.5) edge (-3.4,3.7)
    (-5,3.5) edge (-5.4,3.7)
    (5.5,3.25) edge (5.8,3.4)
    (5.5,1.25) edge (5.8,1.4)
    (-5.5,.25) edge (-5.8,0.4)
    (-5.5,2.25) edge (-5.8,2.4);
    \path[arrow]
    (sink) edge[loop left] ()
    (e00) edge[bend left=8] (sink)
    (e01) edge[bend right=8] (sink)
    (e02) edge[bend left=8] (sink)
    (e03) edge[bend right=8] (sink);
  \end{tikzpicture}}
  \caption{\label{11-fig-cov} The winning regions of \Eve in the
    configuration reachability game (left) and the coverability game
    (right) on the graphs of \cref{11-fig-mwg,12-fig-sem} with target
    configuration $\ell(2,2)$.  The winning vertices are in filled in
    green, while the losing ones are filled with white with a red
    border; the sink is always losing.}
\end{figure}

In the coverability vector game, \Eve's winning region is
$\WE=\{\loc(m+2,n+2),\loc'(m+2,n+2),\loc'(0,n+1),\loc(1,n+2),\loc'(2m+2,1),\loc(2m+3,1)\mid
m,n\in\+N\}$
displayed on the right in \cref{11-fig-cov}.  Observe in particular
that \Adam is forced to use the action $\ell'\step{2,1}\ell$ from
the configurations of the form $\loc'(0,n+1)$, which brings him to a
configuration $\ell(2,n+2)$ coloured $\Win$ in the game, and thus the
configurations of the form $\loc(1,n+1)$ are also winning for \Eve
since she can play $\loc\step{-1,0}\loc'$.  Thus the configurations of
the form $\loc(2m+3,n+1)$ are also winning for \Eve, as she can play
the action $\loc\step{-1,0}\loc'$ to a winning configuration
$\loc'(2m+2,n+1)$ where all the actions available to \Adam go into
her winning region.

````


````{admonition} Remark \label{11-cov2cov}
  In both configuration reachability and coverability, we can
  assume without loss of generality that $\loc_f\in\Loc_\mEve$ is
  controlled by \Eve and that $\vec v_f=\vec 0$ is the zero vector.
  Thus coverability is equivalent to **location reachability**.
  
  There is indeed a \logspace\ reduction to that case.  If
  $\loc_0(\vec v_0)=\loc_f(\vec v_f)$ in the case of "configuration
  reachability", or $\loc_0=\loc_f$ and $\vec v_0\geq\vec v_f$ in the
  case of coverability, the problem is trivial.
   Otherwise, any winning play must use at least one action.  For
  each incoming action $a=(\loc\step{\vec u}\loc_f)$ of $\loc_f$,
  create a new location $\loc_a$ controlled by \Eve and replace $a$ by
  $\loc\step{\vec u}\loc_a\step{\vec 0}\loc_f$, so that \Eve gains the
  control right before any play reaches $\loc_f$.  Also add a new
  location $\smiley$ controlled by \Eve with actions
  $\loc_a\step{-\vec v_f}\smiley$, and use $\smiley(\vec 0)$ as target
  configuration.

````


````{admonition} Remark \label{11-cov2reach}
  There is a \logspace\ reduction from coverability to
  configuration reachability.  By \cref{11-cov2cov}, we can assume
  without loss of generality that $\loc_f\in\Loc_\mEve$ is controlled
  by \Eve and that $\vec v_f=\vec 0$ is the zero vector. It suffices
  therefore to add an action $\loc_f\step{-\vec e_j}\loc_f$ for
  all $1\leq j\leq\dd$.

````

Departing from reachability games, the
following is a very simple kind of safety
games where $C\eqdef\{\varepsilon,\Lose\}$ and $\Omega\eqdef\Safe$;
\cref{11-fig-nonterm} shows \Eve's winning region in the case of the
graphs of \cref{11-fig-mwg,12-fig-sem}.
\decpb[non-termination vector game with given initial credit{\label{11-pb-nonterm} A vector system
  $\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,\dd)$, an initial location
  $\loc_0\in\Loc$, and an initial credit $\vec v_0\in\+N^\dd$.{Does \Eve have a strategy to avoid the sink $\sink$ from
  $\loc_0(\vec v_0)$?\\That is, does she win the non-termination
  game $(\natural(\?V),\col,\Safe)$ from $\loc_0(\vec v_0)$, where
  $\col(e)=\Lose$ if and only if $\ing(e)=\sink$?} 

  \begin{figure}[bhtp]
  \centering\scalebox{.48}{
  \begin{tikzpicture}[auto,on grid,node distance=2.5cm]
    \draw[step=1,lightgray!50,dotted] (-5.7,0) grid (5.7,3.8);
    \draw[color=white](0,-.3) -- (0,3.8);
    \node at (0,3.9) (sink) {\color{red!70!black}\boldmath$\sink$};
    \draw[step=1,lightgray!50] (1,0) grid (5.5,3.5);
    \draw[step=1,lightgray!50] (-1,0) grid (-5.5,3.5);
    \node at (0,0)[lightgray,font=\scriptsize,fill=white] {0};
    \node at (0,1)[lightgray,font=\scriptsize,fill=white] {1};
    \node at (0,2)[lightgray,font=\scriptsize,fill=white] {2};
    \node at (0,3)[lightgray,font=\scriptsize,fill=white] {3};
    \node at (1,3.9)[lightgray,font=\scriptsize,fill=white] {0};
    \node at (2,3.9)[lightgray,font=\scriptsize,fill=white] {1};
    \node at (3,3.9)[lightgray,font=\scriptsize,fill=white] {2};
    \node at (4,3.9)[lightgray,font=\scriptsize,fill=white] {3};
    \node at (5,3.9)[lightgray,font=\scriptsize,fill=white] {4};
    \node at (-1,3.9)[lightgray,font=\scriptsize,fill=white] {0};
    \node at (-2,3.9)[lightgray,font=\scriptsize,fill=white] {1};
    \node at (-3,3.9)[lightgray,font=\scriptsize,fill=white] {2};
    \node at (-4,3.9)[lightgray,font=\scriptsize,fill=white] {3};
    \node at (-5,3.9)[lightgray,font=\scriptsize,fill=white] {4};
    \node at (1,0)[s-eve-small,lose] (e00) {};
    \node at (1,1)[s-adam-small,win](a01){};
    \node at (1,2)[s-eve-small,lose] (e02){};
    \node at (1,3)[s-adam-small,win](a03){};
    \node at (2,0)[s-adam-small,lose](a10){};
    \node at (2,1)[s-eve-small,win] (e11){};
    \node at (2,2)[s-adam-small,lose](a12){};
    \node at (2,3)[s-eve-small,win] (e13){};
    \node at (3,0)[s-eve-small,lose] (e20){};
    \node at (3,1)[s-adam-small,win](a21){};
    \node at (3,2)[s-eve-small,win] (e22){};
    \node at (3,3)[s-adam-small,win](a23){};
    \node at (4,0)[s-adam-small,lose](a30){};
    \node at (4,1)[s-eve-small,win] (e31){};
    \node at (4,2)[s-adam-small,win](a32){};
    \node at (4,3)[s-eve-small,win] (e33){};
    \node at (5,0)[s-eve-small,lose] (e40){};
    \node at (5,1)[s-adam-small,win](a41){};
    \node at (5,2)[s-eve-small,win] (e42){};
    \node at (5,3)[s-adam-small,win](a43){};
    \node at (-1,0)[s-adam-small,win](a00){};
    \node at (-1,1)[s-eve-small,lose] (e01){};
    \node at (-1,2)[s-adam-small,win](a02){};
    \node at (-1,3)[s-eve-small,lose] (e03){};
    \node at (-2,0)[s-eve-small,win] (e10){};
    \node at (-2,1)[s-adam-small,lose](a11){};
    \node at (-2,2)[s-eve-small,win] (e12){};
    \node at (-2,3)[s-adam-small,lose](a13){};
    \node at (-3,0)[s-adam-small,win](a20){};
    \node at (-3,1)[s-eve-small,win] (e21){};
    \node at (-3,2)[s-adam-small,win](a22){};
    \node at (-3,3)[s-eve-small,win] (e23){};
    \node at (-4,0)[s-eve-small,win] (e30){};
    \node at (-4,1)[s-adam-small,win](a31){};
    \node at (-4,2)[s-eve-small,win] (e32){};
    \node at (-4,3)[s-adam-small,win](a33){};
    \node at (-5,0)[s-adam-small,win](a40){};
    \node at (-5,1)[s-eve-small,win] (e41){};
    \node at (-5,2)[s-adam-small,win](a42){};
    \node at (-5,3)[s-eve-small,win] (e43){};
    \path[arrow]    (e11) edge (e00)
    (e22) edge (e11)
    (e31) edge (e20)
    (e32) edge (e21)
    (e21) edge (e10)
    (e12) edge (e01)
    (e23) edge (e12)
    (e33) edge (e22)
    (e13) edge (e02)
    (e43) edge (e32)
    (e42) edge (e31)
    (e41) edge (e30);
    \path[arrow]    (e11) edge (a01)
    (e20) edge (a10)
    (e22) edge (a12)
    (e31) edge (a21)
    (e32) edge (a22)
    (e21) edge (a11)
    (e12) edge (a02)
    (e30) edge (a20)
    (e10) edge (a00)
    (e13) edge (a03)
    (e23) edge (a13)
    (e33) edge (a23)
    (e43) edge (a33)
    (e42) edge (a32)
    (e41) edge (a31)
    (e40) edge (a30);
    \path[arrow]    (a11) edge (e01)
    (a20) edge (e10)
    (a22) edge (e12)
    (a31) edge (e21)
    (a32) edge (e22)
    (a21) edge (e11)
    (a12) edge (e02)
    (a30) edge (e20)
    (a10) edge (e00)
    (a33) edge (e23)
    (a23) edge (e13)
    (a13) edge (e03)
    (a43) edge (e33)
    (a42) edge (e32)
    (a41) edge (e31)
    (a40) edge (e30);
    \path[arrow]    (a01) edge (e22)
    (a10) edge (e31)
    (a11) edge (e32)
    (a00) edge (e21)
    (a02) edge (e23)
    (a12) edge (e33)
    (a22) edge (e43)
    (a21) edge (e42)
    (a20) edge (e41);
    \path[arrow]    (-5.5,3.5) edge (e43)
    (5.5,2.5) edge (e42)
    (2.5,3.5) edge (e13)
    (5.5,0.5) edge (e40)
    (-5.5,1.5) edge (e41)
    (-3.5,3.5) edge (e23)
    (-1.5,3.5) edge (e03)
    (4.5,3.5) edge (e33)
    (5.5,0) edge (e40)
    (5.5,2) edge (e42)
    (-5.5,1) edge (e41)
    (-5.5,3) edge (e43);
    \path[dotted]
    (-5.7,3.7) edge (-5.5,3.5)
    (5.7,2.7) edge (5.5,2.5)
    (2.7,3.7) edge (2.5,3.5)
    (5.7,0.7) edge (5.5,0.5)
    (-3.7,3.7) edge (-3.5,3.5)
    (-1.7,3.7) edge (-1.5,3.5)
    (4.7,3.7) edge (4.5,3.5)
    (-5.7,1.7) edge (-5.5,1.5)
    (5.75,0) edge (5.5,0)
    (5.75,2) edge (5.5,2)
    (-5.75,1) edge (-5.5,1)
    (-5.75,3) edge (-5.5,3);
    \path[arrow]
    (5.5,1) edge (a41)
    (-5.5,2) edge (a42)
    (-5.5,0) edge (a40)
    (5.5,3) edge (a43);
    \path[dotted]
    (5.75,1) edge (5.5,1)
    (-5.75,2) edge (-5.5,2)
    (-5.75,0) edge (-5.5,0)
    (5.75,3) edge (5.5,3);
    \path[-]
    (a30) edge (5.5,.75)
    (a32) edge (5.5,2.75)
    (a31) edge (-5.5,1.75)
    (a23) edge (4,3.5)
    (a03) edge (2,3.5)
    (a13) edge (-3,3.5)
    (a33) edge (-5,3.5)
    (a43) edge (5.5,3.25)
    (a41) edge (5.5,1.25)
    (a40) edge (-5.5,0.25)
    (a42) edge (-5.5,2.25);
    \path[dotted]
    (5.5,.75) edge (5.8,.9)
    (5.5,2.75) edge (5.8,2.9)
    (-5.5,1.75) edge (-5.8,1.9)
    (4,3.5) edge (4.4,3.7)
    (2,3.5) edge (2.4,3.7)
    (-3,3.5) edge (-3.4,3.7)
    (-5,3.5) edge (-5.4,3.7)
    (5.5,3.25) edge (5.8,3.4)
    (5.5,1.25) edge (5.8,1.4)
    (-5.5,.25) edge (-5.8,0.4)
    (-5.5,2.25) edge (-5.8,2.4);
    \path[arrow]
    (sink) edge[loop left] ()
    (e00) edge[bend left=8] (sink)
    (e01) edge[bend right=8] (sink)
    (e02) edge[bend left=8] (sink)
    (e03) edge[bend right=8] (sink);
  \end{tikzpicture}}
  \caption{\label{11-fig-nonterm} The winning region of \Eve in the
    non-termination game on the graphs of \cref{11-fig-mwg,12-fig-sem}.}
\end{figure}
%   Consider the non-termination game on the graphs of%   \cref{11-fig-nonterm}
Finally, one of the most general vector games are "parity@parity
vector game" games, where $C\eqdef\{1,\dots,d\}$ and
$\Omega\eqdef\Parity$.  In order to define a colouring of the "natural
semantics", we assume that we are provided with a **location
  colouring** $\lcol{:}\,\Loc\to\{1,\dots,d\}$.
\decpb[parity vector game with given initial credit{\label{11-pb-parity}A vector system
  $\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,\dd)$, an initial location
  $\loc_0\in\Loc$, an initial credit $\vec v_0\in\+N^\dd$, and a
  location colouring $\lcol{:}\,\Loc\to\{1,\dots,d\}$ for some $d>0$.  {Does \Eve have a strategy to simultaneously avoid the
  sink $\sink$ and fulfil the \index{parity!**see also** vector
  game\protect\mymoot|mymoot}parity objective from $\loc_0(\vec
  v_0)$?\\That is, does she win the parity@parity vector game game
  $(\natural(\?V),\col,\Parity)$ from $\loc_0(\vec v_0)$, where
  $\col(e)\eqdef\lcol(\loc)$ if $\ing(e)=\loc(\vec v)$ for
  some $\vec v\in\+N^\dd$, and $\col(e)\eqdef 1$ if $\ing(e)=\sink$?}

````{admonition} Remark \label{11-nonterm2parity}
  There is a \logspace\ reduction from non-termination to
  parity@parity vector game.
  Indeed, the two games coincide if we pick the constant location
  colouring defined by $\lcol(\loc)\eqdef 2$ for all $\loc\in\Loc$ in
  the parity game.

````

````{admonition} Remark \label{11-cov2parity}
  There is a \logspace\ reduction from coverability to
  parity@parity vector game.  Indeed, by \cref{11-cov2cov}, we can assume
  that $\loc_f\in\Loc_\mEve$ is controlled by \Eve and that the target
  credit is $\vec v_f=\vec 0$ the zero vector.  It suffices
  therefore to add an action $\loc_f\step{\vec 0}\loc_f$ and to colour
  every location $\loc\neq\loc_f$ with $\lcol(\loc)\eqdef 1$ and
  to set $\lcol(\loc_f)\eqdef 2$.

````

The existential initial credit variants of
\crefrange{11-pb-reach}{11-pb-parity} are defined similarly, where
$\vec v_0$ is not given as part of the input, but existentially
quantified in the question.

(11-subsec:undec)=
## Undecidability
The bad news is that, although \crefrange{11-pb-reach}{11-pb-parity}
are all decidable in the one-player case---see
the \hyperref[12-refs]{bibliographic notes} at the end of the
chapter---, they become undecidable in the two-player setting.

````{prf:theorem} NEEDS TITLE 11-th-undec
:label: 11-th-undec

  Configuration reachability, coverability, non-termination, and
  parity@parity vector game vector games, both with given and
  with existential initial credit, are undecidable in any dimension
  $\dd\geq 2$.

````

````{admonition} Proof
:class: dropdown tip

  By \cref{11-cov2reach,12-nonterm2parity}, it suffices to prove the
  undecidability of coverability and non-termination.  For this,
  we exhibit reductions from the halting problem of "deterministic
  Minsky machines" with at least two counters.

  \AP Formally, a deterministic Minsky machine with $\dd$~counters
  $\?M=(\Loc,\Act,\dd)$ is defined similarly to a "vector addition
  system with states" with additional zero test actions
  $a=(\loc\step{i\eqby?0}\loc')$.  The set of locations contains a
  distinguished `halt' location $\loc_\mathtt{halt}$, and for every
  $\loc\in\Loc$, exactly one of the following holds: either (i)
  $(\loc\step{\vec e_i}\loc')\in\Act$ for some $0<i\leq\dd$ and
  $\loc'\in\Loc$, or (ii) $(\loc\step{i\eqby?0}\loc')\in\Act$ and
  $(\loc\step{-\vec e_i}\loc'')\in\Act$ for some $0<i\leq\dd$ and
  $\loc',\loc''\in\Loc$, or (iii) $\loc=\loc_\mathtt{halt}$.  The
  semantics of $\?M$ extends the natural semantics by
  handling zero tests actions $a=(\loc\step{i\eqby?0}\loc')$: we
  define the domain as $\dom a\eqdef\{\loc(\vec v)\mid \vec v(i)=0\}$
  and the image by $a(\loc(\vec v))\eqdef \loc(\vec v)$.  This
  semantics is deterministic, and from any starting vertex of $\natural(\?M)$,
  there is a unique play, which either eventually visits
  $\loc_\mathtt{halt}$ and then the sink in the next step, or keeps
  avoiding both $\loc_\mathtt{halt}$ and the sink
  indefinitely.               
  \AP The halting problem asks, given a deterministic Minsky machine
  and an initial location $\loc_0$, whether it halts, that is, whether
  $\loc_\mathtt{halt}(\vec v)$ is reachable for
  some $\vec v\in\+N^\dd$ starting from $\loc_0(\vec 0)$.  The
  halting problem is undecidable in any dimension
  $\dd\geq 2$ {cite}`Minsky:1967`.
  Thus the halting problem is akin to the coverability of
  $\loc_\mathtt{halt}(\vec 0)$ with given initial credit $\vec 0$,
  but on the one hand there is only one player and on the other hand
  the machine can perform zero tests.

  \begin{figure}[htbp]
    \centering
    \begin{tikzpicture}[auto,on grid,node distance=1.5cm]
      \node(to){$\mapsto$};
      \node[anchor=east,left=2.5cm of to](mm){deterministic Minsky machine};
      \node[anchor=west,right=2.5cm of to](mwg){vector system};
      \node[below=.7cm of to](map){$\rightsquigarrow$};
      \node[left=2.75cm of map](0){$\loc$};
      \node[right=of 0](1){$\loc'$};
      \node[right=1.25cm of map,s-eve](2){$\loc$};
      \node[right=of 2,s-eve](3){$\loc'$};
      \node[below=1.5cm of map](map2){$\rightsquigarrow$};
      \node[left=2.75cm of map2](4){$\loc$};
      \node[below right=.5cm and 1.5cm of 4](5){$\loc''$};
      \node[above right=.5cm and 1.5cm of 4](6){$\loc'$};
      \node[right=1.25cm of map2,s-eve](7){$\loc$};
      \node[below right=.5cm and 1.5cm of 7,s-eve](8){$\loc''$};
      \node[above right=.5cm and 1.5cm of 7,s-adam,inner sep=-1.5pt](9){$\loc'_{i\eqby?0}$};
      \node[below right=.5cm and 1.5cm of 9,s-eve](10){$\loc'$};
      \node[above right=.5cm and 1.5cm of 9,s-adam](11){$\frownie$};
      \path[arrow,every node/.style={font=\scriptsize}]
      (0) edge node{$\vec e_i$} (1)
      (2) edge node{$\vec e_i$} (3)
      (4) edge[swap] node{$-\vec e_i$} (5)
      (4) edge node{$i\eqby?0$} (6)
      (7) edge[swap] node{$-\vec e_i$} (8)
      (7) edge node{$\vec 0$} (9)
      (9) edge[swap] node{$\vec 0$} (10)
      (9) edge node{$-\vec e_i$} (11);
    \end{tikzpicture}
    \caption{\label{11-fig-undec}Schema of the reduction in the proof of \cref{11-th-undec}.}
  \end{figure}
  Here is now a reduction to
  \cref{11-pb-cov}.  Given an instance of the halting problem, i.e.,
  given a deterministic Minsky machine $\?M=(\Loc,\Act,\dd)$ and an
  initial location $\loc_0$, we construct a vector system
  $\?V\eqdef(\Loc\uplus\Loc_{\eqby?0}\uplus\{\frownie\},\Act',\Loc,\Loc_{\eqby?0}\uplus\{\frownie\},\dd)$
  where all the original locations are controlled by~\Eve and
  $\Loc_{\eqby?0}\uplus\{\frownie\}$ is a set of new locations
  controlled by~\Adam.  We use $\Loc_{\eqby?0}$ as a set of
  locations defined by
  \begin{align*}
    \Loc_{\eqby?0}&\eqdef\{\loc'_{i\eqby?0}\mid\exists\loc\in\Loc\mathbin.(\loc\step{i\eqby?0}\loc')\in\Act\}\intertext{and
                   define the set of actions by (see \cref{11-fig-undec})}
    \Act'&\eqdef\{\loc\step{\vec
          e_i}\loc'\mid(\loc\step{\vec e_i}\loc')\in\Act\}\cup\{\loc\step{-\vec e_i}\loc''\mid(\loc\step{-\vec e_i}\loc'')\in\Act\}\\
    &\:\cup\:\{\loc\step{\vec
      0}\loc'_{i\eqby?0},\;\;\:\loc'_{i\eqby?0}\!\!\step{\vec 0}\loc',\;\;\:\loc'_{i\eqby?0}\!\!\step{-\vec e_i}\frownie\mid(\loc\step{i\eqby?0}\loc')\in\Act\}\;.
  \end{align*}
  We use $\loc_0(\vec 0)$ as initial configuration and
  $\loc_\mathtt{halt}(\vec 0)$ as target configuration for the
  constructed coverability instance.  Here is the crux of the
  argument why \Eve has a winning strategy to cover
  $\loc_\mathtt{halt}(\vec 0)$ from $\loc_0(\vec 0)$ if and only if
  the Minsky machine@deterministic Minsky machine halts.
   Consider any configuration $\loc(\vec v)$.  If
  $(\loc\step{\vec e_i}\loc')\in\Act$, \Eve has no choice but to apply
  $\loc\step{\vec e_i}\loc'$ and go to the configuration
  $\loc'(\vec v+\vec e_i)$ also reached in one step in $\?M$.  If
  $\{\loc\step{i\eqby?0}\loc',\loc\step{-\vec e_i}\loc''\}\in\Act$ and
  $\vec v(i)=0$, due to the natural semantics, \Eve cannot use the
  action $\loc\step{-\vec e_i}\loc''$, thus she must use
  $\loc\step{\vec 0}\loc'_{i\eqby?0}$.  Still due to the "natural
  semantics", \Adam cannot use
  $\loc'_{i\eqby?0}\!\!\step{-\vec e_i}\frownie$, thus he must use
  $\loc'_{i\eqby?0}\!\!\step{\vec 0}\loc'$.  Hence \Eve regains the
  control in $\loc'(\vec v)$, which was also the configuration reached
  in one step in $\?M$.  Finally, if
  $\{\loc\step{i\eqby?0}\loc',\loc\step{-\vec e_i}\loc''\}\in\Act$ and
  $\vec v(i)>0$, \Eve can choose: if she uses
  $\loc\step{-\vec e_i}\loc''$, she ends in the configuration
  $\loc''(\vec v-\vec e_i)$ also reached in one step in $\?M$.  In
  fact, she should not use $\loc\step{\vec 0}\loc'_{i\eqby?0}$,
  because \Adam would then have the opportunity to apply
  $\loc'_{i\eqby?0}\!\!\step{-\vec e_i}\frownie$ and to win, as
  $\frownie$ is a deadlock location and all the subsequent moves end
  in the sink.  Thus, if $\?M$ halts, then \Eve has a winning
  strategy that simply follows the unique play of $\?M$, and
  conversely, if \Eve wins, then necessarily she had to follow the
  play of $\?M$ and thus the machine halts.
    
  \medskip Further note that, in a deterministic Minsky machine the
  halting problem is similarly akin to the **complement** of
  non-termination with given initial credit $\vec 0$.  This means
  that, in the vector system
  $\?V=(\Loc\uplus\Loc_{\eqby?0}\uplus\{\frownie\},\Act',\Loc,\Loc_{\eqby?0}\uplus\{\frownie\},\dd)$
  defined earlier, \Eve has a winning strategy to avoid the sink
  from $\loc_0(\vec 0)$ if and only if the given "Minsky
  machine@deterministic Minsky machine" does
  not halt from $\loc_0(\vec 0)$, which shows the undecidability of
  \cref{11-pb-nonterm}.

  \medskip Finally, let us observe that both the existential and the
  universal initial credit variants of the halting problem are also
  undecidable.  Indeed, given an instance of the halting problem,
  i.e., given a deterministic Minsky machine $\?M=(\Loc,\Act,\dd)$
  and an initial location $\loc_0$, we add $\dd$~new locations
  $\loc_\dd,\loc_{\dd-1},\dots,\loc_1$ with respective actions
  $\loc_j\step{-\vec e_j}\loc_j$ and $\loc_j\step{j\eqby?0}\loc_{j-1}$
  for all $\dd\geq j>0$.  This modified machine first resets all its
  counters to zero before reaching $\loc_0(\vec 0)$ and then performs
  the same execution as the original machine.  Thus there exists an
  initial credit $\vec v$ such that the modified machine
  reaches $\loc_\mathtt{halt}$ from $\loc_\dd(\vec v)$ if and only if
  for all initial credits $\vec v$ the modified machine
  reaches $\loc_\mathtt{halt}$ from $\loc_\dd(\vec v)$, if and only if
  $\loc_\mathtt{halt}$ was reachable from $\loc_0(\vec 0)$ in the
  original machine.  The previous construction of a vector system
  applied to the modified machine then shows the undecidability of the
  existential initial credit variants of
  \cref{11-pb-cov,12-pb-nonterm      .

````
