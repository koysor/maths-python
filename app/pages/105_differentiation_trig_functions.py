import streamlit as st

st.set_page_config(layout="wide")
st.markdown("### Differentiating Trigonometric Functions:")

col1, col2 = st.columns([4, 3])

with col1:

    trig_function = st.selectbox(
        label="Trigonometric Function:",
        options=["sin", "cos", "tan", "csc", "sec", "cot"],
    )

    code_snippet = f"""
import streamlit as st
import sympy as sp

x = sp.symbols('x')

# Define the function
f = sp.{trig_function}(x)

# Differentiate
f_derivative = sp.diff(f, x)
st.write('The derivative of $${trig_function}(x)$$ is:')
st.write(f_derivative)
"""

    st.code(code_snippet)
    exec(code_snippet)


with col2:
    st.video(
        "https://www.youtube.com/watch?v=f7ZDGojBjvE&list=PLHnDkwDE03A88Tj3mrg_LRpUWqyVipHkM&index=91&pp=iAQB"
    )
