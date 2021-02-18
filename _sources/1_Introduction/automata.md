(1-sec:automata)=
# Automata


```{math}
\newcommand{\col}{\textsf{col}}
\newcommand{\Automaton}{\mathbf{A}}
```

The study of games is deeply intertwined with automata over infinite words and trees.
We will not elaborate much on that aspect in this book, but in a few places we will use automata.
We define here (non-deterministic) automata over infinite words, and refer to {cite}`Thomas:1997`
for a survey on automata theory over infinite objects (words and trees) and logic.

````{prf:definition} Automata
:label: 1-def:automata

Let $\Sigma$ be an alphabet.
An automaton over the alphabet $\Sigma$ is a tuple $\mathbf{A}= (Q,q_0,\Delta,A)$ where:

*  $Q$ is a finite set of states,

*  $q_0 \in Q$ is the initial state,

*  $\Delta \subseteq Q \times \Sigma \times Q$ is the transition relation,

*  $A \subseteq \Delta^\omega$ is the acceptance condition.

````

We assume that automata are complete: from any state $q$ and letter $a$,
there exists a transition $(q,a,q') \in \Delta$. 
This mirrors the convention for games that every vertex has an outgoing edge.

There is one difference at the syntactic level between games and automata: 
in games the condition is defined over sequences of vertices, 
while in automata the acceptance condition is defined over sequences of transitions (which contain more information than states).
In other words for automata we use transition based acceptance conditions instead of state based acceptance conditions.
This more succinct definition of automata naturally composes with games in the same way as the state based acceptance definition does,
see Section {ref}`1-sec:reductions`, and sometimes yields smaller automata, see Section {ref}`2-sec:zielonka`


For a (finite or infinite) word $w = w_0 w_1 \dots$, a run $\rho = (q_0,w_0,q_1)(q_1,w_1,q_2) \dots$ over $w$ is a sequence of consecutive transitions starting from the initial state $q_0$.
An infinite run is accepting if it belongs to $A$, in which case we also say that it satisfies $A$.
A word $w$ is accepted if there exists an accepting run over $w$. 
We let $L(\mathbf{A}$ denote the set of accepted words and call it the language defined by $\mathbf{A},
or sometimes recognised by $\mathbf{A}.


An automaton is deterministic if for all states $q \in Q$ and letter $a \in \Sigma$, there exists at most one transition $(q,a,q') \in \Delta$.
In that case the transition relation becomes a transition function $\delta : Q \times \Sigma \to Q$.
The key property of deterministic automata is that for every word there exists exactly one run over it.


We use the same approach as for games for defining classes of automata with the same conditions:
an objective $\Omega \subseteq C^\omega$ and a colouring function $\textsf{col}: \Delta \to C$ 
induce an acceptance condition $\Omega[\textsf{col} \subseteq \Delta^\omega$.
For deterministic automata the colouring function becomes $\textsf{col}: Q \times \Sigma \to C$.
As for games the objective qualifies the automaton, so we speak of a parity automaton if it uses a parity objective.

````{prf:theorem} Omega-regular languages
:label: 1-thm:omega_regular_languages

Non-deterministic B&uuml;chi, CoB&uuml;chi, parity, and deterministic parity automata define the same class of languages called $\omega$-regular languages.

````

