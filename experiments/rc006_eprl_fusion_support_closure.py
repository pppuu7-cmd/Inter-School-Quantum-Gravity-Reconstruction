#!/usr/bin/env python3
"""RC-006 source-grounded support-level EPRL/FK coarse-recoupling audit.

This is deliberately *not* a reproduction of the full q-deformed tensor-network
renormalization amplitudes of Dittrich et al. (arXiv:1609.02429).  It tests a
necessary closure condition that is exact at the level of SU(2)_k fusion
support.

The source EPRL map is
    Y_gamma(l) = ((1+gamma)l/2, (1-gamma)l/2)
for the integer-spin cases explicitly listed in the paper.  Given two source
labels l1,l2, we enumerate:
  * coarse diagonal-SU(2)_k labels l in l1 x l2;
  * plus-sector labels J+ in j1+ x j2+;
  * minus-sector labels J- in j1- x j2-;
  * retain triples where l can couple J+ and J- under SU(2)_k fusion.

If the simplicity image were support-closed under this recoupling, each coarse
triple would satisfy (J+,J-) = Y_gamma(l).  Extra triples form the raw transport
/ recoupling envelope.  We then ask whether the source-native Y_gamma(l) target
is contained in that envelope, which is the support-level analogue of
"transport envelope + local selector".

No closure observable, fitted threshold, or tensor singular value enters this
calculation.
"""
from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


def fusion(k: int, a: int, b: int) -> tuple[int, ...]:
    """Integer-spin SU(2)_k fusion support for even k used in RC-006."""
    jmax = k // 2
    if not (0 <= a <= jmax and 0 <= b <= jmax):
        return ()
    upper = min(a + b, k - a - b)
    lower = abs(a - b)
    if upper < lower:
        return ()
    return tuple(range(lower, upper + 1))


def eprl_map(l: int, gamma: Fraction, k: int) -> tuple[int, int] | None:
    jp = Fraction(1, 2) * (1 + gamma) * l
    jm = Fraction(1, 2) * (1 - gamma) * l
    if jp.denominator != 1 or jm.denominator != 1:
        return None
    jp_i, jm_i = int(jp), int(jm)
    jmax = k // 2
    if jp_i < 0 or jm_i < 0 or jp_i > jmax or jm_i > jmax:
        return None
    return jp_i, jm_i


def quantum_dimension(k: int, j: int) -> float:
    # Positive for admissible j <= k/2.  Reported only as descriptive metadata;
    # it is NOT used as an amplitude weight in the support decision.
    num = math.sin((2 * j + 1) * math.pi / (k + 2))
    den = math.sin(math.pi / (k + 2))
    return float(num / den)


def analyze_case(k: int, gamma: Fraction) -> dict:
    jmax = k // 2
    source_l = [l for l in range(jmax + 1) if eprl_map(l, gamma, k) is not None]
    source_map = {l: eprl_map(l, gamma, k) for l in source_l}

    events: set[tuple[int, int, int, int, int]] = set()
    by_l: dict[int, set[tuple[int, int]]] = defaultdict(set)

    for l1 in source_l:
        jp1, jm1 = source_map[l1]
        for l2 in source_l:
            jp2, jm2 = source_map[l2]
            coarse_ls = fusion(k, l1, l2)
            plus = fusion(k, jp1, jp2)
            minus = fusion(k, jm1, jm2)
            for l in coarse_ls:
                for jp in plus:
                    for jm in minus:
                        # The EPRL construction couples the two sector labels to
                        # a diagonal-SU(2) label l.  We use SU(2)_k support as a
                        # necessary recoupling condition.
                        if l not in fusion(k, jp, jm):
                            continue
                        events.add((l1, l2, l, jp, jm))
                        by_l[l].add((jp, jm))

    simple_events = []
    leaked_events = []
    undefined_l_events = []
    for ev in sorted(events):
        _, _, l, jp, jm = ev
        target = eprl_map(l, gamma, k)
        if target is None:
            undefined_l_events.append(ev)
            leaked_events.append(ev)
        elif (jp, jm) == target:
            simple_events.append(ev)
        else:
            leaked_events.append(ev)

    per_l = {}
    capture_flags = []
    for l in sorted(by_l):
        env = sorted(by_l[l])
        target = eprl_map(l, gamma, k)
        captured = target in by_l[l] if target is not None else False
        if target is not None:
            capture_flags.append(captured)
        per_l[str(l)] = {
            "envelope_size": len(env),
            "envelope": [list(x) for x in env],
            "source_target": list(target) if target is not None else None,
            "source_target_captured": bool(captured),
            "extra_channel_count": len(env) - (1 if captured else 0),
        }

    total = len(events)
    leak_fraction = len(leaked_events) / total if total else float("nan")
    all_targets_captured = bool(capture_flags) and all(capture_flags)
    envelope_strictly_larger = any(v["extra_channel_count"] > 0 for v in per_l.values())

    # Algebraic BC control: source Eq. (20)/(21) contains delta_{J+,J-}.
    # We do not pretend to reproduce the BC tensor amplitudes; this only checks
    # that applying the exact source support delta gives zero off-diagonal
    # support by construction.
    bc_raw_pairs = {(jp, jm) for jp in range(jmax + 1) for jm in range(jmax + 1)}
    bc_filtered = {(jp, jm) for jp, jm in bc_raw_pairs if jp == jm}
    bc_control = {
        "raw_pair_count": len(bc_raw_pairs),
        "post_delta_pair_count": len(bc_filtered),
        "post_delta_offdiagonal_count": sum(jp != jm for jp, jm in bc_filtered),
        "note": "sanity control from the exact BC delta_{J+,J-}; not an independent TNR computation",
    }

    return {
        "k": k,
        "gamma": f"{gamma.numerator}/{gamma.denominator}",
        "jmax": jmax,
        "source_allowed_l": source_l,
        "source_map": {str(l): list(source_map[l]) for l in source_l},
        "source_quantum_dimensions": {str(l): quantum_dimension(k, l) for l in source_l},
        "n_recoupling_events": total,
        "n_source_simple_events": len(simple_events),
        "n_leaked_events": len(leaked_events),
        "n_events_with_coarse_l_outside_source_map": len(undefined_l_events),
        "raw_support_leak_fraction": float(leak_fraction),
        "raw_envelope_strictly_larger_than_source_image": bool(envelope_strictly_larger),
        "all_defined_source_targets_captured_by_envelope": bool(all_targets_captured),
        "local_selector_support_recovery": bool(all_targets_captured),
        "per_coarse_l": per_l,
        "bc_delta_sanity_control": bc_control,
        "claim_lock": (
            "Exact SU(2)_k fusion-support necessary-condition audit using the source EPRL map. "
            "It is not the full q-deformed tensor amplitude, does not compute singular values, and does not reproduce the published TNR flow."
        ),
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--k", type=int, required=True)
    p.add_argument("--gamma-num", type=int, required=True)
    p.add_argument("--gamma-den", type=int, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    gamma = Fraction(a.gamma_num, a.gamma_den)
    out = analyze_case(a.k, gamma)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: out[k] for k in (
        "k", "gamma", "source_allowed_l", "n_recoupling_events", "n_leaked_events",
        "raw_support_leak_fraction", "raw_envelope_strictly_larger_than_source_image",
        "all_defined_source_targets_captured_by_envelope", "local_selector_support_recovery")}, indent=2))


if __name__ == "__main__":
    main()
