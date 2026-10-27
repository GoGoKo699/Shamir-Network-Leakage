# Shamir Network Leakage

**Can a dense network of pairwise quantum resources turn one leaked bit per Shamir share into significant information about the secret?** Independent bipartite sources still permit exponential secrecy, even when every pair of devices is connected and the adversary retains quantum side information.

The shares and leaked bits are classical. Each device may perform an arbitrary joint measurement on its local quantum registers, using its share to choose that measurement. The source state is independent of the secret and sharing randomness, and the devices act without communication or adversary feedback during leakage. The [model](science/model.md) specifies the reference and source-independence assumptions.

## Principal results

Let $`n`$ be the number of shares, $`t`$ the reconstruction threshold, and $`p>n`$ an odd prime. Write

```math
\Delta(s,s')=\frac12\|\Omega_s^{BE}-\Omega_{s'}^{BE}\|_1
```

for the distance between the adversary's final states under two chosen secrets.

| Reference scope | Reconstruction regime | Guarantee |
|---|---|---|
| Arbitrary extension of the independent-source device marginal | Every fixed $`t/n>0.9042045925\ldots`$ by a positive margin | Exponentially small $`\Delta`$, uniformly over all graphs and finite dimensions |
| No external quantum reference | Every fixed $`t/n>0.7569352556\ldots`$ by a positive margin | A stronger sufficient exponential-security regime |
| Arbitrary extension | $`t=n`$, $`n\ge4`$ | $`\Delta\le2^{1-n/4}\cos(\pi/(2p))`$ |
| No reference, or reference as another vertex of the bipartite-source graph | $`t=n`$, $`n\ge2`$ | $`\Delta\le2^{1-n/2}\cos(\pi/(2p))`$; exact for even $`n`$ over the allowed class |

In the last row, a matching of Bell pairs attains the bound. No denser network improves this worst-case value. A fixed graph attains it whenever it contains a perfect matching. The bound with an arbitrary purifying reference is not asserted sharp, and both general-threshold rates are sufficient conditions rather than optimal thresholds.

The arbitrary-reference finite bound is explicit. Put $`\tau=t/n`$ and assume $`n/(n-t+1)\ge4`$. Then

```math
\Delta(s,s')\le
\min\left\{1,
2^{\,n-5t/4+(n-t+1)[\tau+h_2(\tau)]}
\right\},
```

where $`h_2`$ is binary entropy. At $`n=1000`$ and $`t=950`$, this bound is below $`2^{-124}`$. The [general-threshold proof](science/general_threshold.md) gives the finite optimization and the asymptotic rate statements.

## Read the science

Start with the [scientific route](science/README.md) or go directly to a result:

| Question | Authoritative account |
|---|---|
| What can the leakage devices and adversary do? | [Sharing and resource model](science/model.md) |
| How does the secret enter the leaked state? | [Share cosets and output parities](science/fourier.md) |
| Why does the source graph give a uniform bound? | [Network coefficient estimates](science/network_bounds.md) |
| What is exact when all shares are needed? | [Full-threshold theorem and Bell-pair construction](science/full_threshold.md) |
| How can reconstruction omit some shares? | [General thresholds and finite bounds](science/general_threshold.md) |
| Which resource changes defeat the argument? | [Classical flags, purification and preparation](science/boundaries.md) |
| Which ingredients and nearby results are established prior work? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| What calculations can be reproduced? | [Verification](verification/README.md) |

The graph inequality, Fourier methods and MDS inequality are inherited. The security result combines them to cover **arbitrarily overlapping independent bipartite sources**, including complete source graphs. The closest source-network reduction selects a large integral independent vertex set; the present one-bit bound remains effective when no such set exists. The [comparison](references/RELATED_WORK.md) preserves the different output and reference assumptions of earlier results.

## Learn the argument

The educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [learning route](learning/README.md) connects selected sections to the exact leakage experiment. Its [source-to-project bridge](learning/WATROUS_BRIDGE.md) translates the notation, explains states, measurements, norms and purifications, and works through a complete two-share Bell-pair example.

The [30-milestone map](learning/MILESTONES.md) follows the scientific dependencies: 14 background milestones assemble the classical sharing and quantum information model, and 16 narrative milestones connect the coefficient bounds to the results, their scope and their significance. Finite-field sharing, Fourier analysis, MDS coding and the network inequalities are supplied by the repository and its cited primary research.

## Reproduce the finite checks

From the repository root, run:

```bash
python3 verification/check_results.py
```

The standard-library checks compare direct leakage distributions with the analytical Bell-pair value, verify finite-field Fourier bookkeeping, reproduce the scalar optimizations, and evaluate the coherent-purification counterexample. Their [documentation](verification/README.md) explains the cases and expected outputs. The graph- and dimension-uniform claims are established by the written proofs.

## Source structure matters

A source graph records which **independent states** are distributed between pairs of devices. It does not specify a stabilizer graph state. Local processing and genuinely classical shared choices are allowed under the stated branchwise condition. Unrestricted communicating preparation can change the resource class, and an arbitrary coherent purification of a classical mixture can enable a GHZ leakage attack. These distinctions are developed in [the boundary examples](science/boundaries.md).

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
