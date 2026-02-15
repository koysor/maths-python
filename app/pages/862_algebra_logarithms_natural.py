import streamlit as st
import sympy as sp  # noqa: F401 — used by exec'd SymPy snippet
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="The Natural Logarithm and Euler's Number", page_icon="📐", layout="wide"
)
st.header("The Natural Logarithm and Euler's Number")

st.write(
    r"""The number $e \approx 2.71828\ldots$ is one of the most important constants in
mathematics. It is **irrational** (it cannot be expressed as a fraction) and
**transcendental** (it is not the root of any polynomial with rational
coefficients). Together with the natural logarithm $\ln$, it forms the
foundation of continuous growth, calculus, and many areas of applied
mathematics."""
)

st.info(r"""**Euler's Number** — The constant $e$ is defined as the limit

$$e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^{\!n}$$

It arises naturally when modelling continuous compound growth and is the
unique base for which the exponential function equals its own derivative.""")


# -- Definitions of e ----------------------------------------------------------

st.markdown("#### Definitions of $e$")

st.write("Two classical definitions are commonly used:")

st.markdown("**1. Limit definition**")

latex_code = r"e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^{n}"
st.code(latex_code, language="latex")
st.latex(latex_code)

st.markdown("**2. Series definition**")

latex_code = r"e = \sum_{k=0}^{\infty} \frac{1}{k!} = 1 + 1 + \frac{1}{2} + \frac{1}{6} + \frac{1}{24} + \cdots"
st.code(latex_code, language="latex")
st.latex(latex_code)

st.write("The table below shows how quickly both definitions converge to $e$:")

convergence_code = """\
import pandas as pd
from math import factorial, e as MATH_E

rows = []
for n in [1, 2, 5, 10, 50, 100, 1_000, 10_000, 100_000]:
    limit_approx = (1 + 1/n) ** n
    series_terms = min(n, 20)  # series converges in ~20 terms
    series_approx = 0
    for k in range(series_terms + 1):
        series_approx += 1 / factorial(k)
    rows.append({
        "n": f"{n:,}",
        "Limit: (1 + 1/n)^n": f"{limit_approx:.10f}",
        "Series: sum 1/k!": f"{series_approx:.10f}",
    })

df = pd.DataFrame(rows)
st.dataframe(df, hide_index=True, use_container_width=False)
st.write(f"**True value:** $e = {MATH_E:.15f}\\\\ldots$")
"""


@st.cache_data
def _calculate_convergence_table():
    import pandas as pd
    from math import factorial

    rows = []
    for n in [1, 2, 5, 10, 50, 100, 1_000, 10_000, 100_000]:
        limit_approx = (1 + 1 / n) ** n
        series_terms = min(n, 20)  # series converges in ~20 terms
        series_approx = 0
        for k in range(series_terms + 1):
            series_approx += 1 / factorial(k)
        rows.append(
            {
                "n": f"{n:,}",
                "Limit: (1 + 1/n)^n": f"{limit_approx:.10f}",
                "Series: sum 1/k!": f"{series_approx:.10f}",
            }
        )
    return pd.DataFrame(rows)


col1, _ = st.columns([4, 2])
with col1:
    from math import e as MATH_E

    st.code(convergence_code, language="python")
    df = _calculate_convergence_table()
    st.dataframe(df, hide_index=True, use_container_width=False)
    st.write(f"**True value:** $e = {MATH_E:.15f}\\\\ldots$")


# -- Relationship between e and ln ---------------------------------------------

st.divider()
st.markdown("#### Relationship between $e$ and $\\ln$")

st.write(r"""The **natural logarithm**, written $\ln(x)$ or $\log_e(x)$, is the inverse
function of the exponential $e^x$. If $e^y = x$ then $\ln(x) = y$.""")

