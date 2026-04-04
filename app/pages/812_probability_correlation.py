import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sys import path as sys_path

sys_path.append("app")
from utils import display_run_python_snippet

st.set_page_config(page_title="Correlation", layout="wide")
st.header("Correlation")

st.write(
    "The Pearson correlation coefficient ρ measures the strength and direction of the "
    "linear relationship between two random variables.  It normalises covariance by the "
    "product of the standard deviations, giving a dimensionless value in [−1, 1]."
)

# ── Formula section ────────────────────────────────────────────────────────────
col_formula, col_props = st.columns(2)

with col_formula:
    st.markdown("#### Formula")

    rho_latex = r"\rho(X, Y) = \frac{\text{Cov}(X, Y)}{\sigma_X \, \sigma_Y}"
    st.code(rho_latex, language="latex")
    st.latex(rho_latex)

    cov_latex = r"\text{Cov}(X, Y) = \mathbb{E}\!\left[(X - \mu_X)(Y - \mu_Y)\right]"
    st.code(cov_latex, language="latex")
    st.latex(cov_latex)

    sigma_latex = (
        r"\sigma_X = \sqrt{\text{Var}(X)}, \quad \sigma_Y = \sqrt{\text{Var}(Y)}"
    )
    st.code(sigma_latex, language="latex")
    st.latex(sigma_latex)

with col_props:
    st.markdown("#### Properties")
    st.info(
        "- ρ ∈ [−1, 1] always\n"
        "- **ρ = 1** — perfect positive linear relationship\n"
        "- **ρ = −1** — perfect negative linear relationship\n"
        "- **ρ = 0** — no *linear* relationship (non-linear patterns may still exist)\n"
        "- Correlation is dimensionless — it is unaffected by scaling or shifting either variable\n"
        "- Correlation does **not** imply causation"
    )

# ── Interactive scatter plot ───────────────────────────────────────────────────
st.divider()
st.markdown("#### Interactive Visualisation")
st.write(
    "Adjust ρ to see how the scatter of two standard-normal variables changes.  "
    "The calculated metrics are derived directly from the formula above."
)

rho_target = st.slider(
    "Target correlation (ρ)", min_value=-0.99, max_value=0.99, value=0.6, step=0.05
)

np.random.seed(42)
cov_matrix = [[1.0, rho_target], [rho_target, 1.0]]
data = np.random.multivariate_normal([0, 0], cov_matrix, size=200)
X, Y = data[:, 0], data[:, 1]

# Compute metrics from the formula
cov_xy = np.cov(X, Y, ddof=1)[0, 1]
sigma_x = np.std(X, ddof=1)
sigma_y = np.std(Y, ddof=1)
rho_calc = cov_xy / (sigma_x * sigma_y)

fig, ax = plt.subplots(figsize=(8, 4))
ax.scatter(X, Y, alpha=0.5, s=20, color="steelblue")
m, b = np.polyfit(X, Y, 1)
x_line = np.linspace(X.min(), X.max(), 100)
ax.plot(x_line, m * x_line + b, color="tomato", linewidth=1.5, label="Best fit")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title(f"Scatter plot  (target ρ = {rho_target:.2f})")
ax.legend()
st.pyplot(fig)

col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric("Pearson ρ (calculated)", f"{rho_calc:.4f}")
with col_m2:
    st.metric("Cov(X, Y)", f"{cov_xy:.4f}")
with col_m3:
    st.metric("σ_X · σ_Y", f"{sigma_x * sigma_y:.4f}")

# ── Code snippet ───────────────────────────────────────────────────────────────
st.divider()
st.markdown("#### Calculating Correlation Step by Step")
st.write(
    "The snippet below shows how to derive ρ from first principles using NumPy, "
    "then verifies the result against `np.corrcoef`."
)

snippet = """\
import numpy as np
import streamlit as st

rng = np.random.default_rng(42)
X = rng.normal(0, 1, 500)
Y = 0.7 * X + rng.normal(0, 1, 500)

cov_matrix = np.cov(X, Y, ddof=1)
cov_xy = cov_matrix[0, 1]
sigma_x = np.std(X, ddof=1)
sigma_y = np.std(Y, ddof=1)
rho = cov_xy / (sigma_x * sigma_y)

st.write(f"Cov(X, Y)          = {cov_xy:.4f}")
st.write(f"σ_X                = {sigma_x:.4f}")
st.write(f"σ_Y                = {sigma_y:.4f}")
st.write(f"ρ = Cov / (σ_X·σ_Y) = {rho:.4f}")
st.write(f"np.corrcoef check  = {np.corrcoef(X, Y)[0, 1]:.4f}")
"""

display_run_python_snippet(snippet)
