# ITER048 — Lorentzian Eq.(11) routing/reference authority

Date: 2026-09-14

## Terminal classification

**SCOPED BLOCKED — `LORENTZIAN_EQ11_ROUTING_REFERENCE_AUTHORITY_BLOCKED_SOURCE_INDEX_INCONSISTENCY`**.

This is not a numerical/scientific failure of Lorentzian EPRL and not an infrastructure failure. The exact arXiv source itself contains a routing inconsistency in Eq.(11): the last 6j factor uses `i_8` while `i_9` is absent from the displayed amplitude, even though the immediately following source comment explicitly maps `rCDl=i9` and `rCDr=i10`. Frozen ITER048 required a one-to-one unambiguous exact-TeX routing of all `i1...i15`; therefore ITER048 cannot PASS and no five-vertex numerical contraction is authorized from Eq.(11) alone.

## Frozen provenance

- prereg commit: `faad5c1dcf5e00a9d2eac425e0db0be505295c5b`
- original production head: `508f09658fe79b75bec5a7efe789dc48cb7b81db`
- original run: `34811518934`
- original jobs: backend-api `103873656998`; algebra-null `103873657125`; tex-eq11 `103873657146`; cited-reference `103873657258`; aggregate `103873711788`
- original artifacts:
  - backend-api `10335255210`, digest `sha256:06ca3f28a0f22a464c98b58e9c0a5e1b6c28f8ed8e16aee8165527d5e2207561`
  - algebra-null `10335062319`, digest `sha256:507d95792e852ef39f2df7ff283a0fd8ae9291e17cf6cb72682c8e2f8d98aced`
  - tex-eq11 `10335052286`, digest `sha256:ad3084d7b002632dd94fbf59d49f4fc8a0132f7e865ca81bdc74741a35e80560`
  - cited-reference `10335106791`, digest `sha256:4373c80c3bd681d091218ff42c02b39c9403f0dc869ff602f72d86d5689bbfd2`
- source-parser recovery head/run: `325579f260f340d0d72cc10d114f04f692ffa6da` / `34811661866`
- cited-reference recovery job/artifact: `103874069254` / `10335185440`, digest `sha256:fe60d3681c02bfcc9516df53d9faaf9e0aafc52aecb3c1300686e809a9568387`
- raw-TeX recovery head/run/job: `6960f12c2af6b51e759e193aa336c16761b48000` / `34811727020` / `103874254568`
- raw-TeX artifact: `10334723630`, digest `sha256:191262f0c2a6d5c5b3ac6f1036caacd6808735c4bc38ecc73c45da49b2c53cb9`
- exact `main.tex` SHA256 from that artifact: `bff93f3a7857658264a04eb23521bb935a68eccb7760b284589ff5ec4073f063`

The first parser/recovery failures were technical extraction under-implementations; frozen science predicates were unchanged. The raw-TeX census is the authoritative source evidence for the blocker.

## Exact source finding

Exact arXiv `main.tex`, Eq. `\label{eq:vertex}`, gives five vertex amplitudes and five 6j factors. The last two 6j lines are source-literally:

- `\{6j\}(j_b,j_7,i_5,j_8,j_1,i_6)\{6j\}(j_b,j_{10},i_7,j_4,j_7,i_{8})`
- `\{6j\}(j_b,j_6,i_8,j_9,j_{10},i_{10}) (-1)^{\chi}`

Thus `i_8` occurs in both the fourth and fifth 6j factors while `i_9` is absent from the displayed Eq.(11) routing.

Immediately below Eq.(11), the authors preserve their code correspondence comment:

- `rbl=i7   rbr=i8`
- `rCDl=i9   rCDr=i10`
- `rIul=i11   rIur=i12`
- `rIu=i13`
- `rIbl=i14   rIbr=i15`

The amplitude nevertheless includes the factor `prod_{e=1}^{15}(2 i_e+1)`. This is exactly the ambiguity the frozen gate was designed to detect; it must not be resolved by fitting a numerical amplitude.

## Other frozen lanes

### Backend API — PASS

Exact backend `qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f` retains the required 10-spin / 5-intertwiner local vertex interface. `BACKEND_API_PASS=true`.

### Algebra/null precheck — PASS, source-conditional

Exact SU(2) basis values in the frozen `jb=1/2` sectors were finite:

- `(0,0) = -1/2`
- `(0,1) = 1/2`
- `(1,0) = 1/2`
- `(1,1) = 1/6`

The malformed duplicated-index control was structurally distinguished. This does not override the source-routing blocker.

### Cited reference — source authority found

The literal repository cited by the frozen source is `https://github.com/PietropaoloFrisoni/Monte_Carlo_spinfoams`, pinned by the recovery lane at commit `84b375f2a2e0d29b44dd8820953553624bb007a3`. Inventory found 20 code/notebook files and 97 relevant vertex-renormalization/sl2cfoam hits, including `notebooks/julia/5-1_move_EPRL_analysis.ipynb`. This makes an independent author-code routing reconciliation scientifically admissible, but it cannot retroactively change ITER048.

## Consequence

ITER048 remains BLOCKED permanently under its preregistration. The exact next admissible gate is a separately preregistered **author-code routing reconciliation** using only the already source-derived `Monte_Carlo_spinfoams` repository at the pinned commit, the exact arXiv TeX and the exact sl2cfoam-next backend. It must determine whether the implementation supplies an unambiguous `i9`/`i8` routing and reject alternative repairs without using amplitude agreement.

Until such a gate passes, the bounded five-vertex contraction is not authorized.

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory = `0 / UNFORMED`. Claim locks remain unchanged.
