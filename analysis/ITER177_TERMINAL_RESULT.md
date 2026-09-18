# ITER177 terminal result — RC008 held-out non-retuned transport

Date: 2026-09-19

## Authoritative execution
- workflow head: `57a62ecb0e029ed72a2dc162cb4888fd3cd04a49`
- run: `35399067738`
- calibration job: `105774550517`
- P1 job: `105774550909`; artifact `10570042417`; sha256 `4ee0e751340de83839cc88779abe8b2e87e127f56f38a6d66bf64e00fc736b13`
- P2 job: `105774550865`; artifact `10570082378`; sha256 `387ea7319abeb3978dfbb37b668b6f4660ff63639360f45f2dd20046cc82aff3`
- H1 job: `105774550835`; artifact `10569027815`; sha256 `5547b572b5f5294471011baa07eee029d644f81d61dedb17d9854ba22fbe19bf`
- H2 job: `105774550795`; artifact `10570282114`; sha256 `5f3fcfc4b8ef99734388a08ef1bedf2c52b6716c8a401c1508b2987341c4b630`
- H3 job: `105774550768`; artifact `10570172307`; sha256 `38e29236aa747e9b55832794a9971d9350e4a538491946bab651f647e520a755`
- H4 job: `105774550763`; artifact `10569697565`; sha256 `02f63ad04f9c820731a28c44c4fd770ec3403c6e914fa9f1bc8662b482367c1a`
- aggregate job: `105774674791`; artifact `10568907833`; sha256 `9e341c6d6ada06a2505244a35456022b82a73834f3e7d5809a6e0ac4036e44ce`

## Scientific adjudication
`INVALID_IMPLEMENTATION_OR_SELECTOR_SYMMETRY_FAIL`

Green CI is not scientific PASS. Calibration passed and no artifacts were missing. All six held-out boundaries satisfied the frozen numerical convergence checks. However the two preregistered permutation controls P1 and P2 had no robust crossing, so the frozen selector-symmetry prerequisite failed before H1–H4 can be used for a scientific transport verdict.

For record only, without promoting the result: H1, H2 and H4 showed robust crossings on [0.50,0.55], while H3 did not. These observations cannot rescue the gate because the control prerequisite failed.

## Claim ceiling
- bridge credit: false
- candidate theory: UNFORMED / 0
- full EPRL refinement: not established
- Lorentzian refinement: not established
- new physics: not established

No threshold, boundary tuple, seed, alpha grid, model or selector is retuned after seeing this result. Re-running the same panel is scientifically inadmissible without a prospectively justified implementation correction or an independently preregistered diagnostic that can distinguish implementation mismatch from genuine selector-symmetry failure.
