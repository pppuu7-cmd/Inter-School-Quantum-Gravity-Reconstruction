# ITER052 — Lorentzian local-vertex argument crosswalk authority

Date: 2026-09-14

## Terminal classification

**PASS — `LORENTZIAN_LOCAL_VERTEX_ARGUMENT_CROSSWALK_AUTHORITY_PASS`**.

This is a source/object crosswalk PASS only. No Lorentzian amplitude value was used or computed. It does not establish a five-vertex numerical result, refinement map, shell convergence, bridge credit, or candidate theory.

## Frozen contract

Preregistration:

`prereg/ITER052_LORENTZIAN_LOCAL_VERTEX_ARGUMENT_CROSSWALK_2026-09-14.md`

Prereg commit: `a3f494374b491110525bee30af7ee1fa581a8fd6`.

Implementation:

`code/iter052/local_vertex_crosswalk.py`

Implementation commit: `f276e4d00a1a0bd63a129913d737318534125cb6`.

Workflow production head: `20b87fbcf7b049c700796daaf4380de4d79cdc5b`.

Authoritative run: **`34819214900`**.

## Source authorities

### Exact arXiv routing object

`sources/ITER052_EQ11_ROUTING_DATA.json`, blob `71c450514555feabd663b71942b1f5d693399cdc`, backed by:

- arXiv `2302.00072`;
- exact `main.tex` SHA256 `bff93f3a7857658264a04eb23521bb935a68eccb7760b284589ff5ec4073f063`;
- ITER048 raw-TeX artifact `10334723630`, digest `sha256:191262f0c2a6d5c5b3ac6f1036caacd6808735c4bc38ecc73c45da49b2c53cb9`.

### Pinned authors' executable implementation

`PietropaoloFrisoni/Monte_Carlo_spinfoams@84b375f2a2e0d29b44dd8820953553624bb007a3`:

- `src/vertex_renormalization_EPRL_MC.jl`, blob `6b627f7c2329724b589947195edc7e5ee7c18bb1`;
- `src/utilities.jl`, blob `7dddb9e34156264c2b599f74ed38853a2799ddb0`.

### Pinned backend axis/API authority

`qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f`:

- `src/vertex.c`, blob `9581999f0d5d59155e8c912fc7f2f3c5a98b346e`;
- `julia/SL2Cfoam.jl`, blob `0c5486ea817bd8da5ab18479a62cf930770e3be4`.

## Authoritative executable crosswalk

The exact author-code comments and tensor mechanics qualify the original local backend intertwiner argument lists, before the Wigner-6j basis change, as:

- up: `(ib,i4,i11,i12,i1)`;
- left: `(ib,i6,i14,i13,i3)`;
- bottom-left: `(ib,i8,i15,i11,i5)`;
- bottom-right: `(ib,i10,i12,i14,i7)`;
- right: `(ib,i2,i13,i15,i9)`.

The exact executable Wigner-6j recoupling pairs are:

`(i1→i2), (i3→i4), (i5→i6), (i7→i8), (i9→i10)`.

After each local fifth-axis basis change, the author-code pre-contracted local lists are:

- up: `(ib,i4,i11,i12,i2)`;
- left: `(ib,i6,i14,i13,i4)`;
- bottom-left: `(ib,i8,i15,i11,i6)`;
- bottom-right: `(ib,i10,i12,i14,i8)`;
- right: `(ib,i2,i13,i15,i10)`.

The pinned backend independently confirms the 5D vertex tensor storage/wrapper order `(i5,i4,i3,i2,i1)` and the ordered single-amplitude `(i1,...,i5)` interface with doubled-label conversion.

## New structural fact — exact degree-2 closure

For the source-qualified executable graph, count each global `i1...i15` occurrence across:

1. the five **original pre-W6j local vertex lists**, excluding boundary `ib`;
2. the five Wigner-6j left/right recoupling pairs.

The raw `graph-incidence` lane gives degree exactly **2 for every `i1...i15`**.

This is the expected closed fixed-summand incidence topology: each global intertwiner participates in exactly two structural incidences before the recoupling basis changes are contracted into the local vertex tensors.

All five prospectively frozen replacement checks also pass: the fifth local slot is exactly the left member of its Wigner pair before pre-contraction and the right member afterward.

## Why literal Eq.(11) cannot be used as an executable argument map by itself

The frozen adversarial controls were decisive.

### N1 — literal Eq.(11)

Using the literal five Eq.(11) local lists and literal fifth 6j `(i8,i10)` gives the global incidence census:

