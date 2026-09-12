#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "sl2cfoam.h"
#include "sl2cfoam_tensors.h"

int main(int argc, char** argv) {
    if (argc != 2) {
        fprintf(stderr, "usage: %s gamma\n", argv[0]);
        return 2;
    }
    double gamma = atof(argv[1]);

    struct sl2cfoam_config conf;
    conf.verbosity = SL2CFOAM_VERBOSE_OFF;
    conf.accuracy = SL2CFOAM_ACCURACY_NORMAL;
    conf.max_two_spin = 24;
    conf.max_MB_mem_per_thread = 0;
    sl2cfoam_init_conf("test/test_data/", gamma, &conf);

    /* Frozen preregistration: j_a=l_a=1, so doubled spins are 2. */
    const sl2cfoam_dspin two_j = 2;
    sl2cfoam_dmatrix b4 = sl2cfoam_b4(two_j, two_j, two_j, two_j,
                                      two_j, two_j, two_j, two_j);
    if (b4 == NULL) {
        fprintf(stderr, "sl2cfoam_b4 returned NULL\n");
        sl2cfoam_free();
        return 3;
    }

    /* For four equal j=1 legs, i,k in {0,1,2}; doubled indices 0,2,4. */
    const int dim = 3;
    const int idx_i1 = 1;
    double row[3];
    for (int q = 0; q < 3; ++q) {
        row[q] = matrix_get(b4, dim, idx_i1, q);
        if (!isfinite(row[q])) {
            fprintf(stderr, "nonfinite B4 row value at q=%d\n", q);
            sl2cfoam_matrix_free((sl2cfoam_matrix)b4);
            sl2cfoam_free();
            return 4;
        }
    }

    const double b11 = row[1];
    const double dvd3 = 27.0 * b11 * b11 * b11;

    double weighted = 0.0;
    for (int q = 0; q < 3; ++q) {
        const int two_k = 2*q;
        const double d_k = (double)(two_k + 1); /* 2k+1 */
        weighted += d_k * row[q] * row[q];
    }
    const double dvd2 = 9.0 * b11 * weighted;

    printf("gamma=%.17g\n", gamma);
    printf("b4_i1_k0=%.17g\n", row[0]);
    printf("b4_i1_k1=%.17g\n", row[1]);
    printf("b4_i1_k2=%.17g\n", row[2]);
    printf("weighted_k_sum=%.17g\n", weighted);
    printf("dvd2_dl0=%.17g\n", dvd2);
    printf("dvd3_dl0=%.17g\n", dvd3);

    sl2cfoam_matrix_free((sl2cfoam_matrix)b4);
    sl2cfoam_free();
    return (isfinite(dvd2) && isfinite(dvd3)) ? 0 : 5;
}
