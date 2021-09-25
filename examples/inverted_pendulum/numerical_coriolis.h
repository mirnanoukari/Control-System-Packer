#include <math.h>
void numerical_coriolis(double dtheta, double dx, double l, double m, double theta, double *out_1499320123812452124) {
   out_1499320123812452124[0] = 0;
   out_1499320123812452124[1] = dtheta*l*m*sin(theta);
   out_1499320123812452124[2] = 0;
   out_1499320123812452124[3] = dx*l*m*sin(theta);
}
