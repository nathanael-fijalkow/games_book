(2-chap:regular)=
# Regular Games

```{image} ./../Illustrations/2.jpg
:alt: illustration
:class: bg-primary mb-1
:width: 400px
:align: center
```


Written by Nathana&euml;l Fijalkow, Florian Horn



This chapter considers the so-called regular games, which from the easiest to the most complicated are: reachability, B&uuml;chi,
parity, Rabin, and then Muller games.
We develop in Section {ref}`2-sec:attractors` the notion of attractors for solving reachability games. 
This is the main building block for constructing algorithms throughout the book.
The next step is B&uuml;chi games in Section {ref}`2-sec:buchi`. 
We then construct a conceptually simple exponential time recursive algorithm for solving parity games in Section {ref}`2-sec:parity`.
We extend the algorithm to Muller games in Section {ref}`2-sec:muller`, and discuss the computational complexities of solving Rabin, Streett, and Muller games.
Finally, Section {ref}`2-sec:zielonka` is devoted to the combinatorial notion of the Zielonka tree, 
which beautifully explains the memory requirements for Muller games and gives additional insights into the structures of Rabin and parity objectives.

````{prf:remark} Finite versus infinite games
:label: 2-rmk:finite_vs_infinite

As in the rest of the book unless otherwise specified we consider finite games.
However all positionality and finite memory determinacy results proved in this chapter hold for infinite games.
In all cases the proofs we give use the finiteness of the games.
However in all cases ({prf:ref}`2-thm:characterisation_Zielonka_tree`, {prf:ref}`2-thm:muller`, {prf:ref}`2-thm:parity`, {prf:ref}`2-thm:Buchi`, and {prf:ref}`2-thm:characterisation_Zielonka_tree`) 
but one ({prf:ref}`2-thm:Rabin_positional_determinacy`),
the proofs can be extended to infinite games with a technical overhead involving in particular a transfinite induction.
The difficulty is illustrated before the proof of {prf:ref}`2-thm:reachability`.

````













