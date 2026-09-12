# ITERATION 006 — RC006 decorated-index leg-order identifiability

Date: 2026-09-12

## Provenance

Prospective computation commit: `d097288896a28c39984c6f45ad5aa1fe30a2c1a9`  
Workflow/head: `79820bd595f6b1c34655314692c4b55fe63ce907`  
Authoritative run: `34700094892`  
Global-identifiability job: `103570205823`  
Global artifact: `10299837254`  
Global digest: `sha256:6b334780f812b2c9d90ea23374d48a38a0ffcfbfd8b4cc0b00eea5105ba87e44`  
Aggregate job: `103570231207`  
Aggregate artifact: `10300465880`  
Aggregate digest: `sha256:0e16e0018951d5877d5a8ba0da99b78a492cd2ef7b9b0aeb28b547f53aef66b8`

The gate was frozen before viewing results. It uses only decorated source indices from the qualified exact math/diagram blocks, never rendered-picture geometry. Computation validity and scientific identifiability were separated prospectively: green CI cannot count as identifiability PASS.

## Raw result

All seven computation lanes were valid and completed successfully. The global lane extracted `34` decorated symbols across eight qualified source anchors, then assigned each decorated symbol an exact source-incidence fingerprint.

The scientific result is **FAIL**:

`SCIENTIFIC_FAIL_SOURCE_INCIDENCE_NONIDENTIFIABLE`.

`source_incidence_unique = false` with `11` interchangeable same-base groups. Examples include:

- `J^+` / `J^-`;
- `j^+` / `j^-`;
- `j^+_1`, `j^+_2`, `j^-_1`, `j^-_2`;
- `j^+_3`, `j^+_4`, `j^-_3`, `j^-_4`;
- `j_1` / `j_2`;
- `j_i^+` / `j_i^-`;
- `l_1` / `l_2`;
- `l_3` / `l_4`;
- `m^+` / `m^-`;
- `m_1` / `m_2`;
- `n^+` / `n^-`.

The product of the surviving within-fingerprint permutation factors gives a lower bound `log10(surviving relabelings) = 5.469692444399043`, i.e. at least about `2.95e5` source-incidence-preserving relabelings under this abstraction.

## Scientific classification

`VALID_COMPUTATION / SCIENTIFIC_FAIL_SOURCE_INCIDENCE_NONIDENTIFIABLE / EQ29_NUMERICAL_AMPLITUDE_REMAINS_BLOCKED`.

This is not an infrastructure or numerical failure. The source contains substantial decorated-leg information, but occurrence-count incidence across the qualified anchor blocks is insufficient to identify a unique oriented/braided Eq.(29) leg ordering. The negative result is preserved; no convention or geometry-based tie breaker will be inserted after the fact.

The result also does not prove that the published source lacks enough authority in principle. It rejects this specific source-incidence abstraction. A stricter prospective object based on ordered local source neighborhoods/adjacency of decorated indices may still distinguish some of the surviving relabelings without using rendered geometry.

## Consequence

- `RC006_EQ29_ORIENTED_BRAIDED_GRAPH_MAPPING_GATE`: **OPEN/BLOCKED**.
- `RC006_EQ29_MINIMAL_K12_AMPLITUDE_GATE`: **BLOCKED**.
- Appendix-C SVD and held-out selector transport remain blocked downstream.
- No Eq.(29) numerical amplitude is authorized from this result.

## Next allowed gate

Prospectively test ordered decorated-index source neighborhoods (predecessor/successor and relative-order fingerprints) on the same qualified source blocks. The gate must preserve non-identifiability whenever multiple same-base decorated symbols retain identical ordered-context fingerprints. Only a source-unique ordering object may advance toward a contraction-ready mapping.

## Claim locks

No `BRIDGE_DERIVED`, continuum result, new physics, candidate theory, RQIR/KMQGB promotion, or all-schools-fail claim follows.
