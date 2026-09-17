# ITER164 preregistration — open-G endpoint Laurent/distributional R-operation

Frozen before ITER164 computation.

## Input lock
- Start only from the validated ITER163 21-term source-complete covariant ledger.
- Preserve the free symmetric metric leg and lower/upper endpoint orientation.
- Do not consume ITER160 `-525` to infer tensor structure.
- Do not set cancelled-propagator/contact sectors to zero.
- Do not perform ITER118 coefficient/rank matching.

## First gate: source-operation availability
Before constructing any Laurent pole tensor, establish whether the repository's authoritative source-derived machinery contains an explicit distributional endpoint extension/R-operation sufficient to act on the open-leg G vertex.

Two independent lanes are frozen:
1. `operation-audit`: inventory exact repository definitions/usages of distributional extension, plus-distribution, Hadamard finite part, R-operation/forest subtraction, Laurent pole extraction and endpoint counterterm/contact prescriptions. It must report file/line evidence and whether an executable/source-faithful open-leg endpoint operation exists.
2. `closure-critic`: independently inspect the ITER161/ITER163 dependency chain and test whether a complete pole tensor can be derived without adding an unstated prescription. It must fail closed on missing orientation-preserving contact treatment.

## Classification
- `PASS_SOURCE_OPERATION_AVAILABLE`: only if an explicit, source-faithful, orientation-preserving operation is identified with enough information to compute the complete open-leg `1/epsilon` pole tensor including contact sectors.
- `BLOCKED_MISSING_SOURCE_OPERATION`: if no such operation is present.
- `BLOCKED_NONUNIQUE_EXTENSION`: if multiple admissible local extensions remain without a frozen selector.
- `SCIENTIFIC_FAIL`: only if a frozen claimed identity/operation is contradicted.
- infrastructure failures remain separate.

A green workflow is not a scientific PASS. The audit may terminate BLOCKED and that is an acceptable scientific outcome. No threshold, basis or prescription may be added after seeing the result to force PASS.

## Next-step lock
Only `PASS_SOURCE_OPERATION_AVAILABLE` authorizes implementation of the Laurent/pole-tensor producer. BLOCKED outcomes authorize only a mathematically/source-justified acquisition/derivation of the missing operation, not ITER118 matching or denser scalar endpoint computation.
