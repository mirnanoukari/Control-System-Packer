#include <math.h>
void numerical_combined(double dtheta, double dx, double g, double l, double m, double theta, double *out_3422592480388761343) {
   out_3422592480388761343[0] = pow(dtheta, 2)*l*m*sin(theta);
   out_3422592480388761343[1] = dtheta*dx*l*m*sin(theta) - g*l*m*sin(theta);
}
