# ITER159 manual source-convention adjudication

Date: 2026-09-17

Preregistration: `prereg/ITER159_PRIMARY_SOURCE_EXACT_CONVENTION_MANIFEST_2026-09-17.md`, commit `d741d367345c5c620f8981fb8ed9fd0d87e8dc71`.

Latest checked execution head: `9d098d19b57e81d9c0a5bcbec5efa076ea22714c`.

Run: `35230270651`.

Artifact: `10500703567`, `iter159-frob-primary-source-conventions`.

Artifact ZIP SHA256: `0a6daac0e655b02c8898395ebb832e249b28938cbc863b486ab72547f6cc47dc`.

Exact evidence JSON SHA256: `bc6253707d784102f8a30016900e765e67f70eb80c32d546fe256605eb0c2a56`.

Frozen source identity: arXiv:1706.01891v2.

Downloaded source archive SHA256 recorded by the run: `b3c0137deb5e599912e0dfc96c2c6375c4715ad5e561c5cb795dae43902b03fd`.

Primary TeX `scalar-oneloop-cqg.tex` SHA256: `120bc07d42b8e30d103a46058270010316f7cb332575b33867ed4a8598ff335a`.

## What the successful extraction establishes

The exact-source evidence set contains source-level material for, among other items:

- `g_{mu nu} = eta_{mu nu} + kappa h_{mu nu}` and `kappa^2=16 pi G_N`;
- the two-parameter linear gravitational gauge-fixing action (`alpha`, `beta`);
- dimension `n` and dimensional regularisation around `n=4`;
- momentum-space denominators `p^2-i0`, loop measure `d^n k/(2pi)^n` and Fourier factor `exp(i p (x-y))`;
- affine geodesic parameter `tau`, starting point, initial tangent and endpoint `tau=1`;
- perturbative geodesic normalization and first-order geodesic equation;
- the fact that the paper's observable is a scalar two-point function at fixed fluctuating geodesic distance.

The run correctly emits `PENDING_MANUAL_SOURCE_CONVENTION_ADJUDICATION` and `automatic_scientific_pass=false`.

## First unresolved frozen convention field

The ITER159 preregistration orders `metric signature` as the first required convention field.

The exact run emitted **zero** source-evidence rows for `metric_signature`. No separately persisted, source-faithful mathematical derivation of the sign of `eta_{mu nu}` from explicit source definitions exists in the ITER159 record.

This audit does **not** claim that arXiv:1706.01891v2 contains no recoverable signature information. It claims only what the frozen gate requires: the current exact convention manifest does not source-faithfully fix this first required field.

Standard-convention inference is not accepted as primary-source authority under the frozen rule.

Later convention fields therefore need not be promoted to complete for this terminal decision. In particular, the broad regex category `curvature_convention` is not itself proof of an explicit Riemann/Ricci sign definition.

## Terminal classification

**`BLOCKED_SCOPED_ITER159_SOURCE_CONVENTION_MANIFEST_INCOMPLETE_METRIC_SIGNATURE`**

Minimal missing primitive for this gate:

> a persisted primary-source statement, or an explicit mathematical derivation solely from persisted primary-source definitions, that fixes the sign of the flat metric `eta_{mu nu}` without importing a secondary-source convention.

This is a source-manifest blocker, not a physical FAIL and not a zero coefficient.

## Scientific firewall remains active

Even if a later repair closes the convention manifest, Fröb's source computes a scalar-matter two-point function at fixed geodesic distance, not the frozen curvature-composite first-M/G endpoint amplitudes. Therefore its coefficients remain `REFERENCE_ONLY` unless exact operator/topology equivalence is separately demonstrated.

No scalar-matter coefficient is imported into the ITER118 endpoint basis.

## Relation to ITER158 audit

ITER159 performs genuine primary-source acquisition and is therefore scientifically useful despite the separate `INVALID_ITER158` implementation audit. It does not retroactively validate the automated ITER158 BLOCKED label.

## Claim locks

`B1_total = UNAUTHORIZED`; `BRIDGE_DERIVED=false`; `NEW_PHYSICS_FOUND=false`; candidate theory remains `UNFORMED / 0%`.
