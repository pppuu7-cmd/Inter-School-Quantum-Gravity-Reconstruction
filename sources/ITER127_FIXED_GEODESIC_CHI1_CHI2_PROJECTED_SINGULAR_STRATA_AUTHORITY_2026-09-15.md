# ITER127 source authority — exact chi1/chi2 projected singular-strata inputs

Date: 2026-09-15
Gate: `ITER127_FIXED_GEODESIC_CHI1_CHI2_PROJECTED_SINGULAR_STRATA_AUTHORITY`
Preregistration: `prereg/ITER127_FIXED_GEODESIC_CHI1_CHI2_PROJECTED_SINGULAR_STRATA_AUTHORITY_2026-09-15.md`
Exact-source artifacts:

- `iter127-frob-geodesic-kernel-authority` — arXiv archive/TeX hashes and short equation evidence;
- `iter127-frob-geodesic-structure` — structural chi1/chi2/Green-kernel checks;
- `iter127-frob-initial-tangent-coefficients` — exact-source coefficient assertions.

Machine singular table: `analysis/iter127_projected_singular_strata_table.json`.

## 1. Source-qualified first-order geodesic structure

Suppressing indices but retaining the exact affine/kernel structure, the source first-order solution has the form

`chi1(t) = -(t/2) h(x).v - int_0^t ds (t-s) Gamma1(x+s v)[v,v]`.

The dedicated exact-source coefficient workflow verifies the source coefficient `-1/2` in the initial-tangent metric term. The exact-source structure workflow verifies the line integral, Christoffel dependence and retarded affine-difference Green kernel.

At the final endpoint `t=1`, the bulk line weight is therefore

**`1-s`.**

Consequences:

- one independent affine parameter in the bulk chi1 term;
- one power of suppression at the final/upper endpoint `s->1`;
- no Green-kernel suppression at the initial/lower endpoint `s->0`;
- the initial-tangent term is endpoint-local and must remain separate from the bulk line term.

Predicates A,G: **PASS**.

## 2. Source-qualified second-order geodesic structure

Again suppressing tensor indices while preserving the source perturbative structure,

`chi2(t) = +(3t/8) h(x)^2.v`
`          - int_0^t ds (t-s)[ Gamma2[v,v]`
`                                + 2 Gamma1[v,d chi1]`
`                                + (partial Gamma1)[chi1,v,v] ]`.

The exact-source coefficient workflow verifies the `+3/8` quadratic initial-tangent metric coefficient and the chi2-to-chi1/Christoffel nesting.

Substituting the source chi1 solution shows that no term requires more than two independent affine parameters at second order.

Predicate B: **PASS**.
Predicate C: **PASS — chi1 <=1 parameter, chi2 <=2 parameters**.

## 3. Exact polynomial suppression weights after substitution

At final endpoint `t=1`, the source Green kernels imply the following source-derived polynomial weights.

### First order / M

Bulk chi1:

`(1-tau)`.

### Second order / G: direct Gamma2

`(1-tau)`.

### Gamma1 times d chi1

Differentiating the first-order Green solution removes the inner `(tau-sigma)` factor from the bulk part of `d chi1`. Hence its nested bulk domain has

`0 <= sigma <= tau <= 1`

with outer weight

`(1-tau)`

and **no polynomial diagonal suppression** as `sigma->tau`.

### (partial Gamma1) times chi1

For the bulk chi1 insertion, the inner Green kernel survives, giving ordered domain

`0 <= sigma <= tau <= 1`

with weight

**`(1-tau)(tau-sigma)`.**

Thus the inner coincidence `sigma->tau` is softened by one power.

For the initial-tangent part `chi1_initial(tau)~tau`, the one-parameter weight is

**`tau(1-tau)`**, suppressing both line endpoints by one power.

### chi1 chi1 endpoint Taylor sector

The two bulk first-order displacements give a square-domain weight

**`(1-tau)(1-sigma)`**.

