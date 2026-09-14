# ITER072 preregistration — CDT spectral-diffusion scale / continuum authority

Date: 2026-09-14
Gate: `ITER072_CDT_SPECTRAL_DIFFUSION_SCALE_CONTINUUM_AUTHORITY`

## Motivation frozen before terminal adjudication

ITER071 established a source-qualified common spectral-dimension definition across 4D CDT and QEG/FRG, but did not authorize a pointwise physical-scale comparator because its frozen 4D CDT source did not calibrate integer diffusion duration to a controlled physical/continuum length scale.

ITER072 isolates that blocker on the CDT side. No FRG scale, value, trajectory or desired correspondence may be used to define the CDT calibration.

## Frozen question

Do 4D CDT sources provide a source-defined calibration from spectral-diffusion duration in lattice units to relative and/or absolute lattice/physical scale, with finite-size/discretization assumptions controlled well enough to support a finite-regulator physical-scale spectral comparator? Separately, do the sources establish the required `a -> 0` continuum limit along a critical trajectory, or only identify candidate scaling behavior?

## Frozen sources

- arXiv:1603.02076 — Jan Ambjorn, Daniel Coumbe, Jakub Gizbert-Studnicki, Jerzy Jurkiewicz, *Searching for a continuum limit in causal dynamical triangulation quantum gravity*.
- arXiv:1411.7712 — D. N. Coumbe, J. Jurkiewicz, *Evidence for Asymptotic Safety from Dimensional Reduction in Causal Dynamical Triangulations*.
- arXiv:2604.05641 — J. Ambjørn, R. Loll, *Causal Dynamical Triangulations: New Lattice Theory of Quantum Gravity*; used only as current status/claim-ceiling authority for continuum-limit interpretation.

Scientific authority in this gate is attached to the frozen arXiv identifiers and exact source-defined equations/statements.

## Required predicates

A. The source explicitly relates diffusion duration `sigma` to the lattice spacing under a diffusion/Laplacian scaling law, rather than merely saying that larger `sigma` probes larger distances.

B. A relative lattice-spacing estimator from spectral-dimension curves is explicitly defined, including the rescaling variable and fit/overlap rule.

C. The relative estimator is applied across bare-coupling points and yields source-reported relative lattice spacings with uncertainties or a stated error procedure.

D. An independent absolute lattice-spacing calibration exists in 4D CDT, stated in physical or Planck units, with its dynamical/semiclassical assumptions explicit.

E. The relative spectral estimator and independent absolute estimator are compared sufficiently to test whether they track the same lattice-spacing change in the audited phase/region.

F. Short-walk discretization, odd/even artifacts, finite volume and fit-window choices are explicitly retained; they cannot be erased to improve scaling.

G. An actual continuum limit must mean source-established approach `a -> 0` with relevant physical observables held fixed along a controlled critical/RG trajectory. Merely observing smaller relative `a`, proposing a trajectory, or approaching a phase boundary is insufficient.

H. No QEG/FRG relation may be imported into A-G. Any later map to `k`, `1/k`, or a QEG diffusion scale requires a separately preregistered cross-school gate.

## Frozen classifications

- `PASS_SCOPED_CDT_DIFFUSION_SCALE_CALIBRATED_CONTINUUM_ESTABLISHED` only if A-G all pass at the claimed 4D scope.
- `PASS_SCOPED_CDT_DIFFUSION_SCALE_CALIBRATED_CONTINUUM_OPEN` if A-F pass sufficiently to establish a CDT-internal physical/relative scale calibration but G remains open or only candidate/proposed.
- `PASS_SCOPED_RELATIVE_SCALE_ONLY` if A-C and F pass but an independent absolute calibration or its cross-check does not.
- `BLOCKED_SOURCE_AUTHORITY` if the frozen stack cannot establish the scale map itself.
- `FAIL_SCOPED_SCALE_CALIBRATION_REJECTED` if the proposed rescaling is contradicted by the frozen evidence.

## Frozen controls

- `SQRT_SIGMA_PHYSICAL_LENGTH_PROMOTION_CONTROL`: `sqrt(sigma)` may not be called an absolute physical length without the lattice-spacing calibration and its assumptions.
- `RELATIVE_ABSOLUTE_SCALE_SWAP_CONTROL`: relative curve alignment may not be promoted to an absolute Planck/physical scale.
- `PHASE_BOUNDARY_CONTINUUM_CONTROL`: movement toward a phase boundary may not be called a continuum limit without `a -> 0` scaling evidence.
- `TWO_ESTIMATOR_AGREEMENT_CONTROL`: agreement of two lattice-spacing estimators is evidence for calibration, not by itself proof of an ultraviolet fixed point.
- `FINITE_SIZE_ERASURE_CONTROL`: short/long diffusion artifacts and finite volume remain part of the result.
- `DE_SITTER_ASSUMPTION_ERASURE_CONTROL`: any absolute calibration derived from the effective de Sitter/minisuperspace sector must retain that assumption.
- `ANISOTROPY_ERASURE_CONTROL`: spacelike/timelike lattice-spacing structure cannot be silently collapsed where it matters.
- `FRG_IMPORT_CONTROL`: no FRG scale relation may be used to rescue a missing CDT calibration.

## Claim ceiling

A scoped PASS can establish only CDT-internal diffusion-scale authority and, if warranted, a finite-regulator physical-scale calibration. It cannot establish a CDT ultraviolet fixed point, the full CDT continuum theory, FRG/CDT equivalence, universal `d_s` flow, `BRIDGE_DERIVED`, `UNIVERSAL_COMMON_PARENT_FOUND`, new physics, or a candidate theory.

Predicates, classifications and controls are frozen before terminal adjudication.