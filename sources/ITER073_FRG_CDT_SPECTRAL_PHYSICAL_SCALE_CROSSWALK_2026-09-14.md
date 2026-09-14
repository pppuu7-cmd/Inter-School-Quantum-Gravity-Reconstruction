# ITER073 source authority — FRG/QEG ↔ CDT spectral physical-scale crosswalk

Date: 2026-09-14
Gate: `ITER073_FRG_CDT_SPECTRAL_PHYSICAL_SCALE_CROSSWALK`
Preregistration commit: `8082e08b2b5349b53b5ffbf20a4676a2e57bf859`

## Frozen sources

### CDT
- arXiv:hep-th/0505113 — J. Ambjorn, J. Jurkiewicz, R. Loll, *Spectral Dimension of the Universe*.
- arXiv:1603.02076 — J. Ambjorn, D. Coumbe, J. Gizbert-Studnicki, J. Jurkiewicz, *Searching for a continuum limit in causal dynamical triangulation quantum gravity*.

### QEG / FRG
- arXiv:hep-th/0508202 — O. Lauscher, M. Reuter, *Fractal Spacetime Structure in Asymptotically Safe Gravity*.
- arXiv:1110.5224 — M. Reuter, F. Saueressig, *Fractal space-times under the microscope: A Renormalization Group view on Monte Carlo data*.

## Executive authority result

The frozen stack does **not** supply an independently normalized 4D physical-resolution crosswalk. It supplies:

1. a common spectral-dimension / heat-kernel observable definition;
2. a CDT-internal relative diffusion/lattice scaling law plus a conditional absolute lattice-spacing estimate;
3. a QEG source-defined relation among heat-kernel modes, Laplacian eigenvalues, RG resolution and anomalous walk scaling;
4. a highly successful published **3D** QEG-to-CDT curve fit.

What is missing is an independent absolute map that fixes the common 4D physical resolution before looking at the target CDT spectral-dimension curve.

## Predicate A — CDT integer diffusion duration -> absolute physical heat parameter/resolution

**PARTIAL / INSUFFICIENT FOR ABSOLUTE CROSSWALK.**

The 2005 CDT source defines continuum fictitious diffusion time `sigma`, notes that it has length dimension two, and on ordinary flat geometry gives the Gaussian relation in which `sqrt(sigma)` measures linear spread. But it explicitly says that translating the lattice result to continuum dimensionful quantities requires a dimensional transmutation and is subtle. Its proposed continuum form contains an unspecified order-one constant.

The discrete CDT implementation uses integer random-walk steps on the dual simplicial structure. The 2016 source materially improves the scale authority by showing that relative comparisons require `sigma/a_rel^2`, and independently estimates the microscopic lattice spacing `a_abs` in Planck units from volume fluctuations.

However, the frozen sources do not close the absolute diffusion normalization

`T_CDT = C_diff(kappa0,Delta,anisotropy,dual geometry) * a_abs^2 * sigma`

with a source-defined `C_diff` valid over the quantum regime. In particular, knowing `a_abs` does not by itself identify the physical centre-to-centre diffusion step or eliminate spacelike/timelike/simplex-geometry dependence.

Thus the relative calibration established in ITER072 is real, but predicate A's stronger absolute cross-school normalization is not source-qualified.

## Predicate B — QEG heat parameter -> mode/RG resolution, anomalous walk retained

**PASS_SCOPED.**

QEG defines a family of scale-dependent effective metrics/Laplacians and identifies a Laplacian eigenmode with eigenvalue `E_n` as probing RG scale

`k^2 = E_n`,

with flat-reference resolution `ell ~ 1/sqrt(E_n)`.

The return probability is not generally controlled by the classical kernel `exp(-p^2 T)` but by

`exp[-p^2 F(p^2) T]`,

where `F` inherits the running effective geometry. In a power-law regime `F(p^2) ~ p^delta`, the untraced kernel has scaling variable

`r / T^(1/(2+delta))`

and therefore

`D_w = 2 + delta`.

Consequently `ell ~ sqrt(T)` is valid only in the regular-diffusion regime `delta=0`; it is not a universal physical-resolution rule across QEG regimes.

## Predicate C — common independently fixed physical normalization

**BLOCKED.**

CDT has a conditional `a_abs/l_Pl` estimate, but the absolute diffusion-step normalization remains incomplete. QEG can describe scales relative to the Planck scale along specified trajectories, but the frozen source does not provide an independently selected 4D QEG trajectory and absolute heat-parameter normalization corresponding to the sampled CDT ensembles.

A common unit label such as `l_Pl` therefore does not yet fix the same physical resolution on both sides.

## Predicate D — diffusion parameter vs walk distance vs RG resolution

**PASS_QEG / PARTIAL_CDT / CROSSWALK_BLOCKED.**

QEG explicitly separates:

