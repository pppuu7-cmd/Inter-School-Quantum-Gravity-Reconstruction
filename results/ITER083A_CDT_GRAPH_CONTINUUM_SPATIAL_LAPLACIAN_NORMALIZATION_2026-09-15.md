# ITER083A terminal result — CDT graph ↔ continuum spatial-Laplacian normalization

Date: 2026-09-15
Gate: `ITER083A_CDT_GRAPH_TO_CONTINUUM_SPATIAL_LAPLACIAN_NORMALIZATION_AUTHORITY`
Preregistration: `d6fcecc6a5f73eb00136ae0c55bf263218dcd489`
Production head: `0658e7558c44faad658db1ead4d4ce941dfef496`
Authoritative run: `34901855352`
Source authority: `5e483a012d71a797c8da2092f2ad466ecda9343e`
Adversarial review: `006c83dc65ebb9e34be1b47480a1a8cfa1fd4c0c`
Aggregate artifact: `10370612949`, digest `sha256:9ac88321745a2c47cd382c89c1191ee6b565e6105d3aa7b727026aa22e1f5c2d`

## Terminal classification

**`PASS_SCOPED_PARTIAL_NORMALIZATION_CONTINUUM_MATCH_OPEN`**

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Result

The frozen CDT sources explicitly define the measured spatial dual-graph Laplacian `L=4I-A`, identify the spacelike edge length `a` as the lattice spacing, and support inverse-length-squared interpretation and nontrivial critical scaling of low eigenvalues. A regular-lattice example makes the expected `1/a^2` dimensional scaling explicit.

This is stronger than ITER082's bare operator-type match. Nevertheless, the exact multiplicative conversion for the **actual unweighted CDT dual-graph Laplacian** to the continuum ADM spatial Laplacian is not derived. The sources also do not establish an `a -> 0` continuum normalization at the measured critical line. Therefore `lambda_graph/a^2` remains a scoped candidate form, not an authorized numerical `lambda_CDT -> k^2` map.

## Predicate summary

- discrete CDT operator normalization: **PASS**;
- continuum spatial operator normalization: **PASS_SCOPED**;
- role of lattice spacing `a`: **PASS_SCOPED**;
- finite-volume/thermodynamic scaling: **PASS_SCOPED**;
- continuum `a -> 0` normalization: **OPEN**;
- exact eigenvalue conversion coefficient: **OPEN / NOT SOURCE-DERIVED**;
- no target fit: **PASS_CONTROL**;
- no post-hoc mode selection: **PASS_CONTROL**.

## What changed

ITER082's blocker `NO_GRAPH_CONTINUUM_NORMALIZATION_AUTHORITY` is narrowed. It is no longer accurate to say that the CDT stack contains no normalization information at all. It contains a source-defined discrete operator, a lattice-spacing scale and inverse-square dimensional semantics.

The remaining blocker is specifically the **geometric/discretization coefficient and convergence map** from the unweighted tetrahedral dual graph to the continuum spatial Laplace-Beltrami operator.

## Claim ceiling

No direct `lambda_CDT = k^2`, no independently normalized FRG cutoff, no shared fixed point, no full theory equivalence, no bridge derivation and no candidate theory follow.

## Highest-information successor

Prospectively test whether a source-qualified finite-volume / discrete-exterior-calculus / barycentric-dual construction on equilateral tetrahedral complexes derives the missing coefficient and shows when the unweighted graph Laplacian is or is not proportional to the continuum Laplacian. Any such derivation must be independent of FRG target values.