st.info(
    r"""**Inverse Relationship** — The exponential and natural logarithm undo
each other:

$$e^{\ln x} = x \quad (x > 0) \qquad \text{and} \qquad \ln(e^x) = x \quad (\text{all } x)$$"""
)

col_left, col_right = st.columns(2)

with col_left:
    st.markdown("**Fundamental identities**")

    latex_code = r"\ln(e^{x}) = x"
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    latex_code = r"e^{\ln x} = x \quad (x > 0)"
    st.code(latex_code, language="latex")
    st.latex(latex_code)

with col_right:
    st.markdown("**Special values**")

    latex_code = r"\ln(1) = 0"
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    latex_code = r"\ln(e) = 1"
    st.code(latex_code, language="latex")
    st.latex(latex_code)

st.markdown("**Properties of $\\ln$**")

st.write(r"Because $\ln$ is a logarithm with base $e$, the standard log laws apply:")

latex_code = r"\ln(xy) = \ln(x) + \ln(y)"
st.code(latex_code, language="latex")
st.latex(latex_code)

latex_code = r"\ln\!\left(\frac{x}{y}\right) = \ln(x) - \ln(y)"
st.code(latex_code, language="latex")
st.latex(latex_code)

latex_code = r"\ln(x^{n}) = n\,\ln(x)"
st.code(latex_code, language="latex")
st.latex(latex_code)


# -- Graphs of e^x and ln(x) ---------------------------------------------------

st.divider()
st.markdown("#### Graphs of $e^x$ and $\\ln(x)$")


@st.cache_resource
def _build_static_graphs():
    fig, (ax_exp, ax_ln) = plt.subplots(1, 2, figsize=(10, 5))

    # Left panel: e^x
    x_exp = np.linspace(-2, 3, 300)
    ax_exp.plot(x_exp, np.exp(x_exp), color="#4A90D9", linewidth=2, label=r"$y = e^x$")
    ax_exp.axhline(0, color="black", linewidth=0.5)
    ax_exp.axvline(0, color="black", linewidth=0.5)

    ax_exp.plot(0, 1, "ro", markersize=7, zorder=5)
    ax_exp.annotate(
        "(0, 1)",
        xy=(0, 1),
        xytext=(0.5, 3),
        fontsize=10,
        arrowprops=dict(arrowstyle="->", color="red"),
        color="red",
    )
    ax_exp.plot(1, np.e, "ro", markersize=7, zorder=5)
    ax_exp.annotate(
        f"(1, e) = (1, {np.e:.3f})",
        xy=(1, np.e),
        xytext=(1.3, 6),
        fontsize=10,
        arrowprops=dict(arrowstyle="->", color="red"),
        color="red",
    )
    ax_exp.axhline(0, color="grey", linestyle="--", alpha=0.5, linewidth=1)
    ax_exp.text(-1.8, 0.3, "asymptote $y = 0$", fontsize=9, color="grey", alpha=0.7)
    ax_exp.set_xlabel("x")
    ax_exp.set_ylabel("y")
    ax_exp.set_title(r"$y = e^x$", fontsize=13)
    ax_exp.legend(loc="upper left")
    ax_exp.grid(True, alpha=0.3)
    ax_exp.set_ylim(-1, 15)

    # Right panel: ln(x)
    x_ln = np.linspace(0.01, 8, 300)
    ax_ln.plot(x_ln, np.log(x_ln), color="#F5A623", linewidth=2, label=r"$y = \ln(x)$")
    ax_ln.axhline(0, color="black", linewidth=0.5)
    ax_ln.axvline(0, color="black", linewidth=0.5)

    ax_ln.plot(1, 0, "ro", markersize=7, zorder=5)
    ax_ln.annotate(
        "(1, 0)",
        xy=(1, 0),
        xytext=(2, -1.5),
        fontsize=10,
        arrowprops=dict(arrowstyle="->", color="red"),
        color="red",
    )
    ax_ln.plot(np.e, 1, "ro", markersize=7, zorder=5)
    ax_ln.annotate(
        f"(e, 1) = ({np.e:.3f}, 1)",
        xy=(np.e, 1),
        xytext=(4, 1.5),
        fontsize=10,
        arrowprops=dict(arrowstyle="->", color="red"),
        color="red",
    )
    ax_ln.axvline(0, color="grey", linestyle="--", alpha=0.5, linewidth=1)
    ax_ln.text(0.15, 1.8, "asymptote $x = 0$", fontsize=9, color="grey", alpha=0.7)
    ax_ln.set_xlabel("x")
    ax_ln.set_ylabel("y")
    ax_ln.set_title(r"$y = \ln(x)$", fontsize=13)
    ax_ln.legend(loc="lower right")
    ax_ln.grid(True, alpha=0.3)
    ax_ln.set_ylim(-3, 3)

    fig.tight_layout()
    return fig


