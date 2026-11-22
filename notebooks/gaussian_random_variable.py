import marimo

__generated_with = "0.25.2"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from scipy import stats

    return mo, np, pd, plt, stats


@app.cell
def _(mo):
    mo.md(r"""
    # The Gaussian Random Variable $\phi$

    Formulas in statistics, physics and finance often contain a symbol $\phi$ with the remark "where $\phi$ is drawn from a standard Normal distribution".  This notebook is about what that remark means.

    The central idea is that **one value of $\phi$ is unpredictable, but many values of $\phi$ follow a precise law**.  You will draw values, watch the bell curve emerge from them, and see how the same draws produce any other Gaussian.

    ## 1. What is $\phi$?

    We write

    $$\phi \sim \mathcal{N}(0, 1)$$

    which reads "$\phi$ is distributed as a Normal (Gaussian) with mean 0 and variance 1".

    - $\phi$ is the **random variable**: a quantity whose value is not known until it is drawn.
    - $\phi_i$ is a **realisation**: the number obtained on draw $i$, such as $0.305$.
    - $\sim$ means "is distributed as".  It does not mean "equals".
    - $f(x) = \dfrac{1}{\sqrt{2\pi}} \, e^{-x^2/2}$ is the **probability density** of $\phi$ at a possible value $x$.
    - $\Phi(x) = P(\phi \le x)$ is the **cumulative distribution function** (CDF): the area under $f$ to the left of $x$.

    Two properties define its centre and spread:

    $$\mathbb{E}[\phi] = 0, \qquad \mathrm{Var}(\phi) = \mathbb{E}[\phi^2] = 1$$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    **A clash of notation.**  Many books, and the [Normal distribution notebook](https://koysor.github.io/maths-python/normal_distribution.html), write $\phi(x)$ for the density.  In this notebook $\phi$ is always the random variable, and the density is $f(x)$.
    """).callout(kind="warn")
    return


@app.cell
def _(mo):
    n_slider = mo.ui.slider(
        steps=[1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000],
        value=100,
        show_value=True,
        label="Number of draws $n$",
    )
    seed_input = mo.ui.number(start=0, stop=99999, step=1, value=42, label="Seed")

    mo.vstack(
        [
            mo.md(r"""
    ## 2. Drawing $\phi$

    A random number generator supplies the draws.  Each is **independent**, so knowing $\phi_1$ tells you nothing about $\phi_2$.

    The **seed** fixes the sequence so that the results can be repeated.  Change it to get a different sequence from the same distribution.  Increasing $n$ adds draws to the ones you already have.  Both controls drive the rest of the notebook.
    """),
            mo.hstack([n_slider, seed_input], justify="start"),
        ]
    )
    return n_slider, seed_input


@app.cell
def _(mo, n_slider, np, seed_input):
    mo.stop(seed_input.value is None, mo.md("Enter a seed to draw values of $\\phi$."))

    seed = int(seed_input.value)
    n_draws = n_slider.value

    rng = np.random.default_rng(seed)
    all_draws = rng.standard_normal(10_000)
    phi_draws = all_draws[:n_draws]  # the first n realisations of φ

    first_draws = mo.md(
        "\n".join(
            f"- $\\phi_{_i} = {_value:.4f}$"
            for _i, _value in enumerate(phi_draws[:5], start=1)
        )
    )

    mo.show_code(first_draws)
    return all_draws, n_draws, phi_draws, seed


@app.cell
def _(np, phi_draws, plt):
    _shown = phi_draws[:100]
    _index = np.arange(1, len(_shown) + 1)

    fig_draws, ax_draws = plt.subplots(figsize=(8, 4))
    ax_draws.axhspan(-1, 1, color="C0", alpha=0.12, label="Within 1 standard deviation")
    ax_draws.vlines(_index, 0, _shown, color="C0", linewidth=1)
    ax_draws.plot(_index, _shown, "o", color="C0", markersize=3, label="$\\phi_i$")
    ax_draws.axhline(0, color="grey", linewidth=0.8)
    ax_draws.set_xlim(0, len(_shown) + 1)
    ax_draws.set_ylim(-4.5, 4.5)
    ax_draws.set_xlabel("Draw number $i$")
    ax_draws.set_ylabel("Value drawn $\\phi_i$")
    ax_draws.set_title(f"Individual draws have no pattern (first {len(_shown)} shown)")
    ax_draws.grid(True, alpha=0.3)
    ax_draws.legend(loc="upper right")
    fig_draws.tight_layout()

    fig_draws
    return


