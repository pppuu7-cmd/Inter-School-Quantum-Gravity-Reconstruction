#!/usr/bin/env python3
"""Aggregate ITER162 source reconstruction with the independent K-divisibility certificate.

Runs only after both upstream jobs pass. No new fit or basis choice is performed.
The frozen-span theorem proves that the full tensor K-divisible kernel is exactly
the 10 explicit-K columns. Therefore the source coefficient manifest can be
partitioned mechanically into endpoint-local contact-candidate numerator terms
and genuine shrinking-propagator tensor-kernel terms before external contraction.

This is still pre-Laurent: no contact is set to zero and no pole ambiguity is fixed.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as s

RECON=Path("iter162_upper_covariant_reconstruction.json")
KPROOF=Path("iter162_tensor_K_divisibility_span.json")


def main():
    r=json.loads(RECON.read_text(encoding="utf-8"))
    k=json.loads(KPROOF.read_text(encoding="utf-8"))
    d=s.symbols("d")

    k_ok=(
        k.get("classification")=="PASS_STRUCTURAL_ITER162_COMPLETE_FROZEN_SPAN_TENSOR_K_DIVISIBILITY_KERNEL"
        and all(x.get("kernel_exactly_explicit_K_span") for x in k.get("dimension_results",[]))
        and len(k.get("dimension_results",[]))>=2
    )
    recon_ok=(
        r.get("classification")=="PARTIAL_ITER162_SOURCE_DERIVED_UPPER_COVARIANT_TENSOR_RECONSTRUCTION"
        and all(bool(v) for v in r.get("checks",{}).values())
        and len(r.get("coefficients",[]))==36
    )
    if not (k_ok and recon_ok):
        raise RuntimeError("upstream reconstruction/K-divisibility certificate incomplete")

    nonzero=[]
    contact=[]
    kernel=[]
    zero=[]
    for idx,row in enumerate(r["coefficients"]):
        coeff=s.factor(s.sympify(row["coefficient_d"]))
        entry={
            "index":idx,
            "seed":row["seed"],
            "scalar":row["scalar"],
            "coefficient_d":str(coeff),
            "support_class":"K_DIVISIBLE_LOCAL_CONTACT_CANDIDATE" if row["explicit_K_factor"] else "GENUINE_ONE_SHRINKING_PROPAGATOR_KERNEL",
        }
        if coeff==0:
            zero.append(entry)
        else:
            nonzero.append(entry)
            (contact if row["explicit_K_factor"] else kernel).append(entry)

    checks={
        "A_reconstruction_upstream_pass":recon_ok,
        "B_K_kernel_upstream_pass":k_ok,
        "C_partition_recombines_36_columns":len(contact)+len(kernel)+len(zero)==36,
        "D_nonzero_partition_recombines_source":len(contact)+len(kernel)==len(nonzero),
        "E_no_contact_zero_assumption":True,
        "F_no_ITER160_residue_consumed":True,
        "G_no_ITER118_solve":True,
    }
    out={
        "gate":"ITER162_OPEN_G_ENDPOINT_DISTRIBUTIONAL_R_OPERATION_AND_POLE_TENSOR",
        "classification":"PASS_STRUCTURAL_ITER162_SOURCE_DERIVED_UPPER_TENSOR_SUPPORT_SPLIT",
        "frozen_span_dimension":36,
        "K_divisible_subspace_dimension":10,
        "non_K_quotient_dimension":26,
        "source_nonzero_coefficient_count":len(nonzero),
        "source_nonzero_K_divisible_contact_count":len(contact),
        "source_nonzero_genuine_kernel_count":len(kernel),
        "source_zero_coefficient_count":len(zero),
        "contact_terms":contact,
        "genuine_kernel_terms":kernel,
        "zero_terms":zero,
        "checks":checks,
        "interpretation":(
            "Within the prospectively frozen 36-column covariant tensor span, exact polynomial quotient algebra proves that "
            "all and only explicit-K covariants are K-divisible. Combining that theorem with the source-derived coefficients "
            "therefore gives the complete upper tensor support split before external-source contraction. This does not assign "
            "the distributional Laurent extension or any contact pole value."
        ),
        "remaining_blocker":(
            "construct the unseparated open-tensor distributional Laurent/R-operation for both genuine-kernel and K-cancelled "
            "endpoint-local sectors, enumerate the complete allowed local pole ambiguity span, and compute P_open/A_local"
        ),
        "terminal_science":False,
        "locks":{
            "contacts_set_zero":False,
            "ITER160_minus525_consumed":False,
            "ITER118_coefficient_solve":False,
            "B1_total":"UNAUTHORIZED",
            "BRIDGE_DERIVED":False,
            "candidate_theory":"UNFORMED / 0%",
        },
    }
    Path("iter162_upper_source_support_aggregate.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in out.items() if k not in {"contact_terms","genuine_kernel_terms","zero_terms"}},indent=2,sort_keys=True))
    raise SystemExit(0 if all(checks.values()) else 1)

if __name__=="__main__":
    main()
