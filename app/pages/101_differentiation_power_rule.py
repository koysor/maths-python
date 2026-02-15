import streamlit as st

st.set_page_config(
    page_title="Differentiation Power Rule", page_icon="📐", layout="wide"
)
st.header("Differentiation Power Rule")


st.markdown("#### The Power Rule")


st.write(
    """The Power Rule is a basic rule of differentiation that allows you to differentiate polynomial functions.
    It states that if you have a function of the form:"""
)

latex_code = r"""
f(x) = x^n
"""
st.latex(latex_code)
st.write(
    """where $$n$$ is a constant, then the derivative of $$f(x)$$ with respect to $$x$$ is given by:"""
)

latex_code = r"""
\frac{d}{dx} (x^n) = n \cdot x^{n-1}
"""
st.latex(latex_code)


col1, col2 = st.columns([4, 3])

with col1:

    st.write("Example of the power rule:")

    n = st.number_input("Enter a value for n:", value=2, step=1)

    with open("app/pages/code_snippets/differentiation_power_rule.py", "r") as f:
        code_snippet = f.read()
    code_snippet = code_snippet.replace("n = 2", f"n = {n}")

    st.code(code_snippet)
    exec(code_snippet)

    st.write(
        "The output from the sympy.diff function is consistent with the workings above but rearranged."
    )

with col2:
    st.write(
        "The SymPy diff() function can be used to compute derivatives symbolically."
    )

    st.code("symypy.diff(expression, variable, n=1)")
    st.write(
        "Where expression is the expression to differentiate, variable is the variable with respect to which to differentiate, and n is the order of the derivative."
    )
    st.write(
        "The default value of n is 1, which means that the first derivative is computed. If n is set to 2, the second derivative is computed."
    )
