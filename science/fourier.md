# Fourier structure of shares and leaked bits

The security proof has two different Fourier expansions. Additive characters of $`\mathbb F_p`$ describe the correlated share distribution. Characters of the binary output cube describe the leaked parities. Keeping their normalizations separate is useful: the input expansion identifies the terms that carry the secret, while the output expansion turns coefficient estimates into trace distance.

The notation and adversary model are fixed in [the model](model.md). The Fourier and MDS-code methods are established ingredients in leakage analysis; [related work](../references/RELATED_WORK.md) gives their provenance.

## 1. The sharing coset and its dual code

Let

```math
C_0=\operatorname{span}_{\mathbb F_p}
\left\{(\alpha_i^j)_{i=1}^n:1\le j\le t-1\right\},
\qquad C=C_0^\perp.
```

The share vector is uniform on $`s\mathbf1+C_0`$. For $`t\ge2`$, coordinatewise multiplication by $`\alpha_i^{-1}`$ turns $`C_0`$ into the evaluation code of polynomials of degree at most $`t-2`$. Consequently

```math
\dim C_0=t-1,
\qquad \dim C=r=n-t+1,
\qquad d(C)=t.
```

Here $`d(C)`$ is the smallest Hamming weight of a nonzero codeword. One direct argument is that every collection of $`t-1`$ columns of the parity-check matrix with entries $`\alpha_i^j`$, $`1\le j\le t-1`$, is independent: its determinant is a nonzero diagonal factor times a Vandermonde determinant. Thus no nonzero vector of weight below $`t`$ lies in $`C`$. The dimension and Singleton bound give equality. Equivalently, $`C`$ is an $`[n,r,t]`$ MDS code.

Projection of $`C`$ onto **any** $`r`$ coordinates is a bijection onto $`\mathbb F_p^r`$. Indeed, a codeword vanishing on those coordinates would have weight at most $`n-r=t-1`$, so it must vanish everywhere; the source and target have the same cardinality $`p^r`$.

For $`\omega=e^{2\pi i/p}`$ and $`k=(k_1,\ldots,k_n)\in\mathbb F_p^n`$, character orthogonality gives

```math
\mathbb E_{Y\mid s}\omega^{\langle k,Y\rangle}
=
\begin{cases}
\omega^{s\sum_i k_i},&k\in C,\\
0,&k\notin C.
\end{cases}
```

Only words in $`C`$ survive. A word with $`\sum_i k_i=0`$ is also independent of the secret. The bounds below safely overcount these additional cancelling terms by retaining all nonzero words. The general-threshold regimes have $`t\ge2`$; when $`t=1`$, $`C_0=\{0\}`$ and $`C=\mathbb F_p^n`$ directly.

## 2. Local observable Fourier coefficients

Represent device $`i`$ by its Hermitian contraction

```math
M_i(y)=P_i(0\mid y)-P_i(1\mid y),
\qquad -I\preceq M_i(y)\preceq I.
```

Define

```math
A_i(k)=\frac1p\sum_{y\in\mathbb F_p}\omega^{-ky}M_i(y),
\qquad
M_i(y)=\sum_{k\in\mathbb F_p}\omega^{ky}A_i(k).
```

Hermiticity and the triangle inequality imply

```math
A_i(-k)=A_i(k)^\dagger,
\qquad \|A_i(k)\|_\infty\le1.
```

Parseval is valid for these finite operator-valued sums:

```math
\sum_k A_i(k)^\dagger A_i(k)
=\frac1p\sum_y M_i(y)^2\preceq I.
```

It follows by expanding the left side and using $`\sum_k\omega^{k(y-z)}=p\,\mathbf1_{y=z}`$. The [network estimates](network_bounds.md) use this identity to obtain symmetric second- or fourth-moment budgets. No trace-norm Parseval identity is asserted.

## 3. Output parities with a quantum reference

For $`S\subseteq[n]`$, write $`\chi_S(b)=(-1)^{\sum_{i\in S}b_i}`$ and define an operator on $`E`$ by

