import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


st.set_page_config(layout="wide")
st.markdown("### The Normal Distribution")


st.write(
    "The Normal Distribution (also known as the Gaussian distribution) is a continuous probability distribution defined by its *mean* (μ) and *standard deviation* (σ).  Denoted as:"
)
st.write(
    "The Normal Distribution is symmetric about the mean, with a bell-shaped curve."
)
st.write(
    "The area under the curve represents the total probability, which is equal to 1."
)


col1, col2 = st.columns(2)

with col1:

    latex_code = r"""
    \mathcal{N}(\mu, \sigma^2)
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)
    st.write(
        """Where:
    - $$\mu$$ is the mean
    - $$\sigma$$ is the standard deviation
    - $$\sigma^2$$ is the variance
    """
    )
    st.write(
        "The mean (μ) is the center of the distribution, and the standard deviation (σ) determines the width of the curve."
    )
    st.write(
        "The larger the standard deviation, the wider the curve, indicating more variability in the data."
    )
    st.write(
        "The normal distribution is often used in statistics to model real-valued random variables whose distributions are not known."
    )
    st.write(
        "Many statistical tests and methods assume that the data follows a normal distribution."
    )
    st.write(
        "The normal distribution is important in statistics because of the Central Limit Theorem, which states that the sum of a large number of independent and identically distributed random variables will be approximately normally distributed, regardless of the underlying distribution."
    )

with col2:

    st.write(
        "The probability density function (PDF) of the normal distribution is given by the formula:"
    )
    latex_code = r"""
    \begin{equation}
    f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}
    \end{equation}
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)
    st.write(
        """Where:
    - $$f(x)$$ is the probability density function (PDF)
    - $$\mu$$ is the mean
    - $$\sigma$$ is the standard deviation
    - $$e$$ is the base of the natural logarithm
    - $$\pi$$ is the constant pi
    """
    )


# Streamlit UI
st.title("Normal Distribution with Shaded Area")

# User inputs
mu = st.number_input("Mean (μ)", value=0.0)
variance = st.number_input("Variance (σ²)", value=1.0, min_value=0.001)
a = st.number_input("Shaded Area Up To x = a", value=0.0)

# Calculate standard deviation from variance
sigma = np.sqrt(variance)

# Generate x values
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
y = norm.pdf(x, mu, sigma)

# Create the plot
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, label=f"N({mu}, {variance})", color="blue")

# Shade area under curve up to point a
x_fill = np.linspace(mu - 4 * sigma, a, 1000)
y_fill = norm.pdf(x_fill, mu, sigma)
ax.fill_between(x_fill, y_fill, alpha=0.4, color="skyblue", label=f"P(X ≤ {a})")

# Add vertical line for mean
ax.axvline(mu, color="red", linestyle="--", label="μ (Mean)")

# Labels and legend
ax.set_title("Normal Distribution with Shaded Area")
ax.set_xlabel("x")
ax.set_ylabel("Probability Density")
ax.grid(True)
ax.legend()

# Show plot in Streamlit
st.pyplot(fig)

# Display the probability P(X ≤ a)
p = norm.cdf(a, mu, sigma)
st.markdown(f"**P(X ≤ {a}) = {p:.4f}**")
