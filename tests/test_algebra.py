import sympy
from maths_lib.algebra import vertex_coefficients


def test_vertex_form_matches_the_original_quadratic():
    """Verify a(x - h)^2 + k expands back to ax^2 + bx + c, including fractions."""
    x = sympy.symbols("x")
    for a, b, c in [(1, 6, 5), (2, 3, -4), (-3, 5, 1)]:
        h, k = vertex_coefficients(a, b, c)
        assert sympy.expand(a * (x - h) ** 2 + k) == a * x**2 + b * x + c
