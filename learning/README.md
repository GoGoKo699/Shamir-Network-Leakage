# Learning the Shamir leakage argument

Several devices hold shares of one secret. Each device can use its share to choose a quantum measurement, and each releases one classical bit. Independent bipartite sources can connect every pair of devices. The problem is to bound the information in the output bits and any quantum system the adversary retains.

Shamir sharing determines which input frequencies can depend on the secret. Source independence bounds the quantum operators attached to those frequencies. The central step sums the outcomes at zero-frequency sites before applying the network inequality. The resulting code sum assigns a factor only to each nonzero coordinate.

## One anchor and its bridge

The educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. Selected parts of Chapters 1–3 supply matrices, states, channels, measurements, polar decomposition and discrimination. Selected parts of Chapter 6 clarify entanglement and communicating local operations. [Author's book page](https://jhwatrous.github.io/books-and-courses.html)

The bridge translates the notation and derives the reference trace-norm bound from polar decomposition. It works through the sum at a zero-frequency site and calculates the full output distribution for two Shamir shares and one Bell pair. In that example, each leaked bit is uniform and their parity carries information about the secret. [Watrous bridge](WATROUS_BRIDGE.md)

This project's finite-field sharing and Fourier derivations, network inequality and weighted dual-code argument build on the quantum information foundations. Their research sources are identified in the [related-work notes](../references/RELATED_WORK.md) and [bibliography](../references/references.bib).

## The thirty-milestone map

The [common map](MILESTONES.md) has exactly **M01–M30**. Each milestone states a question, an understanding target, its dependencies and role in the argument, a conceptual connection and a pointer to the proof.

| Phase | Range | Progression |
|---|---|---|
| Background/preliminaries | M01–M14 | Prime fields, Shamir reconstruction, quantum registers, and the full leakage experiment |
| Narrative/innovation | M15–M30 | Network and polar bounds, the sum over outcomes, the exact even-size optimum, and the matched exponent above one half |

## Routes into the science

| Starting question | Read next |
|---|---|
| How do registers and measurements describe leakage? | [Watrous bridge](WATROUS_BRIDGE.md) and [model](../science/model.md) |
| How can the proof handle a joint quantum reference? | [Polar bound and sum over outcomes](../science/network_bounds.md#4-second-moments-with-an-arbitrary-external-reference) |
| Why is the full-threshold formula exact for even size? | [Full-threshold theorem and Bell matching](../science/full_threshold.md) |
| How do finite bounds and the leading exponent differ below full threshold? | [Explicit finite bound](../science/general_threshold.md#1-explicit-finite-bound) and [sharp exponent above one half](../science/general_threshold.md#2-sharp-exponent-above-one-half) |
| Where does the independent-source assumption matter? | [Resource boundaries](../science/boundaries.md) |
| What does the computation check? | [Verification and its limits](../verification/README.md) |

At full threshold, the upper bound applies to every allowed arbitrary extension, and a Bell matching attains it for an even number of devices. At a reconstruction rate a fixed positive margin above one half, the worst-case distance over admissible graphs has leading exponent $`t/2`$, where $`t`$ is the number of shares needed to reconstruct. The model assumes one leakage episode without communication or feedback and requires a literal independent-source device marginal in each allowed branch.

**Navigation:** [Project overview](../README.md) · [Scientific route](../science/README.md) · [Watrous bridge](WATROUS_BRIDGE.md) · [Milestones](MILESTONES.md).
