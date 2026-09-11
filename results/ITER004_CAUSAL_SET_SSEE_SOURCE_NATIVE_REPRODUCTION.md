# Iter004 Result — Source-Native 2D Causal-Set SSEE Reproduction

Status: `REPRODUCED_EXECUTABLE / SOURCE_NATIVE_SCOPED`  
Date: 2026-09-12  
Workflow run: `34653695608` — **SUCCESS**

## 1. Why this computation is different

Campaigns 001–004 used controlled synthetic inverse problems or abstract channel proxies to discover failure modes.

Campaign 005 instead implements a source-native causal-set/free-field construction:

`Poisson sprinkling`
`-> causal matrix C`
`-> G_R = C/2`
`-> Pauli-Jordan operator Delta = G_R - G_R^T`
`-> Sorkin-Johnston W = positive spectral part of iDelta`
`-> restrict to nested causal diamond`
`-> solve W v = lambda (iDelta) v`
`-> S = sum lambda log|lambda|`.

The spectral cutoff is fixed before entropy evaluation using the source-motivated rule

`|lambda(iDelta)| >= sqrt(N)/(4 pi)`,

applied first in the parent diamond and again after restriction to the nested diamond.

## 2. Campaign design

- parent causal-set sizes: `N = 128, 256, 512, 768`;
- six independent sprinkling seeds at each N;
- nested diamond side ratio: `1/2`;
- total matrix jobs: `24`;
- all matrix jobs and aggregate completed successfully.

## 3. Raw entropy reproduces spacetime-volume scaling

Using the four seed-averaged size groups, the fit

`S_raw = a N_sub + b`

gives

- slope `a = 0.30572`;
- `R^2 = 0.99836`.

Using all 24 individual realizations:

- slope `0.30368`;
- `R^2 = 0.98752`.

The mean raw entropies increase as

- parent N=128: `7.82`;
- N=256: `17.26`;
- N=512: `35.32`;
- N=768: `56.40`.

This reproduces the source-level qualitative statement that the untruncated causal-set SSEE scales with spacetime volume rather than the continuum 1+1D logarithmic/area-law behavior.

## 4. Frozen spectral rule changes the scaling class

After the source-motivated double spectral truncation, the group-mean fit

`S_trunc = a log(sqrt(N_sub)/(4 pi)) + b`

gives

- slope `a = 0.40188`;
- `R^2 = 0.98391`.

The source study reports a coefficient close to `1/3` in its larger/stated numerical regime. The present finite-size reproduction is not expected to match that coefficient exactly, but the fitted `0.402` is qualitatively and quantitatively consistent with movement toward the continuum logarithmic law.

The truncated mean entropies change only slowly with density:

- parent N=128: `1.528`;
- N=256: `1.681`;
- N=512: `1.846`;
- N=768: `1.878`.

By contrast, a linear-in-volume fit to the truncated individual data is weak (`R^2 ~ 0.50`) with slope only about `0.0020`.

## 5. Retained rank scaling

The parent double-sign retained spectral ranks grow much more slowly than N:

- N=128: mean retained rank `41`;
- N=256: `60`;
- N=512: `88.3`;
- N=768: `108`.

This is consistent with the source observation that the truncation removes a large population of near-zero modes and leaves a sublinear number of continuum-like modes.

## 6. BH-003 consequence

This computation strengthens BH-003 in a narrow but important sense:

> a spectral scale fixed independently of the target entropy values is sufficient, in this source-native 1+1D causal-set/free-field realization, to move the entropy from robust spacetime-volume scaling toward the expected continuum logarithmic scaling.

This is substantially stronger than the earlier synthetic CEMR tests because causal order, field commutator, state and entropy all belong to one realization.

## 7. What remains unresolved

The cutoff is not yet purely causal-set-native.

Its derivation uses:

- causal-set discreteness/density;
- the relation between continuum wavelength and Pauli–Jordan eigenvalues;
- source comparison of causal-set and continuum spectra.

Therefore this result does **not** yet establish that the spectral scale follows from causal-set dynamics alone.

The stronger BH-003 question remains:

> can a spectrum-internal or dynamical rule determine the same retained sector without importing the continuum target?

## 8. Next holdout gate

The frozen density rule now moves to H3 testing under `protocol/BH003_SPECTRAL_HOLDOUT_PROTOCOL.md`:

- change nested-region size ratio without changing the cutoff law;
- use new sprinklings and densities;
- fit entropy scaling only after the rule is frozen;
- do not retune the coefficient or threshold by region.

After H3, attempt an entropy-blind spectrum-internal break estimator `RK`.

## 9. Candidate-theory implication

This does not unlock an ISQGR gravitational action. It does, however, promote BH-003 from a purely conceptual bridge to an **executable same-realization bridge programme**.

Candidate model construction remains locked until the regulator/closure principle is shown to transfer beyond the calibration geometry and is related to gravitational rather than only free-field dynamics.

## Claim lock

This result reproduces a finite-size free-field causal-set phenomenon. It does not determine whether the raw volume law or the truncated continuum-like law is the fundamental UV entropy of quantum spacetime.