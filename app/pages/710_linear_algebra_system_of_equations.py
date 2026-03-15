import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Linear Algebra - System of Equations", page_icon="📐", layout="wide"
)
st.header("Linear Algebra - Solving Systems of Equations")


def matrix_heatmap(ax, data, title):
    """Draw an annotated heatmap for a matrix."""
    data = np.array(data, dtype=float)
    abs_max = np.abs(data).max() or 1
    if data.min() < 0:
        ax.imshow(data, cmap="RdBu_r", aspect="equal", vmin=-abs_max, vmax=abs_max)
    else:
        ax.imshow(data, cmap="Blues", aspect="equal", vmin=0, vmax=abs_max * 2)
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


# ── Introduction ───────────────────────────────────────────────────────────────
col_left, col_right = st.columns(2)

with col_left:
    st.info(
        "A **system of equations** is a set of equations sharing the same variables. "
        "A solution is a set of values for those variables that simultaneously satisfies every equation.\n\n"
        "Any linear system can be written in matrix form as **Ax = b**, where:\n"
        "- **A** is the matrix of coefficients\n"
        "- **x** is the vector of unknowns\n"
        "- **b** is the vector of constants\n\n"
        "A **unique solution** exists when the determinant of A is non-zero: **det(A) ≠ 0**. "
        "In that case the solution is **x = A⁻¹b**."
    )

with col_right:
    st.markdown("##### Writing the system in matrix form")
    code = """
import streamlit as st
from sympy import Matrix, symbols, latex

x, y = symbols('x y')

A = Matrix([[2, 1], [1, -3]])
xv = Matrix([x, y])
b = Matrix([5, 1])

st.latex(r'2x + y = 5')
st.latex(r'x - 3y = 1')
st.latex(r'\\Rightarrow Ax = b \\text{ where }')
st.latex(r'A = ' + latex(A) + r',\\quad x = ' + latex(xv) + r',\\quad b = ' + latex(b))
"""
    st.code(code, language="python")
    exec(code)


# ── Step-by-step solution ──────────────────────────────────────────────────────
st.divider()
st.subheader("Step-by-step Solution")

# Step 1 — Write as Ax = b
st.markdown("##### Step 1 — Write as Ax = b")
col_left, col_right = st.columns(2)

with col_left:
    st.info(
        "Arrange the coefficients of each equation into matrix A, the unknowns into vector x, "
        "and the right-hand side constants into vector b."
    )
    st.latex(r"""
\underbrace{\begin{bmatrix} 2 & 1 \\ 1 & -3 \end{bmatrix}}_{A}
\underbrace{\begin{bmatrix} x \\ y \end{bmatrix}}_{\mathbf{x}}
=
\underbrace{\begin{bmatrix} 5 \\ 1 \end{bmatrix}}_{\mathbf{b}}
""")

with col_right:
    A_np = np.array([[2, 1], [1, -3]], dtype=float)
    b_np = np.array([[5], [1]], dtype=float)
    x_placeholder = np.array([[1], [1]], dtype=float)  # visual placeholder

    fig, axes = plt.subplots(1, 3, figsize=(7, 3))
    matrix_heatmap(axes[0], A_np, "A  (2×2 coefficients)")
    matrix_heatmap(axes[1], x_placeholder, "x  (unknowns)")
    matrix_heatmap(axes[2], b_np, "b  (constants)")
    axes[1].set_xlabel("·", fontsize=18, labelpad=2)
    axes[2].set_xlabel("=  b", fontsize=11, labelpad=2)
    fig.suptitle("Ax = b — coefficient matrix, unknowns, constants", fontsize=11)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


# Step 2 — Compute det(A) and A⁻¹
st.markdown("##### Step 2 — Compute det(A) and A⁻¹")
col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex

A = Matrix([[2, 1], [1, -3]])

det_A = A.det()
st.latex(r'\\det(A) = ' + latex(det_A))

A_inv = A.inv()
st.latex(r'A^{-1} = ' + latex(A_inv))
"""
    st.code(code, language="python")
    exec(code)
    st.info(
        "det(A) = −7 ≠ 0, so a unique solution exists. "
        "The inverse A⁻¹ is computed symbolically, giving exact fractions."
    )

with col_right:
    A_inv_np = np.linalg.inv(A_np)
    fig, axes = plt.subplots(1, 2, figsize=(6, 3))
    matrix_heatmap(axes[0], A_np, "A")
    matrix_heatmap(axes[1], A_inv_np, "A⁻¹")
    axes[1].set_xlabel("inverse →", fontsize=10, labelpad=4)
    fig.suptitle("A and its inverse A⁻¹", fontsize=11)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


# Step 3 — Solve x = A⁻¹b
st.markdown("##### Step 3 — Solve x = A⁻¹b")
col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex

A = Matrix([[2, 1], [1, -3]])
b = Matrix([5, 1])

solution = A.inv() * b
st.latex(r'\\mathbf{x} = A^{-1}\\mathbf{b} = ' + latex(solution))
st.latex(r'x = ' + latex(solution[0]) + r',\\quad y = ' + latex(solution[1]))
"""
    st.code(code, language="python")
    exec(code)
    st.info("The exact solution is **x = 16/7** and **y = 3/7**.")

with col_right:
    solution_np = np.linalg.solve(A_np, b_np)
    fig, ax = plt.subplots(figsize=(2.5, 3))
    matrix_heatmap(ax, solution_np, "x = A⁻¹b")
    ax.set_xlabel("solution vector", fontsize=10, labelpad=4)
    fig.suptitle("Exact solution (decimal approximation)", fontsize=10)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


# ── Geometric interpretation ───────────────────────────────────────────────────
st.divider()
st.header("Geometric Interpretation")

col_left, col_right = st.columns([2, 3])

with col_left:
    st.info(
        "Each equation in a 2D linear system defines a **straight line** in the plane. "
        "The solution to the system is the point where the two lines **intersect**.\n\n"
        "- **Line 1:** 2x + y = 5  →  y = 5 − 2x\n"
        "- **Line 2:** x − 3y = 1  →  y = (x − 1) / 3\n\n"
        "These lines cross at exactly one point because det(A) ≠ 0. "
        "If det(A) = 0, the lines would be parallel (no solution) or coincident (infinitely many solutions)."
    )

with col_right:
    x_vals = np.linspace(-1, 4, 300)
    y1 = 5 - 2 * x_vals  # 2x + y = 5
    y2 = (x_vals - 1) / 3  # x - 3y = 1

    x_sol = 16 / 7
    y_sol = 3 / 7

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x_vals, y1, color="royalblue", linewidth=2, label=r"$2x + y = 5$")
    ax.plot(x_vals, y2, color="darkorange", linewidth=2, label=r"$x - 3y = 1$")
    ax.scatter([x_sol], [y_sol], color="crimson", zorder=5, s=80)
    ax.annotate(
        f"({x_sol:.4f}, {y_sol:.4f})\n= (16/7, 3/7)",
        xy=(x_sol, y_sol),
        xytext=(x_sol + 0.3, y_sol + 0.5),
        fontsize=9,
        color="crimson",
        arrowprops=dict(arrowstyle="->", color="crimson", lw=1.2),
    )
    ax.axhline(0, color="grey", linewidth=0.5)
    ax.axvline(0, color="grey", linewidth=0.5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Geometric interpretation — two lines intersecting at the solution")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
