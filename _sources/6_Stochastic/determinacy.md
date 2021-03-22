(6-sec:determinacy)=
# Positional determinacy of stochastic reachability games

Pure memoryless determinacy for non-stochastic games with parity
objectives was established in Chapter {ref}`2-chap:regular` (see {prf:ref}`2-thm:parity`). 
In this section we extend this result to stochastic games. 
We focus on reachability objectives, since we will see in Section {ref}`6-sec:relations` 
that other natural objectives reduce to reachability.

````{prf:theorem} Pure positional determinacy for stochastic reachability games
:label: 6-thm:determinacy

Stochastic reachability games are pure positionally determined.

````

  Let $G = ( V,E,\delta, \textrm{Win})$ be a stochastic reachability
  game.  We define an operator $\mathfrak{F}$ expressing Bellman-like
  equations for the game $G$:

$$
  \mathfrak{F}(\nu)(v) = \left\{\begin{array}{l@{  }l}
      1 & \text{if}\ v =  \textrm{Win} \\
      \max_{(v,v') \in E} \nu(v') & \text{if}\ v \in  V_\mathrm{Eve} \\
      \min_{(v,v') \in E} \nu(v') & \text{if}\ v \in  V_\mathrm{Adam} \\
      \sum_{v' \in  V} \delta(v)(v') \cdot \nu(v') & \text{if} \in   V_{\text{Rand}}
    \end{array}\right.
  $$

  This operator, defined on the complete lattice $[0,1]^{ V}$
  (equipped with the pointwise standard inequality) is
  monotonic. Hence it admits a least fixpoint, which we denote
  $\textrm{lfp}(\mathfrak{F})$.  We show that:
  
````{prf:lemma} Least fixed point characterisation
:label: 6-lem:lfpgeval

  For every $v \in V$:

$$
     \textrm{lfp}(\mathfrak{F}) (v) \le \sup_\sigma \inf_\tau
     \mathbb{P}_{\sigma,\tau}^v( \mathtt{Reach}( \textrm{Win})) \le \inf_\tau \sup_\sigma
     \mathbb{P}_{\sigma,\tau}^v( \mathtt{Reach}( \textrm{Win})) \enspace.
    $$

````

````{admonition} Proof
:class: dropdown tip

    We first argue for the right inequality:
    \begin{eqnarray*}
      \forall \sigma' \forall \tau:\
       \mathbb{P}_{\sigma',\tau}^v( \mathtt{Reach}( \textrm{Win})) & \le & \sup_\sigma
       \mathbb{P}_{\sigma,\tau}^v( \mathtt{Reach}( \textrm{Win})) \\
      \forall \sigma'\forall \tau :\  \inf_{\tau'}
       \mathbb{P}_{\sigma',\tau'}^v( \mathtt{Reach}( \textrm{Win})) & \le & \sup_\sigma
       \mathbb{P}_{\sigma,\tau}^v( \mathtt{Reach}( \textrm{Win})) \\
      \forall \tau:\ \sup_{\sigma'} \inf_{\tau'}
       \mathbb{P}_{\sigma',\tau'}^v( \mathtt{Reach}( \textrm{Win})) & \le & \sup_\sigma
       \mathbb{P}_{\sigma,\tau}^v( \mathtt{Reach}( \textrm{Win})) \\
      \sup_{\sigma'} \inf_{\tau'}
       \mathbb{P}_{\sigma',\tau}'^v( \mathtt{Reach}( \textrm{Win})) & \le & \inf_{\tau} \sup_\sigma
       \mathbb{P}_{\sigma,\tau}^v( \mathtt{Reach}( \textrm{Win})) 
    \end{eqnarray*}

    For proving the left inequality, it is sufficient to show that
    $v \mapsto \sup_\sigma \inf_\tau
     \mathbb{P}_{\sigma,\tau}^v( \mathtt{Reach}( \textrm{Win}))$ is a fixpoint of
    $\mathfrak{F}$.  Pick $v \in  V_\mathrm{Eve}$. 
\begin{eqnarray*}
      \sup_\sigma \inf_\tau  \mathbb{P}_{\sigma,\tau}^v( \mathtt{Reach}( \textrm{Win})) & = &
      \sup_\sigma \inf_\tau \sum_{v'} \sigma(v)(v')  \cdot
       \mathbb{P}_{\sigma',\tau'}^{v'}( \mathtt{Reach}( \textrm{Win})) \\
      & & \text{where}\ \sigma'\ \text{and}\ \tau'\ \text{are residual strategies after}\ (v,v') \\
      & = & \sup_\sigma \sum_{v'} \sigma(v)(v')  \cdot \inf_\tau  \mathbb{P}_{\sigma',\tau'}^{v'}( \mathtt{Reach}( \textrm{Win})) \\
      & & \text{since}\ \tau\ \text{is not concerned by this choice}
      \\
      & = & \max_{(v,v') \in E} \sup_{\sigma\ \text{s.t.}\
        \sigma(v) = v'} \inf_\tau
       \mathbb{P}_{\sigma',\tau'}^{v'}( \mathtt{Reach}( \textrm{Win})) \\
      & & \text{since deterministic choices are the best} \\
      & = & \max_{(v,v') \in E} \sup_{\sigma'} \inf_{\tau'}
       \mathbb{P}_{\sigma',\tau'}^{v'}( \mathtt{Reach}( \textrm{Win})) \\
      & & \text{since the first choice is now fixed} \\
      & = & \mathfrak{F}( \mathbb{P}_{\sigma,\tau}^{\bullet}( \mathtt{Reach}( \textrm{Win})))(v)
    \end{eqnarray*}
    where $\mathbb{P}_{\sigma,\tau}^{\bullet}( \mathtt{Reach}( \textrm{Win})))$ is the
    function with associates with vertex $v$ the value
    $\mathbb{P}_{\sigma,\tau}^{v}( \mathtt{Reach}( \textrm{Win})))$.

    Assume now that $v \in  V_\mathrm{Adam}$. 
    \begin{eqnarray*}
      \sup_\sigma \inf_\tau  \mathbb{P}_{\sigma,\tau}^v( \mathtt{Reach}( \textrm{Win})) & = &
      \sup_\sigma \inf_\tau \sum_{v'} \tau(v)(v')
      \cdot  \mathbb{P}_{\sigma',\tau'}^{v'}( \mathtt{Reach}( \textrm{Win})) \\
      & & \text{where}\ \sigma'\ \text{and}\ \tau'\ \text{are residual
        strategies after}\ (v,v') \\
      & = & \sup_\sigma \min_{(v,v') \in E} \inf_{\tau\
        \text{s.t.}\ \tau(v) = v'} 
        \mathbb{P}_{\sigma',\tau'}^{v'}( \mathtt{Reach}( \textrm{Win})) \\
      & & \text{since deterministic choices are the best} \\
      & = & \min_{(v,v') \in E}  \sup_{\sigma'} \inf_{\tau\
        \text{s.t.}\ \tau(v) = v'}  \mathbb{P}_{\sigma',\tau'}^{v'}( \mathtt{Reach}( \textrm{Win})) \\
      & & \text{since}\ \sigma\ \text{is not concerned with the first
        choice} \\
      & = & \mathfrak{F}( \mathbb{P}_{\sigma,\tau}^{\bullet}( \mathtt{Reach}( \textrm{Win})))(v)
    \end{eqnarray*}

    Finally, let  $v \in   V_{\text{Rand}}$. 
    \begin{eqnarray*}
      \sup_\sigma \inf_\tau  \mathbb{P}_{\sigma,\tau}^v( \mathtt{Reach}( \textrm{Win})) & = & \sum_{v'} \delta(v)(v') \cdot \sup_{\sigma'} \inf_{\tau'}  \mathbb{P}_{\sigma',\tau'}^{v'}( \mathtt{Reach}( \textrm{Win}))\\
            & & \text{where}\ \sigma'\ \text{and}\ \tau'\ \text{are residual
                strategies after}\ (v,v') \\
      & = & \mathfrak{F}( \mathbb{P}_{\sigma,\tau}^{\bullet}( \mathtt{Reach}( \textrm{Win})))(v)
    \end{eqnarray*}
    This concludes the proof.

````

````{prf:lemma} NEEDS TITLE 6-lem:lfpleval
:label: 6-lem:lfpleval

    For every $v \in  V$:

$$
     \textrm{lfp}(\mathfrak{F})(v) \ge \inf_\tau \sup_\sigma
     \mathbb{P}_{\sigma,\tau}^v( \mathtt{Reach}( \textrm{Win})) \enspace.
    $$

````

````{admonition} Proof
:class: dropdown tip

    Let $v \in  V_\mathrm{Adam}$. Since $\textrm{lfp}(\mathfrak{F})$ is a fixpoint of
    $\mathfrak{F}$, and because the arena is finitely branching, there exists $v'\in  V$ such
    that $(v,v') \in E$ and:

$$
       \textrm{lfp}(\mathfrak{F})(v) =  \textrm{lfp}(\mathfrak{F})(v') \enspace.
    $$

    We define $\tau^*$ the MD strategy, that selects for every
    $v\in  V_\mathrm{Adam}$ such a vertex $v'$, and we show now that for every
    $v \in  V$:

$$
     \textrm{lfp}(\mathfrak{F})(v) = \sup_\sigma
     \mathbb{P}_{\sigma,\tau^*}^v( \mathtt{Reach}( \textrm{Win})) \enspace.
    $$

    When $\tau^*$ is fixed, the game becomes a finite Markov decision
    process $\mathcal{G}_{\tau^*}$ (in that MDP, the random vertices are
    isolated from the non-deterministic ones, see {prf:ref}`5-rk:??`). 
    Note that by standard results on MDP,
    see {prf:ref}`5-thm:quantireach` there exists $\sigma^*$ MD such that
    for every $v \in V$:

$$
     \mathbb{P}_{\sigma^*,\tau^*}^v( \mathtt{Reach}( \textrm{Win})) = \sup_\sigma
     \mathbb{P}_{\sigma,\tau^*}^v( \mathtt{Reach}( \textrm{Win})) \enspace.
    $$

    Furthermore, $\mathbb{P}_{\sigma^*,\tau^*}^\bullet( \mathtt{Reach}( \textrm{Win}))$ is
    the least fixpoint of the Bellman equations for the MDP
    $\mathcal{G}_{\tau^*}$ (see {eq}`5-eq:Bellman`).
    
    It remains to observe that $\textrm{lfp}(\mathfrak{F})$ satisfies the
    Bellman equations of the MDP under $\tau^*$: this is true from
    $\textrm{Eve}$ vertices since equations at those vertices are the same in
    the game and in the MDP; this is true from $\textrm{Adam}$ vertices by local
    optimality of $\tau^*$. Hence we deduce that

$$
       \textrm{lfp}(\mathfrak{F}) \ge
       \mathbb{P}_{\sigma^*,\tau^*}^\bullet( \mathtt{Reach}( \textrm{Win})) = \sup_\sigma
       \mathbb{P}_{\sigma,\tau^*}^\bullet( \mathtt{Reach}( \textrm{Win})) \ge \inf_\tau
      \sup_\sigma  \mathbb{P}_{\sigma,\tau}^\bullet( \mathtt{Reach}( \textrm{Win})) \enspace.
    $$

    This concludes the proof of the lemma. 
  
````

````{admonition} Proof
:class: dropdown tip

By {prf:ref}`6-lem:lfpgeval` and {prf:ref}`6-lem:lfpleval`  we derive that:

$$
    \textrm{lfp}(\mathfrak{F}) =
   \sup_\sigma \inf_\tau 
     \mathbb{P}_{\sigma,\tau}^\bullet( \mathtt{Reach}( \textrm{Win})) =  \inf_\tau \sup_\sigma
    \mathbb{P}_{\sigma,\tau}^\bullet( \mathtt{Reach}( \textrm{Win})) = 
    \mathbb{P}_{\sigma^*,\tau^*}^\bullet( \mathtt{Reach}( \textrm{Win})) \enspace.
  $$

  This proves that $\mathcal{G}$ is pure memoryless determined, and that
  $(\sigma^*,\tau^*)$ is an optimal pure positional strategy profile.

````

The proof of {prf:ref}`6-thm:determinacy` yields an algorithm to
compute the value of a stochastic game with reachability
objective. Indeed, because the value in every vertex $v \in  V$
agrees with $\textrm{lfp}(\mathfrak{F})(v)$, it suffices to compute
iteratively approximations of the fixpoint $\textrm{lfp}(\mathfrak{F})$.  This
provides the first value iteration algorithm for general stochastic
reachability games.

Historically this result was proven in the restricted framework of
stopping games. The stochastic game $\mathcal{G} = ( \mathcal{A},\Omega)$ is said
stopping whenever the arena $\mathcal{A}$ has two distinguished sink
vertices $v_{win}$ and $v_{lose}$, and for all strategies $\sigma$ and
$\tau$, for every vertex $v$,
$\mathbb{P}_{\sigma,\tau}^{ \mathcal{A},v}( \mathtt{Reach}(\{ v_{win}, v_{lose}\})) =
1$. Whenever the game is stopping, $\mathfrak{F}$ has a unique
fixpoint, hence the value iteration algorithm can be applied from any
initial tuple of values.

Notice that the proof of {prf:ref}`6-thm:determinacy` and the value
iteration algorithm which derives from it do not assume that the game
is stopping, nor that distributions are uniform.
