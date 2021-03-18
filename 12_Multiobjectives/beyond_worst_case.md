(12-sec:beyond_worst_case)=
# Beyond worst-case synthesis

```{math}

}}
}}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
% Generic probability measure, also prob. measure operator

\renewcommand{\Game}{\game}

```

We now turn to a completely different meaning of **multiobjective**. Let us take a few steps back. Throughout this book, we have studied two types of interaction between players: rational, antagonistic interaction between Eve and Adam; and stochastic interaction with a random player. Consider the quantitative settings of \cref{chap:payoffs} and \cref{chap:mdp}. In the zero-sum two-player games of the former, Adam is seen as a **purely antagonistic adversary**, so the goal of Eve is to ensure strict worst-case guarantees, i.e., a minimal performance level against all possible strategies of Adam. In the MDPs of the latter, Eve interacts with randomness (through actions or random vertices) and she wants to ensure a good **expected value** for the considered payoff.

For most objectives, these two paradigms yield elegant and simple solutions: e.g., memoryless strategies suffice for both games and MDPs with a mean-payoff objective. Nevertheless, the corresponding strategies have clear weaknesses: strategies that are good for the worst-case may exhibit suboptimal behaviours in probable situations while strategies that are good for the expected value may be terrible in some unlikely but possible situations. A natural question, of theoretical and practical interest, is to build -- **synthesize** -- strategies that combine both paradigms: strategies that both ensure (a) some worst-case threshold no matter how the adversary behaves (i.e., against any arbitrary strategy) and (b) a good expectation against the expected behaviour of the adversary (given as a stochastic model). We call this task beyond worst-case synthesis.

The goal of this section is to illustrate the complexity of beyond worst-case synthesis and how it requires fine-tuned interaction between the worst-case and average-case aspects. To that end, we focus on a specific case: the synthesis of **finite-memory strategies** for beyond worst-case **mean-payoff** objectives. Due to the highly technical nature of this approach, we will not present all its details, but rather paint in broad strokes its cornerstones. We hope to give the reader sufficient intuition and understanding to develop a clear view of the challenges arising from rich behavioural models, and some of the techniques that come to the rescue.

## The decision problem

Our goal is to mix the games of \cref{chap:payoffs} and the MDPs of \cref{chap:mdp}, so we need to go back and forth between these models.

> **Two-player game**

 As before, we start with an arena $\mathcal{A} = (G = (V, E), V_{\text{Eve}}, V_{\text{Adam}})$, where the vertices are split between Eve's and Adam's. This arena represents the antagonistic interaction between Eve and Adam, so we consider a worst-case constraint on the corresponding game. We study a single mean-payoff function, so our colouring is $c\colon E \to  \mathbb{Z}$. Let $\alpha \in  \mathbb{Q}$ be the worst-case threshold: we are looking for a strategy of Eve that is winning for objective $\mathtt{MeanPayoff}^{-}_{> \alpha}$. Two things to note: first, we consider the lim-inf variant w.l.o.g. as we focus on **finite-memory** strategies (recall  {prf:ref}`12-prop:MPSI`); second, we use a strict inequality as it will ease the formulation of the upcoming results.

> **MDP**

 To make the connection with MDPs, we fix a finite-memory randomized strategy for Adam in the arena $\mathcal{A}$, $\tau^\text{stoch}$. Recall that a randomized strategy \todo{It seems this is never addressed properly before but used in MDPs, stochastic games, etc: to sort out before its first use.} is a function $E^* \to \mathcal{D}(E)$. As usual, we may build $\mathcal{A}_{\tau^\text{stoch}}$, the product of the arena $\mathcal{A}$ with the memory structure of $\tau^\text{stoch}$, restricted to the choices made by $\tau^\text{stoch}$. Since $\tau^\text{stoch}$ is assumed to be stochastic, what we obtain is not a one-player game for Eve, but an MDP.

To understand this relationship, it is easier to consider the alternative -- and equivalent -- formalism of MDPs, based on random vertices (as used for stochastic games in \cref{chap:stochastic}). Assume for instance that $\tau^\text{stoch}$ is a randomized memoryless strategy, i.e., a function $V_{ \textrm{Adam}} \to \mathcal{D}(E)$. Then, the MDP $\mathcal{A}_{\tau^\text{stoch}}$ is immediately obtained by replacing each Adam's vertex $v$ by a random vertex such that $\delta(v) = \tau^\text{stoch}(v)$, i.e., the probabilistic transition function uses the same probability distributions as Adam's strategy. Formally, we build the MDP $\mathcal{P} =  \mathcal{A}_{\tau^{\text{stoch}}} = (G, V_{\text{Eve}}, V_{\text{Rand}} = V_{\text{Adam}}, \delta = \tau^{\text{stoch}})$.

