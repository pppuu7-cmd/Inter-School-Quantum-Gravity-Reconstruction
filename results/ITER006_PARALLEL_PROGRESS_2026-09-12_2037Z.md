# ISQGR ITER006 parallel progress — 2026-09-12 20:37Z

## Terminal results in this research iteration

### DED/DLD topology prerequisite

Original eight-lane run `34715789027` completed all science lanes, but its aggregate failed from a missing `numpy` dependency. Recovery run `34716846693` reused the immutable lane artifacts and evaluated them with both the unchanged frozen classifier and an independent bit-count implementation. Both classified the prerequisite as `TOPOLOGY_EXTRACTION_UNSTABLE`. Cross-representation EPS↔GS comparisons pass, while DPI component-count stability fails; therefore incidence/embedding was not authorized.

Localization run `34716979296` showed that the instability is confined to DED: both DED representations change from 121 kept components at 300 dpi to 123 at 600 dpi, while DLD is stable at 15→15.

Follow-up run `34717249322` is terminal `DED_EXTRA_600DPI_COMPONENTS_LOCALIZED`. Both original EPS and GS-normalized EPS identify exactly the same two unmatched 600-dpi components: 44 pixels at normalized centroid `(0.189866082925573, 0.5180094786729857)` and 39 pixels at `(0.7200188857412654, 0.8872037914691943)`. This localizes a reproducible DED resolution sensitivity; it does not authorize threshold retuning or bridge promotion.

### RC006 Appendix-B source mapping

After correcting only the wrong pinned source path, run `34716905247` passed the frozen Appendix-B Eq. (B13) mapping at `k=6,10,12` with `bad_cases=0`, classification `RC006_B13_SOURCE_MAPPING_PASS`. Scope is convention/source-formula mapping only; it is not an Eq. (29) amplitude, RG-flow, refinement, continuum or new-physics result.

### RC006 Eq. (29) primary-source authority

Dependency run `34715908026` remains fail-closed as `EQ29_DEPENDENCY_GRAPH_INCOMPLETE` for source-faithful semantics/geometry/R-matrix/path-incidence objects.

A preregistered two-stream primary-source extraction was then launched as run `34717474214` against arXiv:1609.02429v2. Both the versioned source-bundle stream and independent PDF-text stream completed, and the frozen aggregate classified `EQ29_PRIMARY_SOURCE_EXTRACTION_READY`. The source bundle SHA256 is `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`; the only TeX source file is `bc-spin-nets.tex`. Machine extraction found EPRL, intertwiner, simplicity-constraint and R-matrix anchors in the TeX source, while the PDF-text stream independently recovered the EPRL-intertwiner section and R-matrix anchor. This is source-discovery authority only and does not mark Eq. (29) graph/incidence/R-placement as PASS.

## Active compute

Run `34717600962` — `ISQGR Iter006 RC006 Eq29 Exact Source Block` — was launched after preregistration. It has two independent jobs:

- exact hash-pinned TeX/TikZ extraction using the unique `initial 3-valent tensor` source anchor and the immediately following align environment;
- independent source-identity/unique-anchor verification.

A PASS may only establish an immutable raw Eq. (29) source block for a later frozen geometry/incidence audit. It cannot authorize an Eq. (29) amplitude by itself.

## Auto-research audit

The enabled `ISQGR Автоисследование` task remains scheduled hourly with anti-duplicate and anti-idle rules, explicit separation of scientific/infra failures, and the constitutional claim locks. Its previous recovery snapshot became stale because the last auto cycle completed before the topology run reached terminal state; this was a timing race, not a disabled or broken automation. Recovery files are being synchronized to the terminal results above so the next cycle starts from the correct frontier.

## Claim lock

Candidate-theory construction remains `0% / UNFORMED`. No result above authorizes `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, `NEW_QG_THEORY_REQUIRED`, `ALL_KNOWN_SCHOOLS_FAIL`, RQIR promotion or KMQGB promotion.
