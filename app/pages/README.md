# Pages

Each Python `.py` file in this folder automatically becomes a page in the Streamlit web application.

## Ordering

The integer prefixes in the `.py` file names are used to control the ordering in the Streamlit sidebar. These prefixes are automatically hidden in the application's UI.

### Topic Clusters

- **100s**: Calculus & Differentiation
- **200s**: Integration techniques
- **300s**: Stochastic calculus
- **700s**: Linear algebra
- **800s**: Probability & Statistics
- **850s–860s**: Algebra (logarithms, completing the square)
- **999s**: Reference and utility pages

## Conventions

- Use `st.set_page_config(layout="wide")` as the standard layout.
- Use British English spellings for all prose and labels.
- Follow established patterns for displaying and executing code snippets (see `CLAUDE.md` for details).
- Use `st.latex()` for mathematical notation, leveraging SymPy's `latex()` function for dynamic output.
