# Shamir Network Leakage

**Can a dense network of pairwise quantum resources turn one leaked bit per Shamir share into significant information about the secret?** Exponential secrecy holds at every fixed reconstruction rate above one half, even when every pair of devices is connected by an independent source and the adversary retains an arbitrary joint quantum reference.

The shares and leaked bits are classical. Each device may perform an arbitrary joint measurement on its local quantum registers, using its share to choose that measurement. The source state is independent of the secret and sharing randomness, and the devices act without communication or adversary feedback during leakage. The [model](science/model.md) specifies the reference and source-independence assumptions.

## Principal results

Let $`n`$ be the number of shares, $`t`$ the reconstruction threshold, and $`p>n`$ an odd prime. Write

```math
\Delta(s,s')=\frac12\|\Omega_s^{BE}-\Omega_{s'}^{BE}\|_1
```

for the distance between the adversary's final states under two chosen secrets.

| Reconstruction regime | Worst-case distance over admissible graphs and references |
|---|---|
| $`t/n\ge1/2+\eta`$ for any fixed $`\eta>0`$ | $`-\log_2\Delta^\star=t/2+O_\eta(\log n)`$, uniformly in the field and evaluation points |
| $`t=n`$, even $`n\ge2`$ | Exactly $`2^{1-n/2}\cos(\pi/(2p))`$ |
| $`t=n`$, odd $`n\ge3`$ | At most the same formula, with matching exponential order |

Here $`\Delta^\star`$ is the maximum possible leakage in the sense of a supremum over permitted strategies and graphs for each prescribed secret pair. Bell pairs on a reconstruction set give the matching exponent. At full threshold with even $`n`$, a perfect matching of Bell pairs attains the exact value. The rate theorem uses a fixed margin above one half. The behavior at the boundary and below remains open in this model.

An elementary finite bound applies when $`q=n/(n-t+1)\ge2`$. With $`\tau=t/n`$ and binary entropy $`h_2`$,

```math
\Delta(s,s')\le
\min\left\{1,\,
\cos\left(\frac{\pi}{2p}\right)
2^{-t/2+(n-t+1)[\tau+h_2(\tau)]}
\right\}.
```

At $`n=1000`$ and $`t=950`$, this is below $`2^{-411}`$. The [general-threshold proof](science/general_threshold.md) gives the sharper finite optimization and the argument for the exact leading exponent.

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

The proof bounds each Fourier word after summing the positive measurement effects at its inactive devices. This gives a product of local second-moment factors on the word’s support. The inherited quantum Finner inequality and weighted code estimates then give a graph-uniform bound. The [related-work comparison](references/RELATED_WORK.md) traces these ingredients and the closest independent-set reduction.

## Learn the argument

The educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [learning route](learning/README.md) connects selected sections to the exact leakage experiment. Its [source-to-project bridge](learning/WATROUS_BRIDGE.md) translates the notation, explains states, measurements, norms and purifications, and works through a complete two-share Bell-pair example.

The [30-milestone map](learning/MILESTONES.md) follows the scientific dependencies: 14 background milestones assemble the classical sharing and quantum information model, and 16 narrative milestones connect the coefficient bounds to the results, their scope and their significance. Finite-field sharing, Fourier analysis, MDS coding and the network inequalities are supplied by the repository and its cited primary research.

## Reproduce the finite checks

From the repository root, run:

```bash
python3 verification/check_results.py
```

The standard-library checks compare direct leakage distributions with the matching constructions, check the support-only coefficient bound on small instances, reproduce the elementary finite bounds, and evaluate the coherent-purification counterexample. Their [documentation](verification/README.md) explains the cases and expected outputs. The graph- and dimension-uniform claims are established by the written proofs.

## Source structure matters

A source graph records which **independent states** are distributed between pairs of devices. It does not specify a stabilizer graph state. Local processing and genuinely classical shared choices are allowed under the stated branchwise condition. Unrestricted communicating preparation can change the resource class, and an arbitrary coherent purification of a classical mixture can enable a GHZ leakage attack. These distinctions are developed in [the boundary examples](science/boundaries.md).

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
