#include <math.h>
void numerical_combined(double b_1, double b_2, double dtheta_1, double dtheta_2, double g, double l_1, double l_2, double m_1, double m_2, double theta_1, double theta_2, double *out_5071088623219199596) {
   out_5071088623219199596[0] = 1.0*b_1*dtheta_1 + 0.5*dtheta_2*l_1*l_2*(-dtheta_1 + dtheta_2)*sin(theta_1 - theta_2) - g*l_1*(0.5*m_1 + m_2)*sin(theta_1);
   out_5071088623219199596[1] = 1.0*b_2*dtheta_2 + 0.5*dtheta_1*l_1*l_2*(-dtheta_1 + dtheta_2)*sin(theta_1 - theta_2) - 0.5*g*l_2*m_2*sin(theta_2);
}
