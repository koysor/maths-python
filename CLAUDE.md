# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Educational Streamlit web application providing interactive Python code snippets for mathematics and statistics.

**Live deployments:**

- AWS EC2: https://koysor.duckdns.org/maths/

## Commands

**Run the application:**

```bash
./launch_streamlit_app.sh
# or directly:
streamlit run app/maths_python.py
```

**Format code:**

```bash
black .
```

**Lint code:**

```bash
ruff check .
```

**CI runs both checks on the entire repo** (not just `app/`), so format and lint from the root.

**Docker (local):**

```bash
cd docker
docker-compose up --build
# or directly:
docker build -f docker/Dockerfile -t maths-python .
docker run -p 8505:8501 maths-python
```

**Run tests:**

```bash
pytest                        # Run all tests
pytest tests/test_utils.py    # Run a single test file
```

**Dependency management (uses uv):**

```bash
uv sync           # Install dependencies
uv add <package>  # Add new dependency
```

**Pre-commit hooks** (Black, Ruff, detect-secrets) run automatically on `git commit`. Black will auto-reformat files and abort the commit — re-stage the reformatted files and commit again.

## Architecture

**Multi-page Streamlit app** where each `.py` file in `app/pages/` becomes a navigable page.

**Entry point:** `app/maths_python.py`

**Page organization:** Numeric prefixes control sidebar order (e.g., `100_calculus.py`, `200_integration.py`). Prefixes are auto-hidden in the UI.

**Topic clusters:**

- 100s: Calculus/Differentiation
- 200s: Integration techniques
- 300s: Stochastic calculus
- 700s: Linear algebra
- 800s: Probability & statistics
- 850s–860s: Algebra (logarithms, completing the square)
- 999s: Reference pages

**Key utility:** `app/utils.py:display_run_python_snippet()` - Standard pattern for showing code with 4/6 width layout and executing it inline.

## Page Pattern

Each page follows this structure:

1. `st.set_page_config(layout="wide")`
2. Markdown content with LaTeX math notation
3. Code snippets using `display_run_python_snippet()` or direct `st.code()` + `exec()`
4. Interactive components (sliders, inputs) for visualization

**Choosing a code snippet pattern:**

- `display_run_python_snippet(code)` — use for standalone snippets; renders code at 4/6 screen width with output below.
- Code-as-string + `st.code` + `exec` — use for side-by-side layouts where the code is shown in one column and its output (e.g. a chart) in another. Define the code once as a string to avoid duplication:

```python
chart_code = """
import matplotlib.pyplot as plt
...
st.pyplot(fig)
"""
with col_left:
    st.code(chart_code, language="python")
with col_right:
    exec(chart_code)
```

## Key Libraries

### Symbolic Mathematics

- **SymPy** - Computer algebra system for symbolic mathematics
  - Symbolic differentiation and integration
  - Equation solving and simplification
  - LaTeX output via `sympy.latex()` for mathematical rendering
  - Limit calculations and series expansions

### Numerical Computing

- **NumPy** - Fundamental numerical computing
  - Array operations for numerical examples
  - Linear algebra operations for matrix calculations
  - Random number generation for probability demonstrations

- **SciPy** - Scientific computing and advanced numerical methods
  - `scipy.stats` - Probability distributions and statistical functions
  - `scipy.integrate` - Numerical integration methods
  - `scipy.linalg` - Advanced linear algebra operations
  - `scipy.special` - Special mathematical functions

- **pandas** - Data manipulation and tabular data
  - DataFrame structures for organising computational results
  - Data presentation in interactive examples

### Visualisation

- **Matplotlib** - Plotting and visualisations
  - Function plots for calculus demonstrations
  - Distribution plots for probability topics
  - 3D surface plots for multivariable calculus

### Web Application

- **Streamlit** - Interactive web application framework
  - Multi-page navigation for topic organisation
  - Interactive widgets (sliders, inputs) for parameter adjustment
  - LaTeX rendering via `st.latex()`

### Development Tools

- **JupyterLab / Marimo** - Interactive notebook environments
- **pytest** - Testing framework
- **Black** - Code formatting
- **Ruff** - Linting
- **NetworkX** - Graph and network analysis (dev dependency)

## Conventions

- Use British English spellings (e.g., "colour", "centre", "organised", "behaviour")
- Use two spaces after a full stop in prose strings (`st.info`, `st.markdown`, etc.)
- Draft pages use `*_.py` pattern (e.g., `300_calculus_stochastic_.py`) and are gitignored; pages without a numeric prefix appear in the sidebar but have no guaranteed ordering
- Use `st.latex()` for math notation with SymPy's `latex()` function
- Wide layout is standard: `st.set_page_config(layout="wide")`
- Column-based layouts for side-by-side content
- Heatmaps: use `cmap="Blues"` with `vmin=0, vmax=abs_max*2` for non-negative matrices; use `cmap="RdBu_r"` with symmetric `vmin=-abs_max, vmax=abs_max` when the matrix contains negative values
