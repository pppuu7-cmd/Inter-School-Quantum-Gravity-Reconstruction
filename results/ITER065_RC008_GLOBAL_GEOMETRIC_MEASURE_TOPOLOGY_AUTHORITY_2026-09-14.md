# ITER065 — RC008 global geometric measure / topology authority — terminal result

Date: 2026-09-14

## Frozen gate
Preregistration commit: `e1f97fa2ac91a48e9bb479c81074ea091c0d6d21`

Implementation commits:
- `f25ccba64d81de1daa4d3c6205a7425d22b93e3e` — geometric/source gate
- `031cfefd7a0d6f2b62bfce79a12f9a55c544fb98` — aggregate classifier

Initial production head: `3609580257c5ff35bbf292d7d04754031bf3523f`
Initial authoritative run: `34877639682`

Frozen source set: arXiv `1508.07961`, `1605.07649`, `1701.02311`, `1804.00023`.

## Initial run classification
Geometry lanes were terminal success, but all four source-authority jobs failed before scientific evaluation because `gate.py` imported NumPy while the source job installed only `requests` and `pypdf`.

Initial jobs:
- `coarse2` job `104088680434` — terminal success; artifact `10360359283`
- `fine32` job `104088680602` — terminal success; artifact `10360279585`
- `sentinel` job `104088680539` — terminal success; artifact `10361348303`
- source `1508.07961` job `104088680890` — PRE-SCIENCE infrastructure fail
- source `1605.07649` job `104088681482` — PRE-SCIENCE infrastructure fail
- source `1701.02311` job `104088681655` — PRE-SCIENCE infrastructure fail
- source `1804.00023` job `104088681494` — PRE-SCIENCE infrastructure fail
- aggregate job `104089121442` — failed because source artifacts were missing

The source failures are **INFRASTRUCTURE FAIL PRE-SCIENCE**, not scientific FAIL.

## Minimal technical repair
Only the missing runtime dependency was repaired; frozen sources, terms, inclusion logic, numerical predicates and scientific interpretation were unchanged.

Repair workflow commit: `3f1aa480828330941039e7133fab30ca1b3ec6d7`
Repair run: `34877767148`

Repair jobs/artifacts:
- source `1508.07961`: job `104090722998`, artifact `10361751291`
- source `1605.07649`: job `104090723037`, artifact `10361303858`
- source `1701.02311`: job `104090722962`, artifact `10361542560`
- source `1804.00023`: job `104090723009`, artifact `10361691343`
- source aggregate: job `104091156913`, artifact `10362035885`

All four repaired source lanes were terminal success. Automated aggregate classification was `SOURCE_AUTHORITY_CANDIDATE_PRESENT_REQUIRES_MANUAL_EQUATION_AUDIT`, which carries no gate credit by preregistration.

## Geometry diagnostics
### coarse2
Classification: `DIAGNOSTIC_PASS_GEOMETRIC_PULLBACK`.
Across all five frozen points:
- reduced dimension = 1;
- analytic-vs-central-FD Jacobian relative discrepancy was of order `1e-10`, far below the frozen `2e-5` threshold;
- Jacobian rank = 1;
- Gram log-determinant finite with positive sign.

### fine32
Classification: `DIAGNOSTIC_PASS_GEOMETRIC_PULLBACK`.
Across all five frozen points:
- concatenated outputs = 192;
- reduced dimension = 6;
- analytic-vs-central-FD Jacobian relative discrepancy was of order `1e-10`;
- Jacobian rank = 6;
- Gram log-determinant finite with positive sign.

These establish internal correctness of the reduced geometric embedding/pullback implementation only. They do **not** identify the physical spin-foam quantum measure.

## Adversarial sentinel
Classification: `ADVERSARIAL_SENTINEL_REJECTS_CONSTANT_LOCAL_PRODUCT_EQUIVALENCE`.

Frozen coefficient-of-variation results for
`product(local one-hypercuboid Delta_FP) / sqrt(det(J^T J))`:
- `coarse2`: `CV = 1.7507220128211347`
- `fine32`: `CV = 1.8556104685006718`

Both exceed the frozen `1e-2` non-constancy sentinel threshold by a large margin. Narrow conclusion only: the old product of local one-cell `Delta_FP` factors is not identical up to a single normalization constant to this independent geometric embedding-pullback sentinel. This does not determine the correct physical measure.

## Manual equation-level source audit
### arXiv:1701.02311
This is the strongest authority. It explicitly states that converting spins to lengths introduces a nontrivial Faddeev-Popov determinant and includes the determinant in the path integral. Appendix B derives the determinant for **one four-dimensional hypercuboid** and gives the explicit one-hypercuboid `Delta_FP` structure relevant to the earlier implementation.

However, the audited source does not provide an explicit equation deriving the global glued-complex coarse/fine reduced measure as a simple product of one-cell `Delta_FP` factors. The statement that the general case can be inferred from the one-hypercuboid result is not, by itself, sufficient authority for the specific naive factorization used by ITER062B.

### arXiv:1605.07649
Provides coarse/fine and path-integral/measure discussion in the hypercuboidal RG setting, but the audited passages do not derive the required explicit global Faddeev-Popov/Jacobian factorization for the current glued coarse/fine construction.

### arXiv:1508.07961
Provides the foundational quantum-cuboid restricted-state-sum setting, but no explicit global glued-complex Faddeev-Popov factorization for the current construction was found in the audited passages.

### arXiv:1804.00023
Contains an explicit symmetry-reduction Jacobian in its hyperfrustum/cosmological coarse/fine model. This is useful as a structural analogue but is a different restricted model/topology and is not source-faithful authority for the RC008 quantum-cuboid global measure used in ITER062B.

## Terminal scientific classification
**`SCOPED_BLOCKED_RC008_GLOBAL_MEASURE_FACTORISATION_UNDERIVED`**

Equivalent descriptive status: **SCOPED BLOCKED — ONE-CELL FP AUTHORITY PRESENT; GLOBAL GLUED-COMPLEX FACTORISATION NOT EXPLICITLY DERIVED.**

This is not an RC008 physical scientific FAIL. It blocks the previous coarse/fine crossing inference because the global quantum-measure mapping remains unqualified.

## Credit and claim locks
- ITER065 scientific/gate credit: **0**
- RC008 corrected crossing authorized: **false**
- restricted coarse/fine amplitude reproduction: **false**
- bridge credit: **0**
- candidate theory: **0% / UNFORMED**
- overall programme readiness: **50%**, unchanged

No `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, `NEW_QG_THEORY_REQUIRED`, `ALL_KNOWN_SCHOOLS_FAIL`, fixed-point or candidate-theory claim is authorized.

## Next admissible action
Do not rerun the RC008 crossing with another guessed measure. A later RC008 amplitude/refinement gate requires a prospectively frozen, mathematically and source-justified global measure / constraint-overlap / gluing object first.

Compute should move to an independent PHASE_1 front unless such an object is independently derived and qualified.