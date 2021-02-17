(12-sec:total_payoff_shortest_path)=
# Total-payoff and shortest path

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
In this section, we turn to two other objectives deeply studied in~\cref{chap:payoffs}: we study total-payoff and shortest path games. We will see that the multidimension setting has dire consequences for both.

## Total-payoff vs.~mean-payoff

We start with total-payoff games. As for the mean-payoff, we explicitly consider the two variants, $\TotalPayoff^+$ and $\TotalPayoff^-$, for the lim-sup and lim-inf definitions respectively. While~\cref{chap:payoffs} was written using the lim-sup variant, all results are identical for the lim-inf one in one-dimension games {cite}`Gawlitza&Seidl:2009`.

Recall that one-dimension total-payoff games are memoryless determined and solving them is in $\NP \cap \coNP$ (even in $\UP \cap \coUP$ {cite}`Gawlitza&Seidl:2009`)\todo{Could be moved in~\cref{chap:payoffs}}. Furthermore, \cref{chap:payoffs} taught us that total-payoff can be seen as a **refinement** of mean-payoff, as it permits to reason about low (using the lim-inf variant) and high (using the lim-sup one) points of partial sums along a play when the mean-payoff is zero. We formalize this relationship in the next lemma, and study what happens in multiple dimensions. 

````{prf:lemma} NEEDS TITLE 12-lem:MPTP
:label: 12-lem:MPTP

Fix an arena $\arena$ and an initial vertex $v_0 \in \vertices$. Let A, B, C and D denote the following assertions.

1. [A.] Eve has a winning strategy for $\MeanPayoff^{+}_{\geq \vec{0}}$.

2. [B.] Eve has a winning strategy for $\MeanPayoff^{-}_{\geq \vec{0}}$.

3. [C.] There exists $\vec{x} \in \Q^{k}$ such that Eve has a winning strategy for $\TotalPayoff^{-}_{\geq \vec{x}}$.

4. [D.] There exists $\vec{x} \in \Q^{k}$ such that Eve has a winning strategy for $\TotalPayoff^{+}_{\geq \vec{x}}$.

In one-dimension games ($k = 1$), all four assertions are equivalent. In multidimension ones ($k > 1$), the only implications that hold are: $C \implies D \implies A$ and $C \implies B \implies A$. All other implications are false in general.

````

 {prf:ref}`12-lem:MPTP` is depicted in {numref}`12-fig:MPTP`: the only implications that carry over to multiple dimensions are depicted by solid arrows.

```{figure} ./../FigAndAlgos/12-fig:MPTP.png
:name: 12-fig:MPTP
:align: center
Equivalence between mean-payoff and total-payoff games. Dashed im\-pli\-ca\-tions are only valid in one-dimension games. We use $\sigma \models \Omega$ as a shortcut for $\sigma$ is winning from $v_0$ for $\Omega$.
```

````{admonition} Proof
:class: dropdown tip

The implications that remain true in multiple dimensions are the trivial ones. First, satisfaction of the lim-inf version of a given objective clearly implies satisfaction of its lim-sup version by definition. Hence, $B \implies A$ and $C \implies D$. Second, consider a play $\pi \in \TotalPayoff^{-}_{\geq \vec{x}}$ (resp. $\TotalPayoff^{+}_{\geq \vec{x}}$) for some $\vec{x} \in \Q^{k}$. For all dimension $i \in \{1, \ldots{}, k\}$, the corresponding sequence of mean-payoff infima (resp.~suprema) over prefixes can be **lower-bounded** by a sequence of elements of the form $\frac{\vec{x}_i}{\ell}$ with $\ell$ the length of the prefix. We can do this because the sequence of total-payoffs over prefixes is a sequence of integers: it always achieves the value of its limit $\vec{x}_i$ instead of only tending to it asymptotically as could a sequence of rationals (such as the mean-payoffs). Since $\frac{\vec{x}_i}{\ell}$ tends to zero over an infinite play, we do have that $\pi \in \MeanPayoff^{-}_{\geq \vec{x}}$ (resp. $\MeanPayoff^{+}_{\geq \vec{x}}$). Thus, $C \implies B$ and $D \implies A$. Along with the transitive closure $C \implies A$, these are all the implications preserved in multidimension games.

In one-dimension games, all assertions are equivalent. As seen before, we have that lim-inf and lim-sup mean-payoff games coincide as memoryless strategies suffice for both players. Thus, we add $A \implies B$, and $D \implies B$ by transitivity. Second, consider a memoryless (w.l.o.g.) strategy $\sigma_B$ for Eve for $\MeanPayoff^{-}_{\geq \vec{0}}$. Let $\play$ be any consistent play. Then all cycles in $\pi$ are non-negative, otherwise Eve cannot ensure winning with $\sigma_B$ (because Adam could pump the negative cycle). Thus, the sum of weights along $\play$ is at all times bounded from below by $-(\vert V\vert-1)\cdot W$ (for the longest acyclic prefix), with $W$ the largest absolute weight, as usual. Therefore, we have $B \implies C$, and we obtain all other implications by transitive closure.

