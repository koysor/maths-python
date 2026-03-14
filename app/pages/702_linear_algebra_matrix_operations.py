import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Linear Algebra Matrix Operations", page_icon="📐", layout="wide"
)
st.header("Linear Algebra Matrix Operations")


def matrix_heatmap(ax, data, title):
    """Draw an annotated heatmap for a matrix."""
    im = ax.imshow(data, cmap="coolwarm", aspect="equal")
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
    return im


def transformed_square(ax, M, label, color, alpha=1.0):
    """Draw the image of the unit square under matrix M."""
    corners = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]).T
    transformed = M @ corners
    ax.plot(
        transformed[0],
        transformed[1],
        color=color,
        alpha=alpha,
        linewidth=2,
        label=label,
    )
    ax.fill(transformed[0, :-1], transformed[1, :-1], color=color, alpha=alpha * 0.15)


# ── Matrix Addition ──────────────────────────────────────────────────────────
st.markdown("##### Matrix Addition")
st.info(
    "Matrix addition combines two matrices of the same size by adding their corresponding elements. The result is a new matrix of the same size."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex
import numpy as np

A = Matrix([[2, -1], [0, 3]])
st.latex(r'A = ' + latex(A))

B = Matrix([[-1, 4], [5, 3]])
st.latex(r'B = ' + latex(B))

C = A + B
st.latex(r'C = A + B = ' + latex(C))

C_np = np.array(C).astype(np.float64)
st.write("C as numpy array:")
st.latex(latex(Matrix(C_np)))
"""
    st.code(code, language="python")
    exec(code)
    st.write(
        "It may be useful to convert the result to a NumPy array for further processing as NumPy offers superior performance."
    )
    st.info("""
Top row:
- 2 + (-1) = 1
- -1 + 4 = 3
\rBottom row:
- 0 + 5 = 5
- 3 + 3 = 6
""")

with col_right:
    A = np.array([[2, -1], [0, 3]], dtype=float)
    B = np.array([[-1, 4], [5, 3]], dtype=float)
    C = A + B
    fig, axes = plt.subplots(1, 3, figsize=(7, 3))
    matrix_heatmap(axes[0], A, "A")
    matrix_heatmap(axes[1], B, "B")
    matrix_heatmap(axes[2], C, "A + B")
    axes[1].set_xlabel("+", fontsize=18, labelpad=2)
    axes[2].set_xlabel("=  A + B", fontsize=11, labelpad=2)
    fig.suptitle("Matrix Addition — element by element", fontsize=11)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


# ── Matrix Subtraction ───────────────────────────────────────────────────────
st.markdown("##### Matrix Subtraction")
st.info(
    "Matrix subtraction works the same way as addition — subtract corresponding elements. Both matrices must be the same size."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex
import numpy as np

A = Matrix([[1, -3, 4], [2, 1, 1]])
st.latex(r'A = ' + latex(A))

B = Matrix([[0, 2, 1], [5, 2, 3]])
st.latex(r'B = ' + latex(B))

C = A - B
st.latex(r'C = A - B = ' + latex(C))
"""
    st.code(code, language="python")
    exec(code)
    st.info("You can only add or subtract matrices of the same size.")

with col_right:
    A = np.array([[1, -3, 4], [2, 1, 1]], dtype=float)
    B = np.array([[0, 2, 1], [5, 2, 3]], dtype=float)
    C = A - B
    fig, axes = plt.subplots(1, 3, figsize=(7, 3))
    matrix_heatmap(axes[0], A, "A")
    matrix_heatmap(axes[1], B, "B")
    matrix_heatmap(axes[2], C, "A − B")
    axes[1].set_xlabel("−", fontsize=18, labelpad=2)
    axes[2].set_xlabel("=  A − B", fontsize=11, labelpad=2)
    fig.suptitle("Matrix Subtraction — element by element", fontsize=11)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


# ── Scalar Multiplication (×2) ───────────────────────────────────────────────
st.markdown("##### Multiply a Matrix by a Scalar")
st.info(
    "Multiplying a matrix by a scalar multiplies every element by that number. Geometrically, it scales the linear transformation that the matrix represents — stretching or shrinking the space it acts on."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex
import numpy as np

A = Matrix([[1, 2], [-1, 0]])
st.latex(r'A = ' + latex(A))

C = 2*A
st.latex(r'C = 2A = ' + latex(C))
"""
    st.code(code, language="python")
    exec(code)
    st.info("""
Multiply each element by the scalar:
- Top row: 2×1 = 2, 2×2 = 4
- Bottom row: 2×(-1) = -2, 2×0 = 0
""")

with col_right:
    A = np.array([[1, 2], [-1, 0]], dtype=float)
    C = 2 * A
    fig, ax = plt.subplots(figsize=(5, 5))
    # unit square
    corners = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]).T
    ax.plot(corners[0], corners[1], "k--", linewidth=1, alpha=0.4, label="unit square")
    transformed_square(ax, A, "A × unit square", "royalblue")
    transformed_square(ax, C, "2A × unit square", "seagreen")
    ax.axhline(0, color="grey", linewidth=0.5)
    ax.axvline(0, color="grey", linewidth=0.5)
    ax.set_aspect("equal")
    ax.legend(fontsize=9)
    ax.set_title("Effect of scalar ×2 on matrix transformation")
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    plt.close(fig)


# ── Scalar Multiplication (×0.5) ─────────────────────────────────────────────
st.markdown("##### Multiply a Matrix by a Scalar (0.5)")
st.info(
    "Multiplying by a scalar between 0 and 1 shrinks the transformation. The shape of the transformed space is preserved but scaled down."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex
import numpy as np

A = Matrix([[4, 6], [8, 10]])
st.latex(r'A = ' + latex(A))

C = 0.5*A
st.latex(r'C = 0.5A = ' + latex(C))
"""
    st.code(code, language="python")
    exec(code)
    st.info("""
Multiply each element by 0.5:
- Top row: 0.5×4 = 2, 0.5×6 = 3
- Bottom row: 0.5×8 = 4, 0.5×10 = 5
""")

with col_right:
    A = np.array([[4, 6], [8, 10]], dtype=float)
    C = 0.5 * A
    fig, ax = plt.subplots(figsize=(5, 5))
    corners = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]).T
    ax.plot(corners[0], corners[1], "k--", linewidth=1, alpha=0.4, label="unit square")
    transformed_square(ax, A, "A × unit square", "royalblue")
    transformed_square(ax, C, "0.5A × unit square", "seagreen")
    ax.axhline(0, color="grey", linewidth=0.5)
    ax.axvline(0, color="grey", linewidth=0.5)
    ax.set_aspect("equal")
    ax.legend(fontsize=9)
    ax.set_title("Effect of scalar ×0.5 on matrix transformation")
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    plt.close(fig)
