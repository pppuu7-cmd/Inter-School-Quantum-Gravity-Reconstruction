# RC001 Lorentzian EPRL immutable-source-byte coarse/star binding diagnostic

Date: 2026-09-19

Status: **SOURCE_ACQUISITION_DIAGNOSTIC / NON-ITERATION / NOT A REFINEMENT PASS**

This diagnostic was performed while ITER179 remained the active nonterminal gate. It does not open a successor iteration and does not alter any claim lock.

## External immutable authority

Public repository:

`PietropaoloFrisoni/Markov_Chain_Monte_Carlo_spinfoams`

External repository head:

`8a722eb81b7e4c6f4eba75fe76ec7c89d334b53b`

Primary paper:

P. Frisoni, F. Gozzini, F. Vidotto,
*Markov Chain Monte Carlo methods for graph refinement in Spinfoam Cosmology*,
Class. Quantum Grav. 40 (2023) 105001,
arXiv:2207.02881.

The public cluster script fixes the stored Lorentzian EPRL tensors to:

- Immirzi parameter `gamma = 1.2`;
- booster-shell truncation `Delta l = 20`;
- sl2cfoam-next `vertex-fulltensor`.

The public `vertex_ampls/EPRL` directory contains immutable rank-five vertex tensors for half-integer `j=0.5,...,6.0`.

## Direct source-byte extraction

The GitHub connector was used with base64 encoding against the exact external commit so that the binary JLD2 tensors could be decoded without relying on a re-generated amplitude.

Verified blob SHAs used here:

- j=0.5: `1f404f234649d37d673544902ddd9e31925eda5d`;
- j=1.0: `78c3963766808c59fbbd15da22068d28c213342e`;
- j=1.5: `fb7159641bac20af034566bea153672a653a4308`.

The JLD2/HDF object layout was inspected before reading the numerical blocks. No result was accepted from a damaged or manually truncated base64 transfer.

## Coarse 4-simplex exact observable

The public source defines the diagonal angle operator in the intertwiner basis:

`cos(theta_i) = [i(i+1) - 2 j(j+1)] / [2 j(j+1)]`.

For the published five-index EPRL vertex tensor `A[i1,...,i5]`, the exact coarse normalized expectation was evaluated as

`Z_coarse = sum A^2`

and

`<cos(theta_1)>_coarse = sum A^2 cos(theta_i1) / Z_coarse`.

All five tensor legs were independently checked as symmetry controls.

Exact source-byte coarse results:

| j | <cos theta> | max five-node symmetry error | regular-tetrahedron error |
|---:|---:|---:|---:|
| 0.5 | -0.3333333333333334 | 1.39e-15 | 7.22e-16 |
| 1.0 | -0.33333333333333365 | 2.22e-16 | 3.33e-16 |
| 1.5 | -0.3333333333333335 | 6.66e-16 | 3.89e-16 |
| 2.0 | -0.33333333333333104 (node 1) | 1.33e-15 | 1.11e-15 for five-node mean |

Thus the exact published coarse tensors reproduce the regular-tetrahedron value `-1/3` to floating-point precision over all tested spins.

## Exact refined star contraction without MCMC

The public source implements the refined star amplitude as a contraction of one central rank-five EPRL vertex with five surrounding copies of the same rank-five vertex tensor.

For a local boundary observable, the full boundary sum can be performed exactly in a double-layer contraction without enumerating or sampling the 20-node state.

For one surrounding vertex define

`G[a,b] = sum_{i1...i4} A[a,i1,i2,i3,i4] A[b,i1,i2,i3,i4]`

and the operator-inserted Gram matrix

`H[a,b] = sum A[a,i1,...,i4] A[b,i1,...,i4] cos(theta_i1)`.

Then the exact star norm is the double-layer central-vertex contraction with five copies of `G`; the local angle numerator replaces the corresponding one `G` by `H`.

No MCMC sample, published target value, fitted normalization or reported coarse/refined agreement enters this exact contraction.

## Exact coarse versus star results

| j | coarse <cos theta> | exact star <cos theta> | absolute difference |
|---:|---:|---:|---:|
| 0.5 | -0.3333333333333334 | -0.33333333333333265 | 7.77e-16 |
| 1.0 | -0.33333333333333365 | -0.33329431555033084 | 3.90178e-5 |
| 1.5 | -0.3333333333333335 | -0.3331955238948669 | 1.37809e-4 |

The exact star values remain close to the regular-tetrahedron value `-1/3` and to the coarse source tensor result.

For the local quantum spread:

- j=0.5: coarse `0.6666666666666669`, star `0.6666666666666667`;
- j=1.0: coarse `0.640477627779083`, star `0.6427368365781825`;
- j=1.5: coarse `0.6556105868530424`, star `0.6622283051470415`.

The difference in fluctuations is larger than the difference in the mean, qualitatively consistent with the source paper's statement that average boundary geometry is stable while finer fluctuation/correlation structure changes under refinement.

## Scientific interpretation ceiling

This is stronger than the previous source-ledger state because:

1. the Lorentzian EPRL coarse object exists as immutable public tensor data;
2. the refined star object uses exactly the same tensor building block;
3. the local observable definition and normalization can be evaluated directly;
4. an exact, non-MCMC coarse/refined local-angle comparison is now executable.

However this diagnostic was **not prospectively preregistered as a scientific refinement test**.

It does not establish:

- continuum refinement invariance;
- cylindrical consistency;
- graph-independent physical amplitudes;
- agreement for a held-out observable family;
- the correct continuum limit;
- GR recovery;
- a BH-004 cross-realization PASS;
- bridge derivation.

The next admissible Lorentzian lane should prospectively freeze external tensor SHAs, a held-out spin/observable panel, exact/MCMC uncertainty rules and an independent Critic before classifying any refinement result.

## Persistent locks

`B1_total = UNAUTHORIZED`

`ITER118_MATCHING_AUTHORIZED=false`

`BRIDGE_DERIVED=false`

`NEW_PHYSICS_FOUND=false`

`NEW_QG_THEORY_REQUIRED=false`

`ALL_KNOWN_SCHOOLS_FAIL=false`

candidate theory remains `UNFORMED / 0%`.
