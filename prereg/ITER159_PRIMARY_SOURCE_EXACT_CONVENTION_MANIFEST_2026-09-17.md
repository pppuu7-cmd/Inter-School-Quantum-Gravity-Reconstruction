# ITER159 preregistration — primary-source exact convention manifest

Date: 2026-09-17
Parent: ITER158 terminal `BLOCKED_SCOPED_ITER158_PRIMARY_SOURCE_CONVENTION_MAP_INCOMPLETE`, run 35183584814.

## Objective
Acquire the exact arXiv v2 source package for arXiv:1706.01891 (Fröb, CQG 35 035005, DOI 10.1088/1361-6382/aa9ad1) and extract source-level evidence needed to decide whether it is translatable to the frozen ITER118 endpoint object. This is a convention/source gate, not a coefficient gate.

## Frozen required fields
Before any source coefficient can be authority, persist source evidence for: metric signature; metric perturbation normalization; gauge/gauge parameters; Riemann and Ricci sign conventions; Fourier convention if used; dimensional-regularization convention and epsilon definition; loop/integration normalization; geodesic affine parameter and endpoint orientation; tangent normalization; geodesic embedding perturbation normalization; endpoint/boundary prescription; relevant symmetry factors; observable/field content; and the exact map (or explicit non-map) to repository conventions.

## Frozen source identity
Primary source: arXiv:1706.01891v2. Download the source archive, persist SHA256, inventory TeX files with SHA256, and emit bounded source excerpts around convention-bearing patterns. No secondary source may supply a missing convention.

## Scientific firewall
The source computes a scalar matter two-point function at fixed fluctuating geodesic distance, not the frozen curvature-composite first-M/G endpoint amplitudes. Therefore even a complete convention manifest is only `REFERENCE_TRANSLATABLE` unless exact topology/operator equivalence is separately demonstrated. Do not import scalar-matter coefficients into ITER118 endpoint coefficients.

## Terminal classes
`PASS_SCOPED_ITER159_EXACT_SOURCE_CONVENTION_MANIFEST_COMPLETE_REFERENCE_ONLY` iff all required source conventions are either explicitly sourced or mathematically derived from explicit source definitions with provenance, while operator/topology mismatch remains recorded.

`BLOCKED_SCOPED_ITER159_SOURCE_CONVENTION_MANIFEST_INCOMPLETE_<FIELD>` iff at least one required convention cannot be source-faithfully fixed. Name the earliest missing field.

`INVALID_ITER159` for source-version mismatch, evidence fabrication, post-outcome relaxation, or use of secondary-source conventions as primary authority.

Green CI is not scientific PASS. No rank/coefficient solve is authorized by ITER159. `B1_total=UNAUTHORIZED`; `BRIDGE_DERIVED=false`; `NEW_PHYSICS_FOUND=false`; candidate theory remains `UNFORMED / 0%`.