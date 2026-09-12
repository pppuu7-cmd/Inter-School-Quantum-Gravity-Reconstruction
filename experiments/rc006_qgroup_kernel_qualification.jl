# RC-006 source-kernel qualification for SU(2)_k EPRL/FK work.
#
# This is NOT an EPRL amplitude reproduction.  It checks whether the q-number,
# fusion-rule, and q-6j numerical conventions in the independently published
# Steinhaus fusion-basis code are compatible with the integer-representation
# SU(2)_k conventions needed by arXiv:1609.02429 before reusing that kernel in
# a source-equation implementation.
#
# Usage: julia rc006_qgroup_kernel_qualification.jl <level_k> <gamma_num> <gamma_den> <qgroup_def.jl> <out.toml>

using TOML
using Printf

length(ARGS)==5 || error("usage: script level_k gamma_num gamma_den qgroup_def.jl out.toml")
level_k=parse(Int,ARGS[1]); gn=parse(Int,ARGS[2]); gd=parse(Int,ARGS[3]); qfile=ARGS[4]; outfile=ARGS[5]
isodd(level_k) && error("RC006 qualification currently expects even level k")

const p = 2*(level_k+2)
const k = level_k
const z = (k+1)^2
const num_q_values = max(8*p,256)
const TOLERANCE = 1e-13
const A = exp(2im*pi/p)
include(normpath(joinpath(@__DIR__,"..",qfile)))

jmax=level_k÷2
phys=collect(0:jmax)
lab(j)=2*j+1
qdim(j)=q(lab(j))
N(a,b,c)=coupling_rules(lab(a),lab(b),lab(c))

qd=[qdim(j) for j in phys]
qdim_positive=all(x->x>0,qd)

assoc_bad=[]
for a in phys,b in phys,c in phys,d in phys
    lhs=sum(N(a,b,e)*N(e,c,d) for e in phys)
    rhs=sum(N(b,c,f)*N(a,f,d) for f in phys)
    lhs==rhs || push!(assoc_bad,(a,b,c,d,lhs,rhs))
end
assoc_ok=isempty(assoc_bad)

max_dim_rel=0.0
dim_bad=[]
for a in phys,b in phys
    lhs=qdim(a)*qdim(b)
    rhs=sum(N(a,b,c)*qdim(c) for c in phys)
    rel=abs(lhs-rhs)/max(abs(lhs),1e-15)
    global max_dim_rel=max(max_dim_rel,rel)
    rel<=1e-10 || push!(dim_bad,(a,b,lhs,rhs,rel))
end
dim_ok=isempty(dim_bad)

maps=[]
for l in phys
    np=(gd+gn)*l; nm=(gd-gn)*l; den=2*gd
    if np%den==0 && nm%den==0
        jp=np÷den; jm=nm÷den
        if 0<=jp<=jmax && 0<=jm<=jmax && N(jp,jm,l)==1
            push!(maps,(l,jp,jm))
        end
    end
end
expected = if level_k==6 && gn==1 && gd==3
    [(0,0,0),(3,2,1)]
elseif level_k==10 && gn==3 && gd==5
    [(0,0,0),(5,4,1)]
elseif level_k==12 && gn==1 && gd==3
    [(0,0,0),(3,2,1),(6,4,2)]
else
    Tuple{Int,Int,Int}[]
end
map_ok = maps==expected

max_sym_rel=0.0; sym_count=0; sym_bad=0
for a in phys,b in phys,e in phys,d in phys,c in phys,f in phys
    if N(a,b,e)==1 && N(c,d,e)==1 && N(a,c,f)==1 && N(b,d,f)==1
        x=sixjr(lab(a),lab(b),lab(e),lab(d),lab(c),lab(f))
        y=sixjr(lab(b),lab(a),lab(e),lab(c),lab(d),lab(f))
        z6=sixjr(lab(c),lab(d),lab(e),lab(b),lab(a),lab(f))
        scale=max(abs(x),abs(y),abs(z6),1e-14)
        rel=max(abs(x-y),abs(x-z6))/scale
        global max_sym_rel=max(max_sym_rel,rel)
        global sym_count+=1
        rel<=1e-9 || (global sym_bad+=1)
    end
end
sixj_sym_ok=(sym_count>0 && sym_bad==0)

natural = qdim_positive && assoc_ok && dim_ok && map_ok && sixj_sym_ok
out=Dict(
 "test"=>"RC006_QGROUP_KERNEL_QUALIFICATION",
 "level_k"=>level_k,"gamma"=>"$gn/$gd","p"=>p,"jmax"=>jmax,
 "representation_encoding"=>"r=2j+1",
 "quantum_dimensions"=>qd,"qdim_positive"=>qdim_positive,
 "fusion_associativity_ok"=>assoc_ok,"fusion_associativity_bad_count"=>length(assoc_bad),
 "quantum_dimension_fusion_ok"=>dim_ok,"max_quantum_dimension_fusion_relative_error"=>max_dim_rel,
 "eprl_admissible_maps"=>[collect(x) for x in maps],
 "expected_source_maps"=>[collect(x) for x in expected],"eprl_source_map_exact_match"=>map_ok,
 "sixj_symmetry_cases"=>sym_count,"sixj_symmetry_bad_count"=>sym_bad,
 "max_sixj_symmetry_relative_error"=>max_sym_rel,"sixj_symmetry_ok"=>sixj_sym_ok,
 "kernel_qualified_for_next_rc006_implementation_step"=>natural,
 "frozen_gate"=>"positive qdims; exact fusion associativity; qdim fusion identity <=1e-10; exact source EPRL admissibility map; q6j tested tetrahedral symmetries <=1e-9",
 "claim_lock"=>"Kernel qualification only. Passing does not reproduce the 2016 EPRL tensor, RG flow, or any quantum-gravity result; it only permits reuse of the numerical SU(2)_k kernel in a later source-faithful implementation."
)
open(outfile,"w") do io; TOML.print(io,out); end
println(TOML.print(out))
