import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sys import path as sys_path

sys_path.append("app")
from utils import display_run_python_snippet

st.set_page_config(page_title="Covariance", layout="wide")
st.header("Covariance")

st.write(
    "Covariance measures how two random variables change together.  "
    "A positive value means they tend to move in the same direction; "
    "a negative value means they tend to move in opposite directions.  "
    "Unlike correlation, covariance retains the units of the original variables."
)

# ── Formula section ────────────────────────────────────────────────────────────
col_formula, col_props = st.columns(2)

with col_formula:
    st.markdown("#### Formula")

    pop_latex = r"\text{Cov}(X, Y) = \mathbb{E}\!\left[(X - \mu_X)(Y - \mu_Y)\right]"
    st.code(pop_latex, language="latex")
    st.latex(pop_latex)

    sample_latex = r"\text{Cov}(X, Y) = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})"
    st.code(sample_latex, language="latex")
    st.latex(sample_latex)

    st.caption(
        "The sample formula uses n − 1 (Bessel's correction) to give an unbiased estimate."
    )

with col_props:
    st.markdown("#### Properties")
    st.info(
        "- **Cov(X, X) = Var(X)** — covariance of a variable with itself is its variance\n"
        "- **Cov(X, Y) = Cov(Y, X)** — symmetric\n"
        "- Units are the product of the units of X and Y\n"
        "- Sign indicates direction; magnitude depends on scale\n"
        "- Cov(X, Y) = 0 does **not** guarantee independence — only that there is no *linear* relationship"
    )

# ── Interactive scatter plot ───────────────────────────────────────────────────
st.divider()
st.markdown("#### Interactive Visualisation")
st.write(
    "Adjust the sliders to control the spread and relationship between X and Y.  "
    "Notice how covariance scales with the standard deviations, unlike correlation."
)

col_s1, col_s2, col_s3 = st.columns(3)
with col_s1:
    sigma_x = st.slider(
        "σ_X (std dev of X)", min_value=0.5, max_value=5.0, value=1.0, step=0.5
    )
with col_s2:
    sigma_y = st.slider(
        "σ_Y (std dev of Y)", min_value=0.5, max_value=5.0, value=1.0, step=0.5
    )
with col_s3:
    rho = st.slider(
        "Correlation (ρ)", min_value=-0.99, max_value=0.99, value=0.7, step=0.05
    )

# Build covariance matrix from σ_X, σ_Y, ρ
cov_xy_target = rho * sigma_x * sigma_y
cov_matrix = [[sigma_x**2, cov_xy_target], [cov_xy_target, sigma_y**2]]

np.random.seed(42)
data = np.random.multivariate_normal([0, 0], cov_matrix, size=200)
X, Y = data[:, 0], data[:, 1]

cov_calc = np.cov(X, Y, ddof=1)[0, 1]
std_x_calc = np.std(X, ddof=1)
std_y_calc = np.std(Y, ddof=1)

fig, ax = plt.subplots(figsize=(8, 4))
ax.scatter(X, Y, alpha=0.5, s=20, color="steelblue")
m, b = np.polyfit(X, Y, 1)
x_line = np.linspace(X.min(), X.max(), 100)
ax.plot(x_line, m * x_line + b, color="tomato", linewidth=1.5, label="Best fit")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title(f"Scatter plot  (σ_X={sigma_x}, σ_Y={sigma_y}, ρ={rho:.2f})")
ax.legend()
st.pyplot(fig)

col_m1, col_m2, col_m3, col_m4 = st.columns(4)
with col_m1:
    st.metric("Cov(X, Y)", f"{cov_calc:.4f}")
with col_m2:
    st.metric("σ_X (calculated)", f"{std_x_calc:.4f}")
with col_m3:
    st.metric("σ_Y (calculated)", f"{std_y_calc:.4f}")
with col_m4:
    st.metric("ρ = Cov / (σ_X·σ_Y)", f"{cov_calc / (std_x_calc * std_y_calc):.4f}")

# ── Code snippet ───────────────────────────────────────────────────────────────
st.divider()
st.markdown("#### Calculating Covariance with NumPy")

snippet = """\
import numpy as np
import streamlit as st

rng = np.random.default_rng(42)
X = rng.normal(0, 2, 500)           # std dev = 2
Y = 0.8 * X + rng.normal(0, 1, 500) # correlated with X

# np.cov returns the full 2x2 covariance matrix
cov_matrix = np.cov(X, Y, ddof=1)
cov_xy = cov_matrix[0, 1]           # off-diagonal element

# Manual calculation from the formula
cov_manual = np.mean((X - X.mean()) * (Y - Y.mean())) * len(X) / (len(X) - 1)

st.write(f"Cov(X, Y) via np.cov   = {cov_xy:.4f}")
st.write(f"Cov(X, Y) manual       = {cov_manual:.4f}")
st.write(f"Cov(X, X) = Var(X)     = {cov_matrix[0, 0]:.4f}")
st.write(f"np.var(X, ddof=1)      = {np.var(X, ddof=1):.4f}")
"""

display_run_python_snippet(snippet)
