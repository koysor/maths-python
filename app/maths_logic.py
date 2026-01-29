"""Mathematical logic functions for symbolic and numerical calculus operations."""

import sympy


def numerical_derivative(func, x, h=1e-5):
    """
    Compute the numerical derivative of a function at a point using central differences.

    Args:
        func: A callable function f(x) to differentiate.
        x: The point at which to evaluate the derivative.
        h: Step size for the finite difference (default: 1e-5).

    Returns:
        The approximate derivative f'(x).
    """
    return (func(x + h) - func(x - h)) / (2 * h)


def power_rule(variable, exponent):
    """
    Computes the derivative of a variable raised to a power.
    """
    x = sympy.symbols(variable)
    return sympy.diff(x**exponent, x)
