#include <math.h>
void numerical_inertia(double l_1, double l_2, double theta_1, double theta_2, double *out_3845088474358444776) {
   out_3845088474358444776[0] = 1.25*pow(l_1, 2);
   out_3845088474358444776[1] = 0.5*l_1*l_2*cos(theta_1 - theta_2);
   out_3845088474358444776[2] = 0.5*l_1*l_2*cos(theta_1 - theta_2);
   out_3845088474358444776[3] = 0.25*pow(l_2, 2);
}
