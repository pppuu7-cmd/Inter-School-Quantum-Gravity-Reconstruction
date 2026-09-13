# ITER027 — RC006 bounded Eq.(27) component translation/contraction

Date: 2026-09-14

## Scientific question
After ITER026 validated the direct-source q<->qbar primitive, can the already source-pinned Eq.(27) three-valent EPRL graph be translated into a bounded component-level contraction without inventing a convention, changing the normalization family, or importing Eq.(29)/Lambda?

## Frozen scope
This gate is deliberately smaller than a one-step TNR flow. It evaluates only a bounded Eq.(27)-level component translation/contraction using the validated RC006 primitives. It gives zero bridge credit by itself.

Frozen implementation authorities:
- q-CG backend validated in ITER019/020;
- source-gauged cap/cup primitive;
- direct-source qbar primitive validated in ITER026;
- source-qualified R/R^-1 convention from ITER025B;
- source-pinned Eq.(27) topology from ITER021;
- alpha = 0 for this gate only, fixed before production;
- Eq.(29), Lambda/formLambda6j, fitted phases, fitted normalizations, and post-hoc channel repair are forbidden.

## Frozen bounded panel
Primary levels: k = {6,10,12}.
Held-out levels: k = {7,9,11}.
Use only simple-object/admissible channels supported by the existing RC006 backend. The implementation must report the exact external/internal twice-spin labels it evaluates.

## Independent lanes
A. `authority-domain`: verify exact prerequisite provenance, source locators/hashes, admissible bounded panel, and absence of forbidden Eq.(29)/Lambda dependencies.

B. `component-translation`: instantiate the Eq.(27)-relevant component dictionary from q-CG, qbar, cap/cup and R primitives and verify tensor shapes, index ordering and source-duality identities. No amplitude fitting is allowed.

C. `bounded-contraction`: evaluate a bounded set of source-defined local contractions on the frozen primary panel and held-out panel. Required finite-number sanity checks: all outputs finite; equivalent source-prescribed contractions agree within 5e-8; held-out uses the same implementation and alpha=0 without retuning.

D. `null-controls`: at least three deliberately wrong structural variants must be tested, including (i) inverse-parameter qbar legacy construction, (ii) wrong magnetic-index ordering, and (iii) R/R^-1 swap where semantically active. At least 2/3 must be detected by a frozen residual > 1e-6 or by an exact source-authority violation.

Use fail-fast:false. The aggregate is dependent and must wait for all lanes.

## Frozen classification
`SCIENTIFIC PASS — RC006_EQ27_BOUNDED_COMPONENT_CONTRACTION_VALIDATED_SCOPED` only if all A-D pass and no forbidden ingredient is used.

`SCIENTIFIC FAIL — RC006_EQ27_BOUNDED_COMPONENT_CONTRACTION_FAIL` if a fully authorized and numerically stable implementation violates a frozen equality/tolerance.

`BLOCKED — RC006_EQ27_COMPONENT_CONTRACTION_BLOCKED_<reason>` if a required source-qualified mapping/primitive is still missing or Eq.(27) cannot be instantiated without an unqualified convention.

`NUMERICAL/INFRASTRUCTURE FAIL` for non-scientific execution defects. Such defects may be minimally repaired without changing this preregistration.

Green CI is never sufficient for scientific PASS.

## Claim locks
Even PASS does not authorize Eq.(29), Lambda, one-step TNR, bridge credit, preferred alpha, candidate-theory construction, NEW_PHYSICS_FOUND, NEW_QG_THEORY_REQUIRED, ALL_KNOWN_SCHOOLS_FAIL, or BRIDGE_DERIVED.

Candidate theory remains 0% / UNFORMED.
