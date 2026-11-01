"""Calculations for Euler's number and the natural logarithm."""

from math import factorial

import pandas as pd
import sympy


def convergence_table() -> pd.DataFrame:
    """Tabulate the limit and series approximations to e for increasing n."""
    rows = []
    for n in [1, 2, 5, 10, 50, 100, 1_000, 10_000, 100_000]:
        limit_approx = (1 + 1 / n) ** n
        series_terms = min(n, 20)  # series converges in ~20 terms
        series_approx = 0.0
        for k in range(series_terms + 1):
            series_approx += 1 / factorial(k)
        rows.append(
            {
                "n": f"{n:,}",
                "Limit: (1 + 1/n)^n": f"{limit_approx:.10f}",
                "Series: sum 1/k!": f"{series_approx:.10f}",
            }
        )
    return pd.DataFrame(rows)


def exponential_derivatives() -> tuple[str, str, str]:
    """Return the derivatives of e^x, ln(x) and a^x as strings."""
    x = sympy.Symbol("x")
    a = sympy.Symbol("a", positive=True)
    return (
        str(sympy.diff(sympy.exp(x), x)),
        str(sympy.diff(sympy.ln(x), x)),
        str(sympy.diff(a**x, x)),
    )
