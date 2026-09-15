#!/usr/bin/env python3
"""ITER144 technical parser retry.

Physical predicates and pinned source are unchanged from the preregistered ITER144 gate.
This file fixes only nested Pair[...] argument parsing after attempt 1 correctly blocked.
"""
from __future__ import annotations
from fractions import Fraction as F
import re
import iter144_cubic_graviton_s3_source_structure_authority as base

MM_RE = re.compile(r"^Pair\[LorentzIndex\[([mn][123]),D\],LorentzIndex\[([mn][123]),D\]\]$")
IM_RE = re.compile(r"^Pair\[LorentzIndex\[([mn][123]),D\],Momentum\[(p[123]),D\]\]$")
MI_RE = re.compile(r"^Pair\[Momentum\[(p[123]),D\],LorentzIndex\[([mn][123]),D\]\]$")
PP_RE = re.compile(r"^Pair\[Momentum\[(p[123]),D\],Momentum\[(p[123]),D\]\]$")


def parse_source_fixed(text: str):
    expr = ''.join(text.split())
    terms = []
    unknown = []
    common_phase_ok = True
    seen_index = set()
    seen_mom = set()
    for raw in base.split_top_level_terms(expr):
        sign = 1
        if raw[0] == '+':
            raw = raw[1:]
        elif raw[0] == '-':
            sign = -1
            raw = raw[1:]
        coeff = F(sign, 1)
        factors = []
        has_i = False
        has_k = False
        for fac in base.split_product(raw):
            if fac == 'I':
                has_i = True
                continue
            if fac == '\\[Kappa]':
                has_k = True
                continue
            if re.fullmatch(r"\d+/\d+", fac):
                a, b = fac.split('/')
                coeff *= F(int(a), int(b))
                continue
            if re.fullmatch(r"\d+", fac):
                coeff *= F(int(fac), 1)
                continue
            m = MM_RE.match(fac)
            if m:
                ia, ib = m.groups()
                factors.append(('metric', ia, ib))
                seen_index |= {ia, ib}
                continue
            m = IM_RE.match(fac)
            if m:
                ia, pb = m.groups()
                factors.append(('ip', ia, pb))
                seen_index.add(ia)
                seen_mom.add(pb)
                continue
            m = MI_RE.match(fac)
            if m:
                pa, ib = m.groups()
                factors.append(('ip', ib, pa))
                seen_index.add(ib)
                seen_mom.add(pa)
                continue
            m = PP_RE.match(fac)
            if m:
                pa, pb = m.groups()
                factors.append(('pp', pa, pb))
                seen_mom |= {pa, pb}
                continue
            unknown.append(fac)
        common_phase_ok &= has_i and has_k
        terms.append((coeff, factors))
    return {
        'terms': terms,
        'unknown': sorted(set(unknown)),
        'common_phase_ok': common_phase_ok,
        'seen_index': sorted(seen_index),
        'seen_mom': sorted(seen_mom),
    }


base.parse_source = parse_source_fixed

if __name__ == '__main__':
    base.main()
