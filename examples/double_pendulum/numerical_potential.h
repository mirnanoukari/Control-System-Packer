#include <math.h>
void numerical_potential(double g, double l_1, double l_2, double m_1, double m_2, double theta_1, double theta_2, double *out_2753430389373685639) {
   out_2753430389373685639[0] = -g*l_1*(0.5*m_1 + m_2)*sin(theta_1);
   out_2753430389373685639[1] = -0.5*g*l_2*m_2*sin(theta_2);
}
