(7-sec:references)=
# Bibilographic references

We will now give the references for this chapter, split into a few paragraphs, each corresponding to a section in the chapter.

John von Neumanns work on matrix games {cite}`vonNeumann&Morgenstern:1944` (also called normal form games), showing that they have a value and there exists optimal stationary strategies, is typically considered the founding work in game theory. Besides that paper, Dantzig {cite}`Dantzig:1965` showed the equivalence to linear programming, and thus that they can be solved in polynomial time using e.g. Khachiyan's {cite}`Kha:1979` work on the ellipsoid method.
There are also some results on how complex the strategies for matrix games are: For any $\epsilon>0$, there exists an $\epsilon$-optimal strategy that plays uniformly over a multi-set of actions of size $\lceil (\ln n)/\epsilon^2\rceil$ as shown by Lipton and Young {cite}`Lipton&Young:1994` (this is a stronger requirement than patience).
Also, as shown by Feder, Nazerzadeh and Saberi {cite}`FNS:2007` there exists games such that any $\epsilon$-optimal strategy has support at least $\Omega(\frac{\log n}{\epsilon^2})$ (note that if, for some $x$, the support is $\Omega(x)$ then patience is also $\Omega(x)$).
Finally,  as shown by Hansen, Ibsen-Jensen, Podolskii and Tsigaridas {cite}`HIPT:2013`, there is an optimal strategy in any matrix game with patience less than $(n+2)^{\frac{n+2}{2}}/2^{n+1}$ and for each $k$ there exists games with $n=m=2^k$ such that any optimal strategy has patience at least $n^{n/2}/2^{n(1+o(1))}$ (there are also results for $m$ and $n$ not equal to $2^k$ for some $k$, but not quite as tight to the upper bound).

Shapley {cite}`Sha:1953` first considered concurrent games and focused on the class of concurrent discounted games. For these, he showed that they have a value and that there are optimal stationary strategies, using in essence the proof we used for the first 3 items of Lemma {prf:ref}`cor:long`.
The proof of the fourth item, i.e. that the value can be approximated in PPAD, comes from the work of Etessami  and Yannakakis {cite}`EY:2007`. The proof of the fifth item, an upper bound on the patience of $\epsilon$-optimal strategies appears in {cite}`ibsenjensen:2012`.

Everett {cite}`Everett:1957` was the first to consider concurrent reachability games (formally, he considered a slight generalization).
In that paper, he showed that the games have a value and $\epsilon$-optimal stationary strategies (i.e. the first part of Lemma {prf:ref}`lemm:reach_determined` and Lemma {prf:ref}`lemm:reach_class`). He also used the snowball game to show that Eve does not always have an optimal strategy (i.e. Lemma {prf:ref}`lemm:no_opt_reach`).
Finally, he introduced the notion of patience for strategies.
It was shown by Himmelberg, Parthasarathy, Raghavan and Vleck {cite}`Parthasarathy:1973,HPRV:1976` that Adam has an optimal strategy.
Frederiksen and Miltersen {cite}`FM:2013` showed that for each vertex $x$ and action $a$ (except for one action for each vertex), there is a number $c_{x,a}$ and an integer $d_{x,a}$, such that 
for any $\epsilon>0$, the strategy that plays each action $a'$ in vertex $x'$ with pr. $c_{x',a'} \epsilon^{d_{x',a'}}$ is $\epsilon$-optimal (the last action in each vertex is played with the remaining pr.).
They used that to show that approximating the value (since the value can be irrational, it seems reasonable to approximate) can be done in TFNP[NP], slightly inside PSPACE.
Finding the set of vertices of value 0, i.e. Lemma {prf:ref}`lemm:find_0_reach`, is folklore.
Finding the set of vertices of value 1, on the other hand, i.e. Lemma {prf:ref}`lemm:find_1_reach`, is by deAlfaro, Henzinger and Kupferman {cite}`dAHK:1998` (their proof is different).
Hansen, Kouck&yacute; and Miltersen {cite}`Hansen&Koucky&Miltersen:2009` showed that purgatory $k$ requires patience $\epsilon^{2^{k-1}}$ for any $1>\epsilon>0$ for Eve. 
Later, Chatterjee, Hansen and Ibsen-Jensen {cite}`HIC:2017` showed that purgatory duel $k$ requires patience $(3/4)^{2^{k-1}}$ for any $0\leq \epsilon<1/4$ for either player.

Gillette {cite}`Gil:1957` was the first to consider concurrent mean-payoff games and introduced the Big Match game we use as an example. He showed that the Big Match does not have stationary strategies ensuring more than $0$. 
Later, Blackwell and Ferguson {cite}`BF:1968` showed that the Big Match have a value and that value is $1/2$ by showing that some strategies that depends on the full history is $\epsilon$-optimal. They also showed that no optimal Markov strategy (i.e. Lemma {prf:ref}`lemm:no_markov_meanpayoff`) can ensure more than $0$ in that game.
Next, Kohlberg {cite}`Kohlberg:1974` extended this to show that all repeated games with absorbing states have a value.
Finally, Mertens and Neyman {cite}`MN:1981` showed that all concurrent mean-payoff games have a value (i.e the first part of Lemma {prf:ref}`lemm:class_meanpayoff`).
The strategies employed in all these papers kept track on the sum of over the rounds of the values of the vertex in that round minus the color in that round (the strategy by Mertens and Neyman set the memory to 0 if it should have been negative though).
Finding the set of vertices where for every $\epsilon>0$, a finite memory strategy can ensure value $1-\epsilon$ was done by Chatterjee and Ibsen-Jensen {cite}`CI:2015` (the middle part of Lemma {prf:ref}`lemm:class_meanpayoff`).
Futheremore, finding the values in a game with a fixed number of vertices in polynomial time was done by Hansen, Kouck&yacute;, Lauritzen, Miltersen and Tsigaridas {cite}`HKLMT:2011`, informally speaking by doing binary search for the values.
That finite-memory strategies cannot ensure more than $0$ in the Big Match, i.e. Lemma {prf:ref}`lemm:no_finite_meanpayoff` seems to be folklore.
Hansen, Ibsen-Jensen and Kouck&yacute; {cite}`HIK:2016` considered extending Markov strategies with a finite amount of space and showed that if the memory is a deterministic function of the history, then no such strategy can ensure more than $-1$ in the Big Match. They also showed, for any fixed $\epsilon>0$, that in round $T$ one only needs $O(\log \log T)$ bits of memory to play $\epsilon$-optimal in any absorbing game.
Finally, Hansen, Ibsen-Jensen and Neyman {cite}`HIN:2018` showed that Markov strategies extended with a single bit of space suffice to play the Big Match $\epsilon$-optimally, for any $\epsilon>0$ (naturally, the strategy used randomisation to update the memory state).

```{bibliography}
:style: unsrtalpha
:filter: cited and chap == "7"
```