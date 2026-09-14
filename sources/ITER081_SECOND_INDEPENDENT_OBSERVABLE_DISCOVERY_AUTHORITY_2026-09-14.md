# ITER081 source authority — second independent CDT/FRG observable discovery

Date: 2026-09-14
Gate: `ITER081_CDT_FRG_SECOND_INDEPENDENT_REDUCED_OBSERVABLE_DISCOVERY`
Preregistration commit: `57511d4110e33bbfbd978aef9a41840eda2b2895`

## Frozen candidate families

1. CDT reduced transfer/effective-action coefficients — arXiv:1403.5940.
2. CDT spatial Laplace-Beltrami spectrum — arXiv:1903.00430 and arXiv:1912.11311.
3. CDT quantum Ricci curvature — arXiv:2006.06263.
4. Current CDT status — arXiv:2604.05641.
5. FRG scale-dependent spectral geometry — arXiv:2203.08003.
6. FRG relational observables — arXiv:2112.02118.
7. Existing direct reduced map — arXiv:2408.07808, used only to identify information already consumed by ITER078.

## Executive result

The frozen discovery stack contains one clearly independent and scale-sensitive CDT observable family with a plausible FRG scale counterpart:

**the low-lying Laplace-Beltrami spectrum on CDT spatial slices.**

Its spectral gap and low eigenvalues are measured independently of the ITER078 reduced volume-profile/action data, have inverse-length-squared meaning, and exhibit critical scaling near the `C_b-C_dS` transition.

However, the frozen FRG spectral-geometry source defines cutoff modes on the running **four-dimensional self-consistent effective spacetime geometry**, while the CDT eigenvalues are those of **three-dimensional spatial slices**. No source-defined embedding, slicing or mode map identifies the CDT slice eigenvalue with the FRG four-dimensional cutoff eigenvalue `k^2`.

A second, weaker candidate also survives discovery: FRG relational scalar curvature depends on the separate dimensionless couplings `g` and `lambda` and is therefore in principle informative about the theory-space degeneracy left by ITER078. But the frozen stack supplies no source-defined map from CDT finite-radius quantum Ricci curvature to the FRG relational scalar-curvature composite operator.

The correct frozen classification is therefore:

**`PASS_SCOPED_SPATIAL_LAPLACIAN_SCALE_CANDIDATE_ONLY`**

with secondary note:

**`RELATIONAL_CURVATURE_SECONDARY_CANDIDATE_REQUIRES_TYPED_MAP`**.

No numerical second constraint and no bridge credit are authorized.

## Candidate 1 — residual CDT reduced-action coefficients

### Independence

**FAILS THE ITER081 INDEPENDENCE TEST.**

The 2014 CDT transfer-matrix/effective-action source writes a reduced scale-factor action of the schematic form

`S_eff = (1/Gamma) sum_t [kinetic(n_t,n_{t+1}) - lambda n_t + mu n_t^(1/3) + ...]`.

`Gamma`, the mean volume profile, the covariance/transfer matrix, and the potential coefficients belong to the same reduced volume-action sector already used in the direct ITER078 comparison. The source also states that `lambda`, together with `mu`, participates in fixing the total four-volume/profile.

Thus treating another coefficient from the same fit as an independent observable would not supply out-of-sample information. It could refine the same reduced model but does not satisfy predicate A strongly enough for ITER081.

### Verdict

`SAME_REDUCED_ACTION_DATA_CONTROL = TRIGGERED`.

No second-observable credit.

## Candidate 2 — CDT spatial Laplace-Beltrami spectrum

### A. Independent CDT observable

**PASS.**

The 2019 CDT spectral studies compute the spectrum of the graph/Laplace-Beltrami operator directly on spatial slices of independently sampled four-dimensional CDT configurations.

The observable is not reconstructed from the volume-profile covariance or from `(N_4, omega, Gamma)`. On a spatial slice made of tetrahedra, the discrete Laplacian acts on the dual four-regular graph; the lowest nonzero eigenvalue `lambda_1` is the spectral gap.

This is an operationally separate geometric measurement.

### Scale meaning

