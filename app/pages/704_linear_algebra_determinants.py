import streamlit as st

import utils

st.set_page_config(layout="wide")
st.markdown("### Linear Algebra Determinants")


st.write(
    "The determinant is a **scalar value** that can be computed from the elements of a **square matrix**. It provides important properties of the matrix, such as whether it is **invertible**."
)

st.write("""
Knowing the determinant is important because it reveals whether a system of linear equations has a unique solution and whether transformations preserve or distort space. In quantitative finance, determinants are used in portfolio optimization to assess the covariance matrix's invertibility when computing minimum variance portfolios, and in risk management to detect multicollinearity (when variables are highly correlated with each other) among risk factors which can lead to unstable hedging strategies.
""")

st.write("The determinant of a 2x2 matrix is calculated as follows:")
st.latex(r"M = " + r"""
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix} \\
~ \\
\text{det M} = ad - bc
""")

st.info("""
Where **$$det~M = 0$$**, $$M$$ is a **singular matrix** and is **not** invertible. \r\n
Where **$$det~M \\neq 0$$**, $$M$$ is a **non-singular matrix** and is invertible.
""")


st.markdown("##### Example:")

utils.display_run_python_snippet(code_snippet="""
import streamlit as st
from sympy import Matrix, latex                   

A = Matrix( [ [6, 5], [1, 2] ] )
st.latex(r'A = ' + latex(A))

det_A = A.det()
                                 
st.latex(r'det~A = ' + latex(det_A))                                                
""")

latex_code = r"""
det~A = 6 * 2 - 5 * 1 = 12 - 5 = 7
"""
st.latex(latex_code)

st.info(
    """In general, for an $$n x m$$ matrix, the determinant tells you how the matrix scales n-dimensional volume."""
)

st.info(
    """A positive determinant indicates the transformation preserves orientation (no flipping). 
    \r\nA negative determinant means it reverses orientation (includes a reflection).."""
)
