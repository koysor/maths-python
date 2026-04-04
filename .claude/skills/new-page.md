# New Maths Page Skill

Create a new educational Streamlit page for the maths-python app.

## Your task

The user has described a topic for a new page: **$ARGUMENTS**

If no topic was given, ask the user what mathematical topic they want to add.

## Before writing anything

1. **Determine the file number prefix** — scan `app/pages/` to find the right numeric slot:
   - 100s: Calculus / Differentiation
   - 200s: Integration
   - 300s: Stochastic calculus
   - 700s: Linear algebra
   - 800s: Probability & statistics
   - 850s–860s: Algebra
   - 999s: Reference pages
   - Pick the next free number in the correct cluster.

2. **Read 1–2 closely related existing pages** to understand the exact patterns in use for that topic cluster before writing a single line.

## Page structure to follow

Every page must follow this structure in order:

```python
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
# ... other imports as needed
from sys import path as sys_path
sys_path.append("app")
from utils import display_run_python_snippet

st.set_page_config(page_title="<Topic>", layout="wide")
st.header("<Topic Title>")

st.write("One or two sentences introducing the concept.  Two spaces after full stops.")
```

### Section 1 — Formula / Definition  (`st.columns(2)`)

Left column — for each key formula:
```python
latex_str = r"... latex ..."
st.code(latex_str, language="latex")   # always show source
st.latex(latex_str)                    # then render
```

Right column — `st.info()` with bullet-point properties and key rules.

### Section 2 — Interactive Visualisation  (`st.divider()` first)

- Use `st.slider()` or `st.number_input()` for controls placed **above** the figure
- Generate data with NumPy; use `np.random.seed(42)` for reproducibility
- Create figures with `fig, ax = plt.subplots(figsize=(8, 4))` — keep width ≤ 8 to avoid horizontal scrolling
- Display with `st.pyplot(fig)` — no explicit `plt.close()` needed
- Show 3–4 computed metrics below the figure using `st.columns` + `st.metric()`

### Section 3 — Code Snippet  (`st.divider()` first)

Use `display_run_python_snippet(snippet)` for standalone, self-contained code that:
- Demonstrates the step-by-step calculation from the formula
- Imports everything it needs (including `import streamlit as st`)
- Finishes with `st.write()` calls showing labelled results

For side-by-side layouts (code left, chart right), use the string + `st.code` + `exec` pattern:
```python
chart_code = """
import matplotlib.pyplot as plt
...
st.pyplot(fig)
"""
col_left, col_right = st.columns(2)
with col_left:
    st.code(chart_code, language="python")
with col_right:
    exec(chart_code)
```

## Conventions — follow all of these exactly

| Rule | Detail |
|------|--------|
| Language | British English: "visualisation", "normalised", "colour", "centre" |
| Full stops in prose | Two spaces after every full stop inside `st.write`, `st.info`, `st.markdown` strings |
| LaTeX display | Always pair `st.code(x, language="latex")` with `st.latex(x)` — never one without the other |
| Layout | `layout="wide"` always; columns max 2 wide; never cause horizontal scrolling |
| Figure size | `figsize=(8, 4)` or smaller — no wider than 10 |
| Heatmaps — non-negative | `cmap="Blues"`, `vmin=0`, `vmax=abs_max*2` |
| Heatmaps — with negatives | `cmap="RdBu_r"`, symmetric `vmin=-abs_max`, `vmax=abs_max` |
| Draft pages | Suffix `_` before `.py` (e.g. `300_stochastic_.py`) to hide from sidebar |
| Captions | `st.caption()` for small explanatory notes (e.g. Bessel's correction) |

## After writing

Run `black . && ruff check .` from the repo root and fix any issues before finishing.

Confirm the page number, filename, and a one-line summary of what each section covers.
