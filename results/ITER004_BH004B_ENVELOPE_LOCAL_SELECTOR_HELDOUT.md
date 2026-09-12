# ITERATION 004 — BH-004B Transport Envelope + Local Selector Held-Out Test

Date: 2026-09-12  
GitHub Actions run: `34665149672`  
Status: `SUCCESS / NATURAL SUPPORT / STRONG SUPPORT NOT REACHED`

## Question

Can the source-defined physical sector at a child scale be reconstructed without using the child source projector or closure target, by factorizing scale transport into

`P_parent -> E_child -> P_hat_child`,

where `E_child` is the canonically transported parent envelope and the final selector is the child source-native Pauli–Jordan operator evaluated only inside that envelope?

## Construction

For each nested causal-set realization:

1. construct the parent source sector with the frozen BH-003 spectral prescription;
2. canonically restrict the parent basis to the child subset and keep its full numerical rank as the transport envelope `E`;
3. form the child Pauli–Jordan operator `J_child = i Delta_child`;
4. project it into the envelope, `J_E = E^† J_child E`;
5. apply the same frozen scalar source cutoff `sqrt(N_child)/(4*pi)` to `J_E`;
6. map the retained eigenvectors back through `E` to obtain `P_hat_child`;
7. only after prediction is frozen, construct the full child source projector for evaluation.

The child source rank/projector and all closure metrics are evaluation-only.

Campaign:

- parent sizes `N = 640, 896, 1152`;
- seeds `601,602,603,604`;
- `12` held-out jobs;
- nested levels `p_parent=0.5625`, `p_child=0.421875`;
- `24` rank-matched Haar controls per job.

## Preregistered gate

Natural support required all of:

- median rank relative error `<= 0.15`;
- median mean principal cosine `> 0.95`;
- median minimum principal cosine `> 0.50`;
- median normalized-projector-distance ratio `predicted/envelope < 0.80`;
- median leakage and sequential closure gains over rank-matched random controls both `> 1`;
- at least `2/3` of jobs improve both closure metrics.

Strong support required:

- rank error `<= 0.08`;
- mean cosine `> 0.98`;
- minimum cosine `> 0.80`;
- predicted/envelope distance ratio `< 0.60`;
- both median closure gains `> 1.5`;
- at least `0.80` of jobs improve both metrics.

## Aggregate result

| quantity | result |
|---|---:|
| jobs | `12` |
| median predicted/source rank relative error | `0.04957` |
| median mean principal cosine | `0.99106` |
| median minimum principal cosine | `0.92009` |
| median predicted/envelope projector-distance ratio | `0.68045` |
| median source norm captured by envelope | `0.97668` |
| median random/predicted leakage improvement | `3.17595x` |
| median random/predicted sequential-defect improvement | `6.69198x` |
| fraction jobs improving both closure metrics | `1.000` |
| natural support | **YES** |
| strong support | **NO** |

The strong gate fails only because the median predicted/envelope projector-distance ratio (`0.68045`) does not meet the preregistered `<0.60` requirement. All other strong thresholds are met, including rank error, mean/minimum principal cosine, closure gains and cross-job success fraction.

## Interpretation

The result supports a more precise scale-transport architecture than the original rank-matched BH-004 attempt:

`source physical sector`

`-> canonical transported orientation envelope`

`-> child source-native local selector`

`-> predicted child physical sector`.

The local selector materially improves the raw envelope: median projector distance falls to about `68%` of the envelope value while retaining very high all-direction alignment with the held-out source sector.

This also resolves the earlier stable-core negative result. The extra transported directions are not best removed by a globally fitted singular-value threshold. They are better filtered by child-scale source-native operator information inside the transported envelope.

## Structural consequence

For this realization, orientation transport and physical-rank selection should not be identified:

- the parent sector provides a restricted **orientation envelope**;
- local child data select the final physical subspace within it;
- scalar cutoff/measure information enters the selector separately from the transported orientation.

This is consistent with the RM-001 theorem that rank/spectrum alone do not determine projected composition closure, while also avoiding an arbitrary scale-dependent unitary fit.

## Scope lock

This is one free-field 1+1D causal-set realization. It establishes neither a universal QG RG law nor a fundamental `(P,mu)` ontology.

Generic projector/isometry-aware coarse graining is already known in tensor-network and projected-effective-dynamics settings. The scientific question is whether the same source-native factorization reappears in an independent quantum-gravity coarse-graining realization.

Therefore:

- `BH-004B_CAUSAL_SET_SUPPORT = NATURAL_PASS`;
- `BH-004_BRIDGE_DERIVED = NO`;
- `NEW_PHYSICS = NOT ESTABLISHED`;
- `CANDIDATE_THEORY = UNFORMED`.

## Next gate

Test the same semantic factorization on a genuinely different scale/refinement realization. The selected next front is `RC-006_EPRL_FK_TENSOR_COARSE_GRAINING`, a reduced `SU(2)_k x SU(2)_k` EPRL/FK-type spin-net/intertwiner system with explicit tensor-network coarse graining.

A BC-type fixed-point lane should be used as a positive control, while the EPRL/FK-type lane provides the stress test where the source literature reports immediate flow away from the original simplicity constraints.
