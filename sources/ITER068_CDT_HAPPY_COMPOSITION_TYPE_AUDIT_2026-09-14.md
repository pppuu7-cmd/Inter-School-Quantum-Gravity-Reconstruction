# ITER068 source/structure audit — CDT vs HaPPY composition type

Date: 2026-09-14
Gate: `ITER068_CDT_HAPPY_COMPOSITION_TYPE_DISCRIMINATION`
Preregistration commit: `a50779bcd93ba34546b16751d61245ad45e6ee01`

## Frozen authority

### CDT / RC002

Inherited without alteration from terminal ITER067:

- Ambjørn, Jurkiewicz, Loll, arXiv `hep-th/0105267v1`.
- Ambjørn et al., arXiv `1205.3791v1`.
- Ambjørn et al., arXiv `1302.2210v1`.

The source-qualified regulated object is the full transfer-matrix semigroup

`G_N(g1,g2;t1+t2) = sum_g C(g) G_N(g1,g;t1) G_N(g,g2;t2)`

with spatial-triangulation state space, automorphism-weighted identity resolution, one-step sandwich amplitudes, preferred discrete proper time, and the ITER067 positivity limitation (`T_N^2` in d>2, not general elementary-`T_N` positivity).

### HaPPY / RC005

Primary authority frozen to:

F. Pastawski, B. Yoshida, D. Harlow, J. Preskill, *Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence*, arXiv `1503.06237v2`, JHEP 06 (2015) 149.

Exact source objects used:

1. Definition 1 / Eqs. (1)–(2): an isometry `T : H_A -> H_B` preserves inner products and obeys `T^dagger T = I_A`.
2. The paper explicitly notes that composition of isometries is again an isometry.
3. Definition 2: a perfect tensor is proportional to an isometry for every allowed bipartition.
4. Section 3: neighboring perfect-tensor legs are contracted; open boundary legs are physical spins; extra open legs in the pentagon code are bulk/logical inputs.
5. Theorem 1: the full pentagon-tiling network is an isometry from bulk logical degrees of freedom to boundary physical degrees of freedom, obtained by layer-wise composition of local isometries.
6. The construction is an exactly solvable toy model/QECC encoder. The frozen source does not define the network layers as Lorentzian proper-time evolution or a gravitational transfer matrix.

## Typed objects

### CDT composition object

Let `H_t` be the regulated Hilbert space spanned by unlabelled spatial triangulations at discrete proper time `t`, with source-defined automorphism-weighted inner product/identity.

A one-step transfer map has amplitudes

`T_CDT : H_t -> H_(t+1)`

whose matrix elements are sums over Lorentzian sandwich triangulations with state-sum action and `1/C(T)` combinatorial measure. Sequential composition is temporal gluing over an intermediate geometry and explicitly requires the `C(g)` factor.

Physical semantics:

- succession in preferred discrete proper time;
- dynamical path-sum amplitude;
- state-space automorphism quotient/weight;
- propagation between spatial geometries.

### HaPPY composition object

Let

`V_H : H_bulk -> H_boundary`

be the perfect-tensor network encoder.

Local perfect tensors are oriented as isometries for an admissible input/output bipartition; neighboring internal tensor legs are contracted. For the pentagon code, a layer ordering gives a proof that the composed network remains an isometry.

Physical semantics:

- logical-to-physical quantum encoding;
- tensor/subsystem contraction;
- inner-product preservation on the code input;
- operator pushing and boundary reconstruction;
- static hyperbolic code geometry in the frozen realization.

## Frozen mandatory comparison

| mandatory coordinate | CDT | HaPPY | source-faithful common image? |
|---|---|---|---|
| domain/codomain | spatial geometry at `t` -> spatial geometry at `t+1` | logical/bulk factors -> physical/boundary factors | only after forgetting physical type |
| composition | temporal semigroup / history gluing | tensor-leg contraction / composition of isometries | yes at weak linear/tensor algebra level |
| normalization/measure | `1/C(T)` history weight and `C(g)` intermediate-state factor | `V^dagger V = I` isometric normalization | no source-derived identification |
| dynamics | gravitational transfer amplitude from action-weighted histories | encoder; no frozen gravitational time-evolution law | mismatch |
| causal/time semantics | distinguished discrete proper-time succession | no source-defined Lorentzian temporal succession in the static code | mismatch |
| observables | transition amplitudes / spatial-geometry propagation; reduced-volume observables are secondary/effective | logical operators, boundary reconstructions, entanglement/QEC observables | no source-derived transport |
| quotient/equivalence | automorphism-weighted unlabelled triangulations | tensor/Hilbert-space code equivalences | no source-derived identification |

## Weak common algebraic kernel

There is a valid but deliberately weak commonization:

`U_CDT : C_CDT -> Lin`

`U_HAPPY : C_HAPPY -> Lin`

where `Lin` retains only finite-dimensional linear maps/tensors and their contraction/composition.

