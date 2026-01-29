import os
import pytest
import streamlit as st


def get_snippet_files():
    """Return a list of all Python files in the code_snippets directory."""
    snippet_dir = "app/pages/code_snippets"
    return [
        os.path.join(snippet_dir, f)
        for f in os.listdir(snippet_dir)
        if f.endswith(".py")
    ]


@pytest.mark.parametrize("snippet_file", get_snippet_files())
def test_snippet_execution(snippet_file):
    """Verify each code snippet executes without raising exceptions."""
    with open(snippet_file, "r") as f:
        code = f.read()
        try:
            # We need to handle streamlit specific commands
            # For now, we will just exec and check for errors
            exec(code, {"st": st})
        except Exception as e:
            pytest.fail(f"Snippet {snippet_file} failed with error: {e}")
