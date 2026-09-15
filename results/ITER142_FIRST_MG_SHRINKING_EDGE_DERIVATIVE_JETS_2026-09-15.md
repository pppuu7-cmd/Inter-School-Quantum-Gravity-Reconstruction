# ITER142 terminal result — first M/G shrinking-edge derivative allocation and sharp local jets

Date: 2026-09-15
Preregistration: `8351905f440d380692574dbd2efcf0073e4fd49f`
Implementation: `c7a650ae0aa3b6c2ef4a643bf06d14e82b351c70`
Workflow head: `f9d070ab0fb2c626591b294a23a07e44c4ac40d7`
Authoritative run: `34958694104`
Job: `104346825116` (`shrinking-edge-jet-audit`)
Artifact: `10391978026` (`iter142-first-mg-shrinking-edge-derivative-jets`)
Artifact SHA256: `04fbfe6de6aeee72376263591dcb495fb20aa0e2c1e3a356311ab31174bd6d1f`

## Scientific classification

`PASS_SCOPED_FIRST_MG_SHRINKING_EDGE_DERIVATIVE_JETS_CLOSED_LOCAL_RESIDUES_OPEN`

ITER142 recomputed all three exact D=4 connected-cross polynomials, reproduced the ITER141 shrinking-edge incidence, verified the actual shrinking-edge degree remains below the global ITER139 bound 5, and found nonzero highest homogeneous components on every singular edge.

## Sharp local endpoint bounds

The distinction between maximum line degree and the momentum on the edge that actually shrinks is decisive:

- `M_R2_chi1_dR1`: full polynomial degrees `(q,k)=(3,5)`, but ITER141 shows the lower singular edge is the q edge. Therefore `N_sing=3`, `s=0`, `m_raw<=5`, **jet<=4**. The degree-5 k line stays at fixed separation L and does not control this affine singularity.
- `M_R1_chi1_dR2`: degrees `(q,k)=(5,4)`, while the upper singular edge is k. Therefore `N_sing=4`, `s=1`, `m_raw<=6`, **jet<=4**. The degree-5 q line is the fixed-L companion.
- `G_R1_chi2_Gamma2_dR1`: degrees `(q,k)=(3,4)`. Lower uses q: `N_sing=3`, `s=0`, **jet<=4**. Upper uses k: `N_sing=4`, `s=1`, **jet<=4**.

Thus all actually singular endpoints in the first three connected M/G cross channels require at most Taylor order 4 before denominator-cancellation/contact reduction. This is a stronger graph-specific result than the conservative ITER141 max-line jet map; it does not weaken the global ITER139 bound for other rows.

## Scope boundary

Denominator cancellation, contact reduction, distributional endpoint terms and actual `1/epsilon` coefficients remain open. Those operations can lower or eliminate an ordinary local contribution, but they cannot raise the derivative ceiling proved here.

The quadratic-vertex self-pairing/local Wick channel remains a separate renormalization sector.

## Claim ceiling

No curvature pole residue, B1, noncancellation result, finite B0, EDT comparison, bridge, new physics or candidate theory is established. Candidate theory remains `0 / UNFORMED`; bridge credit remains 0.
