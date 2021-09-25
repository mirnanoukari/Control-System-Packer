from sympy import Function, Derivative, Matrix, symbols, diff


def diff_total(expr, diff_by, diff_map):
    """
    Replace variables with their differentials in expression
    @param expression expr: expression to differentiate
    @param symbol diff_by: variable to differentiate with respect to
    @param dictionary diff_map: map for n-th order derivative
    @return expression: result of differentiation
    """
    # Replace all symbols in the diff_map by a functional form
    fun_expr = expr.subs({s: Function(str(s))(diff_by) for s in diff_map})
    diff_expr = diff(fun_expr, diff_by)

    # Create map to replace each 'Derivative' with the variable
    deriv_map = {Derivative(Function(str(v))(diff_by), diff_by): dv
                 for v, dv in diff_map.items()}
    # Replace the 'Derivatives' with the variables in diff_map
    final_diff = diff_expr.subs(deriv_map)

    # Replace functional form with their symbols
    result = final_diff.subs({Function(str(s))(diff_by): s for s in diff_map})

    return result


def diff_symbols(variables, diff_order=1, text_form=False):
    """
    Transform  vector of strings variables to their derivatives in LaTeX form.
    @param array.pyi variables: variables to differentiate
    @param int diff_order: order of derivative of expression
    @param bool text_form: return expression in text form or not
    @return matrix: matrix with variables or their corresponding differential form
    """
    n = len(variables)
    diff_variable = [0] * n
    if diff_order > 0:
        for i in range(n):
            # For each varibale find its derivative
            if text_form:
                diff_variable[i] = '\d' + 'd' * (diff_order - 1) + 'ot{' + str(variables[i]) + '}'
            else:
                diff_variable[i] = 'd' * diff_order + str(variables[i])
        # Matrix with differentials of variables
        var_matrix = Matrix(symbols(diff_variable))
    else:
        # Matrix only with variables
        var_matrix = Matrix(variables)
    return var_matrix


def build_diffmap(variables, diff_order=1, text_form=False):
    """
    Build differential map for n-th order derivative.
    @param array.pyi variables: variables to differentiate
    @param int diff_order: order of derivative of expression
    @param bool text_form: return expression in text form or not
    @return dictionary: map for n-th order derivative
    """
    diff_map = dict()
    for i in range(diff_order + 1):
        # For each variable find corresponding differential form
        di_x = diff_symbols(variables, diff_order=i - 1, text_form=text_form)
        ddi_x = diff_symbols(variables, diff_order=i, text_form=text_form)
        for j in range(len(variables)):
            # Put these forms in the dictionary
            diff_map[di_x[j]] = ddi_x[j]
    return diff_map


def time_diff(expression, variables, order=1, diff_order=1, text_form=False):
    """
    Find and return the derivative of expression with respect to t.
    @param expression: expression that we want to differentiate
    @param array.pyi variables: variables to differentiate
    @param int order: oder of derivative we need
    @param int diff_order: order of derivative of expression itself
    @param bool text_form: return expression in text form or not
    @return expression: derivative of expression with respect to t for given variables
    """
    t = symbols('t')
    result = expression
    for i in range(order):
        # Find differential map
        diff_map = build_diffmap(variables, diff_order, text_form=text_form)
        # Get result of differentiation
        result = diff_total(result, t, diff_map)
    return result