@app.cell
def _(mo, n_slider):
    mo.vstack(
        [
            mo.md(r"""
    ## 3. The bell emerges

    Now ignore the order of the draws and count how many land in each small interval.  Dividing each count by $n$ times the width of the interval puts the histogram on the same scale as the density $f(x)$.

    Move $n$ from 1 up to 10,000.  The short marks under the axis are the draws themselves.
    """),
            n_slider,
        ]
    )
    return


@app.cell
def _(np, stats):
    x_grid = np.linspace(-4, 4, 801)
    density = stats.norm.pdf(x_grid)  # f(x)
    return density, x_grid


@app.cell
def _(density, n_draws, np, phi_draws, plt, x_grid):
    _edges = np.linspace(-4, 4, 33)
    _width = _edges[1] - _edges[0]
    # Not density=True, which would ignore any draws outside the plotted range
    _weights = np.full(n_draws, 1 / (n_draws * _width))

    fig_bell, ax_bell = plt.subplots(figsize=(8, 4))
    _heights, _, _ = ax_bell.hist(
        phi_draws,
        bins=_edges,
        weights=_weights,
        color="C0",
        alpha=0.5,
        label="Draws of $\\phi$",
    )
    ax_bell.plot(x_grid, density, color="C1", label="Density $f(x)$")
    _top = max(0.55, 1.1 * _heights.max())
    ax_bell.plot(
        phi_draws,
        np.full(n_draws, -0.04 * _top),
        "|",
        color="C0",
        alpha=max(0.05, min(1.0, 50 / n_draws)),
    )
    ax_bell.set_xlim(-4, 4)
    ax_bell.set_ylim(-0.08 * _top, _top)
    ax_bell.set_xlabel("Value $x$")
    ax_bell.set_ylabel("Density")
    ax_bell.set_title(f"Histogram of φ for n = {n_draws:,}")
    ax_bell.grid(True, alpha=0.3)
    ax_bell.legend()
    fig_bell.tight_layout()

    fig_bell
    return


@app.cell
def _(mo):
    interval_slider = mo.ui.range_slider(
        -4.0,
        4.0,
        step=0.1,
        value=[-1.0, 1.0],
        show_value=True,
        label="Interval from $a$ to $b$",
    )

    mo.vstack(
        [
            mo.md(r"""
    ## 4. Probability is area

    $\phi$ is continuous, so the probability of drawing any exact value is zero: $P(\phi = x) = 0$.  The height $f(x)$ is therefore **not** a probability.  Probabilities belong to intervals, and equal the area under the density:

    $$P(a \le \phi \le b) = \int_a^b f(x)\,dx = \Phi(b) - \Phi(a)$$

    Compare that exact area with the fraction of your draws that landed in the interval.  Then make $a = b$ and watch the probability vanish.
    """),
            interval_slider,
        ]
    )
    return (interval_slider,)


@app.cell
def _(interval_slider, mo, phi_draws, stats):
    a, b = interval_slider.value
    exact_probability = stats.norm.cdf(b) - stats.norm.cdf(a)
    observed_fraction = ((phi_draws >= a) & (phi_draws <= b)).mean()

    probability_summary = mo.md(
        f"Exact probability: **{exact_probability:.4f}**.  "
        f"Fraction of draws observed: **{observed_fraction:.4f}**."
    )

    mo.show_code(probability_summary)
    return a, b, exact_probability


@app.cell
def _(a, b, density, exact_probability, np, plt, stats, x_grid):
    _inside = np.linspace(a, b, 300)

    fig_area, ax_area = plt.subplots(figsize=(8, 4))
    ax_area.plot(x_grid, density, color="C1")
    ax_area.fill_between(_inside, stats.norm.pdf(_inside), color="C1", alpha=0.3)
    ax_area.vlines([a, b], 0, stats.norm.pdf([a, b]), color="C1", linestyle=":")
    ax_area.set_xlim(-4, 4)
    ax_area.set_ylim(0, 0.45)
    ax_area.set_xlabel("Value $x$")
    ax_area.set_ylabel("Density $f(x)$")
    ax_area.set_title(f"P({a:.1f} ≤ φ ≤ {b:.1f}) = {exact_probability:.4f}")
    ax_area.grid(True, alpha=0.3)
    fig_area.tight_layout()

    fig_area
    return


