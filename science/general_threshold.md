# Security below full threshold

At full threshold, only the parity of all leaked bits can depend on the secret. If $`t<n`$, several output parities can carry information. Their Fourier coefficients are nevertheless organized by an MDS code whose nonzero words have weight at least $`t`$. This minimum weight forces every secret-dependent term to use many small local Fourier coefficients.

The proof combines three established structures: the [share and output Fourier expansions](fourier.md), the [network coefficient bounds](network_bounds.md), and a weighted MDS Hölder inequality. The network estimate is where the independent-source assumption enters. The code inequality removes all dependence on the field size.

Throughout, $`p>n`$ is an odd prime, $`r=n-t+1`$, $`q=n/r`$, and $`\tau=t/n`$. Every bound applies to any two distinct secrets and may be clipped at one.

## 1. Arbitrary quantum side information

### Theorem: finite reference-secure bound

In the arbitrary-extension model, assume $`q\ge4`$. Then

```math
\Delta(s,s')\le
\min\left\{1,\inf_{\lambda\ge1}
\lambda^{-t}\left[2^q+2^{1-q/4}\lambda^q\right]^{n/q}
\right\}.
```

The constants are uniform over every source graph, all finite source and reference dimensions, all permitted local binary measurements, every prime $`p>n`$ and every choice of distinct nonzero evaluation points. The same statement holds under an actual classical shared seed satisfying the source condition branchwise.

For $`t<n`$, the infimum has the closed form

```math
\boxed{\quad
\Delta(s,s')\le
\min\left\{1,
2^{\,n-5t/4+(n-t+1)[\tau+h_2(\tau)]}
\right\},\quad}
```

where

```math
h_2(u)=-u\log_2u-(1-u)\log_2(1-u).
```

At $`t=n`$, interpret this expression by continuity, giving $`2^{1-n/4}`$. The separate [full-threshold result](full_threshold.md) improves this by the factor $`\cos(\pi/(2p))`$.

### Step 1: sum the reference-valued parity coefficients

Let $`\rho_i`$ be the device marginal before local processing and define

```math
b_i(k)=\mathrm{Tr}\!\left[\rho_i A_i(k)^\dagger A_i(k)\right],
\qquad
c_i(k)=\left[b_i(k)b_i(-k)\right]^{1/8}.
```

The arbitrary-reference coefficient lemma gives

```math
\|T_{S,E}(k)\|_1\le\prod_{i\in S}c_i(k_i),
\qquad c_i(-k)=c_i(k),
\qquad \sum_{k\in\mathbb F_p}c_i(k)^4\le1.
```

For a proper subset $`S`$, the proof places identity effects at vertices outside $`S`$; these vertices contribute one to the quantum Finner bound. No factorization of the reference is needed.

The trace-norm triangle estimate from [the Fourier expansion](fourier.md) now yields

```math
\Delta(s,s')
\le\sum_{k\in C\setminus\{0\}}
\prod_{i:k_i\ne0}c_i(k_i)
\prod_{i:k_i=0}\left[1+c_i(0)\right].
```

To see the zero-coordinate factor, fix $`k`$. Every $`i`$ with $`k_i\ne0`$ must belong to the output parity $`S`$, giving $`c_i(k_i)`$. A zero coordinate may be excluded, giving one, or included, giving $`c_i(0)`$. Summing the choices of $`S`$ therefore gives exactly the displayed product. The distance factor $`1/2`$ has already canceled the bound two on the difference of secret phases.

### Step 2: the imported MDS Hölder inequality

For any nonnegative functions $`g_i:\mathbb F_p\to[0,\infty)`$,

```math
\sum_{k\in C}\prod_{i=1}^ng_i(k_i)
\le\prod_{i=1}^n
\left(\sum_{z\in\mathbb F_p}g_i(z)^q\right)^{1/q},
\qquad q=\frac nr.
```

This is the MDS inequality of Horinaga–Yamakawa; the elementary coordinate-subset proof below also appears in Essayag–Zabokritskiy. Both the inequality and the minimum-distance weighting used next are inherited tools. See [related work](../references/RELATED_WORK.md) for exact source locations.

For completeness, let $`K`$ be uniform on $`C`$. There are $`N=\binom nr`$ subsets $`J`$ of size $`r`$, and each coordinate occurs in $`L=\binom{n-1}{r-1}`$ of them. Thus $`N/L=q`$ and

```math
\prod_i g_i(K_i)
=\prod_{|J|=r}\left(\prod_{i\in J}g_i(K_i)\right)^{1/L}.
```

Hölder with $`N`$ equal exponents gives

```math
\mathbb E_C\prod_i g_i(K_i)
\le\prod_{|J|=r}
\left[\mathbb E_C\prod_{i\in J}g_i(K_i)^q\right]^{1/N}.
```

Every $`r`$-coordinate projection is uniform on $`\mathbb F_p^r`$. Each expectation on the right factors into its $`r`$ singleton averages. Counting the $`L`$ occurrences of each coordinate leaves

