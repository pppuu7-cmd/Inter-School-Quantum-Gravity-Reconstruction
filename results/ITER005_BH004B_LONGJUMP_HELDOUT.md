# ITERATION 005 — BH-004B Long-Jump Held-Out Transport

Date: 2026-09-12  
GitHub Actions run: `34665815765`  
Status: `SUCCESS / STRONG SUPPORT IN BOTH LONG-JUMP LANES`

## Design

New sizes and seeds were used with larger nested thinning jumps than Iteration 004:

- lane A: `p_parent=0.75 -> p_child=0.375`;
- lane B: `p_parent=0.75 -> p_child=0.25`;
- parent sizes `N=768,1152,1536`;
- seeds `701,702,703`;
- `9` jobs per lane, `18` total;
- child source projector/rank and closure target remained evaluation-only.

The same preregistered BH-004B natural/strong gates were reused unchanged.

## Aggregate results

### `0.75 -> 0.375`

- median rank relative error: `0.0500`;
- median mean principal cosine: `0.989998`;
- median minimum principal cosine: `0.937160`;
- median predicted/envelope projector-distance ratio: `0.487849`;
- median source norm captured by envelope: `0.976239`;
- median random/predicted leakage improvement: `3.17134x`;
- median random/predicted sequential-defect improvement: `6.51803x`;
- jobs improving both closure metrics: `9/9`;
- natural support: **YES**;
- strong support: **YES**.

### `0.75 -> 0.25`

- median rank relative error: `0.07895`;
- median mean principal cosine: `0.990514`;
- median minimum principal cosine: `0.946815`;
- median predicted/envelope projector-distance ratio: `0.424011`;
- median source norm captured by envelope: `0.977912`;
- median random/predicted leakage improvement: `3.21771x`;
- median random/predicted sequential-defect improvement: `7.28688x`;
- jobs improving both closure metrics: `9/9`;
- natural support: **YES**;
- strong support: **YES**.

## Interpretation

The causal-set envelope + local-selector factorization is not confined to the relatively local scale changes used in Iteration 004. It remains strong under two substantially larger nested-thinning jumps and on completely new sizes/seeds.

Notably, the larger `0.75 -> 0.25` jump does not degrade the principal-angle diagnostics or closure advantage in this campaign.

This substantially strengthens BH-004B inside the present causal-set realization.

## Claim lock

This remains one 1+1D free-field causal-set realization. Strong robustness across thinning ratios is not cross-school universality and is not a fundamental QG renormalization theorem.
