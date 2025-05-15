import streamlit as st


def f(x):
    return x**2 + 3 * x + 5


def numerical_derivative(func, x, h=1e-5):
    return (func(x + h) - func(x - h)) / (2 * h)


# Choose a point to evaluate the derivative
x_value = 1.0
derivative_at_x = numerical_derivative(f, x_value)

st.write(
    f"The derivative of $$f(x)$$ at x={x_value} is approximately: $${derivative_at_x}$$"
)
