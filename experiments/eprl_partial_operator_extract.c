#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include <string.h>

#include "sl2cfoam.h"
#include "sl2cfoam_tensors.h"

static const double NN[4][3] = {
    {0.0, 0.0, 1.0},
    {0.0, 0.9428090415820634, -0.3333333333333333},
    {0.8164965809277260, -0.4714045207910317, -0.3333333333333333},
    {-0.8164965809277260, -0.4714045207910317, -0.3333333333333333}
};

static void closed_shape(double theta, double out[4][3]) {
    double s = sin(theta), c = cos(theta);
    double vals[4][3] = {
        { s, 0.0,  c},
        {-s, 0.0,  c},
        {0.0,  s, -c},
        {0.0, -s, -c}
    };
    memcpy(out, vals, sizeof(vals));
}

static void normals_to_angles(const double n[4][3], double a[4][2]) {
    for (int k = 0; k < 4; ++k) {
        double z = n[k][2];
        if (z > 1.0) z = 1.0;
        if (z < -1.0) z = -1.0;
        a[k][0] = acos(z);
        a[k][1] = atan2(n[k][1], n[k][0]);
    }
}

static sl2cfoam_cvector state_for_label(const char *label) {
    double normals[4][3];
    if (strcmp(label, "regular") == 0) {
        memcpy(normals, NN, sizeof(normals));
    } else if (strcmp(label, "shape_a") == 0) {
        closed_shape(0.92, normals);
    } else if (strcmp(label, "shape_b") == 0) {
        closed_shape(1.02, normals);
    } else if (strcmp(label, "shape_c") == 0) {
        closed_shape(1.12, normals);
    } else if (strcmp(label, "shape_d") == 0) {
        closed_shape(0.82, normals);
    } else {
        fprintf(stderr, "unknown shape label: %s\n", label);
        exit(2);
    }
    double angles[4][2];
    normals_to_angles(normals, angles);
    sl2cfoam_dspin two_js4[4] = {2,2,2,2}; /* j=1 */
    return sl2cfoam_coherentstate_fullrange(two_js4, angles);
}

static void partial_operator(sl2cfoam_tensor_vertex *v,
                             const char *l5, const char *l4, const char *l3,
                             double complex A[3][3]) {
    sl2cfoam_cvector c5 = state_for_label(l5);
    sl2cfoam_cvector c4 = state_for_label(l4);
    sl2cfoam_cvector c3 = state_for_label(l3);

    if (!c5 || !c4 || !c3) {
        fprintf(stderr, "coherent-state allocation failed\n");
        exit(3);
    }

    for (int i2 = 0; i2 < 3; ++i2) {
        for (int i1 = 0; i1 < 3; ++i1) {
            double complex z = 0.0 + 0.0*I;
            for (int i5 = 0; i5 < 3; ++i5)
            for (int i4 = 0; i4 < 3; ++i4)
            for (int i3 = 0; i3 < 3; ++i3) {
                double av = TENSOR_GET(v, 5, i5, i4, i3, i2, i1);
                /* Match official Julia wrapper: transpose(array) * vector,
                   i.e. no complex conjugation of the coherent-state vector. */
                z += av * c5[i5] * c4[i4] * c3[i3];
            }
            A[i2][i1] = z;
        }
    }

    sl2cfoam_vector_free((sl2cfoam_vector)c5);
    sl2cfoam_vector_free((sl2cfoam_vector)c4);
    sl2cfoam_vector_free((sl2cfoam_vector)c3);
}

static void write_operator(FILE *f, const char *name, double complex A[3][3]) {
    fprintf(f, "OP %s\n", name);
    for (int r = 0; r < 3; ++r) {
        for (int c = 0; c < 3; ++c) {
            fprintf(f, "%.17g %.17g%s", creal(A[r][c]), cimag(A[r][c]), c == 2 ? "\n" : " ");
        }
    }
}

int main(int argc, char **argv) {
    if (argc != 5) {
        fprintf(stderr, "usage: %s DATA_ROOT gamma Dl output.txt\n", argv[0]);
        return 2;
    }
    char *root = argv[1];
    double gamma = atof(argv[2]);
    int Dl = atoi(argv[3]);
    const char *outfile = argv[4];

    sl2cfoam_dspin two_js[10] = {2,2,2,2,2,2,2,2,2,2}; /* all j=1 */
    struct sl2cfoam_config conf;
    conf.verbosity = SL2CFOAM_VERBOSE_OFF;
    conf.accuracy = SL2CFOAM_ACCURACY_NORMAL;
    conf.max_two_spin = 3 * (2 + 2*Dl);
    conf.max_MB_mem_per_thread = 0;
    sl2cfoam_init_conf(root, gamma, &conf);

    sl2cfoam_tensor_vertex *v = sl2cfoam_vertex_fullrange(two_js, Dl, TENSOR_RESULT_RETURN);
    if (!v) {
        fprintf(stderr, "vertex_fullrange returned NULL\n");
        sl2cfoam_free();
        return 4;
    }
    if (v->num_keys != 5 || v->dims[0] != 3 || v->dims[1] != 3 || v->dims[2] != 3 || v->dims[3] != 3 || v->dims[4] != 3) {
        fprintf(stderr, "unexpected vertex dimensions: keys=%u dims=%zu,%zu,%zu,%zu,%zu\n",
                v->num_keys, v->dims[0], v->dims[1], v->dims[2], v->dims[3], v->dims[4]);
        sl2cfoam_vertex_free(v);
        sl2cfoam_free();
        return 5;
    }

    struct cfg { const char *name, *l5, *l4, *l3; } cfgs[] = {
        {"train", "regular", "regular", "regular"},
        {"a", "shape_a", "regular", "regular"},
        {"b", "regular", "shape_b", "regular"},
        {"c", "shape_c", "shape_b", "regular"},
        {"d", "shape_d", "regular", "shape_a"}
    };

    FILE *f = fopen(outfile, "w");
    if (!f) {
        perror("fopen");
        sl2cfoam_vertex_free(v);
        sl2cfoam_free();
        return 6;
    }
    fprintf(f, "META gamma %.17g Dl %d spin_j 1 dims 3 3 3 3 3\n", gamma, Dl);
    for (size_t k = 0; k < sizeof(cfgs)/sizeof(cfgs[0]); ++k) {
        double complex A[3][3];
        partial_operator(v, cfgs[k].l5, cfgs[k].l4, cfgs[k].l3, A);
        write_operator(f, cfgs[k].name, A);
    }
    fclose(f);

    sl2cfoam_vertex_free(v);
    sl2cfoam_free();
    return 0;
}
