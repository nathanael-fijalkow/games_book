(4-sec:mean_payoff)=
# Mean payoff games

```{math}

```

A natural approach for aggregating an infinite sequence of weights is to consider the arithmetic mean.
Since the sequence $(\frac{1}{k} \sum_{i = 0}^{k-1} \rho_i)_{k \in  \mathbb{N}}$ may not converge,
we can either consider the limit superior or the limit inferior, leading to the two definitions:

$$
 \mathtt{MeanPayoff}^+(\rho) = \limsup_k \frac{1}{k} \sum_{i = 0}^{k-1} \rho_i \quad ; \quad 
 \mathtt{MeanPayoff}^-(\rho) = \liminf_k \frac{1}{k} \sum_{i = 0}^{k-1} \rho_i.
$$

The goal of Eve is to maximise $\mathtt{MeanPayoff}^+$, which means that the goal of Adam is to minimise it, 
or equivalently to maximise $- \mathtt{MeanPayoff}^+$;
by taking the opposite of each weight this is equivalent to maximising $\mathtt{MeanPayoff}^-$.
In other words, $\mathtt{MeanPayoff}^+$ and $\mathtt{MeanPayoff}^-$ are dual objectives.

In this section we study mean payoff games.
We will first prove that they are prefix independent, then that they are positionally determined for both players,
and then construct algorithms for solving them and compute the value function.
The best known time complexity for both problems is pseudopolynomial, meaning polynomial when the numerical inputs are given in unary.

````{prf:lemma} Prefix independence
:label: 4-lem:prefix_independence_mean_payoff

$\mathtt{MeanPayoff}^+$ is prefix independent.

````

````{admonition} Proof
:class: dropdown tip

We show that $\mathtt{MeanPayoff}^+(\rho_0 \rho_1 \dots) =  \mathtt{MeanPayoff}^+(\rho_p \rho_{p+1} \dots)$
for a fixed $p \in  \mathbb{N}$:

$$

\limsup_k \frac{1}{k} \sum_{i = 0}^{k-1} \rho_i &= 
\limsup_k \left(
\underbrace{\frac{1}{k} \sum_{i = 0}^{p-1} \rho_i}_{\rightarrow 0 \text{ for } k \rightarrow \infty} + 
\underbrace{\frac{k-p}{k}}_{\rightarrow 1 \text{ for } k \rightarrow \infty} \cdot \frac{1}{k-p} \sum_{i = p}^{k-1} \rho_i
\right) \\
&=
\liminf_k \frac{1}{k-p} \sum_{i = 0}^{p-1} \rho_{p + i}.

$$

````

Note that by duality this implies that $\mathtt{MeanPayoff}^-$ is also prefix independent.

In the setting we consider in this chapter, meaning two player zero sum games of perfect information, 
the two objectives are equivalent, which will be a corollary of {prf:ref}`4-thm:mean_payoff_positional`.
We refer to {prf:ref}`12-thm:MMP-Eve`\todo{I do not know where this
theorem has disappeared...} for a setting where limit superior and limit inferior are not equivalent.

As an example, consider the mean payoff game represented in {numref}`4-fig:MP`. 
As we will show later, the positional strategies defined below are optimal strategies for Eve and Adam:

$$
\begin{array}{l}
\sigma^*(v_1) = (v_1,v_2) \quad ; \quad \sigma^*(v_3) = (v_3,v_1) \quad ; \quad \sigma^*(v_4) = (v_4,v_0) \\
\tau^*(v_0) = (v_0,v_4) \quad ; \quad \tau^*(v_2) = (v_2,v_3).
\end{array}
$$

Let us consider $\pi = \pi^{v_1}_{\sigma^*,\tau^*}$ the play starting from $v_1$ consistent with both $\sigma^*$ and $\tau^*$:

$$
\pi = \big((v_1,v_2)(v_2,v_3)(v_3,v_1)\big)^\omega.
$$

We obtain that $\mathtt{MeanPayoff}^+(\pi) = \frac{1 + 3 - 2}{3} = \frac{2}{3}$.

If we restrict ourselves to positional strategies for both players, 
we may easily convince ourselves that this is the best that both players can aim for. 
Indeed,

*  the self loop around $v_4$ has arithmetic mean $O$;
*  the simple cycle alternating between $v_0$ and $v_4$ has arithmetic mean $\frac{1}{2}$;
*  the simple cycle alternating between $v_0$ and $v_1$ has arithmetic mean $1$;
*  the self loop around $v_2$ has arithmetic mean $3$, and
*  the simple cycle alternating between $v_0$, $v_1$, $v_2$ and $v_3$ has arithmetic average $\frac{3}{4}$.

Eve cannot ensure a better outcome than $\frac{2}{3}$ from $v_1,v_2$, and $v_3$:
for instance if she switches her decision in $v_1$ to play $(v_1,v_0)$, 
she will get a lower outcome of $\frac{1}{2}$.
Similarly Adam cannot ensure a better outcome than $\frac{1}{2}$ from $v_0$ and $v_4$.
Let us now prove that positional strategies are indeed sufficient for mean payoff games.

```{figure} ./../FigAndAlgos/4-fig:MP.png
:name: 4-fig:MP
:align: center
A mean payoff game.
```

## Positional determinacy via first cycle games

````{prf:theorem} Positional determinacy of Mean-Payoff
:label: 4-thm:mean_payoff_positional

Limit superior mean payoff objectives are uniformly positionally determined for both players.

````

By duality this is equivalent to saying that both limit superior and limit inferior mean payoff objectives are uniformly positionally determined.

````{admonition} Proof
:class: dropdown tip

Let $\mathcal{A}$ an arena.
We represent a cycle as a sequence $c = v_0 v_1 \dots v_{k-1}$ such that $(v_i, v_{i+1 \mod k}) \in E$;
we note that for technical convenience the sequence does not cycle back to the first vertex.

Let us consider a finite play $\pi = v_0 v_1 v_2\dots$,
we define two objects by induction: 
the cycle decomposition $\mathrm{Cycles}\xspace(\pi)$ and the folded play $\widehat{ \pi}$.
To guide the intuititon: $\mathrm{Cycles}\xspace(\pi)$ is a list of **some** cycles in $\pi$, 
and $\widehat{ \pi}$ is obtained from $\pi$ by removing the cycles from $\mathrm{Cycles}\xspace(\pi)$
and does not contain any cycle.

