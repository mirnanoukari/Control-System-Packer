#include <math.h>
void numerical_momentum(double dtheta_1, double dtheta_2, double l_1, double l_2, double theta_1, double theta_2, double *out_2787242366367463515) {
   out_2787242366367463515[0] = 1.25*dtheta_1*pow(l_1, 2) + 0.5*dtheta_2*l_1*l_2*cos(theta_1 - theta_2);
   out_2787242366367463515[1] = 0.5*dtheta_1*l_1*l_2*cos(theta_1 - theta_2) + 0.25*dtheta_2*pow(l_2, 2);
}
