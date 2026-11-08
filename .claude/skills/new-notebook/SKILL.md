---
name: new-notebook
description: Create an educational marimo notebook in notebooks/ that is published to GitHub Pages and runs in the browser
disable-model-invocation: true
argument-hint: [notebook-name] [topic]
---

Create an educational marimo notebook following the maths-python project conventions.

**Notebook name:** $0 (snake_case filename without .py extension, e.g. `taylor_series`)
**Topic:** $ARGUMENTS

Create the file at `notebooks/$0.py`. Read `notebooks/eulers_number.py` first as the reference example.

## Marimo rules

The full rules are in the shared `koysor-skills:marimo-helper` skill (from `repo-tools`). The essentials:

- Every global name may be defined in only one cell. Prefix loop variables and temporaries with `_` (e.g. `for _n in range(10):`) and avoid generic globals like `df`, `fig`, `ax` or `x` when more than one cell would want them; use descriptive names such as `fig_convergence`.
- Pass dependencies through the cell function's arguments and return what later cells need; no hidden state or side effects.

## Browser constraints

Every `.py` file directly in `notebooks/` is exported to WebAssembly by `.github/workflows/deploy-marimo.yml` and runs in Pyodide, so:

1. **Imports** — only packages in Pyodide's distribution that are also project dependencies: `marimo`, `numpy`, `pandas`, `matplotlib`, `scipy` and `sympy`. Never import `maths_lib` or `streamlit`. There is no test enforcing this, so check the imports yourself.
2. **No network, files or databases** — generate data with `numpy` (seed it, e.g. `rng = np.random.default_rng(42)`) or define small datasets inline.
3. **Light computation** — keep loops and simulations small enough to render in a browser in a few seconds.

## Notebook structure

1. **Header** — `import marimo`, `__generated_with` set to the installed marimo version (`uv run marimo --version`), and `app = marimo.App(width="full")`.
2. **Imports cell** — one cell at the top importing `marimo as mo` and the packages needed, returning them.
3. **Title and introduction** — `mo.md(r"""# Title ...""")` explaining the concept and what the reader will see.
4. **Definition / formula** — LaTeX in `mo.md` with raw strings (`$...$` inline, `$$...$$` display). Define every symbol and list the key properties.
5. **Step-by-step calculation** — code that works through the formula, with `mo.show_code()` in cells whose code is part of the lesson so it also shows in the read-only view.
6. **Interactive example** — `mo.ui.slider` / `mo.ui.number` / `mo.ui.dropdown` widgets for the key parameters, grouped with `mo.hstack` / `mo.vstack` where it helps, with sensible ranges. Plots and results read `widget.value` so they update reactively.
7. **Visualisation** — create and display each matplotlib figure in a single cell with `figsize=(8, 4)` or smaller, ending the cell with the figure. Label axes and titles. For heatmaps, use `cmap="Blues"` with `vmin=0` for non-negative data and `cmap="RdBu_r"` with symmetric limits when there are negatives.
8. **Interpretation** — `mo.md(...).callout(kind="info")` for key insights, and a short summary of what the reader should take away.
9. **Footer** — `if __name__ == "__main__": app.run()`.

Use **British English spelling** throughout (e.g. visualisation, normalised, colour, centre), and two spaces after every full stop in prose.

## Publishing

The deploy workflow picks up the notebook automatically, publishing `$0.html` (view) and `$0-edit.html` (edit code). Add a row to the notebooks table in both `README.md` ("Interactive Marimo Notebooks") and `notebooks/README.md`, keeping the tables alphabetical:

`| Title | [View](https://koysor.github.io/maths-python/$0.html) | [Edit code](https://koysor.github.io/maths-python/$0-edit.html) |`

## Verification

Run each of these from the repo root and fix any failures before finishing:

```bash
uv run marimo check notebooks/$0.py
MPLBACKEND=Agg uv run python notebooks/$0.py   # must exit 0
uv run black notebooks/$0.py
uv run ruff check notebooks/$0.py
```

Optionally open it with `uv run marimo edit notebooks/$0.py` to check the widgets and plots look right.
