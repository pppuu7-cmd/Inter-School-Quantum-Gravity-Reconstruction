# ITER131 — Explicit momentum vertex generator (4D repair)

Date: 2026-09-15

## Frozen gate verdict

**PASS_SCOPED_EXPLICIT_R2_GAMMA2_MOMENTUM_TENSOR_GENERATOR_CLOSED**

This is a scoped symbolic-implementation PASS only. It does not establish a nonzero one-loop pole, a value/sign for B1, agreement with EDT, a cross-school bridge, or new physics.

## Authoritative provenance

- preregistration commit: `85aa6efd9c83c34ee42207d25538acfa5a159f40`
- repaired 4D implementation / run head: `da613bc5cc9bff6b68ff1423f7aec06f5a30a28c`
- authoritative Actions run: `34919245281`
- job: `104223426799` (`momentum-vertex-generator`)
- artifact: `10377945043` (`iter131-explicit-momentum-vertices`)
- artifact SHA256: `291a0eb1d56ecd0065f74b9655aa468d3f7a241047cf02ea187cb7ecbd566e03`

## Consumed raw-log result

The repaired run targets `dimension=4` and reports all frozen checks true:

- A explicit component tables: PASS
- B four-dimensional target: PASS
- C R2 Bose symmetry: PASS
- D Gamma2 lower-index symmetry: PASS
- D Gamma2 leg Bose symmetry: PASS
- E held-out plane-wave polarization: PASS
- F R2 momentum degree 2: PASS
- F Gamma2 momentum degree 1: PASS
- G target independence: PASS

Generated table sizes are `R2_component_count=100` and `Gamma2_component_count=6400`, consistent with the repaired 4D symmetric graviton basis.

The earlier D=2 green run is retained only as implementation history and is not scientific evidence for the 4D gate.

## Scientific consequence

ITER131 closes the explicit 4D R2/Gamma2 momentum-tensor-generator prerequisite. It authorizes preregistration of the next original-calculation layer: Gaussian M/G pole-relevant numerator-jet construction using these frozen tensors, with target-blind algebra and held-out checks. It does **not** authorize reading off or fitting the physical G^2/l^8 logarithmic coefficient.

Candidate theory remains `0 / UNFORMED`; bridge credit remains zero and all claim locks remain active.
