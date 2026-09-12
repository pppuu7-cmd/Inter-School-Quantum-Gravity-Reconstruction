# ITER006 — Eq.(29) immutable-source dependency gate terminal PARTIAL

Date: 2026-09-12

## Frozen gate

Preregistration: `status/ITERATION_006_RC006_EQ29_GEOMETRY_INCIDENCE_RPLACEMENT.md`  
Prereg commit: `4d48152cc183877ea0af5bfd20a0dc4dade43234`  
Implementation commit: `be3615fb36f4c1863b221b86fcf80d7cf4f11125`  
Administrative trigger commit / authoritative head: `9729cef2573778a3b48f6b80b42c6d5fd721366b`  
Run: `34718554940`

Immutable Eq.(29) EPRL block SHA256: `4f505657a580216d176c1c63ec92f5614dc73e8113294722a854d5a350b67083`.

## Terminal artifacts and jobs

- geometry job `103620066552`; artifact `10306086345`; digest `sha256:0bbd669a1f3b137c9f88d374e4ed87ec8d9b969ae676dd92aa5dec5c95d8ed27`;
- incidence job `103620066468`; artifact `10305437790`; digest `sha256:b02efc00fa45d8d6ed247f650e71322d89b1fb99efcd88740e09e5db08477af2`;
- R-placement job `103620066580`; artifact `10305516543`; digest `sha256:2cb8e85f8adc35884bc8186474639b3284eeec39d0791a71e20f25c577eeabb6`;
- aggregate job `103620177874`; summary artifact `10305491683`; digest `sha256:ca82d129681a540d7b0daa618b43b831957e2001a527e1556ea0852c8387ada8`.

All four jobs completed computationally successfully. Green CI is not the scientific classification.

## Frozen scientific classification

Aggregate: `EQ29_SOURCE_DEPENDENCIES_PARTIAL`.

Lane results:

1. **Geometry — PASS:** `SOURCE_LABEL_GEOMETRY_QUALIFIED`. The immutable block contains all frozen labels `J^-`, `J^+`, `l`, `j^-_1`, `j^+_1`, `j^-_2`, `j^+_2`, `l_1`, `l_2`; missing set is empty.
2. **Source-level incidence — PASS:** `SOURCE_PATH_INCIDENCE_QUALIFIED`. A nonempty TikZ path record is machine-extractable and all frozen structural labels are associated with source-level path/node occurrences; missing association set is empty. No raster/proximity inference was used.
3. **R-placement — FAIL/BLOCKED:** `SOURCE_R_PLACEMENT_NOT_MACHINE_QUALIFIED`. The pinned source explicitly contains R-matrix, inverse-R and crossing semantics before the EPRL subsection, but the frozen gate found no R/crossing token inside the EPRL subsection itself and therefore no deterministic Eq.(29)-specific source link. `deterministic_eprl_eq29_link=false`.

This is a scientific/source-authority PARTIAL result, not an infrastructure or numerical failure.

## Interpretation locks

- Geometry and path-incidence dependencies are now source-qualified for the immutable Eq.(29) block.
- R/inverse-R placement remains BLOCKED.
- `eq29_amplitude_authorized=false`.
- bridge credit remains `0`.
- No threshold, lexical criterion or selector from the failed R-placement lane may be weakened after the result.
- Earlier `MIXED_SOURCE_RELATION_QUALIFICATION_6_OF_8` remains preserved; the old failed crossing lexical threshold is not rerun with easier patterns.

A distinct prospectively frozen **TeX structural reference-topology** audit is admissible because the earlier durable result explicitly identified label/reference topology as a new source-structure object. It must use exact TeX labels/refs/section containment rather than easier lexical matching and cannot modify this PARTIAL verdict.

Candidate theory remains `0% / UNFORMED`; `BRIDGE_DERIVED` and all stronger claim locks remain forbidden.
