# ITER027 run 1 — infrastructure failure before science

Date: 2026-09-14

Prospective scientific contract: `prereg/ITER027_RC006_EQ27_BOUNDED_COMPONENT_CONTRACTION_2026-09-14.md` (commit `d07fd121f0abeb34396bb4f2bc4028070fed0e12`).

Implementation commit: `fcb17f980caa82fd7a1a1482a523084125915d53`.
Workflow/production head: `95073389c83cf45851bb44473f972c89af6d3564`.
Run: `34791069641`.

## Classification

`NUMERICAL/INFRASTRUCTURE FAIL — PRE_SCIENCE_MISSING_RUNTIME_DEPENDENCY`

All four science jobs failed before lane logic executed because `code/iter019/qcg_solver_validation.py` imports `mpmath`, while the workflow installed only `numpy scipy`. Representative job `103815265001` terminated at import with `ModuleNotFoundError: No module named 'mpmath'`.

No raw science-lane artifact was uploaded. The dependent aggregate contained no scientific evidence and is not a scientific verdict. Aggregate artifact `10328686285`, digest `sha256:27040cb3f69d9e49dcedfa27cc4ce77581127d1c2d653d98ec9b62e597e4a225`.

## Repair authorization

The preregistration explicitly permits minimal repair of a numerical/infrastructure defect without changing the frozen scientific contract. The only authorized repair is to add the missing runtime dependency `mpmath` to the environment setup. No scientific code, hypothesis, panel, source authority, alpha, thresholds, PASS/FAIL/BLOCKED/INVALID criteria, or interpretation ceiling may change.

After that orchestration-only repair, rerun the exact same ITER027 gate. The retry remains the same scientific gate, not a replacement hypothesis.

Claim locks unchanged. Candidate theory remains `UNFORMED`.
