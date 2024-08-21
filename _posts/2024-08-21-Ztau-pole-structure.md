---
layout: post
title: Pole structure of harmonic decomposition of Narain scalar primary
date: 2024-08-21
description: Harmonic analysis of 2D CFTs I
tags: mathematics, modular forms, mathematical physics, 2D CFTs
categories:
---
In this post we are going to explore the pole structures when decomposing the scalar primary partition function of Narain CFTs using Eisenstein series. This is the content of appendix A of [this](https://arxiv.org/pdf/2208.02259).
Let $$\mu$$ be a point in the Narain moduli space, with associated energy $$H$$ and momentum $$P$$. In our parameterization, given $$(n,m) \in \mbb{Z}^c$$, the momentum $$P(n,m)$$ is the dot product $$2 n \cdot m$$. 
$$
\begin{equation}
Z^{c}(\tau, \mu) =
y^{\frac{c}{2}}(\sum_{n,m \in \mbb{Z}^c} e^{-\pi y H(n,m) + 2\pi i x n \cdot m})
\end{equation}
$$

Our starting point is the following harmonic decomposition, which should be covered in the previous [post](???):
$$\begin{align}\label{eq:Zc-harmonic-decomp}
Z^{c}(\tau, \mu) &= E_{\frac{c}{2}}(\tau) + 3\,\pi^{-\frac{c}{2}}\,\Gamma(\frac{c}{2}-1)\,\mcal{E}^c_{\frac{c}{2}-1}(\mu)\\
&+ \frac{1}{4\pi i}\int_{\Re s = 1/2}\,ds \,\pi^{s-\frac{c}{2}}\,\Gamma(\frac{c}{2}-s)\,\mcal{E}^c_{\frac{c}{2}-s}(\mu)\,E_s(\tau) \\
&+ \sum_{n=1}^{\infty}\,(Z^{c}, \nu_n)\,\nu_n(\tau)
\end{align}$$
Note that this really only holds for $$c > 2$$, we will return to the $$c=1,2$$ cases later or in an another post.

Let us explain each of the four terms 
1. The first term $$E_{\frac{c}{2}}(\tau)$$ is the ensemble average of $$Z^c(\tau, \mu)$$, integrated over the entire Narain moduli space (only converges for $$c > 2$$). Mathematically this is the Seigel-Weil formula. Physically this $$E_{\frac{c}{2}}(\tau)$$ is the partition function of the 3D Chern-Simons gravity theory, and the agreement is the ensemble average of the AdS/CFT.
2. The second term $$3\,\pi^{-\frac{c}{2}}\,\Gamma(\frac{c}{2}-1)\,\mcal{E}^c_{\frac{c}{2}-1}(\mu)$$ comes from the average
$$\begin{equation}
\frac{3}{\pi}\int_{\Gamma\backslash\mbb{H}}(Z^c(\tau,, \mu)-1) \frac{dx\, dy}{y^2}.
\end{equation}$$
Note that the subtractin of the $$1$$ term comes from $$E_{\frac{c}{2}}(\tau)$$. This is also the residue of the Rankin-Selberg transform $$R_s[Z^c - 1]$$ at $$s=1$$.
3. The third term $$\frac{1}{4\pi i}\int_{\Re s = 1/2}\,ds \,\pi^{s-\frac{c}{2}}\,\Gamma(\frac{c}{2}-s)\,\mcal{E}^c_{\frac{c}{2}-s}(\mu)\,E_s(\tau)$$ comes from the Rankin-Selberg transform $$R_s[Z^c - 1]$$.
4. The last term $$\sum_{n=1}^{\infty}\,(Z^{c}, \nu_n)\,\nu_n(\tau)$$ is simply overlap with the cusp forms, which we don't have much to say.

Now let us consider the constant piece, which by definition doesn't have contribution from the cusp forms. 
To do this, we simply integrate $$Z^c(\tau, \mu)$$ over the strip $$-1/2 < x < 1/2$$:
$$\begin{equation}
\int_{-1/2}^{1/2}dx Z^c(\tau, \mu) = y^{c/2} (1 + \sum_{\Delta \in S}e^{-\pi y \Delta})
\end{equation}$$
where $$S$$ is the set of non-trival scalar primary operators and $$\Delta$$ is the dimension. Since we know the constant piece of $$E_s$$, and that $$\nu_k$$ has no constant piece.

\eqref{eq:Zc-harmonic-decomp} implies the following:
$$\begin{align}
\int_{-1/2}^{1/2}dx \,Z^c(\tau, \mu) &= y^{c/2} + \frac{\Lambda(\frac{c-1}{2})}{\Lambda(\frac{c}{2})} y^{1-\frac{c}{2}} + 2\pi^{-\frac{c}{2}}\,\Gamma(\frac{c}{2} - 1)\, \mcal{E}^c_{\frac{c}{2}-1}(\mu) \\ 
&+ \frac{1}{2\pi i}\int_{\frac{1}{2} - i \infty}^{\frac{1}{2} + i\infty}ds\, \pi^{s-\frac{c}{2}}\,\Gamma(\frac{c}{2}-s)\,\mcal{E}^c_{\frac{c}{2}-s}(\mu)\, y^s.
\end{align}$$
We are interested in moving this integral to $$\Re(s) > \frac{c}{2}$$.











