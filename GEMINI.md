# Project Overview

This is an educational interactive web application that provides Python code snippets for mathematics and statistics. The application covers topics including calculus (differentiation and integration), stochastic calculus, linear algebra, and probability distributions. Each topic presents mathematical theory alongside executable Python code examples using libraries like SymPy, NumPy, SciPy, and Matplotlib.

Built with Streamlit, the application organises content into navigable pages where users can explore mathematical concepts through LaTeX-rendered equations and interactive visualisations. Users can adjust parameters with sliders and inputs to see how mathematical operations behave with different values, making it a useful reference for learning computational mathematics.

The codebase follows a modular architecture where each Python file in the `app/pages/` directory automatically becomes a page in the application. This makes it straightforward to add new mathematical topics by creating new page files following the established patterns.

# Building and Running

The project uses `uv` for dependency management. To set up the environment and run the application:

1.  **Install dependencies**:
    ```bash
    uv sync
    ```

2.  **Launch the application**:
    ```bash
    ./launch_streamlit_app.sh
    ```
    This script activates the virtual environment and starts the Streamlit server.

# Directory Structure

- `app/`: Main application code.
  - `pages/`: Individual Streamlit pages. Files are numbered to control their order in the sidebar.
  - `pages/code_snippets/`: Standalone Python scripts that are displayed and executed within the pages.
  - `assets/`: Images and other static assets.
- `tests/`: Unit tests for mathematical logic and utilities.
- `notebooks/`: Jupyter notebooks used for research and prototyping.

# Development Conventions

- **Linting & Formatting**: The project uses `ruff` for linting and `black` for formatting. These are enforced via `pre-commit` hooks.
- **British English**: All spellings within the project (prose, variable names, and comments) must adhere to British English conventions (e.g., *visualisation*, *behaviour*, *centre*).
- **Page Layout**: 
  - Use `st.columns` to create side-by-side layouts (e.g., prose on the left, code/plots on the right).
  - Prefer a `[2, 3]` ratio for a wider display area for code or visualisations.
- **Interactive Elements**: Use `st.slider`, `st.selectbox`, and `st.latex` to create interactive and mathematically-rich experiences.
- **Testing**: New mathematical logic should be accompanied by tests in the `tests/` directory. Run tests using `pytest`.

# Configuration

Streamlit configuration is managed in `.streamlit/config.toml`. Ensure that only supported options are used to avoid startup warnings.
