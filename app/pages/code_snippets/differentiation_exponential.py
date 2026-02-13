import streamlit as st
import sympy as sp

x = sp.symbols("x")

# Define the function
f = sp.exp(x)

# Differentiate
f_derivative = sp.diff(f, x)

st.write("The derivative of $$e^x$$ is:")
st.write(f_derivative)
