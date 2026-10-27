# Secret sharing and independent quantum sources

Shamir sharing hides a classical secret by distributing correlated shares. Ordinary threshold privacy describes an adversary who sees some entire shares and none of the others. Local leakage asks a different question: what can be learned when **every** device emits a short function of its own share? Here the function is implemented by a quantum device that may hold entanglement with other devices and with the adversary.

This project studies one classical leaked bit per device. The quantum resource is supplied by independent sources connecting pairs of devices. A device may combine all of its incident systems in an arbitrary local measurement. The source graph may be complete. The central conclusion is an exponentially small chosen-secret distance at sufficiently high reconstruction rates, uniformly in the graph and all finite quantum dimensions.

## 1. Shares and public parameters

Fix an odd prime $`p>n`$, an integer $`1\le t\le n`$, and distinct nonzero evaluation points $`\alpha_1,\ldots,\alpha_n\in\mathbb F_p`$. To share $`s\in\mathbb F_p`$, sample independent uniform coefficients $`U_1,\ldots,U_{t-1}`$ and set

```math
f(z)=s+\sum_{j=1}^{t-1}U_jz^j,
\qquad Y_i=f(\alpha_i).
```

Any $`t`$ shares reconstruct $`s=f(0)`$, and fewer than $`t`$ shares have a distribution independent of $`s`$. The reconstruction threshold is $`t`$; the reconstruction rate is $`\tau=t/n`$. These parameters and the evaluation points are public.

The sharing algorithm is unchanged. The quantum systems belong to the leakage devices and adversary; the shares and secret remain classical.

## 2. Independent bipartite-source resources

Let $`G=([n],\mathcal E)`$ be any undirected graph. Multiple sources connecting the same pair can be combined into one source. For an edge $`e=\{i,j\}`$, a source supplies a state $`\sigma_e`$ on $`D_{i,e}\otimes D_{j,e}`$. Device $`i`$ also has a local register $`D_{i,0}`$ in state $`\sigma_{i,0}`$. Regrouping tensor factors by device gives

```math
D_i=D_{i,0}\otimes\bigotimes_{e\ni i}D_{i,e},
\qquad
\rho_D=
\left(\bigotimes_{e\in\mathcal E}\sigma_e\right)
\otimes\left(\bigotimes_{i=1}^n\sigma_{i,0}\right).
```

The states may be mixed. There is no fixed upper bound on their finite dimensions, the degree of a vertex, or the number of edges. Isolated vertices and an empty graph are allowed. The entire resource is independent of $`s`$ and the sharing randomness.

The product condition describes the state **before local processing**. Any local channel applied to $`D_i`$ can be absorbed into the later measurement by its adjoint. Communicating preparation that changes this source structure is a different resource model; the [boundary examples](boundaries.md) explain why it matters.

### Three reference scopes

| Scope | State supplied before local processing | Security conclusion |
|---|---|---|
| No external reference | The device state is the product above; the adversary receives only leaked bits | The stronger second-moment bounds apply |
| Reference as a graph vertex | Independent bipartite sources lie on a graph with vertices $`D_1,\ldots,D_n,E`$; no additional purifying system is available outside that graph | The same sharp full-threshold bound applies |
| Arbitrary extension | The device marginal has the product form above, and $`\rho_{DE}`$ is **any** extension of that marginal | The fourth-moment bounds apply, including the general-threshold theorem |

The last scope includes giving the adversary the purifications of all device-device sources and allowing arbitrary joint processing of those purifying registers. More generally, every extension of the fixed marginal can be obtained by a channel on a purification. The source states need not remain independent when conditioned on an adversary measurement outcome. The proofs bound the complete final state, including that outcome, without conditioning away its probability.

The graph-vertex scope is a subclass of the arbitrary-extension scope: tracing out its reference vertex leaves independent local marginal factors from the device-reference edges, together with the device-device sources. Its additional structure permits a stronger bound.

### Classical shared choices

A shared classical seed $`\Lambda`$ may select the graph, states and local strategies, provided the seed is independent of the secret and sharing randomness and the relevant source condition holds in every conditional branch. Give a copy of the seed to the adversary. The joint state then has the form

