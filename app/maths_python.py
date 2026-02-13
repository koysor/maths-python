import streamlit as st
import pathlib

st.set_page_config(layout="wide")
st.markdown("### Snippets of Python and LaTex Code for Maths Operations")


st.write(
    "Source code for this application can be found at https://github.com/koysor/maths-python ."
)


col1, col2 = st.columns(2)

with col1:
    st.image("app/assets/images/maths_python", caption="Maths Python App", width=450)

with col2:
    st.write(f"Current working directory: {pathlib.Path().cwd()}")
