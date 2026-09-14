# ITER053 — Lorentzian five-vertex phase/weight authority

Date: 2026-09-14

## Terminal classification

**PASS — `LORENTZIAN_PHASE_WEIGHT_AUTHORITY_PASS_BOUNDARY_PHASE_QUALIFIED`**.

This is a source/normalization/convention PASS only. No Lorentzian vertex or five-vertex amplitude value was used in any lane. It does not establish a refinement map, an unbounded sum, shell convergence, coarse↔fine equality, bridge credit, or candidate theory.

## Frozen contract

Preregistration: `prereg/ITER053_LORENTZIAN_PHASE_WEIGHT_AUTHORITY_2026-09-14.md`.

The preregistration was strengthened prospectively before execution to include a phase-integral null point sensitive to omission of `df_phase`; no substantive lane had run when that control was added. Final prereg commit: `64e21b96eb968e6cafb77903f589bae380a15540`.

Source extract: `sources/ITER053_PHASE_WEIGHT_DATA.json`, commit `9a4c97544fbdd635ec3775b55a91f538419754ad`, blob `9b668b4b8ad749cb45eadd7b78434d9c1cd64bbb`.

Implementation: `code/iter053/phase_weight_authority.py`, commit `4fd6cc6ff7a1ac5306cf2afa627f28348e066b74`.

Production workflow head: `4fc286f657f7a6378cbc78a3fe4665ca392f4a6b`.

Authoritative run: **`34820237071`**.

## Exact source authorities

Paper source:

- arXiv `2302.00072`;
- exact `main.tex` SHA256 `bff93f3a7857658264a04eb23521bb935a68eccb7760b284589ff5ec4073f063`;
- ITER048 raw-TeX artifact `10334723630`, digest `sha256:191262f0c2a6d5c5b3ac6f1036caacd6808735c4bc38ecc73c45da49b2c53cb9`.

Pinned authors' executable source:

`PietropaoloFrisoni/Monte_Carlo_spinfoams@84b375f2a2e0d29b44dd8820953553624bb007a3`.

Pinned Lorentzian backend:

`qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f`.

## Paper ↔ executable face-weight identity

The paper source fixes

- standard face amplitude `A_f(j_f)=2j_f+1`;
- deformed family `A_f(j_f)=(2j_f+1)^mu`;
- standard member `mu=1`.

The author EPRL Monte Carlo code explicitly states that each internal face contributes `(2j+1)^(weight)`, constructs

`dfj = prod_{f=1}^{10}(2j_f+1)`

and multiplies the fixed contribution by `dfj^weight`. The exact BF control code uses `dfj` to the first power.

Therefore the Lorentzian source-family identification is

**`weight = mu`, with standard `weight = mu = 1`**.

The historical RC006 `alpha` from ITER010 belongs to a different reduced-Euclidean `SU(2)_k x SU(2)_k` q-dimension normalization family. It is not identified with Lorentzian `mu` and may not be imported into this front.

## Intertwiner-dimension reconstruction

Paper Eq.(11) contains `prod_{e=1}^{15}(2i_e+1)`.

The pinned backend source independently shows:

- the 15j kernel multiplies by `sqrt(DIM(i1) DIM(k2) DIM(k3) DIM(k4) DIM(k5))`;
- each B4 booster multiplies by `sqrt(DIM(i) DIM(k))`.

Thus each returned physical vertex component contains `sqrt(prod_{a=1}^{5} DIM(i_a))` in its five external physical intertwiner labels; virtual `k2...k5` dimensions close to full powers internally.

Using the source-qualified ITER052 original five local-vertex incidence lists, every global `i1...i15` occurs in two vertex/recoupling half-dimension incidences. The five author-code Wigner-6j recoupling matrices contribute an additional `sqrt(DIM(i_left) DIM(i_right))` over the recoupled pairs.

The exact symbolic lane gives **global exponent 1 for every `i1...i15`**. Therefore the paper edge product is already reconstructed by backend vertex normalization plus the Wigner recoupling factors.

A second manual `prod(2i+1)` multiplier would double count and is rejected by the frozen null control.

## Exact phase crosswalk

The author-code total fixed-summand phase is the product of:

1. `df_phase = (-1)^(2*(j1+...+j10))`;
2. five exact Wigner recoupling phases;
3. five exact final-contraction phases.

The symbolic lane derives the total author exponent coefficients:

- `j1,j3,j6,j7,j10`: coefficient 5;
- `j2,j4,j5,j8,j9`: coefficient 1;
- `i11...i15`: coefficient 1;
- boundary `jb`: coefficient 10.

Paper `chi` has coefficient 1 on each `j1...j10` and `i11...i15` and no boundary term.

Therefore

