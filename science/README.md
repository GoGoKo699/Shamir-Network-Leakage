# Scientific route

Each device holds one classical Shamir share and releases one classical bit after a share-dependent quantum measurement. The attacker receives all bits and an arbitrary quantum reference. Even a complete network of independent pair sources permits exponential secrecy at every reconstruction rate a fixed margin above one half.

## A connected reading route

1. [Model](model.md) specifies the shares, the independent-source marginal, and chosen-secret trace distance.
2. [Fourier structure](fourier.md) expands every classical output block. The sharing coset retains only dual-code words.
3. [Network estimates](network_bounds.md) show how the polar trace-norm bound allows the inactive outcomes of a word to be summed before applying quantum Finner. The remaining local weights have a paired second-moment budget.
4. [Full threshold](full_threshold.md) reduces the difference to one parity and uses Bell pairs to attain the exact even-size optimum under arbitrary quantum extensions.
5. [General thresholds](general_threshold.md) gives explicit finite bounds and the exact leading exponent above one half. A matching on reconstruction positions attains that exponent.
6. [Resource boundaries](boundaries.md) explains the role of a classical flag, the device marginal, and the absence of communication.

In each Fourier word, the effects at its zero-frequency devices are positive and sum to identity. The trace-norm argument lets this sum occur before the network inequality. The resulting product uses only the nonzero positions. Pairing opposite frequencies limits each nonzero factor to $`1/\sqrt2`$. The dual code controls how many words with large factors can contribute.

| Conclusion | Proof ingredients |
|---|---|
| Arbitrary-reference bound for each Fourier word | Polar decomposition, state Cauchy–Schwarz, inactive-effect completeness and positive quantum Finner |
| Explicit finite bound | Dual-code minimum distance and weighted MDS Hölder |
| Sharp exponent above one half | Weighted list recovery over generalized Reed–Solomon codes and the construction on a reconstruction set |
| Exact even-size full-threshold distance | Full-parity identity, odd-prime phase factor and a Bell-pair matching |

The [related-work account](../references/RELATED_WORK.md) identifies the inherited inequalities and compares the resource models. The [verification route](../verification/README.md) reproduces finite examples. The optimal security transition at or below rate one half and the exact odd-size finite optimum remain open here.
