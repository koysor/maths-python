# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Educational Streamlit web application providing interactive Python code snippets for mathematics and statistics. Live at https://maths-python-koysor.streamlit.app/

## Commands

**Run the application:**
```bash
./launch_streamlit_app.sh
# or directly:
streamlit run app/maths_python.py
```

**Format code:**
```bash
black app/
```

**Lint code:**
```bash
ruff check app/
```

**Docker (local):**
```bash
docker build -f docker/Dockerfile -t maths-python-app .
docker run -p 8501:8501 maths-python-app
```

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
- 999s: Reference pages

**Key utility:** `app/utils.py:display_run_python_snippet()` - Standard pattern for showing code with 4/6 width layout and executing it inline.

## Page Pattern

Each page follows this structure:
1. `st.set_page_config(layout="wide")`
2. Markdown content with LaTeX math notation
3. Code snippets using `display_run_python_snippet()` or direct `st.code()` + `exec()`
4. Interactive components (sliders, inputs) for visualization

## Key Libraries

- **SymPy** - Symbolic mathematics
- **NumPy/SciPy** - Numerical computing
- **Matplotlib** - Visualization
- **NetworkX** - Graph/network analysis

## Conventions

- Draft pages end with underscore (e.g., `page_name_.py`) and are gitignored
- Use `st.latex()` for math notation with SymPy's `latex()` function
- Wide layout is standard: `st.set_page_config(layout="wide")`
- Column-based layouts for side-by-side content
