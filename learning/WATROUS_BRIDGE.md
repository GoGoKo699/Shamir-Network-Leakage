# From Watrous to the leakage proofs

John Watrous's *The Theory of Quantum Information* provides the language needed to turn a physical leakage experiment into a statement about matrices. This bridge follows that language into the repository's proofs: a device is a register, its leaked bit is a measurement outcome, the adversary's information is a density operator, and security is a bound on the distinguishability of two such operators.

The book is the educational anchor for the quantum-information background. The finite-field sharing arguments and independent-source network bounds have their own derivations in the [science pages](../science/README.md) and their research attribution in [related work](../references/RELATED_WORK.md). The calculations below apply the background to this project's experiment; they do not attribute the network secrecy theorem to Watrous.

## 1. Source version and precise reading locations

**Bibliographic reference:** John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018. The [author's book page](https://jhwatrous.github.io/books-and-courses.html) identifies the publication date as April 2018 and links both the published book and an author-hosted manuscript.

The pointers below refer to the **standard-layout, author-hosted manuscript**, whose [complete version](https://jhwatrous.github.io/TQI.pdf) is labelled a 2018 pre-publication copy. The linked chapter files were inspected on 27 October 2026. These URLs do not expose a numbered manuscript revision. Page numbers below are the printed book pages, rather than the page counter of a chapter PDF. The author also provides [errata dated 23 July 2025](https://jhwatrous.github.io/TQI.errata.pdf) for the published edition; that document distinguishes the published edition from the manuscript.

| Background needed here | Verified book location | Use in this repository |
|---|---|---|
| Vector spaces, matrices, adjoints, and tensor factors | [Chapter 1](https://jhwatrous.github.io/TQI.1.pdf), §§1.1.1–1.1.2, beginning on pp. 1 and 8; partial trace on pp. 21–22 | Registers and marginal states in [the model](../science/model.md) |
| Matrix decompositions and norms | Chapter 1, §1.1.3, p. 24 onward; polar decomposition p. 30, Schmidt decomposition p. 31; norm duality and Hölder in Eqs. (1.173)–(1.174), unitary trace-norm formula in Eq. (1.182) | Polar decomposition, trace-norm witnesses and local second moments in [network bounds](../science/network_bounds.md) |
| Classical labels and density operators | [Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), §§2.1.1–2.1.2, pp. 58–67 | Shares, output bits, and classical-quantum states |
| Joint states with a classical register | Chapter 2, §2.2.3, pp. 95–96, Eq. (2.170) | The block form of leaked outcomes and actual shared seeds |
| Reductions and purifying registers | Chapter 2, §2.1.3, pp. 67–72; Theorems 2.10 and 2.12 | The three reference scopes and endpoint purifications |
| Channels and their representations | Chapter 2, §§2.2.1–2.2.2, beginning on pp. 72 and 77; Proposition 2.29, pp. 90–91 | Absorbing local preprocessing; obtaining extensions from a purification |
| POVMs, product measurements, and partial measurements | Chapter 2, §§2.3.1–2.3.2, beginning on pp. 100 and 105 | The binary observable and the adversary's conditional state |
| Binary state discrimination | [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf), §3.1.1, p. 125 onward; Theorem 3.4 on p. 128 | Operational meaning of the chosen-secret distance |
| Contraction under processing | Chapter 1, Eq. (1.183), p. 34; Chapter 3, §3.3.2, Corollary 3.40, p. 168 | Discarding added registers and bounding the adversary's final processing |
| Entanglement and communicating local operations | [Chapter 6](https://jhwatrous.github.io/TQI.6.pdf), §6.1.1, p. 310 onward; §6.1.2, p. 324 onward | Bell sources, separability, and the preparation boundary |

The completely bounded norm developed later in §3.3.2 is not needed for the repository's security parameter. The comparison here is between two final states for a fixed permitted strategy, and the ordinary trace norm already captures every final measurement of those states.

## 2. Translating the notation

The same letter can denote different objects in the book and in the sharing problem. In particular, a classical field element is not a quantum state vector, and the device name $`D_i`$ is not the book's notation for the set of density operators.

| Watrous notation or convention | Notation here | Translation |
|---|---|---|
| $`\mathcal X`$, a finite-dimensional complex Euclidean space | The Hilbert space associated with $`D_i`$, $`E`$, or a classical register | A register's linear state space |
| $`\mathrm L(\mathcal X)`$, $`\mathrm{Pos}(\mathcal X)`$, $`\mathrm D(\mathcal X)`$ | Operators, positive semidefinite operators, and states on the named register | In particular, $`\rho_{DE}\succeq0`$ and $`\mathrm{Tr}\,\rho_{DE}=1`$ |
| $`A^*`$ | $`A^\dagger`$ | Conjugate transpose |
| $`e_b`$, $`E_{b,b}=e_be_b^*`$ | $`\lvert b\rangle`$, $`\lvert b\rangle\langle b\rvert`$ | Basis vectors and classical basis projectors |
| A measurement $`\mu(b)`$ | $`P_i(b\mid y)`$ | The effect for bit $`b`$, with the measurement selected by share $`y`$ |
| $`\Vert A\Vert `$ for the spectral norm | $`\Vert A\Vert _\infty`$ | Largest singular value |
| $`\Vert A\Vert _2`$, the Frobenius norm | $`\Vert A\Vert _2`$, also called Hilbert-Schmidt norm | Square root of the sum of squared singular values |
| Trace distance written as $`\Vert \rho-\sigma\Vert _1`$ on p. 34 | $`\Delta(\rho,\sigma)=\frac12\Vert \rho-\sigma\Vert _1`$ | This repository includes a factor of one half |

The last row controls the guessing-probability convention. For equal prior probabilities, Watrous's Theorem 3.4 gives, in the repository's notation,

```math
P_{\mathrm{guess}}
=\frac12+\frac14\Vert \Omega_s^{BE}-\Omega_{s'}^{BE}\Vert _1
=\frac{1+\Delta(s,s')}{2}.
```

Thus $`\Delta`$ is the optimal difference between acceptance probabilities. The excess probability of guessing correctly above one half is $`\Delta/2`$. Keeping these quantities distinct prevents a factor-of-two error when interpreting a security exponent.

## 3. From registers to the adversary's state

Fix a secret $`s\in\mathbb F_p`$, a prime $`p>n`$, and reconstruction threshold $`t`$. The dealer samples a Shamir share vector $`Y=(Y_1,\ldots,Y_n)`$. The devices and adversary already hold a state $`\rho_{DE}`$, independent of that vector and of the secret. The joint state before leakage can be written as

```math
\sum_y \Pr[Y=y\mid s]\,
|y\rangle\langle y|_Y\otimes\rho_{DE}.
```

The classical register $`Y`$ is diagonal. Its values select local measurements; no coherent superposition of share values is supplied as an additional resource. This is the density-operator expression of the [sharing and resource assumptions](../science/model.md).

### Partial trace identifies what is retained

For an operator on $`D\otimes E`$, the partial trace can be evaluated in any orthonormal basis $`\{|a\rangle\}`$ of $`D`$:

```math
\mathrm{Tr}_D Z
=\sum_a(\langle a|\otimes I_E)Z(|a\rangle\otimes I_E).
```

The result is an operator on $`E`$. Applying this operation to a joint density operator produces the state seen by an observer who keeps $`E`$ and discards $`D`$. In the leakage experiment the devices' unreleased registers are discarded, while the classical outcomes are retained.

For a fixed share vector $`y`$ and output string $`b`$, write $`P(b\mid y)=\bigotimes_iP_i(b_i\mid y_i)`$. The unnormalized state on the adversary's register is

```math
\tau_E(b\mid y)
=\mathrm{Tr}_D\!\left[
(P(b\mid y)\otimes I_E)\rho_{DE}
\right].
```

Its trace is the probability of that output. Positivity is easiest to see in the equivalent form with $`\sqrt{P(b\mid y)}`$ on both sides of $`\rho_{DE}`$. The two partial traces agree because an operator acting only on a traced-out register may be moved cyclically under that partial trace. No commutation between $`P(b\mid y)`$ and $`\rho_{DE}`$ is assumed.

Keeping the outcome as a classical label gives

```math
\Omega_s^{BE}
=\mathbb E_{Y\mid s}\sum_b
|b\rangle\langle b|_B\otimes\tau_E(b\mid Y).
```

This is the object compared in every theorem. Its blocks contain both the output probabilities and the reference state conditional on each output. Bounding only the classical distribution of $`B`$ would omit information that may remain in $`E`$.

### Local channels and the absence of signaling

Suppose a device applies a local channel $`\Phi_i`$ before measuring an effect $`Q_i(b\mid y)`$. The adjoint channel gives the effective measurement

```math
P_i(b\mid y)=\Phi_i^*(Q_i(b\mid y)),
\qquad
\mathrm{Tr}[Q_i(b\mid y)\Phi_i(\sigma)]
=\mathrm{Tr}[P_i(b\mid y)\sigma].
```

Because the adjoint preserves the identity and positivity, these effective operators again form a POVM. This is why the model permits arbitrary local preprocessing without assigning it a separate proof step. Joint processing of all incident source halves is still local to one device.

If an outcome is not retained, summing its effects gives the identity. In particular,

```math
\sum_b\tau_E(b\mid y)
=\mathrm{Tr}_D\rho_{DE}=\rho_E.
```

The adversary's unconditioned state cannot reveal the devices' measurement choices. Conditional states can change, and the outcomes needed to identify those states can carry information. The full-threshold proof uses the more specific fact that a proper output parity depends only on a proper subset of shares. Shamir privacy then removes its secret dependence; no-signaling alone would not establish the complete secrecy theorem.

## 4. Why one leaked bit becomes a Hermitian contraction

For a binary POVM, define

```math
M_i(y)=P_i(0\mid y)-P_i(1\mid y)=2P_i(0\mid y)-I.
```

The eigenvalues of $`P_i(0\mid y)`$ lie between zero and one. Therefore $`M_i(y)`$ is Hermitian and satisfies $`-I\preceq M_i(y)\preceq I`$. Conversely, every Hermitian operator in this interval gives a binary POVM through

```math
P_i(b\mid y)=\frac{I+(-1)^bM_i(y)}2.
```

This parametrization includes noisy measurements and randomized classical output, not only projective measurements. Its operational content is

```math
\mathbb E[(-1)^{B_i}\mid y,\sigma]
=\mathrm{Tr}[M_i(y)\sigma].
```

Products of these signs are output parities. Expanding a product of binary effects therefore produces a sum indexed by subsets of devices. The exact expansion and its trace-distance consequences are derived in [the output Fourier account](../science/fourier.md#3-output-parities-with-a-quantum-reference).

The Fourier coefficient $`A_i(k)=p^{-1}\sum_y\omega^{-ky}M_i(y)`$ is generally **not** Hermitian: its weights can be complex. What remains true is $`A_i(-k)=A_i(k)^\dagger`$ and $`\Vert A_i(k)\Vert _\infty\le1`$. This is why the network proof needs an inequality for complex operators, even though each actual measurement is represented by a Hermitian observable.

## 5. The norms serve different purposes

For a matrix $`Z`$, the three relevant Schatten norms are

```math
\Vert Z\Vert _1=\mathrm{Tr}\,\sqrt{Z^\dagger Z},
\qquad
\Vert Z\Vert _2=\sqrt{\mathrm{Tr}\,Z^\dagger Z},
\qquad
\Vert Z\Vert _\infty=\text{largest singular value of }Z.
```

The operator norm certifies that Fourier coefficients are contractions. The Hilbert-Schmidt norm turns tensor entries into a square-sum that can be controlled by Cauchy-Schwarz. The trace norm bounds the adversary's distinguishing power. Substituting one of these norms for another without accounting for dimension would lose the dimension-uniform guarantee.

The relevant instances of Schatten Hölder are

```math
|\mathrm{Tr}(X^\dagger Y)|
\le\Vert X\Vert _\infty\Vert Y\Vert _1,
\qquad
|\mathrm{Tr}(X^\dagger Y)|
\le\Vert X\Vert _2\Vert Y\Vert _2.
```

The first inequality pairs a bounded witness with the quantity being distinguished. The second is Hilbert-Schmidt Cauchy-Schwarz, used for the graph tensor contraction and the state-weighted estimate below.

### A trace-norm witness for an operator on the reference

The unitary variational formula in Watrous, Eq. (1.182), applies to any reference operator $`T_E`$, including a non-Hermitian Fourier coefficient:

```math
\Vert T_E\Vert _1=\max_{V_E\text{ unitary}}
|\mathrm{Tr}(V_ET_E)|.
```

For a device operator $`K`$, set $`T_E=\mathrm{Tr}_D[(K\otimes I_E)\rho_{DE}]`$. The quantity inside the maximum is then $`|\mathrm{Tr}[\rho_{DE}(K\otimes V_E)]|`$.

The useful scalar bound comes from factoring $`K`$ before applying Cauchy–Schwarz. As in Watrous §1.1.3, use polar decomposition and set $`|K|=(K^\dagger K)^{1/2}`$. The polar factor can be extended to a unitary $`U`$ on the device space. Then

```math
K=|K^\dagger|^{1/2}U|K|^{1/2},
\qquad
\Vert T_E\Vert _1
\le
\left(\mathrm{Tr}[\rho_D|K^\dagger|]\right)^{1/2}
\left(\mathrm{Tr}[\rho_D|K|]\right)^{1/2}.
```

To see the bound, set $`L=|K^\dagger|^{1/2}\otimes I_E`$ and $`R=|K|^{1/2}\otimes I_E`$. Pair $`L\rho_{DE}^{1/2}`$ and $`(U\otimes V_E)R\rho_{DE}^{1/2}`$ in the Hilbert–Schmidt inner product. Their squared norms are the two device expectations above by unitarity and partial trace. The inequality holds for each witness, so it also holds after maximizing. The reference may be any extension of $`\rho_D`$. The product-source structure is used on $`\rho_D`$ at the later graph step. See [network bounds §4](../science/network_bounds.md#4-second-moments-with-an-arbitrary-external-reference).

### Local second moments on the source graph

For a positive local product $`\bigotimes_i H_i`$, the graph bound controls its expectation by $`\prod_i(\mathrm{Tr}[\rho_i H_i^2])^{1/2}`$. One way to read this bound is to measure each $`H_i`$ in its spectral basis and apply quantum Finner to the nonnegative spectral values. Taking $`H_i=|A_i(k)|`$ gives the moment $`b_i(k)=\mathrm{Tr}[\rho_i A_i(k)^\dagger A_i(k)]`$. Taking $`H_i=|A_i(k)^\dagger|`$ gives $`b_i(-k)`$.

On a product of Fourier operators, apply the graph bound to both polar factors. The square root of their product supplies the local weight $`h_i(k)=[b_i(k)b_i(-k)]^{1/4}`$. Operator Parseval yields $`\sum_k b_i(k)\le1`$, so $`\sum_k h_i(k)^2\le1`$. The two frequencies $`k`$ and $`-k`$ have the same weight and are distinct for $`k\ne0`$ over an odd prime field. Thus each nonzero weight is at most $`1/\sqrt2`$.

This derives a second-moment budget for the arbitrary-reference argument. Watrous supplies the norm and measurement language, and [the graph proof](../science/network_bounds.md#2-complex-contraction-on-a-graph) supplies the network inequality.

### Classical blocks retain their probabilities

For a block-diagonal operator,

```math
\left\Vert \sum_b|b\rangle\langle b|\otimes Z_b\right\Vert _1
=\sum_b\Vert Z_b\Vert _1.
```

The identity follows because the singular values of a direct sum are the singular values of its blocks collected together. It explains why the security proof works with unnormalized conditional states. Renormalizing each block separately would discard its probability and could overstate the adversary's advantage on a rare outcome.

Channel contraction, including the partial-trace case in Watrous's Eq. (1.183), then ensures that further processing cannot increase the final distance. The bounds already allow the adversary's best collective decision rule.

### Summing the outcomes with zero frequency

Fix a nonzero dual-code word $`k`$ and one leaked string. For every nonzero coordinate $`k_i`$, Fourier expansion of the local effect gives $`(-1)^{u_i}A_i(k_i)/2`$. Summing the trace-norm contribution over both possible values of $`u_i`$ cancels the factor of one half. For every zero coordinate, the coefficient is the positive averaged effect $`B_i(u_i)=p^{-1}\sum_y P_i(u_i\mid y)`$.

For an example with one zero coordinate $`j`$, let $`F`$ be the product operator at the nonzero coordinates. For the two outcomes at $`j`$, the polar bound has the form $`\sqrt{x_b y_b}`$, with

```math
x_b=\mathrm{Tr}\!\left[\rho_D (|F^\dagger|\otimesB_j(b))\right],
\qquad
y_b=\mathrm{Tr}\!\left[\rho_D (|F|\otimesB_j(b))\right].
```

The notation puts $`j`$ last in the tensor product. Sum the two upper bounds using scalar Cauchy–Schwarz:

```math
\sum_{b=0}^{1}\sqrt{x_b y_b}
\le
\sqrt{\left(\sum_b x_b\right)\left(\sum_b y_b\right)}.
```

Completeness replaces $`\sum_bB_j(b)`$ by identity inside each scalar trace. The same argument sums over several zero coordinates at once, since the sum of the corresponding products of averaged effects is identity. Quantum Finner can now act on each positive product in the scalar bound. The resulting upper bound is a product of $`h_i(k_i)`$ only over nonzero coordinates. This order of operations is what removes the factors at zero frequency for a classical output with a quantum reference. See [the support bound in network bounds §4](../science/network_bounds.md#4-second-moments-with-an-arbitrary-external-reference).

## 6. Purification is a representation choice with a location

The purification theorems in §2.1.3 say how a mixed state can arise as the reduction of a pure state and how different purifications are related. In the resource model, the location of the added register determines which theorem applies.

Consider one mixed source $`\sigma_{D_iD_j}`$. A purification can be placed at an endpoint, for example by replacing $`D_i`$ with $`D_iR`$. The source remains bipartite across $`D_iR:D_j`$. Extending the measurement at $`D_i`$ by the identity on $`R`$ reproduces the original experiment. This is the pure-source dilation used to justify the graph contraction on the device marginal.

If instead the adversary holds $`R`$, the source is distributed over $`D_i,D_j,E`$. The device marginal remains the same bipartite state. The arbitrary-extension proof uses polar decomposition to control the reference witness through that marginal. The graph-vertex proof applies directly when every source, including those to the adversary, connects only two vertices. The book's existence theorem for purifications does not remove this distinction about who holds the registers.

Proposition 2.29 in §2.2.2 gives a useful description of that broader scope. Fix any purification $`|\psi\rangle_{DR}`$ of the required device marginal. Every extension of the same marginal can be written as

```math
\rho_{DE}
=(\mathrm{id}_D\otimes\Phi_{R\to E})
(|\psi\rangle\langle\psi|)
```

for a channel $`\Phi`$. Thus one may view arbitrary side information as the result of processing a purification. This representation preserves the prescribed device marginal. It does not turn a third-party purifying register into a device endpoint or allow a different, coherently mixed device marginal.

There is a second distinction between an actual classical label and coherent side information. The cq form is described explicitly in Watrous, §2.2.3, Eq. (2.170). An allowed shared seed in this model has the form

```math
\sum_\lambda q_\lambda|\lambda\rangle\langle\lambda|_\Lambda
\otimes\rho_{DE}^{(\lambda)},
```

with the network assumption valid in every branch. The block trace-norm identity proves that a uniform bound survives when $`\Lambda`$ is revealed. An arbitrary purification of the unlabelled mixture need not have this form. The [GHZ boundary example](../science/boundaries.md) demonstrates that the distinction changes the attainable leakage.

Chapter 6 supplies the vocabulary for separability and LOCC. The preparation restriction here is more specific: source independence is required before the local processing absorbed into the measurement. A sequence of local operations **with communicated outcomes** can change that resource structure. Calling the initial supply “Bell pairs” does not by itself certify that the state used during leakage satisfies the independent-source assumption.

## 7. Worked binary example: two shares and one Bell pair

This example combines a reduced density operator, a binary POVM, correlated output bits, and the trace-distance convention. Take $`n=t=2`$ and $`p=3`$. In the additive coordinates from [the full-threshold proof](../science/full_threshold.md#2-additive-coordinates-and-the-single-relevant-parity), the shares satisfy

```math
X_1+X_2=s\pmod3,
```

and each coordinate is uniform. Compare secrets $`s=0`$ and $`s=1`$.

Give the devices the Bell vector $`|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2`$. Its density matrix and one-device marginal are

```math
\rho_{D_1D_2}
=\frac12
\begin{pmatrix}
1&0&0&1\\
0&0&0&0\\
0&0&0&0\\
1&0&0&1
\end{pmatrix},
\qquad
\rho_{D_1}=\rho_{D_2}=\frac I2.
```

For a real angle $`\theta`$, define

```math
M(\theta)
=\begin{pmatrix}0&e^{-i\theta}\\e^{i\theta}&0\end{pmatrix},
\qquad
P(b\mid\theta)=\frac{I+(-1)^bM(\theta)}2.
```

The matrix $`M(\theta)`$ is Hermitian and squares to the identity, so these effects are rank-one projectors. Each outcome is individually uniform on a device's marginal $`I/2`$. Multiplying the two matrices against the Bell state gives

```math
\mathrm{Tr}[\rho_{D_1D_2}(M(\theta_1)\otimes M(\theta_2))]
=\cos(\theta_1+\theta_2).
```

Use the share-dependent angles

```math
\theta_1(x)=\frac{4\pi x}{3}-\frac\pi6,
\qquad
\theta_2(x)=\frac{4\pi x}{3}.
```

Their sum depends on the secret, modulo an irrelevant multiple of $`2\pi`$. The full output-parity expectation is therefore

```math
F(s)=\mathbb E[(-1)^{B_1+B_2}\mid s]
=\cos\!\left(\frac{4\pi s}{3}-\frac\pi6\right),
\qquad
F(0)=\frac{\sqrt3}{2},
\quad F(1)=-\frac{\sqrt3}{2}.
```

The single-bit expectations vanish, so $`P_s(b_1,b_2)=[1+(-1)^{b_1+b_2}F(s)]/4`$. The four probabilities are explicit:

| Output $`b_1b_2`$ | Secret $`0`$ | Secret $`1`$ |
|---|---:|---:|
| $`00`$ | $`(2+\sqrt3)/8`$ | $`(2-\sqrt3)/8`$ |
| $`01`$ | $`(2-\sqrt3)/8`$ | $`(2+\sqrt3)/8`$ |
| $`10`$ | $`(2-\sqrt3)/8`$ | $`(2+\sqrt3)/8`$ |
| $`11`$ | $`(2+\sqrt3)/8`$ | $`(2-\sqrt3)/8`$ |

Every individual bit has probability one half under either secret, yet the parity distinguishes them. The two diagonal output density operators differ by

```math
\Omega_0^B-\Omega_1^B
=\frac{\sqrt3}{4}\mathrm{diag}(1,-1,-1,1).
```

Consequently,

```math
\Vert \Omega_0^B-\Omega_1^B\Vert _1=\sqrt3,
\qquad
\Delta(0,1)=\frac{\sqrt3}{2},
\qquad
P_{\mathrm{guess}}=\frac12+\frac{\sqrt3}{4}.
```

An optimal decision rule outputs secret zero for even parity and secret one for odd parity. The distance equals $`\cos(\pi/6)`$, the arbitrary-reference full-threshold upper bound at $`n=2,p=3`$. This small instance displays the mechanism; exponential suppression appears when the number of devices grows. The [matching attack proof](../science/full_threshold.md#4-bell-pair-attainment) establishes the exact expression for every even $`n`$.

## 8. The additional mathematics supplied by the repository

The book's framework makes the quantum expressions meaningful. Four further steps organize and control those expressions in this sharing problem. Their authoritative proofs are local, with research sources kept in [related work](../references/RELATED_WORK.md).

| Additional step | Role in the argument | Authoritative derivation |
|---|---|---|
| Arithmetic over $`\mathbb F_p`$ and Shamir sharing | Uniform polynomial coefficients determine a correlated classical share distribution; interpolation gives local additive coordinates at full threshold | [Model, Section 1](../science/model.md#1-shares-and-public-parameters); [Fourier account, Section 5](../science/fourier.md#5-full-threshold-and-additive-coordinates) |
| Finite-field and binary-output Fourier expansions | Additive characters select surviving input frequencies; binary characters identify leaked parities | [Fourier account, Sections 1–4](../science/fourier.md) |
| Independent-source graph contraction and quantum Finner | The resource factorization bounds scalar or reference-valued coefficients uniformly in graph density and dimension | [Network bounds](../science/network_bounds.md) |
| Weighted code sums and list recovery | Minimum codeword weight forces each nonzero term to involve many devices. MDS Hölder gives an explicit finite bound. The weighted generalized Reed–Solomon estimate gives the leading exponent above one half. | [General thresholds](../science/general_threshold.md) |

The relevant field characters are the numbers $`\omega^{kx}`$, where $`\omega=e^{2\pi i/p}`$ and products $`kx`$ are computed modulo $`p`$. Orthogonality is the finite sum identity $`\sum_x\omega^{kx}=0`$ for $`k\ne0`$. This Fourier transform is an algebraic expansion of the measurement family, not a quantum Fourier-transform circuit performed by the devices.

At full threshold, proper output parities are secret independent. One paired-frequency sum yields the bound $`2^{1-n/2}\cos(\pi/(2p))`$ for every permitted reference. Independent Bell pairs attain it at even size. Below full threshold, the support bound leads to a weighted dual-code sum. When the reconstruction rate is at least $`1/2+\eta`$ for fixed $`\eta>0`$, the sharp leading exponent is $`t/2`$, with a matching construction on a reconstruction set. See [full threshold](../science/full_threshold.md) and [general thresholds](../science/general_threshold.md).

**Navigation:** [Milestones](MILESTONES.md) · [Scientific overview](../science/README.md) · [Resource boundaries](../science/boundaries.md) · [Research attribution](../references/RELATED_WORK.md).
