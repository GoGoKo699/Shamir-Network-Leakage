# Scientific route

The question is whether independent pairwise entanglement can help noncommunicating leakage devices overcome the secrecy of classical Shamir shares. Each device emits one classical bit. The attacker may combine all those bits with a retained quantum system. The answer depends on the structure of the supplied resource, even when its graph is complete and its local dimensions are unbounded.

## A connected reading route

1. [Model](model.md): specify classical Shamir sharing, the independent source state, three reference scopes, and chosen-secret trace distance.
2. [Fourier structure](fourier.md): express the sharing distribution as an affine MDS code and the leaked state through output parities.
3. [Network estimates](network_bounds.md): bound a Fourier coefficient by local weighted norms, then obtain symmetric second or fourth moments.
4. [Full threshold](full_threshold.md): reduce the secret dependence to the full parity, prove the finite-prime bound and attain the even-device optimum with Bell pairs.
5. [General thresholds](general_threshold.md): use the dual code's minimum weight and the MDS Hölder inequality to retain exponential secrecy below full threshold.
6. [Resource boundaries](boundaries.md): compare an actual classical flag with a coherent purification and explain the limits imposed by the preparation model.

The [related-work account](../references/RELATED_WORK.md) identifies the imported inequalities and gives the closest model comparisons. The [verification route](../verification/README.md) reproduces finite examples and scalar optimizations.

## How the argument works

An individual leakage device can choose a complicated measurement on many quantum systems. Its output is still one classical bit, so the measurement is described by a Hermitian contraction. Fourier expansion in its share value gives local operators with a bounded moment budget.

The independent sources constrain how these local operators combine. In a graph, each source index is shared by two vertices. Repeated Cauchy–Schwarz bounds the resulting tensor contraction by a product of local weighted Hilbert–Schmidt norms. This is the established graph Finner mechanism. Giving the adversary an arbitrary extension requires an additional state Cauchy–Schwarz step; the resulting local budget is a fourth moment instead of a second moment.

The shares supply another constraint. A nonzero Fourier word that survives averaging over the sharing randomness has at least $`t`$ nonzero coordinates. Every secret-dependent contribution therefore contains many local factors. Pairing opposite frequencies and applying the MDS inequality converts those factors into an exponential bound without a field-size loss.

At full threshold, all proper share marginals are secret independent. Only the parity of every leaked bit can distinguish secrets, and the argument becomes sharp in the narrower reference model. Independent Bell pairs attain the resulting exponent: after averaging over the additive sharing constraint, only two common-frequency terms survive.

## Proof dependencies

| Conclusion | Necessary ingredients |
|---|---|
| Full-threshold bound without a reference or with a graph-vertex reference | Exact output-parity equality; complex graph contraction; paired second moments |
| Exact even-device optimum in that scope | The upper bound; the explicit Bell-pair measurement construction |
| Full-threshold bound with arbitrary reference | Trace-norm duality; state Cauchy–Schwarz; event Finner; paired fourth moments |
| General-threshold arbitrary-reference bound | Output-parity trace-norm triangle; dual-code expansion; fourth moments; weighted MDS Hölder |
| Stronger general-threshold bound without a quantum reference | Scalar output Parseval and Minkowski; second moments; convex local-moment endpoint bound; weighted MDS Hölder |

The optimum for even-device full-threshold leakage and the sufficient general-threshold rates are distinct statements. The latter do not identify the true transition between security and insecurity. Likewise, a complete **source** graph and a complete stabilizer graph state describe different supplied resources.

Each claim has one proof home in the pages above. The mathematical result concerns the declared single, noninteractive leakage episode; the boundary examples show why changing the reference or preparation assumptions can change the answer.
