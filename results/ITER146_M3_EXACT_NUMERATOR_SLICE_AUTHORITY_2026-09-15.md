# ITER146 terminal result — exact interaction-dressed M3 numerator slices

Date: 2026-09-15
Gate: `ITER146_FIXED_GEODESIC_CURVATURE_M3_EXACT_NUMERATOR_SLICE_AUTHORITY`
Preregistration: `01c829aab04c10a2cbfbd209a944f8b502f1d39e`
Implementation: `79b29b606a0acc7a1bfe08b37da02a3bbc5f6383`
Workflow head: `229947b559e3738180282b77a59d2a81772ef0e2`
Authoritative run: `34994417063`
Job: `104466939263`
Artifact: `10406914029` (`iter146-m3-exact-numerator-slices`)
Artifact SHA256: `91b55142e1c01966c219953058b57a0b4fcc2cd9c84963344f15b51e5b9aa33e`

## Frozen classification

`FAIL_SCOPED_M3_TENSOR_ALLOCATION_OR_ROUTING_MISMATCH`

The frozen gate does **not** PASS because predicate D failed: the degree-8 polynomial interpolated from lambda=0..8 did not reproduce the withheld lambda=9,10 values on any of the four panels.

The remaining frozen checks passed:

- exact ITER145 routing / S3 momentum conservation;
- pinned ITER144 S3 blob authority;
- explicit R1, chi1, dR1 and three D=4 de Donder projector allocations;
- nominal interpolant degree 8 on all four panels;
- all S3 leg permutations;
- global `(Q,k)->(-Q,-k)` parity control;
- target blindness.

## Minimal cause localization

The failure is localized to an evaluator-domain mismatch, not yet to a physical tensor/routing contradiction.

ITER146 reused the ITER144 component evaluator `source_value`. That function was built and validated only on integer momentum panels and explicitly performs

`mom[p_i] = tuple(sympy.Integer(x) for x in p)`.

ITER145 routing at fractional affine parameter `tau` generates rational routed momenta

`p=-Q-(1-tau)k`, `r=Q-tau k`.

Therefore rational momentum components were coerced through `Integer(...)` before the S3 polynomial was evaluated. This destroys the exact rational affine dependence required by ITER146 and explains why a formally degree-8 tensor object failed degree-8 held-out interpolation.

This diagnosis does **not** retroactively invalidate ITER144: its frozen authority panels were integer-momentum panels, where the coercion is identity. It does invalidate use of that helper unchanged for rational routed momenta.

## Next admissible gate

Open a minimal rational-momentum S3 evaluator authority/repair gate that:

1. preserves the same pinned ITER144 source and parser;
2. replaces only integer coercion by exact SymPy expression preservation;
3. proves equality with the original ITER144 evaluator on integer panels;
4. verifies degree-two S3 momentum homogeneity on rational/symbolic panels;
5. reruns the frozen ITER146 numerator-slice held-outs without changing their tensor/routing predicates.

Only if that repair passes may the M3 branch proceed to a full invariant numerator/bubble-reduced representation.

## Claim ceiling

No full M3 invariant numerator, pole, B1, noncancellation, B0, EDT comparison, bridge, new physics or candidate theory is established. Candidate theory remains `0 / UNFORMED`; bridge credit remains 0.
