# Preregistration — ITER056 Lorentzian refinement-map source authority audit

Date frozen: 2026-09-14

## Inherited terminal state

ITER055 is terminal **SCIENTIFIC PASS — `LORENTZIAN_RECOUPLING_MINIPANEL_TRANSPORT_PASS_SCOPED`**, authoritative run `34821443455`, production head `82f2d33cebdec0e8bcaee165a7150cf5884eb0a0`.

ITER054+ITER055 establish only bounded fixed-summand transport across the four low-spin recoupling classes. They do not establish a full internal sum, a coarse↔fine equality, or a derived refinement map.

## Scientific question

Does the pinned author source contain an **explicit, executable or algebraically unambiguous refinement/coarse-graining map** together with separately identifiable fine and coarse Lorentzian EPRL objects such that a later coarse↔fine numerical test can be preregistered without inventing a map after seeing amplitudes?

This is an authority/qualification gate only. It must not evaluate a coarse↔fine numerical equality and must not fit any map or normalization.

## Frozen external authority

Repository: `PietropaoloFrisoni/Monte_Carlo_spinfoams`

Commit: `84b375f2a2e0d29b44dd8820953553624bb007a3`

Tree: `5ded1505fbb148b8ab336027a509f942d9565176`

Primary EPRL 5→1 notebook:

- path `notebooks/julia/5-1_move_EPRL_analysis.ipynb`
- blob `bd1a55c0e95b98244df02e049346ba8b7488797a`

The notebook is treated as source evidence, not as a numerical truth oracle.

## Frozen qualification rule

A future coarse↔fine numerical gate is authorized only if the source audit can pin **all three** of the following from the frozen source without amplitude-value fitting:

1. **Fine object:** a source-defined 5→1 / vertex-renormalization EPRL amplitude object with its boundary variables and bulk variables identifiable.
2. **Coarse object:** a separately source-defined coarse/single-vertex (or otherwise explicitly stated coarse) EPRL object with its boundary variables identifiable.
3. **Map:** an explicit source-defined correspondence from the fine boundary/object variables to the coarse boundary/object variables, including every required normalization/weight convention. Co-presence of a fine and a coarse amplitude in one file is not sufficient.

A plot, asymptotic visual comparison, fitted rescaling, inferred equality, common variable name, or hand-written identification by us does not qualify as a refinement map.

## Independent lanes

Use `fail-fast:false` and no amplitude execution:

1. `source-identity`: verify exact repo commit/tree and exact notebook blob.
2. `fine-object-inventory`: extract code/markdown cells defining the EPRL vertex-renormalization/fine object, boundary labels and bulk variables; emit exact cell IDs and source excerpts/hashes.
3. `coarse-object-inventory`: independently search the pinned repository for a separately defined coarse/single-vertex EPRL comparison object; emit exact file/blob/cell or line provenance.
4. `map-inventory`: search for an explicit mapping/equality/embedding/coarse-graining prescription connecting the two objects; emit provenance and the literal variable-level correspondence if present.
5. `null-controls`: reject keyword-only matches, plots without an algebraic map, BF-only objects as substitutes for EPRL, fitted/post-hoc rescalings, and amplitude-value-dependent candidate selection.

The aggregate may summarize evidence but cannot turn missing authority into PASS merely because all jobs are green.

## Classification

**AUTHORITY PASS — `LORENTZIAN_REFINEMENT_MAP_SOURCE_AUTHORITY_PASS_SCOPED`** only if fine object, coarse object, and explicit map are all independently source-pinned and null controls pass.

**SCOPED BLOCKED — `LORENTZIAN_REFINEMENT_MAP_SOURCE_AUTHORITY_BLOCKED`** if the exact source is accessible but one or more of the three required objects cannot be established from source without inference or fitting.

`INFRASTRUCTURE FAIL` only if source retrieval/parsing fails before the authority question is evaluated.

No scientific FAIL of EPRL follows from absence of a source-qualified map.

## Claim locks

This gate cannot by itself produce bridge credit or candidate theory.

- `refinement_map_derived=false`
- `bridge_credit=false`
- candidate theory `UNFORMED / 0%`
- RC006 numerical retry remains unauthorized
- RC009 remains SCOPED BLOCKED
- no `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, or `BRIDGE_DERIVED` claim.

## Next gate

Only terminal AUTHORITY PASS permits a separate prospectively preregistered coarse↔fine numerical object test. BLOCKED forbids inventing or fitting a refinement map from amplitude outputs.