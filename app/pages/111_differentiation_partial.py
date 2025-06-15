import streamlit as st

st.set_page_config(layout="wide")
st.markdown("### Partial Differentiation")


col1, col2 = st.columns([4, 3])

with col1:
    st.write(
        "**Partial Differentiation** is a technique used in calculus to take the derivative of a multivariable function with respect to one variable while treating the other variables as constants."
    )

    st.write("Example:")

    latex_code = r"""
    f(x, y) = x^2 + 3xy^2
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

    st.write("Partial derivative with respect to $$x$$:")
    st.write("- Treat $$y$$ as a constant and differentiate with respect to $$x$$.")
    latex_code = r"""
    \frac{\partial f}{\partial x} = 2x + 3y^2
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)
    st.write("Partial derivative with respect to $$y$$:")
    st.write("- Treat $$x$$ as a constant and differentiate with respect to $$y$$.")
    latex_code = r"""
    \frac{\partial f}{\partial y} = 6xy
    """
    st.code(latex_code, language="latex")
    st.latex(latex_code)

with col2:
    st.video("https://www.youtube.com/watch?v=AXqhWeUEtQU")


st.markdown("### Using SymPy")

with open("app/pages/code_snippets/differentiation_partial.py", "r") as f:
    code_snippet = f.read()

st.code(code_snippet, language="python")
exec(code_snippet)