**PASS_SCOPED.**

The source explicitly notes that the spectral gap has mass dimension two, hence inverse-length-squared meaning. For a regular extended geometry,

`lambda_n proportional_to 1/D^2`

for graph diameter `D` at low mode number.

The Laplace-Beltrami eigenvalues can equivalently be interpreted as diffusion rates or squared wavenumbers of the corresponding eigenmodes.

Thus the spectrum carries genuine scale information independently of the scale-factor effective action.

### Critical behavior

**PASS_SCOPED.**

The low-lying spectrum distinguishes CDT phases. In the `C_b` phase, B-like slices possess a nonzero spectral gap in the thermodynamic limit, while the gap closes toward the `C_dS` phase.

The sources study several low eigenvalues and find a hierarchy of characteristic inverse-length scales. Near the candidate `C_b-C_dS` continuum transition, these scales approach zero with compatible critical behavior, making them credible independent probes of running scales and criticality.

The exact transition-order/continuum interpretation remains evidence-level and does not by itself fix an FRG scale.

### B/C. FRG spectral counterpart and sensitivity

**PARTIAL POSITIVE AUTHORITY.**

The 2022 FRG spectral-geometry source defines eigenmodes of the Laplacian/d'Alembertian on the running self-consistent metric. The EAA regulator is a function of this operator and distinguishes modes around eigenvalues of order `k^2`.

In particular, FRG cutoff modes satisfy an eigenvalue condition of the form

`-Box_k chi = +/- k^2 chi`

and their quantum numbers depend on the dimensionless cosmological constant `lambda(k)`. Therefore the FRG spectral data carry information beyond a generic inverse length and beyond the already mapped product `g lambda`.

This makes Laplacian spectral data a high-information scale/theory-space candidate.

### E. Typed-domain obstruction

**NOT YET SOURCE-QUALIFIED.**

The CDT observable is the Laplace-Beltrami spectrum of **three-dimensional spatial slices**. The FRG frozen source analyzes modes of the **four-dimensional running effective spacetime geometry**.

The frozen stack does not derive:

- a map from the CDT slice Laplacian to the FRG four-dimensional Laplacian/d'Alembertian;
- a foliation/slicing prescription for the FRG background yielding the same slice operator;
- equality of a CDT slice gap `lambda_1` with a four-dimensional FRG cutoff eigenvalue `k^2`;
- a common normalization of graph eigenvalues and continuum effective-metric eigenvalues.

This is not a cosmetic dimensional mismatch. A spatial spectral gap can diagnose slice connectivity and phase structure without being the same physical mode resolution as the four-dimensional EAA cutoff.

### Candidate verdict

The family satisfies independence and scale-sensitivity strongly enough for a dedicated next gate, but not for a direct second theory-space constraint in ITER081.

`SPATIAL_LAPLACIAN_SCALE_CANDIDATE = QUALIFIED_SCOPED`.

## Candidate 3 — CDT QRC ↔ FRG relational scalar curvature

### Independent CDT side

**PASS.**

CDT quantum Ricci curvature is an independent finite-radius metric observable and is not reconstructed from the reduced volume-action parameters.

### FRG relational side

**PASS AS A GENUINELY RUNNING OBSERVABLE FAMILY.**

The 2021/2022 FRG relational-observable source constructs observables in physical relational coordinates using the composite-operator flow. At leading derivative order it includes the inverse relational metric and relational scalar curvature.

Their scaling dimensions are computed at the asymptotic-safety fixed point and depend on the dimensionless Newton coupling `g` and cosmological constant `lambda`. Thus this family is, in principle, sensitive to information beyond the single product constrained by ITER078.

### Cross-framework typing

**NOT ESTABLISHED.**

The CDT QRC object is a finite-radius quasi-local metric-space observable based on average distances between geodesic spheres. The FRG relational scalar curvature is a local/composite scalar expressed in dynamical physical coordinates and evolved under the FRG composite-operator flow.

No frozen source derives the finite-radius/small-radius limit, normalization, averaging and scale map needed to identify these two quantum observables.

