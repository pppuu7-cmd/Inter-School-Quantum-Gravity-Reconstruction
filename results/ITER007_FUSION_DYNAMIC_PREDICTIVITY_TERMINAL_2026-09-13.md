# ITER007 — fusion dynamic predictivity terminal classification

Recovered and consumed on 2026-09-13 from validated Actions evidence that had not been fully reflected in the active recovery front.

## Authoritative run
- implementation/workflow commit: `250147344b252c1d158bb8fd657046e4dc10e95b`
- workflow: `ISQGR Fusion Dynamic Predictivity Audit`
- run: `34676760272`
- matrix: 12 independent lanes = 2 tests × 6 couplings, `g={0,0.25,0.5,0.75,1.0,1.15}`
- aggregate job: `103508171070`
- summary artifact: `10292547840`
- summary digest: `sha256:6741b889fa004f94043da26549feaf46e3577fb273165fd15a41dc2b9d8f256b`

All 12 lane jobs and aggregate completed successfully. Raw lane artifact digests were consumed from the aggregate log / Actions metadata.

## Frozen tests and results
### Continuous ribbon-amplitude predictivity
Frozen aggregate support required median fraction of RG steps where all metrics exceed the permutation p95 to be >=0.6 and at least 4/6 couplings to have majority significant steps.

Observed:
- median fraction = `0.0`
- fraction of couplings with majority significant steps = `0.0`
- support = `false`

Each of the six couplings had `fraction_steps_all_metrics_above_permutation_p95 = 0.0`.

### Cross-lag incremental predictivity
Frozen aggregate support required median fraction of steps above permutation p95 >=0.6, median L1 improvement >0, and at least 4/6 couplings with majority significant steps.

Observed:
- median fraction above permutation p95 = `0.0`
- fraction of couplings with majority significant steps = `0.0`
- median mean L1 improvement = `-0.8561568629900482`
- support = `false`

All six couplings had zero positive-improvement fraction; mean L1 improvements were negative, ranging from about `-0.889` at g=0 to `-0.537` at g=1.15.

## Scientific classification
`SCOPED_NEGATIVE_FUSION_DYNAMIC_SELECTOR_PREDICTIVITY`

This is a substantive negative result for the tested nearest-framework q-deformed lattice-gauge/TNR realization: neither the continuous ribbon-sector amplitude/ranking observable nor the frozen cross-lag SVD augmentation provides the preregistered predictive support beyond permutation/persistence controls.

It extends the prior binary ribbon-support null result and means this fusion-basis selector path should not receive bridge credit or be repeated with denser sampling absent a new source-motivated observable/dynamical object.

## Scope locks
This is not a no-go theorem for BH-004/BH-004B, EPRL/FK gravity, source-native selectors in general, tensor-network renormalization, or quantum gravity. It is a nearest-framework control only. `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, candidate theory, and cross-school universality remain unauthorized.
