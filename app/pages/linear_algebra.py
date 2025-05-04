import streamlit as st

st.set_page_config(layout="wide")
st.markdown("### Linear Algebra")

latex_code = r"""
A = \begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}, \quad
\vec{b} = \begin{bmatrix}
5 \\
6
\end{bmatrix}

"""
st.code(latex_code, language='latex')
st.latex(latex_code)