(9-sec:forward_algorithm)=
# Forward Algorithm


```{math}
\newcommand{\Eve}{\textrm{Eve}}
\newcommand{\Adam}{\textrm{Adam}}
\newcommand{\game}{\mathcal{G}}
\newcommand{\arena}{\mathcal{A}}
\newcommand{\Win}{\textrm{Win}}
\newcommand{\Reach}{\mathtt{Reach}}
```

The backward algorithm we just presented is conceptually simple, but
it~is often not very efficient in practice,
as federations tend to grow too much in size in each iteration of the
computation.
The forward algorithm we will now present is more efficient in practice.
It performs a forward exploration and only applies the controllable predecessor along branches
that actually reach the target state from the initial state. If the witness
trace is not excessively long, which is often the case in practice,
this limits the size of the federations.


%develop and implement, but they are usually not very efficient in

%\NM{Give intuition why? Especially, why for timed games?? La

%  convaincante...}

%been designed to gain in efficiency.

We present below the algorithm proposed in {cite}`CDFLL05`,
and as a first step, we explain the untimed version of that algorithm,
based on an algorithm of Liu and Smolka for computing
fixpoints {cite}`LS98`.


## A Forward Algorithm for Finite-State Games


The original algorithm of Liu and Smolka is expressed in terms of
**(pre-)fixpoints** in **dependency graphs**: a~dependency graph
is a pair $G=(V,E)$ in which $E \subseteq V \times 2^V$ relates
states with sets of states.

For any order-preserving 
function $f\colon 2^V\to2^V$
(**order-preserving** meaning non-decreasing for the $\subseteq$-relation),

a~**pre-fixpoint** is a set $X\subseteq V$ for which $f(X)\subseteq
X$; it~is a **fixpoint** if $f(X)=X$. By~Knaster-Tarski theorem, such
functions always admit a least pre-fixpoint which is also the least fixpoint.

%pre-fixpoint and the least fixpoint coincide.

Fix a dependency graph $G=(V,E)$. 
For $W\subseteq V$,
we~define a mapping $f_W\colon 2^V\to 2^V$: for
each $X\subseteq V$, we~let $f_W(X)=W\cup \{v\in V\mid \exists (v,Y)\in
E.\ Y\subseteq X\}$.

%By~Knaster-Tarski theorem, $f_W$~admits a least

%fixpoint.
Clearly, $X\subseteq X'$ implies $f_W(X)\subseteq f_W(X')$, so that $f_W$ admits
a least (pre-)fixpoint.
The~Liu-Smolka
algorithm aims at deciding whether a given vertex $v_0\in V$ belongs
to the least fixpoint of $f_W$.  Classical algorithms for computing
least fixpoints consist in iteratively
computing $(f_W^i(\emptyset))_i$ until convergence (assuming $V$~is
finite). Observe that this corresponds to the algorithm of  {prf:ref}`9-thm:timed-control`
for timed games.
The~Liu-Smolka algorithm proceeds from $v_0$, and explores
the dependency graph until it can claim that $v_0$~is, or that it
is~not, in the least fixpoint of $f_W$.

