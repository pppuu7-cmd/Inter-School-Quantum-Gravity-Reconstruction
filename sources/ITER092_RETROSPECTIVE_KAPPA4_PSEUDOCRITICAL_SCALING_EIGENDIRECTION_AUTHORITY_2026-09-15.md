# ITER092 source authority — retrospective kappa4 pseudocritical scaling eigendirection adjudication

Date: 2026-09-15
Protocol: `b1fa8614840fd5b5cc0762a989b42a5d7110a04b`

## Published finite-size result

arXiv `1906.04557` / JHEP07(2019)166 studies the toroidal CDT B-C transition over lattice volumes up to `Nbar_41=1600k`.

For the transition displacement in `Delta`, the source fits

`Delta^crit(Nbar_41) = Delta^crit(infinity) - A Nbar_41^(-1/gamma)`

and obtains

`gamma_Delta = 1.64 +/- 0.18`.

The paper then reports that the pseudocritical bare cosmological coupling behaves very similarly and fits

`K_4^crit(Nbar_41) = K_4^crit(infinity) - B Nbar_41^(-1/gamma)`

with

`gamma_K4 = 1.62 +/- 0.25`,

consistent with the `Delta` result.

It explicitly states that the dependence of `K_4^crit` and `Delta^crit` is approximately linear along the two sides of the hysteresis and that **both pseudocritical parameters scale in the same way with lattice volume**.

## Interpretation under ITER091 controls

This is genuine four-dimensional CDT finite-size source authority for the `K_4` coordinate. It is stronger than merely saying that `K_4` must be tuned with volume.

However, the measured exponent belongs to the displacement of the **phase-transition location in the multi-coupling bare parameter space**. The same exponent appears simultaneously in `Delta`, and the source does not diagonalize a renormalization-group stability matrix or construct a pure cosmological scaling field orthogonal to the other bare directions.

Thus the data are naturally consistent with a single mixed scaling direction whose components are visible in both `K_4` and `Delta`. They do not establish that the bare coordinate axis `K_4` itself is an RG eigendirection.

## Why the exponent is not yet a renormalized cosmological exponent

A phase-transition shift exponent answers how a pseudocritical point approaches its infinite-volume location as the finite system grows. A renormalized cosmological eigendirection would require, in addition:

1. a source-defined scaling field, generally a linear/nonlinear combination of bare couplings near the critical point;
2. its normalization/mixing relative to the other bare coupling directions;
3. a continuum RG eigenvalue or response relation;
4. for cross-framework use, a typed map to the FRG stability eigendirection/cosmological coupling.

None of these is constructed from `K_4^crit(N)` alone in the frozen source.

The result therefore improves ITER091 by supplying a measured pseudocritical scaling law, but it does not supply the missing independent renormalized cosmological direction.

## Distinction from critical cosmological subtraction

The standard CDT continuum motivation writes the bare critical subtraction schematically as a physical cosmological term, e.g. `kappa_4-kappa_4^c` multiplying the physical volume after suitable powers of the lattice spacing. That is a continuum scaling ansatz/interpretation of the cosmological source.

The 2019 exponent above instead describes the **finite-volume shift of the phase-transition location** in the coupled `(Delta,K_4)` plane. These two statements are not the same observable and cannot be interchanged without an additional source derivation.

## Predicate adjudication

- A published `K_4^crit` fit form/exponent: **PASS**, `gamma=1.62+/-0.25`.
- B corresponding `Delta^crit` shift: **PASS**, `gamma=1.64+/-0.18`.
- C source says they scale together: **PASS**.
- D transition shift versus cosmological renormalization kept distinct: **PASS_CONTROL**.
- E no FRG critical-exponent identification: **PASS_CONTROL**.
- F bare cosmological semantics do not create eigendirection purity: **PASS_CONTROL**.

## Source classification

**`SOURCE_SUPPORTS_MIXED_PSEUDOCRITICAL_SHIFT_NOT_INDEPENDENT_COSMOLOGICAL_DIRECTION`**

Prospective validation credit: **0** by protocol.
Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Highest-information successor

The missing object is now sharper: not another scalar exponent, but the **local mixing/eigenvector structure of bare couplings near a candidate continuous CDT transition**.

A useful successor should ask whether source data determine the tangent/normal directions of the pseudocritical surface (or a multi-observable response matrix) well enough to construct scaling fields as combinations of `kappa_0`, `Delta`, and `kappa_4`, rather than treating any bare coordinate axis as an RG eigendirection.
