# ITER123 adversarial critic — line form-factor / two-point kinematic projector

Date: 2026-09-15
Gate: `ITER123_FIXED_GEODESIC_CURVATURE_DEFECT_LINE_FORM_FACTOR_KINEMATIC_PROJECTOR`
Source authority: `sources/ITER123_FIXED_GEODESIC_CURVATURE_DEFECT_LINE_FORM_FACTOR_KINEMATIC_PROJECTOR_2026-09-15.md`

## Attack 1 — centering the line changes the physical observable

Rejected when all insertions are translated consistently. On the flat background the endpoint-anchored and centered parameterizations are related by a global translation. Their Fourier line factors differ by the expected phase `exp(i z/2)`, which is compensated by the translated endpoint insertion. Centering is a representation convenience, not a new relational prescription.

## Attack 2 — `u=0` is singular because the line factor contains `1/(q.n)`

Rejected. The exact centered factor is `Phi(z)=2 sin(z/2)/z` and has the regular continuous limit `Phi(0)=1`. Writing it as a quotient before taking the limit does not create a physical singularity.

## Attack 3 — two d=4 points are unsafe in dimensional regularization

The strengthened source result resolves this: for general `d`, the same kinematics `u=0,1/2` give

`det M_d=1/4`.

The inverse can therefore be applied to pole coefficients before the `d -> 4` limit. This avoids losing ordinary `d`-dependent trace information. Possible genuinely evanescent operator sectors in a future full loop calculation still have to be classified separately; ITER123 does not prove their absence.

## Attack 4 — evaluating the raw full amplitude at two points is enough

Rejected. The projector is valid only after bulk/contact, field-redefinition-redundant and other non-genuine structures have been consistently separated so that the relevant divergence lies in the ITER120-122 genuine defect span. Applying the 2x2 inversion prematurely would alias other structures into `rho_0,rho_1`.

## Attack 5 — line-form-factor zeros make the method unstable

They are known exceptional kinematics, not a structural failure. One simply avoids nonzero `z=2 pi k`. The first point `u=0` is regular, and for the second point `u=1/2` the external `Q,l` can be chosen generically away from zeros.

## Attack 6 — `u=1/2` has no Euclidean realization

Rejected. With `0<=u<=1` for real Euclidean `q,n`, `u=1/2` is an ordinary angle satisfying `(q.n)^2=q^2/2`.

## Attack 7 — the residues reconstructed by the projector are already B1

Rejected. They are genuine defect pole/mixing projections in the chosen basis. The physical `B_1` still requires the complete RG/pole combination with F/M/G, defect counterterms and gauge/field-redefinition consistency.

## Critic verdict

**CONFIRMS `PASS_SCOPED_TWO_POINT_KINEMATIC_PROJECTOR_FOR_GENUINE_DEFECT_RESIDUES`.**

The exact general-d two-point inversion is suitable as a computational projector for the next UV calculation, but only after basis reduction and counterterm subtraction are under control.

Bridge credit: **0**. Candidate theory: **UNFORMED / 0%**.