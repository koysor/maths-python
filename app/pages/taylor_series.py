import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

st.set_page_config(page_title="Taylor Series", page_icon="📐", layout="wide")
st.header("Taylor Series")

col_prose, col_snippet = st.columns(2)

with col_prose:
    st.write(
        "The Taylor Series allows us to represent a function as an infinite sum of terms "
        "calculated from the values of its derivatives at a single point."
    )
    st.write(
        "By truncating the series after a certain number of terms, we can approximate the "
        "function with a polynomial."
    )
    st.write("The Taylor Series is given by the formula:")
    st.latex(r"\sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x - a)^n")
    st.write("Where:")
    st.write(
        r"- $f^{(n)}(a)$ is the nth derivative of the function evaluated at the point $a$."
    )
    st.write(r"- $n!$ is the factorial of $n$.")
    st.write(r"- $x$ is the variable.")
    st.write(r"- $a$ is the point around which the series is expanded.")
    st.info(
        "**What does 'at the point $a$' mean?**\n\n"
        "The series is built entirely from the function's value and its derivatives evaluated "
        "at $x = a$. Knowing $f(a)$, $f'(a)$, $f''(a)$, … is enough to reconstruct the "
        "function's shape nearby — the first term captures the value, the second the slope, "
        "the third the curvature, and so on.\n\n"
        "Expanding around $a = 0$ (a **Maclaurin series**) is the most common choice and "
        "keeps the algebra clean since $(x - 0)^n = x^n$. But any point can be used — "
        r"for example, $\ln(x)$ must be expanded around $a > 0$ since $\ln(0)$ is undefined. "
        "The approximation is always most accurate close to $a$."
    )
    st.write(
        "The Taylor Series can be used to approximate functions that are difficult to compute "
        "directly, such as trigonometric, exponential, and logarithmic functions."
    )
    st.write(
        "The more terms we include in the series, the more accurate the approximation becomes."
    )
    st.write(
        "The Taylor Series is particularly useful in calculus, physics, and engineering, "
        "where it is often used to simplify complex calculations."
    )

with col_snippet:
    code_snippet = """\
import sympy as sp

x = sp.symbols('x')
f = sp.sin(x)
# .series(variable, expansion point, number of terms)
taylor_series = f.series(x, 0, 5)

st.write(taylor_series)
"""
    st.code(code_snippet, language="python")
    exec(code_snippet)  # noqa: S102
    st.write(
        "In this example, we use SymPy to compute the Taylor Series of the sine "
        "function around the point 0 up to the 5th term."
    )
    st.write(
        "You can modify the function and the point of expansion to compute the Taylor Series "
        "for other functions."
    )

# ---------------------------------------------------------------------------
# Interactive Approximation
# ---------------------------------------------------------------------------

st.divider()
st.header("Interactive Approximation")

# Per-function data tables — all configuration lives here, not scattered below.
x = sp.Symbol("x")

FUNC_SYMS = {
    "sin(x)": sp.sin(x),
    "cos(x)": sp.cos(x),
    "exp(x)": sp.exp(x),
    "ln(1+x)": sp.ln(1 + x),
}

# String used inside the displayed code block for each function.
FUNC_CODE_STR = {
    "sin(x)": "sp.sin(x)",
    "cos(x)": "sp.cos(x)",
    "exp(x)": "sp.exp(x)",
    "ln(1+x)": "sp.ln(1 + x)",
}

# x-axis bounds — ln(1+x) is restricted to its radius of convergence.
X_BOUNDS = {
    "sin(x)": (-2.0, 2.0),
    "cos(x)": (-2.0, 2.0),
    "exp(x)": (-2.0, 2.0),
    "ln(1+x)": (-0.9, 1.5),
}

INFO_MESSAGES = {
    "sin(x)": (
        "**sin(x)** is periodic and bounded between −1 and 1. Its Taylor series only contains "
        "odd powers of x (x, x³, x⁵, …), so each new term refines the wave shape. With enough "
        "terms the approximation tracks the true sine closely near x = 0, but drifts away further out."
    ),
    "cos(x)": (
        "**cos(x)** is also periodic and bounded between −1 and 1. Its Taylor series only contains "
        "even powers of x (1, x², x⁴, …), reflecting the function's symmetry about the y-axis. "
        "Adding more terms extends how far the approximation stays accurate."
    ),
    "exp(x)": (
        "**exp(x)** grows without bound, but its Taylor series converges everywhere on the real line. "
        "Every new term adds another power of x (1, x, x²/2!, …), and the approximation improves "
        "across an ever-wider range as the term count increases."
    ),
    "ln(1+x)": (
        "**ln(1+x)** has a finite radius of convergence: the series only converges for −1 < x ≤ 1. "
        "The plot is restricted to that region so you can see how the approximation improves near "
        "x = 0, while outside the interval no finite number of terms will catch up to the true function."
    ),
}

# --- Widgets ---

col1, col2 = st.columns(2)
with col1:
    func_name = st.selectbox("Function", list(FUNC_SYMS.keys()))
with col2:
    n_terms = st.slider("Number of terms", min_value=1, max_value=10, value=3)

# --- Computation ---

f_sym = FUNC_SYMS[func_name]
taylor_poly = f_sym.series(x, 0, n_terms + 1).removeO()
f_approx = sp.lambdify(x, taylor_poly, "numpy")
f_true = sp.lambdify(x, f_sym, "numpy")

x_lo, x_hi = X_BOUNDS[func_name]
x_vals = np.linspace(x_lo, x_hi, 400)

term_label = f"{n_terms} term{'s' if n_terms > 1 else ''}"

# --- Info box ---

st.info(INFO_MESSAGES[func_name])

# --- Two-column layout: code on the left, chart on the right ---

col_code, col_chart = st.columns([2, 3])

with col_code:
    st.code(
        f"""\
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.Symbol("x")
f_sym = {FUNC_CODE_STR[func_name]}
taylor_poly = f_sym.series(x, 0, {n_terms + 1}).removeO()
f_approx = sp.lambdify(x, taylor_poly, "numpy")
f_true   = sp.lambdify(x, f_sym,       "numpy")

x_vals = np.linspace({x_lo}, {x_hi}, 400)

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(x_vals, f_true(x_vals),
        label="True: {func_name}", linewidth=2)
ax.plot(x_vals, f_approx(x_vals),
        label="Taylor ({term_label})",
        linestyle="--", linewidth=2, color="orange")
ax.set_ylim(-4, 4)
ax.axhline(0, color="grey", linewidth=0.5)
ax.axvline(0, color="grey", linewidth=0.5)
ax.set_title("Taylor approximation of {func_name} around x = 0")
ax.set_xlabel("x")
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
""",
        language="python",
    )
    st.latex(r"P(x) = " + sp.latex(taylor_poly))

with col_chart:
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(x_vals, f_true(x_vals), label=f"True: {func_name}", linewidth=2)
    ax.plot(
        x_vals,
        f_approx(x_vals),
        label=f"Taylor ({term_label})",
        linestyle="--",
        linewidth=2,
        color="orange",
    )
    ax.set_ylim(-4, 4)
    ax.axhline(0, color="grey", linewidth=0.5)
    ax.axvline(0, color="grey", linewidth=0.5)
    ax.set_title(f"Taylor approximation of {func_name} around x = 0")
    ax.set_xlabel("x")
    ax.legend()
    ax.grid(alpha=0.3)
    st.pyplot(fig)
