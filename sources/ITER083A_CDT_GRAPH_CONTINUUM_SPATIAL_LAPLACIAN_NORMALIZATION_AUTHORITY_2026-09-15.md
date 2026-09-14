# ITER083A source authority — CDT graph ↔ continuum spatial-Laplacian normalization

Date: 2026-09-15
Gate: `ITER083A_CDT_GRAPH_TO_CONTINUUM_SPATIAL_LAPLACIAN_NORMALIZATION_AUTHORITY`
Preregistration: `d6fcecc6a5f73eb00136ae0c55bf263218dcd489`
Production head: `0658e7558c44faad658db1ead4d4ce941dfef496`
Authoritative run: `34901855352`
Aggregate artifact: `10370612949`, digest `sha256:9ac88321745a2c47cd382c89c1191ee6b565e6105d3aa7b727026aa22e1f5c2d`

Frozen exact-PDF artifacts:
- `1804.02294`: artifact `10371331828`, digest `sha256:1086e8fc87b137cb4fa0e6c20aa59e7515d7a7ee162165c7f68106eebc5cffe8`.
- `1903.00430`: artifact `10370692535`, digest `sha256:8ae639b95195ed778f1e02f25ded81ed835860d0abc6964954f7cfd517381c4f`.
- `1912.11311`: artifact `10370982926`, digest `sha256:8cb79646913bc41f36e7bb0986ee47e82258eac5fe4e07c4e5d5b73518b18e12`.
- `2306.10408`: artifact `10371346599`, digest `sha256:1b57f9f09d7a94e41b0cda5438b53d09dbcd0be970b6548ead5cc4b3b716a531`.

## Equation-level findings

### 1. CDT discrete operator is explicit, but dimensionless

`1804.02294` defines the spatial-slice dual graph and the graph Laplacian

`L = D - A`,

with `L = 4 I - A` on the 4-regular dual graph of a CDT spatial slice. The algebra is the real-valued functions on dual vertices. This fixes the discrete domain and the numerical normalization used in the measurements.

The same source gives a one-dimensional hypercubic calibration example in which the combinatorial difference operator approximates the continuum Laplace operator with an explicit `1/a^2` factor. This is valid evidence for inverse-length-squared scaling of low graph eigenvalues under a controlled regular-lattice approximation. It is not an exact derivation of the physical normalization of the unweighted dual-graph operator on arbitrary CDT spatial triangulations.

### 2. The CDT sources retain the lattice-spacing issue rather than solving it

`1804.02294` states that the elementary spacelike edge length `a` is the lattice spacing and that the discretization must become irrelevant in a continuum limit. Its spectral scales are reported in units of the elementary lattice spacing / tetrahedron size.

`1903.00430` and `1912.11311` use the same dimensionless dual-graph operator and explicitly interpret the low eigenvalues on dimensional grounds as inverse squared length scales. They perform `V_S -> infinity` thermodynamic extrapolations and find common critical scaling of low eigenvalues near the candidate `C_b-C_dS` transition.

Crucially, these papers distinguish this evidence from an established continuum normalization. They do not derive a universal multiplicative conversion from a dimensionless eigenvalue of `4I-A` to an eigenvalue of a continuum spatial Laplace-Beltrami operator. The thermodynamic limit is not promoted to `a -> 0`, and the critical behavior is not itself an operational calibration of `a`.

### 3. Foliated FRG supplies a continuum spatial momentum operator, not the lattice matching constant

`2306.10408` formulates FRG flow on foliated spacetimes in ADM variables. Its coarse-graining scale `k` has momentum dimension and its regulator is built from continuum kinetic/momentum operators. The frozen source therefore supplies the continuum side needed by ITER082/083A.

It does not contain a derivation mapping the CDT unweighted dual graph to that continuum operator, nor a coefficient converting CDT graph eigenvalues to `k^2`. The existence of a spatial regulator operator is a type match, not a lattice normalization theorem.

## Predicate adjudication

- Explicit CDT discrete Laplacian normalization: **PASS** — `L=4I-A` is source-defined.
- Explicit continuum spatial-Laplacian / momentum normalization on the FRG side: **PASS_SCOPED**.
- Source-defined role of CDT lattice spacing `a`: **PASS_SCOPED** — `a` is the spacelike edge cutoff and inverse-square scaling is source-motivated.
- Controlled finite-volume scaling: **PASS_SCOPED** — thermodynamic extrapolations are explicit.
- Controlled continuum `a -> 0` normalization: **OPEN**.
- Exact graph-eigenvalue → continuum-eigenvalue conversion rule for the measured CDT operator: **NOT ESTABLISHED**.
- Target-fitted proportionality: **FORBIDDEN / NOT USED**.
- Post-hoc mode selection: **FORBIDDEN / NOT USED**.

## Controls

- `GRAPH_COMBINATORIAL_TO_PHYSICAL_CONTROL`: passed. Dimensionless graph eigenvalues are not silently treated as physical eigenvalues.
- `LAMBDA_OVER_A2_CONTROL`: passed. `lambda_graph/a^2` is retained as a dimensional/regular-lattice candidate, not promoted to an exact CDT↔ADM map.
- `THERMODYNAMIC_CONTINUUM_SWAP_CONTROL`: passed. `V_S -> infinity` is not identified with `a -> 0`.
- `PHASE_CRITICAL_TO_FRG_K_CONTROL`: passed. CDT critical scaling is not identified with FRG `k`.
- `ADM_OPERATOR_EXISTENCE_CONTROL`: passed. The FRG spatial operator does not supply the missing graph normalization by itself.

## Source classification

**`PASS_SCOPED_PARTIAL_NORMALIZATION_CONTINUUM_MATCH_OPEN`**

The frozen stack establishes the operator types, the discrete normalization actually used, the lattice-spacing dimension, and nontrivial thermodynamic/critical scaling. It does not establish the exact multiplicative graph↔continuum normalization or an operational `lambda_CDT -> k^2` rule.

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**.
