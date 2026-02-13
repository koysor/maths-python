import streamlit as st

import utils

st.set_page_config(layout="wide")
st.markdown("### Linear Algebra - Matrix Inversion")

st.markdown("##### Introduction")

st.write("""
Matrix inversion is the process of finding a matrix that, when multiplied with the original matrix, produces the identity matrix.
The inverse of matrix **A** is denoted as **A⁻¹**, and it satisfies the equation **AA⁻¹ = A⁻¹A = I**, where **I** is the identity matrix.
""")

st.write("""
Not all matrices have an inverse. A matrix is invertible (or non-singular) only if its determinant is non-zero.
Matrix inversion is crucial for solving systems of linear equations, computing least squares solutions in regression analysis,
and performing transformations in computer graphics and robotics.
""")

st.info("""
Only square matrices can have an inverse, and the inverse exists only when **det(A) ≠ 0**.
""")


st.markdown("##### Example: 2x2 Matrix Inversion")

st.write("For a 2x2 matrix, the inverse can be calculated using the formula:")

st.latex(r"""
\text{If } A = \begin{bmatrix} a & b \\ c & d \end{bmatrix},
\text{ then } A^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}
""")

utils.display_run_python_snippet(code_snippet="""
import streamlit as st
from sympy import Matrix, latex

A = Matrix([[4, 7], [2, 6]])
st.latex(r'A = ' + latex(A))

# Calculate determinant
det_A = A.det()
st.latex(r'det(A) = ' + latex(det_A))

# Calculate inverse
A_inv = A.inv()
st.latex(r'A^{-1} = ' + latex(A_inv))

# Verify: A * A_inv should equal identity matrix
I = A * A_inv
st.latex(r'A \cdot A^{-1} = ' + latex(I))
""")

st.info("""
Calculation steps:
- Determinant: det(A) = 4×6 - 7×2 = 24 - 14 = 10
- Since det(A) = 10 ≠ 0, the matrix is invertible
- Apply formula: A⁻¹ = (1/10) × [[6, -7], [-2, 4]]
- Verification: A × A⁻¹ = I (identity matrix)
""")
