---
layout: post
title: Being confused about differential cohomology III 
date: 2024-08-07
description: Building differential cohomology
tags: mathematics, mathematical-physics
categories:
---

Welcome to part III of being confused. We are going to construct differential cohomologies using the recollement machinary from the previous post. To start we will follow section 7 of [this notes](https://arxiv.org/abs/2109.12250). Let $$E$$ be a (topological) cohomology theory:
1. Choose a pure sheaf $$\hat{P}$$, i.e., a sheaf $$\hat{P}$$ with $$\hat{P}(*) = 0$$.
2. Compute $$\Gamma_{\#}(\hat{P}) = |\hat{P}(\Delta_{\mathrm{alg}}^{\buleet})$$.
3. Define a map $$f \colon E \to \Gamma_{\#}\hat{P}$$.
Then we simply construct $$\hat{E}$$ by the pullback procedure from last time.


<b>Example: trivial case.</b> take $$\hat{P} = 0$$ thus $$\Gamma_{\#}(\hat{P}) = 0$$. Then the differential refinement is just the constant sheaf $$\Gamma^*(E)$$.

<b>Example: Ordinar differential cohomology</b> Consider the de Rham complex $$\Omega^*$$, say viewed as a sheaf with valued in the derived $$\infty$$-category $$D(\mbb{R})$$. Note that $$\Omega^k$$ is in degree $$-k$$. By the de Rham theorem, the spectra $$\Omega^*$$ is equivalent to the constant discrete sheaf $$\mbb{R}_{\disc}$$, concentrated in degree $$0$$. Thus $$\Omega^* \simeq \Gamma^*H\mbb{R}$$. Therefore it is not pure and is a $$\mbb{R}$$-invariant sheaf. In particular, the purification $$\Cyc(\Omega^*)$$ is a $$0$$. For $$k \in \mbb{N}$$, let $$\Omega^{\geq k}$$ denote the stunted piece where we kill everything in degrees less than $$k$$. Note that $$\Omega^{\geq k}(*) = 0$$ thus $$\Gamma_* \Omega^{\geq k}$$ for $$k \geq 1$$, thus it is in fact a pure sheaf!

Therefore can compute $$\Gamma_{\#}(\Omega^{\geq k})$$:
<b>Lemma</b>For any $$k \geq 0$$, there is an equivalence $$\Gamma_{\#}\Omega^{\geq k} \simeq H\mbb{R}$$.
<b>Proof</b>This holds for $$k = 0$$. For the higher case, it suffices to show that $$\Gamma_{\#}\Omega^k = 0$$ for $$k \geq 1$$, which we will not prove here.

Now we can define $$H\mbb{Z}(k)$$ as the differential refinment of $$H\mbb{Z}$$ corresponding to the pair $$(\Omega^{\geq k}, H\mbb{Z} \to H\mbb{R} = \Gamma_{\#}\Omega^{\geq k})$$. It is straightforward to check this agrees with the definition that we gave in [the first post](???).

<b>Example: differential $$K$$-theory</b>:
Now we are finally ready to define some other differential cohomology theories haha.
Let $$V$$ be a graded $$\mbb{R}$$ vector space, viewed as an element in $$D(\mbb{R})$$, hence spectra. Let $$\Omega^{\geq k}(V)$$ the sheave of de Rham forms with $$V$$ coefficients. Note that the total degree is the sum of the differential form degree plus the $$V$$ graiding. 
For $$k \geq 0$$, we have 
$$$\Gamma_{\#}\Omega^{\geq k}(V) \simeq V$$$; furthermore, for $$k \geq 1$$, the sheaf $$\Omega^{\geq k}(V)$$ is a pure sheaf.


Now we have to define a connecting morphism, in this case is the **Chern character** $$\ch$$:
$$\begin{equation}
\ch \colon KU \to  \mbb{R}[u^{\pm 1}],
\end{equation}$$
with $$u$$ in degree $$2$$.
This allows us to define the differential refinement $$\hat{KU}(k)$$ of $$KU$$ defined by $$(\Omega^{\geq k}[u^{\pm 1}], KU \to \mbb{R}[u^{\pm 1}] \simeq \Gamma_{\#}\Omega^{\geq k}[u^{\pm 1}])$$.

Similarly, given the Pontryagin character $$\ch_o \colon KO \to \mbb{R}[\beta^{\pm 1}]$$ with $$\beta$$ in degree $$4$$. This defines a differetial refinments $$\widehat{KO}(k)$$ of $$KO$$.

More generally, given any spectrum $$E$$, then $$E_{\mbb{R}} \coloneqq E \otimes H\mbb{R} \simeq H(E^* \otimes \mbb{R})$$, where $$E^* = \pi_{-*} E$$ is the homotopy group, viewed as a graded abelian groups.
Then $$(\Omega^{\geq k})(E^*_{\mbb{R}})$$ together with the map $$E_{\mbb{R}} \to E_{\mbb{R}} \simeq 
\Gamma_{\#}(\Omega^{\geq k})(E^*_{\mbb{R}})$$ defines a differential refinement $$\hat{E}(k)$$ of $$E$$. 