If $\pi$ is a single vertex then the cycle decomposition is empty and the folded play is equal to $\pi$.
Otherwise let $\pi = \pi' \cdot v$, by induction we have already defined $\mathrm{Cycles}\xspace(\pi')$ and $\widehat{\pi'}$.
There are two cases:

*  Either $v$ appears in $\widehat{\pi'}$ and then $\widehat{\pi}$ is obtained from $\widehat{\pi'} \cdot v$ 
by replacing that cycle by $v$ and $\mathrm{Cycles}\xspace(\pi)$ by adding the cycle to $\mathrm{Cycles}\xspace(\pi')$.

*  Or $v$ does not appear in $\widehat{\pi'}$ and then $\widehat{\pi} = \widehat{\pi'} \cdot v$ 
and $\mathrm{Cycles}\xspace(\pi) =  \mathrm{Cycles}\xspace(\pi')$.

The cycle decomposition breaks down $\pi$ into (possibly interleaved) cycles and the folded play:
every vertex in $\pi$ either belongs to exactly one cycle in $\mathrm{Cycles}\xspace(\pi)$ or to $\widehat{\pi}$.
For instance for $\pi = v_0 v_1 v_2 v_3 v_2 v_4 v_1 v_5$
we have $\mathrm{Cycles}\xspace(\pi) = (c_1 = v_2 v_3 ; c_2 = v_1 v_2 v_4)$ and $\widehat{\pi} = v_0 v_1 v_5$,
as illustrated in {numref}`4-fig:example_cycle_decomposition`.

```{figure} ./../FigAndAlgos/4-fig:example_cycle_decomposition.png
:name: 4-fig:example_cycle_decomposition
:align: center
An example for the cycle decomposition. The first cycle is $c_1$ and is in red, 
the cycle $c_2$ is in blue, and $\widehat{\pi} = v_0 v_1 v_5$.
```

The definition of $\mathrm{Cycles}\xspace(\pi)$ is extended for infinite plays.
We write $\mathrm{FC}\xspace(\pi)$ for the first cycle in $\pi$.
Let us note that the definitions above do not depend on the mean payoff objectives.

Let $\mathcal{G} = ( \mathcal{A}, \mathtt{MeanPayoff}^+[ \mathfrak{c}])$ a limit superior mean payoff game.
The outline of the proof is as follows.

1.  We define the condition $\mathrm{FirstCycle}\xspace$ and $\mathcal{G}_{\text{FC}} = ( \mathcal{A}, \mathrm{FirstCycle}\xspace)$,
and show that $\textrm{val}^{ \mathcal{G}} =   \textrm{val}^{ \mathcal{G}_{\text{FC}}}$ 
and that if $\mathcal{G}_{\text{FC}}$ is positionally determined for both players then $\mathcal{G}$ is positionally determined for both players.
2.  We define the condition $\mathrm{FirstCycleReset}\xspace_v$ (parameterised by a vertex $v$) 
and $\mathcal{G}_{\text{FCR}(v)} = ( \mathcal{A}, \mathrm{FirstCycleReset}\xspace_v)$,
and show that $\textrm{val}^{ \mathcal{G}} =   \textrm{val}^{ \mathcal{G}_{\text{FCR}(v)}}$.
3.  We show that $\mathcal{G}_{\text{FC}}$ is positionally determined for both players.

**Step 1.**
For a path $\pi = v_0 v_1 \dots v_{k-1}$ we write $\mathrm{Mean}\xspace(\pi)$ for $\frac{1}{k} \sum_{i = 0}^{k-1}  \mathfrak{c}(v_i)$.
The condition $\mathrm{FirstCycle}\xspace$ computes the arithmetic mean of the first cycle.
Formally:

$$
 \mathrm{FirstCycle}\xspace(\pi) =  \mathrm{Mean}\xspace( \mathrm{FC}\xspace(\pi)).
$$

Let us define $\mathcal{G}_{\text{FC}} = ( \mathcal{A}, \mathrm{FirstCycle}\xspace)$.
We make two claims:

*  let $\sigma_{\text{FC}}$ a strategy in $\mathcal{G}_{\text{FC}}$, it induces a strategy $\sigma$ in $\mathcal{G}$ 
such that $\textrm{val}^{\sigma_{\text{FC}}} \le   \textrm{val}^{\sigma}$, and $\sigma$ is positional if $\sigma_{\text{FC}}$ is, and
*  let $\tau_{\text{FC}}$ a strategy in $\mathcal{G}_{\text{FC}}$, it induces a strategy $\tau$ in $\mathcal{G}$
such that $\textrm{val}^{\tau_{\text{FC}}} \ge   \textrm{val}^{\tau}$, and $\tau$ is positional if $\tau_{\text{FC}}$ is.

Let us prove the first claim.
We let $\sigma(\pi) = \sigma_{\text{FC}}(\widehat{\pi})$:
by definition if $\pi$ is a play consistent with $\sigma$ then $\widehat{\pi}$ is a play consistent with $\sigma_{\text{FC}}$.
Note that indeed if $\sigma_{\text{FC}}$ is positional then so is $\sigma$.
We show that $\textrm{val}^{\sigma_{\text{FC}}} \le   \textrm{val}^{\sigma}$.

Let $\pi$ be a play consistent with $\sigma$ from $v_0$ and $x =   \textrm{val}^{\sigma_{\text{FC}}}(v_0)$.
We first argue that all cycles in $\mathrm{Cycles}\xspace(\pi)$ have an arithmetic mean greater than or equal to $x$.
Indeed consider a cycle $c$ in $\mathrm{Cycles}\xspace(\pi)$ and let $\pi'$ the prefix of $\pi$
ending with the cycle $c$.
The play $\widehat{\pi'}$ is consistent with $\sigma_{\text{FC}}$, implying that $\mathrm{Mean}\xspace(c) \ge x$.

To conclude that $\mathtt{MeanPayoff}^+(\pi) \ge x$ we show the following property:

$$

(\forall c \in  \mathrm{Cycles}\xspace(\pi),\  \mathrm{Mean}\xspace(c) \ge x) \implies  \mathtt{MeanPayoff}^+(\pi) \ge x.
$$ (4-eq:cycle_positive)

To estimate $\mathtt{MeanPayoff}^+(\pi)$ let us look at the prefix $\pi_{< k}$ of $\pi$ of length $k$.
Indeed we note that $\mathtt{MeanPayoff}^+(\pi) = \limsup_k  \mathrm{Mean}\xspace(\pi_{< k})$.

To calculate $\mathrm{Mean}\xspace(\pi_{< k})$ we use the fact that 
every vertex in $\pi_{< k}$ either belongs to exactly one cycle in $\mathrm{Cycles}\xspace(\pi_{< k})$ or to $\widehat{\pi_{< k}}$,
and the linearity of the arithmetic mean:

$$
 \mathrm{Mean}\xspace(\pi_{< k}) =  \mathrm{Mean}\xspace  \left\{  \mathrm{Mean \right\}\xspace(\widehat{ \pi_{< k}}),  \left\{  \mathrm{Mean \right\}\xspace(c) : c \in  \mathrm{Cycles}\xspace(\pi_{< k})}}.
$$

By assumption each $\mathrm{Mean}\xspace(c)$ is greater than or equal to $x$.
Note that since $\widehat{ \pi_{< k}}$ does not contain any cycle, it has length at most $n$, independently of $k$.
On the other hand $\mathrm{Cycles}\xspace(\pi_{< k})$ has size at least $k / n$.
Hence when $k$ tends to infinity the term $\mathrm{Mean}\xspace(\widehat{ \pi_{< k}})$ vanishes and we have 
$\mathtt{MeanPayoff}^+(\pi) = \limsup_k  \mathrm{Mean}\xspace(\pi_{< k}) \ge x$.

We turn to the second claim.
The construction is identical for Adam:
we let $\tau(\pi) = \tau_{\text{FC}}(\widehat{\pi})$.
We show that $\textrm{val}^{\tau_{\text{FC}}} \ge   \textrm{val}^{\tau}$ following the same arguments.
Let $\pi$ be a play consistent with $\tau$ from $v_0$ and $x =   \textrm{val}^{\tau_{\text{FC}}}(v_0)$.

To conclude that $\mathtt{MeanPayoff}^+(\pi) \le x$ we show the following property:

$$

(\forall c \in  \mathrm{Cycles}\xspace(\pi),\  \mathrm{Mean}\xspace(c) \le x) \implies  \mathtt{MeanPayoff}^+(\pi) \le x.
$$ (4-eq:cycle_negative)

This follows as above from the linearity of the arithmetic mean and the cycle decomposition.

Let us now prove that $\textrm{val}^{ \mathcal{G}} =   \textrm{val}^{ \mathcal{G}_{\text{FC}}}$ using the two claims.
We first need to establish that $\mathcal{G}_{\text{FC}}$ is determined: 
one argument is that $\mathrm{FirstCycle}\xspace$ is a Borel condition, 
hence determinacy follows from the general Borel determinacy result ({prf:ref}`1-thm:borel_determinacy`),
another simpler argument is that $\mathrm{FirstCycle}\xspace$ is a finite duration condition,
meaning that the outcome of the play is determined with a finite number of steps (at most $n$),
hence determinacy follows from an easier direct argument for finite duration games.

It follows from the two claims that

$$
\begin{array}{llll}
  \textrm{val}^{ \mathcal{G}_{\text{FC}}} 
& = \sup_{\sigma_{\text{FC}}}   \textrm{val}^{\sigma_{\text{FC}}} 
& \le \sup_{\sigma}   \textrm{val}^{\sigma}
& =   \textrm{val}^{ \mathcal{G}} \\
  \textrm{val}^{ \mathcal{G}_{\text{FC}}}
& = \inf_{\tau_{\text{FC}}}   \textrm{val}^{\tau_{\text{FC}} }
& \ge \inf_{\tau}   \textrm{val}^{\tau}
& =   \textrm{val}^{ \mathcal{G}},
\end{array}
$$

where in both lines: 
the first equalities is by determinacy of $\mathcal{G}_{\text{FC}}$,
the inequalities thanks to the two claims,
and the last equalities by determinacy of $\mathcal{G}$.
The two obtained inequalities imply that $\textrm{val}^{ \mathcal{G}} =   \textrm{val}^{ \mathcal{G}_{\text{FC}}}$,
and positional optimal strategies for either player in $\mathcal{G}_{\text{FC}}$ 
induce positional optimal strategies in $\mathcal{G}$.

**Step 2.**
We define a third condition on $\mathcal{A}$:

$$
 \mathrm{FirstCycleReset}\xspace_v(\pi) = 
\begin{cases}
 \mathrm{FirstCycle}\xspace(\pi) & \text{ if } \pi \text{ does not visit } v \text{ before }  \mathrm{FC}\xspace(\pi), \\
 \mathrm{FirstCycle}\xspace(\pi_{\ge k}) & \text{ for } k \text{ the first index such that }   \textrm{In}(\pi_k) = v.
\end{cases}
$$

In words: if a cycle is closed before visiting $v$, then the condition is $\mathrm{FirstCycle}\xspace$
and otherwise when reaching $v$ the game is `reset' and the condition is $\mathrm{FirstCycle}\xspace$ from this point onwards.

This second step is similar to the first step; the reason why we separated them is because this step
relies on the fact that $\mathtt{MeanPayoff}^+$ is prefix independent.

Let us define $\mathcal{G}_{\text{FCR}(v)} = ( \mathcal{A}, \mathrm{FirstCycleReset}\xspace_v)$.
We make two claims:

*  let $\sigma_{\text{FCR}(v)}$ an optimal strategy in $\mathcal{G}_{\text{FCR}(v)}$, it induces a strategy $\sigma$ in $\mathcal{G}$ 
such that $\textrm{val}^{\sigma_{\text{FCR}(v)}} \le   \textrm{val}^{\sigma}$, and 
*  let $\tau_{\text{FCR}(v)}$ an optimal strategy in $\mathcal{G}_{\text{FCR}(v)}$, it induces a strategy $\tau$ in $\mathcal{G}$
such that $\textrm{val}^{\tau_{\text{FCR}(v)}} \ge   \textrm{val}^{\tau}$.

Let us prove the first claim.
We let

$$
\sigma(\pi) = 
\begin{cases}
\sigma_{\text{FCR}(v)}(\widehat{\pi}) & \text{if } \pi \text{ does not contain } v, \\
\sigma_{\text{FCR}(v)}(\widehat{\pi_{\ge k}}) & \text{for } k \text{ the first index such that }   \textrm{In}(\pi_k) = v.
\end{cases}
$$

We show that $\textrm{val}^{\sigma_{\text{FCR}(v)}} \le   \textrm{val}^{\sigma}$.
Let $\pi$ a play consistent with $\sigma$ from $v_0$ and $x =   \textrm{val}^{\sigma_{\text{FCR}(v)}}(v_0)$.
There are two cases.

Either $\pi$ does not contain $v$, and then as in the first step 
this implies that all cycles in $\pi$ have an arithmetic mean greater than or equal to $x$,
and we conclude as in the first step that $\mathrm{FirstCycleReset}\xspace_v(\pi) \ge x$.

Or $\pi$ contains $v$. We first argue that $x =   \textrm{val}^{\sigma_{\text{FCR}(v)}}(v_0) \le   \textrm{val}^{\sigma_{\text{FCR}(v)}}(v)$.
Indeed, let $\pi_0$ be a play without cycles from $v_0$ to $v$ consistent with $\sigma_{\text{FCR}(v)}$,
we let $\sigma'(\pi) = \sigma_{\text{FCR}(v)}(\pi_0 \pi)$.
Then $\textrm{val}^{\sigma_{\text{FCR}(v)}}(v_0) \le   \textrm{val}^{\sigma'}(v) \le   \textrm{val}^{\sigma_{\text{FCR}(v)}}(v)$,
the first inequality is because a play $\pi$ consistent with $\sigma'$ from $v$ 
correspond to the play $\pi_0 \pi$ consistent with $\sigma_{\text{FCR}(v)}$ from $v_0$,
and the second inequality by optimality of $\sigma_{\text{FCR}(v)}$.

Let $y =   \textrm{val}^{\sigma_{\text{FCR}(v)}}(v)$, the inequality above reads $x \le y$.
Let $\pi'$ the suffix of $\pi$ starting from the first occurrence of $v$,
then $\pi'$ is consistent with $\sigma_{\text{FCR}(v)}$ from $v$,
so as in the first step this implies that all cycles in $\pi'$ have an arithmetic mean greater than or equal to $y$.
We conclude as in the first step that $\mathtt{MeanPayoff}^+(\pi') \ge y \ge x$,
The last but important argument is that $\mathtt{MeanPayoff}^+$ is prefix independent,
implying that $\mathtt{MeanPayoff}^+(\pi) \ge x$.

We prove that $\textrm{val}^{ \mathcal{G}} =   \textrm{val}^{ \mathcal{G}_{\text{FCR}(v)}}$ using the two claims
following the same arguments as in the first step.
In particular we need to establish that $\mathcal{G}_{\text{FCR}(v)}$ is determined,
and again it either follows from the general Borel determinacy result ({prf:ref}`1-thm:borel_determinacy`)
or by determinacy for finite duration games.

**Step 3.**
We (finally!) prove that $\mathcal{G}_{\text{FC}}$ is positionally determined for both players.
Let us prove positional determinacy for Eve, the case of Adam being symmetric.
We show that for all games there exists an optimal positional strategy,
by induction on the number of vertices of Eve with more than one outgoing edge.
The base case is clear since in that case there is a unique strategy and it is positional.
Let $v \in  V_\mathrm{Eve}$ with more than one outgoing edge.

Let $\sigma_{\text{FCR}(v)}$ an optimal strategy in $\mathcal{G}_{\text{FCR}(v)}$.
Intuitively, since the game is reset at the first visit of $v$ and that the second visit to $v$ would close a loop hence determine the outcome, 
we can use any optimal strategy from $v$.
We define $\sigma'$ as follows:

$$
\sigma'(\pi) = 
\begin{cases}
\sigma(\pi) & \text{if } \pi \text{ does not contain } v, \\
\sigma(\pi_{\ge k}) & \text{for } k \text{ the last index such that }   \textrm{In}(\pi_k) = v.
\end{cases}
$$

Note that indeed $\sigma'$ uses only one outgoing edge of $v$.
We show that $\textrm{val}^{ \mathcal{G}_{\text{FCR}(v)},\sigma}(v_0) \le   \textrm{val}^{ \mathcal{G}_{\text{FCR}(v)},\sigma'}(v_0)$,
implying that $\sigma'$ is optimal in $\mathcal{G}_{\text{FCR}(v)}$ and the inequality is an equality.

Let $\pi$ be a play consistent with $\sigma'$ from $v_0$.
If it does not contain $v$ it is consistent with $\sigma$, so $\mathrm{FirstCycleReset}\xspace_v(\pi) \ge   \textrm{val}^{ \mathcal{G}_{\text{FCR}(v)},\sigma}(v_0)$.
If it contains $v$, let $\pi'$ the suffix of $\pi$ starting from the first occurrence of $v$,
then $\mathrm{FirstCycleReset}\xspace_v(\pi) =  \mathrm{FirstCycle}\xspace(\pi')$.
Since $\pi'$ is consistent with $\sigma$ (until a cycle is formed) we have $\mathrm{FirstCycle}\xspace(\pi') \ge   \textrm{val}^{ \mathcal{G}_{\text{FCR}(v)},\sigma}(v_0)$,
implying that $\mathrm{FirstCycleReset}\xspace_v(\pi) \ge   \textrm{val}^{ \mathcal{G}_{\text{FCR}(v)},\sigma}(v_0)$.
We conclude: $\textrm{val}^{ \mathcal{G}_{\text{FCR}(v)},\sigma'}(v_0) \le   \textrm{val}^{ \mathcal{G}_{\text{FCR}(v)},\sigma}(v_0)$.

Let $\mathcal{B}$ the arena obtained from $\mathcal{A}$ by removing all outgoing edges of $v$ not used by $\sigma'$.
Let $\mathcal{G}'_{\text{FCR}(v)} = (\mathcal{B},  \mathrm{FirstCycleReset}\xspace_v)$ and $\mathcal{G}'_{\text{FC}} = (\mathcal{B},  \mathrm{FirstCycle}\xspace)$.
By definition we have $\textrm{val}^{ \mathcal{G}_{\text{FCR}(v)},\sigma'} =   \textrm{val}^{ \mathcal{G}'_{\text{FCR}(v)},\sigma'} =   \textrm{val}^{ \mathcal{G}'_{\text{FCR}(v)}}$.
In the previous step we proved that $\textrm{val}^{ \mathcal{G}'_{\text{FC}}} =   \textrm{val}^{ \mathcal{G}'_{\text{FCR}(v)}}$,
so $\textrm{val}^{ \mathcal{G}'_{\text{FC}}} =   \textrm{val}^{ \mathcal{G}_{\text{FC}}}$.
The arena $\mathcal{B}$ contains one less vertex of Eve with more than one outgoing edge,
so the induction hypothesis applies and implies that there exists an optimal strategy in $\mathcal{G}'_{\text{FC}}$,
which is also optimal in $\mathcal{G}_{\text{FC}}$ thanks to the equality $\textrm{val}^{ \mathcal{G}'_{\text{FC}}} =   \textrm{val}^{ \mathcal{G}_{\text{FC}}}$.

````

Let us extract from the proof of {prf:ref}`4-thm:mean_payoff_positional` a more general positionality result via first cycle games.

````{prf:theorem} Generalised positional determinacy
:label: 4-thm:first_cycle_games

Let $\Phi$ a quantitative objective over the set of colours $C$.
Let $f : C^* \to  \mathbb{R}$ satisfying the following properties,
for all games $\mathcal{G}$ with objective $\Phi$:

*  for all $x \in   \mathbb{R} \cup  \left\{ \pm \infty \right\}$, for all plays $\pi$,

$$
(\forall c \in  \mathrm{Cycles}\xspace(\pi),\ f(c) \ge x) \implies \Phi(\pi) \ge x,
$$

*  for all $x \in   \mathbb{R} \cup  \left\{ \pm \infty \right\}$, for all plays $\pi$,

$$
(\forall c \in  \mathrm{Cycles}\xspace(\pi),\ f(c) \le x) \implies \Phi(\pi) \le x,
$$

*  $\Phi$ is prefix independent.

Then $\Phi$ is positionally determined for both players.

````

In the proof above, the role of $f$ is played by the function $\mathrm{Mean}\xspace$.

The first two items are used to prove that the first cycle games induced by $f$ are equivalent to the games with objective $\Phi$,
and the third item to prove the equivalence with first cycle games with reset;
the equivalence between the two types of first cycle games yield the positionality of these games,
implying the positionality of games with objective $\Phi$.

````{prf:corollary} Limit superior and limit inferior mean payoff games
:label: 4-cor:rational-MP

*  Limit superior and limit inferior mean payoff games are equivalent:
for every arena $\mathcal{A}$ and colouring function $\mathfrak{c} : E \to  \mathbb{Z}$,
let $\mathcal{G}_{+} = ( \mathcal{A}, \mathtt{MeanPayoff}^+[ \mathfrak{c}])$ and $\mathcal{G}_{-} = ( \mathcal{A}, \mathtt{MeanPayoff}^-[ \mathfrak{c}])$,
then $\textrm{val}^{ \mathcal{G}_+} =   \textrm{val}^{ \mathcal{G}_-}$.
This implies that a positional strategy is optimal in $\mathcal{G}_+$ if and only if it is optimal in $\mathcal{G}_-$.

Since they are equivalent we speak of mean payoff games without specifying whether the objective is $\mathtt{MeanPayoff}^+$ or $\mathtt{MeanPayoff}^-$,
and write $\mathtt{MeanPayoff}$ instead.

*  For all mean payoff games $\mathcal{G}$ and vertices $v$, 
the value $\textrm{val}^ \mathcal{G}(v)$ is a rational number of the form $\frac{a}{n}$ with $a \in [-nW,nW]$,
where $W$ is the largest weight appearing in $\mathcal{G}$ in absolute value.

````

````{admonition} Proof
:class: dropdown tip

Thanks to {prf:ref}`4-thm:mean_payoff_positional`, there exist $\sigma_+$ and $\tau_+$ optimal positional strategies in $\mathcal{G}_+$
and $\sigma_-$ and $\tau_-$ optimal positional strategies in $\mathcal{G}_-$ (for the latter by duality).
By definition $\textrm{val}^{ \mathcal{G}_+}(v) =  \mathtt{MeanPayoff}^+(\pi^v_{\sigma_+,\tau_+})$ and $\textrm{val}^{ \mathcal{G}_-}(v) =  \mathtt{MeanPayoff}^-(\pi^v_{\sigma_-,\tau_-})$.
Since $\mathtt{MeanPayoff}^- \le  \mathtt{MeanPayoff}^+$ we already have $\textrm{val}^{ \mathcal{G}_-} \le   \textrm{val}^{ \mathcal{G}_+}$.

For two positional strategies $\sigma$ and $\tau$, the play $\pi^v_{\sigma,\tau}$ is a lasso, meaning of the form $\pi c^\omega$
with $\pi$ a simple path and $c$ a simple cycle, 
implying that $\mathtt{MeanPayoff}^+(\pi^v_{\sigma,\tau}) =  \mathtt{MeanPayoff}^-(\pi^v_{\sigma,\tau})$,
let us write $\mathtt{MeanPayoff}(\pi^v_{\sigma,\tau})$ for this value.

We have:

$$
 \mathtt{MeanPayoff}(\pi^v_{\sigma_+,\tau_+}) 
\le  \mathtt{MeanPayoff}(\pi^v_{\sigma_+,\tau_-})
\le  \mathtt{MeanPayoff}(\pi^v_{\sigma_-,\tau_-}),
$$

where the first inequality is by optimality of $\tau_-$ and the second inequality by optimality of $\sigma_-$.
Hence $\textrm{val}^{ \mathcal{G}_+} \le   \textrm{val}^{ \mathcal{G}_-}$, and finally $\textrm{val}^{ \mathcal{G}_+} =   \textrm{val}^{ \mathcal{G}_-}$.

For the second item, recall that $\textrm{val}^ \mathcal{G}(v) =  \mathtt{MeanPayoff}(\pi^v_{\sigma,\tau})$
with $\sigma$ and $\tau$ optimal positional strategies.
Let us write $\pi^v_{\sigma,\tau} = \pi c^\omega$ with $\pi$ a simple path and $c$ a simple cycle, 
then by prefix independence $\mathtt{MeanPayoff}(\pi^v_{\sigma,\tau}) =  \mathrm{Mean}\xspace(c)$,
thus $\textrm{val}^ \mathcal{G}(v)$ is the mean of at most $n$ weights from $\mathcal{G}$.

````

## \texorpdfstring{Solving mean payoff games in $\textrm{NP}\cap \textrm{coNP}$}{Solving mean payoff games in NP and coNP}

The positional determinacy of mean payoff games easily gives an upper bound on the complexity of **solving** these games.

````{prf:theorem} Complexity of mean payoff
:label: 4-thm:MP-NPcoNP

Solving mean payoff games is in $\textrm{NP}\cap \textrm{coNP}$.

````

````{admonition} Proof
:class: dropdown tip

The first ingredient for this proof is a polynomial time algorithm for solving the one player variants of mean payoff games.
Indeed, they correspond to the minimum cycle mean problem in a weighted graph,
which can be solved in polynomial time by a dynamic programming algorithm.
The second ingredient is the positional determinacy result proved in {prf:ref}`4-thm:mean_payoff_positional`.

Let us show the $\textrm{NP}$ membership. 
Consider a mean payoff game $\mathcal{G}$, a vertex $v$ and a threshold $x \in   \mathbb{Q} \cup  \left\{ \pm \infty \right\}$.
Thanks to {prf:ref}`4-thm:mean_payoff_positional`, we know that there exist an optimal positional strategy for Eve.
With a non-deterministic Turing machine, we may guess a positional strategy for Eve, and check that it ensures $x$ in $\mathcal{G}$ from $v$. 

Let us now show the $\textrm{coNP}$ membership. 
By determinacy of mean payoff games, whether Eve **cannot** ensure $x$ in $\mathcal{G}$ from $v$ 
is equivalent to whether Adam can ensure $x$ in $\mathcal{G}$ from $v$.
Again thanks to {prf:ref}`4-thm:mean_payoff_positional`, we know that there exist an optimal positional strategy for Adam.
With a non-deterministic Turing machine, we may guess a positional strategy for Adam, and check that it ensures $x$ in $\mathcal{G}$ from $v$. 

````

We can turn the non-deterministic algorithm given in {prf:ref}`4-thm:MP-NPcoNP` into a deterministic algorithm 
with exponential complexity since there are exponential many positional strategies.

We now show that solving mean payoff games is at least as hard as solving parity games.

````{prf:theorem} Link with parity games
:label: 4-thm:parity2MP

  Solving parity games reduce in polynomial time to solving mean payoff games with threshold $0$.

````

````{admonition} Proof
:class: dropdown tip

Let $\mathcal{G} = ( \mathcal{A},  \mathtt{Parity}[ \mathfrak{c}])$ a parity game with $n$ vertices and priorities in $[1,d]$.
We construct a mean payoff game $\mathcal{G}' = ( \mathcal{A},  \mathtt{MeanPayoff}[ \mathfrak{c}'])$ using the same arena:

$$
 \mathfrak{c}'(v) = (-n)^{ \mathfrak{c}(v)}.
$$

Note that $\mathfrak{c}'(v)$ is of polynomial size since $\log(| \mathfrak{c}'(v)|) =  \mathfrak{c}(v) \log(n) \leq d \log(n)$.

The key property relating $\mathfrak{c}'$ and $\mathfrak{c}$ is the following:
for $c = v_0 \dots v_{k-1}$ a simple cycle (implying $k \le n$),
the largest priority in $c$ is even 
if and only if $\mathrm{Mean}\xspace(c) \ge 0$.
Indeed, if the largest priority in $c$ is $p$ even reached in $v_i$ then $\mathfrak{c}'(v_i) = n^p$
and for $j \neq i$ we have $\mathfrak{c}'(v_j) \ge -n^{p-1}$,
and since there are at most $n$ vertices in total the largest priority dominates the others.

We claim that $W_\mathrm{Eve}( \mathcal{G}) =  W_\mathrm{Eve}( \mathcal{G}')$.

Let $\sigma$ be a positional strategy winning from $W_\mathrm{Eve}( \mathcal{G})$, we show that $\sigma$ is also winning from $W_\mathrm{Eve}( \mathcal{G})$ in $\mathcal{G}'$.
Since mean payoff are uniformly positionally determined for both players (see {prf:ref}`4-thm:mean_payoff_positional`),
there exists $\tau$ a positional strategy winning from $W_\mathrm{Adam}( \mathcal{G}')$.
Let $v \in  W_\mathrm{Eve}( \mathcal{G})$, we consider $\pi = \pi^v_{\sigma,\tau}$ the play consistent with $\sigma$ and $\tau$ starting from $v$.
Since $\sigma$ and $\tau$ are positional, $\pi$ is a simple path followed by a simple cycle $c$.
Because $\sigma$ is winning the largest priority in $c$ is even, 
so thanks to the property above $\mathrm{Mean}\xspace(c) \ge 0$, meaning that $\mathtt{MeanPayoff}(\pi) \ge 0$.
Thus $W_\mathrm{Eve}( \mathcal{G}) \subseteq  W_\mathrm{Eve}( \mathcal{G}')$.
The converse implication is proved similarly swapping the two players.

````

We note that we did not construct a reduction between objectives as defined in Section {ref}`1-sec:reductions`:
indeed it is not true that $\mathtt{Parity}$ reduces to $\mathtt{MeanPayoff}_{\ge 0}$, the reduction depends on the number $n$ of vertices.

As a corollary of {prf:ref}`4-thm:MP-NPcoNP`, this polynomial reduction gives an alternative proof of the fact
that solving parity games is in $\textrm{NP} \cap  \textrm{coNP}$.

## A strategy improvement algorithm

````{prf:theorem} Strategy improvement algorithm
:label: 4-thm:strategy_improvement

There exists a strategy improvement algorithm for solving mean payoff games in \mynote{FILL IN}.

````

We rely on the high-level presentation of strategy improvement algorithms given in Section {ref}`1-sec:strategy_improvement`.
The algorithm is very similar and actually extends the strategy improvement algorithm for parity games presented in Section {ref}`3-sec:strategy_improvement`.

> **Adding the option of stopping the game.**

Let $\mathcal{G}$ be a mean payoff game with weights in $[-W,W]$.
Let us give Eve an extra move $\mathtt{-}$ that indicates that the game should stop and that she can play from any vertex of hers.
So a strategy for Eve is now a function $\sigma :  V_\mathrm{Eve} \rightarrow E \cup  \left\{  \mathtt{- \right\}}$ 
where $\sigma(v) =  \mathtt{-}$ indicates that Eve has chosen to stop the game, and $\sigma(v) \ne  \mathtt{-}$ should be interpreted as normal.
Adam is not allowed to stop the game, so strategies for Adam remain unchanged.
We say that a play ending with $\mathtt{-}$ is stopped.

For reasoning it will be useful to consider the mean payoff graph $\mathcal{G}[\sigma]$ obtained from $\mathcal{G}$ by restricting the outgoing edges from $V_\mathrm{Eve}$
to those prescribed by $\sigma$. 
We say that a mean payoff graph (without stopping option) satisfies mean payoff from $v$ if all infinite paths $\pi$ from $v$ satisfy 
$\mathtt{MeanPayoff}(\pi) \ge 0$.
Then a strategy $\sigma$ is winning from $v$ if and only if the mean payoff graph $\mathcal{G}[\sigma]$ satisfies mean payoff from $v$.

Since we added the option for Eve to stop the game we introduce a new terminology: 
we say that a strategy $\sigma$ respects mean payoff if all infinite plays consistent with $\sigma$ satisfy mean payoff,
equivalently all infinite paths in $\mathcal{G}[\sigma]$ satisfy mean payoff, not requiring anything of stopped plays.

We say that a cycle is non-negative if the sum of the weights in the cycle is non-negative, and it is negative otherwise. 
Respecting mean payoff is characterised using cycles:

````{prf:observation} Characterisation using cycles
:label: 4-fact:characterisation

A strategy $\sigma$ respects mean payoff if and only if all cycles in $\mathcal{G}[\sigma]$ are non-negative.

````

The algorithm will only manipulate strategies respecting mean payoff.

> **Evaluating a strategy.**

The first question is: given a strategy $\sigma$, how to evaluate it (in order to later improve it)?
As explained in Section {ref}`1-sec:strategy_improvement` towards this goal we define a value function $\textrm{val}^{\sigma} : V \to Y$.

We let $\textrm{val}^{\sigma}(v) = \min_\tau   \textrm{val}( \pi_{\sigma,\tau}^v)$ where $\tau$ ranges over (general) strategies for Adam, so we first need to define the value of the play $\pi =  \pi_{\sigma,\tau}^v$.
If $\pi$ is stopped, then $\textrm{val}( \pi)$ is the sum of the weights in $\pi$.
Otherwise $\textrm{val}( \pi)$ is $\top$ if $\pi$ satisfies mean payoff, and $\bot$ if $\pi$ does not satisfy mean payoff.
So the value of a play is either $\top$, $\bot$, or an integer;
we let $Y =   \mathbb{Z} \cup  \left\{ \pm \infty \right\}$ and equip it with the natural order $\le$.

> **The value function as a fixed point.**

We define $\delta : Y \times [-W,W] \to Y$ by

$$
\delta(t,w) = 
\begin{cases}
t + w & \text{ if } t \in  \mathbb{Z}, \\
\top & \text{ if } t = \top, \\
\bot & \text{ if } t = \bot.
\end{cases}
$$

We note that $\delta$ is monotonic: for all $w \in Y$,
if $t \le t'$ then $\delta(t,w) \le \delta(t',w)$. 
We extend $\delta$ to $\delta : Y \times [-W,W]^* \to Y$.

We let $F^\sigma_V$ denote the set of functions $\mu : V \to Y$ such that $\mu(v) = \emptyset$ if $\sigma(v) =  \mathtt{-}$,
it is a lattice when equipped with the componentwise (partial) order induced by $Y$:
we say that $\mu \le \mu'$ if for all vertices $v$ we have $\mu(v) \le \mu'(v)$.
We then define an operator $\mathbb{O} : F^\sigma_V \to F^\sigma_V$ by

$$
 \mathbb{O}(\mu)(v) = 
\begin{cases}
\min  \left\{ \delta( \mu(v'),  \mathfrak{c \right\}(v)) : (v,v') \in E} & \text{if } \sigma(v) \neq  \mathtt{-} \\
\emptyset & \text{if } \sigma(v) =  \mathtt{-}.
\end{cases}
$$

Since $\delta$ is monotonic so is $\mathbb{O}$.

````{prf:observation} NEEDS LABEL Fixed point
\label{4-fact:fixed-point]
The function $\textrm{val}^\sigma$ is a fixed point of $\mathbb{O}$ in $F^\sigma_V$.

````

Unfortunately, $\textrm{val}^{\sigma}$ is not in general the greatest fixed point of $\mathbb{O}$ in $F^\sigma_V$;
let us analyse this in more details.
Let $\mu$ a fixed point of $\mathbb{O}$ in $F^\sigma_V$, there are two cases. 
For a vertex $v$ such that there exists a stopped play $\pi$ starting from $v$, we have $\mu(v) \le   \textrm{val}(\pi)$, and more generally
$\mu(v) \le \inf_{\pi}   \textrm{val}(\pi)$ where $\pi$ ranges over all stopped plays starting from $v$.
The problem is for a vertex $v$ such that no plays starting from $v$ are stopped: 
we can have either $\mu(v) = \top$ or $\mu(v) = \bot$, irrespective of whether the play satisfies mean payoff or not.
From this discussion we obtain the following result.

````{prf:lemma} Greatest fixed point
:label: 4-lem:greatest_fixed_point

If $\sigma$ respects mean payoff, then $\textrm{val}^{\sigma}$ is the greatest fixed point of $\mathbb{O}$ in $F^\sigma_V$.

````

> **Improving a strategy.**

We reach the last item in the construction of the algorithm: the notion of switchable edges.
Let $\sigma$ a strategy. We say that an edge $e = (v,v')$ is switchable if

$$
\delta(  \textrm{val}^{\sigma}(v'), \mathfrak{c}(v)) > \delta(  \textrm{val}^{\sigma}(u), \mathfrak{c}(v)) \text{ where } \sigma(v) = (v,u).
$$

Intuitively: according to $\textrm{val}^{\sigma}$, playing $e$ is better than playing $\sigma(v)$.

Given a strategy $\sigma$ and an edge $e = (v,v')$ we use $\sigma[v \to e]$ to denote the strategy playing $e$ from $v$ 
and follow $\sigma$ from all other vertices.
Let us write $\sigma \le \sigma'$ if for all vertices $v$ we have $\textrm{val}^{\sigma}(v) \le   \textrm{val}^{\sigma'}(v)$,
and $\sigma < \sigma'$ if additionally $\neg (\sigma' \le \sigma)$.

> **The algorithm.**

The algorithm starts with a specified initial strategy, which is the strategy
$\sigma_0$ where $\sigma_0(v) =  \mathtt{-}$ for all vertices $v \in  V_\mathrm{Eve}$. 
It may not hold that $\sigma_0$ respects mean payoff since $\mathcal{G}$ may contain negative cycles fully controlled by Adam.
This can be checked in linear time and the attractor to the corresponding vertices removed from the game.
After this preprocessing $\sigma_0$ indeed respects mean payoff.

The pseudocode of the algorithm is given in {numref}`4-algo:strategy_improvement`.

```{figure} ./../FigAndAlgos/4-algo:strategy_improvement.png
:name: 4-algo:strategy_improvement
:align: center
The strategy improvement algorithm for mean payoff games.
```

> **Proof of correctness.**

We start by stating a very simple property of $\delta$, which is key in the arguments below.

````{prf:observation} Non-negative sum of weights
:label: 4-fact:non-negative-sum

Let $t \in Y$ and $w_1,\dots,w_k \in [-W,W]$ such that $t$ and $\delta(t,w_1 \dots w_k)$ are neither $\top$ nor $\bot$.
Then $t \le \delta(t,w_1 \dots w_k)$ if and only if $\sum_{i \in [1,k]} w_i \ge 0$.

````

The following lemma states the two important properties of $(Y,\le)$ and $\delta$.

````{prf:lemma} Value functions vs satisfaction of mean payoff
:label: 4-lem:key_property

Let $G$ a mean payoff graph (with no stopping option).

*  If there exists $\mu : V \to Y$ such that for all vertices $v$ we have $\mu(v) \neq \top,\bot$
and for all edges $(v,u) \in E$ we have $\mu(v) \le \delta(\mu(u), \mathfrak{c}(v))$,
then $G$ satisfies mean payoff.
*  If there exists $\mu : V \to Y$ such that for all vertices $v$ we have $\mu(v) \neq \top,\bot$
and for all edges $(v,u) \in E$ we have $\mu(v) \ge \delta(\mu(u), \mathfrak{c}(v))$,
then $G$ satisfies the complement of mean payoff.

````

````{admonition} Proof
:class: dropdown tip

We prove the first property, the second is proved in exactly the same way.
Thanks to the characterisation using cycles it is enough to show that all cycles in $G$ are non-negative.
Let us consider a cycle in $G$:

$$
\pi = v_0 v_1 \dots v_{k-1}.
$$

For all $i \in [0,k-1]$ we have $\mu(v_i) \le \delta(\mu(v_{i+1 \mod k}), \mathfrak{c}(v_i))$.
By monotonicity of $\delta$ this implies $\mu(v_1) \le \delta(\mu(v_1), \mathfrak{c}(v_{k-1}) \cdots  \mathfrak{c}(v_0))$.
Thanks to {prf:ref}`4-fact:non-negative-sum`, this implies that $\sum_{i \in [0,k-1]}  \mathfrak{c}(v_i) \ge 0$.

````

Let $\sigma$ a strategy respecting mean payoff. 
A progress measure for $\mathcal{G}[\sigma]$ is a post-fixed point of $\mathbb{O}$ in $F^\sigma_V$:
it is a function $\mu : V \to Y$ such that $\mu(v) = \emptyset$ if $\sigma(v) =  \mathtt{-}$ and $\mu \le  \mathbb{O}(\mu)$,
which means that $\mu(v) \le \min  \left\{  \delta(\mu(v'), \mathfrak{c \right\}(v)) : (v,v') \in E}$.

We now rely on {prf:ref}`4-lem:greatest_fixed_point` and {prf:ref}`4-lem:key_property` to prove the two principles: progress and optimality.

````{prf:lemma} Progress
:label: 4-lem:progress

Let $\sigma$ be a strategy respecting mean payoff and $e = (v,v')$ be a switchable edge.
We let $\sigma'$ denote $\sigma[v \to e]$.
Then $\sigma'$ respects mean payoff and $\sigma < \sigma'$.

````

````{admonition} Proof
:class: dropdown tip

We first argue that $\sigma'$ respects mean payoff.
The fact that $e = (v,v')$ is switchable reads

$$
\delta(  \textrm{val}^\sigma(v'), \mathfrak{c}(v)) > \delta(  \textrm{val}^\sigma(u), \mathfrak{c}(v)),
$$

and by definition of $\textrm{val}^\sigma$ we have $\textrm{val}^\sigma(v) = \delta(  \textrm{val}^\sigma(u), \mathfrak{c}(v))$,
which implies $\textrm{val}^\sigma(v) < \delta(  \textrm{val}^\sigma(v'), \mathfrak{c}(v))$, and in particular $\textrm{val}^\sigma(v) \neq \top$.

Let us consider the mean payoff graph $\mathcal{G}[\sigma']$ and note that for all edges $e' = (s,t)$ 
we have $\textrm{val}^\sigma(s) \le \delta(  \textrm{val}^\sigma(t), \mathfrak{c}(s))$:
indeed either $e'$ is an edge in $\mathcal{G}[\sigma]$ and this is by definition of $\textrm{val}^\sigma$,
or $e' = e$ and the inequality was proved just above.

Since $\sigma$ respects mean payoff $\textrm{val}^\sigma$ does not take the value $\bot$.
But we cannot apply (the first item of) {prf:ref}`4-lem:key_property` yet because $\textrm{val}^\sigma$ may have value $\top$.
However by definition of $\textrm{val}^\sigma$ for all vertices $s$ such that $\textrm{val}^\sigma(s) = \top$ all paths from $s$ satisfy mean payoff,
so it is enough to consider the mean payoff graph obtained from $\mathcal{G}[\sigma']$ by removing all such vertices.
The first item of {prf:ref}`4-lem:key_property` implies that it satisfies mean payoff, hence $\mathcal{G}[\sigma']$ as well.

At this point we know that $\sigma'$ respects mean payoff, which thanks to {prf:ref}`4-lem:greatest_fixed_point`
implies that $\textrm{val}^{\sigma'}$ is the greatest fixed point of $\mathbb{O}$ in $F^{\sigma'}_V$.

We now argue that $\textrm{val}^\sigma$ is a progress measure for $\mathcal{G}[\sigma']$.
For all vertices but $v$ this is clear because the outgoing edges are the same in $\mathcal{G}[\sigma]$ and in $\mathcal{G}[\sigma']$.
For $v$ as argued above we have $\textrm{val}^\sigma(v) < \delta(  \textrm{val}^\sigma(v'), \mathfrak{c}(v))$.
It follows that $\textrm{val}^\sigma$ is indeed a progress measure for $\mathcal{G}[\sigma']$.
Since $\textrm{val}^{\sigma'}$ is the greatest fixed point of $\mathbb{O}$ in $F^{\sigma'}_V$, this implies that 
$\textrm{val}^{\sigma} \le   \textrm{val}^{\sigma'}$.

We now show that $\textrm{val}^{\sigma} <   \textrm{val}^{\sigma'}$. 
Using $\textrm{val}^{\sigma}(v') \le   \textrm{val}^{\sigma'}(v')$ and the monotonicity of $\delta$ we obtain that
$\delta(  \textrm{val}^\sigma(v'), \mathfrak{c}(v)) \le \delta(  \textrm{val}^{\sigma'}(v'), \mathfrak{c}(v))$.
By definition of $\textrm{val}^{\sigma'}$ we have $\textrm{val}^{\sigma'}(v) = \delta(  \textrm{val}^{\sigma'}(v'), \mathfrak{c}(v))$
and together with $\textrm{val}^\sigma(v) < \delta(  \textrm{val}^\sigma(v'), \mathfrak{c}(v))$ this implies that
$\textrm{val}^\sigma(v) <   \textrm{val}^{\sigma'}(v)$.

````

````{prf:lemma} Optimality
:label: 4-lem:optimality

Let $\sigma$ be a strategy respecting mean payoff that has no switchable edges, then 
$\sigma$ is winning from all vertices of $W_\mathrm{Eve}(  \mathcal{G})$.

````

````{admonition} Proof
:class: dropdown tip

The fact that $\sigma$ respects mean payoff means that it is a winning strategy
from all vertices $v$ such that $\textrm{val}^\sigma(v) = \top$.
It also implies that for all vertices $v$ we have $\textrm{val}^{\sigma}(v) \neq \bot$.
We now prove that Adam has a winning strategy from all vertices $v$ such that $\textrm{val}^{\sigma}(v) \neq \top$.
We construct a strategy of Adam by

$$
\forall v \in  V_\mathrm{Adam},\ \tau(v) =  \textrm{argmin}  \left\{  \delta(  \textrm{val}^{\sigma \right\}(u), \mathfrak{c}(v)) : (v,u) \in E }.
$$

We argue that $\tau$ ensures the complement of mean payoff from all vertices $v$ such that $\textrm{val}^{\sigma}(v) \neq \top$.
Let us consider $\mathcal{G}[\tau]$ the mean payoff graph obtained from $\mathcal{G}$ by restricting the outgoing edges from $V_\mathrm{Adam}$
to those prescribed by $\tau$.
We argue that for all edges $(v,,v')$ in $\mathcal{G}[\tau]$, we have 
$\textrm{val}^{\sigma}(v) \ge \delta(  \textrm{val}^{\sigma}(v'), \mathfrak{c}(v))$.
Once this is proved we conclude using the second item of {prf:ref}`4-lem:key_property` implying that $\mathcal{G}[\tau]$ satisfies the complement of mean payoff.

The first case is when $v \in  V_\mathrm{Eve}$. 
Let $\sigma(v) = (v,u)$.
Since the edge $e = (v,v')$ is not switchable we have 
$\delta(  \textrm{val}^{\sigma}(v'), \mathfrak{c}(v)) \le \delta(  \textrm{val}^{\sigma}(u), \mathfrak{c}(v))$.
By definition of $\textrm{val}^\sigma$ we have $\textrm{val}^\sigma(v) = \delta(  \textrm{val}^{\sigma}(u), \mathfrak{c}(v))$,
implying the desired inequality.

The second case is when $v \in  V_\mathrm{Adam}$, it holds by definition of $\tau$.

````

> **Complexity analysis.**

\mynote{WORK HERE}
The computation of $\textrm{val}^\sigma$ for a strategy $\sigma$ can be seen to be a shortest path problem where distances are measured using the operator $\le$. 
Thus, any algorithm for the shortest path problem can be applied, such as the Bellman-Ford algorithm.
In particular computing $\textrm{val}^\sigma$ can be done in polynomial time, and even more efficiently through a refined analysis.

An aspect of the algorithm we did not develop is choosing the switchable edge.
It is possible to switch not only one edge but a set of switchable edges at each iteration, making this question worse: 
which subset of the switchable edges should be chosen?
Many possible rules for choosing this set have been studied, as for instance the **greedy all-switches** rule. 

The next question is the number of iterations, meaning the length of the sequence
$\sigma_0,\sigma_1,\dots$. It is at most exponential since it is bounded by the number of strategies (which is bounded aggressively by $m^n$).
There are lower bounds showing that the sequence can be of exponential length, which apply to different rules for choosing switchable edges.
Hence the overall complexity is exponential; we do not elaborate further here. 
We refer to Section {ref}`4-sec:references` for bibliographic references and a discussion on the family of strategy improvement algorithms.

Notice that we can easily compute the largest progress measure
(i.e. the value) of $G$ by an adaptation of Bellman-Ford algorithm
computing shortest paths from all sources to the sink vertex
$\octagon$. For a positional strategy $\sigma$ of Eve, we let
$\mathcal{G}[\sigma]$ the graph obtained by removing all edges
$(v,c,w)\in E$ different from the choice $\sigma(v)$.

The complexity of this algorithm depends on the size of the graph of
the game, but also on the maximal weight
$W = \max_{(v,c,v')\in E} |c|$ on edges of the arena, in absolute
values. Indeed, notice that the largest progress measure of a graph
$\mathcal{G}[\sigma]$, with $\sigma$ an admissible strategy, has all its
values in $\{-(n-1)W,(n-1)W\}\cup\{+\infty\}$: this is because
finite values are weights of finite paths with no cycles, that
therefore must have at most $n-1$ edges, each of weight bounded in
absolute value by $W$. A switch must increase the value of at
least one vertex by $1$; since there are $n$ vertices, the total
number of switches is therefore bounded by $O(n^2W)$. At
each iteration, the most expensive computation lies in the computation
of the largest progress measure in $\mathcal{G}[\sigma]$. As we have seen,
this can be done by using Bellman-Ford algorithm, which requires
$O(nm)$ operations. In the overall, this strategy
improvement algorithm therefore costs $O(n^3mW)$
operations. In (Section 6 in {cite}`Bjorklund&Vorobyov:2007`), this bound
is improved in $O(n^2 mW)$ by replacing the use of
Bellman-Ford algorithm by a more clever computation.

> **A binary search to compute the values.**

Now that we know how to decide if Eve has a strategy to ensure a
positive value, we can even use this procedure to compute the values
of the game in case of an arena with only integral
costs. By {prf:ref}`4-cor:rational-MP`, we know that the value $\textrm{val}(v)$
of all vertices $v$ is a rational number with denominator in
$\{1,\ldots,n\}$. Moreover, since it is the average value of the
weight of a cycle, it lies in the interval $[-W,W]$. A binary search
of the value will thus require $\log_2(n^2W)$ steps. We can use the
previous strategy improvement algorithm to decide whether Eve can
guarantee a value greater than $\alpha$ for a given rational $\alpha$:
it is equivalent to testing whether Eve can guarantee a value greater
than $0$ in a modified game where all edge weights have been
subtracted by $\alpha$. The complexity proof shown above for the
strategy improvement algorithm is however different when the weights
of edges are rational, instead of integers, since the number of
switches can now be bigger. Indeed, the largest progress measure is
now the weight of a path of length $k\leq n$ which is thus of the form
$(\sum_{i=1}^k c_i)-k\alpha$, with $c_i$ the original weights of
edges. There are still $O(n^2W)$ possible weights of this form,
which implies that

````{prf:theorem} Binary search computation
:label: 4-thm:MP-strategy-improvement-binary-search

  Strategy improvement algorithm with a binary search computes the
  values of a mean payoff game in time
  $O(n^3 mW(\log n+\log W))$.

````

This algorithm can be randomised, as also shown in
{cite}`Bjorklund&Vorobyov:2007`: the expected complexity then becomes
$\min[ O(n^3 mW(\log n+\log W)),(\log W) 2^{\mathcal
  O(\sqrt{n\log n})}]$.

## A value iteration algorithm

Instead of a strategy improvement algorithm to find vertices from
which Eve can guarantee a mean payoff $>0$, we now give an algorithm
that finds vertices from which Eve can guarantee a mean payoff
$\geq 0$, called value iteration
{cite}`Brim&Chaloupka&Doyen&Gentilini&Raskin:2011`. Instead of relying
on switches amongst admissible strategies of Eve, it relies on an
iterative computation of the greatest fixed-point of a monotonous
operator relying on a similar notion of progress measures as before.

We first need to extend the notion of progress measures from graphs to
games: we choose a definition consistent with the one presented above,
thus slightly adapted with respect to
{cite}`Brim&Chaloupka&Doyen&Gentilini&Raskin:2011`. A progress measure
for a mean payoff game $\mathcal{G}$ is a function $\mu\colon V\to  \overline \mathbb{R}$ with
$\overline \mathbb{R} =  \mathbb{R}\cup\{-\infty,+\infty\}$ such that

$$

  \forall v\in V_\mathrm{Eve}\quad \mu(v)&\leq
                               \min\big(0,\max_{(v,c,v')\in E}(\mu(v')+c)\big)\\
  \forall v\in V_\mathrm{Adam}\quad \mu(v)&\leq \min\big(0, \min_{(v,c,v')\in E}(\mu(v')+c)\big)

$$

The minimisation with $0$ reflects the stratagem we used in strategy
iteration to allow Eve to stop the game prematurely. Once again,
progress measures can be compared pointwise: $\mu\leq \mu'$ if
$\mu(v)\leq \mu'(v)$ for all vertices $v$. Since every subset of
progress measure has an infimum and a supremum, this makes the set of
all progress measures a complete lattice. It is not empty, since the
function mapping each vertex to $-\infty$ is a progress
measure. Therefore, there exists a greatest progress measure.

````{prf:theorem} Greatest progress measure
:label: 4-thm:greatest-progress-measure

  Let $\mathcal{G}$ be a mean payoff game. The greatest progress measure $\mu$
  of $\mathcal{G}$ is such that Eve can guarantee a non-negative mean payoff
  from $v$ if and only if $\mu(v)\neq -\infty$.

````

````{admonition} Proof
:class: dropdown tip

  We consider the qualitative game with non-negative mean payoff as an
  objective.

  We first prove that for all progress measures $\mu$, if $\mu(v)\neq
  -\infty$, then Eve wins mean payoff from $v$. Indeed, the progress
  measure $\mu$ induces a positional strategy for Eve defined by
  $\sigma(v)=(v,c,v')$ for an edge $(v,c,v')$ (that is certain to
  exist, by definition) such that $\mu(v)\leq \mu(v')+c$. We argue
  that $\sigma$ is a winning strategy from $U=\{v\mid \mu(v)\neq
  -\infty\}$. Let us consider the graph $G$ obtained by restricting
  $\mathcal{G}$ to vertices in $U$ and to edges prescribed by $\sigma$. The
  progress measure $\mu$ induces a progress measure for the graph $G$,
  so thanks to {prf:ref}`4-thm:MP-progress-measure`, the graph $G$
  satisfies mean payoff, which means that $\sigma$ is indeed winning
  from $U$.

  Reciprocally, let $\sigma$ be a positional strategy winning from the
  winning set $W_\mathrm{Eve}$ of Eve for mean payoff. We build a progress
  measure $\mu$ as follows. As above, we consider the graph $G$
  obtained by restricting $\mathcal{G}$ to vertices in $W_\mathrm{Eve}$ and to the
  edges prescribed by $\sigma$. Since $\sigma$ is a winning strategy,
  the graph $G$ satisfies mean payoff, so thanks
  to {prf:ref}`4-thm:MP-progress-measure`, there exists a largest progress
  measure $\mu\colon  W_\mathrm{Eve}\to  \mathbb{R}\cup\{+\infty\}$. It extends into a
  mapping $\mu'\colon V\to  \mathbb{R}\cup\{+\infty,-\infty\}$ by letting
  $\mu'(v)=-\infty$ if $v\in W_\mathrm{Adam}$, and $\mu'(v)=\min(0,\mu(v))$ if
  $v\in  W_\mathrm{Eve}$. This is a progress measure since, if $v\in  V_\mathrm{Adam}\cap W_\mathrm{Eve}$,
  $\mu'(v)=\min(0,\mu(v))\leq \min(0,\min_{(v,c,w)\in
  E}(\mu(w)+c)$\todo{Euh, non, ça va pas du tout !}  This progress
  measure satisfies the property that if $\mu'(v)\neq -\infty$ then
  $v\in  W_\mathrm{Eve}$. It follows that the greatest progress measure of $\mathcal{G}$
  satisfies the same property.

````

The value iteration algorithm consists in starting with the function
$\mu_0$ mapping each vertex $v$ to $0$: clearly, $\mu_0$ is greater
than or equal to the greatest progress measure of $\mathcal{G}$ (because of
the requirement that $\mu(v)$ must be at most $0$ in the definition of
progress measures). We then update it locally to try to patch local
discrepancies, until it is no longer possible, thus reaching a
progress measure, and even the greatest one, which, by the previous
theorem, gives the winning vertices for Eve.

The update is performed with an operator $\textrm{Lift}$ mapping each function
$\mu\colon V\to  \overline \mathbb{R}$ to a new function $\textrm{Lift}(\mu)\colon V\to  \overline \mathbb{R}$
defined for all vertices $v\in V$ by

$$\textrm{Lift}(\mu)(v) =
  \begin{cases}
     \mathop{\downarrow_{-(n-1)W}}\min\big(0,\max_{(v,c,v')\in E} (\mu(v')+c)\big) & \text{if } v\in
     V_\mathrm{Eve}\\
     \mathop{\downarrow_{-(n-1)W}}\min\big(0,\min_{(v,c,v')\in E} (\mu(v')+c)\big) & \text{if } v\in  V_\mathrm{Adam}
  \end{cases}$$

 where $\mathop{\downarrow_{k}}\colon  \overline \mathbb{R}\to  \overline \mathbb{R}$ is the
mapping defined by $\downward k(x) = x$ if $x\geq k$, and
$\downward k(x) = -\infty$ otherwise. The overall method, very
simple, is given in {numref}`4-algo:value_iteration_MP`.

```{figure} ./../FigAndAlgos/4-algo:value_iteration_MP.png
:name: 4-algo:value_iteration_MP
:align: center
The value iteration algorithm.
```

The co-domain of $\textrm{Lift}$ are functions
$V\to \{-\infty,-nW+1,-nW+2,\ldots,0\}$, i.e. a finite set of
functions. Therefore, $\textrm{Lift}$ is a Scott-continuous mapping over which
we can apply Kleene's fixed-point theorem, ensuring that the sequence
$( \textrm{Lift}^i(\mu_0))_{i\geq 0}$ converges towards the greatest fixed
point $\mu^*$ of $\textrm{Lift}$. By the fact that $\mu^*= \textrm{Lift}(\mu^*)$, we
can deduce that $\mu^*$ is a progress measure. We can indeed show that
this is the greatest progress measure of the game. The main ingredient
is that the use of the widening operator $\mathop{\downarrow_{-nW}}$ is
correct, i.e. that it does not jump over the greatest progress measure
which must map every vertex $v\in W_\mathrm{Eve}$ to the minimum between $0$ and
the weight of a finite path (as we have seen in the previous proof):
this weight is thus at least $-(n-1)W$, so that it is correct to
jump directly to $-\infty$ when we reach a value less than
that. Therefore, by {prf:ref}`4-thm:greatest-progress-measure`, the value
iteration algorithm returns the set of winning vertices for Eve.

We finally study the complexity of this algorithm. The
value associated to every vertex can decrease at most
$O(nW)$ times in total. Updating the value of a single
vertex $v$ can be done with a complexity linear in the number of
successors of $v$, i.e. linear in the size of
$\mathrm{post}(v) = \{(v,c,v')\in E\}$. By looking at all the
predecessors $\mathrm{pre}(v) = \{(v',c,v)\in E\}$ of a vertex $v$ we
have just updated, it is also possible to maintain the list of
vertices for which an update is required throughout the algorithm (see
{cite}`Brim&Chaloupka&Doyen&Gentilini&Raskin:2011` for a detailed
explanation), so that the overall complexity of the value iteration
algorithm is of the form

$$\sum_{v\in V} O\big((|\mathrm{post}(v)| +
  |\mathrm{pre}(v)|)nW\big) =  O(mn W)$$

````{prf:theorem} Value iteration algorithm
:label: 4-thm:MP-value-iteration-Brim

  Value iteration algorithm finds the set $W_\mathrm{Eve}$ of vertices from which
  Eve can guarantee a non-negative mean payoff in a game $\mathcal{G}$ with a
  complexity $O(mnW)$.

````

As a corollary, we can compute the values of all vertices in a
mean payoff game, using a similar binary search as explained before for
strategy improvement:

````{prf:theorem} Binary search computation
:label: 4-thm:MP-value-iteration-Brim-binary-search

  Value iteration algorithm with a binary search allows one to compute
  the values of a mean payoff game in time
  $O(n^2 mW(\log n+\log W))$.

````

