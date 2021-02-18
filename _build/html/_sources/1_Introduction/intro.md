(1-sec:intro)=
# What is this book about?


```{math}
```

The objective of this book is to present the state of the art on games on graphs, which is part of a larger research topic called game theory.
Games on graphs is the field concerned with games whose rules and evolution are represented by a graph. We mostly focus on infinite duration games, but their study is deeply interleaved with finite duration games.
They form a prominent model in two related subjects: the first is automata theory and logic, and the second is verification and synthesis,
both of which have been very active for decades.
Some of the models were introduced and studied in neighbouring research communities such as optimisation, machine learning, model theory, and set theory.

This book does not claim to give a full account of all existing results or models in the litterature, which is close to impossible for two reasons: the wealth of existing results and the constant flow of new ones.

The primary objective in this book is algorithmic: construct efficient algorithms for analysing different types of games.
Yet the goal is not to describe their implementation in full details but rather to explain their theoretical foundations.
In this endeavour we often need to set the stage by proving properties of the corresponding games and most prominently of their winning strategies. 
So the language of this book is mathematics.

All the material presented in this book is accessible to an advanced master student or a PhD student with a background in computer science or mathematics. The goal is at the same time to present all the basic and fundamental results commonly assumed by the research community working on games on graphs, and most of the latest prominent advances.
We assume familiarity with complexity theory and the notions of graphs and automata but as much as possible do not rely on advanced results in these fields.

The book is divided in five parts each including two or three chapters. At the end of each chapter is a section dedicated to bibliographic references. This chapter (Chapter {ref}`1-chap:introduction`) introduces some notations and notions used throughout the book and Chapter {ref}`2-chap:regular` gives some fundamental results useful in most chapters. After that and to some extent each part is independent. As much as possible we avoid back references but some chapters naturally build on the previous ones in which case we clearly indicate this.

## Usual notations

We write $[i,j]$ for the interval $\set{i,i+1,\dots,j-1,j}$, and use parentheses to exclude extremal values,
so $[i,j)$ is $\set{i,i+1,\dots,j-1}$.

An alphabet $\Sigma$ is a finite set. 
We let $\Sigma^*$ denote the set of finite sequences of $\Sigma$ (also called finite words),
$\Sigma^+$ the subset of non-empty sequences, and $\Sigma^\omega$ the set of infinite sequences of $\Sigma$ (also called infinite words).
For a (finite or infinite) sequence $u = u_0 u_1 \cdots$, we let $u_i$ denote the $i$th element of $u$
and $u_{< i}$ the prefix of $u$ of length $i$, **i.e.** the finite sequence $u_0 u_1 \cdots u_{i-1}$.
Similarly $u_{\le i} = u_0 u_1 \cdots u_i$.

The length of $u$ is $|u|$.
