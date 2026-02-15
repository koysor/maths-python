import streamlit as st
import utils

st.set_page_config(
    page_title="Linear Algebra Matrix Operations", page_icon="📐", layout="wide"
)
st.header("Linear Algebra Matrix Operations")


st.markdown("##### Matrix Addition")


utils.display_run_python_snippet(code_snippet="""
import streamlit as st
from sympy import Matrix, latex
import numpy as np                        

A = Matrix([[2, -1], [0, 3]])
st.latex(r'A = ' + latex(A))

B = Matrix([[-1, 4], [5, 3]])
st.latex(r'B = ' + latex(B))
                                 
C = A + B
st.latex(r'C = A + B = ' + latex(C))

C_np = np.array(C).astype(np.float64)
st.write("C as numpy array:")
st.latex(latex(Matrix(C_np)))                                                  
""")

st.write(
    "It may be useful to convert the result to a NumPy array for further processing as NumPy offers superior performance."
)

st.info("""
Top row: 
- 2 + (-1) = 1
- -1 + 4 = 3
\rBottom row:
- 0 + 5 = 5 
- 3 + 3 = 6   
""")


st.markdown("##### Matrix Subtraction")


utils.display_run_python_snippet(code_snippet="""
import streamlit as st
from sympy import Matrix, latex
import numpy as np                        

A = Matrix([[1, -3, 4], [2, 1, 1]])
st.latex(r'A = ' + latex(A))

B = Matrix([[0, 2, 1], [5, 2, 3]])
st.latex(r'B = ' + latex(B))
                                 
C = A - B
st.latex(r'C = A - B = ' + latex(C))                                                
""")

st.info(("You can only add or subtract matrices of the same size. "))


st.markdown("##### Multiply a Matrix by a Scalar")

utils.display_run_python_snippet(code_snippet="""
import streamlit as st
from sympy import Matrix, latex
import numpy as np

A = Matrix([[1, 2], [-1, 0]])
st.latex(r'A = ' + latex(A))

C = 2*A
st.latex(r'C = 2A = ' + latex(C))
""")

st.info("""
Multiply each element by the scalar:
- Top row: 2×1 = 2, 2×2 = 4
- Bottom row: 2×(-1) = -2, 2×0 = 0
""")


st.markdown("##### Multiply a Matrix by a Scalar (0.5)")

utils.display_run_python_snippet(code_snippet="""
import streamlit as st
from sympy import Matrix, latex
import numpy as np

A = Matrix([[4, 6], [8, 10]])
st.latex(r'A = ' + latex(A))

C = 0.5*A
st.latex(r'C = 0.5A = ' + latex(C))
""")

st.info("""
Multiply each element by 0.5:
- Top row: 0.5×4 = 2, 0.5×6 = 3
- Bottom row: 0.5×8 = 4, 0.5×10 = 5
""")
