import streamlit as st
import sympy as sp

x = sp.symbols("x")

# Define the function
f = sp.ln(x)

# Differentiate
f_derivative = sp.diff(f, x)

st.write("The derivative of $$ln(x)$$ is:")
st.write(f_derivative)
