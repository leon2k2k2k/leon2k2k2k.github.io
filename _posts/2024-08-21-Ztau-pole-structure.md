---
layout: post
title: Pole structure of harmonic decomposition of Narain scalar primary
date: 2024-08-21
description: Harmonic analysis of 2D CFTs I
tags: mathematics, modular forms, mathematical physics, 2D CFTs
categories:
---
<span style="color:red">I might be misssing a factor of $$2$$ for the energy $$\Delta$$!!</span>

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
\int_{-1/2}^{1/2}dx Z^c(\tau, \mu) = y^{\frac{c}{2}} (1 + \sum_{\Delta \in S}e^{-\pi y \Delta})
\end{equation}$$
where $$S$$ is the set of non-trival scalar primary operators and $$\Delta$$ is the dimension. Since we know the constant piece of $$E_s$$, and that $$\nu_k$$ has no constant piece.

\eqref{eq:Zc-harmonic-decomp} implies the following:
$$\begin{align}\label{eq:eq-1}
\int_{-1/2}^{1/2}dx \,Z^c(\tau, \mu) &= y^{\frac{c}{2}} + \frac{\Lambda(\frac{c-1}{2})}{\Lambda(\frac{c}{2})} y^{1-\frac{c}{2}} + 3\pi^{-\frac{c}{2}}\,\Gamma(\frac{c}{2} - 1)\, \mcal{E}^c_{\frac{c}{2}-1}(\mu) \\ 
&+ \frac{1}{2\pi i}\int_{\frac{1}{2} - i \infty}^{\frac{1}{2} + i\infty}ds\, \pi^{s-\frac{c}{2}}\,\Gamma(\frac{c}{2}-s)\,\mcal{E}^c_{\frac{c}{2}-s}(\mu)\, y^s.
\end{align}$$
We are interested in moving this integral to $$\Re(s) > \frac{c}{2}$$.
The claim is that the only poles we are going to hit is $$s = \frac{c}{2}, \frac{1 + z_k}{2}$$, where $$z_k$$ is the non-trivial zeros of the Riemann zeta function. Showing this is the goal of the post:

## Pole structures
Dividing by $$y^{\frac{c}{2}}$$ and elimintate the constant term, we have the following: 
$$\begin{align}\label{eq:eq-2}
\sum_{\Delta \in S}e^{-\pi y \Delta} &= \frac{\Lambda(\frac{c-1}{2})}{\Lambda(\frac{c}{2})} y^{1-c} + 3\pi^{-\frac{c}{2}}\,\Gamma(\frac{c}{2} - 1)\, \mcal{E}^c_{\frac{c}{2}-1}(\mu) y^{-\frac{c}{2}}\\ 
&+ \frac{1}{2\pi i}\int_{\frac{1}{2} - i \infty}^{\frac{1}{2} + i\infty}ds\, \pi^{s-\frac{c}{2}}\,\Gamma(\frac{c}{2}-s)\,\mcal{E}^c_{\frac{c}{2}-s}(\mu)\, y^{s - \frac{c}{2}}.
\end{align}$$

To derive the pole structure, the idea is to use the discreteness of the spectrum. In particular, there is a gap above the groundstate. 

Now the idea is to use the Laplace transform, which we now review. 
Let $$\rho(t)$$ be the density function for scalar primaries:
$$\begin{equation}
\rho(t) = \sum_{\Delta' \in S}\delta_{\pi \Delta', t}.
\end{equation}$$

Let $$f(t)$$ be a function on $$(0, \infty)$$, then the *Laplace transform* $$\cL(f)(s)$$ is the function 
$$\begin{equation}
\cL(f)(s) \coloneqq \int_0^{\infty} f(t)e^{-ty} dy.
\end{equation}$$
By construction, the Laplace transform $$\cL(\rho)$$ is precisely the primary counting partition function $$\sum_{\Delta \in S}e^{-\pi y \Delta}$$.

Now we are going to perform inverse Laplace transform to the right hand side of  \eqref{eq:eq-2}, this is easy as the only $$y$$ dependence is of the form $$y^{s}$$. Note that the Laplace transform of $$t^s$$ is $$\frac{\Gamma(s+1)}{y^{s+1}}$$. Conversely, the inverse Laplace transform $$\cL^{-1}(y^s) = \frac{1}{\Gamma(-s)t^{(s+1)}}$$.

So we have 
$$\begin{align}\label{eq:eq-3}
\rho(t) = \cL^{-1}(\sum_{\Delta \in S}e^{-\pi y \Delta})
&= \frac{\Lambda(\frac{c-1}{2})}{\Lambda(\frac{c}{2})} \frac{t^{c-2}}{\Gamma(c-1)}\\
&+ 3\pi^{-\frac{c}{2}}\,\Gamma(\frac{c}{2} - 1)\, \mcal{E}^c_{\frac{c}{2}-1}(\mu)
\frac{t^{\frac{c}{2}-1}}{\Gamma(\frac{c}{2})}\\
&+ 
\frac{1}{2\pi i}\int_{\frac{1}{2} - i \infty}^{\frac{1}{2} + i\infty}ds\, \pi^{s-\frac{c}{2}}\,\Gamma(\frac{c}{2}-s)\,\mcal{E}^c_{\frac{c}{2}-s}(\mu)\, \frac{t^{\frac{c}{2}-s-1}}{\Gamma(\frac{c}{2}-s)}.
\end{align}$$



