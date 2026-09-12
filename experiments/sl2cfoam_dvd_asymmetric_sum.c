#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "sl2cfoam.h"
#include "sl2cfoam_tensors.h"

#define MAX_CACHE 512

typedef struct { sl2cfoam_dspin j[4], l[4]; sl2cfoam_dmatrix m; } entry;
static entry cache[MAX_CACHE]; static int cache_n=0;

static int same4(const sl2cfoam_dspin a[4],const sl2cfoam_dspin b[4]){for(int q=0;q<4;++q)if(a[q]!=b[q])return 0;return 1;}
static void irange(const sl2cfoam_dspin x[4],int *lo,int *hi){int a=abs(x[0]-x[1]),b=abs(x[2]-x[3]),c=x[0]+x[1],d=x[2]+x[3];*lo=a>b?a:b;*hi=c<d?c:d;}
static sl2cfoam_dmatrix get_b4(const sl2cfoam_dspin j[4],const sl2cfoam_dspin l[4]){
  for(int n=0;n<cache_n;++n)if(same4(cache[n].j,j)&&same4(cache[n].l,l))return cache[n].m;
  if(cache_n>=MAX_CACHE){fprintf(stderr,"cache overflow\n");exit(20);} 
  sl2cfoam_dmatrix m=sl2cfoam_b4(j[0],j[1],j[2],j[3],l[0],l[1],l[2],l[3]);
  if(!m){fprintf(stderr,"NULL b4\n");exit(21);} memcpy(cache[cache_n].j,j,4*sizeof(int));memcpy(cache[cache_n].l,l,4*sizeof(int));cache[cache_n].m=m;++cache_n;return m;
}
static double elem(const sl2cfoam_dspin j[4],const sl2cfoam_dspin l[4],int ti,int tk){
  int imin,imax,kmin,kmax;irange(j,&imin,&imax);irange(l,&kmin,&kmax);
  if(ti<imin||ti>imax||((ti-imin)&1))return 0.0;if(tk<kmin||tk>kmax||((tk-kmin)&1))return 0.0;
  int dimi=(imax-imin)/2+1,ii=(ti-imin)/2,kk=(tk-kmin)/2;double v=matrix_get(get_b4(j,l),dimi,ii,kk);
  if(!isfinite(v)){fprintf(stderr,"nonfinite b4\n");exit(22);}return v;
}
static void cleanup(void){for(int n=0;n<cache_n;++n)sl2cfoam_matrix_free((sl2cfoam_matrix)cache[n].m);cache_n=0;}

int main(int argc,char **argv){
  if(argc!=3){fprintf(stderr,"usage: %s gamma maxD\n",argv[0]);return 2;}double gamma=atof(argv[1]);int maxD=atoi(argv[2]);if(maxD<0||maxD>2)return 3;
  struct sl2cfoam_config conf;conf.verbosity=SL2CFOAM_VERBOSE_OFF;conf.accuracy=SL2CFOAM_ACCURACY_NORMAL;conf.max_two_spin=28;conf.max_MB_mem_per_thread=0;sl2cfoam_init_conf("test/test_data/",gamma,&conf);
  const sl2cfoam_dspin J[4]={2,4,4,4}, JP[4]={2,4,4,2};
  const sl2cfoam_dspin firstL[4]={2,4,4,4};
  const double first=elem(J,firstL,2,2);
  printf("gamma=%.17g\n",gamma);
  for(int D=0;D<=maxD;++D){
    double s2=0.0,s3=0.0;long long terms2=0,nz2=0,terms3=0,nz3=0;
    int l1max=2+2*D,l2max=4+2*D,l3max=4+2*D,l4max=4+2*D;
    for(int l1=2;l1<=l1max;l1+=2)for(int l2=4;l2<=l2max;l2+=2)for(int l3=4;l3<=l3max;l3+=2){
      sl2cfoam_dspin A[4]={l1,l2,l3,4},B[4]={2,l3,l2,l1};int a0,a1,b0,b1;irange(A,&a0,&a1);irange(B,&b0,&b1);int lo=a0>b0?a0:b0,hi=a1<b1?a1:b1;
      if(lo&1)++lo;for(int tk=lo;tk<=hi;tk+=2){++terms2;double x=elem(J,A,2,tk),y=elem(JP,B,2,tk);double term=(double)(tk+1)*x*y;if(term!=0.0)++nz2;s2+=term;}
    }
    /* d_i d_i' d_t / d_j3' = 3*3*3/5 = 27/5; integer-spin phase is +1. */
    double dvd2=(27.0/5.0)*first*s2;
    for(int l1=2;l1<=l1max;l1+=2)for(int l2=4;l2<=l2max;l2+=2)for(int l3=4;l3<=l3max;l3+=2)for(int l4=4;l4<=l4max;l4+=2){
      sl2cfoam_dspin A[4]={2,4,l3,l4},B[4]={l1,l2,l3,l4},C[4]={2,4,l2,l1};++terms3;double x=elem(J,A,2,2),y=elem(J,B,2,2),z=elem(JP,C,2,2);double term=x*y*z;if(term!=0.0)++nz3;s3+=term;
    }
    double dvd3=27.0*s3;if(!isfinite(dvd2)||!isfinite(dvd3)){fprintf(stderr,"nonfinite amplitude\n");cleanup();sl2cfoam_free();return 5;}
    printf("D=%d dvd2=%.17g dvd3=%.17g terms2=%lld nonzero2=%lld terms3=%lld nonzero3=%lld cache=%d\n",D,dvd2,dvd3,terms2,nz2,terms3,nz3,cache_n);
  }
  cleanup();sl2cfoam_free();return 0;
}
