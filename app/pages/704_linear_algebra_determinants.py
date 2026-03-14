import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Linear Algebra Determinants", page_icon="📐", layout="wide"
)
st.header("Linear Algebra Determinants")


# ── Introduction ─────────────────────────────────────────────────────────────
st.info(
    "The determinant is a **scalar value** computed from the elements of a **square matrix**. "
    "It reveals whether the matrix is **invertible**, how it scales space, and whether it "
    "preserves or reverses orientation. A determinant of zero means the matrix is singular "
    "and cannot be inverted."
)

st.info(
    "In quantitative finance, determinants are used in portfolio optimisation to assess "
    "whether a covariance matrix is invertible when computing minimum variance portfolios, "
    "and in risk management to detect multicollinearity among risk factors — which can lead "
    "to unstable hedging strategies."
)


# ── 2×2 Formula ──────────────────────────────────────────────────────────────
st.markdown("##### 2×2 Determinant")
st.info(
    "For a 2×2 matrix, the determinant is the product of the main diagonal minus the "
    "product of the off-diagonal. Geometrically it equals the signed area of the "
    "parallelogram formed by the two column vectors."
)

col_left, col_right = st.columns(2)

with col_left:
    st.latex(
        r"M = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \qquad \det M = ad - bc"
    )
    st.info(r"""
- **det M = 0** → singular matrix, **not** invertible
- **det M ≠ 0** → non-singular matrix, invertible
""")

with col_right:
    # Generic illustration: unit square vs parallelogram for a simple example
    a, b, c, d = 2, 1, 0.5, 2
    col1 = np.array([a, c])
    col2 = np.array([b, d])
    det = a * d - b * c
    fig, ax = plt.subplots(figsize=(5, 4))
    origin = np.zeros(2)
    parallelogram = np.array([origin, col1, col1 + col2, col2, origin])
    ax.fill(parallelogram[:, 0], parallelogram[:, 1], alpha=0.2, color="royalblue")
    ax.plot(parallelogram[:, 0], parallelogram[:, 1], "royalblue", linewidth=1.5)
    ax.quiver(
        *origin,
        *col1,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="royalblue",
        label=f"col 1: ({a}, {c})",
    )
    ax.quiver(
        *origin,
        *col2,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="tomato",
        label=f"col 2: ({b}, {d})",
    )
    cx, cy = (col1 + col2) / 2
    ax.text(
        cx,
        cy,
        f"area = det = {det:.4g}",
        ha="center",
        va="center",
        fontsize=10,
        color="navy",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7),
    )
    lim = max(col1.max(), (col1 + col2).max(), col2.max()) + 0.5
    ax.set_xlim(-0.5, lim)
    ax.set_ylim(-0.5, lim)
    ax.axhline(0, color="grey", linewidth=0.5)
    ax.axvline(0, color="grey", linewidth=0.5)
    ax.set_aspect("equal")
    ax.legend(fontsize=9)
    ax.set_title("det M = area of parallelogram (schematic)", fontsize=10)
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    plt.close(fig)


# ── Example ───────────────────────────────────────────────────────────────────
st.markdown("##### Example")
st.info("Computing the determinant of a 2×2 matrix using SymPy.")

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex

A = Matrix([[6, 5], [1, 2]])
st.latex(r'A = ' + latex(A))

det_A = A.det()
st.latex(r'\\det A = ' + latex(det_A))
"""
    st.code(code, language="python")
    exec(code)
    st.latex(r"\det A = 6 \times 2 - 5 \times 1 = 12 - 5 = 7")

with col_right:
    A = np.array([[6, 5], [1, 2]], dtype=float)
    col1 = A[:, 0]
    col2 = A[:, 1]
    det = np.linalg.det(A)

    fig, ax = plt.subplots(figsize=(5, 4))
    origin = np.zeros(2)
    parallelogram = np.array([origin, col1, col1 + col2, col2, origin])
    ax.fill(parallelogram[:, 0], parallelogram[:, 1], alpha=0.2, color="royalblue")
    ax.plot(parallelogram[:, 0], parallelogram[:, 1], "royalblue", linewidth=1.5)
    ax.quiver(
        *origin,
        *col1,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="royalblue",
        label=f"col 1: ({col1[0]:.0f}, {col1[1]:.0f})",
    )
    ax.quiver(
        *origin,
        *col2,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="tomato",
        label=f"col 2: ({col2[0]:.0f}, {col2[1]:.0f})",
    )
    cx, cy = (col1 + col2) / 2
    ax.text(
        cx,
        cy,
        f"area = det = {det:.4g}",
        ha="center",
        va="center",
        fontsize=11,
        color="navy",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7),
    )
    lim = max(col1.max(), (col1 + col2).max(), col2.max()) + 1
    ax.set_xlim(-0.5, lim)
    ax.set_ylim(-0.5, lim)
    ax.axhline(0, color="grey", linewidth=0.5)
    ax.axvline(0, color="grey", linewidth=0.5)
    ax.set_aspect("equal")
    ax.legend(fontsize=9)
    ax.set_title(f"A = [[6,5],[1,2]] — det A = {det:.4g}", fontsize=10)
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    plt.close(fig)

    st.info(
        "For an n×n matrix, the determinant tells you how the matrix scales "
        "n-dimensional volume."
    )
    st.info(
        "A **positive** determinant means the transformation preserves orientation. "
        "A **negative** determinant means it reverses orientation (includes a reflection)."
    )
