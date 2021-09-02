from .misc._diff import diff_symbols
from sympy import diff, zeros, Matrix, lambdify

# , MatrixSymbol, Eq, eye
# from sympy.utilities.codegen import codegen
# # from sympy.printing.ccode import C99CodePrinter
# from numpy import dot as n_dot
# from numpy.linalg import inv as n_inv
# from numpy import concatenate


class MechanicalSystem:
    """"""

    def __init__(self,
                 q,  # the vector of generalized coordinates
                 K=0,  # kinetic energy as function of generalized coordinates and velocities
                 P=0,  # potential energy as function of potential coordinates
                 R=0  # rayleigh dissipative function as function of coordinates and velocities
                 ):

        # q : nx1 vector of generalized coordinates
        self.q = Matrix(q)
        # dq : nx1 vector of generalized velocities
        self.dq = diff_symbols(q)
        # ddq : nx1 vector of generalized accelerations
        self.ddq = diff_symbols(q, 2)
        # the state of mechanical system is 2n vector
        # x = [q, dq]
        self.state = {'q': self.q, 'dq': self.dq}
        # n is dimension of problem
        self.n = len(q)

        # p is nx1 generalized momenta
        self.p = zeros(self.n, 1)
        # D is nxn PD inertia matrix
        self.D = zeros(self.n, self.n)
        # C is nxn matrix of coriolis and centrifugal effects
        self.C = zeros(self.n, self.n)
        # c is nx1 vector of resulting coriolis and centrifugal forces
        self.c = zeros(self.n, 1)
        # g is nx1 vector of potential forces
        self.g = zeros(self.n, 1)
        # d is nx1 vector of dissipative forces
        self.d = zeros(self.n, 1)
        # h is nx1 vector of combined coriolis, potential and dissipative forces
        self.h = zeros(self.n, 1)
        # Q is nx1 vector of generalized coordinates
        self.Q = zeros(self.n, 1)
        # K is kinetic energy
        self.K = K
        # P is potential energy
        self.P = P
        # Rayleigh dissipation function
        self.R = R
        # self.t = symbols('t')

    def __del__(self):
        print("System was destructed")

    def set_kinetic_energy(self, expr):
        '''Set the kinetic energy of system as expression 
           of generalized coordinates and velocities K(q,dq)'''
        self.K = expr

    def set_potential_energy(self, expr):
        '''Set the potential energy of system as expression 
           of generalized coordinates P(q)'''
        self.P = expr

    def set_rayleigh(self, expr):
        '''Set the rayleigh function of system as expression 
           of generalized coordinates and velocities R(q, dq)'''
        self.R = expr

    # /////////////////////////
    # // Symbolical Routines //
    # /////////////////////////

    def get_lagrange_equations(self, simp=False):
        '''Calculate the dynamical terms using 
           Euler-Lagrange equations: 
            dp/dt - dL/dq + dR/dq = Q
        '''
        # Calculate Lagrangian
        self.L = self.K - self.P

        # Obtain generalized momentum and inertia matrix
        for i in range(self.n):
            # Obtain generalized momentum p
            self.p[i] = diff(self.L, self.dq[i])
            # find the row of inertia matrix
            self.D[i, :] = Matrix([self.p[i]]).jacobian(self.dq)
            # find the gravitational terms
            self.g[i] = diff(self.P, self.q[i])
            # find the dissipative forces
            self.d[i] = diff(self.R, self.dq[i])

        # TODO: find a way how to get rid from two identical cycles
        for i in range(self.n):
            # find the matrix if coriolis and centrifugal
            self.C[i, :] = Matrix([self.p[i]]).jacobian(self.q)
            - (self.dq).T*diff(self.D, self.q[i])/2
            # find the coriolis and centrifugal force
            self.c[i] = self.C[i, :]*self.dq

        print('Dynamics is calculated')

        # Simplify terms
        if simp:
            for term in [self.D, self.C, self.c, self.g, self.d]:
                term.simplify()
            print('Dynamics was simplified')

        # get the combined term
        self.h = self.c + self.g + self.d

        # calculate the final result
        self.Q = self.D*self.ddq + self.h

    # ////////////////////////
    # // Numerical Routines //
    # ////////////////////////
    # the code below transform the expressions above to functions
    # that can be evaluated numerically.
    # everything is done via lambdify routine

    def get_numerical_momentum(self):
        '''Return the function of 
           generalized momenta: p(q, dq)'''
        self.p_num = lambdify([self.q, self.dq], self.p)
        return self.p_num

    def get_numerical_inertia(self):
        '''Return the function of 
           inertia matrix: D(q)'''
        self.D_num = lambdify([self.q], self.D)
        return self.D_num

    def get_numerical_coriolis(self):
        '''Return the function of 
           coriolis and centrifugal: C(q, dq)'''
        self.C_num = lambdify([self.q, self.dq], self.C)
        return self.C_num

    def get_numerical_potential(self):
        '''Return the function of 
           potential forces: g(q)'''
        self.g_num = lambdify([self.q], self.g)
        return self.g_num

    def get_numerical_combined(self):
        '''Return the function of 
           combined potential, centrifugal 
           and dissipative forces: d(q,dq)'''
        self.h_num = lambdify([self.q, self.dq], self.h) 
        return self.h_num


    # //////////////////////////////////
    # ///// WORK IN PROGRESS.... ///////
    # //////////////////////////////////

    def get_numerical(self):
        # self.nD = self.get_numerical_inertia()
        # self.nh = self.get_numerical_combined()
        pass
    
    # Calculate numerical value of state derevitive dxdt = f(x, u)
    def calcStateSpace(self, state, control):
        # q, dq = state[:self.n], state[self.n:]
        # u = control
        # D = self.nD
        # h = self.nh
        # # print(h(q,dq))
        # ddq = nDot(nInv(D(q)), (u - h(q, dq)[0]))
        # return concatenate((dq, ddq))
        pass

    def getStateSpace(self):
        # self.getNumerical()
        # def f(x, u): return self.calcStateSpace(x, u)
        # return f
        pass

    # Find usefull Partial derevitives

    def findPartials(self):
        # self.dDdq = diff(self.D, self.q)
        # self.dhdq = diff(self.h, self.q)
        # self.dhddq = diff(self.h, self.dq)
        pass

    def getPartials(self):
        # dDdq = lambdify([self.q], self.dDdq)
        # dhdq = lambdify([self.q, self.dq], self.dhdq)
        # dhddq = lambdify([self.q, self.dq], self.dhddq)
        # return dDdq, dhdq, dhddq
        pass

    def findLinearization(self):
        # self.A = zeros(2*self.n, 2*self.n)
        # self.B = zeros(2*self.n, self.n)
        # invD = self.D.inv()
        # self.A[:self.n, self.n:] = eye(self.n)
        # self.B[self.n:, :] = invD
        pass

    def setParameters(self):
        pass

    def calcLinearization(self):
        pass