It suppresses each upper endpoint but does not itself soften the diagonal `tau->sigma`.

Predicate D: **PASS_SOURCE_PLUS_ALGEBRA**.

## 4. Initial-tangent terms are a distinct endpoint sector

The exact source initial-data expansion supplies local terms with coefficients

- first order: `-1/2`;
- second order: `+3/8`.

They are not to be folded into affine line kernels. In the curvature calculation they belong to endpoint/local composite mixing and can participate in subdivergence cancellation even when they do not create an independent line parameter.

Predicate G: **PASS_CONTROL**.
`INITIAL_TANGENT_LINE_KERNEL_SWAP_CONTROL`: **PASS_CONTROL**.

## 5. Singular-strata table

The machine table records eleven source/algebra sectors covering:

- first-order initial and bulk chi1;
- second-order initial and direct Gamma2 terms;
- Gamma1-dchi1 initial/bulk pieces;
- dGamma1-chi1 initial/bulk pieces;
- chi1-chi1 initial/one-line/two-line pieces.

For each row it records parameter count, integration domain, polynomial weight, endpoint/diagonal strata and whether the ITER126 local subtraction method applies.

Key suppression facts are:

- every direct outer Green integral ending at the final endpoint carries `(1-tau)`;
- `d chi1` removes the inner Green suppression, leaving the nested diagonal unsuppressed;
- `chi1` itself retains `(tau-sigma)`, softening the nested diagonal by one power;
- two independent bulk chi1 factors give `(1-tau)(1-sigma)` but no diagonal suppression;
- initial-tangent pieces remain endpoint-local.

Predicate F: **PASS_TABLE_CLOSED**.

## 6. Curvature/projector derivatives are intentionally not converted to residues yet

The table supplies **geodesic polynomial suppression orders**, not the full local singular exponent. Curvature vertices, Christoffel derivatives, the ITER122 `Box_perp` projectors and loop tensor numerators can increase or cancel local powers.

Therefore ITER127 does not assign any row a `1/epsilon` coefficient or `B1` contribution. It only freezes the exact affine weights needed by ITER126's local subtraction algorithm.

Predicate E: **PASS_CONTROL**.
`MATTER_RESIDUE_CURVATURE_RESIDUE_CONTROL`: **PASS_CONTROL**.

## 7. Source-integrity controls

The source package was downloaded directly from arXiv by GitHub Actions; archive/TeX SHA256 values are preserved in the authority artifact. Short equation-only evidence is preserved with source file/line locations.

No coefficient in this authority record was selected from EDT data or reconstructed solely from a generic geodesic equation.

Predicate H: **PASS_CONTROL**.
`MEMORY_RECONSTRUCTION_CONTROL`: **PASS_CONTROL**.
`GENERIC_GEODESIC_SOURCE_EQUATION_SWAP_CONTROL`: **PASS_CONTROL**.
`TARGET_WEIGHT_SELECTION_CONTROL`: **PASS_CONTROL**.

## Source classification

**`PASS_SCOPED_EXACT_CHI1_CHI2_WEIGHTS_SOURCE_QUALIFIED_SINGULAR_TABLE_CLOSED`**

The fixed-geodesic source inputs needed for the local UV analysis are now exact and reproducible: first-/second-order initial data, outer Green weights, nested parameter count and the diagonal/endpoint polynomial suppression structure.

## Highest-information successor

`ITER128_FIXED_GEODESIC_CURVATURE_PROJECTED_LOCAL_SINGULAR_DEGREE_CENSUS`

Combine these exact affine weights with the derivative content of `R1`, `Gamma1`, `Gamma2`, `chi1`, `chi2` and the ITER122 genuine-defect projectors. For every ITER127 row, compute a conservative local superficial singular degree and the exact Taylor-jet order required by ITER126. Keep possible tensor cancellations separate from power-counting upper bounds.

## Claim ceiling

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**. No curvature pole residue, `B1`, noncancellation theorem, EDT fit, direct discrepancy, bridge or new physics follows.