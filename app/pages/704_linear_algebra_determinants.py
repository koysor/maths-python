import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Linear Algebra Determinants", page_icon="📐", layout="wide"
)
st.header("Linear Algebra Determinants")


def plot_parallelogram(ax, col1, col2, det, title):
    """Plot the parallelogram formed by two column vectors, labelled with the determinant."""
    origin = np.zeros(2)
    para = np.array([origin, col1, col1 + col2, col2, origin])
    color = "royalblue" if det >= 0 else "tomato"
    ax.fill(para[:, 0], para[:, 1], alpha=0.2, color=color)
    ax.plot(para[:, 0], para[:, 1], color=color, linewidth=1.5)
    ax.quiver(
        *origin,
        *col1,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="royalblue",
        label=f"col 1: {tuple(col1.astype(int))}",
    )
    ax.quiver(
        *origin,
        *col2,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="seagreen",
        label=f"col 2: {tuple(col2.astype(int))}",
    )
    cx, cy = (col1 + col2) / 2
    ax.text(
        cx,
        cy,
        f"area = |det| = {abs(det):.4g}\ndet = {det:.4g}",
        ha="center",
        va="center",
        fontsize=9,
        color="navy",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
    )
    all_pts = np.array([origin, col1, col2, col1 + col2])
    pad = 1
    ax.set_xlim(all_pts[:, 0].min() - pad, all_pts[:, 0].max() + pad)
    ax.set_ylim(all_pts[:, 1].min() - pad, all_pts[:, 1].max() + pad)
    ax.axhline(0, color="grey", linewidth=0.5)
    ax.axvline(0, color="grey", linewidth=0.5)
    ax.set_aspect("equal")
    ax.legend(fontsize=9)
    ax.set_title(title, fontsize=10)
    ax.grid(True, alpha=0.3)


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
    fig, ax = plt.subplots(figsize=(5, 4))
    plot_parallelogram(
        ax,
        np.array([2.0, 0.5]),
        np.array([1.0, 2.0]),
        3.5,
        "det M = signed area of parallelogram (schematic)",
    )
    st.pyplot(fig)
    plt.close(fig)


# ── 2×2 Example ───────────────────────────────────────────────────────────────
st.markdown("##### 2×2 Example")
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
    det = np.linalg.det(A)
    fig, ax = plt.subplots(figsize=(5, 4))
    plot_parallelogram(
        ax, A[:, 0], A[:, 1], det, f"A = [[6,5],[1,2]] — det A = {det:.4g}"
    )
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


# ── 3×3 Determinant ───────────────────────────────────────────────────────────
st.markdown("##### 3×3 Determinant")
st.info(
    "For a 3×3 matrix the determinant is computed by cofactor expansion along the first row. "
    "Each element in the top row is multiplied by the determinant of the 2×2 submatrix "
    "remaining after removing that element's row and column, alternating signs. "
    "Geometrically, |det| equals the volume of the parallelepiped formed by the three column vectors."
)

col_left, col_right = st.columns(2)

with col_left:
    st.latex(r"""
M = \begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix}
""")
    st.latex(r"""
\det M = a(ei - fh) - b(di - fg) + c(dh - eg)
""")

    code = """
import streamlit as st
from sympy import Matrix, latex

A = Matrix([[2, -1, 3], [0, 4, -2], [1, 5, 6]])
st.latex(r'A = ' + latex(A))

det_A = A.det()
st.latex(r'\\det A = ' + latex(det_A))
"""
    st.code(code, language="python")
    exec(code)
    st.latex(r"""
\det A = 2(4 \times 6 - (-2) \times 5) - (-1)(0 \times 6 - (-2) \times 1) + 3(0 \times 5 - 4 \times 1)
= 2(34) + 1(-2) + 3(-4) = 68 - 2 - 12 = 54
""")

with col_right:
    A3 = np.array([[2, -1, 3], [0, 4, -2], [1, 5, 6]], dtype=float)
    c1, c2, c3 = A3[:, 0], A3[:, 1], A3[:, 2]
    det3 = np.linalg.det(A3)

    fig = plt.figure(figsize=(5, 5))
    ax3d = fig.add_subplot(111, projection="3d")
    origin = np.zeros(3)

    for vec, color, label in [
        (c1, "royalblue", "col 1"),
        (c2, "seagreen", "col 2"),
        (c3, "tomato", "col 3"),
    ]:
        ax3d.quiver(*origin, *vec, color=color, label=label, arrow_length_ratio=0.1)

    # draw parallelepiped edges
    verts = [c1, c2, c3, c1 + c2, c1 + c3, c2 + c3, c1 + c2 + c3]
    edges = [
        (origin, c1),
        (origin, c2),
        (origin, c3),
        (c1, c1 + c2),
        (c1, c1 + c3),
        (c2, c1 + c2),
        (c2, c2 + c3),
        (c3, c1 + c3),
        (c3, c2 + c3),
        (c1 + c2, c1 + c2 + c3),
        (c1 + c3, c1 + c2 + c3),
        (c2 + c3, c1 + c2 + c3),
    ]
    for start, end in edges:
        ax3d.plot(*zip(start, end), color="royalblue", alpha=0.3, linewidth=0.8)

    ax3d.set_xlabel("X")
    ax3d.set_ylabel("Y")
    ax3d.set_zlabel("Z")
    ax3d.legend(fontsize=8)
    ax3d.set_title(f"Parallelepiped — volume = |det| = {abs(det3):.4g}", fontsize=10)
    st.pyplot(fig)
    plt.close(fig)


