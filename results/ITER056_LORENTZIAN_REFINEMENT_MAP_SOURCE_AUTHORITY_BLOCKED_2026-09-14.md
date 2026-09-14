# ITER056 — Lorentzian refinement-map source authority audit

Date: 2026-09-14

## Terminal classification

**SCOPED BLOCKED — `LORENTZIAN_REFINEMENT_MAP_SOURCE_AUTHORITY_BLOCKED`**

This is not a scientific FAIL of Lorentzian EPRL and not an infrastructure failure. It means the exact frozen author source did not supply all authority objects required to preregister a source-faithful coarse↔fine numerical comparison.

## Frozen source

- repository `PietropaoloFrisoni/Monte_Carlo_spinfoams`
- commit `84b375f2a2e0d29b44dd8820953553624bb007a3`
- tree `5ded1505fbb148b8ab336027a509f942d9565176`
- EPRL 5→1 notebook `notebooks/julia/5-1_move_EPRL_analysis.ipynb`
- notebook blob `bd1a55c0e95b98244df02e049346ba8b7488797a`

Prereg commit: `55160b6b48194d4d8ef2698bcf1b04dd3c038800`.

Implementation commit: `05f2660b37d7cf21f006cdeff086ea9fb5b697bb`.

Production head: `f8f6c04e2c525110eb860350923922a5ca182d73`.

Authoritative run: `34822881473`.

## Jobs and artifacts

- source-identity job `103908232089`, artifact `10338458177`, digest `sha256:351328fb527ff612e9ecc8089db42804fd921ffbfd9a69ef445528a10c5d8090`
- fine-object-inventory job `103908232165`, artifact `10339062290`, digest `sha256:8b895525ab8831712f23341779596512560ff0dd80e73458a42128817ecc193b`
- coarse-object-inventory job `103908232001`, artifact `10339241732`, digest `sha256:e2e4b62e5e7cfd372b01b260101df430db75ac7de45283b5a82dff8df11848d9`
- map-inventory job `103908232021`, artifact `10339122035`, digest `sha256:86d8f59b6d31060f42d3ca0850310a699396e6089396ce08562ccba78881cab0`
- null-controls job `103908231806`, artifact `10338942617`, digest `sha256:2a3ae2d764e1225011ffc1078a5fd6d62cc5d8f02c8b027582a09775ccbffef6`
- aggregate job `103908307101`, artifact `10338687626`, digest `sha256:5eef9a31442b2355b81708d7b4670cd43e901b42be06cbfe4c80ddf892f9bb67`

## Raw evidence

Source identity passed exactly: commit, tree and notebook blob all match the preregistered values.

The fine object is source-qualified. The pinned notebook explicitly identifies itself as `EPRL vertex renormalization`; code cell `11b6bc2f-5f21-4524-91fd-83d9c4815e23` reads EPRL vertex-renormalization data under

`vertex_renormalization/jb_0.5/.../EPRL/immirzi_0.1/.../ib_0/...`

and cell `458c6439-71d9-4a99-9439-48cc92a6b159` defines `get_VR_amplitudes(Dl,mu)`.

However, the independent coarse-object inventory returned no source-qualified candidate for a separately defined coarse/single-vertex EPRL object. The explicit-map inventory likewise returned no explicit mapping/equality/embedding prescription connecting a distinct fine object to a distinct coarse object.

Frozen null controls passed: keyword-only presence, plot-only comparisons, BF-only objects, fitted rescaling, and amplitude-value-dependent candidate selection are all rejected as substitutes for a refinement map.

Aggregate classification is therefore `LORENTZIAN_REFINEMENT_MAP_SOURCE_AUTHORITY_BLOCKED` with:

- `source_identity_pass=true`
- `fine_object_qualified=true`
- `coarse_object_qualified=false`
- `explicit_map_qualified=false`
- `null_controls_pass=true`

## Interpretation ceiling

ITER056 does not weaken ITER054 or ITER055. Their bounded five-vertex fixed-summand transport results remain valid in scope.

But the next coarse↔fine numerical bridge step is not authorized from this source alone. A coarse object or refinement map must not be invented, inferred from visual plots, fitted from amplitudes, or introduced post-hoc.

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory remains `UNFORMED / 0%`.

## Next admissible direction

An independent cited-authority search may look for an explicit Lorentzian EPRL coarse/fine map in source material referenced by the author implementation or closely associated 5→1/vertex-renormalization literature. Such a search is authority discovery only; it must remain amplitude-blind and cannot relax the three-object requirement.