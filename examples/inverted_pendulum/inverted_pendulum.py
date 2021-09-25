# # from modeling.mechanics.dynamics import MechanicalSystem
from lib.symbolical_dynamics.euler_lagrange import MechanicalSystem
from sympy import symbols, cos

# The below provide the equations of inverted pendulum (cart-pole)
# for given kinetic and potential energy
# https://en.wikipedia.org/wiki/inverted_pendulum

inv_pendulum = MechanicalSystem(symbols(r'x, theta'))
q, dq = inv_pendulum.q, inv_pendulum.dq
print(f'\nThe generalized coordinates are:\n{q}')
print(f'\nThe generalized velocities are:\n{dq}')

M, m, g, l = symbols(r'M, m, g, l')

K = .5 * (M + m) * dq[0]**2 - m*l*dq[0]*dq[1] * cos(q[1]) + .5 * m * l**2 * dq[1]**2
inv_pendulum.set_kinetic_energy(K)

print(f'\nKinetic energy:\n{K}')

P = m * g * l * cos(q[1])
inv_pendulum.set_potential_energy(P)

print(f'Potential energy:\n{P}')

inv_pendulum.get_lagrange_equations(simp=True)
print(f'\nEquations of motion:\n{inv_pendulum.Q}')
print(f'\nInertia matrix:\n{inv_pendulum.D}')
print(f'\nGeneralized momenta:\n{inv_pendulum.p}')

inv_pendulum.get_headers()
