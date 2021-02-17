(6-sec:determinacy)=
# Positional determinacy of stochastic reachability games

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
%   [Mar98] ?}
Pure memoryless determinacy for non-stochastic games with parity
objectives was established in Chapter {ref}`2-chap:regular` (see {prf:ref}`2-thm:parity`). 
In this section we extend this result to stochastic games. 
We focus on reachability objectives, since we will see in Section {ref}`6-sec:relations` 
that other natural objectives reduce to reachability.
%  these reductions}

````{prf:theorem} Pure positional determinacy for stochastic reachability games
:label: 6-thm:determinacy

Stochastic reachability games are pure positionally determined.

````


````{admonition} Proof
:class: dropdown tip

  Let $G = (\vertices,E,\delta,\Win)$ be a stochastic reachability
  game.  We define an operator $\mathfrak{F}$ expressing Bellman-like
  equations for the game $G$:
  

$$
  \mathfrak{F}(\nu)(v) = \left\{\begin{array}{l@{~~}l}
      1 & \text{if}\ v = \Win \\
      \max_{(v,v') \in E} \nu(v') & \text{if}\ v \in \VE \\
      \min_{(v,v') \in E} \nu(v') & \text{if}\ v \in \VA \\
      \sum_{v' \in \vertices} \delta(v)(v') \cdot \nu(v') & \text{if} \in \Randomvertices
    \end{array}\right.
  $$

  This operator, defined on the complete lattice $[0,1]^{\vertices}$
  (equipped with the pointwise standard inequality) is
  monotonic. Hence it admits a least fixpoint, which we denote
  $\lfp(\mathfrak{F})$.  We show that:
  
````{prf:lemma} NEEDS TITLE AND LABEL 
    \label{6-lem:lfpgeval}
    For every $v$:
    

$$
    \lfp(\mathfrak{F}) (v) \le \sup_\sigma \inf_\tau
    \probm_{\sigma,\tau}^v(\Reach(\Win)) \le \inf_\tau \sup_\sigma
    \probm_{\sigma,\tau}^v(\Reach(\Win)) \enspace.
    $$

   

    \label{6-lem:lfpgeval}
    For every $v$:
    

$$
    \lfp(\mathfrak{F}) (v) \le \sup_\sigma \inf_\tau
    \probm_{\sigma,\tau}^v(\Reach(\Win)) \le \inf_\tau \sup_\sigma
    \probm_{\sigma,\tau}^v(\Reach(\Win)) \enspace.
    $$

  
````

  \begin{proof}
    We first argue for the right inequality:
    \begin{eqnarray*}
      \forall \sigma' \forall \tau:\
      \probm_{\sigma',\tau}^v(\Reach(\Win)) & \le & \sup_\sigma
      \probm_{\sigma,\tau}^v(\Reach(\Win)) \\
      \forall \sigma'\forall \tau :\  \inf_{\tau'}
      \probm_{\sigma',\tau'}^v(\Reach(\Win)) & \le & \sup_\sigma
      \probm_{\sigma,\tau}^v(\Reach(\Win)) \\
      \forall \tau:\ \sup_{\sigma'} \inf_{\tau'}
      \probm_{\sigma',\tau'}^v(\Reach(\Win)) & \le & \sup_\sigma
      \probm_{\sigma,\tau}^v(\Reach(\Win)) \\
      \sup_{\sigma'} \inf_{\tau'}
      \probm_{\sigma',\tau}'^v(\Reach(\Win)) & \le & \inf_{\tau} \sup_\sigma
      \probm_{\sigma,\tau}^v(\Reach(\Win)) 
    \end{eqnarray*}

    For proving the left inequality, it is sufficient to show that
    $v \mapsto \sup_\sigma \inf_\tau
    \probm_{\sigma,\tau}^v(\Reach(\Win))$ is a fixpoint of
    $\mathfrak{F}$.  Pick $v \in \VE$. 
                                  \begin{eqnarray*}
      \sup_\sigma \inf_\tau \probm_{\sigma,\tau}^v(\Reach(\Win)) & = &
      \sup_\sigma \inf_\tau \sum_{v'} \sigma(v)(v')  \cdot
      \probm_{\sigma',\tau'}^{v'}(\Reach(\Win)) \\
      & & \text{where}\ \sigma'\ \text{and}\ \tau'\ \text{are residual
        strategies after}\ (v,v') \\
      & = & \sup_\sigma \sum_{v'} \sigma(v)(v')  \cdot \inf_\tau \probm_{\sigma',\tau'}^{v'}(\Reach(\Win)) \\
      & & \text{since}\ \tau\ \text{is not concerned by this choice}
      \\
      & = & \max_{(v,v') \in E} \sup_{\sigma\ \text{s.t.}\
        \sigma(v) = v'} \inf_\tau
      \probm_{\sigma',\tau'}^{v'}(\Reach(\Win)) \\
      & & \text{since deterministic choices are the best} \\
      & = & \max_{(v,v') \in E} \sup_{\sigma'} \inf_{\tau'}
      \probm_{\sigma',\tau'}^{v'}(\Reach(\Win)) \\
      & & \text{since the first choice is now fixed} \\
      & = & \mathfrak{F}(\probm_{\sigma,\tau}^{\bullet}(\Reach(\Win)))(v)
    \end{eqnarray*}
    where $\probm_{\sigma,\tau}^{\bullet}(\Reach(\Win)))$ is the
    function with associates with vertex $v$ the value
    $\probm_{\sigma,\tau}^{v}(\Reach(\Win)))$.
                                                         
    Assume now that $v \in \VA$. 
                                                       \begin{eqnarray*}
      \sup_\sigma \inf_\tau \probm_{\sigma,\tau}^v(\Reach(\Win)) & = &
      \sup_\sigma \inf_\tau \sum_{v'} \tau(v)(v')
      \cdot \probm_{\sigma',\tau'}^{v'}(\Reach(\Win)) \\
      & & \text{where}\ \sigma'\ \text{and}\ \tau'\ \text{are residual
        strategies after}\ (v,v') \\
      & = & \sup_\sigma \min_{(v,v') \in E} \inf_{\tau\
        \text{s.t.}\ \tau(v) = v'} 
       \probm_{\sigma',\tau'}^{v'}(\Reach(\Win)) \\
      & & \text{since deterministic choices are the best} \\
      & = & \min_{(v,v') \in E}  \sup_{\sigma'} \inf_{\tau\
        \text{s.t.}\ \tau(v) = v'} \probm_{\sigma',\tau'}^{v'}(\Reach(\Win)) \\
      & & \text{since}\ \sigma\ \text{is not concerned with the first
        choice} \\
      & = & \mathfrak{F}(\probm_{\sigma,\tau}^{\bullet}(\Reach(\Win)))(v)
    \end{eqnarray*}

    Finally, let  $v \in \Randomvertices$. 
    \begin{eqnarray*}
      \sup_\sigma \inf_\tau \probm_{\sigma,\tau}^v(\Reach(\Win)) & = & \sum_{v'} \delta(v)(v') \cdot \sup_{\sigma'} \inf_{\tau'} \probm_{\sigma',\tau'}^{v'}(\Reach(\Win))\\
            & & \text{where}\ \sigma'\ \text{and}\ \tau'\ \text{are residual
                strategies after}\ (v,v') \\
      & = & \mathfrak{F}(\probm_{\sigma,\tau}^{\bullet}(\Reach(\Win)))(v)
    \end{eqnarray*}
    This concludes the proof.    
  
````

  
````{prf:lemma} NEEDS TITLE AND LABEL 
    \label{6-lem:lfpleval}
    For every $v \in \vertices$:
    

$$
    \lfp(\mathfrak{F})(v) \ge \inf_\tau \sup_\sigma
    \probm_{\sigma,\tau}^v(\Reach(\Win)) \enspace.
    $$

   

    \label{6-lem:lfpleval}
    For every $v \in \vertices$:
    

$$
    \lfp(\mathfrak{F})(v) \ge \inf_\tau \sup_\sigma
    \probm_{\sigma,\tau}^v(\Reach(\Win)) \enspace.
    $$

  
````

  
````{admonition} Proof
:class: dropdown tip

    Let $v \in \VA$. Since $\lfp(\mathfrak{F})$ is a fixpoint of
    $\mathfrak{F}$, and because the arena is finitely branching, there exists $v'\in \vertices$ such
    that $(v,v') \in E$ and:
    

$$
      \lfp(\mathfrak{F})(v) = \lfp(\mathfrak{F})(v') \enspace.
    $$

    We define $\tau^*$ the MD strategy, that selects for every
    $v\in \VA$ such a vertex $v'$, and we show now that for every
    $v \in \vertices$:
    

$$
    \lfp(\mathfrak{F})(v) = \sup_\sigma
    \probm_{\sigma,\tau^*}^v(\Reach(\Win)) \enspace.
    $$

    When $\tau^*$ is fixed, the game becomes a finite Markov decision
    process $\game_{\tau^*}$ (in that MDP, the random vertices are
    isolated from the non-deterministic ones, see
    Remark~\ref{5-rk:??}). Note that by standard results on MDP,
    see~\ref{5-thm:quantireach} there exists $\sigma^*$ MD such that
    for every $v \in V$:
    

$$
    \probm_{\sigma^*,\tau^*}^v(\Reach(\Win)) = \sup_\sigma
    \probm_{\sigma,\tau^*}^v(\Reach(\Win)) \enspace.
    $$

    Furthermore, $\probm_{\sigma^*,\tau^*}^\bullet(\Reach(\Win))$ is
    the least fixpoint of the Bellman equations for the MDP
    $\game_{\tau^*}$ (see~\ref{5-eq:Bellman}).
    
    It remains to observe that $\lfp(\mathfrak{F})$ satisfies the
    Bellman equations of the MDP under $\tau^*$: this is true from
    \Eve vertices since equations at those vertices are the same in
    the game and in the MDP; this is true from \Adam vertices by local
    optimality of $\tau^*$. Hence we deduce that
    

$$
      \lfp(\mathfrak{F}) \ge
      \probm_{\sigma^*,\tau^*}^\bullet(\Reach(\Win)) = \sup_\sigma
      \probm_{\sigma,\tau^*}^\bullet(\Reach(\Win)) \ge \inf_\tau
      \sup_\sigma \probm_{\sigma,\tau}^\bullet(\Reach(\Win)) \enspace.
    $$

    This concludes the proof of the lemma. 
  
````

By Lemma~\ref{6-lem:lfpgeval} and~\ref{6-lem:lfpleval}  we derive that:
 

$$
   \lfp(\mathfrak{F}) =
   \sup_\sigma \inf_\tau 
    \probm_{\sigma,\tau}^\bullet(\Reach(\Win)) =  \inf_\tau \sup_\sigma
   \probm_{\sigma,\tau}^\bullet(\Reach(\Win)) = 
   \probm_{\sigma^*,\tau^*}^\bullet(\Reach(\Win)) \enspace.
  $$

  This proves that $\game$ is pure memoryless determined, and that
  $(\sigma^*,\tau^*)$ is an optimal pure positional strategy profile.
         
\end{proof}

The proof of Theorem~\ref{6-thm:determinacy} yields an algorithm to
compute the value of a stochastic game with reachability
objective. Indeed, because the value in every vertex $v \in \vertices$
agrees with $\lfp(\mathfrak{F})(v)$, it suffices to compute
iteratively approximations of the fixpoint $\lfp(\mathfrak{F})$.  This
provides the first value iteration algorithm for general stochastic
reachability games.

Historically this result was proven in the restricted framework of
stopping games. The stochastic game $\game = (\arena,\Omega)$ is said
stopping whenever the arena $\arena$ has two distinguished sink
vertices $\vwin$ and $\vlose$, and for all strategies $\sigma$ and
$\tau$, for every vertex $v$,
$\probm_{\sigma,\tau}^{\arena,v}(\Reach(\{\vwin,\vlose\})) =
1$. Whenever the game is stopping, $\mathfrak{F}$ has a unique
fixpoint, hence the value iteration algorithm can be applied from any
initial tuple of values.%   (see CHJ-soda04). Check whether it is a byproduct of reductions.}
%   Let $\arena$ be an arena with two distinguished sink vertices%   $\Reach(\Win)$ where $\Win = \{\vwin\}$. The stochastic game $\game%   $\sigma$ and $\tau$,%   every vertex $v$. Whenever the arena/game is stopping,% \end{remark}

Notice that the proof of Theorem~\ref{6-thm:determinacy} and the value
iteration algorithm which derives from it do not assume that the game
is stopping, nor that distributions are uniform.
