# ITER097 preregistration — CDT response-matrix PSD-bound identifiability

Date: 2026-09-15
Gate: `ITER097_RESPONSE_MATRIX_PSD_BOUND_IDENTIFIABILITY`

## Motivation frozen before adjudication

ITER093 identified the exact finite-volume CDT thermodynamic response matrix

`F = Cov(A)`, `A=(-N_0, N_41-6N_0, N_4)`.

ITER094-ITER096 exhausted the frozen public-data routes for matched primitive `N_0,N_41,N_32` samples. The remaining question is whether published scalar susceptibilities plus exact covariance positivity can nevertheless constrain the missing matrix strongly enough to identify or exclude candidate bare scaling directions.

## Frozen question

Given only source-published diagonal variances/susceptibilities for selected action-conjugate observables, qualitative/quantitative pseudocritical-line slopes, exact linear identities, and the requirement `F >= 0`, can one derive nontrivial bounds on the eigenvectors/eigenvalue ordering of the full response matrix that survive all allowed off-diagonal covariances and the volume-fixing ambiguity?

## Mathematical authority

For any covariance matrix:

- `F` is symmetric positive semidefinite;
- `|F_ij| <= sqrt(F_ii F_jj)`;
- every principal minor is nonnegative;
- fixing one or more diagonal entries does not determine the signs or magnitudes of cross-covariances inside those bounds.

No probabilistic model beyond covariance positivity may be inserted.

## Frozen source constraints from prior gates

ITER093 establishes:

- exact basis `A=(-N_0,N_41-6N_0,N_4)`;
- diagonal susceptibilities exist for selected observables;
- required matched off-diagonal cross-covariances are unpublished;
- the `kappa_4` row/column is protocol-sensitive under volume fixing.

ITER092 supplies only a mixed finite-size pseudocritical `K_4-Delta` trajectory/tangent and explicitly does not identify a pure cosmological eigendirection.

ITER094-ITER096 establish that no qualifying public matched-count dataset is available on the frozen surfaces.

## Required predicates

A. Derive the complete PSD/Cauchy-Schwarz admissible interval for each missing covariance from any available diagonal authority.

B. Test whether all matrices in the admissible family share a common eigenvector sector or eigenvalue ordering narrow enough to identify a scaling field.

C. Test whether a pseudocritical-line tangent can reduce the covariance family without assuming that the tangent is itself a Fisher/RG eigenvector.

D. Keep the `kappa_4` row/column conditional on volume-fixing/deconvolution status.

E. No FRG eigenvector, fixed point or target basis may be used to choose among allowed CDT matrices.

## Frozen classifications

- `PASS_SCOPED_PSD_BOUNDS_IDENTIFY_NONTRIVIAL_SCALING_SECTOR` only if the admissible PSD family forces a source-robust eigenvector/eigenvalue sector.
- `PASS_SCOPED_PSD_BOUNDS_EXCLUDE_SPECIFIC_SECTORS` if robust exclusions are possible but no unique sector is identified.
- `NO_GO_SCOPED_MARGINALS_DO_NOT_IDENTIFY_RESPONSE_EIGENDIRECTIONS` if admissible cross-covariances permit materially different eigenvectors/orderings while respecting all frozen published constraints.
- `BLOCKED_SOURCE_NUMERICAL_DIAGONALS` only if even the qualitative identifiability question cannot be answered without exact diagonal values.

## Controls

- `ZERO_COVARIANCE_CONTROL`: missing off-diagonals cannot be set to zero by convenience.
- `MAX_CORRELATION_CONTROL`: saturating Cauchy-Schwarz is an allowed adversarial endpoint unless source evidence excludes it.
- `TANGENT_EIGENVECTOR_SWAP_CONTROL`: a phase-boundary tangent is not promoted to a Fisher or RG eigenvector.
- `FIXED_VOLUME_ROW_CONTROL`: suppressed/externally stiffened volume fluctuations cannot be treated as the unconstrained `kappa_4` response.
- `FRG_TARGET_SELECTION_CONTROL`: no CDT matrix may be selected because it resembles an FRG stability matrix.

## Claim ceiling

A no-go is only an identifiability result for the frozen published summaries. It does not imply absence of continuum scaling fields, failure of CDT, a bridge failure theorem, new physics, or a candidate theory.