- fictitious heat-kernel parameter `T`;
- RG/mode scale `k ~ sqrt(E)`;
- physical resolving length `ell ~ 1/k` for a mode;
- typical diffusion displacement, whose scaling is governed by `D_w` and can be anomalous.

The CDT sources distinguish diffusion time from proper time and provide spectral scale calibration, but the frozen 4D stack does not provide a comparator-grade running walk-dimension / displacement law that would allow the QEG anomalous diffusion distance to be matched physically regime by regime.

This omission matters because the QEG source itself notes that if CDT and QEG spectral dimensions agree in a nonclassical regime, their walk dimensions need not agree; their microscopic Hausdorff structures are typed differently.

## Predicate E — mutually reliable comparison window

**PARTIAL.**

CDT supplies an empirical reliability window by excluding short-walk odd/even artifacts and long-walk finite-size effects. QEG explicitly marks theory-space regions where the Einstein-Hilbert truncation becomes unreliable.

Thus reliability cuts exist on both sides. But without the missing independent scale normalization, the source stack cannot prove that these windows overlap at the same 4D physical resolution.

## Predicate F — independent QEG trajectory selection

**FAILS FOR THE PUBLISHED DIRECT FIT / NO ALTERNATIVE FROZEN AUTHORITY.**

The 2011 paper performs an impressive direct QEG/CDT comparison in `d=3`, obtaining approximately percent-level agreement over a reliable diffusion-time interval. But its procedure explicitly selects the QEG RG trajectory by fitting its initial conditions to the target CDT spectral-dimension data.

That is valid evidence that QEG can represent the curve, and it is scientifically informative about which QEG regime the data resemble. It is not an independent scale bridge under ITER073 because the target observable is used to select the comparator trajectory.

The same source says that an analogous `d=4` comparison would require detailed 4D Monte Carlo data. No frozen source supplies a 4D QEG trajectory/scale normalization fixed independently of the target 4D `D_s` curve.

## Predicate G — genuinely four-dimensional crosswalk

**NOT ESTABLISHED.**

Both theories have 4D spectral-dimension predictions/measurements. But the detailed source-level direct fit and trajectory inference in the frozen QEG stack is 3D. The source explicitly distinguishes this and says the 4D comparison requires access to detailed 4D Monte Carlo data.

The 3D fit therefore cannot be promoted to 4D physical-scale authority.

## Predicate H — claim ceiling

**PASS_CONTROL.**

Even a future scale-matched spectral agreement would authorize only a same-observable comparator. No microscopic equivalence follows.

## Additional structural finding — spectral equality does not imply walk equality

The QEG analysis gives, in scaling regimes,

`D_s/2 = d_H/D_w`.

It also notes that QEG keeps `d_H = d`, whereas CDT may have nonclassical microscopic Hausdorff structure. The paper explicitly concludes that even if `D_s^CDT = D_s^QEG` in a nonclassical regime, one should not generally expect `D_w^CDT = D_w^QEG` there.

This is a direct warning against turning a shared spectral-dimension curve into a universal physical-distance calibration.

## Controls

- `SQRT_T_UNIVERSAL_DISTANCE_CONTROL`: triggered successfully; QEG has `D_w != 2` outside the classical regime.
- `DIFFUSION_RG_TIME_SWAP_CONTROL`: passes; no heat time/RG time identity is made.
- `RG_SCALE_DIFFUSION_SCALE_SWAP_CONTROL`: passes; QEG scale enters through mode spectrum and `F(p^2)` rather than a universal `k=1/sqrt(T)` rule.
- `CDT_ABS_LATTICE_DIFFUSION_NORMALIZATION_CONTROL`: triggers; `a_abs` alone does not fix the full absolute diffusion normalization.
- `FIT_CIRCULARITY_CONTROL`: triggers on the published 3D direct fit; fit quality is retained but not counted as independent bridge authority.
- `3D_TO_4D_PROMOTION_CONTROL`: triggers; 3D fit cannot authorize 4D.
- `ANOMALOUS_WALK_ERASURE_CONTROL`: triggers; walk dimension remains explicit.
- `FINITE_WINDOW_CONTROL`: reliability windows exist but cannot yet be physically aligned.
- `NUMERICAL_AGREEMENT_BRIDGE_CONTROL`: passes.

## Source-authority classification

**`BLOCKED_INDEPENDENT_PHYSICAL_SCALE_NORMALIZATION`**

What is established:

- common observable definition: yes;
- CDT relative diffusion/lattice scale calibration: yes;
- CDT conditional absolute lattice spacing: yes;
- QEG mode/RG/heat-kernel scale semantics: yes;
- representation-level curve fit: yes in 3D;
- independent 4D physical-resolution crosswalk: **no**.

## Claim ceiling

No pointwise 4D physical-scale comparator is authorized by ITER073. No numerical spectral-dimension agreement can receive bridge credit under this gate.