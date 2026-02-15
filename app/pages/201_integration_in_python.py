import streamlit as st

st.set_page_config(
    page_title="Integration Example with SymPy", page_icon="📐", layout="wide"
)


st.header("Integration Example with SymPy")


st.write("To calculate the definite integral:")

latex_code = """
\int_{2}^{5} (6x + 1) \,dx
"""
st.latex(latex_code)

st.write("The SymPy library in Python can be used...")

with open("app/pages/code_snippets/integration_sympy.py", "r") as f:
    code_snippet = f.read()

st.code(code_snippet)
exec(code_snippet)


st.header("Integration Example with SciPy")

with open("app/pages/code_snippets/integration_scipy.py", "r") as f:
    code_snippet = f.read()

st.code(code_snippet)
exec(code_snippet)
