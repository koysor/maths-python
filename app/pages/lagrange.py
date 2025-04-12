import streamlit as st
from sympy.parsing.latex import parse_latex


st.set_page_config(layout="wide")
st.markdown("### Lagrange")


def latex_to_sympy_and_print(latex_code):
    st.code(latex_code, language="latex")
    st.latex(latex_code)
    sympy_expression = parse_latex(latex_code)
    st.code(sympy_expression, language="sympy")


summary_lagrange = """
The Lagrange method allows standard calculus to be used to solve optimization problems with equality constraints.
The method involves creating a new function called the Lagrangian, which is the objective function plus the product of the constraint(s) and a Lagrange multiplier.
\nThe Lagrange multiplier is a scalar that is used to enforce the constraint(s) in the optimization problem.
\nThe method involves taking the partial derivatives of the Lagrangian with respect to the variables and the Lagrange multiplier, and setting them equal to zero.
\nThe resulting system of equations can be solved to find the optimal values of the variables that satisfy the constraints.
"""
st.info(summary_lagrange)


st.markdown("#### The Lagrangian Function:")

latex_code = r"""
{L}(x, y, \lambda) = f(x, y) - \lambda g(x, y)
"""
latex_to_sympy_and_print(latex_code)
