#include <math.h>
void numerical_inertia(double M, double l, double m, double theta, double *out_8584476315496453074) {
   out_8584476315496453074[0] = M + m;
   out_8584476315496453074[1] = -l*m*cos(theta);
   out_8584476315496453074[2] = -l*m*cos(theta);
   out_8584476315496453074[3] = 1.0*pow(l, 2)*m;
}
