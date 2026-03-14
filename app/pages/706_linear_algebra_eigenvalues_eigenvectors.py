import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Linear Algebra - Eigenvalues and Eigenvectors",
    page_icon="📐",
    layout="wide",
)
st.header("Linear Algebra - Eigenvalues and Eigenvectors")


# ── Introduction ──────────────────────────────────────────────────────────────
st.info(
    "An **eigenvector** of a square matrix is a non-zero vector that, when the matrix is "
    "applied to it, only changes in scale — not direction. The scaling factor is called the "
    "**eigenvalue** λ. Formally: **Av = λv**."
)

st.info(
    """Applications of eigenvalues and eigenvectors:
- **PCA**: Dimensionality reduction in data science and machine learning
- **Stability Analysis**: Determining stability of differential equations and dynamical systems
- **Google PageRank**: Ranking web pages via the dominant eigenvector of the link matrix
- **Quantum Mechanics**: Energy levels correspond to eigenvalues of the Hamiltonian operator
- **Vibration Analysis**: Natural frequencies of mechanical systems correspond to eigenvalues"""
)


# ── Characteristic Equation ───────────────────────────────────────────────────
st.markdown("##### The Characteristic Equation")
st.info(
    "Eigenvalues are found by solving det(A − λI) = 0, known as the characteristic equation. "
    "For an n×n matrix this produces a degree-n polynomial in λ whose roots are the eigenvalues."
)

col_left, col_right = st.columns(2)

with col_left:
    st.latex(r"A\mathbf{v} = \lambda\mathbf{v}")
    st.latex(r"(A - \lambda I)\mathbf{v} = \mathbf{0}")
    st.latex(r"\det(A - \lambda I) = 0")
    st.info(
        "The equation (A − λI)v = 0 has a non-zero solution only when A − λI is singular, "
        "i.e. its determinant is zero. This gives the characteristic polynomial."
    )

with col_right:
    st.markdown("**Worked characteristic equation for A = [[4, 2], [1, 3]]:**")
    st.latex(r"""
A - \lambda I = \begin{bmatrix} 4-\lambda & 2 \\ 1 & 3-\lambda \end{bmatrix}
""")
    st.latex(r"""
\det(A - \lambda I) = (4-\lambda)(3-\lambda) - 2 \times 1
= \lambda^2 - 7\lambda + 10 = 0
""")
    st.latex(
        r"(\lambda - 5)(\lambda - 2) = 0 \implies \lambda_1 = 5,\quad \lambda_2 = 2"
    )