Before tackling the algorithm, let us link least fixpoints in
dependency graphs and winning sets in concurrent games (with
reachability objectives): with a concurrent arena
$\calC=(V,\Act,\delta,c')$ and a target set $\textrm{Win}, we~associate
the dependency graph $G=(V,E)$, where $(v,T)\in E$ whenever $v\in V$
and $T\subseteq V$ is such that there exists an action $a$ for which
$T=\{v' \mid \exists a'\in\Act.\ v'=\delta(v,a,a')\}$.  Then for any
set $X\subseteq V$, the~set $f_{\textrm{Win}(X)$ contains $\textrm{Win} and all the
states from which Eve can force a visit to $X$ in one step.
We~then~have:

````{prf:proposition} NEEDS TITLE 9-prop:fixp-game
:label: 9-prop:fixp-game

The least fixpoint of $f_{\textrm{Win}$ in $G$ corresponds to the set $W$ of
winning states for~\textrm{Eve}in $\calC$.

````


````{admonition} Proof
:class: dropdown tip

  The winning states of~\textrm{Eve}form a pre-fixpoint of $f_{\textrm{Win}$
  containing~\textrm{Win} indeed, for any $v\in f_{\textrm{Win}(W)$, either $v\in
  \textrm{Win}, or \textrm{Eve}has an action to move from $v$ to some state
  in $W$. Hence $v$ is winning, i.e., $v\in W$.
  

%  are all winning. Hence all the states in the least fixpoint of $f_{\textrm{Win}$ 

  Conversely, from any state $v$ that is not in the least
  pre-fixpoint $X$, for any~edge $(v,T)$, there is a state $v'\in T$
  that again is not in $X$. This defines a strategy for \textrm{Adam}to avoid
  reaching $\textrm{Win}, so that \textrm{Eve}does not have a winning strategy from $v$.

````



\begin{algorithm}
  \SetKwFunction{Pop}{pop}\SetAlgoNoEnd
  \KwData{A dependency graph $G=(V,E)$, a~set $W\subseteq V$, a~node $v_0\in V$}
  \KwResult{Is $v_0$ in the least fixpoint of $f_W$?}

  
  
  \For{$v\in V$}{\lIf{$v\in W$}{$F(v):=1$}
    \lElseIf{$v==v_0$}{$F(v):=0$}
            \lElse{$F(v):=\bot$}}
  
  $\Dep(v_0):=\emptyset$;

  $\Wait:=\{(v,T)\in E \mid v=v_0\}$;

  \While{($\Wait\not=\emptyset$ and $F(v_0)==0$)}
        {$(v,T):=\Pop{\Wait}$;\\
          \If({// case 1}){$F(v)==0$ and $\forall v'\in T.\ F(v')==1$}
             {$F(v):=1$;\\
              $\Wait:=\Wait\cup\Dep(v)$;}
          \ElseIf({// case 2}){$\exists v'\in T.\ F(v')==0$}
                {$\Dep(v'):=\Dep(v') \cup \{(v,T)\}$;}
                \ElseIf({// case 3}){$\exists v'\in T.\ F(v')==\bot$}
                  {$F(v'):=0$; \\
                  $\Dep(v'):=\{(v,T)\}$;\\
                  $\Wait:=\Wait\cup\{(w,U)\in E \mid w=v'\}$;
                  }
                  }
                  \Return{$F(v_0)$}
  \caption{Liu-Smolka algorithm\protect\footnotemark for least fixpoint of $f_W$}
  \label{9-algo:LS98}
\end{algorithm}
\footnotetext{Our version of the algorithm slightly differs from the
  original one {cite}`LS98`: we~let $\Dep(v'):=\{(v,T)\}$ at the penultimate line
  of the **while** loop (which otherwise results in a wrong
  result, as~already noticed in {cite}`JLSO13`), reinforce the
  condition for case $1$ (which otherwise would not guarantee
  termination), and reinforce the condition of the **while** loop
  to get earlier termination.}

%
%
%
%

{numref}`9-algo:LS98` can be seen as an alternation of forward
exploration and backward propagation. Intuitively, the algorithm first
explores the graph in a forward manner, remembering for each node $v$
the set $\Dep(v)$ of nodes that **depend** on $v$, and have to be
reexplored if the status of $v$ is updated.

%the parent of

For~each $v$, the algorithm maintains a
value $F(v)$, which is $\bot$ if $v$ has not been explored~yet,
$0$~if $v$~has been explored but not yet been shown to be winning, 
and $1$ if $v$ is known to be winning. 
% edge $e=(v,T)$, if some vertex $v'\in T$ has $F(v)=0$, then $e$ is

%The function $F$ is used to mark whether a given vertex has not been explored yet ($\bot$),

Whenever a vertex $v$ whose all successors are winning is found, the value of $v$ is set to $1$, and its parents (in $\Dep(v)$)
are scheduled to be visited again to check whether their statuses have to be changed.
This is how the backward propagation is triggered; in~fact, the~search will climb in the tree as long as the values of
vertices can be updated to $1$.

%Thus, the backward propagation is only triggered when the value of some node becomes $1$ so as to update its parents in the exploration.


% fixpoint of $f_W$. For~each $v$, the algorithm computes a

% $0$~if $v$~has been explored but not yet been shown to belong to $S$,

% edge $e=(v,T)$, if some vertex $v'\in T$ has $F(v)=0$, then $e$ is

% in case $F(v')$ is eventually set to $1$. Notice that for any $v\in

%\NM{Should we say more? We are just rephrasing the algo...}

 
 
 
 
 
 

The correctness of this algorithm relies on the following lemma:

````{prf:lemma} {cite}`LS98`
:label: 9-lemma:ls98

  The following properties hold at the end of each run in the
  **while** loop of {numref}`9-algo:LS98`:
  
  *  for any $v\in V$, if $F(v)=1$, then $v$ belongs to the least
    fixpoint containing $W$;
  *  for any $v\in V$ with $F(v)=0$, and any $(v,T)\in E$, either
    $(v,T)\in \Wait$ or $(v,T)\in\Dep(v')$ for some $v'\in T$ with
    $F(v')=0$.
  

````


````{admonition} Proof
:class: dropdown tip

  We~fix an execution of {numref}`9-algo:LS98`, and prove that both
  claims are true at the beginning and end of each iteration through
  the **while** loop. To~clarify the presentation, we~use
  superscript $i$ to indicate the value of variables at the end of the
  $i$-th run through the loop, so that $\Wait^3$ is the value of
  variable $\Wait$ after three iterations (and $\Wait^0$ is its value
  after initialization). In~particular, $(v^i,T^i)$ is the
  symbolic transition popped from the $\Wait$ list during the $i$-th
  iteration (and is not defined for $i=0$).

  Let us first prove the first property: the initialization phase
  clearly enforces that if $F^0(x)=1$, then $x\in W$, which is
  included in any fixpoint of $f_W$. Now, assume that the property
  holds true at the beginning of the $i$-th run through the loop
  (i.e.,~if $F^{i-1}(x)=1$, then $x$ is in the least fixpoint), and
  pick some $x\in V$ such that $F^i(x)=1$. If $F^{i-1}(x)=1$, our
  result follows; if~not, then the $i$-th iteration of the loop must
  have run via case $1$, hence $F^{i-1}(x')=1$ for all $x'\in
  T^i$. By~our induction hypothesis, this indicates that $T^i$ is part
  of the least fixpoint, and by definition of $f_W$, $x$~must also
  belong to the least fixpoint.

  
  
  
  
  
  
  
  
  
  

  \smallskip
  The second statement also clearly holds after initialization:
  initially, $F^0(x)=0$ only for $x=v_0$, and all transitions
  from $v_0$ have been stored in $\Wait^0$. We~now assume that the
  property holds when entering the **while** loop for the $i$-th
  time, and consider $x$ such that $F^i(x)=0$ at the end of that
  loop. We~pick $(x,Y)\in E$.
  
  *  if the $i$-th run through the loop visits case $1$, then
    already $F^{i-1}(x)=0$ (hence $x\not=v^i$). Then either
    $(x,Y)\in\Wait^{i-1}$, or $(x,Y)\in\Dep^{i-1}(x')$ for some $x'\in Y$
    with $F(x')=0$. In~the former case: since $x\not=v^i$,
    if $(x,Y)\in\Wait^{i-1}$ then also $(x,Y)\in \Wait^i$;

%    
%    
    in the latter case: if $(x,Y)\in\Dep^{i-1}(x')$ for some $x'\in Y$
    with $F(x')=0$, then **(i)**~either $x'=v^i$, and
    $(x,Y)\in\Wait^i$ because $\Dep^{i-1}(v^i)\subseteq \Wait^i$
    (last~line of case $1$), **(ii)**~or ${x'\not=v^i}$, and
    $(x,Y)\in \Dep^{i-1}(x')=\Dep^{i}(x')$ and $F^i(x')=F^{i-1}(x')=0$.

  *  if the $i$-th run goes to case $2$, then again $F^{i-1}(x)=0$,
    and the induction hypothesis applies: either $(x,Y)$ is
    in $\Wait^{i-1}$, or~it is in $\Dep^{i-1}(x')$ for some $x'\in Y$
    with $F^{i-1}(x')=0$. For the latter case, observe that
    $\Dep^{i-1}(x')\subseteq \Dep^i(x')$, and $F^{i}(x')=F^{i-1}(x')$
    when running case $2$; for the former case, we~have
    $\Wait^i=\Wait^{i-1}\setminus\{(v^i,T^i)\}$, so that $(x,Y)$
    remain in $\Wait^i$ if $(x,Y)\not=(v^i,T^i)$; finally,
    if $(x,Y)=(v^i,T^i)$, then case $2$ precisely adds $(v^i,T^i)$
    to $\Dep^i(v')$ for some $v'\in T^i$ with $F^i(v')=0$, which concludes
    the proof for this case.

  *  for case $3$, we~first consider the case where $x$ is the
    state $v'$ selected at the beginning of case $3$: in~that case,
    all transitions from $x$ are added to $\Wait$, so that
    $(x,Y)\in\Wait^i$. Now, if $x$ is not the selected state $v'$,
    then $F^{i-1}(x)=0$, and again either $x\in\Wait^{i-1}$ or
    $x\in\Dep^{i-1}(x')$ for some $x'\in Y$ with
    $F^{i-1}(x')=0$. The~latter case is preserved when running
    case $3$; if $x\in\Wait^{i-1}$: if $(x,Y)\not=(v^i,T^i)$, then
    $x\in\Wait^i$, while if $(x,Y)=(v^i,T^i)$, then
    $(x,Y)\in\Dep^i(v')$ for the state $v'\in T^i$ selected at the
    beginning of case $3$ (and~for which $F^i(v')=0$).
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
%
  
  
  
  
  
  
  
%
  
  
  
  
  
  
  
  
  

````

As a corollary, if the algorithm terminates after $n$ rounds of the
**while** loop, then either $F^n(v_0)=1$, or
$F^n(v_0)=0$ and $\Wait^n=\emptyset$.

*  From the first claim of the lemma above, the former case entails
  that $v_0$ belongs to the least fixpoint.
*  Now consider the second case, and let $B=\left\{v\in V\mid
  F^n(v)\in \{\bot,1\}\right\}$. We prove that $f_W(B)\subseteq
  B$. For this, we~pick $v\in f_W(B)$:
  \begin{itemize}
  *  if $v\in W$, then $F(v)$~is set to $1$ initially, and may
    never be changed, so that $v\in B$;
  *  otherwise, there is a transition $(v,T)$ such that $T\subseteq
    B$. If $v\notin B$, then $(v,T)\in\Dep^n(v')$ for some $v'\in T$
    with $F^n(v')=0$, which contradicts the fact that $T\subseteq B$.
  
  This proves that $f_W(B)\subseteq B$, so that $B$ is a pre-fixpoint
  of $f_W$. It~thus contains the least (pre-)fixpoint of $f_W$, so
  that any state $v$ not in $B$ (i.e., with $F^n(v)=0$) for sure does
  not belong to that least fixpoint. In~particular, $v_0$ is not in
  the fixpoint.
\end{itemize}

%
%
%
%
%
%
%

%
%
%
%

\medskip
It~remains to prove termination. For this, we~first notice that, for
any hyper-edge $(v,S)$, if $(v,S)\in\Dep^i(v')$ then $(v,S)\in\Wait^j$
for some $j<i$, and if $(v,S)\in\Wait^j$ or $(v,S)\in\Dep^j(v')$ for
some $v'$, then $F^j(v)\not=\bot$.

We~then set

$$
M= 
2\size{\Wait} + 
2\hskip-4pt\sum_{v\text{ s.t. }F(v)=\bot}\hskip-4pt \size{\{(v,S)\in E\}} 
+ \hskip-4pt\sum_{v\text{ s.t. }F(v)=0}\hskip-4pt \size{\Dep(v)}
- \hskip-4pt\sum_{v\text{ s.t. }F(v)=1}\hskip-4pt \size{\Dep(v)}

%+ \sum_{v\mid F(v)=0} \sum_{(v',S)\in \Dep(v)} (|S|+1).
$$

again writing $M^i$ for the value of $M$ after the $i$-th run through
the **while** loop.  This value is at most $2\size{E}$ when
entering the **while** loop for the first time; clearly, it~can
never go below $-\size{E}$. We~now prove that $M^{i}<M^{i-1}$,

which implies termination of the algorithm.

Consider the $i$-th run through the loop, popping $(v^i,T^i)$
from $\Wait^{i-1}$ (which decreases $M$ by $2$). We~consider all three cases:

*  if~case $1$ applies, $F^i(v)$ is set to $1$.
  The~set $\Dep^{i-1}(v)$ is added to $\Wait^i$. This globally
  leaves $M$ unchanged, so that globally $M^i=M^{i-1}-2$;
*  if~case $2$ applies, $\Dep^{i-1}(v')$~is augmented by (at~most) one edge,
  and since $F^i(v')=0$, this increases $M$ by at most $1$. Hence globally
  $M^i\leq M^{i-1}-1$;
*  finally, case $3$ increases $M$ by $1$: the edges added
  to $\Wait$ are compensated by the fact that $F(v')$ no longer
  is $\bot$, and only one extra edge has to be considered in the
  second sum. Hence again $M^i\leq M^{i-1}-1$.

This concludes the correctness proof of {numref}`9-algo:LS98`.

````{prf:theorem} NEEDS TITLE AND LABEL 
{numref}`9-algo:LS98` terminates, and returns $1$ if, and only~if,
$v_0$~belongs to the least fixpoint of $f_W$.
 

{numref}`9-algo:LS98` terminates, and returns $1$ if, and only~if,
$v_0$~belongs to the least fixpoint of $f_W$.

````

Using {prf:ref}`9-prop:fixp-game`, we~get a **forward** algorithm for
deciding if a given state of a concurrent game is winning
for~Eve. This corresponds to the OTFUR algorithm
of {cite}`CDFLL05`.


%
%
%
%
%
%
%
%
%
%
%
%
%
%

%
%
%
%
%
%
%
%
%
%

%
%
%
%

%
%
%

%





%
%
%
%
%
%
%
%
%
%
%
%
%
%
%


## Extension to Timed Games

%
%
%

We now explain how to adapt the algorithm above to (infinite-state)
timed games. 

For~efficiency, the~algorithm relies on zones (and~DBMs); instead of
computing whether a given zone $(\ell,Z)$ is winning, the~algorithm
maintains, for each~zone $S=(\ell,Z)$ it~explores, a~subzone $(\ell,Z')$ of
configurations that it knows are winning; this subzone is stored as
$F(S)$, and is updated during the execution.
As~in {numref}`9-algo:LS98`, a~waiting list keeps track of the
zones to be explored, and a dependency list stores the list of nodes
to be revisited upon update of the winning subzone of a zone.
The algorithm is given in {numref}`9-algo:sotftr`.

%computing for each explored zone $Z$ of the timed game,

%configurations. {numref}`9-algo:sotftr` follows the same ideas as

%re-evaluating transitions upon update of the winning subzone.

%
%
%
%
%
%

\begin{algorithm}
  \SetKwFunction{Pop}{pop}\SetAlgoNoEnd
  \KwData{A reachability timed game $\mathcal{G}(\mathcal{A} \mathtt{Reach}\textrm{Win})$,
    a~location $\ell_0\in \Locs$}
  \KwResult{Is $(\ell_0,\mathbf{0})$ winning for Eve?}

  $S_0:=\posttime(\ell_0,\mathbf 0)$;
  
  
  
  

  \leIf{$c(S_0)==\textrm{Win}}{$F(S_0):=S_0$}{$F(S_0):=\emptyset$}

  $\Passed:=\{S_0\}$;  
  // $\Passed$ stores all configurations for which $F$ is defined
    

  
  $\Dep(S_0):=\emptyset$;

  $\Wait:=\{(S_0,\alpha,T) \mid 
    T=\posttime(\postta_{\alpha}(S_0))\not=\emptyset, \alpha\text{ transition of }\mathcal{G}}$;

  \While{($\Wait\not=\emptyset$ and $(v_0,\mathbf 0)\notin F(S_0)$)}
        {$(S,\alpha,T)):=\Pop{\Wait}$;\\
          \If({// case $A$}){$T\in\Passed$}
          {$\Dep(T):=\Dep(T) \cup \{(S,\alpha,T)\}$;\\
          $W:=\predt\left(F(S)\cup \bigcup_{\substack{S\xrightarrow{c} V\\ \!\!V\in\Passed\!\!}} \predc(F(V)),\ \bigcup_{\substack{S\xrightarrow{u} V\\ \!\!V\in\Passed\!\!}}\predu(V\setminus F(V))\right) \cap S$;\\
          \If{$F(S) \subsetneq W$}{$F(S):=W$;\\
              $\Wait:=\Wait\cup\Dep(S)$;}}
          \Else({// case $B$})
                  {$\Passed:=\Passed \cup\{T\}$; \\
                    \If{$c(T)==\textrm{Win}}{$F(T):=T$\\ $\Wait:=\Wait\cup\{(S,\alpha,T)\}$}
                       \Else{$F(T):=\emptyset$}
                  $\Dep(T):=\{(S,\alpha,T)\}$;\\
                  $\Wait:=\Wait\cup\{(T,\alpha,U) \mid U=\posttime(\postta_{\alpha}(T))\not=\emptyset, \alpha\text{ transition of }\mathcal{G}}$;
        }
        }
  \leIf{$(v_0,\mathbf 0)\in F(S_0)$}{\Return 1}{\Return 0}

        \caption{Symbolic on-the-fly algorithm for timed reachability}
  \label{9-algo:sotftr}
\end{algorithm}



The correctness of the algorithm can be proven using the following
lemma. We~omit the proof of this lemma, as it is tedious and and does
not contain any difficult argument.

````{prf:lemma} NEEDS TITLE 9-lem:sotftr
:label: 9-lem:sotftr

  The following properties hold at the end of each run through
  the **while** loop of {numref}`9-algo:sotftr`:
  
  *  for any $S\in\Passed$ and any transition $\alpha$, if
    $T=\posttime(\postta_\alpha(S))\not=\emptyset$,
    then either $(S,\alpha,T)\in\Wait$, or
    $T\in\Passed$ and $(S,\alpha,T)\in\Dep(T)$;
  *  for any $S\in\Passed$ and $q\in F(S)$,  $q$ is winning for~Eve;
  *  for any $S\in\Passed$ and $q\in S\setminus F(S)$,
    either
    
    $\Wait$ contains a symbolic transition $(S,\alpha,S')$ from $S$
    with $S'\in\Passed$,
    
    
    
    or
    

$$
      q\notin \predt\Bigl(F(S)\cup \bigcup_{\substack{S\xrightarrow{c} V\\ V\in\Passed}} \predc(F(V)),\ \bigcup_{\substack{S\xrightarrow{u} V\\ V\in\Passed}} \predu(V\setminus F(V))\Bigr) \cap S.
    $$

  

````

The proof is omitted but can be found in {cite}`CDFLL05`.

%je ne sais pas comment le citer correctement \href{}{https://hal.archives-ouvertes.fr/hal-00350475} sans dupliquer la version concur}

%
%
%
%
%
%
%
%

%
%
%
%
%
%
%

%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%

%
%
%
%
%
%
%
%

%
%
%
%
%
%
%
%
%
%
%
%
%

%
%
%
%
%
%
%
%
%
%
%

%
%
%
%
%
%
%
%
%
%

%
%
%

%
%

%
%
%
%
%
%
%
%
%
%
%
%
%
    

%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%


%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%
%


Using these invariants, we get the following result:

````{prf:lemma} NEEDS TITLE AND LABEL 
  If {numref}`9-algo:sotftr` terminates, all configurations in $F(S)$ for
  any $S\in\Passed$ are winning for~Eve;  if~additionally
  $\Wait=\emptyset$, then all configurations in $S\setminus F(S)$, for
  any $S\in\Passed$, are losing for~Eve.
 

  If {numref}`9-algo:sotftr` terminates, all configurations in $F(S)$ for
  any $S\in\Passed$ are winning for~Eve;  if~additionally
  $\Wait=\emptyset$, then all configurations in $S\setminus F(S)$, for
  any $S\in\Passed$, are losing for~Eve.

````


````{admonition} Proof
:class: dropdown tip

The~first statement corresponds to the second statement of
 {prf:ref}`9-lem:sotftr`. Now, assume $\Wait^n=\emptyset$ after
termination at the $n$-th step,
and

let $L=\{q\in \Locs\times\mathbb{R}_{\geq 0}^{\Clocks} \mid \exists
S\in\Passed^n.\ q\in S\setminus F^n(S)\}$, and $M$ be the complement
of $L$. For~any $S\in\Passed^n$, we~then have $M\cap S\subseteq
F^n(S)$.

%  and $q \not \in F(S_2)$?}

%  Since $q\in S$, then $q \in F^n(S)$.}

Pick $q\in \pi(M)\cup \textrm{Win}, where we abusively write $\textrm{Win} to denote
all configurations with location colored $\textrm{Win}. We~prove that $q\in M$:

*  if $q\in\textrm{Win}: assume $q\in L$, and pick $S\in\Passed^n$ such
  that $q\in S\setminus F^n(S)$. Since $q\in S$, it~holds $c(S)=\textrm{Win};
  but then $F^n(S)$ is defined (since $S\in\Passed^n$), and it
  equals $S$ by initialization of $F$. This contradicts the fact that
  $q\in S\setminus F^n(S)$, hence $q\in M$.
*  if $q\in\pi(M)$: we again assume $q\in L$. Then for some
  $S\in\Passed^n$, $q\in S\setminus F^n(S)$. By~the third property of
   {prf:ref}`9-lem:sotftr`, $q\notin W^n$

  
  (because $\Wait^n$ is
  empty).  Since $M\cap U \subseteq F^n(U)$ for all $U\in\Passed^n$
  and $F^n(U)=\emptyset$ for all $U\notin\Passed^n$,
  and by monotonicity, we~get
  

$$
  q\notin\predt\Biggl((M\cap S)\cup \bigcup_{\substack{S\xrightarrow{c}
    V}} \predc(M\cap V),\ \bigcup_{\substack{S\xrightarrow{u}
    V}} \predu(V\setminus (M\cap V))\Biggr) \cap S.
  $$

  
  
%
  Now, notice that any $S\in\Passed^n$ is closed under $\posttime$. Then
  \begin{xalignat*}1
    \pi(M)\cap S &= \predt(M\cup\predc(M), \predu(\overline M)) \\
     &= \predt((M\cap S)\cup (\predc(M)\cap S), \predu(\overline M)).
  \end{xalignat*}
  Now, it~can be checked that $\predc(M)\cap S \subseteq
  \bigcup_{\substack{S\xrightarrow{c} V}} \predc(M\cap V)$ and
  $\predu(\overline M) \supseteq \bigcup_{\substack{S\xrightarrow{u}
      V}} \predu(V\setminus (M\cap V))$.  So the fact that $q\in
  \pi(M)$ and $q\in S$ leads to a contradiction. This entails that
  $q\notin L$, hence $q\in M$.

In the end, we~have proven that $\pi(M)\cup\textrm{Win}\subseteq M$, so that
$M$ is a pre-fixpoint of $X\mapsto \pi(X)\cup\textrm{Win}, hence it~contains
all winning configurations of~\textrm{Eve}and $L$ only contains losing
configurations.

````


%\NM{termination relies on extrapolation... Explain?}

The procedure given in {numref}`9-algo:sotftr` will in general not
terminate: as in the case of timed automata, the number of zones
generated by the algorithm may be infinite. This is classically
avoided using **extrapolation**: this consists in abstracting the
zones being considered by larger zones, defined by only using integer
constants less than the maximal constant appearing in the timed arena
(as we did for regions in the proof
of {prf:ref}`9-thm:timed-control`). This can be proven to preserve
correctness, and makes the~number of zones finite. Termination follows
by noticing that any triple $(S,\alpha,T)$ may be added to $\Wait$ only
a finite number of times (bounded by the number of regions
in $T$). 

We~can then conclude:

````{prf:theorem} NEEDS TITLE AND LABEL 
{numref}`9-algo:sotftr` terminates when extrapolation is used, and returns $1$ if, and only~if,
$(\ell_0,\mathbf{0})$~is winning for~\textrm{Eve}
 

{numref}`9-algo:sotftr` terminates when extrapolation is used, and returns $1$ if, and only~if,
$(\ell_0,\mathbf{0})$~is winning for~\textrm{Eve}

````

