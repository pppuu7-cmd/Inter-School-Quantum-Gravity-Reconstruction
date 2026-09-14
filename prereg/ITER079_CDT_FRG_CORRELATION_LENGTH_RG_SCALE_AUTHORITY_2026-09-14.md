# ITER079 preregistration — CDT correlation length ↔ FRG RG-scale authority

Date: 2026-09-14
Gate: `ITER079_CDT_FRG_CORRELATION_LENGTH_RG_SCALE_AUTHORITY`

## Motivation

ITER078 established, in scope, a direct equation-level reduced minisuperspace action/parameter crosswalk between CDT and the simplest FRG Einstein-Hilbert sector. Its single explicit retained blocker is the physical meaning of the cross-framework scale: the direct literature derives formulas containing `1/k` but also states that `a proportional_to 1/k` is only dimensional and that the relation between the geometric CDT correlation length and FRG `k` is not known well enough for direct critical-exponent matching.

ITER079 isolates this scale-setting problem. No further action-shape or parameter fit can compensate for a missing operational scale map.

## Frozen question

Does the frozen source stack provide a source-defined physical matching condition that maps the CDT geometric correlation length / finite-size-scaling trajectory to the FRG coarse-graining scale `k` beyond dimensional analysis?

A valid map must distinguish and relate, rather than collapse:

- dimensionless lattice correlation length `xi_CDT`;
- lattice spacing/cutoff `a` (and where relevant `a_t`);
- physical correlation length `ell_CDT = a * xi_CDT` or its source-defined gravitational analogue;
- FRG EAA coarse-graining scale `k`;
- a physical observable/resolution condition that says why a given CDT scale and a given FRG `k` represent the same physics.

## Frozen sources

Direct CDT↔FRG scale analysis:
- arXiv:2408.07808 — J. Ambjørn, J. Gizbert-Studnicki, A. Görlich, D. Németh, *Is Lattice Quantum Gravity Asymptotically Safe? Making contact between Causal Dynamical Triangulations and the Functional Renormalization Group*.
- arXiv:2411.02330 — J. Ambjørn, J. Gizbert-Studnicki, A. Görlich, D. Németh, *IR and UV limits of CDT and their relations to FRG*.

CDT scale/continuum authority:
- arXiv:1603.02076 — J. Ambjørn, D. Coumbe, J. Gizbert-Studnicki, J. Jurkiewicz, *Searching for a continuum limit in causal dynamical triangulation quantum gravity*.
- arXiv:2604.05641 — J. Ambjørn, R. Loll, *Causal Dynamical Triangulations: New Lattice Theory of Quantum Gravity*.

FRG scale semantics:
- arXiv:2302.14152 — F. Saueressig, *The Functional Renormalization Group in Quantum Gravity*.

No source outside this stack may upgrade the result after detailed adjudication.

## Required predicates

A. The CDT correlation-length object is explicitly defined operationally/geometrically, including whether `xi_CDT` is a conventional propagator correlation length, a volume/finite-size scaling length, or another gravitational observable.

B. The source gives the scaling of `xi_CDT` with `N_4`, distance variables and/or distance from the critical locus, including the finite-size assumptions and critical exponent used.

C. The relation between dimensionless `xi_CDT`, lattice cutoff `a` (and `a_t` where relevant), and a physical gravitational length is explicitly defined rather than assumed from ordinary fixed-background lattice field theory.

D. FRG `k` is explicitly defined operationally as a coarse-graining/resolution scale in the EAA, including regulator and mode-resolution semantics.

E. A source-defined matching condition identifies a CDT physical resolution/correlation length with an FRG scale. `a ~ 1/k`, `xi ~ k^-1`, or similar dimensional relations alone cannot satisfy this predicate.

F. The matching condition must state its validity range: IR, crossover, critical/UV region, or a specific reduced Einstein-Hilbert trajectory.

G. The mapping must preserve the distinction between a regulator cutoff (`a`), a diverging correlation length (`xi`), and a renormalization/coarse-graining parameter (`k`). It cannot identify all inverse lengths by name.

H. If a common observable is used to set the scale (e.g. volume/radius, Newton scale, curvature, spectral quantity), its value/normalization must be fixed independently enough that it does not merely reuse the target reduced-action correspondence being validated.

I. Critical exponents may be compared across CDT and FRG only after E-G establish the scale map. Similar exponent values or fixed-point language cannot substitute for the mapping.

J. Regulator/truncation/lattice dependence and anisotropy remain explicit. A map valid only in the reduced minisuperspace sector must remain typed as such.

K. Current 2026 status claims about a CDT UV critical path must retain evidence/theorem distinctions and cannot retroactively supply a scale map absent from the direct derivation.

## Frozen classifications

- `PASS_SCOPED_OPERATIONAL_CORRELATION_LENGTH_RG_SCALE_MAP_ESTABLISHED` only if A-J pass with an explicit physical matching condition.
- `PASS_SCOPED_REDUCED_SCALE_RELATION_ONLY` if the stack gives a nontrivial source-defined relation among `a`, `xi_CDT`, `k` and reduced couplings, but still lacks an independently operational physical matching condition.
- `SCOPED_BLOCKED_NO_OPERATIONAL_XI_TO_K_MAP_AUTHORITY` if both scale objects are well defined separately and the direct sources explicitly leave their physical relation unresolved.
- `FAIL_SCOPED_PROPOSED_SCALE_MAP_REJECTED` if a concrete proposed map is contradicted by the frozen source stack.
- `INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION` only for source-access failure.

## Mandatory controls

- `DIMENSIONAL_INVERSE_LENGTH_CONTROL`: dimensional `a ~ 1/k` or `xi ~ 1/k` cannot count as operational scale matching.
- `LATTICE_SPACING_CORRELATION_LENGTH_SWAP_CONTROL`: `a` and `xi_CDT` cannot be interchanged.
- `PROPAGATOR_GEOMETRIC_XI_SWAP_CONTROL`: gravitational/geometric correlation length cannot be treated as an ordinary matter propagator correlation length unless source-defined.
- `FIXED_K_FIXED_PHYSICS_CONTROL`: holding `k` or `lambda_k g_k` fixed while `a -> 0` is a continuum-scaling statement, not automatically an operational identification of `k` with the lattice correlation length.
- `CRITICAL_EXPONENT_PREMAP_CONTROL`: exponent comparison is forbidden before the scale map is established.
- `REDUCED_FULL_SCALE_CONTROL`: a scale relation in the minisuperspace reduction cannot become a full-theory RG-scale identity.
- `COMMON_UNIT_CONTROL`: expressing both sides in Planck or length units is necessary but insufficient for matching operational resolution.
- `TARGET_OBSERVABLE_CIRCULARITY_CONTROL`: an observable already used to construct the ITER078 reduced map cannot automatically count as independent scale validation.
- `REGULATOR_ERASURE_CONTROL`: FRG regulator/truncation and CDT lattice/anisotropy remain explicit.
- `UV_FIXED_POINT_PROMOTION_CONTROL`: compatibility with a critical path is not proof of a shared UV fixed point or common scale coordinate.

## Claim ceiling

Even the strongest PASS can establish only a scoped correlation-length/RG-scale relation under its stated observable and truncation assumptions. It cannot establish full CDT/FRG equivalence, a proven shared UV fixed point, a universal common parent, `BRIDGE_DERIVED`, new physics or a candidate quantum-gravity theory.

Candidate theory remains `UNFORMED / 0%`; bridge credit remains zero absent a later constitutional gate.

Predicates, source stack and classifications are frozen before detailed equation-level adjudication.