# ── Eigenvalues Example ───────────────────────────────────────────────────────
st.markdown("##### Example: Eigenvalues with SymPy")
st.info(
    "SymPy solves the characteristic equation symbolically and returns exact eigenvalues."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex

A = Matrix([[4, 2], [1, 3]])
st.latex(r'A = ' + latex(A))

eigenvals = A.eigenvals()
for val, multiplicity in eigenvals.items():
    st.latex(r'\\lambda = ' + latex(val) + rf',\\quad \\text{{multiplicity}} = {multiplicity}')
"""
    st.code(code, language="python")
    exec(code)
    st.info("""
Characteristic equation: λ² − 7λ + 10 = 0
- (λ − 5)(λ − 2) = 0
- λ₁ = 5, λ₂ = 2
""")

with col_right:
    A = np.array([[4, 2], [1, 3]], dtype=float)
    eigenvals, eigenvecs = np.linalg.eig(A)

    fig, ax = plt.subplots(figsize=(5, 5))
    origin = np.zeros(2)
    colors = ["royalblue", "tomato"]

    for i, (lam, color) in enumerate(zip(eigenvals, colors)):
        v = eigenvecs[:, i]
        v = v / np.linalg.norm(v)
        Av = A @ v
        ax.quiver(
            *origin,
            *v,
            angles="xy",
            scale_units="xy",
            scale=1,
            color=color,
            alpha=0.5,
            label=f"v{i+1} (λ={lam:.0f})",
            width=0.012,
        )
        ax.quiver(
            *origin,
            *Av,
            angles="xy",
            scale_units="xy",
            scale=1,
            color=color,
            label=f"Av{i+1} = {lam:.0f}v{i+1}",
            width=0.006,
        )

    lim = abs(A @ eigenvecs).max() + 0.5
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.axhline(0, color="grey", linewidth=0.5)
    ax.axvline(0, color="grey", linewidth=0.5)
    ax.set_aspect("equal")
    ax.legend(fontsize=8)
    ax.set_title("Eigenvectors only scale under A — direction unchanged", fontsize=10)
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    plt.close(fig)


# ── Eigenvectors ──────────────────────────────────────────────────────────────
st.markdown("##### Eigenvectors with SymPy")
st.info(
    "Once eigenvalues are known, eigenvectors are found by solving (A − λI)v = 0 for each λ. "
    "SymPy's eigenvects() returns eigenvalue, multiplicity, and eigenvector together."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex

A = Matrix([[4, 2], [1, 3]])
st.latex(r'A = ' + latex(A))

eigenvects = A.eigenvects()
for eigenval, multiplicity, eigenvec_list in eigenvects:
    st.latex(r'\\lambda = ' + latex(eigenval))
    for vec in eigenvec_list:
        st.latex(r'\\mathbf{v} = ' + latex(vec))
"""
    st.code(code, language="python")
    exec(code)
    st.info("""
- For λ₁ = 5: v₁ = [2, 1]
- For λ₂ = 2: v₂ = [−1, 1]

Verify: A·v₁ = 5·v₁ and A·v₂ = 2·v₂
""")

with col_right:
    v1 = np.array([2.0, 1.0])
    v2 = np.array([-1.0, 1.0])
    Av1 = A @ v1
    Av2 = A @ v2

    fig, ax = plt.subplots(figsize=(5, 5))
    origin = np.zeros(2)

    ax.quiver(
        *origin,
        *v1,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="royalblue",
        label="v₁ = [2, 1]",
        width=0.012,
    )
    ax.quiver(
        *origin,
        *Av1,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="royalblue",
        alpha=0.4,
        label=f"Av₁ = {Av1.tolist()} = 5v₁",
        width=0.006,
    )

    ax.quiver(
        *origin,
        *v2,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="tomato",
        label="v₂ = [−1, 1]",
        width=0.012,
    )
    ax.quiver(
        *origin,
        *Av2,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="tomato",
        alpha=0.4,
        label=f"Av₂ = {Av2.tolist()} = 2v₂",
        width=0.006,
    )

    all_vecs = np.array([v1, Av1, v2, Av2])
    lim = abs(all_vecs).max() + 1
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.axhline(0, color="grey", linewidth=0.5)
    ax.axvline(0, color="grey", linewidth=0.5)
    ax.set_aspect("equal")
    ax.legend(fontsize=8)
    ax.set_title("Av = λv — eigenvectors scale but don't rotate", fontsize=10)
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    plt.close(fig)


# ── Verification ──────────────────────────────────────────────────────────────
st.markdown("##### Verification: Av = λv")
st.info(
    "We can verify the eigenvalue equation directly by computing both sides and confirming they are equal."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex

A = Matrix([[4, 2], [1, 3]])
eigenval = 5
eigenvec = Matrix([2, 1])

st.latex(r'A = ' + latex(A))
st.latex(r'\\lambda = ' + latex(eigenval) + r',\\quad \\mathbf{v} = ' + latex(eigenvec))

Av = A * eigenvec
lambda_v = eigenval * eigenvec

st.latex(r'A\\mathbf{v} = ' + latex(Av))
st.latex(r'\\lambda\\mathbf{v} = ' + latex(lambda_v))
st.write("Av = λv ✓" if Av == lambda_v else "Mismatch!")
"""
    st.code(code, language="python")
    exec(code)

with col_right:
    v = np.array([2.0, 1.0])
    lam = 5.0
    Av = A @ v
    lam_v = lam * v

    fig, ax = plt.subplots(figsize=(5, 4))
    origin = np.zeros(2)
    ax.quiver(
        *origin,
        *v,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="royalblue",
        label="v = [2, 1]",
        width=0.012,
    )
    ax.quiver(
        *origin,
        *Av,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="seagreen",
        label=f"Av = {Av.tolist()}",
        width=0.008,
    )
    ax.quiver(
        *origin,
        *lam_v,
        angles="xy",
        scale_units="xy",
        scale=1,
        color="tomato",
        alpha=0.5,
        label=f"λv = 5×[2,1] = {lam_v.tolist()}",
        width=0.005,
    )

    lim = max(abs(Av).max(), abs(lam_v).max()) + 1
    ax.set_xlim(-1, lim)
    ax.set_ylim(-1, lim)
    ax.axhline(0, color="grey", linewidth=0.5)
    ax.axvline(0, color="grey", linewidth=0.5)
    ax.set_aspect("equal")
    ax.legend(fontsize=8)
    ax.set_title("Av and λv coincide — verification", fontsize=10)
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    plt.close(fig)


# ── NumPy ─────────────────────────────────────────────────────────────────────
st.markdown("##### Eigenvalues with NumPy")
st.info(
    "NumPy's `np.linalg.eig()` is computationally efficient for large matrices. "
    "It returns eigenvalues as a 1D array and eigenvectors as columns of a 2D array. "
    "Results are floating-point approximations."
)

col_left, col_right = st.columns(2)

with col_left:
    code = """
import streamlit as st
from sympy import Matrix, latex
import numpy as np

A = np.array([[4, 2], [1, 3]])
eigenvals, eigenvecs = np.linalg.eig(A)

st.write("Eigenvalues:")
st.latex(latex(Matrix(eigenvals)))

st.write("Eigenvectors (columns):")
st.latex(latex(Matrix(eigenvecs.round(4))))

st.latex(r'\\lambda_1 = ' + f'{eigenvals[0]:.4g}')
st.latex(r'\\lambda_2 = ' + f'{eigenvals[1]:.4g}')
"""
    st.code(code, language="python")
    exec(code)
    st.info(
        "NumPy normalises eigenvectors to unit length. "
        "SymPy returns unnormalised integer vectors where possible."
    )

with col_right:
    eigenvals_np, eigenvecs_np = np.linalg.eig(A)
    fig, ax = plt.subplots(figsize=(5, 5))
    origin = np.zeros(2)
    colors = ["royalblue", "tomato"]

    for i, (lam, color) in enumerate(zip(eigenvals_np, colors)):
        v = eigenvecs_np[:, i]
        Av = A @ v
        ax.quiver(
            *origin,
            *v,
            angles="xy",
            scale_units="xy",
            scale=1,
            color=color,
            label=f"v{i+1} unit (λ={lam:.0f})",
            width=0.012,
        )
        ax.quiver(
            *origin,
            *Av,
            angles="xy",
            scale_units="xy",
            scale=1,
            color=color,
            alpha=0.4,
            label=f"Av{i+1} = {lam:.0f}·v{i+1}",
            width=0.006,
        )

    lim = max(abs(A @ eigenvecs_np).max()) + 0.5
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.axhline(0, color="grey", linewidth=0.5)
    ax.axvline(0, color="grey", linewidth=0.5)
    ax.set_aspect("equal")
    ax.legend(fontsize=8)
    ax.set_title("NumPy unit eigenvectors and their images under A", fontsize=10)
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    plt.close(fig)


# ── Properties ────────────────────────────────────────────────────────────────
st.markdown("##### Properties of Eigenvalues")
st.info(
    "These properties link eigenvalues to other matrix properties and are useful for "
    "quick sanity checks when computing eigenvalues."
)

col_left, col_right = st.columns(2)

with col_left:
    st.markdown("""
| Property | Rule |
|---|---|
| Trace | Sum of eigenvalues = trace(A) |
| Determinant | Product of eigenvalues = det(A) |
| Invertibility | A is invertible ⟺ all λ ≠ 0 |
| Symmetric matrices | Always have real eigenvalues and orthogonal eigenvectors |
| Complex eigenvalues | Can occur for real matrices (come in conjugate pairs) |
""")

with col_right:
    code = """
import streamlit as st
from sympy import Matrix, latex, trace

A = Matrix([[4, 2], [1, 3]])
eigenvals = list(A.eigenvals().keys())

lam1, lam2 = eigenvals[0], eigenvals[1]
st.latex(r'\\lambda_1 = ' + latex(lam1) + r',\\quad \\lambda_2 = ' + latex(lam2))
st.latex(r'\\lambda_1 + \\lambda_2 = ' + latex(lam1 + lam2) +
         r' = \\text{tr}(A) = ' + latex(trace(A)))
st.latex(r'\\lambda_1 \\cdot \\lambda_2 = ' + latex(lam1 * lam2) +
         r' = \\det(A) = ' + latex(A.det()))
"""
    st.code(code, language="python")
    exec(code)
