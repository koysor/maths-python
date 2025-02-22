import streamlit as st


st.set_page_config(layout="wide")
st.markdown("### Differentiation")

summary_differentiation = """
Differentiation is the process of finding the slope or rate of change of a function at a particular point.
\nThis is also known as the first derivative of a function.
\nThe second derivative is the rate at which the slope or first derivative is changing.
"""
st.info(summary_differentiation)


st.markdown("#### Differentiation Example with Sympy")

st.write("The Sympy library is used to perform symbolic differentiation which produces as output an exact formula for the derivative.")

expression = "x^2 + 3x + 5"

latex_code = f"""
f(x) = {expression}
"""
st.latex(latex_code,)

code_snippet = """
import sympy as sp
import streamlit as st

x = sp.symbols('x')

f = x**2 + 3*x + 5
f_prime = sp.diff(f, x)
f_double_prime = sp.diff(f_prime, x)

st.write(f"Function: {f}")
st.write(f"Derivative: {f_prime}")
st.write(f"Second Derivative: {f_double_prime}")
"""

st.code(code_snippet)
exec(code_snippet)


st.markdown("#### Differentiation Example Using the Finite Differences Method")

st.write("""You can implement differentiation using the finite differences method.
Differentiation using finite differences is a numerical method to approximate the derivative of a function at a particular point based on discreate data points.
The difference between the discreate data points should be small to get a good approximation of the tangent line at a particular point.""")


code_snippet = """
import streamlit as st

def f(x):
    return x**2 + 3*x + 5

def numerical_derivative(func, x, h=1e-5):
    return (func(x + h) - func(x - h)) / (2 * h)

# Choose a point to evaluate the derivative
x_value = 1.0
derivative_at_x = numerical_derivative(f, x_value)

st.write(f"The derivative of f(x) at x={x_value} is approximately: {derivative_at_x}")
st.write(f"This is consistent with the First Derivative symbol above, {f_prime} .  As 2*(1) + 3 = 5.")
"""

st.code(code_snippet)
exec(code_snippet)


st.markdown("#### Differentiation Example Using SciPy")

code_snippet = """
import streamlit as st
import numpy as np
from scipy.optimize import approx_fprime

def f(x):
    return x[0]**2 + 3*x[0] + 5  # Function expects an array input

x_value = np.array([1.0])
epsilon = np.sqrt(np.finfo(float).eps)  # Optimal step size for numerical differentiation

# Compute the derivative
deriv = approx_fprime(x_value, f, epsilon)

st.write(f"The derivative of f(x) at x={x_value[0]} is approximately: {deriv[0]}")
"""

st.code(code_snippet)
exec(code_snippet)