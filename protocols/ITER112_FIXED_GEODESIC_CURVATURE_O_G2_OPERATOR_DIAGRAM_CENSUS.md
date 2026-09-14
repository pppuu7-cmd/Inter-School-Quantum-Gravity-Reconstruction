# ITER112 preregistration — fixed-geodesic curvature O(G^2) operator/diagram census

Date: 2026-09-15
Status: FROZEN BEFORE COMPUTE
Parent frontier: ITER111 terminal source-discovery saturation.

## Scientific question
Before any coefficient calculation or comparison to EDT, enumerate the perturbative sectors that can contribute to the separated connected scalar-curvature two-point observable at fixed fluctuating geodesic distance in 4D through O(G^2), and test whether dimensional/power-counting constraints alone can force cancellation of the G^2/l^8 sector.

## Frozen scope
This iteration is a structural census only. It does not calculate the physical coefficient. The observable is schematically
C_RR(ell)=<R(x) R(y) delta(d_g(x,y)-ell)>_c / <delta(d_g(x,y)-ell)>,
with metric expansion g=eta+kappa h and kappa^2 proportional to G.

Track three independent classes:
A. curvature-insertion expansion sectors R^(m)(x) R^(n)(y);
B. geodesic/world-function localization expansion sectors delta^(q)(d_0-ell) [delta d]^q and mixed curvature-localization terms;
C. renormalization/counterterm/contact sectors, separated from noncontact long-range sectors.

## Frozen power-counting rules
- In 4D, [G]=L^2 and [R]=L^-2.
- A nonzero separated connected O(G^p) RR tail has engineering scaling G^p / ell^(4+2p), modulo logarithms, absent another physical scale.
- Therefore p=2 implies ell^-8 and p=3 implies ell^-10.
- Local counterterms/contact distributions are not allowed to establish cancellation of a separated nonanalytic tail.

## Independent computation lanes
1. `sector-census`: enumerate perturbative order partitions contributing through O(kappa^4), preserving curvature vs localization origin.
2. `power-counting`: symbolic dimensional audit for all p=0..4 and verify the unique scale-free separated powers.
3. `cancellation-logic`: construct an algebraic independence table of source classes and test whether symmetry/dimensional information alone enforces pairwise cancellation. This is a logical null test, not a coefficient calculation.
4. aggregate: combine machine-readable outputs and classify only the structural gate.

## Frozen decision rule
PASS_SCOPED_STRUCTURAL_CENSUS if all lanes complete and show at least one symmetry-allowed O(G^2) separated sector while no frozen dimensional/symmetry rule forces its total coefficient to vanish.
NO_GO_SCOPED_SYMMETRY_FORCES_G2_CANCELLATION only if the preregistered algebraic rules produce an identity cancellation independent of numerical coefficients.
NUMERICAL_OR_IMPLEMENTATION_FAIL if the census is internally inconsistent.

A PASS does NOT establish a nonzero physical G^2 coefficient; it only authorizes a later explicit tensor/integral coefficient calculation. No EDT exponent comparison is authorized by this iteration alone.

## Claim locks
No ALL_KNOWN_SCHOOLS_FAIL, NEW_QG_THEORY_REQUIRED, NEW_PHYSICS_FOUND, BRIDGE_DERIVED, candidate action/Hamiltonian/field equations, or candidate-theory construction. Candidate theory remains 0/UNFORMED.
