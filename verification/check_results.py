#!/usr/bin/env python3
"""Reproduce finite checks; these checks supplement the proofs, not replace them.

Python 3.10+; standard library only. Run from any working directory.
"""

from __future__ import annotations

import argparse
import cmath
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from time import perf_counter


EXPECTED_PATH = Path(__file__).with_name("expected_results.json")
TOLERANCE = 2e-10


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(actual: float | complex, expected: float | complex, message: str) -> None:
    require(
        abs(actual - expected) <= TOLERANCE * max(1.0, abs(expected)),
        f"{message}: {actual!r} != {expected!r}",
    )


def additive_shares(n: int, p: int, secret: int):
    for prefix in itertools.product(range(p), repeat=n - 1):
        yield prefix + ((secret - sum(prefix)) % p,)


def eigenbra(theta: float, bit: int) -> tuple[complex, complex]:
    """Bra of the outcome-bit eigenvector of cos(theta) X + sin(theta) Y."""
    scale = 1 / math.sqrt(2)
    return scale, (-1 if bit else 1) * cmath.exp(-1j * theta) * scale


def bell_born_probability(theta_a: float, theta_b: float, bits: int) -> float:
    """Born rule on (|00>+|11>)/sqrt(2), without inserting a cosine correlator."""
    bra_a = eigenbra(theta_a, bits & 1)
    bra_b = eigenbra(theta_b, (bits >> 1) & 1)
    amplitude = sum(bra_a[j] * bra_b[j] for j in range(2)) / math.sqrt(2)
    return abs(amplitude) ** 2


