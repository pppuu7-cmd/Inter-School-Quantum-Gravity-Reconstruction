# ITER114 mathematical correction — separated one-loop log degree

Date: 2026-09-15
Supersedes the separated-point `log^2` claim in ITER114 source/critic/terminal records. The original commits remain in history for auditability.

## Error

ITER114 correctly quoted the fixed-geodesic source distributions

`H_0^(k)(x;mu) = i/(64 pi^4) partial^2[log^k(mu^2 x^2)/x^2]`, `k=1,2`,

but then incorrectly treated `H_0^(2)` as carrying a separated `log^2` dependence after the Laplacian had acted.

## Exact correction at nonzero separation

Let

`L = log(mu^2 r^2)`.

In four Euclidean dimensions, for `r>0`,

`partial^2 [L/r^2] = -4/r^4`,

and

`partial^2 [L^2/r^2] = 8(1-L)/r^4`.

Therefore:

- `H_0^(1)` is proportional to `r^-4` at separated points;
- `H_0^(2)` is proportional to `r^-4 [constant - log(mu^2 r^2)]` at separated points.

The phrase "double logarithm" is correct for the **distributional representation before the outer Laplacian is evaluated**, and reflects the double UV pole/geodesic renormalization structure. It does **not** imply a separated `log^2` term in the final radial function.

## Consequence for scalar-curvature insertions

Four additional external derivatives appropriate to the two scalar-curvature insertions can raise the radial power from `r^-4` to `r^-8` and can lower logarithmic degree, but cannot increase it.

Hence the complete separated one-loop fixed-geodesic curvature basis under the ITER114 assumptions is restricted to

**`C_RR^geo(r;mu) = (G^2/r^8) [B_0(mu) + B_1(mu) log(mu^2 r^2)] + O(G^3)`**,

plus contact distributions at `r=0`.

There is no independent separated `B_2 log^2` coefficient at this order in this basis.

## Scientific status

This correction was identified before any coefficient was inferred from EDT data and before ITER115 was adjudicated. It is therefore a source/mathematical correction, not target-driven retuning.

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**.