# ISQGR iteration-ID reconciliation

Date: 2026-09-15
Repository: `pppuu7-cmd/Inter-School-Quantum-Gravity-Reconstruction`

## Purpose

This note repairs bookkeeping only. No historical commit is deleted or rewritten and no scientific classification is upgraded by renaming.

A later recovery pass re-read an early D=2 ITER131 run without first noticing that the same canonical ITER131 had already been repaired to D=4 and terminalized, and then accidentally reused the already occupied labels ITER132 and ITER133. The duplicated labels are retained as immutable history but are not part of the canonical sequential iteration numbering.

## Canonical sequence

- **ITER131**: explicit R2/Gamma2 momentum generator. Authoritative repaired D=4 head `da613bc5cc9bff6b68ff1423f7aec06f5a30a28c`; terminal result `429f3a96e675a85143977b5c9adf982a80695079`; classification `PASS_SCOPED_EXPLICIT_R2_GAMMA2_MOMENTUM_TENSOR_GENERATOR_CLOSED`.
- **ITER132**: Gaussian M/G numerator-jet gate. Preregistered `27a8c8d378f35957ade6b0c79cad382ecdcdcd76`; terminal prerequisite blocker `14f5dc7d49c4a2f2a8f6d46aaaf90feb8c9af3d4`; classification `BLOCKED_MISSING_PREREQUISITE`.
- **ITER133**: fixed-geodesic localization kernels. Terminal `bbd278373228563b1580fc45301d2496997043e1`; classification `PASS_SCOPED_DERIVATIVE_AND_CHI1_KERNELS_CLOSED_CHI2_OPEN`.
- **ITER134**: chi2 localization-kernel attempt. Terminal `84e7cb55e090e71b8800dd533cc54cf4ee6de2a7`; `BLOCKED_MISSING_SECOND_ORDER_PATH_RESPONSE_AUTHORITY`.
- **ITER135**: second-order path-response diagnostics. Terminal `f9f1145c77d712c3f05fc13302b74f731b23c3ed`; `PASS_DIAGNOSTIC_PARTIAL_GATE_OPEN`.
- **ITER136**: completion diagnostics. Terminal `995a81c651c5bd0ac027e0686fef6a858401429c`; `PASS_DIAGNOSTIC_SCALARIZED_COMPLETION_FULL_TENSOR_AUTHORITY_OPEN`.
- **ITER137**: explicit 4D tensor held-outs, launched at `5d4f70adcf69c1e0856e313b7db7bb8686559ca2`. The workflow completed technically but its own Gamma2 lane reports `gamma2_indexed_contraction_executed=false`, so it is diagnostic rather than full scientific closure.

## Noncanonical duplicate labels

The following later commits remain valid evidence but their iteration numbers are noncanonical collisions:

- `6c07e6808bd0f5e6cfbf96eb5a55f0cd622d6f0d`: later ITER131 terminalization based on the obsolete D=2 run. It is superseded by the earlier authoritative D=4 ITER131 terminal `429f3a96...`.
- `7cbd4ee5aaaa1836decf33bdd6d66c31296722e8` through `bb97dcdfca730542a823cc0ba580476209dff1bc`: labeled ITER132 D4 transfer. Treat this as **replication RPL-D4-01**, not canonical ITER132. Its independent direct metric reconstruction is useful corroborating evidence for canonical ITER131.
- `a12924f79a5be406bb10d9e2a8457d432ce35651`: labeled ITER133 first M/G numerator jets. This label collides with canonical ITER133. Its scientific intent is reissued prospectively under the next free canonical number, ITER138.
- `f8d9f86f2688cfd1438b6e66d430a8c20c3825c1`: recovery addendum based on the duplicate numbering. It is superseded for active-gate bookkeeping by this reconciliation and subsequent recovery notes.

## Scientific consequence

The repaired D=4 ITER131 authority was already sufficient for nonlinear momentum vertices. RPL-D4-01 independently strengthens confidence because it reconstructed R2 directly from `g -> g^-1 -> Gamma -> Ricci` on held-out 4D panels, but it does not consume a new canonical iteration number.

The next free canonical number is **ITER138**. Any resumed exact M/G numerator work must use ITER138 or later and must cite the canonical ITER132 preregistration/blocker plus the prerequisite results accumulated in ITER133-137.

Candidate theory remains `0 / UNFORMED`; bridge credit remains 0; no B1 value, noncancellation result, EDT match, new physics, or cross-school bridge is authorized by this bookkeeping repair.
