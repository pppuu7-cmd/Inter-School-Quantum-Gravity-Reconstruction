# ITER150 result — first M/G nonlocal two-propagator master pole

Date: 2026-09-16.

## Preregistered authority

- Branch/commit: `research/iter150-nonlocal-master-pole` / `71cd4031b23c8e7654d2c99c3364604e39af414f`.
- GitHub Actions run: `35140549227`, job `104943683326`.
- Frozen upstream: ITER140 v6 run `35040499084`, aggregate artifact `10431112965`.
- ITER140 input SHA256 in the run: `7cdd350d3c53007a2312a35f4a504bde446534309626e1e04c9aa7477d4713c0`.
- ITER150 artifact: `10465465110`, artifact ZIP SHA256 `9e99d4b6854847a83b62ffde5c68969c96e5ac8f7d2c132375e49a737619fcd9`.
- Exact result JSON SHA256: `0748f4f29a684738ae019cd35e27cd51b5f2f37b6c6b956342eb51a6851cdc90`.
- The gate was executed twice from the same frozen input and the two JSON outputs compared byte-for-byte with `cmp`.

## Classification

`PASS_SCOPED_FIRST_MG_NONLOCAL_TWO_PROPAGATOR_MASTER_POLE_NONZERO_CONTACT_SUBTRACTION_OPEN`

All frozen checks A-I passed.

## Exact scoped result

The nonzero Q^0 K^0 two-propagator inputs were frozen directly from ITER140. Their simple-pole residues are:

- `M_R2_chi1_dR1 : b^2*S^2` -> `0`.
- `M_R1_chi1_dR2 : a^2*S^2` -> `0`.
- `M_R1_chi1_dR2 : a*b*S^2` -> `0`.
- `M_R1_chi1_dR2 : b^2*S^2` -> `0`.
- `G_R1_chi2_Gamma2_dR1 : b^2*S^2` -> `-1050/(pi^4 L^10)`.

Therefore the summed raw separated connected-cross TWO_PROPAGATOR residue is

`-1050/(pi^4 L^10)` multiplying `1/epsilon` in `d=4-2 epsilon`.

Independent internal checks in the gate include: closed radial tensor contractions versus independently assembled radial expressions, a direct D=4 Cartesian derivative spot-check, and an independent Gamma-function residue reconstruction for the pole-producing Beta function.

## Claim ceiling

This closes only the raw separated connected-cross TWO_PROPAGATOR master-pole subproblem for the first M/G channels. It does **not** include Q/K-cancelled contact sectors, endpoint or bulk counterterms, subdivergence subtraction, full defect mixing, full `B1_total`, gauge/BRST consistency, EDT, bridge derivation, new physics, or candidate-theory construction.

The next admissible gate is a prospectively frozen contact + endpoint/counterterm subtraction step testing whether this raw residue survives the complete renormalized first-M/G sector without retuning the numerator, basis, support partition, subtraction order, or threshold.
