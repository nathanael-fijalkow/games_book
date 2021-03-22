(5-sec:references)=
# Bibliographic references

There is a broad field of study related to Markov decision processes, with a history going as far as  1950's {cite}`Bellman:1957`. It is beyond the scope of this chapter to provide a comprehensive overview of the related literature. Nonetheless, in this section we provide pointers to the most significant works connected to our techniques as well as to works that can serve as a starting point for a further study.

One of the most widely used references for MDP-related research is the textbook by Puterman {cite}`Puterman:2005`. The textbook views MDPs from an operations research point-of-view, focusing on finite-horizon, discounted, total-reward, and average reward (an alternative name for mean-payoff) objectives. Regular objectives fall outside of the book's focus, though reachability can be viewed as a special case of the `positive bounded total reward' objectives studied in the book. An in-depth study of the textbook will impart to its reader the knowledge of many useful techniques for MDP analysis, though a reader who is a newcomer to MDPs might feel somewhat intimidated by its sheer volume and generality. In this chapter, we follow Puterman's exposition mainly in the discounted payoff, albeit in a rather condensed form. 

For mean-payoff MDPs, {cite}`Puterman:2005` follows similar blueprint as in the discounted case: first characterizing the optimal values via a suitable optimality equation and then deriving the value iteration, strategy improvement, and linear programming methods from this characterization. We use the linear programming as our foundational stone, focusing on the relationship between strategies and feasible solutions of the program. We note that value and strategy iteration for mean-payoff MDPs come with super-polynomial lower bounds, see, e.g. {cite}`Fearnley:2010,Fearnley:2010b`, or {cite}`Puterman:2005`, where it is shown that strategy improvement converges at least as fast as value iteration.

Also, {cite}`Puterman:2005` makes the initial analysis of mean-payoff MDPs in the context of **unichain** MDPs, and then extends to arbitrary MDPs, with strongly connected MDPs treated as a special case of the latter. While unichain is an important theoretical concept, in the context of formal methods and automata it is preferable to work with strongly connected MDPs. We also note that all the results in the mean-payoff sections hold also for $\mathtt{MeanPayoff}^{\;+}$. Almost all of the proofs are the same, with an important exception of {prf:ref}`5-cor:mp-value-bound`, where Fatou's lemma cannot be used to prove that $\textsf{p-Payoff}( v_0,\sigma) \leq  \textsf{s-Payoff}( v_0,\sigma)$. Instead, we could use **martingale techniques** here. Martingales are an important concept in probability theory {cite}`Williams:1991`, with applications e.g. in analysis of infinite-state MDPs and stochastic games {cite}`Brazdil&Brozek&Etessami&Kucera:2011`. We can use martingales to strengthen {prf:ref}`5-lem:dual-bound-step` by showing that the probability  of $\sum_{i=0}^{n-1} c( \pi_i) \geq \sqrt{n}\cdot  \mathbb{E}^\sigma_{ v_0}[\sum_{i=0}^{n-1} c( \pi_i)]$ converges (with an exponential rate of decay) to $0$ as $n\rightarrow \infty$, which allows us to prove the required bound for $\limsup$.

 The notion of a (M)EC as well as many techniques we use in the EC section are due to de Alfaro, whose thesis {cite}`dA:1997` details the evolution of the concept and its relation to similar notions. The algorithm for MEC decomposition is taken from {cite}`Chatterjee&Henzinger:2011`, where more advanced algorithms as well as use of MECs in parity MDPs are discussed.

For an overview of literature related to verification of temporal properties in MDPs, we refer the reader to the monograph {cite}`Baier&Katoen:2008`.

MDPs are also used as a prime model in reinforcement learning (RL), one of the classical yet rapidly evolving sub-fields of AI. For RL-centric view of MDPs, we point the reader towards the textbooks {cite}`Sutton&Barto:2018,Bertsekas:2017`.


```{bibliography}
:style: unsrtalpha
:filter: cited and chap == "5"
```