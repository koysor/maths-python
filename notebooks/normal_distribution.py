import marimo

__generated_with = "0.25.2"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from scipy import integrate, stats

    return integrate, mo, np, pd, plt, stats


@app.cell
def _(mo):
    mo.md(r"""
    # The Normal (Gaussian) Distribution

    The Normal distribution is the classic **bell curve**.  It is symmetric, most values cluster near the mean, and the tails fall away rapidly.

    It matters in quantitative finance because empirical daily returns, once standardised, fit the Normal distribution remarkably well.  This notebook works through three claims about it:

    1. The standard Normal has mean 0, standard deviation 1 and total area 1.
    2. About 68%, 95% and 99.7% of values lie within 1, 2 and 3 standard deviations of the mean.
    3. Daily returns can be modelled as $R_i = \bar{R} + s\,\phi_i$, **but** real returns have fatter tails than the Normal predicts.

    Each section shows the Python code that does the work, followed by an interactive chart.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 1. The probability density function

    The **standard Normal** probability density function (PDF) is

    $$\phi(x) = \frac{1}{\sqrt{2\pi}} \, e^{-\frac{1}{2}x^2}$$

    and the general Normal with mean $\mu$ and standard deviation $\sigma$, written $N(\mu, \sigma^2)$, is

    $$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \, e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

    where

    - $x$ is the value of the random variable,
    - $\mu$ is the mean (the centre of the bell),
    - $\sigma$ is the standard deviation (the width of the bell),
    - $\frac{1}{\sqrt{2\pi}}$ is the constant that makes the total area under the curve equal to 1.

    The code below writes $\phi$ straight from the formula, checks it against SciPy, and integrates it over the whole real line.
    """)
    return


@app.cell
def _(integrate, mo, np, stats):
    def phi(x):
        """Standard Normal PDF, written straight from the formula."""
        return np.exp(-0.5 * x**2) / np.sqrt(2 * np.pi)

    check_points = np.linspace(-4, 4, 9)
    matches_scipy = np.allclose(phi(check_points), stats.norm.pdf(check_points))
    total_area, area_error = integrate.quad(phi, -np.inf, np.inf)

    mo.show_code(mo.md(f"""
    - Matches `scipy.stats.norm.pdf`: **{matches_scipy}**
    - Area under the curve: **{total_area:.10f}** (numerical error about {area_error:.1e})
    - Peak height $\\phi(0) = 1/\\sqrt{{2\\pi}}$: **{phi(0.0):.5f}**
    """))
    return (phi,)


@app.cell
def _(mo):
    mu_slider = mo.ui.slider(-2.0, 2.0, step=0.1, value=1.0, label="Mean $\\mu$")
    sigma_slider = mo.ui.slider(
        0.5, 2.0, step=0.1, value=1.5, label="Standard deviation $\\sigma$"
    )

    mo.vstack(
        [
            mo.md(r"""
    ## 2. Shifting and stretching: $\mu$ and $\sigma$

    Changing $\mu$ slides the bell left or right; changing $\sigma$ makes it wider and flatter or narrower and taller.  The area always stays 1.

    Any Normal can be turned back into the standard Normal by **standardising**: $z = \dfrac{x - \mu}{\sigma}$.  The densities are related by $f(x) = \phi(z) / \sigma$.
    """),
            mo.hstack([mu_slider, sigma_slider], justify="start"),
        ]
    )
    return mu_slider, sigma_slider


@app.cell
def _(mo, mu_slider, np, sigma_slider, stats):
    mu = mu_slider.value
    sigma = sigma_slider.value

    x_grid = np.linspace(-10, 10, 2001)
    general_pdf = stats.norm(mu, sigma).pdf(x_grid)

    # Standardise, then rescale the standard Normal density
    z_grid = (x_grid - mu) / sigma
    same_curve = np.allclose(general_pdf, stats.norm.pdf(z_grid) / sigma)
    area_general = np.trapezoid(general_pdf, x_grid)

    mo.show_code(
        mo.md(
            f"$f(x) = \\phi(z)/\\sigma$ everywhere: **{same_curve}**.  "
            f"Area under $N({mu:.1f}, {sigma:.1f}^2)$: **{area_general:.4f}**"
        )
    )
    return general_pdf, mu, sigma, x_grid


@app.cell
def _(general_pdf, mu, phi, plt, sigma, x_grid):
    fig_pdf, ax_pdf = plt.subplots(figsize=(8, 4))
    ax_pdf.plot(
        x_grid, phi(x_grid), "--", color="grey", label="Standard Normal $N(0, 1)$"
    )
    ax_pdf.plot(x_grid, general_pdf, color="C0", label=f"$N({mu:.1f}, {sigma:.1f}^2)$")
    ax_pdf.axvline(mu, color="C0", linewidth=0.8, linestyle=":")
    ax_pdf.set_xlim(-6, 6)
    ax_pdf.set_xlabel("$x$")
    ax_pdf.set_ylabel("Density")
    ax_pdf.set_title("Normal PDF: effect of the mean and standard deviation")
    ax_pdf.grid(True, alpha=0.3)
    ax_pdf.legend()
    fig_pdf.tight_layout()

    fig_pdf
    return


