(11-sec:avag)=
# Asymmetric games

```{math}

\newcommand{\capp}[2][C]{\overline{\vec #2}^{#1}}

```

{prf:ref}`11-th:undec` shows that vector games are too powerful to be
algorithmically relevant, except in dimension one where
{prf:ref}`11-th:dim1` applies.  This prompts the study of restricted kinds
of vector games, which might be decidable in arbitrary dimension.
This section introduces one such restriction, called
**asymmetry**, which turns out to be very fruitful: it yields
decidable games (see Section {ref}`11-sec:complexity`), and is
related to another class of games on counter systems called energy
games (see Section {ref}`11-sec:resource`).

> **Asymmetric Games**

 A vector system
$\mathcal{V}=( \mathcal{L}, A, \mathcal{L}_\mathrm{Eve}, \mathcal{L}_\mathrm{Adam}, k)$ is
asymmetric\index{asymmetry|see{vector system}} if, for all
locations $\ell\in \mathcal{L}_\mathrm{Adam}$ controlled by Adam and all actions
$( \ell \xrightarrow{\,\vec u,} \ell')\in A$ originating from those,
$\vec u=\vec 0$ the zero vector.  In other words, Adam may only
change the current location, and cannot interact directly with the
counters.

````{prf:example} Asymmetric vector system
:label: 11-ex:avg

  {numref}`11-fig:avg` presents an asymmetric vector system of
  dimension two with locations partitioned as $\mathcal{L}_\mathrm{Eve}=\{ \ell, \ell_{2,1}, \ell_{\text-1,0}\}$ and $\mathcal{L}_\mathrm{Adam}=\{ \ell'\}$
  
  .  We omit the labels on the actions originating from Adam\'s
  locations, since those are necessarily the zero vector.  It is
  worth observing that this vector system behaves quite differently
  from the one of {prf:ref}`11-ex:mwg` on \cpageref{11-ex:mwg}: for
  instance, in $\ell'(0,1)$, Adam can now ensure that the sink will
  be reached by playing the action $\ell' \xrightarrow{\,0,0,} \ell_{\text-1,0}$,
  whereas in {prf:ref}`11-ex:mwg`, the action $\ell' \xrightarrow{\,-1,0,} \ell$
  was just inhibited by the natural semantics.

````

```{figure} ./../FigAndAlgos/11-fig:avg.png
:name: 11-fig:avg
:align: center
An asymmetric vector system.
```

(11-sec:reach)=
## The Case of Configuration Reachability

In spite of the restriction to asymmetric vector systems,
configuration reachability remains undecidable.

````{prf:theorem} Reachability in asymmetric vector games is undecidable
:label: 11-th:asym-undec

  Configuration reachability asymmetric vector games, both with
  given and with existential initial credit, are undecidable in
  any dimension $k\geq 2$.

````

````{admonition} Proof
:class: dropdown tip

  We first reduce from the halting problem of deterministic Minsky
  machines to configuration reachability with given initial
  credit.  Given an instance of the halting problem, i.e., given
  $\mathcal{M}=( \mathcal{L}, A, k)$ and an initial location $\ell_0$ where we
  assume without loss of generality that $\mathcal{M}$ checks that all its
  counters are zero before going to $\ell_\mathtt{halt}$, we construct
  an asymmetric vector system
  $\mathcal{V}  \stackrel{\!\,\!\,\textrm{def}}{=}( \mathcal{L}\uplus \mathcal{L}_{ \stackrel{\!\,\!\,\textrm{?0}}{=}}\uplus \mathcal{L}_{ k}, A', \mathcal{L}\uplus \mathcal{L}'_{ \stackrel{\!\,\!\,\textrm{?0}}{=}}, \mathcal{L}_{ \stackrel{\!\,\!\,\textrm{?0}}{=}}, k)$
  where all the original locations and $\mathcal{L}_{ k}$ are
  controlled by Eve and $\mathcal{L}_{ \stackrel{\!\,\!\,\textrm{?0}}{=}}$ is controlled by Adam.

```{figure} ./../FigAndAlgos/11-fig:asym-undec.png
:name: 11-fig:asym-undec
:align: center
Schema of the reduction in the proof of {prf:ref}`11-th:asym-undec`.
```

  We
  use $\mathcal{L}_{ \stackrel{\!\,\!\,\textrm{?0}}{=}}$ and $\mathcal{L}_{ k}$ as two sets of locations disjoint from $\mathcal{L}$ defined by
  
$$

     \mathcal{L}_{ \stackrel{\!\,\!\,\textrm{?0}}{=}}&  \stackrel{\!\,\!\,\textrm{def}}{=}\{ \ell'_{i \stackrel{\!\,\!\,\textrm{?0}}{=}}\in \mathcal{L}\times\{1,\dots, k\}\mid\exists \ell\in \mathcal{L}\mathbin.( \ell \xrightarrow{\,i \stackrel{\!\,\!\,\textrm{?0,}}{=}} \ell')\in A\}\\
     \mathcal{L}_{ k}&  \stackrel{\!\,\!\,\textrm{def}}{=}\{ \ell_{i}\mid 1\leq i\leq  k\}
    \intertext{and define the set of actions by (see {numref}`11-fig:asym-undec`)}
     A'&  \stackrel{\!\,\!\,\textrm{def}}{=}\{ \ell \xrightarrow{\,\vec
          e_i,} \ell'\mid( \ell \xrightarrow{\,\vec e_i,} \ell')\in A\}\cup\{ \ell \xrightarrow{\,-\vec e_i,} \ell''\mid( \ell \xrightarrow{\,-\vec e_i,} \ell'')\in A\}\\
    &\:\cup\:\{ \ell \xrightarrow{\,\vec
      0,} \ell'_{i \stackrel{\!\,\!\,\textrm{?0}}{=}},\;\;\: \ell'_{i \stackrel{\!\,\!\,\textrm{?0}}{=}}\!\! \xrightarrow{\,\vec
      0,} \ell',\;\;\: \ell'_{i \stackrel{\!\,\!\,\textrm{?0}}{=}}\!\! \xrightarrow{\,\vec 0,} \ell_{i}\mid
      ( \ell \xrightarrow{\,i \stackrel{\!\,\!\,\textrm{?0,}}{=}} \ell')\in A\}\\
    &\:\cup\:\{ \ell_i\! \xrightarrow{\,-\vec e_j,} \ell_{i},\;\;\: \ell_{i}\! \xrightarrow{\,\vec
      0,} \ell_\mathtt{halt}\mid 1\leq i,j\leq k, j\neq i\}\;.
  
$$

  We use $\ell_0(\vec 0)$ as initial configuration and
  $\ell_\mathtt{halt}(\vec 0)$ as target configuration for the
  constructed configuration reachability instance.  Here is the crux
  of the argument why Eve has a winning strategy to reach
  $\ell_\mathtt{halt}(\vec 0)$ from $\ell_0(\vec 0)$ if and only if
  the Minsky machine halts, i.e., if
  and only if the Minsky machine
  reaches $\ell_\mathtt{halt}(\vec 0)$.
  
  Consider any configuration $\ell(\vec v)$.  If
  $( \ell \xrightarrow{\,\vec e_i,} \ell')\in A$, Eve has no choice but to apply
  $\ell \xrightarrow{\,\vec e_i,} \ell'$ and go to the configuration
  $\ell'(\vec v+\vec e_i)$ also reached in one step in $\mathcal{M}$.  If
  $\{ \ell \xrightarrow{\,i \stackrel{\!\,\!\,\textrm{?0,}}{=}} \ell', \ell \xrightarrow{\,-\vec e_i,} \ell''\}\in A$ and
  $\vec v(i)=0$, due to the natural semantics, Eve cannot use the
  action $\ell \xrightarrow{\,-\vec e_i,} \ell''$, thus she must use
  $\ell \xrightarrow{\,\vec 0,} \ell'_{i \stackrel{\!\,\!\,\textrm{?0}}{=}}$.  Then, either Adam plays
  $\ell'_{i \stackrel{\!\,\!\,\textrm{?0}}{=}}\!\! \xrightarrow{\,\vec 0,} \ell'$ and Eve regains the
  control in $\ell'(\vec v)$, which was also the configuration reached
  in one step in $\mathcal{M}$, or Adam plays
  $\ell'_{i \stackrel{\!\,\!\,\textrm{?0}}{=}}\!\! \xrightarrow{\,\vec 0,} \ell_{i}$ and Eve 
  regains the control in $\ell_{i}(\vec v)$ with
  $\vec v(i)=0$.  Using the actions
  $\ell_{i}\! \xrightarrow{\,-\vec e_j,} \ell_{i}$ for
  $j\neq i$, Eve can then reach $\ell_{i}(\vec 0)$ and move
  to $\ell_\mathtt{halt}(\vec 0)$.  Finally, if
  $\{ \ell \xrightarrow{\,i \stackrel{\!\,\!\,\textrm{?0,}}{=}} \ell', \ell \xrightarrow{\,-\vec e_i,} \ell''\}\in A$ and
  $\vec v(i)>0$, Eve can choose: if she uses
  $\ell \xrightarrow{\,-\vec e_i,} \ell''$, she ends in the configuration
  $\ell''(\vec v-\vec e_i)$ also reached in one step in $\mathcal{M}$.  In
  fact, she should not use $\ell \xrightarrow{\,\vec 0,} \ell'_{i \stackrel{\!\,\!\,\textrm{?0}}{=}}$,
  because Adam would then have the opportunity to apply
  $\ell'_{i \stackrel{\!\,\!\,\textrm{?0}}{=}}\!\! \xrightarrow{\,\vec 0,} \ell_{i}$, and in
  $\ell_{i}(\vec v)$ with $\vec v(i)>0$, there is no way to
  reach a configuration with an empty $i$th component, let alone to
  reach $\ell_\mathtt{halt}(\vec 0)$.  Thus, if $\mathcal{M}$ halts, then Eve 
  has a winning strategy that mimics the unique play
  of $\mathcal{M}$, and conversely, if Eve wins, then necessarily she had to
  follow the play of $\mathcal{M}$ and thus the machine halts.

 Finally, regarding the existential initial credit
  variant, the arguments used in the proof of {prf:ref}`11-th:undec` apply
  similarly to show that it is also undecidable.

````

In dimension one, {prf:ref}`11-th:dim1` applies, thus configuration
reachability is decidable in $\textrm{EXPSPACE}$.  This bound is actually
tight.

````{prf:theorem} Asymmetric vector games are $\textrm{EXPSPACE}$-complete in dimension one
:label: 11-th:asym-dim1

  Configuration reachability asymmetric vector games, both with
  given and with existential initial credit,
  are $\textrm{EXPSPACE}$-complete in dimension one.

````

````{admonition} Proof
:class: dropdown tip

  Let us first consider the existential initial credit variant.  We
  proceed as in {prf:ref}`11-th:countdown-given` and {prf:ref}`11-th:countdown-exist` and
  reduce from the acceptance problem for a deterministic Turing
  machine working in exponential space $m=2^{p(n)}$.  The reduction is
  mostly the same as in {prf:ref}`11-th:countdown-given`, with a few changes.
  Consider the integer $m-n$ from that reduction.  While this is an
  exponential value, it can be written as $m-n=\sum_{0\leq e\leq
  p(n)}2^{e}\cdot b_e$ for a polynomial number of bits $b_0,\dots,b_{p(n)}$.
  For all $0\leq d\leq p(n)$, we define $m_d  \stackrel{\!\,\!\,\textrm{def}}{=} \sum_{0\leq e\leq
  d}2^{e}\cdot b_e$; thus $m-n+1=m_{p(n)}+1$.

  We define now the sets of
  locations
  
$$

     \mathcal{L}_\mathrm{Eve}&  \stackrel{\!\,\!\,\textrm{def}}{=}\{ \ell_0,\smiley\}
      \cup\{ \ell_\gamma\mid\gamma\in\Gamma'\}
      \cup\{ \ell_\gamma^k\mid 1\leq k\leq 3\}
      \cup\{ \ell_{=j}\mid 0<j\leq n\}\\
      &\:\cup\:\{ \ell_{1\leq?\leq m_d+1}\mid 0\leq d\leq
  p(n)\}\cup\{ \ell_{1\leq?\leq 2^d}\mid 1\leq d\leq p(n)\}\;,\\
     \mathcal{L}_\mathrm{Adam}&  \stackrel{\!\,\!\,\textrm{def}}{=}\{ \ell_{(\gamma_1,\gamma_2,\gamma_3)}\mid\gamma_1,\gamma_2,\gamma_3\in\Gamma'\}\;.
  
$$

  The intention behind the locations $\ell_{=j}\in \mathcal{L}_\mathrm{Eve}$ is
  that Eve can reach $\smiley(0)$ from a configuration $\ell_{=j}(c)$ if
  and only if $c=j$; we define accordingly $A$ with the
  action $\ell_{=j} \xrightarrow{\,-j,}\smiley$.
  Similarly, Eve should be able to reach $\smiley(0)$ from
  $\ell_{1\leq?\leq m_d+1}(c)$ for $0\leq d\leq p(n)$ if and only if
  $1\leq c\leq m_d+1$,
  which is implemented by the following actions: if $b_{d+1}=1$, then
  
$$

     \ell_{1\leq?\leq m_{d+1}+1}& \xrightarrow{\,0,} \ell_{1\leq?\leq 2^{d+1}}\;,&
     \ell_{1\leq?\leq m_{d+1}+1}& \xrightarrow{\,-2^{d+1,}} \ell_{1\leq ?\leq m_{d}+1}\;,
    \intertext{and if $b_{d+1}=0$,}
     \ell_{1\leq?\leq m_{d+1}+1}& \xrightarrow{\,0,} \ell_{1\leq ?\leq m_{d}+1}\;,
    \intertext{and finally}
     \ell_{1\leq?\leq m_0+1}& \xrightarrow{\,-b_0,} \ell_{=1}\;,& \ell_{1\leq?\leq m_0+1}& \xrightarrow{\,0,} \ell_{=1}\;,
    \intertext{where for all $1\leq d\leq p(n)$, $\ell_{1\leq?\leq 2^d}(c)$ allows to
    reach $\smiley(0)$ if and only if $1\leq c\leq 2^d$:}
     \ell_{1\leq?\leq 2^{d+1}}& \xrightarrow{\,-2^{d,}} \ell_{1\leq?\leq
                               2^d}\;,& \ell_{1\leq?\leq
                                        2^{d+1}}& \xrightarrow{\,0,} \ell_{1\leq?\leq
                                                  2^d}\;,\\ \ell_{1\leq?\leq
    2^1}& \xrightarrow{\,-1,} \ell_{=1}\;,& \ell_{1\leq?\leq 2^1}& \xrightarrow{\,0,} \ell_{=1}\;.
  
$$

  The remainder of the reduction is now very similar to the reduction shown
  in {prf:ref}`11-th:countdown-given`.
  Regarding initialisation, Eve can choose her initial position,
  which we implement by the actions
  
$$

     \ell_0 & \xrightarrow{\,-1,}  \ell_0 &  \ell_0 & \xrightarrow{\,-1,} \ell_{(q_\mathrm{final},a)}&&\text{for $a\in\Gamma$}\;.
    \intertext{Outside the boundary cases, the game is implemented by
    the following actions:}
     \ell_\gamma& \xrightarrow{\,-m,} \ell_{(\gamma_1,\gamma_2,\gamma_3)}&&&&\text{for
  $\gamma_1,\gamma_2,\gamma_3\vdash\gamma$}\;,\\  \ell_{(\gamma_1,\gamma_2,\gamma_3)}& \xrightarrow{\,0,} \ell^k_{\gamma_k}& \ell^k_{\gamma_k}& \xrightarrow{\,-k,} \ell_{\gamma_k}&&\text{for
  $k\in\{1,2,3\}$}\;.
  \intertext{We handle the endmarker positions via the following
  actions, where Eve proceeds along the left edge
  of {numref}`11-fig:exp` until she reaches the initial left endmarker:}
    \ell_\triangleright& \xrightarrow{\,-m-2,} \ell_\triangleright\;,&  \ell_\triangleright& \xrightarrow{\,-1,} \ell_{=1}\;,&  \ell_\triangleleft& \xrightarrow{\,-m-1,} \ell_\triangleright\;.
  \intertext{For the positions inside the input word $w=a_1\cdots
  a_n$, we use the actions}
   \ell_{(q_0,a_1)}& \xrightarrow{\,-2,} \ell_{=1}\;,& \ell_{a_j}& \xrightarrow{\,-2,} \ell_{=j}&&\text{for
  $1<j\leq n$}\;.
  \intertext{Finally, for the blank symbols of $C_1$, which should be
  associated with a counter value $c$ such that $n+3\leq c\leq m+3$,
  i.e., such that $1\leq c-n-2\leq m-n+1=m_{p(n)}+1$, we use the
  action}
   \ell_\Box& \xrightarrow{\,-n-2,} \ell_{1\leq?\leq m_{p(n)}+1}\;.
  
$$

  Regarding the given initial credit variant, we add a new location
  $\ell'_0$ controlled by Eve and let her choose her initial credit
  when starting from $\ell'_0(0)$ by using the new actions
  $\ell'_0 \xrightarrow{\,1,} \ell'_0$ and $\ell'_0 \xrightarrow{\,0,} \ell_0$.

````

(11-sec:mono)=
## Asymmetric Monotone Games

The results on configuration reachability might give the impression
that asymmetry does not help much for solving vector games: we
obtained in Section {ref}`11-sec:reach` exactly the same results as in the
general case.  Thankfully, the situation changes drastically if we
consider the other types of vector games: coverability,
non-termination, and parity become decidable
in asymmetric vector games.  The main rationale for this comes from
order theory, which prompts the following definitions.

> **Quasi-orders**

 A quasi-order $(X,{\leq})$ is a
set $X$ together with a reflexive and transitive
relation ${\leq}\subseteq X\times X$.  Two elements $x,y\in X$ are
incomparable if $x\not\leq y$ and $y\not\leq x$, and they are
equivalent if $x\leq y$ and $y\leq x$.  The associated strict relation
$x<y$ holds if $x\leq y$ and $y\not\leq x$.

The upward closure of a subset $S\subseteq X$ is the set of
elements greater or equal to the elements of S:
${\uparrow}S  \stackrel{\!\,\!\,\textrm{def}}{=}\{x\in X\mid\exists y\in S\mathbin.y\leq x\}$.  A
subset $U\subseteq X$ is upwards closed if ${\uparrow}U=U$.  When
$S=\{x\}$ is a singleton, we write more simply ${\uparrow}x$ for its
upward closure and call the resulting upwards closed set a
principal filter.  Dually, the downward closure of $S$ is
${\downarrow}S  \stackrel{\!\,\!\,\textrm{def}}{=}\{x\in X\mid\exists y\in S\mathbin.x\leq y\}$, a
downwards closed set is a subset $D\subseteq X$ such that
$D={\downarrow}D$, and ${\downarrow}x$ is called a principal
ideal.  Note that the complement $X\setminus U$ of an upwards closed
set $U$ is downwards closed and vice versa.

> **Monotone Games**

Let us consider again the natural semantics $\mathcal{A}_\mathbb{N}(\mathcal{V})$ of a
vector system.  The set of vertices
$V= \mathcal{L}\times\mathbb{N}^ k\cup\{ \bot\}$ is naturally equipped with a
partial ordering: $v\leq v'$ if either $v=v'= \bot$, or $v= \ell(\vec
v)$ and $v'= \ell(\vec v')$ are two configurations that share the same
location and satisfy $\vec v(i)\leq\vec v'(i)$ for all $1\leq
i\leq k$, i.e., if $\vec v\leq\vec v'$ for the componentwise
ordering.

Consider a set of colours $C$ and a vertex colouring $\mathrm{vcol}{:}\,V\to C$
of the natural semantics $\mathcal{A}_\mathbb{N}(\mathcal{V})$ of a vector system, which
defines a colouring $\mathfrak{c}{:}\,E\to C$ where
$\mathfrak{c}(e)  \stackrel{\!\,\!\,\textrm{def}}{=} \mathrm{vcol}( \textrm{In}(e))$.  We
say that the colouring $\mathrm{vcol}$ is monotonic if $C$ is finite and,
for every colour $p\in C$, the set $\mathrm{vcol}^{-1}(p)$ of vertices coloured
by $p$ is upwards closed with respect to ${\leq}$.  Clearly, the
colourings of coverability, non-termination, and parity vector games are monotonic, whereas those of
configuration reachability vector games are not.  By extension, we
call a vector game **monotonic** if its underlying colouring
is monotonic.

````{prf:lemma} Simulation
:label: 11-lem:mono

  In a monotonic asymmetric vector game, if Eve wins from a
  vertex $v_0$, then she also wins from $v'_0$ for all $v'_0\geq
  v_0$.

````

````{admonition} Proof
:class: dropdown tip

  It suffices for this to check that, for all $v_1\leq v_2$ in $V$,
  \begin{description}
  \item[(colours)] $\mathrm{vcol}(v_1)= \mathrm{vcol}(v_2)$ since $\mathrm{vcol}$ is monotonic;
  \item[(zig Eve)] if $v_1,v_2\in V_\mathrm{Eve}$, $a\in A$, and
    $\Delta(v_1,a)=v'_1\neq \bot$ is defined, then
    $v'_2  \stackrel{\!\,\!\,\textrm{def}}{=} \Delta(v_2,a)$ is such that $v'_2\geq v'_1$: indeed,
    $v'_1\neq \bot$ entails that $v_1$ is a configuration
    $\ell(\vec v_1)$ and $v'_1= \ell'(\vec v_1+\vec u)$ for the action
    $a=( \ell \xrightarrow{\,\vec u,} \ell')\in A$, but then $v_2= \ell(\vec v_2)$
    for some $\vec v_2\geq\vec v_1$ and
    $v'_2= \ell'(\vec v_2+\vec u)\geq v'_1$;
  \item[(zig Adam)] if $v_1,v_2\in V_\mathrm{Adam}$, $a\in A$, and
    $\Delta(v_2,a)=v'_2$ is defined, then
    $v'_1  \stackrel{\!\,\!\,\textrm{def}}{=} \Delta(v_1,a)\leq v'_2$: indeed, either $v'_2= \bot$ and
    then $v'_1= \bot$, or $v'_2\neq \bot$, thus
    $v_2= \ell(\vec v_2)$, $v'_2= \ell'(\vec v_2)$, and
    $a=( \ell \xrightarrow{\,\vec 0,} \ell')\in A$ (recall that the game is
    asymmetric), but then $v_1= \ell(\vec v_1)$ for some
    $\vec v_1\leq\vec v_2$ and thus $v'_1= \ell'(\vec v_1)\leq v'_2$.
  \end{description}
  The above conditions show that, if $\sigma{:}\,E^\ast\to A$ is a
  strategy of Eve that wins from $v_0$, then by
  simulating $\sigma$ starting from $v'_0$---i.e., by applying the
  same actions when given a pointwise larger or equal history---she
  will also win.\todoquestion{Is that clear?}

````

Note that {prf:ref}`11-lem:mono` implies that $W_\mathrm{Eve}$ is upwards closed:
$v_0\in W_\mathrm{Eve}$ and $v_0\leq v'_0$ imply $v_0'\in W_\mathrm{Eve}$.  {prf:ref}`11-lem:mono`
does not necessarily hold in vector games without the asymmetry
condition.  For instance, in both {numref}`11-fig:cov,11-fig:nonterm` on
\cpageref{11-fig:cov}, $\ell'(0,1)\in W_\mathrm{Eve}$ but $\ell'(1,2)\in W_\mathrm{Adam}$ for
the coverability and non-termination objectives.  This is due to
the fact that the action $\ell' \xrightarrow{\,-1,0,} \ell$ is available
in $\ell'(1,2)$ but not in $\ell'(0,1)$.

> **Well-quasi-orders**

 What makes monotonic vector games so
interesting is that the partial order $(V,{\leq})$ associated with the
natural semantics of a vector system is a well-quasi-order.  A
quasi-order $(X,{\leq})$ is well (a **wqo**)
if any of the following equivalent characterisations
hold {cite}`Kruskal:1972,Schmitz&Schnoebelen:2012`:

  *  in any infinite sequence $x_0,x_1,\cdots$ of elements
    of $X$, there exists an infinite sequence of indices
    $n_0<n_1<\cdots$ such that $x_{n_0}\leq
    x_{n_1}\leq\cdots$---infinite sequences in $X$ are good---,
  *  any strictly ascending sequence $U_0\subsetneq
    U_1\subsetneq\cdots$ of upwards closed sets $U_i\subseteq X$ is
    finite---$X$ has the ascending chain condition---,
  *  any non-empty upwards closed $U\subseteq X$ has at least
    one, and at most finitely many minimal elements up to equivalence;
    therefore any upwards closed $U\subseteq X$ is a finite union
    $U=\bigcup_{1\leq j\leq n}{\uparrow}x_j$ of finitely many
    principal filters ${\uparrow}x_j$---$X$ has the finite basis
    property.

The fact that $(V,{\leq})$ satisfies all of the above is an easy
consequence of **Dickson's Lemma** {cite}`Dickson:1913`.

> **Pareto Limits**

 By the finite basis property of
$(V,{\leq})$ and {prf:ref}`11-lem:mono`, in a monotonic asymmetric
vector game, $W_\mathrm{Eve}=\bigcup_{1\leq j\leq n}{\uparrow} \ell_j(\vec v_j)$
is a finite union of principal filters.  The set
$\mathsf{Pareto}  \stackrel{\!\,\!\,\textrm{def}}{=}\{ \ell_1(\vec v_1),\dots, \ell_n(\vec v_n)\}$ is
called the Pareto limit or **Pareto frontier** of the game.
Both the existential and the given initial credit variants of the
game can be reduced to computing this Pareto limit: with
existential initial credit and an initial location $\ell_0$, check
whether $\ell_0(\vec v)\in\mathsf{Pareto}$ for some $\vec v$, and with
given initial credit and an initial configuration $\ell_0(\vec v_0)$, check
whether $\ell_0(\vec v)\in\mathsf{Pareto}$ for some $\vec v\leq\vec
v_0$.

````{prf:example} NEEDS LABEL Pareto limit

  Consider the asymmetric vector system from {numref}`11-fig:avg` on
  \cpageref{11-fig:avg}.  For the coverability game with target
  configuration $\ell(2,2)$, the Pareto limit is
  $\mathsf{Pareto}=\{ \ell(2,2), \ell'(3,2), \ell_{2,1}(0,1), \ell_{\text-1,0}(3,2)\}$,
  while for the non-termination game, $\mathsf{Pareto}=\emptyset$:
  Eve loses from all the vertices.  Observe that this is consistent
  with Eve\'s winning region in the coverability energy game
  shown in {numref}`11-fig:cov-nrg`.

````

````{prf:example} Doubly exponential Pareto limit
:label: 11-ex:pareto

  Consider the one-player vector system of {numref}`11-fig:pareto`,
  where the meta-decrement from $\ell_0$ to $\ell_1$ can be
  implemented using $O(n)$ additional counters and a set $\mathcal{L}'$ of
  $O(n)$ additional locations by the arguments of the
  forthcoming {prf:ref}`11-th:avag-hard`.

```{figure} ./../FigAndAlgos/11-fig:pareto.png
:name: 11-fig:pareto
:align: center
A one-player vector system
  with a large Pareto limit.
```
  For the coverability game with target
  configuration $\ell_f(\vec 0)$, if $\ell_0$ is the initial location
  and we are given initial credit $m\cdot\vec e_1$, Eve wins if and
  only if $m\geq 2^{2^n}$, but with existential initial credit she
  can start from $\ell_0(\vec e_2)$ instead.  We have indeed
  $\mathsf{Pareto}\cap(\{ \ell_0, \ell_1, \ell_f\}\times\mathbb{N}^ k)=\{ \ell_0(\vec
  e_2), \ell_0(2^{2^n}\cdot\vec e_1), \ell_1(\vec 0), \ell_f(\vec 0)\}$.
  Looking more in-depth into the construction of {prf:ref}`11-th:avag-hard`,
  there is also an at least double exponential number of distinct
  minimal configurations in $\mathsf{Pareto}$.

````

> **Finite Memory**

Besides having a finitely represented winning region, Eve also has
finite memory strategies in asymmetric vector games with parity
objectives; the following argument is straightforward to adapt to
the other regular objectives from Chapter {ref}`2-chap:regular`.

````{prf:lemma} Finite memory suffices in parity asymmetric vector games
:label: 11-lem:finmem

  If Eve has a strategy winning from some vertex $v_0$ in a
  parity asymmetric vector game, then she has a
  finite-memory one.

````

````{admonition} Proof
:class: dropdown tip

  Assume $\sigma$ is a winning strategy from $v_0$.  Consider the tree
  of vertices visited by plays consistent with $\sigma$: each branch
  is an infinite sequence $v_0,v_1,\dots$ of elements of $V$ where the
  maximal priority occuring infinitely often is some even number $p$.
  Since $(V,{\leq})$ is a wqo, this is a good sequence: there
  exists infinitely many indices $n_0<n_1<\cdots$ such that
  $v_{n_0}\leq v_{n_1}\leq\cdots$.  There exists $i<j$ such
  that $p=\max_{n_i\leq n<n_j} \mathrm{vcol}(v_n)$ is the maximal priority
  occurring in some interval $v_{n_i},v_{n_{i+1}},\dots,v_{n_{j-1}}$.
  Then Eve can play in $v_{n_j}$ as if she were in $v_{n_i}$, in
  $v_{n_j+1}$ as if she were in $v_{n_i+1}$ and so on, and we prune
  the tree at index $n_j$ along this branch so that $v_{n_j}$ is a
  leaf, and we call $v_{n_i}$ the return node of that leaf.  We
  therefore obtain a finitely branching tree with finite branches,
  which by K\H{o}nig's Lemma is finite.

  The finite tree we obtain this way is sometimes called a
  self-covering tree.

  It is relatively straightforward to construct a finite memory
  structure $(M,m_0,\delta)$ (as defined in Section {ref}`1-sec:memory`) from a
  self-covering tree, using its internal nodes as memory states plus
  an additional sink memory state $m_\bot$; the initial memory
  state $m_0$ is the root of the tree.  In a node $m$ labelled by
  $\ell(\vec v)$, given an edge
  $e=( \ell(\vec v'), \ell'(\vec v'+\vec u))$ arising from an
  action $\ell \xrightarrow{\,\vec u,} \ell'\in A$, if $\vec v'\geq\vec v$ and
  $m$ has a child $m'$ labelled by $\ell'(\vec v+\vec u)$ in the
  self-covering tree, then either $m'$ is a leaf with return
  node $m''$ and we set $\delta(m,e)  \stackrel{\!\,\!\,\textrm{def}}{=} m''$, or $m'$ is an
  internal node and we set $\delta(m,e)  \stackrel{\!\,\!\,\textrm{def}}{=} m'$; in all the other
  cases, $\delta(m,e)  \stackrel{\!\,\!\,\textrm{def}}{=} m_\bot$.

  \todoquestion{Is that reasonably clear?  A
    bit heavy no?}

````

\TODO{Provide an additional example of a self-covering tree.}

````{prf:example} NEEDS LABEL doubly exponential memory

  Consider the one-player vector system of {numref}`11-fig:finitemem`,
  where the meta-decrement from $\ell_1$ to $\ell_0$ can be
  implemented using $O(n)$ additional counters and $O(n)$ additional
  locations by the arguments of the forthcoming {prf:ref}`11-th:avag-hard`
  on \cpageref{11-th:avag-hard}.

```{figure} ./../FigAndAlgos/11-fig:finitemem.png
:name: 11-fig:finitemem
:align: center
A one-player vector system
  witnessing the need for double exponential memory.
```

  For the parity game with location colouring
  $\mathrm{lcol}( \ell_0)  \stackrel{\!\,\!\,\textrm{def}}{=} 2$ and $\mathrm{lcol}( \ell_1)  \stackrel{\!\,\!\,\textrm{def}}{=} 1$, note that Eve 
  must visit $\ell_0$ infinitely often in order to fulfil the parity
  requirements.  Starting from the initial
  configuration $\ell_0(\vec 0)$, any winning play of Eve begins
  by 
$$
  \ell_0(\vec 0) \xrightarrow{\,0,} \ell_1(\vec 0) \xrightarrow{\,\vec
      e_1,} \ell_1(\vec e_1) \xrightarrow{\,\vec e_1,}\cdots \xrightarrow{\,\vec
      e_1,} \ell_1(m\cdot\vec
    e_1) \xrightarrow{\,-2^{2^n,}} \ell_0((m-2^{2^n})\cdot\vec
    e_1) 
$$
 for some $m\geq 2^{2^n}$ before she visits
  again a
  configuration---namely $\ell_0((m-2^{2^n})\cdot\vec e_1)$---greater
  or equal than a previous configuration---namely
  $\ell_0(\vec 0)$---**and** witnesses a maximal even parity in the
  meantime.  She then has a winning strategy that simply repeats this
  sequence of actions, allowing her to visit successively
  $\ell_0(2(m-2^{2^n})\cdot\vec e_1)$,
  $\ell_0(3(m-2^{2^n})\cdot\vec e_1)$, etc.  In this example, she
  needs at least $2^{2^n}$ memory to remember how many times the
  $\ell_1 \xrightarrow{\,\vec e_1,} \ell_1$ loop should be taken.

````

(11-sec:attr)=
### Attractor Computation for Coverability
So far, we have not seen how to compute the Pareto limit derived
from {prf:ref}`11-lem:mono` nor the finite memory structure derived
from {prf:ref}`11-lem:finmem`.  These objects are not merely finite but
also computable.  The simplest case is the one of coverability
asymmetric monotonic vector games: the fixed-point computation of
Section {ref}`2-sec:attractors` for reachability objectives can be turned into
an algorithm computing the Pareto limit of the game.

````{prf:observation} Computable Pareto limit
:label: 11-fact:pareto-cov

  The Pareto limit of a coverability asymmetric vector game is
  computable.

````

````{admonition} Proof
:class: dropdown tip

Let $\ell_f(\vec v_f)$ be the target configuration.  We define a
chain $U_0\subseteq U_1\subseteq\cdots$ of sets $U_i\subseteq V$ by

$$

  U_0&  \stackrel{\!\,\!\,\textrm{def}}{=}{\uparrow} \ell_f(\vec v_f)\;,&
  U_{i+1}&  \stackrel{\!\,\!\,\textrm{def}}{=} U_i\cup\mathrm{Pre}(U_i)\;.

$$

Observe that for all $i$, $U_i$ is upwards closed.  This can be
checked by induction over $i$: it holds initially in $U_0$, and for
the induction step, if $v\in U_{i+1}$ and $v'\geq v$, then either

*  $v= \ell(\vec v)\in\mathrm{Pre}(U_i)\cap V_\mathrm{Eve}$ thanks to some
  $\ell \xrightarrow{\,\vec u,} \ell'\in A$ such that
  $\ell'(\vec v+\vec u)\in U_i$; therefore $v'= \ell(\vec v')$ for some
  $\vec v'\geq \vec v$ is such that $\ell'(\vec v'+\vec u)\in U_i$ as
  well, thus $v'\in \mathrm{Pre}(U_i)\subseteq U_{i+1}$, or
*  $v= \ell(\vec v)\in\mathrm{Pre}(U_i)\cap V_\mathrm{Adam}$ because for all
  $\ell \xrightarrow{\,\vec 0,} \ell'\in A$, $\ell'(\vec v)\in U_i$; therefore
  $v'= \ell(\vec v')$ for some $\vec v'\geq \vec v$ is such that
  $\ell'(\vec v')\in U_i$ as well, thus
  $v'\in \mathrm{Pre}(U_i)\subseteq U_{i+1}$, or
*  $v\in U_i$ and therefore $v'\in U_i\subseteq U_{i+1}$.

By the ascending chain condition, there is a finite rank $i$ such
that $U_{i+1}\subseteq U_i$ and then $W_\mathrm{Eve}=U_i$.  Thus the
Pareto limit is obtained after finitely many steps.
In order to turn this idea into an algorithm, we need a way of
representing those infinite upwards closed sets $U_i$.  Thankfully,
by the finite basis property, each $U_i$ has a finite basis $B_i$
such that ${\uparrow}B_i=U_i$.  We therefore compute the following
sequence of sets

$$

  B_0&  \stackrel{\!\,\!\,\textrm{def}}{=}\{ \ell_f(\vec v_f)\}&B_{i+1}&  \stackrel{\!\,\!\,\textrm{def}}{=}
                                       B_i\cup\min\mathrm{Pre}({\uparrow}B_i)\;.

$$

Indeed, given a finite basis $B_i$ for $U_i$, it is straightforward to
compute a finite basis for the upwards closed $\mathrm{Pre}(U_i)$.
This results in {numref}`11-algo:cov` below.

````

```{figure} ./../FigAndAlgos/11-algo:cov.png
:name: 11-algo:cov
:align: center
Fixed point algorithm for coverability in asymmetric vector
  games.
```

While this algorithm terminates thanks to the ascending chain
condition, it may take quite long.  For instance, in
{prf:ref}`11-ex:pareto`, it requires at least $2^{2^n}$ steps before it
reaches its fixed point.  This is a worst-case instance, as it turns
out that this algorithm works in  \textrm{kEXP}[2]; see the bibliographic notes
at the end of the chapter.  Note that such a
fixed-point computation does not work directly for non-termination
or parity vector games, due to the need for greatest fixed-points.

