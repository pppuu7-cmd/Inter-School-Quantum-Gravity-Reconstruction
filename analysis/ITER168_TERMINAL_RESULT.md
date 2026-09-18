# ITER168 terminal result — semantic provenance audit

Date: 2026-09-18.

Authoritative execution: commit `b68870800d5750f3fcf880e830a454fa0cea52fc`, run `35322037024`.

Jobs: extractor `105526478677`; leakage critic `105526478813`; completeness critic `105526478904`.

Extractor artifact `10537741739`, ZIP SHA256 `b77e63d80721d22b0f22fd2dc94337451f548763bbdf9c05aed1894195b779c3`.

## Scientific classification

**`BLOCKED_SCOPED_ITER168_MISSING_EXECUTABLE_SOURCE_GEOMETRY`**.

All three jobs were technically green, but green CI is not scientific PASS. The extractor's only `iter163_geometry_hits` were `s.Rational(x.numerator,x.denominator)` in the ITER163 reconstruction/critic. Those denominators are rational-number representation denominators, not the physical propagator/phase denominator geometry required by the frozen ITER168 preregistration. Therefore the lane-local `PASS_SCOPED_SUBCHECK_EXECUTABLE_PROVENANCE` does not satisfy the preregistered scientific PASS condition.

The audit did successfully remove the ITER167 prose-leakage failure mode: Markdown/recovery/navigator text is no longer needed as positive evidence. But the trace from the ITER163 21-term/open-leg reconstruction to source-derived endpoint singular geometry is still not established.

## Preserved results and locks

ITER163 source-complete tensor bookkeeping/K-divisibility remains scoped valid. ITER164-166 blockers and the ITER167 provenance-leakage scientific failure remain preserved. No Laurent/R-operation, ITER118 matching, `B1_total`, bridge credit, candidate equations or candidate theory is authorized.

## Next admissible gate

ITER169 upstream-source trace gate: trace `analysis/iter163_complete_covariant_reconstruction.py -> analysis/iter161_endpoint_open_leg_factorization.py -> analysis/iter140_first_mg_general_d_invariant_continuation.py` and the source-derived affine Wick/denominator-support chain. Positive evidence must mechanically connect the G-family endpoint open vertex to source occurrence/Wick-edge geometry and denominator/contact support, not merely share labels. Independently falsify the trace and test endpoint/orientation/contact consistency. A PASS may only authorize rebuilding the source-qualified singular-sector manifest; it does not authorize Laurent/R-operation or bridge credit.