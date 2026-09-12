# ISQGR CURRENT FRONT

Date: 2026-09-12  
Active iteration: `ITERATION_006`  
Iteration completion: **74%**  
Amplitude/refinement cross-realization validation: **44%**  
Overall scientific programme readiness: **49%**  
Candidate-theory construction: **0% — UNFORMED / constitutionally locked**

## Preserved blockers

RC006 remains `SCIENTIFIC_FAIL_CONTRACTION_SERIALIZATION_UNSTABLE`; minimal Eq.(29) amplitude is BLOCKED. RC008 remains source-only BLOCKED. RC009 remains `SCOPED BLOCKED`. Lorentzian Delta4 finite-cutoff/profile/scaling remains `SATURATED NEGATIVE/SCOPED` with no bridge credit. Generic projector/orientation/envelope structure remains absorbed by standard amplitude-level TNR.

## Closed Lorentzian DVD finite-shell layers

Pinned source: arXiv:1801.03771. Pinned kernel: `qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f`.

Closed numerical layers include genuine Dl0 pilot `34703528413`, held-out Dl0 gamma 5/5 `34703682106`, B4 multishell validity 12/12 `34707794670`, symmetric finite shell sum `34708369655`, symmetric held-out gamma 5/5 `34708554742`, asymmetric mixed-spin B4 `34708641965`, asymmetric finite shell sum `34708800382`, asymmetric held-out gamma 5/5 `34709003568`, and symmetric D3 extension 8/8 `34708941068`. These remain finite-cutoff robustness results, not a refinement bridge.

## Refinement-source semantics

Run `34709790323` established `SOURCE_REFINEMENT_AUTHORITY_NOT_FOUND` for the pinned DVD source itself. DVD2 and DVD3 are different internal foams at the same two-4-link-dipole boundary and are not a direct coarse/fine boundary-refinement pair.

Run `34710188640` found refinement semantics across the source ladder but not an executable Lorentzian DVD refinement operator: `REFINEMENT_SEMANTIC_COMPONENTS_FOUND_BUT_LORENTZIAN_DVD_COMPATIBILITY_NOT_YET_ESTABLISHED`.

Run `34710443728` collected primary contexts from arXiv:0909.0939, 1010.5227 and 1010.5437. The useful source-level result is that Lorentzian fixed-boundary refinement/trivial extension is semantically authorized in the literature, but must be instantiated as an explicit larger foam rather than inferred from arbitrary-graph support alone.

## New terminal results

### Direct DVD2↔DVD3 structural audit

Run `34710895347`, launch commit `674d842e256bba054a8a090509d1cc332e4710e9`.

Classification: `DVD23_DIRECT_TRIVIAL_EXTENSION_EXCLUDED`.

Both source-labelled DVD2 and DVD3 have eight faces and are topologically distinct. Under the arXiv:1010.5437 nontrivial trivial-extension rule, an injective 8→8 face map is bijective and leaves no additional refined face for a new `j=0` coloring. This excludes only direct DVD2→DVD3 identification; a newly constructed strict larger foam remains allowed.

### Lorentzian one-zero-spin B4 primitive capability

Run `34711008648`, head `b60cc12ac2927404d9d76a50be1fdd3f533c36a3`, aggregate job `103599966017`, artifact `10303646260`, digest `sha256:c9404133ba09be62129f217b97d05c16a0f6236d8772e34e2fe23b5b577d8814`.

Classification: `B4_ZERO_SPIN_PRIMITIVE_AGGREGATE_PASS`.

Frozen gamma lanes `0.5,1.2,2.0` all passed. Each lane had four one-zero-spin placements with finite nonzero fast-vs-accurate comparisons; worst relative error was `2.03838e-16 < 1e-5`. This only qualifies the numerical primitive needed by a potential strict trivial extension. It does not establish a refined foam, amplitude identity, cylindrical consistency or `BRIDGE_DERIVED`.

Durable result: `results/ITER006_ZERO_SPIN_PRIMITIVE_AND_DIRECT_REFINEMENT_UPDATE.md`.

## Active gate

Held-out asymmetric zero-spin B4 robustness is active. Prereg commit: `354c960a99aa2e5726d39e16108860bfc7f0711e`. Launch commit: `d11fefbd2826c3a3772da0d4c052298c063e7f18`. Run: `34712687076`.

Frozen gamma panel: `0.3,0.8,1.6,2.5,3.0`; frozen nonzero spins are asymmetric. PASS can only upgrade primitive numerical robustness. It cannot create bridge credit.

## Exact next gate / claim locks

1. Consume and classify `34712687076` against its frozen `1e-5` numerical-validity threshold.
2. If PASS, construct and preregister an explicit strict larger Lorentzian fixed-boundary foam with at least one source-authorized `j=0` added face before evaluating any amplitude identity.
3. Only after an explicit source-mapped parent/refined pair exists may a non-retuned coarse/refined amplitude-consistency test be launched.
4. Do not substitute DVD2/DVD3, internal-face count, foam complexity or shell depth `D` for a genuine refinement map.
5. `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`, candidate action/Hamiltonian/field equations and RQIR/KMQGB promotion remain forbidden.

Iteration completion: **74%**. Amplitude/refinement validation: **44%**. Overall readiness: **49%**. Candidate theory: **0% / UNFORMED**.
