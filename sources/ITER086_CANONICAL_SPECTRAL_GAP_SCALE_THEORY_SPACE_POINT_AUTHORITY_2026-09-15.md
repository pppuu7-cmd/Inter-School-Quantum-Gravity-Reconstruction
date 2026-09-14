# ITER086 source authority — canonical spectral-gap scale ↔ reduced-map FRG theory-space point

Date: 2026-09-15
Gate: `ITER086_CANONICAL_SPECTRAL_GAP_SCALE_THEORY_SPACE_POINT_TEST`
Preregistration: `f54bb3238eb1a52923230537256e973936d82ec2`

## Frozen hypothesis

`H_gap`: the FRG scale `k` entering the already-qualified ITER078 reduced minisuperspace map is the Litim threshold of the **lowest strictly positive** normalized spatial Laplacian eigenmode of the same CDT ensemble,

`k^2 = z_1 = 9 ell_1/a^2`.

The preregistration explicitly froze `ell_1` before matched-data search and allowed round/de-Sitter spectral identities only as **held-out consistency checks**, never as fitting input.

## Algebraic closure from the preregistration

Combining `H_gap` with the ITER078 reduced map gives

`g_1 = (3/(8 pi)) ell_1 Gamma (omega/omega_0)^(4/3)`,

and

`lambda_1^FRG = [8 pi/(3*1.63)] (omega/omega_0)^(2/3) / [ell_1 sqrt(N_4)]`.

Thus the absolute lattice spacing cancels. This algebra is sound conditional on `H_gap`.

## Held-out self-consistent-background test

The direct CDT↔FRG source arXiv `2408.07808` defines the self-consistent Euclidean de-Sitter background of the Einstein-Hilbert EAA by

`R_k = 3/sqrt(Lambda_k) = 3/(sqrt(lambda_k) k)`.

It also states that the reduced minisuperspace treatment concerns global quantities and cites the result that, on compact space, only constant modes contribute to fluctuations of global quantities such as the three-volume. This is already a warning that a nonzero spatial Laplace mode is not itself the minisuperspace fluctuation mode.

For a round spatial `S^3` of radius `R_k`, the scalar Laplace-Beltrami spectrum is

`z_l = l(l+2)/R_k^2`,  `l=0,1,2,...`.

The lowest strictly positive mode is therefore

`z_1 = 3/R_k^2`.

Using the source-defined self-consistent radius,

`R_k^2 = 9/(lambda_k k^2)`,

hence

`z_1 = (lambda_k/3) k^2`.

The frozen hypothesis demands `z_1=k^2`. Therefore, in the very semiclassical round-de-Sitter limit to which the reduced map is anchored,

**`H_gap => lambda_k = 3`.**

This conclusion is independent of CDT target data, `Gamma`, `omega`, `N_4`, absolute `a`, and any spectral-dimension value.

## FRG-domain consistency

The same direct source warns that in most Einstein-Hilbert FRG approaches the beta functions become singular at `lambda_k=1/2` and treats the small-coupling/Gaussian regime with `lambda_k << 1`.

More specifically, the frozen foliated fluctuation source arXiv `2306.10408` has a singular locus at `lambda=1/2` and restricts the physically interesting connected region containing its main UV fixed point to `g>=0`, `lambda<=1/2`, below the second singular locus.

The preregistration forbids switching regulator/flow definitions merely to rescue a failed point. Although couplings from distinct background/fluctuation schemes must not be numerically identified as universal quantities, both frozen authorities make clear that `lambda=3` is not in the connected source-qualified Einstein-Hilbert domain used for the intended asymptotically safe flow comparison.

Thus `H_gap` does not merely lack calibration: its canonical threshold condition forces the reduced self-consistent geometry into the wrong FRG branch/domain already in the semiclassical consistency limit.

## Predicate adjudication

- A same-ensemble numerical tuple: **NOT CONSUMED / NOT NEEDED FOR FALSIFICATION**. The hypothesis fails a preregistered held-out analytic consistency condition before target-data use.
- B independent mode selection: **PASS_CONTROL** — `ell_1` was frozen prospectively.
- C exact algebra/no extra factor: **PASS**.
- D source-defined FRG domain: **FAIL_FOR_H_GAP** — self-consistent limit forces `lambda=3`, outside the intended connected EH flow domain and beyond the common `lambda=1/2` singular boundary.
- E multiple-point trajectory test: **MOOT AFTER ANALYTIC FAILURE**.
- F beta-flow ordering: **MOOT AFTER ANALYTIC FAILURE**.
- G spectral dimension held out: **PASS_CONTROL** — no `D_s` target was used.
- H continuum caveat retained: **PASS_CONTROL**.
- I matched-data absence is not used as evidence: **PASS_CONTROL**.

## Controls

- `MODE_SELECTION_CONTROL`: passed. No higher mode was substituted after failure.
- `SAME_ENSEMBLE_CONTROL`: passed vacuously; no mixed numerical tuple was constructed.
- `ABSOLUTE_A_REINTRODUCTION_CONTROL`: passed.
- `FRG_DOMAIN_RESCUE_CONTROL`: passed — no regulator/mode switching is attempted to avoid `lambda=3`.
- `DE_SITTER_GEOMETRY_CONTROL`: passed exactly as preregistered — round-sphere spectral geometry is used only as an out-of-sample consistency check.
- `SPECTRAL_DIMENSION_HOLDOUT_CONTROL`: passed.
- `TRAJECTORY_INITIAL_CONDITION_FIT_CONTROL`: passed.
- `BACKGROUND_PRODUCTION_CONTROL`: retained. The domain evidence from the fluctuation flow is corroborative; the decisive algebraic inconsistency already arises inside the direct reduced self-consistent-background construction.

## Source classification

**`FAIL_SCOPED_CANONICAL_GAP_SCALE_INCOMPATIBLE`**

The failure is narrow and constructive. It rejects only the canonical hypothesis that the **lowest nonzero spatial mode sits at the FRG cutoff threshold** of the reduced minisuperspace map. It does not reject ITER084's normalized spatial spectrum or ITER085's regulator-mode probe relation.

A weaker relation of the form `z_1/k^2 = F(lambda_k)` is in fact already suggested by the self-consistent de-Sitter geometry, where the round limit gives `z_1/k^2=lambda_k/3`. Any successor must freeze such a non-threshold relation before using CDT numerical values.

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**.
