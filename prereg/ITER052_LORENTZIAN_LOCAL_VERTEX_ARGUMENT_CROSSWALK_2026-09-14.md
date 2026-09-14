# Preregistration — ITER052 Lorentzian local-vertex argument crosswalk authority

Date frozen: 2026-09-14

## Inherited terminal state

ITER051 is terminal PASS — `LORENTZIAN_PINNED_BACKEND_RUNTIME_PASS`, authoritative run `34818301950`, terminal report commit `16c8934ae7074f5c29aa20af3ded0a73dbfb0bdf`.

ITER048 remains historical `SCOPED_BLOCKED`; ITER049 remains valid only in its author-code fifth-6j routing-reconciliation scope; ITER050 remains `INVALID_IMPLEMENTATION`.

No five-vertex numerical contraction is authorized until the local argument mapping is source-qualified.

## Scientific/source question

Does the pinned authors' executable 5→1 implementation define a unique source-qualified local-vertex argument crosswalk, via its explicit Wigner-6j pre-contractions and tensor-axis convention, that closes the global `i1...i15` incidence graph without amplitude fitting?

This is a source/object authority gate. It evaluates no Lorentzian amplitude values.

## Frozen source authorities

### Exact arXiv routing data

Machine-readable extraction:

`sources/ITER052_EQ11_ROUTING_DATA.json`, git blob `71c450514555feabd663b71942b1f5d693399cdc`.

Underlying authority:

- `arXiv:2302.00072`;
- exact `main.tex` SHA256 `bff93f3a7857658264a04eb23521bb935a68eccb7760b284589ff5ec4073f063`;
- ITER048 raw-TeX artifact id `10334723630`, digest `sha256:191262f0c2a6d5c5b3ac6f1036caacd6808735c4bc38ecc73c45da49b2c53cb9`.

### Pinned authors' executable code

Repository/commit:

`PietropaoloFrisoni/Monte_Carlo_spinfoams@84b375f2a2e0d29b44dd8820953553624bb007a3`.

Frozen files:

- `src/vertex_renormalization_EPRL_MC.jl`, git blob `6b627f7c2329724b589947195edc7e5ee7c18bb1`;
- `src/utilities.jl`, git blob `7dddb9e34156264c2b599f74ed38853a2799ddb0`.

### Pinned backend axis/API authority

`qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f`.

Frozen files:

- `src/vertex.c`, git blob `9581999f0d5d59155e8c912fc7f2f3c5a98b346e`;
- `julia/SL2Cfoam.jl`, git blob `0c5486ea817bd8da5ab18479a62cf930770e3be4`.

## Frozen literal Eq.(11) data

Literal local vertex intertwiner lists:

- up `(ib,i4,i11,i12,i2)`;
- left `(ib,i6,i13,i14,i4)`;
- bottom-left `(ib,i8,i15,i11,i6)`;
- bottom-right `(ib,i10,i12,i14,i15)`;
- right `(ib,i2,i13,i15,i10)`.

Literal 6j intertwiner pairs:

`(i1,i2), (i3,i4), (i5,i6), (i7,i8), (i8,i10)`.

Exact source comment crosswalk:

`rBCl=i1, rBCr=i2, rABl=i3, rABr=i4, rAEl=i5, rAEr=i6, rbl=i7, rbr=i8, rCDl=i9, rCDr=i10, rIul=i11, rIur=i12, rIu=i13, rIbl=i14, rIbr=i15`.

## Frozen executable mapping hypothesis H052

The pinned author-code comments plus tensor-axis/pre-contraction implementation imply the following **original backend local argument lists before Wigner-6j basis change**:

- up `(ib,i4,i11,i12,i1)`;
- left `(ib,i6,i14,i13,i3)`;
- bottom-left `(ib,i8,i15,i11,i5)`;
- bottom-right `(ib,i10,i12,i14,i7)`;
- right `(ib,i2,i13,i15,i9)`.

The executable Wigner-6j basis-change pairs are prospectively frozen as:

`(i1→i2), (i3→i4), (i5→i6), (i7→i8), (i9→i10)`.

After replacing each original local `i5` by the right recoupling label, the executable pre-contracted local lists are frozen as:

- up `(ib,i4,i11,i12,i2)`;
- left `(ib,i6,i14,i13,i4)`;
- bottom-left `(ib,i8,i15,i11,i6)`;
- bottom-right `(ib,i10,i12,i14,i8)`;
- right `(ib,i2,i13,i15,i10)`.

The author-code final contraction must use exactly these pre-contracted label incidences in the backend tensor-axis order.

No mapping may be altered after any lane result is seen.

## Frozen structural invariant

