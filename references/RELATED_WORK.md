# Related work and attribution

The result studied here concerns **one classical bit of local leakage from each share of the unchanged Shamir scheme**, when the devices use independent bipartite quantum sources on an arbitrary graph. The graph, source dimensions, and local dimensions are unrestricted. The security statements distinguish an adversary who is another vertex of that source graph from an adversary holding an arbitrary extension of the specified device marginal. These are different reference models.

The analytical ingredients below have direct predecessors. The additional conclusion is a trace-distance secrecy guarantee for this network leakage model, uniform in the graph and prime field, together with the exact full-threshold value for even numbers of devices in the source-graph reference model. See the [scientific overview](../README.md) for the precise theorem scopes.

## Local leakage from Shamir sharing

[Shamir's construction](https://doi.org/10.1145/359168.359176) supplies the sharing scheme; it is not modified here. [Benhamouda, Degwekar, Ishai, and Rabin](https://eprint.iacr.org/2019/653) established local leakage resilience for additive sharing and high-threshold Shamir sharing over suitable prime fields using Fourier analysis and additive combinatorics. The linked ePrint's 18 April 2023 revision is the version published in *Journal of Cryptology* 34, article 10 (2021).

Classical local leakage has subsequently reached substantially smaller threshold rates. For example, [Sun and Wootters, arXiv:2610.12357v1](https://arxiv.org/abs/2610.12357v1), prove one-bit local leakage resilience at a threshold rate below one half by an absolute constant. The larger sufficient rates in this repository address a stronger correlated quantum adversary; they are not improvements to the classical threshold rate.

### The closest quantum leakage results

| Source | Resource and output model | Relevant result and comparison |
|---|---|---|
| [Batra, Kitagawa, Nishimaki, and Yamakawa, arXiv:2609.37276v1](https://arxiv.org/abs/2609.37276v1) | One-qubit leakage without prior entanglement; more generally, disjoint bounded entangled blocks without an outside reference. A separate reduction permits an identified entangled support. | Sections 3–5 use Fourier analysis and dual MDS codes. Sections 6.1–6.2 reveal the identified support. Section 6.3, Theorem 18, gives a constant-advantage classical-bit attack using a GHZ resource on a reconstruction set. Overlapping source graphs of unbounded degree do not form bounded disjoint blocks. |
| [Essayag and Zabokritskiy, arXiv:2610.06350v1](https://arxiv.org/abs/2610.06350v1) | One-qubit or classical-bit leakage with finite references; correlated chains, quantum memories, and source-network applications. | Section 7.1 selects an **integral independent vertex set** and reveals its complement. Corollary 7.1 gives a constant-rate security interval when that set has linear size. A complete graph has only a singleton such set. Here the classical-bit network bound remains exponential on complete graphs. |

The second paper's independent device–reference theorem has the sharp full-threshold exponential base $2/\pi$ for a classical bit, with arbitrary finite references; the present network bounds do not improve that special case. Its quantum-output and correlated-memory results also have scopes beyond this repository. The comparison is therefore between specific resource/output models, rather than a model-wide domination claim.

The distinction from a GHZ resource is substantive. The GHZ attack is already established by Batra and coauthors, using the phase-accumulation method of [Buhrman, van Dam, Høyer, and Tapp](https://doi.org/10.1103/PhysRevA.60.2737). The Bell-pair construction here uses the same equatorial measurement algebra to attain a different, source-restricted optimum. No new GHZ attack or phase-accumulation principle is claimed.

## Imported analytic ingredients

### Network Finner and the complex contraction

[Finner's inequality](https://doi.org/10.1214/aop/1176989534) bounds products of functions of overlapping independent variables. [Renou, Wang, Boreiri, Beigi, Gisin, and Brunner](https://doi.org/10.1103/PhysRevLett.123.070403) prove its quantum network counterpart for independent bipartite sources: their Theorem 2 and Appendix D give event and positive-function bounds for fractional independent-set weights.

The all-half-weight case applies to every source graph. Schmidt expansion followed by classical graph Finner gives the associated weighted Hilbert–Schmidt contraction for complex local operators. Positivity of those Fourier operators is not required. The proof in this repository spells out this form because the displayed event theorem alone should not be quoted as a theorem about arbitrary non-Hermitian operators. The inequality and the source-graph mechanism are inherited.

### Fourier analysis and opposite frequencies

The translation from Shamir cosets to sums over a dual MDS code follows the established leakage approach. The matrix-valued version and block estimates are explicit in Batra and coauthors, Sections 3–5. Essayag and Zabokritskiy, Lemmas 3.1–3.2, explicitly exploit opposite Fourier frequencies to sharpen moment bounds. Pairing a frequency with its negative is therefore also an inherited idea.

Here a binary POVM gives a Hermitian contraction at each device. Combining its paired Fourier budget with the network contraction yields a second-moment bound in the source-graph reference model. Trace-norm duality, state Cauchy–Schwarz, and event Finner instead yield a fourth-moment budget under an arbitrary reference. The secret-dependent output-parity calculation connects these budgets to the stated secrecy bounds.

### The MDS inequality and minimum-distance weighting

For an MDS code $C$ of length $n$ and dimension $k$, [Horinaga and Yamakawa, arXiv:2607.14650v2](https://arxiv.org/abs/2607.14650v2), Theorem 3.1, prove the inequality

```math
\sum_{a\in C}\prod_{i=1}^n h_i(a_i)
\le
\prod_{i=1}^n
\left(\sum_z h_i(z)^{n/k}\right)^{k/n}
\qquad (h_i\ge0).
```

Their Fourier-bias analysis also introduces a weight parameter to exploit the dual code's minimum distance. Batra and coauthors, Lemma 4, give a block version. Essayag and Zabokritskiy, Lemma 3.4, present the singleton inequality with the elementary proof obtained by applying Hölder to all $k$-coordinate projections. The proof and weighting argument used here are included for completeness and are not new inequalities.

Horinaga–Yamakawa v2, revised 22 October 2026, treats optimal polynomial intersection and Max-LINSAT with quantum membership-oracle access. Its subsequent-work discussion credits Batra and coauthors for quantum leakage applications. It does not state a security theorem for independent entanglement-source networks.

## Other network and XOR-game results

[Briët, Buhrman, Lee, and Vidick, *Multipartite entanglement in XOR games*](https://rintonpress.com/xxqic13/qic-13-34/0334-0360.pdf), study multiplayer XOR games with clique-wise entanglement. Theorem 2 of the published 2013 version bounds the quantum/classical bias ratio by a factor depending exponentially on the number of source coalitions. For pair sources, that parameter is the number of edges. This does not provide the present graph-uniform secrecy bound on dense networks. Their general game comparison and the fixed Shamir-input distribution studied here are different statements.

An accessible prior account of the same contraction mechanism is [Ruge Lin, *GHZ Communication Cost*](https://github.com/GoGoKo699/GHZ-Communication-Cost/tree/99bd0004bcd1b395d27bff9b092db64dc0672c24), at the pinned revision shown in the link. Its [branch-bound proof](https://github.com/GoGoKo699/GHZ-Communication-Cost/blob/99bd0004bcd1b395d27bff9b092db64dc0672c24/science/branch-bound.md), equations B2–B4, contains the complex Schmidt/Finner calculation. Its [communication converse](https://github.com/GoGoKo699/GHZ-Communication-Cost/blob/99bd0004bcd1b395d27bff9b092db64dc0672c24/science/communication-converses.md), Corollary C4, already controls GHZ preparation uniformly over arbitrary source graphs.

That preparation result bounds a quantum output's GHZ fidelity under charged classical communication. The present task bounds distinguishability between two distributions of **classical sharing inputs** after local leakage. A coherent superposition satisfying the sharing promise is not a free resource in the preparation model. The secrecy calculation consequently requires the share-coset Fourier and output-parity analysis in addition to the inherited network inequality. This repository does not establish a new preparation-communication theorem.

## Model distinctions needed when using these comparisons

The arbitrary-reference theorem assumes that the specified device marginal has the declared independent bipartite-source form. This is stronger than saying that a state is a mixture of such marginals with an arbitrary coherent purification. Classical seeds are handled by conditioning on actual classical branches in which the source hypothesis holds.

The exact even-device optimum uses the narrower source-graph reference model, including the case without a reference. Its value is not asserted to be optimal for arbitrary purifying references. Nor does the one-bit theorem cover emitted qubits, adaptive feedback, free LOCC preprocessing, or repeated leakage from a stored share. These distinctions keep the comparisons at the same security and resource level.

## Source versions

The bibliography is in [references.bib](references.bib). The source versions used for the close comparisons are:

| Key | Version and precise passage |
|---|---|
| `BatraEtAl2026` | arXiv:2609.37276v1, 29 September 2026; Sections 3–6, Lemma 4, and Section 6.3, Theorem 18. |
| `EssayagZabokritskiy2026` | arXiv:2610.06350v1, 5 October 2026; Lemmas 3.1–3.4, Corollary 4.3, Section 7.1 and Corollary 7.1. |
| `HorinagaYamakawa2026` | arXiv:2607.14650v2, 22 October 2026; Theorem 3.1, Fourier-bias weighting, Sections 1.3–1.4. |
| `RenouEtAl2019` | *Physical Review Letters* 123, 070403 (2019); author version arXiv:1901.08287v1, Theorem 2 and Appendix D. |
| `BrietEtAl2013` | *Quantum Information and Computation* 13(3–4), 334–360 (2013); Theorem 2, p. 337. The journal manuscript was revised 26 November 2012; the earlier arXiv:0911.4007v1 has a different title. |
| `LinGHZ2026` | Public research notes at commit `99bd0004bcd1b395d27bff9b092db64dc0672c24`; branch-bound B2–B4 and communication-converse C4. |

The 2026 arXiv sources are cited as preprints. The repository source is cited as public research notes. Their bibliographic status is distinct from that of the published journal articles.
