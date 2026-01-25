import streamlit as st

import utils


st.set_page_config(layout="wide")
st.markdown("### Linear Algebra - Eigenvalues and Eigenvectors")

st.markdown("##### Introduction")

st.write(
    """
An **eigenvector** of a square matrix is a non-zero vector that, when the matrix is multiplied by it, results in a scalar multiple of itself.
The corresponding scalar is called the **eigenvalue**. Mathematically, for a matrix **A**, eigenvector **v**, and eigenvalue **λ** (lambda):
"""
)

st.latex(r"A \mathbf{v} = \lambda \mathbf{v}")

st.write(
    """
This equation means that multiplying matrix **A** by eigenvector **v** only scales the vector by **λ**, without changing its direction.
Eigenvalues and eigenvectors are fundamental in understanding the behavior of linear transformations.
"""
)

st.info(
    """
Applications of eigenvalues and eigenvectors:
- **Principal Component Analysis (PCA)**: Dimensionality reduction in data science and machine learning
- **Stability Analysis**: Determining stability of differential equations and dynamical systems
- **Google's PageRank**: Ranking web pages based on the eigenvector of the web link matrix
- **Quantum Mechanics**: Energy levels correspond to eigenvalues of the Hamiltonian operator
- **Vibration Analysis**: Natural frequencies of mechanical systems
"""
)


st.markdown("##### Finding Eigenvalues")

st.write(
    """
To find eigenvalues, we solve the **characteristic equation**:
"""
)

st.latex(r"\det(A - \lambda I) = 0")

st.write("where **I** is the identity matrix and **det** denotes the determinant.")


st.markdown("##### Example: 2×2 Matrix")

utils.display_run_python_snippet(
    code_snippet="""
import streamlit as st
from sympy import Matrix, latex

# Define a 2x2 matrix
A = Matrix([[4, 2], [1, 3]])
st.latex(r'A = ' + latex(A))

# Calculate eigenvalues
eigenvals = A.eigenvals()
st.write("Eigenvalues:")
for val, multiplicity in eigenvals.items():
    st.latex(r'\lambda = ' + latex(val))
"""
)

st.info(
    """
For the matrix A = [[4, 2], [1, 3]]:
- Characteristic equation: det(A - λI) = (4-λ)(3-λ) - 2×1 = 0
- Expanding: λ² - 7λ + 10 = 0
- Solving: (λ-5)(λ-2) = 0
- Eigenvalues: λ₁ = 5, λ₂ = 2
"""
)


st.markdown("##### Eigenvectors")

st.write(
    """
Once eigenvalues are found, we can compute the corresponding eigenvectors by solving:
"""
)

st.latex(r"(A - \lambda I)\mathbf{v} = \mathbf{0}")

utils.display_run_python_snippet(
    code_snippet="""
import streamlit as st
from sympy import Matrix, latex

# Define the matrix
A = Matrix([[4, 2], [1, 3]])
st.latex(r'A = ' + latex(A))

# Calculate eigenvalues and eigenvectors
eigenvects = A.eigenvects()

st.write("Eigenvalues and their eigenvectors:")
for eigenval, multiplicity, eigenvec_list in eigenvects:
    st.latex(r'\lambda = ' + latex(eigenval))
    st.write(f"Multiplicity: {multiplicity}")
    for vec in eigenvec_list:
        st.latex(r'\mathbf{v} = ' + latex(vec))
"""
)

st.info(
    """
Each eigenvalue has a corresponding eigenvector:
- For λ₁ = 5: eigenvector v₁ = [2, 1]
- For λ₂ = 2: eigenvector v₂ = [1, -1]

You can verify: A × v₁ = 5 × v₁ and A × v₂ = 2 × v₂
"""
)


st.markdown("##### Verification Example")

st.write("Let's verify that Av = λv for one of the eigenvalue-eigenvector pairs:")

utils.display_run_python_snippet(
    code_snippet="""
import streamlit as st
from sympy import Matrix, latex

# Define the matrix
A = Matrix([[4, 2], [1, 3]])

# Use eigenvalue λ = 5 with eigenvector v = [2, 1]
eigenval = 5
eigenvec = Matrix([2, 1])

st.latex(r'A = ' + latex(A))
st.latex(r'\lambda = ' + latex(eigenval))
st.latex(r'\mathbf{v} = ' + latex(eigenvec))

# Left side: A × v
Av = A * eigenvec
st.latex(r'A\mathbf{v} = ' + latex(Av))

# Right side: λ × v
lambda_v = eigenval * eigenvec
st.latex(r'\lambda\mathbf{v} = ' + latex(lambda_v))

st.write("Verification: A𝐯 = λ𝐯 ✓")
"""
)


st.markdown("##### Eigenvalues with NumPy")

st.write(
    "NumPy provides efficient functions for computing eigenvalues and eigenvectors:"
)

utils.display_run_python_snippet(
    code_snippet="""
import streamlit as st
from sympy import Matrix, latex
import numpy as np

# Define the matrix
A = np.array([[4, 2], [1, 3]])

# Calculate eigenvalues and eigenvectors
eigenvals, eigenvecs = np.linalg.eig(A)

st.write("Eigenvalues:")
st.write(eigenvals)

st.write("Eigenvectors (as columns):")
st.write(eigenvecs)

st.write("Eigenvalues as LaTeX:")
st.latex(r'\lambda_1 = ' + str(eigenvals[0]))
st.latex(r'\lambda_2 = ' + str(eigenvals[1]))
"""
)

st.info(
    """
NumPy's `np.linalg.eig()` returns:
- A 1D array of eigenvalues
- A 2D array where each column is an eigenvector corresponding to the eigenvalue at the same index

This is computationally efficient for large matrices and numerical applications.
"""
)


st.markdown("##### Properties of Eigenvalues")

st.info(
    """
Important properties:
- The **sum of eigenvalues** equals the **trace** of the matrix (sum of diagonal elements)
- The **product of eigenvalues** equals the **determinant** of the matrix
- Eigenvalues can be real or complex numbers, even for real matrices
- A matrix is invertible if and only if all its eigenvalues are non-zero
- Symmetric matrices always have real eigenvalues and orthogonal eigenvectors
"""
)
