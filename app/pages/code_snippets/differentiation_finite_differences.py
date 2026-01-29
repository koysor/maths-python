import streamlit as st
from app.maths_logic import numerical_derivative


def f(x):
    return x**2 + 3 * x + 5


# Choose a point to evaluate the derivative
x_value = 1.0
derivative_at_x = numerical_derivative(f, x_value)

st.write(
    f"The derivative of $$f(x)$$ at x={x_value} is approximately: $${derivative_at_x}$$"
)
