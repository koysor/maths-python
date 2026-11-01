"""Algebraic manipulation of expressions."""

import sympy


def vertex_coefficients(a: int, b: int, c: int) -> tuple[sympy.Rational, sympy.Expr]:
    """Return (h, k) such that ax^2 + bx + c = a(x - h)^2 + k."""
    h = sympy.Rational(-b, 2 * a)
    k = c - sympy.Rational(b**2, 4 * a)
    return h, k
