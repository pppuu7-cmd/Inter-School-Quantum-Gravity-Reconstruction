# ITER132 terminal result — D=4 transfer authority for explicit R2/Gamma2 vertices

Date: 2026-09-15
Prereg commit: `7cbd4ee5aaaa1836decf33bdd6d66c31296722e8`
Implementation commit: `353e2c00c35c810a515d0585fc83723fbaf56af3`
Workflow commit: `19ee1c82ffa4e2983ba5f1451f90c4df8bb10dc1`
Authoritative run: `34951905279`
Job: `104324613596` (`d4-transfer-audit`)
Artifact: `10389487686` (`iter132-d4-vertex-transfer`)
Artifact SHA256: `4d6dc0baea302bd99735e4bf04407b85881f18657ecb0d8776ee2528396a1b0f`

## Scientific classification

`PASS_SCOPED_D4_R2_GAMMA2_VERTEX_TRANSFER_CLOSED`

All frozen predicates passed:

- full D=4 ten-element symmetric graviton-leg basis instantiated;
- R2 Bose symmetry passed on the full basis;
- Gamma2 lower-index and leg-Bose symmetries passed on the full basis;
- R2 degree-2 and Gamma2 degree-1 momentum homogeneity passed;
- three independent direct metric-reconstruction panels passed exactly;
- the direct panels included off-diagonal polarizations and non-collinear integer momenta;
- construction remained target-independent.

The direct reconstruction built `g`, the O(kappa^2) inverse metric, Christoffels and Ricci scalar with an independent Fourier-derivative operator and did not call the R2 vertex routine under test.

## Consequence

The D=4 nonlinear R2/Gamma2 momentum vertices are now authorized as inputs to the preregistered ITER133 first exact M/G numerator-jet calculation.

No loop pole, B1, noncancellation, EDT match, bridge, new physics or candidate theory is implied.