@app.cell
def _(mo):
    k_slider = mo.ui.slider(
        0.5, 4.0, step=0.1, value=2.0, label="Number of standard deviations $k$"
    )

    mo.vstack(
        [
            mo.md(r"""
    ## 3. The 68–95–99.7 rule

    The probability that a standard Normal value lies within $k$ standard deviations of the mean is

    $$P(-k \le Z \le k) = \Phi(k) - \Phi(-k)$$

    where $\Phi$ is the cumulative distribution function (CDF), the area under $\phi$ to the left of a point.  The table compares the rule of thumb with the exact values.
    """),
            k_slider,
        ]
    )
    return (k_slider,)


@app.cell
def _(mo, pd, stats):
    rule_rows = []
    for _k, _rule in [(1, 0.68), (2, 0.95), (3, 0.997)]:
        _exact = stats.norm.cdf(_k) - stats.norm.cdf(-_k)
        rule_rows.append({"k": _k, "Rule of thumb": _rule, "Exact": round(_exact, 5)})

    rule_table = pd.DataFrame(rule_rows)

    mo.show_code(rule_table)
    return


@app.cell
def _(k_slider, np, phi, plt, stats):
    k_value = k_slider.value
    _x = np.linspace(-4.5, 4.5, 901)
    _inside = np.abs(_x) <= k_value
    _area_inside = stats.norm.cdf(k_value) - stats.norm.cdf(-k_value)

    fig_rule, ax_rule = plt.subplots(figsize=(8, 4))
    ax_rule.plot(_x, phi(_x), color="C0")
    ax_rule.fill_between(_x, phi(_x), where=_inside, color="C0", alpha=0.3)
    ax_rule.set_xlabel("$z$ (standard deviations from the mean)")
    ax_rule.set_ylabel("Density")
    ax_rule.set_title(
        f"P(-{k_value:.1f} ≤ Z ≤ {k_value:.1f}) = {_area_inside:.4f}"
        f"   (outside: {1 - _area_inside:.4f})"
    )
    ax_rule.grid(True, alpha=0.3)
    fig_rule.tight_layout()

    fig_rule
    return


@app.cell
def _(mo):
    r_bar_slider = mo.ui.slider(
        -0.2, 0.2, step=0.01, value=0.05, label="Daily mean return $\\bar{R}$ (%)"
    )
    vol_slider = mo.ui.slider(
        0.2, 4.0, step=0.1, value=1.2, label="Daily volatility $s$ (%)"
    )
    n_days_slider = mo.ui.slider(
        50, 2520, step=10, value=1260, label="Number of trading days"
    )

    mo.vstack(
        [
            mo.md(r"""
    ## 4. Simulating daily returns

    If standardised returns are Normal, each daily return can be modelled as

    $$R_i = \bar{R} + s \cdot \phi_i, \qquad \phi_i \sim N(0, 1)$$

    where $\bar{R}$ is the average daily return, $s$ is the daily standard deviation (volatility) and $\phi_i$ is a fresh random draw from the standard Normal each day.  Compounding the returns gives a price path $S_i = S_0 \prod_{j=1}^{i} (1 + R_j)$, starting from $S_0 = 100$.
    """),
            mo.hstack([r_bar_slider, vol_slider, n_days_slider], justify="start"),
        ]
    )
    return n_days_slider, r_bar_slider, vol_slider


@app.cell
def _(mo, n_days_slider, np, pd, r_bar_slider, vol_slider):
    rng = np.random.default_rng(42)
    phi_draws = rng.standard_normal(n_days_slider.value)

    r_bar = r_bar_slider.value / 100
    daily_vol = vol_slider.value / 100
    daily_returns = r_bar + daily_vol * phi_draws  # R_i = R̄ + s·φ_i
    prices = 100 * np.cumprod(1 + daily_returns)

    sample_stats = pd.DataFrame(
        {
            "Model": [r_bar, daily_vol],
            "Sample": [daily_returns.mean(), daily_returns.std(ddof=1)],
        },
        index=["Mean", "Standard deviation"],
    )

    mo.show_code(sample_stats)
    return daily_returns, daily_vol, prices, r_bar


@app.cell
def _(daily_returns, daily_vol, np, plt, r_bar, stats):
    _x = np.linspace(daily_returns.min(), daily_returns.max(), 400)

    fig_returns, ax_returns = plt.subplots(figsize=(8, 4))
    ax_returns.hist(
        daily_returns,
        bins=50,
        density=True,
        alpha=0.5,
        color="C0",
        label="Simulated returns",
    )
    ax_returns.plot(
        _x, stats.norm(r_bar, daily_vol).pdf(_x), color="C1", label="Model Normal PDF"
    )
    ax_returns.set_xlabel("Daily return")
    ax_returns.set_ylabel("Density")
    ax_returns.set_title("Histogram of simulated daily returns")
    ax_returns.grid(True, alpha=0.3)
    ax_returns.legend()
    fig_returns.tight_layout()

    fig_returns
    return


