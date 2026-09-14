# ITER084 source authority — CDT cell-centred TPFA ↔ dual-graph Laplacian normalization

Date: 2026-09-15
Gate: `ITER084_CDT_CELL_CENTERED_TPFA_GRAPH_LAPLACIAN_NORMALIZATION`
Preregistration: `68138f796c29d2bd7035d12083b8a8d53b593519`
Workflow launch: `74d08a37425cd5b982699ad3c3b3e07039cd8dab`

## Source-qualified input

### CDT operator and geometry

arXiv `1804.02294`, Sec. III, states that CDT spatial slices can be faithfully represented by dual undirected **unweighted** graphs because all spatial tetrahedra have spacelike edge length `a` and the distance between centres of adjacent tetrahedra is the same. The graph vertices are tetrahedra and graph edges are tetrahedron adjacencies. It defines

`L_graph = D - A`,

and, because every spatial tetrahedron has four neighbours,

`L_graph = 4 I - A`.

The same source defines `a` as the spacelike lattice spacing and explicitly uses the positive sign convention in which the graph matrix approximates `-Delta` in its regular-lattice example.

### Cell-centred finite-volume authority

Eymard-Gallouët-Herbin, arXiv `math/0505109` / IMA J. Numer. Anal. 26 (2006), Definition 2.1, treats arbitrary dimension `d`, defines cell unknowns at points `x_K`, and requires the line between adjacent cell centres to be orthogonal to their common face. For an interior face `sigma=K|L` it defines the transmissibility

`tau_sigma = m(sigma) / d_KL`,

where `m(sigma)` is the face measure and `d_KL` is the centre-to-centre distance. Its discrete bilinear form contains `tau_sigma (u_L-u_K)(v_L-v_K)`, and the finite-volume scheme converges on the stated Euclidean admissible-mesh class as mesh size tends to zero.

The 2000 Handbook chapter is the underlying classical TPFA authority cited by this source.

### Tetrahedral-Laplacian distinction control

Alexa-Herholz-Kohlbrenner-Sorkine-Hornung (2020), DOI `10.1111/cgf.14068`, shows explicitly that tetrahedral discrete Laplacians are not unique: primal and circumcentric-dual vertex constructions differ in three dimensions. This prevents importing a vertex-DEC/FEM coefficient into the CDT cell-centred operator.

## Exact target-independent derivation

For a regular tetrahedron of side length `a`:

- triangular face area:
  `A_f = (sqrt(3)/4) a^2`;
- tetrahedron volume:
  `V_t = a^3/(6 sqrt(2)) = (sqrt(2)/12) a^3`;
- inradius / centre-to-face distance:
  `r = (sqrt(6)/12) a`.

Two adjacent equilateral tetrahedra glued across a face can be locally unfolded across that face. Their centres lie on the common normal, one on each side, hence

`d_KL = 2 r = (sqrt(6)/6) a = a/sqrt(6)`.

Thus the Eymard-Gallouët-Herbin interior-face transmissibility is constant on every spatial dual edge:

`tau = A_f / d_KL`

`    = [(sqrt(3)/4)a^2] / [a/sqrt(6)]`

`    = (3 sqrt(2)/4) a`.

For the isotropic positive Laplace operator `-Delta`, the cell balance divided by the control-volume measure is

`(-Delta_FV u)_K = (1/V_t) sum_{L~K} tau (u_K-u_L)`.

Since every CDT spatial tetrahedron has exactly four neighbours and all `tau` and `V_t` are equal,

`(-Delta_FV u)_K = [tau/V_t] [4u_K - sum_{L~K}u_L]`.

The coefficient is

`tau/V_t = [(3 sqrt(2)/4)a] / [a^3/(6 sqrt(2))] = 9/a^2`.

Therefore

**`-Delta_FV = (9/a^2) L_graph = (9/a^2)(4I-A)`**

for the frozen cell-centred TPFA discretization on equilateral CDT spatial tetrahedra.

Equivalently, at finite regulator and within this discretization,

**`lambda_FV = (9/a^2) lambda_graph`**.

No FRG quantity and no target observable enters this derivation.

## Predicate adjudication

- A — CDT domain and `4I-A`: **PASS**.
- B — equilateral tetrahedral geometry fixed by `a`: **PASS**.
- C — TPFA orthogonality across each common face: **PASS_SCOPED_LOCAL** after local unfolding; regular tetrahedron centre = incenter = circumcenter = barycenter and adjacent centres lie on the face normal.
- D — source-defined transmissibility and cell-centred FV normalization: **PASS**.
- E — unique target-independent coefficient: **PASS**, `c(a)=9/a^2`.
- F — sign convention: **PASS**, positive graph Laplacian corresponds to `-Delta`.
- G — CDT quantum/continuum convergence: **OPEN**. The Euclidean admissible-mesh convergence theorem does not establish convergence of an ensemble of fluctuating piecewise-flat CDT manifolds to a smooth continuum Laplace-Beltrami operator.
- H — FRG independence: **PASS_CONTROL**.

## Frozen controls

- `CELL_VERTEX_OPERATOR_SWAP_CONTROL`: **PASS**. No vertex DEC/FEM tetrahedral coefficient was used.
- `MASS_VOLUME_ERASURE_CONTROL`: **PASS**. The `1/V_t` factor is essential; omitting it would give the wrong dimensions and coefficient.
- `ORTHOGONALITY_CONTROL`: **PASS_SCOPED_LOCAL**. The two-cell equilateral patch is orthogonal after intrinsic unfolding.
- `CURVED_MANIFOLD_CONVERGENCE_CONTROL`: **PASS**. Local normalization is not promoted to a CDT continuum theorem.
- `EQUILATERAL_CONTROL`: **PASS**. The factor `9` is restricted to the frozen regular spatial tetrahedra.
- `SIGN_CONTROL`: **PASS**.
- `TARGET_FIT_CONTROL`: **PASS**. The coefficient was derived before and independently of any FRG/CDT spectral target.

## Source classification

**`PASS_SCOPED_EXACT_LOCAL_TPFA_COEFFICIENT_CONTINUUM_CONVERGENCE_OPEN`**

This resolves the narrow finite-regulator geometric coefficient left open by ITER083A under the source-qualified cell-centred TPFA interpretation. It does **not** prove the CDT continuum limit or authorize `lambda_CDT = k^2` in FRG.

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**.
