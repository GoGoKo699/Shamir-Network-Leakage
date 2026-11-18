# Security below full threshold

Let $`t`$ be the number of Shamir shares needed to reconstruct a secret distributed to $`n`$ devices. Each device emits one classical bit. The adversary receives all the bits and can hold an arbitrary quantum extension of the independent bipartite-source device marginal. The [model](model.md) specifies the source and communication assumptions.

The support-only estimate in [the network proof](network_bounds.md#4-second-moments-with-an-arbitrary-external-reference) gives two results. An elementary inequality for the dual sharing code gives a finite bound. Weighted list recovery gives the sharp leading exponent at every reconstruction rate a fixed margin above one half.

Throughout, $`p>n`$ is an odd prime, $`C`$ is the dual sharing code, $`r=n-t+1`$ is its dimension, and $`q=n/r`$. The [Fourier account](fourier.md#1-the-sharing-coset-and-its-dual-code) proves that $`C`$ is MDS with minimum nonzero weight $`t`$. All bounds apply to every pair of distinct chosen secrets and all allowed finite source and reference dimensions. Genuine classical flags are handled branchwise as in the [network proof](network_bounds.md#6-conditioning-on-actual-classical-randomness).

## 1. Explicit finite bound

Write $`\gamma_p=\cos(\pi/(2p))`$. If $`q\ge2`$, then

```math
\Delta(s,s')
\le \min\left\{1,\,
\gamma_p\inf_{\lambda\ge1}\lambda^{-t}
\left[\left(1+2^{1-q/2}\lambda^q\right)^r-1\right]
\right\}.
```

*Equation (1.1).*

One directly computable choice is $`\lambda=\sqrt 2`$, which gives $`\gamma_p\,2^{-t/2}(3^r-1)`$, clipped at one. A second closed-form bound, valid for $`t\lt n`$ and $`q\ge2`$, follows by dropping the minus one in (1.1). With $`\tau=t/n`$ and $`h_2(u)=-u\log_2 u-(1-u)\log_2(1-u)`$, it is

```math
\Delta(s,s')
\le \min\left\{1,\,
\gamma_p 2^{-t/2+r[\tau+h_2(\tau)]}\right\}.
```

*Equation (1.2).*

For example, at $`n=1000`$ and $`t=950`$, (1.2) is below $`2^{-411.94}`$ for all primes $`p>n`$. At full threshold the choice $`\lambda=\sqrt 2`$ in (1.1) already recovers the [exact even-size bound](full_threshold.md#1-the-exact-law-for-even-size).

### MDS Hölder and minimum-distance weighting

For nonnegative functions $`g_i:\mathbb F_p\to[0,\infty)`$ the inherited MDS Hölder inequality is

```math
\sum_{k\in C}\prod_{i=1}^n g_i(k_i)
\le\prod_{i=1}^n
\left(\sum_{z\in\mathbb F_p}g_i(z)^q\right)^{1/q}.
```

*Equation (1.3).*

To see this, let $`\mathcal I`$ be the family of all $`r`$-coordinate sets and $`L=|\mathcal I|`$. Each coordinate occurs in $`Lr/n`$ sets, so the integrand equals the product over $`I\in\mathcal I`$ of $`\left[\prod_{i\in I}g_i(k_i)^q\right]^{1/L}`$. Hölder with $`L`$ equal exponents gives one sum over $`C`$ for each $`I`$. Since projection onto $`I`$ is a bijection, that sum factors as $`\prod_{i\in I}\sum_z g_i(z)^q`$. Counting the occurrences of each coordinate yields (1.3).

Use the local weights $`h_i`$ from the [support-only estimate](network_bounds.md#4-second-moments-with-an-arbitrary-external-reference). Set $`g_i(0)=1`$ and $`g_i(z)=\lambda h_i(z)`$ for $`z\ne0`$. When $`q\ge2`$, the cap and second-moment budget give

```math
\sum_{z\ne0} h_i(z)^q
\le 2^{1-q/2}\sum_{z\ne0} h_i(z)^2
\le 2^{1-q/2}.
```

*Equation (1.4).*

Every nonzero word has at least $`t`$ nonzero coordinates. Its product of $`g_i`$ exceeds or equals $`\lambda^t`$ times its original weight, and the zero word contributes exactly one. Thus (1.3) bounds the sum in the support-only estimate by

```math
\lambda^{-t}\left[\left(1+2^{1-q/2}\lambda^q\right)^r-1\right].
```

*Equation (1.5).*

This proves (1.1). To obtain (1.2), let $`x=\lambda^q`$ and $`\beta=2^{1-q/2}`$ and minimize $`x^{-t/q}(1+\beta x)^r`$. The minimum for $`t\lt n`$ occurs at $`x=\tau/[(1-\tau)\beta]\ge1`$. Substitution gives $`2^{r[h_2(\tau)+\tau\log_2\beta]}=2^{-t/2+r[\tau+h_2(\tau)]}`$. The condition $`q\ge2`$ ensures $`\beta\le1`$ and $`\tau>1/2`$.

## 2. Sharp exponent above one half

Fix $`0\lt \eta\lt 1/2`$. There are constants $`A_\eta>0`$, $`b_\eta>0`$ and $`n_\eta`$ such that for $`n\ge n_\eta`$ and $`t/n\ge1/2+\eta`$, the following holds for every allowed prime, evaluation set and pair of distinct secrets. If $`\Delta_{\max}(s,s')`$ denotes the supremum over allowed graphs, source states, extensions and local strategies, then

```math
\sqrt{2}\,\gamma_p\,2^{-t/2}
\le \Delta_{\max}(s,s')
\le A_\eta n^{b_\eta}2^{-t/2}.
```

*Equation (2.1).*

Equivalently, $`-\log_2\Delta_{\max}(s,s')=t/2+O_\eta(\log n)`$. The constants are uniform in $`p`$ and the evaluation points. The upper bound applies on every prescribed graph, including the complete graph. The lower bound uses a Bell-pair matching on reconstruction positions, which is available when optimizing over graphs.

### Upper bound from weighted list recovery

The support-only sum has weights with $`h_i(z)\le c=2^{-1/2}`$ for $`z\ne0`$ and $`\sum_{z\ne0}h_i(z)^2\le1`$. The zero coordinate has weight one in the code sum. This puts the sum into the form of the Sun–Wootters weighted estimate given by [Essayag–Zabokritskiy, Lemma 3.5](https://arxiv.org/abs/2610.06350v2), using the primal code $`C_0`$ of dimension $`t-1`$ and fixed rate margin. The following singleton argument, using the same bounded-list method, gives a prefactor times $`c^t`$.

The dual code $`C`$ is also generalized Reed–Solomon. Indeed, writing $`P(X)=\prod_j(X-\alpha_j)`$, its words are $`k_i=f(\alpha_i)/(\alpha_iP'(\alpha_i))`$ with $`\deg f\lt r`$. These vectors are orthogonal to $`C_0`$ by the Lagrange leading-coefficient identity, since $`\sum_i u(\alpha_i)/P'(\alpha_i)=0`$ for $`\deg u\le n-2`$. The vectors span a space of dimension $`r`$, so they give the whole dual code.

Work with weights $`w_i`$ that equal $`h_i`$ away from zero and satisfy $`w_i(0)=1`$. Put $`\epsilon=\eta/2`$ and take $`n`$ large enough that $`r\le(1/2-\epsilon)n`$ and $`m=\lfloor\epsilon n\rfloor\ge\epsilon n/2`$. Fix $`0\lt \theta\lt c`$ so that $`2\sqrt{2}\,\theta^{\epsilon/2}\le c`$. Call a coordinate small when $`k_i\ne0`$ and $`w_i(k_i)\le\theta`$.

- **Fewer than $`m`$ small coordinates.** The word agrees with the lists $`\{0\}\cup\{z\ne0:w_i(z)>\theta\}`$ on at least $`n-m`$ positions. Each list contains at most $`1+\theta^{-2}`$ symbols by the squared-weight budget. Agreement exceeds the code rate by at least $`1/2`$, since $`n-m\ge r+n/2`$. The field-uniform bounded-list Reed–Solomon estimate of [Jeronimo, Theorem 1.1 and Corollary 8.1](https://eccc.weizmann.ac.il/report/2026/169/) gives at most $`A_\eta' n^{b_\eta}`$ such words. Dividing each list by its fixed nonzero column multiplier transfers the bound to this generalized Reed–Solomon code. Each nonzero word contributes at most $`c^t`$ by minimum distance.
- **At least $`m`$ small coordinates.** Mark a set of $`m`$ such coordinates and sum over all possible marked sets. For each marked set, extract $`\theta^m`$ from these weights. At least $`2r`$ unmarked positions remain. Choose two disjoint information sets of size $`r`$ there and drop the factors outside them, each at most one. Cauchy–Schwarz over codewords, the two projection bijections, and $`\sum_z w_i(z)^2\le2`$ bound the sum of the two information-set products by $`2^r`$. There are at most $`2^n`$ choices of marked set. The total is thus at most $`2^n\theta^m2^r\le c^n\le c^t`$.

Combining these estimates with the support-only bound proves the upper bound in (2.1). The bounded-list theorem is the imported coding input. The reduction to a support-only sum is where the independent-source quantum model enters.

### Lower bound from reconstruction positions

Choose any $`t`$ evaluation positions and let all other devices emit constants. The selected evaluations of a polynomial of degree below $`t`$ determine it, and fixing its constant term fixes one linear relation with nonzero reconstruction coefficients. Rescaling each selected share by its coefficient gives $`t`$ uniform additive shares of the same secret.

On these positions, the [Bell-pair construction](full_threshold.md#4-bell-pair-attainment) gives distance $`2^{1-t/2}\gamma_p`$ for even $`t`$. For odd $`t\ge3`$ it uses $`(t-1)/2`$ pairs and one deterministic bit. Its distance is at least $`2^{-(t-1)/2}\gamma_p`$ by (4.8) of the full-threshold proof. Both yield the lower bound in (2.1). The convention of choosing the challenge pair before selecting a strategy is the one in [the model](model.md#4-security-convention).

## 3. Scope

The sufficient-rate guarantee is asymptotic at a fixed gap above one half, so (2.1) gives no explicit onset as the gap shrinks. The finite estimate (1.1) has explicit constants and can be used directly whenever it is useful. The exact full-threshold statement covers even device counts, and the asymptotic exponent covers both parities.

The result concerns one classical bit per device and the literal independent bipartite-source marginal. See [resource boundaries](boundaries.md) for coherent mixtures, communication and other leakage outputs. The [earlier released proof](https://github.com/GoGoKo699/Shamir-Network-Leakage/blob/f3452b19e8a91f5de80d1e754d865a3097dcc999/science/general_threshold.md) records the fourth-moment estimate and its sufficient rate near 90.42 percent for arbitrary references.

**Related:** [Full-threshold law and Bell-pair attainment](full_threshold.md) · [Network proof](network_bounds.md) · [Related work](../references/RELATED_WORK.md).
