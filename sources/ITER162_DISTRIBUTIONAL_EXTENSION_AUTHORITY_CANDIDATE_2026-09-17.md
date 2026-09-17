# ITER162 distributional-extension authority candidate

Date: 2026-09-17

Status: **AUTHORITY_CANDIDATE_ONLY — NOT YET APPLIED TO THE OPEN-G ENDPOINT TENSOR**

Active gate: `ITER162_OPEN_G_ENDPOINT_DISTRIBUTIONAL_R_OPERATION_AND_POLE_TENSOR`.

## Source

Michael Dütsch, Klaus Fredenhagen, Kai Johannes Keller, Katarzyna Rejzner,
“Dimensional Regularization in Position Space, and a Forest Formula for Epstein-Glaser Renormalization”,
Journal of Mathematical Physics 55, 122303 (2014), DOI `10.1063/1.4902380`.
Accepted-version repository copy inspected from White Rose Research Online; arXiv version `1311.5424`.

Relevant section: **4.1 Regularization of numerical distributions**.

## Exact source statements relevant to ITER162

For an analytic regularization `t^zeta` of a distribution `t in D'(R^n \ {0})`, the paper derives in eq. (52) that the Laurent **principal part** acts only through a finite jet at the origin.

Lemma 4.3, eq. (53), then states that the principal part is a local distribution of order bounded by the degree of divergence:

`pp(t^zeta) = sum_{|gamma| <= sd(t)-n} C_gamma(zeta) delta^(gamma)`.

Corollary 4.4, eq. (54), states that removing the principal part (minimal subtraction) defines an extension with the same scaling degree.

These are directly relevant to the frozen ITER162 requirement that the pole ambiguity be represented as an explicit finite local delta-derivative span rather than hidden behind a generic “scheme dependent” label.

## What this source does NOT establish for ISQRG

This paper does **not** by itself establish that the current source-derived unseparated open-G endpoint tensor satisfies all hypotheses of the cited theorem in the exact form required by ITER162.

Before promotion from `AUTHORITY_CANDIDATE_ONLY`, the repository must still establish, source-faithfully and without scalar inversion:

1. the exact distribution space/domain of the open upper-endpoint tensor before K-contact separation;
2. the analytic/meromorphic regularization parameter corresponding to the frozen `d=4-2 epsilon` continuation;
3. the scaling degree / singular order of every tensor support component;
4. the correct ambient-vs-affine endpoint restriction/extension map, respecting the ITER153 pullback obstruction;
5. tensor covariance, symmetry in `(a,b)`, unit tangent `n^2=1`, and endpoint orientation;
6. the resulting complete local pole ambiguity basis under the ITER118 derivative ceiling;
7. whether the source-derived pole tensor has a nonzero image in `P_open / A_local`.

In particular, Lemma 4.3 does not supply the missing open-G Laurent coefficients, does not authorize setting cancelled-propagator contacts to zero, and does not authorize an ITER118 coefficient/rank solve.

## Current admissible use

`NAVIGATOR / MATHEMATICAL_EXTENSION_THEOREM_CANDIDATE` only.

It may be used to design the next exact ITER162 sub-gate: compute the source-derived scaling degree and local jet order, then mechanically enumerate the covariant delta-derivative ambiguity span. It must not be cited as proof that the complete endpoint pole tensor is already unique.

Claim locks remain:

- `B1_total = UNAUTHORIZED`;
- `BRIDGE_DERIVED = false`;
- `NEW_PHYSICS_FOUND = false`;
- candidate theory = `UNFORMED / 0%`.
