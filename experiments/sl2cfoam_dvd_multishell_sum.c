#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "sl2cfoam.h"
#include "sl2cfoam_tensors.h"

#define MAX_CACHE 128

typedef struct {
    sl2cfoam_dspin l[4];
    sl2cfoam_dmatrix m;
} cache_entry;

static cache_entry cache[MAX_CACHE];
static int cache_n = 0;

static int same_l(const sl2cfoam_dspin a[4], const sl2cfoam_dspin b[4]) {
    return a[0]==b[0] && a[1]==b[1] && a[2]==b[2] && a[3]==b[3];
}

static sl2cfoam_dmatrix get_b4(const sl2cfoam_dspin l[4]) {
    for (int n=0; n<cache_n; ++n) if (same_l(cache[n].l,l)) return cache[n].m;
    if (cache_n >= MAX_CACHE) {
        fprintf(stderr,"B4 cache overflow\n"); exit(20);
    }
    sl2cfoam_dmatrix m = sl2cfoam_b4(2,2,2,2,l[0],l[1],l[2],l[3]);
    if (!m) { fprintf(stderr,"sl2cfoam_b4 returned NULL\n"); exit(21); }
    memcpy(cache[cache_n].l,l,4*sizeof(sl2cfoam_dspin));
    cache[cache_n].m=m;
    ++cache_n;
    return m;
}

static void k_range(const sl2cfoam_dspin l[4], int *kmin, int *kmax) {
    int a=abs(l[0]-l[1]), b=abs(l[2]-l[3]);
    int c=l[0]+l[1], d=l[2]+l[3];
    *kmin = a>b?a:b;
    *kmax = c<d?c:d;
}

static double b4_elem(const sl2cfoam_dspin l[4], int two_i, int two_k) {
    /* Boundary j=(1,1,1,1), so doubled i range is 0,2,4. */
    const int two_i_min=0, two_i_max=4;
    if (two_i<two_i_min || two_i>two_i_max || ((two_i-two_i_min)&1)) return 0.0;
    int kmin,kmax; k_range(l,&kmin,&kmax);
    if (two_k<kmin || two_k>kmax || ((two_k-kmin)&1)) return 0.0;
    const int dimi=(two_i_max-two_i_min)/2+1;
    const int ii=(two_i-two_i_min)/2;
    const int kk=(two_k-kmin)/2;
    sl2cfoam_dmatrix m=get_b4(l);
    double v=matrix_get(m,dimi,ii,kk);
    if (!isfinite(v)) { fprintf(stderr,"nonfinite B4 element\n"); exit(22); }
    return v;
}

static void free_cache(void) {
    for (int n=0;n<cache_n;++n) sl2cfoam_matrix_free((sl2cfoam_matrix)cache[n].m);
    cache_n=0;
}

int main(int argc, char **argv) {
    if (argc!=3) {
        fprintf(stderr,"usage: %s gamma max_D\n",argv[0]); return 2;
    }
    double gamma=atof(argv[1]);
    int maxD=atoi(argv[2]);
    if (maxD<0 || maxD>2) { fprintf(stderr,"frozen max_D must be 0..2\n"); return 3; }

    struct sl2cfoam_config conf;
    conf.verbosity=SL2CFOAM_VERBOSE_OFF;
    conf.accuracy=SL2CFOAM_ACCURACY_NORMAL;
    /* Maximum auxiliary doubled spin is 6; follow pinned b4_test rule max_l+20. */
    conf.max_two_spin=26;
    conf.max_MB_mem_per_thread=0;
    sl2cfoam_init_conf("test/test_data/",gamma,&conf);

    const sl2cfoam_dspin base[4]={2,2,2,2};
    const double first=b4_elem(base,2,2);

    printf("gamma=%.17g\n",gamma);
    for (int D=0; D<=maxD; ++D) {
        double s2=0.0, s3=0.0;
        long long terms2=0, nz2=0, terms3=0, nz3=0;
        const int maxl=2*(1+D);

        /* DVD2: source delta collapses l4=j3'=1 => doubled l4=2. */
        for (int l1=2;l1<=maxl;l1+=2)
        for (int l2=2;l2<=maxl;l2+=2)
        for (int l3=2;l3<=maxl;l3+=2) {
            sl2cfoam_dspin a[4]={l1,l2,l3,2};
            sl2cfoam_dspin b[4]={2,l3,l2,l1};
            int amin,amax,bmin,bmax; k_range(a,&amin,&amax); k_range(b,&bmin,&bmax);
            int km=amin>bmin?amin:bmin, kM=amax<bmax?amax:bmax;
            if (km<=kM) {
                /* All frozen j,l are integer spins, hence doubled k parity is even. */
                if (km&1) ++km;
                for (int tk=km;tk<=kM;tk+=2) {
                    ++terms2;
                    double x=b4_elem(a,2,tk), y=b4_elem(b,2,tk);
                    double term=(double)(tk+1)*x*y; /* d_k=2k+1=tk+1 */
                    if (term!=0.0) ++nz2;
                    s2 += term;
                }
            }
        }
        const double dvd2=9.0*first*s2;

        /* DVD3: exact source factor ordering, fixed t'=i=i'=1. */
        for (int l1=2;l1<=maxl;l1+=2)
        for (int l2=2;l2<=maxl;l2+=2)
        for (int l3=2;l3<=maxl;l3+=2)
        for (int l4=2;l4<=maxl;l4+=2) {
            sl2cfoam_dspin a[4]={2,2,l3,l4};
            sl2cfoam_dspin b[4]={l1,l2,l3,l4};
            sl2cfoam_dspin c[4]={2,2,l2,l1};
            ++terms3;
            double x=b4_elem(a,2,2), y=b4_elem(b,2,2), z=b4_elem(c,2,2);
            double term=x*y*z;
            if (term!=0.0) ++nz3;
            s3 += term;
        }
        const double dvd3=27.0*s3;
        if (!isfinite(dvd2) || !isfinite(dvd3)) {
            fprintf(stderr,"nonfinite DVD shell sum at D=%d\n",D); free_cache(); sl2cfoam_free(); return 5;
        }
        printf("D=%d dvd2=%.17g dvd3=%.17g terms2=%lld nonzero2=%lld terms3=%lld nonzero3=%lld cache=%d\n",
               D,dvd2,dvd3,terms2,nz2,terms3,nz3,cache_n);
    }

    free_cache();
    sl2cfoam_free();
    return 0;
}
