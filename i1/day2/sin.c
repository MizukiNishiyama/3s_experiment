#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define PI 3.14159265358979323846
#define SAMPLE_RATE 44100

int main(int argc, char *argv[]) {
    if (argc != 4) {
        fprintf(stderr, "Usage: %s <amplitude> <frequency> <samples>\n", argv[0]);
        return 1;
    }

    int A = atoi(argv[1]);
    double f = atof(argv[2]);
    int n = atoi(argv[3]);

    for (int i = 0; i < n; i++) {
        double t = (double)i / SAMPLE_RATE;
        double sample = A * sin(2 * PI * f * t);
        short output = (short)sample;

        fwrite(&output, sizeof(short), 1, stdout);
    }

    return 0;
}