`E_author - chi_paper = 10*jb + 4*(j1+j3+j6+j7+j10)`.

For half-integer labels the `4*j` terms are even integers, and `10*jb` has the same sign parity as `2*jb`. Hence the complete source-qualified residual is exactly

**`phase_author / phase_paper = (-1)^(2*jb)`**.

There is no residual dependence on any bulk spin `j1...j10` or bulk intertwiner `i1...i15`.

For the frozen later sectors with `jb=1/2`, the conversion factor is `-1`.

This boundary factor is retained explicitly; it is not silently repaired away.

## Adversarial controls

All controls PASS.

- RC006 `alpha=mu` import is rejected by source/model identity.
- A second manual edge-dimension product is rejected because it changes all exact edge exponents from 1 to 2.
- Omission of the frozen up-recouping phase changes the residual sign on the prospectively frozen S0/S1/S2 panel.
- Omission of `df_phase` is detected by prospectively added S2, where the correct residual remains the boundary factor `-1` but the omission flips it to `+1`.
- Every correct frozen panel point gives exactly the boundary-only residual.

No amplitude value was used to construct or select these controls.

## Independent lane results

All five required lanes PASS:

- `paper-authority`;
- `author-code`;
- `backend-normalization`;
- `symbolic-crosswalk`;
- `null-controls`.

Aggregate classification: `LORENTZIAN_PHASE_WEIGHT_AUTHORITY_PASS_BOUNDARY_PHASE_QUALIFIED`.

## Actions provenance

Jobs:

- paper-authority `103899925979`;
- null-controls `103899926148`;
- backend-normalization `103899926169`;
- author-code `103899926179`;
- symbolic-crosswalk `103899926209`;
- aggregate `103900063193`.

Artifacts:

- author-code id `10338415602`, digest `sha256:0581409a358d83972ce7eceb1421efc5adfbcb0d6682a298f986b84fcb4cbe34`;
- paper-authority id `10338326079`, digest `sha256:975cf5a0e40342b2198eb06d436303f26e6eb48394912557290e871bca332d7a`;
- null-controls id `10338236518`, digest `sha256:59c040226743b9a4ecc535b198692f6b42d7f258d0d7a870cbdbe5e4d452633a`;
- symbolic-crosswalk id `10338121872`, digest `sha256:14d8b415aead80702eb6428ce62ef931f19ddb8cb3df5e89bdfe1a31796c97ac`;
- backend-normalization id `10337688316`, digest `sha256:76c83e40034245618316958df0dad9628e2f158100a78771e478ae150db43257`;
- aggregate id `10338081973`, digest `sha256:6bf6c97c9b8dd6f5d704893e71e9e1ec7472c5d5670cfddf36d0409b83fb8266`.

Manual raw-artifact audit agrees with the frozen aggregate. `amplitude_values_used=false` in every lane and aggregate.

## New structural fact

The Lorentzian paper and authors' executable implementation are source-equivalent for the fixed-summand **bulk** normalization and phase structure once the executable basis convention is accounted for. The only surviving sign mismatch is a boundary-state phase `(-1)^(2jb)`, while the full paper edge-dimension product is already embedded through backend/Wigner square-root factors.

This removes the last identified source-convention blocker before a genuinely executable bounded five-vertex fixed-configuration test.

## Authorized successor

A new separately preregistered bounded five-vertex fixed-configuration gate is authorized using:

- ITER051 exact validated pinned backend/runtime;
- ITER052 exact original local argument mapping and Wigner recoupling pairs;
- ITER053 standard Lorentzian `mu=weight=1`;
- no extra manual edge-dimension product;
- correct physical→doubled label conversion (`i=0→two_i=0`, `i=1→two_i=2`);
- the already outcome-independent frozen primary/held-out call map in `sources/ITER053_FIXED_SECTOR_BACKEND_CALL_MAP.json`;
- a prospectively declared reporting convention before execution.

The recommended production convention is `AUTHOR_EXECUTABLE_CONVENTION`, because it directly follows the pinned implementation. The corresponding paper Eq.(11) value may also be reported only through the pre-frozen conversion

`A_paper = (-1)^(2jb) * A_author`.

For `jb=1/2`, `A_paper = -A_author`.

## Claim ceiling

Even a successor bounded-summand PASS would establish only finite executable local fixed configurations. It would not establish an unbounded spin sum, shell convergence, coarse↔fine equality, a refinement map, bridge credit, or candidate theory.

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory remains **UNFORMED / 0%**.

Still unauthorized: unbounded ten-face summation, shell convergence, coarse↔fine equality, zero-face deletion, full Eq.(27), Eq.(29)/Lambda, one-step TNR, bridge derivation, candidate formation, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`.