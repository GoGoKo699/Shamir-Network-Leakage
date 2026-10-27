# Full-threshold secrecy and the matching Bell-pair attack

For full-threshold Shamir sharing, every proper subset of shares is independent of the secret. With one classical leaked bit per device, this makes every proper output parity secret independent, even when the adversary retains a quantum reference. Only the parity of all output bits remains. Its Fourier expansion, together with the [network coefficient bounds](network_bounds.md), gives an estimate independent of the graph's degree and of all source dimensions.

In the graph-vertex reference model, the resulting bound is exact for every even number of devices. Independent Bell pairs attain it. With an arbitrary external reference extending a product device marginal, the proof gives a weaker exponential upper bound; exact optimality is not claimed in that broader model.

## 1. The two full-threshold bounds

Let $`p>n`$ be an odd prime and consider $`(n,n)`$ Shamir sharing at distinct nonzero evaluation points. Every device emits one classical bit by an arbitrary local binary measurement. The state supplied by the sources is independent of the secret and sharing randomness, and devices do not communicate during leakage. The adversary receives all bits and retains the allowed reference $`E`$. Write

```math
\Delta(s,s')
=\frac12\left\|\Omega_s^{BE}-\Omega_{s'}^{BE}\right\|_1
```

for two distinct chosen secrets. The [model](model.md) specifies the experiment and the reference scopes precisely.

### Theorem 1.1: exact even-size law for graph-vertex references

Suppose independent bipartite sources lie on an arbitrary graph with vertices $`D_1,\ldots,D_n`$ and, optionally, one adversary vertex $`E`$. For $`n\ge2`$,

```math
\boxed{\quad
\Delta(s,s')\le
2^{1-n/2}\cos\!\left(\frac{\pi}{2p}\right).
\quad}
\tag{1.1}
```

This includes the case with no external reference. For every even $`n`$ and every pair $`s\ne s'`$, a strategy using a perfect matching of Bell pairs and no reference attains equality. Thus (1.1) is the exact maximum over the allowed graphs and strategies when $`n`$ is even. It is also attained on any prescribed graph containing a perfect matching, if the source states can be chosen freely and other edges are ignored.

The statement does not assert equality for odd $`n`$ or for every prescribed graph. It allows independent device-adversary sources and arbitrary collective processing at the adversary vertex. A purification of a device-device source held by a third party is not automatically a bipartite source in this model.

### Theorem 1.2: arbitrary external references

Suppose the device marginal is a literal tensor product of independent bipartite-source states, and $`\rho_{DE}`$ is any extension of that marginal. For $`n\ge4`$,

```math
\boxed{\quad
\Delta(s,s')\le
2^{1-n/4}\cos\!\left(\frac{\pi}{2p}\right).
\quad}
\tag{1.2}
```

The extension can contain purifications of all device-device sources and arbitrary correlations among the adversary's registers. The right side is uniform in the graph, its degree, and all finite dimensions. For fewer than four devices, the general bound $`\Delta\le1`$ remains available; the fourth-moment proof below is stated for $`n\ge4`$.

Both theorems allow an actual classical shared seed that selects the graph, states, and local measurements, with the corresponding source condition satisfied in each conditional branch. The seed may be given to the adversary. The coherent purification of an unlabelled classical mixture is a different resource, as discussed in [the model](model.md) and [the boundary examples](boundaries.md).

## 2. Additive coordinates and the single relevant parity

