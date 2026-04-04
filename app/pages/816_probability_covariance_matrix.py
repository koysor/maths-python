import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sys import path as sys_path

sys_path.append("app")
from utils import display_run_python_snippet

st.set_page_config(page_title="Covariance Matrix", layout="wide")
st.header("Covariance Matrix")

st.write(
    "A covariance matrix (also called a variance-covariance matrix) summarises the pairwise "
    "covariances and variances of a set of random variables in a single square matrix.  "
    "It is the multivariate generalisation of variance."
)

# ── Formula section ────────────────────────────────────────────────────────────
col_formula, col_props = st.columns(2)

with col_formula:
    st.markdown("#### Definition")

    def_latex = r"\Sigma = \mathbb{E}\!\left[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^\top\right]"
    st.code(def_latex, language="latex")
    st.latex(def_latex)

    elem_latex = (
        r"\Sigma_{ij} = \text{Cov}(X_i, X_j) = \mathbb{E}[(X_i - \mu_i)(X_j - \mu_j)]"
    )
    st.code(elem_latex, language="latex")
    st.latex(elem_latex)

    st.markdown("#### Relationship to Correlation Matrix")
    decomp_latex = r"\Sigma = \mathbf{D}\, \mathbf{R}\, \mathbf{D}, \qquad \mathbf{D} = \operatorname{diag}(\sigma_1, \sigma_2, \ldots, \sigma_n)"
    st.code(decomp_latex, language="latex")
    st.latex(decomp_latex)
    st.caption(
        "R is the correlation matrix (off-diagonals are Pearson ρ values); "
        "D is the diagonal matrix of standard deviations."
    )

with col_props:
    st.markdown("#### Properties")
    st.info(
        "- **Diagonal entries** Σᵢᵢ = Var(Xᵢ) — always non-negative\n"
        "- **Off-diagonal entries** Σᵢⱼ = Cov(Xᵢ, Xⱼ) — can be negative\n"
        "- **Symmetric**: Σ = Σᵀ, because Cov(Xᵢ, Xⱼ) = Cov(Xⱼ, Xᵢ)\n"
        "- **Positive semi-definite**: xᵀΣx ≥ 0 for all real vectors x\n"
        "- Eigenvalues are all ≥ 0 (consequence of PSD)\n"
        "- Used in multivariate normal distributions, PCA, and portfolio optimisation"
    )

    st.markdown("#### Example — 3 variables")
    mat_latex = (
        r"\Sigma = \begin{pmatrix}"
        r"\sigma_1^2 & \sigma_{12} & \sigma_{13} \\"
        r"\sigma_{12} & \sigma_2^2 & \sigma_{23} \\"
        r"\sigma_{13} & \sigma_{23} & \sigma_3^2"
        r"\end{pmatrix}"
    )
    st.code(mat_latex, language="latex")
    st.latex(mat_latex)

# ── Interactive heatmap ────────────────────────────────────────────────────────
st.divider()
st.markdown("#### Interactive Visualisation")
st.write(
    "Set the standard deviations and pairwise correlations below to build a 3×3 covariance "
    "matrix.  The heatmap updates live — notice how the diagonal (variances) dominates when "
    "standard deviations are large, and how off-diagonal sign matches the correlation sign."
)

col_s1, col_s2, col_s3 = st.columns(3)
with col_s1:
    s1 = st.slider("σ₁", min_value=0.5, max_value=4.0, value=1.0, step=0.5)
    s2 = st.slider("σ₂", min_value=0.5, max_value=4.0, value=2.0, step=0.5)
    s3 = st.slider("σ₃", min_value=0.5, max_value=4.0, value=1.5, step=0.5)
with col_s2:
    r12 = st.slider(
        "ρ₁₂ (corr X₁, X₂)", min_value=-0.99, max_value=0.99, value=0.7, step=0.05
    )
    r13 = st.slider(
        "ρ₁₃ (corr X₁, X₃)", min_value=-0.99, max_value=0.99, value=-0.3, step=0.05
    )
    r23 = st.slider(
        "ρ₂₃ (corr X₂, X₃)", min_value=-0.99, max_value=0.99, value=0.5, step=0.05
    )

