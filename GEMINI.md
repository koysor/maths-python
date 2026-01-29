# Project Overview

This is an educational interactive web application that provides Python code snippets for mathematics and statistics. The application covers topics including calculus (differentiation and integration), stochastic calculus, linear algebra, and probability distributions. Each topic presents mathematical theory alongside executable Python code examples using libraries like SymPy, NumPy, SciPy, and Matplotlib.

Built with Streamlit, the application organises content into navigable pages where users can explore mathematical concepts through LaTeX-rendered equations and interactive visualizations. Users can adjust parameters with sliders and inputs to see how mathematical operations behave with different values, making it a useful reference for learning computational mathematics.

The codebase follows a modular architecture where each Python file in the `app/pages/` directory automatically becomes a page in the application. This makes it straightforward to add new mathematical topics by creating new page files following the established patterns.

# Building and Running

To run the application, execute the following command:

```bash
./launch_streamlit_app.sh
```

This will start the Streamlit server and open the application in your web browser.

# Development Conventions

The project uses `ruff` for linting and `black` for formatting. The configuration for these tools can be found in the `pyproject.toml` file.

New pages can be added to the application by creating a new Python file in the `app/pages` directory. The file name will be used as the page title. The file should contain Streamlit code to generate the page content.

All spellings within the project should adhere to British English conventions.
