(8-chap:signal)=
# Games with Signals

```{image} ./../Illustrations/8.jpg
:alt: illustration
:class: bg-primary mb-1
:width: 400px
:align: center
```

```{math}
```


Written by Hugo Gimbert



> **Imperfect information.**

This chapter presents a few results about zero-sum games with imperfect information.
Those games are a generalization of concurrent games in order to take into account the possibility that players might be imperfectly informed about the current state of the game
and the actions taken by their opponent, or even their own action. We will also discuss situations where players may forget what they used to know.

Before providing formal definitions of games with imperfect information,
we give three examples.

> **Simple poker.**


%Chris Ferguson, Bright Trading, Westwood, California Thomas S. Ferguson, University of California, Los Angeles
Our first example is a finite duration game which is a simplified version of poker,
inspired by Borel and von Neumann simplified poker {cite}`ferguson`.
This game is played with  $4$ cards $\{\spadesuit,\heartsuit,\clubsuit,\diamondsuit\}$.

*  The goal of Eve and Adam is to win
the content of a pot in which, initially, they both put $1$ euro.
*  Eve receives a private random card, unknown by Adam.
*  Eve decides whether to check or raise.
If she checks then she wins the pot iff her card is $\spadesuit$.
*  If Eve raises then Adam has two options: fold
or call. If Adam folds then Eve receives the pot.
If Adam raises then both player add two euros in the pot
and Eve wins the pot iff her card is $\spadesuit$.

A natural strategy for Eve is to raise when she has a spade and otherwise
check. Playing so, she reveals her card to Adam,
and we will see that the optimal behaviour for her
consists in bluffing from time to time,
i.e. raise although her card is not a spade.

> **The distracted logician.**

Our second example is another finite duration game.
A logician is driving home. For that he should go through two crossings,
and turn left at the first one and right at the second one.
This logician is very much absorbed in his thoughts,
trying to prove that $P\neq NP$,
and is thus pretty distracted: upon taking a decision, he cannot  tell
whether he already saw a crossing or not.

This simple example is useful to discuss the observability of actions
and make a distinction between
mixed strategies and behavioral strategy.
 
> **Network controller.**

The following example is inspired from collision regulation
in ethernet protocols: the controller of a network card
has to share an ethernet layer with
another network card, controller by another controller,
possibly malicious.

When sending a data packet,
the controller selects a delay in microseconds between $1$ and $512$
and transmits this delay to the network card.
The other controller does the same.
The network cards try to send their data packet at the chosen dates.
Choosing the same date results in a data collision, and the process is repeated until
there is no collision, at that time the data can be sent.

The chosen delay has to be kept hidden from the opponent.
This way, it can be chosen randomly,
which ensures that the data will eventually be sent with probability $1$,
whatever does the opponent.
  
> **Guess my set.**

Our third example is an infinite duration game,
parametrized by some integer $n$.
The play is
divided into three phases.

*  In the first phase, Eve secretly chooses a subset
$X \subsetneq \{1, \ldots,2n\}$ of size $n$
among the $\binom{2n}{n}$ possibilities.
*  In the second phase, Eve discloses to Adam
$\frac{1}{2}\binom{2n}{n}$ pairwise distinct sets of size
$n$ which are all different from $X$. 
*  In the third phase, Adam aims at guessing $X$ by trying up to
$\frac{1}{2} \binom{2n}{n}$ sets of size $n$. 
If Adam succeeds in guessing $X$,
the game restarts from the beginning. Otherwise, 
Eve wins.

Clearly Adam has a strategy to prevent forever
Eve to win: try up one by one all those sets
that were not disclosed by Eve.
This strategy uses a lot of memory:
Adam has to remember the whole sequence of $\frac{1}{2} \binom{2n}{n}$
 sets disclosed by Eve.
We will see that a variant of this game can be represented 
in a compact way, using a number of states polynomial in $n$.
As a consequence, playing optimally a game with imperfect-information and infinite duration
might require a memory of size doubly-exponential in the size of the game.









