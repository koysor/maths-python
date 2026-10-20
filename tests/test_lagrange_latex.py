import ast
from pathlib import Path

from sympy.parsing.latex import parse_latex

PAGE = Path("app/pages/lagrange.py")


def page_latex_expressions():
    """Return every `latex_code = ...` string assigned in the Lagrange page."""
    tree = ast.parse(PAGE.read_text(encoding="utf-8"))
    return [
        node.value.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Assign)
        and any(getattr(target, "id", "") == "latex_code" for target in node.targets)
    ]


def test_page_has_latex_expressions():
    """Guard against the extraction silently finding nothing."""
    assert page_latex_expressions()


def test_lagrange_latex_parses():
    """SymPy's LaTeX parser needs a specific antlr4-python3-runtime version.

    antlr4 4.13.x makes parse_latex raise ImportError, which would crash the
    Lagrange page.  The runtime is pinned in pyproject.toml; this test makes a
    bad bump fail in CI instead of in production.
    """
    for latex_code in page_latex_expressions():
        assert parse_latex(latex_code) is not None
