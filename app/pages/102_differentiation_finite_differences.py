import streamlit as st


st.set_page_config(layout="wide")
st.markdown("### Differentiation Finite Differences")

st.markdown("#### Differentiation Example Using the Finite Differences Method")

st.write(
    """You can implement differentiation using the finite differences method.
    Differentiation using finite differences is a **numerical method** to approximate the derivative of a function at a particular point based on discrete data points.
    The difference between the discrete data points should be **small** to get a good approximation of the tangent line at a particular point."""
)


with open("app/pages/code_snippets/differentiation_finite_differences.py", "r") as f:
    code_snippet = f.read()

st.code(code_snippet)
exec(code_snippet)

st.write(
    r"""This is consistent with the First Derivative of $$x^2 + 3x + 5$$ which is $$2x + 3$$ . 
        As $$2*(1) + 3 = 5$$."""
)
