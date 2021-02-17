(12-sec:mean_payoff_energy)=
# Mean-payoff and energy

```{math}

\newcommand{\expv}{\mathbf{E}} \newcommand{\markovProcess}{\ensuremath{{\mathcal{P}} }}
\newcommand{\stratStoch}{\ensuremath{\tau^{\text{stoch}} }}
\newcommand{\BWC}{\text{BWC}}
\newcommand{\ecsSet}{\ensuremath{\mathcal{E}} }
\newcommand{\edgesNonZero}{\ensuremath{E_{\delta}} }
\newcommand{\ec}{\ensuremath{U} }
\newcommand{\playerOne}{\text{Eve} }
\newcommand{\playerTwo}{\text{Adam} }
\newcommand{\winningECs}{\ensuremath{\mathcal{W}} }
\newcommand{\losingECs}{\ensuremath{\mathcal{L}} }
\newcommand{\edges}{\ensuremath{E} }
\newcommand{\maxWinningECs}{\ensuremath{\mathcal{U}_{\textsc{w}}} }
\newcommand{\infVisited}[1]{\ensuremath{{\sf Inf}(#1)} }
\newcommand{\negligibleStates}{\ensuremath{V_{{\sf neg}}} }
\newcommand{\stratWC}{\ensuremath{\sigma^{\text{wc}}} }
\newcommand{\stratExp}{\ensuremath{\sigma^{\text{e}}} }
\newcommand{\stratComb}{\ensuremath{\sigma^{\text{cmb}}} }
\newcommand{\stratSecure}{\ensuremath{\sigma^{\text{sec}}} }
\newcommand{\stratWNS}{\ensuremath{\sigma^{\text{wns}}} }
\newcommand{\stratGlobal}{\ensuremath{\sigma^{\text{glb}}} }
\newcommand{\stepsWC}{\ensuremath{L} }
\newcommand{\stepsExp}{\ensuremath{K} }
\newcommand{\stepsGlobal}{\ensuremath{N} }
\newcommand{\cmbSum}{\ensuremath{\mathsf{Sum}} }
\newcommand{\typeA}{\ensuremath{**(a)**} }
\newcommand{\typeB}{\ensuremath{**(b)**} }
\newcommand{\thresholdWC}{\ensuremath{\alpha} }
\newcommand{\thresholdExp}{\ensuremath{\beta} }
\newcommand{\state}{\ensuremath{v} }
\newcommand{\gameNonZero}{\ensuremath{\arena_{\delta}} }
\newcommand{\reduc}{\ensuremath{\downharpoonright} }
\newcommand{\probm}{\mathbb{P}} 
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
Another well-known equivalence in one-dimension is the one between mean-payoff and energy games (in the existential initial credit form), mentioned in~\cref{chap:payoffs}. The reduction is trivial: Eve has a winning strategy (and an initial credit) in the energy game if and only if she has a strategy to ensure mean-payoff at least equal to zero in the mean-payoff game played over the same arena. Intuitively, the mean-payoff strategy of Eve has to reach a subgame where she can ensure that all cycles formed are non-negative (see cycle games in~\cref{chap:payoffs}). The initial credit (which can be as high as Eve wants) offsets the cost of reaching such a subgame as well as the low point of cycles in it (which can be negative but is bounded).

How does it fare in multiple dimensions? The study of vector games with energy semantics in Chapter {ref}`11-chap:counters` gives the following result.

````{prf:theorem} NEEDS TITLE 12-thm:MEG
:label: 12-thm:MEG

Solving multidimension energy games is \coNP-complete. Finite\--mem\-ory strategies are required for Eve and memoryless ones suffice for Adam.

````
 

Based on {prf:ref}`12-thm:MMP-Eve` and {prf:ref}`12-ex:MMP2`, it is clear that the aforementioned equivalence holds no more, as mean-payoff games benefit from infinite memory while energy games do not. In {prf:ref}`12-ex:MMP2`, the strategy that achieves $\vec{x} = (0, 0)$ for the mean-payoff does so by switching infinitely often but with decreasing frequency between $v_0$ and $v_1$: the switch becomes negligible in the limit which is fine for the mean-payoff. Still, this would lead the energy to drop below zero eventually, whatever the initial credit chosen by Eve, hence showing why the reduction does not carry over.


## Finite memory

Game-theoretic models are generally used in applications, such as controller synthesis, where one actually wants to **implement** a winning strategy when it exists. This is why finite-memory strategies have a particular appeal. Hence it is interesting to study what happens when we restrict Eve to finite-memory strategies in multidimension mean-payoff games. 

We first observe that when both players use finite-memory strategies, the resulting play is ultimately periodic, hence the lim-inf and lim-sup variants coincide (the limit exists) and take the value of the mean over the periodic part.

````{prf:proposition} NEEDS TITLE 12-prop:MPSI
:label: 12-prop:MPSI

The lim-sup and lim-inf variants of multidimension mean-payoff games coincide under finite-memory, i.e., their winning regions are identical in all games.

````

We now go back to the relationship with energy games. In the following, we write  $\vec{0}$ for the $k$-dimension vector $(0,\ldots{},0)$. When restricting both players to finite memory, we regain the equivalence between mean-payoff and energy games by a natural extension of the argument sketched above for one-dimension games.

````{prf:theorem} NEEDS TITLE 12-thm:MPEG-equivalence
:label: 12-thm:MPEG-equivalence

For all arena and initial vertex, Eve has a winning strategy for the existential initial credit multidimension energy game if and only if she has a finite-memory winning strategy for the multidimension mean-payoff game with threshold $\vec{x} = \vec{0}$.

````


````{admonition} Proof
:class: dropdown tip

Let $\arena$ be an arena coloured by integer vectors of dimension $k$ and $v_0$ be the initial vertex. We first consider the left-to-right implication. Assume that Eve has a strategy $\sigma$ and some initial credit $\vec{c}_0 \in \N^k$ such that she wins the energy objective over $\arena$. By {prf:ref}`12-thm:MEG`, we may assume $\sigma$ to be finite-memory and $\mem = (M, m_0, \delta)$ to be its memory structure. Let $\arena_\sigma$ be the classical product of the arena with this memory structure ($\arena \times \mem$) restricted to the choices made by $\sigma$. We claim that any cycle in $\arena_\sigma$ is non-negative in all dimensions (we simply project paths of $\arena_\sigma$ to $C^\omega$ to interpret them as we do for paths in $\arena$). By contradiction, assume that there exists a cycle whose sum of weights is strictly negative in some dimension. Then the play reaching this cycle and looping in it forever is a play consistent with $\sigma$ that is losing for the energy objective, contradicting the hypothesis. Hence, it is indeed the case that all reachable cycles in $\arena_\sigma$ are non-negative in all dimensions. Thus, $\sigma$ ensures mean-payoff at least equal to zero in all dimensions (for lim-inf and lim-sup variants).

In the opposite direction, assume that $\sigma$ is a finite-memory winning strategy for $\MeanPayoff^{-}_{\geq \vec{0}}$ (or equivalently $\MeanPayoff^{+}_{\geq \vec{0}}$). Using the same argument as before, we have that all cycles in $\arena_\sigma$ are non-negative. Therefore there exists some initial credit $\vec{c}_0 \in \N^k$ such that $\sigma$ satisfies the energy objective. As a trivial bound, one may take initial credit $\vert V\vert \cdot \vert M \vert \cdot W$ in all dimensions, where $\vert V\vert$ is the number of vertices of $\arena$, $\vert M \vert$ the number of memory states of $\mem$, and $W$ is the largest absolute weight appearing in the arena: this quantity bounds the lowest sum of weights achievable under an acyclic path.

````

Observe that the finite-memory assumption is crucial to lift mean-payoff winning strategies to the energy game. Intuitively, the reasoning would break for a strategy like the one used in {prf:ref}`12-ex:MMP2` because the memory structure would need to be infinite and $\arena_\sigma$ would actually not contain any cycle but an infinite path of ever-decreasing energy such that no bound on the initial credit could be established.

Also, note that {prf:ref}`12-thm:MPEG-equivalence` makes no mention of the specific variant of mean-payoff used. This is because both players play using finite-memory: Eve by hypothesis and Adam thanks to the equivalence and {prf:ref}`12-thm:MEG`. Hence, {prf:ref}`12-prop:MPSI` applies. To sum up, we obtain the following.

````{prf:corollary} NEEDS TITLE AND LABEL 
Solving multidimension mean-payoff games under finite-memory is \coNP-complete. Finite-mem\-ory strategies are required for Eve and memoryless ones suffice for Adam.
 

Solving multidimension mean-payoff games under finite-memory is \coNP-complete. Finite-mem\-ory strategies are required for Eve and memoryless ones suffice for Adam.

````



## Infinite memory

We now turn to the general case, where Eve is allowed to use infinite memory. By {prf:ref}`12-ex:MMP3`, we already know that lim-sup and lim-inf variants are not equivalent. We will cover the lim-sup case in details and end with a brief overview of the lim-inf one.

## Lim-sup variant

Without loss of generality, we fix the objective $\MeanPayoff^{+}_{\geq \vec{0}}$ (one can always modify the weights in the arena and consider the shifted-game with threshold zero). We have seen in our original example ({numref}`12-fig:MultiMP`) that Eve could focus on each dimension independently and alternatively in such a way that in the limit, she obtains the supremum in each dimension. This is the core idea that we will exploit.

````{prf:lemma} NEEDS TITLE 12-lem:MMP-Eve
:label: 12-lem:MMP-Eve

Let $\arena$ be an arena such that from all vertex $v \in \vertices$ and for all dimension $i$, $1 \leq i \leq k$, Eve has a winning strategy for $\{\play \in E^\omega \mid \MeanPayoff^{+}_{i}(\play) \geq 0\}$. Then, from all vertex $v \in \vertices$, she has a winning strategy for $\MeanPayoff^{+}_{\geq \vec{0}}$.

````

Hence, being able to win in each dimension **separately** suffices to guarantee winning in all dimensions **simultaneously**. Note that the converse is obvious.

````{admonition} Proof
:class: dropdown tip

For each vertex $v \in \vertices$ and dimension $i$, $1 \leq i \leq k$, let $\sigma_i^v$ be a winning strategy for Eve from $v$ for $\{\play \in E^\omega \mid \MeanPayoff^{+}_{i}(\play) \geq 0\}$.

Let $T_{\sigma_i^v}$ be the infinite tree obtained by **unfolding**  $\sigma_i^v$: it represents all plays consistent with this strategy. Formally, such a tree is obtained inductively as follows:

*  The root of the tree represents $v$.
*  Given a node $\eta$ representing the branch (i.

```{margin}
Nodes refer to the tree, vertices to the arena.
```

e., prefix of play) $\rho$ starting in vertex $v$ and ending in vertex $v_\eta$, we add children as follows:
\begin{itemize}
*  if $v_\eta \in V_{\text{Eve}}$, $\eta$ has a unique child representing the vertex $\out(e)$ reached through edge $e = \sigma_i^v(\rho)$;
*  otherwise $\eta$ has one child for each possible successor of $v_\eta$, i.e., for each $\out(e)$ such that $e \in E$ and $\ing(e) = v_\eta$.
 
\end{itemize} 
For $\varepsilon > 0$, we declare a node $\eta$ of $T_{\sigma_i^v}$ to be **$\varepsilon$-good** if the mean over dimension $i$ on the path from the root to $\eta$ is at least $-\varepsilon$ (as usual, we project this path to $C^\omega$ to evaluate it). For $\ell \in \N$, let $\widehat{T}^{i, \ell}_{v, \varepsilon}$ be the tree obtained from $T_{\sigma_i^v}$ by removing all descendants of $\varepsilon$-good nodes that are at depth at least $\ell$: hence, all branches of $\widehat{T}^{i, \ell}_{v, \varepsilon}$ have length at least $\ell$ and their leaves are $\varepsilon$-good.

We first show that $\widehat{T}^{i, \ell}_{v, \varepsilon}$ is a finite tree. By K\"onig's Lemma {cite}`Konig:1936`, we only need to show that every branch is finite. By contradiction, assume it is not the case and there exists some infinite branch. By construction, it implies that this branch contains no $\varepsilon$-good node after depth $\ell$. Thus, the corresponding play $\pi$, which is consistent with $\sigma_i^v$, necessarily has $\MeanPayoff^{+}_{i}(\play) \leq -\varepsilon$. This contradicts the hypothesis that $\sigma_i^v$ is winning for dimension $i$. Hence the tree is indeed finite.

Based on these finite trees, we now build an infinite-memory strategy for Eve that will be winning for the conjunct objective $\MeanPayoff^{+}_{\geq \vec{0}}$:

% \RestyleAlgo{plain}

\begin{algorithm}[ht]
$\varepsilon \leftarrow 1$

\Loop{
\For{$i = 1$ to $k$}{
Let $v$ be the current vertex, $L$ the length of the play so far.

$\ell \leftarrow \frac{L\cdot W}{\varepsilon}$

Play according to $\sigma_i^v$ until a leaf of $\widehat{T}^{i, \ell}_{v, \varepsilon}$ is reached.
}
$\varepsilon \leftarrow \frac{\varepsilon}{2}$
}
\end{algorithm}



 Recall that $W$ is the largest absolute weight in the game. Consider the situation whenever an iteration of the for-loop ends. Let $M$ be the number of steps the play followed $\sigma_i$ during this loop execution. Then, the mean-payoff in dimension $i$ is at least $\frac{-L\cdot W - M\cdot \varepsilon}{L + M} \geq \frac{-L\cdot W - M\cdot \varepsilon}{M}$. Since $M \geq \frac{L\cdot W}{\varepsilon}$ by definition, we obtain that the mean-payoff in dimension $i$ is at least $-2\cdot \varepsilon$.

Observe that since all trees are finite, we always exit the for-loop eventually, hence $\varepsilon$ tends to zero. Therefore, the supremum mean-payoff is at least zero in all dimensions, which makes this strategy winning for $\MeanPayoff^{+}_{\geq \vec{0}}$.

````

This construction is tight in the sense that infinite memory is needed for Eve, as previously proved. For Adam, we show a better situation. The proof scheme will also be the base of the upcoming algorithm.

````{prf:lemma} NEEDS TITLE 12-lem:MMP-Adam
:label: 12-lem:MMP-Adam

Memoryless strategies suffice for Adam in multidimension lim-sup mean-payoff games.

````


````{admonition} Proof
:class: dropdown tip

The proof works by induction on the number of vertices of the arena. The base case $\vert V\vert = 1$ is trivial. Assume the only vertex belongs to Adam. If there exists a self loop (recall we allow several edges per pair of vertices) which has a negative weight on some dimension, Adam wins by looping on it forever. In the opposite case, he cannot win.

Now assume $\vert V\vert \geq 2$. For $i \in \{1,\ldots,k\}$, let $W^i_{\text{Adam}}$ be the winning region of Adam for the complement of $\{\play \in E^\omega \mid \MeanPayoff^{+}_{i}(\play) \geq 0\}$, i.e., the region where Adam has a strategy to force a strictly negative mean-payoff in dimension $i$ (as studied in Section {ref}`4-sec:MP`). Let $W^{\text{disj}}_{\text{Adam}} = \bigcup_{i = 1}^{k} W^i_{\text{Adam}}$. We have two cases.

First, $W^{\text{disj}}_{\text{Adam}} = \emptyset$. Then, Eve can win all one-dimension games from everywhere and by {prf:ref}`12-lem:MMP-Eve`, she can also win for $\MeanPayoff^{+}_{\geq \vec{0}}$. Thus, Adam has no winning strategy.

Second, $W^{\text{disj}}_{\text{Adam}} \neq \emptyset$. Then, there exists $i \in \{1,\ldots,k\}$ such that $W^i_{\text{Adam}} \neq \emptyset$. In this set, Adam has a memoryless winning strategy $\tau_i$ to falsify objective $\{\play \in E^\omega \mid \MeanPayoff^{+}_{i}(\play) \geq 0\}$ (because one-dimension mean-payoff games are memoryless determined, as proved in {prf:ref}`4-thm:mean_payoff_positional`). This strategy also falsifies $\MeanPayoff^{+}_{\geq \vec{0}}$, hence $W^i_{\text{Adam}}$ is part of the winning region for Adam -- we denote it $W_{\text{Adam}}$, as usual.
By prefix independence of the mean-payoff, the attractor $W^{i, \Pre}_{\text{Adam}}= \AttrA(W^i_{\text{Adam}})$ is also part of $W_{\text{Adam}}$. We denote by $\tau_\Pre$ the corresponding attractor strategy of Adam. Moreover, the graph restricted to $\vertices \setminus W^{i, \Pre}_{\text{Adam}}$ constitutes a proper arena $\arena'$.

Let $W'_{\text{Adam}}$ be the winning region of Adam in $\arena'$ (for the original objective $\MeanPayoff^{+}_{\geq \vec{0}}$). The arena $\arena'$ has strictly less vertices than $\arena$ since we removed the non-empty region $W^i_{\text{Adam}}$. Hence we can apply the induction hypothesis: Adam has a memoryless winning strategy $\tau'$ in $W'_{\text{Adam}}$. The region $V \setminus (W^{i, \Pre}_{\text{Adam}} \cup W'_{\text{Adam}})$ is winning for Eve in $\arena'$ by determinacy. But it is also winning in $\arena$, i.e., the original game, since Adam cannot force the play to go in $W^{i, \Pre}_{\text{Adam}}$ from there (otherwise it would be part of the attractor too).

\todo{Would a figure be useful?}

We define the following memoryless strategy for Adam, which we claim is winning from $W_{\text{Adam}} = W^{i, \Pre}_{\text{Adam}} \cup W'_{\text{Adam}}$:

$$
\tau(v) =
\begin{cases}
\tau_\Pre(v) &\text{if } v \in W^{i, \Pre}_{\text{Adam}} \setminus W^{i}_{\text{Adam}},\\
\tau_i(v) &\text{if } v \in W^{i}_{\text{Adam}},\\
\tau'(v) &\text{if } v \in W'_{\text{Adam}}.
\end{cases}
$$

Since we already know that Eve wins from $V \setminus W_{\text{Adam}}$, it remains to prove that $\tau$ is winning from $W_{\text{Adam}}$ to conclude. Consider any play $\pi$ consistent with $\tau$ and starting in $W_{\text{Adam}}$. Two cases are possible. First, the play eventually reaches $W^{i}_{\text{Adam}}$ and Adam switches to $\tau_i$: then prefix independence of the mean-payoff guarantees that Adam wins. Second, the play never reaches $W^{i}_{\text{Adam}}$: then $\pi$ necessarily stays in $\arena'$, and $\tau'$ is winning from $W'_{\text{Adam}}$ in $\arena'$. Therefore, $\tau$ does win from everywhere in $W_{\text{Adam}}$, while being memoryless, which ends the proof.

````

We use the core reasoning of this proof to build an algorithm solving multidimension lim-sup mean-payoff games ({numref}`12-algo:MMP`). Intuitively, we iteratively remove vertices that are declared losing for Eve because Adam can win on some dimension from them. Such vertices can be computed in pseudo-polynomial time using the algorithm presented in~\cref{chap:payoffs}, \todo{I need a label on Subsect. 4.3.4 to cite it precisely.} here dubbed \textsf{SolveOneDimMeanPayoff}, and taking as parameters the arena and the considered dimension. Since removing vertices based on some dimension $i$ may decrease the power of Eve and her ability to win for another dimension $i'$, we need the outer loop: in the end, we ensure that $V'$ contains exactly all the vertices from which Eve has a winning strategy for each dimension. By {prf:ref}`12-lem:MMP-Eve` and the proof of {prf:ref}`12-lem:MMP-Adam`, we know that this is equal to $W_{\text{Eve}}$.

````{admonition} Remark 
\label{12-rmk:properArena}
The restriction $\arena' \downharpoonright V'$ defines a proper arena because $W^i_{\text{Adam}} = \AttrA(W^i_{\text{Adam}})$. Indeed, any vertex $v$ from which Adam can force to reach $W^i_{\text{Adam}}$ also belongs to $W^i_{\text{Adam}}$ by prefix independence of the mean-payoff.

````

\begin{algorithm}
 \KwData{Arena $\arena$ with vertices $\vertices$}
 \KwResult{$W_{\text{Eve}}$, the winning region of Eve for $\MeanPayoff^{+}_{\geq \vec{0}}$}
 $\arena' \leftarrow \arena$; $V' \leftarrow V$\;
 \Repeat{$LosingVertices = \text{false}$}{
  $LosingVertices \leftarrow \text{false}$\;
  \For{$i = 1$ to $k$}{
    $W^i_{\text{Adam}} \leftarrow V' \setminus \textsf{SolveOneDimMeanPayoff}(\arena', i)$;\\
    \If{$W^i_{\text{Adam}} \neq \emptyset$}{
    $V' \leftarrow V' \setminus W^i_{\text{Adam}}$\\
    $\arena' \leftarrow \arena' \downharpoonright V'$\tcc*{Restriction of $\arena'$ to $V'$}
    $LosingVertices \leftarrow \text{true}$\;
    }
  }
 }
 \Return $V'$
 \caption{Solver for multidimension lim-sup mean-payoff games}
 \label{12-algo:MMP}
\end{algorithm}

We wrap up with the following theorem.

````{prf:theorem} NEEDS TITLE 12-thm:MMPsup
:label: 12-thm:MMPsup

Solving multidimension lim-sup mean-payoff game is in $\NP \cap \coNP$. Infinite-memory strategies are required for Eve and memoryless ones suffice for Adam. Furthermore, the winning regions can be computed in pseudo-polynomial time, through at most $\vert V \vert \cdot k$ calls to an algorithm solving one-dimension mean-payoff games.

````


````{admonition} Proof
:class: dropdown tip

The correctness of {numref}`12-algo:MMP` follows from {prf:ref}`12-lem:MMP-Eve` and {prf:ref}`12-lem:MMP-Adam`, and its complexity is trivial to assess, using $\textsf{SolveOneDimMeanPayoff}$ as a pseudo-polynomial black-box. The memory bounds follow from {prf:ref}`12-lem:MMP-Eve`, {prf:ref}`12-lem:MMP-Adam` and {prf:ref}`12-thm:MMP-Eve`. Hence, only the $\NP \cap \coNP$ membership remains. Recall that the decision problem under study is: given an arena $\arena$ and an initial vertex $v_0$, does $v_0$ belong to $W_{\text{Eve}}$ or not?

We first prove that the problem is in $\NP$. A non-deterministic algorithm guesses the winning region $W_{\text{Eve}}$ containing $v_0$ and witness memoryless strategies $\sigma_i$ for all dimensions (we know that memoryless strategies suffice by {prf:ref}`4-thm:mean_payoff_positional`). Then, it checks for every dimension $i$, for every vertex $v \in W_{\text{Eve}}$, that $\sigma_i$ is winning. This boils down to solving a polynomial number of one-player one-dimension mean-payoff games for Adam over the arenas $\arena_{\sigma_i}$ obtained by fixing $\sigma_i$. As noted in~\cref{chap:payoffs}, \todo{I need a label for Subsect. 4.2.2} it can be done in polynomial time using Karp's algorithm for finding the minimum cycle mean in a weighted digraph {cite}`Karp:1978`. By {prf:ref}`12-lem:MMP-Eve`, we know that if the verification checks out, Eve has a winning strategy in $W_{\text{Eve}}$ for objective $\MeanPayoff^{+}_{\geq \vec{0}}$.

Finally, we prove $\coNP$ membership. The algorithm guesses a memoryless winning strategy $\tau$ for Adam (from $v_0$). The verification then consists in checking that Eve has no winning strategy in the arena $\arena_{\tau}$. This can be done using {numref}`12-algo:MMP`, through $\vert V \vert \cdot k$ calls to \textsf{SolveOneDimMeanPayoff}. In this case however, such calls only need to solve **one-player** one-dimension mean-payoff games for Eve, which again can be done in polynomial time, resorting to Karp's algorithm. Thus, the verification takes polynomial time in total, and $\coNP$ membership follows.

````


## Lim-inf variant
 For the sake of conciseness, we give only a brief sketch. Without loss of generality, we fix the objective $\MeanPayoff^{-}_{\geq \vec{0}}$. We know that infinite-memory strategies are needed for Eve by {prf:ref}`12-thm:MMP-Eve`. Again, things look better for Adam.

````{prf:lemma} NEEDS TITLE 12-lem:MPlimInfAdam
:label: 12-lem:MPlimInfAdam

Memoryless strategies suffice for Adam in multidimension lim-inf mean-payoff games.

````


````{admonition} Proof
:class: dropdown tip
[Sketch]
We mention the sketch as it is interesting in its own right. Recall that~\cref{chap:payoffs} presented a general recipe, due to Gimbert and Zielonka {cite}`Gimbert&Zielonka:2004,Gimbert&Zielonka:2005`, to prove memoryless determinacy. Clearly, such a recipe cannot work here due to {prf:ref}`12-thm:MMP-Eve`. Still, a similar result by Kopczynski deals with half-memoryless determinacy {cite}`Kopczynski:2006`. This new recipe states that if the objective of Eve is both **prefix independent** and **convex**, then memoryless strategies suffice for Adam. We already know that $\MeanPayoff^{-}_{\geq \vec{0}}$ is prefix independent. An objective is said to be convex if it is closed under combinations (shuffling): if two infinite sequences of colours $\play = \rho_1 \rho_2 \ldots{}$ and $\play' = \rho'_1 \rho'_2 \ldots{}$, with all $\rho_i$, $\rho'_i$ being finite prefixes, belong to the objective, then $\play'' = \rho_1 \rho'_1 \rho_2 \rho'_2 \ldots{}$ does too. Conjunctions of lim-inf mean-payoff are convex, hence the result applies here.

````


````{admonition} Remark 
Lim-sup mean-payoff objectives are **not** convex, hence the ad-hoc proof in {prf:ref}`12-lem:MMP-Adam`. Consider the integer sequence $\play = (2)^{5^0} (-4)^{5^1} (2)^{5^2} (-4)^{5^3}\ldots{}$ where the length of the $i$-th sequence of numbers if $5^{i-1}$. One can prove that at the end of each sequence of $2$'s (resp. $-4$'s), the mean is above (and tends to) $1$ (resp.~is exactly $-3$). Let $\play'$ be the sequence obtained by swapping all $2$'s and $-4$'s. We have $\MeanPayoff^{+}(\play) = \MeanPayoff^{+}(\play') \geq 1$, hence $\play, \play' \in \MeanPayoff^{+}_{\geq 0}$.

Still, by shuffling $\play$ and $\play'$ in one-one alternation, we build $\play'' = 2, -4, 2, -4 \ldots{}$, which is such that $\MeanPayoff^{+}(\play'') = -1$, hence  $\play'' \not\in \MeanPayoff^{+}_{\geq 0}$. Hence lim-sup mean-payoff is not convex.

````

Complexity-wise, multidimension lim-inf mean-payoff games look a lot like multidimension energy games, even though we proved they are not equivalent without memory restrictions.

````{prf:theorem} NEEDS TITLE AND LABEL 
Solving multidimension lim-inf mean-payoff games is $\coNP$-complete. Infinite-memory strategies are required for Eve and memoryless ones suffice for Adam.
 

Solving multidimension lim-inf mean-payoff games is $\coNP$-complete. Infinite-memory strategies are required for Eve and memoryless ones suffice for Adam.

````

We already discussed memory through {prf:ref}`12-ex:MMP2` and {prf:ref}`12-lem:MPlimInfAdam`. The $\coNP$-hardness can be shown through a reduction from \textsf{3UNSAT} similar to the one used for existential initial credit multidimension energy games in~\cref{12-exist-hard}. The matching upper bound relies on memoryless strategies being sufficient for Adam, and the capacity to solve one-player instances of multidimension lim-inf mean-payoff games in polynomial time. The latter problem is addressed by reduction to detecting non-negative multi-cycles in graphs (which can be done in polynomial time based on {cite}`Kosaraju&Sullivan:1988`).

## Wrap-up
 
We have seen that multidimension mean-payoff games and multidimension energy games behave relatively well. Sure, infinite memory is needed for Eve in general, but complexity-wise, the gap with one-dimension games is small and even non-existent for the lim-sup variant. Furthermore, if we are interested in finite-memory strategies, the equivalence with energy games is preserved. Hence, we may say that both mean-payoff and energy games hold up nicely in the multidimension world.
