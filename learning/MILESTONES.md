# Thirty milestones for Shamir network leakage

This common map describes the understanding needed to follow the project's question, argument, results and limits. Its stable identifiers are **M01–M30**. The targets depend on the science, rather than on a particular reader's starting knowledge. They organize the main story; specialist calculations remain in the canonical proof pages.

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [Watrous bridge](WATROUS_BRIDGE.md) identifies the selected sections, translates notation and explains which connections the project supplies locally. References to Watrous below use that edition's section numbering. Finite-field sharing, coding theory, network Finner and the leakage argument are supplied by the project and its cited primary research; those research citations are not additional educational anchors.

## Allocation and dependency structure

| Phase | Milestones | Scientific role |
|---|---|---|
| Background/preliminaries | M01–M14: 14 milestones | Build the classical sharing and quantum information languages, then combine them into one precise leakage experiment. |
| Narrative/innovation | M15–M30: 16 milestones | Connect local coefficient estimates to the full-threshold optimum, general-threshold secrecy, resource boundaries and the complete contribution. |

Fourteen background milestones are warranted because neither side of this problem can replace the other. Finite-field interpolation and MDS codes explain how a secret enters correlated classical shares. Quantum states, measurements, extensions and norms explain what the leakage devices and adversary can do. M14 joins these prerequisites into the exact experiment whose security is proved.

The sixteen narrative milestones move from a single network contraction to the whole secrecy statement. M15–M20 establish two coefficient bounds with different reference assumptions. M21–M24 turn them into the full-threshold results and the matching construction. M25–M28 handle the additional parity terms below full threshold. M29 makes the resource boundary concrete, and M30 integrates the meaning, attribution, scope and evidence. This phase includes inherited ingredients needed for the result; its name does not claim that each ingredient is new.

Dependencies name earlier milestones supplying the essential ideas. Source pointers lead to the canonical statements and proofs, so this map need not duplicate their full derivations.

## Background/preliminaries — M01–M14

### M01 — Arithmetic over a prime field

