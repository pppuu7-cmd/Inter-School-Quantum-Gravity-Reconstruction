using Cuba
using TOML
using Printf
using Statistics

# RC-009 true coarse/fine observable reconstruction for the symmetry-restricted
# Riemannian EPRL-FK hyperfrustum model.
#
# Source target: Bahr, Rabuffo, Steinhaus, arXiv:1804.00023v3,
# isotemporal gauge Eqs. (45)-(55), asymptotic amplitude Eqs. (32),(35)-(39).
#
# Geometry convention lock:
#   cos(phi) = (j1-j0)/(4k)
#   K = sqrt(-cos(2phi)) = sqrt(1-(j1-j0)^2/(8k^2))
#   H = 2k*K/(sqrt(j0)+sqrt(j1))
#   V4 = k^2*K*(Q-2)
# This makes the source area-variable volume and Euclidean hyperfrustum
# height/volume relations mutually consistent.
#
# This script evaluates SAME-COUPLING coarse/fine observables.  It is a fixed
# point / cylindrical-consistency audit, not a fit of coarse couplings.

const GAMMA = 0.5
const JI = 1.0
const JF = 1.0
const HTOTAL = 6.0

function k_from_height(j0::Float64, j1::Float64, H::Float64)
    s = sqrt(j0) + sqrt(j1)
    d = j1 - j0
    # From H = 2k/(sqrt(j0)+sqrt(j1))*sqrt(1-d^2/(8k^2)).
    return 0.5 * sqrt(H^2*s^2 + 0.5*d^2)
end

function jacobian_k_to_H(j0::Float64, j1::Float64, H::Float64)
    s = sqrt(j0) + sqrt(j1)
    d = j1 - j0
    # |dk/dH| from the exact inverse above; equivalent to the source Jacobian.
    return H*s^2 / sqrt(4.0*H^2*s^2 + 2.0*d^2)
end

function frustum_geometry(j0::Float64, j1::Float64, H::Float64)
    (j0 > 0 && j1 > 0 && H > 0) || return nothing
    k = k_from_height(j0,j1,H)
    d = j1-j0
    c = d/(4.0*k) # cos(phi)
    abs(c) < inv(sqrt(2.0)) || return nothing
    phi = acos(clamp(c,-1.0,1.0))
    K2 = -cos(2.0*phi)
    K2 > 0 || return nothing
    K = sqrt(K2)
    # Exact height closure sanity.
    Hback = 2.0*k*K/(sqrt(j0)+sqrt(j1))
    abs(Hback-H) <= 5e-12*max(1.0,H) || error("height closure failed: H=$H Hback=$Hback")
    Q = 2.0 + (j0+j1)/(2.0*k)
    invtan = 1.0/tan(phi)
    abs(invtan) <= 1.0 + 1e-12 || return nothing
    theta = acos(clamp(invtan,-1.0,1.0))
    side_theta = acos(clamp(cos(theta)^2,-1.0,1.0))
    SR = 6.0*j0*(pi/2-theta) + 6.0*j1*(pi/2-(pi-theta)) + 12.0*k*(pi/2-side_theta)
    V4 = k^2*K*(Q-2.0)
    V4geom = 0.5*k*(j0+j1)*K
    abs(V4-V4geom) <= 5e-12*max(1.0,abs(V4geom)) || error("volume closure failed")
    return (;k,K,Q,phi,theta,SR,V4)
end

function log_abs_dressed_amp(j0::Float64,j1::Float64,H::Float64,alpha::Float64,G::Float64,Lambda::Float64; mode::String="full")
    g=frustum_geometry(j0,j1,H)
    g === nothing && return -Inf
    k,K,Q,SR,V4 = g.k,g.K,g.Q,g.SR,g.V4
    x = 1.0 + K^2 - 2.0*Q
    D = (j0^3*j1^3*k^15/16.0) * K *
        (K - im*K^2 + im*Q)^3 * x^3 * (K+im)^6 * (K-3im)^2 *
        (1.0 + 3.0*K^2 - 2.0*Q - 2im*K*(Q-1.0))^3
    absD=abs(D)
    absD > 0 || return -Inf
    B = absD / ((1.0+K^2)^3 * abs(1.0+K^2-2.0*Q)^6)
    B > 0 || return -Inf
    varphi=angle(D)
    regge = cos(GAMMA*SR/G - Lambda*V4/G)
    branch = if mode == "full"
        cos(SR/G + varphi) + regge
    elseif mode == "regge_only"
        regge
    else
        error("unknown amplitude mode $mode")
    end
    ab=abs(branch)
    ab > 1e-300 || return -Inf
    return (3.0*alpha-1.5)*(log(j0)+log(j1)) + 6.0*(alpha-1.0)*log(k) - log(B) + log(ab)
end

