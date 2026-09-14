# ITER064 — RC008 crossing-convergence + global-measure manual audit

Date: 2026-09-14

## Terminal manual verdict

**INVALID SCIENTIFIC / DIAGNOSTIC INFERENCE — `RC008_CROSSING_ENDPOINT_NONCONVERGENCE_AND_GLOBAL_MEASURE_MAPPING_UNRESOLVED`**

This is **not** a scientific FAIL of RC008, EPRL-FK, or spin-foam refinement. It withdraws scientific credit from the ITER062B crossing reconstruction and diagnostic credit from the ITER064 crossing-stability claim until the numerical crossing endpoints and the glued-complex geometric measure are source-qualified and converged.

Candidate theory remains `UNFORMED / 0%`; bridge credit remains zero.

## Provenance consumed

### ITER062B

- prereg: `prereg/ITER062B_RC008_RESTRICTED_HYPERCUBOID_COARSE_FINE_NUMERICAL_RECONSTRUCTION_2026-09-14.md`
- production head: `3f4b1c89d5183cde99ae6f7cdfa9efe06ae6d829`
- authoritative run: `34874113741`
- aggregate job: `104077252124`
- aggregate artifact: `10359819990`
- digest: `sha256:fd62c82a618b6ded0e4ab0013610f00a33a70551e9d3f76ab1188d1c2f44493b`
- historical automated/manual report: `results/ITER062B_RC008_RESTRICTED_COARSE_FINE_NUMERICAL_RECONSTRUCTION_2026-09-14.md`

### ITER063

Preserved as terminal `INVALID_IMPLEMENTATION_OR_SELECTOR_SYMMETRY_FAIL`; no gate credit. Its failed P1/P2 selector controls motivated ITER064 and are not reinterpreted as physics.

### ITER064

- prereg commit: `aa2179c06bbbc3d54fbd917e1809e335839d30ed`
- production head: `be911ba4e7a847049f4882fbe615d0f25774b3ad`
- authoritative run: `34874915843`
- jobs: B2 `104079605838`, P1 `104079605579`, P2 `104079605734`, aggregate `104079838227`
- aggregate artifact: `10361141304`
- digest: `sha256:f248f9146222a411d04b3b74359650f89ff81ce77e9fcb5083cb3a5220376bf8`
- workflow aggregate classification: `DIAGNOSTIC_PASS_PERMUTATION_CROSSING_STABLE`

Green CI and the workflow classification are preserved as execution facts, but are not accepted as the terminal scientific interpretation for the reasons below.

## Finding 1 — the ITER062B primary crossing uses a non-converged endpoint

ITER062B declared B0 crossing `[0.50, 0.55]` and used that crossing to satisfy the primary reproduction predicate.

The authoritative aggregate itself records for B0 at `alpha=0.50`:

- `fine_ess = false`;
- `fine_level = false`;
- fine ESS fraction `4.6583628165555926e-05`, below the frozen `1e-4` threshold;
- coarse mean `0.40703564009776133`;
- fine mean `0.6732951088608872`;
- difference `+0.26625946876312584`.

At `alpha=0.55`, all frozen convergence checks pass and the difference is `-0.11953836164640588`.

The preregistration evaluated convergence only on the central subset `[0.55,0.60,0.65,0.70]`, while the crossing search was allowed to use the full panel. Consequently the aggregate could call `[0.50,0.55]` a robust crossing even though one of the two endpoints did not satisfy the gate's own ESS/level convergence diagnostics.

This is a preregistration/inference gap, not a physical result.

## Finding 2 — ITER064 high-statistics diagnostic does not close that gap

ITER064 increased statistics to eight frozen Sobol seeds and powers `2^16, 2^18`, but retained the same logical asymmetry: convergence is required only on `[0.55,0.60,0.65,0.70]`, whereas crossings may use `alpha=0.50`.

At `2^18`, all three B2/P1/P2 reported crossings `[0.50,0.55]`, but the authoritative aggregate records at `alpha=0.50`:

| boundary | D=fine-coarse | stderr | fine ESS check | fine CV check |
|---|---:|---:|---|---|
| B2 | `+1.7352397178352406` | `0.7108412841131606` | FAIL | FAIL |
| P1 | `+0.8688160701971994` | `0.6941321335609576` | FAIL | FAIL |
| P2 | `+1.3278633647616047` | `0.633022249103691` | FAIL | FAIL |

At `alpha=0.55`, all corresponding central convergence checks pass and all three differences are stably negative (`-1.383...`).

Thus ITER064 demonstrates that spatial permutation differences seen in ITER063 were sensitive to seed/statistics, but it **does not establish a numerically converged crossing**. The positive `alpha=0.50` endpoint remains outside the converged regime under the run's own diagnostics.

The workflow label `DIAGNOSTIC_PASS_PERMUTATION_CROSSING_STABLE` is therefore a mechanical contract outcome, not admissible evidence that the physical/source crossing is established.

## Finding 3 — glued-complex geometric measure was not source-instantiated

The source chain remains valid and valuable:

