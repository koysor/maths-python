import math

from maths_lib.logarithms import convergence_table, exponential_derivatives


def test_convergence_table_approaches_e():
    """Verify both approximations converge on e, and the series gets closer."""
    table = convergence_table()
    assert table["n"].tolist()[0] == "1"
    assert table["n"].tolist()[-1] == "100,000"
    limit, series = (
        float(table[column].iloc[-1])
        for column in ("Limit: (1 + 1/n)^n", "Series: sum 1/k!")
    )
    assert math.isclose(limit, math.e, rel_tol=1e-4)
    assert math.isclose(series, math.e, rel_tol=1e-9)


def test_exponential_derivatives():
    """Verify the derivatives of e^x, ln(x) and a^x."""
    assert exponential_derivatives() == ("exp(x)", "1/x", "a**x*log(a)")
