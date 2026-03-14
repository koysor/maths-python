import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Linear Algebra Matrix Multiplication", page_icon="📐", layout="wide"
)
st.header("Linear Algebra Matrix Multiplication")


def matrix_heatmap(ax, data, title, highlight_row=None, highlight_col=None):
    """Draw an annotated heatmap for a matrix, with optional row/col highlighting."""
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
    if highlight_row is not None:
        for j in range(data.shape[1]):
            ax.add_patch(
                plt.Rectangle(
                    (j - 0.5, highlight_row - 0.5),
                    1,
                    1,
                    fill=False,
                    edgecolor="gold",
                    linewidth=3,
                )
            )
    if highlight_col is not None:
        for i in range(data.shape[0]):
            ax.add_patch(
                plt.Rectangle(
                    (highlight_col - 0.5, i - 0.5),
                    1,
                    1,
                    fill=False,
                    edgecolor="limegreen",
                    linewidth=3,
                )
            )
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title, fontsize=11)
    return im


# ── Summary ──────────────────────────────────────────────────────────────────
st.markdown("##### Summary")
st.info(
    "Unlike scalar multiplication, matrix multiplication combines two matrices by computing "
    "dot products of rows and columns. It allows us to compose transformations, model "
    "relationships between variables, and perform complex calculations efficiently."
)

st.markdown("##### Dimensions Rule")
st.info(
    "Matrices can be multiplied together only if the **number of columns** in the first "
    "matrix equals the **number of rows** in the second. If A is n×m and B is m×k, "
    "then C = AB is n×k. The order matters: in general AB ≠ BA."
)

col_left, col_right = st.columns(2)

with col_left:
    st.markdown("""
**$$AB = C$$**
- A has size **n × m**
- B has size **m × k**
- C has size **n × k**

Each element $C_{ij}$ is the dot product of row $i$ of A with column $j$ of B:

$$C_{ij} = \\sum_{k} A_{ik} B_{kj}$$
""")

with col_right:
    # Illustrate compatible dimensions schematically
    fig, ax = plt.subplots(figsize=(5, 2.5))
    ax.axis("off")
    style = dict(
        ha="center",
        va="center",
        fontsize=13,
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.4", alpha=0.15),
    )
    ax.text(0.15, 0.6, "A\n(n × m)", color="royalblue", transform=ax.transAxes, **style)
    ax.text(0.45, 0.6, "B\n(m × k)", color="tomato", transform=ax.transAxes, **style)
    ax.text(0.75, 0.6, "C\n(n × k)", color="seagreen", transform=ax.transAxes, **style)
    ax.text(
        0.31, 0.6, "×", transform=ax.transAxes, ha="center", va="center", fontsize=16
    )
    ax.text(
        0.60, 0.6, "=", transform=ax.transAxes, ha="center", va="center", fontsize=16
    )
    ax.annotate(
        "",
        xy=(0.55, 0.25),
        xytext=(0.15, 0.25),
        xycoords="axes fraction",
        arrowprops=dict(arrowstyle="<->", color="royalblue", lw=1.5),
    )
    ax.text(
        0.35,
        0.18,
        "shared dimension (m)",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=9,
        color="grey",
    )
    ax.set_title("Dimension compatibility", fontsize=11)
    st.pyplot(fig)
    plt.close(fig)


# ── SymPy Example ────────────────────────────────────────────────────────────
st.markdown("##### Example of Matrix Multiplication with SymPy")
st.info(
    "SymPy performs exact symbolic arithmetic — results are kept as exact integers or "
    "fractions rather than floating-point approximations."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex

A = Matrix([[5, -1, 2], [8, 3, -4]])
st.latex(r'A = ' + latex(A))

B = Matrix([[2, 2], [9, -3], [7, 4]])
st.latex(r'B = ' + latex(B))

C = A * B
st.latex(r'C = AB = ' + latex(C))
"""
    st.code(code, language="python")
    exec(code)
    st.write(
        "A is a **2×3** matrix and B is a **3×2** matrix, so C is a **2×2** matrix."
    )

with col_right:
    A = np.array([[5, -1, 2], [8, 3, -4]], dtype=float)
    B = np.array([[2, 2], [9, -3], [7, 4]], dtype=float)
    C = A @ B
    fig, axes = plt.subplots(1, 3, figsize=(7, 3))
    matrix_heatmap(axes[0], A, "A  (2×3)")
    matrix_heatmap(axes[1], B, "B  (3×2)")
    matrix_heatmap(axes[2], C, "C = AB  (2×2)")
    axes[1].set_xlabel("×", fontsize=18, labelpad=2)
    axes[2].set_xlabel("=  AB", fontsize=11, labelpad=2)
    fig.suptitle("Matrix Multiplication — A (2×3) × B (3×2) = C (2×2)", fontsize=10)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    st.info("""**Top left** C[0,0] — row 0 of A · col 0 of B:
- 5×2 + (−1)×9 + 2×7 = 10 − 9 + 14 = **15**""")
    st.info("""**Top right** C[0,1] — row 0 of A · col 1 of B:
- 5×2 + (−1)×(−3) + 2×4 = 10 + 3 + 8 = **21**""")
    st.info("""**Bottom left** C[1,0] — row 1 of A · col 0 of B:
- 8×2 + 3×9 + (−4)×7 = 16 + 27 − 28 = **15**""")
    st.info("""**Bottom right** C[1,1] — row 1 of A · col 1 of B:
- 8×2 + 3×(−3) + (−4)×4 = 16 − 9 − 16 = **−9**""")


# ── NumPy Example ─────────────────────────────────────────────────────────────
st.markdown("##### Example of Matrix Multiplication with NumPy")
st.info(
    "NumPy uses floating-point arithmetic and is significantly faster than SymPy for "
    "large matrices. Use `np.dot()` or the `@` operator for matrix multiplication."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import latex, Matrix
import numpy as np

A = np.array([[5, -1, 2], [8, 3, -4]])
B = np.array([[2, 2], [9, -3], [7, 4]])

C = np.dot(A, B)
st.write(str(type(C)))
st.latex(r'C = AB = ' + latex(Matrix(C)))
"""
    st.code(code, language="python")
    exec(code)

with col_right:
    A = np.array([[5, -1, 2], [8, 3, -4]], dtype=float)
    B = np.array([[2, 2], [9, -3], [7, 4]], dtype=float)
    C = np.dot(A, B)
    fig, axes = plt.subplots(1, 3, figsize=(7, 3))
    matrix_heatmap(axes[0], A, "A  (2×3)")
    matrix_heatmap(axes[1], B, "B  (3×2)")
    matrix_heatmap(axes[2], C, "C = np.dot(A, B)")
    axes[1].set_xlabel("×", fontsize=18, labelpad=2)
    axes[2].set_xlabel("=  np.dot(A, B)", fontsize=10, labelpad=2)
    fig.suptitle("NumPy dot product — same result as SymPy", fontsize=10)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
