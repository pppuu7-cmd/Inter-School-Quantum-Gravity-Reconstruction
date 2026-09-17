# ITER157 preregistration — fixed-geodesic endpoint tensor-pole equation source derivation

Date: 2026-09-17
Gate: `ITER157_FIXED_GEODESIC_ENDPOINT_TENSOR_POLE_EQUATION_SOURCE_DERIVATION`
Frozen parent terminal/main SHA: `aa650a23b4026f6c6ba4abf223d7459c07923b2a`

## Scientific objective

ITER156 ended with an exact rank-0 / nullity-8 endpoint coefficient system because no admissible pre-existing explicit tensor-resolved endpoint pole equations were available. ITER157 is therefore an **equation acquisition / first-principles derivation gate**, not a coefficient-fit gate and not another repository authority audit.

The only scientific question is:

> For the three frozen first-M/G endpoint strata, can source-faithful calculation and/or exact primary-source authority produce explicit general-d tensor-resolved divergent endpoint pole equations in the immutable ITER118 endpoint basis?

No ITER158 rank/nullspace calculation on any newly produced equation set is permitted until ITER157 terminalizes PASS and a separate ITER158 preregistration is committed.

## Frozen endpoint basis

The curvature endpoint basis is immutable and ordered exactly as

1. `R`
2. `S := R_mn n^m n^n`
3. `DR := n^a nabla_a R`
4. `DS := n^a nabla_a S`
5. `BoxR := Box R`
6. `D2R := (n.nabla)^2 R`
7. `BoxS := Box S`
8. `D2S := (n.nabla)^2 S`

No ninth curvature operator may be introduced. No operator may be deleted after outcome. Any basis transformation used internally must be invertible, exact, and recorded, with final equations mapped back to this ordering.

The identity/contact convention is not a ninth connected curvature coefficient.

## Frozen scoped graph families / strata

Canonical repository families, inherited from ITER154B, are:

- `M_R2_chi1_dR1`;
- `M_R1_chi1_dR2`;
- `G_R1_chi2_Gamma2_dR1`.

For each family the producer must recover and record, before accepting any equation:

- exact source insertion and perturbative term;
- uncontracted vertex/numerator object used;
- propagators;
- tangent/geodesic tensors;
- endpoint stratum and orientation;
- loop normalization and measure;
- dimensional convention;
- symmetry factor and powers of `i`.

If the current source chain cannot recover one of these primitives, the missing primitive is scientific output rather than permission to guess it.

## Frozen dimensional and renormalization rules

Use the repository dimensional convention `d = 4 - 2 epsilon` unless an earlier frozen microscopic source explicitly proves a different convention for the same object. Such a discrepancy must be translated exactly before any coefficient is accepted.

Never set `d=4` before pole extraction. Keep distinct:

- `1/epsilon^2`;
- `1/epsilon`;
- finite;
- `O(epsilon)`.

Within the three ITER154B connected-cross bubble cores, strict proper ordinary bulk/local-composite subdivergence counterterm insertions are zero and `R_sub G = G` **only for that scoped proper-subdivergence operation**. This does not imply that the full bubble, endpoint, line-defect or contact divergence vanishes.

## ITER153 distributional firewall

The seven previously identified endpoint/contact distributions remain unresolved renormalized objects. Their known momentum derivative orders must not be promoted into endpoint counterterm coefficients without an explicit authorized renormalization map.

In particular:

- no `scaleless = 0` argument may be applied after prematurely setting the endpoint separation to zero;
- absence of a pole equation is never a zero coefficient;
- a contact distribution is not automatically an endpoint counterterm coefficient.

## Raw-tensor-first requirement

For every scoped family, derive or source the object in the order

`frozen propagators/vertices -> uncontracted tensor numerator -> regulated endpoint kernel -> local endpoint pole tensor -> tensor decomposition -> ITER118 projection equations`.

The accepted pole object must be persisted **before scalar projection** and must retain, where present:

- free tensor indices;
- metric tensors;
- tangent vectors `n`;
- transverse/normal projectors;
- loop/external momenta or covariant derivatives;
- curvature structures;
- normalization and symmetry factors.

A scalar invariant manifest alone cannot satisfy ITER157.

## Support classification before solving

Every divergent term must be classified before coefficient solving as exactly one of:

- `BULK`;
- `LINE_DEFECT`;
- `ENDPOINT`;
- `CONTACT_DISTRIBUTION`;
- `UNRESOLVED`.

Slot 7 may use only terms justified as `ENDPOINT` in this gate.

## Prospective source/convention manifest rule

Before a source contributes any accepted tensor residue/equation, a committed source/convention manifest must record, to the extent applicable:

- source identifier and immutable repository SHA or arXiv/DOI/version;
- page/equation/section;
- metric signature;
- Riemann and Ricci conventions;
- Fourier convention;
- `d`/epsilon convention;
- graviton/ghost propagator normalization;
- relevant vertex normalization;
- tangent orientation and endpoint orientation;
- geodesic/worldline parameterization;
- factors of `i`;
- loop measure and `(2*pi)^d` convention;
- symmetry factors;
- exact source-to-repository conversion map.

No silent convention conversion is admissible.

## Primary-source lane

Primary literature is admissible only when it supplies an explicit mathematical primitive that can enter the tensor derivation/equation manifest. Generic reviews or qualitative statements cannot authorize coefficients.

A literature coefficient is not imported directly: the exact conversion chain must be

`source convention -> repository convention -> repository tensor object -> ITER118 endpoint basis`,

