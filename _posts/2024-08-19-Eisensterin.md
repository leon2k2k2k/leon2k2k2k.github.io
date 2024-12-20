---
layout: post
title: Pseudo-Eisenstein series, functional equations, and poles
date: 2024-08-19
description: Eisenstein series II
tags: mathematics, modular forms
categories:
---
In this note we are going to review how Eisenstein series (the weight $$0$$ trivial MTCs ones) naturally comes from the study of scalar piece of modular functions. Using this, we are going to establish basic facts about the Eisenstein series, functional equations, harmonic decompositions, and pole structures.
We are basically following this excellent [note](https://www-users.cse.umn.edu/~garrett/m/mfms/notes_2013-14/13_1_cont_afc_spec.pdf), which I got from Discord lol.

Let $$G = \SL_2(\mbb{R})$$. We need to denote a number of its subgroups: $$A$$ the diagonal matrices, $$A^+$$ the diagonal matrices with positive coefficients, $$N$$ be the upper-triangular unipotent (i.e. the diagonal part is $$\pm 1$$), $$P = NA$$ the upper-triangular, $$P^+ = NA^+$$, and $$K = \SO_2(\mbb{R})$$. Finally, we also have the discrete parts: $$\Gamma = \SL_2(\mbb{Z})$$, $$\Gamma_{\infty} = N \cap \Gamma$$ is the $$\mbb{Z}$$ subgroup that generated by $$T = \begin{pmatrix} 1 & 1 \\ 0 & 1\end{pmatrix}$$, and $$\mbb{H} = G/K$$ is the upper half plane.

## Scalar piece, adjunctions, and psudo-Eisenstein series
In this story, the central idea of Eisenstein series is that they describe the *scalar (constant)* piece of the modular function. 
The idea is the following, we have a commutative square of inclusions
$$\begin{equation}\label{eq:group-comm-square}
\begin{array}[ccc]
s \Gamma_{\infty} & \to & \Gamma \\ 
\downarrow & & \downarrow \\ 
N & \to & G
\end{array}
\end{equation}$$
We are interested in functions on $$\Gamma\backslash \mbb{H}$$, while the constant piece comes from $$N \backslash \mbb{H}$$ which can be identified with the positive $$y$$-axis $$i(0, \infty)$$. First we are going to define a map from modular functions to functions on $$N \backslash \mbb{H}$$, by integrating over $$N$$. Of course we need to quote by the common subgroup $$\Gamma_{\infty}$$.
Let $$f$$ be a reasonable function on $$\Gamma\backslash\mbb{H}$$.
<b>Definition:</b> The constant term $$\cp f$$ is 
$$\begin{equation}\label{eq:cp-formula}
\cp f(y) = \cp f(z) = \int_{\Gamma_{\infty}\backslash N} f(z) dz
\end{equation}$$
<br>
By definition, this is an $$N$$-invariant function on $$\mbb{H}$$, equivalently a function on the positive $$y$$-axis.

A function $$f$$ is a *cusp form* if the constant term vanishes $$\cp f = 0$$. As we will see, the theory Eisenstein series give an explicit decomposition of functions orthogonal to the cusp forms.

We are going to turn $$\cp$$ into a part of an adjunction. To do that we need pairings. For $$H$$ a subgroup of $$G$$ and nice functions $$f, F$$ (not necessarily from the same space of functions), consider the pairing:
$$\begin{equation}
\langle f, H\rangle_{H\backslash \mbb{H}} = \int_{H \backslash \mbb{H}} f \cdot F
\end{equation}$$
note that this is complex linear thus *not* hermitian.

Now we can define the adjunct of $$\cp$$, via the pairing for $$H = \Gamma$$ and $$H = N$$:
<b>Definition:</b> Let $$\psi$$ be a compactly supported function on $$N \backslash \mbb{H}$$, we define $$\Psi_{\psi}$$, the psuedo-Eisenstein series associated to $$\psi$$, to be the modular invariant function such that for every modular invariant functino $$f$$, we have 
$$
\begin{equation}\label{eq:adj-formula}
\langle \cp f, \psi\rangle_{N\backslash \mbb{H}} = \langle f, \Psi_{\psi}\rangle_{\Gamma \backslash \mbb{H}}.
\end{equation}$$
Note that the invariant measure on $$N\backslash \mbb{H}$$ is $$dy/y^2$$.

By explicitly computation, we see that $$\Psi_{\psi}$$ is of the form 
$$
\begin{equation}\label{eq:psi-formula}
\sum_{\gamma \in \Gamma_{\infty}\backslash \Gamma} \psi(yz).
\end{equation}
$$ 
Note that the formulas \eqref{eq:cp-formula} and \eqref{eq:psi-formula} is symmetrical with respect to \eqref{eq:group-comm-square}. Moving forward, just like adjunctions in category theory, we are going to take \eqref{eq:adj-formula} to be the *defining property* of (pseudo)-Eisenstein series.

Note that in contrast to fuctions on $$\Gamma\backslash \mbb{H}$$, we completely understand functions on $$N\backslash \mbb{H} \simeq i(0, \infty)$$ and its Fourier decomposition, which we now turn to.

## Meillin transform and Eisenstein series
Meillin transform is a natural multiplicative extension of Fourier transform, which we review!
Given $$\psi$$ in $$C^{\infty}_c(0, \infty)$$, its Mellin transform $$M\psi$$ is a function on the complex plane:
$$\begin{equation}
M\psi(s) = \int_0^{\infty} \psi(y) y^{-s} \frac{dy}{y}.
\end{equation}$$
For $$\psi$$ compactly supported, $$M\psi$$ is converge nicely for all $$s$$ on the complex plane. In particular this is holomorpsic in $$s$$. Note that the $$s = 0 + it$$ line is the Fourier line. For more general $$\psi$$, such as the ones are well be interested in for $$2d$$ CFT partition functions, the constant piece will not be compactly supported, and $$M\psi(s)$$ might have poles or entire regions of singularities.


The Meillin inversion says the following, if $$\psi$$ is compactly supported, then we have
$$\begin{equation}\label{eq:meillin-inversion}
\psi(y)  = \frac{1}{2\pi i}\int_{\sigma - i \infty}^{\sigma + i \infty} M\psi(s) y^s ds
\end{equation}$$
for any choice of real $$\sigma$$. For general $$\psi$$, this holds for $$\sigma = 0$$, and continue to hold as well as $$M\psi(s)$$ is well-defined and add up contribution from poles.

Now we are going to use the Meillin inversion formula \eqref{eq:meillin-inversion} to decompose pseudo-Eisenstein series. Let us first introduce Eisenstein series (once again!):

<b>Definition:</b> let $$s$$ be a complex number, then the Eisenstein $$E_s$$ is the pseudo-Eisenstein series $$\Psi_{y^s}$$ associated to the function $$y^s$$.
Note that this is only well-defined for $$\Re(s) > 1$$, for general $$s$$ we analytically continue in $$s$$. As we will see, the poles of $$E_s$$ is extremely interesting.

Now we have the following: for any compactly generated $$\psi$$, by \eqref{eq:meillin-inversion} and \eqref{eq:psi-formula} we have 
$$
\begin{equation}
\Psi_{\psi}(z) = \frac{1}{2\pi i}\sum_{\gamma \in \Gamma_{\infty}\backslash \Gamma} \int_{\sigma - i \infty}^{\sigma + i \infty} M\psi(s) \cdot (\Im(\gamma z))^s ds.
\end{equation}
$$
Now we want to exchange the sum and integral, but can only do so when the double integral is absolutely convergent, which happens for $$\sigma > 1$$. This is the same as the fact that  $$\Re(s) > 1$$ is when the sum for $$E_s$$ converge absolutely. Therefore for $$\sigma > 1$$, we have 
$$\begin{equation}\label{eq:helper-1}
\Psi_{\psi}(z) = \frac{1}{2\pi i}\int_{\sigma - i \infty}^{\sigma+ i \infty} M\psi(z) \cdot E_s(z) ds.
\end{equation}$$

There is a couple things to point out:
1. As we will see, the best line is $$\sigma = 1/2$$, which is outside of the region of $$\sigma > 1$$.
2. The formula \eqref{eq:helper-1} is unsatisfactory becuase it referes to $$\psi(z)$$ itself rather than the constant piece of $$\Psi_{\psi}(z)$$. Thus we need to understand $$\cp(\Psi_{\psi})$$, in particular for the Eisenstein series.
3. We are also interested in general $$\sigma$$ for $$\sigma < 1$$.

Let's first consider point 2. Using \eqref{eq:adj-formula}, we see that 
$$
\begin{equation}\label{eq:Es-pairing}
\langle E_s, f\rangle_{\Gamma\backslash \mbb{H}} = \langle y^s, \cp f\rangle_{N\backslash \mbb{H}} = M(\cp f)(1-s). 
\end{equation}$$ 
Note that the $$1$$ in $$1-s$$ comes from the fact that the integral in $$N\backslash \mbb{H}$$ is $$\frac{dy}{y^2}$$ rather than the multiplicative $$\frac{dy}{y}$$. To me this seems to be a very important fact. 

## Functional equation of Eisenstein series
Now let's talk about the meromorphic continuation. First we are going to provide the following formula, which I don't really know how to derive:
$$\begin{equation}\label{eq:constant-piece-of-Es}
\cp E_s = y^s + c_s y^{1-s}
\end{equation}$$
here $$c_s = \Lambda(2s-1)/\Lambda(2s)$$ and $$\Lambda(s) = \pi^{-s/2}\Gamma(s/2)\zeta(s)$$ is the completed zeta function. Recall that the complete zeta function satisfies the functional equality $$\Lambda(1-s) = \Lambda(s)$$.
Although I don't know where this formula comes from, the $$y^s$$ piece is obvious, while $$y^{1-s}$$ seems to come from $$S$$-transform.

Furthermore, $$E_s$$ is an eigenvector of the Laplacian operator 
$$\Delta_s = y^2(\partial_x ^2 + \partial_y^2)$$ with eigenvalue $$s(s-1)$$. Note that the eigenvalue  is invariant under $$s \mapsto 1-s$$. This and the constant piece is hinting at the following function:
$$\begin{equation}\label{eq:Es-func-eq}
E_{1-s} \Lambda((1-s)/2) = E_s \Lambda(s/2)
\end{equation}$$
Note that also $$E_{\overline{s}} = \overline{E}_s$$. In particular we see that $$c_s$$ doesn't vanish on the line $$\Re(s) = 1/2$$ and $$E_{1/2 + it}$$ is a special line!

Let's take a look at the zeroes and poles of $$E_s$$. To start, recall that the completed zeta function $$\Lambda(s)$$ has pole at $$s = 1$$ and zeros at the non-trivial zeroes $$z_k$$ of the Riemann zeta function. Looking at \eqref{eq:constant-piece-of-Es}, we see that problem arises when $$2s - 1 = 1$$ or $$2s = z_k$$, hence $$E_s$$ has poles at $$s = 1$$ and $$s = z_k/2$$. Furthermore, the pole at $$s = 1$$ has a constant residue, which as we will see plays a major role later.


## Harmonic decomposition
Now we are going to re-write \eqref{eq:helper-1} to get a harmonic decomposition.
First we would like to write this in terms of $$\Psi_{\psi}$$ instead of $$\psi$$.

First we move the integral to $$\sigma = 1/2 + it$$, recall that we get one pole of $$E_s$$ at $$s=1$$. We will return to this later and simply write it as $$\Res$$ for now.
$$\begin{equation}\label{eq:harmonic-decomp-1}
\Psi_{\psi} - \Res = \frac{1}{2\pi i} \int_{1/2 - i \infty}^{1/2 + i \infty} M\psi(s) E_s ds.
\end{equation}$$
By \eqref{eq:constant-piece-of-Es} and \eqref{eq:Es-pairing}, we have 
$$\begin{equation}\label{eq:helper-2}
M(\cp\Psi_{\psi})(s) = \langle E_{1-s}, \Psi_{\psi}\rangle = M\psi(s) + c_{1-s}M\psi(1-s).
\end{equation}$$
Going back to \eqref{eq:harmonic-decomp-1}, we can use the functional equation \eqref{eq:Es-func-eq}, i.e. $$E_{1-s} = c_{1-s}E_s$$ to obsorb the second  term in 
\eqref{eq:helper-2}. This means that \eqref{eq:harmonic-decomp-1} can be written as 
$$\begin{align}
\Psi_{\psi} - \Res &= \frac{1}{2\pi i} \int_{1/2 - i \infty}^{1/2 + i \infty} M\psi(s) E_s ds\\
&= \frac{1}{2\pi i} \int_{1/2 + i0}^{1/2 + i \infty} M\psi(s) E_s + M\psi(1-s) E_{1-s} ds\\
&= \frac{1}{2\pi i}\int_{1/2+i0}^{1/2+ i \infty}M(\cp \Psi_{\psi}(s))E_s ds
\end{align}
$$
Note that this only works for $$s = 1/2 + it$$ as it is the line invariant under $$s \mapsto 1-s$$. Furthermore, using the fact that $$E_{\overline{s}} = \overline{E_s}$$, we have 
$$
\begin{equation}
\Psi_{\psi} - \Res = \frac{1}{4\pi i}\int_{1/2 - i \infty}^{1/2 + i \infty} \langle \Psi_{\psi}, E_s\rangle \cdot E_s ds
\end{equation}$$
where $$\langle -,-\rangle$$ is the *complex-hermitian pairing* where we conjugate the second factor.

Now let's get to the residue part. Recall that the only pole of $$E_s$$ in the half-plane $$\Re(s) \geq 1/2$$ is at $$s = 1$$, it is a simple pole with value $$\frac{3}{\pi}$$, as we will see, this is the volume of $$\Gamma\backslash \mbb{H}$$.
Thus 
$$
\begin{align}
\Res = M\psi(1) \cdot \res_{s=1}E_s = \int_0^{\infty} \psi(y) \frac{dy}{y} = \int_{N\backslash \mbb{H}}\psi(y)\frac{dy}{y^2} = \int_{\Gamma_{\infty}\backslash \mbb{H}} \psi(z) \frac{dx\, dy}{y^2}\\
 = \int_{\Gamma\backslash \mbb{H}}\sum_{\gamma \in \Gamma_{\infty}\backslash \Gamma} \psi(z)  = \int_{\Gamma\backslash \mbb{H}} \Psi_{\psi} \frac{dx\, dy}{y^2} = \langle  \Psi_{\psi}, 1\rangle.
\end{align}
$$
Therefore we see that $$M\psi(1)$$ is the inner product of $$\Psi_{\psi}$$ with the constant function $$1$$. That's great! This is telling us that we also get the constant functions.

To summarize, we get a harmonic decomposition theorem:

<b>Theorem:</b>
Let $$f$$ be a square-integrable function orthgonal to the cuspforms, then we have an $$L^2$$ equality:
$$
\begin{equation}
f =_{L^2} \frac{1}{4\pi i}\int_{1/2 - i\infty}^{1/2+ i\infty} \langle f, E_s \rangle \cdot E_s ds + \frac{\langle f,1\rangle \cdot 1}{\langle 1, 1\rangle}.
\end{equation}
$$
Tah dah!



<br><br>
<br>

## References:
- https://www-users.cse.umn.edu/~garrett/m/mfms/notes_2013-14/13_1_cont_afc_spec.pdf. 







