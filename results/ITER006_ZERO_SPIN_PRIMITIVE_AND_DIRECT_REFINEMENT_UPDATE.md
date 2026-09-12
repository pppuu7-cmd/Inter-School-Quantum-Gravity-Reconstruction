# ITER006 — zero-spin primitive and direct-refinement update

Date: 2026-09-12

## Direct DVD2↔DVD3 structural refinement audit

Authoritative run: `34710895347` on launch commit `674d842e256bba054a8a090509d1cc332e4710e9`.

Preregistered source facts and the face-cardinality argument were satisfied. DVD2 and DVD3 are source-labelled topologically distinct eight-face DVD graphs; under the arXiv:1010.5437 strict trivial-extension rule an injective 8→8 face map is bijective and leaves no additional refined face on which to place a new `j=0` coloring.

Classification: `DVD23_DIRECT_TRIVIAL_EXTENSION_EXCLUDED`.

Scope lock: this excludes only direct DVD2→DVD3 identification as a nontrivial trivial extension. It does not exclude Lorentzian fixed-boundary refinement using a newly constructed strict larger foam.

## One-zero-spin Lorentzian B4 primitive capability

Authoritative run: `34711008648`, head `b60cc12ac2927404d9d76a50be1fdd3f533c36a3`, aggregate job `103599966017`, aggregate artifact `10303646260`, digest `sha256:c9404133ba09be62129f217b97d05c16a0f6236d8772e34e2fe23b5b577d8814`.

Frozen gamma lanes `0.5,1.2,2.0`: 3/3 PASS. Each lane contained four one-zero-spin B4 placements and all four produced finite nonzero fast/accurate comparisons. Worst observed relative error across the aggregate was `2.03838e-16`, far below the frozen `1e-5` numerical-validity threshold.

Classification: `B4_ZERO_SPIN_PRIMITIVE_AGGREGATE_PASS`.

## Held-out asymmetric zero-spin robustness

Authoritative run: `34712687076`; preregistration commit `354c960a99aa2e5726d39e16108860bfc7f0711e`; launch commit `d11fefbd2826c3a3772da0d4c052298c063e7f18`; aggregate job `103604345234`.

Frozen held-out gamma values `0.3,0.8,1.6,2.5,3.0`: 5/5 PASS. All frozen asymmetric one-zero-spin B4 configurations passed; worst aggregate relative error was `1.74533e-06`, below the unchanged `1e-5` threshold.

Classification: `B4_ZERO_SPIN_ASYMMETRIC_HELDOUT_AGGREGATE_PASS`.

Scientific interpretation: the pinned Lorentzian B4 kernel has now passed both the original and an independent asymmetric held-out one-zero-spin numerical-validity gate. Further primitive-only zero-spin scans are saturated unless a new failure mode is identified.

Scope lock: numerical primitive support is not a refined 2-complex, a trivial-extension amplitude identity, cylindrical consistency, continuum convergence, or `BRIDGE_DERIVED`.

## DED→DLD source-topology candidate audit

Authoritative run: `34712970339`, launch commit `811a207f4bcd16c5709fc8c3b6b7429a154776b1`, artifact `10304455008`, digest `sha256:d62023021e50213e3424c46a2d4cb2fb75c7138287f21ba51c093486d515c4b6`.

The source audit found DED structural context, DLD structural context, and the independent refinement-definition context. It did **not** find an explicit textual DED↔DLD refinement relation and did not reconstruct an incidence-preserving injective V/E/F map.

Classification: `DED_DLD_STRICT_EXTENSION_CANDIDATE_SOURCE_QUALIFIED` with `strict_incidence_embedding_proven=false`.

This is PARTIAL only. Counts, names, or visual resemblance may not be promoted to a strict refinement relation.

## Lorentzian cylindrical-normalization source mapping

Authoritative run: `34712985651`, launch commit `0f1b5993147498af6a961bde27ba04b0389c1908`, job `103605014961`, artifact `10304340366`, digest `sha256:13349d2538ed2845e64353c8488868f8800832780ec28e7afb169d567ff2d979`.

The preregistered source audit found, in the same primary-source framework, all five required semantic objects: subfoam/refinement, trivial extension, cylindrical consistency, the multiplicity/automorphism factor, and the amplitude relation. The source explicitly distinguishes the raw coloring amplitude from the multiplicity-corrected amplitude and states cylindrical consistency for trivial extensions.

Classification: `LORENTZIAN_TRIVIAL_EXTENSION_NORMALIZATION_SOURCE_MAPPED`.

Scope lock: source mapping alone is not numerical cylindrical consistency in the DVD realization and gives no bridge credit.

## Active next gates

1. `ISQGR DED DLD Source Figure Incidence Audit` tests whether the pinned vector figures expose enough machine-readable incidence information to reconstruct a strict DED→DLD map without guessing.
2. RC006 relation-aware serialization retry uses independently validated source-reference relations but preserves the original 10-lane / 100%-agreement gate.
3. No DED/DLD amplitude identity is allowed before an incidence-preserving strict refinement map is actually established.
