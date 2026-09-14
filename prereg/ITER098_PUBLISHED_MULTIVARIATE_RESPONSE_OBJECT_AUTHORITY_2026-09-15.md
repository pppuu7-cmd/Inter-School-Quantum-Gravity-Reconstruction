# ITER098 preregistration — published multivariate CDT response-object authority

Date: 2026-09-15
Gate: `ITER098_PUBLISHED_MULTIVARIATE_RESPONSE_OBJECT_AUTHORITY`

## Motivation frozen before adjudication

ITER097 proved that marginal susceptibilities plus PSD constraints cannot identify the bare-coupling response eigendirections. Before marking the direct CDT scaling-field route saturated, test whether the literature already publishes a genuinely multivariate object carrying cross-information that is source-typed closely enough to constrain the ITER093 matrix without raw primitive-count samples.

## Frozen candidate object classes

1. covariance matrices of spatial-volume/profile fluctuations;
2. Hessians/inverse covariances used to reconstruct effective actions;
3. transfer-matrix effective-action fits;
4. joint/multihistogram or reweighting Jacobians;
5. principal-component directions or explicit mixed susceptibilities.

## Frozen source anchors

- arXiv:1111.6938 — 4D CDT covariance-matrix/effective-action review material;
- arXiv:1510.08719 — effective action in four-dimensional CDT;
- arXiv:1604.08786 — toroidal-topology covariance of spatial-volume fluctuations;
- ITER093 frozen phase-transition source stack.

## Required predicates

A. Candidate object must contain explicit cross-information, not only diagonal susceptibilities.

B. Its domain/basis must be identified exactly.

C. A source-defined map must exist from that basis to the action-conjugate basis `A=(-N_0,N_41-6N_0,N_4)` if it is to constrain ITER093.

D. Integrating out microscopic degrees of freedom or projecting to spatial-volume profiles cannot be silently inverted.

E. A Hessian of an effective minisuperspace action cannot be substituted for a Hessian with respect to bare CDT couplings unless a source-defined Jacobian/map is given.

F. Any transfer-matrix covariance/effective-action object must preserve its state/volume typing.

## Frozen classifications

- `PASS_SCOPED_MULTIVARIATE_OBJECT_CONSTRAINS_BARE_RESPONSE` only if an explicit source map to the ITER093 basis is available.
- `PASS_SCOPED_MULTIVARIATE_OBJECT_EXISTS_DIFFERENT_DOMAIN` if genuine cross-information exists but lives in a different projected/effective variable space and cannot constrain the bare-coupling matrix without a new map.
- `SCOPED_BLOCKED_NO_PUBLISHED_MULTIVARIATE_OBJECT` if no genuine mixed object is found.

## Controls

- `PROFILE_BARE_BASIS_SWAP_CONTROL`
- `EFFECTIVE_ACTION_BARE_HESSIAN_SWAP_CONTROL`
- `INVERSE_COVARIANCE_COVARIANCE_SWAP_CONTROL`
- `INTEGRATION_OUT_INVERSION_CONTROL`
- `TRANSFER_MATRIX_FISHER_SWAP_CONTROL`

## Claim ceiling

A positive result in a different domain is useful structural information only. It does not reopen ITER093, create bridge credit, establish an RG eigendirection, or form a candidate theory unless the required basis map is source-derived.
