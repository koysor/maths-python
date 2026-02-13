import marimo

__generated_with = "0.17.8"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt

    return mo, np, plt


@app.cell
def _(mo):
    mo.md(r"""
    ### Euler's Number

    The number $e$ in mathematics is a fundamental mathematical constant approximately equal to 2.71828.  It is the base of the natural logarithm and the natural exponential function.

    Mathematically, $e$ can be defined as the limit:

    $$e = \lim_{n \to \infty} \left( 1 + \frac{1}{n} \right)^n$$

    The function $y = e^x$ has a slope of 1 at $x = 0$ .
    The gradient of the function $e^x$ is also $e^x$.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### $x$ against $e^x$
    """)
    return


@app.cell
def _(np, plt):
    # Generate data
    x = np.linspace(-2, 5, 100)
    y = np.exp(x)

    # Create the plot
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, y, label="$e^x$")
    ax.set_xlabel("x")
    ax.set_ylabel("$e^x$")
    ax.set_title("Plot of x vs $e^x$")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()

    fig
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
