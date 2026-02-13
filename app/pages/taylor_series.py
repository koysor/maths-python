import streamlit as st

st.set_page_config(layout="wide")
st.markdown("### Taylor Series")

st.write(
    "The Taylor Series allows us to represent a function as an infinite sum of terms calculated from the values of its derivatives at a single point."
)
st.write(
    "By truncating the series after a certain number of terms, we can approximate the function with a polynomial."
)
st.write("The Taylor Series is given by the formula:")
latex_code = r"""
\sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x - a)^n
"""
st.code(latex_code, language="latex")
st.latex(latex_code)
st.write("Where:")
st.write(
    r"- $$f^{(n)}(a)$$ is the nth derivative of the function evaluated at the point $$(a)$$."
)
st.write("- \(n!\) is the factorial of \(n\).")
st.write("- \(x\) is the variable.")
st.write("- \(a\) is the point around which the series is expanded.")
st.write(
    "The Taylor Series can be used to approximate functions that are difficult to compute directly, such as trigonometric, exponential, and logarithmic functions."
)
st.write(
    "The more terms we include in the series, the more accurate the approximation becomes."
)
st.write(
    "The Taylor Series is particularly useful in calculus, physics, and engineering, where it is often used to simplify complex calculations."
)

code_snippet = """
import streamlit as st
import sympy as sp

x = sp.symbols('x')
f = sp.sin(x)
taylor_series = f.series(x, 0, 5)

st.write(taylor_series)
"""
st.code(code_snippet, language="python")
exec(code_snippet)
st.write(
    "In this example, we use the SymPy library to compute the Taylor Series of the sine function around the point 0 up to the 5th term."
)
st.write("The output will show the Taylor Series expansion of the sine function.")
st.write(
    "You can modify the function and the point of expansion to compute the Taylor Series for other functions."
)
st.write(
    "The Taylor Series is a powerful tool in mathematics and has many applications in various fields."
)