function coarse_logweight(j::Float64,alpha,G,Lambda; mode="full")
    a=JI/27.0^(2/3) # each of 3^3 cubes has equal 3-volume; area scales n^{-2/3}=1/9
    # Explicitly enforce the source value 1/9, avoiding roundoff in exponentiation.
    a=1.0/9.0
    H=HTOTAL/2.0
    J1=jacobian_k_to_H(a,j,H)
    J2=jacobian_k_to_H(j,a,H)
    l1=log_abs_dressed_amp(a,j,H,alpha,G,Lambda;mode=mode)
    l2=log_abs_dressed_amp(j,a,H,alpha,G,Lambda;mode=mode)
    if !isfinite(l1) || !isfinite(l2) || J1<=0 || J2<=0
        return -Inf
    end
    return log(J1)+log(J2)+27.0*l1+27.0*l2
end

function fine_logweight(j1::Float64,j2::Float64,alpha,G,Lambda; mode="full")
    a=1.0/16.0
    H=HTOTAL/3.0
    ls=(log_abs_dressed_amp(a,j1,H,alpha,G,Lambda;mode=mode),
        log_abs_dressed_amp(j1,j2,H,alpha,G,Lambda;mode=mode),
        log_abs_dressed_amp(j2,a,H,alpha,G,Lambda;mode=mode))
    all(isfinite,ls) || return -Inf
    Js=(jacobian_k_to_H(a,j1,H),jacobian_k_to_H(j1,j2,H),jacobian_k_to_H(j2,a,H))
    all(x->x>0,Js) || return -Inf
    return sum(log,Js)+64.0*sum(ls)
end

function coarse_obs(j::Float64)
    a=1.0/9.0; H=HTOTAL/2.0
    V3=27.0*j^(3/2)
    g1=frustum_geometry(a,j,H); g2=frustum_geometry(j,a,H)
    V4=27.0*(g1.V4+g2.V4)
    return (V3,V3^2,V4)
end

function fine_obs(j1::Float64,j2::Float64)
    a=1.0/16.0; H=HTOTAL/3.0
    # Middle height H_total/2 is halfway through the middle time step.  In the
    # hyperfrustum geometry the cube edge length (scale factor) is sqrt(j), so
    # linear edge interpolation gives the middle-slice area below.
    amid=0.5*(sqrt(j1)+sqrt(j2))
    V3=64.0*amid^3
    gs=(frustum_geometry(a,j1,H),frustum_geometry(j1,j2,H),frustum_geometry(j2,a,H))
    V4=64.0*sum(g.V4 for g in gs)
    return (V3,V3^2,V4)
end

function grid_anchor_coarse(jmin,jmax,alpha,G,Lambda,mode)
    mx=-Inf
    for u in range(0.0,1.0,length=801)
        j=jmin+(jmax-jmin)*u
        mx=max(mx,coarse_logweight(j,alpha,G,Lambda;mode=mode))
    end
    isfinite(mx) || error("no finite coarse grid weight")
    return mx+2.0
end

function grid_anchor_fine(jmin,jmax,alpha,G,Lambda,mode)
    mx=-Inf
    for u in range(0.0,1.0,length=61), v in range(0.0,1.0,length=61)
        j1=jmin+(jmax-jmin)*u; j2=jmin+(jmax-jmin)*v
        mx=max(mx,fine_logweight(j1,j2,alpha,G,Lambda;mode=mode))
    end
    isfinite(mx) || error("no finite fine grid weight")
    return mx+2.0
end

function integrate_coarse(jmin,jmax,alpha,G,Lambda,mode; maxevals=800000)
    anchor=grid_anchor_coarse(jmin,jmax,alpha,G,Lambda,mode)
    span=jmax-jmin
    function f(x,out)
        j=jmin+span*x[1]
        lw=coarse_logweight(j,alpha,G,Lambda;mode=mode)
        if !isfinite(lw)
            out[1]=out[2]=out[3]=out[4]=0.0; return
        end
        w=exp(clamp(lw-anchor,-745.0,650.0))*span
        o=coarse_obs(j)
        out[1]=w; out[2]=w*o[1]; out[3]=w*o[2]; out[4]=w*o[3]
    end
    # Cuhre requires ndim>=2; x[2] is an exact dummy dimension of unit length.
    r=cuhre(f,2,4;rtol=5e-4,atol=1e-12,maxevals=maxevals,key=13)
    I=r.integral
    I[1] > 0 || error("nonpositive coarse Z")
    mean=I[2]/I[1]; m2=I[3]/I[1]
    return (anchor=anchor,V3=mean,VarV3=m2-mean^2,V4=I[4]/I[1],result=r)
end

function integrate_fine(jmin,jmax,alpha,G,Lambda,mode; maxevals=1200000)
    anchor=grid_anchor_fine(jmin,jmax,alpha,G,Lambda,mode)
    span=jmax-jmin
    function f(x,out)
        j1=jmin+span*x[1]; j2=jmin+span*x[2]
        lw=fine_logweight(j1,j2,alpha,G,Lambda;mode=mode)
        if !isfinite(lw)
            out[1]=out[2]=out[3]=out[4]=0.0; return
        end
        w=exp(clamp(lw-anchor,-745.0,650.0))*span^2
        o=fine_obs(j1,j2)
        out[1]=w; out[2]=w*o[1]; out[3]=w*o[2]; out[4]=w*o[3]
    end
    r=cuhre(f,2,4;rtol=7.5e-4,atol=1e-12,maxevals=maxevals,key=13)
    I=r.integral
    I[1] > 0 || error("nonpositive fine Z")
    mean=I[2]/I[1]; m2=I[3]/I[1]
    return (anchor=anchor,V3=mean,VarV3=m2-mean^2,V4=I[4]/I[1],result=r)