Let $$N_0(t) = \int_{0}^{t}\rho(t') dt'$$ be the simple function that counts the number of scalar primaries with energy $$\leq \Delta = \pi t$$. Note that the existence of a gap above the groundstate implies that there exists an $$\epsilon$$ such that $$N_0(t) = 0$$ for $$t \leq \epsilon$$. 
Using \eqref{eq:eq-3}, we can simply compute $$N_0(t)$$:
$$\begin{align}
&\frac{\Lambda(\frac{c-1}{2})}{\Lambda(\frac{c}{2})} \frac{t^{c-1}}{\Gamma(c)}\\
&+ 3\pi^{-\frac{c}{2}}\,\Gamma(\frac{c}{2} - 1)\, \mcal{E}^c_{\frac{c}{2}-1}(\mu)
\frac{t^{\frac{c}{2}}}{\Gamma(\frac{c}{2}+1)}\\
&+ 
\frac{1}{2\pi i}\int_{\frac{1}{2} - i \infty}^{\frac{1}{2} + i\infty}ds\, \pi^{s-\frac{c}{2}}\,\Gamma(\frac{c}{2}-s)\,\mcal{E}^c_{\frac{c}{2}-s}(\mu)\, \frac{t^{\frac{c}{2}-s}}{\Gamma(\frac{c}{2}-s+1)}.
\end{align}$$

When we take $$\Delta = 2 \pi t$$ and expand out $$\Lambda$$, we get the following:
$$\begin{align}
N_0(\Delta) &= \frac{2\pi^c\zeta(c-1)\Delta^{c-1}}{(c-1)\zeta(c)\Gamma(\frac{c-1}{2})^2\zeta(c)}\\
&+ 12 \frac{2^\frac{c}{2}\Delta^{\frac{c}{2}}\mcal{E}^c_{\frac{c}{2}-1}(\mu)}{c (c-2)}\\
&+ \frac{1}{2\pi i}\int_{\frac{1}{2} - i \infty}^{\frac{1}{2} + i\infty}ds\, \frac{2^{\frac{c}{2} - s}\Delta^{\frac{c}{2} - s}\mcal{E}^c_{\frac{c}{2} - s}(\mu)}{\frac{c}{2}-s}
\end{align}$$
Note that for the first line we used the Legendre duplication formula
$$\begin{equation}
\Gamma(z)\Gamma(z +\frac{1}{2}) = 2^{1-2z}\sqrt{\pi}\Gamma(2z).
\end{equation}
$$

Now using the functional equation on $$\mcal{E}^c_{s}$$ on the integrade, and the fact that it needs to cancel the first two terms, we arrive at the fact that $$\mcal{E}^c_{\frac{c}{2}+s-1}$$ has poles at $$s = \frac{z_n}{2}$$ where $$z_n$$ is a non-trivial zero of the Zeta function.
Moreoever, to cancel out the first term we see that $$\mcal{E}^c_0(\mu) = -1$$.

Look into the paper for this argument. 

Now going back to the integrand of \eqref{eq:eq-2}, there are a pole coming from $$\Gamma(\frac{c}{2}-s)$$ at $$s = \frac{c}{2}$$, and poles at $$s = 1 - \frac{z_n}{2}$$, equivalently $$s = \frac{1 + z_n}{2}$$ by the functional equation of the zeta function. This completes the claim.
Now we are going to move the integral to the right on \eqref{eq:eq-2}. Note that the pole at $$s = \frac{c}{2}$$ simply contributes to the constant term $$-1$$, we can move to the left hand side of \eqref{eq:eq-2}. Thus we get the following:
$$\begin{align}\label{eq:eq-4}
1 + \sum_{\Delta \in S}e^{-\pi y \Delta} &= \frac{\Lambda(\frac{c-1}{2})}{\Lambda(\frac{c}{2})} y^{1-c} + 
\epsilon_c(\mu)y^{-\frac{c}{2}}\\ 
&+ \sum_{k=1}^{\infty}\Re(\delta_{k,c}(\mu)y^{-\frac{c}{2}+\frac{1+z_k}{2}})\\
&+ \frac{1}{2\pi i}\int_{\gamma - i \infty}^{\gamma+ i\infty}ds\, \pi^{s-\frac{c}{2}}\,\Gamma(\frac{c}{2}-s)\,\mcal{E}^c_{\frac{c}{2}-s}(\mu)\, y^{s - \frac{c}{2}}.
\end{align}$$
Here $$\gamma > \frac{c}{2}$$. 
Here we have $$\mu$$-dependent residues:
$$
\begin{align}
\epsilon_c(\mu) &= \frac{3}{\pi}\int_{\Gamma\backslash \mbb{H}}\frac{dx dy}{y^2} (Z^c(\tau, \nu) - E_{\frac{c}{2}}(\tau)), \\ 
\delta_{k,c}(\mu) &= \int_{\Gamma\backslash \mbb{H}}\frac{dx dy}{y^2}(Z^c(\tau, \nu) - E_{\frac{c}{2}}(\tau)) \Res_{s = \frac{z_k}{2}}E_s(\tau)
\end{align}
$$

The integrand is going to integrate to something of the form $$O(e^{\frac{-2\pi n^2 \Delta}{y}})$$. Lastly, take $$T = y^{-1}$$, and we exaimine the high temperature before of the scalar primary partition function, we get the (5.1) of the paper:
$$\begin{align}\label{eq:eq-5}
1 + \sum_{\Delta \in S}e^{\frac{-2\pi \Delta}{T}} &= \frac{\Lambda(\frac{c-1}{2})}{\Lambda(\frac{c}{2})} T^{c-1} + 
\epsilon_c(\mu)T^{\frac{c}{2}}\\ 
&+ \sum_{k=1}^{\infty}T^{\frac{c}{2} - \frac{3}{4}}
[\Re(\delta_{k,c}) \cos(\Im(z_k) \log T) - \Im(\delta_{k,c})\sin(\Im(z_k) \log T)]\\
&+ O(e^{-2\pi\Delta_{\mathrm{gap}}T})
\end{align}$$