- `i1=1, i2=3, i3=1, i4=3, i5=1, i6=3, i7=1, i8=3, i9=0, i10=3, i11=2, i12=2, i13=2, i14=2, i15=3`.

It therefore fails exact degree-2 closure and entirely omits `i9`.

### N2 — fifth-6j repair alone

Replacing only the literal fifth 6j by the ITER049 `COMMENT_REPAIR` pair `(i9,i10)` is still insufficient. The resulting census remains non-closed:

- `i1=1, i2=3, i3=1, i4=3, i5=1, i6=3, i7=1, i8=2, i9=1, i10=3, i11=2, i12=2, i13=2, i14=2, i15=3`.

Thus ITER049 correctly repaired its scoped fifth-6j question, but that result alone was not a full local-vertex argument theorem.

### N3 — incidence alone is insufficient

Swapping the executable left inner slots `i14,i13` preserves the degree-2 census. The null lane therefore required and passed the stronger exact ordered-signature control: the pinned author code contains the frozen order `rIbl,rIu` and does not contain the swapped `rIu,rIbl` local-range signature.

Hence the PASS is not derived from graph degrees alone; it needs exact source order plus tensor-axis mechanics.

## Independent lane results

All five required lanes PASS:

- `tex-authority` — exact routing data/provenance/literal lists/6j pairs/comment crosswalk match;
- `author-code` — all five local range comments, spin calls, Wigner pairings, pre-contracted shapes, final contraction signatures and utility tensor mechanics match;
- `backend-axis` — C tensor order, Julia wrapper, five-intertwiner API and doubled conversion match;
- `graph-incidence` — H052 degree-2 closure and all replacement checks PASS;
- `null-controls` — N1 and N2 fail closure; N3 is rejected by exact ordered author-code signature.

No lane read or computed a Lorentzian amplitude value.

## Actions provenance

Jobs:

- author-code `103896654479`;
- backend-axis `103896654647`;
- graph-incidence `103896654677`;
- tex-authority `103896654679`;
- null-controls `103896654690`;
- aggregate `103896705116`.

Artifacts:

- graph-incidence id `10338020287`, digest `sha256:1e61540cc0b89688599e6a79de0f0eb5d4201de048801a8945df36e2352b4741`;
- null-controls id `10337890708`, digest `sha256:bf1a29c92de58dcacce480a2269e804a9e4eb9e327e019d08fce221a7a7f2520`;
- backend-axis id `10337509130`, digest `sha256:e14aea746764a304001c403a81e4cf3f281d1e6a88847e0813a4e93ab69cea6d`;
- author-code id `10337048507`, digest `sha256:49345a7587f0a73e7e20b4e784b2457183580e876dc9ac652eb27102a2f7261b`;
- tex-authority id `10336968664`, digest `sha256:ba343816c533782c7b28f0a341013dff4f5082e2872bf84ed44817d390e9f2f0`;
- aggregate id `10337417876`, digest `sha256:c435fd981b6b67cb20187a971f6a528b26c8ba14b0a3e4823025e58ca5a1e8c5`.

Aggregate classification is `LORENTZIAN_LOCAL_VERTEX_ARGUMENT_CROSSWALK_AUTHORITY_PASS`; manual raw-artifact audit agrees with the frozen contract.

## Scientific consequence

The executable local-vertex object is now source-qualified sufficiently to construct fixed configurations through the authors' basis-change convention without guessing the local intertwiner slots.

Together with ITER051, this closes two independent prerequisites:

1. exact Lorentzian backend runtime executability;
2. exact local vertex argument/basis crosswalk.

It does not yet close the phase/face/intertwiner-weight convention needed for a faithful five-vertex summand.

## Authorized next gate

Before any numerical five-vertex value is evaluated, prospectively freeze a **Lorentzian five-vertex phase/weight authority gate** comparing:

- exact Eq.(11) `(-1)^chi`, face and intertwiner dimension factors;
- the source's explicit reduction of `chi`;
- author code `dfj`, `df_phase`, the five per-vertex sign factors, and `face_weights_vec`/weight exponent semantics;
- the relation, if any, between the project's historical `alpha` notation and the paper/code face-weight parameter.

No numerical amplitude may be used to choose a phase or weight convention.

Only after that authority gate PASS may a new bounded primary/held-out five-vertex numerical gate be preregistered using the ITER051 runtime and the ITER052 argument mapping.

## Claim ceiling

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory remains **UNFORMED / 0%**.

Still unauthorized: unbounded ten-face summation, shell convergence, coarse↔fine equality, zero-face deletion, full Eq.(27), Eq.(29)/Lambda, one-step TNR, bridge derivation, candidate formation, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`.