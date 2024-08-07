---
layout: post
title: Various Eisenstein series
date: 2024-07-13
description: Eisenstein series I
tags: mathematics, modular forms
categories:
---
For the first series of post I want to talk about real-analytic Eisenstein series and their vector-valued generalization. The motivation is to understand the ensemble average/3D quantum gravity aspects of [this paper](https://arxiv.org/abs/2311.00699), which has been on my bucket list for while now.

Here's a rough list of topics:
1. Various Eisenstein series.
3. Representation theoretic definition of Eisenstein series and continuous spectrum of automorphic forms. 
4. Siegel-Weil formulas.
4. Vector-valued generalizations.

Other things to write about: Hecke operators.


In this post we will review all the different type of Eisenstein series, from the simplest holomorphic Eisenstein series all the way up to weight $k$ real-analytic Eisenstein series. Much of it is from [here](https://math.berkeley.edu/~btw/small-eisenstein.pdf)


In this post we will take our time to review through various version of Eisenstein series. Here's the summarization:

1. Holomorphic Eisenstein seires $$E_k(\tau)$$: 
labeled by $$k \in 2\mathbb{N}$$, this is holomorphic, transforms as weight $k$ modular form under the $$Mp_2(\mathbb{Z})$$ transform, and holomorphic in $$\infty$$.
1. Real-analytic Eisenstein series $$E(\tau, s)$$:
they are labeled by $s$ in the upper complex plane (???), real-analytic, transform as weight $0$ under $$Mp_2(\mathbb{Z})$$, and are Eigenvalues of the Laplacian 
\begin{equation}
\Delta = -y^2(\partial_x^2 + \partial_y^2)
\end{equation}
with eigenvalue $$s(1-s)$$. For  $$s = \frac{1}{2} + it$$ family they show up in the spectral theory of modular function, as they are the continuous series. 
1. Weight $$k$$ real-analytic Eisenstein series $$E_k(s, \tau)$$: This is the combination of the two above. They are harmonic weak Maass forms, satisfies the weight $$k$$ Laplacian equation 
\begin{equation}
\Delta_k = -y^2(\partial_x^2 + \partial_y^2)+ iky(\partial_x + i \partial_y)
\end{equation}
QUESTION: what about the spectral theory of here? do we still use $$s = \frac{1}{2}+it$$?

## Holomorphic Eisenstein series
Recall the group $$\SLZ$$ as well as its double cover $$\MpZ$$. Basically $$\MpZ$$ allows us to take square root of $$c \tau + d$$.  -->
There is a canonical action of $$\SLZ$$ on the upper half plane,
which has coordinate $$\tau$$. $$\MpZ$$ has generators $$S$$ and $$T$$, with $$T$$ generates the subgroup $$\Gamma_{\infty}$$ which is the fixed point of $$y = \Im(\tau)$$.

For $$M = \begin{pmatrix}a & b \\ c & d \end{pmatrix}$$, we have this important equation:
\begin{equation}\label{eq:imaginary-under-M}
\Im(M\tau) = 
 \Im(\frac{a \tau + b}{c \tau + d}) = \frac{\Im{(a \tau + b)(c \bar{\tau} + d)}}{|c\tau + d|^2} = \frac{\Im(ad \tau + bc \bar{\tau})}{|c\tau + d|^2} = 
\frac{\Im(\tau)}{|c\tau + d|^2}
\end{equation}
From 

Let us first recall the definition of a modular form: 

**Definition:** Let $$k$$ be an half integer. A modular form of weight $$k$$ is a holomorphic function: $$\mbb{H} \to \mbb{C}$$ satisfying the following:
1. $$f$$ transforms under the action of $\MPZ$ by   
   \begin{equation}
    f(M \cdot \tau)  = (c \tau + d)^k f(\tau).
   \end{equation}
2. $$f$$ is holomorphic at $$\infty$$. That is, let $$q = e^{2\pi i \tau}$$. Consider the Fourier expansion 
    \begin{equation}
    f(\tau) = \sum a_n q^n,
    \end{equation}
$$f$$ is holomorphic at $$\infty$$ if all coefficients $$a_n$$ are zero for $$n < 0$$. 

Such a holomorphic form is a **cusp** form if $$a_0 = 0$$.
Note that condition (1) above is equivalent to 
\begin{equation}
f(\tau + 1) = f(\tau), \quad f(-1/\tau) = \tau^k f(\tau).
\end{equation}
One can show that for all $$k$$, the space of weight $$k$$ modular forms is finite dimensional. With the first non-trivial one at $$k = 4$$, where it is one-dimensional spanned by the Eisenstein series $$E_2$$, which we will now define.

<b>Definition:</b> 
Let $$k$$ be an integer, then the Eisenstein series $$E_k(\tau)$$ is defined as 
\begin{equation}
E_k(\tau) = \sum_{c, d \in \mbb{Z}^2-(0,0)} \frac{1}{(m + n \tau)^{2k}}
\end{equation}
This sum converges absolutely when $k \geq 2$. It is straightfoward to see that for $$k \geq 2$$, $$E_k(\tau)$$ is a modular form with weight $$k$$.


<b>Example:</b>

$$E_4(\tau) = 1 + 240 \sum_{n=1}^{\infty} \frac{n^3q^n}{1-q^n}, \quad E_4^2 = E_8$$.

## Real-analytic Eisenstein series
Now we move onto real-analytic Eisenstein series. They are **Maass forms**, which are real-analytic generalization of modular functions (i.e. modular functions of weight $$0$$).

<b>Definition:</b> A complex-valued smooth function $$f \colon \mbb{H} \to \mbb{C}$$ is a **Maass form**  if 
1. We have
   \begin{equation}
   f(M \cdot \tau) = f(\tau).
   \end{equation}
2. $$f$$ is an eigenfunction of the hyperbolic Laplacian:
   \begin{equation} \Delta_k = -y^2 (\partial_x^2 + \partial_y^2 )
   .\end{equation}
3. $$f$$ has moderate growth at the cusp, i.e., there exists $$N$$ such that $$f(\tau) =O(y^N)$$ as $$y \to \infty$$.

We call $$f$$ **weak Maass form** if it satifies (1) and (2) above, and the following growth condition:

3'. $$f$$ have at most linear exponential growth at the cusp, i.e., exists $$C> 0$$ such that $$f(\tau) = O(e^{Cy})$$ as $$y \to \infty$$.

More generally, when we are dealing with cases where there are more than one cusp, for example working with higher level $$N$$, we are going to have growth condition on all cusps.

The idea of real-analytic Eisenstein series is simple: if you want a modular function, you can sum up $$\MpZ$$ images of a function $$f$$. However, we can do something a bit smarter, take the function $$y^{s}$$, it is automatically invariant under $$T$$ transforms, therefore we just need to sum up its image under $$\Gamma_{\infty}\backslash\MpZ$$, which is in correspondence with pairs of integers $c,d$ with the $(c,d) = 1$. 

<b>Definition:</b> 
Fix $$s \in \mbb{C}$$, then 
\begin{equation}
E_s(\tau) = \sum_{\gamma \in \Gamma_{\infty}\\backslash \MpZ}\frac{1}{2|c\tau + d|^{-2s}} = \sum_{c \geq 0, (c,d) = 1} y^s|_{\gamma}
\end{equation}
Note that we avoided doubling by setting $$c \geq 0$$. Also sometimes people do not write the factor $$y^s$$.

This sum converges when $$\Re(s) \geq 1$$, however, it has an analytic continuation everywhere in the $$s$$ plane:
\begin{equation}\label{eq:Es-analytic-def}
E_s(\tau ) = y^s + \frac{\Lambda(1-s)}{\Lambda(s)}y^{1-s} + 
\sum_{j=1}^{\infty} \frac{4 \sigma_{2s-1}j \sqrt{y}K_{s-\frac{1}{2}}(2 \pi j y)}
{\Lambda(s)j^{s-1/2}}
\, \cos(2\pi j x).
\end{equation}
Here $$\sigma_{2s-1}(j)$$
is the divisor function, $$K$$ is the modified Bessel function of the second kind, and $$\Lambda$$ is the completed zeta function:
\begin{equation}
\Lambda(s) = \pi^{-s}\zeta(2s)\Gamma(s),
\end{equation}
and it satisfies the functional equation:
\begin{equation}
\Lambda(s) = \Lambda(\frac{1}{2} - s)
\end{equation}
From \eqref{eq:Es-analytic-def} we have 
\begin{equation}
\Lambda(s)E_s(\tau) = \Lambda(1-s)E_{1-s}(\tau).
\end{equation}

$$E_s(\tau)$$ has the following properties:
1. The Eisenstein series $$E_s(\tau)$$ is analytic in $$\tau$$.
2. $$E_s(\tau)$$ is meromorphic in $$s$$ with a unique pole of residue $$3/\pi$$ at $$s = 1$$ (for all $$s$$ in $$\mbb{H}$$), and infinitely many poles in the strip of $$0 < \Re(s)< \frac{1}{2}$$ at $$\rho/2$$, where $$\rho$$ is a non-trivial zero of the Riemann zeta-function $$\zeta$$.
3. For any $$s$$, $$E_s(\tau)$$ is a weak Maass form of weight $$0$$, and is an eigenvector of the Laplacian $$\Delta_0 = \Delta$$ with eigenvalue $$s(1-s)$$.
4. Note that $$E_s(\tau)$$ are not square integrable over the fundamental domain $$\mbb{H}/\SLZ$$.


These $$E_s(\tau)$$, for $$s = \frac{1}{2} + it$$, will also play a crucial in the harmonic analysis of modular functions on $$\mbb{H}$$, which we will study in the [next post]{???}.


## Real analytic weight $$k$$ Eisenstein series
Now we introduce weight $$k$$ Maass forms, which are higher weight generalizations of Maass forms.

<b> Definition:</b> 
A function $$f \colon \mbb{H} \to \mbb{C}$$ is a Maass form of weight $$k$$ if 
1. We have
   \begin{equation}
   f(M \cdot \tau) = (\frac{c\bar{\tau}+d}{|c \tau + d|})^k f(\tau).
   \end{equation}
   NOTE THAT SOME PEOPLE ALSO DIVIDE BY 
2. $$f$$ is an eigenfunction of the hyperbolic Laplacian:
   \begin{equation} \Delta_k = -y^2 (\partial_x^2 + \partial_y^2 ) + iky \partial_x
   .\end{equation}
3. $$f$$ has moderate growth at the cusp, i.e., there exists $$N$$ such that $$f(\tau) =O(y^N)$$ as $$y \to \infty$$. 

Now we are going to define real-analytic weight $$k$$ Eisenstein series 
<b>Definition:</b> 
???? WHat is it

The **real-analytic Eisenstein seires** of weight $$k$$ is 
\begin{equation}
    \sum_{c \geq 0, (c,d) = 1} (c \tau + d)^{-k} |
\end{equation}


## Real analytic weight $$(p,q)$$ Eisenstein series
Our next goal is to generalize this to weight 







<br><br>
<br>

## References:
- https://arxiv.org/abs/2311.00699
- https://math.berkeley.edu/~btw/small-eisenstein.pdf,
- Borcherds Products on O(2,l) and Chern Classes of Heegner Divisors Section I