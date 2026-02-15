import streamlit as st
import pathlib

st.set_page_config(page_title="Maths Python", page_icon="📐", layout="wide")
st.header("Snippets of Python and LaTeX Code for Maths Operations")

st.sidebar.title("📐 Maths Python")
st.sidebar.info(
    "Interactive Python code snippets for mathematics and statistics, "
    "covering calculus, integration, linear algebra, probability, and algebra "
    "with worked examples and visualisations."
)


st.write(
    "Source code for this application can be found at https://github.com/koysor/maths-python ."
)


col1, col2 = st.columns(2)

with col1:
    st.image("app/assets/images/maths_python", caption="Maths Python App", width=450)

with col2:
    st.write(f"Current working directory: {pathlib.Path().cwd()}")
