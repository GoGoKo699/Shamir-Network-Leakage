# Where the resource hypothesis applies

The security statement concerns the quantum resource available when the shares arrive. Conditional on a genuinely classical shared seed, the device marginal must have the independent bipartite-source form in [the model](model.md). Each device may process all of its incident source registers locally. The adversary may hold any extension of that device marginal and may process its reference jointly with all leaked bits.

The distinction between a classical seed and a coherent purification is essential. The following example gives an explicit failure of the broader, unlabelled-mixture hypothesis.

## A classical seed gives conditional security

An allowed shared seed is an actual classical register:

```math
\rho_{\Lambda DE}
=\sum_\lambda p_\lambda
|\lambda\rangle\langle\lambda|_\Lambda
\otimes\rho_{DE}^{(\lambda)}.
```

Here trace distance has the $`\Delta`$ convention fixed in [the model](model.md#4-security-convention). The seed probabilities are independent of the secret and sharing randomness. For every seed value, the device marginal of $`\rho_{DE}^{(\lambda)}`$ satisfies the independent-source condition. The states, source graph, and local measurement choices may depend on this seed.

Reveal $`\Lambda`$ to the adversary. The two secret-dependent cq states are block diagonal in the same seed register, so

```math
\mathrm{TD}(\rho_s,\rho_{s'})
=\sum_\lambda p_\lambda\,
\mathrm{TD}\!\left(
\rho_s^{(\lambda)},\rho_{s'}^{(\lambda)}
\right).
```

A uniform conditional bound therefore gives the same overall bound. Discarding the seed can only reduce trace distance. This argument requires the conditional resource condition on the whole experiment, including the adversary's quantum reference.

## An arbitrary purification of the mixture can fail

The phase-and-parity mechanism is the standard GHZ leakage mechanism discussed in [related work](../references/RELATED_WORK.md). Here the adversary's purifying qubit makes its consequence for the resource hypothesis explicit.

Consider the device marginal

```math
\Omega_D=
\frac12|0^n\rangle\langle0^n|
+\frac12|1^n\rangle\langle1^n|.
```

It is a mixture of two product states. Thus a condition that merely places the *unlabelled* device marginal in the convex hull of independent-source states would include it. Now give the adversary the purifying qubit of

```math
|\Psi\rangle_{DE}
=\frac{|0^n\rangle|0\rangle_E+
|1^n\rangle|1\rangle_E}{\sqrt2}.
```

Use the [full-threshold additive coordinates](fourier.md#5-full-threshold-and-additive-coordinates): $`X`$ is uniform subject to $`\sum_iX_i=s`$ in $`\mathbb F_p`$. For a nonzero $`k`$, device $`i`$ measures

```math
M_i(x)=
\cos(2\pi kx/p)\sigma_x+\sin(2\pi kx/p)\sigma_y.
```

Write its outcome as $`b_i\in\{0,1\}`$, with eigenvalue $`(-1)^{b_i}`$. The measurement eigenvector is
```math
|b_i;\theta_i\rangle
=2^{-1/2}\left(
|0\rangle+(-1)^{b_i}e^{i\theta_i}|1\rangle
\right),
\qquad \theta_i=2\pi kX_i/p.
```

Applying the corresponding bras to the device registers leaves the unnormalized reference vector

```math
2^{-(n+1)/2}
\left(
|0\rangle+
(-1)^{\oplus_i b_i}e^{-2\pi i ks/p}|1\rangle
\right).
```

Every output string has probability $`2^{-n}`$. The adversary uses its known parity to apply $`Z^{\oplus_i b_i}`$, obtaining

```math
|\chi_s\rangle=
\frac{|0\rangle+e^{-2\pi i ks/p}|1\rangle}{\sqrt2}.
```

Consequently the distance of the complete cq outputs is

```math
\begin{aligned}
\mathrm{TD}(\rho_s,\rho_{s'})
&=\sqrt{1-|\langle\chi_s|\chi_{s'}\rangle|^2}\\
&=\left|\sin\!\left(\frac{\pi k(s-s')}{p}\right)\right|.
\end{aligned}
```

For any prescribed distinct secrets, choose
$`k(s-s')=(p-1)/2\pmod p`$. The distance is
```math
\cos\!\left(\frac{\pi}{2p}\right),
```
independent of $`n`$. The bits alone are uniform and the reference alone is maximally mixed; their joint state carries the secret-dependent phase.

For comparison, retain a *classical* copy of the preparation label:
```math
\rho_{\Lambda DE}^{\rm flag}
=\frac12\sum_{\ell=0}^1
|\ell\rangle\langle\ell|_\Lambda
\otimes|\ell^n\rangle\langle\ell^n|_D
\otimes|\ell\rangle\langle\ell|_E.
```
The same equatorial measurements now produce independent uniform bits in each branch. The whole output, including $`\Lambda E`$, is independent of the secret, and its distinguishing distance is exactly zero.

The device marginals of these two experiments agree. Their extensions differ, and the coherent extension does not satisfy the branchwise classical-seed hypothesis. In the finite check $`n=5,p=7`$, the coherent distance is $`0.9749279122\ldots`$; applying the product-marginal bound to this inadmissible extension would incorrectly give $`0.8198133865\ldots`$. The [verification script](../verification/README.md) obtains both cq distances directly from the measurement amplitudes.

## A source graph is not a stabilizer graph state

An edge in the source graph denotes a separately supplied bipartite state. If a device has several neighbors, it holds a separate register for each incident source and can measure these registers jointly. A complete source graph is a tensor product over all such independent edge states, with the tensor factors regrouped by device.

By contrast, the qubit *graph state* associated with a graph is prepared by controlled-phase operations on one qubit per vertex. A complete-graph stabilizer state is locally equivalent to a GHZ state; see [Hein et al., *Entanglement in Graph States and its Applications*, Section 4.1 and Figure 9](https://arxiv.org/pdf/quant-ph/0602096). It is not the resource obtained by placing independent Bell pairs on the complete source graph. The theorem's topology-independent guarantee concerns source graphs; it does not imply security for every stabilizer graph state bearing the same graph name.

## Preparation and leakage access

Local preparation channels can be absorbed into each device's measurement. Arbitrary communication during preparation is a different resource: for example, a center can use Bell pairs and teleportation, with communicated correction outcomes, to distribute a GHZ state. The relevant premise is therefore the independent-source state at share arrival, or its explicitly allowed local processing. It is not enough that a preparation protocol began with pairwise Bell states.

The leakage experiment emits one classical bit from each share and permits no communication between devices or feedback from the adversary. This limitation is used by the output-parity expansion and the local Fourier bounds. A leaked qubit, several classical bits, or adaptive requests for additional leakage define different experiments.

The bounds compare two chosen secrets within this single experiment. They do not automatically give a theorem for reusing the same quantum resource across sessions: the first measurements can change and correlate the retained registers, so the resource hypothesis would need to be established again. No repeated-session composition claim is made here.