For a correct pre-basis-change fixed summand graph, every global intertwiner `i1...i15` must have exactly two structural incidences across:

1. the five original local vertex argument lists, excluding boundary `ib`;
2. the five Wigner-6j recoupling pairs.

H052 predicts exact degree 2 for all 15 labels.

This invariant is source-topological, not amplitude-based.

## Frozen null interpretations

### N1 — `TEX_LITERAL`

Use the five literal Eq.(11) local lists and the literal fifth 6j `(i8,i10)`.

Expected null outcome frozen in advance: graph-incidence condition is violated, including missing `i9`.

### N2 — `ITER049_6J_ONLY_REPAIR`

Use literal Eq.(11) local lists but repair only the fifth 6j to `(i9,i10)`.

Expected null outcome frozen in advance: fifth-6j routing is repaired, but the full local-vertex incidence graph still fails exact degree-2 closure.

### N3 — `LEFT_INNER_SLOT_SWAP`

Start from H052 but swap executable left local slots `i14,i13` to `i13,i14` while retaining all incidences.

Expected null outcome: degree census alone cannot reject this, so the pinned author-code comment/tensor-axis signature must reject it. This is the required control showing that incidence alone is insufficient.

## Independent lanes

1. `tex-authority`: verify exact extracted Eq.(11) data object, source hash provenance, literal local lists, literal 6j pairs and comment crosswalk.
2. `author-code`: independently verify the five pinned `vertex_compute` spin calls, five local range comments, five Wigner-6j left/right name pairs, pre-contracted tensor shapes, and final contraction index ordering from exact author-code blobs.
3. `backend-axis`: independently verify the pinned backend stores/wraps vertex tensor axes as `(i5,i4,i3,i2,i1)` and that the single-amplitude API consumes `(i1,...,i5)` physical intertwiners before doubled conversion.
4. `graph-incidence`: evaluate H052's exact global-label degree census and pre-contraction replacement map only from the prospectively frozen mappings.
5. `null-controls`: evaluate N1, N2 and N3. N1/N2 must fail structural closure; N3 must be rejected by exact author-code ordered signature despite preserving degrees.

Use `fail-fast:false`. No lane may inspect or compute a Lorentzian amplitude.

## Frozen PASS criteria

`TEX_AUTHORITY_PASS`: exact routing data and provenance match the frozen source object.

`AUTHOR_CODE_PASS`: exact pinned source contains all five prospectively frozen local range signatures, Wigner-6j pairings, pre-contracted shapes and final contraction connectivity; no expected signature is missing or multiply incompatible.

`BACKEND_AXIS_PASS`: exact backend axis/order/API evidence supports the prospectively frozen conversion between local `(i1,...,i5)` and wrapped tensor axes `(i5,...,i1)`.

`GRAPH_INCIDENCE_PASS`: all `i1...i15` have degree exactly two under H052; each Wigner-6j left label is the original local recoupled slot and each right label is the corresponding pre-contracted replacement.

`NULL_CONTROLS_PASS`: N1 and N2 fail degree-2 closure; N3 is rejected by the ordered author-code signature.

## Terminal classifications

- `LORENTZIAN_LOCAL_VERTEX_ARGUMENT_CROSSWALK_AUTHORITY_PASS` iff all five lanes PASS.
- `LORENTZIAN_LOCAL_VERTEX_ARGUMENT_CROSSWALK_BLOCKED_SOURCE_AXIS_CONVENTION` if exact pinned sources leave a material local-axis/basis ambiguity after all source evidence is applied.
- `LORENTZIAN_LOCAL_VERTEX_ARGUMENT_CROSSWALK_STRUCTURAL_FAIL` only if exact pinned executable source contradicts H052 or its global graph fails the frozen incidence invariant.
- `INVALID_IMPLEMENTATION` if the gate does not test the frozen mappings/controls or uses amplitude values.
- `INVALID_PROVENANCE` if any frozen source identity cannot be established.

## Consequence of PASS

PASS authorizes only a **new separately preregistered bounded five-vertex fixed-configuration gate** using:

- the ITER051 validated runtime backend;
- the H052 source-qualified original local vertex mapping;
- source-qualified Wigner-6j recoupling pairs;
- correct physical-to-doubled label conversion (`i=0→two_i=0`, `i=1→two_i=2`);
- frozen primary/held-out configurations and no post-hoc retuning.

PASS does not authorize unbounded ten-face sums, shell convergence, coarse↔fine equality, refinement-map derivation, bridge credit or candidate formation.

## Claim locks

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory remains `UNFORMED / 0%`.

Still unauthorized: `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`, full Eq.(27), Eq.(29)/Lambda, one-step TNR, unbounded Lorentzian refinement.