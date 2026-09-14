# ITER032 authority-regex technical repair

Date: 2026-09-14

## First authoritative attempt

Run: `34804399944`
Production head: `5f624a8a9f08a1aa75b3031e954cba2e66bcd859`
Jobs: authority `103853284855`; factors `103853284954`; assembly `103853284982`; nulls `103853285020`; aggregate `103853318125`.
Artifacts: authority `10333155543` (`sha256:584da9e53cc37c3e9bdec38bb9b1deeabc943ad9c8d3f30d9d2c45df292a3aae`); factors `10332157095` (`sha256:4094dcd7f8b32bf837b54a8231334f36c9c8f84496e54e42382b79c90ad4345b`); assembly `10333101024` (`sha256:c575bd9f912ff3af37f57318a3068e8ae8eb134c737bd74ec95e07f3362f18cb`); nulls `10332796265` (`sha256:7ed7ca410eae0f01f69b9653f694acde552e3f9c2a340626cd5e2a7e128617aa`); aggregate `10333036518` (`sha256:4ee4bb3491487e5244889dede7ed9b8ea0536392353c06997d1947be8b4b3276`).

## Classification

The aggregate is **`NUMERICAL_OR_INFRASTRUCTURE_FAIL_PRE_SCIENCE`**, not scientific FAIL and not PASS. Lane A stopped with Python regex parser error `nothing to repeat at position 24` before source-factorization authority could be evaluated. The defect was the technical separator-cleanup regex, specifically an optional quantifier applied to a word-boundary assertion. No frozen scientific predicate failed.

The other three lanes produced useful but non-authorizing diagnostics under the preregistered science:
- independent factor reconstruction PASS; max single-factor residual `5.551115123125783e-16` versus frozen `5e-8`; held-out not retuned;
- factorized two-factor assembly PASS; max residual `3.596947722116015e-16` versus frozen `5e-8`; held-out not retuned;
- null controls PASS with 3/3 wrong constructions detected; good residual `5.551559314731637e-17`; wrong residuals `0.7137917357844188`, `0.6431041321077906`, `0.6431041321077906`.

Because source-factorization authority is a prerequisite lane, these diagnostics do not by themselves constitute ITER032 scientific PASS.

## Minimal repair

Repair commit `43ed319f0047a3a71c9eed8962902c7b25ac97d5` removes only the invalid regex quantification in the TeX separator-cleanup expression. The exact source authority rule, primary/held-out panels, adjacent-row pairing, `alpha=0`, numerical threshold `5e-8`, null threshold `1e-6`, and 2/3 null criterion are unchanged.

No claim lock is relaxed. Eq.(29)/Lambda, one-step TNR, full Eq.(27) amplitude, bridge credit and candidate theory remain unauthorized.
