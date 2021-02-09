(1-sec:references)=
# Bibliographic references

The study of games, usually called game theory, has a very long history rooted in mathematics, logic, and economics, among other fields.
Foundational ideas and notions emerged from set theory with for instance backward induction by Zermelo {cite}`Zermelo:1913`, 
and topology with determinacy results by Martin {cite}`Martin:1975` (stated as  {ref}`Theorem <1-thm:borel_determinacy>` in this chapter),
and Banach-Mazur and Gale-Stewart games {cite}`Gale&Stewart:1953`.

The topic of this book is a small part of game theory: we focus on infinite duration games played on graphs.
In this chapter we defined deterministic games, meaning games with no source of randomness, which will be the focus of Part {ref}`part:classic`.
Part {ref}`part:stochastic` introduces stochastic games, which were initially studied in mathematics.
We refer to {ref}`Section <6-sec:references>` for more bibliographic references on stochastic games,
and focus in this chapter on references for deterministic games.

The model presented in this chapter emerged from the study of automata theory and logic, where it is used as a tool for various purposes.
Let us first discuss the role of games in two contexts: 
for solving the synthesis problem of reactive systems and for automata and logic over infinite trees.


The synthesis problem for non-terminating reactive systems, sometimes called Church's problem, 
was formulated in general terms by Church {cite}`Church:1957,Church:1962`:
from a specification of a step-by step transformation of an input stream given in some logical formalism, 
construct a system satisfying the specification.
The first published paper solving Church's problem for monadic second-order logic was written by B&uuml;chi and Landweber {cite}`Buchi&Landweber:1969`, following a paper by Landweber {cite}`Landweber:1967` (then B&uuml;chi's PhD student) focussing on solving games.
However, the idea of casting the synthesis problem as a game between a system and its environment is due to McNaughton:
in the technical report {cite}`McNaughton:1965` McNaughton attempted to give a solution to the synthesis problem using games, initiating many of the most important ideas for analysing games. 
Unfortunately the proof contained an error which Landweber detected and communicated to McNaughton,
who then decided to let Landweber publish his complete solution.
One of the most difficult step in the solution of Church's problem for monadic second-order logic by B&uuml;chi and Landweber {cite}`Buchi&Landweber:1969` is the determinisation procedure from B&uuml;chi to Muller automata due to McNaughton {cite}`McNaughton:1966`.
We refer to Thomas' survey {cite}`Thomas:2009` for more details on some historical and technical aspects of the early papers on Church's synthesis problem.


Games emerged in another aspect of automata theory: for understanding the difficult result of Rabin {cite}`Rabin:1969` saying that automata over infinite trees can be effectively complemented. 
This is the key step for proving Rabin's seminal result that the monadic second-order theory of the infinite binary tree is decidable.
The celebrated paper of Gurevich and Harrington {cite}`Gurevich&Harrington:1982` revisits Rabin's result by reducing the complementation question to a determinacy result for games. Interestingly, they credit McNaughton for airing the idea of using games in this context and then for exploiting it to Landweber {cite}`Landweber:1967`, B&uuml;chi and Landweber {cite}`Buchi&Landweber:1969`, and B&uuml;chi {cite}`Buchi:1977`.


Both lines of work have been highly influential in automata theory and logic;
we refer to the reference section in {ref}`Chapter <2-chap:regular>` for more bibliographic references on this connection.
They bind automata theory and logic to the study of games on graphs and provide motivations and questions many of which are still open today.


Beyond these two examples there are many applications of games in theoretical computer science and logic in particular.
The following quote is due to Hodges {cite}`Hodges:1993`:

> An extraordinary number of basic ideas in model theory can be expressed in terms of games.

Let us mention model checking games, which are used for checking whether a model satisfies a formula.
They often form both a theoretical tool for understanding the model checking problem and proving its properties, as well as an algorithmic backend for effectively deciding properties of a logical formalism (we refer to {cite}`Graedel:2002` for a survey on model checking games).
Another important construction of a game for understanding logical properties is the Ehrenfeucht-Fra&iuml;ss&eacute; games {cite}`Ehrenfeucht:1961,Fraissé:1950,Fraissé:1953` whose goal is to determine whether two models are equivalent against a logical formalism.



```{bibliography}
:style: unsrtalpha
```