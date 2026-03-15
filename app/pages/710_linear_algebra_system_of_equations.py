"""
Linear Algebra — Solving Systems of Equations
==============================================

Covers the matrix form Ax = b for 2×2 linear systems, including:

- Writing a system in matrix form
- Computing the determinant and matrix inverse
- Solving x = A⁻¹b symbolically (SymPy) and numerically (NumPy)
- The numpy.linalg.solve alternative and its LU decomposition basis
- Geometric interpretation of solutions as line intersections
- Behaviour when det(A) = 0 (parallel and coincident lines)
- Interactive explorer with adjustable coefficients
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Linear Algebra - System of Equations", page_icon="📐", layout="wide"
)
st.header("Linear Algebra - Solving Systems of Equations")


def matrix_heatmap(ax, data, title):
    """
    Draw an annotated heatmap for a matrix on the given Axes.

    Uses a diverging colourmap (RdBu_r) when the data contains negative
    values, and a sequential colourmap (Blues) otherwise.  Each cell is
    labelled with its value formatted to four significant figures.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes to draw on.
    data : array-like
        The matrix values to visualise.
    title : str
        Title displayed above the heatmap.
    """
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
col_left, col_right = st.columns([2, 3])

with col_left:
    st.info(
        "A **system of equations** is a set of equations sharing the same variables.  "
        "A solution is a set of values for those variables that simultaneously satisfies every equation.\n\n"
        "Any linear system can be written in matrix form as **Ax = b**, where:\n"
        "- **A** is the matrix of coefficients\n"
        "- **x** is the vector of unknowns\n"
        "- **b** is the vector of constants\n\n"
        "A **unique solution** exists when the determinant of A is non-zero: **det(A) ≠ 0**.  "
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

A_np = np.array([[2, 1], [1, -3]], dtype=float)
b_np = np.array([[5], [1]], dtype=float)

step1_code = """
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

A_np = np.array([[2, 1], [1, -3]], dtype=float)
b_np = np.array([[5], [1]], dtype=float)
x_placeholder = np.array([[1], [1]], dtype=float)

fig, axes = plt.subplots(1, 3, figsize=(7, 3))
matrix_heatmap(axes[0], A_np, "A  (coefficients)")
matrix_heatmap(axes[1], x_placeholder, "x  (unknowns)")
matrix_heatmap(axes[2], b_np, "b  (constants)")
fig.suptitle("Ax = b — coefficient matrix, unknowns, constants", fontsize=11)
plt.tight_layout()
st.pyplot(fig)
plt.close(fig)
"""

with col_right:
    st.code(step1_code, language="python")
    exec(step1_code)


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
    st.markdown("For a 2×2 matrix the determinant is:")
    st.latex(r"\det\begin{bmatrix}a & b \\ c & d\end{bmatrix} = ad - bc")
    st.markdown("Applying this to A:")
    st.latex(r"\det(A) = (2)(-3) - (1)(1) = -6 - 1 = -7")
    st.info(
        "det(A) = −7 ≠ 0, so a unique solution exists.  "
        "The inverse A⁻¹ is computed symbolically, giving exact fractions."
    )
    st.markdown("For a 2×2 matrix the inverse is:")
    st.latex(
        r"\begin{bmatrix}a & b \\ c & d\end{bmatrix}^{-1}"
        r"= \frac{1}{ad-bc}\begin{bmatrix}d & -b \\ -c & a\end{bmatrix}"
    )
    st.markdown("Applying this to A:")
    st.latex(
        r"A^{-1} = \frac{1}{-7}\begin{bmatrix}-3 & -1 \\ -1 & 2\end{bmatrix}"
        r"= \begin{bmatrix}3/7 & 1/7 \\ 1/7 & -2/7\end{bmatrix}"
    )

step2_code = """
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

A_np = np.array([[2, 1], [1, -3]], dtype=float)
A_inv_np = np.linalg.inv(A_np)

