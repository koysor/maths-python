import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

st.set_page_config(
    page_title="Linear Algebra Vector Operations", page_icon="📐", layout="wide"
)
st.header("Linear Algebra Vector Operations")


# ── Vector Addition ──────────────────────────────────────────────────────────
st.markdown("##### Vector Addition")
st.info(
    "Vector addition combines two vectors by adding their corresponding components. Geometrically, it is equivalent to placing the tail of one vector at the tip of the other and drawing the resultant vector."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex

a = Matrix([1, 3, -2])
st.latex(r'\\mathbf{a} = ' + latex(a))

b = Matrix([4, -1, 5])
st.latex(r'\\mathbf{b} = ' + latex(b))

c = a + b
st.latex(r'\\mathbf{c} = \\mathbf{a} + \\mathbf{b} = ' + latex(c))
"""
    st.code(code, language="python")
    exec(code)
    st.info("""
Add corresponding components:
- 1 + 4 = 5
- 3 + (-1) = 2
- (-2) + 5 = 3
""")

with col_right:
    a = np.array([1, 3])
    b = np.array([4, -1])
    c = a + b
    fig, ax = plt.subplots(figsize=(5, 5))
    origin = np.zeros(2)
    ax.quiver(
        *origin,
        *a,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="royalblue",
        label=r"$\mathbf{a}$",
    )
    ax.quiver(
        *a,
        *b,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="tomato",
        label=r"$\mathbf{b}$ (from tip of $\mathbf{a}$)",
    )
    ax.quiver(
        *origin,
        *c,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="seagreen",
        label=r"$\mathbf{a}+\mathbf{b}$",
    )
    lim = max(abs(c).max(), abs(a).max(), abs(b).max()) + 1
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.axhline(0, color="grey", linewidth=0.5)
    ax.axvline(0, color="grey", linewidth=0.5)
    ax.set_aspect("equal")
    ax.legend()
    ax.set_title("Vector Addition (2D projection)")
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    plt.close(fig)


# ── Vector Subtraction ───────────────────────────────────────────────────────
st.markdown("##### Vector Subtraction")
st.info(
    "Vector subtraction finds the difference between two vectors by subtracting corresponding components. Geometrically, it gives the vector pointing from the tip of one vector to the tip of the other."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex

a = Matrix([5, 2, -1])
st.latex(r'\\mathbf{a} = ' + latex(a))

b = Matrix([3, -4, 2])
st.latex(r'\\mathbf{b} = ' + latex(b))

c = a - b
st.latex(r'\\mathbf{c} = \\mathbf{a} - \\mathbf{b} = ' + latex(c))
"""
    st.code(code, language="python")
    exec(code)
    st.info("You can only add or subtract vectors of the same dimension.")

with col_right:
    a = np.array([5, 2])
    b = np.array([3, -4])
    c = a - b
    fig, ax = plt.subplots(figsize=(5, 5))
    origin = np.zeros(2)
    ax.quiver(
        *origin,
        *a,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="royalblue",
        label=r"$\mathbf{a}$",
    )
    ax.quiver(
        *origin,
        *b,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="tomato",
        label=r"$\mathbf{b}$",
    )
    ax.quiver(
        *b,
        *c,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="seagreen",
        label=r"$\mathbf{a}-\mathbf{b}$ (from tip of $\mathbf{b}$)",
    )
    lim = max(abs(a).max(), abs(b).max(), abs(c).max()) + 1
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.axhline(0, color="grey", linewidth=0.5)
    ax.axvline(0, color="grey", linewidth=0.5)
    ax.set_aspect("equal")
    ax.legend()
    ax.set_title("Vector Subtraction (2D projection)")
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    plt.close(fig)


# ── Scalar Multiplication ────────────────────────────────────────────────────
st.markdown("##### Multiply a Vector by a Scalar")
st.info(
    "Multiplying a vector by a scalar stretches or shrinks it by that factor. The direction stays the same for positive scalars, reverses for negative scalars, and the result is the zero vector for a scalar of zero."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex

a = Matrix([2, -1, 4])
st.latex(r'\\mathbf{a} = ' + latex(a))

c = 3 * a
st.latex(r'3\\mathbf{a} = ' + latex(c))
"""
    st.code(code, language="python")
    exec(code)
    st.info("""
Multiply each component by the scalar:
- 3×2 = 6
- 3×(-1) = -3
- 3×4 = 12
""")

with col_right:
    a = np.array([2, -1])
    scalar = 3
    c = scalar * a
    fig, ax = plt.subplots(figsize=(5, 5))
    origin = np.zeros(2)
    ax.quiver(
        *origin,
        *a,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="royalblue",
        label=r"$\mathbf{a}$",
    )
    ax.quiver(
        *origin,
        *c,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="seagreen",
        label=r"$3\mathbf{a}$",
    )
    lim = max(abs(c).max(), abs(a).max()) + 1
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.axhline(0, color="grey", linewidth=0.5)
    ax.axvline(0, color="grey", linewidth=0.5)
    ax.set_aspect("equal")
    ax.legend()
    ax.set_title("Scalar Multiplication (2D projection)")
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    plt.close(fig)


# ── Dot Product ──────────────────────────────────────────────────────────────
st.markdown("##### Dot Product")
st.info(
    "The dot product takes two vectors and returns a single number (a scalar). It measures how much two vectors point in the same direction. If the result is zero, the vectors are perpendicular."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex

a = Matrix([1, 2, 3])
st.latex(r'\\mathbf{a} = ' + latex(a))

b = Matrix([4, -5, 6])
st.latex(r'\\mathbf{b} = ' + latex(b))

dot = a.dot(b)
st.latex(r'\\mathbf{a} \\cdot \\mathbf{b} = ' + latex(dot))
"""
    st.code(code, language="python")
    exec(code)
    st.info("""
Multiply corresponding components and sum:
- (1×4) + (2×(-5)) + (3×6) = 4 - 10 + 18 = 12
""")

with col_right:
    a = np.array([1, 2])
    b = np.array([4, -5])
    dot = np.dot(a, b)
    cos_theta = dot / (np.linalg.norm(a) * np.linalg.norm(b))
    theta = np.degrees(np.arccos(np.clip(cos_theta, -1, 1)))
    # projection of b onto a
    proj = (dot / np.dot(a, a)) * a

    fig, ax = plt.subplots(figsize=(5, 5))
    origin = np.zeros(2)
    ax.quiver(
        *origin,
        *a,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="royalblue",
        label=r"$\mathbf{a}$",
    )
    ax.quiver(
        *origin,
        *b,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="tomato",
        label=r"$\mathbf{b}$",
    )
    ax.quiver(
        *origin,
        *proj,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="seagreen",
        label="projection of b onto a",
    )
    ax.plot([b[0], proj[0]], [b[1], proj[1]], "k--", linewidth=0.8, alpha=0.5)
    lim = max(abs(a).max(), abs(b).max()) + 1
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.axhline(0, color="grey", linewidth=0.5)
    ax.axvline(0, color="grey", linewidth=0.5)
    ax.set_aspect("equal")
    ax.legend(fontsize=8)
    ax.set_title(f"Dot Product (2D) — angle = {theta:.1f}°, a·b = {dot}")
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    plt.close(fig)


# ── Cross Product ────────────────────────────────────────────────────────────
st.markdown("##### Cross Product")
st.info(
    "The cross product takes two 3D vectors and returns a new vector that is perpendicular to both. It is useful for finding normal vectors to surfaces and for calculating torque or angular momentum in physics."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex

a = Matrix([1, 0, 0])
st.latex(r'\\mathbf{a} = ' + latex(a))

b = Matrix([0, 1, 0])
st.latex(r'\\mathbf{b} = ' + latex(b))

c = a.cross(b)
st.latex(r'\\mathbf{a} \\times \\mathbf{b} = ' + latex(c))
"""
    st.code(code, language="python")
    exec(code)
    st.info(r"""
The cross product is only defined for 3-dimensional vectors and returns a vector perpendicular to both inputs.

Computed as a 3×3 determinant:

$$\mathbf{a} \times \mathbf{b} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{vmatrix}$$

Expanding each component:

- **i**: $(0 \times 0) - (0 \times 1) = 0$
- **j**: $-[(1 \times 0) - (0 \times 0)] = 0$
- **k**: $(1 \times 1) - (0 \times 0) = 1$

Result: $[0, 0, 1]$ — the unit vector along the z-axis.  By the right-hand rule, pointing along x then y must produce a vector pointing along z.
""")

with col_right:
    a = np.array([1, 0, 0])
    b = np.array([0, 1, 0])
    c = np.cross(a, b)
    fig = plt.figure(figsize=(5, 5))
    ax3d = fig.add_subplot(111, projection="3d")
    origin = np.zeros(3)
    ax3d.quiver(*origin, *a, color="royalblue", label=r"$\mathbf{a}$")
    ax3d.quiver(*origin, *b, color="tomato", label=r"$\mathbf{b}$")
    ax3d.quiver(*origin, *c, color="seagreen", label=r"$\mathbf{a} \times \mathbf{b}$")
    ax3d.set_xlim(0, 1.2)
    ax3d.set_ylim(0, 1.2)
    ax3d.set_zlim(0, 1.2)
    ax3d.set_xlabel("X")
    ax3d.set_ylabel("Y")
    ax3d.set_zlabel("Z")
    ax3d.legend()
    ax3d.set_title("Cross Product")
    st.pyplot(fig)
    plt.close(fig)


# ── Vector Magnitude ─────────────────────────────────────────────────────────
st.markdown("##### Vector Magnitude (Norm)")
st.info(
    "The magnitude (or norm) of a vector is its length — the straight-line distance from the origin to the point the vector represents. It is always a non-negative number."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex, sqrt

a = Matrix([3, 4])
st.latex(r'\\mathbf{a} = ' + latex(a))

magnitude = a.norm()
st.latex(r'\\|\\mathbf{a}\\| = ' + latex(magnitude))
"""
    st.code(code, language="python")
    exec(code)
    st.info(r"""
$$\|\mathbf{a}\| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$
""")

with col_right:
    a = np.array([3, 4])
    mag = np.linalg.norm(a)
    fig, ax = plt.subplots(figsize=(5, 5))
    origin = np.zeros(2)
    ax.quiver(
        *origin,
        *a,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="royalblue",
        label=r"$\mathbf{a}$",
    )
    ax.annotate(
        "",
        xy=a,
        xytext=origin,
        arrowprops=dict(arrowstyle="-", color="seagreen", lw=1.5, linestyle="dashed"),
    )
    ax.text(a[0] / 2 + 0.2, a[1] / 2, f"‖a‖ = {mag:.0f}", color="seagreen", fontsize=11)
    ax.plot(*a, "o", color="royalblue")
    lim = mag + 1
    ax.set_xlim(-1, lim)
    ax.set_ylim(-1, lim)
    ax.axhline(0, color="grey", linewidth=0.5)
    ax.axvline(0, color="grey", linewidth=0.5)
    ax.set_aspect("equal")
    ax.legend()
    ax.set_title("Vector Magnitude")
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    plt.close(fig)


# ── Unit Vector ──────────────────────────────────────────────────────────────
st.markdown("##### Unit Vector (Normalisation)")
st.info(
    "A unit vector is a vector that has been scaled to have a magnitude of exactly 1. It preserves the direction of the original vector but discards its length. Unit vectors are used when only direction matters, such as in surface normals or directional lighting in graphics."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex

a = Matrix([3, 4])
st.latex(r'\\mathbf{a} = ' + latex(a))

unit = a.normalized()
st.latex(r'\\hat{\\mathbf{a}} = ' + latex(unit))
"""
    st.code(code, language="python")
    exec(code)
    st.info(r"""
Divide each component by the magnitude:
$$\hat{\mathbf{a}} = \frac{\mathbf{a}}{\|\mathbf{a}\|}$$

A unit vector has magnitude 1 and points in the same direction as the original vector.
""")

with col_right:
    a = np.array([3, 4])
    unit = a / np.linalg.norm(a)
    fig, ax = plt.subplots(figsize=(5, 5))
    origin = np.zeros(2)
    ax.quiver(
        *origin,
        *a,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="royalblue",
        alpha=0.4,
        label=r"$\mathbf{a}$ (original)",
    )
    ax.quiver(
        *origin,
        *unit,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="seagreen",
        label=r"$\hat{\mathbf{a}}$ (unit vector)",
    )
    theta = np.linspace(0, 2 * np.pi, 300)
    ax.plot(
        np.cos(theta),
        np.sin(theta),
        "k--",
        linewidth=0.8,
        alpha=0.4,
        label="unit circle",
    )
    lim = np.linalg.norm(a) + 0.5
    ax.set_xlim(-0.5, lim)
    ax.set_ylim(-0.5, lim)
    ax.axhline(0, color="grey", linewidth=0.5)
    ax.axvline(0, color="grey", linewidth=0.5)
    ax.set_aspect("equal")
    ax.legend()
    ax.set_title("Unit Vector (Normalisation)")
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    plt.close(fig)