For multidimension games, all dashed implications are false. We only need to consider two of them.

1. \label{12-lem:MPTP_proof1} To show that implication $D \implies B$ does not hold, consider the Eve-owned one-player game where $V = \{v\}$ and the only edges are two self loops of weights $(1, -2)$ and $(-2, 1)$. Clearly, any finite vector $\vec{x} \in \Q^{2}$ for $\TotalPayoff^{+}_{\geq \vec{x}}$ can be achieved by an infinite-memory strategy consisting in playing both loops successively for longer and longer periods, each time switching after getting back above threshold $\vec{x}$ in the considered dimension. However, it is impossible to build any strategy, even with infinite memory, that satisfies $\MeanPayoff^{-}_{\geq \vec{0}}$ as the lim-inf mean-payoff would be at best a linear combination of the two cycle values, i.e., strictly less than zero in at least one dimension in any case.

2.  Lastly, consider the game in {numref}`12-fig:MultiMP` where we modify the weights to add a third dimension with value $0$ on the self loops and $-1$ on the other edges. As already proved, the strategy that plays for $\ell$ steps in the left cycle, then goes for $\ell$ steps in the right one, then repeats for $\ell' > \ell$ and so on, is a winning strategy for $\MeanPayoff^{-}_{\geq \vec{0}}$. Nevertheless, for any strategy of Eve, the play is such that either (i) it only switches between $v_0$ and $v_1$ a finite number of times, in which case the sum in dimension $1$ or $2$ decreases to infinity from some point on; or (ii) it switches infinitely often and the sum in dimension $3$ decreases to infinity. In both cases, objective $\TotalPayoff^{+}_{\geq \vec{x}}$ is not satisfied for any finite vector $\vec{x} \in  \Q^{3}$. Hence, $B \implies D$ is falsified.

All other implications are deduced false as they would otherwise contradict the last two cases by transitivity.

````

We see that the relationship between mean-payoff and total-payoff games breaks in multiple dimensions. Nonetheless, one may still hope for good properties for the latter, as one-dimension total-payoff games are in $\NP \cap \coNP$ (\cref{chap:payoffs}). \todo{I need label for Subsect. 4.4.3.} This hope, however, will not last long.

## Undecidability

In contrast to mean-payoff games, total-payoff ones become undecidable in multiple dimensions.

````{prf:theorem} NEEDS TITLE 12-thm:TPundec
:label: 12-thm:TPundec

Total-payoff games are undecidable in any dimension $k \geq 5$.

````


````{admonition} Proof
:class: dropdown tip

We use a reduction from two-dimensional robot games {cite}`Niskanen&Potapov&Reichert:2016`, which were mentioned in~\cref{chap:counters}. They are a restricted case of configuration reachability vector games, recently proved to be already undecidable. They are expressible as follows: $\mathcal{V} = (\mathcal{L} = \{\ell_0, \ell_1\}, T, \mathcal{L}_{\text{Eve}} = \{\ell_0\}, \mathcal{L}_{\text{Adam}} = \{\ell_1\})$ and $T \subseteq \mathcal{L} \times [-M, M]^2\times \mathcal{L}$ for some $M \in \N$. The game starts in configuration $\ell_0(x_0, y_0)$ for some $x_0, y_0 \in \Z$ and the goal of Eve is to reach configuration $\ell_0(0, 0)$.

The reduction is as follows. Given a robot game $\mathcal{V}$, we build a five-dimension total-payoff game $\game$ such that Eve wins in $\game$ if and only if she wins in $\mathcal{V}$. Let $\game = (\arena, \TotalPayoff^{+}_{\geq \vec{0}})$ (we will discuss the lim-inf case later), where arena $\arena$ has vertices $V = V_{\text{Eve}} \uplus V_{\text{Adam}}$ with $V_{\text{Eve}} = \{v_{\text{init}}, v_0, v_{\text{stop}}\}$ and $V_{\text{Adam}} = \{v_1\}$, and $E$ is built as follows:

*  if $(\ell_i, (a,b), \ell_j) \in T$, then $(v_i, (a, -a, b, -b, 0), v_j) \in E$,
*  $(v_0, (0, 0, 0, 0, 1), v_{\text{stop}}) \in E$ and $(v_{\text{stop}}, (0, 0, 0, 0, 0), v_{\text{stop}}) \in E$,
*  $(v_{\text{init}}, (x_0, -x_0, y_0, -y_0, -1), v_0) \in E$ (where $(x_0, y_0)$ is the initial credit in $\mathcal{V}$).

The initial vertex is $v_{\text{init}}$. Intuitively, dimensions $1$ and $2$ (resp. $3$ and $4$) encode the value of the first counter (resp.~second counter) and its opposite at all times. The initial credit is encoded thanks to the initial edge, afterwards the game is played as in the vector game, with the exception that Eve may branch from $v_0$ to the absorbing vertex $v_{\text{stop}}$, which has a zero self loop. The role of the last dimension is to force Eve to branch eventually.