fig, axes = plt.subplots(1, 2, figsize=(6, 3))
matrix_heatmap(axes[0], A_np, "A")
matrix_heatmap(axes[1], A_inv_np, "A⁻¹")
fig.suptitle("A and its inverse A⁻¹", fontsize=11)
plt.tight_layout()
st.pyplot(fig)
plt.close(fig)
"""

with col_right:
    st.code(step2_code, language="python")
    exec(step2_code)


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
    st.markdown(
        "**Why does this work?**\n\n"
        "Think of A as a transformation: it takes the unknown vector **x** and maps it to **b**.  "
        "A⁻¹ is the transformation that *undoes* A — just as dividing by a number undoes multiplication:\n\n"
        "If $\\ 3x = 12$, then $x = \\frac{1}{3} \\times 12 = 4$.\n\n"
        "The same logic applies in matrix form:"
    )
    st.latex(
        r"A\mathbf{x} = \mathbf{b}"
        r"\;\Rightarrow\;"
        r"A^{-1}A\mathbf{x} = A^{-1}\mathbf{b}"
        r"\;\Rightarrow\;"
        r"I\mathbf{x} = A^{-1}\mathbf{b}"
        r"\;\Rightarrow\;"
        r"\mathbf{x} = A^{-1}\mathbf{b}"
    )
    st.markdown(
        "Multiplying both sides by A⁻¹ on the left cancels A (since A⁻¹A = I, the identity matrix), "
        "leaving **x** isolated on the left and A⁻¹**b** on the right."
    )

step3_code = """
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

A_np = np.array([[2, 1], [1, -3]], dtype=float)
b_np = np.array([[5], [1]], dtype=float)
solution_np = np.linalg.solve(A_np, b_np)

fig, ax = plt.subplots(figsize=(2.5, 3))
matrix_heatmap(ax, solution_np, "x = A⁻¹b")
fig.suptitle("Solution vector (decimal)", fontsize=10)
plt.tight_layout()
st.pyplot(fig)
plt.close(fig)
"""

with col_right:
    st.code(step3_code, language="python")
    exec(step3_code)


# ── Alternative: numpy.linalg.solve ───────────────────────────────────────────
st.divider()
st.subheader("Alternative: `numpy.linalg.solve`")

col_left, col_right = st.columns(2)

with col_left:
    st.info(
        "In practice, explicitly computing A⁻¹ is avoided — it is numerically unstable and slow for large matrices.  "
        "`numpy.linalg.solve` uses LU decomposition internally, which is faster and more accurate.  "
        "It solves **Ax = b** directly without forming A⁻¹."
    )
    st.markdown(
        "**What is LU decomposition?**\n\n"
        "LU decomposition splits A into two simpler matrices:\n\n"
        "- **L** (Lower triangular) — a matrix with zeros above the diagonal\n"
        "- **U** (Upper triangular) — a matrix with zeros below the diagonal\n\n"
        "so that **A = LU**.  "
        "Triangular matrices are much easier to solve than a general matrix — you just substitute values in from one end, "
        "a process called *forward substitution* (for L) and *back substitution* (for U).\n\n"
        "So instead of solving **Ax = b** in one hard step, the approach breaks it into two easy steps:\n\n"
        "1. Solve **Ly = b** for **y** using forward substitution\n"
        "2. Solve **Ux = y** for **x** using back substitution\n\n"
        "Think of it like factoring a number: solving 12x = 60 is harder to reason about than "
        "splitting it into 3 × 4 × x = 60 and peeling off one factor at a time."
    )

with col_right:
    code = """
import streamlit as st
import numpy as np

A = np.array([[2, 1], [1, -3]], dtype=float)
b = np.array([5, 1], dtype=float)

