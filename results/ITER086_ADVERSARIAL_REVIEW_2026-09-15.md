# ITER086 adversarial review — canonical spectral-gap scale hypothesis

Date: 2026-09-15
Preregistration: `f54bb3238eb1a52923230537256e973936d82ec2`
Source authority: `16447e30a109dbe8aaa109cd39584de7e8a3273f`

## Attack 1 — the round-sphere check is an illicit fit

Rejected. The preregistration explicitly froze de-Sitter/round-sphere identities as **held-out consistency checks**. No round-sphere datum was used to choose `ell_1`, derive the TPFA coefficient, or tune the threshold hypothesis. The test is therefore out-of-sample with respect to `H_gap`.

## Attack 2 — the factor in the source radius convention may be nonstandard

The direct source writes

`R_k = 3/sqrt(Lambda_k) = 3/(sqrt(lambda_k) k)`.

Using that exact source convention and `z_1(S^3)=3/R_k^2` gives

`z_1/k^2 = lambda_k/3`,

so `H_gap: z_1=k^2` forces `lambda_k=3`.

Suppose instead one attempted to rescue the hypothesis by replacing this with the conventional four-dimensional Einstein relation `R^2=3/Lambda`. Then the equatorial `S^3` gap would satisfy `z_1=Lambda=lambda_k k^2`, and the same threshold hypothesis would force `lambda_k=1`.

Thus even the strongest normalization rescue changes `3` to `1`; it does not move the hypothesis into the source-qualified foliated Einstein-Hilbert region bounded by the `lambda=1/2` singular locus.

## Attack 3 — choose another eigenmode

Forbidden by `MODE_SELECTION_CONTROL`. Moreover higher round-sphere modes have `z_l=l(l+2)/R^2 > z_1` and would force an even smaller radius / larger dimensionless curvature at threshold, not repair the fundamental mismatch in a canonical way.

No mode switching is allowed after the failure of `ell_1`.

## Attack 4 — use a smooth regulator with no sharp threshold

Forbidden as a rescue. ITER086 froze the Litim-threshold hypothesis inherited from ITER085. A smooth regulator would define a different bridge hypothesis and must be preregistered separately. It cannot retroactively validate `H_gap`.

## Attack 5 — the fluctuation-flow `lambda=1/2` boundary uses a different coupling definition than the reduced/background map

This is a valid scope warning. The 2023 fluctuation paper itself cautions that couplings extracted in different background/fluctuation projections are not directly numerically identical.

For that reason the terminal failure does **not** rest solely on numerical transplantation of the `1/2` pole. The deeper problem is internal to the reduced self-consistent construction: assigning the global minisuperspace scale to the first nonconstant spatial mode forces an order-one dimensionless cosmological curvature (`lambda=3` in the source's stated convention) while the same direct comparison treats the relevant Gaussian regime with `lambda << 1`, and the connected asymptotic-safety flows used as comparators do not pass through that forced point.

The foliated `lambda=1/2` singular locus is corroborating domain evidence, not an erased scheme distinction.

## Attack 6 — the first nonzero mode can set a coarse-graining scale even if the minisuperspace fluctuation itself is a constant mode

In principle an external nonzero spectral probe can define a resolution scale for an effective action dominated by global modes. This observation prevents a stronger claim that **any** relation between `ell_1` and `k` is impossible.

But it does not save the specific equality `k^2=z_1`. The held-out self-consistent-background calculation fixes the ratio `z_1/k^2` as a function of the dimensionless curvature rather than as the universal constant one.

This attack therefore suggests the correct successor: test a source-derived relation `z_1/k^2 = F(lambda_k)` rather than a threshold identity.

## Attack 7 — matched numerical CDT data might shift the conclusion

No. The contradiction is analytic in the semiclassical limit and appears before inserting the numerical tuple. Consuming target data after this failure to search for a favorable exception would invert the preregistered logic and risk rescue-by-fit.

The matched datasets remain scientifically useful for a **new** prospectively frozen relation, but not for repairing ITER086.

## Verdict

The terminal-strength classification remains

**`FAIL_SCOPED_CANONICAL_GAP_SCALE_INCOMPATIBLE`**.

What fails is only the universal threshold equality for the lowest nonzero spatial mode. ITER084's normalization and ITER085's regulator support crosswalk remain valid.

The failure points directly to a better hypothesis class: the nonzero spatial gap should be related to the self-consistent background curvature and hence to `lambda_k`, not identified with `k^2` by itself.

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**.
