import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Linear Algebra - Identity Matrices", page_icon="📐", layout="wide"
)
st.header("Linear Algebra - Identity Matrices")


def matrix_heatmap(ax, data, title):
    """Draw an annotated heatmap for a matrix."""
    ax.imshow(data, cmap="Blues", aspect="equal", vmin=0, vmax=1)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            ax.text(
                j,
                i,
                f"{data[i, j]:.4g}",
                ha="center",
                va="center",
                fontsize=12,
                fontweight="bold",
            )
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title, fontsize=11)


def plot_transformed_shape(ax, M, shape, color, label, alpha=0.3):
    """Apply matrix M to a 2D shape and plot it."""
    transformed = M @ shape
    closed = np.hstack([transformed, transformed[:, [0]]])
    ax.fill(closed[0], closed[1], color=color, alpha=alpha)
    ax.plot(closed[0], closed[1], color=color, linewidth=2, label=label)


UNIT_SQUARE = np.array([[0, 1, 1, 0], [0, 0, 1, 1]], dtype=float)


# ── Introduction ──────────────────────────────────────────────────────────────
st.info(
    "An identity matrix is a square matrix with **1s on the main diagonal** and **0s everywhere else**. "
    "It is the matrix equivalent of the number 1 in arithmetic — multiplying any compatible matrix "
    "by the identity leaves it unchanged: **AI = IA = A**."
)

st.info("""The identity matrix is used for:
- Matrix inversion: A × A⁻¹ = I
- Solving systems of linear equations
- Understanding transformations that preserve vectors
- As a starting point for iterative algorithms""")


# ── Examples ──────────────────────────────────────────────────────────────────
st.markdown("##### Identity Matrix Examples")
st.info(
    "Identity matrices of any size share the same structure: 1s on the diagonal, 0s elsewhere. "
    "The subscript denotes the dimension."
)

col_left, col_right = st.columns(2)

with col_left:
    st.latex(r"""
I_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}, \quad
I_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
""")
    code = """
import streamlit as st
from sympy import eye, latex

I2 = eye(2)
st.latex(r'I_2 = ' + latex(I2))

I3 = eye(3)
st.latex(r'I_3 = ' + latex(I3))

I4 = eye(4)
st.latex(r'I_4 = ' + latex(I4))
"""
    st.code(code, language="python")
    exec(code)

with col_right:
    fig, axes = plt.subplots(1, 3, figsize=(7, 3))
    for n, ax in zip([2, 3, 4], axes):
        matrix_heatmap(ax, np.eye(n), f"I{n}  ({n}×{n})")
    fig.suptitle("Identity matrices — 1s on diagonal, 0s elsewhere", fontsize=11)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


# ── Verifying the Identity Property ──────────────────────────────────────────
st.markdown("##### Verifying the Identity Property")
st.info(
    "Multiplying any matrix by the identity — in either order — returns the original matrix unchanged. "
    "Geometrically, the identity transformation leaves every vector exactly where it is."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, eye, latex

A = Matrix([[3, 7], [2, 5]])
st.latex(r'A = ' + latex(A))

I = eye(2)
st.latex(r'I = ' + latex(I))

st.latex(r'A \\cdot I = ' + latex(A * I))
st.latex(r'I \\cdot A = ' + latex(I * A))
"""
    st.code(code, language="python")
    exec(code)
    st.info("""
- A × I = A ✓
- I × A = A ✓
- Order doesn't matter with the identity: **AI = IA = A**
""")

with col_right:
    A = np.array([[3, 7], [2, 5]], dtype=float)
    I2 = np.eye(2)
    AI = A @ I2

    fig, axes = plt.subplots(1, 3, figsize=(7, 3))
    matrix_heatmap(axes[0], A, "A")
    matrix_heatmap(axes[1], I2, "I")
    matrix_heatmap(axes[2], AI, "A · I  (= A)")
    axes[1].set_xlabel("×", fontsize=18, labelpad=2)
    axes[2].set_xlabel("=  A · I", fontsize=11, labelpad=2)
    fig.suptitle("A · I returns A unchanged — element by element", fontsize=11)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    # geometric: show A and A@I transform unit square identically
    fig2, axes2 = plt.subplots(1, 2, figsize=(7, 3))
    for ax in axes2:
        ax.axhline(0, color="grey", linewidth=0.5)
        ax.axvline(0, color="grey", linewidth=0.5)
        ax.set_aspect("equal")
        ax.grid(True, alpha=0.3)

    plot_transformed_shape(axes2[0], A, UNIT_SQUARE, "royalblue", "A × unit square")
    axes2[0].set_title("Transformed by A", fontsize=10)
    axes2[0].legend(fontsize=8)

    plot_transformed_shape(axes2[1], AI, UNIT_SQUARE, "seagreen", "AI × unit square")
    axes2[1].set_title("Transformed by AI (identical)", fontsize=10)
    axes2[1].legend(fontsize=8)

    lim = abs(A @ UNIT_SQUARE).max() + 1
    for ax in axes2:
        ax.set_xlim(-1, lim)
        ax.set_ylim(-1, lim)

    fig2.suptitle("A and AI produce the same transformation", fontsize=11)
    plt.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)


# ── NumPy ─────────────────────────────────────────────────────────────────────
st.markdown("##### Identity Matrices with NumPy")
st.info(
    "NumPy's `np.eye(n)` creates an n×n identity matrix as a floating-point array. "
    "It is efficient for large-scale numerical computations."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import latex, Matrix
import numpy as np

I_np = np.eye(3)
st.write("NumPy identity matrix (3×3):")
st.latex(latex(Matrix(I_np)))

A = np.array([[2, 3, 1], [4, 5, 6], [7, 8, 9]])
result = np.dot(A, I_np)

st.write("Original matrix A:")
st.latex(latex(Matrix(A)))

st.write("A × I:")
st.latex(latex(Matrix(result)))
"""
    st.code(code, language="python")
    exec(code)
    st.info(
        "NumPy's `np.eye(n)` is equivalent to SymPy's `eye(n)` but returns a float64 array."
    )

with col_right:
    A_np = np.array([[2, 3, 1], [4, 5, 6], [7, 8, 9]], dtype=float)
    I_np = np.eye(3)
    result_np = A_np @ I_np

    fig, axes = plt.subplots(1, 3, figsize=(7, 3))
    matrix_heatmap(axes[0], A_np, "A  (3×3)")
    matrix_heatmap(axes[1], I_np, "I₃  (3×3)")
    matrix_heatmap(axes[2], result_np, "A · I₃  (= A)")
    axes[1].set_xlabel("×", fontsize=18, labelpad=2)
    axes[2].set_xlabel("=  A · I₃", fontsize=11, labelpad=2)
    fig.suptitle("NumPy: A · I = A unchanged", fontsize=11)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
