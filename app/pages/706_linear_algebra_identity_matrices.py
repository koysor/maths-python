import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Linear Algebra - Identity Matrices", page_icon="📐", layout="wide"
)
st.header("Linear Algebra - Identity Matrices")


def matrix_heatmap(ax, data, title):
    """Draw an annotated heatmap for a matrix."""
    vmax = data.max() * 2 if data.max() > 0 else 1
    ax.imshow(data, cmap="Blues", aspect="equal", vmin=0, vmax=vmax)
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


# ── Identity Transformation ───────────────────────────────────────────────────
st.markdown("##### The Identity Transformation")
st.info(
    "The identity matrix represents the transformation that leaves every vector exactly where "
    "it is — no rotation, scaling, or shearing. Contrasted with a non-identity transformation, "
    "this makes clear what 'doing nothing' means geometrically."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, eye, latex
import numpy as np

I = eye(2)
A = Matrix([[2, 1], [0, 1]])

vectors = [Matrix([1, 0]), Matrix([0, 1]), Matrix([1, 1])]
for v in vectors:
    Iv = I * v
    Av = A * v
    st.latex(
        r'I\\mathbf{v} = ' + latex(Iv) +
        r',\\quad A\\mathbf{v} = ' + latex(Av)
    )
"""
    st.code(code, language="python")
    exec(code)
    st.info(
        "Under I every vector maps to itself. Under A the vectors are sheared — "
        "only the identity leaves all directions unchanged."
    )

with col_right:
    vectors = np.array([[1, 0], [0, 1], [1, 1], [-1, 1]], dtype=float).T
    A_shear = np.array([[2, 1], [0, 1]], dtype=float)
    I2 = np.eye(2)

    fig, axes = plt.subplots(1, 2, figsize=(7, 4))
    colors = ["royalblue", "tomato", "seagreen", "purple"]
    labels = ["[1,0]", "[0,1]", "[1,1]", "[-1,1]"]

    for panel, (M, title) in enumerate(
        [(I2, "I  (identity)"), (A_shear, "A  (shear)")]
    ):
        ax = axes[panel]
        ax.axhline(0, color="grey", linewidth=0.5)
        ax.axvline(0, color="grey", linewidth=0.5)
        ax.set_aspect("equal")
        ax.grid(True, alpha=0.3)
        ax.set_title(title, fontsize=11)
        for i, (v, color, lbl) in enumerate(zip(vectors.T, colors, labels)):
            Mv = M @ v
            ax.quiver(
                0,
                0,
                *Mv,
                angles="xy",
                scale_units="xy",
                scale=1,
                color=color,
                label=lbl,
                width=0.012,
            )
        ax.set_xlim(-2, 3)
        ax.set_ylim(-1.5, 2)
        ax.legend(fontsize=8)

    fig.suptitle("I leaves vectors unchanged — A shears them", fontsize=11)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


# ── Relationship to Matrix Inverse ────────────────────────────────────────────
st.markdown("##### Relationship to Matrix Inverse")
st.info(
    "The inverse of a matrix A is defined as the matrix A⁻¹ such that A × A⁻¹ = A⁻¹ × A = I. "
    "The identity matrix is therefore the result of a matrix multiplied by its own inverse — "
    "it is the 'neutral element' that confirms the inverse has fully undone the transformation."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, eye, latex

A = Matrix([[4, 7], [2, 6]])
st.latex(r'A = ' + latex(A))

A_inv = A.inv()
st.latex(r'A^{-1} = ' + latex(A_inv))

st.latex(r'A \\cdot A^{-1} = ' + latex(A * A_inv))
st.latex(r'A^{-1} \\cdot A = ' + latex(A_inv * A))
"""
    st.code(code, language="python")
    exec(code)
    st.info(
        "A × A⁻¹ = I confirms that the inverse exactly undoes the original transformation."
    )

with col_right:
    A_inv_np = np.array([[4, 7], [2, 6]], dtype=float)
    A_inv_inv = np.linalg.inv(A_inv_np)
    result = A_inv_np @ A_inv_inv

    fig, axes = plt.subplots(1, 3, figsize=(7, 3))
    matrix_heatmap(axes[0], A_inv_np, "A")
    matrix_heatmap(axes[1], A_inv_inv, "A⁻¹")
    matrix_heatmap(axes[2], result, "A · A⁻¹ = I")
    axes[1].set_xlabel("×", fontsize=18, labelpad=2)
    axes[2].set_xlabel("=  I", fontsize=11, labelpad=2)
    fig.suptitle("A · A⁻¹ always produces the identity matrix", fontsize=11)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


# ── Scalar Multiples of the Identity (cI) ────────────────────────────────────
st.markdown("##### Scalar Multiples of the Identity (cI)")
st.info(
    "Multiplying the identity by a scalar c produces a diagonal matrix with c on every diagonal "
    "entry. This scales all vectors uniformly. In practice, cI appears in **ridge regression** "
    "(adding λI to a covariance matrix to ensure invertibility) and **regularisation** more broadly."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, eye, latex

I = eye(3)
st.latex(r'I_3 = ' + latex(I))

for c in [2, 0.5, -1]:
    cI = c * I
    st.latex(rf'{c} \\cdot I = ' + latex(cI))
"""
    st.code(code, language="python")
    exec(code)
    st.info(
        "**Ridge regression regularisation:**\n\n"
        "Adding λI to a covariance matrix Σ guarantees invertibility even when Σ is singular:\n\n"
        r"$(\\Sigma + \\lambda I)^{-1}$ always exists for λ > 0"
    )

with col_right:
    scalars = [0.5, 1, 2, 3]
    fig, axes = plt.subplots(1, 4, figsize=(9, 3))
    for ax, c in zip(axes, scalars):
        matrix_heatmap(ax, c * np.eye(3), f"{c}·I₃")
    fig.suptitle("Scalar multiples of I — uniform scaling on diagonal", fontsize=11)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    # geometric: show how cI scales vectors uniformly
    fig2, axes2 = plt.subplots(1, 2, figsize=(7, 3))
    for ax in axes2:
        ax.axhline(0, color="grey", linewidth=0.5)
        ax.axvline(0, color="grey", linewidth=0.5)
        ax.set_aspect("equal")
        ax.grid(True, alpha=0.3)

    plot_transformed_shape(
        axes2[0], np.eye(2), UNIT_SQUARE, "royalblue", "I × unit square"
    )
    axes2[0].set_title("I  (no scaling)", fontsize=10)
    axes2[0].legend(fontsize=8)

    plot_transformed_shape(
        axes2[1], 2 * np.eye(2), UNIT_SQUARE, "tomato", "2I × unit square"
    )
    axes2[1].set_title("2I  (uniform scale ×2)", fontsize=10)
    axes2[1].legend(fontsize=8)

    for ax in axes2:
        ax.set_xlim(-0.5, 3)
        ax.set_ylim(-0.5, 3)

    fig2.suptitle("cI scales space uniformly in all directions", fontsize=11)
    plt.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)
