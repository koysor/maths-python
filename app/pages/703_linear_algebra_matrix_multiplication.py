import streamlit as st

import utils


st.set_page_config(layout="wide")
st.markdown("### Linear Algebra Matrix Multiplication")


st.markdown("##### Matrix Multiplication")

st.write(
    "Matrices can be multiplied together if the **number of columns** in the first matrix is equal to the **number of rows** in the second matrix."
)

st.write(
    "The **product matrix** will have the same **number of rows** as the first matrix and the same **number of columns** as the second matrix."
)

st.info(
    body="""**$$AB = C$$** \r\n
- Where **A** is matrix with size **n x m** \r\n
- Where **B** is a matrixwith size **m x k** \r\n
- Then **C** is a matrix with size **n x k**"""
)

st.write(
    "The order in which the matrices are multiplied matters. In general, **$$AB \\neq BA$$**."
)
st.write(
    "The product of two matrices is calculated by taking the dot product of the **rows of the first matrix** with the **columns of the second matrix**."
)


st.markdown("##### Example of Matrix Multiplication with SymPy")

utils.display_run_python_snippet(
    code_snippet="""
import streamlit as st
from sympy import Matrix, latex                   

A = Matrix( [ [5, -1, 2], [8, 3, -4] ] )
st.latex(r'A = ' + latex(A))

B = Matrix( [ [2, 2], [9, -3], [7, 4] ] )
st.latex(r'B = ' + latex(B))
                                 
C = A * B
st.latex(r'C = A * B = ' + latex(C))                                                
"""
)

st.write(
    "A is a **2 x 3** matrix and B is a **3 x 2** matrix, therefore the product C is a **2 x 2** matrix."
)

st.info(
    """**Top left cell of C**: \r\n
- 5 * 2 + (-1) * 9 + 2 * 7 = 10 - 9 + 14 = 15 \r\n
        """
)

st.info(
    """**Top right cell of C**: \r\n
- 5 * 2 + (-1) * (-3) + 2 * 4 = 10 + 3 + 8 = 21 \r\n
        """
)

st.info(
    """**Bottom left cell of C**: \r\n
- 8 * 2 + 3 * 9 + (-4) * 7 = 16 + 27 - 28 = 15 \r\n
        """
)

st.info(
    """**Bottom right cell of C**: \r\n
- 8 * 2 + 3 * (-3) + (-4) * 4 = 16 - 9 - 16 = -9 \r\n
        """
)


st.markdown("##### Example of Matrix Multiplication with NumPy")

utils.display_run_python_snippet(
    code_snippet="""
import streamlit as st
from sympy import latex
import numpy as np                  

A = [[5, -1, 2], [8, 3, -4]]
B = [[2, 2], [9, -3], [7, 4]]
                                 
C = np.dot(A, B)
st.write(str(type(C)))
st.latex(r'C = A * B = ' + latex(C))                                           
"""
)


