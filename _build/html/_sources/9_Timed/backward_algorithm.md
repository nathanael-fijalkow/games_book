(9-sec:backward_algorithm)=
# Backward Algorithm

```{math}

\renewcommand{\Game}{\game}

```

Given the DBM data structure we presented,
a backward fixpoint algorithm follows for computing the winning configurations in a timed game:

````{prf:theorem} NEEDS TITLE 9-thm:timed-control
:label: 9-thm:timed-control

   For any timed game $\mathcal{A}$ and target set $G \subseteq  V_\mathrm{Eve}$, 
   the limit $\lim_{k \rightarrow \infty} \pi^k(G)$ exists, and is reached 
   in a finite number of steps. This limit is precisely the set of states from
   which the controller has a winning strategy for reaching $G$.

````

````{admonition} Proof
:class: dropdown tip
[Sketch]

  We briefly explain why the fixpoint computation terminates and refer
  to {cite}`AMPS98,CDFLL05` for more details.  The proof relies on the notion of
  **regions**. Intuitively, regions are minimal zones, not
  containing any other zone. More precisely, writing $K$ for the maximal
  (absolute) integer constant appearing in the timed game, the set of regions is
  the set of zones associated with
  DBMs $(\mathord\prec_{i,j},M_{i,j})$ such that

  *  $M_{i,j}\in [-K; K]\cup\{-\infty;+\infty\}$ for all $i$ and $j$;
  *  for all $i\not=j$,
     
        *  either $M_{i,j}=-M_{j,i}$ and
      $\mathord\prec_{i,j}=\mathord\prec_{j,i}=\mathord\leq$,
         *  or $|M_{i,j}+M_{j,i}|=1$ and 
      $\mathord\prec_{i,j}=\mathord\prec_{j,i}=\mathord<$,
        *  or $(\prec_{i,j},M_{i,j})=(<,+\infty)$ and $(\prec_{j,i},M_{j,i})=(<,-K)$.

  The set of regions form a finite partition of $\mathbb{R}_{\geq 0}^{ \mathcal{C}}$.
  The main argument for the proof is that the
  image by $\pi$ of any finite union of regions is a finite union of
  regions. Since $\pi$ is non-decreasing, the sequence $\pi^k(G)$
  converges after finitely many steps.

  The fact that $\pi^k(G)$ may
  only contain winning configurations follows from our construction,
  and can be proved easily by induction on $k$.
  One can also show that for all configurations outside of $\pi^k(G)$,
  there is no strategy that is winning within $k$ steps. This follows since
  the definition of $\pi(\cdot)$ gives the actions to be played by  Adam to
  prevent  Eve from winning.
  Note that this does not necessarily yield a winning strategy for  Adam,
  since the game is not determined.

````