# Build Σ = D * R * D
sigma = np.array([s1, s2, s3])
R = np.array(
    [
        [1.0, r12, r13],
        [r12, 1.0, r23],
        [r13, r23, 1.0],
    ]
)
D = np.diag(sigma)
cov = D @ R @ D

# Check positive semi-definiteness
eigenvalues = np.linalg.eigvalsh(cov)
is_psd = np.all(eigenvalues >= -1e-10)

with col_s3:
    st.markdown("**Resulting Σ**")
    st.dataframe(
        {f"X{j+1}": [f"{cov[i, j]:.3f}" for i in range(3)] for j in range(3)},
        hide_index=False,
        use_container_width=True,
    )
    if is_psd:
        st.success("Positive semi-definite ✓")
    else:
        st.error("Not positive semi-definite — adjust correlations")

# Heatmap — covariance matrix has negative entries, so use RdBu_r with symmetric limits
abs_max = np.abs(cov).max()
fig, axes = plt.subplots(1, 2, figsize=(8, 3))

# Left: covariance matrix
im0 = axes[0].imshow(cov, cmap="RdBu_r", vmin=-abs_max, vmax=abs_max)
axes[0].set_title("Covariance matrix Σ")
axes[0].set_xticks([0, 1, 2])
axes[0].set_xticklabels(["X₁", "X₂", "X₃"])
axes[0].set_yticks([0, 1, 2])
axes[0].set_yticklabels(["X₁", "X₂", "X₃"])
for i in range(3):
    for j in range(3):
        axes[0].text(j, i, f"{cov[i, j]:.2f}", ha="center", va="center", fontsize=9)
plt.colorbar(im0, ax=axes[0])

# Right: correlation matrix derived from Σ
D_inv = np.diag(1.0 / sigma)
R_derived = D_inv @ cov @ D_inv
im1 = axes[1].imshow(R_derived, cmap="RdBu_r", vmin=-1, vmax=1)
axes[1].set_title("Correlation matrix R (derived)")
axes[1].set_xticks([0, 1, 2])
axes[1].set_xticklabels(["X₁", "X₂", "X₃"])
axes[1].set_yticks([0, 1, 2])
axes[1].set_yticklabels(["X₁", "X₂", "X₃"])
for i in range(3):
    for j in range(3):
        axes[1].text(
            j, i, f"{R_derived[i, j]:.2f}", ha="center", va="center", fontsize=9
        )
plt.colorbar(im1, ax=axes[1])

plt.tight_layout()
st.pyplot(fig)

col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric(
        "Var(X₁), Var(X₂), Var(X₃)", f"{cov[0,0]:.2f}, {cov[1,1]:.2f}, {cov[2,2]:.2f}"
    )
with col_m2:
    st.metric("Min eigenvalue", f"{eigenvalues.min():.4f}")
with col_m3:
    st.metric("Determinant |Σ|", f"{np.linalg.det(cov):.4f}")

# ── Code snippet ───────────────────────────────────────────────────────────────
st.divider()
st.markdown("#### Computing a Covariance Matrix with NumPy")
st.write(
    "The snippet below generates three correlated variables and computes their covariance "
    "matrix from data, verifying the diagonal = variances property."
)

snippet = """\
import numpy as np
import streamlit as st

# Define the true covariance matrix
sigma = np.array([1.0, 2.0, 1.5])
R = np.array([[1.0,  0.7, -0.3],
              [0.7,  1.0,  0.5],
              [-0.3, 0.5,  1.0]])
D = np.diag(sigma)
cov_true = D @ R @ D

# Generate samples from a multivariate normal
rng = np.random.default_rng(42)
data = rng.multivariate_normal(mean=[0, 0, 0], cov=cov_true, size=1000)

# Estimate covariance matrix from data  (n x 3 → 3 x 3)
cov_est = np.cov(data.T, ddof=1)

st.write("**True Σ (diagonal = variances):**")
st.write(cov_true.round(3))

st.write("**Estimated Σ from 1 000 samples:**")
st.write(cov_est.round(3))

st.write("**Diagonal entries vs np.var:**")
for i in range(3):
    st.write(f"  Σ[{i},{i}] = {cov_est[i,i]:.4f}  |  "
             f"np.var(X{i+1}, ddof=1) = {np.var(data[:, i], ddof=1):.4f}")
"""

display_run_python_snippet(snippet)
