# RC-006 q-group recoupling-matrix orthogonality diagnostic.
#
# Follows the actual use of sixjr() in the pinned Fusion-basis-coarse-graining
# basis transformations.  For fixed external integer-sector spins a,b,c,d,
# admissible intermediate e and f define M[e,f]=sixjr(a,b,e,d,c,f) in the
# code's r=2j+1 encoding.  Because sixjr() already contains sqrt(q(e)q(f)),
# the source implementation uses M directly as a basis-change coefficient.
# The appropriate convention-level self-consistency check is therefore
# M*M' ~= I and M'*M ~= I on square admissible recoupling blocks.
#
# This diagnostic is frozen after the earlier raw tetrahedral-symmetry
# qualification failed at k=12.  It does not erase that result.

using TOML
using LinearAlgebra

length(ARGS)==3 || error("usage: script level_k qgroup_def.jl out.toml")
level_k=parse(Int,ARGS[1]); qfile=ARGS[2]; outfile=ARGS[3]
const p=2*(level_k+2)
const k=level_k
const z=(k+1)^2
const num_q_values=max(8*p,256)
const TOLERANCE=1e-13
const A=exp(2im*pi/p)
include(normpath(joinpath(@__DIR__,"..",qfile)))

jmax=level_k÷2
phys=collect(0:jmax)
lab(j)=2*j+1
N(a,b,c)=coupling_rules(lab(a),lab(b),lab(c))

block_count=0
square_nontrivial=0
bad_count=0
max_left=0.0
max_right=0.0
worst=Dict{String,Any}()

for a in phys,b in phys,c in phys,d in phys
    es=[e for e in phys if N(a,b,e)==1 && N(c,d,e)==1]
    fs=[f for f in phys if N(a,c,f)==1 && N(b,d,f)==1]
    isempty(es) && continue
    isempty(fs) && continue
    global block_count += 1
    length(es)==length(fs) || continue
    length(es)>1 || continue
    global square_nontrivial += 1
    M=zeros(Float64,length(es),length(fs))
    for (ie,e) in enumerate(es),(jf,f) in enumerate(fs)
        M[ie,jf]=sixjr(lab(a),lab(b),lab(e),lab(d),lab(c),lab(f))
    end
    I0=Matrix{Float64}(I,size(M,1),size(M,1))
    le=opnorm(M*M'-I0,Inf)
    re=opnorm(M'*M-I0,Inf)
    global max_left=max(max_left,le)
    global max_right=max(max_right,re)
    if max(le,re)>1e-9
        global bad_count += 1
        if isempty(worst) || max(le,re)>worst["error"]
            global worst=Dict("a"=>a,"b"=>b,"c"=>c,"d"=>d,"e_channels"=>es,"f_channels"=>fs,
                              "left_error"=>le,"right_error"=>re,"error"=>max(le,re))
        end
    end
end

passed=(square_nontrivial>0 && bad_count==0)
out=Dict(
 "test"=>"RC006_QGROUP_RECOUPLING_ORTHOGONALITY",
 "level_k"=>level_k,"p"=>p,"jmax"=>jmax,
 "all_nonempty_recoupling_blocks"=>block_count,
 "square_nontrivial_blocks_tested"=>square_nontrivial,
 "bad_block_count"=>bad_count,
 "max_left_orthogonality_inf_norm"=>max_left,
 "max_right_orthogonality_inf_norm"=>max_right,
 "worst_block"=>worst,
 "recoupling_orthogonality_pass"=>passed,
 "frozen_gate"=>"all nontrivial square admissible recoupling blocks satisfy max(||MM^T-I||_inf,||M^TM-I||_inf)<=1e-9",
 "interpretation_lock"=>"Convention diagnostic for the independent q-deformed numerical kernel only. Passing may show the earlier bare tetrahedral-symmetry test was inappropriate to this normalized sixjr convention; it does not reproduce the RC006 EPRL tensor or RG flow."
)
open(outfile,"w") do io; TOML.print(io,out); end
TOML.print(stdout,out); println()
