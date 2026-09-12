# ITER006 DVD23 synthetic incidence gate audit — 2026-09-12

Run `34715884817` completed successfully and emitted classification `DVD23_STRUCTURAL_REFINEMENT_MAP_ADMISSIBLE`.

## Scientific audit

The workflow is computationally valid but **non-source-authoritative** for a DVD2→DVD3 refinement claim. The implementation in `experiments/dvd23_refinement_incidence_gate.py` declares its own minimal coarse and fine foams and constructs the fine object by splitting the single declared coarse internal edge `int01` into the path `int0m -> intm1`, while keeping the boundary labels identical. The passing predicates therefore verify consistency of that synthetic construction; they do not extract or prove an injective V/E/F incidence map from the pinned source `arXiv:1801.03771`.

Accordingly:

- classification for programme accounting: `SYNTHETIC_STRUCTURAL_SELF_CONSISTENCY_PASS_SOURCE_AUTHORITY_ABSENT`;
- bridge/refinement credit: **0**;
- cylindrical-consistency/amplitude permission: **not authorized**;
- this run does **not** override the earlier source-scoped direct DVD2↔DVD3 exclusion or the current requirement for explicit source-derived incidence preservation;
- no downstream amplitude identity may be launched from this run alone.

This audit is a claim-lock correction, not a negative result about whether some genuine source-derived refinement map exists.
