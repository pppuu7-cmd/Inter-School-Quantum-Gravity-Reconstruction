#!/usr/bin/env python3
"""Minimal source-faithful symbolic namespace for q-EPRL Proposition 3.4.

Schema-only object. No numerical amplitude, no historical holdout/sign input.
"""
from __future__ import annotations
import copy, json

SCHEMA_VERSION = "RC006-QEPRL-BRAID-v1"


def canonical_exemplar():
    return {
        "schema_version": SCHEMA_VERSION,
        "source": {"arxiv": "1112.2511v1", "object": "Proposition 3.4"},
        "input_representations": [
            {"slot":"alpha1","family":"alpha1","label":"K1"},
            {"slot":"alpha2","family":"alpha2","label":"K2"},
            {"slot":"alpha3","family":"alpha3","label":"K3"},
            {"slot":"alpha4","family":"alpha4","label":"K4"}
        ],
        "braid_operator": {
            "name":"c",
            "ordered_inputs":["alpha2","alpha1"],
            "source_definition":"tau_compose_pi_tensor_pi_of_R",
            "orientation_convention":"SOURCE_R_ACTION_UNRESOLVED_INVERSE_AUXILIARY_GATE"
        },
        "summations":[{"index":"K","domain":"source_representation_domain"}],
        "kernel": {
            "name":"Lambda",
            "upper_indices":["K2","J"],
            "lower_indices":["K1","K"],
            "arguments":["alpha2"]
        },
        "output_representations": [
            {"slot":"alpha2","family":"alpha2","label":"K2"},
            {"slot":"alpha1","family":"alpha1","label":"K"},
            {"slot":"alpha3","family":"alpha3","label":"K3"},
            {"slot":"alpha4","family":"alpha4","label":"K4"}
        ],
        "domain_metadata": {"alpha1(K)_necessarily_EPRL": False},
        "legacy_projection": {"pair_sign_authoritative": False, "status":"non_authoritative_projection"}
    }


def validate(o):
    errors=[]
    if o.get("schema_version") != SCHEMA_VERSION: errors.append("schema_version")
    ins=o.get("input_representations",[]); outs=o.get("output_representations",[])
    if [(x.get("slot"),x.get("label")) for x in ins] != [("alpha1","K1"),("alpha2","K2"),("alpha3","K3"),("alpha4","K4")]: errors.append("input_representations")
    b=o.get("braid_operator",{})
    if b.get("ordered_inputs") != ["alpha2","alpha1"] or b.get("source_definition") != "tau_compose_pi_tensor_pi_of_R": errors.append("braid_operator")
    if o.get("summations") != [{"index":"K","domain":"source_representation_domain"}]: errors.append("summation_K")
    k=o.get("kernel",{})
    if not (k.get("name")=="Lambda" and k.get("upper_indices")==["K2","J"] and k.get("lower_indices")==["K1","K"] and k.get("arguments")==["alpha2"]): errors.append("Lambda_kernel")
    if [(x.get("slot"),x.get("label")) for x in outs] != [("alpha2","K2"),("alpha1","K"),("alpha3","K3"),("alpha4","K4")]: errors.append("output_representations")
    if o.get("domain_metadata",{}).get("alpha1(K)_necessarily_EPRL") is not False: errors.append("domain_escape_flag")
    lp=o.get("legacy_projection",{})
    if lp.get("pair_sign_authoritative") is not False or lp.get("status")!="non_authoritative_projection": errors.append("legacy_projection_lock")
    return errors


def canonicalize(o):
    # Deliberately explicit canonical JSON form; list ordering is physical/source ordering.
    return json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=False)


def destructive_controls():
    base=canonical_exemplar(); out=[]
    cases=[]
    x=copy.deepcopy(base); x.pop("summations"); cases.append(("REMOVE_SUMMATION_K",x))
    x=copy.deepcopy(base); x.pop("kernel"); cases.append(("REMOVE_LAMBDA_KERNEL",x))
    x=copy.deepcopy(base); x["output_representations"][1]["label"]="K1"; cases.append(("REMOVE_ALPHA1_K_OUTPUT_DEPENDENCE",x))
    x=copy.deepcopy(base); x["domain_metadata"]["alpha1(K)_necessarily_EPRL"]=True; cases.append(("FORCE_EPRL_DOMAIN",x))
    x=copy.deepcopy(base); x["braid_operator"]={"name":"pair_sign","ordered_inputs":["alpha2","alpha1"],"source_definition":"pair_sign_only"}; cases.append(("PAIR_SIGN_ONLY",x))
    for name,obj in cases: out.append({"name":name,"errors":validate(obj),"fails_closed":bool(validate(obj))})
    return out

if __name__ == "__main__":
    o=canonical_exemplar()
    print(json.dumps({"object":o,"validation_errors":validate(o),"canonical":canonicalize(o),"null_controls":destructive_controls()},indent=2,sort_keys=True,ensure_ascii=False))
