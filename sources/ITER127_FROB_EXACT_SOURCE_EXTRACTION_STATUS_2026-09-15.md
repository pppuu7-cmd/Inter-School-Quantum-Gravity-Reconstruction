# ITER127 exact-source extraction status — Fröb fixed-geodesic chi1/chi2 authority

Date: 2026-09-15
Active gate: `ITER127_FIXED_GEODESIC_CHI1_CHI2_PROJECTED_SINGULAR_STRATA_AUTHORITY`
Preregistration: `prereg/ITER127_FIXED_GEODESIC_CHI1_CHI2_PROJECTED_SINGULAR_STRATA_AUTHORITY_2026-09-15.md`
Extractor: `analysis/iter127_extract_frob_geodesic_kernels.py`
Workflow: `.github/workflows/iter127_frob_geodesic_kernel_authority.yml`
Artifact: `iter127-frob-geodesic-kernel-authority`

## Transport status

**SOURCE EXTRACTION COMPLETED / SCIENTIFIC INTERPRETATION PENDING.**

The workflow successfully:

- downloaded the exact current arXiv source package for `1706.01891`;
- preserved the archive SHA256 inside the artifact;
- recursively inventoried TeX source files with SHA256 hashes;
- located short equation environments containing the geodesic `chi` notation and line integrals;
- emitted equation-only evidence with file/line locations;
- asserted that the selected evidence contains both `chi`-sensitive and integral-sensitive equations.

## Why the gate is not terminal yet

The next scientific step is to read the extracted first-/second-order geodesic equations and map their exact affine polynomial weights, nested integration domains and initial-tangent terms into the ITER126 endpoint/coincidence subtraction table.

That interpretation has not yet been frozen in a source-authority result. In particular, no coefficient reconstructed merely from the generic geodesic equation or from memory is being substituted for the exact source formula.

## Current claim ceiling

No `chi_1/chi_2` weight table is yet claimed complete. No curvature pole residue, `B_1`, noncancellation result, EDT fit, bridge, new physics or candidate theory follows from the successful source extraction alone.

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.
