# ITER084 adversarial review — CDT cell-centred TPFA normalization

Date: 2026-09-15
Preregistration: `68138f796c29d2bd7035d12083b8a8d53b593519`
Source authority: `6155de3f2aeeea12472fd2f560df64fe3d6ec760`

## Strongest attacks

### Attack 1 — the factor `9/a^2` is an arbitrary finite-volume convention

If the coefficient came only from choosing a particular control-volume rule, it would not close ITER083A.

**Result:** the factor survives an independent local Taylor test of the graph stencil. Let the four unit vectors from a tetrahedron centre to the centres of its four neighbours, after local face unfolding, be `n_i`. Tetrahedral symmetry gives

`sum_i n_i = 0`,

`sum_i n_i n_i^T = (4/3) I_3`.

The neighbour distance is `d=a/sqrt(6)`. For a smooth scalar field,

`sum_i f(x+d n_i) = 4 f(x) + (d^2/2) sum_i n_i^T H[f] n_i + ...`

`                 = 4 f(x) + (2 d^2/3) Delta f(x) + ...`.

Hence

`(4I-A)f = -(2 d^2/3) Delta f + ... = -(a^2/9) Delta f + ...`,

again yielding `-Delta = (9/a^2)(4I-A)` at leading local order. The TPFA coefficient is therefore not an isolated shape convention; it agrees with the isotropic second-moment normalization of the actual four-neighbour stencil.

### Attack 2 — use the naive dual-edge length and set the factor to `1/d^2 = 6/a^2`

**Rejected.** A four-direction tetrahedral stencil is not a Cartesian nearest-neighbour stencil. Its second directional moment is `(4/3)I`, which supplies the additional `3/2` shape factor. The finite-volume mass/face geometry encodes the same factor. `6/a^2` fails the isotropic Taylor consistency check.

### Attack 3 — vertex DEC/FEM on a tetrahedral mesh gives different weights, so the graph coefficient is not unique

**Rejected as a category swap.** The CDT observable is defined on dual vertices representing tetrahedral cells. The frozen gate is cell-centred. Alexa et al. correctly show that vertex-based tetrahedral Laplacians are nonunique in 3D, but that fact is a control against substitution, not a refutation of the cell-centred TPFA stencil.

### Attack 4 — the finite-volume mass matrix makes this a generalized eigenproblem, not a scalar multiple of `4I-A`

For a generic mesh this is serious. Here every spatial tetrahedron has the same volume `V_t`, so the cell mass matrix is exactly `V_t I`. Every shared face has the same area and every adjacent-centre distance is the same, so every transmissibility is the same. The generalized FV operator therefore collapses exactly to one scalar coefficient multiplying the unweighted graph Laplacian. No nonuniform mass or edge weights remain at the frozen regulator.

### Attack 5 — regular tetrahedra cannot tile flat Euclidean three-space, invalidating TPFA

This attack limits the **convergence claim**, not the local coefficient. A CDT slice is an intrinsically piecewise-flat simplicial manifold with curvature concentrated at lower-dimensional hinges. Any pair of adjacent tetrahedra can be unfolded isometrically across its common face; their centres lie on the face normal and the local flux geometry is well defined. Thus the finite-regulator local stencil is valid.

However, the Eymard-Gallouët-Herbin convergence theorem is stated for admissible meshes of Euclidean polygonal/polyhedral domains. It cannot be promoted without additional analysis to convergence of a fluctuating curved CDT ensemble to a smooth continuum Laplace-Beltrami operator. This is exactly why ITER084 retains `CONTINUUM_CONVERGENCE_OPEN`.

### Attack 6 — curvature hinges spoil the four-direction Taylor argument

The local Taylor argument is a consistency check, not a global convergence theorem. The four neighbour-centre geodesic segments cross the four faces away from lower-dimensional hinges and can be individually developed into the central tetrahedron's Euclidean tangent frame. The argument verifies the local coefficient under a smooth-field/continuum interpretation, but it does not erase Regge curvature or prove uniform convergence across an ensemble.

### Attack 7 — an arbitrary diffusion constant rescales the answer

A physical diffusion equation may contain an extra diffusivity `D`. The geometric Laplace-Beltrami operator itself corresponds to unit diffusivity. ITER084 normalizes the geometry operator, not a phenomenological diffusion constant. Multiplying the heat equation by an external `D` is a different observable convention and does not create ambiguity in the geometric coefficient.

## Verdict

The attacks do not overturn the finite-regulator normalization:

**`-Delta_FV = (9/a^2)(4I-A)`**

is independently supported by (i) source-qualified cell-centred TPFA geometry and (ii) the tetrahedral stencil second-moment calculation.

The attack that survives is global: source authority still does not prove the CDT `a -> 0` continuum spectral convergence theorem.

Therefore the terminal-strength classification remains

**`PASS_SCOPED_EXACT_LOCAL_TPFA_COEFFICIENT_CONTINUUM_CONVERGENCE_OPEN`**.

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**.