@app.cell
def _(plt, prices):
    fig_prices, ax_prices = plt.subplots(figsize=(8, 4))
    ax_prices.plot(range(1, len(prices) + 1), prices, color="C0")
    ax_prices.axhline(100, color="grey", linewidth=0.8, linestyle="--")
    ax_prices.set_xlabel("Trading day")
    ax_prices.set_ylabel("Price")
    ax_prices.set_title("Price path built from the simulated returns ($S_0 = 100$)")
    ax_prices.grid(True, alpha=0.3)
    fig_prices.tight_layout()

    fig_prices
    return


@app.cell
def _(mo):
    nu_slider = mo.ui.slider(
        3, 30, step=1, value=4, label="Student-t degrees of freedom $\\nu$"
    )

    mo.vstack(
        [
            mo.md(r"""
    ## 5. The caveat: fat tails

    Real returns have slightly **fatter tails** than a perfect Normal, so extreme moves happen more often than the model predicts.  A common stand-in for fat-tailed returns is the **Student-t** distribution with $\nu$ degrees of freedom.  Its variance is $\nu / (\nu - 2)$, so we rescale it to have variance 1 and compare it fairly with the standard Normal.

    The data here are synthetic: the notebook runs in your browser and cannot download market prices.  Smaller $\nu$ means fatter tails; as $\nu \to \infty$ the Student-t becomes the Normal.

    The table converts each tail probability into "once every $N$ trading days" (about 252 trading days make a year).
    """),
            nu_slider,
        ]
    )
    return (nu_slider,)


@app.cell
def _(mo, np, nu_slider, pd, stats):
    nu = nu_slider.value
    t_unit = stats.t(nu, scale=np.sqrt((nu - 2) / nu))  # Student-t with variance 1

    tail_rows = []
    for _k in [3, 4, 5]:
        _p_normal = 2 * stats.norm.sf(_k)  # P(|Z| > k)
        _p_t = 2 * t_unit.sf(_k)
        tail_rows.append(
            {
                "k": _k,
                "Normal P(|Z|>k)": f"{_p_normal:.2e}",
                "Normal: once every N days": f"{1 / _p_normal:,.0f}",
                "Student-t P(|Z|>k)": f"{_p_t:.2e}",
                "Student-t: once every N days": f"{1 / _p_t:,.0f}",
            }
        )

    tail_table = pd.DataFrame(tail_rows)

    mo.show_code(tail_table)
    return nu, t_unit


@app.cell
def _(np, nu, phi, plt, t_unit):
    _x = np.linspace(-6, 6, 1201)

    fig_tails, ax_tails = plt.subplots(figsize=(8, 4))
    ax_tails.plot(_x, phi(_x), color="C0", label="Standard Normal")
    ax_tails.plot(
        _x, t_unit.pdf(_x), color="C3", label=f"Student-t, ν = {nu} (variance 1)"
    )
    ax_tails.set_yscale("log")
    ax_tails.set_ylim(1e-9, 1)
    ax_tails.set_xlabel("Standard deviations from the mean")
    ax_tails.set_ylabel("Density (log scale)")
    ax_tails.set_title(
        "Fat tails: the Student-t decays far more slowly than the Normal"
    )
    ax_tails.grid(True, alpha=0.3)
    ax_tails.legend()
    fig_tails.tight_layout()

    fig_tails
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 6. Spotting fat tails with a QQ plot

    A **quantile–quantile (QQ) plot** sorts a standardised sample and plots it against the quantiles a Normal distribution would give.  Normal data lie on a straight line.  Fat-tailed data bend into an **S-shape**: the extreme points sit below the line on the left and above it on the right, because they are more extreme than the Normal expects.
    """)
    return


@app.cell
def _(mo, np, nu, plt, stats, t_unit):
    rng_qq = np.random.default_rng(7)
    normal_sample = rng_qq.standard_normal(1000)
    t_sample = t_unit.rvs(size=1000, random_state=rng_qq)

    # Standardise, as we would with real returns
    t_standardised = (t_sample - t_sample.mean()) / t_sample.std(ddof=1)

    fig_qq, (ax_qq_normal, ax_qq_t) = plt.subplots(1, 2, figsize=(8, 4), sharey=True)
    stats.probplot(normal_sample, dist="norm", plot=ax_qq_normal)
    stats.probplot(t_standardised, dist="norm", plot=ax_qq_t)
    ax_qq_normal.set_title("Normal sample")
    ax_qq_t.set_title(f"Student-t sample, ν = {nu}")
    fig_qq.tight_layout()

    mo.show_code(mo.as_html(fig_qq))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Key takeaways

    - The standard Normal $\phi(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$ has mean 0, standard deviation 1 and total area 1.
    - Any Normal can be standardised with $z = (x - \mu)/\sigma$, so one table or function covers them all.
    - About 68%, 95% and 99.7% of values lie within 1, 2 and 3 standard deviations of the mean.
    - Daily returns can be simulated as $R_i = \bar{R} + s\,\phi_i$, which is the starting point for modelling asset prices.
    - **But** real returns have fatter tails: a Normal model underestimates how often large losses occur, which matters for risk measures such as Value at Risk.
    """).callout(kind="info")
    return


if __name__ == "__main__":
    app.run()