end

function relcons(c,f)
    num=sum(abs(c[i]-f[i]) for i=1:3)
    den=sum(0.5*(abs(c[i])+abs(f[i])) for i=1:3)
    return num/max(den,1e-300)
end

length(ARGS)>=7 || error("usage: script alpha G Lambda jmin jmax mode output.toml")
alpha=parse(Float64,ARGS[1]); G=parse(Float64,ARGS[2]); Lambda=parse(Float64,ARGS[3])
jmin=parse(Float64,ARGS[4]); jmax=parse(Float64,ARGS[5]); mode=ARGS[6]; outfile=ARGS[7]

@printf("RC009 parameters alpha=%.9g G=%.9g Lambda=%.9g j=[%.5g,%.5g] mode=%s\n",alpha,G,Lambda,jmin,jmax,mode)
# Flat-geometry sanity: both discretizations represent V3=1 and V4=6 at constant intermediate area.
cflat=coarse_obs(1/9); fflat=fine_obs(1/16,1/16)
@printf("FLAT sanity coarse V3=%.12g V4=%.12g fine V3=%.12g V4=%.12g\n",cflat[1],cflat[3],fflat[1],fflat[3])
abs(cflat[1]-1)<1e-12 && abs(cflat[3]-6)<1e-12 || error("coarse flat geometry sanity failed")
abs(fflat[1]-1)<1e-12 && abs(fflat[3]-6)<1e-12 || error("fine flat geometry sanity failed")

co=integrate_coarse(jmin,jmax,alpha,G,Lambda,mode)
fi=integrate_fine(jmin,jmax,alpha,G,Lambda,mode)
cvec=(co.V3,co.VarV3,co.V4); fvec=(fi.V3,fi.VarV3,fi.V4)
R=relcons(cvec,fvec)

@printf("COARSE V3=%.12g Var=%.12g V4=%.12g fail=%d neval=%d\n",co.V3,co.VarV3,co.V4,co.result.fail,co.result.neval)
@printf("FINE   V3=%.12g Var=%.12g V4=%.12g fail=%d neval=%d\n",fi.V3,fi.VarV3,fi.V4,fi.result.fail,fi.result.neval)
@printf("CYLINDRICAL_R=%.12g\n",R)

out=Dict(
 "test"=>"RC009_ISOTEMPORAL_COARSE_FINE_CUHRE_RECONSTRUCTION",
 "status"=>"PASS_EXECUTION",
 "alpha"=>alpha,"G"=>G,"Lambda"=>Lambda,"jmin"=>jmin,"jmax"=>jmax,"amplitude_mode"=>mode,
 "source_setup"=>Dict("coarse_hyperfrusta"=>54,"fine_hyperfrusta"=>192,"boundary_total_area_spin"=>1.0,"total_height"=>6.0,"gamma"=>GAMMA),
 "geometry_lock"=>Dict("K_convention"=>"sqrt(-cos(2phi))","height_inversion"=>"k=0.5*sqrt(H^2*(sqrt(j0)+sqrt(j1))^2+(j1-j0)^2/2)"),
 "coarse"=>Dict("V3"=>co.V3,"VarV3"=>co.VarV3,"V4"=>co.V4,"anchor"=>co.anchor,"fail"=>co.result.fail,"neval"=>co.result.neval,"nregions"=>co.result.nregions,"integral_error"=>co.result.error,"probability"=>co.result.prob),
 "fine"=>Dict("V3"=>fi.V3,"VarV3"=>fi.VarV3,"V4"=>fi.V4,"anchor"=>fi.anchor,"fail"=>fi.result.fail,"neval"=>fi.result.neval,"nregions"=>fi.result.nregions,"integral_error"=>fi.result.error,"probability"=>fi.result.prob),
 "relative_cylindrical_consistency_R"=>R,
 "preregistered_gate"=>Dict("natural"=>"both Cuhre fail codes 0 and R<=0.05","strong"=>"both Cuhre fail codes 0 and R<=0.01"),
 "natural_same_coupling_consistency_support"=>(co.result.fail==0 && fi.result.fail==0 && R<=0.05),
 "strong_same_coupling_consistency_support"=>(co.result.fail==0 && fi.result.fail==0 && R<=0.01),
 "interpretation_lock"=>"This reconstructs the source-defined symmetry-restricted asymptotic coarse/fine observable integrals at the same couplings. Failure can reflect parameter/source ambiguity, cutoff or numerical convergence, or implementation details and is not a refutation of full EPRL-FK. Success is not evidence for a full-theory continuum limit."
)
open(outfile,"w") do io; TOML.print(io,out); end
