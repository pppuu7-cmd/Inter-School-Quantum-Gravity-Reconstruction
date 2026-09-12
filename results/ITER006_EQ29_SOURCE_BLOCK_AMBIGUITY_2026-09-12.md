# ITER006 RC006 Eq. (29) source-block ambiguity — 2026-09-12

Preregistered run `34717600962` attempted exact extraction of the hash-pinned Eq. (29) TeX/TikZ block from arXiv:1609.02429v2 source bundle SHA256 `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`.

The preregistered identification rule required the source sentence containing `initial 3-valent tensor` to be unique before selecting the immediately following align environment. Both the main extractor and an independent verifier found **three** literal occurrences of that anchor. The main extractor therefore returned `EQ29_SOURCE_BLOCK_AMBIGUOUS`; the independent verifier returned `SOURCE_IDENTITY_OR_ANCHOR_FAIL` because `anchor_count = 3`.

This is a correct fail-closed outcome of the preregistered rule, not a negative physics result and not an infrastructure failure. No source block was selected, no graph/incidence object was promoted, and Eq. (29) amplitude remains unauthorized.

The next admissible action is a +0 source-parser diagnostic that distinguishes active TeX from commented/legacy duplicate text using TeX `%` comment semantics and reports all literal and active occurrences with nearest section/subsection headers. Run `34717736113` was launched for exactly that purpose. If and only if the active-document anchor becomes unique under a prospectively recorded source-semantic rule, a new source-block extractor may be preregistered. Manual selection of one of the three literal occurrences is forbidden.

Claim locks remain unchanged: no Eq. (29) amplitude, no bridge credit, no `NEW_PHYSICS_FOUND`, candidate theory `UNFORMED`.
