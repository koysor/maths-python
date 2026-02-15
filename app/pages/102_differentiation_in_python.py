import streamlit as st

st.set_page_config(
    page_title="Differentiation Examples in Python", page_icon="📐", layout="wide"
)
st.header("Differentiation Examples in Python")


st.markdown("#### Differentiation Example with SymPy")

st.write(
    "The SymPy library is used to perform symbolic differentiation which produces as output an exact formula for the derivative."
)

expression = "x^2 + 3x + 5"

latex_code = f"""
f(x) = {expression}
"""
st.latex(latex_code)


with open("app/pages/code_snippets/differentiation_sympy.py", "r") as f:
    code_snippet = f.read()

st.code(code_snippet)
exec(code_snippet)

st.write(
    "Note that sp.symbols() tells Sympy to treat x as a mathematical variable or symbol and not as a standard Python variable."
)


st.markdown("#### Differentiation Example Using SciPy")

with open("app/pages/code_snippets/differentiation_scipy.py", "r") as f:
    code_snippet = f.read()  # Read the content of the file

st.code(code_snippet)
exec(code_snippet)

st.info(
    """The scipy.optimize.approx_fprime function is used to compute the derivative of a function at a particular point 
    using the finite differences method.
    See https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.approx_fprime.html
    """
)
