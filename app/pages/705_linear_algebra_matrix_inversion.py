import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Linear Algebra - Matrix Inversion", page_icon="📐", layout="wide"
)
st.header("Linear Algebra - Matrix Inversion")


def plot_transformed_shape(ax, M, shape, color, label, alpha=0.3):
    """Apply matrix M to a 2D shape (2×n array of column points) and plot it."""
    transformed = M @ shape
    closed = np.hstack([transformed, transformed[:, [0]]])
    ax.fill(closed[0], closed[1], color=color, alpha=alpha)
    ax.plot(closed[0], closed[1], color=color, linewidth=2, label=label)


# unit square corners as column vectors
UNIT_SQUARE = np.array([[0, 1, 1, 0], [0, 0, 1, 1]], dtype=float)


# ── Introduction ─────────────────────────────────────────────────────────────
st.info(
    "Matrix inversion finds a matrix that, when multiplied with the original, produces the "
    "identity matrix. The inverse of **A** is written **A⁻¹** and satisfies "
    "**AA⁻¹ = A⁻¹A = I**. Geometrically, A⁻¹ exactly undoes the transformation that A applies."
)

st.info(
    "Matrix inversion is used for solving systems of linear equations, computing least-squares "
    "solutions in regression analysis, and performing transformations in computer graphics. "
    "Only square matrices with a non-zero determinant have an inverse."
)

st.info(
    "Only square matrices can have an inverse, and the inverse exists only when **det(A) ≠ 0**."
)


# ── 2×2 Formula ──────────────────────────────────────────────────────────────
st.markdown("##### 2×2 Matrix Inversion Formula")
st.info(
    "For a 2×2 matrix the inverse has a closed-form solution: swap the diagonal elements, "
    "negate the off-diagonal elements, and divide everything by the determinant."
)

col_left, col_right = st.columns(2)

with col_left:
    st.latex(r"""
\text{If } A = \begin{bmatrix} a & b \\ c & d \end{bmatrix},
\text{ then } A^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}
""")
    st.info(r"""
Steps:
1. Compute det(A) = ad − bc
2. If det(A) = 0, the matrix is singular — no inverse exists
3. Swap a and d, negate b and c
4. Divide every element by det(A)
""")

with col_right:
    # schematic: show that A then A_inv returns to identity transformation
    A = np.array([[2, 1], [1, 2]], dtype=float)
    A_inv = np.linalg.inv(A)

    fig, axes = plt.subplots(1, 3, figsize=(9, 3))
    for ax in axes:
        ax.axhline(0, color="grey", linewidth=0.5)
        ax.axvline(0, color="grey", linewidth=0.5)
        ax.set_aspect("equal")
        ax.grid(True, alpha=0.3)

    plot_transformed_shape(axes[0], np.eye(2), UNIT_SQUARE, "royalblue", "unit square")
    axes[0].set_title("Original", fontsize=10)
    axes[0].legend(fontsize=8)

    plot_transformed_shape(axes[1], A, UNIT_SQUARE, "tomato", "after A")
    axes[1].set_title("Transformed by A", fontsize=10)
    axes[1].legend(fontsize=8)

    plot_transformed_shape(
        axes[2], A_inv @ A, UNIT_SQUARE, "seagreen", "after A⁻¹A = I"
    )
    axes[2].set_title("Transformed by A⁻¹ (undone)", fontsize=10)
    axes[2].legend(fontsize=8)

    for ax in axes:
        ax.set_xlim(-0.5, 4)
        ax.set_ylim(-0.5, 4)

    fig.suptitle("A⁻¹ reverses the transformation of A", fontsize=11)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


# ── SymPy Example ─────────────────────────────────────────────────────────────
st.markdown("##### Example: 2×2 Matrix Inversion")
st.info("Computing the inverse of a 2×2 matrix with SymPy, and verifying AA⁻¹ = I.")

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex

A = Matrix([[4, 7], [2, 6]])
st.latex(r'A = ' + latex(A))

det_A = A.det()
st.latex(r'\\det(A) = ' + latex(det_A))

A_inv = A.inv()
st.latex(r'A^{-1} = ' + latex(A_inv))

I = A * A_inv
st.latex(r'A \\cdot A^{-1} = ' + latex(I))
"""
    st.code(code, language="python")
    exec(code)
    st.info("""
Calculation steps:
- det(A) = 4×6 − 7×2 = 24 − 14 = 10
- Since det(A) = 10 ≠ 0, the matrix is invertible
- A⁻¹ = (1/10) × [[6, −7], [−2, 4]]
- Verification: A × A⁻¹ = I ✓
""")

with col_right:
    A = np.array([[4, 7], [2, 6]], dtype=float)
    A_inv = np.linalg.inv(A)

    fig, axes = plt.subplots(1, 3, figsize=(9, 3))
    for ax in axes:
        ax.axhline(0, color="grey", linewidth=0.5)
        ax.axvline(0, color="grey", linewidth=0.5)
        ax.set_aspect("equal")
        ax.grid(True, alpha=0.3)

    plot_transformed_shape(axes[0], np.eye(2), UNIT_SQUARE, "royalblue", "unit square")
    axes[0].set_title("Original", fontsize=10)
    axes[0].legend(fontsize=8)

    plot_transformed_shape(axes[1], A, UNIT_SQUARE, "tomato", "after A")
    axes[1].set_title("Transformed by A", fontsize=10)
    axes[1].legend(fontsize=8)

    plot_transformed_shape(
        axes[2], A_inv @ A, UNIT_SQUARE, "seagreen", "after A⁻¹A = I"
    )
    axes[2].set_title("Transformed by A⁻¹ (undone)", fontsize=10)
    axes[2].legend(fontsize=8)

    # set consistent axis limits across all panels
    transformed = A @ UNIT_SQUARE
    lim = max(abs(transformed).max() + 1, 2)
    for ax in axes:
        ax.set_xlim(-1, lim)
        ax.set_ylim(-1, lim)

    fig.suptitle("A = [[4,7],[2,6]] — A⁻¹ reverses the transformation", fontsize=11)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
