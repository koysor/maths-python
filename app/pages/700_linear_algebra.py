import streamlit as st

st.set_page_config(page_title="Linear Algebra", page_icon="📐", layout="wide")
st.header("Linear Algebra")

st.write(
    "Linear algebra is the branch of mathematics concerning linear equations, linear functions, and their representations through matrices and vector spaces."
)

st.header("Vectors")
st.write(
    "A vector is a quantity that has both magnitude and direction. It can be represented as an ordered list of numbers, which are called components."
)

st.write("A vector in 2D space can be represented as:")
latex_code = r"""
\vec{v} = 
\begin{bmatrix}
    x \\
    y \\
    z
\end{bmatrix}
"""
st.code(latex_code, language="latex")
st.latex(latex_code)

code_snippet = """
import sympy as sp
import streamlit as st

# Define symbols
x, y, z = sp.symbols('x y z')

# Create a column vector
v = sp.Matrix([x, y, z])

st.write(v)
"""
st.code(code_snippet, language="python")
exec(code_snippet)


st.header("Matrices")

st.write(
    "A matrix can be represented as a rectangular array of numbers, symbols, or expressions, arranged in rows and columns."
)
latex_code = r"""
M =
\begin{bmatrix}
    a_{11} & a_{12} \\
    a_{21} & a_{22}
\end{bmatrix}
"""
st.code(latex_code, language="latex")
st.latex(latex_code)
st.write("A matrix with m rows and n columns is called an m x n matrix.")
st.write("For example, a 2x3 matrix has 2 rows and 3 columns:")
latex_code = r"""
A =
\begin{bmatrix}
    1 & 2 & 3 \\
    4 & 5 & 6
\end{bmatrix}
"""
st.code(latex_code, language="latex")
st.latex(latex_code)
st.write("A matrix can also be represented as a list of lists in Python:")
code_snippet = """
import streamlit as st
import numpy as np
from sympy import Matrix, latex

A = np.array([[1, 2, 3], [4, 5, 6]])
st.latex(latex(Matrix(A)))   
"""
st.code(code_snippet, language="python")
exec(code_snippet)
st.write("This creates a 2x3 matrix with the specified values.")
