# ITER055 — Lorentzian recoupling minipanel transport

Date: 2026-09-14

## Terminal classification

**SCIENTIFIC PASS — `LORENTZIAN_RECOUPLING_MINIPANEL_TRANSPORT_PASS_SCOPED`**

This verdict is based on the frozen preregistration, all seven raw evidence artifacts, and the dependent aggregate. Green CI alone is not treated as a scientific predicate.

## Frozen authority

- Source map commit: `457f06952c29c5d7b0462a27f2fd068ee7f1bf29`
- Source map blob: `370d21534b1d6529f189a55073bd0bbd481a4784`
- Prereg commit: `0d96a7c9f4c4fbb07a5001b0c3586e90bee1e8f0`
- Implementation commit: `4cdd16bb046b0e17e0de6a48b4da4672ec58f8bb`
- Production head / authoritative run head: `82f2d33cebdec0e8bcaee165a7150cf5884eb0a0`
- Authoritative run: `34821443455`

## Jobs and artifacts

- null-controls: job `103903711742`; artifact `10338675884`; digest `sha256:a873c32e9b8120e3014e5d9f58706ae00fef96804235e2205e80168f69265ae0`
- map-and-symbolic-controls: job `103903711986`; artifact `10338292046`; digest `sha256:dc07e5c53c1a6d02542d7265519081cf684feae3993922bad9346cbfcfb85161`
- R11-A: job `103903712030`; artifact `10337919712`; digest `sha256:d8e4d762bf08142ae920622bae3a944782655b8c3b742d2f1b03cea718c24108`
- runtime-identity: job `103903712059`; artifact `10338343122`; digest `sha256:ca4e66010893a4bde237742dc1396b871af69542d08286c949f9a39cd62eb843`
- R10-A: job `103903712074`; artifact `10338163944`; digest `sha256:64b37e6396a834351faa1de564ba3016f02b75f6a9281a14edcc3c864c6e82b4`
- R11-B: job `103903712098`; artifact `10338084030`; digest `sha256:c92ed15cf3b45f814757c8992a662419d9f4a1746caeeb7bad12fa483c18885f`
- R10-B: job `103903712138`; artifact `10338258315`; digest `sha256:629d273216c23385d033395709e7d855699efb300556fa0458fc8356302c71d3`
- aggregate: job `103903853005`; artifact `10337969589`; digest `sha256:a5d6f4de322db0163ef2824164636dc94c93e8480f4641743aedd74ae3f421cc`

## Raw scientific results

The map/symbolic lane independently verified the immutable map and exact frozen recoupling factors:

- `R10`: `-sqrt(3)/2`
- `R11`: `-1/2`

The runtime lane reproduced all four ITER051 hashes exactly.

### R10: 1→0 transport

Each of the five source-mapped local calls used `two_js=[1,1,1,1,1,1,1,1,1,1]` and `two_is=[0,0,0,0,2]` and returned

`V_v = -2.32959640243e-09`.

Both independent replicas gave exactly:

- `A_author = -3.422603183002116e-41`
- `A_paper = +3.422603183002116e-41`

A/B differences are zero for every local vertex and for both final summands.

### R11: 1→1 transport

Each local call used `two_js=[1,1,1,1,1,1,1,1,1,1]` and `two_is=[2,2,2,2,2]` and returned

`V_v = -5.43572493901e-09`.

Both replicas gave exactly:

- `A_author = +1.5185788242379515e-40`
- `A_paper = -1.5185788242379515e-40`

Again A/B differences are zero.

All preregistered adversarial nulls were rejected: wrong physical-i encoding, reuse of ITER054 outputs, changed gamma/Dl/weight, second edge-dimension product, and output-dependent sign/normalization.

## Interpretation ceiling

Together ITER054+ITER055 now cover all four low-spin recoupling classes `0→0`, `0→1`, `1→0`, `1→1` for the bounded five-vertex fixed-summand construction without retuning. This is a transport result only.

It does **not** establish the full internal sum, shell convergence, a coarse↔fine equality, zero-face deletion, refinement invariance, a derived refinement map, bridge credit, continuum/GR recovery, or candidate theory.

Locks remain:

- `refinement_map_derived=false`
- `bridge_credit=false`
- candidate theory `UNFORMED / 0%`
- no `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, or `BRIDGE_DERIVED` claim.

## Next admissible gate

Only a prospectively frozen **source-authority qualification of an explicit refinement map and the corresponding coarse/fine objects** is admissible before any coarse↔fine numerical comparison. No shell-convergence or unbounded-sum escalation is authorized by ITER055.