In contrast to \cref{chap:stochastic}, we explicitly allow the transition function to assign probability zero to some edges of the underlying graph $G$, i.e., the support of $\delta(v)$ in some vertex $v \in V_{\text{Rand}}$ might not include all edges $e \in E$ such that $\textrm{In}(e) = v$.
This is important as far as modelling is concerned, as in our context, transition functions will be defined according to a stochastic model for Adam, and we cannot reasonably assume that such a model always involves all the possible actions of Adam. Consequently, given the MDP $\ensuremath{{\mathcal{P}$, we define the subset of edges $\ensuremath{E_{\delta} = \{ e \in E \mid  \textrm{In}(e) \in V_{\text{Rand}} \implies \delta( \textrm{In}(e))(e) > 0\}$, representing all edges that either start in a vertex of Eve, or are chosen with non-zero probability by the transition function $\delta$. Edges in $E\setminus  \ensuremath{E_{\delta}$ will only matter in the two-player game interpretation, whereas all MDP-related concepts, such as end-components, are defined with regard to edges in $\ensuremath{E_{\delta}$ exclusively.

> **Beyond worst-case problem**

 Let us sum up the situation: we have a two-player arena $\mathcal{A}$ with a mean-payoff objective $\mathtt{MeanPayoff}^{-}_{> \alpha}$ and a finite-memory stochastic model for Adam yielding the MDP $\mathcal{A}_{\tau^\text{stoch}}$. Now, let $\beta \in  \mathbb{Q}$ be the expected value threshold we want to ensure in the MDP (i.e., on average against the stochastic model of Adam).

```{admonition} Problem

Our beyond worst-case (BWC) problem is as follows.

**INPUT**: An arena $\mathcal{A}$, a finite-memory stochastic model $\tau^\text{stoch}$, an\\ & initial vertex $v_0$, two thresholds $\alpha, \beta \in  \mathbb{Q}$\\

**QUESTION**: Does Eve have a **finite-memory** strategy $\sigma$ such that $\sigma$ is \\ & winning for objective $\mathtt{MeanPayoff}^{-}_{> \alpha} \text{ from } v_0 \text{ in }  \mathcal{A}$\\ &
and $\mathbf{E}^{\sigma}_{ \mathcal{A}_{\tau^\text{stoch}},v_0}[ \mathtt{MeanPayoff}^{-}] > \beta$?

```

We assume $\beta > \alpha$, otherwise the problem trivially reduces to the classical worst-case analysis: if all plays consistent with $\sigma$ have mean-payoff greater than $\alpha \geq \beta$ then the expected value is also greater than $\alpha$ regardless of the stochastic model.

## The approach in a nutshell

We present our solution to the BWC problem in {numref}`12-algo:BWC`. We give an intuitive sketch of its functioning in the following, and illustrate it on a toy example. 

DO SOMETHING WITH THIS ALGORITHM IT DOES NOT COMPILE!!!

## Inputs and outputs
 The algorithm takes as input: an arena $\mathcal{A}^{i}$, a finite-memory stochastic model of Adam $\tau^{i}$, a worst-case threshold $\alpha^{i}$, an expected value threshold $\beta^{i}$, and an initial vertex $v_0^{i}$. Its output is $Yes$ if and only if there exists a finite-memory strategy of Eve satisfying the BWC problem.

The output as described in {numref}`12-algo:BWC` is Boolean: the algorithm answers whether a satisfying strategy exists or not, but does not explicitly construct it (to avoid tedious formalization within the pseudocode). Nevertheless, we sketch the synthesis process in the following and we highlight the role of each step of the algorithm in the construction of a winning strategy, as producing a witness winning strategy is a straightforward by-product of the process we apply to decide satisfaction of the BWC problem.

## Preprocessing
 The first part of the algorithm is dedicated to the preprocessing of the arena $\mathcal{A}^{i}$ and the stochatic model $\tau^{i}$ given as inputs in order to apply the second part of the algorithm on a modified arena $\mathcal{A}$ and stochastic model $\tau^{\text{stoch}}$, simpler to manipulate. We show in the following that the answer to the BWC problem on the modified arena is $Yes$ if and only if it is also $Yes$ on the input arena, and we present how a winning strategy of Eve in $\mathcal{A}$ can be transferred to a winning strategy in $\mathcal{A}^{i}$.

The preprocessing is composed of four main steps. First, we modify the colouring function $c^i$ in order to consider the equivalent BWC problem with thresholds $(0,\, \beta)$ instead of $(\alpha^{i},\, \beta^{i})$. This classical trick is used to get rid of explicitly considering the worst-case threshold in the following, as it is equal to zero.

Second, observe that any strategy that is winning for the BWC problem must also be winning for the classical **worst-case problem**, as solved in the two-player games of \cref{chap:payoffs}. Such a strategy cannot allow visits of any vertex from which Eve cannot ensure winning against an antagonistic adversary because mean-payoff is a prefix independent objective (hence it is not possible to win it over the finite prefix up to such a vertex). Thus, we reduce our study to $\mathcal{A}^{w}$, the subarena induced by Eve's worst-case winning vertices -- which we compute in pseudo-poly\-nomial time thanks to $\textsf{SolveWorstCaseMeanPayoff}( \mathcal{A}, c)$ (implementing the algorithm of \cref{chap:payoffs}). \todo{I need a label on Subsect. 4.3.4 to cite it precisely.}  Note that we use the modified colouring and that $\mathcal{A}^{w}$ is a proper arena (same argument as \cref{12-rmk:properArena}). Obviously, if from the initial vertex $v_0^{i}$, Eve cannot win the worst-case problem, then the answer to the BWC problem is No.

Third, we build arena $\mathcal{A}$, the product of $\mathcal{A}^{w}$ and the memory structure of Adam's stochastic model $\tau^i$. Intuitively, we expand the initial arena by integrating the memory elements in the graph. Note that this does not modify the power of Adam in the two-player interpretation of the arena.

Fourth, the finite-memory stochastic model $\tau^{i}$ on $\mathcal{A}^{i}$ clearly translates to a memoryless stochastic model $\tau^{\text{stoch}}$ on $\mathcal{A}$. This will help us obtain elegant proofs for the second part of the algorithm.

````{prf:example} NEEDS TITLE AND LABEL 

```{figure} ./../FigAndAlgos/12-fig:bwcRunningExample.png
:name: 12-fig:bwcRunningExample
:align: center
Beyond worst-case mean-payoff problem: $\ensuremath{U_{2}$ and $\ensuremath{U_{3}$ are maximal winning ECs, $\ensuremath{U_{1}$ is losing.
```

In order to illustrate several notions and strategies, we will consider the arena depicted in {numref}`12-fig:bwcRunningExample` throughout our presentation. The stochastic model of $\text{Adam$ is memoryless and is described by the probabilities written close to the start of outgoing edges. The colouring (weights) is written besides them.

We consider the $\text{BWC}$ problem with the worst-case threshold $\ensuremath{\alpha = 0$. Observe that this arena satisfies the assumptions guaranteed at the end of the preprocessing part of the algorithm. That is, the worst-case threshold is zero, a worst-case winning strategy of $\text{Eve$ exists in all vertices (e.g., the memoryless strategy choosing edges $( \ensuremath{v_{1},  \ensuremath{v_{9})$, $( \ensuremath{v_{3},  \ensuremath{v_{5})$, $( \ensuremath{v_{6},  \ensuremath{v_{9})$, $( \ensuremath{v_{9},  \ensuremath{v_{10})$ and $( \ensuremath{v_{10},  \ensuremath{v_{9})$ in their respective starting vertices), and the stochastic model is memoryless, as explained above.

```{figure} ./../FigAndAlgos/12-fig:bwcRunningExample.png
:name: 12-fig:bwcRunningExample
:align: center
Beyond worst-case mean-payoff problem: $\ensuremath{U_{2}$ and $\ensuremath{U_{3}$ are maximal winning ECs, $\ensuremath{U_{1}$ is losing.
```

In order to illustrate several notions and strategies, we will consider the arena depicted in {numref}`12-fig:bwcRunningExample` throughout our presentation. The stochastic model of $\text{Adam$ is memoryless and is described by the probabilities written close to the start of outgoing edges. The colouring (weights) is written besides them.

We consider the $\text{BWC}$ problem with the worst-case threshold $\ensuremath{\alpha = 0$. Observe that this arena satisfies the assumptions guaranteed at the end of the preprocessing part of the algorithm. That is, the worst-case threshold is zero, a worst-case winning strategy of $\text{Eve$ exists in all vertices (e.g., the memoryless strategy choosing edges $( \ensuremath{v_{1},  \ensuremath{v_{9})$, $( \ensuremath{v_{3},  \ensuremath{v_{5})$, $( \ensuremath{v_{6},  \ensuremath{v_{9})$, $( \ensuremath{v_{9},  \ensuremath{v_{10})$ and $( \ensuremath{v_{10},  \ensuremath{v_{9})$ in their respective starting vertices), and the stochastic model is memoryless, as explained above.

````

## Analysis of end-components
 The second part hence operates on an arena $\mathcal{A}$ such that from all vertices, Eve has a strategy to achieve a strictly positive mean-payoff value (recall that $\alpha = 0$). We consider the MDP $\ensuremath{{\mathcal{P} =  \mathcal{A}_{ \ensuremath{\tau^{\text{stoch}}$ and notice that the underlying graphs of $\mathcal{A}$ and $\ensuremath{{\mathcal{P}$ are the same thanks to $\ensuremath{\tau^{\text{stoch}$ being memoryless. The following steps rely on the analysis of **end-components** (ECs) in the MDP, i.e., strongly connected subgraphs in which Eve can ensure to stay when playing against Adam's stochastic model ( {prf:ref}`5-def:ec`).

The motivation to the analysis of ECs is the following. It is well-known that under any arbitrary strategy $\sigma$ of Eve in $\ensuremath{{\mathcal{P}$, the probability that vertices visited infinitely often along a play constitute an EC is one ( {prf:ref}`5-lem:EC-inf`). Recall that the mean-payoff is prefix independent, therefore the value of any play only depends on those colors that are seen infinitely often. Hence, the expected mean-payoff $\mathbf{E}^{\sigma}_{ \ensuremath{{\mathcal{P},v_0}[ \mathtt{MeanPayoff}^{-}]$ depends **uniquely** on the value obtained in the ECs. Inside an EC, we can compute the maximal expected value that can be achieved by Eve, and this value is the same in all vertices of the EC, as established in  {prf:ref}`5-thm:mp-valcomp`.

Consequently, in order to satisfy the expected value requirement, an acceptable strategy for the $\text{BWC}$ problem has to favor reaching ECs with a sufficient expectation, but under the constraint that it should also ensure satisfaction of the worst-case requirement. As we show in the following, this constraint implies that some ECs with high expected values may still need to be avoided because they do not permit to guarantee the worst-case requirement. This is the cornerstone of the classification of ECs that follows.

## Classification of end-components
 Let $\ensuremath{\mathcal{E} \subseteq 2^{V}$ denote the set of all ECs in $\ensuremath{{\mathcal{P}$. Notice that by definition, only edges in $\ensuremath{E_{\delta}$, as defined earlier, are involved to determine which sets of vertices form an EC in $\ensuremath{{\mathcal{P}$. As such, for any EC $\ensuremath{U \in  \ensuremath{\mathcal{E}$, there may exist edges from $\ensuremath{E \setminus  \ensuremath{E_{\delta}$ starting in $\ensuremath{U$, such that Adam can force leaving $\ensuremath{U$ when using an arbitrary strategy in $\mathcal{A}$. Still these edges will never be used by the stochastic model $\ensuremath{\tau^{\text{stoch}$. This remark will be important to the definition of strategies of Eve that guarantee the worst-case requirement, as Eve needs to be able to react to the hypothetical use of such an edge. We will see that it is also the case **inside** an EC.

Now, we want to consider the ECs in which $\text{Eve$ can ensure that the worst-case requirement will be fulfilled (i.e., without having to leave the EC): we call them **winning** ECs (WECs). The others will need to be eventually avoided, hence will have zero impact on the expectation of a finite-memory strategy satisfying the $\text{BWC}$ problem. So we call the latter **losing** ECs (LECs). The subtlety of this classification is that it involves considering the ECs both in the MDP $\ensuremath{{\mathcal{P}$, and in the arena $\mathcal{A}$.

Formally, let $\ensuremath{U \in  \ensuremath{\mathcal{E}$ be an EC. It is **winning** if, in the subarena induced by $\ensuremath{U$, from all vertices, $\text{Eve$ has a strategy to ensure a **strictly** positive mean-payoff against any strategy of $\text{Adam$ **that only chooses edges which are assigned non-zero probability by $\ensuremath{\tau^{\text{stoch}$**, or equivalently, edges in $\ensuremath{E_{\delta}$. This can be interpreted as looking at arena $\ensuremath{ \mathcal{A}_{\delta}$, which is the restriction of $\mathcal{A}$ to edges in $\ensuremath{E_{\delta}$.

We denote $\ensuremath{\mathcal{W} \subseteq  \ensuremath{\mathcal{E}$ the set of such ECs. Non-winning ECs are **losing**: in those, whatever the strategy of $\text{Eve$ played against the stochastic model $\ensuremath{\tau^{\text{stoch}$ (or any strategy with the same support), there exists at least one play for which the mean-payoff is not strictly positive (even if its probability is zero, its mere existence is not acceptable for the worst-case requirement).

```{figure} ./../FigAndAlgos/12-fig:bwcWinningECsComputationExample.png
:name: 12-fig:bwcWinningECsComputationExample
:align: center
EC $\ensuremath{U_{2}$ is losing. The set of MWECs is $\ensuremath{\mathcal{U}_{w} =  \ensuremath{\mathcal{W} = \{ \ensuremath{U_{1},  \ensuremath{U_{3}\}$.
```

````{prf:example} NEEDS TITLE AND LABEL 
Note that an EC is winning if $\text{Eve$ has a worst-case winning strategy from **all** vertices. This point is important as it may well be the case that winning strategies exist in a strict subset of vertices of the EC. This does not contradict the definition of ECs as strongly connected subgraphs, as the latter only guarantees that every vertex can be reached **with probability one**, and not necessarily **surely**. Hence one cannot call upon the prefix independence of the mean-payoff to extend the existence of a winning strategy to all vertices.

Such a situation can be observed on the arena of {numref}`12-fig:bwcWinningECsComputationExample`, where the EC $\ensuremath{U_{2}$ is losing (because from $\ensuremath{v_{1}$, the play $( \ensuremath{v_{1} \ensuremath{v_{3} \ensuremath{v_{4})^{\omega}$ can be forced by $\text{Adam$, yielding mean-payoff $-1/3 \leq 0$), while its sub-EC $\ensuremath{U_{3}$ is winning. From $\ensuremath{v_{1}$, $\text{Eve$ can ensure to reach $\ensuremath{U_{3}$ almost-surely, but not surely, which is critical in this case.

Note that an EC is winning if $\text{Eve$ has a worst-case winning strategy from **all** vertices. This point is important as it may well be the case that winning strategies exist in a strict subset of vertices of the EC. This does not contradict the definition of ECs as strongly connected subgraphs, as the latter only guarantees that every vertex can be reached **with probability one**, and not necessarily **surely**. Hence one cannot call upon the prefix independence of the mean-payoff to extend the existence of a winning strategy to all vertices.

Such a situation can be observed on the arena of {numref}`12-fig:bwcWinningECsComputationExample`, where the EC $\ensuremath{U_{2}$ is losing (because from $\ensuremath{v_{1}$, the play $( \ensuremath{v_{1} \ensuremath{v_{3} \ensuremath{v_{4})^{\omega}$ can be forced by $\text{Adam$, yielding mean-payoff $-1/3 \leq 0$), while its sub-EC $\ensuremath{U_{3}$ is winning. From $\ensuremath{v_{1}$, $\text{Eve$ can ensure to reach $\ensuremath{U_{3}$ almost-surely, but not surely, which is critical in this case.

````

## Maximal winning end-components
 Based on these definitions, observe that {numref}`12-algo:BWC` does not actually compute the set $\ensuremath{\mathcal{W}$ containing all WECs, but rather the set $\ensuremath{\mathcal{U}_{w} \subseteq  \ensuremath{\mathcal{W}$, defined as $\ensuremath{\mathcal{U}_{w} = \{ \ensuremath{U \in  \ensuremath{\mathcal{W} \mid \forall\,  \ensuremath{U' \in  \ensuremath{\mathcal{W},\,  \ensuremath{U \subseteq  \ensuremath{U' \Rightarrow  \ensuremath{U =  \ensuremath{U'\}$, i.e., the set of **maximal** WECs (MWECs).

The intuition on **why we can** restrict our study to this subset is as follows. If an EC $\ensuremath{U_{1} \in  \ensuremath{\mathcal{W}$ is included in another EC $\ensuremath{U_{2} \in  \ensuremath{\mathcal{W}$, i.e., $\ensuremath{U_{1} \subseteq  \ensuremath{U_{2}$, we have that the maximal expected value achievable in $\ensuremath{U_{2}$ is at least equal to the one achievable in $\ensuremath{U_{1}$. Indeed, $\text{Eve$ can reach $\ensuremath{U_{1}$ with probability one (by virtue of $\ensuremath{U_{2}$ being an EC and $\ensuremath{U_{1} \subseteq  \ensuremath{U_{2}$) and stay in it forever with probability one (by virtue of $\ensuremath{U_{1}$ being an EC): hence the expectation of such a strategy would be equal to what can be obtained in $\ensuremath{U_{1}$ thanks to the prefix independence of the mean-payoff. This property implies that it is sufficient to consider MWECs in our computations.

As for **why we do it**, observe that the complexity gain is critical. The number of WECs can be as large as $\vert \ensuremath{\mathcal{W}\vert \leq \vert \ensuremath{\mathcal{E}\vert \leq 2^{\vert V\vert}$, that is, exponential in the size of the input. Yet, the number of MWECs is bounded by $\vert \ensuremath{\mathcal{U}_{w}\vert \leq \vert V\vert$ as they are disjoint by definition: for any two WECs with a non-empty intersection, their union also constitutes an EC, and is still winning because $\text{Eve$ can essentially stick to the EC of her choice.

The computation of the set $\ensuremath{\mathcal{U}_{w}$ is executed by a recursive subalgorithm calling polynomially-many times an oracle solving the worst-case problem (e.g., following the pseudo-polynomial-time algorithm of \cref{chap:payoffs}). \todo{I need a label on Subsect. 4.3.4 to cite it precisely.} Roughly sketched, this algorithm computes the maximal EC decomposition of an MDP (in polynomial time by  {prf:ref}`5-thm:MEC-decomposition-complexity`), then checks for each EC $\ensuremath{U$ in the decomposition (their number is polynomial) if $\ensuremath{U$ is winning or not, which requires a call to an oracle solving the worst-case threshold problem on the corresponding subgame. If $\ensuremath{U$ is losing, it may still be the case that a sub-EC $\ensuremath{U' \subsetneq  \ensuremath{U$ is winning. Therefore we recurse on the MDP reduced to $\ensuremath{U$, where vertices from which $\text{Adam$ can win in $\ensuremath{U$ have been removed (they are a no-go for $\text{Eve$). Hence the stack of calls is also at most polynomial.

````{prf:lemma} NEEDS TITLE 12-lem:MWEC
:label: 12-lem:MWEC

The set $\ensuremath{\mathcal{U}_{w}$ of MWECs can be computed in pseudo-polynomial time, and deciding if a set of vertices $U \subseteq V$ belongs to $\ensuremath{\mathcal{U}_{w}$ is in $\textrm{NP} \cap  \textrm{coNP}$.

````

The complexity follows from  {prf:ref}`4-thm:MP-NPcoNP` and $\P^{ \textrm{NP} \cap  \textrm{coNP}} =  \textrm{NP} \cap  \textrm{coNP}$ {cite}`Brassard:1979`.

````{prf:example} NEEDS TITLE AND LABEL 
Consider the running example in {numref}`12-fig:bwcRunningExample`. Note that vertices $\ensuremath{v_{1}$, $\ensuremath{v_{2}$ and $\ensuremath{v_{5}$ do not belong to any EC: given any strategy of $\text{Eve$ in $\ensuremath{{\mathcal{P}$, with probability one, any consistent play will only visit these vertices a finite number of times ( {prf:ref}`5-lem:EC-inf`). The set of **MWECs** is $\ensuremath{\mathcal{U}_{w} = \{ \ensuremath{U_{2},  \ensuremath{U_{3}\}$. Obviously, these ECs are disjoint. The set of WECs is larger, $\ensuremath{\mathcal{W} =  \ensuremath{\mathcal{U}_{w} \cup \{\{ \ensuremath{v_{9},  \ensuremath{v_{10}\}, \{ \ensuremath{v_{6},  \ensuremath{v_{7}\}\}$.

End-component $\ensuremath{U_{1}$ is **losing**: in the subarena $\ensuremath{ \mathcal{A}_{\delta}  \ensuremath{\downharpoonright  \ensuremath{U_{1}$, Adam's strategy consisting in always picking the $-1$ edge guarantees a negative mean-payoff. Note that this edge is present in $\ensuremath{E_{\delta}$ as it is assigned probability $1/2$ by the stochastic model $\ensuremath{\tau^{\text{stoch}$. Here, we witness why it is important to base our definition of WECs on $\ensuremath{ \mathcal{A}_{\delta}$ rather than $\mathcal{A}$. Indeed, in $\mathcal{A}  \ensuremath{\downharpoonright  \ensuremath{U_{2}$, it is also possible for $\text{Adam$ to guarantee a negative mean-payoff by always choosing edges with weight $-1$. However, to achieve this, $\text{Adam$ has to pick edges that are **not** in $\ensuremath{E_{\delta}$: this will never happen against the stochastic model and as such, this can be watched by $\text{Eve$ to see if $\text{Adam$ uses an arbitrary antagonistic strategy, and dealt with. If $\text{Adam$ conforms to $\ensuremath{E_{\delta}$, i.e., if he plays in $\ensuremath{ \mathcal{A}_{\delta}$, he has to pick the edge of weight $1$ in $\ensuremath{v_{7}$ and $\text{Eve$ has a worst-case winning strategy consisting in always choosing to go in $\ensuremath{v_{7}$. This EC is thus classified as **winning**. Note that for $\ensuremath{U_{3}$, in both subarenas $\mathcal{A}  \ensuremath{\downharpoonright  \ensuremath{U_{3}$ and $\ensuremath{ \mathcal{A}_{\delta}  \ensuremath{\downharpoonright  \ensuremath{U_{3}$, $\text{Eve$ can guarantee a strictly positive mean-payoff by playing $( \ensuremath{v_{9}\, \ensuremath{v_{10})^\omega$: even **arbitrary** strategies of $\text{Adam$ cannot endanger $\text{Eve$ in this case.

Lastly, consider the arena depicted in {numref}`12-fig:bwcWinningECsComputationExample`. While $\ensuremath{U_{2}$ is a strict superset of $\ensuremath{U_{3}$, the former is losing whereas the latter is winning, as explained above. Hence, the set $\ensuremath{\mathcal{U}_{w}$ is equal to $\{ \ensuremath{U_{1},  \ensuremath{U_{3}\}$.

Consider the running example in {numref}`12-fig:bwcRunningExample`. Note that vertices $\ensuremath{v_{1}$, $\ensuremath{v_{2}$ and $\ensuremath{v_{5}$ do not belong to any EC: given any strategy of $\text{Eve$ in $\ensuremath{{\mathcal{P}$, with probability one, any consistent play will only visit these vertices a finite number of times ( {prf:ref}`5-lem:EC-inf`). The set of **MWECs** is $\ensuremath{\mathcal{U}_{w} = \{ \ensuremath{U_{2},  \ensuremath{U_{3}\}$. Obviously, these ECs are disjoint. The set of WECs is larger, $\ensuremath{\mathcal{W} =  \ensuremath{\mathcal{U}_{w} \cup \{\{ \ensuremath{v_{9},  \ensuremath{v_{10}\}, \{ \ensuremath{v_{6},  \ensuremath{v_{7}\}\}$.

End-component $\ensuremath{U_{1}$ is **losing**: in the subarena $\ensuremath{ \mathcal{A}_{\delta}  \ensuremath{\downharpoonright  \ensuremath{U_{1}$, Adam's strategy consisting in always picking the $-1$ edge guarantees a negative mean-payoff. Note that this edge is present in $\ensuremath{E_{\delta}$ as it is assigned probability $1/2$ by the stochastic model $\ensuremath{\tau^{\text{stoch}$. Here, we witness why it is important to base our definition of WECs on $\ensuremath{ \mathcal{A}_{\delta}$ rather than $\mathcal{A}$. Indeed, in $\mathcal{A}  \ensuremath{\downharpoonright  \ensuremath{U_{2}$, it is also possible for $\text{Adam$ to guarantee a negative mean-payoff by always choosing edges with weight $-1$. However, to achieve this, $\text{Adam$ has to pick edges that are **not** in $\ensuremath{E_{\delta}$: this will never happen against the stochastic model and as such, this can be watched by $\text{Eve$ to see if $\text{Adam$ uses an arbitrary antagonistic strategy, and dealt with. If $\text{Adam$ conforms to $\ensuremath{E_{\delta}$, i.e., if he plays in $\ensuremath{ \mathcal{A}_{\delta}$, he has to pick the edge of weight $1$ in $\ensuremath{v_{7}$ and $\text{Eve$ has a worst-case winning strategy consisting in always choosing to go in $\ensuremath{v_{7}$. This EC is thus classified as **winning**. Note that for $\ensuremath{U_{3}$, in both subarenas $\mathcal{A}  \ensuremath{\downharpoonright  \ensuremath{U_{3}$ and $\ensuremath{ \mathcal{A}_{\delta}  \ensuremath{\downharpoonright  \ensuremath{U_{3}$, $\text{Eve$ can guarantee a strictly positive mean-payoff by playing $( \ensuremath{v_{9}\, \ensuremath{v_{10})^\omega$: even **arbitrary** strategies of $\text{Adam$ cannot endanger $\text{Eve$ in this case.

Lastly, consider the arena depicted in {numref}`12-fig:bwcWinningECsComputationExample`. While $\ensuremath{U_{2}$ is a strict superset of $\ensuremath{U_{3}$, the former is losing whereas the latter is winning, as explained above. Hence, the set $\ensuremath{\mathcal{U}_{w}$ is equal to $\{ \ensuremath{U_{1},  \ensuremath{U_{3}\}$.

````

## Ensure reaching winning end-components
 As discussed, under any arbitrary strategy of $\text{Eve$, vertices visited infinitely often form an EC with probability one ( {prf:ref}`5-lem:EC-inf`). Now, if we take a **finite-memory** strategy that **satisfies** the $\text{BWC}$ problem, we can refine this result and state that they form a **winning** EC with probability one. Equivalently, let $\ensuremath{{\sf Inf}( \pi)$ denote the set of vertices visited infinitely often along a play $\pi$: we have that the probability that a play $\pi$ is such that $\ensuremath{{\sf Inf}( \pi) =  \ensuremath{U$ for some $\ensuremath{U \in  \ensuremath{\mathcal{E} \setminus  \ensuremath{\mathcal{W}$ is zero. The equality is crucial. It may be the case, with non-zero probability, that $\ensuremath{{\sf Inf}( \pi) =  \ensuremath{U' \subsetneq  \ensuremath{U$, for some $\ensuremath{U' \in  \ensuremath{\mathcal{W}$, and $\ensuremath{U \in  \ensuremath{\mathcal{E} \setminus  \ensuremath{\mathcal{W}$ (hence the recursive algorithm to compute $\ensuremath{\mathcal{U}_{w}$). It is clear that $\text{Eve$ should not visit all the vertices of a LEC forever, as then she would not be able to guarantee the worst-case threshold inside the corresponding subarena.

````{prf:lemma} NEEDS TITLE AND LABEL 
\label{12-lem:

```{margin}
This is no longer true if Eve may use infinite memory: there may still be some incentive to stay in a LEC. But this goes beyond the scope of our overview.
```

EC-inf}
For any initial vertex $ v_0 $ and finite-memory strategy $ \sigma $ that satisfies the BWC problem, it holds that $  \mathbb{P}^\sigma_{ \ensuremath{{\mathcal{P}, v_0} ( \{ \pi \mid  \ensuremath{{\sf Inf}( \pi) \in  \ensuremath{\mathcal{W} \}) = 1 $.

\label{12-lem:

```{margin}
This is no longer true if Eve may use infinite memory: there may still be some incentive to stay in a LEC. But this goes beyond the scope of our overview.
```

EC-inf}
For any initial vertex $ v_0 $ and finite-memory strategy $ \sigma $ that satisfies the BWC problem, it holds that $  \mathbb{P}^\sigma_{ \ensuremath{{\mathcal{P}, v_0} ( \{ \pi \mid  \ensuremath{{\sf Inf}( \pi) \in  \ensuremath{\mathcal{W} \}) = 1 $. 

````

We denote $\ensuremath{V_{{\sf neg}} = V \setminus \bigcup_{ \ensuremath{U \in  \ensuremath{\mathcal{U}_{w}}  \ensuremath{U$ the set of vertices that, with probability one, are only seen a finite number of times when a $\text{BWC}$ satisfying strategy is played, and call them **negligible** vertices.

Our ultimate goal here is to modify the colouring of $\ensuremath{{\mathcal{P}$ from $c$ to $c'$, such that a classical optimal strategy for the expected value problem ( {prf:ref}`5-thm:general-mp-main`) using this new colouring $c'$ will naturally avoid LECs and prescribe which WECs are the most interesting to reach for a $\text{BWC}$ strategy on the initial arena $\mathcal{A}$ and MDP $\ensuremath{{\mathcal{P}$ with colouring $c$. For the sake of readability, let us simply use $\ensuremath{{\mathcal{P}$ and $\ensuremath{{\mathcal{P}'$ to refer to MDP $\ensuremath{{\mathcal{P}$ with respective colourings $c$ and $c'$.

Observe that the expected value obtained in $\ensuremath{{\mathcal{P}$ by any $\text{BWC}$ satisfying strategy of $\text{Eve$ only depends on the weights of edges involved in WECs, or equivalently, in MWECs (as the set of plays that are not trapped in them has measure zero). Consequently, we define colouring $c'$ as follows: we keep the weights unchanged in edges that belong to some $\ensuremath{U \in  \ensuremath{\mathcal{U}_{w}$, and we put them to zero everywhere else, i.e., on any edge involving a negligible vertex. Weight zero is taken because it is lower than the expectation granted by WECs, which is **strictly** greater than zero by definition (as $\alpha = 0$).

````{prf:example} NEEDS TITLE AND LABEL 
Consider $\ensuremath{U_{1}$ in {numref}`12-fig:bwcRunningExample`. This EC is losing as argued before. The optimal expectation achievable in $\ensuremath{{\mathcal{P}  \ensuremath{\downharpoonright  \ensuremath{U_{1}$ by $\text{Eve$ is $4$: this is higher than what is achievable in both $\ensuremath{U_{2}$ and $\ensuremath{U_{3}$. Note that there exists no WEC included in $\ensuremath{U_{1}$. By \cref{chap:mdp}, we know that any strategy of $\text{Eve$ will see its expectation bounded by the maximum between the optimal expectations of the ECs $\ensuremath{U_{1}$, $\ensuremath{U_{2}$ and $\ensuremath{U_{3}$. Our previous arguments further refine this bound by restricting it to the maximum between the expectations of $\ensuremath{U_{2}$ and $\ensuremath{U_{3}$. Indeed, $\text{Eve$ cannot benefit from the expected value of $\ensuremath{U_{1}$ while using finite memory, as being trapped in $\ensuremath{U_{1}$ induces the existence of plays losing for the worst-case. Hence there is no point in playing inside $\ensuremath{U_{1}$ and $\text{Eve$ may as well cross it directly and try to maximize its expectation using the WECs, $\ensuremath{U_{2}$ and $\ensuremath{U_{3}$. The set of negligible vertices in $\ensuremath{{\mathcal{P}$ is $\ensuremath{V_{{\sf neg}} = V \setminus ( \ensuremath{U_{2} \cup  \ensuremath{U_{3}) = \{ \ensuremath{v_{1},  \ensuremath{v_{2},  \ensuremath{v_{3},  \ensuremath{v_{4},  \ensuremath{v_{5}\}$. We depict $\ensuremath{{\mathcal{P}'$ in {numref}`12-fig:bwc_mp_modifiedMDP`.

In the arena depicted in {numref}`12-fig:bwcWinningECsComputationExample`, we already observed that $\ensuremath{\mathcal{E} = \{ \ensuremath{U_{1},  \ensuremath{U_{2},  \ensuremath{U_{3}\}$ and $\ensuremath{\mathcal{W} =  \ensuremath{\mathcal{U}_{w} = \{ \ensuremath{U_{1},  \ensuremath{U_{3}\}$. Consider the negligible vertex $\ensuremath{v_{1} \in  \ensuremath{V_{{\sf neg}} =  \ensuremath{U_{2} \setminus  \ensuremath{U_{3}$. A finite-memory strategy of $\text{Eve$ may only take the edge $( \ensuremath{v_{1},  \ensuremath{v_{3})$ finitely often in order to ensure the worst-case requirement. If $\text{Eve$ were to play this edge repeatedly, the losing play $( \ensuremath{v_{1} \ensuremath{v_{3} \ensuremath{v_{4})^{\omega}$ would exist (while of probability zero). Therefore, $\text{Eve$ can only ensure that $\ensuremath{U_{3}$ is reached with a probability arbitrarily close to one, and not equal to one, because at some point, she has to switch to edge $( \ensuremath{v_{1},  \ensuremath{v_{2})$ (after a bounded time since $\text{Eve$ uses a finite-memory strategy).

Consider $\ensuremath{U_{1}$ in {numref}`12-fig:bwcRunningExample`. This EC is losing as argued before. The optimal expectation achievable in $\ensuremath{{\mathcal{P}  \ensuremath{\downharpoonright  \ensuremath{U_{1}$ by $\text{Eve$ is $4$: this is higher than what is achievable in both $\ensuremath{U_{2}$ and $\ensuremath{U_{3}$. Note that there exists no WEC included in $\ensuremath{U_{1}$. By \cref{chap:mdp}, we know that any strategy of $\text{Eve$ will see its expectation bounded by the maximum between the optimal expectations of the ECs $\ensuremath{U_{1}$, $\ensuremath{U_{2}$ and $\ensuremath{U_{3}$. Our previous arguments further refine this bound by restricting it to the maximum between the expectations of $\ensuremath{U_{2}$ and $\ensuremath{U_{3}$. Indeed, $\text{Eve$ cannot benefit from the expected value of $\ensuremath{U_{1}$ while using finite memory, as being trapped in $\ensuremath{U_{1}$ induces the existence of plays losing for the worst-case. Hence there is no point in playing inside $\ensuremath{U_{1}$ and $\text{Eve$ may as well cross it directly and try to maximize its expectation using the WECs, $\ensuremath{U_{2}$ and $\ensuremath{U_{3}$. The set of negligible vertices in $\ensuremath{{\mathcal{P}$ is $\ensuremath{V_{{\sf neg}} = V \setminus ( \ensuremath{U_{2} \cup  \ensuremath{U_{3}) = \{ \ensuremath{v_{1},  \ensuremath{v_{2},  \ensuremath{v_{3},  \ensuremath{v_{4},  \ensuremath{v_{5}\}$. We depict $\ensuremath{{\mathcal{P}'$ in {numref}`12-fig:bwc_mp_modifiedMDP`.

In the arena depicted in {numref}`12-fig:bwcWinningECsComputationExample`, we already observed that $\ensuremath{\mathcal{E} = \{ \ensuremath{U_{1},  \ensuremath{U_{2},  \ensuremath{U_{3}\}$ and $\ensuremath{\mathcal{W} =  \ensuremath{\mathcal{U}_{w} = \{ \ensuremath{U_{1},  \ensuremath{U_{3}\}$. Consider the negligible vertex $\ensuremath{v_{1} \in  \ensuremath{V_{{\sf neg}} =  \ensuremath{U_{2} \setminus  \ensuremath{U_{3}$. A finite-memory strategy of $\text{Eve$ may only take the edge $( \ensuremath{v_{1},  \ensuremath{v_{3})$ finitely often in order to ensure the worst-case requirement. If $\text{Eve$ were to play this edge repeatedly, the losing play $( \ensuremath{v_{1} \ensuremath{v_{3} \ensuremath{v_{4})^{\omega}$ would exist (while of probability zero). Therefore, $\text{Eve$ can only ensure that $\ensuremath{U_{3}$ is reached with a probability arbitrarily close to one, and not equal to one, because at some point, she has to switch to edge $( \ensuremath{v_{1},  \ensuremath{v_{2})$ (after a bounded time since $\text{Eve$ uses a finite-memory strategy).

````

```{figure} ./../FigAndAlgos/12-fig:bwc_mp_modifiedMDP.png
:name: 12-fig:bwc_mp_modifiedMDP
:align: center
Putting all weights outside MWECs to zero naturally drives the optimal expectation strategy in $\ensuremath{{\mathcal{P}'$, depicted by the thick edges, toward the highest valued MWECs. ECs are annotated with their corresponding optimal expectations in the original MDP $\ensuremath{{\mathcal{P}$ and the modified MDP $\ensuremath{{\mathcal{P}'$.
```

## Reach the highest valued winning end-components
 We compute the maximal expected mean-payoff $\beta^{\ast}$ that can be achieved by $\text{Eve$ in $\ensuremath{{\mathcal{P}'$, from $v_0$. This computation takes polynomial time and memoryless strategies suffice to achieve the maximal value, as established in  {prf:ref}`5-thm:general-mp-main`.

As discussed before, such a strategy reaches an EC of $\ensuremath{{\mathcal{P}'$ with probability one. Basically, we build a strategy that favours reaching ECs with high associated expectations in $\ensuremath{{\mathcal{P}'$.

We argue that the ECs reached with probability one by this strategy are necessarily WECs in $\ensuremath{{\mathcal{P}$. Clearly, if a WEC is reachable instead of a losing one, it will be favoured because of the weights definition in $\ensuremath{{\mathcal{P}'$ (expectation is strictly higher in WECs). Thus it remains to check if the set of WECs is reachable with probability one from any vertex in $V$. That is the case because of the preprocessing: we know that all vertices are winning for the worst-case requirement. Clearly, from any vertex in $A = V \setminus \bigcup_{ \ensuremath{U \in  \ensuremath{\mathcal{E}}  \ensuremath{U$, $\text{Eve$ cannot ensure to stay in $A$ (otherwise it would form an EC) and thus must be able to win the worst-case requirement from reached ECs. Now for any vertex in $B = \bigcup_{ \ensuremath{U \in  \ensuremath{\mathcal{E}}  \ensuremath{U \setminus \bigcup_{ \ensuremath{U \in  \ensuremath{\mathcal{U}_{w}}  \ensuremath{U$, i.e., vertices in LECs and not in any sub-EC winning, $\text{Eve$ cannot win the worst-case by staying in $B$, by definition of LEC. Since we know $\text{Eve$ can ensure the worst-case by hypothesis, it is clear that she must be able to reach $C = \bigcup_{ \ensuremath{U \in  \ensuremath{\mathcal{U}_{w}}  \ensuremath{U$ from any vertex in $B$, as claimed.

## Inside winning end-components
 Based on that, we know that WECs of $\ensuremath{{\mathcal{P}$ will be reached with probability one when maximizing the expected value in $\ensuremath{{\mathcal{P}'$. Let us first consider what we can say about such ECs if we assume that $\ensuremath{E_{\delta} =  \ensuremath{E$, i.e., if the stochastic model $\ensuremath{\tau^{\text{stoch}$ maps all possible edges to non-zero probabilities. 
We establish a finite-memory **combined strategy** $\ensuremath{\sigma^{\text{cmb}}$ of $\text{Eve$ that ensures (i) worst-case satisfaction while yielding (ii) an expected value $\varepsilon$-close to the maximal expectation inside the EC.

For two well-chosen parameters $\ensuremath{K,  \ensuremath{L \in  \mathbb{N}$, it is informally defined as follows: in phase $\ensuremath{**(a)**$, play a memoryless expected value optimal strategy $\ensuremath{\sigma^{\text{e}}$ for $\ensuremath{K$ steps and memorize $\ensuremath{\mathsf{Sum} \in  \mathbb{Z}$, the sum of weights along these steps; in phase $\ensuremath{**(b)**$, if $\ensuremath{\mathsf{Sum} > 0$, go to $\ensuremath{**(a)**$, otherwise play a memoryless worst-case optimal strategy $\ensuremath{\sigma^{\text{wc}}$ for $\ensuremath{L$ steps, then go to $\ensuremath{**(a)**$. In $\ensuremath{**(a)**$, $\text{Eve$ tries to increase her expectation and approach the optimal one, while in $\ensuremath{**(b)**$, she compensates, if needed, losses that occurred in $\ensuremath{**(a)**$.

The two memoryless strategies exist on the subarena induced by the EC: by definition of ECs, based on $\ensuremath{E_{\delta}$, the stochastic model of $\text{Adam$ will never be able to force leaving the EC against the combined strategy.

A key result to our approach is the existence of values for $\ensuremath{K$ and $\ensuremath{L$ such that (i) and (ii) are verified. We see plays as sequences of periods, each starting with phase $\ensuremath{**(a)**$.

First, for any $\ensuremath{K$, it is possible to define $\ensuremath{L( \ensuremath{K)$ such that any period composed of phases $\ensuremath{**(a)**+ \ensuremath{**(b)**$ ensures a mean-payoff at least $1/( \ensuremath{K+ \ensuremath{L) > 0$. Periods containing only phase $\ensuremath{**(a)**$ trivially induce a mean-payoff at least $1/ \ensuremath{K$ as they are not followed by phase $\ensuremath{**(b)**$. Both rely on the weights being integers. As the length of any period is bounded by $( \ensuremath{K+ \ensuremath{L)$, the inequality remains strict for the mean-payoff of any play, granting (i).

Now, consider parameter $\ensuremath{K$. Clearly, when $\ensuremath{K \rightarrow \infty$, the expectation over phase $\ensuremath{**(a)**$ tends to the optimal one. Nevertheless, phases $\ensuremath{**(b)**$ also contribute to the overall expectation of the combined strategy, and (in general) lower it so that it is strictly less than the optimal for any $\ensuremath{K,  \ensuremath{L \in  \mathbb{N}$. Hence to prove (ii), we not only need that the probability of playing phase $\ensuremath{**(b)**$ decreases when $\ensuremath{K$ increases, but also that it decreases faster than the increase of $\ensuremath{L$, needed to ensure (i), so that overall, the contribution of phases $\ensuremath{**(b)**$ tends to zero when $\ensuremath{K \rightarrow \infty$. This is indeed the case and is proved using results bounding the probability of observing a mean-payoff significantly (more than some $\varepsilon$) different than the optimal expectation along a phase $\ensuremath{**(a)**$ of length $\ensuremath{K \in  \mathbb{N}$: this probability decreases exponentially when $\ensuremath{K$ increases, while $\ensuremath{L$ only needs to be polynomial in $\ensuremath{K$.

````{prf:theorem} NEEDS TITLE 12-thm:insideWinning
:label: 12-thm:insideWinning

Let $U \in  \ensuremath{\mathcal{W}$ be a WEC, $\ensuremath{\tau^{\text{stoch}$ be such that $\ensuremath{E_{\delta} =  \ensuremath{E$, $v_0 \in U$ be the initial vertex, and let $\beta^\ast \in  \mathbb{Q}$ be the maximal expected value achievable by $\text{Eve$ in EC $U$. Then, for all $\varepsilon > 0$, there exists a finite-memory strategy of $\text{Eve$ that satisfies the $\text{BWC}$ problem for the thresholds pair $(0,\, \beta^\ast - \varepsilon)$.

````

````{prf:example} NEEDS TITLE AND LABEL 
Consider the subarena $\ensuremath{ \mathcal{A}_{\delta}  \ensuremath{\downharpoonright  \ensuremath{U_{3} =  \mathcal{A}  \ensuremath{\downharpoonright  \ensuremath{U_{3}$ from {numref}`12-fig:bwcRunningExample` and the initial vertex $\ensuremath{v_{10}$. Clearly, the worst-case requirement can be satisfied, that is why the EC is classified as winning. Always choosing to go to $\ensuremath{v_{9}$ when in $\ensuremath{v_{10}$ is an optimal memoryless worst-case strategy $\ensuremath{\sigma^{\text{wc}}$ that guarantees a mean-payoff $\alpha^\ast = 1$. Its expectation is $\mathbf{E}^{ \ensuremath{\sigma^{\text{wc}}}_{( \mathcal{A}  \ensuremath{\downharpoonright  \ensuremath{U_{3})_{\tau^\text{stoch}},v_{10}}[ \mathtt{MeanPayoff}^{-}] = 1$. On the other hand, the strategy $\ensuremath{\sigma^{\text{e}}$ that always selects the edge going to $\ensuremath{v_{11}$ is optimal regarding the expected value criterion: it induces expectation $\beta^\ast = \big(0 + \big(1/2 \cdot 9 + 1/2 \cdot (-1)\big)\big)/2 = 2$ against the stochastic model $\ensuremath{\tau^{\text{stoch}$. However, it can only guarantee a mean-payoff of value $-1/2$ in the worst-case.

By the reasoning above, we know that it is possible to find finite-memory strategies satisfying the $\text{BWC}$ problem for any thresholds pair $(0,\, 2 - \varepsilon)$, $\varepsilon > 0$. In particular, consider the thresholds pair $(0,\, 3/2)$. We build a combined strategy $\ensuremath{\sigma^{\text{cmb}}$ as sketched before. Let $\ensuremath{K =  \ensuremath{L = 2$: the strategy plays the edge $( \ensuremath{v_{10},  \ensuremath{v_{11})$ once, then if the edge of value $9$ has been chosen by $\text{Adam$, it chooses $( \ensuremath{v_{10},  \ensuremath{v_{11})$ again; otherwise it chooses the edge $( \ensuremath{v_{10},  \ensuremath{v_{9})$ once and then resumes choosing $( \ensuremath{v_{10},  \ensuremath{v_{11})$. This strategy satisfies the $\text{BWC}$ problem. In the worst-case, $\text{Adam$ always chooses the $-1$ edge, but each time he does so, the $-1$ is followed by two $+1$ thanks to the cycle $\ensuremath{v_{10}  \ensuremath{v_{9}  \ensuremath{v_{10}$. Strategy $\ensuremath{\sigma^{\text{cmb}}$ hence guarantees a mean-payoff equal to $(0 - 1 + 1 + 1)/4 = 1/4 > 0$ in the worst-case. For the expected value requirement, we can build the induced Markov chain $( \mathcal{A}  \ensuremath{\downharpoonright  \ensuremath{U_{3})_{ \ensuremath{\sigma^{\text{cmb}}, \tau^\text{stoch}}$ ({numref}`12-fig:mp_insideSWEC_MC`) and check that its expectation is $\mathbf{E}^{ \ensuremath{\sigma^{\text{cmb}}}_{( \mathcal{A}  \ensuremath{\downharpoonright  \ensuremath{U_{3})_{\tau^\text{stoch}},v_{10}}[ \mathtt{MeanPayoff}^{-}] = 5/3 > 3/2$ (\cref{chap:payoffs}).

```{figure} ./../FigAndAlgos/12-fig:mp_insideSWEC_MC.png
:name: 12-fig:mp_insideSWEC_MC
:align: center
Markov chain induced by the combined strategy $\ensuremath{\sigma^{\text{cmb}}$ and the stochastic model $\ensuremath{\tau^{\text{stoch}$ over the WEC $\ensuremath{U_{3}$ of $\mathcal{A}$.
```

Consider the subarena $\ensuremath{ \mathcal{A}_{\delta}  \ensuremath{\downharpoonright  \ensuremath{U_{3} =  \mathcal{A}  \ensuremath{\downharpoonright  \ensuremath{U_{3}$ from {numref}`12-fig:bwcRunningExample` and the initial vertex $\ensuremath{v_{10}$. Clearly, the worst-case requirement can be satisfied, that is why the EC is classified as winning. Always choosing to go to $\ensuremath{v_{9}$ when in $\ensuremath{v_{10}$ is an optimal memoryless worst-case strategy $\ensuremath{\sigma^{\text{wc}}$ that guarantees a mean-payoff $\alpha^\ast = 1$. Its expectation is $\mathbf{E}^{ \ensuremath{\sigma^{\text{wc}}}_{( \mathcal{A}  \ensuremath{\downharpoonright  \ensuremath{U_{3})_{\tau^\text{stoch}},v_{10}}[ \mathtt{MeanPayoff}^{-}] = 1$. On the other hand, the strategy $\ensuremath{\sigma^{\text{e}}$ that always selects the edge going to $\ensuremath{v_{11}$ is optimal regarding the expected value criterion: it induces expectation $\beta^\ast = \big(0 + \big(1/2 \cdot 9 + 1/2 \cdot (-1)\big)\big)/2 = 2$ against the stochastic model $\ensuremath{\tau^{\text{stoch}$. However, it can only guarantee a mean-payoff of value $-1/2$ in the worst-case.

By the reasoning above, we know that it is possible to find finite-memory strategies satisfying the $\text{BWC}$ problem for any thresholds pair $(0,\, 2 - \varepsilon)$, $\varepsilon > 0$. In particular, consider the thresholds pair $(0,\, 3/2)$. We build a combined strategy $\ensuremath{\sigma^{\text{cmb}}$ as sketched before. Let $\ensuremath{K =  \ensuremath{L = 2$: the strategy plays the edge $( \ensuremath{v_{10},  \ensuremath{v_{11})$ once, then if the edge of value $9$ has been chosen by $\text{Adam$, it chooses $( \ensuremath{v_{10},  \ensuremath{v_{11})$ again; otherwise it chooses the edge $( \ensuremath{v_{10},  \ensuremath{v_{9})$ once and then resumes choosing $( \ensuremath{v_{10},  \ensuremath{v_{11})$. This strategy satisfies the $\text{BWC}$ problem. In the worst-case, $\text{Adam$ always chooses the $-1$ edge, but each time he does so, the $-1$ is followed by two $+1$ thanks to the cycle $\ensuremath{v_{10}  \ensuremath{v_{9}  \ensuremath{v_{10}$. Strategy $\ensuremath{\sigma^{\text{cmb}}$ hence guarantees a mean-payoff equal to $(0 - 1 + 1 + 1)/4 = 1/4 > 0$ in the worst-case. For the expected value requirement, we can build the induced Markov chain $( \mathcal{A}  \ensuremath{\downharpoonright  \ensuremath{U_{3})_{ \ensuremath{\sigma^{\text{cmb}}, \tau^\text{stoch}}$ ({numref}`12-fig:mp_insideSWEC_MC`) and check that its expectation is $\mathbf{E}^{ \ensuremath{\sigma^{\text{cmb}}}_{( \mathcal{A}  \ensuremath{\downharpoonright  \ensuremath{U_{3})_{\tau^\text{stoch}},v_{10}}[ \mathtt{MeanPayoff}^{-}] = 5/3 > 3/2$ (\cref{chap:payoffs}).

```{figure} ./../FigAndAlgos/12-fig:mp_insideSWEC_MC.png
:name: 12-fig:mp_insideSWEC_MC
:align: center
Markov chain induced by the combined strategy $\ensuremath{\sigma^{\text{cmb}}$ and the stochastic model $\ensuremath{\tau^{\text{stoch}$ over the WEC $\ensuremath{U_{3}$ of $\mathcal{A}$.
```

````

````{admonition} Remark 
\label{12-rmk:bwcMemorylessNotEnough}
Memoryless strategies do not suffice for the $\text{BWC}$ problem, even with randomization. Indeed, the edge $( \ensuremath{v_{10},  \ensuremath{v_{11})$ cannot be assigned a non-zero probability as it would endanger the worst-case requirement (since the play $( \ensuremath{v_{10} \ensuremath{v_{11})^{\omega}$ cycling on the edge of weight $-1$ would exist and have a negative mean-payoff). Hence, the only acceptable memoryless strategy is $\ensuremath{\sigma^{\text{wc}}$, which has only an expectation of $1$.

````

Now, consider what happens if $\ensuremath{E_{\delta} \subsetneq E$. Then, if $\text{Adam$ uses an arbitrary strategy, he can take edges of probability zero, i.e., in $E \setminus  \ensuremath{E_{\delta}$, either staying in the EC, or leaving it. In both cases, this must be taken into account in order to satisfy the worst-case constraint as it may involve dangerous weights (recall that zero-probability edges are not considered when an EC is classified as winning or not). Fortunately, if this were to occur, $\text{Eve$ could switch to a worst-case winning memoryless strategy $\ensuremath{\sigma^{\text{sec}}$, which exists in all vertices thanks to the preprocessing, to preserve the worst-case requirement. Regarding the expected value, this has no impact as it occurs with probability zero against $\ensuremath{\tau^{\text{stoch}$. The strategy to follow in WECs hence adds this reaction procedure to the combined strategy: we call it the **witness-and-secure strategy** $\ensuremath{\sigma^{\text{wns}}$.

````{prf:theorem} NEEDS TITLE 12-thm:wns
:label: 12-thm:wns

Let $U \in  \ensuremath{\mathcal{W}$ be a WEC, $v_0 \in U$ be the initial vertex, and $\beta^\ast \in  \mathbb{Q}$ be the maximal expected value achievable by $\text{Eve$ in EC $U$. Then, for all $\varepsilon > 0$, there exists a finite-memory strategy of $\text{Eve$ that satisfies the $\text{BWC}$ problem for the thresholds pair $(0,\, \beta^\ast - \varepsilon)$.

````

````{prf:example} NEEDS TITLE AND LABEL 
Consider the WEC $\ensuremath{U_{2}$ in {numref}`12-fig:bwcRunningExample` and the initial vertex $\ensuremath{v_{6} \in  \ensuremath{U_{2}$. $\text{Eve$ can ensure a strictly positive mean-payoff in the subarena $\ensuremath{ \mathcal{A}_{\delta}  \ensuremath{\downharpoonright  \ensuremath{U_{2}$, but not in $\mathcal{A}  \ensuremath{\downharpoonright  \ensuremath{U_{2}$. Indeed, it is easy to see that by always choosing the $-1$ edges (which requires an edge $( \ensuremath{v_{7},  \ensuremath{v_{6}) \in  \ensuremath{E_{\delta} \setminus  \ensuremath{E$), $\text{Adam$ can ensure a negative mean-payoff whatever the strategy of $\text{Eve$. However, there exists a strategy that ensures the worst-case constraint, i.e., that yields a strictly positive mean-payoff against any strategy of Adam, by leaving the EC. Let $\ensuremath{\sigma^{\text{sec}}$ be the memoryless strategy that takes the edge $( \ensuremath{v_{6},  \ensuremath{v_{9})$ and then cycle on $( \ensuremath{v_{10} \ensuremath{v_{9})^{\omega}$ forever: it guarantees a mean-payoff of $1 > 0$.

For a moment, consider the EC $\ensuremath{U_{2}$ in $\ensuremath{ \mathcal{A}_{\delta}$. Graphically, it means that the $-1$ edge from $\ensuremath{v_{7}$ to $\ensuremath{v_{6}$ disappears. In the subarena $\ensuremath{ \mathcal{A}_{\delta}  \ensuremath{\downharpoonright  \ensuremath{U_{2}$, there are two particular memoryless strategies. The optimal worst-case strategy $\ensuremath{\sigma^{\text{wc}}$ guarantees a mean-payoff of $1/2 > 0$ by choosing to go to $\ensuremath{v_{7}$. The optimal expectation strategy $\ensuremath{\sigma^{\text{e}}$ yields an expected mean-payoff of $3$ by choosing to go to $\ensuremath{v_{8}$ (naturally this strategy yields the same expectation whether we consider edges in $\ensuremath{E_{\delta}$ or in $E$). Based on them, we build the combined strategy $\ensuremath{\sigma^{\text{cmb}}$ of Eve as defined earlier and by  {prf:ref}`12-thm:insideWinning`, for any $\varepsilon > 0$, there are values of $\ensuremath{K$ and $\ensuremath{L$ such that it satisfies the $\text{BWC}$ problem for thresholds $(0,\, 3-\varepsilon)$ in $\ensuremath{ \mathcal{A}_{\delta}  \ensuremath{\downharpoonright  \ensuremath{U_{2}$. For instance, for $\ensuremath{K =  \ensuremath{L = 2$, we have $\mathbf{E}^{ \ensuremath{\sigma^{\text{cmb}}}_{( \mathcal{A}  \ensuremath{\downharpoonright  \ensuremath{U_{2})_{\tau^\text{stoch}},v_{6}}[ \mathtt{MeanPayoff}^{-}] = 13/6$.

We construct the witness-and-secure strategy $\ensuremath{\sigma^{\text{wns}}$ based on $\ensuremath{\sigma^{\text{cmb}}$ and $\ensuremath{\sigma^{\text{sec}}$ as described above. In this case, that means playing as $\ensuremath{\sigma^{\text{cmb}}$ until the $-1$ edge from $\ensuremath{v_{7}$ to $\ensuremath{v_{6}$ is taken by $\text{Adam$. This strategy ensures a worst-case mean-payoff equal to $1 > 0$ thanks to $\ensuremath{\sigma^{\text{sec}}$ and yields expectation $\mathbf{E}^{ \ensuremath{\sigma^{\text{wns}}}_{( \mathcal{A}  \ensuremath{\downharpoonright  \ensuremath{U_{2})_{\tau^\text{stoch}},v_{6}}[ \mathtt{MeanPayoff}^{-}] = 13/6$ for $\ensuremath{K =  \ensuremath{L = 2$.

Finally, notice that securing the mean-payoff by switching to  $\ensuremath{\sigma^{\text{sec}}$ **is needed** to satisfy the worst-case requirement if $\text{Adam$ plays in $\ensuremath{E \setminus  \ensuremath{E_{\delta}$. Also, observe that it is still necessary to alternate according to $\ensuremath{\sigma^{\text{cmb}}$ in $\ensuremath{ \mathcal{A}_{\delta}  \ensuremath{\downharpoonright  \ensuremath{U_{2}$ and that playing $\ensuremath{\sigma^{\text{e}}$ is not sufficient to ensure the worst-case (because $\text{Eve$ has to deal with the $-1$ edge from $\ensuremath{v_{8}$ to $\ensuremath{v_{6}$ that remains in $\ensuremath{E_{\delta}$).

Consider the WEC $\ensuremath{U_{2}$ in {numref}`12-fig:bwcRunningExample` and the initial vertex $\ensuremath{v_{6} \in  \ensuremath{U_{2}$. $\text{Eve$ can ensure a strictly positive mean-payoff in the subarena $\ensuremath{ \mathcal{A}_{\delta}  \ensuremath{\downharpoonright  \ensuremath{U_{2}$, but not in $\mathcal{A}  \ensuremath{\downharpoonright  \ensuremath{U_{2}$. Indeed, it is easy to see that by always choosing the $-1$ edges (which requires an edge $( \ensuremath{v_{7},  \ensuremath{v_{6}) \in  \ensuremath{E_{\delta} \setminus  \ensuremath{E$), $\text{Adam$ can ensure a negative mean-payoff whatever the strategy of $\text{Eve$. However, there exists a strategy that ensures the worst-case constraint, i.e., that yields a strictly positive mean-payoff against any strategy of Adam, by leaving the EC. Let $\ensuremath{\sigma^{\text{sec}}$ be the memoryless strategy that takes the edge $( \ensuremath{v_{6},  \ensuremath{v_{9})$ and then cycle on $( \ensuremath{v_{10} \ensuremath{v_{9})^{\omega}$ forever: it guarantees a mean-payoff of $1 > 0$.

For a moment, consider the EC $\ensuremath{U_{2}$ in $\ensuremath{ \mathcal{A}_{\delta}$. Graphically, it means that the $-1$ edge from $\ensuremath{v_{7}$ to $\ensuremath{v_{6}$ disappears. In the subarena $\ensuremath{ \mathcal{A}_{\delta}  \ensuremath{\downharpoonright  \ensuremath{U_{2}$, there are two particular memoryless strategies. The optimal worst-case strategy $\ensuremath{\sigma^{\text{wc}}$ guarantees a mean-payoff of $1/2 > 0$ by choosing to go to $\ensuremath{v_{7}$. The optimal expectation strategy $\ensuremath{\sigma^{\text{e}}$ yields an expected mean-payoff of $3$ by choosing to go to $\ensuremath{v_{8}$ (naturally this strategy yields the same expectation whether we consider edges in $\ensuremath{E_{\delta}$ or in $E$). Based on them, we build the combined strategy $\ensuremath{\sigma^{\text{cmb}}$ of Eve as defined earlier and by  {prf:ref}`12-thm:insideWinning`, for any $\varepsilon > 0$, there are values of $\ensuremath{K$ and $\ensuremath{L$ such that it satisfies the $\text{BWC}$ problem for thresholds $(0,\, 3-\varepsilon)$ in $\ensuremath{ \mathcal{A}_{\delta}  \ensuremath{\downharpoonright  \ensuremath{U_{2}$. For instance, for $\ensuremath{K =  \ensuremath{L = 2$, we have $\mathbf{E}^{ \ensuremath{\sigma^{\text{cmb}}}_{( \mathcal{A}  \ensuremath{\downharpoonright  \ensuremath{U_{2})_{\tau^\text{stoch}},v_{6}}[ \mathtt{MeanPayoff}^{-}] = 13/6$.

We construct the witness-and-secure strategy $\ensuremath{\sigma^{\text{wns}}$ based on $\ensuremath{\sigma^{\text{cmb}}$ and $\ensuremath{\sigma^{\text{sec}}$ as described above. In this case, that means playing as $\ensuremath{\sigma^{\text{cmb}}$ until the $-1$ edge from $\ensuremath{v_{7}$ to $\ensuremath{v_{6}$ is taken by $\text{Adam$. This strategy ensures a worst-case mean-payoff equal to $1 > 0$ thanks to $\ensuremath{\sigma^{\text{sec}}$ and yields expectation $\mathbf{E}^{ \ensuremath{\sigma^{\text{wns}}}_{( \mathcal{A}  \ensuremath{\downharpoonright  \ensuremath{U_{2})_{\tau^\text{stoch}},v_{6}}[ \mathtt{MeanPayoff}^{-}] = 13/6$ for $\ensuremath{K =  \ensuremath{L = 2$.

Finally, notice that securing the mean-payoff by switching to  $\ensuremath{\sigma^{\text{sec}}$ **is needed** to satisfy the worst-case requirement if $\text{Adam$ plays in $\ensuremath{E \setminus  \ensuremath{E_{\delta}$. Also, observe that it is still necessary to alternate according to $\ensuremath{\sigma^{\text{cmb}}$ in $\ensuremath{ \mathcal{A}_{\delta}  \ensuremath{\downharpoonright  \ensuremath{U_{2}$ and that playing $\ensuremath{\sigma^{\text{e}}$ is not sufficient to ensure the worst-case (because $\text{Eve$ has to deal with the $-1$ edge from $\ensuremath{v_{8}$ to $\ensuremath{v_{6}$ that remains in $\ensuremath{E_{\delta}$).

````

## Global strategy synthesis
 In summary, (a) LECs should be avoided and will be by a strategy that optimizes the expectation on the MDP $\ensuremath{{\mathcal{P}'$; (b) in WECs, $\text{Eve$ can obtain ($\varepsilon$-closely) the expectation of the EC **and** ensure the worst-case threshold.

Hence, we finally compare the value $\ensuremath{\beta^{\ast}$ computed by {numref}`12-algo:BWC` with the expected value threshold $\ensuremath{\beta$: (i) if it is strictly higher, we conclude that there exists a finite-memory strategy satisfying the $\text{BWC}$ problem, and (ii) if it is not, we conclude that there does not exist such a strategy.

To prove (i), we establish a finite-memory strategy in $\mathcal{A}$, called **global strategy** $\ensuremath{\sigma^{\text{glb}}$, of $\text{Eve$ that ensures a strictly positive mean-payoff against an antagonistic adversary, and ensures an expected mean-payoff $\varepsilon$-close to $\ensuremath{\beta^{\ast}$ (hence, strictly greater than $\ensuremath{\beta$) against the stochastic adversary modeled by $\ensuremath{\tau^{\text{stoch}$ (i.e., in $\ensuremath{{\mathcal{P}$). The intuition is as follows. We play the memoryless optimal strategy of $\ensuremath{{\mathcal{P}'$ for a sufficiently long time, defined by a parameter $\ensuremath{N \in  \mathbb{N}$, in order to be with probability close to one in a WEC (the convergence is exponential by results on absorption times in Markov chains). Then, if we are inside a WEC, we switch to the corresponding witness-and-secure strategy (there is a different one for each MWEC) which, as sketched in the previous paragraph, ensures the worst-case and the expectation thresholds. If we are not yet in a WEC, then we switch to a worst-case winning strategy, which always exists thanks to the preprocessing. Thus the mean-payoff of plays that do not reach WECs is strictly positive. Since in WECs we are $\varepsilon$-close to the maximal expected value of the EC, we can conclude that it is possible to play the optimal expectation strategy of $\ensuremath{{\mathcal{P}'$ for sufficiently long to obtain an overall expected value which is arbitrarily close to $\ensuremath{\beta^{\ast}$, and still guarantee the worst-case threshold in all consistent plays.

To prove (ii), it suffices to understand that only ECs have an impact on the expectation, and that LECs cannot be used forever without endangering the worst-case requirement.

Note that given a winning strategy on $\mathcal{A}$, it is possible to build a corresponding winning strategy on $\mathcal{A}^{i}$ by reintegrating the memory states of $\tau^i$ in the memory structure of the winning strategy of $\text{Eve$. Hence {numref}`12-algo:BWC` is correct and complete.

````{prf:theorem} NEEDS TITLE 12-thm:bwcCorrectAndComplete
:label: 12-thm:bwcCorrectAndComplete

If {numref}`12-algo:BWC` answers Yes, then there exist values of the parameters such that the pure finite-memory global strategy $\ensuremath{\sigma^{\text{glb}}$ satisfies the $\text{BWC}$ mean-payoff problem. In the opposite case, there exists no finite-memory strategy that satisfies the $\text{BWC}$ mean-payoff problem.

````

````{prf:example} NEEDS TITLE AND LABEL 
Consider the arena in {numref}`12-fig:bwcRunningExample` and the associated MDP $\ensuremath{{\mathcal{P}$. Following \cref{chap:mdp}, analysis of the maximal ECs $\ensuremath{U_{1}$, $\ensuremath{U_{2}$ and $\ensuremath{U_{3}$ reveals that the maximal expected mean-payoff achievable in $\ensuremath{{\mathcal{P}$ is $4$. It is for instance obtained by the memoryless strategy that chooses to go to $\ensuremath{v_{2}$ from $\ensuremath{v_{1}$ and to $\ensuremath{v_{4}$ from $\ensuremath{v_{3}$. Observe that playing in $\ensuremath{U_{1}$ forever is needed to achieve this expectation. By  {prf:ref}`12-lem:EC-inf`, this should not be allowed as the worst-case cannot be ensured if it is. Indeed, $\text{Adam$ can produce worst-case losing plays by playing the $-1$ edge. Clearly, the maximal expected value that $\text{Eve$ can ensure while guaranteeing the worst-case requirement is thus bounded by the maximal expectation in $\ensuremath{{\mathcal{P}'$, i.e., by $3$, as depicted in {numref}`12-fig:bwc_mp_modifiedMDP`. Let $\ensuremath{\sigma^{\text{e}}$ denote an optimal memoryless expectation strategy in $\ensuremath{{\mathcal{P}'$ that tries to enter $\ensuremath{U_{2}$ by playing $( \ensuremath{v_{1},  \ensuremath{v_{2})$ and $( \ensuremath{v_{3},  \ensuremath{v_{5})$, and then plays edge $( \ensuremath{v_{6},  \ensuremath{v_{8})$ forever (thick edges in {numref}`12-fig:bwc_mp_modifiedMDP`).

Observe that {numref}`12-algo:BWC` answers Yes for any thresholds pair $(0,\,  \ensuremath{\beta)$ such that $\ensuremath{\beta < 3$. For the sake of illustration, we construct the global strategy $\ensuremath{\sigma^{\text{glb}}$ as presented earlier, with $\ensuremath{N = 6$ and $\ensuremath{K =  \ensuremath{L = 2$. For the first six steps, it behaves exactly as $\ensuremath{\sigma^{\text{e}}$. Note that after the six steps, the probability of being in $\ensuremath{U_{2}$ is $1/4 + 1/8 = 3/8$. Then, $\ensuremath{\sigma^{\text{glb}}$ switches to another strategy depending on the current vertex ($\ensuremath{\sigma^{\text{wns}}$ or $\ensuremath{\sigma^{\text{wc}}$) and sticks to this strategy forever. In particular, if the current vertex belongs to $\ensuremath{U_{2}$, it switches to $\ensuremath{\sigma^{\text{wns}}$ for $\ensuremath{K =  \ensuremath{L = 2$, which guarantees the worst-case threshold and induces an expectation of $13/6$. By definition of $\ensuremath{\sigma^{\text{glb}}$, if the current vertex after six steps is not in $\ensuremath{U_{2}$, then $\ensuremath{\sigma^{\text{glb}}$ switches to $\ensuremath{\sigma^{\text{wc}}$ which guarantees a mean-payoff of $1$ by reaching vertex $\ensuremath{v_{9}$ and then playing $( \ensuremath{v_{9} \ensuremath{v_{10})^{\omega}$. Overall, the expected mean-payoff of $\ensuremath{\sigma^{\text{glb}}$ against $\ensuremath{\tau^{\text{stoch}$ is
```{math}\n
 \mathbf{E}^{ \ensuremath{\sigma^{\text{glb}}}_{ \mathcal{A}_{\tau^\text{stoch}},v_{1}}[ \mathtt{MeanPayoff}^{-}] \geq \dfrac{3}{8}\cdot\dfrac{13}{6} + \dfrac{5}{8}\cdot 1 = \dfrac{23}{16}.
\\n```
Notice that by taking $\ensuremath{N$, $\ensuremath{K$ and $\ensuremath{L$ large enough, it is possible to satisfy the $\text{BWC}$ problem for any $\ensuremath{\beta < 3$ with the strategy $\ensuremath{\sigma^{\text{glb}}$. Also, observe that the WEC $\ensuremath{U_{2}$ is crucial to achieve expectations strictly greater than $2$, which is the upper bound when limited to EC $\ensuremath{U_{3}$. For instance, $\ensuremath{N = 25$ and $\ensuremath{K =  \ensuremath{L = 2$ implies an expectation strictly greater than $2$ for the global strategy.

Lastly, note that in general, the maximal expectation achievable in $\ensuremath{{\mathcal{P}'$ (and thus in $\ensuremath{{\mathcal{P}$ when limited to strategies that respect the worst-case requirement) may depend on a combination of ECs instead of a unique one. This is transparent through the solving of the expected value problem in the MDP $\ensuremath{{\mathcal{P}'$. Hence, the approach followed by {numref}`12-algo:BWC` is a way of solving a complex problem by breaking it into smaller pieces.

Consider the arena in {numref}`12-fig:bwcRunningExample` and the associated MDP $\ensuremath{{\mathcal{P}$. Following \cref{chap:mdp}, analysis of the maximal ECs $\ensuremath{U_{1}$, $\ensuremath{U_{2}$ and $\ensuremath{U_{3}$ reveals that the maximal expected mean-payoff achievable in $\ensuremath{{\mathcal{P}$ is $4$. It is for instance obtained by the memoryless strategy that chooses to go to $\ensuremath{v_{2}$ from $\ensuremath{v_{1}$ and to $\ensuremath{v_{4}$ from $\ensuremath{v_{3}$. Observe that playing in $\ensuremath{U_{1}$ forever is needed to achieve this expectation. By  {prf:ref}`12-lem:EC-inf`, this should not be allowed as the worst-case cannot be ensured if it is. Indeed, $\text{Adam$ can produce worst-case losing plays by playing the $-1$ edge. Clearly, the maximal expected value that $\text{Eve$ can ensure while guaranteeing the worst-case requirement is thus bounded by the maximal expectation in $\ensuremath{{\mathcal{P}'$, i.e., by $3$, as depicted in {numref}`12-fig:bwc_mp_modifiedMDP`. Let $\ensuremath{\sigma^{\text{e}}$ denote an optimal memoryless expectation strategy in $\ensuremath{{\mathcal{P}'$ that tries to enter $\ensuremath{U_{2}$ by playing $( \ensuremath{v_{1},  \ensuremath{v_{2})$ and $( \ensuremath{v_{3},  \ensuremath{v_{5})$, and then plays edge $( \ensuremath{v_{6},  \ensuremath{v_{8})$ forever (thick edges in {numref}`12-fig:bwc_mp_modifiedMDP`).

Observe that {numref}`12-algo:BWC` answers Yes for any thresholds pair $(0,\,  \ensuremath{\beta)$ such that $\ensuremath{\beta < 3$. For the sake of illustration, we construct the global strategy $\ensuremath{\sigma^{\text{glb}}$ as presented earlier, with $\ensuremath{N = 6$ and $\ensuremath{K =  \ensuremath{L = 2$. For the first six steps, it behaves exactly as $\ensuremath{\sigma^{\text{e}}$. Note that after the six steps, the probability of being in $\ensuremath{U_{2}$ is $1/4 + 1/8 = 3/8$. Then, $\ensuremath{\sigma^{\text{glb}}$ switches to another strategy depending on the current vertex ($\ensuremath{\sigma^{\text{wns}}$ or $\ensuremath{\sigma^{\text{wc}}$) and sticks to this strategy forever. In particular, if the current vertex belongs to $\ensuremath{U_{2}$, it switches to $\ensuremath{\sigma^{\text{wns}}$ for $\ensuremath{K =  \ensuremath{L = 2$, which guarantees the worst-case threshold and induces an expectation of $13/6$. By definition of $\ensuremath{\sigma^{\text{glb}}$, if the current vertex after six steps is not in $\ensuremath{U_{2}$, then $\ensuremath{\sigma^{\text{glb}}$ switches to $\ensuremath{\sigma^{\text{wc}}$ which guarantees a mean-payoff of $1$ by reaching vertex $\ensuremath{v_{9}$ and then playing $( \ensuremath{v_{9} \ensuremath{v_{10})^{\omega}$. Overall, the expected mean-payoff of $\ensuremath{\sigma^{\text{glb}}$ against $\ensuremath{\tau^{\text{stoch}$ is
```{math}\n
 \mathbf{E}^{ \ensuremath{\sigma^{\text{glb}}}_{ \mathcal{A}_{\tau^\text{stoch}},v_{1}}[ \mathtt{MeanPayoff}^{-}] \geq \dfrac{3}{8}\cdot\dfrac{13}{6} + \dfrac{5}{8}\cdot 1 = \dfrac{23}{16}.
\\n```
Notice that by taking $\ensuremath{N$, $\ensuremath{K$ and $\ensuremath{L$ large enough, it is possible to satisfy the $\text{BWC}$ problem for any $\ensuremath{\beta < 3$ with the strategy $\ensuremath{\sigma^{\text{glb}}$. Also, observe that the WEC $\ensuremath{U_{2}$ is crucial to achieve expectations strictly greater than $2$, which is the upper bound when limited to EC $\ensuremath{U_{3}$. For instance, $\ensuremath{N = 25$ and $\ensuremath{K =  \ensuremath{L = 2$ implies an expectation strictly greater than $2$ for the global strategy.

Lastly, note that in general, the maximal expectation achievable in $\ensuremath{{\mathcal{P}'$ (and thus in $\ensuremath{{\mathcal{P}$ when limited to strategies that respect the worst-case requirement) may depend on a combination of ECs instead of a unique one. This is transparent through the solving of the expected value problem in the MDP $\ensuremath{{\mathcal{P}'$. Hence, the approach followed by {numref}`12-algo:BWC` is a way of solving a complex problem by breaking it into smaller pieces.

````

## Complexity bounds
 The input size of the algorithm depends on the size of the arena, the size of the memory structure for the stochastic model, and the encodings of probabilities, weights and thresholds. We can prove that all computing steps require (deterministic) polynomial time except for calls to an algorithm solving the worst-case threshold problem, which is in $\textrm{NP} \cap  \textrm{coNP}$ and not known to be in $\P$ ( {prf:ref}`4-thm:MP-NPcoNP`). Hence, the overall complexity of the $\text{BWC}$ problem is in $\textrm{NP} \cap  \textrm{coNP}$ (using $\P^{ \textrm{NP} \cap  \textrm{coNP}} =  \textrm{NP} \cap  \textrm{coNP}$ {cite}`Brassard:1979`) and may collapse to $\P$ if the worst-case problem were to be proved in $\P$.

The $\text{BWC}$ problem is at least as difficult as the worst-case problem thanks to a trivial polynomial-time reduction from the latter to the former. Thus, membership to $\textrm{NP} \cap  \textrm{coNP}$ can be seen as optimal regarding our current knowledge of mean-payoff games.

````{prf:theorem} NEEDS TITLE 12-thm:bwcDecisionProblem
:label: 12-thm:bwcDecisionProblem

The BWC mean-payoff problem is in $\textrm{NP} \cap  \textrm{coNP}$ and at least as hard as solving mean-payoff games. Moreover, pseudo-polynomial-memory strategies may be necessary for Eve and are always sufficient.

````

The memory bounds follow from the (involved) probability results used to determine the values of parameters $K$, $L$ and $N$ in the aforementioned strategies: such parameters need to be polynomial in the size of the arena but also in the probabilities, weights and thresholds.

Using the pseudo-polynomial-time algorithm of \cref{chap:payoffs} for mean-payoff games, \todo{I need label for Subsect. 4.3.4} we obtain the following corollary.

````{prf:corollary} NEEDS TITLE AND LABEL 
{numref}`12-algo:BWC` solves the BWC mean-payoff problem in pseudo-poly\-no\-mial time.

{numref}`12-algo:BWC` solves the BWC mean-payoff problem in pseudo-poly\-no\-mial time.

````

## Wrap-up
 As witnessed by our long overview, solving the beyond worst-case problem requires much more involved techniques than solving the two individual problems, worst-case and expected value, separately. Complexity-wise, it is fortunate that the problem stays in $\textrm{NP} \cap  \textrm{coNP}$, and is no more complex that simple mean-payoff games. The multiobjective nature of the problem still incurs a cost with regard to strategies: whereas memoryless strategies suffice both in mean-payoff games and mean-payoff MDPs, we here need pseudo-polynomial memory. Finally, note that Eve does not need to use randomness: pure strategies still suffice.
