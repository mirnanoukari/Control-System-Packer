from sympy import Function, Derivative, Matrix, symbols, diff

# TODO: 
#  Add dependence_order option: dependence of expression on time derevitives of variable
#  Write documantation strings 

def difftotal(expr, diffby, diffmap):
    # Replace all symbols in the diffmap by a functional form
    fnexpr = expr.subs({s:Function(str(s))(diffby) for s in diffmap})
    diffexpr = diff(fnexpr, diffby)

    # Replace the Derivatives with the variables in diffmap
    derivmap = {Derivative(Function(str(v))(diffby), diffby):dv 
                for v, dv in diffmap.items()}
   
    finaldiff = diffexpr.subs(derivmap)

    # Replace functional form with their symbols
    output = finaldiff.subs({Function(str(s))(diffby):s for s in diffmap})

    return output


# Transform  vector of strings variables to their derevvitives in LaTeX form 
def diff_symbols(variable, order = 1, texform = False):
    n = len(variable)
    dvariable = [0]*n
    if order>0:
      for i in range(n):
        if texform:
          dvariable[i] = '\d' + 'd'*(order-1) + 'ot{' + str(variable[i]) +'}'
        else:
          dvariable[i] = 'd'*(order) + str(variable[i])

      out = Matrix(symbols(dvariable))
    else:
      out = Matrix(variable)
    return out


# build differential map for n-th order derivetive
def build_diffmap(variable, order=1, texform = False):
    diff_map = dict()
    n = len(variable)
    for i in range(order+1):
      di_x = diff_symbols(variable, i-1, texform = texform)
      ddi_x = diff_symbols(variable, i, texform = texform)
      for j in range(n):
        diff_map[di_x[j]] = ddi_x[j]
    return diff_map


def time_diff(expression, variables, order = 1, dorder = 1, texform = False):
    t = symbols('t')
    diffmap = build_diffmap(variables, dorder, texform = texform)
    result = difftotal(expression, t, diffmap)
    # for i in range(order):
    #   diffmap = build_diffmap(variables, dorder)
    #   result = difftotal(result, t, diffmap)
    return result