```math
\rho_{\Lambda DE}
=\sum_\lambda q_\lambda
|\lambda\rangle\langle\lambda|\otimes\rho_{DE}^{(\lambda)}.
```

The weights $`q_\lambda`$ are the same for both challenge secrets. A uniform branchwise distance bound therefore survives averaging. This condition does not permit an arbitrary coherent purification of an unlabelled mixture of network states. A concrete [GHZ counterexample](boundaries.md) separates those two assumptions.

## 3. Local leakage and the adversary's final state

For each share value $`y\in\mathbb F_p`$, device $`i`$ uses a binary POVM

```math
P_i(0\mid y)+P_i(1\mid y)=I_{D_i},
\qquad P_i(b\mid y)\succeq0,
```

and emits its outcome $`B_i\in\{0,1\}`$. This includes arbitrary local computation, local ancillas and randomized binary output, because only the final classical bit is released. Devices do not communicate with one another, and the adversary sends no feedback during leakage. The adversary receives all bits and retains $`E`$; unreleased device registers are traced out.

Let $`P(b\mid y)=\bigotimes_iP_i(b_i\mid y_i)`$. The final classical-quantum state is

```math
\Omega_s^{BE}
=\mathbb E_{Y\mid s}\sum_{b\in\{0,1\}^n}
|b\rangle\langle b|\otimes
\mathrm{Tr}_D\!\left[
(P(b\mid Y)\otimes I_E)\rho_{DE}
\right].
```

The partial trace expression is positive and is the conditional reference state for the POVM outcome. It follows equally from any instrument realizing that POVM, since the device's postmeasurement system is discarded. Any subsequent channel or joint measurement performed by the adversary cannot increase trace distance.

Strategies may depend on public parameters and on the prescribed pair of challenge secrets. Each device's dependence on the realized sharing is restricted to its own share. The theorems hold uniformly over every such strategy.

## 4. Security convention

For distinct secrets $`s,s'`$, define

```math
\Delta(s,s')
=\frac12\left\|\Omega_s^{BE}-\Omega_{s'}^{BE}\right\|_1.
```

With equal prior probabilities for the two secrets, optimal guessing succeeds with probability $`(1+\Delta)/2`$. Thus $`\Delta`$ is the difference between optimal acceptance probabilities, and its half is the excess guessing probability above $`1/2`$. With no reference, $`\Delta`$ is total variation distance between the two bit distributions.

A statement $`\Delta\le2^{-cn}`$ uniformly over every pair of secrets and every permitted strategy is information-theoretic: no running-time or computational-hardness assumption is imposed. The established theorems concern this single leakage episode. They do not by themselves provide a repeated-leakage or later-device-compromise guarantee.

## 5. Results and notation

| Quantity | Meaning |
|---|---|
| $`n,t,p`$ | Number of devices, reconstruction threshold, prime field size |
| $`Y_i,D_i,B_i`$ | Classical share, local quantum register, emitted bit |
| $`E`$ | Retained adversary reference |
| $`M_i(y)=P_i(0\mid y)-P_i(1\mid y)`$ | Hermitian contraction for a binary measurement |
| $`A_i(k)=p^{-1}\sum_y\omega^{-ky}M_i(y)`$ | Operator Fourier coefficient, with $`\omega=e^{2\pi i/p}`$ |
| $`C_0,C`$ | Zero-secret sharing code and its dual |
| $`r=n-t+1,\ q=n/r,\ \tau=t/n`$ | Dual dimension, moment exponent, reconstruction rate |
| $`h_2`$ | Binary entropy, with logarithms to base two |

The [Fourier account](fourier.md) identifies the secret-dependent coefficients. The [network estimates](network_bounds.md) control each coefficient from the resource structure. At [full threshold](full_threshold.md), only one output parity can depend on the secret. The [general-threshold proof](general_threshold.md) sums the remaining coefficients over the dual code.

The reference-secure sufficient rate is about $`0.904205`$, while the no-reference argument gives about $`0.756935`$. These values describe proved sufficient regimes, not optimal security thresholds. Exact optimality is established for even $`n`$ at full threshold in the no-reference and graph-vertex scopes.

**Next:** [Fourier structure of the shares and leaked bits](fourier.md).
