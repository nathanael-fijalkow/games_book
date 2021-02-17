(11-sec:references)=
# Bibliographic references

```{math}
\newcommand{\?}{\mathcal}
\newcommand{\+}{\mathbb}
\newcommand{\tup}[1]{\langle #1\rangle}
\newcommand{\eqby}[1]{\stackrel{\!\,\!\,\raisebox{-.15ex}{\scalebox{.5}{\textrm{#1}}}}{=}}
\newcommand{\eqdef}{\eqby{def}}
\newcommand{\Loc}{\?L}
\newcommand{\Act}{A}
\providecommand{\dom}[1]{\mathrm{dom}\,#1}
\newcommand\pto{\mathrel{\ooalign{\hfil$\mapstochar\mkern5mu$\hfil\cr$\to$\cr}}}
\newcommand{\weight}{w}
\newcommand{\loc}{\ell}
\newcommand{\sink}{\bot}
\newcommand{\dd}{k}
\newcommand{\CounterReach}{\textsf{CounterReach}\xspace}
\newcommand{\Cover}{\textsf{Cover}\xspace}
\newcommand{\NonTerm}{\textsf{NonTerm}\xspace}
\newcommand{\decpb}[3][]{\begin{problem}[#1]\\[-1.7em]\begin{description}     
    \item[\textsc{input:}] {#2}
    \item[\textsc{question:}] {#3}
    \end{description}
  \end{problem}}
\newcommand{\step}[1]{\xrightarrow{\,\raisebox{-1pt}[0pt][0pt]{\scriptsize\ensuremath
      {#1}}\,}}
\newcommand{\mstep}[1]{\xrightarrow{\,\raisebox{-1pt}[6pt][0pt]{\scriptsize\ensuremath
      {#1}}\,}}
\newcommand{\inst}[1]{\mathrel{\mathtt{#1}}}
\providecommand{\pop}{\mathrm{pop}}
\providecommand{\push}[1]{\mathrm{push}(#1)}
\providecommand{\mymoot}[1]{}
\newcommand{\blank}{\Box}
\newcommand{\emkl}{\triangleright}
\newcommand{\emkr}{\triangleleft}
\renewcommand{\natural}{\arena_\+N}
\newcommand{\energy}{\arena_\+E}
\newcommand{\bounded}{\arena_B}
\newcommand{\capped}{\arena_C}
\newcommand{\capp}[2][C]{\overline{\vec #2}^{#1}}
\let\oldcite\cite
\renewcommand{\cite}{\citep}
\providecommand{\citep}{\oldcite}
\providecommand{\citet}{\cite}
\providecommand{\citem}[2][1]{#1 {cite}`#2`}
\providecommand{\qedhere}{\ensuremath\Box}
\providecommand{\col}{\mathfrak c}
\newcommand{\lcol}{\mathrm{lcol}}
\newcommand{\vcol}{\mathrm{vcol}}
\newcommand{\litt}{\loc}
\newcommand{\Effect}{\Delta}

\newcommand{\Eve}{\textrm{Eve}}
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
> **Vector Addition Systems with States**

In their one-player version, i.e.\ in "vector addition systems with
states", all the games presented in \cref{11-counters} are decidable.
With given initial credit, configuration reachability is simply
called `reachability' and was first shown decidable by
\citem[Mayr]{Mayr:1981} (with simpler proofs
in {cite}`Kosaraju:1982,Lambert:1992,Leroux:2011`) and recently shown
to be of non-elementary complexity {cite}`Czerwinski&Lasota&Lazic&Leroux&Mazowiecki:2019`.  Coverability and
non-termination are considerably easier, as they are
\EXPSPACE-complete {cite}`Lipton:1976,Rackoff:1978` and so is
parity@parity vector game {cite}`Habermehl:1997`.  With "existential
initial credit, the problems are markedly simpler: configuration
reachability becomes \EXPSPACE-complete, while coverability" is in
\NL\ and non-termination and parity can be solved in polynomial
time by~\cref{11-thm-zcycle} using linear programming
techniques {cite}`Kosaraju&Sullivan:1988`.

> **Undecidability of Vector Games**

The undecidability results of Subsection {ref}`11-subsec:undec` are folklore.  One
can find undecidability proofs
in {cite}`Abdulla&Bouajjani&dOrso:2003,Raskin&Samuelides&VanBegin:2005`;
non-termination was called `deadlock-freedom' by \citem[Raskin et
al.]{Raskin&Samuelides&VanBegin:2005}. Configuration reachability is
undecidable even in very restricted cases, like the robot games
of~\citet{Niskanen&Potapov&Reichert:2016}.

