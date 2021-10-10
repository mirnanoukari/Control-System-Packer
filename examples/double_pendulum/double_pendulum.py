# # from modeling.mechanics.dynamics import MechanicalSystem
from lib.symbolical_dynamics.euler_lagrange import MechanicalSystem
from sympy import Matrix, symbols, cos, sin, simplify, lambdify
from sympy.utilities.autowrap import autowrap
from sympy.utilities.codegen import codegen


def wrapping(expression):
    return autowrap(expression, backend='cython')


# The below provide the equations of double pendulum
# for given kinetic and potential energy
# https://en.wikipedia.org/wiki/Double_pendulum

double_pendulum = MechanicalSystem(symbols(r'theta_1, theta_2'))
q, dq = double_pendulum.q, double_pendulum.dq

# print(f'\nThe generalized coordinates are:\n{q}')
# print(f'\nThe generalized velocities are:\n{dq}')

m1, m2, l1, l2, g = symbols(r'm_1, m_2, l_1, l_2, g')

# The cartesian coordinates of center of mass of point 1
r1 = Matrix([.5 * l1 * sin(q[0]),
             .5 * l1 * cos(q[0])])

# The cartesian coordinates of center of mass of point 1
r2 = Matrix([l1 * sin(q[0]) + .5 * l2 * sin(q[1]),
             l1 * cos(q[0]) + .5 * l2 * cos(q[1])])

# ////// POTENTIAL ENERGY /////
# The potential energy is given as
# P = (y1 * m1 + y2 *m2 )*g
P = simplify((r1[1] * m1 + r2[1] * m2) * g)
double_pendulum.set_potential_energy(P)

# ///// KINETIC ENERGY /////
# One may calculate linear velocities using chain rule:
# The linear velocity of point 1:
dr1 = r1.jacobian(q) * dq
# The linear velocity of point 2:
dr2 = r2.jacobian(q) * dq

# The kinetic energy is equal to:
# K = .5*m1*v1**2 + .5*m2*v2**2
# # where v is linear velocity: v**2 = dr.T * dr   
K = simplify(.5 * dr1.T * dr1 + .5 * dr2.T * dr2)
double_pendulum.set_kinetic_energy(K[0])

# ////// FRICTION /////
# To account for friction forces we introduce the 
# Rayleigh dissipation function (power if dissipative forces)
b1, b2 = symbols(r'b_1, b_2')

R = .5 * b1 * dq[0] ** 2 + .5 * b2 * dq[1] ** 2
double_pendulum.set_rayleigh(R)

double_pendulum.get_lagrange_equations(simp=True)

print(f'\nEquations of motion:\n{double_pendulum.Q}')
print(f'\nInertia matrix:\n{double_pendulum.D}')
print(f'\nGeneralized momenta:\n{double_pendulum.p}')

double_pendulum.create_headers()
double_pendulum.create_cpp_file()
double_pendulum.bind_cpp_file()