ITER077 already showed that QRC cannot be identified with FRG background curvature by name. The relational scalar is a better candidate than background curvature, but it still requires its own prospectively frozen typed-map gate.

### Candidate verdict

`RELATIONAL_CURVATURE_SECONDARY_CANDIDATE_REQUIRES_TYPED_MAP`.

It is not the preferred immediate scale candidate because the spatial Laplacian is more directly connected to the unresolved resolution-scale problem.

## Candidate 4 — current CDT review/status

The 2026 CDT review supports the importance of independent geometric observables and finite-size/critical scaling but does not supply a new source-defined CDT observable that already closes the FRG theory-space degeneracy or `k` normalization beyond the candidates above.

No extra candidate is promoted from review language alone.

## Frozen predicate summary

### Spatial Laplacian candidate
- A independent CDT observable: **PASS**.
- B source-defined FRG spectral counterpart: **PARTIAL / SAME GENERAL OPERATOR FAMILY**.
- C beyond `g lambda` or scale information: **PASS_SCOPED**; FRG cutoff mode spectrum depends on `lambda(k)` and `k`, CDT eigenvalues are independent inverse-length scales.
- D prospective typed map can be stated without target fitting: **PASS**.
- E dimensionality/domain compatible now: **NO; 3D SLICE vs 4D SPACETIME MAP MISSING**.
- F regulator/lattice semantics retained: **PASS_CONTROL**.
- G plausibly reduces degeneracy: **YES AS CANDIDATE, NOT YET AS ESTABLISHED CONSTRAINT**.

### Relational-curvature candidate
- independent on both sides: **YES**;
- sensitivity to separate `(g,lambda)`: **YES_SCOPED**;
- source-defined CDT-QRC ↔ relational-curvature map: **NO**.

### Same-action coefficients
- independence: **NO**.

## Mandatory-control audit

- `SAME_REDUCED_ACTION_DATA_CONTROL`: **triggered** for transfer-action residual coefficients.
- `VOLUME_FIXING_LAMBDA_CONTROL`: **triggered**; volume-fixing/reduced potential coefficients receive no independent cosmological-coupling credit.
- `SPATIAL_SLICE_FULL_SPACETIME_CONTROL`: **triggered** for the Laplacian candidate; this is its main unresolved type gap.
- `EIGENVALUE_K_CONTROL`: **triggered**; `lambda_1 = k^2` is not authorized across frameworks.
- `PHASE_ORDER_PARAMETER_CONTROL`: **passes as ceiling**; spectral gap phase sensitivity does not automatically determine `(g,lambda)`.
- `QRC_RELATIONAL_SCALAR_CONTROL`: **triggered**; a dedicated map is still required.
- `CURVATURE_BACKGROUND_CONTROL`: **passes**; relational and background curvature remain distinct.

## Source-authority classification

**`PASS_SCOPED_SPATIAL_LAPLACIAN_SCALE_CANDIDATE_ONLY`**

Secondary surviving candidate:

**`RELATIONAL_CURVATURE_SECONDARY_CANDIDATE_REQUIRES_TYPED_MAP`**.

This classification means that ITER081 successfully found an independent, source-measured CDT observable family worth a dedicated comparator gate. It does **not** mean that the observable already fixes `k`, separates `(g,lambda)`, or validates ITER078.

## Recommended successor

The highest-information immediate successor is:

**`PREREGISTER_ITER082_CDT_SPATIAL_LAPLACIAN_FRG_MODE_SCALE_CROSSWALK_AUTHORITY`**

The gate should freeze the CDT slice-spectrum sources and FRG cutoff-mode spectral-geometry source, then ask whether a source-defined slicing/embedding and normalization can connect the 3D CDT eigenvalue scales to the FRG four-dimensional mode-resolution `k` without using dimensional analogy alone.

A separate later gate may compare CDT QRC with FRG relational scalar curvature.

## Claim ceiling

ITER081 does not supply a numerical second constraint, a unique `(g_k,lambda_k)`, an operational `k`, out-of-sample validation, bridge credit, a shared UV fixed point, full theory equivalence, new physics or a candidate theory.