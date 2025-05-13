import streamlit as st
import sympy as sp


x = sp.symbols("x")

# Set the exponent
n = 2

# Define the function
f = x**n

# Differentiate
f_derivative = sp.diff(f, x)

st.write(f"The derivative of $$x^{n}$$ is:")
st.write(f"$$\\frac{{d}}{{dx}}(x^{n}) = {n} \\cdot x^{{{n}-1}}$$")
st.write(f_derivative)
