---
layout: post
title: Being confused about differential cohomology II 
date: 2024-08-07
description: From recollement on differential cohomology to differential Hexagons
tags: mathematics, mathematical-physics
categories:
---

In this post we are going to describe the sheaves of spectra approach to differential cohomology, and see how the differential Hexagons that we saw in [earlier](???) naturally falls out of it using the machinary of recollement. I will largely follow Section 6 of [this notes](https://arxiv.org/abs/2109.12250). This post will be pretty $$\infty$$-categorical.


## Sheaves on manifolds
Let $$\Mfld$$ be the category of smoth manifolds. We equipped $$\Mfld$$ with the Grothendieck topology where covering are open covers. 

Let $$\cC$$ be a presentable $$\infty$$-category. Let $$\Sh(\Mfld; \cC)$$ be the full subcategory of $$\PSh(\Mfld; \cC)$$ consisting of $$\cC$$-valued sheaves.
There exists a sheafification functor $$\PSh(\Mfld; \cC) \to \Sh(\Mfld; \cC)$$, left adjoint to the canonical inclusion.

Let $$\Spaces, \Sp$$ be the $$\infty$$-categories of spaces and spectra.
We take as a definition that differential cohomology theories (spectra) are sheaves of spectra on $$\Mfld$$.

Let us give some simple examples: 
1. Any manifold $$M$$ defines a $$\Spaces$$-valued representable sheaves. 
2. Any topological space $$T$$ defines a $$\Spaces$$-valued sheave by $$X \mapsto \Hom_{\Spaces}(M, T)$$. Note that we are implicitily using the forgetful functor $$\Mfld \to \Spaces$$. This will play a crucial role.
3. Let $$G$$ be a lie group, then there are three different $$\Spaces$$-valued sheaves:
- $$BG$$: here we view $$G$$ as a topological group and $$BG$$ be its classifying space. It gives a presheaf by the second construction.
- $$B_{\bullet}G$$: this is the classiying space representing the smooth Lie group $$G$$. I.e., for a manifold $$X$$, the space $$B_{\bullet}G$$ is the space of principal $$G$$-bundles on $$X$$ .
- $$B_{\nabla}G$$: For a manifold $$X$$, the space $$B_{\nabla}G$$ is the space of $$G$$-principal bundles on $$X$$ together with connections.
4. For $$i \geq 0$$, let $$\Omega^i$$ be the $$\mbb{R}$$-vector space valued sheave with $$X \mapsto \Omega^i(X)$$.

<b>Remark:</b> Since every manifold has a good cover, it follows that sheaves are determined its value on the full subcategory of $$\mathbb{R}^n$$ for $$n \geq 0$$.
Another useful lemma is Proposition 3.4.7 of [this notes](https://arxiv.org/abs/2109.12250):
<b>Proposition</b>: If $$\cC$$ is a compactly generated $$\infty$$-category, then a morphism in $$\Sh(\Mfld; \cC)$$ is an equivalence if for every $$n \geq 0$$, the map on stalk of a point in $$\mbb{R}^n$$ is an equivalence on $\cC$.


## $$\mbb{R}$$-invariant sheaves
Now we discuss $$\mbb{R}$$-invariant differential spectra. 
<b>Definition</b>: Let $$\cC$$ be a presentable $$\infty$$-category. A $$\cC$-valued (pre)sheaf $$\cF$$ is $$\mbb{R}$$-invariant if for each manifold $$M$$, the projection $$\mathrm{pr} \colon M \times \mbb{R} \times M$$ induces an equivalence $$F(M) \xrightarrow{\simeq} F(M \times \mbb{R})$$.
We will write $$\Sh_{\mbb{R}}(\Mfld; \cC)$$ for the full subcategory of $$\mbb{R}$$-invariant sheaves.

Note that a sheaf is $$\mbb{R}$$-invariant if it takes homotopy equivalences  between manifolds to equivalences. This is going to $$M \times \mbb{R}$$ opens the door for homotopy equivalence.

<b>Proposition</b>: The global section map $$\cF \mapsto \cF(*)$$ defines an equivalence of $$\infty$$-category $$\Sh_{\mbb{R}}(\Mfld; \cC) \to \cC$$.

The inverse is given by taking an object $$c \in \cC$$ to the sheafification of the constant presheaf with value on $$\cC$$.

## The left and right adjoints
Now we are going to define the adjunctions between $$\Sh(\Mfld; \cC)$$ and $$\Sh_{\mbb{R}}(\Mfld; \cC) \simeq \cC$$. We already have the evaluation functor $$\Gamma_* \colon \Sh(\Mfld; \cC) \to \cC$$, and fully faithful left adjoint $$\Gamma^* \colon \cC \to \Sh(\Mfld; \cC)$$ of sheafification of the constant functor.
Given $$c \in \cC$$ and $$X \in \Mfld$$, then $$\Gamma^*(c)(M) = c^M$$, where on the right we view $$M$$ as space and the formula is given by cotensoring.

Now we are going to define the left adjoint to $$\Gamma^*$$, which is denoted as $$\Gamma_{\#}$$.
Let $$\Delta^n_{\mathrm{alg}}$$ be the algebraic $$n$$-simplex, consisting of points in $$(t_0, \cdots, t_n) \in \mathbb{R}^{n+1}$$ with $$\sum_i t_i = 1$$.
Note that the collection so$$\Delta^n_{\mathrm{alg}}$$ forms a cosimplicial manifold. 
Let $$\cF$$ be a $$\cC$$-valued sheaf, we define $$\Gamma_{\#}(\cF)$$ to be the geometric realization $$|\cF(\Delta^n_{\mathrm{alg}})|$$.
One can show that $$\Gamma_{\#}$$ is the right adjoint of $$\Gamma^*$$.

To summarize, for $$\cC$$ be a presentable $$\infty$$-category we have a diagram of adjuntions:
$$\begin{equation}
\begin{array}{ccc}
& \xleftarrow{\Gamma_{\#}}&\\\
\cC & \xrightarrow{\Gamma^*} & \Sh(\Mfld; \cC) \\\
& \xleftarrow{\Gamma_{*}}& 
\end{array}
\end{equation}$$
It follows that $$\Gamma^* \circ \Gamma_{\#}$$ and $$\Gamma^* \circ \Gamma_{*}$$ are left and right localizations respectively. We are going to denote them as $$L$$ and $$R$$ respectively. Note that they both takes sheaf to $$\mbb{R}$$-invariant sheaves.

 Let $$\cF$$ be a $$\cC$$-valued sheaf, then we have canonical maps $$R \cF \to \cF \to L \cF$$.
For $$X$$ a manifold, $$L\cF(M) = \cF(\Delta^n_{\mathrm{alg}})|^{M} $$ and $$R\cF(M) = \cF(*)^{M}$$. 
When $$\cC$$ is spectra, then $$\Gamma_{\#}\cF$$ and $$\Gamma_{*}\cF$$ are simply spectra, and its value on $$M$$ is the spectra underlying the topological cohomologies of $$M$$ with coefficients in $$\Gamma_{\#}\cF$$ and $$\Gamma_{*}\cF$$. 

<b>Example:</b>
Let $$M$$ be a manifold. We abuse notation and  also denote by $$M$$ the representing sheaf. Then $$\Gamma_* M = M(*)$$ is the discrete set $$M_{\disc}$$. Therefore $$RM$$ is the constant sheaf on the discrete set $$M_{\disc}$$. Note that the canonical map $$M_{\disc} \to M$$ is simply identity on the underlying set.
On the other hand, $$|M(\Delta^n_{\mathrm{alg}})|$$ is the underlying space $$M$$. Heauristically this is because there are path in $$\Delta^n_{\mathrm{alg}}$$ that allows us to explore the topology of $$M$$. 

<b>Example:</b> Let $$G$$ be a Lie group, let us consider $$B_{\bullet}G$$ and $$B_{\nabla}G$$. In this case $$B_{\bullet}G(*) = B_{\nabla}G(*)$$ is the discrete groupoid $$BG_{\disc}$$. Thus $$RB_{\bullet}G = RB_{\nabla}G$$ parametrizes flat $$G$$-bundles, which indeed is a homotopic invariant notion. $$LB_{\bullet}G$$???




<b>Example:</b>
For $$\mbb{Z}(0) = \mbb{Z}$$ this is a $$\mbb{R}$$-invariant sheaf, thuse $$R\mbb{Z} = \mbb{Z} = L\mbb{Z}$$. For $$n \geq 1$$, its value at $$*$$ is $$\mbb{Z}(n) \to \mbb{R}_{\disc}$$, thus its $$B\mbb{R}/\mbb{Z}_{\disc}$$. Therefore $$R\mbb{Z}(n)$$ is the ordinary spectra representing $$\mbb{R}/\mbb{Z}$$ cohomology. On the other hand $$|mbb{Z}(n)(\Delta^n_{\mathrm{alg}})|$$ is ???.

<b>Remark:</b> In general $$R\cF$$ is discrete/flat like while  $$L\cF$$ is continous.




## Recollection on recollement
Let us review recollement for stable $$\infty$$-categories.
Let $$\cX$$ be an $$\infty$$-category and $$\cZ$$ be a full subcategory of $$\cX$$. Then the right orthogonal complement $$\cZ^{\perp}$$ of $$\cZ$$ is the full subcategory consisting of objects that are right orthogonal to $$\cZ$$, that is, objects $$x \in \cX$$ such that $$\Hom_{\cX}(z, x) = 0$$ for every $$z \in \cZ$$. Similarly, $$^{\perp}\cZ$$ is the full subcategory of left orthogonal objects.


Let us recall a recollement: a recollement of $$\cX$$ is two full subcategory $$\cZ$$ and $$U$$ with a chain of adjunctions:
$$\begin{equation}
\begin{array}{ccccc}
& \xleftarrow{i^*}&    & \xleftarrow{j_!}    &                  \\\
\cZ & \xrightarrow{i_*} & \cX   &  \xrightarrow{j^*}  & U     \\\
& \xleftarrow{i^!} &     &    \xleftarrow{j_*}               & 
\end{array}
\end{equation}$$
such that $$j^* i_* \colon \cZ \to U$$ is constant on the terminal object of $$U$$, and $$i^*, j^*$$ are jointly conservative.


In this case, we have a gluing functor $$i^* \circ j_* \colon U \to \cZ$$. This is a gluing functor because we can use it to glue $$\cZ$$ from $$U$$ and $$\cZ$$ using $$i^* \circ j_*$$. See Theorem 6.1.9 of [this notes](https://arxiv.org/abs/2109.12250)
<b>Theorem:</b>
Given a recollement of $$\cX$$ via full subcategories $$\cZ$$ and $$U$$, the following commutative square:
$$ \begin{equation}
\begin{array}[ccc]
        s \cX & \rightarrow & \mathrm{Fun}([1], \cZ) \\\
\downarrow j^* & & \downarrow \mathrm{target} \\\ 
        U & \xrightarrow{i^* j_*} & \cZ
\end{array}
\end{equation} $$
The top arrow takes $$x \in \cX$$ is the map $$i^*(x \to j_* j^* x)$$.

We see that objects in $$\cX$$ corresponds to a triplet $$(z \in \cZ, y \in U, \phi \colon z \to i^* j_* u)$$.
Therefore an object $$x \in \cX$$ corresponds to the triplet $$(i^* x \in \cZ, j^* x \in U, \phi \colon i^* x \to i^* j_* j^* x)$$. Furthermore, for any $$x \in \cX$$, we have a pullback square 
$$\begin{equation}
\begin{array}[ccc]
   x x & \rightarrow & j_*j^* x \\\ 
   \downarrow & & \downarrow \\\ 
   i_*i^* x & \rightarrow & i_*i^* j_*j^* x.
\end{array}
\end{equation}$$
Recollement allow us to construct objects and morphisms in $$\cX$$ via those in $$\cZ$$ and $$U$$ together with the gluing functor.

The following is the statement about how to construct a recollement. This is Proposition 6.1.21 from [this notes](https://arxiv.org/abs/2109.12250)
<b> Proposition:</b>Let $$\cX$$ be a stable $$\infty$$-category, and $$i_{*} \colon \cZ \to \cX$$ be a full subcategory. Suppose that $$i_{*}$$ admits a left adjoint $$i^*$$ and a right adjoint $$i^!$$, then:
1. The icnlusion $$\cZ^{\perp} \subset \cX$$ admits a left adjoint $$j^{\perp} \colon \cX \to \cZ^{\perp}$$ defined by 
\begin{equation}
j^{\perp}\coloneqq \mathrm{cofib}(i_* i^! \to \id).
\end{equation}
2. The inclusion $${^{\perp}\cZ} \subset \cX$$ admits a right adjoint $$^{\perp}j \colon X \to{ ^{\perp}\cZ}$$ defined by 
\begin{equation}
^{\perp}j \coloneqq \mathrm{fib}(id \to i^*i_*).
\end{equation}
3. The composite functoors 
\begin{equation}
Z^{\perp} \hookrightarrow X \xrightarrow{^\perp j} {^{\perp}Z }\quad \mathrm{and} \quad 
{^{\perp}Z} \hookrightarrow X \xrightarrow{^{\perp} j} Z^{\perp}
\end{equation}
are inverses of $$\infty$$-categories.
4. $$\cZ$$ is the recollement of the stable subcategories $$Z$$ and $$Z^{\perp}$$.


## Recollement for differential cohomology
Here we apply recollement to differential cohomology, and more generally $$\cC$$-valued sheave on $$\Mfld$$, where $$\cC$$ is presentable and stable.
In the setting above, $$\cX$$ is $$\Sh(\Mfld; \cC)$$ and $$\cZ$$ is $$\Sh_{\mbb{R}}(\Mfld; \cC) \simeq \cC$$. As we describe above, the inclusion functor $$\Gamma^*$$ has left adjoint $$\Gamma_{\#}$$ and right adjoint $$\Gamma_*$$. This satisfies the criterion of the proposition above. Let us defined the $$U$$:
<b> Definition</b>:
A $$\cC$$-valued sheaf $$\cF$$  is **pure** if $$\cF$$ is right orthogonal to $$\Sh_{\mbb{R}}$$. We write $$\Sh_{\pu}(\Mfld; \cC)$$ for the full subcategory of pure sheaves.
Note that $$\cF$$ is pure if and only if $$\cF(*) = 0$$. Examples are $$\Omega^i$$ for $$i \geq 1$$. 

Now we are going to define the map $$\Cyc \colon \Sh(\Mfld; \cC) \to \Sh_{\pu}(\Mfld; \cC)$$, defined as the cofiber of 
$$R\cF \to \cF$$. Similarly, we define $$\Def \colon \Sh_{\pu}(\Mfld; \cC) \to \Sh(\Mfld; \cC)$$ given by the fiber of 
$$\cF \to L\cF$$.

To summarize, we get the following:
$$\begin{equation}
\begin{array}{ccccc}
& \xleftarrow{\Gamma_{\#}}&    & \xleftarrow{\Def}    &                  \\\
\Sh_{\mbb{R}}(\Mfld; \cC) & \xrightarrow{\Gamma^*} & \Sh(\Mfld; \cC)   &  \xrightarrow{\Cyc}  & \Sh_{\pu}(\Mfld; \cC)     \\\
& \xleftarrow{\Gamma_*} &     &    \leftarrow               & 
\end{array}
\end{equation}$$

Furthermore, using the decomposition, we see that $$\Sh(\Mfld; \cC)$$ is the $$\infty$$-category of triples 
$$ (E_{\mbb{R}}, E_{\pu}, \phi \colon E_{\mbb{R}} \to L E_{\pu})$$, where $$E_{\mbb{R}}$$ is a $$\mbb{R}$$-invariant sheaf, $$E_{\pu}$$ is a pure sheaf, and $$\phi$$ is any morphism. For a sheaf $$\cF$$, it corresponds to $$(L\cF, \Cyc \cF, L\cF \to L \Cyc \cF)$$.

Furthermore, let us denote the composite $$\Def(\cF) \to \cF \to \Cyc(\cF)$$ as $$d$$.



## Differential Hexagons
Finally we are ready for the differential hexagon!!!
Let $$\cF$$ be a $$\cC$$-valued sheaf on $$\Mfld$$. Then we have the differential Hexagon hexagon:
$$\begin{equation}\label{eq:diff-hex-0}
\begin{array}{ccccccccc}
&   & R\cF &    &    &   & L\cF &  &  \\\
& \nearrow& & \searrow   & & \nearrow & & \searrow & \\\
\Sigma^{-1}L\Cyc(\cF) &  & & & \cF & & & & L\Cyc(\cF)\\\
& \searrow& & \nearrow   & & \searrow & & \nearrow & \\\
&   & \Def(\cF) & & & &  \Cyc(\cF) &  & 
\end{array}
\end{equation}$$
Here the diagonals are fiber sequences, top and bottoms rows four maps are fiber sequences (plus one more term), and both squares are pullback square. In particular the right square is precisely the pullback square that's needed to glue.

## Returning to ordinary differential cohomology!