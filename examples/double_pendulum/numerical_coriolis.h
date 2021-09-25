#include <math.h>
void numerical_coriolis(double dtheta_1, double dtheta_2, double l_1, double l_2, double theta_1, double theta_2, double *out_8124209321856086755) {
   out_8124209321856086755[0] = -0.5*dtheta_2*l_1*l_2*sin(theta_1 - theta_2);
   out_8124209321856086755[1] = 0.5*dtheta_2*l_1*l_2*sin(theta_1 - theta_2);
   out_8124209321856086755[2] = -0.5*dtheta_1*l_1*l_2*sin(theta_1 - theta_2);
   out_8124209321856086755[3] = 0.5*dtheta_1*l_1*l_2*sin(theta_1 - theta_2);
}
