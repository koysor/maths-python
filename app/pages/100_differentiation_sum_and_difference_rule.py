"""
Streamlit page for demonstrating the Differentiation Sum and Difference Rules.

This page explains how to differentiate functions composed of multiple terms
added or subtracted together. It includes:
- Mathematical definitions of the sum and difference rules.
- Worked examples showing the rules in practice.
- Interactive calculation of gradients at specific points.
- Integration with SymPy for symbolic computation and visualization.
"""

import streamlit as st

st.set_page_config(layout="wide")
st.markdown("### Differentiation Sum & Difference Rule")

st.write("""The sum and difference rules allow you to differentiate functions that are
    composed of multiple terms added or subtracted together. Rather than treating the
    entire expression at once, you can differentiate each term individually.""")

st.info("**N.B.** Differentiate each term separately.")


st.markdown("#### Sum Rule")

st.write("If $$f(x)$$ and $$g(x)$$ are both differentiable, then:")

st.latex(r"\frac{d}{dx} \left[ f(x) + g(x) \right] = f'(x) + g'(x)")


st.markdown("#### Difference Rule")

st.write("Similarly, for the difference of two functions:")

st.latex(r"\frac{d}{dx} \left[ f(x) - g(x) \right] = f'(x) - g'(x)")


st.markdown("#### Worked Example — Sum Rule")

st.write("Differentiate $$f(x) = x^3 + 5x^2$$")

st.write("Apply the power rule to each term individually:")

st.latex(r"\frac{d}{dx}(x^3) = 3x^2")

st.latex(r"\frac{d}{dx}(5x^2) = 10x")

st.write("Combining using the sum rule:")

st.latex(r"f'(x) = 3x^2 + 10x")


st.markdown("#### Worked Example — Difference Rule")

st.write("Differentiate $$g(x) = 4x^3 - 2x$$")

st.write("Apply the power rule to each term individually:")

st.latex(r"\frac{d}{dx}(4x^3) = 12x^2")

st.latex(r"\frac{d}{dx}(2x) = 2")

st.write("Combining using the difference rule:")

st.latex(r"g'(x) = 12x^2 - 2")


st.markdown("#### Gradient at a Point")

st.write(
    "To find the gradient of the curve at a particular point, substitute the "
    "$$x$$-value into the derivative."
)


def g_func(x):
    """
    Calculate the value of the example function g(x) = 4x^3 - 2x.

    Args:
        x (float): The x-value at which to evaluate the function.

    Returns:
        float: The value of the function at x.
    """
    return 4 * x**3 - 2 * x


def g_prime_func(x):
    """
    Calculate the value of the derivative g'(x) = 12x^2 - 2.

    Args:
        x (float): The x-value at which to evaluate the derivative.

    Returns:
        float: The value of the derivative at x.
    """
    return 12 * x**2 - 2


x_val = st.number_input(
    "Enter a value for x:",
    value=1.0,
    min_value=-2.0,
    max_value=2.0,
    step=0.5,
    format="%.1f",
)

g_val = g_func(x_val)
g_prime_val = g_prime_func(x_val)

st.write(f"For $$g(x) = 4x^3 - 2x$$ at $$x = {x_val}$$:")

st.latex(rf"g({x_val}) = 4({x_val})^3 - 2({x_val}) = {g_val}")
st.latex(rf"g'({x_val}) = 12({x_val})^2 - 2 = {g_prime_val}")

st.write(f"So the gradient at $$x = {x_val}$$ is **{g_prime_val}**.")


st.markdown("#### SymPy Example")

with open(
    "app/pages/code_snippets/differentiation_sum_and_difference_rule.py", "r"
) as f:
    code_snippet = f.read()

code_snippet = code_snippet.replace("x_point = 1.0", f"x_point = {x_val}")

st.code(code_snippet)
exec(code_snippet)
