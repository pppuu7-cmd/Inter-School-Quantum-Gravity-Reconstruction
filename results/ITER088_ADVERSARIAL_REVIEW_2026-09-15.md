# ITER088 adversarial review — retrospective CdS spatial-gap scaling

Date: 2026-09-15
Protocol: `385f70a3c24f3f4dc39a5ba8e2380516786ad5d7`
Source authority: `152d258b9919f1958beb80206d776363e7d4a9cd`

## Attack 1 — unknown absolute normalization can turn `d_eff=1.6` into 3

Rejected. An unknown multiplicative normalization changes `A_n` in

`<lambda_n> = A_n V_S^(-2/d_eff)`

but not the power-law exponent. The source-reported `d_eff approximately 1.6` therefore cannot be repaired into 3 by restoring simplex-volume or TPFA constants.

## Attack 2 — only `lambda_1` matters and perhaps it behaves differently

Rejected by the source and protocol. The paper explicitly shows `n=1,3,5`, reports the same fitted effective dimension, and states that similar results extend to a few tens of low modes. Selecting a different low mode after seeing the result would violate the mode-family control.

## Attack 3 — the gap closes, so the slices are ordinary three-dimensional manifolds in the thermodynamic limit

Too strong. Gap closure establishes an extended geometry with finite large-scale dimension, not its numerical value. The source extracts the dimension from the volume scaling of the low eigenvalues and obtains approximately 1.6.

Thus `lambda_1 -> 0` and `d_eff=3` are distinct propositions.

## Attack 4 — the global `C_dS` phase is four-dimensional de Sitter, so each spatial slice must be a round `S^3`

Rejected. The de-Sitter result concerns the ensemble-averaged global three-volume profile. The spatial Laplacian spectrum is an independent observable of individual fluctuating slices. The published spectral result is precisely evidence that the low-mode spatial geometry is not captured by a simple round-`S^3` spectrum at accessible finite regulator.

No contradiction follows: different observables can probe different sectors/coarse-grainings of the same ensemble.

## Attack 5 — `d_eff approximately 1.6` is only a finite-size artifact and therefore cannot reject the round law

This is a valid continuum-limit caveat but does not save the specific finite-regulator claim. ITER087 proposed the scaling law as an accessible held-out finite-size test. The 2019 source performs that finite-size test and finds a different exponent with acceptable fit quality.

The correct conclusion is scoped:

- round-`S^3` low-mode scaling is rejected for the accessible published `C_dS` spectral data;
- the final continuum infrared spatial dimension remains open.

## Attack 6 — use the effective spectral dimension itself as the next FRG bridge

Not automatically. ITER071 established a common abstract spectral-dimension definition, while ITER073/074 retained scale and walk-normalization issues, and ITER080 retained FRG trajectory underdetermination. The present result cannot be used to select an FRG trajectory post hoc.

## Attack 7 — because the result was already known before the protocol commit, it should be discarded

It should not receive prospective validation credit, but it remains legitimate source authority about the observable. The protocol explicitly labels the adjudication retrospective and assigns zero validation credit.

This distinction preserves the scientific information without retroactive preregistration.

## Verdict

The classification survives:

**`SOURCE_REJECTS_ROUND_S3_IR_SCALING_ACCESSIBLE_CDS`**.

The retained positive results are:

- the low-mode gap closes in `C_dS` as volume grows;
- the finite-size scaling is source-fit by `d_eff approximately 1.6`;
- the spectral sector is demonstrably independent enough to falsify a naive round-slice inference from the global de-Sitter profile.

Prospective validation credit: **0**.
Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.
