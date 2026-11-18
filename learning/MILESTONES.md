# Thirty milestones for Shamir network leakage

This common map describes the understanding needed to follow the project's question, argument, results and limits. Its stable identifiers are **M01–M30**. The targets depend on the science, rather than on a particular reader's starting knowledge. They organize the main story; specialist calculations remain in the canonical proof pages.

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [Watrous bridge](WATROUS_BRIDGE.md) identifies the selected sections, translates notation and explains which connections the project supplies locally. References to Watrous below use that edition's section numbering. Finite-field sharing, coding theory, network Finner and the leakage argument are supplied by the project and its cited primary research; those research citations are not additional educational anchors.

## Allocation and dependency structure

| Phase | Milestones | Scientific role |
|---|---|---|
| Background/preliminaries | M01–M14: 14 milestones | Build the classical sharing and quantum information languages, then combine them into one precise leakage experiment. |
| Narrative/innovation | M15–M30: 16 milestones | Connect local coefficient estimates to the full-threshold optimum, general-threshold secrecy, resource boundaries and the complete contribution. |

Fourteen background milestones are warranted because neither side of this problem can replace the other. Finite-field interpolation and MDS codes explain how a secret enters correlated classical shares. Quantum states, measurements, extensions and norms explain what the leakage devices and adversary can do. M14 joins these prerequisites into the exact experiment whose security is proved.

The sixteen narrative milestones move from a network contraction to the secrecy theorem. M15–M21 connect graph bounds, polar decomposition and the sum over leaked outcomes. M22–M24 derive and attain the full-threshold optimum for even size. M25–M28 give an explicit finite bound and then match the leading exponent above one half. M29 tests the resource assumptions, and M30 brings the argument and its limitations together.

Dependencies name earlier milestones supplying the essential ideas. Source pointers lead to the canonical statements and proofs, so this map need not duplicate their full derivations.

## Background/preliminaries — M01–M14

### M01 — Arithmetic over a prime field

