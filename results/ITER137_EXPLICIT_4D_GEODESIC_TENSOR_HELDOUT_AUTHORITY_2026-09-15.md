# ITER137 terminal result — explicit 4D geodesic tensor held-outs

Date: 2026-09-15
Preregistration: `aced43798d1068725f7afd5787356db0b9af037f`
Implementation: `96879a881889033ff590590293a8548ba38138ee`
Workflow head: `5d4f70adcf69c1e0856e313b7db7bb8686559ca2`
Authoritative run: `34944153962`

## Scientific classification

`BLOCKED_MISSING_PREREQUISITE`

The workflow completed technically with conclusion `success`, but the preregistered scientific gate explicitly requires an indexed Gamma2 contraction. The production implementation deliberately reports `gamma2_indexed_contraction_executed=false` and classifies that lane `BLOCKED_MISSING_PREREQUISITE`; therefore green CI cannot be promoted to a scientific PASS.

## Consumed lanes

- `tensor-audit (gamma1-heldouts)`, job `104299482460`: three explicit D=4 Gamma1/direct-differentiation panels passed componentwise. Artifact `10385689255`, SHA256 `86963e5be137c012264048f66267e2eadd5e2ad668faf884e623babf824ec82a`.
- `tensor-audit (reversal-and-gamma2-prereq)`, job `104299482652`: endpoint velocity-reversal checks passed, but the required indexed Gamma2 contraction was not executed. Artifact `10386328352`, SHA256 `ad7b7d450ce47a62bddc59775fac49fe1ee2b39674611fbb654efdacd8c494bf`.

## Later prerequisite evidence

Canonical ITER131 had already been repaired to an explicit D=4 R2/Gamma2 component generator (`da613bc5cc9bff6b68ff1423f7aec06f5a30a28c`, terminal `429f3a96e675a85143977b5c9adf982a80695079`). A later independently coded D=4 direct-metric replication, now reconciled as `RPL-D4-01`, also passed. These later/rediscovered authorities may be consumed prospectively by ITER138+, but they do not retroactively alter the frozen ITER137 production result.

Candidate theory remains `0 / UNFORMED`; bridge credit remains 0. No pole residue, B1, EDT match, new physics, or candidate theory follows.
