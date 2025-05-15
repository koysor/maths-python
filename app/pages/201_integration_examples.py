import streamlit as st


st.set_page_config(layout="wide")
st.markdown("### Integration Example with SymPy")


st.write("To calculate the definite integral:")

latex_code = """
\int_{2}^{5} (6x + 1) \,dx
"""
st.latex(latex_code)

st.write("The SymPy library in Python can be used...")

code_snippet = """
from sympy import symbols, integrate

x = symbols("x")

f = 6*x + 1

# Calculate the definite integral from 2 to 5
st.write(integrate(f, (x, 2, 5)))
"""

st.code(code_snippet)
exec(code_snippet)
