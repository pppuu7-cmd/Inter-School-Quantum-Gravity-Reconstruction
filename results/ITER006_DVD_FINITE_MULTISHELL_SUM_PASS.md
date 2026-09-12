# ITER006 — source-gated Lorentzian EPRL DVD2/DVD3 finite multi-shell sum PASS

Date: 2026-09-12

## Scope

This is a prospectively frozen finite auxiliary-shell diagnostic of the source-labelled two-vertex Lorentzian EPRL amplitudes `DVD2` and `DVD3` from arXiv:1801.03771, evaluated with the pinned `sl2cfoam-next` B4 kernel.

It is **not** a coarse/fine refinement map, cylindrical consistency test, continuum-limit result, bridge derivation, novelty claim, or new-physics claim.

## Source and protocol locks

- paper root SHA256: `27e781f9ae9b36056a57b7747dc3c58b5b9c944dd0214041149843d8434e16c1`
- `DVD2` equation hash: `799f56dc22f55a09bf744d62c459ee95e38794e5be02c114a73d06c057d0e94c`
- `DVD3` equation hash: `7d2fb958574c76f67e52d32ffea2cb22beb01c1e7d6583d383fce159b2eadfab`
- numerical kernel: `qg-cpt-marseille/sl2cfoam-next` commit `052e4346028870bd76f69a3034e6cae8defb8f7f`
- frozen boundary: `j_a=j'_a=1`, `i=t=i'=t'=1`
- gamma: `{0.5,1.2,2.0}`
- finite auxiliary cutoff: `D=0,1,2`
- each unconstrained auxiliary `l` runs over integer spins `1..1+D`
- repeat gate: max relative difference `<=1e-12`
- D0 regression gate against prior genuine two-vertex pilot: `<=1e-12`
- no preregistered monotonicity or convergence-direction gate

The finite cutoff is explicitly a numerical regulator modeled on the same paper's labelled shell pattern around `giorgio`; it is not asserted to be the source definition of a finite DVD sum. A pre-numerical parser amendment is preserved in `protocol/ITER006_DVD_MULTISHELL_SOURCE_GATE_AMENDMENT.json`.

## Provenance

Authoritative run: `34708369655`.

- source-manifest job `103592473582`: PASS
- gamma 0.5 job `103592489921`: PASS
- gamma 1.2 job `103592489940`: PASS
- gamma 2.0 job `103592489928`: PASS
- aggregate job `103592649819`: PASS
- aggregate artifact `10302776275`
- aggregate artifact digest: `sha256:0ec040025f6cb55953cedbb6f79c28ab142a3563b09a41be039867e422693796`

All numerical lanes were evaluated twice; the maximum repeat relative difference was `0.0` in every lane.

## Results

### gamma = 0.5

| D | DVD2 | DVD3 | DVD2/DVD3 | normalized split | DVD2 increment | DVD3 increment |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 5.496983896037186e-4 | 5.496983896037186e-4 | 1.000000 | 0 | — | — |
| 1 | 1.160314452673374e-3 | 8.875229918840471e-4 | 1.307363 | 0.235101 | 0.526251 | 0.380638 |
| 2 | 1.7502215813554412e-3 | 1.031647217053245e-3 | 1.696531 | 0.410562 | 0.337047 | 0.139703 |

### gamma = 1.2

| D | DVD2 | DVD3 | DVD2/DVD3 | normalized split | DVD2 increment | DVD3 increment |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1.2780379206216302e-5 | 1.2780379206216303e-5 | 1.000000 | 1.33e-16 | — | — |
| 1 | 2.5960000424492336e-5 | 2.100830367642193e-5 | 1.235702 | 0.190743 | 0.507690 | 0.391651 |
| 2 | 3.3937577257182434e-5 | 2.3629590996910224e-5 | 1.436232 | 0.303734 | 0.235066 | 0.110932 |

### gamma = 2.0

| D | DVD2 | DVD3 | DVD2/DVD3 | normalized split | DVD2 increment | DVD3 increment |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 3.7591052442651034e-7 | 3.759105244265104e-7 | 1.000000 | 1.41e-16 | — | — |
| 1 | 7.376380837393899e-7 | 6.261295759045302e-7 | 1.178092 | 0.151170 | 0.490386 | 0.399628 |
| 2 | 8.952613602454995e-7 | 6.959576595319952e-7 | 1.286373 | 0.222621 | 0.176064 | 0.100334 |

## Observations allowed by the preregistered diagnostic

1. D0 exactly reproduces the previous genuine two-vertex pilot: worst relative regression error is `1.41e-16`.
2. DVD2 and DVD3 separate immediately when the auxiliary shell is enlarged beyond D0.
3. For **all three gamma values and both amplitudes**, the relative D1→D2 increment is smaller than the D0→D1 increment.
4. The effect is much stronger for DVD3: D1→D2 increments are approximately 0.140, 0.111, and 0.100 for gamma 0.5, 1.2, and 2.0 respectively.
5. These facts are consistent with finite-cutoff stabilization over the tested window, but D<=2 is insufficient to claim mathematical or physical convergence.

## Decision

`DVD_FINITE_MULTISHELL_SUM_AGGREGATE_PASS = YES`.

Promotion remains blocked at the refinement/bridge level. The next useful independent tests are held-out gamma transport of the same finite-shell diagnostic and a prospectively frozen asymmetric boundary that breaks the special symmetric D0 identity.
