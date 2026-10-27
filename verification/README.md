# Reproducible checks

Run the checks with Python 3.10 or later:

```sh
python3 verification/check_results.py
```

The script uses only the Python standard library, reads its expected-results file relative to its own location, and also works when invoked from another working directory. A complete run takes less than a second in the development environment. It performs finite calculations that support the examples and catch normalization or parameter errors. The universal security statements depend on the analytic proofs.

## What is checked

| Calculation | Independent inputs and comparison | Scope |
|---|---|---|
| Bell-pair leakage | Compute each pair's Born probabilities from measurement eigenvectors, enumerate additive sharings and all output strings, and compare the resulting total variation with $`2^{1-n/2}\cos(\pi/(2p))`$. | $`n=2,4,6`$, with $`p=3,5,7`$, respectively; selected distinct secrets. |
| Shamir Fourier bookkeeping | Enumerate polynomial-sharing cosets and their direct leakage histograms; independently enumerate the dual code and reconstruct every output parity and probability. | $`(n,t,p)=(4,3,5)`$ and $`(5,3,7)`$. All Fourier comparisons in this group are exact. |
| MDS facts used in those examples | Check the dual's cardinality, minimum nonzero weight, and every projection onto $`n-t+1`$ coordinates. | The same two finite codes. |
| Bound optimization | Numerically minimize the original finite moment bounds and compare their values with the closed expressions; independently locate both sufficient-rate crossings by numerical minimization. | Three arbitrary-reference parameter choices, both branches of the finite no-reference optimizer, and the two asymptotic sufficient rates. |
| Classical-flag boundary | Construct the output cq blocks by applying the measurement eigenbras to a GHZ purification and to its dephased classical mixture. Compute the $`2\times2`$ Hermitian trace norms directly. | $`n=5,p=7`$, with both leakage bits and the reference retained. |

The exact Fourier group uses integer polynomials. Multiplication first takes place modulo $`z^p-1`$; reduction by $`1+z+\cdots+z^{p-1}=0`$ then evaluates the expressions at a primitive $`p`$-th root. Rational results use Python's Fraction type. This checks field constraints, Fourier phases, factors of $`p`$, and Walsh factors of $`2`$ without a floating-point Fourier transform.

The chosen general-threshold examples have secret-dependent proper output parities. They therefore test the terms that disappear at full threshold but must be retained below full threshold. They are checks of the Fourier identity, not claims that the high-threshold security bound is useful at those small parameters.

## Recorded results

The computed record is in [expected_results.json](expected_results.json). Representative values are:

| Quantity | Result |
|---|---:|
| Matching optimum, $`n=4,p=5`$ | $`0.4755282581475768`$ |
| Matching optimum, $`n=6,p=7`$ | $`0.2437319780454559`$ |
| Arbitrary-reference sufficient rate | $`0.9042045924785356`$ |
| No-reference sufficient rate | $`0.7569352555764817`$ |
| Optimized finite log-base-two bound, $`n=1000,t=950`$ | $`-124.4437551870862`$ |
| Coherent-purification cq distance, $`n=5,p=7`$ | $`0.9749279121818236`$ |
| Genuinely classical flagged-mixture cq distance in that example | $`0`$ |

The finite log bound refers to the displayed security upper bound, not an attack achieving that distance. The sufficient rates describe where the stated analytic bounds become exponentially small; the computation does not establish optimal security thresholds.

For the full machine-readable calculation, run:

```sh
python3 verification/check_results.py --json
```

The default run compares freshly calculated results with the recorded snapshot. Floating-point entries use an absolute/relative tolerance of $`2\times10^{-10}`$; exact fractions and integer identities use exact comparison. Numerical minimizer locations are deliberately omitted from the snapshot because floating-point plateaus can move an optimizer slightly without changing the minimum value.

To update the record after an intentional, reviewed change:

```sh
python3 verification/check_results.py --write-expected
```

That command writes only after every independent identity and inequality check has passed. Updating the snapshot cannot bypass those checks. Review a changed snapshot together with the scientific reason for the change.

## Limits of this evidence

These calculations verify the stated finite instances and the optimization formulas. They do not establish a dimension-independent graph inequality, optimize over all measurements, cover all finite fields or graphs, or prove composition across repeated leakage experiments. The classical-flag counterexample is explained analytically in [the model boundaries](../science/boundaries.md).