Under this forgetful map:

- CDT matrix multiplication/semigroup composition contracts an intermediate state label;
- HaPPY tensor-network assembly contracts internal Hilbert-space indices;
- associativity of linear-map/tensor contraction is common.

This is **not** physically sufficient for the preregistered PASS because `U_CDT` and `U_HAPPY` erase precisely the mandatory semantics that distinguish the mechanisms.

Classification of this fact:

`COMMON_ALGEBRAIC_KERNEL_ONLY`.

## Why the strong physical hypothesis fails

### 1. Dynamics cannot be preserved by the frozen commonization

CDT composition is part of the regulated gravitational dynamics: its matrix elements are action-weighted sums over interpolating histories.

HaPPY composition proves that a static network is an isometric QECC encoder. The frozen source supplies no gravitational time-evolution law whose composition is the layer-wise tensor contraction.

Identifying encoder depth with physical evolution would add a new dynamical postulate.

### 2. Time/causal semantics cannot be preserved

The CDT arrow is explicitly indexed by discrete proper-time slices and glues consecutive slabs.

The HaPPY layer ordering is sufficient to prove an isometry of a hyperbolic tensor network, but the frozen source does not identify that ordering with Lorentzian proper time or causal succession.

Therefore

`CDT proper time = HaPPY radial/layer depth`

is `NEW_BRIDGE_ASSUMPTION`, not a source-derived map.

### 3. Measure/isometry structures are not the same object

CDT's `C(g)` and `1/C(T)` factors encode automorphism counting in the triangulation state sum and are required for correct gluing.

HaPPY's `V^dagger V = I` encodes inner-product preservation of the logical-to-physical map.

Both are normalization-relevant, but no frozen source derives one as an image/quotient of the other. Replacing both by the word `normalization` destroys physical content.

### 4. Observable transport is absent

CDT's native comparator is propagation between spatial geometries and, only after reduction, spatial-volume observables.

HaPPY's native exact observables are logical operators, their boundary representations, and entanglement/QEC quantities.

No source-defined map sends a nontrivial CDT observable class to the HaPPY logical/QEC observable class while preserving interpretation.

### 5. Domain/codomain types differ before forgetting

A temporal state transition between spatial geometries is not a logical-to-physical encoding map. They become formally comparable only after forgetting these object types.

Therefore the strong common parent is not derived by the frozen sources.

## Controls

C1 `FORGETFUL_LINEARIZATION_CONTROL`: **DETECTED / WEAK COMMONALITY ONLY**. Both objects descend to generic linear/tensor composition, but mandatory semantics are lost.

C2 `TIME_RADIAL_SWAP_CONTROL`: **REJECTED**. No source-derived identification of proper time with network depth.

C3 `NORMALIZATION_DROP_CONTROL`: **DETECTED**. Dropping CDT automorphism factors or HaPPY isometry destroys qualified source structure.

C4 `FULL_EFFECTIVE_COLLAPSE_CONTROL`: **REJECTED** by inherited ITER067 full/effective separation.

C5 `DYNAMICS_ENCODING_SWAP_CONTROL`: **REJECTED**. Transfer dynamics and QEC encoding are distinct source objects.

C6 `OBSERVABLE_ERASURE_CONTROL`: **DETECTED**. A commonization omitting native observables is only algebraic.

C7 `TOY_MODEL_PROMOTION_CONTROL`: **REJECTED**. HaPPY remains a toy-model mechanism card, not a full QG realization.

All seven controls behave as preregistered.

## Researcher classification

The source stack is sufficient to adjudicate the gate; this is not a missing-authority BLOCKED result.

The strongest source-faithful common object is the forgetful algebraic kernel of linear-map/tensor composition. It cannot preserve/derive the mandatory physical coordinates without additional bridge assumptions.

**Researcher verdict:**

`FAIL_SCOPED / PHYSICAL_COMPOSITION_TYPE_EQUIVALENCE_REJECTED`

with retained positive sub-result:

`COMMON_ALGEBRAIC_KERNEL_ONLY`.

## New structural fact

The Interface-Atlas coordinate `C` is too coarse for bridge accounting. At minimum, this gate resolves two source-grounded subtypes:

- `C_seq` — temporal/state-sum sequential composition with physical propagation semantics and history/state measure data;
- `C_tensor` — subsystem/tensor-contraction composition implementing an isometric encoding map.

A future parent principle may still encompass both, but it must *derive* the typed embeddings and their semantics; it cannot identify them merely because both use contraction/composition in linear algebra.

## Scope / claim ceiling

This result does not show:

- that no common categorical parent can ever exist;
- that HaPPY is irrelevant to quantum gravity;
- that CDT is incompatible with holography;
- that composition/refinement H0 is globally false;
- that all quantum-gravity schools use inequivalent composition;
- any full bridge, common parent, new theory, or new physics.

It rules out only the strong source-faithful identification of these two frozen composition mechanisms **without additional physical structure**.