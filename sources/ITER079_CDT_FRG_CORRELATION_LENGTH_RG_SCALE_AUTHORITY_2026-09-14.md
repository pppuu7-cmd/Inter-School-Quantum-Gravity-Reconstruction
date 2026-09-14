# ITER079 source authority — CDT correlation length ↔ FRG RG-scale

Date: 2026-09-14
Gate: `ITER079_CDT_FRG_CORRELATION_LENGTH_RG_SCALE_AUTHORITY`
Preregistration commit: `87c23a0ff5dcc134b7b98e588951c58f0c158b07`

## Frozen source stack

Direct CDT↔FRG scale analysis:
- arXiv:2408.07808 — J. Ambjørn, J. Gizbert-Studnicki, A. Görlich, D. Németh, *Is Lattice Quantum Gravity Asymptotically Safe? Making contact between Causal Dynamical Triangulations and the Functional Renormalization Group*.
- arXiv:2411.02330 — J. Ambjørn, J. Gizbert-Studnicki, A. Görlich, D. Németh, *IR and UV limits of CDT and their relations to FRG*.

CDT scale/continuum authority:
- arXiv:1603.02076 — J. Ambjørn, D. Coumbe, J. Gizbert-Studnicki, J. Jurkiewicz, *Searching for a continuum limit in causal dynamical triangulation quantum gravity*.
- arXiv:2604.05641 — J. Ambjørn, R. Loll, *Causal Dynamical Triangulations: New Lattice Theory of Quantum Gravity*.

FRG scale semantics:
- arXiv:2302.14152 — F. Saueressig, *The Functional Renormalization Group in Quantum Gravity*.

## Executive result

The frozen stack does **not** establish an independently operational one-to-one map between the CDT geometric correlation length and the FRG coarse-graining scale `k`.

It does establish a weaker, nontrivial reduced scaling relation among:

- the CDT finite-size/geometric correlation length `xi ~ N_4^(1/4)`;
- the lattice cutoffs `a` and `a_t`;
- the reduced FRG coupling combination `lambda_k g_k`;
- the FRG parameter `k` through the direct minisuperspace map.

The direct follow-up explicitly states that the resulting `a proportional_to 1/k` behavior is **only dimensional**; the physical content is instead that for fixed `k` / fixed `lambda_k g_k`, the lattice cutoff tends to zero when the CDT correlation length diverges.

Therefore the source-authority classification is:

**`PASS_SCOPED_REDUCED_SCALE_RELATION_ONLY`**

with mandatory lock:

**`OPERATIONAL_CDT_XI_TO_FRG_K_MAP = NOT_ESTABLISHED`**.

Bridge credit remains zero.

## A — CDT correlation-length object

**PASS_SCOPED.**

The direct sources do not import an ordinary matter propagator correlation length into gravity. They construct a gravitational/geometric analogue from the two-point function of fluctuating geometries and finite-size scaling.

In the four-dimensional CDT de-Sitter phase the volume/three-volume two-point observables exhibit scaling with the linear size of the ensemble. With Hausdorff dimension approximately four, the direct source identifies

`xi_CDT proportional_to N_4^(1/4)`

as the relevant dimensionless correlation-length scale.

The follow-up is explicit about the qualification: this correlation length is tied to correlations between spacetime points/geodesic separation in the ensemble and is **not** the propagation length of an ordinary field degree of freedom. It also notes that in practical finite-size scaling one does not measure a separate exponential correlation length; one uses the scaling behavior as evidence that `N_4^(1/d_H)` plays this role.

## B — finite-size and critical scaling

**PASS_SCOPED.**

The direct sources use `N_4^(1/4)` as the finite-size correlation-length variable and derive pseudocritical scaling toward the candidate `A-C_dS` critical locus. The measured bare-coupling shift and the reduced observables `omega`, `Gamma`, and `omega^2 Gamma` are analyzed as functions of `N_4` and distance from the transition.

The numerical critical exponents retain substantial transition-order and hysteresis uncertainties. The source explicitly warns that the data do not settle the UV fixed-point question.

## C — dimensionless xi, lattice cutoff and physical gravitational length

**PASS_SCOPED / MODEL-DEPENDENT.**

The direct source writes the physical scaling relation

`xi_CDT * a proportional_to ell_phys = V_4^(1/4)`

within the de-Sitter finite-size-scaling construction, with `xi_CDT ~ N_4^(1/4)`.

This supplies a source-defined distinction between:

- dimensionless correlation length in lattice units;
- lattice spacing/cutoff `a`;
- physical/global length extracted from the four-volume.

The relation remains part of the reduced de-Sitter/finite-size description and does not establish a universal local correlation length for all CDT observables.

## D — FRG k semantics

**PASS.**

The FRG review defines `k` as the coarse-graining scale of the Effective Average Action. Dimensionful couplings are converted to dimensionless theory-space coordinates using powers of `k`, and RG trajectories are maps `k -> Gamma_k`.

The regulator makes the flow trace peak at momenta `p^2 approximately k^2`, so the running at scale `k` integrates fluctuations of momenta comparable to that coarse-graining scale.

Thus `k` has an explicit regulator/mode-resolution meaning. It is not merely an arbitrary inverse length and is not the same object as a lattice spacing or a geometric two-point correlation length.

## E — independent operational xi <-> k matching condition

