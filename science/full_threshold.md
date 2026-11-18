# Full-threshold secrecy and the matching Bell-pair attack

At full threshold, every proper subset of shares is independent of the secret. The only output parity that can depend on it is the parity of all leaked bits, even in the presence of a quantum reference. Independent Bell pairs attain the resulting trace-distance bound when the number of devices is even, also when the adversary is allowed an arbitrary extension of the independent-source device marginal.

## 1. The exact law for even size

Let $`p>n`$ be an odd prime and consider $`(n,n)`$ Shamir sharing at distinct nonzero evaluation points. Every device emits one classical bit by a local binary measurement. The sources are independent of the shared secret and the sharing randomness, and the devices make their measurements without communicating. The adversary receives all bits and retains the reference $`E`$. See [the model](model.md) for the full resource assumptions.

### Theorem 1.1: full-threshold distance with arbitrary references

Suppose the device marginal is a literal tensor product of independent bipartite-source states and $`\rho_{DE}`$ is any extension. For $`n\ge2`$ and each pair $`s\ne s'`$,

```math
\boxed{\quad
\Delta(s,s')=\frac12\Vert \Omega_s^{BE}-\Omega_{s'}^{BE}\Vert _1
\le 2^{1-n/2}\cos\!\left(\frac{\pi}{2p}\right).
\quad}
```

*Equation (1.1).*

The extension may hold all source purifications and be processed collectively. The bound is uniform in the graph, the source dimensions and the finite reference dimension. Actual classical shared flags are allowed when the source condition holds in each branch.

For every even $`n`$, independent Bell pairs on a perfect matching attain equality, with a trivial reference. Thus (1.1) is the exact maximum over permitted graphs and strategies. It is also attained on any prescribed graph that contains a perfect matching when sources may be chosen freely and other edges ignored. For odd $`n\ge3`$, Section 4 gives a lower bound within a universal constant factor of the upper bound.

## 2. Additive coordinates and the single relevant parity