def matching_distribution(
    n: int, p: int, secret: int, frequency: int, total_phase: float, sharings=None
) -> list[float]:
    tables = []
    for edge in range(n // 2):
        phase = total_phase if edge == 0 else 0.0
        table = {}
        for x, y in itertools.product(range(p), repeat=2):
            angles = (2 * math.pi * frequency * x / p + phase,
                      2 * math.pi * frequency * y / p)
            table[x, y] = [bell_born_probability(*angles, b) for b in range(4)]
        tables.append(table)
    distribution = [0.0] * (1 << n)
    if sharings is None:
        sharings = additive_shares(n, p, secret)
    for shares in sharings:
        probabilities = [1.0]
        for edge, table in enumerate(tables):
            pair = table[shares[2 * edge], shares[2 * edge + 1]]
            # The first device occupies the least-significant output bit.
            probabilities = [
                probabilities[low] * pair[high]
                for high in range(4)
                for low in range(len(probabilities))
            ]
        offset = 0
        if n % 2 and math.cos(2 * math.pi * frequency * shares[-1] / p) < 0:
            offset = 1 << (n - 1)
        for output, probability in enumerate(probabilities, start=offset):
            distribution[output] += probability
    count = p ** (n - 1)
    return [probability / count for probability in distribution]


def parity_expectation(distribution, mask: int):
    return sum(
        (-1 if (output & mask).bit_count() % 2 else 1) * probability
        for output, probability in enumerate(distribution)
    )


def check_matching() -> list[dict]:
    results = []
    for n, p, secrets in [(2, 3, (0, 1)), (4, 5, (1, 3)), (6, 7, (2, 5))]:
        s, t = secrets
        frequency = ((p - 1) // 2) * pow((s - t) % p, -1, p) % p
        phase = math.pi / 2 - math.pi * frequency * (s + t) / p
        distributions = [
            matching_distribution(n, p, secret, frequency, phase)
            for secret in secrets
        ]
        for distribution in distributions:
            close(sum(distribution), 1.0, "Bell probability normalization")
            require(min(distribution) >= -TOLERANCE, "Negative Born probability")
            for mask in range(1, (1 << n) - 1):
                close(parity_expectation(distribution, mask), 0.0,
                      "Proper Bell output parity")
        actual = sum(abs(a - b) for a, b in zip(*distributions)) / 2
        claimed = 2 ** (1 - n / 2) * math.cos(math.pi / (2 * p))
        close(actual, claimed, "Matching attack optimum")
        results.append({
            "n": n, "p": p, "secrets": list(secrets), "frequency": frequency,
            "sharings_per_secret": p ** (n - 1),
            "outcomes": 1 << n,
            "direct_total_variation": actual,
            "exact_formula": claimed,
        })
    return results


def scaled_reconstruction_shares(points: tuple[int, ...], p: int, secret: int):
    weights = [
        math.prod(-y * pow((x - y) % p, -1, p) for y in points if y != x) % p
        for x in points
    ]
    for coefficients in itertools.product(range(p), repeat=len(points) - 1):
        yield tuple(
            weight * (secret + sum(c * pow(point, j, p)
                                   for j, c in enumerate(coefficients, start=1))) % p
            for point, weight in zip(points, weights)
        )


def check_odd_reconstruction_set() -> list[dict]:
    results = []
    for n, t, p, secrets in [(5, 3, 7, (0, 1)), (6, 5, 7, (2, 5))]:
        points = (n,) + tuple(range(1, t))
        s, other = secrets
        frequency = ((p - 1) // 2) * pow((s - other) % p, -1, p) % p
        phase = math.pi / 2 - math.pi * frequency * (s + other) / p
        distributions = []
        for secret in secrets:
            sharings = set(scaled_reconstruction_shares(points, p, secret))
            require(sharings == set(additive_shares(t, p, secret)),
                    "Lagrange scaling failed to recover uniform additive shares")
            distribution = matching_distribution(t, p, secret, frequency, phase, sorted(sharings))
            close(sum(distribution), 1.0, "Odd strategy probability normalization")
            distributions.append(distribution)
        for mask in range(1, (1 << t) - 1):
            close(parity_expectation(distributions[0], mask),
                  parity_expectation(distributions[1], mask), "Proper parity depends on secret")
        actual = sum(abs(a - b) for a, b in zip(*distributions)) / 2
        sign_coefficient = sum(abs(math.cos(2 * math.pi * x / p)) for x in range(p)) / p
        require(sign_coefficient >= 1 / 2, "Odd singleton coefficient floor")
        claimed = 2 ** (1 - (t - 1) / 2) * sign_coefficient * math.cos(math.pi / (2 * p))
        close(actual, claimed, "Odd reconstruction-set witness")
        results.append({
            "n": n, "t": t, "p": p, "secrets": list(secrets),
            "reconstruction_points": list(points), "singleton_coefficient": sign_coefficient,
            "direct_total_variation": actual, "witness_formula": claimed,
        })
    return results


def cyclic_product(left: list[int], right: list[int]) -> list[int]:
    """Integer multiplication modulo z^p-1; no floating-point roots of unity."""
    p = len(left)
    result = [0] * p
    for i, a in enumerate(left):
        if a:
            for j, b in enumerate(right):
                if b:
                    result[(i + j) % p] += a * b
    return result


def exact_fourier_parities(
    n: int, t: int, p: int, secret: int, dual: list[tuple[int, ...]], signs
) -> list[Fraction]:
    transforms = []
    for local_signs in signs:
        table = []
        for frequency in range(p):
            numerator = [0] * p
            for share, value in enumerate(local_signs):
                numerator[-frequency * share % p] += value
            table.append(numerator)
        transforms.append(table)
    parities = []
    for mask in range(1 << n):
        active = [i for i in range(n) if mask >> i & 1]
        numerator = [0] * p
        for word in dual:
            if any(word[i] and not (mask >> i & 1) for i in range(n)):
                continue
            term = [1] + [0] * (p - 1)
            for i in active:
                term = cyclic_product(term, transforms[i][word[i]])
            phase = secret * sum(word) % p
            for exponent, value in enumerate(term):
                numerator[(exponent + phase) % p] += value
        # At a primitive p-th root, z^(p-1) = -(1+...+z^(p-2)).
        canonical = [value - numerator[-1] for value in numerator[:-1]]
        require(not any(canonical[1:]), "A parity average was not rational")
        parities.append(Fraction(canonical[0], p ** len(active)))
    return parities


def check_shamir_fourier() -> list[dict]:
    results = []
    for n, t, p in [(4, 3, 5), (5, 3, 7)]:
        points = list(range(1, n + 1))
        rows = [tuple(pow(x, degree, p) for x in points)
                for degree in range(1, t)]
        # Brute-force the annihilator independently of an MDS generator formula.
        dual = [
            word for word in itertools.product(range(p), repeat=n)
            if all(sum(a * b for a, b in zip(word, row)) % p == 0
                   for row in rows)
        ]
        dimension = n - t + 1
        require(len(dual) == p ** dimension, "Wrong dual-code cardinality")
        min_weight = min(sum(value != 0 for value in word)
                         for word in dual if any(word))
        require(min_weight == t, "Wrong MDS minimum weight")
        projections = list(itertools.combinations(range(n), dimension))
        for coordinates in projections:
            require(
                len({tuple(word[i] for i in coordinates) for word in dual})
                == p ** dimension,
                "A claimed MDS information-set projection was not bijective",
            )
        signs = [
            [1 if (x * x + (i + 2) * x + i) % p < (p + 1) // 2 else -1
             for x in range(p)]
            for i in range(n)
        ]
        all_parities = []
        distributions = []
        for secret in (0, 1):
            counts = [0] * (1 << n)
            coset = set()
            for coefficients in itertools.product(range(p), repeat=t - 1):
                shares = tuple(
                    (secret + sum(c * rows[j][i]
                                  for j, c in enumerate(coefficients))) % p
                    for i in range(n)
                )
                coset.add(shares)
                output = sum((signs[i][shares[i]] < 0) << i for i in range(n))
                counts[output] += 1
            total = p ** (t - 1)
            require(len(coset) == total, "A Shamir coset was enumerated incorrectly")
            direct = [Fraction(count, total) for count in counts]
            fourier = exact_fourier_parities(n, t, p, secret, dual, signs)
            for mask, value in enumerate(fourier):
                require(value == parity_expectation(direct, mask),
                        "Exact Shamir Fourier parity disagrees with enumeration")
            for output, probability in enumerate(direct):
                recovered = sum(
                    (-1 if (output & mask).bit_count() % 2 else 1) * value
                    for mask, value in enumerate(fourier)
                ) / (1 << n)
                require(recovered == probability, "Exact Walsh normalization failed")
            all_parities.append(fourier)
            distributions.append(direct)
        for mask in range(1 << n):
            if mask.bit_count() < t:
                require(all_parities[0][mask] == all_parities[1][mask],
                        "A below-threshold share parity depended on the secret")
        dependent_proper = sum(
            all_parities[0][mask] != all_parities[1][mask]
            for mask in range(1, (1 << n) - 1)
        )
        require(dependent_proper > 0,
                "Chosen example no longer tests secret-dependent proper parities")
        distance = sum(abs(a - b) for a, b in zip(*distributions)) / 2
        results.append({
            "n": n, "t": t, "p": p,
            "dual_dimension": dimension, "dual_words": len(dual),
            "minimum_nonzero_weight": min_weight,
            "bijective_information_sets": len(projections),
            "exact_parity_identities_checked": 2 * (1 << n),
            "secret_dependent_proper_parities": dependent_proper,
            "direct_total_variation_fraction": str(distance),
        })
    return results


def triangle_effect(p: int, device: int, share: int, bit: int) -> list[list[complex]]:
    """A binary effect at a two-qubit vertex of the triangle fixture."""
    frequency = (2, 4, 1)[device]
    angle = 2 * math.pi * frequency * share / p
    effect = [[0j] * 4 for _ in range(4)]
    sign = (-1) ** bit
    for column in range(4):
        effect[column][column] = (1 + sign * (0.12 + 0.04 * (-1) ** (column & 1))) / 2
        effect[column ^ 2][column] = sign * 0.55 * cmath.exp(1j * (-1) ** (column >> 1) * angle) / 2
        effect[column ^ 1][column] = sign * 0.20 * cmath.exp(2j * (-1) ** (column & 1) * angle) / 2
    return effect


def triangle_reference_block(operators) -> list[complex]:
    """Trace devices out of a triangle with one purified mixed source and two Bell sources."""
    terms = [((2 * a + c, 2 * a + b, 2 * b + c), a, math.sqrt((0.6, 0.4)[a]) / 2)
             for a, b, c in itertools.product(range(2), repeat=3)]
    block = [0j] * 4
    for states, a, amp in terms:
        for other_states, other_a, other_amp in terms:
            block[2 * a + other_a] += amp * other_amp * math.prod(
                op[y][x] for op, x, y in zip(operators, states, other_states)
            )
    return block


def qubit_trace_norm(block: list[complex]) -> float:
    """Sum the singular values of a complex two-by-two Fourier block."""
    a, b, c, d = block
    return math.sqrt(sum(abs(x) ** 2 for x in block) + 2 * abs(a * d - b * c))


def fourier_triangle_effects(outcome, omega: complex, p: int):
    matrices = []
    for z in range(p):
        phases = [omega ** (-x * z) / p for x in range(p)]
        matrices.append([
            [sum(phase * matrix[a][b] for phase, matrix in zip(phases, outcome))
             for b in range(4)]
            for a in range(4)
        ])
    return matrices


def check_support_only_reference() -> dict:
    p, points = 5, (1, 2, 3)
    omega = cmath.exp(2j * math.pi / p)
    effects = [[[triangle_effect(p, device, x, bit) for x in range(p)]
                for bit in (0, 1)] for device in range(3)]
    fourier = [[fourier_triangle_effects(outcome, omega, p) for outcome in vertex]
               for vertex in effects]
    masses = []
    for device, vertex in enumerate(fourier):
        diagonal = (0.3, 0.3, 0.2, 0.2) if device != 2 else (0.25,) * 4
        second_moments = []
        for plus, minus in zip(*vertex):
            second_moments.append(sum(
                diagonal[b] * abs(plus[a][b] - minus[a][b]) ** 2
                for a, b in itertools.product(range(4), repeat=2)
            ))
        masses.append([(second_moments[z] * second_moments[-z % p]) ** 0.25 for z in range(p)])
    outcomes = list(itertools.product(range(2), repeat=3))
    expansions = [[0j] * 4 for _ in outcomes]
    majorant = 0.0
    proper_support_terms = 0
    words = [word for word in itertools.product(range(p), repeat=3)
             if any(word) and sum(a * k for a, k in zip(points, word)) % p == 0]
    for word in words:
        coefficient_norm = 0.0
        for output, expansion in zip(outcomes, expansions):
            block = triangle_reference_block([vertex[b][k] for vertex, b, k in zip(fourier, output, word)])
            coefficient_norm += qubit_trace_norm(block)
            for i, element in enumerate(block):
                expansion[i] += (1 - omega ** sum(word)) * element
        bound = math.prod(h[k] for h, k in zip(masses, word) if k)
        require(coefficient_norm <= bound + TOLERANCE, "Support-only coefficient bound violated")
        majorant += abs(1 - omega ** sum(word)) * bound / 2
        if not all(word) and coefficient_norm > TOLERANCE:
            proper_support_terms += 1
    require(proper_support_terms > 0, "Fixture must exercise inactive outcomes")

    distance = 0.0
    bit_only_distance = 0.0
    for output, expansion in zip(outcomes, expansions):
        direct = [0j] * 4
        for secret in (0, 1):
            for slope in range(p):
                shares = [(secret + slope * point) % p for point in points]
                block = triangle_reference_block([vertex[b][x] for vertex, b, x in zip(effects, output, shares)])
                for i, element in enumerate(block):
                    direct[i] += (-1) ** secret * element / p
        for actual, expected in zip(direct, expansion):
            close(actual, expected, "Direct quantum output block disagrees with Fourier expansion")
        distance += qubit_trace_norm(direct) / 2
        bit_only_distance += abs(direct[0] + direct[3]) / 2
    require(distance <= majorant + TOLERANCE, "Direct reference distance exceeds weighted bound")
    require(distance > bit_only_distance + TOLERANCE, "Fixture must retain information in the reference")
    return {
        "n": 3, "t": 2, "p": p,
        "nonzero_dual_words_checked": len(words),
        "nonvanishing_proper_support_terms": proper_support_terms,
        "direct_cq_trace_distance": distance,
        "leaked_bits_only_distance": bit_only_distance,
        "phase_weighted_support_only_majorant": majorant,
    }


def logsumexp2(a: float, b: float) -> float:
    high, low = max(a, b), min(a, b)
    return high + math.log2(1 + 2 ** (low - high))


def entropy2(tau: float) -> float:
    if tau in (0.0, 1.0):
        return 0.0
    return -tau * math.log2(tau) - (1 - tau) * math.log2(1 - tau)


def numerical_minimum(function) -> tuple[float, float]:
    """Golden-section minimization of the original log-bound on 0<=log2(lambda)<=4."""
    low, high = 0.0, 4.0
    ratio = (math.sqrt(5) - 1) / 2
    left = high - ratio * (high - low)
    right = low + ratio * (high - low)
    f_left, f_right = function(left), function(right)
    for _ in range(96):
        if f_left <= f_right:
            high, right, f_right = right, left, f_left
            left = high - ratio * (high - low)
            f_left = function(left)
        else:
            low, left, f_left = left, right, f_right
            right = low + ratio * (high - low)
            f_right = function(right)
    optimum = (low + high) / 2
    value = function(optimum)
    require(value < min(function(0.0), function(4.0)),
            "Numerical minimum was not inside the checked interval")
    return optimum, value


def support_only_log_bound(n: int, t: int, log_lambda: float, subtract_zero: bool) -> float:
    r = n - t + 1
    q = n / r
    log_partition = r * logsumexp2(0.0, 1 - q / 2 + q * log_lambda)
    if subtract_zero:
        log_partition += math.log2(-math.expm1(-log_partition * math.log(2)))
    return -t * log_lambda + log_partition


def check_optimization() -> list[dict]:
    finite = []
    for n, t in [(10, 6), (40, 37), (1000, 950)]:
        r = n - t + 1
        tau = t / n
        log_lambda, relaxed = numerical_minimum(
            lambda x: support_only_log_bound(n, t, x, subtract_zero=False)
        )
        closed = -t / 2 + r * (tau + entropy2(tau))
        close(relaxed, closed, "Relaxed support-only finite optimization")
        retained = support_only_log_bound(n, t, log_lambda, subtract_zero=True)
        require(retained <= relaxed + TOLERANCE, "Subtracting the zero word increased the bound")
        simple = -t / 2 + math.log2(3 ** r - 1)
        close(support_only_log_bound(n, t, 0.5, subtract_zero=True), simple,
              "Explicit lambda=sqrt(2) bound")
        finite.append({
            "n": n, "t": t, "q": n / r,
            "relaxed_numerical_log2_bound": relaxed,
            "relaxed_closed_log2_bound": closed,
            "zero_word_subtracted_at_relaxed_optimizer_log2_bound": retained,
            "lambda_sqrt_two_log2_bound": simple,
        })
    close(support_only_log_bound(4, 4, 0.5, subtract_zero=True), -1.0,
          "Full-threshold support-only factor before the finite-prime phase")
    return finite


def ghz_and_flagged_cq_blocks(n: int, p: int, secret: int, frequency: int):
    coherent = [[0j] * 4 for _ in range(1 << n)]
    flagged = [[0j] * 4 for _ in range(1 << n)]
    angles = [2 * math.pi * frequency * x / p for x in range(p)]
    bras = [[eigenbra(theta, b) for b in range(2)] for theta in angles]
    for shares in additive_shares(n, p, secret):
        for output in range(1 << n):
            amplitude_0 = amplitude_1 = complex(1 / math.sqrt(2))
            for i, share in enumerate(shares):
                local = bras[share][output >> i & 1]
                amplitude_0 *= local[0]
                amplitude_1 *= local[1]
            a = abs(amplitude_0) ** 2
            d = abs(amplitude_1) ** 2
            off_diagonal = amplitude_0 * amplitude_1.conjugate()
            block = coherent[output]
            block[0] += a
            block[1] += off_diagonal
            block[2] += off_diagonal.conjugate()
            block[3] += d
            # Dephasing the actual source flag removes the coherent cross terms.
            flagged[output][0] += a
            flagged[output][3] += d
    count = p ** (n - 1)
    return (
        [[entry / count for entry in block] for block in coherent],
        [[entry / count for entry in block] for block in flagged],
    )


def hermitian_qubit_trace_norm(matrix: list[complex]) -> float:
    a, z, w, d = matrix
    close(a.imag, 0.0, "Hermitian diagonal")
    close(d.imag, 0.0, "Hermitian diagonal")
    close(z, w.conjugate(), "Hermitian off-diagonal")
    trace = a.real + d.real
    gap = math.sqrt((a.real - d.real) ** 2 + 4 * abs(z) ** 2)
    return (abs(trace + gap) + abs(trace - gap)) / 2


def cq_distance(left, right) -> float:
    return sum(
        hermitian_qubit_trace_norm([a - b for a, b in zip(l, r)])
        for l, r in zip(left, right)
    ) / 2


def check_coherent_mixture_boundary() -> dict:
    n, p, s, t = 5, 7, 0, 1
    frequency = ((p - 1) // 2) * pow((s - t) % p, -1, p) % p
    coherent_s, flagged_s = ghz_and_flagged_cq_blocks(n, p, s, frequency)
    coherent_t, flagged_t = ghz_and_flagged_cq_blocks(n, p, t, frequency)
    for blocks in (coherent_s, coherent_t, flagged_s, flagged_t):
        close(sum((block[0] + block[3]).real for block in blocks), 1.0,
              "CQ normalization")
    coherent_distance = cq_distance(coherent_s, coherent_t)
    flagged_distance = cq_distance(flagged_s, flagged_t)
    claimed = math.cos(math.pi / (2 * p))
    close(coherent_distance, claimed, "Coherent-purification counterexample")
    close(flagged_distance, 0.0, "Genuinely classical flagged resource")
    marginal_s = [[sum(block[j] for block in coherent_s) for j in range(4)]]
    marginal_t = [[sum(block[j] for block in coherent_t) for j in range(4)]]
    close(cq_distance(marginal_s, marginal_t), 0.0,
          "The reference without the leaked bits must not signal the secret")
    hypothetical_bound = 2 ** (1 - n / 2) * claimed
    require(coherent_distance > hypothetical_bound + 0.01,
            "Counterexample did not separate the invalid relaxed hypothesis")
    return {
        "n": n, "p": p, "secrets": [s, t], "frequency": frequency,
        "sharings_per_secret": p ** (n - 1),
        "coherent_cq_trace_distance": coherent_distance,
        "classically_flagged_cq_trace_distance": flagged_distance,
        "reference_without_bits_trace_distance": cq_distance(marginal_s, marginal_t),
        "counterexample_formula": claimed,
        "inapplicable_product_marginal_bound": hypothetical_bound,
    }


def compare_snapshot(actual, expected, path: str = "results") -> None:
    if isinstance(expected, dict):
        require(isinstance(actual, dict) and actual.keys() == expected.keys(),
                f"Snapshot keys changed at {path}")
        for key in expected:
            compare_snapshot(actual[key], expected[key], f"{path}.{key}")
    elif isinstance(expected, list):
        require(isinstance(actual, list) and len(actual) == len(expected),
                f"Snapshot list changed at {path}")
        for i, (a, e) in enumerate(zip(actual, expected)):
            compare_snapshot(a, e, f"{path}[{i}]")
    elif isinstance(expected, float):
        close(actual, expected, f"Snapshot {path}")
    else:
        require(actual == expected, f"Snapshot mismatch at {path}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="print the full result record")
    parser.add_argument(
        "--write-expected", action="store_true",
        help="write a new snapshot only after every independent check passes",
    )
    args = parser.parse_args()
    started = perf_counter()
    results = {
        "schema_version": 2,
        "matching_born_enumeration": check_matching(),
        "odd_reconstruction_set_enumeration": check_odd_reconstruction_set(),
        "exact_shamir_fourier": check_shamir_fourier(),
        "triangle_support_only_reference": check_support_only_reference(),
        "support_only_bound_optimization": check_optimization(),
        "coherent_mixture_boundary": check_coherent_mixture_boundary(),
    }
    if args.write_expected:
        EXPECTED_PATH.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
        snapshot_status = "snapshot written after all checks passed"
    else:
        require(EXPECTED_PATH.is_file(), "Missing expected_results.json")
        compare_snapshot(results, json.loads(EXPECTED_PATH.read_text(encoding="utf-8")))
        snapshot_status = "checked snapshot agrees"
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print("PASS: explicit Bell Born-rule leakage distributions (n=2,4,6)")
        print("PASS: odd reconstruction sets with a Bell matching and singleton bit")
        print("PASS: exact Shamir dual-code, Fourier, and output-parity identities")
        print("PASS: mixed triangle reference blocks and support-only coefficient inequalities")
        print("PASS: finite support-only bound formulas and relaxed minimization")
        print("PASS: coherent purification and genuinely classical flag boundary")
        print(f"PASS: {snapshot_status}")
        print(f"Elapsed: {perf_counter() - started:.2f} seconds")
        print("Finite checks support the stated examples; the analytic proofs remain necessary.")


if __name__ == "__main__":
    main()
