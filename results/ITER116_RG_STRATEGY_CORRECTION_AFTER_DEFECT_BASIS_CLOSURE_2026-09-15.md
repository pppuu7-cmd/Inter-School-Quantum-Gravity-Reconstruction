# ITER116 strategy correction — B1 is controlled by the complete projected RG/pole system

Date: 2026-09-15
Original valid RG result: `results/ITER116_FIXED_GEODESIC_CURVATURE_G2_SINGLE_LOG_RG_HIERARCHY_AUTHORITY_2026-09-15.md`
Triggering later authority: ITER117–ITER123.

## What remains valid

For the corrected separated basis

`C(l;mu)=G^2 l^-8[B_0(mu)+B_1 log(mu^2 l^2)]+O(G^3)`,

at the frozen order,

`mu dB_1/dmu=0`,

`mu dB_0/dmu=-2B_1`.

Also, `B_1 != 0` is sufficient to prove that the complete `O(G^2)` separated correlator is not identically zero.

These statements are unchanged.

## What is superseded

ITER116 described `B_1` too narrowly as if it were necessarily obtainable from the raw highest/double-pole `H^(2)` residue alone.

ITER117–120 establish additional curvature-specific line-defect counterterms. Their renormalized finite couplings can contribute to `B_0`, and their beta functions/pole residues can feed the RG equation for the explicit logarithmic coefficient.

In a minimal-subtraction description, beta functions are generally controlled by the appropriate simple-pole mixing data after subdivergence subtraction, while overlapping/geodesic divergences can also generate higher poles and `H^(2)`-type structures. The physical `B_1` is determined only after **all** such RG/pole information is projected onto the complete renormalized observable.

Therefore:

> `B_1` is controlled by the complete projected RG/pole system, not by an isolated raw highest pole of one diagram/class.

## Correct calculation target

The minimal noncancellation calculation must include:

1. direct nonlocal logarithmic pole structures from F/M/G;
2. bulk and endpoint subdivergence subtraction;
3. beta/pole mixing of the genuine defect operators retained after the ITER120 field-redefinition quotient;
4. geodesic/observable-specific renormalization;
5. projection of the complete RG data onto the single physical `B_1` coefficient.

A highest-pole residue remains a useful diagnostic/check where present, but is not by itself guaranteed to equal the physical `B_1`.

## Why this is not target retuning

The correction follows from closing the renormalization basis and does not use the EDT exponent or any target value. It strengthens the bookkeeping before any pole coefficient has been calculated.

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**.