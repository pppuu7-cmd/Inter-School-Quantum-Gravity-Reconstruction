# ITER118 terminal result — fixed-geodesic curvature line/endpoint counterterm power counting

Date: 2026-09-15
Gate: `ITER118_FIXED_GEODESIC_CURVATURE_LINE_ENDPOINT_COUNTERTERM_POWER_COUNTING`
Preregistration: `29eadfb45f0d2966262d9a34e648db55353e708b`
Source authority: `e3fd7bec52807bed587d91e8c43a9cc60534b550`
Adversarial review: `dd45512c4893d15ca32d1f9556b1fbd639e04ecd`

## Terminal classification

**`PASS_SCOPED_FINITE_LINE_ENDPOINT_COUNTERTERM_BASIS_POWER_COUNTING_CLOSED`**

Scope: one-loop, flat four-dimensional background, linear-curvature defect sector through local geometric dimension four.

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Main result

The curvature-decorated fixed-geodesic observable does not require an infinite counterterm functional at `O(G^2)` within the frozen EFT derivative accuracy.

The finite endpoint basis is spanned by:

- `R`, `R_nn`;
- `D R`, `D R_nn`;
- `Box R`, `D^2 R`, `Box R_nn`, `D^2 R_nn`;

plus identity/contact normalization and the already known geodesic embedding renormalization.

Modulo total derivatives, the independent line-interior curvature basis reduces to four operators:

- `int ds R`;
- `int ds R_nn`;
- `int ds Box_perp R`;
- `int ds Box_perp R_nn`.

Their required powers of the geodesic length are fixed by engineering dimension; they do not introduce a second independent physical scale.

## Important separation between endpoint and line sectors

Endpoint-local linear curvature mixing remains contact-like when contracted with the anchor curvature at lower order. The line sector is different: contact singularities of the local curvature kernel occur inside the line integral and can require defect renormalization whose finite coefficients depend on the total geodesic length. The four line operators therefore cannot be removed from the separated `B_0/B_1` analysis without an explicit mixing calculation.

## Consequence for the highest-log diagnostic

ITER116's `B_1` shortcut is now well-posed only after the pole/mixing matrix for these four line operators is included. The scalar matter `Z_chi` residue alone is insufficient.

## Exact successor

`ITER119_FIXED_GEODESIC_CURVATURE_LINE_DEFECT_MIXING_RANK_AUTHORITY`

Project the four line-interior operators onto the anchored scalar `RR` channel and determine, using linearized Bianchi identities, tree kernels and endpoint/line symmetries, the rank of the defect mixing problem. The goal is to reduce the four allowed line couplings to the smallest combinations that can actually feed separated `B_0/B_1` before any full one-loop pole integration.

## Claim ceiling

No line counterterm is asserted to have a nonzero pole, no `B_1` value/noncancellation theorem, no EDT fit or direct EDT/EFT conflict, no continuum EDT, no `BRIDGE_DERIVED`, no new physics and no candidate theory follow.