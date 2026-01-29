import streamlit as st
import sympy


def display_run_python_snippet(code_snippet: str):
    """
    Display and run a Python code snippet in Streamlit.  Aligns the code to a width of 4/6ths of the screen to the left.
    """

    col1, _ = st.columns([4, 2])

    with col1:
        st.code(code_snippet, language="python")
        exec(code_snippet)


def to_latex(expression):
    """
    Converts a SymPy expression to a LaTeX string.
    """
    return sympy.latex(expression)
