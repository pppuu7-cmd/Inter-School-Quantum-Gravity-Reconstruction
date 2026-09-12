# ITERATION 006 — RC006 contraction serialization stability

Date: 2026-09-12

## Authoritative provenance

- Workflow run: `34700639086`
- Head commit: `8a358e5a710a618a8b92b689ee4470266787ef7b`
- Aggregate job: `103571679523`
- Summary artifact: `10300052796`

## Prospectively frozen gate

A source-derived canonical decorated-symbol serialization was permitted to authorize the minimal `k=12` Eq.(29) amplitude only if all of the following held simultaneously:

1. the full-source order was unique;
2. all eight leave-one-qualified-anchor-out orders remained unique;
3. every holdout retained exactly `100%` pairwise-order agreement with the full-source order;
4. the deliberately unordered null restored ambiguity.

No criterion was changed after viewing the result.

## Raw terminal result

The terminal aggregate consumed all ten lane artifacts and reported:

- `valid = true`;
- `lane_count = 10`;
- `full_unique = true`;
- `holdout_unique_count = 6` out of 8;
- `min_pairwise_order_agreement = 0.8698752228163993`;
- `null_ambiguous = true`;
- `serialization_gate_pass = false`.

The workflow was technically green, but the preregistered scientific gate failed.

## Scientific classification

`SCIENTIFIC_FAIL_CONTRACTION_SERIALIZATION_UNSTABLE`

This is not an infrastructure or numerical failure. The available exact source contexts determine a unique full-source order, but that serialization is not robust under all single-anchor deletions. The previous ordered-context identifiability and 8/8 uniqueness holdout result therefore does **not** suffice to establish a stable contraction serialization.

## Consequence

The dependent minimal `k=12, gamma=1/3` Eq.(29) numerical amplitude remains **BLOCKED**. It must not be launched by weakening the holdout criterion, selecting a favorable subset of anchors, or treating the green workflow as a scientific PASS.

The next RC006 work is diagnostic/source-authority work: localize which exact source relations carry the unstable ordering and determine whether an additional source-explicit contraction relation removes the ambiguity without retuning. If no such source authority exists, the Eq.(29) reconstruction remains blocked.

## Claim lock

No q-deformed EPRL/FK amplitude, TNR refinement bridge, `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, or candidate-theory claim follows from this result.
