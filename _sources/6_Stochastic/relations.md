(6-sec:relations)=
# Relations between all games


```{math}
\newcommand{\weight}{\mathbf{w}}
\newcommand{\Adam}{\textrm{Adam}}
\newcommand{\arena}{\mathcal{A}}
\newcommand{\vertices}{V}
\newcommand{\VE}{V_\mEve}
\newcommand{\VA}{V_\mAdam}
\newcommand{\Win}{\textrm{Win}}
\newcommand{\Reach}{\mathtt{Reach}}
\newcommand{\Parity}{\mathtt{Parity}}
\newcommand{\MeanPayoff}{\mathtt{MeanPayoff}}
\newcommand{\mEve}{\mathrm{Eve}}
\newcommand{\mAdam}{\mathrm{Adam}}
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
  For any arena $\mathcal{A} with weights in $[0,1]$ and $\lambda$ a
  discount factor, one can construct a stochastic arena $\mathcal{A}$ with
  $\textrm{Win}\subseteq V$ and an injection
  $\iota : V\to V$ such that
  $\forall v \in V
  

$$
    \mathsf{value}(v,\mathcal{A}\textrm{discount}(\lambda)) =
    \mathsf{value}(\iota(v),\mathcal{A},\mathtt{Reach}\textrm{Win}) \enspace.
  $$

 

  \label{prop:dg2ssg}
  For any arena $\mathcal{A} with weights in $[0,1]$ and $\lambda$ a
  discount factor, one can construct a stochastic arena $\mathcal{A}$ with
  $\textrm{Win}\subseteq V$ and an injection
  $\iota : V\to V$ such that
  $\forall v \in V
  

$$
    \mathsf{value}(v,\mathcal{A}\textrm{discount}(\lambda)) =
    \mathsf{value}(\iota(v),\mathcal{A},\mathtt{Reach}\textrm{Win}) \enspace.
  $$


````


````{admonition} Proof
:class: dropdown tip

  The idea of the transformation is simple. The vertices in $\mathcal{A}$
  are formed of the vertices in $\mathcal{A} plus two sink vertices
  $\smiley$ and $\frownie$, and some fresh random vertices. Then, an
  edge $e = (v,\mathbf{w}v')$ of $\mathcal{A} is simulated in $\mathcal{A}$ with
  a transition from $v$ to a random vertex $v_e$, and the distribution
  $\delta(v_e)$ assigns probability $\lambda$ to $v'$,
  $(1{-}\lambda)\mathbf{w} to $\smiley$ and $(1{-}\lambda)(1{-}\mathbf{w}$
  to $\frownie$. The set $\textrm{Win} of target vertices in $\mathcal{A}$
  consists of $\{smiley\}$. To complete the reduction, we let $\iota$
  be the identity function on vertices of $\mathcal{A}.

  Note that the transformation from $\mathcal{A} to $\mathcal{A}$ is clearly
  polynomial.

  To establish that this transformation preserves the values,
  **i.e.**\ that for every $v \in V,
  $\mathsf{value}(v,\mathcal{A}\textrm{discount}(\lambda)) =
  \mathsf{value}(v,\mathcal{A},\mathtt{Reach}\textrm{Win})$, we prove that these
  values are solutions to the same system of equations.

  In the sequel, we write $\mathsf{value}_{\mathcal{A}}(v)$ as a shortcut
  for $\mathsf{value}(v,\mathcal{A},\mathtt{Reach}\textrm{Win})$.
  By~\Cref{th:determinacy}, the values in the stochastic simple game
  $\mathcal{A}$ are solutions to the system of Bellman equations. The sink
  vertices have trivial values, $\mathsf{value}_{\mathcal{A}}(\smiley) =1$
  and $\mathsf{value}_{\mathcal{A}}(\frownie) =0$.  For every non-random
  vertex $v \notin \{\smiley,\frownie\}$ in $\mathcal{A}$,
  

$$
    \mathsf{value}_{\mathcal{A}}(v)
  = \begin{cases}   \max_{(v,v_e) \in E'}  \mathsf{value}_{\mathcal{A}}(v_e) & \text{if}\ v \in V_\mathrm{Eve}\
     \min_{(v,v_e) \in E'}  \mathsf{value}_{\mathcal{A}}(v_e)  & \text{if}\ v \in V_\mathrm{Adam}  \end{cases}
 $$

 Moreover, for every random vertex $v_e$, with $e=(v,\mathbf{w}v')$
 

$$
   \mathsf{value}_{\mathcal{A}}(v_e) = \lambda \cdot
   \mathsf{value}_{\mathcal{A}}(v') + (1{-}\lambda) \mathbf{w}\cdot
   \mathsf{value}_{\mathcal{A}}(\smiley) \enspace.
  $$

 Eliminating the fresh
  random vertices, we obtain that for every non-random vertex
  $v \notin \{\smiley,\frownie\}$ in $\mathcal{A}$,
  

$$
    \mathsf{value}_{\mathcal{A}}(v) =
    \begin{cases}
      \max_{e=(v,\mathbf{w}v') \in E}  \lambda \cdot
   \mathsf{value}_{\mathcal{A}}(v') + (1{-}\lambda) \mathbf{w}& \text{if}\ v \in V_\mathrm{Eve}
      \min_{(v,\mathbf{w}v') \in E}  \lambda \cdot
   \mathsf{value}_{\mathcal{A}}(v') + (1{-}\lambda) \mathbf{w}& \text{if}\ v \in V_\mathrm{Adam}  \end{cases}
    $$


    We thus observe that the values in $\mathcal{A}$, after elimination of
    values for intermediate random vertices, satisfy the equations of
    values in the discounted game (see the proof
    of {prf:ref}`4-thm:discounted` in~\Cref{chap:4_Payoffs}). Since
    this system of equations has a unique solution, we deduce the
    desired equality:
    $\mathsf{value}_{\mathcal{A}}(v) =
    \mathsf{value}(v,\mathcal{A}\textrm{discount}(\lambda))$.
    
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
  Let $\mathcal{A} be a stochastic arena with integer costs. One can
  effectively compute a discount factor $\lambda^*$ such that for
  every $\lambda \in [\lambda^*,1)$, any optimal pure positional
  strategy profile in the discounted game with discount factor
  $\lambda$ is also an optimal strategy profile in the mean-payoff
  game.
 

  Let $\mathcal{A} be a stochastic arena with integer costs. One can
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
  For every stochastic arena $\mathcal{A} with priorities in $[0,d]$, one
  can construct a weight function from $V to $\mathbb{Z}$
  such that $\forall v \in V, if
  $ \mathsf{value}(v,\mathcal{A}\textrm{parity}) \notin \{0,1\}$, then
  

$$
    \mathsf{value}(v,\mathcal{A}\textrm{parity}) =
    \frac 1 2 (\mathsf{value}(v,\mathcal{A}\textrm{mean\_payoff})  {+} 1) \enspace.
  $$

 

  For every stochastic arena $\mathcal{A} with priorities in $[0,d]$, one
  can construct a weight function from $V to $\mathbb{Z}$
  such that $\forall v \in V, if
  $ \mathsf{value}(v,\mathcal{A}\textrm{parity}) \notin \{0,1\}$, then
  

$$
    \mathsf{value}(v,\mathcal{A}\textrm{parity}) =
    \frac 1 2 (\mathsf{value}(v,\mathcal{A}\textrm{mean\_payoff})  {+} 1) \enspace.
  $$


````


````{admonition} Proof
:class: dropdown tip

  One can pre-compute the vertices with value $1$ (resp. $0$) for the
  parity objective in polynomial time.
  
  \nat{ref for this ? Florian}
  Let us
  write $W_\Eve$ and $W_\textrm{Adam} for these sets, respectively. We let
  $p_{\min}$ be the minimal probability that appears in the arena
  $\mathcal{A}, and $n$ be the number of vertices.
  
  We define the following weight function: for every $v \in W_\Eve$,
  to every edge $(v,k,v')$ in the parity game, we associate the weight
  $1$; for every $v \in W_\textrm{Adam}, to every edge $(v,k,v')$, we associate
  the weight $-1$; most importantly, for every
  $v \notin W_\Eve \cup W_\textrm{Adam}, to every edge $(v,k,v')$, we associate the
  weight $(-1)^k (2n)^k p_{\min}^{-nk}$.

  Let us prove that the above weight function satisfies
  

$$
    \forall v \in V\setminus (W_\Eve \cup W_\textrm{Adam},\ 
    \mathsf{value}(v,\mathcal{A}\textrm{parity}) = \frac 1 2
    (\mathsf{value}(v,\mathcal{A}\textrm{mean\_payoff}) {+} 1)\enspace.
  $$

  To do so, we prove both inequalities.

  \fbox{here we assume sinks for $W_\Eve$ and $W_\textrm{Adam}, with
    appropriate priorities}
  
  
````{prf:lemma} NEEDS TITLE AND LABEL  Let $v \in V. Let $\sigma$ be a pure
    positional optimal strategy for Eve in the parity game
    $(\mathcal{A}\textrm{parity})$. For every positional strategy $\tau$
    of Adam
    $\probm_{\sigma,\tau}^v(\mathtt{Reach}W_\textrm{Adam}) \leq 1 -
    \mathsf{value}(v,\mathcal{A}\textrm{parity})$.
     
 Let $v \in V. Let $\sigma$ be a pure
    positional optimal strategy for Eve in the parity game
    $(\mathcal{A}\textrm{parity})$. For every positional strategy $\tau$
    of Adam
    $\probm_{\sigma,\tau}^v(\mathtt{Reach}W_\textrm{Adam}) \leq 1 -
    \mathsf{value}(v,\mathcal{A}\textrm{parity})$.
    
````

    This is a direct consequence of the definition of the value.

    
````{prf:lemma} NEEDS TITLE AND LABEL 
      Let $\sigma$ be a pure positional optimal strategy for Eve in
      the parity game $(\mathcal{A}\textrm{parity})$. For every positional
      strategy $\tau$ of Adam, for every BSCC $C$ induced by
      $(\sigma,\tau)$ different from $W_\textrm{Adam} and $W_\Eve$,
      $\probm_{\sigma,\tau}^C(\textrm{parity}) >0$.
     

      Let $\sigma$ be a pure positional optimal strategy for Eve in
      the parity game $(\mathcal{A}\textrm{parity})$. For every positional
      strategy $\tau$ of Adam, for every BSCC $C$ induced by
      $(\sigma,\tau)$ different from $W_\textrm{Adam} and $W_\Eve$,
      $\probm_{\sigma,\tau}^C(\textrm{parity}) >0$.
    
````

    \begin{proof}
      Indeed, $\mathsf{value}(C,\mathcal{A}\textrm{parity}) \in (0,1)$ by
      definition. Since $\sigma$ is optimal, for $v \in C$,
      $\probm_{\sigma,\tau}^v(\textrm{parity}) \geq
      \mathsf{value}(v,\mathcal{A}\textrm{parity}) >0$ (and even
      $\probm_{\sigma,\tau}^v(\textrm{parity})=1$).
    
````

    As a consequence, the maximum parity in $C$ is even since all
    vertices of $C$ are visited infinitely-often almost-surely when
    starting from $C$ and playing $(\sigma,\tau)$.

    Corollary: under $(\sigma,\tau)$ with $\sigma$ optimal for parity,
    apart from the $W_\textrm{Adam} BSCC, all BSCC are good for \Eve.

    
````{prf:lemma} NEEDS TITLE AND LABEL 
      Let $\sigma$ be a pure positional optimal strategy for Eve in
      the parity game $(\mathcal{A}\textrm{parity})$. For every positional
      strategy $\tau$ of Adam, for every good BSCC $C$ induced by
      $(\sigma,\tau)$, $\MeanPayoff_{\sigma,\tau}^C(\mathcal{A} \geq 1$.
     

      Let $\sigma$ be a pure positional optimal strategy for Eve in
      the parity game $(\mathcal{A}\textrm{parity})$. For every positional
      strategy $\tau$ of Adam, for every good BSCC $C$ induced by
      $(\sigma,\tau)$, $\MeanPayoff_{\sigma,\tau}^C(\mathcal{A} \geq 1$.
    
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
      \MeanPayoff_{\sigma,\tau}^{v} & \geq & - \probm_{\sigma,\tau}^v(\mathtt{Reach}W_\textrm{Adam}) + \sum_{C \textrm{ Good BSCC}} \probm_{\sigma,\tau}^v(\mathtt{Reach}C))\\
                                    & \geq & -1 + \mathsf{value}(v,\mathcal{A}\textrm{parity}) + \probm_{\sigma,\tau}^v(\mathtt{Parity}\\
                                    & \geq & -1 + \mathsf{value}(v,\mathcal{A}\textrm{parity}) + \inf_{\tau'} \probm_{\sigma,\tau'}^v(\mathtt{Parity}\\
                                    & \geq & -1 + \mathsf{value}(v,\mathcal{A}\textrm{parity}) + \mathsf{value}(v,\mathcal{A}\textrm{parity})\\
                                    &  \geq & -1 + 2  \mathsf{value}(v,\mathcal{A}\textrm{parity}) \enspace.
    \end{eqnarray*}

    Assume again that $\sigma$ is positional optimal for the parity
    objective, and fix $\tau$ an optimal counterstrategy for \textrm{Adam}in
    $(\mathcal{A}\mathtt{MeanPayoff}$. We deduce:
    \begin{eqnarray*}
      -1 + 2 \mathsf{value}(v,\mathcal{A}\textrm{parity}) & \leq & 
                                                               \MeanPayoff_{\sigma,\tau}^{v}\\
                                                      & = & \inf_{\tau'}
                                                            \MeanPayoff_{\sigma,\tau'}^{v}\\
                                                      & \leq &
                                                                \sup_{\sigma'}\inf_{\tau'}
                                                               \MeanPayoff_{\sigma',\tau'}^{v}\\
                                                      & = & 
                                                            \mathsf{value}(v,\mathcal{A}\mathtt{MeanPayoff} \enspace.
    \end{eqnarray*} 
    
    This proves the first inequality.

    The reverse inequality, can be proved by swapping the roles of
    $\Eve$ and $\textrm{Adam} everywhere.
\end{proof}

Figure~\ref{6-fig:reductions} summarizes the relations between classes
of stochastic games.
