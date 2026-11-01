import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from page_runner import page_files, run_all_pages  # noqa: E402


@pytest.fixture(scope="session")
def page_outcomes():
    """Run all the pages once, in parallel, for the tests below to look up."""
    return run_all_pages()


@pytest.mark.parametrize("page", [p.name for p in page_files()])
def test_page_runs(page, page_outcomes):
    """Verify each page runs without an exception under `streamlit run`'s sys.path."""
    assert page_outcomes[page] is None, page_outcomes[page]
