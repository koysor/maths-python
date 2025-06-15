import sympy as sp
import streamlit as st


# Define the variables
x, y = sp.symbols("x y")

# Define the function
f = x**2 + 3 * x * y**2
st.write("Function:", f)

# Compute the partial derivatives
df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)

st.write(
    r"Partial derivative with respect to $$x$$, $$\frac{\partial f}{\partial x} $$:",
    df_dx,
)
st.write(
    r"Partial derivative with respect to $$y$$, $$\frac{\partial f}{\partial y} $$:",
    df_dy,
)
