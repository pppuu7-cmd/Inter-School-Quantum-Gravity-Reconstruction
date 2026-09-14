# ITER051 source record — Lorentzian local-vertex argument crosswalk

Date: 2026-09-14

Purpose: outcome-independent source/object audit for the Lorentzian 5→1 front. This record does not modify ITER048 or ITER049, does not affect the active ITER051 all-zero runtime smoke point, and does not itself authorize a five-vertex numerical result.

## Exact source objects

### Exact arXiv Eq.(11) object

Authoritative raw-TeX recovery from ITER048:

- source `arXiv:2302.00072`, exact `main.tex` SHA256 `bff93f3a7857658264a04eb23521bb935a68eccb7760b284589ff5ec4073f063`;
- raw-TeX artifact id `10334723630`, digest `sha256:191262f0c2a6d5c5b3ac6f1036caacd6808735c4bc38ecc73c45da49b2c53cb9`.

Eq. `\label{eq:vertex}` gives the five local vertex intertwiner lists, in the backend/source local `(i1,i2,i3,i4,i5)` argument order:

1. up: `(ib, i4, i11, i12, i2)`;
2. left: `(ib, i6, i13, i14, i4)`;
3. bottom-left: `(ib, i8, i15, i11, i6)`;
4. bottom-right: `(ib, i10, i12, i14, i15)`;
5. right: `(ib, i2, i13, i15, i10)`.

The exact same source neighborhood preserves the authors' code-name crosswalk:

- `rBCl=i1`, `rBCr=i2`;
- `rABl=i3`, `rABr=i4`;
- `rAEl=i5`, `rAEr=i6`;
- `rbl=i7`, `rbr=i8`;
- `rCDl=i9`, `rCDr=i10`;
- `rIul=i11`, `rIur=i12`;
- `rIu=i13`;
- `rIbl=i14`, `rIbr=i15`.

ITER048 already permanently records the separate displayed-Eq.(11) fifth-6j inconsistency (`i8` repeated while `i9` is absent). ITER049 resolves that specific routing issue structurally in favor of `COMMENT_REPAIR`; this file does not rewrite either terminal result.

### Pinned authors' executable EPRL implementation

`PietropaoloFrisoni/Monte_Carlo_spinfoams@84b375f2a2e0d29b44dd8820953553624bb007a3`, file `src/vertex_renormalization_EPRL_MC.jl`.

Immediately before each `vertex_compute` call, the executable source preserves the local intertwiner-range ordering in comments. Combining those exact comments with the arXiv code-name crosswalk gives:

1. up source-code local list:
   `(ib, rABr, rIul, rIur, rBCl)` = **`(ib, i4, i11, i12, i1)`**;
2. left:
   `(ib, rAEr, rIbl, rIu, rABl)` = **`(ib, i6, i14, i13, i3)`**;
3. bottom-left:
   `(ib, rbr, rIbr, rIul, rAEl)` = **`(ib, i8, i15, i11, i5)`**;
4. bottom-right:
   `(ib, rCDr, rIur, rIbl, rbl)` = **`(ib, i10, i12, i14, i7)`**;
5. right:
   `(ib, rBCr, rIu, rIbr, rCDl)` = **`(ib, i2, i13, i15, i9)`**.

This ordering is independently confirmed by the implementation's tensor mechanics: `sl2cfoam-next` stores the five vertex axes as `(i5,i4,i3,i2,i1)` in the wrapped Julia array, while `tensor_contraction!` contracts the first Julia axis with the Wigner-6j matrix. The resulting pre-contracted shapes in the authors' code exactly replace the corresponding left-side `i5` labels by their right-side recoupling labels before the final ten-intertwiner contraction.

## Exact mismatch census

Comparing literal Eq.(11) local `A_v` lists with the executable comments/crosswalk:

- up: Eq.(11) local i5 = `i2`; executable local i5 = `i1`;
- left: Eq.(11) local `(i3,i4,i5)` = `(i13,i14,i4)`; executable = `(i14,i13,i3)`;
- bottom-left: Eq.(11) local i5 = `i6`; executable = `i5`;
- bottom-right: Eq.(11) local i5 = `i15`; executable = `i7`;
- right: Eq.(11) local i5 = `i10`; executable = `i9`.

These differences are invisible in the all-zero primary/smoke sector but are material in the frozen alternating `0/1` held-out sector.

No amplitude value was used to discover or choose between these mappings.

## Interpretation ceiling

This source audit establishes that **ITER049's fifth-6j `COMMENT_REPAIR` PASS is not by itself a full local-vertex-argument crosswalk theorem**. ITER049 remains valid in its exact routing scope.

The discrepancies may arise from basis recoupling/orientation conventions between the displayed Eq.(11) formula and the executable tensor implementation; this record does not guess a repair and does not declare either object physically wrong.

## Consequence for the active ITER051 gate

No effect on the frozen ITER051 runtime smoke point: all five physical intertwiners are zero, so all listed mappings reduce to the same local zero tuple. ITER051 may proceed unchanged.

## Consequence for the next numerical gate

Even if ITER051 terminally PASSes runtime executability, **do not immediately execute the alternating held-out five-vertex summand** from ITER050's sector definition.

First run a separate prospectively frozen `LORENTZIAN_LOCAL_VERTEX_ARGUMENT_CROSSWALK` authority gate that determines, without amplitude fitting, which local argument mapping is the source-qualified object for the executable 5→1 contraction and how the authors' pre-contraction/Wigner-6j basis transformation reproduces the published formula.

Only after that crosswalk gate closes may a repaired bounded five-vertex primary/held-out numerical gate be preregistered.

## Persistent locks

No refinement map, no unbounded sum, no convergence claim, no bridge credit, no candidate theory. `refinement_map_derived=false`; `bridge_credit=false`; candidate theory remains `UNFORMED / 0%`.