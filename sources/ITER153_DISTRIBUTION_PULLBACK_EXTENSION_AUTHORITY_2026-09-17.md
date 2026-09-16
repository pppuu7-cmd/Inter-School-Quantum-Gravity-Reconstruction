# ITER153 source authority — distributional pullback, extension, and fixed-geodesic restriction

Date: 2026-09-17
Preregistration parent: `bbcb9021e0245f3a506efa072d90cff992177126`
Gate: `ITER153_FIXED_GEODESIC_CURVATURE_ENDPOINT_CONTACT_DISTRIBUTIONAL_EXTENSION_AUTHORITY`

This authority record is frozen after preregistration and before the ITER153 contact outcome. It supplies mathematical rules only; it does not contain or select a desired contact residue.

## 1. Microlocal pullback rule

We use the standard Hörmander distributional pullback criterion. For a smooth map `F:X->Y`, define the normal set

`N_F = {(F(x), eta) : eta != 0, (dF_x)^T eta = 0}`.

If `WF(u) intersect N_F` is empty, the pullback `F^*u` is canonically defined. For an embedding this is the familiar condition that the wavefront set avoid covectors conormal to the embedded submanifold.

Source identity: L. Hörmander, *The Analysis of Linear Partial Differential Operators I*, Theorem 8.2.4, as restated in standard microlocal-QFT treatments. The theorem is used as a sufficient canonical-authorization criterion. Failure of the criterion is not promoted here to a universal theorem of nonexistence for every possible extra prescription; it means the ordinary canonical pullback is not authorized by this theorem.

## 2. Delta-distribution wavefront class

For a point-supported Dirac distribution at the origin in `R^4`,

`WF(delta_0) = {(0,xi): xi != 0}`.

Finite nonzero derivatives of `delta_0` have the same wavefront cone: differentiation may change order but does not remove the point-supported conormal singular directions relevant to the pullback test.

For a line embedding `F(s)=sigma L s n`, `L>0`, `n^2=1`,

`(dF_s)^T xi = sigma L (n.xi)`.

Thus its normal set at the coincidence point contains every nonzero covector with `n.xi=0`.

This is the exact geometric test used by ITER153; the implementation must compute the nonempty transverse normal subspace directly rather than hard-code the gate outcome.

## 3. Scaling degree / local-extension theorem

Brunetti and Fredenhagen, arXiv:math-ph/9903028, develop the local extension of distributions in perturbative QFT using scaling degree. The relevant result is the standard point-extension theorem: a distribution on `R^D\{0}` with finite scaling degree has an extension preserving scaling degree; below dimension `D` the extension is unique, while at or above the dimensional threshold the extension has finite local freedom given by derivatives of Dirac delta up to the degree of divergence.

Nguyen Viet Dang, arXiv:1412.2808, generalizes extension theory to closed embedded submanifolds and microlocal control of the extension wavefront set.

For an ambient Dirac derivative,

`sd(partial^alpha delta^(D)) = D + |alpha|`.

This records singular strength but does not create a line pullback when the pullback hypothesis fails.

## 4. Fixed-geodesic source context

Markus B. Fröb, arXiv:1706.01891, *One-loop quantum gravitational corrections to the scalar two-point function at fixed geodesic distance*, studies fields restricted to a perturbative geodesic. The source explicitly identifies the fixed-geodesic observable as nonlocal and strongly divergent and obtains a finite answer only after a dedicated wave-function renormalization of the geodesic embedding coordinates. The repository's frozen ITER107 authority further records that restricting field-theoretic distributions to the one-dimensional geodesic produces new divergences not removed by ordinary bulk counterterms alone.

This source is evidence against treating a geodesic restriction as a passive substitution or assigning unsupported contact terms zero. It does not provide the curvature-contact residues needed by ITER153.

## 5. Application to a denominator-cancelled endpoint contact

For the frozen denominator `Q*K`, a Q-cancelled term is polynomial in q times the remaining K-propagator; a K-cancelled term is polynomial in k times the remaining Q-propagator. Under Fourier transformation of the cancelled momentum, a polynomial of total degree `m` yields an order-`m` derivative of an ambient Dirac distribution, contracted with the surviving momentum and `n` tensors.

This statement is a Fourier/distribution identity and is not the ITER126 endpoint-power prototype. No numerical prototype residue is imported.

The ITER153 problem is then a restriction/pullback problem of that ambient point-supported contact to the frozen geodesic line map, followed—only if an authorized line distribution exists—by Laurent extraction in `d=4-2 epsilon`.

## 6. Independent regularization diagnostic

As an independent diagnostic of canonical line restriction, a smooth approximate identity for an ambient delta may be pulled back to the line before removing its width. For example in four dimensions,

`delta_eta^(4)(x) = (pi*eta^2)^(-2) exp(-|x|^2/eta^2)`

gives along `x=L s n`

`delta_eta^(4)(L s n) = pi^(-2) eta^(-4) exp(-L^2 s^2/eta^2)`.

Pairing with a one-dimensional test function and rescaling `s=(eta/L)u` has leading magnitude proportional to `eta^(-3)/L`; derivatives of the ambient delta raise the negative power further. Hence the naive line restriction has no regulator-independent distributional limit without subtraction/local renormalization data. The exact coefficient depends on the chosen approximate identity and derivative contraction, so this diagnostic may establish need for extra local input but may not be used as a numerical renormalization prescription.

## 7. Claim discipline

- The Hörmander condition is a canonical pullback authorization criterion, not an excuse to claim universal impossibility of every generalized extension.
- A smoothing or analytic regulator introduced only inside ITER153 is a diagnostic unless the frozen parent theory/source uniquely selects it.
- Scaling-degree extension freedom is local renormalization freedom and must not be fixed by desired cancellation.
- A missing source-qualified line distribution is `BLOCKED_SCOPED`, not a derived zero.
- No ITER126 prototype residue is transferable.
- Counterterm subtraction, line mixing and `B1_total` remain downstream.