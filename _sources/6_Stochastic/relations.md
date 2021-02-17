(6-sec:relations)=
# Relations between all games

```{math}
\newcommand{\adist}{\ensuremath{f}}
\newcommand{\probm}{\mathbb{P}}
\newcommand{\lfp}{**lfp**}
\newcommand{\vwin}{\ensuremath{v_{\textsc{win}}}}
\newcommand{\vlose}{\ensuremath{v_{\textsc{lose}}}}
\newcommand{\Adamvertices}{\VA}
\newcommand{\Evevertices}{\VE}
\newcommand{\Randomvertices}{\vertices_{\text{Rand}}}
\newcommand{\perm}{\pi}
\newcommand{\DetAtt}{\ensuremath{**DetAtt**}}

\newcommand{\weight}{\mathbf{w}} \newcommand{\nats}{\mathbb{N}}\newcommand{\Eve}{\textrm{Eve}}
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
Stochastic reachability games are powerful enough to encode
non-stochastic discounted games. 
More interestingly, they are central to the analysis of several important classes of stochastic
games: in particular, stochastic games with parity objectives,
mean-payoff objectives or discounted payoff all reduce to stochastic
reachability games. This motivates the fact that we focused on
reachability for determinacy in Section {ref}`6-sec:determinacy`), and that
in Section {ref}`6-sec:algos` we only give algorithms for stochastic games
with reachability objectives.


% games and stochastic MP-discounted-parity games, and SSGs.



## From discounted games to stochastic reachability games

\nat{reference: ZP-tcs96}

````{prf:proposition} NEEDS TITLE AND LABEL 
  \label{prop:dg2ssg}
  For any arena $\arena$ with weights in $[0,1]$ and $\lambda$ a
  discount factor, one can construct a stochastic arena $\arena'$ with
  $\Win \subseteq \vertices'$ and an injection
  $\iota : \vertices \to \vertices'$ such that
  $\forall v \in \vertices$
  

$$
    \mathsf{value}(v,\arena,\textrm{discount}(\lambda)) =
    \mathsf{value}(\iota(v),\arena',\Reach(\Win)) \enspace.
  $$

 

  \label{prop:dg2ssg}
  For any arena $\arena$ with weights in $[0,1]$ and $\lambda$ a
  discount factor, one can construct a stochastic arena $\arena'$ with
  $\Win \subseteq \vertices'$ and an injection
  $\iota : \vertices \to \vertices'$ such that
  $\forall v \in \vertices$
  

$$
    \mathsf{value}(v,\arena,\textrm{discount}(\lambda)) =
    \mathsf{value}(\iota(v),\arena',\Reach(\Win)) \enspace.
  $$


````


````{admonition} Proof
:class: dropdown tip

  The idea of the transformation is simple. The vertices in $\arena'$
  are formed of the vertices in $\arena$ plus two sink vertices
  $\smiley$ and $\frownie$, and some fresh random vertices. Then, an
  edge $e = (v,\weight,v')$ of $\arena$ is simulated in $\arena'$ with
  a transition from $v$ to a random vertex $v_e$, and the distribution
  $\delta(v_e)$ assigns probability $\lambda$ to $v'$,
  $(1{-}\lambda)\weight$ to $\smiley$ and $(1{-}\lambda)(1{-}\weight)$
  to $\frownie$. The set $\Win$ of target vertices in $\arena'$
  consists of $\{smiley\}$. To complete the reduction, we let $\iota$
  be the identity function on vertices of $\arena$.

  Note that the transformation from $\arena$ to $\arena'$ is clearly
  polynomial.

  To establish that this transformation preserves the values,
  **i.e.**\ that for every $v \in \vertices$,
  $\mathsf{value}(v,\arena,\textrm{discount}(\lambda)) =
  \mathsf{value}(v,\arena',\Reach(\Win))$, we prove that these
  values are solutions to the same system of equations.

  In the sequel, we write $\mathsf{value}_{\arena'}(v)$ as a shortcut
  for $\mathsf{value}(v,\arena',\Reach(\Win))$.
  By~\Cref{th:determinacy}, the values in the stochastic simple game
  $\arena'$ are solutions to the system of Bellman equations. The sink
  vertices have trivial values, $\mathsf{value}_{\arena'}(\smiley) =1$
  and $\mathsf{value}_{\arena'}(\frownie) =0$.  For every non-random
  vertex $v \notin \{\smiley,\frownie\}$ in $\arena'$,
  

$$
    \mathsf{value}_{\arena'}(v)
  = \begin{cases}   \max_{(v,v_e) \in E'}  \mathsf{value}_{\arena'}(v_e) & \text{if}\ v \in \VE \\
     \min_{(v,v_e) \in E'}  \mathsf{value}_{\arena'}(v_e)  & \text{if}\ v \in \VA
   \end{cases}
 $$

 Moreover, for every random vertex $v_e$, with $e=(v,\weight,v')$
 

$$
   \mathsf{value}_{\arena'}(v_e) = \lambda \cdot
   \mathsf{value}_{\arena'}(v') + (1{-}\lambda) \weight \cdot
   \mathsf{value}_{\arena'}(\smiley) \enspace.
  $$

 Eliminating the fresh
  random vertices, we obtain that for every non-random vertex
  $v \notin \{\smiley,\frownie\}$ in $\arena'$,
  

$$
    \mathsf{value}_{\arena'}(v) =
    \begin{cases}
      \max_{e=(v,\weight,v') \in E}  \lambda \cdot
   \mathsf{value}_{\arena'}(v') + (1{-}\lambda) \weight & \text{if}\ v \in \VE\\
      \min_{(v,\weight,v') \in E}  \lambda \cdot
   \mathsf{value}_{\arena'}(v') + (1{-}\lambda) \weight & \text{if}\ v \in \VA
   \end{cases}
    $$


    We thus observe that the values in $\arena'$, after elimination of
    values for intermediate random vertices, satisfy the equations of
    values in the discounted game (see the proof
    of {prf:ref}`4-thm:discounted` in~\Cref{chap:4_Payoffs}). Since
    this system of equations has a unique solution, we deduce the
    desired equality:
    $\mathsf{value}_{\arena'}(v) =
    \mathsf{value}(v,\arena,\textrm{discount}(\lambda))$.
    
    \qed
  
````

  Remark that~\Cref{prop:dg2ssg} trivially extends to
  discounted stochastic games: from a discounted stochastic game, one
  can build a stochastic reachability game that preserves the values.

## From stochastic mean-payoff to stochastic discounted

As a simple generalisation of the non-stochastic case (see
 {prf:ref}`4-thm:MP2discounted` \nat{add label to Theorem~4.9}), one can
also provide a reduction from mean-payoff objectives to discounted
payoff objectives, for what concerns stochastic arenas. More
precisely:

````{prf:theorem} NEEDS TITLE AND LABEL 
  Let $\arena$ be a stochastic arena with integer costs. One can
  effectively compute a discount factor $\lambda^*$ such that for
  every $\lambda \in [\lambda^*,1)$, any optimal pure positional
  strategy profile in the discounted game with discount factor
  $\lambda$ is also an optimal strategy profile in the mean-payoff
  game.
 

  Let $\arena$ be a stochastic arena with integer costs. One can
  effectively compute a discount factor $\lambda^*$ such that for
  every $\lambda \in [\lambda^*,1)$, any optimal pure positional
  strategy profile in the discounted game with discount factor
  $\lambda$ is also an optimal strategy profile in the mean-payoff
  game.

````

\nat{reference AM-isaac'09, Lemmas 1 and 2 (direct proof) + original
  proof without expression for $\lambda^*$ in LL-siamR'69}

## From stochastic parity  to stochastic mean-payoff

\nat{reference CH-ipl08, Theorem 3}

````{prf:proposition} NEEDS TITLE AND LABEL 
  For every stochastic arena $\arena$ with priorities in $[0,d]$, one
  can construct a weight function from $\vertices$ to $\mathbb{Z}$
  such that $\forall v \in \vertices$, if
  $ \mathsf{value}(v,\arena,\textrm{parity}) \notin \{0,1\}$, then
  

$$
    \mathsf{value}(v,\arena,\textrm{parity}) =
    \frac 1 2 (\mathsf{value}(v,\arena,\textrm{mean\_payoff})  {+} 1) \enspace.
  $$

 

  For every stochastic arena $\arena$ with priorities in $[0,d]$, one
  can construct a weight function from $\vertices$ to $\mathbb{Z}$
  such that $\forall v \in \vertices$, if
  $ \mathsf{value}(v,\arena,\textrm{parity}) \notin \{0,1\}$, then
  

$$
    \mathsf{value}(v,\arena,\textrm{parity}) =
    \frac 1 2 (\mathsf{value}(v,\arena,\textrm{mean\_payoff})  {+} 1) \enspace.
  $$


````


````{admonition} Proof
:class: dropdown tip

  One can pre-compute the vertices with value $1$ (resp. $0$) for the
  parity objective in polynomial time.
  
  \nat{ref for this ? Florian}
  Let us
  write $W_\Eve$ and $W_\Adam$ for these sets, respectively. We let
  $p_{\min}$ be the minimal probability that appears in the arena
  $\arena$, and $n$ be the number of vertices.
  
  We define the following weight function: for every $v \in W_\Eve$,
  to every edge $(v,k,v')$ in the parity game, we associate the weight
  $1$; for every $v \in W_\Adam$, to every edge $(v,k,v')$, we associate
  the weight $-1$; most importantly, for every
  $v \notin W_\Eve \cup W_\Adam$, to every edge $(v,k,v')$, we associate the
  weight $(-1)^k (2n)^k p_{\min}^{-nk}$.

  Let us prove that the above weight function satisfies
  

$$
    \forall v \in \vertices \setminus (W_\Eve \cup W_\Adam),\ 
    \mathsf{value}(v,\arena,\textrm{parity}) = \frac 1 2
    (\mathsf{value}(v,\arena,\textrm{mean\_payoff}) {+} 1)\enspace.
  $$

  To do so, we prove both inequalities.

  \fbox{here we assume sinks for $W_\Eve$ and $W_\Adam$, with
    appropriate priorities}
  
  
````{prf:lemma} NEEDS TITLE AND LABEL  Let $v \in \vertices$. Let $\sigma$ be a pure
    positional optimal strategy for Eve in the parity game
    $(\arena,\textrm{parity})$. For every positional strategy $\tau$
    of Adam
    $\probm_{\sigma,\tau}^v(\Reach(W_\Adam)) \leq 1 -
    \mathsf{value}(v,\arena,\textrm{parity})$.
     
 Let $v \in \vertices$. Let $\sigma$ be a pure
    positional optimal strategy for Eve in the parity game
    $(\arena,\textrm{parity})$. For every positional strategy $\tau$
    of Adam
    $\probm_{\sigma,\tau}^v(\Reach(W_\Adam)) \leq 1 -
    \mathsf{value}(v,\arena,\textrm{parity})$.
    
````

    This is a direct consequence of the definition of the value.

    
````{prf:lemma} NEEDS TITLE AND LABEL 
      Let $\sigma$ be a pure positional optimal strategy for Eve in
      the parity game $(\arena,\textrm{parity})$. For every positional
      strategy $\tau$ of Adam, for every BSCC $C$ induced by
      $(\sigma,\tau)$ different from $W_\Adam$ and $W_\Eve$,
      $\probm_{\sigma,\tau}^C(\textrm{parity}) >0$.
     

      Let $\sigma$ be a pure positional optimal strategy for Eve in
      the parity game $(\arena,\textrm{parity})$. For every positional
      strategy $\tau$ of Adam, for every BSCC $C$ induced by
      $(\sigma,\tau)$ different from $W_\Adam$ and $W_\Eve$,
      $\probm_{\sigma,\tau}^C(\textrm{parity}) >0$.
    
````

    \begin{proof}
      Indeed, $\mathsf{value}(C,\arena,\textrm{parity}) \in (0,1)$ by
      definition. Since $\sigma$ is optimal, for $v \in C$,
      $\probm_{\sigma,\tau}^v(\textrm{parity}) \geq
      \mathsf{value}(v,\arena,\textrm{parity}) >0$ (and even
      $\probm_{\sigma,\tau}^v(\textrm{parity})=1$).
    
````

    As a consequence, the maximum parity in $C$ is even since all
    vertices of $C$ are visited infinitely-often almost-surely when
    starting from $C$ and playing $(\sigma,\tau)$.

    Corollary: under $(\sigma,\tau)$ with $\sigma$ optimal for parity,
    apart from the $W_\Adam$ BSCC, all BSCC are good for \Eve.

    
````{prf:lemma} NEEDS TITLE AND LABEL 
      Let $\sigma$ be a pure positional optimal strategy for Eve in
      the parity game $(\arena,\textrm{parity})$. For every positional
      strategy $\tau$ of Adam, for every good BSCC $C$ induced by
      $(\sigma,\tau)$, $\MeanPayoff_{\sigma,\tau}^C(\arena) \geq 1$.
     

      Let $\sigma$ be a pure positional optimal strategy for Eve in
      the parity game $(\arena,\textrm{parity})$. For every positional
      strategy $\tau$ of Adam, for every good BSCC $C$ induced by
      $(\sigma,\tau)$, $\MeanPayoff_{\sigma,\tau}^C(\arena) \geq 1$.
    
````

    
````{admonition} Proof
:class: dropdown tip

      The case $C = W_\Eve$ is trivial. We assume
      $C \cap W_\Eve = \emptyset$ in the sequel.
      
      Let $v$ be a vertex with maximal parity $d_C$ (hence even and
      non-zero) in $C$. Starting from $C$ and under $(\sigma,\tau)$,
      the frequency of $v$ is at least $\frac{1}{n} p_{\min}^n$
      \fbox{to be argued}

      Given the definition of the weight function, the mean-payoff
      from $C$ and under $(\sigma,\tau)$ is at least
      

$$
        \frac{1}{n} p_{\min}^n (2n)^{d_C} p_{\min}^{-n d_C} -
        (2n)^{d_C -1} \frac{1}{p_{\min}^{n (d_C-1)}} = (2n)^{d_C -1}
        \frac{1}{p_{\min}^{n (d_C-1)}} =
        (\frac{2n}{p_{\min}^n})^{d_C{-}1}\enspace.
      $$

      Here, we bounded from above the frequency of over states in $C$
      by $1$, and considered the worst case, **i.e.**, parity
      $d_C-1$.
    
````

    \begin{eqnarray*}
      \MeanPayoff_{\sigma,\tau}^{v} & \geq & - \probm_{\sigma,\tau}^v(\Reach(W_\Adam)) + \sum_{C \textrm{ Good BSCC}} \probm_{\sigma,\tau}^v(\Reach(C))\\
                                    & \geq & -1 + \mathsf{value}(v,\arena,\textrm{parity}) + \probm_{\sigma,\tau}^v(\Parity)\\
                                    & \geq & -1 + \mathsf{value}(v,\arena,\textrm{parity}) + \inf_{\tau'} \probm_{\sigma,\tau'}^v(\Parity)\\
                                    & \geq & -1 + \mathsf{value}(v,\arena,\textrm{parity}) + \mathsf{value}(v,\arena,\textrm{parity})\\
                                    &  \geq & -1 + 2  \mathsf{value}(v,\arena,\textrm{parity}) \enspace.
    \end{eqnarray*}

    Assume again that $\sigma$ is positional optimal for the parity
    objective, and fix $\tau$ an optimal counterstrategy for \Adam in
    $(\arena,\MeanPayoff)$. We deduce:
    \begin{eqnarray*}
      -1 + 2 \mathsf{value}(v,\arena,\textrm{parity}) & \leq & 
                                                               \MeanPayoff_{\sigma,\tau}^{v}\\
                                                      & = & \inf_{\tau'}
                                                            \MeanPayoff_{\sigma,\tau'}^{v}\\
                                                      & \leq &
                                                                \sup_{\sigma'}\inf_{\tau'}
                                                               \MeanPayoff_{\sigma',\tau'}^{v}\\
                                                      & = & 
                                                            \mathsf{value}(v,\arena,\MeanPayoff) \enspace.
    \end{eqnarray*} 
    
    This proves the first inequality.

    The reverse inequality, can be proved by swapping the roles of
    $\Eve$ and $\Adam$ everywhere.
\end{proof}

Figure~\ref{6-fig:reductions} summarizes the relations between classes
of stochastic games.
