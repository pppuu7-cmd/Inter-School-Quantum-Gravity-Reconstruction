# ITER032 result — bounded two-factor Eq.(27) network assembly

Date: 2026-09-14

Scientific classification: **PASS — `RC006_EQ27_TWO_FACTOR_BOUNDED_NETWORK_ASSEMBLY_PASS`**.

This is a bounded factorized-composition PASS only. It is not a full Eq.(27) amplitude derivation, not Eq.(29)/Lambda, not one-step TNR, and gives zero bridge/candidate-theory credit.

## Frozen provenance

- preregistration commit: `bda9c7c12a2f2e4886d4734b9d1835119a700491`
- initial implementation commit: `a369586e5d05b04e757f36468e58aaba00cb1253`
- first production head/run: `5f624a8a9f08a1aa75b3031e954cba2e66bcd859` / `34804399944`
- first-run classification: `NUMERICAL_OR_INFRASTRUCTURE_FAIL_PRE_SCIENCE` due solely to Lane-A regex parser error; B-D diagnostics were retained but were non-authorizing
- regex-only repair commit: `43ed319f0047a3a71c9eed8962902c7b25ac97d5`
- repair note commit: `fa1abbf36713aef4f6e29c262455475bf34e9960`
- authoritative recovery production head: `e1c472ae48f9aeb0aae8419404f1f6382a37b045`
- authoritative run: `34804537344`

Authoritative jobs/artifacts:
- assembly job `103853680863` -> artifact `10332118510`, digest `sha256:2f952fa457537fd8909a3fac915741293a81666026f37fc5f48b506499759ca1`
- authority job `103853680965` -> artifact `10333021691`, digest `sha256:4106ea0ef1adeb6cc94c4aeb20ba67ba78ca65fcc320b104ae8a0bc51cebde2f`
- nulls job `103853681028` -> artifact `10332401803`, digest `sha256:d44a0fa6e3c4e0282da33ae5c00909a057e61ef0955b50d56efd7383241df196`
- factors job `103853681161` -> artifact `10332672531`, digest `sha256:3e7398d54718426e1d38d1663aae89e8a339c162ad65f6909cbd05e5a772bf92`
- aggregate job `103853724474` -> artifact `10333010977`, digest `sha256:9a36150c1efac2f20f3763088a80fdb9fc849232f6e64044776efd68ffd21f5a`

## Scientific readout

Lane A source-factorization authority PASS:
- exact archive SHA `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`
- exact Eq.(27) display SHA `88d2f7be9489980a763dd66b5c4900473c79900ccf72790095ae1675e9733b2d`
- exactly 2 bracketed graphical factors and 2 source sum structures
- factors are distinct/non-nested and source syntax separates them multiplicatively via `\\times`
- no missing prerequisite and no forbidden executable Eq.(29)/Lambda dependency.

Lane B independent-factor reconstruction PASS:
- max single-factor residual `8.671119018262734e-16` versus frozen threshold `5e-8`
- primary `k={6,10,12}`, held-out `k={7,9,11}`
- no held-out retuning.

Lane C bounded two-factor assembly PASS:
- max two-factor residual `5.55287100034665e-16` versus frozen threshold `5e-8`
- all values finite
- same deterministic adjacent-row rule in primary and held-out panels
- no held-out retuning.

Lane D adversarial nulls PASS:
- good residual `5.551559314731637e-17`
- detected 3/3 wrong constructions against preregistered requirement >=2/3
- wrong residuals: flipped second target sign `0.7137917357844188`; second factor using first q-dimension `0.6431041321077906`; collapsed second factor identity `0.6431041321077906`.

Aggregate has `scientific_pass=true`, `failed_lanes=[]`, `infrastructure_lanes=[]`, `authority_blocked=false`, while explicitly keeping `full_eq27_amplitude_claimed=false`, `eq29_amplitude_authorized=false`, `one_step_tnr_authorized=false`, `bridge_credit=false`.

## Exact authorization

ITER032 authorizes only a **new separately preregistered source-summation/scalar lift gate** asking whether the remaining explicit Eq.(27) scalar prefactor and its two source summations can be instantiated source-faithfully around the validated factorized bounded object, with primary/held-out transport and frozen nulls.

It does not authorize Eq.(29), Lambda, one-step TNR, candidate-theory construction, bridge credit, or a claim that the full Eq.(27) amplitude has already been derived.

Candidate theory remains `UNFORMED / 0%`. Overall programme roadmap readiness remains 49% pending closure of a higher roadmap rubric/gate.