@app.cell
def _(mo, n_slider):
    mo.vstack(
        [
            mo.md(r"""
    ## 5. Mean 0 and variance 1

    The values 0 and 1 describe the distribution, not any particular sample.  From $n$ draws we can only estimate them:

    $$\bar{\phi} = \frac{1}{n}\sum_{i=1}^{n} \phi_i, \qquad s^2 = \frac{1}{n-1}\sum_{i=1}^{n} (\phi_i - \bar{\phi})^2$$

    The sample mean is itself random, with standard deviation $1/\sqrt{n}$.  **Four times as many draws only halves the typical error.**  The sample variance needs at least two draws.
    """),
            n_slider,
        ]
    )
    return


@app.cell
def _(mo, n_draws, pd, phi_draws):
    sample_mean = phi_draws.mean()
    sample_variance = phi_draws.var(ddof=1) if n_draws > 1 else None

    moments_table = pd.DataFrame(
        {
            "Statistic": ["Mean", "Variance"],
            "Theory": ["0", "1"],
            "Sample": [
                f"{sample_mean:.4f}",
                "—" if sample_variance is None else f"{sample_variance:.4f}",
            ],
        }
    )

    mo.show_code(moments_table)
    return


@app.cell
def _(all_draws, n_draws, np, plt, seed):
    _counts = np.arange(1, len(all_draws) + 1)
    _running_mean = np.cumsum(all_draws) / _counts
    _band = 1.96 / np.sqrt(_counts)

    fig_mean, ax_mean = plt.subplots(figsize=(8, 4))
    ax_mean.fill_between(
        _counts,
        -_band,
        _band,
        color="grey",
        alpha=0.2,
        label="95% band at each $n$: $\\pm 1.96/\\sqrt{n}$",
    )
    ax_mean.plot(_counts, _running_mean, color="C0", label="Running mean")
    ax_mean.plot(
        n_draws, _running_mean[n_draws - 1], "o", color="C3", label="Your choice of $n$"
    )
    ax_mean.axhline(0, color="grey", linewidth=0.8)
    ax_mean.set_xscale("log")
    ax_mean.set_ylim(-2, 2)
    ax_mean.set_xlabel("Number of draws $n$ (log scale)")
    ax_mean.set_ylabel("Sample mean")
    ax_mean.set_title(f"The sample mean settles towards 0 (seed {seed})")
    ax_mean.grid(True, alpha=0.3)
    ax_mean.legend(loc="upper right")
    fig_mean.tight_layout()

    fig_mean
    return


@app.cell
def _(mo):
    mo.md(r"""
    The band holds 95% of sample means **at each separate value of $n$**.  It does not promise that 95% of whole paths stay inside, so expect some seeds to wander out for a while.
    """)
    return


@app.cell
def _(mo):
    u_slider = mo.ui.slider(
        0.001,
        0.999,
        step=0.001,
        value=0.841,
        show_value=True,
        label="Uniform draw $u$",
    )

    mo.vstack(
        [
            mo.md(r"""
    ## 6. Where can a draw come from?

    Suppose you can only draw $u$ uniformly between 0 and 1.  Feeding it backwards through the CDF gives a Gaussian draw:

    $$u \sim U[0, 1] \quad \Longrightarrow \quad \phi = \Phi^{-1}(u) \sim \mathcal{N}(0, 1)$$

    This is **inverse transform sampling**.  It works because $P(\Phi^{-1}(u) \le x) = P(u \le \Phi(x)) = \Phi(x)$.  The CDF is steep near 0, so a wide range of $u$ maps to values near the centre, and only a sliver maps to each tail.

    NumPy's `standard_normal` uses a faster method called the *ziggurat algorithm*, but the draws have the same distribution.
    """),
            u_slider,
        ]
    )
    return (u_slider,)


@app.cell
def _(mo, stats, u_slider):
    u_value = u_slider.value
    phi_from_u = stats.norm.ppf(u_value)  # ppf is the inverse CDF

    inverse_summary = mo.md(
        f"$u = {u_value:.3f}$ gives $\\phi = \\Phi^{{-1}}(u) = {phi_from_u:.4f}$"
    )

    mo.show_code(inverse_summary)
    return phi_from_u, u_value