- **Phase:** Background/preliminaries.
- **Central question:** Why are shares and secrets elements of a finite field rather than ordinary real numbers?
- **Understanding target:** Interpret addition, multiplication and nonzero inverses in $`\mathbb F_p`$. Explain why distinct nonzero evaluation points exist when the odd prime satisfies $`p>n`$, and why equations and randomness in this field have exact finite meanings.
- **Dependencies and story role:** Starting point for the classical side of the problem; establishes the objects on which sharing and Fourier analysis act.
- **Conceptual connection:** Invertible field arithmetic makes interpolation possible and later lets a nonzero secret difference select a Fourier phase.
- **Source pointers:** [Model §1](../science/model.md#1-shares-and-public-parameters); [full-threshold proof §4](../science/full_threshold.md#4-bell-pair-attainment) for the later use of inverses. Finite-field background is supplied locally, not by a claimed Watrous section.

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
- **Source pointers:** Watrous §§1.1.1–1.1.2 and §2.1.3; [model §2](../science/model.md#2-independent-bipartite-source-resources); [Bell-pair construction](../science/full_threshold.md#4-bell-pair-attainment).

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
- **Conceptual connection:** Opposite-frequency symmetry and the binary-measurement constraint give the local second-moment budget and the cap on each nonzero weight, independently of field size.
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
- **Central question:** Why can a dense independent-source network still admit a product bound on an operator expectation?
- **Understanding target:** Follow how Schmidt expansion places every edge index at exactly two vertices and how Cauchy–Schwarz bounds the complex tensor contraction by local weighted Hilbert–Schmidt norms. Explain how a mixed source can be purified into a device endpoint for this calculation.
- **Dependencies and story role:** Requires M06–M07, M09, M11 and M14. Establishes the contraction used to read the graph structure.
- **Conceptual connection:** Unbounded degree changes the local matrices while every source still has two endpoints.
- **Source pointers:** [Network estimates §2](../science/network_bounds.md#2-complex-contraction-on-a-graph), especially Lemma 2.1 and Eq. (2.4). Watrous §1.1.3 supplies Schmidt decomposition and norms.

### M16 — Quantum Finner for positive products

- **Phase:** Narrative/innovation.
- **Central question:** How does the source graph bound the expectation of a product of positive local operators?
- **Understanding target:** Interpret the bound by the product of local second-moment square roots. Relate it to the event bound for effects by using $`B_i^2\preceq B_i`$ when $`0\preceq B_i\preceq I`$. Explain why the proof for general positive operators will retain the second moments.
- **Dependencies and story role:** Requires M08, M11 and M15. Supplies the positive-operator form needed on the device marginal.
- **Conceptual connection:** The absolute value of a Fourier operator is positive and can enter this bound even when the Fourier operator is complex.
- **Source pointers:** [Network estimates §§2 and 4](../science/network_bounds.md). Watrous §§1.1.3 and 2.3.1 give the operator and measurement ingredients. [Research attribution](../references/RELATED_WORK.md#network-finner-and-the-complex-contraction) identifies quantum Finner.

### M17 — The adversary as a source-graph vertex

- **Phase:** Narrative/innovation.
- **Central question:** When can the retained adversary register enter the graph contraction directly?
- **Understanding target:** Use trace-norm duality to insert a unitary at vertex $`E`$, whose weighted norm contributes at most one. Explain what changes in the resource representation when an adversary holds purification registers for sources between devices.
- **Dependencies and story role:** Requires M07, M09, M11, M14 and M15. Shows how reference geometry enters a direct graph proof.
- **Conceptual connection:** A witness acts on all of $`E`$ jointly. Whether that witness can be assigned to a source-graph vertex depends on which systems each independent source supplies.
- **Source pointers:** [Network estimates §3](../science/network_bounds.md#3-second-moments-and-graph-vertex-references) and [model reference scopes](../science/model.md#three-reference-scopes). Watrous §1.1.3, Eqs. (1.182)–(1.183), supplies the norm identity.

### M18 — A second-moment budget for each device

- **Phase:** Narrative/innovation.
- **Central question:** How does one leaked bit constrain all Fourier coefficients of a device at once?
- **Understanding target:** Apply operator Parseval and $`M_i(y)^2\preceq I`$ to $`b_i(k)=\mathrm{Tr}(\rho_i A_i(k)^\dagger A_i(k))`$. Explain why pairing opposite frequencies in $`h_i(k)=[b_i(k)b_i(-k)]^{1/4}`$ gives $`\sum_k h_i(k)^2\le1`$ and $`h_i(k)\le1/\sqrt 2`$ when $`k\ne0`$.
- **Dependencies and story role:** Requires M08–M09, M12 and M16. Gives the local budget that both reconstruction regimes use.
- **Conceptual connection:** Two equal contributions occupy the budget for each opposite-frequency pair. The symmetry of the pair is enough even when the two unsymmetrized moments differ.
- **Source pointers:** [Fourier structure §2](../science/fourier.md#2-local-observable-fourier-coefficients) and [network estimates §4](../science/network_bounds.md#4-second-moments-with-an-arbitrary-external-reference). Watrous §1.1.3 supplies the matrix norm background.

### M19 — Polar decomposition for an arbitrary reference

- **Phase:** Narrative/innovation.
- **Central question:** How can a trace-norm witness on an arbitrary extension be controlled by the device marginal alone?
- **Understanding target:** Factor the device operator as $`K=|K^\dagger|^{1/2}U|K|^{1/2}`$. Use trace-norm duality and Cauchy–Schwarz on the joint state to obtain the geometric mean of device expectations of $`|K^\dagger|`$ and $`|K|`$. Explain how the bound includes every unitary witness on the reference.
- **Dependencies and story role:** Requires M07, M09, M14 and M16–M18. Extends the second-moment method to arbitrary extensions of the prescribed marginal.
- **Conceptual connection:** Polar decomposition moves all reference dependence into the unitary witness. Both scalar factors retain positive products on the devices.
- **Source pointers:** [Network estimates §4](../science/network_bounds.md#4-second-moments-with-an-arbitrary-external-reference). Watrous §1.1.3 locates polar decomposition and trace-norm duality.

### M20 — Fourier coefficients of the binary effects

- **Phase:** Narrative/innovation.
- **Central question:** How does a fixed codeword appear in each classical outcome block?
- **Understanding target:** For a leaked bit $`u_i`$, read the nonzero-frequency coefficient of $`P_i(u_i\mid y)`$ as $`(-1)^{u_i}A_i(k_i)/2`$. At zero frequency read it as the averaged effect $`B_i(u_i)`$, a positive operator, with the two effects summing to identity.
- **Dependencies and story role:** Requires M05, M08, M12–M14 and M19. Prepares the outcome sum before applying the graph bound.
- **Conceptual connection:** The dual word determines which sites carry signs and which carry positive effects.
- **Source pointers:** [Fourier structure](../science/fourier.md) and [network estimates §4](../science/network_bounds.md#4-second-moments-with-an-arbitrary-external-reference). Watrous §§2.3.1–2.3.2 supplies the local effect model.

### M21 — Summing outcomes outside the codeword support

- **Phase:** Narrative/innovation.
- **Central question:** Why does a zero-frequency site contribute no penalty to the bound on a codeword?
- **Understanding target:** Use trace-norm additivity across classical blocks. Sum the nonzero-frequency outcome signs in absolute value, cancelling the factors of one half. Sum the remaining positive-effect terms by scalar Cauchy–Schwarz before applying Finner. Identify the resulting product of $`h_i(k_i)`$ over the support.
- **Dependencies and story role:** Requires M05, M09, M13 and M18–M20. Connects the device estimate to the full adversarial state and the weighted dual-code sum.
- **Conceptual connection:** Completeness acts inside each scalar sum after Cauchy–Schwarz. This keeps the conditional reference and outcome probabilities in the calculation.
- **Source pointers:** [Network estimates §4](../science/network_bounds.md#4-second-moments-with-an-arbitrary-external-reference) and [Watrous bridge §5](WATROUS_BRIDGE.md#5-the-norms-serve-different-purposes).

### M22 — Full threshold leaves one relevant parity

- **Phase:** Narrative/innovation.
- **Central question:** Why does the full-threshold problem reduce exactly to the parity of all leaked bits?
- **Understanding target:** Combine additive coordinates with the privacy of every proper share subset. Explain why proper output-parity operators are secret independent even with $`E`$, and obtain $`\Delta=\frac12\|F_{[n],E}(s)-F_{[n],E}(s')\|_1`$. Identify the surviving common-frequency words $`(k,\ldots,k)`$.
- **Dependencies and story role:** Requires M02–M03, M10, M12 and M20–M21. Gives the exact reduction used at $`t=n`$.
- **Conceptual connection:** The single parity gives an equality and exposes the finite-prime factor in the next step.
- **Source pointers:** [Fourier structure §5](../science/fourier.md#5-full-threshold-and-additive-coordinates) and [full-threshold proof §2](../science/full_threshold.md#2-additive-coordinates-and-the-single-relevant-parity). Watrous §2.3.2 supplies the partial-measurement interpretation.

### M23 — Paired Hölder and the finite-prime factor

- **Phase:** Narrative/innovation.
- **Central question:** How do the local second-moment budgets give a sharp full-threshold upper bound?
- **Understanding target:** Use opposite-frequency symmetry and Hölder to bound the common-frequency sum by $`2^{1-n/2}`$. Explain why the largest odd-prime phase difference has magnitude $`2\cos(\pi/(2p))`$ and where the trace-distance normalization cancels the factor of two.
- **Dependencies and story role:** Requires M12, M18–M19 and M22. Completes the full-threshold upper bound for arbitrary extensions.
- **Conceptual connection:** Frequency pairing and the phase factor have different origins. One counts the moment budget and the other reflects the spacing of field characters.
- **Source pointers:** [Network estimates §5](../science/network_bounds.md#5-pairing-the-nonzero-frequencies) and [full-threshold proof §3](../science/full_threshold.md#3-fourier-proof-and-the-finite-prime-factor).

### M24 — A Bell matching attains the even-device optimum

- **Phase:** Narrative/innovation.
- **Central question:** Can an admissible strategy attain the full-threshold upper bound?
- **Understanding target:** Follow independent Bell pairs and share-dependent equatorial measurements to a product of cosine correlations. Explain why additive averaging retains only the two terms with a common sign. Choose a frequency and phase for the challenge pair and obtain $`2^{1-n/2}\cos(\pi/(2p))`$.
- **Dependencies and story role:** Requires M06, M08, M11 and M22–M23. Matches the converse at even size.
- **Conceptual connection:** The same construction attains the optimum across the allowed arbitrary-extension class and on a prescribed graph containing a perfect matching. The upper bound also applies at odd size.
- **Source pointers:** [Full-threshold proof §4](../science/full_threshold.md#4-bell-pair-attainment), [two-share example](WATROUS_BRIDGE.md#7-worked-binary-example-two-shares-and-one-bell-pair) and [verification](../verification/README.md).

### M25 — Weighted MDS Hölder and minimum distance

- **Phase:** Narrative/innovation.
- **Central question:** How can a sum over many dual words be controlled independently of field size?
- **Understanding target:** Use bijective $`r`$-coordinate projections to understand MDS Hölder with $`r=n-t+1`$ and $`q=n/r`$. Give every nonzero coordinate a weight $`\lambda\ge1`$ so minimum distance extracts $`\lambda^{-t}`$. Explain why the all-zero word contributes one to the weighted sum and is subtracted.
- **Dependencies and story role:** Requires M13, M18 and M21. Turns the support sum into a computable finite expression.
- **Conceptual connection:** MDS controls how the code combines coordinates, and binary quantum measurement controls the mass and size of each local nonzero weight.
- **Source pointers:** [General-threshold proof §1](../science/general_threshold.md#1-explicit-finite-bound) and [MDS attribution](../references/RELATED_WORK.md#the-mds-inequality-and-minimum-distance-weighting).

### M26 — Reading the finite bound

- **Phase:** Narrative/innovation.
- **Central question:** What explicit bound is available before taking a limit in the number of shares?
- **Understanding target:** Under $`q\ge2`$, use the second-moment budget and $`h_i(k)\le1/\sqrt 2`$ to bound the local $`q`$-mass. Interpret the optimization over $`\lambda`$ and the resulting entropy estimate. Explain the difference between computing this finite bound and determining the leading exponent.
- **Dependencies and story role:** Requires M18, M21 and M25. Gives a finite estimate for arbitrary references and sets up the sharper asymptotic question.
- **Conceptual connection:** The finite Hölder estimate and the asymptotic code-sum estimate start from the same support bound.
- **Source pointers:** [General-threshold proof §1](../science/general_threshold.md#1-explicit-finite-bound) and [finite verification](../verification/README.md).

### M27 — The code sum above one half

- **Phase:** Narrative/innovation.
- **Central question:** How does the weighted code estimate improve the asymptotic reconstruction range?
- **Understanding target:** Use the support product and the weighted dual-code estimate for generalized Reed–Solomon sharing. Identify the cap $`1/\sqrt 2`$ on every nonzero weight and the bounded local second moment. Distinguish words with few small coordinates, which agree with bounded lists, from words with many small coordinates, whose total weight is controlled on two disjoint information sets. Interpret the polynomial loss and the fixed positive margin in $`t/n\ge1/2+\eta`$.
- **Dependencies and story role:** Requires M13, M18, M21 and M25–M26. Establishes the uniform upper bound with leading exponent $`t/2`$.
- **Conceptual connection:** The code estimate depends on the local weights, and those weights already allow arbitrary reference dimension and complete source graphs.
- **Source pointers:** [General-threshold proof §2](../science/general_threshold.md#2-sharp-exponent-above-one-half) and [coding-theory attribution](../references/RELATED_WORK.md).

### M28 — Matching the exponent on a reconstruction set

- **Phase:** Narrative/innovation.
- **Central question:** Why does the upper bound capture the leading worst-case exponent below full threshold?
- **Understanding target:** Select any $`t`$ shares that reconstruct and reduce their marginal to a full-threshold additive sharing. Pair those devices when $`t`$ is even. At odd $`t`$, explain how a sign-of-cosine bit on the leftover device provides a nonzero coefficient of constant size. Use constant outputs outside the chosen set.
- **Dependencies and story role:** Requires M02–M03, M22–M24 and M27. Matches the leading exponent over admissible graphs for either parity of $`t`$.
- **Conceptual connection:** The marginal has exactly the constraints that the full-threshold calculation needs. The odd leftover device affects a constant, and the polynomial upper factor contributes $`O(\log n)`$ to the exponent.
- **Source pointers:** [General-threshold proof §2](../science/general_threshold.md#2-sharp-exponent-above-one-half) and [Bell-pair calculation](../science/full_threshold.md#4-bell-pair-attainment).

### M29 — Classical flags, coherent purifications and preparation

- **Phase:** Narrative/innovation.
- **Central question:** Why can an allowed classical shared choice and a coherent purification of the same device mixture have different security consequences?
- **Understanding target:** Explain averaging of a uniform branchwise bound when the classical flag is retained. Follow the GHZ purification example, in which leaked parity and a retained qubit reveal a secret-dependent phase. Identify where the independent-source premise can fail if devices communicate during preparation.
- **Dependencies and story role:** Requires M05–M07, M10–M11, M14 and M23–M28. Tests the theorem's premises through concrete resource changes.
- **Conceptual connection:** The graph bound applies to each labelled branch. With a coherently purified unlabelled mixture, the averaged device marginal can lose the required product form.
- **Source pointers:** [Resource boundaries](../science/boundaries.md) and [network estimates §6](../science/network_bounds.md#6-conditioning-on-actual-classical-randomness). Watrous §§2.1.3 and 6.1.2 provides the purification and LOCC background.

### M30 — The complete result, its significance and its evidence

- **Phase:** Narrative/innovation.
- **Central question:** What establishes the secrecy exponent, and what makes the finite even-size statement exact?
- **Understanding target:** Connect the literal independent-source marginal, polar inequality and sum over inactive outcomes to the weighted dual-code sum. Explain the exact even-size full-threshold optimum and the matching $`t/2`$ exponent above a fixed margin from one half. Identify the inherited network and coding tools and the scope of the finite checks.
- **Dependencies and story role:** Integrates both phases, especially M14, M19–M24 and M26–M29. Completes the scientific story.
- **Conceptual connection:** The argument covers one classical bit per device in a single episode without communication or feedback. Rates at or below one half, exact finite odd-size optima, leakage of quantum registers and feedback are outside the established conclusions.
- **Source pointers:** [Project overview](../README.md), [scientific route](../science/README.md), [related work](../references/RELATED_WORK.md), [resource boundaries](../science/boundaries.md), and [verification](../verification/README.md).
