# RC-006 Appendix-B Eq. (B13) source-mapping audit.
#
# Independently implement the normalized graphical recoupling coefficient
# defined in arXiv:1609.02429 Eq. (B13), using integer spin variables j and
# q-number/q-factorial formulas. Compare exhaustively to the pinned
# Fusion-basis-coarse-graining sixjr() implementation (r=2j+1 labels).
#
# This is a convention bridge only. Passing authorizes translating source
# diagrams that explicitly reduce via Eq. (B13) into the validated recoupling
# object. It is not an EPRL tensor or RG-flow reproduction.

using TOML

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

# Independent source-side q-number implementation for integer spin arguments.
qsrc(n::Int)=sin(pi*n/(level_k+2))/sin(pi/(level_k+2))
function qfsrc(n::Int)
    n<0 && error("negative q factorial")
    n==0 && return 1.0
    return prod(qsrc(m) for m in 1:n)
end
function delta_src(a::Int,b::Int,c::Int)
    N(a,b,c)==1 || return 0.0
    return sqrt(qfsrc(a+b-c)*qfsrc(a-b+c)*qfsrc(-a+b+c)/qfsrc(a+b+c+1))
end

# Standard q-Racah bracket in spin-j notation, matching the bracket [6j] in B13.
function bracket6j(a::Int,b::Int,e::Int,d::Int,c::Int,f::Int)
    (N(a,b,e)==1 && N(a,c,f)==1 && N(b,d,f)==1 && N(c,d,e)==1) || return 0.0
    A1=a+b+e; A2=a+c+f; A3=b+d+f; A4=c+d+e
    B1=a+b+c+d; B2=a+d+e+f; B3=b+c+e+f
    lo=max(A1,A2,A3,A4); hi=min(B1,B2,B3)
    s=0.0
    for n in lo:hi
        s += (-1)^n*qfsrc(n+1)/(qfsrc(n-A1)*qfsrc(n-A2)*qfsrc(n-A3)*qfsrc(n-A4)*qfsrc(B1-n)*qfsrc(B2-n)*qfsrc(B3-n))
    end
    return delta_src(a,b,e)*delta_src(c,d,e)*delta_src(a,c,f)*delta_src(b,d,f)*s
end

# Eq. B13 graphical coefficient = (-1)^(j1+j2+j3+j4)*sqrt(d_e d_f)*[6j].
function graph_b13(a,b,e,d,c,f)
    return (-1)^(a+b+c+d)*sqrt(qsrc(2*e+1)*qsrc(2*f+1))*bracket6j(a,b,e,d,c,f)
end

count=0; bad=0; max_abs=0.0; max_rel=0.0; worst=Dict{String,Any}()
for a in phys,b in phys,e in phys,d in phys,c in phys,f in phys
    if N(a,b,e)==1 && N(a,c,f)==1 && N(b,d,f)==1 && N(c,d,e)==1
        src=graph_b13(a,b,e,d,c,f)
        code=sixjr(lab(a),lab(b),lab(e),lab(d),lab(c),lab(f))
        ae=abs(src-code); re=ae/max(abs(src),abs(code),1e-14)
        global count+=1; global max_abs=max(max_abs,ae); global max_rel=max(max_rel,re)
        if ae>1e-11 && re>1e-11
            global bad+=1
            if isempty(worst) || re>worst["relative_error"]
                global worst=Dict("a"=>a,"b"=>b,"c"=>c,"d"=>d,"e"=>e,"f"=>f,
                                  "source_value"=>src,"code_value"=>code,
                                  "absolute_error"=>ae,"relative_error"=>re)
            end
        end
    end
end
pass=(count>0 && bad==0)
out=Dict(
 "test"=>"RC006_APPENDIX_B13_SIXJR_SOURCE_MAPPING",
 "level_k"=>level_k,"cases_tested"=>count,"bad_cases"=>bad,
 "max_absolute_error"=>max_abs,"max_relative_error"=>max_rel,
 "appendix_b13_mapping_pass"=>pass,"worst_case"=>worst,
 "frozen_gate"=>"for every admissible integer-sector sextuple, source-side Eq.B13 coefficient and pinned sixjr agree to abs<=1e-11 or rel<=1e-11",
 "permission_if_pass"=>"Use pinned sixjr only where the RC006 source graph has been explicitly reduced by the paper's B13/B16 identities; Eq29 as a whole remains unimplemented until its graph is mapped without ambiguity.",
 "claim_lock"=>"Convention/source-formula qualification only; not an EPRL amplitude, TNR flow, refinement, continuum, bridge, or new-physics result."
)
open(outfile,"w") do io; TOML.print(io,out); end
TOML.print(stdout,out); println()
