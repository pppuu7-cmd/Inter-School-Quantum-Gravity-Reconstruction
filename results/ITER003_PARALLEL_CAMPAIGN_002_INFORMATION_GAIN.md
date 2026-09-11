# Iter003 Result — Campaign 002 / CEMR Causal-Channel Information Gain

Status: `NUMERICALLY_VERIFIED_SYNTHETIC`  
Date: 2026-09-12  
Workflow run: `34652677145` — **SUCCESS**

## 1. Scientific question

After the novelty audit, BH-002 CEMR is useful only if the independent causal channel does work that an entanglement/area inversion does not already do.

Campaign 002 tests criterion C1 in a synthetic linearized inverse problem:

- `phi` modes represent conformal-scale information;
- `q` modes represent nonconformal/light-cone/shear information;
- area data mix `phi` and `q` with controlled degeneracy;
- an independent causal channel directly constrains `q` in the proxy.

This is deliberately an identifiability benchmark, not a physical HRT/causal-set simulation.

## 2. Main result — no rank gain

Across all 24 jobs,

`mean_rank_gain = 0`.

The area-only design matrix was already formally full-rank. Therefore this campaign does **not** support the strongest possible C1 claim that adding causal data repairs a true rank deficiency.

This negative result is retained.

## 3. Strong conditioning gain in the near-degenerate regime

For degeneracy `d=0.999`:

### precise causal channel, sigma_causal=0.02

- area-only condition number: about `1999`;
- joint condition number: about `6.84`;
- conformal-sector variance reduction: about `250.6x`;
- conformal RMSE improvement: about `13.9x`.

### noisier causal channel, sigma_causal=0.10

- area-only condition number: about `1999`;
- joint condition number: about `97.1`;
- variance reduction: about `20.2x`;
- RMSE improvement: about `4.16x`.

Thus an independent causal channel can strongly regularize an *ill-conditioned but formally identifiable* area inversion.

## 4. Moderate degeneracy

At `d=0.99`:

- area-only condition number: about `199`;
- precise causal channel reduces it to about `6.67` and improves RMSE by about `4.36x`;
- noisier causal channel gives a weaker reduction to about `67.5` and RMSE improvement about `1.56x`.

The value of the causal channel therefore depends quantitatively on both pre-existing degeneracy and causal-channel precision.

## 5. Weak degeneracy / noisy causal channel

At `d=0.9`, area-only condition number is already about `19`.

With precise causal data (`sigma_causal=0.02`):

- condition number improves to about `5.38`;
- variance improves by about `3.13x`;
- RMSE improves by about `1.42x`.

With noisier causal data (`sigma_causal=0.10`):

- condition number only improves to about `16.0`;
- variance improves by about `1.16x`;
- mean RMSE improvement factor is `0.951`, i.e. this particular finite-seed average is slightly worse after adding the causal data.

This is important falsification behavior: adding a second channel is not automatically beneficial.

## 6. Revised CEMR criterion C1

Campaign 002 suggests splitting C1 into:

- `C1a — rank gain`: causal data remove a true null direction;
- `C1b — conditioning gain`: causal data sharply reduce a near-degeneracy / posterior variance even when rank is already full.

Campaign 002 supports only **C1b in the synthetic proxy**, not C1a.

## 7. Implication for the physical programme

A future source-defined causal/entanglement overlap test should report:

1. rank of each channel and the joint problem;
2. smallest singular values / condition number;
3. covariance reduction in metric parameters;
4. sensitivity to causal-channel uncertainty;
5. whether the causal data add a genuinely independent row space rather than repeat entanglement constraints.

A qualitative statement that “causality helps” is no longer sufficient.

## 8. Relation to the 2026 HEE inversion novelty firewall

Because covariant entanglement inversion can itself contain cross-leaf integrability and projected light-cone information in controlled settings, the physical CEMR programme must demonstrate that its chosen causal observable adds independent conditioning/obstruction beyond that information.

## 9. Current verdict

`BH-002 = RETAIN / CONDITIONING-GAIN ROUTE SUPPORTED_SYNTHETICALLY`.

But no new physics claim is authorized. The decisive remaining problem is to replace the abstract causal constraint with a concrete, source-defined causal observable in the **same regime** as the entanglement reconstruction.

## Claim lock

The dramatic condition-number improvements are properties of this constructed inverse problem. They establish a useful design criterion, not a physical result about spacetime.