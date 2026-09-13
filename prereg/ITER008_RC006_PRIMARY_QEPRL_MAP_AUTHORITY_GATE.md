# ITER008 RC006 PRIMARY q-EPRL MAP AUTHORITY GATE — PREREGISTRATION

Date: 2026-09-13
Status: PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION

## Scientific question
Can the reduced Euclidean RC006 source object in Dittrich–Schnetter–Seth–Steinhaus, arXiv:1609.02429v2, be reconstructed directly from equations explicitly printed in that primary source, without importing the blocked Lambda/q-binomial convention path?

## Source object and scope
Primary source: arXiv:1609.02429v2.
Frozen source equations:
- Eq. (22): j+ = (1+gamma) l / 2, j- = (1-gamma) l / 2 for gamma<1.
- Eq. (23): at jmax=k/2, mapped j+,j- must be admissible integer representations <= jmax in the integer-representation sector used by the paper.
- Eqs. (35)-(36): [n] = (q^(n/2)-q^(-n/2))/(q^(1/2)-q^(-1/2)), q=exp(2*pi*i/(k+2)), equivalently sin(pi*n/(k+2))/sin(pi/(k+2)).
- Eq. (37): d_j=[2j+1].
Published nontrivial map controls explicitly listed by the source: k=6,gamma=1/3; k=10,gamma=3/5; k=12,gamma=1/3.

This gate is only a reduced Euclidean quantum-group/TNR source-authority and algebra reconstruction certificate. It is NOT the Lorentzian EPRL amplitude, NOT the blocked Lambda low-spin general formlamb6j reconstruction, NOT a genuine multivertex refinement map, and carries zero bridge credit by itself.

## Frozen streams
A — q-number convention equivalence and root-of-unity controls.
- k in {6,10,12}; integer n=1..k+1.
- complex-q and sine forms must agree within 1e-12 absolute.
- [0] and [k+2] must vanish within 1e-12.
- d_j must be positive for integer admissible j=0..floor(k/2).

B — published EPRL map controls.
- Exhaustively enumerate rational gamma=p/q in (0,1), reduced, denominator <= 12, on integer l=0..jmax.
- Apply Eq. (22) and integer/admissibility rule of Eq. (23).
- The three source-listed pairs must reproduce exactly:
  k=6,gamma=1/3 includes l=3 -> (2,1);
  k=10,gamma=3/5 includes l=5 -> (4,1);
  k=12,gamma=1/3 includes l=3 -> (2,1) and l=6 -> (4,2).
- No source claim is made that these are exhaustive across all possible gamma conventions beyond the frozen enumeration; the gate only tests exact reproduction of printed controls.

C — forbidden-map/null controls.
- For each k, perturb each accepted published gamma by +/-1/60 when it remains in (0,1); at least one nontrivial source-listed endpoint mapping must fail exact integer Eq. (23) admissibility for each perturbed gamma.
- Deliberate wrong q convention q=exp(i*pi/(k+2)) must disagree with Eq. (36) for at least 80% of n=2..k.

D — numerical convergence / independent evaluation.
- Re-evaluate q-numbers at 50 decimal digits using mpmath and compare to double-precision sine values; max relative discrepancy on nonzero values <=1e-12.
- Symmetry [n]=[k+2-n] must hold <=1e-12 for n=1..k+1.

## Frozen interpretation
PASS only if all A-D predicates pass: `RC006_PRIMARY_QEPRL_MAP_SOURCE_RECONSTRUCTED_SCOPED`.
Any source-equation/published-control mismatch: `SCIENTIFIC_FAIL_SOURCE_RECONSTRUCTION_MISMATCH`.
Dependency/runtime/parser failure before predicates: `INFRASTRUCTURE_OR_NUMERICAL_FAIL`.

PASS does not promote Eq.(29)/formlamb6j, does not resolve the prior q-binomial provenance blocker, does not establish a Lorentzian or multivertex refinement bridge, and does not change candidate-theory status.

Frozen thresholds and controls must not be changed after production evidence is observed.