We proceed to prove the correctness of the reduction. First, let $\sigma_{\game}$ be a winning strategy of Eve in $\game$. We claim that Eve can also win in $\mathcal{V}$. Any play $\pi$ consistent with $\sigma_{\game}$ necessarily ends in $v_{\text{stop}}$: otherwise its lim-sup total-payoff on the last dimension would be $-1$ (as the sum always stays at $-1$). Due to the branching edge and the self loop having weight zero in all first four dimensions, we also have that the current sum on these dimensions must be non-negative when branching, otherwise the objective would be falsified. By construction of $\arena$, the only way to achieve this is to have a sum exactly equal to zero in all first four dimensions (as dimensions $1$ and $2$ are opposite at all times and so are $3$ and $4$). Finally, observe that obtaining a partial sum of $(0, 0, 0, 0, -1)$ in $v_0$ is equivalent to reaching configuration $\ell_0(0, 0)$ in $\mathcal{V}$. Hence, we can easily build a strategy $\sigma_{\mathcal{V}}$ in $\mathcal{V}$ that mimics $\sigma_{\game}$ in order to win the robot game. This strategy $\sigma_{\mathcal{V}}$ could in general use arbitrary memory (since we start with an arbitrary winning strategy $\sigma_{\game}$) while formally robot games as defined in {cite}`Niskanen&Potapov&Reichert:2016` only allow strategies to look at the current configuration. Still, from $\sigma_{\mathcal{V}}$, one can easily build a corresponding strategy that meets this restriction ($\mathcal{V}$ being a configuration reachability game, there is no reason to choose different actions in two visits of the same configuration). Hence, if Eve wins in $\game$, she also wins in $\mathcal{V}$.

For the other direction, from a winning strategy $\sigma_{\mathcal{V}}$ in $\mathcal{V}$, we can similarly define a strategy $\sigma_{\game}$ that mimics it in $\game$ to reach $v_0$ with partial sum $(0, 0, 0, 0, -1)$, and at that point, branches to $v_{\text{stop}}$. Such a strategy ensures reaching the absorbing vertex with a total-payoff of zero in all dimensions, hence is winning in $\game$.

Thus, the reduction holds for lim-sup total-payoff. Observe that the exact same reasoning holds for the lim-inf variant. Indeed, the last dimension is always $-1$ outside of $v_{\text{stop}}$, hence any play not entering $v_{\text{stop}}$ also has its lim-inf below zero in this dimension. Furthermore, once $v_{\text{stop}}$ is entered, the sum in all dimensions stays constant, hence the limit exists and both variants coincide.

````

An almost identical reduction can be used for **shortest path** games.

````{prf:theorem} NEEDS TITLE 12-thm:SPundec
:label: 12-thm:SPundec

Shortest path games are undecidable in any dimension $k \geq 4$.

````


````{admonition} Proof
:class: dropdown tip

The proof is almost identical to the last one. We use objective $\ShortestPath_{\leq \vec{0}}$ with target edge $(v_{\text{stop}}, (0, 0, 0, 0), v_{\text{stop}})$ and drop the last dimension in arena $\arena$: it is now unnecessary as the shortest path objective by definition will force Eve to branch to $v_{\text{stop}}$, as otherwise the value of the play would be infinite in all dimensions. The rest of the reasoning is the same as before.

````


````{admonition} Remark 
The decidability of total-payoff games with $k \in \{2, 3, 4\}$ dimensions and shortest path games with $k \in \{2, 3\}$ dimensions remains an open question. Furthermore, our undecidability results crucially rely on weights being in $\Z$: they do not hold when we restrict weights to $\N$. A similar situation will be presented in Section {ref}`12-sec:percentile`, in the context of percentile queries.\todo{Check if enough place to do it.}

````


### Memory
 Let us go back to the game used in  {prf:ref}`12-lem:MPTP_proof1` in the proof of {prf:ref}`12-lem:MPTP`: we have seen that for any threshold $\vec{x} \in \Q^{2}$, Eve has an infinite-memory winning strategy for $\TotalPayoff^{+}_{\geq \vec{x}}$. In other words, she can ensure an **arbitrarily high** total-payoff with infinite memory. Yet, it is easy to check that there exists no finite-memory strategy of Eve that can achieve a finite threshold vector in the very same game: alternating would still be needed, but the negative amount to compensate grows boundlessly with each alternation, thus no amount of finite memory can ensure to go above the threshold infinitely often. Hence, this simple game highlights a huge gap between finite and infinite memory: with finite memory, the total-payoff on at least one dimension is $-\infty$; with infinite memory, the total-payoff in both dimensions may be as high as Eve wants. This further highlights the untameable behaviour of multidimension total-payoff games.

### Wrap-up
 Multiple dimensions are a curse for total-payoff and shortest path games as both become undecidable. This is in stark contrast to mean-payoff and energy games, which remain tractable, as seen in Section {ref}`12-sec:mean_payoff_energy`. The bottom line is that most of the equivalences, relationships, and well-known behaviours of one-dimension games simply fall apart when lifting them to multiple dimensions.
