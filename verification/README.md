# Reproducible checks

Run the checks with Python 3.10 or later:

```sh
python3 verification/check_results.py
```

The script uses only the Python standard library, reads its expected-results file relative to its own location, and also works when invoked from another working directory. A complete run takes a few seconds. It performs finite calculations that support the examples and catch normalization or parameter errors. The universal security statements depend on the analytic proofs.

## What is checked

| Calculation | Independent inputs and comparison | Scope |
|---|---|---|
| Bell-pair leakage | Compute each pair's Born probabilities from measurement eigenvectors, enumerate additive sharings and all output strings, and compare the resulting total variation with $`2^{1-n/2}\cos(\pi/(2p))`$. | $`n=2,4,6`$, with $`p=3,5,7`$, respectively; selected distinct secrets. |
| Odd reconstruction set | Enumerate Shamir shares on a chosen reconstruction set, check the Lagrange-scaled additive shares, and compute the leakage from the Bell pairs and the singleton bit. | $`(n,t,p)=(5,3,7)`$ and $`(6,5,7)`$ with proper reconstruction subsets. |
| Shamir Fourier bookkeeping | Enumerate polynomial-sharing cosets and their direct leakage histograms; independently enumerate the dual code and reconstruct every output parity and probability. | $`(n,t,p)=(4,3,5)`$ and $`(5,3,7)`$. All Fourier comparisons in this group are exact. |
| MDS facts used in those examples | Check the dual's cardinality, minimum nonzero weight, and every projection onto $`n-t+1`$ coordinates. | The same two finite codes. |
| Support-only coefficient bound | Evaluate reference-valued outcome blocks directly and by Fourier expansion on a triangle with one purified mixed source and two Bell sources. Check the sum of trace norms against the support-only product for every nonzero dual word. | $`(n,t,p)=(3,2,5)`$. Four nonvanishing terms have an inactive site. |
| Finite bound optimization | Numerically minimize the relaxed support-only moment bound and compare with the entropy formula. Check the zero-word subtraction and the closed evaluation at $`\lambda=\sqrt{2}`$. | Three proper thresholds and the full-threshold factor before the finite-prime phase. |
| Classical-flag boundary | Construct the output cq blocks by applying the measurement eigenbras to a GHZ purification and to its dephased classical mixture. Compute the $`2\times2`$ Hermitian trace norms directly. | $`n=5,p=7`$, with both leakage bits and the reference retained. |

The exact Fourier group uses integer polynomials. Multiplication first takes place modulo $`z^p-1`$; reduction by $`1+z+\cdots+z^{p-1}=0`$ then evaluates the expressions at a primitive $`p`$-th root. Rational results use Python's Fraction type. This checks field constraints, Fourier phases, factors of $`p`$, and Walsh factors of $`2`$ without a floating-point Fourier transform.

The general-threshold examples exercise secret-dependent proper output parities. In the triangle example, the reference holds the purification of the edge state $`0.6|00\rangle\langle00|+0.4|11\rangle\langle11|`$. The other two edges each supply a pure Bell pair. The program computes the $`2\times2`$ reference blocks by tracing the devices out of this explicit joint state and obtains trace norms from the two singular values. The tested majorant retains the exact secret phase difference for each dual word.

## Recorded results

The computed record is in [expected_results.json](expected_results.json). Representative values are:

| Quantity | Result |
|---|---:|
| Matching optimum, $`n=4,p=5`$ | $`0.4755282581475768`$ |
| Matching optimum, $`n=6,p=7`$ | $`0.2437319780454559`$ |
| Odd witness, $`n=5,t=3,p=7`$ | $`0.6258980382192605`$ |
| Triangle distance with joint quantum reference | $`0.1742352118352403`$ |
| Triangle distance using the leaked bits alone | $`0.0138196601125011`$ |
| Relaxed finite log-base-two bound, $`n=1000,t=950`$ | $`-411.9437551870863`$ |
| Coherent-purification cq distance, $`n=5,p=7`$ | $`0.9749279121818236`$ |
| Genuinely classical flagged-mixture cq distance in that example | $`0`$ |

The finite log bound is a security upper bound. The [general-threshold proof](../science/general_threshold.md) derives the asymptotic exponent above one half using the weighted coding estimate.

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
