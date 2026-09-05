---
name: marimo-solution
description: >
  Generate a complete Marimo notebook model solution for a mathematics problem,
  pitched at A Level students (UK, age 17-18). Includes step-by-step working,
  LaTeX source and rendered output, notation guides, visualisations, and a
  Plain English summary.
argument-hint: <mathematics problem or question>
allowed-tools: Write, Read, Bash
---

Generate a complete, runnable Marimo Python notebook (.py) that provides a model solution to the following mathematics problem:

Input: `$@`

If no problem is provided, ask the user for one before proceeding.

---

## Output File

Save the notebook as `solution.py` in the current directory (or a name derived from the topic if more appropriate). The notebook must run without errors using `marimo run solution.py` or `marimo edit solution.py`.

---

## Notebook Structure

Build the notebook cell by cell in the following order. Each logical section is its own cell. Use `mo.md()`, `mo.callout()`, `mo.accordion()`, `mo.hstack()`, `mo.vstack()`, and reactive cells throughout.

### Cell 1 — Imports

```python
import marimo as mo
import sympy as sp
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
```

### Cell 2 — Header

- Title: the topic name (e.g. "Integration by Parts — Model Solution")
- Difficulty badge: one of GCSE / AS Level / A Level / Further Maths
- A bullet list of prerequisite knowledge the student should already know before attempting this problem

### Cell 3 — The Question

- Display the original question verbatim inside a `mo.callout(kind="info")` box
- Show any given information, constraints, or diagrams clearly
- Show the raw LaTeX string in a Python variable and in a `mo.md()` code fence, then render it:

```python
latex_question = r"..."
mo.vstack([
    mo.md(f"```latex\n{latex_question}\n```"),
    mo.md(f"$${latex_question}$$"),
])
```

This pattern (show source, then render) is repeated for every formula throughout the notebook.

### Cell 4 — Key Notation & Concepts

Before any algebra, define every symbol, operator, and term that appears in the problem.

Use a table:

| Notation | Meaning |
|----------|---------|
| `\int`   | The integral — the area under a curve |
| ...      | ...     |

Show the LaTeX source for each symbol alongside its plain-English meaning.

### Cell 5 — Strategy Overview

- A short plain-English paragraph (3–5 sentences) explaining the overall approach **before** any algebra begins
- "Why this method?" — explain why this technique is chosen over alternatives, in plain English
- A numbered checklist of the major steps about to be performed

### Cells 6+ — Step-by-Step Solution

For **each** step, create a separate cell containing:

1. **Heading**: e.g. "Step 2 — Expand the brackets"
2. **What we're doing**: one sentence in plain English before any maths
3. **Working**: show the LaTeX source string, then render the formula using the show-source-then-render pattern above
4. **Why it works**: name the rule or theorem being applied (e.g. "Chain Rule", "completing the square") and give a one-line statement of what it says
5. **Common mistake**: a `mo.callout(kind="warn")` flagging the error students most often make at this step

Never skip algebraic steps — show every line of working. Use `\begin{align*} ... &= ... \end{align*}` to align multi-line working, and annotate each line with `\quad \text{(reason)}`.

### Cell — The Answer

- Boxed final answer inside a `mo.callout(kind="success")`
- State the answer in words as well as symbols
- Include units if applicable
- Show a verification check (substitute back, differentiate to verify, estimate order of magnitude, etc.)

### Cell — Alternative Method (if one exists)

Wrap a second approach inside `mo.accordion({"Alternative Method": ...})` so it does not clutter the main flow. Note when each method is preferable.

### Cell — Visualisation

Where the problem is geometric or involves functions, include a Matplotlib plot:

- For functions: plot the curve with roots, turning points, and any shaded area labelled
- For geometry: a labelled diagram
- For probability: a tree diagram or distribution curve

Show the plot code in a visible cell so the student can read and modify it. Return the figure using `mo.pyplot(fig)`.

### Cell — Exam Technique Tips

A `mo.callout(kind="neutral")` containing:

- The difference between "show that" and "find" in terms of required working
- Mark-scheme language relevant to this type of question
- How many marks to expect and where they are awarded
- Any memory aids or mnemonics (e.g. ILATE for integration by parts)

### Cell — Practice Problems

Three similar problems in increasing difficulty, wrapped in:

```python
mo.accordion({
    "Practice Problem 1 (similar difficulty)": mo.vstack([...]),
    "Practice Problem 2 (slightly harder)": mo.vstack([...]),
    "Practice Problem 3 (exam stretch)": mo.vstack([...]),
})
```

Each problem has a nested accordion for hints and another for the final answer (not the full solution).

### Cell — Glossary

An alphabetical `mo.accordion()` where each entry is a technical term used in the solution, defined in plain English without assuming prior knowledge of the term.

### Cell — Plain English Summary

The final cell in the notebook. This is the most important cell for a learner who is lost or anxious.

Write 3–6 short paragraphs (no LaTeX, no symbols) that explain:

1. **What kind of problem this was** — describe it as a story or real-world analogy where possible
2. **The core idea behind the method** — what mathematical insight makes the solution work, in everyday language
3. **The key steps in plain words** — a narrative walkthrough of what was done and why, without any algebra
4. **What could go wrong** — the most common errors and misconceptions, described plainly
5. **How to know you've got it right** — intuition checks a student can apply without a mark scheme
6. **Where this topic fits in A Level maths** — briefly connect it to other topics the student will encounter

Use `mo.callout(kind="success")` to wrap this summary so it stands out visually as a friendly, reassuring closing note.

---

## Style & Language Rules

- Write at the level of a confident 18-year-old, not a university student
- Use British English spellings throughout (colour, centre, organised, behaviour, etc.)
- Never use jargon without immediately defining it in plain English
- Prefer "multiply both sides by..." over "apply the multiplicative inverse"
- When invoking a theorem or rule, always state its name and give a one-line plain-English statement of what it says
- Use analogies to reinforce abstract ideas (integration as "area under a curve", logarithms as "the power you raise the base to")
- Avoid phrases like "trivially", "obviously", "clearly" — nothing is obvious to a learner

## LaTeX Conventions

- Always show the raw LaTeX string in a Python variable, display it in a code fence, then render it — never render without showing the source
- Use `\displaystyle` for inline fractions so they are readable at screen size
- Align multi-line working with `\begin{align*}` and annotate each line with `\quad \text{(reason)}`
- Use `\boxed{}` for the final answer

## Marimo Conventions

- Every cell that produces output must return or display its value
- Use `mo.md(f"...")` with f-strings for dynamic content
- The notebook must run top-to-bottom without errors
- Do not use `st.` — this is a Marimo notebook, not a Streamlit app
