# Fourier bounds for independent bipartite-source networks

This page derives the support-only Fourier estimate used for [general reconstruction thresholds](general_threshold.md) and the coefficient bound used at [full threshold](full_threshold.md). Both are controlled by second moments of local Fourier operators. They allow an arbitrary quantum extension of the literal independent-source device marginal, including an adversary who holds all source purifications.

The graph contraction below is an inherited ingredient. Its complex-operator form is the Schmidt tensor contraction used in [GHZ-Communication-Cost, Section B3, in the proof of Theorem B1](https://github.com/GoGoKo699/GHZ-Communication-Cost/blob/99bd0004bcd1b395d27bff9b092db64dc0672c24/science/branch-bound.md). The positive-effect consequence is the quantum Finner inequality of [Renou et al., *Limits on correlations in networks for quantum and no-signaling resources*, Theorem 2 and Appendix D](https://arxiv.org/abs/1901.08287), also published as [Physical Review Letters 123, 070403 (2019)](https://doi.org/10.1103/PhysRevLett.123.070403). We give complete proofs of the forms needed here, including the passage from scalar contractions to operator-valued Fourier coefficients.

## 1. Notation and the source assumptions

Let $`p`$ be an odd prime, put $`\omega=e^{2\pi i/p}`$, and let $`D_1,\ldots,D_n`$ be the devices. Device $`i`$ has a family of binary-measurement observables

```math
M_i(x)=P_i(0\mid x)-P_i(1\mid x),
\qquad -I\le M_i(x)\le I,
\qquad x\in\mathbb F_p.
```

Its normalized Fourier operators are

```math
A_i(k)=\frac1p\sum_{x\in\mathbb F_p}\omega^{-kx}M_i(x).
\tag{1.1}
```

Hermiticity and the triangle inequality give

```math
A_i(-k)=A_i(k)^\dagger,
\qquad \|A_i(k)\|_\infty\le1.
\tag{1.2}
```

The source graph may be any finite graph. Each edge supplies a state on one register at each endpoint, independently of all other edges. A vertex may apply a joint operation to all of its incident registers. There is no bound on degree, on the number of sources, or on their finite dimensions. Parallel edges can be combined into one tensor-product source. Independent local states are allowed as well.

For the **graph-vertex reference model**, the vertices are $`D_1,\ldots,D_n`$ and, optionally, one additional vertex $`E`$. Every source is bipartite between two of these vertices. The adversary may hold all registers at $`E`$ and process them jointly. In proving bounds in this model, we use a pure-source dilation: purify each mixed edge into one of its endpoints, enlarge that endpoint's Hilbert space, and extend the operators by identities on the added registers. Independent local states can likewise be purified locally. This operation preserves the experiment being bounded, or gives the adversary additional local registers that can subsequently be discarded. It does not place a purification at a third endpoint.

The notation $`\rho_i`$ in the second-moment estimates below denotes the local marginal in this chosen pure-source dilation. We do not identify its weighted Hilbert-Schmidt norm with the norm computed from the marginal before dilation. All final bounds are uniform in the dilation, so this choice introduces no dimension-dependent loss.

For the **arbitrary-reference model**, the requirement instead concerns the literal device marginal:

```math
\Omega_D=\mathrm{Tr}_E\rho_{DE}
=\bigotimes_{e=\{i,j\}}\Omega_{D_{i,e}D_{j,e}},
\qquad
D_i=\bigotimes_{e\ni i}D_{i,e},
\tag{1.3}
```

with independent local factors included if necessary. The state $`\rho_{DE}`$ may be any extension of $`\Omega_D`$. In particular, $`E`$ can purify device-device sources and can contain correlations across the source references. In Section 4, $`\rho_i=\Omega_{D_i}`$ is the original device marginal; no choice of purification is needed to define it. The operational restrictions and the treatment of genuinely classical shared randomness are stated in [the model](model.md).

## 2. Complex contraction on a graph

### Lemma 2.1: weighted graph contraction

Let $`\rho_G`$ be a tensor product of pure bipartite states on the edges of a graph with vertex set $`V`$. Let $`\rho_v`$ be its marginal at vertex $`v`$. For arbitrary complex operators $`K_v`$ on the vertex spaces,

```math
\left|\mathrm{Tr}\!\left[\rho_G\bigotimes_{v\in V}K_v\right]\right|
\le
\prod_{v\in V}
\left\|\rho_v^{1/4}K_v\rho_v^{1/4}\right\|_2.
\tag{2.1}
```

Here $`\|X\|_2=(\mathrm{Tr}\,X^\dagger X)^{1/2}`$. No positivity or Hermiticity of $`K_v`$ is required.

**Proof.** Write each edge state in Schmidt form,

```math
|\psi_e\rangle
=\sum_a\sqrt{\eta_{e,a}}\,|a\rangle_{u,e}|a\rangle_{v,e},
\qquad
\eta_{e,a}\ge0,
\qquad
\sum_a\eta_{e,a}=1.
```

Expanding the expectation introduces two indices $`a_e,b_e`$ for every edge. At vertex $`v`$, let $`\mathbf a_v=(a_e:e\ni v)`$ and define $`\mathbf b_v`$ similarly. The expectation is the full contraction of the tensors

```math
F_v\bigl((a_e,b_e):e\ni v\bigr)
=\langle\mathbf b_v|K_v|\mathbf a_v\rangle
\prod_{e\ni v}(\eta_{e,a_e}\eta_{e,b_e})^{1/4}.
\tag{2.2}
```

Indeed, each edge occurs at two endpoints, so multiplying the tensors produces exactly its Schmidt weight $`\sqrt{\eta_{e,a_e}\eta_{e,b_e}}`$.

We use the following elementary tensor-contraction bound. If two tensors share the collection of indices $`\gamma`$ and have disjoint remaining index collections $`\alpha,\beta`$, their contraction is

```math
Z_{\alpha,\beta}=\sum_\gamma X_{\alpha,\gamma}Y_{\gamma,\beta}.
```

Cauchy-Schwarz gives

```math
\begin{aligned}
\|Z\|_2^2
&\le
\sum_{\alpha,\beta}
\left(\sum_\gamma|X_{\alpha,\gamma}|^2\right)
\left(\sum_\gamma|Y_{\gamma,\beta}|^2\right)\\
&=\|X\|_2^2\|Y\|_2^2.
\end{aligned}
\tag{2.3}
```

Merge vertices successively, contracting all edges joining the two clusters at each merge. Every edge index occurs in exactly two vertex tensors, so the remaining indices of the two clusters are disjoint. Equation (2.3) therefore applies at every step. Disconnected components can be contracted separately. The absolute value of the final scalar is at most $`\prod_v\|F_v\|_2`$.

The marginal $`\rho_v`$ is diagonal in the product Schmidt basis, with eigenvalue $`\prod_{e\ni v}\eta_{e,a_e}`$ at $`\mathbf a_v`$. Consequently,

```math
\begin{aligned}
\|F_v\|_2^2
&=\sum_{\mathbf a_v,\mathbf b_v}
\prod_{e\ni v}\sqrt{\eta_{e,a_e}\eta_{e,b_e}}
\,|\langle\mathbf b_v|K_v|\mathbf a_v\rangle|^2\\
&=\left\|\rho_v^{1/4}K_v\rho_v^{1/4}\right\|_2^2.
\end{aligned}
```

Substitution proves (2.1). Pure local ancillas amount to fixed local tensor indices and do not change the argument. This proof is the graph Cauchy-Schwarz, or graph Finner, contraction in a form that applies directly to complex Fourier operators. $`\square`$

We will also use the elementary inequality, valid for every state $`\sigma`$ and operator $`K`$,

```math
\left\|\sigma^{1/4}K\sigma^{1/4}\right\|_2^2
\le\frac12\mathrm{Tr}\!\left[\sigma(K^\dagger K+KK^\dagger)\right].
\tag{2.4}
```

To verify it, diagonalize $`\sigma`$ with eigenvalues $`r_a`$. The left side is $`\sum_{a,b}\sqrt{r_ar_b}|K_{ab}|^2`$, and $`\sqrt{r_ar_b}\le(r_a+r_b)/2`$ gives the right side. In particular, a Hermitian contraction has weighted squared norm at most one, and a unitary has weighted squared norm at most one.

### Corollary 2.2: positive-effect quantum Finner inequality

Let $`\Omega_D`$ be an independent bipartite-source device state, with mixed sources allowed. For local effects $`0\le B_i\le I`$,

```math
\mathrm{Tr}\!\left[\Omega_D\bigotimes_{i=1}^n B_i\right]
\le
\prod_{i=1}^n\left(\mathrm{Tr}\,\Omega_{D_i}B_i\right)^{1/2}.
\tag{2.5}
```

For positive local operators $`L_i`$, the squared-observable form is

```math
\mathrm{Tr}\!\left[\Omega_D\bigotimes_{i=1}^n L_i\right]
\le
\prod_{i=1}^n\left(\mathrm{Tr}\,\Omega_{D_i}L_i^2\right)^{1/2}.
\tag{2.6}
```

**Proof.** For pure sources, apply (2.1) and then (2.4) to each positive $`L_i`$. Since $`L_i^\dagger=L_i`$, the local bound in (2.4) is $`\mathrm{Tr}(\Omega_{D_i}L_i^2)`$. For mixed sources, purify each source into an endpoint and extend each operator by identity. The joint expectation and every local expectation of a squared operator remain unchanged. Applying the pure-source result to this calculation proves (2.6). The event form (2.5) follows from $`B_i^2\le B_i`$. $`\square`$

## 3. Second moments and graph-vertex references

For a set $`S\subseteq[n]`$ and frequencies $`\mathbf k_S=(k_i:i\in S)`$, define the operator on $`E`$

```math
T_{S,E}(\mathbf k_S)
=\mathrm{Tr}_D\!\left[
\left(\bigotimes_{i\in S}A_i(k_i)
\otimes I_{D_{[n]\setminus S}}\otimes I_E\right)\rho_{DE}
\right].
\tag{3.1}
```

When $`E`$ is trivial, this is a scalar. When $`S=[n]`$, we also write $`T_E(\mathbf k)`$.

### Proposition 3.1: symmetric second-moment majorants

In the graph-vertex reference model, choose the pure-source dilation described in Section 1 and set

```math
a_i(k)=\left\|\rho_i^{1/4}A_i(k)\rho_i^{1/4}\right\|_2.
\tag{3.2}
```

Then, for every $`S`$ and $`\mathbf k_S`$,

```math
\|T_{S,E}(\mathbf k_S)\|_1\le\prod_{i\in S}a_i(k_i),
\qquad
a_i(-k)=a_i(k),
\qquad
\sum_{k\in\mathbb F_p}a_i(k)^2\le1.
\tag{3.3}
```

If the dilation enlarged the adversary's space, the trace-norm estimate also holds for the original coefficient after discarding the added registers.

**Proof.** First work in the dilated state. Trace-norm duality gives

```math
\|T_{S,E}(\mathbf k_S)\|_1
=\max_{U_E:\,U_E^\dagger U_E=I}
\left|\mathrm{Tr}\!\left[
\rho_{DE}\left(
\bigotimes_{i\in S}A_i(k_i)
\otimes I_{D_{[n]\setminus S}}\otimes U_E
\right)\right]\right|.
\tag{3.4}
```

Apply (2.1) to the graph with $`E`$ as an additional vertex. A device outside $`S`$ contributes $`\|\rho_i^{1/2}\|_2=1`$. The adversary contributes at most one by (2.4), since $`U_E`$ is unitary. The remaining factors are exactly $`a_i(k_i)`$. For a trivial $`E`$, the same proof is the scalar graph contraction. Partial trace is a quantum channel and contracts the trace norm, so added adversary registers can then be discarded.

Equation (1.2) implies $`a_i(-k)=a_i(k)`$. Parseval in the Hilbert space of matrices, followed by (2.4) for the Hermitian $`M_i(x)`$, gives

```math
\begin{aligned}
\sum_k a_i(k)^2
&=\frac1p\sum_{x\in\mathbb F_p}
\left\|\rho_i^{1/4}M_i(x)\rho_i^{1/4}\right\|_2^2\\
&\le\frac1p\sum_{x\in\mathbb F_p}\mathrm{Tr}\,\rho_iM_i(x)^2
\le1.
\end{aligned}
\tag{3.5}
```

This proves all parts of (3.3). $`\square`$

The proposition permits arbitrary independent device-adversary edges and a collective adversary measurement. The next section uses a different argument that also allows purifications of device-device sources at an external reference.

## 4. Second moments with an arbitrary external reference

For this section let $`\rho_{DE}`$ be any extension of the literal independent-source device marginal (1.3). For a device operator $`K`$, write

```math
\mathcal T(K)=\mathrm{Tr}_D[(K\otimes I_E)\rho_{DE}],
\qquad
|K|=(K^\dagger K)^{1/2}.
```

### Lemma 4.1: trace-norm bound from the device marginal

For any device operator $`K`$,

```math
\|\mathcal T(K)\|_1
\le
\left[\mathrm{Tr}(\Omega_D|K^\dagger|)
      \mathrm{Tr}(\Omega_D|K|)\right]^{1/2}.
\tag{4.1}
```

**Proof.** Extend the polar factor of $`K`$ to a unitary $`U`$ on the finite-dimensional device space. Then $`K=|K^\dagger|^{1/2}U|K|^{1/2}`$. In the trace-norm dual formula, test $`\mathcal T(K)`$ against an arbitrary unitary $`V_E`$. The resulting expectation is $`\mathrm{Tr}(\rho_{DE}X^\dagger Y)`$ with

```math
X=|K^\dagger|^{1/2}\otimes I_E,
\qquad
Y=(U\otimes V_E)(|K|^{1/2}\otimes I_E).
```

State-weighted Cauchy–Schwarz bounds its modulus by the product of the two weighted norms. Their squares are $`\mathrm{Tr}(\Omega_D|K^\dagger|)`$ and $`\mathrm{Tr}(\Omega_D|K|)`$. The bound is independent of $`V_E`$. Taking the supremum proves (4.1), including for singular device marginals. $`\square`$

### Proposition 4.2: the support-only Fourier bound

Define

```math
b_i(z)=\mathrm{Tr}\!\left[\rho_i A_i(z)^\dagger A_i(z)\right],
\qquad
h_i(z)=\left[b_i(z)b_i(-z)\right]^{1/4},
\qquad
\rho_i=\Omega_{D_i}.
\tag{4.2}
```

Then $`h_i(-z)=h_i(z)`$, $`\sum_z h_i(z)^2\le 1`$, and $`h_i(z)\le 1/\sqrt{2}`$ for every nonzero $`z`$. In particular, the reference-valued coefficients of (3.1) satisfy

```math
\|T_{S,E}(\mathbf k_S)\|_1
\le \prod_{i\in S}h_i(k_i).
\tag{4.3}
```

There is also a support-only estimate for the complete bit-outcome record. Set $`\widehat P_i(b_i,z)=p^{-1}\sum_x\omega^{-zx}P_i(b_i\mid x)`$ and define the reference coefficient on the outcome block $`b`$ by

```math
R_b(k)=\mathcal T\!\left(\bigotimes_i\widehat P_i(b_i,k_i)\right).
```

For any frequency word $`k\in\mathbb F_p^n`$, let $`S=\{i:k_i\ne0\}`$. Then

```math
\sum_{b\in\{0,1\}^n}\|R_b(k)\|_1
\le\prod_{i\in S} h_i(k_i).
\tag{4.4}
```

**Proof.** For (4.3), apply (4.1) to the operator product in (3.1). Its positive moduli factor as tensor products of the local moduli. Apply the squared-observable form (2.6) to both factors on the right of (4.1). The local squared expectations are $`b_i(k_i)`$ and $`b_i(-k_i)`$ because $`A_i(-z)=A_i(z)^\dagger`$. Operator Parseval gives

```math
\sum_z b_i(z)=\frac1p\sum_{x\in\mathbb F_p}\mathrm{Tr}(\rho_i M_i(x)^2)\le1.
```

Cauchy–Schwarz gives $`\sum_z\sqrt{b_i(z)b_i(-z)}\le1`$. The weights $`h_i`$ are symmetric by definition, and a nonzero frequency and its negative are distinct for odd $`p`$. Their equal squared contributions give the cap $`1/\sqrt 2`$.

For (4.4), write $`B_i(b_i)=\widehat P_i(b_i,0)`$. These average effects are positive and sum to identity over $`b_i`$. At a nonzero frequency, $`\widehat P_i(b_i,z)=(-1)^{b_i}A_i(z)/2`$. Thus the outcome-block operator is a sign times $`2^{-|S|}\mathcal T(K_b)`$, where

```math
K_b=\bigotimes_{i\in S}A_i(k_i)\otimes\bigotimes_{i\notin S}B_i(b_i).
```

Summation over the bits at nonzero-frequency sites cancels $`2^{-|S|}`$. At the remaining sites, both positive moduli of $`K_b`$ include the factors $`B_i(b_i)`$. After applying (4.1), use scalar Cauchy–Schwarz over these remaining outcomes:

```math
\sum_{b_{S^c}}
\left[\mathrm{Tr}(\Omega_D|K_b^\dagger|)
       \mathrm{Tr}(\Omega_D|K_b|)\right]^{1/2}
\le
\left[
\left(\sum_{b_{S^c}}\mathrm{Tr}(\Omega_D|K_b^\dagger|)\right)
\left(\sum_{b_{S^c}}\mathrm{Tr}(\Omega_D|K_b|)\right)
\right]^{1/2}.
```

In each trace sum, $`\sum_{b_i}B_i(b_i)=I_{D_i}`$ removes the zero-frequency factors. The two remaining positive products are the ones bounded by (2.6) in the proof of (4.3). This proves (4.4). $`\square`$

When the shares are uniform on $`s\mathbf 1+C_0`$, the [sharing-character identity](fourier.md#1-the-sharing-coset-and-its-dual-code) gives the block difference

```math
\sum_{k\in C\setminus\{0\}}
  (\omega^{s\sum_i k_i}-\omega^{s'\sum_i k_i})R_b(k),
\qquad C=C_0^\perp.
```

The trace norm adds over classical blocks. Taking the triangle inequality over codewords and using (4.4) gives

```math
\Delta(s,s')
\le\cos\!\left(\frac{\pi}{2p}\right)
\sum_{k\in C\setminus\{0\}}\prod_{i:k_i\ne0}h_i(k_i).
\tag{4.5}
```

The factor $`\cos(\pi/(2p))`$ bounds half the phase difference for every residue in an odd field. Each zero-frequency site contributes one to (4.5) because its average effects were summed before the graph inequality.

The [earlier fourth-moment proof](https://github.com/GoGoKo699/Shamir-Network-Leakage/blob/f3452b19e8a91f5de80d1e754d865a3097dcc999/science/network_bounds.md#4-fourth-moments-with-an-arbitrary-external-reference) used the event-probability form (2.5) and a coefficient bound on $`K^\dagger K`$. The trace-norm argument here keeps both positive moduli and uses the completeness of the average effects in the actual output blocks.

## 5. Pairing the nonzero frequencies

### Lemma 5.1: dimension-free paired-frequency bound

Let $`d>0`$, let $`n\ge d`$, and let $`f_i:\mathbb F_p\to[0,\infty)`$ satisfy

```math
f_i(-k)=f_i(k),
\qquad
\sum_{k\in\mathbb F_p}f_i(k)^d\le1.
```

Then

```math
\sum_{k\ne0}\prod_{i=1}^n f_i(k)
\le2^{1-n/d}.
\tag{5.1}
```

**Proof.** Because $`p`$ is odd, a nonzero frequency $`k`$ is different from $`-k`$. The two corresponding terms in the moment bound are equal, so $`f_i(k)\le2^{-1/d}`$ for $`k\ne0`$. Since $`n\ge d`$,

```math
\sum_{k\ne0}f_i(k)^n
\le2^{-(n-d)/d}\sum_{k\ne0}f_i(k)^d
\le2^{1-n/d}.
```

Hölder's inequality with $`n`$ equal exponents now gives

```math
\sum_{k\ne0}\prod_i f_i(k)
\le\prod_i\left(\sum_{k\ne0}f_i(k)^n\right)^{1/n}
\le2^{1-n/d}.
```

$`\square`$

Taking $`f_i=h_i`$ and $`d=2`$ gives the full-threshold exponent $`n/2`$ for arbitrary external references. The [full-threshold proof](full_threshold.md) explains why only this common-frequency sum remains. The [general-threshold proof](general_threshold.md) uses (4.5) to combine the same local weights over the full dual code.

## 6. Conditioning on actual classical randomness

All estimates above are uniform in the source graph, source dimensions, and measurement family. They therefore remain valid when those choices depend on a genuine classical register $`\Lambda`$, provided the required source condition holds in every conditional state. One may give $`\Lambda`$ to the adversary and apply the appropriate estimate separately in every block of

```math
\rho_{\Lambda DE}
=\sum_\lambda w_\lambda|\lambda\rangle\langle\lambda|\otimes\rho^{(\lambda)}_{DE}.
```

The trace norm of a block-diagonal difference is the weighted sum of the block trace norms. No uniform dimension or graph is needed across the blocks.

This argument requires a classical flag. An arbitrary coherent purification of an unlabelled convex mixture of independent-source states is outside the stated model. In particular, a mixture of $`|0^n\rangle`$ and $`|1^n\rangle`$ has a GHZ purification that permits constant one-bit leakage about an additive secret. The [model assumptions](model.md) describe this distinction and the restriction on communication before the resource snapshot.