```math
\mathbb E_C\prod_i g_i(K_i)
\le\prod_i\left[\frac1p\sum_zg_i(z)^q\right]^{r/n}.
```

Multiplying by $`|C|=p^r`$ cancels the field factors. The exponent $`q`$ need not be integral.

### Step 3: use minimum distance and paired fourth moments

For $`\lambda\ge1`$, set

```math
g_i(0)=1+c_i(0),
\qquad g_i(z)=\lambda c_i(z)\quad(z\ne0).
```

Every nonzero codeword has weight at least $`t`$. Consequently

```math
\Delta(s,s')
\le\lambda^{-t}\sum_{k\in C\setminus\{0\}}\prod_i g_i(k_i)
\le\lambda^{-t}\sum_{k\in C}\prod_i g_i(k_i).
```

Adding the zero codeword is an upper-bound relaxation. Because $`p`$ is odd, each nonzero frequency belongs to a distinct pair $`\{z,-z\}`$. The fourth-moment budget implies $`c_i(0)\le1`$ and $`c_i(z)\le2^{-1/4}`$ for $`z\ne0`$. For $`q\ge4`$,

```math
\sum_{z\ne0}c_i(z)^q
\le2^{1-q/4}\sum_{z\ne0}c_i(z)^4
\le2^{1-q/4}.
```

It follows that

```math
\sum_zg_i(z)^q
\le2^q+2^{1-q/4}\lambda^q.
```

The MDS inequality proves the finite theorem. The simultaneous upper bounds on the zero-frequency and nonzero-frequency budgets are deliberately loose; their validity does not require that a single measurement attain both.

### Step 4: optimize the finite bound

Put $`x=2^{1-5q/4}\lambda^q`$. The logarithm of the untruncated bound is

```math
n-\frac{5t}{4}+\frac tq
-\frac tq\log_2x+r\log_2(1+x).
```

For $`t<n`$, its derivative vanishes at $`x=t/(n-t)`$, giving

```math
\log_2\lambda_*
=\frac54+\frac rn
\left[\log_2\frac{t}{n-t}-1\right].
```

This value exceeds zero throughout the stated $`q\ge4`$ regime, so $`\lambda_*\ge1`$ is admissible. Substitution yields the boxed expression. When $`t=n`$, the infimum is the limit as $`\lambda\to\infty`$.

An especially simple, slightly weaker bound comes from $`\lambda=2^{5/4}`$:

```math
\Delta(s,s')\le
\min\left\{1,\ 2^{n-5t/4}\,3^{n-t+1}\right\}.
```

## 2. The reference-secure asymptotic regime

For a fixed reconstruction rate, the optimized exponent per device converges to

```math
E_{\rm ref}(\tau)
=1-\frac54\tau+(1-\tau)\left[\tau+h_2(\tau)\right].
```

On $`[3/4,1]`$ this function is strictly decreasing. Indeed,

```math
E_{\rm ref}'(\tau)
=-\frac14-2\tau-h_2(\tau)
+(1-\tau)\log_2\frac{1-\tau}{\tau}<0.
```

It is positive at $`3/4`$ and negative at one. Its unique zero in this interval is

```math
\tau_{\rm ref}^{\rm suff}=0.9042045924785356\ldots.
```

For any fixed $`\eta>0`$ with $`\tau_{\rm ref}^{\rm suff}+\eta\le1`$, there are $`c>0`$ and $`n_0`$ such that $`n\ge n_0`$ and $`t/n\ge\tau_{\rm ref}^{\rm suff}+\eta`$ imply $`\Delta\le2^{-cn}`$. The finite exponent differs from $`nE_{\rm ref}(\tau)`$ by $`\tau+h_2(\tau)`$, a bounded additive term. The rate condition also ensures $`q\ge4`$ for sufficiently large $`n`$.

For example:

| Shares $`n`$ | Threshold $`t`$ | Logarithm to base two of the optimized upper bound |
|---:|---:|---:|
| 1000 | 950 | $`-124.443755187\ldots`$ |

This is a bound in the declared mathematical model, uniform over $`p>n`$, rather than an implementation-specific parameter recommendation. The unknown optimal reconstruction threshold may be lower.

## 3. A stronger bound without a quantum reference

### Theorem: finite scalar bound

With no external quantum reference, let $`q\ge2`$. Then

```math
\Delta(s,s')\le
\min\left\{1,\inf_{\lambda\ge1}\lambda^{-t}
\max\left\{
\left[1+2^{1-q/2}\lambda^q\right]^{n/q},\ 2^{n/2}
\right\}\right\}.
```

An actual classical shared seed is still allowed. The theorem is proved branchwise and then averaged with the seed supplied to the adversary. The argument in this section is scalar and does not establish the same bound with a retained quantum reference.

### Proof

In a pure-source dilation, the network contraction supplies symmetric coefficients $`a_i(z)`$ satisfying

