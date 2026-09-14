# ITER092 terminal result — retrospective kappa4 pseudocritical scaling eigendirection adjudication

Date: 2026-09-15
Gate: `ITER092_RETROSPECTIVE_KAPPA4_PSEUDOCRITICAL_SCALING_EIGENDIRECTION_ADJUDICATION`
Protocol: `b1fa8614840fd5b5cc0762a989b42a5d7110a04b`
Source authority: `886d8d3e30e4dc00481da11717a19545957e7921`
Adversarial review: `b7d698a70a1053a9e397bc77fd19c426f28c039d`

## Terminal classification

**`SOURCE_SUPPORTS_MIXED_PSEUDOCRITICAL_SHIFT_NOT_INDEPENDENT_COSMOLOGICAL_DIRECTION`**

Prospective validation credit: **0** by protocol.
Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Published result

The toroidal CDT B-C transition source fits

`Delta^crit(Nbar_41)=Delta^crit(infinity)-A Nbar_41^(-1/gamma)`

with

`gamma_Delta=1.64+/-0.18`,

and

`K_4^crit(Nbar_41)=K_4^crit(infinity)-B Nbar_41^(-1/gamma)`

with

`gamma_K4=1.62+/-0.25`.

It also reports an approximately linear relation between the pseudocritical `K_4` and `Delta` coordinates and explicitly states that both scale in the same way with lattice volume.

## Interpretation

This is real finite-size scaling authority for the bare `K_4` coordinate, but it does not isolate a pure cosmological RG eigendirection.

The source evidence is naturally described as a **mixed pseudocritical transition displacement** in multi-coupling bare parameter space whose components are visible in both `Delta` and `K_4`.

A bare coordinate being cosmological in the Regge action does not make that coordinate an eigenvector of the continuum RG stability matrix.

## What ITER092 adds to ITER091

ITER091's statement `renormalized cosmological map open` can now be sharpened:

- a nontrivial finite-size exponent for the `K_4` pseudocritical coordinate is measured;
- but the same exponent appears in `Delta`, so a scalar `K_4` exponent does not separate the cosmological direction;
- the missing object is the **scaling-field mixing/eigenvector structure** near a candidate continuum transition.

## Claim ceiling

No FRG critical exponent, no pure cosmological eigendirection, no separate `lambda_k`, no shared fixed point, no bridge derivation and no candidate theory follow.

## Highest-information successor

Audit whether CDT sources expose enough **joint thermodynamic response information** for the bare action observables conjugate to `(kappa_0,Delta,kappa_4)` to construct local scaling-field directions rather than using coordinate axes.

The natural object is the connected covariance/Fisher matrix of the action observables (or an equivalent multi-coupling response matrix), with the artificial volume-fixing contribution removed. A useful PASS would require source-qualified cross-covariances/eigenvectors near a candidate continuous transition, not merely separate susceptibilities.
