# ITER169 preregistration — upstream source trace gate

Frozen prospectively after ITER168 terminalized BLOCKED and before ITER169 execution.

## Purpose
Determine whether the ITER163 G-family open endpoint tensor can be mechanically traced through ITER161/ITER140 to source-derived affine Wick-edge geometry and denominator/contact support, without prose inference or coefficient retuning.

## Frozen positive requirements
1. Exact import/call chain from `iter163_complete_covariant_reconstruction.upper_open_vertex` use to `iter161_endpoint_open_leg_factorization.upper_open_vertex`, then `iter140...g2_real/dr1_real/r1_tensor` for `G_R1_chi2_Gamma2_dR1`.
2. Executable affine source geometry independently yields G-family Wick edges with separations `tau` and `1-tau`, endpoint zeros lower/upper, and phase `tau*qN-(1-tau)*kN`.
3. Denominator/contact support identifies denominator `Q*K`, q-edge `tau*L`, k-edge `(1-tau)*L`, lower shrinking q and upper shrinking k; cancelled-propagator contacts remain represented and are not set to zero before the frozen graph-level R-operation.
4. Lane C must attempt to falsify family identity, endpoint orientation, edge mapping, phase, and contact consistency.

## Forbidden positive evidence
Markdown/recovery/navigator prose; rational-number `.denominator`; fitted ITER118 coefficients; ITER160 residue; inverse-28 reconstruction; post-result threshold/model/basis/contact changes.

## Outcomes
- `PASS_SCOPED_ITER169_UPSTREAM_SOURCE_TRACE_COMPLETE` only if all three independent lanes agree on the mechanical trace and no frozen consistency check fails. This authorizes only a later source-qualified singular-sector manifest reconstruction.
- `BLOCKED_SCOPED_ITER169_TRACE_INCOMPLETE` if a required link is absent or only lexical/prose.
- `SCIENTIFIC_FAIL_ITER169_SOURCE_CHAIN_CONTRADICTED` if executable source objects exactly contradict a frozen positive requirement.
- infrastructure/numerical failure remains separate.

No ITER169 outcome authorizes Laurent/R-operation, ITER118 matching, B1_total, bridge credit, candidate equations or candidate theory.