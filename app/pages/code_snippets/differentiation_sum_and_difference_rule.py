"""
SymPy snippet for demonstrating the Sum and Difference Rules.

This script performs symbolic differentiation using SymPy, evaluates the
derivative at a specific point, and plots the function and its derivative
using Matplotlib.
"""

import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols("x")

# Sum rule example: f(x) = x^3 + 5x^2
f_sum = x**3 + 5 * x**2
f_sum_derivative = sp.diff(f_sum, x)

st.write("**Sum rule example:**")
st.write(f"$$f(x) = {sp.latex(f_sum)}$$")
st.write(f"$$f'(x) = {sp.latex(f_sum_derivative)}$$")

# Difference rule example: g(x) = 4x^3 - 2x
f_diff = 4 * x**3 - 2 * x
f_diff_derivative = sp.diff(f_diff, x)

st.write("**Difference rule example:**")
st.write(f"$$g(x) = {sp.latex(f_diff)}$$")
st.write(f"$$g'(x) = {sp.latex(f_diff_derivative)}$$")

# Evaluate at a specific point
x_point = 1.0
g_at_point = float(f_diff.subs(x, x_point))
g_prime_at_point = float(f_diff_derivative.subs(x, x_point))

st.write(
    f"At $$x = {x_point}$$: $$g(x) = {g_at_point}$$, $$g'(x) = {g_prime_at_point}$$"
)

# Plot the function and its derivative with highlighted point
f_np = sp.lambdify(x, f_diff, "numpy")
f_deriv_np = sp.lambdify(x, f_diff_derivative, "numpy")

x_vals = np.linspace(-2, 2, 200)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x_vals, f_np(x_vals), label=f"$g(x) = {sp.latex(f_diff)}$")
ax.plot(x_vals, f_deriv_np(x_vals), label=f"$g'(x) = {sp.latex(f_diff_derivative)}$")
ax.plot(x_point, g_at_point, "ro", markersize=8, label=f"$g({x_point}) = {g_at_point}$")
ax.plot(
    x_point,
    g_prime_at_point,
    "rs",
    markersize=8,
    label=f"$g'({x_point}) = {g_prime_at_point}$",
)
ax.axhline(y=0, color="grey", linewidth=0.5)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(f"Difference rule: $g(x) = {sp.latex(f_diff)}$ and its derivative")
ax.legend()
ax.grid(True, alpha=0.3)
st.pyplot(fig)

st.info(
    "The **blue curve** is the original function and the **orange curve** is its derivative. "
    "The derivative tells you the **slope** of the blue curve at every point. "
    "What matters is the **sign** of the orange curve, not whether it is rising or falling:\n\n"
    "- Where the orange curve is **above zero**, the blue curve is **rising**\n"
    "- Where the orange curve is **below zero**, the blue curve is **falling**\n"
    "- Where the orange curve **crosses zero**, the blue curve has a "
    "**turning point** (a local maximum or minimum)\n\n"
    "For example, the orange curve can be falling yet still positive — this simply means "
    "the blue curve is still rising, but less steeply."
)