At full threshold, the [Lagrange change of coordinates](fourier.md#5-full-threshold-and-additive-coordinates) gives nonzero coefficients $`\ell_i`$ such that

```math
X_i=\ell_iY_i,
\qquad
\sum_{i=1}^nX_i=s.
```

*Equation (2.1).*

The vector $`X`$ is uniform on this affine hyperplane. Indeed, evaluation of a polynomial of degree at most $`n-1`$ at the $`n`$ distinct points is invertible. Fixing its constant coefficient imposes exactly the displayed linear equation. Multiplication by each $`\ell_i\ne0`$ is an invertible local relabelling, so it leaves the set of possible leakage strategies unchanged.

For this page, write $`M_i(x)`$ for the rescaled measurement family: it is the original family evaluated at $`\ell_i^{-1}x`$. Define its Fourier coefficients by

```math
A_i(k)=\frac1p\sum_{x\in\mathbb F_p}\omega^{-kx}M_i(x),
\qquad \omega=e^{2\pi i/p}.
```

*Equation (2.2).*

For $`S\subseteq[n]`$, let

```math
F_{S,E}(s)
=\mathbb E_{X\mid\sum_iX_i=s}
\mathrm{Tr}_D\!\left[
\left(\bigotimes_{i\in S}M_i(X_i)
\otimes I_{D_{S^c}}\otimes I_E\right)\rho_{DE}
\right].
```

*Equation (2.3).*

This is an operator on the adversary's reference. Expanding the binary POVMs gives the exact output-parity identity

```math
\Omega_s^{BE}
=2^{-n}\sum_{b\in\{0,1\}^n}|b\rangle\langle b|\otimes
\sum_{S\subseteq[n]}(-1)^{\sum_{i\in S}b_i}F_{S,E}(s).
```

*Equation (2.4).*

If $`S`$ is proper, the marginal $`X_S`$ is uniform on $`\mathbb F_p^{|S|}`$ independently of $`s`$. The operator inside the average in (2.3) depends only on $`X_S`$. Consequently $`F_{S,E}(s)`$ is independent of the secret for every proper $`S`$. This reasoning does not assume the reference is uncorrelated with the devices. The identity operators on complementary devices arise from summing their outcome probabilities; operations whose outputs are not retained cannot signal to $`E`$.

Put $`F_E(s)=F_{[n],E}(s)`$. All proper parity terms cancel between two secrets, leaving

```math
\Omega_s^{BE}-\Omega_{s'}^{BE}
=2^{-n}\sum_b(-1)^{\sum_i b_i}|b\rangle\langle b|
\otimes\bigl[F_E(s)-F_E(s')\bigr].
```

*Equation (2.5).*

Trace norm is additive over classical blocks. There are $`2^n`$ blocks with equal norm, so the factor $`2^{-n}`$ cancels exactly:

```math
\Delta(s,s')=\frac12\Vert F_E(s)-F_E(s')\Vert _1.
```

*Equation (2.6).*

This exact reduction takes advantage of full threshold. The general bound uses the full classical outcome record and sums the zero-frequency effects for each dual codeword.

## 3. Fourier proof and the finite-prime factor

The Fourier inverse is $`M_i(x)=\sum_k\omega^{kx}A_i(k)`$. Uniform averaging on the hyperplane $`\sum_iX_i=s`$ annihilates every frequency vector except a diagonal vector $`(k,\ldots,k)`$. One may check this directly by substituting $`X_n=s-\sum_{i\lt n}X_i`$ and averaging the remaining coordinates independently. Thus

```math
F_E(s)=\sum_{k\in\mathbb F_p}\omega^{ks}T_E(k),
\qquad
T_E(k)=\mathrm{Tr}_D\!\left[
\left(\bigotimes_{i=1}^n A_i(k)\otimes I_E\right)\rho_{DE}
\right].
```

*Equation (3.1).*

The zero frequency cancels in the difference. Equations (2.6) and (3.1) imply

```math
\Delta(s,s')
\le\frac12\sum_{k\ne0}
|\omega^{ks}-\omega^{ks'}|\,\Vert T_E(k)\Vert _1.
```

*Equation (3.2).*

For any nonzero residue $`j\in\mathbb F_p`$,

```math
\frac12|1-\omega^j|
=\left|\sin\!\left(\frac{\pi j}{p}\right)\right|
\le\cos\!\left(\frac{\pi}{2p}\right).
```

*Equation (3.3).*

The maximum is reached at $`j=(p-1)/2`$ or $`j=(p+1)/2`$, since $`p`$ is odd. For $`s\ne s'`$ and $`k\ne0`$, the residue $`k(s-s')`$ is nonzero. Substitution in (3.2) gives

```math
\Delta(s,s')
\le\cos\!\left(\frac{\pi}{2p}\right)
\sum_{k\ne0}\Vert T_E(k)\Vert _1.
```

*Equation (3.4).*

The [arbitrary-reference second moments](network_bounds.md#4-second-moments-with-an-arbitrary-external-reference) give

```math
\Vert T_E(k)\Vert _1\le\prod_i h_i(k),
\qquad
h_i(-k)=h_i(k),
\qquad
\sum_{k\in\mathbb F_p}h_i(k)^2\le1.
```

The [paired-frequency lemma](network_bounds.md#5-pairing-the-nonzero-frequencies) with moment order two and $`n\ge2`$ yields

```math
\sum_{k\ne0}\Vert T_E(k)\Vert _1
\le\sum_{k\ne0}\prod_i h_i(k)
\le 2^{1-n/2}.
```

*Equation (3.5).*

Combining (3.4) and (3.5) proves Theorem 1.1's upper bound. $`\square`$

## 4. Bell-pair attainment

Let $`n=2m`$. Pair the devices as $`(1,2),(3,4),\ldots,(2m-1,2m)`$, and supply the independent Bell states

```math
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}.
```

There is no adversary reference. Fix a nonzero $`k\in\mathbb F_p`$ and real phases $`\phi_i`$. On additive share $`x`$, device $`i`$ measures the equatorial observable

```math
M_i(x)
=\cos\!\left(\frac{2\pi kx}{p}+\phi_i\right)\sigma_x
+\sin\!\left(\frac{2\pi kx}{p}+\phi_i\right)\sigma_y,
```

*Equation (4.1).*

where $`\sigma_x,\sigma_y`$ are the Pauli matrices. It reports bit $`b_i`$ when the eigenvalue is $`(-1)^{b_i}`$. This is a binary projective measurement and releases exactly one classical bit.

The single-site marginal of $`|\Phi^+\rangle`$ is maximally mixed. Also

```math
\langle\Phi^+|
(\cos\theta\,\sigma_x+\sin\theta\,\sigma_y)
\otimes(\cos\theta'\,\sigma_x+\sin\theta'\,\sigma_y)
|\Phi^+\rangle
=\cos(\theta+\theta').
```

*Equation (4.2).*

For a parity that contains exactly one endpoint of some pair, its conditional expectation is zero. A parity that is a union of complete pairs has expectation equal to the product of the corresponding cosines. If that union is nonempty and proper, averaging over the additive shares makes it zero: its Fourier expansion has a nonzero frequency at selected coordinates and zero at an omitted coordinate, so no diagonal frequency vector survives.

For the full parity, expand the product over all $`m`$ pairs. Each cosine contributes two Fourier terms, with signs $`+1`$ and $`-1`$. Only the choice of all plus signs and the choice of all minus signs give a diagonal frequency vector. They are distinct because $`p`$ is odd and $`k\ne0`$. Writing $`\Phi=\sum_i\phi_i`$, the full parity expectation is therefore

```math
F(s)=2^{-m}\left(e^{i\Phi}\omega^{ks}+e^{-i\Phi}\omega^{-ks}\right)
=2^{1-m}\cos\!\left(\frac{2\pi ks}{p}+\Phi\right).
```

*Equation (4.3).*

All nonempty proper output parities vanish, so the complete output distribution is

```math
P_s(b)
=2^{-n}\left[
1+(-1)^{\sum_i b_i}\,2^{1-m}
\cos\!\left(\frac{2\pi ks}{p}+\Phi\right)
\right].
```

*Equation (4.4).*

Using the parity reduction or summing the classical probabilities directly gives

```math
\begin{aligned}
\Delta(s,s')
&=\frac12|F(s)-F(s')|\\
&=2^{1-m}
\left|\sin\!\left(\frac{\pi k(s-s')}{p}\right)\right|
\left|\sin\!\left(\frac{\pi k(s+s')}{p}+\Phi\right)\right|.
\end{aligned}
```

*Equation (4.5).*

Because $`p`$ is prime and $`s-s'\ne0`$, choose $`k`$ so that

```math
k(s-s')=\frac{p-1}{2}\pmod p.
```

Then the first sine in (4.5) has magnitude $`\cos(\pi/(2p))`$. Choose the total phase $`\Phi`$ so that the second sine has magnitude one; a single device can supply the required phase. The state and measurements depend only on the prescribed pair of challenge secrets, as allowed in the [security convention](model.md#4-security-convention). They do not depend on which secret was shared. The resulting distance is exactly

```math
\Delta(s,s')
=2^{1-n/2}\cos\!\left(\frac{\pi}{2p}\right).
```

*Equation (4.6).*

The Bell matching is available in both reference models. It attains the arbitrary-reference upper bound in Theorem 1.1.

### Odd device counts

Let $`n=2m+1\ge3`$. Keep the construction on $`2m`$ paired devices and let the unpaired device report the sign of $`\cos(2\pi kx/p)`$ as its bit. Its normalized coefficient at $`k`$ equals the real number

```math
c_k=\frac1p\sum_{x\in\mathbb F_p}|\cos(2\pi kx/p)|
\ge\frac1p\sum_{x\in\mathbb F_p}\cos^2(2\pi kx/p)
=\frac12.
```

*Equation (4.7).*

For the coefficient equality, multiply the sign by $`\omega^{-kx}`$ and pair $`x`$ with $`-x`$ to cancel the imaginary part. At least one Bell pair is present, and all its contributing frequencies are $`\pm k`$. The diagonal-word condition then evaluates the single unpaired coefficient at those frequencies. Thus (4.3) holds with the extra factor $`c_k`$. Using the same challenge-dependent phase choice as in (4.5) gives

```math
\Delta(s,s')
=2^{1-m}c_k\cos\!\left(\frac{\pi}{2p}\right)
\ge 2^{-(n-1)/2}\cos\!\left(\frac{\pi}{2p}\right).
```

*Equation (4.8).*

The [general-threshold lower bound](general_threshold.md#lower-bound-from-reconstruction-positions) applies these constructions on any selected reconstruction set.

## 5. Scope, dependencies, and verification

The proof uses the independent-source condition at the resource snapshot, before operations that are absorbed into the local measurements. Unrestricted communicating preparation can turn a collection of Bell pairs into a multipartite resource and need not preserve this condition. The [boundary examples](boundaries.md) give the relevant counterexamples. Similarly, one classical bit is the output restriction used by the parity expansion. No corresponding claim about a leaked qubit, repeated leakage, or a later release of the device registers follows from this proof.

The network inequalities used in Section 3 are inherited from the graph-contraction and quantum Finner literature, with the precise sources and the required complex-operator proof given in [network bounds](network_bounds.md). The share-character and output-parity identities are developed in [the Fourier account](fourier.md). The conclusions here combine those ingredients into a graph-independent secrecy bound and an exact even-size attack. The [related-work discussion](../references/RELATED_WORK.md) compares the reference models and leakage restrictions of the surrounding secret-sharing results.

The finite calculations in [verification](../verification/README.md) check the attack probabilities and the distances in (4.6) and (4.8) for small instances. Those calculations check normalizations and constants; the proofs above establish the dimension-uniform statements.

**Related:** [General reconstruction thresholds](general_threshold.md) · [Network coefficient estimates](network_bounds.md) · [Resource boundaries](boundaries.md).
