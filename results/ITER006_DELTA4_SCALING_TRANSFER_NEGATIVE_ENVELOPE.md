# ITERATION 006 — Lorentzian EPRL Delta4 scaling/transfer envelope

Date: 2026-09-12
Status: **SCIENTIFIC NEGATIVE / BOUNDARY CLASSIFICATION**
Candidate theory impact: **none** (`UNFORMED`)

## Scope

All tests below use the public four-vertex Lorentzian EPRL `Delta_4` data from `PietropaoloFrisoni/HowToSpinFoamAmplitude`, pinned at commit `4fa7e31ffc6553e56da94a443a53a4059a5d2035`. These are finite shell-cutoff convergence tests. They are **not** a refinement/coarse-graining map and cannot promote `BRIDGE_DERIVED`.

## 1. Boundary-spin scaling-class gate — failed

Authoritative run: `34692390732`  
ISQGR commit: `72a9936846370e0ce6a9a0749aee575d46414da6`

A boundary-spin-specific exponent model reduced median chronological held-out error relative to one global exponent by about **40.8%**, but the frozen aggregate gate failed:

- j-specific model beats global: **17/24**, threshold was `>=18/24`;
- median alpha for `j=0.5`: `3.7628106593`, relative regime spread `0.5218629616` (> `0.35` threshold);
- median alpha for `j=1.0`: `5.2418963438`, relative regime spread `0.3544765354` (also > `0.35`);
- median relative alpha separation: `0.3285138948`;
- `alpha_j_regime_stable = false`.

**Decision:** retain the signal but reject the preregistered claim of a stable two-class boundary-spin scaling law.

## 2. Cross-gamma held-out transfer — failed

Implementation commits:

- `f1f25612bb405547f8ecc94478a1f02567b13e7c` — analysis code;
- `085a7b60e40c7f2678a68e2459e7c7ab3a40204d` — 24-lane workflow.

Authoritative run: `34693763297`  
Tasks: **72** = 6 tail windows x 4 holdout windows x 3 held-out Immirzi sectors.

Frozen slopes were trained only on two gamma sectors and transferred to the third; the held-out sector could calibrate only an intercept on its early prefix. A swapped-boundary-spin null was evaluated in parallel.

Aggregate:

- all `72/72` tasks identifiable;
- median correct-j improvement vs global: about **+16.7%**;
- correct-j beats global: **52/72**;
- median correct-j improvement vs swapped-j null: about **+44.4%**;
- correct-j beats swapped-j: **61/72**;
- per-held-out-gamma median correct-j vs global:
  - `gamma=0.1`: about **-37.1%**;
  - `gamma=1.0`: about **+59.7%**;
  - `gamma=1.2`: about **+20.9%**.

The frozen gate required positive median transfer in **every** held-out gamma sector. Therefore this is a **scientific FAIL**, not a near-pass.

**Decision:** there is finite-cutoff boundary-spin structure, but no supported universal j-specific exponent transfer across all three Immirzi sectors.

## 3. `gamma=0.1` separate-crossover explanation — failed

Implementation commits:

- `437c55e07689c80d5dfd0a5fb077266230bebfeb` — diagnostic code;
- `93397d7ce77a46dd5086a0bc128323f644d46de2` — workflow.

Authoritative run: `34694130700`  
Job: `103554553372`  
Artifact: `10297842263`  
Artifact SHA256: `515ca67bbcbac78334ad0756de233a801aac1306cf4523d5e351677ccdc38887`

This diagnostic was explicitly forbidden from rescuing the failed cross-gamma gate. It tested whether `gamma=0.1` alone had a training-identifiable log-log slope crossover.

Results:

- `gamma=0.1, j=1`: crossover support; median piecewise-vs-single improvement `0.7141537148`, slope separation `0.3084707098`;
- but similar crossover support also occurs at:
  - `gamma=1.0, j=1`: median improvement `0.8802745149`, separation `0.3419726857`;
  - `gamma=1.2, j=1`: median improvement `0.7314897105`, separation `0.3140720142`;
- all `j=0.5` trajectories are shorter (`Dl_max=15`), and only two of four requested holdout windows are identifiable.

Aggregate `gamma01_separate_crossover_pattern_support = false`.

**Interpretation:** crossover behaviour tracks the longer `j=1` cutoff trajectory at least as strongly as it tracks `gamma=0.1`; the special-low-gamma explanation is rejected.

## Saturation decision

The existing Delta4 scaling tables have now been tested by:

1. global vs boundary-spin scaling;
2. chronological held-out prediction;
3. cross-gamma transfer;
4. swapped-spin null;
5. gamma-specific crossover diagnostics.

The scaling-fit front is therefore **saturated**. Additional fits to the same tables are low information gain unless new raw multi-vertex data, a true refinement map, or a distinct source-defined observable is introduced.

## Claim lock

These negative results do **not** invalidate Lorentzian EPRL. They only reject the tested finite-cutoff scaling/universality interpretations on this pinned four-vertex dataset. They do not authorize candidate theory construction, `BRIDGE_DERIVED`, or new-physics claims.
