#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "sl2cfoam.h"
#include "sl2cfoam_tensors.h"

#define MAX_CACHE 512

typedef struct { sl2cfoam_dspin l[4]; sl2cfoam_dmatrix m; } cache_entry;
static cache_entry cache[MAX_CACHE]; static int cache_n=0;

static int same_l(const sl2cfoam_dspin a[4],const sl2cfoam_dspin b[4]){for(int q=0;q<4;++q)if(a[q]!=b[q])return 0;return 1;}
static void krange(const sl2cfoam_dspin l[4],int *lo,int *hi){int a=abs(l[0]-l[1]),b=abs(l[2]-l[3]),c=l[0]+l[1],d=l[2]+l[3];*lo=a>b?a:b;*hi=c<d?c:d;}
static sl2cfoam_dmatrix get_b4(const sl2cfoam_dspin l[4]){
  for(int n=0;n<cache_n;++n)if(same_l(cache[n].l,l))return cache[n].m;
  if(cache_n>=MAX_CACHE){fprintf(stderr,"cache overflow\n");exit(20);}sl2cfoam_dmatrix m=sl2cfoam_b4(2,2,2,2,l[0],l[1],l[2],l[3]);if(!m){fprintf(stderr,"NULL b4\n");exit(21);}memcpy(cache[cache_n].l,l,4*sizeof(int));cache[cache_n].m=m;++cache_n;return m;
}
static double elem(const sl2cfoam_dspin l[4],int ti,int tk){int k0,k1;krange(l,&k0,&k1);if(ti<0||ti>4||(ti&1))return 0.0;if(tk<k0||tk>k1||((tk-k0)&1))return 0.0;int dimi=3,ii=ti/2,kk=(tk-k0)/2;double v=matrix_get(get_b4(l),dimi,ii,kk);if(!isfinite(v)){fprintf(stderr,"nonfinite b4\n");exit(22);}return v;}
static void cleanup(void){for(int n=0;n<cache_n;++n)sl2cfoam_matrix_free((sl2cfoam_matrix)cache[n].m);cache_n=0;}

int main(int argc,char **argv){
  if(argc!=2){fprintf(stderr,"usage: %s gamma\n",argv[0]);return 2;}double gamma=atof(argv[1]);
  struct sl2cfoam_config conf;conf.verbosity=SL2CFOAM_VERBOSE_OFF;conf.accuracy=SL2CFOAM_ACCURACY_NORMAL;conf.max_two_spin=28;conf.max_MB_mem_per_thread=0;sl2cfoam_init_conf("test/test_data/",gamma,&conf);
  const sl2cfoam_dspin base[4]={2,2,2,2};double first=elem(base,2,2);printf("gamma=%.17g\n",gamma);
  for(int D=0;D<=3;++D){double s2=0.0,s3=0.0;long long terms2=0,nz2=0,terms3=0,nz3=0;int maxl=2*(1+D);
    for(int l1=2;l1<=maxl;l1+=2)for(int l2=2;l2<=maxl;l2+=2)for(int l3=2;l3<=maxl;l3+=2){sl2cfoam_dspin A[4]={l1,l2,l3,2},B[4]={2,l3,l2,l1};int a0,a1,b0,b1;krange(A,&a0,&a1);krange(B,&b0,&b1);int lo=a0>b0?a0:b0,hi=a1<b1?a1:b1;if(lo&1)++lo;for(int tk=lo;tk<=hi;tk+=2){++terms2;double x=elem(A,2,tk),y=elem(B,2,tk),term=(double)(tk+1)*x*y;if(term!=0.0)++nz2;s2+=term;}}
    double dvd2=9.0*first*s2;
    for(int l1=2;l1<=maxl;l1+=2)for(int l2=2;l2<=maxl;l2+=2)for(int l3=2;l3<=maxl;l3+=2)for(int l4=2;l4<=maxl;l4+=2){sl2cfoam_dspin A[4]={2,2,l3,l4},B[4]={l1,l2,l3,l4},C[4]={2,2,l2,l1};++terms3;double term=elem(A,2,2)*elem(B,2,2)*elem(C,2,2);if(term!=0.0)++nz3;s3+=term;}
    double dvd3=27.0*s3;if(!isfinite(dvd2)||!isfinite(dvd3)){fprintf(stderr,"nonfinite amplitude\n");cleanup();sl2cfoam_free();return 5;}
    printf("D=%d dvd2=%.17g dvd3=%.17g terms2=%lld nonzero2=%lld terms3=%lld nonzero3=%lld cache=%d\n",D,dvd2,dvd3,terms2,nz2,terms3,nz3,cache_n);
  }
  cleanup();sl2cfoam_free();return 0;
}
