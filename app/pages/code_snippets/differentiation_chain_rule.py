import streamlit as st
from sympy import symbols, diff


x = symbols("x")
y = (x**3 + 1)**(1/2)

# Compute the derivative using chain rule
dy_dx = diff(y, x)

st.write(dy_dx)