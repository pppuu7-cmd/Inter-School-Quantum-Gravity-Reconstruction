# ITER084 preregistration — CDT cell-centred TPFA ↔ dual-graph Laplacian normalization

Date: 2026-09-15
Gate: `ITER084_CDT_CELL_CENTERED_TPFA_GRAPH_LAPLACIAN_NORMALIZATION`

## Motivation frozen before coefficient derivation

ITER083A established partial normalization authority for the CDT spatial dual-graph Laplacian `L=4I-A`, but left the geometric coefficient relating this dimensionless operator to a continuum-normalized spatial diffusion/Laplace operator open.

The measured CDT scalar field is naturally a function on dual vertices, i.e. on spatial tetrahedra. Therefore a cell-centred finite-volume / two-point-flux approximation (TPFA), not a vertex-based tetrahedral DEC/FEM Laplacian, is the most direct independent candidate for fixing the missing coefficient.

No FRG eigenvalue, cutoff, trajectory, target spectrum or CDT critical fit may be used to determine the coefficient.

## Frozen sources

- arXiv `1804.02294` — CDT spatial dual-graph Laplacian and equilateral spatial-tetrahedron geometry/lattice-spacing semantics.
- R. Eymard, T. Gallouët, R. Herbin, *Finite Volume Methods*, Handbook of Numerical Analysis VII (2000), DOI `10.1016/S1570-8659(00)07005-8` — admissible orthogonal cell-centred meshes, face transmissibility and TPFA normalization.
- R. Eymard, T. Gallouët, R. Herbin, *A cell-centred finite-volume approximation for anisotropic diffusion operators on unstructured meshes in any space dimension*, IMA J. Numer. Anal. 26 (2006), DOI `10.1093/imanum/dri036` — orthogonality and convergence authority in arbitrary dimension.
- M. Alexa, P. Herholz, M. Kohlbrenner, O. Sorkine-Hornung, *Properties of Laplace Operators for Tetrahedral Meshes*, Comput. Graph. Forum 39 (2020), DOI `10.1111/cgf.14068` — control source showing that tetrahedral discrete Laplacians are not unique and that vertex-based primal/dual constructions must not be substituted for the CDT cell-centred operator.

## Frozen question

When the CDT spatial triangulation is treated as a cell-centred finite-volume mesh whose cells are equilateral tetrahedra of spacelike edge length `a`, does source-qualified TPFA geometry imply an exact local relation

`(-Delta)_FV = c(a) (4I-A)`

for scalar values at tetrahedron centres? If yes, what is `c(a)` and which assumptions are required? Separately, does the frozen authority establish convergence of this finite-regulator piecewise-flat operator to the continuum Laplace-Beltrami operator in the CDT continuum limit, or only the local discretization normalization?

## Required predicates

A. The CDT source explicitly fixes the measured operator domain and matrix `L=4I-A` on the 4-regular dual graph.

B. For an equilateral spatial tetrahedron, the face area, cell volume, centre-to-face distance and neighbouring-centre distance are fixed geometrically from `a` without fitted parameters.

C. Adjacent CDT tetrahedron centres satisfy the TPFA orthogonality/admissibility condition across their common triangular face after local unfolding.

D. The finite-volume source explicitly defines face transmissibility as face measure divided by centre distance (or an equivalent source-defined formula) and the cell-normalized discrete diffusion/Laplace operator.

E. Substituting the equilateral CDT geometry yields a unique coefficient `c(a)` multiplying `4I-A`; the derivation must be algebraic and target-independent.

F. The sign convention is explicit: the positive graph Laplacian is compared to `-Delta`, not silently to the opposite convention.

G. Local finite-volume normalization is kept distinct from a theorem that the random CDT sequence converges to a smooth continuum Laplace-Beltrami operator as `a -> 0`.

H. No FRG quantity enters A-G. Any later `lambda_phys <-> k^2` comparison requires a separate gate.

## Frozen controls

- `CELL_VERTEX_OPERATOR_SWAP_CONTROL`: CDT cell-centred `4I-A` cannot be replaced by a vertex DEC/FEM tetrahedral Laplacian.
- `MASS_VOLUME_ERASURE_CONTROL`: face transmissibility alone is insufficient; division by the tetrahedron control-volume measure must be retained.
- `ORTHOGONALITY_CONTROL`: a two-point flux formula is not authorized unless adjacent cell centres connect orthogonally to the common face in the locally unfolded geometry.
- `CURVED_MANIFOLD_CONVERGENCE_CONTROL`: Euclidean-domain TPFA convergence does not by itself prove the CDT quantum/continuum Laplace-Beltrami limit.
- `EQUILATERAL_CONTROL`: any exact constant derived from regular tetrahedra cannot be generalized to arbitrary distorted tetrahedral meshes.
- `SIGN_CONTROL`: `L_graph` is positive semidefinite and must correspond to `-Delta` under the chosen convention.
- `TARGET_FIT_CONTROL`: no constant may be fitted to FRG, spectral-dimension, de-Sitter, or critical-eigenvalue data.

## Frozen classifications

- `PASS_SCOPED_EXACT_LOCAL_TPFA_COEFFICIENT_CONTINUUM_CONVERGENCE_OPEN` if A-F pass with a unique source-derived coefficient while G remains unproven at CDT continuum-theory level.
- `PASS_SCOPED_FV_PROPORTIONALITY_EXTRA_ASSUMPTION_REQUIRED` if proportionality is derivable only after an additional geometric/discretization assumption not fixed by the CDT source.
- `FAIL_SCOPED_UNWEIGHTED_GRAPH_NOT_CELL_CENTERED_FV_NORMALIZED` if the source-qualified finite-volume stencil necessarily contains nonconstant weights incompatible with `4I-A` even for the frozen equilateral CDT geometry.
- `BLOCKED_SOURCE_AUTHORITY` if the frozen stack does not expose the required TPFA/operator formulas sufficiently to adjudicate.
- `INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION` only for source-transport/extraction failure.

## Claim ceiling

Even a PASS can establish only an exact finite-regulator local normalization of the CDT graph Laplacian under the frozen cell-centred TPFA interpretation. It cannot establish the CDT continuum limit, an FRG cutoff map, a shared UV fixed point, theory equivalence, `BRIDGE_DERIVED`, `UNIVERSAL_COMMON_PARENT_FOUND`, new physics or a candidate theory.

Predicates, controls and classifications are frozen before coefficient evaluation.