- **Phase:** Background/preliminaries.
- **Central question:** Why are shares and secrets elements of a finite field rather than ordinary real numbers?
- **Understanding target:** Interpret addition, multiplication and nonzero inverses in $`\mathbb F_p`$. Explain why distinct nonzero evaluation points exist when the odd prime satisfies $`p>n`$, and why equations and randomness in this field have exact finite meanings.
- **Dependencies and story role:** Starting point for the classical side of the problem; establishes the objects on which sharing and Fourier analysis act.
- **Conceptual connection:** Invertible field arithmetic makes interpolation possible and later lets a nonzero secret difference select a Fourier phase.
- **Source pointers:** [Model §1](../science/model.md#1-shares-and-public-parameters); [full-threshold proof §4](../science/full_threshold.md#4-an-attack-attaining-the-graph-vertex-bound-for-even-size) for the later use of inverses. Finite-field background is supplied locally, not by a claimed Watrous section.

### M02 — Polynomial interpolation and reconstruction

- **Phase:** Background/preliminaries.
- **Central question:** How can distributed polynomial evaluations determine a secret?
- **Understanding target:** Explain the role of the secret as the constant coefficient and of the other coefficients as randomness. Relate degree at most $`t-1`$ to reconstruction from $`t`$ evaluations. At full threshold, recognize the nonzero Lagrange weights that turn the secret into a weighted sum of all shares.
- **Dependencies and story role:** Requires M01; converts field arithmetic into a reconstruction mechanism.
- **Conceptual connection:** The local rescaling $`X_i=\ell_iY_i`$ will turn full-threshold Shamir sharing into uniform additive sharing without changing the allowed leakage strategies.
- **Source pointers:** [Model §1](../science/model.md#1-shares-and-public-parameters); [Fourier structure §5](../science/fourier.md#5-full-threshold-and-additive-coordinates); Shamir's original construction in the [bibliography](../references/references.bib).

### M03 — Threshold privacy and correlated shares

- **Phase:** Background/preliminaries.
- **Central question:** How can individual collections of shares hide a secret that enough shares reconstruct exactly?
- **Understanding target:** Explain why fewer than $`t`$ shares have the same distribution for every secret, although the complete share vector depends on the secret. Distinguish this threshold-privacy statement from local leakage, in which all devices reveal a small output.
- **Dependencies and story role:** Requires M01–M02; joins randomness, reconstruction and privacy before introducing the attacker.
- **Conceptual connection:** Uniform sharing cosets support both the privacy argument and the later cancellation of secret-independent output parities.
- **Source pointers:** [Model, opening and §1](../science/model.md); [Fourier structure §1](../science/fourier.md#1-the-sharing-coset-and-its-dual-code); [full-threshold proof §2](../science/full_threshold.md#2-additive-coordinates-and-the-single-relevant-parity).

### M04 — Classical distinguishing distance

- **Phase:** Background/preliminaries.
- **Central question:** What does it mean for two leakage distributions to reveal almost no information about which secret was shared?
- **Understanding target:** Interpret total variation distance as $`\frac12\sum_b|P_s(b)-P_{s'}(b)|`$. Relate distance $`\Delta`$ to equal-prior guessing probability $`(1+\Delta)/2`$, and distinguish an upper bound on an attack's success from a construction attaining that bound.
- **Dependencies and story role:** Requires M03; gives the classical operational meaning of security before its quantum extension.
- **Conceptual connection:** This normalization will remain unchanged when probability differences become operators on an adversary's retained system.
- **Source pointers:** [Model §4](../science/model.md#4-security-convention); Watrous §3.1.1 for the quantum discrimination framework used in M09; [Watrous bridge](WATROUS_BRIDGE.md) for the normalization convention.

### M05 — Quantum states and classical registers

- **Phase:** Background/preliminaries.
- **Central question:** How can one mathematical description contain a classical share, a leaked bit and a quantum device?
- **Understanding target:** Identify a density operator as positive with trace one, and distinguish pure states, mixed states and an explicitly classical register. Recognize a classical–quantum state as a block-diagonal record whose quantum block can depend on a classical value.
- **Dependencies and story role:** Builds on the probability language of M04; begins the quantum background with single registers.
- **Conceptual connection:** Shares and outputs remain classical even though measurements and the adversary's reference are quantum. Classical block structure will later make trace norms add exactly.
- **Source pointers:** Watrous §§2.1.1–2.1.2; [model §3](../science/model.md#3-local-leakage-and-the-adversarys-final-state); [Watrous bridge](WATROUS_BRIDGE.md).

### M06 — Joint systems, correlations and partial trace

- **Phase:** Background/preliminaries.
- **Central question:** What changes when several quantum registers are considered jointly rather than separately?
- **Understanding target:** Read tensor products as joint-system structure, without assuming that every joint state factors. Explain reduced states and partial trace, and distinguish a product state from an entangled state using the Bell pair as the relevant example.
- **Dependencies and story role:** Requires M05; moves from individual quantum registers to correlated devices and an adversary.
- **Conceptual connection:** Devices can each hold many edge registers. Regrouping those registers by device changes their presentation, not the independence of the original sources.
- **Source pointers:** Watrous §§1.1.1–1.1.2 and §2.1.3; [model §2](../science/model.md#2-independent-bipartite-source-resources); [Bell-pair construction](../science/full_threshold.md#4-an-attack-attaining-the-graph-vertex-bound-for-even-size).

### M07 — Purifications and extensions

- **Phase:** Background/preliminaries.
- **Central question:** How much can a retained quantum reference know when the device marginal is fixed?
- **Understanding target:** Distinguish a marginal, an extension and a purification. Explain how different joint states can have the same device marginal, and why giving an adversary purifying registers can change the leakage experiment even when that marginal is unchanged.
- **Dependencies and story role:** Requires M05–M06; supplies the language needed to state the reference assumptions precisely.
- **Conceptual connection:** The proof may purify a source into one endpoint for analysis. Giving that purification to an additional adversary is a different resource allocation and must be justified separately.
- **Source pointers:** Watrous §2.1.3, especially Theorems 2.10 and 2.12, and §2.2.2, Proposition 2.29, for obtaining an extension by a channel on a purification; [model, three reference scopes](../science/model.md#three-reference-scopes); [network estimates §1](../science/network_bounds.md#1-notation-and-the-source-assumptions).

### M08 — Binary measurements as Hermitian contractions

- **Phase:** Background/preliminaries.
- **Central question:** What mathematical restriction follows from releasing exactly one classical bit?
- **Understanding target:** Describe a binary POVM by positive effects summing to the identity. Pass between its effects and $`M_i(y)=P_i(0\mid y)-P_i(1\mid y)`$, with $`-I\preceq M_i(y)\preceq I`$. Keep general binary POVMs distinct from the projective measurements used in the attaining example.
- **Dependencies and story role:** Requires M05–M06; translates the output restriction into a local operator constraint.
- **Conceptual connection:** Share-dependent observables encode arbitrary local measurements on all incident registers while preserving the useful bound $`M_i(y)^2\preceq I`$.
- **Source pointers:** Watrous §§2.3.1–2.3.2; [model §3](../science/model.md#3-local-leakage-and-the-adversarys-final-state); [Fourier structure §2](../science/fourier.md#2-local-observable-fourier-coefficients).

### M09 — Operator norms and quantum discrimination

- **Phase:** Background/preliminaries.
- **Central question:** Which operator quantities measure distinguishability, and which quantities make its proof manageable?
- **Understanding target:** Distinguish the trace, Hilbert–Schmidt and operator norms. Relate trace-norm duality and the Holevo–Helstrom theorem to optimal discrimination. Preserve the convention $`\Delta=\frac12\|\Omega_s-\Omega_{s'}\|_1`$: Watrous calls the full norm $`\|\rho-\sigma\|_1`$ trace distance.
- **Dependencies and story role:** Requires M04–M08; joins the classical security convention to quantum states and measurements.
- **Conceptual connection:** The theorem bounds trace norm, while its local coefficient estimates use weighted Hilbert–Schmidt norms or moments. Those quantities play different roles.
- **Source pointers:** Watrous §1.1.3, including Eq. (1.182), and §3.1.1, Theorem 3.4; [model §4](../science/model.md#4-security-convention); [Watrous bridge](WATROUS_BRIDGE.md).

### M10 — Local channels and discarded outcomes

- **Phase:** Background/preliminaries.
- **Central question:** Which processing can be included in a leakage device without changing the experiment being bounded?
- **Understanding target:** Explain why a local channel can be absorbed into a measurement through its adjoint, why an unrecorded local operation cannot signal to another system, and why the adversary's later processing cannot increase distinguishing distance. Keep these facts distinct from permission to communicate between devices.
- **Dependencies and story role:** Requires M06–M09; specifies operational freedom before the source restrictions are assembled.
- **Conceptual connection:** Summing an omitted device's outcomes inserts an identity operator. This is the step that later preserves secret-independent proper parities even with a quantum reference.
- **Source pointers:** Watrous §§2.2.1–2.2.2, §2.3.2 and §3.3.2, Corollary 3.40; [model §§2–3](../science/model.md); [full-threshold proof §2](../science/full_threshold.md#2-additive-coordinates-and-the-single-relevant-parity).

### M11 — Independent bipartite-source graphs

- **Phase:** Background/preliminaries.
- **Central question:** What resource does an edge in the source graph actually supply?
- **Understanding target:** Read the initial state as a tensor product over independent bipartite sources and local factors. Explain how each device may jointly process all its incident registers, how the graph may be complete, and why source independence does not imply independence of device states.
- **Dependencies and story role:** Requires M06–M10; connects local quantum objects into the global resource model.
- **Conceptual connection:** Every source index belongs to two endpoints. This structural property, rather than a degree bound or a large independent vertex set, drives the graph contraction. A source graph is also distinct from a stabilizer graph state.
- **Source pointers:** [Model §2](../science/model.md#2-independent-bipartite-source-resources); [network estimates §1](../science/network_bounds.md#1-notation-and-the-source-assumptions); [source-graph distinction](../science/boundaries.md#a-source-graph-is-not-a-stabilizer-graph-state). Watrous §§1.1.1 and 2.1.3 supply the tensor and marginal language.

### M12 — Finite Fourier analysis and opposite frequencies

- **Phase:** Background/preliminaries.
- **Central question:** How does expanding a share-dependent measurement into frequencies expose a usable constraint?
- **Understanding target:** Interpret finite-field characters, Fourier normalization, inversion and Parseval. For Hermitian $`M_i(y)`$, explain $`A_i(-k)=A_i(k)^\dagger`$ and why $`k\ne-k`$ for nonzero frequencies over an odd prime field. A Fourier operator need not itself be Hermitian.
- **Dependencies and story role:** Requires M01, M08 and M09; joins the classical field inputs to quantum operator coefficients.
- **Conceptual connection:** Opposite-frequency symmetry and the binary-measurement constraint will limit the total local second or fourth moment without a factor depending on field size.
- **Source pointers:** [Fourier structure §2](../science/fourier.md#2-local-observable-fourier-coefficients); [network estimates §§1 and 5](../science/network_bounds.md). Watrous §1.1.3 supplies matrix inner products and norms; the finite-field Fourier derivation is supplied locally.

### M13 — Sharing cosets, dual codes and the MDS property

- **Phase:** Background/preliminaries.
- **Central question:** Which input frequencies survive averaging over the sharing randomness?
- **Understanding target:** Recognize the affine sharing coset $`s\mathbf1+C_0`$ and its dual code $`C=C_0^\perp`$. Explain its dimension $`r=n-t+1`$, minimum nonzero weight $`t`$, and bijective projection onto any $`r`$ coordinates. Identify secret-independent surviving words as a possible additional cancellation.
- **Dependencies and story role:** Requires M01–M03 and M12; consolidates the classical algebra into the structure used by the security proof.
- **Conceptual connection:** Character orthogonality removes frequencies outside the dual code; minimum distance forces every retained nonzero word to involve many devices.
- **Source pointers:** [Fourier structure §1](../science/fourier.md#1-the-sharing-coset-and-its-dual-code); [MDS provenance](../references/RELATED_WORK.md#the-mds-inequality-and-minimum-distance-weighting). This coding-theory connection is supplied locally, outside the Watrous anchor's role.

### M14 — The complete leakage experiment

- **Phase:** Background/preliminaries.
- **Central question:** What precise experiment is claimed to hide the chosen secret?
- **Understanding target:** Connect the classical sharing, secret-independent source state, share-dependent binary measurements, leaked register $`B`$ and retained reference $`E`$ into $`\Omega_s^{BE}`$. State the three reference scopes, the absence of communication or feedback during leakage, and the pairwise chosen-secret distance. Strategies may know the challenge pair but not which member was shared.
- **Dependencies and story role:** Integrates M01–M13 and completes the background phase with the problem stated as a whole.
- **Conceptual connection:** The resource snapshot, one-bit output and single-episode restriction are premises used by the proof, rather than conclusions inferred from a small distance.
- **Source pointers:** [Complete model](../science/model.md); [scientific route](../science/README.md). Watrous §§2.1–2.3 and §3.1.1 provide the state, channel, measurement and discrimination framework.

## Narrative/innovation — M15–M30

### M15 — Schmidt expansion and graph contraction

- **Phase:** Narrative/innovation.
- **Central question:** Why can a dense independent-source network still admit a product bound on a single Fourier coefficient?
- **Understanding target:** Follow how Schmidt expansion places every edge index at exactly two vertices and how repeated Cauchy–Schwarz bounds the complex tensor contraction by local weighted Hilbert–Schmidt norms. Explain why the operators need not be positive and why mixed-source purification into an endpoint is legitimate.
- **Dependencies and story role:** Requires M06–M07, M09, M11 and M14; begins the narrative with its local network mechanism.
- **Conceptual connection:** Unbounded degree changes the local matrices but does not alter the two-endpoint contraction rule or introduce a dimension factor.
- **Source pointers:** [Network estimates, Lemma 2.1 and Eq. (2.4)](../science/network_bounds.md#2-complex-contraction-on-a-graph); Watrous §1.1.3 for Schmidt decomposition and norms; [attribution](../references/RELATED_WORK.md#network-finner-and-the-complex-contraction).

### M16 — Quantum Finner for positive effects

- **Phase:** Narrative/innovation.
- **Central question:** What does the graph contraction imply for the probability of simultaneous local accepting events?
- **Understanding target:** Explain the bound of a joint event probability by the product of square roots of local event probabilities. Identify where positivity, $`0\preceq B_i\preceq I`$, and $`B_i^2\preceq B_i`$ enter, and why mixed-source endpoint dilation preserves the probabilities used in this statement.
- **Dependencies and story role:** Requires M08, M11 and M15; turns the complex contraction into the event form needed for arbitrary references.
- **Conceptual connection:** A positive measurement effect and a general Fourier observable are different objects. Later the valid effect is $`A_i(k)^\dagger A_i(k)`$.
- **Source pointers:** [Network estimates, Corollary 2.2](../science/network_bounds.md#corollary-22-positive-effect-quantum-finner-inequality); Watrous §§2.3.1–2.3.2 for effects; Renou et al. in [related work](../references/RELATED_WORK.md#network-finner-and-the-complex-contraction).

### M17 — A reference that is another graph vertex

- **Phase:** Narrative/innovation.
- **Central question:** When can the adversary's entire retained system be included directly in the graph contraction?
- **Understanding target:** Use trace-norm duality to insert a unitary at vertex $`E`$, whose weighted norm contributes at most one. Explain why arbitrary joint processing of that vertex is allowed, while assigning the purification of a device-device source to a third endpoint is outside this reference scope.
- **Dependencies and story role:** Requires M07, M09, M11, M14 and M15; establishes the structured-reference branch of the argument.
- **Conceptual connection:** Bounding an operator on $`E`$ reduces to bounding scalar expectations, while retaining the original bipartite-source structure.
- **Source pointers:** [Network estimates, Proposition 3.1 and Eqs. (3.1)–(3.4)](../science/network_bounds.md#3-second-moments-and-graph-vertex-references); Watrous §1.1.3, Eqs. (1.182)–(1.183); [model reference scopes](../science/model.md#three-reference-scopes).

### M18 — Symmetric second-moment budgets

- **Phase:** Narrative/innovation.
- **Central question:** How does one leaked bit bound all local Fourier coefficients at once?
- **Understanding target:** Connect matrix Parseval, the weighted norm and $`M_i(y)^2\preceq I`$ to $`\sum_k a_i(k)^2\le1`$. Explain the symmetry $`a_i(-k)=a_i(k)`$ and the product bound on network coefficients, with the local marginal defined in the chosen pure-source dilation.
- **Dependencies and story role:** Requires M08–M09, M12 and M15–M17; completes the coefficient budget for no reference or a graph-vertex reference.
- **Conceptual connection:** A fixed local budget prevents many opposite-frequency pairs from all having large weight, regardless of the field size or device dimension.
- **Source pointers:** [Network estimates, Proposition 3.1 and Eq. (3.5)](../science/network_bounds.md#3-second-moments-and-graph-vertex-references); [operator Fourier identity](../science/fourier.md#2-local-observable-fourier-coefficients); Watrous §1.1.3 for the Hilbert–Schmidt norm.

### M19 — Removing an arbitrary reference by Cauchy–Schwarz

- **Phase:** Narrative/innovation.
- **Central question:** What remains controllable when the adversary's extension has no graph factorization?
- **Understanding target:** Follow trace-norm duality and state Cauchy–Schwarz to bound a reference-valued coefficient by $`(\mathrm{Tr}\,\Omega_D K^\dagger K)^{1/2}`$. Explain why the extension disappears from this expression but the literal independent-source device marginal remains necessary.
- **Dependencies and story role:** Requires M07, M09, M14 and M15; opens the broader-reference branch without treating $`E`$ as a graph vertex.
- **Conceptual connection:** Security is bounded for the complete final state, without conditioning on an adversary measurement and discarding the probability of its outcome.
- **Source pointers:** [Network estimates, Eqs. (4.3)–(4.4)](../science/network_bounds.md#4-fourth-moments-with-an-arbitrary-external-reference); Watrous §1.1.3 for duality, §2.1.3 for purifications and §2.2.2, Proposition 2.29, for arbitrary extensions.

### M20 — Symmetric fourth-moment budgets

- **Phase:** Narrative/innovation.
- **Central question:** Why does the arbitrary-reference argument produce a fourth moment rather than a second moment?
- **Understanding target:** Combine M19's square root with event Finner's square root, then symmetrize the bounds for $`k`$ and $`-k`$. Explain $`c_i(k)=[b_i(k)b_i(-k)]^{1/8}`$ and $`\sum_k c_i(k)^4\le1`$, without assuming $`b_i(k)=b_i(-k)`$.
- **Dependencies and story role:** Requires M12, M16 and M19; completes the coefficient estimate for arbitrary extensions.
- **Conceptual connection:** The two square roots explain the change in the eventual exponent. This is a difference between proved estimates, not a proof that the optimal leakage rates separate by the same amount.
- **Source pointers:** [Network estimates, Proposition 4.1 and Eqs. (4.5)–(4.9)](../science/network_bounds.md#4-fourth-moments-with-an-arbitrary-external-reference); Watrous §§1.1.3 and 2.3.1 for the underlying norm and effect notions.

### M21 — Output parities and the final state

- **Phase:** Narrative/innovation.
- **Central question:** How do coefficient estimates become a bound on everything the adversary receives?
- **Understanding target:** Expand the binary output register into parity characters $`\chi_S(b)`$ with operator-valued coefficients $`F_{S,E}(s)`$. Explain the exact cq identity, additivity of trace norm across classical blocks, and the resulting sum of parity norms. Keep this binary expansion separate from the finite-field input expansion.
- **Dependencies and story role:** Requires M04–M05, M08–M09, M12 and M14; connects local coefficient control to the global distinguishing task.
- **Conceptual connection:** The factors $`2^{-n}`$ and the number of classical output blocks cancel. A scalar Parseval improvement is available only when the reference is absent.
- **Source pointers:** [Fourier structure §§3–4](../science/fourier.md#3-output-parities-with-a-quantum-reference); Watrous §§2.1–2.3 for the cq and measurement framework.

### M22 — Full threshold leaves one relevant parity

- **Phase:** Narrative/innovation.
- **Central question:** Why does the full-threshold problem reduce exactly to the parity of all leaked bits?
- **Understanding target:** Combine additive coordinates with the privacy of every proper share subset. Explain why proper output-parity operators are secret independent even with $`E`$, and obtain $`\Delta=\frac12\|F_{[n],E}(s)-F_{[n],E}(s')\|_1`$. Identify the surviving common-frequency words $`(k,\ldots,k)`$.
- **Dependencies and story role:** Requires M02–M03, M10, M12 and M21; integrates the sharing and output structure before applying either network budget.
- **Conceptual connection:** The single-parity equality is stronger than a general triangle bound and enables the exact even-device result.
- **Source pointers:** [Fourier structure §5](../science/fourier.md#5-full-threshold-and-additive-coordinates); [full-threshold proof §§2–3](../science/full_threshold.md#2-additive-coordinates-and-the-single-relevant-parity). Watrous §2.3.2 supports the partial-measurement interpretation.

### M23 — Paired Hölder and the finite-prime factor

- **Phase:** Narrative/innovation.
- **Central question:** How do the two local moment budgets yield exponential full-threshold secrecy without a field-size loss?
- **Understanding target:** Explain why symmetric moment order $`d`$ gives $`\sum_{k\ne0}\prod_i f_i(k)\le2^{1-n/d}`$ for $`n\ge d`$. Combine this with the largest odd-prime phase difference to obtain the factor $`\cos(\pi/(2p))`$. Track $`d=2,n\ge2`$ and $`d=4,n\ge4`$ separately.
- **Dependencies and story role:** Requires M12, M18, M20 and M22; completes both full-threshold upper bounds.
- **Conceptual connection:** Opposite-frequency pairs replace a naive sum over $`p-1`$ frequencies, while the reference model determines the available moment order.
- **Source pointers:** [Network estimates, Lemma 5.1](../science/network_bounds.md#5-pairing-the-nonzero-frequencies); [full-threshold proof §3](../science/full_threshold.md#3-fourier-proof-and-the-finite-prime-factor); Watrous §1.1.3 for norm and Hölder background.

### M24 — A Bell matching attains the even-device optimum

- **Phase:** Narrative/innovation.
- **Central question:** Can an admissible strategy attain the full-threshold upper bound?
- **Understanding target:** Follow independent Bell pairs and share-dependent equatorial measurements to a product of cosine correlations. Explain why additive averaging retains only the all-plus and all-minus Fourier terms, and how a frequency and total phase chosen for the challenge pair attain $`2^{1-n/2}\cos(\pi/(2p))`$.
- **Dependencies and story role:** Requires M06, M08, M11 and M22–M23; joins the converse with a matching construction.
- **Conceptual connection:** Equality holds for even $`n`$ over the permitted graph class, and on any prescribed graph containing a perfect matching. It does not establish sharpness for arbitrary extensions or every fixed graph.
- **Source pointers:** [Full-threshold proof §4](../science/full_threshold.md#4-an-attack-attaining-the-graph-vertex-bound-for-even-size); [finite Bell-pair checks](../verification/README.md); Watrous §§1.1.3, 2.1.3 and 2.3 for bipartite states and measurements.

### M25 — General thresholds and zero-frequency choices

- **Phase:** Narrative/innovation.
- **Central question:** What must be counted when proper output parities can also depend on the secret?
- **Understanding target:** Organize the parity sum by nonzero dual-code words. A nonzero coordinate forces its device into the parity; a zero coordinate may be included or excluded. Explain the arbitrary-reference factor $`1+c_i(0)`$ and why merely reusing the single full parity would omit real terms.
- **Dependencies and story role:** Requires M13, M20–M22; starts the extension from full reconstruction threshold to $`t<n`$.
- **Conceptual connection:** The sharing code supplies the compulsory sites, while the binary output expansion supplies the optional sites. Their interaction determines the local factors to which MDS Hölder will apply.
- **Source pointers:** [Fourier structure §3](../science/fourier.md#3-output-parities-with-a-quantum-reference); [general-threshold proof §1, Step 1](../science/general_threshold.md#step-1-sum-the-reference-valued-parity-coefficients).

### M26 — Weighted MDS Hölder and minimum distance

- **Phase:** Narrative/innovation.
- **Central question:** How can a sum over many dual-code words be bounded without paying for their field-dependent count?
- **Understanding target:** Explain how bijective $`r`$-coordinate projections yield the MDS inequality with $`q=n/r`$. Use a weight $`\lambda\ge1`$ on nonzero coordinates and minimum weight $`t`$ to extract $`\lambda^{-t}`$. Recognize adding the zero word as an upper-bound relaxation.
- **Dependencies and story role:** Requires M13, M18, M20 and M25; combines coding structure with local moment budgets.
- **Conceptual connection:** The normalization factors cancel because the code has $`p^r`$ words. Both the MDS inequality and minimum-distance weighting are imported ingredients, not new analytic claims.
- **Source pointers:** [General-threshold proof §1, Steps 2–3](../science/general_threshold.md#step-2-the-imported-mds-hölder-inequality); [MDS attribution](../references/RELATED_WORK.md#the-mds-inequality-and-minimum-distance-weighting). Watrous §1.1.3 supplies related norm inequalities, not this code theorem.

### M27 — The finite arbitrary-reference bound and its rate

- **Phase:** Narrative/innovation.
- **Central question:** When does the general bound remain exponentially small despite arbitrary quantum side information?
- **Understanding target:** Combine fourth moments and weighted MDS Hölder under the finite condition $`q=n/(n-t+1)\ge4`$. Interpret optimizing $`\lambda`$ and the entropy expression for the exponent. Explain the sufficient asymptotic rate $`0.9042045925\ldots`$ with a fixed positive margin, rather than treating that decimal as an optimal threshold.
- **Dependencies and story role:** Requires M20, M21 and M25–M26; completes the arbitrary-reference general-threshold theorem.
- **Conceptual connection:** The asymptotic rate is extracted from a finite, graph- and dimension-uniform bound. The full-threshold theorem separately retains the sharper finite-prime cosine factor.
- **Source pointers:** [General-threshold proof §§1–2](../science/general_threshold.md#1-arbitrary-quantum-side-information); [optimization checks](../verification/README.md); [model reference scopes](../science/model.md#three-reference-scopes).

### M28 — The stronger scalar bound without a reference

- **Phase:** Narrative/innovation.
- **Central question:** Which additional improvement becomes available when the leaked state is an ordinary probability distribution?
- **Understanding target:** Explain scalar output Parseval, Minkowski and the factor $`\sqrt{1+a_i(0)^2}`$. Connect the shared second-moment budget to a convex local expression whose maximum is at an endpoint. Interpret the finite $`q\ge2`$ optimizer and sufficient rate $`0.7569352556\ldots`$ without extending the scalar step to operator-valued trace norm.
- **Dependencies and story role:** Requires M18, M21 and M25–M27; completes the second general-threshold result and explains why its proof is stronger in a narrower scope.
- **Conceptual connection:** Retaining a square-sum over parities saves information lost by a triangle inequality. The two sufficient rates do not prove a separation between optimal security thresholds.
- **Source pointers:** [Fourier structure §4](../science/fourier.md#4-the-stronger-scalar-output-estimate); [general-threshold proof §3](../science/general_threshold.md#3-a-stronger-bound-without-a-quantum-reference); [optimization checks](../verification/README.md).

### M29 — Classical flags, coherent purifications and preparation

- **Phase:** Narrative/innovation.
- **Central question:** Why can an allowed classical shared choice and a coherent purification of the same device mixture have different security consequences?
- **Understanding target:** Explain averaging of a uniform branchwise bound with the classical flag retained. Contrast this with the explicit GHZ purification whose leaked parity and retained qubit reveal a secret-dependent phase. Distinguish local processing from communicating preparation, source graphs from stabilizer graph states, and a single leakage episode from resource reuse.
- **Dependencies and story role:** Requires M05–M07, M10–M11, M14 and M23–M28; examines the global theorem's premises through concrete resource changes.
- **Conceptual connection:** Equality of device marginals alone does not license replacing a branchwise classical model by arbitrary extensions of an unlabelled convex mixture.
- **Source pointers:** [Resource boundaries](../science/boundaries.md); [network estimates §6](../science/network_bounds.md#6-conditioning-on-actual-classical-randomness); Watrous §§2.1.3 and 6.1.2 for purifications and LOCC. The network-specific boundary example is supplied locally.

### M30 — The complete result, its significance and its evidence

- **Phase:** Narrative/innovation.
- **Central question:** What has the argument established about one-bit Shamir leakage, and what evidence supports each part?
- **Understanding target:** Explain how independent bipartite sources constrain even a dense network, how share-code structure forces many small Fourier factors, and how the output expansion turns those factors into secrecy. Distinguish the exact even-device full-threshold optimum from sufficient general-threshold rates, inherited tools from the cryptographic conclusion, and universal analytic proofs from finite numerical checks.
- **Dependencies and story role:** Integrates both phases, especially M14, M23–M24 and M27–M29; completes the map with the contribution as a whole.
- **Conceptual connection:** The result concerns unchanged classical Shamir sharing, one classical bit per device and the declared reference/resource models. It supplies no automatic theorem for leaked qubits, adaptive feedback or repeated resource use.
- **Source pointers:** [Scientific overview](../README.md); [proof dependency route](../science/README.md); [related work](../references/RELATED_WORK.md); [resource boundaries](../science/boundaries.md); [verification and its limits](../verification/README.md); [Watrous bridge](WATROUS_BRIDGE.md).

