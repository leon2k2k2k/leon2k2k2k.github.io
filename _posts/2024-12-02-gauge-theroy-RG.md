---
layout: post
title: RG flow of 4D gauge theory
date: 2024-12-02
description: 
tags: High energy physics, gauge theroy
categories:
---
Four dimension gauge theories are some of the most subtle parts of high energy physics. One of the things that I have been wanting to throughly understand is the famous one loop determinant calculation of the beta function for 4D gauge theory:
$$
\begin{equation}
\frac{1}{g^2(\mu)} = \frac{1}{g^2} - \frac{1}{4\pi^2}\left[
    \frac{11}{3}I(adj) - \frac{1}{3}N_sI(R_s) - \frac{4}{3}N_fI(R_f)
\right] \log(\frac{\Lambda^2_{UV}}{\mu^2}).
\end{equation}$$
We will explain this equation later on.

Its famous because overall negative sign in front of the $\frac{11}{3}$, which implies \emph{asymptotic freedom} for 4D Yang-Mills, that is, the coupling constant grows smaller and smaller at the UV(ultra-violent) energy scale. 
In 2004, Gross, Politzer, and Wilczek were awarded the Nobel prize for the computation.

The negative sign also implies the phenonemon of \emph{confinement}, that is, in the IR (infra-red), there is a scale, called the QCD scale, that the massless gluon description breaks down and it is supplanted by a different description, where gluons comes in a composite called glueballs (and if there are quarks they are combined into neutrons and protons). Even today, confinement is still not well-understood. In fact, one of its implications, the existence of mass gap, is one of the seven millenium problem in mathematics.

I am interested in understanding the computation of (1), and see if there are interesting applications for the study of smooth four-manifolds (which I hopefully will get to in another post!). This post is going to be pretty detailed, as I am a beginner in all of this. We will first explain the meaning and motivation of (1).

## What is renormalization?
The concept of renormalization in quantum field theory is simple yet profound: when we are defining a QFT, it is defined at some finite length scale. Now, when we zoom out and look at the same theory at a larger length scale, then the theory might look completely different! Even if it doesn't, the coupling constants, which measure the strength of interactions, can change. In short, coupling constants are a function of the length scale that we are interested in! More abstractly, there is a vector field, i.e. a flow, in the space of quantum field theories.

How do we actually compute it?
The idea is also quite simple, to get from a ultra-violet length scale $\Lambda_{UV}$ to a infra-red length scale  
$\Lambda_{IR}$, we need to integrate over all interactions that occurs between those length scale. 
We typically do this infinitesimally as well as perturbatively, i.e., count Feynmann diagrams by the order of the loops. 


## The engineering dimension
Starting at the zero-loop, which is also the ''classical'' level, we are simply looking at the dimension of the coupling constant. Recall the in a QFT we set $c = 1$ and $\hbar = 1$, leaving us with a single unit of dimension, which is $L = E^{-1}$. 

In our case, the dimension (in terms of length) of $\frac{1}{g^2}$ is $4-D$. This is often called the engineering dimension. This means that in our case of $D = 4$, the gauge coupling constant is classically invariant under scaling. 

However, this is not true in the quantum theory. For non-abelian gauge theories, there are loop contributions that ruins the scale invariance. Note that the abelian gauge theory is simply free.

Interesting, it is believed that for the maximally symmetric $N=4$ SYM (super Yang-Mills), the theory is expected to be conformally invariant.\footnote{Yang-Mills secretly depends on a $\tau$ parameter, where $\tau$ lives in $\mathbb{H}/SL(2,\Z)$. We will not get to that today. For $N=4$, the theory is conformally invariant for every value of $\tau$.}

The computation done in (1) is a one-loop computation, which we now turn to. 

\TODO{two things: either go to ghosts and anti-fields.}

## Renormalization at 1-loop
To do this

## I would like to complete this at a later stage, but I am moving forward right now. I am following David Tong gauge theory notes, which itself is following probably Peskin-Schroeder. Peskin-Schroeder also talks about how to do those integrals. In particular the ghost contribution is similar to problem 9.1, which is the point where I stopped.