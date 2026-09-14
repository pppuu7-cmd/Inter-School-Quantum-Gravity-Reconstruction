# ITER083A adversarial review — graph↔continuum Laplacian normalization

Date: 2026-09-15
Source-authority commit: `5e483a012d71a797c8da2092f2ad466ecda9343e`

## Strongest rescue attempts

### Rescue 1 — promote the regular-lattice formula directly

Argument: because `1804.02294` exhibits a lattice Laplacian approximation with an explicit `1/a^2` factor, simply define `lambda_phys = lambda_graph/a^2` for CDT slices.

Rejection: the displayed calibration is a regular one-dimensional hypercubic example. The measured CDT operator is the unweighted Laplacian `4I-A` on irregular dual graphs of tetrahedral complexes. The frozen stack does not derive the geometric finite-volume/DEC weights or multiplicative coefficient needed to turn this particular graph operator into the continuum ADM Laplacian. Dimensional correctness is not source-defined normalization.

### Rescue 2 — use equilateral tetrahedra to fix the constant by geometry

Argument: every spatial tetrahedron has fixed edge length `a`, so the dual-link geometry should determine a universal conversion constant.

Rejection: this is a promising successor calculation, but it is not contained in the frozen source authority. Moreover, the unweighted adjacency Laplacian is not automatically identical to a barycentric/circumcentric finite-volume Laplacian. A derivation must specify primal/dual volumes, dual-edge lengths, field inner product and continuum convergence before a coefficient is authorized.

### Rescue 3 — treat critical eigenvalue scaling as the missing continuum map

Argument: the low eigenvalues scale to zero with a common critical exponent near `C_b-C_dS`, so they define the physical lattice spacing and hence the crosswalk.

Rejection: the sources themselves distinguish thermodynamic extrapolation and candidate critical behavior from an established `a -> 0` continuum limit. A relative running scale does not determine an absolute graph↔continuum operator normalization or identify the FRG cutoff `k`.

### Rescue 4 — define `k^2` by the lowest CDT eigenvalue

Argument: FRG suppresses modes near `k^2`, so choose `k^2=lambda_CDT` (possibly times a constant).

Rejection: that constant is exactly the missing normalization. Choosing it from target agreement would violate the preregistered no-target-fit control.

## Adversarial verdict

No rescue supports `PASS_SCOPED_SOURCE_DEFINED_GRAPH_CONTINUUM_NORMALIZATION`.

The strongest defensible classification remains:

**`PASS_SCOPED_PARTIAL_NORMALIZATION_CONTINUUM_MATCH_OPEN`**.

The positive content is real: operator domains, dimension, lattice-spacing role, thermodynamic scaling and a continuum spatial operator are all present. The missing item is narrow and mathematical: the exact normalization/convergence map for the CDT unweighted dual-graph operator.

Bridge credit: **0**.
