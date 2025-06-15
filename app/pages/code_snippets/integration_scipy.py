import streamlit as st
from scipy.integrate import quad


# Define the function
f = lambda x: 6 * x + 1

# Define limits of integration
a = 2  # lower limit
b = 5  # upper limit

# Compute the integral
result, error = quad(f, a, b)

st.write("Integral:", result)

st.info(
    "SciPy's `quad` function computes the definite integral of a function over a specified interval. The result is the area under the curve of the function between the limits of integration. \
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html"
)