st.pyplot(_build_static_graphs())


# -- Derivatives ---------------------------------------------------------------

st.divider()
st.markdown("#### Derivatives")

col_deriv_left, col_deriv_right = st.columns(2)

with col_deriv_left:
    st.markdown("**Derivative of $e^x$**")

    latex_code = r"\frac{d}{dx}\, e^{x} = e^{x}"
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write(
        r"The exponential function $e^x$ is its own derivative — the slope at any "
        r"point equals the function value at that point."
    )

with col_deriv_right:
    st.markdown("**Derivative of $\\ln(x)$**")

    latex_code = r"\frac{d}{dx}\, \ln(x) = \frac{1}{x} \quad (x > 0)"
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write(
        r"The slope of $\ln(x)$ decreases as $x$ grows, which is consistent with "
        r"the curve flattening out for large $x$."
    )

st.info(r"""**Why $e$ is special** — For a general exponential $a^x$ the derivative is

$$\frac{d}{dx}\, a^{x} = a^{x} \ln(a)$$

Only when $a = e$ does $\ln(a) = 1$, so the extra factor disappears and
$\frac{d}{dx}\, e^{x} = e^{x}$. This is the defining property that makes $e$ the
*natural* base.""")

st.markdown("**General formula**")

latex_code = r"\frac{d}{dx}\, a^{x} = a^{x} \ln(a)"
st.code(latex_code, language="latex")
st.latex(latex_code)

st.write(r"When $a = e$ this reduces to $e^x \cdot \ln(e) = e^x \cdot 1 = e^x$.")


# -- Python verification with SymPy --------------------------------------------

st.divider()
st.markdown("#### Python Verification with SymPy")

sympy_code = """\
import sympy as sp

x = sp.Symbol("x")
a = sp.Symbol("a", positive=True)

# Derivative of e^x
deriv_exp = sp.diff(sp.exp(x), x)
st.write("d/dx e^x =", deriv_exp)

# Derivative of ln(x)
deriv_ln = sp.diff(sp.ln(x), x)
st.write("d/dx ln(x) =", deriv_ln)

# Derivative of a^x (general base)
deriv_ax = sp.diff(a**x, x)
st.write("d/dx a^x =", deriv_ax)
"""


@st.cache_data
def _compute_sympy_derivatives():
    x = sp.Symbol("x")
    a = sp.Symbol("a", positive=True)
    return (
        str(sp.diff(sp.exp(x), x)),
        str(sp.diff(sp.ln(x), x)),
        str(sp.diff(a**x, x)),
    )


_deriv_exp, _deriv_ln, _deriv_ax = _compute_sympy_derivatives()

col1, _ = st.columns([4, 2])
with col1:
    st.code(sympy_code, language="python")
    st.write("d/dx e^x =", _deriv_exp)
    st.write("d/dx ln(x) =", _deriv_ln)
    st.write("d/dx a^x =", _deriv_ax)

st.info(
    "For the general laws of logarithms (product, quotient, power rules for any "
    "base), see the **Logarithms** page in the sidebar."
)
