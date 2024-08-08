---
layout: post
title: Being confused about differential cohomology I
date: 2024-08-05
description: Ordinary differential cohomology
tags: mathematics, mathematical-physics
categories:
---

In this post I want to talk about differential cohomologies, which are ``differential refinement'' of cohomology theories. I am mainly confused because there are two major approaches, one is the classical differential Hexagons, which we will get to, the other is sheaves on spectra, which makes a lot more sense to me. 

In this post, Ww are going to focus ordinary differential cohomology. In the classical case we will review [Cheegar-Simons](https://math.mit.edu/juvitop/pastseminars/notes_2019_Fall/cheeger-simons.pdf), then we will move to Delign cohomology to define sheaves on spectra. 
A good reference is [this](https://arxiv.org/abs/2109.12250).

## Baby example I: $$\hatH^1(X; \mbb{Z})$$
Let us first review how differential cohomology is different from ordinary topological cohomology theory.
Let $$X$$ be a topological space, then the first cohomology group $$H^1(X; \mbb{Z}) = \Hom(H_1(X; \mbb{Z}); \mbb{Z})$$ 
is the set of linear maps from the first homology $$H_1(X; \mbb{Z})$$ to $$\mbb{Z}$$.

Now let's consider the differential cohomology counterpart: now we take $$X$$ to be a smooth manifold; we define $$\hatH^1(X; \mbb{Z})$$ to be smooth maps from $$X$$ to $$S^1$$. It is clear that there is a map $$\hatH^1(X; \mbb{Z}) \to H^1(X; \mbb{Z})$$ given by taking a map $$f \colon X \to S^1$$ to the image of the generator $$\nu \in H^1(S^1, \mbb{Z})$$ under the pullback map $$f^* \colon H^1(S^1; \mbb{Z}) \to H^1(X; \mbb{Z})$$. Explicitly, given a $$1$$-cycle $$\gamma \in X$$, then $$f$$ restricted to $$\gamma$$ is a map from $$S^1 \to S^1$$. Then $$f^*(\nu)[\gamma]$$ is simply the winding number of this map.

Let us also remark that the map $$\hatH^1(X; \mbb{Z}) \to H^1(X; \mbb{Z})$$ is surjective: this follows from the de Rham theorem. Given any class $$a \in H^1(X; \mbb{Z})$$, then by de Rham theorem there exists a closed differential form $$\alpha \in \Omega^1(X)$$ whose class in de Rham cohomology 
corresponds to $$a$$ in  $$H^1(X; \mbb{R})$$. By constructions, $$\alpha$$ has integral periods. We can define a smooth map $$f \colon X \to S^1$$ from $$\alpha$$ has follows: let's say that $$X$$ is connected, and we fix $$x \in X$$. Then for any $$y \in X$$ we take $$f(y) \coloneqq \int_\gamma \alpha \mod \mbb{Z}$$, 
where $$\gamma$$ is a path from $$x$$ to $$y$$. Note that this is well-defined as two different path form a closed loop, whose integral is an integer as $$\alpha$$ has integral periods.

It is clear that $$\hatH^1(X; \mbb{Z})$$ contains more information then just $$H^1(X; \mbb{Z})$$, in particular it contains differential informations: given $$f \in \hatH^1(X; \mbb{Z})$$, we have a one-form $$f^*\alpha$$ where the one-form $$\alpha \in \Omega^1(S^1)$$ is simply flat one $$d_x$$, when we write $$S^1$$ as $$\mbb{R}/\mbb{Z}$$. Moreoever, the de Rham class of $$\alpha$$ is equal to $$f^*(\nu)$$, viewed as a class in $$H^1(X; \mbb{R})$$.

This is a part of the ``differential cohomology hexagon'':

$$\begin{equation}\label{eq:diff-hex-0}
\begin{array}{ccccccccc}
&   & H^0(X; \mbb{R}/\mbb{Z}) &    &    &   & H^1(X; \mbb{R}) &  &  \\\
& \nearrow& & \searrow   & & \nearrow & & \searrow & \\\
H^0(X; \mbb{R}) &  & & & \hatH^1(X; \mbb{Z}) & & & & H^1(X; \mbb{R})\\\
& \searrow& & \nearrow   & & \searrow & & \nearrow & \\\
&   & \Omega^0(X)/\Omega^0_{\cl}(X)_{\mbb{Z}} & & & &  \Omega^1_{\cl}(X)_{\mbb{Z}} &  & 
\end{array}
\end{equation}$$

Here $$\Omega^i_{\cl}$$ means closed forms, and $$\Omega^i_{\cl}(X)_{\mbb{Z}}$$ means closed forms with integral periods. Note that the diagonals are in fact exact, and the top maps is the Bockstein homomorphism (which is $$0$$ here but not in general), while the lower map is the de Rham differential.
\eqref{eq:diff-hex-0} is called the differential Hexagon, one of the two approaches to diff cohomology we will discuss in this post.

<!-- sheaf cohomology stuff -->
Let us shed light on the other approach too. Let $$\Mfld$$ be the category of manifold, which we equipped with the Grothendieck topology consisting of open sets and open covering. We are going to consider sheaves on $$\Mfld$$.

Let us view $$\mbb{Z}$$ as a discrete abelian group manifold, hence $$\Hom(-, \mbb{Z})$$ is a sheaf on the category $$\Mfld$$ of manifolds with valued in $$\Ab$$. Furthermore, we have sheaves $$\Omega^i$$ parametrizing $$i$$-th forms on $$X$$. In particular, the sheave $$\Omega^0$$ is represented by the abelian group smooth manifold $$\mbb{R}$$. 
The canonical inclusion $$\mbb{Z} \to \mbb{R}$$ can be viewed as a map of sheaf. Let $$\mbb{Z}(1)$$ denote the chain complex $$\mbb{Z} \to \Omega^0$$, with $$\mbb{Z}$$ in degree $$0$$. Note that it is actually equivalent to $$\Omega \mbb{T}$$, where we view $$\mbb{T} = S^1$$ toghether with its abelian group structure.

Now its straightforward to define $$\hatH^1(X; \mbb{Z})$$, it is simply the value of $$\mbb{T}$$ on $$X$$, equivalently it is the first hyper-cohomology $$H^1(X; \mbb{Z}(1))$$. Later on we will define all cohomology that way.


## Baby example II: $$\hatH^2(X; \mbb{Z})$$
Alright, let's do the second cohomology. Recall that $$H^2(X; \mbb{Z})$$ is the isomorphism classes of (topological) line bundles on $$X$$. Let us define $$\hatH^2(X; \mbb{Z})$$ is the isomorphism classes of smooth line bundles with connections. Once again there is a map $$\hatH^2(X; \mbb{Z}) \to H^2(X; \mbb{Z})$$ that forgets the line bundle. Once again, it additionally has differential information, which is $$\hatH^2(X; \mbb{Z}) \to \Omega^2_{\cl}(X)_{\mbb{Z}}$$, taking a connection $$\nabla$$ to its curvature $$F_{\nabla}$$. Furthermore, there is a Hexagon similar to \eqref{eq:diff-hex-0}. I will skip writing it since we are going to do the general case very soon!

Moving on to the sheaf perspective. There is actually a lot of options
<b>Definition:</b> 
for $$n \geq 0$$, let $$\mbb{Z}(n)$$ be the sheaves of chain complex 
\begin{equation}\label{eq:Deligne}
\mbb{Z} \to \Omega^0 \to \Omega^1 \to \cdots \to \Omega^{n-1}
\end{equation}
Note that $$\mbb{Z}(0) = \mbb{Z}$$ and there are maps $$\mbb{Z}(n) \to \mbb{Z}(n-1)$$.


Let us consider their second cohomology:
1. $$H^2(X; \mbb{Z})$$ is the ordinary topological cohomology.
2. $$H^2(X; \mbb{Z}(1))$$ is the group of isomorphism classes of smooth $$\mbb{T}$$ bundles.
3. $$H^2(X; \mbb{Z}(2))$$ is $$\hatH^2(X; \mbb{Z})$$.

Well, what does $$H^2(X; \mbb{Z}(n))$$ represent in general? First note that $$H^n(X; \mbb{Z}(n+1)) \simeq H^n(X; \mbb{Z}(n+1+k))$$ for any $$k \geq 0$$. This is because those higher differential forms does not matter. Secondly, they are all equivalent to $$H^N(X; \mbb{R}/\mbb{Z}_{\disc})$$. This is because by de Rham theorem, the chain complex $$\Omega^0 \to \cdots \to \Omega^n \to \cdots $$ is 
equivalent to the discrete sheaf $$\mbb{R}_{\disc}$$, where we view $$\mbb{R}$$ as a discrete group manifold.
Thus $$\mbb{Z}(\infty) \simeq \mbb{Z} \to \mbb{R}_{\disc} \simeq 0 \to \mbb{T}_{\disc}$$.
Therefore we see that $$H^2(X; \mbb{Z}(n))$$ is $$H^1(X; \mbb{T}_{\disc})$$, which is equivalent to line bundles with \emph{flat} connections! This is easy to see if we consider the hyper-Cech-cohomology, where we are asking for $$d(\alpha_i) = 0$$ for  each local $$1$$-form $$\alpha_i$$ on the open set $$U_i$$ of $$X$$.

Note that the map $$H^1(X; \mbb{R}/\mbb{Z}_{\disc}) = H^2(X; \mbb{Z}(3)) \to H^2(X; \mbb{Z}(2))$$ appears in the Hexagon axioms.
cite[Yamashita-Yonekura, 1.3], cite[Cheeger-Simons]
## Cheegar-Simons differential group
Let us now review the Cheegar-Simons differential character group: 
<b>Cheeger-Simons differential character:</b>
Let $$X$$ be a manifold, then $$\hatH^n_{\CS}$$ consists of pairs $$(\omega, k)$$, where 
- $$\omega$$ is a closed form $$\omega \in \Omega^n_{\cl}(X)$$, 
- $$k$$ is a group homomorphism $$k \colon Z_{\infty, n-1}(X; \mbb{Z}) \to \mbb{R}/\mbb{Z}$$,
- $$\omega$$ and $$k$$ satisfy the following compatibility condition: for any $$c \in C_{\infty, n}(X; \mbb{Z})$$, we have 
\begin{equation}
k(\partial c) = <c, \omega>_{X} \mod \mbb{Z}.
\end{equation}

Here $$Z_{\infty, *}$$ and $$C_{\infty, *}$$ is the groups of smooth singular cycles and chains.
Let's check that $$\hatH^n_{\CS}$$ agrees with our $$\hatH^1$$ and $$\hatH^2$$:
for $$n = 1$$, given a map $$f \colon X \to S^1$$, then the associated Cheegar-Simon character is $$(\omega = f^* \alpha, a \mapsto \sum_{x \in a} f(x))$$. As for the other way, $$f (x)$$ is simply just $$a(\{x\})$$. The compatibility with $$\omega$$ implies that $$f$$ is smooth.

Similary, for $$n = 2$$, then given a connection the associated Cheegar-Simon character is $$(d\nabla, \gamma \mapsto \mathrm{hol}_{\nabla}\gamma)$$.

Let's check that the Cheegar-Simons character satsfies the differential Hexagon:
$$\begin{equation}\label{eq:diff-hex-n}
\begin{array}{ccccccccc}
&   & H^{n-1}(X; \mbb{R}/\mbb{Z}) &    &    &   & H^n(X; \mbb{R}) &  &  \\\
& \nearrow& & \searrow   & & \nearrow & & \searrow & \\\
H^{n-1}(X; \mbb{R}) &  & & & \hatH^n(X; \mbb{Z}) & & & & H^n(X; \mbb{R})\\\
& \searrow& & \nearrow   & & \searrow & & \nearrow & \\\
&   & \Omega^{n-1}(X)/\Omega^{n-1}_{\cl}(X)_{\mbb{Z}} & & & &  \Omega^{n}_{\cl}(X)_{\mbb{Z}} &  & 
\end{array}
\end{equation}$$
Let's describe the maps:
- $$H^{n-1}(X; \mbb{R}/\mbb{Z}) \to \hatH^n(X; \mbb{Z})$$ is given by $$\alpha \mapsto (0, c \mapsto <c, \alpha>_{X})$$.
- $$\Omega^{n-1}(X) \to \hatH^n(X; \mbb{Z})$$ is given by $$\beta \mapsto (d\beta, c \mapsto \int_{c}\beta \mod \mbb{Z})$$.
- $$\hatH^n(X; \mbb{Z}) \to \Omega^n_{\cl}(X)_{\mbb{Z}}$$ is given by $$(\omega, h) \mapsto \omega$$.
- $$\hatH^n(X; \mbb{Z}) \to\hatH^n(X; \mbb{Z})$$ is given by $$(\omega, h) \mapsto (c \mapsto \int_c \omega - \tilde{h}(\partial c))$$. Here $$\tilde{h}$$ is a lift of $$h$$ to a morphism $$Z_{\infty, n-1}(X) \to \mbb{R}$$. Note that such map always exist as $$Z_{\infty, n-1}(X)$$ is free. It is straightforward to check that this is closed, and a different choice of $$\tilde{h}$$ differ by an exact cycle.

In fact, there is a statement that map that satisfies the differential Hexagon are isomorphic to each other. I think its [Simons-Sullivan](https://arxiv.org/abs/math/0701077).

## Deligne cohomology
We have already met Deligne cohomologies, they are the $$\mbb{Z}(n)$$ groups before. The important thing is the the top degree recovers differential cohomology: 
<b> Theorem </b>: Let $$X$$ be a manifold, then there exists an equivalence:
\begin{equation}
H^n(X; \mbb{Z}(n)) \simeq \hatH^n_{\CS}(X; \mbb{Z}).
\end{equation}

However, we see that there is a vast family of cohomology in between $$H^n(X; \mbb{Z})$$ and $$H^n(X; \mbb{Z}(n))$$.
It turns out that the intermediate cohomology groups are also interesting, in particular when evaluating not at a manifold $$X$$, but rather a stack. See [this paper](https://arxiv.org/abs/2112.10837) that I wrote with Arun and Christoph a while back for how middle dimension cohomology groups are related to the family of Virasoro central extensions.


We end the blog with the following question:
<b> Question </b>: why does cohomology in $$\mbb{Z}(n)$$ satisfies the differential Hexagon axioms \eqref{eq:diff-hex-n}? 

Appearantly this is answered in [this paper](https://arxiv.org/abs/1311.3188), which we will visit next time. Hopefully we will also check out some generalized differential cohomology theories, such as differential $$KO, K$$ and bordism theories.


<br><br>
<br>

## References:
- https://arxiv.org/abs/2109.12250. 
- https://math.mit.edu/juvitop/pastseminars/notes_2019_Fall/cheeger-simons.pdf.
- https://arxiv.org/abs/math/0701077