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

Scope lock: this is numerical primitive support only. It does not establish a refined 2-complex, a trivial-extension amplitude identity, cylindrical consistency, continuum convergence, or `BRIDGE_DERIVED`.

## Next gate

A held-out asymmetric zero-spin primitive gate was preregistered at commit `354c960a99aa2e5726d39e16108860bfc7f0711e` and launched at commit `d11fefbd2826c3a3772da0d4c052298c063e7f18`, run `34712687076`. Frozen gamma values are `0.3,0.8,1.6,2.5,3.0`; the nonzero spins are asymmetric. PASS may only upgrade primitive numerical robustness, not bridge status.
