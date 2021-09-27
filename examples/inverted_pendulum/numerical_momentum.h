#include <math.h>
void numerical_momentum(double M, double dtheta, double dx, double l, double m, double theta, double *out_7833949798600791816) {
   out_7833949798600791816[0] = -dtheta*l*m*cos(theta) + 2*dx*(0.5*M + 0.5*m);
   out_7833949798600791816[1] = 1.0*dtheta*pow(l, 2)*m - dx*l*m*cos(theta);
}