**NOT ESTABLISHED.**

This is the decisive missing predicate.

The 2024 direct paper states that it is unclear whether the CDT critical exponent can be directly compared with its FRG counterpart because the authors do not know the precise connection between the CDT correlation length

`xi proportional_to N_4^(1/4)`

and the FRG scale `k`.

The follow-up devotes a section to the **enigmatic relation between `a` and `k`**. It derives near-UV formulas in which `a` and `a_t` contain factors proportional to `1/k`, but then explicitly says that

`a proportional_to 1/k`

is only a dimensional relation.

No separate physical observable is used to select a unique FRG `k` for a given measured CDT `xi`.

## F — validity range of the reduced relation

**PASS_SCOPED.**

The direct relations are derived in the simplest Einstein-Hilbert/minisuperspace comparison, with separate discussion of:

- the generic infinite-volume/IR limit inside phase `C_dS`;
- the candidate UV scaling trajectory near the `A-C_dS` boundary;
- finite-size pseudocritical scaling.

The relation is not claimed as a global full-theory scale map.

## G — cutoff, correlation length and RG scale remain distinct

**PASS_CONTROL.**

The sources themselves preserve the distinction:

- `a^{-1}` is the lattice UV cutoff;
- `xi_CDT` diverges in lattice units toward criticality;
- `k` is the FRG coarse-graining parameter;
- at fixed reduced FRG coupling/`k`, the continuum lattice limit is represented by `a -> 0` while `xi_CDT -> infinity`.

The statement `a ~ 1/k` is not allowed to collapse these three objects.

## H — independent common observable for scale setting

**NOT ESTABLISHED.**

The frozen stack does not add a new held-out physical observable that independently fixes the value of `k` corresponding to a CDT ensemble.

The four-volume/radius and reduced coupling combination used in the direct comparison are the same reduced sector already used to construct the ITER078 parameter map. Reusing them cannot count as independent validation of the scale identification under the preregistered circularity control.

## I — critical-exponent comparison

**NOT AUTHORIZED AS CROSS-FRAMEWORK EQUALITY.**

The CDT source extracts candidate critical exponents. The authors themselves say the precise `xi` ↔ `k` relation is missing, so direct comparison with FRG critical exponents is not yet justified.

Similar exponent values, when present, cannot substitute for predicate E.

## J — regulator/truncation and anisotropy

**PASS_AS_SCOPE_LOCK.**

The reduced relation retains:

- CDT lattice cutoff and finite-size scaling;
- the distinct temporal/spatial scales encoded by `omega` where needed;
- the FRG regulator and Einstein-Hilbert truncation;
- reduced minisuperspace scope.

No scheme-independent full-theory scale identity is claimed.

## K — 2026 current-status authority

**PASS_AS_EVIDENCE UPDATE, NOT MAP AUTHORITY.**

The 2026 CDT review strengthens the evidence that `N_4^(1/4)` functions as a correlation length and that a candidate UV critical path may exist. It also uses the reduced dimensionless coupling `Lambda G` in the finite-size interpretation.

This does not supply the missing independent physical matching condition between `xi_CDT` and FRG `k`. Current evidence for critical scaling therefore cannot retroactively close predicate E.

## Mandatory-control audit

- `DIMENSIONAL_INVERSE_LENGTH_CONTROL`: **triggered successfully**; `a ~ 1/k` receives no operational-map credit.
- `LATTICE_SPACING_CORRELATION_LENGTH_SWAP_CONTROL`: **passes**; `a` and `xi` remain distinct.
- `PROPAGATOR_GEOMETRIC_XI_SWAP_CONTROL`: **passes**; the gravitational correlation length is explicitly nonstandard.
- `FIXED_K_FIXED_PHYSICS_CONTROL`: **passes**; fixed `k` with `a -> 0`, `xi -> infinity` is recorded as continuum scaling, not scale identity.
- `CRITICAL_EXPONENT_PREMAP_CONTROL`: **triggers**; exponent equality is not authorized.
- `REDUCED_FULL_SCALE_CONTROL`: **passes**; scope remains minisuperspace/reduced.
- `COMMON_UNIT_CONTROL`: **passes**; common length dimensions do not create the map.
- `TARGET_OBSERVABLE_CIRCULARITY_CONTROL`: **triggers**; ITER078 reduced observables are not counted as independent scale validation.
- `REGULATOR_ERASURE_CONTROL`: **passes**.
- `UV_FIXED_POINT_PROMOTION_CONTROL`: **passes**; UV remains candidate/evidence-level.

## Why this is a partial PASS rather than full BLOCKED

The frozen stack goes beyond a mere absence statement. It provides a nontrivial source-derived relation among `xi_CDT`, `a`, `N_4`, `k` and the reduced FRG coupling combination, and it states the physical continuum-scaling content at fixed reduced coupling.

What it explicitly does **not** provide is the stronger operational map assigning the same physical resolution to a unique pair `(xi_CDT, k)` independently of the reduced-action construction.

This matches the preregistered class:

**`PASS_SCOPED_REDUCED_SCALE_RELATION_ONLY`**.

## Claim ceiling

ITER079 does not establish a common RG coordinate, direct critical-exponent equality, a shared/proven UV fixed point, full CDT/FRG equivalence, `BRIDGE_DERIVED`, a universal common parent, new physics or a candidate theory.