with independent Critic verification.

## First-principles lane

The preferred lane is reconstruction from frozen repository microscopic objects. The producer must attempt to recover the earliest uncontracted object upstream of the scalar-invariant outputs and derive the endpoint short-distance pole without setting endpoint separation to zero before distribution/support classification.

If the frozen source chain has irreversibly discarded tensor data, ITER157 must identify the earliest exact lossy map and name the minimal missing primitive; it must not manufacture an inverse.

## Projection-family freeze

No projection may be chosen in response to an observed coefficient nullspace.

Before any ITER158 rank calculation, ITER157 must commit a complete projection manifest or a deterministic prospective projection-generation algorithm. Every equation must have exact form

`P_alpha[T_pole] = Sum_i A_{alpha i} c_i = r_alpha`

and record:

- projector definition;
- family/endpoint stratum;
- pole order;
- exact row `A_alpha i` in the frozen basis;
- exact residue `r_alpha`;
- raw-tensor content hash;
- equation content hash.

If direct symbolic projectors are impractical, a generic-curvature-jet reconstruction is allowed only with a prospectively frozen deterministic seed, exact rational jets obeying curvature identities, an overdetermined construction set, and held-out validation jets. Highly symmetric backgrounds alone are forbidden.

## Symmetry and normalization controls

Mandatory exact controls:

- Riemann index symmetries;
- algebraic/differential Bianchi identities in the retained linear sector;
- tangent normalization;
- tangent-normal orthogonality;
- projector idempotence;
- endpoint orientation;
- covariance under legal invertible basis/index transformations;
- explicit `(2*pi)^d`, powers of `i`, loop factors, propagator/vertex normalizations, couplings, symmetry factors, line measure and endpoint multiplicity.

A symmetry identity may reduce redundancy but cannot create a dynamical coefficient absent from the source calculation.

## Producer / Critic independence

The Critic must independently reconstruct the convention/topology/support logic and at least one nontrivial tensor/projection check from source-level objects. Merely re-reading producer JSON is insufficient.

## Frozen terminal classifier

### PASS

`PASS_SCOPED_ITER157_SOURCE_FAITHFUL_ENDPOINT_TENSOR_POLE_EQUATIONS_DERIVED`

iff all of the following hold:

1. all three frozen families are processed;
2. source-faithful raw tensor pole objects are actually obtained for every equation claimed;
3. source/convention provenance is complete and checkable;
4. general-d pole extraction is valid;
5. endpoint/line/bulk/contact separation is justified;
6. an explicit frozen projection/equation manifest is produced;
7. independent Critic agrees with producer on the accepted equation set;
8. no absent equation or null direction is interpreted as zero;
9. no `B1_total` or downstream bridge/new-physics claim is formed.

PASS does **not** require or permit a rank conclusion; rank belongs to separately preregistered ITER158.

### BLOCKED

`BLOCKED_SCOPED_ITER157_ENDPOINT_TENSOR_POLE_SOURCE_INCOMPLETE`

iff one or more indispensable primitives cannot be sourced or derived without invention. The terminal record must name the exact missing primitive(s), localize the earliest lossy/undefined step, and select the single highest-downstream-leverage primitive for any successor. Acceptable primitive labels include, but are not limited to:

- `UNCONTRACTED_TENSOR_NUMERATOR_MISSING`;
- `ENDPOINT_VERTEX_NORMALIZATION_MISSING`;
- `GENERAL_D_ENDPOINT_OPERATOR_UNDEFINED`;
- `GEODESIC_BOUNDARY_CONDITION_UNSPECIFIED`;
- `ENDPOINT_PROJECTION_MAP_INCOMPLETE`;
- `REGULATED_DISTRIBUTION_EXTENSION_MISSING`;
- `PRIMARY_SOURCE_CONVENTION_NOT_TRANSLATABLE`.

A generic statement such as `source missing` is forbidden.

### INVALID

Use `INVALID` for provenance, convention, implementation, basis mutation, post-outcome projection selection, or other preregistration contamination.

### SCIENTIFIC_FAIL

Use `SCIENTIFIC_FAIL` only if a completed source-faithful calculation contradicts a prospectively frozen structural predicate. Failure to source a primitive is BLOCKED, not scientific falsification.

## ITER158 firewall

Only after ITER157 terminal PASS may a separate preregistration

`ITER158_FIXED_GEODESIC_ENDPOINT_POLE_EQUATION_RANK_AND_COEFFICIENT_SOLVE`

be committed. ITER158 may use only the frozen ITER157 equation manifest. No equation may be added after rank/nullspace inspection.

## Claim firewall

Throughout ITER157:

- `B1_direct = UNAUTHORIZED_FINAL`;
- `beta_defect = UNAUTHORIZED_FINAL`;
- `B1_defect = UNAUTHORIZED_FINAL`;
- `B1_total = UNAUTHORIZED`;
- `ALL_KNOWN_SCHOOLS_FAIL = false`;
- `NEW_QG_THEORY_REQUIRED = false`;
- `NEW_PHYSICS_FOUND = false`;
- `BRIDGE_DERIVED = false`;
- `candidate_theory_authorized = false`;
- candidate theory remains `UNFORMED / 0%`.

## Scientific-efficiency rule

No successor task is justified unless it produces a genuinely new mathematical object: a raw tensor residue, endpoint pole equation, exact convention map, exact minimal missing primitive, projection relation, or downstream matrix. Repeating ITER155/156 authority/search logic is explicitly outside this gate.
