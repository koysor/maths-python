import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from math import comb


st.set_page_config(layout="wide")
st.markdown("### The Binomial Distribution")


st.write(
    "The Binomial Distribution is a discrete probability distribution that models the number of successes in a fixed number of independent Bernoulli trials, each with the same probability of success."
)
st.write(
    "It is commonly used to model scenarios like coin flips, quality control testing, or any situation with binary outcomes (success/failure)."
)


col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Notation")
    latex_code = r"""
    X \sim \text{Binomial}(n, p)
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)
    st.write(
        """Where:
    - $$n$$ is the number of trials
    - $$p$$ is the probability of success on each trial
    - $$q = 1 - p$$ is the probability of failure
    - $$X$$ is the number of successes (can be 0, 1, 2, ..., n)
    """
    )

    st.markdown("#### Key Properties")
    st.write("**Mean (Expected Value):**")
    latex_mean = r"\mathbb{E}[X] = \mu = np"
    st.code(latex_mean, language="latex")
    st.latex(latex_mean)

    st.write("**Variance:**")
    latex_var = r"\text{Var}(X) = \sigma^2 = np(1-p) = npq"
    st.code(latex_var, language="latex")
    st.latex(latex_var)

    st.write("**Standard Deviation:**")
    latex_std = r"\sigma = \sqrt{np(1-p)}"
    st.code(latex_std, language="latex")
    st.latex(latex_std)

with col2:
    st.markdown("#### Probability Mass Function (PMF)")
    st.write(
        "The probability of getting exactly $k$ successes in $n$ trials is given by:"
    )
    latex_pmf = r"""
    P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
    """
    st.code(latex_pmf, language="latex")
    st.latex(latex_pmf)
    st.write(
        """Where:
    - $$\\binom{n}{k} = \\frac{n!}{k!(n-k)!}$$ is the binomial coefficient ("n choose k")
    - $$p^k$$ is the probability of $$k$$ successes
    - $$(1-p)^{n-k}$$ is the probability of $$(n-k)$$ failures
    """
    )

    st.markdown("#### Cumulative Distribution Function (CDF)")
    st.write("The probability of getting at most $k$ successes:")
    latex_cdf = r"""
    P(X \leq k) = \sum_{i=0}^{k} \binom{n}{i} p^i (1-p)^{n-i}
    """
    st.code(latex_cdf, language="latex")
    st.latex(latex_cdf)


st.markdown("---")
st.markdown("### Interactive Visualisation")

# User inputs
col_input1, col_input2 = st.columns(2)
with col_input1:
    n = st.slider("Number of trials (n)", min_value=1, max_value=50, value=10)
with col_input2:
    p = st.slider(
        "Probability of success (p)", min_value=0.0, max_value=1.0, value=0.5, step=0.01
    )

k_highlight = st.slider(
    "Highlight P(X ≤ k) for k =", min_value=0, max_value=n, value=n // 2
)

# Calculate distribution values
k_values = np.arange(0, n + 1)
pmf_values = binom.pmf(k_values, n, p)

# Calculate statistics
mean = n * p
variance = n * p * (1 - p)
std_dev = np.sqrt(variance)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 5))

# Plot bars - colour based on whether k <= k_highlight
colours = ["skyblue" if k <= k_highlight else "lightgray" for k in k_values]
bars = ax.bar(k_values, pmf_values, color=colours, edgecolor="navy", alpha=0.7)

# Add vertical line for mean
ax.axvline(mean, color="red", linestyle="--", linewidth=2, label=f"μ = {mean:.2f}")

# Labels and formatting
ax.set_title(f"Binomial Distribution: n = {n}, p = {p:.2f}", fontsize=14)
ax.set_xlabel("Number of Successes (k)", fontsize=12)
ax.set_ylabel("Probability P(X = k)", fontsize=12)
ax.set_xticks(k_values)
ax.grid(axis="y", alpha=0.3)
ax.legend()

# Adjust x-axis for large n
if n > 20:
    ax.set_xticks(np.arange(0, n + 1, max(1, n // 10)))

st.pyplot(fig)

# Display statistics
col_stat1, col_stat2, col_stat3 = st.columns(3)
with col_stat1:
    st.metric("Mean (μ)", f"{mean:.4f}")
with col_stat2:
    st.metric("Variance (σ²)", f"{variance:.4f}")
with col_stat3:
    st.metric("Std Dev (σ)", f"{std_dev:.4f}")

# Display probability calculations
st.markdown("---")
st.markdown("### Probability Calculations")

cdf_value = binom.cdf(k_highlight, n, p)
pmf_at_k = binom.pmf(k_highlight, n, p)

col_prob1, col_prob2 = st.columns(2)
with col_prob1:
    st.markdown(f"**P(X = {k_highlight})** = {pmf_at_k:.6f}")
    st.write(f"Probability of exactly {k_highlight} successes")

with col_prob2:
    st.markdown(f"**P(X ≤ {k_highlight})** = {cdf_value:.6f}")
    st.write(f"Probability of at most {k_highlight} successes (shaded area)")


# Example calculation
st.markdown("---")
st.markdown("### Worked Example")

st.write(f"For n = {n} trials and p = {p:.2f}:")

# Show the PMF calculation for k_highlight
binom_coef = comb(n, k_highlight)
p_power = p**k_highlight
q_power = (1 - p) ** (n - k_highlight)

latex_example = rf"""
P(X = {k_highlight}) = \binom{{{n}}}{{{k_highlight}}} \times {p:.2f}^{{{k_highlight}}} \times {1-p:.2f}^{{{n - k_highlight}}}
= {binom_coef} \times {p_power:.6f} \times {q_power:.6f}
= {pmf_at_k:.6f}
"""
st.latex(latex_example)


st.markdown("---")
st.markdown("### Common Applications")
st.write(
    """
