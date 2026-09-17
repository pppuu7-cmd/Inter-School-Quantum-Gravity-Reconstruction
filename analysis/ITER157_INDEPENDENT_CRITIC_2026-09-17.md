# ITER157 independent scientific Critic

Date: 2026-09-17

## Frozen input reconstructed independently

Scientific preregistration commit: `88aabc760dc01ad73585276d3345bfdf8a90aedf`.

Frozen question: whether **pre-existing repository material** contains at least one explicit, source-faithful tensor-resolved divergent first-M/G endpoint pole equation, or a complete derivation chain, mapping into the immutable ITER118 basis `R,S,DR,DS,BoxR,D2R,BoxS,D2S` with an explicit coefficient.

The Critic did **not** accept the producer `candidate_count` as scientific evidence. It inspected the raw artifact candidates against their source contexts and the frozen admissibility rule.

## Independent acceptance tests

A candidate is admissible only if the same mathematical object simultaneously supplies:

1. a divergent pole/residue relation;
2. a fixed-geodesic endpoint stratum relevant to the first-M/G scope;
3. a tensor-resolved endpoint object;
4. an ITER118 basis direction as the actual endpoint operator direction;
5. an explicit coefficient or complete equation sufficient to determine one;
6. normalization/conventions sufficient to map into the repository basis.

## Candidate replay

1. `analysis/ITER153_RESULT_2026-09-17.md:117` — reject. Successor-gate prose; explicitly retains endpoint/line coefficients symbolically.
2. `analysis/ITER156_RESULT_2026-09-17.md:11` — reject. Negative rank-0/no-equation statement, not an equation.
3. `analysis/iter153_adversarial_critic.py:148` — reject. Critic prose naming a missing graph-level R-operation.
4. `analysis/iter156_endpoint_coefficient_identifiability.py:15` — reject. Regex search pattern for `R`, not a physical coefficient.
5. `analysis/iter156_endpoint_coefficient_identifiability.py:16` — reject. Regex search pattern for `S`, not a physical coefficient.
6. `prereg/ITER156_FIXED_GEODESIC_FIRST_MG_ENDPOINT_COEFFICIENT_IDENTIFIABILITY_2026-09-17.md:14` — reject. Prospective basis/rank rule, not a residue.
7. `results/ITER118_ADVERSARIAL_CRITIC_2026-09-15.md:38` — reject. The identity reducing line integrals of `DR`/`DS` to boundary differences is an operator-classification statement; it has no first-M/G UV pole, pole order, graph-specific tensor residue, coefficient, or normalization map.

Accepted candidates: **0**.
Rejected candidates: **7**.

## Critic verdict

`PASS_CRITIC_ITER157_BLOCKED_CLASSIFICATION_SOUND`

The only frozen scientific classification consistent with the preregistration is:

`BLOCKED_SCOPED_ITER157_NO_SOURCE_FAITHFUL_ENDPOINT_TENSOR_POLE_EQUATION_FOUND`

This is a source/equation blocker, not a physical FAIL. It does not set any endpoint coefficient or divergence to zero. It does not authorize `B1_total`, bridge credit, new-physics claims, or candidate-theory construction.
