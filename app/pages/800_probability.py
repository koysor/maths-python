import streamlit as st

st.set_page_config(layout="wide")
st.markdown("### Probability")


st.markdown("##### Notation")

st.write("To denote the expected value of a random variable $$X$$:")
latex_code = r"""
    \mathbb{E}[X] = \int_{-\infty}^{\infty} x f(x) dx
"""
st.code(latex_code, language="latex")
st.latex(latex_code)
