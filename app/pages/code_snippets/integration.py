import streamlit as st
from sympy import symbols, integrate

x = symbols("x")

f = 6*x + 1

# Calculate the definite integral from 2 to 5
st.write(integrate(f, (x, 2, 5)))