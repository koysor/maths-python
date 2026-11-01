"""Run every Streamlit page and report the ones that fail.

Each page gets its own process, because repeated imports in one process produce
false NumPy errors, and `sys.path` is set the way `streamlit run` sets it: the
entry script's folder is added, and the repository root is not.

Runs without pytest, so CI can use it on an install without dev dependencies:
    uv run --no-sync python tests/page_runner.py
"""

import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE_DIR = ROOT / "app" / "pages"

_RUN_PAGE = """
import os, sys
root = os.getcwd()
sys.path[:] = [os.path.join(root, "app")] + [p for p in sys.path if p not in ("", root)]
from streamlit.testing.v1 import AppTest
at = AppTest.from_file(os.path.abspath(sys.argv[1]), default_timeout=120).run()
sys.exit(1 if at.exception else 0)
"""


def page_files() -> list[Path]:
    """Return every page script, which excludes the snippet folder and `__init__.py`."""
    return sorted(p for p in PAGE_DIR.glob("*.py") if p.name != "__init__.py")


def run_page(page: Path) -> str | None:
    """Run one page, returning None on success or its error output on failure."""
    result = subprocess.run(
        [sys.executable, "-c", _RUN_PAGE, str(page)],
        cwd=ROOT,
        env={**os.environ, "MPLBACKEND": "Agg"},
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=300,
    )
    return None if result.returncode == 0 else result.stderr[-1500:]


def run_all_pages() -> dict[str, str | None]:
    """Run every page in parallel and map each file name to its outcome."""
    pages = page_files()
    with ThreadPoolExecutor(max_workers=os.cpu_count()) as pool:
        return dict(zip((p.name for p in pages), pool.map(run_page, pages)))


if __name__ == "__main__":
    outcomes = run_all_pages()
    failures = {name: error for name, error in outcomes.items() if error}
    for name, error in failures.items():
        print(f"FAILED {name}\n{error}\n")
    print(f"{len(outcomes) - len(failures)} of {len(outcomes)} pages ran cleanly")
    sys.exit(1 if failures else 0)
