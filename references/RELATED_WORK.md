# Related work and attribution

The result concerns **one classical bit of local leakage from each share of the unchanged Shamir scheme**. Independent bipartite quantum sources may connect any pair of devices. The adversary may hold any finite extension of the resulting device marginal.

The [support-only Fourier bound](../science/network_bounds.md#4-second-moments-with-an-arbitrary-external-reference) lets existing weighted code estimates apply at every fixed reconstruction rate above one half. Over all permitted graphs and extensions, the leading exponent is half the reconstruction threshold. The Bell-pair matching gives the exact even-size value when reconstruction requires every share.

## Local leakage from Shamir sharing

[Shamir's construction](https://doi.org/10.1145/359168.359176) supplies the sharing scheme; it is not modified here. [Benhamouda, Degwekar, Ishai, and Rabin](https://eprint.iacr.org/2019/653) established local leakage resilience for additive sharing and high-threshold Shamir sharing over suitable prime fields using Fourier analysis and additive combinatorics. The linked ePrint's 18 April 2023 revision is the version published in *Journal of Cryptology* 34, article 10 (2021).

Classical local leakage has subsequently reached substantially smaller threshold rates. For example, [Sun and Wootters, arXiv:2610.12357v2](https://arxiv.org/abs/2610.12357v2), prove one-bit local leakage resilience below one half by an absolute constant. [Zhang, Wang, and Kong, arXiv:2611.12325](https://arxiv.org/abs/2611.12325), give the explicit classical sufficient rate 0.489. Those results concern classical local leakage. The source-network result here permits quantum-assisted devices and arbitrary quantum side information.

### The closest quantum leakage results

| Source | Resource and output model | Relevant result and comparison |
|---|---|---|
| [Batra, Kitagawa, Nishimaki, and Yamakawa, arXiv:2609.37276v1](https://arxiv.org/abs/2609.37276v1) | One-qubit leakage without prior entanglement; more generally, disjoint bounded entangled blocks without an outside reference. A separate reduction permits an identified entangled support. | Sections 3–5 use Fourier analysis and dual MDS codes. Sections 6.1–6.2 reveal the identified support. Section 6.3, Theorem 18, gives a constant-advantage classical-bit attack using a GHZ resource on a reconstruction set. Overlapping source graphs of unbounded degree do not form bounded disjoint blocks. |
| [Essayag and Zabokritskiy, arXiv:2610.06350v2](https://arxiv.org/abs/2610.06350v2) | One-qubit or classical-bit leakage with finite references; correlated chains, quantum memories, and source-network applications. | Supplement S7.1 selects an **integral independent vertex set** and reveals its complement. Corollary S7.1 uses an independent set of linear size for a constant-rate guarantee. The one-bit result here covers complete source graphs, whose maximum independent set is a singleton. |

The independent device–reference theorem in Essayag and Zabokritskiy has sharp base $``2/\pi``$ per required share for a classical bit. The broader source network studied here has base $``1/\sqrt2``$, attained by entangling pairs of leakage devices. The same paper treats quantum outputs and correlated memories under other hypotheses.

The distinction from a GHZ resource is substantive. The GHZ attack is already established by Batra and coauthors, using the phase-accumulation method of [Buhrman, van Dam, Høyer, and Tapp](https://doi.org/10.1103/PhysRevA.60.2737). The Bell-pair construction here uses the same equatorial measurement algebra to attain a different, source-restricted optimum. No new GHZ attack or phase-accumulation principle is claimed.

## Imported analytic ingredients

### Network Finner and the complex contraction

[Finner's inequality](https://doi.org/10.1214/aop/1176989534) bounds products of functions of overlapping independent variables. [Renou, Wang, Boreiri, Beigi, Gisin, and Brunner](https://doi.org/10.1103/PhysRevLett.123.070403) prove its quantum network counterpart for independent bipartite sources: their Theorem 2 and Appendix D give event and positive-function bounds for fractional independent-set weights.

The all-half-weight case applies to every source graph. Schmidt expansion followed by classical graph Finner gives the associated weighted Hilbert–Schmidt contraction for complex local operators. Positivity of those Fourier operators is not required. The proof in this repository spells out this form because the displayed event theorem alone should not be quoted as a theorem about arbitrary non-Hermitian operators. The inequality and the source-graph mechanism are inherited.

### Fourier analysis and opposite frequencies

The translation from Shamir cosets to sums over a dual MDS code follows the established leakage approach. The matrix-valued version and block estimates are explicit in Batra and coauthors, Sections 3–5. Essayag and Zabokritskiy’s paired-moment bounds in Supplement S1 explicitly exploit opposite Fourier frequencies. Pairing a frequency with its negative is therefore also an inherited idea.

Here a binary POVM gives a Hermitian contraction at each device. A polar trace-norm bound leaves two expectations of positive product observables. Summing the inactive outcomes in those expectations removes their effects by completeness. Applying positive quantum Finner after that sum produces a second-moment weight on each nonzero coordinate, even with an arbitrary reference.

### The MDS inequality and minimum-distance weighting

For an MDS code $`C`$ of length $`n`$ and dimension $`k`$, [Horinaga and Yamakawa, arXiv:2607.14650v2](https://arxiv.org/abs/2607.14650v2), Theorem 3.1, prove the inequality

```math
\sum_{a\in C}\prod_{i=1}^n h_i(a_i)
\le
\prod_{i=1}^n
\left(\sum_z h_i(z)^{n/k}\right)^{k/n}
\qquad (h_i\ge0).
```

Their Fourier-bias analysis introduces a weight parameter to exploit the dual code’s minimum distance. Batra and coauthors, Lemma 4, give a block version. Essayag and Zabokritskiy give related block and weighted estimates in version 2, Supplement S5.1. The proof and weighting argument used here are included for completeness and are not new inequalities.

Horinaga–Yamakawa v2, revised 22 October 2026, treats optimal polynomial intersection and Max-LINSAT with quantum membership-oracle access. Its subsequent-work discussion credits Batra and coauthors for quantum leakage applications. It does not state a security theorem for independent entanglement-source networks.

### List recovery and the sharp exponent

[Sun and Wootters](https://arxiv.org/abs/2610.12357v2) use weighted dual-code sums in local leakage. [Essayag and Zabokritskiy v2](https://arxiv.org/abs/2610.06350v2), Lemma 3.5, state the weighted estimate for generalized Reed–Solomon codes and use it for independent device–reference pairs. Its field-uniform polynomial factor comes from [Jeronimo, Theorem 1.1 and Corollary 8.1](https://eccc.weizmann.ac.il/report/2026/169/). The [general-threshold proof](../science/general_threshold.md#2-sharp-exponent-above-one-half) gives the singleton specialization with one Fourier factor per active coordinate. The dense-network conclusion depends on the reference-valued coefficient reduction and the Bell-pair construction.

## Other network and XOR-game results

[Briët, Buhrman, Lee, and Vidick, *Multipartite entanglement in XOR games*](https://rintonpress.com/xxqic13/qic-13-34/0334-0360.pdf), study multiplayer XOR games with clique-wise entanglement. Theorem 2 of the published 2013 version bounds the quantum/classical bias ratio by a factor depending exponentially on the number of source coalitions. For pair sources, that parameter is the number of edges. This does not provide the present graph-uniform secrecy bound on dense networks. Their general game comparison and the fixed Shamir-input distribution studied here are different statements.

An accessible prior account of the same contraction mechanism is [Ruge Lin, *GHZ Communication Cost*](https://github.com/GoGoKo699/GHZ-Communication-Cost/tree/99bd0004bcd1b395d27bff9b092db64dc0672c24), at the pinned revision shown in the link. Its [branch-bound proof](https://github.com/GoGoKo699/GHZ-Communication-Cost/blob/99bd0004bcd1b395d27bff9b092db64dc0672c24/science/branch-bound.md), equations B2–B4, contains the complex Schmidt/Finner calculation. Its [communication converse](https://github.com/GoGoKo699/GHZ-Communication-Cost/blob/99bd0004bcd1b395d27bff9b092db64dc0672c24/science/communication-converses.md), Corollary C4, already controls GHZ preparation uniformly over arbitrary source graphs.

That preparation result bounds a quantum output's GHZ fidelity under charged classical communication. The present task bounds distinguishability between two distributions of **classical sharing inputs** after local leakage. A coherent superposition satisfying the sharing promise is not a free resource in the preparation model. The secrecy calculation consequently requires the share-coset Fourier and output-parity analysis in addition to the inherited network inequality. This repository does not establish a new preparation-communication theorem.

## Model distinctions needed when using these comparisons

The arbitrary-reference theorem assumes that the specified device marginal has the declared independent bipartite-source form. This is stronger than saying that a state is a mixture of such marginals with an arbitrary coherent purification. Classical seeds are handled by conditioning on actual classical branches in which the source hypothesis holds.

The exact even-device optimum admits the full arbitrary-extension model. It concerns a single noninteractive episode with one classical bit per share. Emitted qubits, adaptive feedback, communicating preparation, and repeated leakage define other experiments.

## Source versions

The bibliography is in [references.bib](references.bib). The source versions used for the close comparisons are:

| Key | Version and precise passage |
|---|---|
| `BatraEtAl2026` | arXiv:2609.37276v1, 29 September 2026; Sections 3–6, Lemma 4, and Section 6.3, Theorem 18. |
| `EssayagZabokritskiy2026` | arXiv:2610.06350v2, 4 November 2026. Lemma 3.5, Corollary 4.3, Supplements S1, S5.1, and S7.1. |
| `HorinagaYamakawa2026` | arXiv:2607.14650v2, 22 October 2026; Theorem 3.1, Fourier-bias weighting, Sections 1.3–1.4. |
| `SunWootters2026` | arXiv:2610.12357v2. Weighted code counting and classical local leakage. |
| `Jeronimo2026` | ECCC TR26-169. Theorem 1.1 and Corollary 8.1. |
| `ZhangWangKong2026` | arXiv:2611.12325. Explicit classical one-bit threshold from the abstract. |
| `RenouEtAl2019` | *Physical Review Letters* 123, 070403 (2019); author version arXiv:1901.08287v1, Theorem 2 and Appendix D. |
| `BrietEtAl2013` | *Quantum Information and Computation* 13(3–4), 334–360 (2013); Theorem 2, p. 337. The journal manuscript was revised 26 November 2012; the earlier arXiv:0911.4007v1 has a different title. |
| `LinGHZ2026` | Public research notes at commit `99bd0004bcd1b395d27bff9b092db64dc0672c24`; branch-bound B2–B4 and communication-converse C4. |

The 2026 arXiv sources are cited as preprints. The repository source is cited as public research notes. Their bibliographic status is distinct from that of the published journal articles.
