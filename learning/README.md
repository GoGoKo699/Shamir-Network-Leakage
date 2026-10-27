# Learning the Shamir leakage argument

The question begins with a familiar distributed task: several devices hold shares of one secret, and each device releases just one bit. A device may use its share to choose a quantum measurement, and independent sources may connect every pair of devices. The problem is to bound the information in all released bits together, including any quantum system retained by an adversary.

Two kinds of structure matter. Shamir sharing determines which combinations of local inputs can depend on the secret. Source independence constrains the quantum correlations that can turn those combinations into leaked information. The proofs join these structures through Fourier coefficients and the distance between the adversary's final states.

## One anchor and its bridge

The educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**, available through the [author's book page](https://jhwatrous.github.io/books-and-courses.html). Selected parts of Chapters 1–3 supply matrices, states, channels, measurements and discrimination; selected parts of Chapter 6 clarify entanglement and communicating local operations.

The [Watrous bridge](WATROUS_BRIDGE.md) gives precise reading locations in the inspected author manuscript and connects them directly to this experiment. It includes a notation table, the construction of the final classical–quantum state, the roles of three operator norms, the location of purifying registers, and a complete two-share Bell-pair example. In that example, each leaked bit alone is uniform while their parity carries information about the secret.

Watrous supplies the quantum information foundations. The repository supplies the finite-field sharing and Fourier derivations, the dual-code argument, and the application of independent-source network bounds. Their research provenance is recorded in [related work](../references/RELATED_WORK.md) and the [bibliography](../references/references.bib).

## The thirty-milestone map

The [common map](MILESTONES.md) has exactly **M01–M30**, divided according to the two mathematical languages and their eventual synthesis:

| Phase | Range | Progression |
|---|---|---|
| Background/preliminaries | M01–M14 | From prime-field arithmetic and individual quantum registers to the complete sharing, measurement and reference experiment. |
| Narrative/innovation | M15–M30 | From local network coefficients to full-threshold bounds, an attaining construction, general thresholds, resource boundaries and the contribution as a whole. |

Each milestone states a central question, an understanding target, its dependencies and story role, a conceptual connection, and canonical source pointers. The allocation gives both the classical and quantum prerequisites room to develop before they meet. The narrative then connects inherited analytic ingredients to the secrecy result. Its final milestone integrates the assumptions, attribution, meaning and evidence.

## Routes into the science

| Starting question | Read next |
|---|---|
| How do registers and measurements describe this leakage experiment? | [Watrous bridge](WATROUS_BRIDGE.md), then [the model](../science/model.md) |
| Which ideas depend on which prerequisites? | [Thirty milestones](MILESTONES.md) |
| How are the complete proofs organized? | [Scientific route](../science/README.md) |
| Why does full threshold leave only one secret-dependent output parity? | [Input and output Fourier structure](../science/fourier.md), then [the full-threshold theorem](../science/full_threshold.md) |
| Where does the adversary's reference change the estimate? | [Network coefficient bounds](../science/network_bounds.md), especially the second- and fourth-moment arguments |
| How do more surviving parities change the result below full threshold? | [General thresholds and finite optimization](../science/general_threshold.md) |
| Why do classical flags and coherent purifications lead to different conclusions? | [Resource boundaries](../science/boundaries.md) |
| What can be checked by finite computation? | [Verification and its limits](../verification/README.md) |

The reference assumptions stay attached to each result throughout these routes. The exact even-device full-threshold optimum applies to no reference or a reference that is another vertex of the independent-source graph. The arbitrary-extension theorem has a different upper bound. The general-threshold rates are sufficient conditions extracted from finite estimates, with no claim that they are optimal thresholds.

**Navigation:** [Project overview](../README.md) · [Scientific route](../science/README.md) · [Watrous bridge](WATROUS_BRIDGE.md) · [Milestones](MILESTONES.md).