```math
|T_S(k)|\le\prod_{i\in S}a_i(k_i),
\qquad a_i(-z)=a_i(z),
\qquad\sum_z a_i(z)^2\le1.
```

The dilation and its local marginals are specified in [the network estimate](network_bounds.md); no weighted norm is silently identified across purification. Use the scalar output square-sum from [the Fourier account](fourier.md). Minkowski over nonzero words $`k\in C`$, followed by the phase bound two, gives

```math
\Delta(s,s')\le
\sum_{k\in C\setminus\{0\}}
\left(\sum_{S\supseteq\mathrm{supp}\,k}|T_S(k)|^2\right)^{1/2}.
```

The choices to include or exclude a zero-frequency site now occur inside a square root. Thus

```math
\Delta(s,s')\le
\sum_{k\in C\setminus\{0\}}
\prod_{i:k_i\ne0}a_i(k_i)
\prod_{i:k_i=0}\sqrt{1+a_i(0)^2}.
```

Apply the same minimum-distance weighting and MDS inequality, with $`g_i(0)=\sqrt{1+a_i(0)^2}`$ and $`g_i(z)=\lambda a_i(z)`$ for $`z\ne0`$. Write $`u_i=a_i(0)^2`$. Pairing the nonzero frequencies yields

```math
\sum_{z\ne0}a_i(z)^q
\le2^{1-q/2}(1-u_i)^{q/2},
\qquad q\ge2.
```

For example, group the squared mass of each opposite pair into $`w_j=2a_i(z_j)^2`$. Then $`\sum_jw_j\le1-u_i`$ and $`\sum_jw_j^{q/2}\le(\sum_jw_j)^{q/2}`$. This proves the displayed inequality.

The local moment is bounded by

```math
\sum_zg_i(z)^q
\le(1+u_i)^{q/2}
+2^{1-q/2}\lambda^q(1-u_i)^{q/2}.
```

This function of $`u_i\in[0,1]`$ is convex. Its maximum occurs at an endpoint and equals

```math
\max\left\{1+2^{1-q/2}\lambda^q,\ 2^{q/2}\right\}.
```

Taking the product of $`n`$ identical bounds to the power $`1/q`$ proves the theorem.

### Exact finite optimization and a sufficient asymptotic rate

For $`t<n`$, define

```math
\beta=2^{1-q/2},\qquad
x_0=\frac{2^{q/2}-1}{\beta},\qquad
x_* =\frac{\tau}{\beta(1-\tau)}.
```

The minimizing $`x=\lambda^q`$ is $`\max\{x_0,x_*\}`$. To verify this, below $`x_0`$ the constant term $`2^{n/2}`$ controls the maximum and the objective decreases. Above $`x_0`$, the logarithmic derivative of $`x^{-t/q}(1+\beta x)^{n/q}`$ changes sign at $`x_*`$. Also $`x_0\ge1`$ for $`q\ge2`$, so the domain restriction is satisfied. At $`t=n`$, the infimum is the limit $`\lambda\to\infty`$.

In the fixed-rate limit, $`q\to1/(1-\tau)`$. For $`\tau>3/4`$, equivalently $`q>4`$, the crossing point $`x_0`$ controls because $`2^{q/2}>q`$. Define

```math
L(\tau)=\tau+(1-\tau)
\log_2\!\left(1-2^{-1/[2(1-\tau)]}\right).
```

The resulting exponent per device is

```math
E_0(\tau)=\frac12-\tau L(\tau).
```

On $`(3/4,1)`$, $`L`$ is positive and strictly increasing: its first term increases, and differentiating its second term also gives a positive derivative. Hence $`E_0`$ is strictly decreasing. Its zero is

```math
\tau_0^{\rm suff}=0.756935255576482\ldots.
```

Every fixed positive margin above this value gives exponential secrecy without an external quantum reference, for sufficiently large $`n`$. All finite evaluations retain $`q=n/(n-t+1)`$; replacing it by $`1/(1-\tau)`$ is justified only in the asymptotic statement. The finite optimizer, roots and example values are reproduced by [the verification script](../verification/README.md).

## 4. What the thresholds express

The two rates come from different output and network estimates. A retained quantum reference is controlled by trace-norm duality and state Cauchy–Schwarz, which lead to fourth moments and a sum of parity norms. Without that reference, a second-moment network bound and a scalar square-sum over parities are available. These differences explain the two sufficient regimes; they do not establish a matching separation between the optimal rates.

The source graph disappears from both final bounds because weight $`1/2`$ at every vertex is a valid fractional independent set for every bipartite-source graph. The graph can therefore be dense even though the secret-dependent Fourier terms remain small. The comparison with independent-set reductions is developed in [related work](../references/RELATED_WORK.md).

**Related:** [Exact full-threshold result](full_threshold.md) · [Resource boundaries](boundaries.md) · [Finite verification](../verification/README.md).
