import streamlit as st

import utils

st.set_page_config(
    page_title="Linear Algebra - Identity Matrices", page_icon="📐", layout="wide"
)
st.header("Linear Algebra - Identity Matrices")

st.markdown("##### Introduction")

st.write("""
An identity matrix is a special square matrix that acts as the multiplicative identity in matrix algebra,
similar to how the number 1 works in regular arithmetic. It is denoted as **I** or **Iₙ** for an n×n matrix.
""")

st.write("""
The identity matrix has **1s on the main diagonal** (top-left to bottom-right) and **0s everywhere else**.
When any matrix is multiplied by an identity matrix of compatible dimensions, the original matrix remains unchanged: **AI = IA = A**.
""")

st.info("""
The identity matrix is crucial for:
- Matrix inversion (since A × A⁻¹ = I)
- Solving systems of linear equations
- Understanding linear transformations that preserve vectors
- Serving as a starting point for iterative algorithms
""")


st.markdown("##### Identity Matrix Examples")

st.write("Here are identity matrices of different sizes:")

st.latex(r"""
I_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}, \quad
I_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}, \quad
I_4 = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}
""")


st.markdown("##### Creating Identity Matrices with SymPy")

utils.display_run_python_snippet(code_snippet="""
import streamlit as st
from sympy import Matrix, eye, latex

# Create a 2x2 identity matrix
I2 = eye(2)
st.latex(r'I_2 = ' + latex(I2))

# Create a 3x3 identity matrix
I3 = eye(3)
st.latex(r'I_3 = ' + latex(I3))

# Create a 4x4 identity matrix
I4 = eye(4)
st.latex(r'I_4 = ' + latex(I4))
""")


st.markdown("##### Verifying the Identity Property")

st.write(
    "Let's verify that multiplying any matrix by an identity matrix returns the original matrix:"
)

utils.display_run_python_snippet(code_snippet="""
import streamlit as st
from sympy import Matrix, eye, latex

# Define a matrix A
A = Matrix([[3, 7], [2, 5]])
st.latex(r'A = ' + latex(A))

# Create 2x2 identity matrix
I = eye(2)
st.latex(r'I = ' + latex(I))

# Multiply A × I
AI = A * I
st.latex(r'A \cdot I = ' + latex(AI))

# Multiply I × A
IA = I * A
st.latex(r'I \cdot A = ' + latex(IA))
""")

st.info("""
As demonstrated:
- A × I = A (original matrix unchanged)
- I × A = A (order doesn't matter with identity)
- This confirms the identity property: **AI = IA = A**
""")


st.markdown("##### Identity Matrices with NumPy")

utils.display_run_python_snippet(code_snippet="""
import streamlit as st
from sympy import latex, Matrix
import numpy as np

# Create a 3x3 identity matrix using NumPy
I_np = np.eye(3)
st.write("NumPy identity matrix (3×3):")
st.latex(latex(Matrix(I_np)))

# Verify with matrix multiplication
A = np.array([[2, 3, 1], [4, 5, 6], [7, 8, 9]])
result = np.dot(A, I_np)

st.write("Original matrix A:")
st.latex(latex(Matrix(A)))

st.write("A × I:")
st.latex(latex(Matrix(result)))
""")

st.info("""
NumPy's `np.eye(n)` function creates an n×n identity matrix efficiently.
This is particularly useful for numerical computations and large-scale linear algebra operations.
""")
