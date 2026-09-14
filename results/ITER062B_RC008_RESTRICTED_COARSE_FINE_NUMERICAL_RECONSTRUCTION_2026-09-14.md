# ITER062B — RC008 restricted coarse/fine numerical reconstruction

Date: 2026-09-14

## Frozen provenance

- prereg commit: `6fa9eb40d45be8facc952716bde83c57e962469d`
- implementation commit: `8039a7e8a17aa2b62baead26452425971367ae9c`
- production/workflow head: `3f4b1c89d5183cde99ae6f7cdfa9efe06ae6d829`
- authoritative Actions run: `34874113741`
- aggregate job: `104077252124`
- aggregate artifact: `10359819990`
- aggregate digest: `sha256:fd62c82a618b6ded0e4ab0013610f00a33a70551e9d3f76ab1188d1c2f44493b`

All five scientific lanes and the dependent aggregate completed successfully. Green CI alone was not used as the scientific verdict; the raw aggregate was consumed against the preregistered predicates.

## Scientific classification

**SCIENTIFIC PASS — `SCIENTIFIC_PASS_RC008_RESTRICTED_COARSE_FINE_NUMERICAL_RECONSTRUCTION_SCOPED`**

Calibration passed: source homogeneity, axis-relabeling invariance, FP positivity/finiteness and malformed-area-map detection all satisfied the frozen checks.

At the frozen alpha panel and without boundary-specific retuning:

- B0 `(1,1,1,1)`: converged; robust crossing bracket `[0.50,0.55]`; report-only linear location `0.534507642057044`.
- B1 `(1,1,1,3)`: converged; robust crossing bracket `[0.55,0.60]`; report-only linear location `0.5669524248350563`.
- B2 `(3,1,1,1)`: converged; robust crossing bracket `[0.50,0.55]`; report-only linear location `0.5277179126897538`.
- B3 `(3,5,1,1)`: converged but no robust crossing on the frozen panel.

Thus B0 satisfies the primary reproduction predicate and at least one held-out boundary transports the same non-retuned crossing; in fact B1 and B2 both do. B3 is a preserved held-out negative result, not retuned away.

## Scope locks

This PASS is only for the severe symmetry-restricted geometric large-j Riemannian EPRL-FK quantum-cuboid/hypercuboid truncation under the source-qualified coarse/fine construction. It does not establish full EPRL/FK refinement, Lorentzian refinement, q-deformed reconstruction, continuum/GR recovery, a cross-school bridge, or new physics.

`bridge_credit=false`; `candidate_theory=UNFORMED/0`; `full_eprl_refinement=false`; `lorentzian_refinement=false`; `new_physics=false`.

## Next admissible gate

A prospectively frozen held-out non-retuned transport/selector panel is now admissible. It must reuse the same amplitude, integration method, alpha panel, numerical thresholds and crossing predicate. New boundaries must be fixed before execution and include both moderate and stronger anisotropy; no boundary may be selected or discarded after seeing results.
