# ITER006 — DVD2/DVD3 auxiliary-support combinatorics

Date: 2026-09-12

## Provenance

- Workflow run: `34708207163`
- Job: `103592020373`
- Artifact: `10301858577`
- Artifact digest: `sha256:4325022b9a03a5045eb02498f729365361dc46e42fdab1473878c70033b91335`
- Numerical B4 values were not used.
- Frozen symmetric boundary: boundary spins/intertwiners as in the Dl0 DVD pilot.

## Raw result

The prewritten script classified the result as `DVD_SUPPORT_COMBINATORICS_INCONCLUSIVE` because its specific diagnostic hypothesis — equal support cardinality at `D=0` followed by unequal cardinality at larger `D` — was false. That classification is preserved and is not rewritten after seeing the result.

Observed support counts:

| D | DVD2 admissible `(l1,l2,l3,k')` terms | DVD3 admissible fixed-`k=1` `(l1,l2,l3,l4)` terms |
|---:|---:|---:|
| 0 | 3 | 1 |
| 1 | 21 | 16 |
| 2 | 66 | 49 |
| 3 | 147 | 100 |

Thus the two source-labelled formulas have different auxiliary support cardinalities already at `D=0`. The previously observed numerical equality `DVD2=DVD3` at the frozen Dl0 symmetric point therefore cannot be explained by identical term support alone; it must arise from the weighted B4 values/normalization in that special configuration.

## Claim lock

This is only an SU(2)-admissibility/support-count observation. It does not establish a booster identity, shell convergence, a refinement map, cylindrical consistency, a continuum limit, a bridge, novelty, or new physics.
