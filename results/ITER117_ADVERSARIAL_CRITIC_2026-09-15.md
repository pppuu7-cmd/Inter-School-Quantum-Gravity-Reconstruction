# ITER117 adversarial critic — fixed-geodesic curvature counterterm completeness

Date: 2026-09-15
Gate: `ITER117_FIXED_GEODESIC_CURVATURE_COUNTERTERM_COMPLETENESS_AUTHORITY`
Preregistration: `e4a795628797db43b8487d8a916c666600382431`
Source authority: `cab64a2fc6bc292b159e1ab9003aabb5a5541468`

## Attack 1 — if Z_chi is contact-only for RR, geodesic divergences must cancel automatically

Not established. The direct Z_chi variation of the lower-order RR correlator is contact-only, so the known scalar-style counterterm cannot absorb a separated divergence. This leaves two possibilities: separated divergences cancel among F/M/G, or the curvature-decorated line observable requires additional endpoint/line composite counterterms. Source authority does not select between them.

## Attack 2 — products of renormalized operators are automatically finite at separated endpoints

Too naive because the nonlocal geodesic operator integrates fluctuating fields along the path connecting the endpoints. UV singularities can arise when line insertions coincide with each other or approach endpoints even when the endpoints themselves remain separated. The matter calculation already demonstrates observable-specific geodesic divergences of this kind.

## Attack 3 — any new endpoint/line counterterm would destroy predictivity completely

Rejected. EFT/composite-operator renormalization normally yields a finite basis at fixed perturbative/derivative order. The issue is to enumerate that basis and specify renormalization conditions, not to assume arbitrary functions. ITER117 records basis incompleteness, not infinite arbitrariness.

## Attack 4 — local endpoint counterterms can generate separated tails through contractions

Possible for nonlinear/mixed endpoint operators, so the source audit correctly avoids the overstrong statement that **all** local endpoint mixing is contact-only. What is proven contact-only is the direct scalar-style Z_chi variation and local structures proportional to derivatives/multiples of the lower-order RR correlator. New nonlinear endpoint operators must be power-counted explicitly.

## Attack 5 — tangent-dependent counterterms violate rotational invariance

Not necessarily. The fixed geodesic supplies a physical unit tangent `n^mu`, so endpoint scalars such as `R_mn n^m n^n` are rotationally covariant functions of the physical line geometry. They would not introduce an arbitrary external direction beyond the observable's own separation vector.

## Attack 6 — because no explicit extra divergence is yet shown, the standard basis should be assumed sufficient

Rejected by the frozen sufficiency criterion. Absence of an explicit counterexample is not a renormalization theorem. The matter result proves sufficiency only for its own insertion/operator content.

## Attack 7 — ITER116 highest-pole shortcut is invalid entirely

Too strong. The RG logic remains correct once the renormalized curvature-specific observable is defined: a nonzero separated log coefficient `B_1` would prove noncancellation and is tied to the highest-log/pole structure. ITER117 only shows that the counterterm basis must be closed before assigning the net residue.

## Critic verdict

**CONFIRMS `PASS_SCOPED_ZCHI_SEPARATED_INACTIVE_CURVATURE_PRODUCT_COUNTERTERM_BASIS_OPEN`.**

The next task is not full loop integration but a finite power-counting/operator-mixing classification of line/endpoint counterterms at `O(G^2)`.

Bridge credit: **0**. Candidate theory: **UNFORMED / 0%**.