@app.cell
def _(phi_from_u, plt, stats, u_value, x_grid):
    fig_inverse, ax_inverse = plt.subplots(figsize=(8, 4))
    ax_inverse.plot(x_grid, stats.norm.cdf(x_grid), color="C1", label="CDF $\\Phi(x)$")
    ax_inverse.plot(
        [-4, phi_from_u, phi_from_u],
        [u_value, u_value, 0],
        "--",
        color="C0",
        label="$u \\to \\phi$",
    )
    ax_inverse.plot(phi_from_u, u_value, "o", color="C0")
    ax_inverse.set_xlim(-4, 4)
    ax_inverse.set_ylim(0, 1.02)
    ax_inverse.set_xlabel("Value $x$")
    ax_inverse.set_ylabel("Cumulative probability $u$")
    ax_inverse.set_title("Turning a uniform draw into a Gaussian draw")
    ax_inverse.grid(True, alpha=0.3)
    ax_inverse.legend(loc="center left")
    fig_inverse.tight_layout()

    fig_inverse
    return


@app.cell
def _(mo):
    mu_slider = mo.ui.slider(
        -3.0, 3.0, step=0.1, value=2.0, show_value=True, label="Mean $\\mu$"
    )
    sigma_slider = mo.ui.slider(
        0.5,
        3.0,
        step=0.1,
        value=1.5,
        show_value=True,
        label="Standard deviation $\\sigma$",
    )

    mo.vstack(
        [
            mo.md(r"""
    ## 7. Any Gaussian from $\phi$

    There is no need for a separate generator for each Gaussian.  Stretch $\phi$ by $\sigma$, then shift it by $\mu$:

    $$X = \mu + \sigma\phi \sim \mathcal{N}(\mu, \sigma^2)$$

    This is why $\phi$ appears in so many formulas: $\mu$ and $\sigma$ carry the units and the scale, while $\phi$ carries all the randomness.
    """),
            mo.hstack([mu_slider, sigma_slider], justify="start"),
        ]
    )
    return mu_slider, sigma_slider


@app.cell
def _(mo, mu_slider, phi_draws, sigma_slider):
    mu = mu_slider.value
    sigma = sigma_slider.value
    x_draws = mu + sigma * phi_draws  # the same draws, stretched and shifted

    transform_summary = mo.md(
        f"The first draw $\\phi_1 = {phi_draws[0]:.4f}$ "
        f"becomes $X_1 = {x_draws[0]:.4f}$"
    )

    mo.show_code(transform_summary)
    return mu, sigma, x_draws


@app.cell
def _(mu, n_draws, np, phi_draws, plt, sigma, stats, x_draws):
    _edges = np.linspace(-16, 16, 129)
    _weights = np.full(n_draws, 1 / (n_draws * (_edges[1] - _edges[0])))
    _x = np.linspace(-12, 12, 1201)

    fig_transform, ax_transform = plt.subplots(figsize=(8, 4))
    for _values, _mean, _sd, _colour, _label in [
        (phi_draws, 0, 1, "C0", "$\\phi$"),
        (x_draws, mu, sigma, "C2", "$X = \\mu + \\sigma\\phi$"),
    ]:
        ax_transform.hist(
            _values,
            bins=_edges,
            weights=_weights,
            color=_colour,
            alpha=0.35,
            label=_label,
        )
        ax_transform.plot(_x, stats.norm.pdf(_x, _mean, _sd), color=_colour)
    ax_transform.set_xlim(-12, 12)
    ax_transform.set_ylim(0, max(0.85, ax_transform.get_ylim()[1]))
    ax_transform.set_xlabel("Value")
    ax_transform.set_ylabel("Density")
    ax_transform.set_title("The same random draws on two different scales")
    ax_transform.grid(True, alpha=0.3)
    ax_transform.legend()
    fig_transform.tight_layout()

    fig_transform
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Key takeaways

    - $\phi \sim \mathcal{N}(0, 1)$ describes **how values are drawn**.  It is not one particular number.
    - A single draw is unpredictable, but the histogram of many draws approaches the bell curve.
    - Probability is the area under the density, so $P(a \le \phi \le b) = \Phi(b) - \Phi(a)$.
    - Sample estimates are noisy, and the error of the mean shrinks like $1/\sqrt{n}$.
    - A uniform draw becomes a Gaussian draw through $\phi = \Phi^{-1}(u)$.
    - Every Gaussian can be built from the standard one with $X = \mu + \sigma\phi$.
    """).callout(kind="info")
    return


if __name__ == "__main__":
    app.run()