- **Quality Control**: Number of defective items in a batch
- **Clinical Trials**: Number of patients responding to treatment
- **Polling**: Number of voters supporting a candidate
- **Games of Chance**: Number of heads in coin flips
- **Genetics**: Number of offspring with a particular trait
"""
)

st.markdown("### Applications in Quantitative Finance")

st.write(
    """
The binomial distribution is fundamental in quantitative finance, underpinning several
important models and techniques.
"""
)

col_fin1, col_fin2 = st.columns(2)

with col_fin1:
    st.markdown("#### Binomial Option Pricing Model")
    st.write(
        """
The **Cox-Ross-Rubinstein (CRR) model** uses a binomial tree to price options.
At each time step, the underlying asset price can move up by factor $u$ or down by factor $d$.
"""
    )
    latex_crr = r"""
    u = e^{\sigma\sqrt{\Delta t}}, \quad d = e^{-\sigma\sqrt{\Delta t}} = \frac{1}{u}
    """
    st.code(latex_crr, language="latex")
    st.latex(latex_crr)

    st.write("The **risk-neutral probability** of an up move is:")
    latex_rn_prob = r"""
    p = \frac{e^{r\Delta t} - d}{u - d}
    """
    st.code(latex_rn_prob, language="latex")
    st.latex(latex_rn_prob)

    st.write("The option price is the discounted expected payoff:")
    latex_option = r"""
    C_0 = e^{-rT} \sum_{k=0}^{n} \binom{n}{k} p^k (1-p)^{n-k} \max(S_0 u^k d^{n-k} - K, 0)
    """
    st.code(latex_option, language="latex")
    st.latex(latex_option)

    st.write(
        """
Where $r$ is the risk-free rate, $\\sigma$ is volatility, $\\Delta t = T/n$ is the time step,
$S_0$ is the initial stock price, and $K$ is the strike price.
"""
    )

with col_fin2:
    st.markdown("#### Credit Risk Modelling")
    st.write(
        """
In credit portfolios, the binomial distribution models the **number of defaults**
among $n$ obligors, each with default probability $p$.
"""
    )
    latex_default = r"""
    P(\text{exactly } k \text{ defaults}) = \binom{n}{k} p^k (1-p)^{n-k}
    """
    st.code(latex_default, language="latex")
    st.latex(latex_default)

    st.markdown("#### Value at Risk (VaR)")
    st.write(
        """
For a portfolio of $n$ independent positions with equal loss probability $p$,
VaR can be computed using the binomial distribution to find the loss threshold
at a given confidence level.
"""
    )


st.markdown("---")
st.markdown("### Relationship to Other Distributions")
st.write(
    """
- As $$n \\to \\infty$$ and $$p \\to 0$$ with $$np = \\lambda$$ constant, the binomial approaches the **Poisson distribution**
- For large $$n$$, the binomial can be approximated by the **Normal distribution** with $$\\mu = np$$ and $$\\sigma = \\sqrt{np(1-p)}$$
- A single trial ($$n = 1$$) is a **Bernoulli distribution**
"""
)
