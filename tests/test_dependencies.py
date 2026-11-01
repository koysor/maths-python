import ast
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCAL_MODULES = {"app", "maths_lib", "pages", "utils"}
# Top-level modules provided by a package with a different name
PROVIDED_BY = {"mpl_toolkits": "matplotlib"}
# Modules that need a package their own distribution doesn't install
ALSO_NEEDS = {"sympy.parsing.latex": "antlr4-python3-runtime"}


def imported_modules(path: Path) -> set[str]:
    """Return the full dotted name of every absolute module imported by a file."""
    modules = set()
    for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
        if isinstance(node, ast.Import):
            modules.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.level == 0:
            modules.add(node.module)
    return modules


def required_packages(modules: set[str]) -> set[str]:
    """Translate imported modules into the packages that must be installed."""
    packages = {ALSO_NEEDS[m] for m in modules if m in ALSO_NEEDS}
    for top_level in {m.split(".")[0] for m in modules}:
        if top_level not in sys.stdlib_module_names | LOCAL_MODULES:
            packages.add(PROVIDED_BY.get(top_level, top_level))
    return packages


def runtime_dependencies() -> set[str]:
    """Return the package names in pyproject.toml's runtime dependencies."""
    pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    return {
        re.match(r"[A-Za-z0-9._-]+", requirement).group().lower()
        for requirement in pyproject["project"]["dependencies"]
    }


def test_shipped_code_only_needs_runtime_dependencies():
    """Verify everything the app imports is installed by the --no-dev Docker image."""
    files = [*(ROOT / "app").rglob("*.py"), *(ROOT / "src").rglob("*.py")]
    needed = required_packages(set().union(*map(imported_modules, files)))
    assert not needed - runtime_dependencies()


def test_latex_parsing_needs_antlr4():
    """Verify the indirect requirement behind parse_latex is detected."""
    assert required_packages({"sympy.parsing.latex"}) == {
        "antlr4-python3-runtime",
        "sympy",
    }
