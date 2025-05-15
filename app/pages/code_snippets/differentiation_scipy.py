import streamlit as st
import numpy as np
from scipy.optimize import approx_fprime


def f(x):
    return x[0] ** 2 + 3 * x[0] + 5  # Function expects an array input


x_value = np.array([1.0])
epsilon = np.sqrt(
    np.finfo(float).eps
)  # Optimal step size for numerical differentiation
st.write(f"epsilon: $${epsilon}$$")

# Compute the derivative
deriv = approx_fprime(x_value, f, epsilon)

st.write(
    f"The derivative of $$f(x)$$ at $$x={x_value[0]}$$ is approximately: $${deriv[0]}$$"
)