# ── Singular Matrix ───────────────────────────────────────────────────────────
st.markdown("##### Singular Matrix (det = 0)")
st.info(
    "When the columns of a matrix are linearly dependent (one column is a multiple of another), "
    "the parallelogram collapses to a line and has zero area. The determinant is zero, "
    "the matrix is singular, and the system Ax = b either has no solution or infinitely many."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex

A = Matrix([[2, 4], [1, 2]])
st.latex(r'A = ' + latex(A))

det_A = A.det()
st.latex(r'\\det A = ' + latex(det_A))
"""
    st.code(code, language="python")
    exec(code)
    st.latex(r"\det A = 2 \times 2 - 4 \times 1 = 4 - 4 = 0")
    st.info("Column 2 = 2 × column 1, so the columns are linearly dependent.")

with col_right:
    A_sing = np.array([[2, 4], [1, 2]], dtype=float)
    det_sing = np.linalg.det(A_sing)
    c1, c2 = A_sing[:, 0], A_sing[:, 1]
    origin = np.zeros(2)

    fig, ax = plt.subplots(figsize=(5, 4))
    # parallelogram degenerates — draw the line
    ax.plot(
        [0, c1[0] + c2[0]],
        [0, c1[1] + c2[1]],
        "royalblue",
        linewidth=2,
        label="degenerate parallelogram (a line)",
    )
    ax.quiver(
        *origin,
        *c1,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="royalblue",
        label=f"col 1: {tuple(c1.astype(int))}",
    )
    ax.quiver(
        *origin,
        *c2,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="seagreen",
        label=f"col 2: {tuple(c2.astype(int))}",
    )
    ax.text(
        3,
        1,
        "det = 0\n(zero area)",
        ha="center",
        fontsize=10,
        color="navy",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
    )
    ax.set_xlim(-0.5, 7)
    ax.set_ylim(-0.5, 4)
    ax.axhline(0, color="grey", linewidth=0.5)
    ax.axvline(0, color="grey", linewidth=0.5)
    ax.set_aspect("equal")
    ax.legend(fontsize=9)
    ax.set_title("Singular matrix — columns collapse to a line", fontsize=10)
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    plt.close(fig)


# ── Negative Determinant ──────────────────────────────────────────────────────
st.markdown("##### Negative Determinant")
st.info(
    "A negative determinant means the transformation includes a reflection — "
    "the orientation of space is reversed. The magnitude |det| still gives the area/volume "
    "scaling factor, but the sign indicates the columns are arranged in clockwise order "
    "rather than anticlockwise."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex

A = Matrix([[1, 4], [2, 3]])
st.latex(r'A = ' + latex(A))

det_A = A.det()
st.latex(r'\\det A = ' + latex(det_A))
"""
    st.code(code, language="python")
    exec(code)
    st.latex(r"\det A = 1 \times 3 - 4 \times 2 = 3 - 8 = -5")
    st.info(
        "The area of the parallelogram is |−5| = 5, but the negative sign indicates "
        "the column vectors are arranged clockwise — orientation is reversed."
    )

with col_right:
    A_neg = np.array([[1, 4], [2, 3]], dtype=float)
    det_neg = np.linalg.det(A_neg)
    fig, ax = plt.subplots(figsize=(5, 4))
    plot_parallelogram(
        ax,
        A_neg[:, 0],
        A_neg[:, 1],
        det_neg,
        f"det A = {det_neg:.4g} — orientation reversed",
    )
    # annotate clockwise arrow
    ax.annotate(
        "clockwise\n(reflected)",
        xy=(2.5, 2),
        fontsize=9,
        color="tomato",
        ha="center",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
    )
    st.pyplot(fig)
    plt.close(fig)


# ── Key Properties ────────────────────────────────────────────────────────────
st.markdown("##### Key Properties")
st.info(
    "These properties allow determinants to be computed and reasoned about without "
    "always expanding the full formula. Each can be verified numerically with SymPy."
)

col_left, col_right = st.columns(2)

with col_left:
    st.markdown("""
| Property | Rule |
|---|---|
| Product | det(AB) = det(A) · det(B) |
| Transpose | det(Aᵀ) = det(A) |
| Scalar | det(cA) = cⁿ · det(A) for n×n |
| Inverse | det(A⁻¹) = 1 / det(A) |
| Identity | det(I) = 1 |
""")

with col_right:
    code = """
import streamlit as st
from sympy import Matrix, latex

A = Matrix([[3, 1], [2, 4]])
B = Matrix([[1, 2], [0, 3]])

st.latex(r'\\det(A) = ' + latex(A.det()))
st.latex(r'\\det(B) = ' + latex(B.det()))
st.latex(r'\\det(AB) = ' + latex((A * B).det()))
st.latex(r'\\det(A) \\cdot \\det(B) = ' + latex(A.det() * B.det()))
st.latex(r'\\det(A^T) = ' + latex(A.T.det()))
st.latex(r'\\det(2A) = ' + latex((2 * A).det()) + r'\\quad (= 2^2 \\cdot \\det A = ' + latex(4 * A.det()) + r')')
st.latex(r'\\det(A^{-1}) = ' + latex(A.inv().det()))
"""
    st.code(code, language="python")
    exec(code)
