# ITER161 preregistration — G `b^2*S^2` raw endpoint tensor lift to ITER118 operator equations

Date: 2026-09-17

Gate: `ITER161_G_B2S2_ENDPOINT_RAW_TENSOR_LIFT_TO_ITER118_OPERATOR_EQUATIONS`

Frozen parent: `b3b9dd5486c0a410c5c9d12dba2250c7ad679843`.

## Motivation fixed before outcome

ITER160 confirms, under the frozen local meromorphic prescription, that the ITER150 raw TWO_PROPAGATOR pole in

`G_R1_chi2_Gamma2_dR1 : b^2*S^2`

has lower- and upper-endpoint support residues

`-525/(pi^4 L^10) * 1/epsilon`

at each endpoint. These are raw scalar support residues, not ITER118 coefficients.

ITER140 contains exact arbitrary-integer-`D` indexed microscopic ingredients before its final 28-scalar-invariant reconstruction. The present gate asks whether enough tensor information can be retained/reconstructed prospectively from that pre-scalarization machinery to form a source-faithful endpoint operator equation.

## Immutable endpoint operator basis

The ITER118 endpoint basis remains

`[R, S, DR, DS, BoxR, D2R, BoxS, D2S]`,

where `S=R_nn` and `D=n^mu partial_mu` along the geodesic.

No basis mutation, nonlinear curvature insertion or downstream line-defect projector is allowed.

## Frozen upstream authorities

1. ITER118 terminal basis/power-counting authority, commit `748e1e284eac649bcea0666832e690ddf84eacdd`.
2. ITER140 exact arbitrary-integer-`D` indexed engine `analysis/iter140_first_mg_general_d_invariant_continuation.py`.
3. ITER150 raw two-propagator pole and exact Fourier/affine normalization.
4. ITER154B no-proper-subdivergence result for the scoped first-M/G bubbles.
5. ITER160 confirmed lower/upper raw support split.

ITER153 contact distributions remain outside this gate and may not be imported, set to zero or used as endpoint coefficients.

## Required derivation order

The gate must operate **before** the lossy 28-scalar-invariant reconstruction wherever possible:

1. reuse the exact general-`D` microscopic definitions (`pmap`, `r1_tensor`, `dr1_real`, `g2_real` and the G-family contraction);
2. identify every index contraction currently performed inside `G1_value` and its helpers;
3. define a tensor-resolved object by retaining the maximal set of indices needed to compare with a local endpoint operator insertion, rather than summing them prematurely;
4. preserve `D` symbolically/through exact integer-D continuation before `D=4-2 epsilon` pole extraction;
5. carry lower and upper endpoint orientation/support separately;
6. construct linearized/tree insertion kernels for the immutable ITER118 endpoint operators in the **same anchored observable channel and normalization**;
7. only after both sides are frozen, assemble exact endpoint matching equations.

The existing 28-scalar invariant output is a consistency check only. It must not be inverted as if scalarization preserved a unique tensor preimage.

## Raw-tensor persistence requirement

Before any coefficient solve, persist a machine-readable manifest containing, for every candidate equation:

- graph/family and endpoint (`lower` or `upper`);
- all retained free indices and their symmetries;
- metric/tangent contractions;
- momentum/derivative assignment;
- general-`D` normalization;
- pole order and coefficient;
- support class;
- exact ITER118 tree kernel(s) compared;
- orientation/sign convention;
- source commit/blob provenance.

If the graph contribution is intrinsically a fully contracted scalar in the frozen observable and no source-faithful free-index matching object exists, do not invent one. Instead identify the exact earliest contraction/matching primitive that prevents coefficient extraction.

## Pole and support locks

The only numerical pole input authorized from ITER160 is the scoped raw support value for the G `b^2*S^2` two-propagator master.

It may be used to normalize a tensor lift only after the tensor structure is independently derived. It may not be used to choose the tensor structure or fit a desired ITER118 direction.

`lower = upper` from ITER160 is a support statement, not an endpoint orientation theorem for ITER118 operators. Endpoint sign/orientation must be derived separately.

## Equation/rank firewall

No rank, nullspace or coefficient solve is allowed until the complete tensor equation manifest for this scoped G master is prospectively frozen in a separate committed file.

A single valid equation is scientific progress even if it does not determine all eight coefficients.

Missing equations are not zero coefficients.

## Frozen terminal classes

### PASS

`PASS_SCOPED_ITER161_G_ENDPOINT_TENSOR_OPERATOR_EQUATION_DERIVED`

iff at least one source-faithful lower/upper tensor-resolved raw pole object and its matching ITER118 tree-kernel equation are derived and persisted with complete conventions/provenance, without scalar inversion or forbidden support import.

PASS does not imply slot 7 is closed unless the resulting manifest independently proves sufficient rank in a later gate.

### BLOCKED

`BLOCKED_SCOPED_ITER161_G_ENDPOINT_TENSOR_LIFT_EXACT_MISSING_PRIMITIVE`

iff the pre-scalarization chain cannot produce a unique source-faithful endpoint matching object. The result must name the single exact earliest missing/irreversibly contracted primitive and show why downstream scalar data cannot reconstruct it uniquely.

### SCIENTIFIC_FAIL

`SCIENTIFIC_FAIL_ITER161_FROZEN_TENSOR_LIFT_IDENTITY_CONTRADICTED`

iff a complete source-faithful tensor lift exists but contradicts a prospectively frozen structural identity used by this gate.

### INVALID

`INVALID_ITER161`

for post-outcome tensor-basis selection, inversion of the scalarized 28-invariant map as a unique tensor inverse, use of ITER153 contacts as endpoint residues, use of ITER123 as an endpoint projector, missing provenance, or implementation error.

## Independent Critic requirements

The Critic must test:

- that tensor structure was derived independently of the known `-525/(pi^4 L^10)` normalization;
- no scalar invariant was assigned a unique tensor preimage without proof;
- general-`D` de Donder projector normalization is retained;
- lower/upper endpoint support and orientation are not conflated;
- ITER118 tree kernels belong to the same anchored observable/channel;
- missing tensor information is never interpreted as zero;
- no forbidden contact/line projection enters.

## Claim locks

`B1_total = UNAUTHORIZED`.

`BRIDGE_DERIVED = false`.

`NEW_PHYSICS_FOUND = false`.

Candidate theory remains `UNFORMED / 0%`.
