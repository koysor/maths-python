import streamlit as st


st.set_page_config(layout="wide")
st.markdown("### Differentiation")

summary_differentiation = """
Differentiation is the process of finding the slope or rate of change of a function at a particular point.
\nThis is also known as the first derivative of a function or the gradient function.
\nThe second derivative is the rate at which the slope or first derivative is changing.
"""
st.info(summary_differentiation)


st.markdown("### Differentiating from First Principles")

col1, col2 = st.columns([4,3])

with col1:
    st.write("""As the distance between two points on a curve approaches zero, 
    the slope of the line between the two points approaches the slope of the tangent line at a particular point on the curve.""")

    latex_code = r"""
    \frac{dy}{dx} = \lim_{h \to 0 } \frac{f(x+h)-f(x)}{h}
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

with col2:
    st.video("https://www.youtube.com/watch?v=K8bVclWiEoM")


st.markdown("### Second Derivative")

col1, col2 = st.columns([4,3])

with col1:
    st.write("The second derivative is the rate at which the slope or first derivative is changing.")
    latex_code = r"""
    \frac{d^2y}{dx^2}
    """
    st.latex(latex_code)

with col2:
    st.video("https://www.youtube.com/watch?v=L9hU4xrhEDs")


st.markdown("#### Differentiation Example with Sympy")

st.write("The Sympy library is used to perform symbolic differentiation which produces as output an exact formula for the derivative.")

expression = "x^2 + 3x + 5"

latex_code = f"""
f(x) = {expression}
"""
st.latex(latex_code)

code_snippet = """
import sympy as sp
import streamlit as st

x = sp.symbols('x')

f = x**2 + 3*x + 5
st.write(f"Function: {f}")

f_prime = sp.diff(f, x)
st.write(f"Derivative: {f_prime}")

f_double_prime = sp.diff(f_prime, x)
st.write("We differentiate twice to get the second-order derivative.")
st.write(f"Second Derivative: {f_double_prime}")
"""

st.code(code_snippet)
exec(code_snippet)

st.write("Note that sp.symbols() tells Sympy to treat x as a mathematical variale or symbol and not as a standard Python variable.")


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
st.write(f"epsilon: {epsilon}")

# Compute the derivative
deriv = approx_fprime(x_value, f, epsilon)

st.write(f"The derivative of f(x) at x={x_value[0]} is approximately: {deriv[0]}")
"""

st.code(code_snippet)
exec(code_snippet)

st.info("""The scipy.optimize.approx_fprime function is used to compute the derivative of a function at a particular point 
    using the finite differences method.
    See https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.approx_fprime.html
    """)


st.markdown("#### The Chain Rule")

col1, col2 = st.columns([4,3])

with col1:
    st.write("The chain rule is used to differentiate composite functions.  It allows you to differentiate a function nested within another function.")
    latex_code = r"""
    y = f(g(x))
    """
    st.latex(latex_code)

    st.write("Example:")
    st.write("Substitute the inside function with u.")
    latex_code = r"""
    y = \sqrt{x^3 + 1} \\
    u = x^3 + 1 \\
    y = \sqrt{u} = u^{1/2}
    """
    st.latex(latex_code)

    st.write("Treat u as a single variable and differentiate.")
    latex_code = r"""
    \frac{dy}{du} = \frac{1}{2}u^{-1/2}
    """
    st.latex(latex_code)

    st.write("Replace u with the inside function.")
    latex_code = r"""
    \frac{dy}{du} = \frac{1}{2}(x^3 + 1)^{-1/2} \\
    = \frac{1}{2\times\sqrt{x^3 + 1}}
    """
    st.latex(latex_code)

    st.write("Multiply the result by the derivative of u.")
    latex_code = r"""
    \frac{du}{dx} = 3x^2 \\
    \frac{dy}{dx} = \frac{dy}{du} \times \frac{du}{dx} \\
    \frac{dy}{dx} = \frac{3x^2}{2\times\sqrt{x^3 + 1}}
    """
    st.latex(latex_code)

    code_snippet = """
from sympy import symbols, diff

x = symbols("x")
y = (x**3 + 1)**(1/2)

# Compute the derivative using chain rule
dy_dx = diff(y, x)

st.write(dy_dx)
    """
    st.code(code_snippet)
    exec(code_snippet)

    st.write("The output from the sympy.diff function is consistent with the workings above but rearranged, e.g. with the 3/2 faction replaced with 1.5 in the numerator.")

with col2:
    st.video("https://www.youtube.com/watch?v=9IAUw5brhf4&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=87&pp=iAQB")


st.markdown("#### Differentiating Exponential Functions")

col1, col2 = st.columns([4,3])

with col1:
    pass

with col2:
    st.video("https://www.youtube.com/watch?v=MTGKaRwVh7M&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=89&pp=iAQB")


st.markdown("#### Differentiating Trigonometric Functions")

col1, col2 = st.columns([4,3])

with col1:
    pass

with col2:
    st.video("https://www.youtube.com/watch?v=f7ZDGojBjvE&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=91&pp=iAQB")


st.markdown("#### Product Rule")

col1, col2 = st.columns([4,3])

with col1:
    pass

with col2:
    st.video("https://www.youtube.com/watch?v=51j5A5JrCwA&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=92&pp=iAQB")


st.markdown("#### Quotient Rule")

col1, col2 = st.columns([4,3])

with col1:
    pass

with col2:
    st.video("https://www.youtube.com/watch?v=Cj9hiHBt1ss&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=94&t=8s&pp=iAQB")


st.markdown("#### Parametric Differentiation")

col1, col2 = st.columns([4,3])

with col1:
    pass

with col2:
    st.video("https://www.youtube.com/watch?v=wFFaBh2jG-8&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=97&pp=iAQB")


st.markdown("#### Implicit Differentiation")

col1, col2 = st.columns([4,3])

with col1:
    pass

with col2:
    st.video("https://www.youtube.com/watch?v=FPFrDxl8GxQ&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=98&pp=iAQB")


st.markdown("#### Solving Differential Equations")

col1, col2 = st.columns([4,3])

with col1:
    pass

with col2:
    st.video("https://www.youtube.com/watch?v=ao9YmyNTLN4&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=112")


st.markdown("#### Partial Derivatives")

col1, col2 = st.columns([4,3])

with col1:
    pass

with col2:
    st.video("https://www.youtube.com/watch?v=AXqhWeUEtQU")