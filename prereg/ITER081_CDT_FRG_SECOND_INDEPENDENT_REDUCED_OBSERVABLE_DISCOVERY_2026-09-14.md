# ITER081 preregistration — second independent CDT/FRG observable discovery for theory-space resolution

Date: 2026-09-14
Gate: `ITER081_CDT_FRG_SECOND_INDEPENDENT_REDUCED_OBSERVABLE_DISCOVERY`

## Motivation

ITER078 establishes a direct reduced CDT↔FRG map but primarily constrains the dimensionless combination `lambda_k g_k`. ITER079 leaves the operational `xi_CDT <-> k` map open. ITER080 shows that this is insufficient for out-of-sample spectral prediction because the finite-scale QEG spectral dimension depends on the separate theory-space point `(g_k,lambda_k)` and its RG trajectory.

ITER081 is therefore a **source-discovery/authority gate**, not a fit. It asks whether CDT already provides a second independent observable, not constructed from the same `N_4, omega, Gamma` reduced volume-action data, that has a source-defined FRG counterpart capable in principle of constraining the missing theory-space direction and/or fixing the operational scale.

## Frozen candidate families and sources

### CDT reduced-action residual coefficients
- arXiv:1403.5940 — J. Ambjørn, J. Gizbert-Studnicki, A. Görlich, J. Jurkiewicz, *The effective action in 4-dim CDT. The transfer matrix approach*.

### CDT spatial Laplacian spectrum
- arXiv:1903.00430 — G. Clemente, M. D'Elia, A. Ferraro, *Spectral Methods and Running Scales in Causal Dynamical Triangulations*.
- arXiv:1912.11311 — G. Clemente, M. D'Elia, A. Ferraro, *Spectral Methods in Causal Dynamical Triangulations*.

### CDT quantum curvature
- arXiv:2006.06263 — N. Klitgaard, R. Loll, *How round is the quantum de Sitter universe?*.

### Current CDT observable/status authority
- arXiv:2604.05641 — J. Ambjørn, R. Loll, *Causal Dynamical Triangulations: New Lattice Theory of Quantum Gravity*.

### FRG spectral-geometry candidate
- arXiv:2203.08003 — R. Ferrero, M. Reuter, *The Spectral Geometry of de Sitter Space in Asymptotic Safety*.

### FRG relational-observable candidate
- arXiv:2112.02118 — A. Baldazzi, K. Falls, R. Ferrero, *Relational observables in asymptotically safe gravity*.

### Existing direct-map authority
- arXiv:2408.07808 — direct CDT↔FRG reduced-action/parameter map, used only to define what information is already consumed and therefore not independent.

No candidate source outside this frozen set may be promoted after seeing the discovery result.

## Independence requirement

A candidate receives second-observable credit only if its CDT measurement is not algebraically reconstructed solely from the same reduced data already entering ITER078:

`N_4`, `omega`, `Gamma`, the mean volume profile, and its covariance/effective scale-factor action.

A reparametrization or subleading coefficient fixed by the same effective-action fit is not automatically independent.

## Required predicates for a comparator-grade candidate

A. The CDT observable is explicitly defined and measured independently of the ITER078 reduced-map inputs.

B. A source-defined FRG observable/effective quantity exists whose mathematical type is close enough for a non-forgetful comparison; sharing terminology is insufficient.

C. The FRG quantity depends on information beyond the already mapped product `lambda_k g_k` or provides an independent operational scale/resolution condition.

D. A prospective typed map can be stated without already fitting the CDT target observable.

E. Dimensionality/domain are compatible: full 4D spacetime, spatial slice, relational scalar, background metric and global minisuperspace sectors must remain distinct.

F. Regulator/lattice/truncation and ensemble/expectation semantics remain explicit.

G. The candidate must plausibly reduce the one-dimensional theory-space/scale degeneracy exposed by ITER080 rather than merely remeasure de-Sitter roundness.

## Candidate-specific controls

### Transfer-action coefficients
- `SAME_REDUCED_ACTION_DATA_CONTROL`: coefficients extracted from the same volume-action fit cannot count as independent unless the source demonstrates statistically/operationally separate information.
- `VOLUME_FIXING_LAMBDA_CONTROL`: a Lagrange multiplier or coefficient fixing total volume cannot be promoted to an independently measured cosmological coupling.

### Spatial Laplacian spectrum
- `SPATIAL_SLICE_FULL_SPACETIME_CONTROL`: the Laplacian on 3D spatial slices cannot be silently identified with the four-dimensional EAA/de-Sitter Laplacian.
- `EIGENVALUE_K_CONTROL`: an eigenvalue or spectral gap may fix an FRG scale only if the source defines which eigenmode/resolution condition corresponds to `k`; generic inverse-length scaling is insufficient.
- `PHASE_ORDER_PARAMETER_CONTROL`: an eigenvalue that acts mainly as a phase/order diagnostic does not automatically determine `(g,lambda)`.

### Curvature / relational observables
- `QRC_RELATIONAL_SCALAR_CONTROL`: CDT finite-radius quantum Ricci curvature cannot be replaced by FRG relational local scalar curvature without a derived map.
- `CURVATURE_BACKGROUND_CONTROL`: a relational observable, a mean-background curvature and an EAA curvature coupling remain distinct.

## Frozen classifications

- `PASS_SCOPED_SECOND_INDEPENDENT_OBSERVABLE_CANDIDATE_QUALIFIED` if at least one candidate satisfies A-G strongly enough to authorize a dedicated prospective comparator gate.
- `PASS_SCOPED_SPATIAL_LAPLACIAN_SCALE_CANDIDATE_ONLY` if the spatial Laplacian is genuinely independent and scale-sensitive but the 3D-slice ↔ 4D-FRG map is not yet source-qualified.
- `PASS_SCOPED_RELATIONAL_CURVATURE_CANDIDATE_ONLY` if a closer FRG relational observable exists but no source-defined CDT-QRC correspondence is yet available.
- `PASS_SCOPED_MULTIPLE_CANDIDATES_REQUIRE_TYPED_FOLLOWUP` if more than one independent family survives discovery but none yet closes the degeneracy.
- `SCOPED_BLOCKED_NO_SECOND_INDEPENDENT_OBSERVABLE_AUTHORITY` if no frozen candidate satisfies independence and type requirements sufficiently to justify a focused next gate.

## Claim ceiling

ITER081 is discovery/authority only. It cannot establish a second constraint numerically, fix `(g_k,lambda_k)`, close the `xi <-> k` map, validate ITER078 out of sample, create bridge credit, prove a shared UV fixed point, establish full theory equivalence or authorize a candidate theory.

Candidate theory remains `UNFORMED / 0%`; bridge credit remains zero.

Sources, candidate families, independence criteria and classifications are frozen before detailed candidate adjudication.