- arXiv:1508.07961v2 primary hypercuboid amplitude source, `QuantumCuboids_article.tex`, SHA256 `ba973b02a05688c2b122c95a111b70b0fe03a126fac399b073725574afc7358b`;
- arXiv:1701.02311v2 coarse-graining source, `QuantumCuboidsLong_article.tex`, SHA256 `78415347fa92b1d0bce1bbd4010faeb3cc939c5f5d6b14d72f340138e4c573ef`.

The latter explicitly states that the geometric-sector integration measure is obtained by restricting the Riemannian metric `ds^2 = sum_f dj_f^2` to the geometricity-constraint submanifold by pullback. Appendix `Sec:Appx:FadeevPopov` derives, **for one 4D hypercuboid**, the local factor

`Delta_FP = J / cos(theta)`, with `J = x y^2 z`,

and says that the general case can be inferred.

However `code/iter062b/reconstruct.py` implements the inference by adding `log_fp(x,y,z,t)` inside `local_parts` and then multiplying that factor independently for every local hypercuboid: two factors in the coarse two-hypercuboid integral and 32 factors in the fine `2x2x2x4` integral.

No machine-readable derivation in ITER062A/B shows that this product of local one-hypercuboid factors equals the pullback measure of the **glued**, shared-face, embedding-constrained complex. The source RG object itself contains shared fine face spins and area-sum constraints; after the geometric restriction it leaves one coarse integration variable and six fine variables. The global pullback/Jacobian for those reduced coordinates is therefore part of the scientific object and cannot be replaced by a local product by analogy.

A simple coarse-sector consistency check already exposes the issue: after fixed coarse area sums, the three timelike split areas are proportional to `(Y t, Z t, X t)`. Pulling back their Euclidean spin-space metric to the one-dimensional split coordinate gives a `t`-independent metric factor (up to fixed multiplicities/constants). In contrast, the implemented `Delta_FP(X,Y,Z,t) Delta_FP(X,Y,Z,2T-t)` is generally split-dependent. A complete incidence-aware derivation is therefore required before the product prescription can receive source authority.

This finding does not assert what the correct global factor must be for the full fine complex; it establishes that the current factorization was not source-qualified at the level required by the preregistration.

## Finding 4 — published source sentinels disagree strongly with the executable crossing

This comparison is **a posteriori only** and is not used as a post-hoc fit target.

The exact arXiv:1701.02311v2 source reports the projected RG fixed-point crossings for the same boundary tuples approximately as:

- `(1,1,1,1)`: `alpha* ~ 0.628`;
- `(1,1,1,3)`: `alpha* = 0.662`;
- `(3,1,1,1)`: `alpha* = 0.614`;
- `(3,5,1,1)`: `alpha* = 0.607`.

ITER062B instead reported approximately `0.535`, `0.567`, `0.528`, and no crossing for the fourth tuple. In the converged central region the executable differences do not reproduce the published sign structure (for example B0 remains negative at both `0.60` and `0.65`).

Because these values were explicitly excluded as fit targets, the mismatch is not itself a frozen scientific FAIL. It is an independent source-fidelity sentinel supporting the conclusion that the current executable integral is not yet a validated reconstruction of the published object.

## Reconciliation

- ITER061 source authority PASS remains valid.
- ITER062A restricted amplitude-kernel source closure PASS remains valid.
- ITER062B historical workflow result is retained for provenance, but its **scientific PASS is superseded by this manual audit**. Status becomes `INVALID_SCIENTIFIC_INFERENCE_SOURCE_MEASURE_MAPPING_UNRESOLVED`; it is neither PASS nor scientific FAIL.
- ITER063 remains INVALID with no scientific gate credit.
- ITER064 is terminal `INVALID_DIAGNOSTIC_INFERENCE_CROSSING_ENDPOINT_NONCONVERGED`; its data support only the narrower observation that the earlier permutation discrepancy is seed/QMC sensitive.
- `restricted_coarse_fine_amplitude_reproduced=false` until a corrected source-qualified gate passes.
- `full_eprl_refinement_derived=false`; `lorentzian_refinement_derived=false`; `bridge_credit=false`; candidate theory `UNFORMED / 0%`.

## Exact next gate

**`RC008_GLOBAL_GEOMETRIC_MEASURE_TOPOLOGY_AUTHORITY`**.

Before another numerical crossing calculation, prospectively freeze and derive the geometric-sector measure for the entire glued complexes from the unique spin variables, embedding/area-sum constraints and global pullback metric:

1. immutable coarse and fine incidence dictionaries for unique face-spin variables and shared faces;
2. exact constraint list and reduced coordinates (1 coarse / 6 fine);
3. symbolic or automatic-differentiation pullback metric/Jacobian from unique spins to reduced coordinates;
4. independent numerical determinant implementation over held-out geometric fixtures;
5. a coarse two-hypercuboid analytic sentinel;
6. explicit comparison against the old product-of-local-`Delta_FP` prescription as an adversarial comparator;
7. no amplitude crossing computation until this measure gate is terminal.

A later numerical successor must require convergence **at every endpoint used to assert a crossing**, not merely on a separate central alpha subset, and should use the published fixed-point values only as held-out source sentinels after implementation freeze, never as fitting targets.
