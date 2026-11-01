# Copilot instructions

## Build, test, and run

Python dependencies are managed with `uv`.

```bash
uv sync
./launch_streamlit_app.sh
uv run streamlit run app/maths_python.py
uv run pytest
uv run pytest tests/test_calculus.py
uv run pytest tests/test_calculus.py::test_name
uv run black --check .
uv run ruff check .
uv run mypy src/maths_lib
uv run pre-commit run --all-files
```

Use the test file and pytest node ID relevant to the change for focused runs.
The launcher resolves the repository path and invokes Streamlit through `uv`.
Docker instructions are in `docker/README.md`.

## Architecture

`app/maths_python.py` is the Streamlit entry point. Streamlit discovers each
Python file in `app/pages/` as a page; numeric filename prefixes set sidebar
order and group topics (100s calculus, 200s integration, 300s stochastic
calculus, 700s linear algebra, 800s probability and algebra, and 999s reference
pages).
`src/maths_lib/` is an installable package for calculations the reader never
sees and helpers shared between pages; code displayed as part of a lesson stays
in its page. `app/utils.py` provides the shared snippet display helper.
`app/pages/code_snippets/` contains standalone examples used by pages;
`notebooks/` is for exploratory work.

`tests/test_pages.py` runs every page with the `sys.path` that `streamlit run`
sets, so pages must not import from `app.`. Anything needed at runtime belongs in
`[project].dependencies`, because the Docker image installs with `--no-dev`;
`tests/test_dependencies.py` checks this.

## Repository-specific conventions

- Use British English in page prose and labels. Use two spaces after full stops
  in new user-facing prose strings; older pages are mixed.
- Pages use `st.set_page_config(layout="wide")` and `st.latex()` for equations.
  Use `display_run_python_snippet(code)` for a standalone snippet. For
  side-by-side code and output, define the code once as a string and both show
  and execute that same string.
- Numeric page prefixes control order and are hidden in the UI. New draft pages
  ending in `_.py` are gitignored, but 7 older ones (for example
  `810_probability_poisson_.py`) are tracked, so edits to them do show up. Pages
  without numeric prefixes have no guaranteed sidebar order.
- Keep heatmap scales comparable: use `Blues` with `vmin=0` and
  `vmax=abs_max*2` for non-negative matrices; use `RdBu_r` with symmetric
  bounds for matrices containing negative values.
- Streamlit settings live in `.streamlit/config.toml`; only use supported
  options.
