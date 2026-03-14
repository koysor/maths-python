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


# ── Non-invertible Matrix ─────────────────────────────────────────────────────
st.markdown("##### Non-invertible Matrix")
st.info(
    "When det(A) = 0 the matrix is singular — its columns are linearly dependent and the "
    "transformation collapses space to a lower dimension. No inverse exists because the "
    "transformation cannot be undone: information is permanently lost."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex

A = Matrix([[2, 4], [1, 2]])
st.latex(r'A = ' + latex(A))
st.latex(r'\\det(A) = ' + latex(A.det()))

try:
    A_inv = A.inv()
except Exception as e:
    st.error(f"Cannot invert: {e}")
"""
    st.code(code, language="python")
    exec(code)
    st.info(
        "Column 2 = 2 × column 1, so the columns are linearly dependent. "
        "The matrix squashes 2D space onto a line — that cannot be reversed."
    )

with col_right:
    A_sing = np.array([[2, 4], [1, 2]], dtype=float)
    c1, c2 = A_sing[:, 0], A_sing[:, 1]
    origin = np.zeros(2)

    fig, axes = plt.subplots(1, 2, figsize=(7, 3))
    for ax in axes:
        ax.axhline(0, color="grey", linewidth=0.5)
        ax.axvline(0, color="grey", linewidth=0.5)
        ax.set_aspect("equal")
        ax.grid(True, alpha=0.3)

    plot_transformed_shape(axes[0], np.eye(2), UNIT_SQUARE, "royalblue", "unit square")
    axes[0].set_title("Original", fontsize=10)
    axes[0].legend(fontsize=8)
    axes[0].set_xlim(-0.5, 2)
    axes[0].set_ylim(-0.5, 2)

    # the transformed square degenerates to a line segment
    transformed = A_sing @ UNIT_SQUARE
    axes[1].plot(
        transformed[0],
        transformed[1],
        "tomato",
        linewidth=3,
        label="collapses to a line",
    )
    axes[1].set_title("Transformed by A (singular)", fontsize=10)
    axes[1].legend(fontsize=8)
    axes[1].set_xlim(-0.5, 7)
    axes[1].set_ylim(-0.5, 4)
    axes[1].text(
        3,
        2,
        "det = 0\nno inverse",
        ha="center",
        fontsize=9,
        color="tomato",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
    )

    fig.suptitle("Singular matrix — space collapses, inverse undefined", fontsize=10)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


# ── 3×3 Inversion ─────────────────────────────────────────────────────────────
st.markdown("##### 3×3 Matrix Inversion")
st.info(
    "For matrices larger than 2×2 there is no simple closed-form formula. In practice "
    "we rely on numerical methods (Gaussian elimination, LU decomposition) implemented "
    "in SymPy or NumPy. The same conditions apply: the matrix must be square with det ≠ 0."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex

A = Matrix([[2, 1, 0], [1, 3, 1], [0, 1, 4]])
st.latex(r'A = ' + latex(A))
st.latex(r'\\det(A) = ' + latex(A.det()))

A_inv = A.inv()
st.latex(r'A^{-1} = ' + latex(A_inv))

I = A * A_inv
st.latex(r'A \\cdot A^{-1} = ' + latex(I))
"""
    st.code(code, language="python")
    exec(code)

with col_right:
    code_np = """
import streamlit as st
from sympy import Matrix, latex
import numpy as np

A = np.array([[2, 1, 0], [1, 3, 1], [0, 1, 4]], dtype=float)
A_inv = np.linalg.inv(A)
st.latex(r'A^{-1} \\approx ' + latex(Matrix(A_inv.round(4))))

# verify
I = A @ A_inv
st.latex(r'A \\cdot A^{-1} \\approx ' + latex(Matrix(I.round(10))))
"""
    st.code(code_np, language="python")
    exec(code_np)
    st.info(
        "NumPy uses floating-point arithmetic so results may have tiny rounding errors, "
        "but A·A⁻¹ is effectively the identity matrix."
    )


# ── Key Properties ────────────────────────────────────────────────────────────
st.markdown("##### Key Properties")
st.info(
    "These identities are useful when manipulating expressions involving inverses. "
    "Note that the order reverses for products — (AB)⁻¹ = B⁻¹A⁻¹, not A⁻¹B⁻¹."
)

col_left, col_right = st.columns(2)

with col_left:
    st.markdown("""
| Property | Rule |
|---|---|
| Double inverse | (A⁻¹)⁻¹ = A |
| Product | (AB)⁻¹ = B⁻¹A⁻¹ |
| Transpose | (Aᵀ)⁻¹ = (A⁻¹)ᵀ |
| Determinant | det(A⁻¹) = 1 / det(A) |
| Scalar | (cA)⁻¹ = (1/c) A⁻¹ |
""")

with col_right:
    code = """
import streamlit as st
from sympy import Matrix, latex

A = Matrix([[3, 1], [2, 4]])
B = Matrix([[1, 2], [0, 3]])

st.latex(r'(A^{-1})^{-1} = A \\quad \\Rightarrow ' + latex(A.inv().inv()))
st.latex(r'(AB)^{-1} = ' + latex((A * B).inv()))
st.latex(r'B^{-1}A^{-1} = ' + latex(B.inv() * A.inv()))
st.latex(r'(A^T)^{-1} = ' + latex(A.T.inv()))
st.latex(r'(A^{-1})^T = ' + latex(A.inv().T))
st.latex(r'\\det(A^{-1}) = ' + latex(A.inv().det()) + r',\\quad 1/\\det(A) = ' + latex(1 / A.det()))
"""
    st.code(code, language="python")
    exec(code)