```math
F_{S,E}(s)=\mathbb E_{Y\mid s}\operatorname{Tr}_D
\left[
\left(\bigotimes_{i\in S}M_i(Y_i)
\otimes I_{D_{S^c}}\otimes I_E\right)\rho_{DE}
\right].
```

The empty parity is $`F_{\varnothing,E}(s)=\rho_E`$. Using $`P_i(b_i\mid y_i)=[I+(-1)^{b_i}M_i(y_i)]/2`$ gives the exact cq expansion

```math
\Omega_s^{BE}
=2^{-n}\sum_b|b\rangle\langle b|\otimes
\sum_{S\subseteq[n]}\chi_S(b)F_{S,E}(s).
```

Trace norm adds over classical blocks. Applying the triangle inequality inside each block yields

```math
\Delta(s,s')
\le\frac12\sum_{S\subseteq[n]}
\|F_{S,E}(s)-F_{S,E}(s')\|_1.
```

The $`2^n`$ output strings exactly cancel the factor $`2^{-n}`$. This step is valid for arbitrary reference dimension. It is the output estimate used in the reference-secure general-threshold theorem.

Insert the local Fourier expansions. For $`k\in\mathbb F_p^n`$ with $`\operatorname{supp}k\subseteq S`$, set

```math
T_{S,E}(k)=\operatorname{Tr}_D
\left[
\left(\bigotimes_{i\in S}A_i(k_i)
\otimes I_{D_{S^c}}\otimes I_E\right)\rho_{DE}
\right].
```

The sharing character identity gives

```math
F_{S,E}(s)
=\sum_{\substack{k\in C\\\operatorname{supp}k\subseteq S}}
\omega^{s\sum_i k_i}T_{S,E}(k).
```

The zero word cancels between two secrets. Every remaining phase difference has modulus at most two, so

```math
\Delta(s,s')
\le\sum_{S\subseteq[n]}
\sum_{\substack{k\in C\setminus\{0\}\\\operatorname{supp}k\subseteq S}}
\|T_{S,E}(k)\|_1.
```

The phase factor two cancels the one half in the distance convention. This is the starting point of [the arbitrary-reference threshold bound](general_threshold.md).

## 4. The stronger scalar output estimate

Without an external quantum reference, $`F_S(s)`$ and $`T_S(k)`$ are scalars. If $`d_S=F_S(s)-F_S(s')`$, Cauchy–Schwarz over output strings and scalar Parseval give

```math
\begin{aligned}
\Delta(s,s')
&=\frac12\,2^{-n}\sum_b\left|\sum_S\chi_S(b)d_S\right|\\
&\le\frac12\left(\sum_S|d_S|^2\right)^{1/2}.
\end{aligned}
```

This retains a square-sum over output parities rather than their sum of norms. Minkowski's inequality can then move the sum over nonzero codewords outside that Euclidean norm. It produces the stronger no-reference general-threshold estimate. The reference-secure proof uses the preceding trace-norm triangle inequality instead.

## 5. Full threshold and additive coordinates

When $`t=n`$, Lagrange interpolation supplies nonzero coefficients

```math
\ell_i=\prod_{j\ne i}\frac{-\alpha_j}{\alpha_i-\alpha_j},
\qquad s=\sum_i\ell_iY_i.
```

Set $`X_i=\ell_iY_i`$. This is an invertible local change of each device's classical input. The vector $`X`$ is uniform on

```math
\left\{x\in\mathbb F_p^n:\sum_i x_i=s\right\}.
```

In these coordinates, the surviving input Fourier frequencies are diagonal words $`(k,\ldots,k)`$. Every proper subset of shares is uniform and independent of the secret. Summing out unobserved bit outcomes puts identity operators on those devices, so every proper output-parity operator is also secret independent, even in the presence of $`E`$. Only the full output parity contributes to the difference:

```math
\Delta(s,s')
=\frac12\|F_{[n],E}(s)-F_{[n],E}(s')\|_1.
```

The [full-threshold proof](full_threshold.md) exploits this exact equality and pairs frequencies $`k`$ and $`-k`$. General thresholds require the dual-code summation because more output parities can depend on the secret.

**Next:** [Network coefficient bounds](network_bounds.md), then [full threshold](full_threshold.md) or [general thresholds](general_threshold.md).
