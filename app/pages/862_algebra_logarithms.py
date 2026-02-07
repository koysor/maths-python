import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.markdown("### Logarithms")

st.write(
    "Logarithms, or logs, are a way of expressing numbers in terms of their powers."
)

col1, col2 = st.columns(2)

with col1:

    latex_code = r"""
    \log_a{b} = x \iff a^x = b
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.info(
        "$$a$$ is the base of the logarithm, $$b$$ is the number you want to find the log of, and $$x$$ is the exponent to which the base must be raised to produce that number."
    )

with col2:

    col1, col2 = st.columns(2)

    with col1:
        a = st.number_input("Enter a value for a:", value=2, step=1)

    with col2:
        b = st.number_input("Enter a value for b:", value=8, step=1)

    latex_code = f"""
    \\log_{a}{b} = x \\iff {a}^x = {b}
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)


st.markdown("### Laws of Logarithms")

latex_code = r"""
\log_a{x} + \log_a{y} = \log_a{(x \cdot y)}
"""
st.code(latex_code, language="latex")
st.latex(latex_code)

latex_code = r"""
\log_a{x} - \log_a{y} = \log_a{(\frac{x}{y})}
"""
st.code(latex_code, language="latex")
st.latex(latex_code)

latex_code = r"""
\log_a{\frac{1}{x}} = -\log_a{x}
"""
st.code(latex_code, language="latex")
st.latex(latex_code)

latex_code = r"""
\log_a{x^n} = n\log_a{x}
"""
st.code(latex_code, language="latex")
st.latex(latex_code)


# -- Changing the base ---------------------------------------------------------

st.markdown("---")
st.markdown("### Changing the Base")

st.write(
    r"The shape of $y = \log_a(x)$ depends entirely on the base $a$. "
    r"Drag the slider to see how the curve changes."
)


@st.fragment
def base_explorer():
    base = st.slider(
        "Base (a)",
        min_value=0.2,
        max_value=10.0,
        value=2.0,
        step=0.1,
        key="log_base",
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    x = np.linspace(0.01, 20, 500)

    # Reference curves (faint)
    for ref_base, colour, label in [
        (2, "#AAAAAA", r"$\log_2$"),
        (np.e, "#CCCCCC", r"$\ln$"),
        (10, "#DDDDDD", r"$\log_{10}$"),
    ]:
        ax.plot(
            x,
            np.log(x) / np.log(ref_base),
            color=colour,
            linewidth=1,
            linestyle=":",
            label=label,
        )

    # Active curve
    y = np.log(x) / np.log(base)
    ax.plot(x, y, color="#4A90D9", linewidth=2.5, label=rf"$\log_{{{base:.1f}}}(x)$")

    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)

    # Mark (1, 0) — always on the curve
    ax.plot(1, 0, "ro", markersize=7, zorder=5)
    ax.annotate(
        "(1, 0)",
        xy=(1, 0),
        xytext=(2, -2),
        fontsize=10,
        color="red",
        arrowprops=dict(arrowstyle="->", color="red"),
    )

    # Mark (a, 1)
    if 0.01 < base <= 20:
        ax.plot(base, 1, "go", markersize=7, zorder=5)
        ax.annotate(
            f"({base:.1f}, 1)",
            xy=(base, 1),
            xytext=(min(base + 1.5, 17), 1.8),
            fontsize=10,
            color="green",
            arrowprops=dict(arrowstyle="->", color="green"),
        )

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(rf"$y = \log_{{{base:.1f}}}(x)$", fontsize=13)
    ax.legend(loc="lower right", fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-0.5, 20)
    ax.set_ylim(-4, 4)

    fig.tight_layout()
    st.pyplot(fig)

    if base < 1:
        st.info(
            r"When $a < 1$ the curve is **reflected** — $\log_a(x)$ is a decreasing "
            r"function because raising a fraction to a larger power produces a smaller result."
        )
    elif abs(base - 1.0) < 0.15:
        st.warning(
            r"As $a$ approaches 1 the curve diverges — $\log_1(x)$ is undefined "
            r"because $1^x = 1$ for all $x$."
        )


base_explorer()


# -- Inverse relationship: a^x and log_a(x) ------------------------------------

st.markdown("---")
st.markdown("### Inverse Relationship: $a^x$ and $\\log_a(x)$")

st.write(
    r"The exponential $y = a^x$ and the logarithm $y = \log_a(x)$ are inverse "
    r"functions — each one undoes the other. Graphically, their curves are mirror "
    r"images across the line $y = x$."
)


@st.fragment
def inverse_explorer():
    base_inv = st.slider(
        "Base (a)",
        min_value=1.1,
        max_value=10.0,
        value=2.0,
        step=0.1,
        key="inv_base",
    )

    fig, ax = plt.subplots(figsize=(7, 7))

    # y = x mirror line
    mirror = np.linspace(-2, 8, 200)
    ax.plot(
        mirror, mirror, color="#AAAAAA", linestyle="--", linewidth=1, label="$y = x$"
    )

    # a^x
    x_exp = np.linspace(-2, 4, 300)
    y_exp = base_inv**x_exp
    ax.plot(
        x_exp, y_exp, color="#4A90D9", linewidth=2.5, label=rf"$y = {base_inv:.1f}^x$"
    )

    # log_a(x)
    x_log = np.linspace(0.01, 12, 300)
    y_log = np.log(x_log) / np.log(base_inv)
    ax.plot(
        x_log,
        y_log,
        color="#F5A623",
        linewidth=2.5,
        label=rf"$y = \log_{{{base_inv:.1f}}}(x)$",
    )

    # Mark key mirror pairs: (0, 1) <-> (1, 0)
    ax.plot(0, 1, "o", color="#4A90D9", markersize=8, zorder=5)
    ax.plot(1, 0, "o", color="#F5A623", markersize=8, zorder=5)
    ax.annotate(
        "(0, 1)",
        xy=(0, 1),
        xytext=(-1.5, 2),
        fontsize=10,
        color="#4A90D9",
        arrowprops=dict(arrowstyle="->", color="#4A90D9"),
    )
    ax.annotate(
        "(1, 0)",
        xy=(1, 0),
        xytext=(2.5, -1.5),
        fontsize=10,
        color="#F5A623",
        arrowprops=dict(arrowstyle="->", color="#F5A623"),
    )

    # Mark (1, a) <-> (a, 1)
    ax.plot(1, base_inv, "o", color="#4A90D9", markersize=8, zorder=5)
    ax.plot(base_inv, 1, "o", color="#F5A623", markersize=8, zorder=5)

    # Dashed line connecting the mirror pair
    ax.plot(
        [1, base_inv],
        [base_inv, 1],
        color="#E74C3C",
        linestyle=":",
        linewidth=1.5,
        alpha=0.7,
    )

    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Exponential and logarithm as mirror images", fontsize=13)
    ax.legend(loc="upper left", fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-2, 8)
    ax.set_ylim(-2, 8)
    ax.set_aspect("equal")

    fig.tight_layout()
    st.pyplot(fig)


inverse_explorer()