At full threshold, the [Lagrange change of coordinates](fourier.md#5-full-threshold-and-additive-coordinates) gives nonzero coefficients $`\ell_i`$ such that

```math
X_i=\ell_iY_i,
\qquad
\sum_{i=1}^nX_i=s.
\tag{2.1}
```

The vector $`X`$ is uniform on this affine hyperplane. Indeed, evaluation of a polynomial of degree at most $`n-1`$ at the $`n`$ distinct points is invertible. Fixing its constant coefficient imposes exactly the displayed linear equation. Multiplication by each $`\ell_i\ne0`$ is an invertible local relabelling, so it leaves the set of possible leakage strategies unchanged.

For this page, write $`M_i(x)`$ for the rescaled measurement family: it is the original family evaluated at $`\ell_i^{-1}x`$. Define its Fourier coefficients by

```math
A_i(k)=\frac1p\sum_{x\in\mathbb F_p}\omega^{-kx}M_i(x),
\qquad \omega=e^{2\pi i/p}.
\tag{2.2}
```

For $`S\subseteq[n]`$, let

```math
F_{S,E}(s)
=\mathbb E_{X\mid\sum_iX_i=s}
\mathrm{Tr}_D\!\left[
\left(\bigotimes_{i\in S}M_i(X_i)
\otimes I_{D_{S^c}}\otimes I_E\right)\rho_{DE}
\right].
\tag{2.3}
```

This is an operator on the adversary's reference. Expanding the binary POVMs gives the exact output-parity identity

```math
\Omega_s^{BE}
=2^{-n}\sum_{b\in\{0,1\}^n}|b\rangle\langle b|\otimes
\sum_{S\subseteq[n]}(-1)^{\sum_{i\in S}b_i}F_{S,E}(s).
\tag{2.4}
```

If $`S`$ is proper, the marginal $`X_S`$ is uniform on $`\mathbb F_p^{|S|}`$ independently of $`s`$. The operator inside the average in (2.3) depends only on $`X_S`$. Consequently $`F_{S,E}(s)`$ is independent of the secret for every proper $`S`$. This reasoning does not assume the reference is uncorrelated with the devices. The identity operators on complementary devices arise from summing their outcome probabilities; operations whose outputs are not retained cannot signal to $`E`$.

Put $`F_E(s)=F_{[n],E}(s)`$. All proper parity terms cancel between two secrets, leaving

```math
\Omega_s^{BE}-\Omega_{s'}^{BE}
=2^{-n}\sum_b(-1)^{\sum_i b_i}|b\rangle\langle b|
\otimes\bigl[F_E(s)-F_E(s')\bigr].
\tag{2.5}
```

Trace norm is additive over classical blocks. There are $`2^n`$ blocks with equal norm, so the factor $`2^{-n}`$ cancels exactly:

```math
\Delta(s,s')=\frac12\|F_E(s)-F_E(s')\|_1.
\tag{2.6}
```

This exact reduction is stronger than the sum of parity norms used below full threshold.

## 3. Fourier proof and the finite-prime factor

The Fourier inverse is $`M_i(x)=\sum_k\omega^{kx}A_i(k)`$. Uniform averaging on the hyperplane $`\sum_iX_i=s`$ annihilates every frequency vector except a diagonal vector $`(k,\ldots,k)`$. One may check this directly by substituting $`X_n=s-\sum_{i<n}X_i`$ and averaging the remaining coordinates independently. Thus

```math
F_E(s)=\sum_{k\in\mathbb F_p}\omega^{ks}T_E(k),
\qquad
T_E(k)=\mathrm{Tr}_D\!\left[
\left(\bigotimes_{i=1}^n A_i(k)\otimes I_E\right)\rho_{DE}
\right].
\tag{3.1}
```

The zero frequency cancels in the difference. Equations (2.6) and (3.1) imply

```math
\Delta(s,s')
\le\frac12\sum_{k\ne0}
|\omega^{ks}-\omega^{ks'}|\,\|T_E(k)\|_1.
\tag{3.2}
```

For any nonzero residue $`j\in\mathbb F_p`$,

```math
\frac12|1-\omega^j|
=\left|\sin\!\left(\frac{\pi j}{p}\right)\right|
\le\cos\!\left(\frac{\pi}{2p}\right).
\tag{3.3}
```

The maximum is reached at $`j=(p-1)/2`$ or $`j=(p+1)/2`$, since $`p`$ is odd. For $`s\ne s'`$ and $`k\ne0`$, the residue $`k(s-s')`$ is nonzero. Substitution in (3.2) gives

```math
\Delta(s,s')
\le\cos\!\left(\frac{\pi}{2p}\right)
\sum_{k\ne0}\|T_E(k)\|_1.
\tag{3.4}
```

In the graph-vertex reference model, [Proposition 3.1 of the network estimates](network_bounds.md#3-second-moments-and-graph-vertex-references) supplies

```math
\|T_E(k)\|_1\le\prod_i a_i(k),
\qquad a_i(-k)=a_i(k),
\qquad \sum_k a_i(k)^2\le1.
```

The coefficients $`a_i(k)`$ are computed in a pure-source dilation, with mixed-edge purifications assigned to their endpoints. Applying the [paired-frequency lemma](network_bounds.md#5-pairing-the-nonzero-frequencies) with moment order two and $`n\ge2`$ yields

```math
\sum_{k\ne0}\|T_E(k)\|_1
\le\sum_{k\ne0}\prod_i a_i(k)
\le2^{1-n/2}.
\tag{3.5}
```

Combining (3.4) and (3.5) proves Theorem 1.1's upper bound.

For an arbitrary extension of the independent-source device marginal, [Proposition 4.1](network_bounds.md#4-fourth-moments-with-an-arbitrary-external-reference) instead gives

```math
\|T_E(k)\|_1\le\prod_i c_i(k),
\qquad c_i(-k)=c_i(k),
\qquad \sum_k c_i(k)^4\le1.
```

Apply the same paired-frequency lemma with moment order four and $`n\ge4`$:

```math
\sum_{k\ne0}\|T_E(k)\|_1
\le2^{1-n/4}.
\tag{3.6}
```

Equations (3.4) and (3.6) prove Theorem 1.2. The output-parity and phase arguments are identical in the two proofs; the different exponents arise entirely from the available network coefficient estimates. $`\square`$

## 4. An attack attaining the graph-vertex bound for even size

Let $`n=2m`$. Pair the devices as $`(1,2),(3,4),\ldots,(2m-1,2m)`$, and supply the independent Bell states

```math
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}.
```

There is no adversary reference. Fix a nonzero $`k\in\mathbb F_p`$ and real phases $`\phi_i`$. On additive share $`x`$, device $`i`$ measures the equatorial observable

```math
M_i(x)
=\cos\!\left(\frac{2\pi kx}{p}+\phi_i\right)\sigma_x
+\sin\!\left(\frac{2\pi kx}{p}+\phi_i\right)\sigma_y,
\tag{4.1}
```

where $`\sigma_x,\sigma_y`$ are the Pauli matrices. It reports bit $`b_i`$ when the eigenvalue is $`(-1)^{b_i}`$. This is a binary projective measurement and releases exactly one classical bit.

The single-site marginal of $`|\Phi^+\rangle`$ is maximally mixed. Also

```math
\langle\Phi^+|
(\cos\theta\,\sigma_x+\sin\theta\,\sigma_y)
\otimes(\cos\theta'\,\sigma_x+\sin\theta'\,\sigma_y)
|\Phi^+\rangle
=\cos(\theta+\theta').
\tag{4.2}
```

For a parity that contains exactly one endpoint of some pair, its conditional expectation is zero. A parity that is a union of complete pairs has expectation equal to the product of the corresponding cosines. If that union is nonempty and proper, averaging over the additive shares makes it zero: its Fourier expansion has a nonzero frequency at selected coordinates and zero at an omitted coordinate, so no diagonal frequency vector survives.

For the full parity, expand the product over all $`m`$ pairs. Each cosine contributes two Fourier terms, with signs $`+1`$ and $`-1`$. Only the choice of all plus signs and the choice of all minus signs give a diagonal frequency vector. They are distinct because $`p`$ is odd and $`k\ne0`$. Writing $`\Phi=\sum_i\phi_i`$, the full parity expectation is therefore

```math
F(s)=2^{-m}\left(e^{i\Phi}\omega^{ks}+e^{-i\Phi}\omega^{-ks}\right)
=2^{1-m}\cos\!\left(\frac{2\pi ks}{p}+\Phi\right).
\tag{4.3}
```

All nonempty proper output parities vanish, so the complete output distribution is

```math
P_s(b)
=2^{-n}\left[
1+(-1)^{\sum_i b_i}\,2^{1-m}
\cos\!\left(\frac{2\pi ks}{p}+\Phi\right)
\right].
\tag{4.4}
```

Using the parity reduction or summing the classical probabilities directly gives

```math
\begin{aligned}
\Delta(s,s')
&=\frac12|F(s)-F(s')|\\
&=2^{1-m}
\left|\sin\!\left(\frac{\pi k(s-s')}{p}\right)\right|
\left|\sin\!\left(\frac{\pi k(s+s')}{p}+\Phi\right)\right|.
\end{aligned}
\tag{4.5}
```

Because $`p`$ is prime and $`s-s'\ne0`$, choose $`k`$ so that

```math
k(s-s')=\frac{p-1}{2}\pmod p.
```

Then the first sine in (4.5) has magnitude $`\cos(\pi/(2p))`$. Choose the total phase $`\Phi`$ so that the second sine has magnitude one; a single device can supply the required phase. The state and measurements depend only on the prescribed pair of challenge secrets, as allowed in the [security convention](model.md#4-security-convention). They do not depend on which secret was shared. The resulting distance is exactly

```math
\Delta(s,s')
=2^{1-n/2}\cos\!\left(\frac{\pi}{2p}\right).
\tag{4.6}
```

This proves the attainment assertion in Theorem 1.1. The attack also supplies a lower bound in the arbitrary-reference model, because a trivial reference is allowed there. It does not match the fourth-moment upper bound (1.2).

## 5. Scope, dependencies, and verification

The proof uses the independent-source condition at the resource snapshot, before operations that are absorbed into the local measurements. Unrestricted communicating preparation can turn a collection of Bell pairs into a multipartite resource and need not preserve this condition. The [boundary examples](boundaries.md) give the relevant counterexamples. Similarly, one classical bit is the output restriction used by the parity expansion. No corresponding claim about a leaked qubit, repeated leakage, or a later release of the device registers follows from this proof.

The network inequalities used in Section 3 are inherited from the graph-contraction and quantum Finner literature, with the precise sources and the required complex-operator proof given in [network bounds](network_bounds.md). The share-character and output-parity identities are developed in [the Fourier account](fourier.md). The conclusions here combine those ingredients into a graph-independent secrecy bound and an exact even-size attack. The [related-work discussion](../references/RELATED_WORK.md) compares the reference models and leakage restrictions of the surrounding secret-sharing results.

The finite calculations in [verification](../verification/README.md) reproduce the attack probabilities and the distance in (4.6) for small instances. Those calculations check normalizations and constants; the proofs above establish the dimension-uniform statements.

**Related:** [General reconstruction thresholds](general_threshold.md) · [Network coefficient estimates](network_bounds.md) · [Resource boundaries](boundaries.md).
