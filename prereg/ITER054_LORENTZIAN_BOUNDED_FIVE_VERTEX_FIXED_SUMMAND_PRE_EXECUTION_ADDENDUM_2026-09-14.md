# ITER054 pre-execution preregistration addendum

Date: 2026-09-14

This addendum is committed **before any ITER054 workflow or substantive vertex output exists**. It changes no object, source, input, mapping, convention, tolerance, control or PASS criterion in `prereg/ITER054_LORENTZIAN_BOUNDED_FIVE_VERTEX_FIXED_SUMMAND_2026-09-14.md`.

It only makes explicit the terminal class for an exact-runtime execution defect that the main prereg's numerical predicates already require to be absent:

**`SCIENTIFIC FAIL — LORENTZIAN_BOUNDED_FIVE_VERTEX_FIXED_SUMMAND_NUMERICAL_FAIL`** iff the exact frozen ITER051 runtime identity is established and at least one of the ten required source-defined local backend calls (five in a primary replica or five in a held-out replica) reproducibly exits nonzero or returns an unparseable/non-finite value under the frozen inputs.

This class is distinct from:

- A/B reproducibility FAIL after individually valid executions;
- runtime transport BLOCKED;
- source-object BLOCKED;
- invalid implementation/infrastructure failure.

An exact finite zero amplitude remains a valid value and is not a FAIL by itself.