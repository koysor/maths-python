import math
import sympy
from app.maths_logic import power_rule, numerical_derivative


def test_power_rule():
    """Verify power_rule returns correct symbolic derivatives for various exponents."""
    assert power_rule("x", 2) == 2 * sympy.symbols("x")
    assert power_rule("y", 3) == 3 * sympy.symbols("y") ** 2
    assert power_rule("z", 0) == 0


def test_numerical_derivative():
    """Verify numerical_derivative approximates derivatives using central differences."""
    # Derivative of x^2 at x=3 should be 6
    assert math.isclose(numerical_derivative(lambda x: x**2, 3), 6, rel_tol=1e-5)

    # Derivative of a constant should be 0
    assert math.isclose(numerical_derivative(lambda x: 5, 10), 0, abs_tol=1e-10)

    # Derivative of sin(x) at x=0 should be cos(0) = 1
    assert math.isclose(numerical_derivative(math.sin, 0), 1, rel_tol=1e-5)
