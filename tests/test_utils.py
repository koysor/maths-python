import sympy
from app.utils import to_latex


def test_to_latex():
    """Verify to_latex converts SymPy expressions to valid LaTeX strings."""
    x = sympy.symbols("x")
    expr = x**2 + 2 * x + 1
    assert to_latex(expr) == "x^{2} + 2 x + 1"
