import sympy as sp
import streamlit as st

x = sp.symbols("x")

f = x**2 + 3 * x + 5
st.write(f"Function: $${f}$$")

f_prime = sp.diff(f, x)
st.write(f"Derivative: $${f_prime}$$")

f_double_prime = sp.diff(f_prime, x)
st.write("We differentiate twice to get the second-order derivative.")
st.write(f"Second Derivative: $${f_double_prime}$$")
