# ITERATION 006 — RC006 ordered-context holdout robustness

Date: 2026-09-12

## Authoritative provenance

- Workflow run: `34700277881`
- Head commit: `219391c897159f4541cb629d553c373981ed8531`
- Aggregate job: `103570712196`
- Aggregate artifact: `10300002366`
- Aggregate artifact digest: `sha256:c30209c9675947d78435974d5fc11c20ffc11000b64487f98af39a48e0e56e3d`

## Frozen gate

The prospectively frozen gate required all eight leave-one-qualified-anchor-out lanes to retain ordered-context uniqueness without retuning, while the ninth `null_unordered` control had to restore ambiguity. Green CI alone was explicitly insufficient.

## Raw-result classification

The aggregate consumed all nine lane artifacts and reported:

- `lane_count = 9`;
- `holdout_passes = 8`;
- `null_classification = SCIENTIFIC_PASS_NULL_RESTORES_AMBIGUITY`;
- `robust_source_order_gate_pass = true`.

Therefore the scientific classification is:

`SCIENTIFIC_PASS_ORDERED_CONTEXT_HOLDOUT_ROBUSTNESS_PREREQUISITE_ONLY`.

This strengthens the source-order identifiability result: uniqueness is not dependent on any single one of the eight qualified anchors, and deliberately erasing ordered-neighborhood information restores ambiguity as required by the negative control.

## Scope / claim lock

This result authorizes only the next source-derived contraction-serialization validation step. It is **not** an Eq.(29) numerical amplitude, an EPRL/FK TNR reconstruction, a refinement bridge, or evidence for a candidate theory. `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, and candidate-theory construction remain locked.

## Next gate

A stricter contraction-serialization stability gate is now required: a full-source canonical serialization must remain pairwise-order identical under each leave-one-anchor-out perturbation, while the unordered null remains ambiguous. Only PASS of that frozen gate may authorize launching the minimal `k=12, gamma=1/3` Eq.(29) amplitude.
