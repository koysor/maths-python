# Marimo notebooks

The browser-ready notebooks are published on [GitHub Pages](https://koysor.github.io/maths-python/).  They run in WebAssembly, so you can view and execute them without setting up a local environment.

Each notebook is published in two versions from the same source file.  **View** is a read-only page showing only the outputs and interactive widgets.  **Edit code** shows the Python code and lets you change and re-run it in the browser; changes are kept only in your browser.

| Notebook | View (read-only) | Code (editable) |
|----------|------------------|-----------------|
| Euler's Number | [View](https://koysor.github.io/maths-python/eulers_number.html) | [Edit code](https://koysor.github.io/maths-python/eulers_number-edit.html) |
| The Normal Distribution | [View](https://koysor.github.io/maths-python/normal_distribution.html) | [Edit code](https://koysor.github.io/maths-python/normal_distribution-edit.html) |

Every `.py` file directly in this folder is published by `.github/workflows/deploy-marimo.yml`.  The notebooks run in Pyodide, so they can use numpy, matplotlib and other Pyodide packages, but cannot import `maths_lib`.  To run one locally:

```bash
uv run marimo edit notebooks/eulers_number.py
```