x = np.linalg.solve(A, b)
st.latex(r'x = ' + f'{x[0]:.6f}' + r',\\quad y = ' + f'{x[1]:.6f}')
"""
    st.code(code, language="python")
    exec(code)


# ── Geometric interpretation ───────────────────────────────────────────────────
st.divider()
st.header("Geometric Interpretation")

col_left, col_right = st.columns([2, 3])

geo_code = """
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

A = np.array([[2, 1], [1, -3]], dtype=float)
b = np.array([5, 1], dtype=float)
x_sol, y_sol = np.linalg.solve(A, b)

x_vals = np.linspace(-1, 4, 300)
y1 = 5 - 2 * x_vals       # 2x + y = 5  →  y = 5 - 2x
y2 = (x_vals - 1) / 3     # x - 3y = 1  →  y = (x - 1) / 3

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x_vals, y1, color="royalblue", linewidth=2, label=r"$2x + y = 5$")
ax.plot(x_vals, y2, color="darkorange", linewidth=2, label=r"$x - 3y = 1$")
ax.scatter([x_sol], [y_sol], color="crimson", zorder=5, s=80)
ax.annotate(
    f"({x_sol:.4f}, {y_sol:.4f})\\n= (16/7, 3/7)",
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
"""

with col_left:
    st.info(
        "Each equation in a 2D linear system defines a **straight line** in the plane.  "
        "The solution to the system is the point where the two lines **intersect**.\n\n"
        "- **Line 1:** 2x + y = 5  →  y = 5 − 2x\n"
        "- **Line 2:** x − 3y = 1  →  y = (x − 1) / 3\n\n"
        "These lines cross at exactly one point because det(A) ≠ 0.  "
        "If det(A) = 0, the lines would be parallel (no solution) or coincident (infinitely many solutions)."
    )
    st.code(geo_code, language="python")

with col_right:
    exec(geo_code)


# ── det(A) = 0: no solution / infinite solutions ───────────────────────────────
st.divider()
st.subheader("When det(A) = 0 — No Unique Solution")

st.info(
    "When det(A) = 0, the two lines are either **parallel** (no solution) or **coincident** (infinitely many solutions).  "
    "In both cases `numpy.linalg.solve` raises a `LinAlgError: Singular matrix`."
)

col_left, col_right = st.columns(2)

parallel_code = """
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

xv = np.linspace(-1, 4, 300)
fig, ax = plt.subplots(figsize=(5, 3.5))
ax.plot(xv, (3 - xv) / 2, color="royalblue", linewidth=2, label=r"$x+2y=3$")
ax.plot(xv, (5 - xv) / 2, color="darkorange", linewidth=2, label=r"$x+2y=5$")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Parallel lines — no intersection")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
st.pyplot(fig)
plt.close(fig)
"""

coincident_code = """
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

xv = np.linspace(-1, 4, 300)
fig, ax = plt.subplots(figsize=(5, 3.5))
ax.plot(xv, (3 - xv) / 2, color="royalblue", linewidth=4, alpha=0.4, label=r"$x+2y=3$")
ax.plot(xv, (6 - 2 * xv) / 4, color="darkorange", linewidth=2, linestyle="--", label=r"$2x+4y=6$")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Coincident lines — infinitely many solutions")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
st.pyplot(fig)
plt.close(fig)
"""

with col_left:
    st.markdown("**Parallel lines — no solution**")
    st.latex(r"""
\begin{cases} x + 2y = 3 \\ x + 2y = 5 \end{cases}
\quad\Rightarrow\quad
A = \begin{bmatrix}1 & 2\\1 & 2\end{bmatrix},\;\det(A)=0
""")
    st.code(parallel_code, language="python")
    exec(parallel_code)

with col_right:
    st.markdown("**Coincident lines — infinitely many solutions**")
    st.latex(r"""
\begin{cases} x + 2y = 3 \\ 2x + 4y = 6 \end{cases}
\quad\Rightarrow\quad
A = \begin{bmatrix}1 & 2\\2 & 4\end{bmatrix},\;\det(A)=0
""")
    st.code(coincident_code, language="python")
    exec(coincident_code)


# ── Interactive explorer ───────────────────────────────────────────────────────
st.divider()
st.header("Interactive Explorer")

st.info(
    "Adjust the coefficients of A and the constants b to explore how the system changes.  "
    "When det(A) is close to zero, watch the lines become nearly parallel and the solution move to infinity."
)

col_sliders, col_plot = st.columns([1, 2])

with col_sliders:
    st.markdown("**Matrix A**")
    c1, c2 = st.columns(2)
    with c1:
        a11 = st.slider("a₁₁", -5.0, 5.0, 2.0, 0.5)
        a21 = st.slider("a₂₁", -5.0, 5.0, 1.0, 0.5)
    with c2:
        a12 = st.slider("a₁₂", -5.0, 5.0, 1.0, 0.5)
        a22 = st.slider("a₂₂", -5.0, 5.0, -3.0, 0.5)

    st.markdown("**Vector b**")
    b1 = st.slider("b₁", -10.0, 10.0, 5.0, 0.5)
    b2 = st.slider("b₂", -10.0, 10.0, 1.0, 0.5)

A_i = np.array([[a11, a12], [a21, a22]], dtype=float)
b_i = np.array([[b1], [b2]], dtype=float)
det_i = np.linalg.det(A_i)

with col_plot:
    st.latex(
        rf"A = \begin{{bmatrix}} {a11} & {a12} \\ {a21} & {a22} \end{{bmatrix}}, "
        rf"\quad b = \begin{{bmatrix}} {b1} \\ {b2} \end{{bmatrix}}, "
        rf"\quad \det(A) = {det_i:.4f}"
    )

    fig, ax = plt.subplots(figsize=(6, 4))
    xv = np.linspace(-10, 10, 500)

    # Line 1: a11*x + a12*y = b1  →  y = (b1 - a11*x) / a12
    if abs(a12) > 1e-9:
        ax.plot(
            xv,
            (b1 - a11 * xv) / a12,
            color="royalblue",
            linewidth=2,
            label=rf"${a11}x + {a12}y = {b1}$",
        )
    elif abs(a11) > 1e-9:
        ax.axvline(
            b1 / a11, color="royalblue", linewidth=2, label=rf"${a11}x + {a12}y = {b1}$"
        )

    # Line 2: a21*x + a22*y = b2  →  y = (b2 - a21*x) / a22
    if abs(a22) > 1e-9:
        ax.plot(
            xv,
            (b2 - a21 * xv) / a22,
            color="darkorange",
            linewidth=2,
            label=rf"${a21}x + {a22}y = {b2}$",
        )
    elif abs(a21) > 1e-9:
        ax.axvline(
            b2 / a21,
            color="darkorange",
            linewidth=2,
            label=rf"${a21}x + {a22}y = {b2}$",
        )

    if abs(det_i) > 1e-9:
        sol_i = np.linalg.solve(A_i, b_i.ravel())
        if -10 <= sol_i[0] <= 10 and -10 <= sol_i[1] <= 10:
            ax.scatter([sol_i[0]], [sol_i[1]], color="crimson", zorder=5, s=80)
            ax.annotate(
                f"({sol_i[0]:.3f}, {sol_i[1]:.3f})",
                xy=(sol_i[0], sol_i[1]),
                xytext=(sol_i[0] + 0.5, sol_i[1] + 0.5),
                fontsize=9,
                color="crimson",
                arrowprops=dict(arrowstyle="->", color="crimson", lw=1.2),
            )
        st.success(f"Unique solution: x = {sol_i[0]:.4f}, y = {sol_i[1]:.4f}")
    else:
        st.error(
            "det(A) ≈ 0 — no unique solution exists (lines are parallel or coincident)."
        )

    ax.axhline(0, color="grey", linewidth=0.5)
    ax.axvline(0, color="grey", linewidth=0.5)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