> **Succinct One-Counter Games**

One-dimensional vector systems are often called **one-counter
nets** in the literature, by contrast with **one-counter automata**
where zero tests are allowed.  The \EXPSPACE-completeness of "succinct
one-counter games was shown by~\citem[Hunter]{Hunter:2015}.  Countdown games"
were originally defined with given initial credit and a "zero
reachability" objective, and shown
\EXP-complete in {cite}`Jurdzinski&Laroussinie&Sproston:2008`; see also
\citet{Kiefer:2013} for a variant called hit-or-run games.  The
hardness proofs for \cref{11-countdown-given,12-countdown-exist} are
adapted from~\citet{Jancar&Osicka&Sawa:2018}, where countdown games
with existential initial credit were first introduced.

> **Asymmetric Vector Games**

The asymmetric vector games of \cref{11-avag} appear
under many guises in the litterature: as `and-branching' "vector
addition systems with states"
in {cite}`Lincoln&Mitchell&Scedrov&Shankar:1992`, as `vector games'
in {cite}`Kanovich:1995`, as `B-games'
in {cite}`Raskin&Samuelides&VanBegin:2005`, as `single sided' vector
addition games in {cite}`Abdulla&al:2013`, and as `alternating'
vector addition systems with states in {cite}`Courtois&Schmitz:2014`.

The undecidability of configuration reachability shown
in Subsection {ref}`11-subsec:reach` was already proven by \citem[Lincoln et
al.]{Lincoln&Mitchell&Scedrov&Shankar:1992} and used to show the
undecidability of propositional linear logic;
\citem[Kanovich]{Kanovich:1995,Kanovich:2016} refines this result to
show the undecidability of the $(!,\oplus)$-Horn fragment of linear
logic.  Similar proof ideas are used for Boolean BI and separation
logic in {cite}`Larchey&Galmiche:2013,Brotherston&Kanovich:2014`.

> **Asymmetric Monotone Vector Games**

The notion of asymmetric infinite games over a well-quasi-ordered
arena constitutes a natural extension of the notion of
well-structured systems of
\citet{Abdulla&Cerans&Jonsson&Tsay:2000} and
\citet{Finkel&Schnoebelen:2001}, and was undertaken
in {cite}`Abdulla&Bouajjani&dOrso:2003,Raskin&Samuelides&VanBegin:2005`.
The decidability of coverability and non-termination through wqo
arguments like those of \cref{11-pareto-cov} was shown
by~\citem[Raskin et al.]{Raskin&Samuelides&VanBegin:2005}.  More
advanced wqo techniques were needed for the first decidability proof
of parity@parity vector game in {cite}`Abdulla&al:2013`.  See
also {cite}`Schmitz&Schnoebelen:2012` for more on the algorithmic uses of
wqos.

By analysing the attractor computation of Subsection {ref}`11-subsec:attr`, one can
show that {numref}`11-algo:cov` works in \kEXP[2], thus matching the
optimal upper bound from~\cref{11-avag-easy}: this can be done using
the Rackoff-style argument of \citet{Courtois&Schmitz:2014} and the
analysis of \citet{Bozzelli&Ganty:2011}, or by a direct analysis of the
attractor computation algorithm {cite}`Lazic&Schmitz:2019`.

> **Energy Games**

\AP An alternative take on energy games is to see a vector system
$\?V=(\Loc,\Act,\Loc_\mEve,\Loc_\mAdam,\dd)$ as a finite arena with
edges $\loc\step{\vec u}\loc'$ coloured by $\vec u$, thus with set of
colours $C\eqdef\+Z^\dd$.  For an initial credit $\vec v_0\in\+N^\dd$
and $1\leq i\leq\dd$, the associated energy objective is then
defined as\todoquestion{is that the right place for this?}
\begin{equation*}
  \mathsf{Energy}_{\vec v_0}(i)\eqdef\left\{\pi\in E^\omega\;\middle|\;\forall
  n\in\+N\mathbin.\left(\vec v_0(i)+\sum_{0\leq j\leq n}c(\pi)(i)\right)\geq 0\right\}\;,
\end{equation*%  or $\Omega\subseteq E^\omega$?}
that is, $\pi$ is winning if the successive sums of weights on
coordinate $i$ are always non-negative.
\AP The multi-energy objective then asks for the play $\pi$ to
belong simultaneously to $\mathsf{Energy}_{\vec v_0}(i)$ for all
$1\leq i\leq\dd$.  This is a multiobjective in the sense of the
forthcoming \cref{chap:multiobjective}.  Multi-energy games are
equivalent to non-termination games played on the arena
$\energy(\?V)$ defined by the energy semantics.
\TODO{energy games with weak or hard upper bounds, bounding games}

\TODO{references for energy games}
{cite}`Chakrabarti&deAlfaro&Henzinger&Stoelinga:2003,Bouyer&Fahrenberg&Larsen&Markey&Srba:2008`
... in {cite}`Abdulla&al:2013`, where the
relationship with energy games was also first observed.  The
equivalence with mean-payoff games in dimension~one was first
noticed by~\citem[Bouyer et
al.]{Bouyer&Fahrenberg&Larsen&Markey&Srba:2008}.  A similar connection
in the multi-dimensional case was established
in {cite}`Chatterjee&Doyen&Henzinger&Raskin:2010,Velner&al:2015` and
will be discussed in~\cref{chap:multiobjective}.

> **Complexity**

 \Cref{11-tbl-cmplx} summarises the complexity
results for asymmetric vector games.  For the upper bounds with
existential initial credit of Subsection {ref}`11-subsec:up-exist`, the existence
of counterless winning strategies for \Adam was originally shown by
\citem[Br\'azdil et al.]{Brazdil&Jancar&Kucera:2010} in the case of
non-termination games; the proof of \cref{11-counterless} is a
straightforward adaptation using
ideas from {cite}`Chatterjee&Doyen:2012` to handle "parities@parity
vector game.  An alternative proof through bounding games" is
presented in {cite}`Colcombet&Jurdzinski&Lazic&Schmitz:2017`.

The \coNP\ upper of \cref{11-exist-easy} was shown soon after
Br\'azdil et al.'s work by
\citem[Chatterjee et al.]{Chatterjee&Doyen&Henzinger&Raskin:2010} in
the case of non-termination games.  The extension of
\cref{11-exist-easy} to parity@parity vector game was shown
by {cite}`Chatterjee&Randour&Raskin:2014` by a reduction from
parity@parity vector games to non-termination games somewhat
reminiscent of \cref{?}.  The proof of
\cref{11-exist-easy} takes a slightly different approach using
\cref{11-lem-zcycle} for finding non-negative cycles, which is a
trivial adaptation of a result by \citem[Kosaraju and
Sullivan]{Kosaraju&Sullivan:1988}.  The pseudo-polynomial bound
of~\cref{11-exist-pseudop} is taken
from {cite}`Colcombet&Jurdzinski&Lazic&Schmitz:2017`.

For the upper bounds with given initial credit of
Subsection {ref}`11-subsec:up-given`, regarding coverability, the \kEXP[2] upper
bound of \cref{11-avag-easy} was first shown by~\citem[Courtois and
Schmitz]{Courtois&Schmitz:2014} by adapting Rackoff's technique for
vector addition systems with states {cite}`Rackoff:1978`.  Regarding
non-termination, the first complexity upper bounds were shown
by~\citem[Br\'azdil et al.]{Brazdil&Jancar&Kucera:2010} and were
in \kEXP, thus non-elementary in the size of the input.  Very
roughly, \todo{This is a leftover from a previous write-up}
their argument went as follows: one can extract a pseudo-polynomial
existential Pareto bound $B$ in the one-player case from the proof
of \cref{11-thm-zcycle}, from which the proof of \cref{11-counterless}
yields a $2^{|\Act|}(B+|\Loc|)$ existential Pareto bound in the
two-player case, and finally by arguments similar to \cref{?} a tower
of $\dd$ exponentials on the given initial credit problem.  The
two-dimensional case with a unary encoding was shown a bit later to be
in~\P\ by~\citem[Chaloupka]{Chaloupka:2013}.  Finally, a
matching \kEXP[2] upper bound (and pseudo-polynomial in any fixed
dimension) was obtained by~\citem[Jurdzi\'nski et
al.]{Jurdzinski&Lazic&Schmitz:2015}.  Regarding "parity@parity vector
game", \citem[Jan\v{c}ar]{Jancar:2015} showed how to obtain
non-elementary upper bounds by reducing to the case
of~\citet{Brazdil&Jancar&Kucera:2010}, before a tight \kEXP[2] upper
bound (and pseudo-polynomial in fixed dimension with a fixed number of
priorities) was shown
in {cite}`Colcombet&Jurdzinski&Lazic&Schmitz:2017`.

The \coNP\ hardness with existential initial credit in
\cref{11-exist-hard} originates from
\citet{Chatterjee&Doyen&Henzinger&Raskin:2010}.  The \kEXP[2]-hardness
of both coverability and non-termination games with "given initial
credit" from \cref{11-avag-hard} was shown
in {cite}`Courtois&Schmitz:2014` by adapting Lipton's construction for
vector addition systems with states {cite}`Lipton:1976`; similar
proofs can be found for instance
in {cite}`Demri&Jurdzinski&Lachish&Lazic:2012,Berard&Haddad&Sassolas&Sznajder:2012`.
The hardness for \EXP-hardness in dimension two was first shown by
{cite}`Fahrenberg&Juhl&Larsen&Srba:2011`; the direct proof in
\cref{11-avag-two} by a reduction from countdown games was suggested
by~\citet{Mazowiecki&Perez:2017}.

The $\NP\cap\coNP$ upper bounds in dimension~one from
Subsection {ref}`11-subsec:mono-dim1` are due to \citem[Bouyer et
al.]{Bouyer&Fahrenberg&Larsen&Markey&Srba:2008} for "given
initial credit" and \citem[Chatterjee
and Doyen]{Chatterjee&Doyen:2012} for existential initial credit.

> **Some Applications**

Besides their many algorithmic applications for solving various types
of games, vector games have been employed in several fields to prove
decidability and complexity results, for instance for linear,
relevance, or separation
logics {cite}`Lincoln&Mitchell&Scedrov&Shankar:1992,Kanovich:1995,Urquhart:1999,Larchey&Galmiche:2013,Brotherston&Kanovich:2014,Kanovich:2016`,
resource-bounded logics {cite}`Alechina&al:2018`, simulation and
bisimulation
problems {cite}`Kiefer:2013,Abdulla&al:2013,Courtois&Schmitz:2014,Jancar&Osicka&Sawa:2018`,
orchestration synthesis {cite}`DeGiacomo&Vardi&Felli&Alechina&Logan:2018`,
and model-checking probabilistic timed
automata {cite}`Jurdzinski&Laroussinie&Sproston:2008`.

\input{tab-cmplx}

```{bibliography}
:style: unsrtalpha
:filter: cited and chap == "11"
```